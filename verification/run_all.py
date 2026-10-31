#!/usr/bin/env python3
"""Reproduce the exact finite checks using only the Python standard library.

Default execution recomputes the checks and compares their deterministic summary
with results.json. Use --write-results to regenerate that file intentionally.
The direct RSK checks count standard tableaux recursively, without hook lengths.
"""

import argparse
from bisect import bisect_right
from collections import Counter, defaultdict
from fractions import Fraction
from functools import lru_cache
from itertools import product
import json
from math import comb, factorial
from pathlib import Path


def require(condition, context):
    """Keep checks active even when Python is invoked with -O."""
    if not condition:
        raise AssertionError(context)


@lru_cache(maxsize=None)
def partitions(n, max_part=None):
    if n == 0:
        return ((),)
    if max_part is None:
        max_part = n
    return tuple(
        (first,) + tail
        for first in range(min(n, max_part), 0, -1)
        for tail in partitions(n - first, first)
    )


@lru_cache(maxsize=None)
def specht_dimension(shape):
    hook_product = 1
    for row_index, row_length in enumerate(shape):
        for column in range(row_length):
            below = sum(length > column for length in shape[row_index + 1 :])
            hook_product *= row_length - column + below
    return factorial(sum(shape)) // hook_product


def horizontal_strip(lam, nu):
    """Check lambda_i >= nu_i >= lambda_(i+1), including trailing rows."""
    length = max(len(lam), len(nu))
    lam_padded = lam + (0,) * (length - len(lam) + 1)
    nu_padded = nu + (0,) * (length - len(nu))
    return all(
        lam_padded[i] >= nu_padded[i] >= lam_padded[i + 1]
        for i in range(length)
    )


def branch_fidelity(lam, nu, d):
    """The inherited one-output CG formula, evaluated exactly."""
    lam_padded = lam + (0,) * (d - len(lam))
    nu_padded = nu + (0,) * (d - 1 - len(nu))
    fidelity = Fraction(1)
    for j in range(d - 1):
        fidelity *= Fraction(
            lam_padded[0] - nu_padded[j] + j,
            lam_padded[0] - lam_padded[j + 1] + j,
        )
    return fidelity


def binomial_or_zero(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def binary_risk(n, k):
    g = n - 2 * k
    return sum(
        (
            Fraction(
                binomial_or_zero(n, k - r) - binomial_or_zero(n, k - r - 1),
                comb(n, k),
            )
            * Fraction(r, g + 2 * r)
            for r in range(k + 1)
        ),
        Fraction(0),
    )


def exact_sector_checks(max_n=18, max_d=8):
    cases = 0
    branches = 0
    strict_cases = 0
    binary_cases = 0
    examples = []

    for n in range(1, max_n + 1):
        previous_risk = None
        for k in range((n - 1) // 2 + 1):
            m = n - k
            g = m - k
            target = binary_risk(n, k)
            lower = Fraction(k, (m + 1) * (g + 2))
            upper = min(
                Fraction(k, (g + 1) * (g + 2)),
                Fraction(k, g * g + n),
            )
            require(lower <= target <= upper, ("risk bounds", n, k, target))
            if previous_risk is not None:
                require(previous_risk <= target, ("monotonicity", n, k))
            if k == 1:
                require(target == Fraction(1, n * n), ("one fault", n))
            previous_risk = target
            binary_cases += 1

            for d in range(2, min(n + 1, max_d) + 1):
                for nu in partitions(k):
                    if len(nu) > d - 1:
                        continue
                    normalization = Fraction(0)
                    risk = Fraction(0)
                    tails = [Fraction(0) for _ in range(k + 1)]

                    for lam in partitions(n):
                        if len(lam) > d or not horizontal_strip(lam, nu):
                            continue
                        probability = Fraction(
                            specht_dimension(lam),
                            comb(n, m) * specht_dimension(nu),
                        )
                        normalization += probability
                        fidelity = branch_fidelity(lam, nu, d)
                        r = lam[0] - m
                        context = (n, k, d, nu, lam)
                        require(0 <= r <= k, ("first-row excess", context, r))
                        require(0 <= fidelity <= 1, ("fidelity", context, fidelity))
                        require(
                            1 - fidelity <= Fraction(r, g + 2 * r),
                            ("branch bound", context, fidelity),
                        )
                        risk += probability * (1 - fidelity)
                        for threshold in range(r + 1):
                            tails[threshold] += probability
                        branches += 1

                    context = (n, k, d, nu)
                    require(normalization == 1, ("normalization", context))
                    require(risk <= target, ("binary domination", context, risk))
                    for threshold, tail in enumerate(tails):
                        require(
                            tail <= Fraction(comb(n, k - threshold), comb(n, k)),
                            ("tail domination", context, threshold, tail),
                        )
                    if nu == () or nu == (k,):
                        require(risk == target, ("binary equality", context, risk))
                    elif risk < target:
                        strict_cases += 1

                    if n == 9 and k == 3 and d == 4:
                        examples.append(
                            {
                                "N": n,
                                "k": k,
                                "d": d,
                                "nu": list(nu),
                                "risk": str(risk),
                                "binary_risk": str(target),
                            }
                        )
                    cases += 1

    return {
        "N_max": max_n,
        "d_range": "2 through min(N+1, 8)",
        "bad_irrep_cases": cases,
        "branches": branches,
        "binary_count_cases": binary_cases,
        "strictly_better_than_binary": strict_cases,
        "examples": examples,
        "status": "passed",
    }


def rsk(word):
    """Ordinary row insertion: weak rows and strict columns.

    Returns both the semistandard insertion tableau P and the standard
    recording tableau Q. Only the newly created cell receives a Q label.
    """
    insertion = []
    recording = []
    for time, letter in enumerate(word, start=1):
        row_index = 0
        while True:
            if row_index == len(insertion):
                insertion.append([letter])
                recording.append([time])
                break
            row = insertion[row_index]
            column = bisect_right(row, letter)
            if column == len(row):
                row.append(letter)
                recording[row_index].append(time)
                break
            row[column], letter = letter, row[column]
            row_index += 1
    return (
        tuple(tuple(row) for row in insertion),
        tuple(tuple(row) for row in recording),
    )


@lru_cache(maxsize=None)
def standard_tableaux(shape):
    """Enumerate SYTs by deleting the cell containing the largest label.

    This uses removable corners and never uses the hook-length formula.
    """
    if not shape:
        return frozenset({()})
    label = sum(shape)
    tableaux = set()
    for row_index, length in enumerate(shape):
        next_length = shape[row_index + 1] if row_index + 1 < len(shape) else 0
        if length <= next_length:
            continue
        smaller = list(shape)
        smaller[row_index] -= 1
        if smaller[row_index] == 0:
            smaller.pop(row_index)
        for tableau in standard_tableaux(tuple(smaller)):
            rows = [list(row) for row in tableau]
            if row_index == len(rows):
                rows.append([label])
            else:
                rows[row_index].append(label)
            tableaux.add(tuple(tuple(row) for row in rows))
    return frozenset(tableaux)


RSK_CASES = (
    ("no_faults", (), 3, 1),
    ("binary_row", ((1, 1, 1),), 4, 1),
    ("hook_repeated_letters", ((1, 1), (2,)), 4, 2),
    ("hook_distinct_letters", ((1, 2), (3,)), 4, 3),
    ("column", ((1,), (2,), (3,)), 4, 3),
    ("rectangle", ((1, 1), (2, 2)), 5, 2),
    ("four_box_hook", ((1, 1, 2), (2,)), 5, 2),
    ("three_rows", ((1, 2), (2,), (3,)), 5, 3),
)


def direct_rsk_case(name, fixed_p, m, bad_alphabet_size):
    nu = tuple(len(row) for row in fixed_p)
    k = sum(nu)
    n = m + k
    d = bad_alphabet_size + 1
    require(m > k, ("strict majority in RSK case", name))

    # First enumerate all bad words with this exact insertion tableau.
    bad_words = []
    bad_recordings = set()
    for word in product(range(1, d), repeat=k):
        insertion, recording = rsk(word)
        if insertion == fixed_p:
            bad_words.append(word)
            require(recording not in bad_recordings, ("bad-word injectivity", name))
            bad_recordings.add(recording)
    require(
        bad_recordings == standard_tableaux(nu),
        ("all bad recording tableaux", name),
    )

    recordings_by_shape = defaultdict(set)
    counts_by_shape = Counter()
    pattern_maxima = {}
    accepted = 0

    # This is a direct word enumeration, not sampling from the claimed Pieri law.
    for word in product(range(1, d + 1), repeat=n):
        if word.count(d) != m:
            continue
        stripped_word = tuple(letter for letter in word if letter < d)
        stripped_insertion, _ = rsk(stripped_word)
        if stripped_insertion != fixed_p:
            continue

        insertion, recording = rsk(word)
        restricted_insertion = tuple(
            tuple(letter for letter in row if letter < d)
            for row in insertion
            if any(letter < d for letter in row)
        )
        require(
            restricted_insertion == fixed_p,
            ("restriction of insertion tableau", name, word),
        )
        lam = tuple(len(row) for row in insertion)
        require(horizontal_strip(lam, nu), ("horizontal strip", name, word))
        require(
            recording not in recordings_by_shape[lam],
            ("full-word injectivity", name, word),
        )
        recordings_by_shape[lam].add(recording)
        counts_by_shape[lam] += 1
        accepted += 1

        pattern = tuple(letter == d for letter in word)
        position = 0
        maximum = 0
        for is_good in pattern:
            position += -1 if is_good else 1
            maximum = max(maximum, position)
        r = lam[0] - m
        require(0 <= r <= maximum, ("pointwise bridge domination", name, word))
        if bad_alphabet_size == 1:
            require(r == maximum, ("binary LIS equality", name, word))
        pattern_maxima[pattern] = maximum

    allowed_shapes = {
        lam for lam in partitions(n) if horizontal_strip(lam, nu)
    }
    require(
        set(counts_by_shape) == allowed_shapes,
        ("all and only Pieri shapes", name),
    )
    denominator = comb(n, m) * len(standard_tableaux(nu))
    require(accepted == denominator, ("word denominator", name, accepted))
    require(len(pattern_maxima) == comb(n, m), ("all binary patterns", name))

    shapes = []
    for lam in sorted(allowed_shapes, reverse=True):
        expected_recordings = standard_tableaux(lam)
        require(
            recordings_by_shape[lam] == expected_recordings,
            ("all recording tableaux for full shape", name, lam),
        )
        observed = Fraction(counts_by_shape[lam], accepted)
        predicted = Fraction(len(expected_recordings), denominator)
        require(observed == predicted, ("conditional Pieri probability", name, lam))
        shapes.append(
            {
                "lambda": list(lam),
                "word_count": counts_by_shape[lam],
                "probability": str(observed),
            }
        )

    maximum_counts = Counter(pattern_maxima.values())
    for threshold in range(k + 1):
        observed_tail_count = sum(
            count for maximum, count in maximum_counts.items() if maximum >= threshold
        )
        require(
            observed_tail_count == comb(n, k - threshold),
            ("reflection count", name, threshold),
        )

    return {
        "name": name,
        "N": n,
        "m": m,
        "k": k,
        "d": d,
        "nu": list(nu),
        "fixed_bad_insertion_tableau": [list(row) for row in fixed_p],
        "full_words_enumerated": d**n,
        "bad_words_with_fixed_tableau": len(bad_words),
        "accepted_full_words": accepted,
        "shapes": shapes,
        "bridge_maximum_counts": [
            {"maximum": maximum, "count": maximum_counts[maximum]}
            for maximum in range(k + 1)
        ],
        "status": "passed",
    }


def direct_rsk_checks():
    cases = [direct_rsk_case(*case) for case in RSK_CASES]
    return {
        "case_count": len(cases),
        "full_words_enumerated": sum(case["full_words_enumerated"] for case in cases),
        "accepted_full_words": sum(case["accepted_full_words"] for case in cases),
        "dimension_count_method": "explicit standard-tableau corner recursion",
        "cases": cases,
        "status": "passed",
    }


def run_all():
    return {
        "schema_version": 1,
        "arithmetic": "exact integers and fractions; no floating point",
        "exact_sector_checks": exact_sector_checks(),
        "direct_rsk_checks": direct_rsk_checks(),
        "status": "all checks passed",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--write-results",
        action="store_true",
        help="replace results.json with the deterministic summary from this run",
    )
    args = parser.parse_args()
    results = run_all()
    results_path = Path(__file__).resolve().with_name("results.json")
    if args.write_results:
        results_path.write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")
    else:
        expected = json.loads(results_path.read_text(encoding="utf-8"))
        require(results == expected, "Recomputed results differ from results.json")

    sectors = results["exact_sector_checks"]
    words = results["direct_rsk_checks"]
    print(
        "Exact sector checks:",
        sectors["bad_irrep_cases"],
        "cases and",
        sectors["branches"],
        "branches.",
    )
    print(
        "Direct RSK checks:",
        words["case_count"],
        "cases,",
        words["full_words_enumerated"],
        "words enumerated, and",
        words["accepted_full_words"],
        "accepted words.",
    )
    print("Results written." if args.write_results else "Committed results match.")


if __name__ == "__main__":
    main()
