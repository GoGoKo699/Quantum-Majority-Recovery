# Reproducible finite verification

Run the checks from the repository root:

```sh
python3 verification/run_all.py
```

The script uses only the Python standard library. It recomputes every check and compares the deterministic summary with [results.json](results.json). It uses exact integers and `fractions.Fraction`; no floating-point tolerance or random seed is involved. Assertions remain active even if Python is invoked with `-O`.

To replace the recorded summary after an intentional change to the verification scope, run:

```sh
python3 verification/run_all.py --write-results
```

The recorded run reports:

```text
Exact sector checks: 1929 cases and 10142 branches.
Direct RSK checks: 8 cases, 336601 words enumerated, and 1219 accepted words.
Committed results match.
```

## Exact rational sector calculations

The first suite covers every $`1\le N\le18`$, every strict-majority fault count $`0\le k<N/2`$, every $`2\le d\le\min(N+1,8)`$, and every bad partition $`\nu\vdash k`$ with at most $`d-1`$ rows. For each case it enumerates all $`\lambda\vdash N`$ with at most $`d`$ rows such that $`\lambda/\nu`$ is a horizontal strip. Trailing zero rows are included in the interlacing test.

Specht dimensions in this suite are computed with the hook-length formula. The suite evaluates the conditional law

```math
p(\lambda\mid\nu)
=\frac{f^\lambda}{\binom Nm f^\nu}
```

and the inherited one-output CG fidelity formula

```math
a_{\lambda,\nu}
=\prod_{j=1}^{d-1}
\frac{\lambda_1-\nu_j+j-1}
     {\lambda_1-\lambda_{j+1}+j-1}.
```

The formula is attributed to the purity-amplification literature in [RELATED_WORK.md](../references/RELATED_WORK.md#LTHC2026), with the pointwise combinatorial expression also given by [Scharnhorst et al.](../references/RELATED_WORK.md#SSW2026). Its application to a complete bad branching block is justified in the [sector reduction](../science/sector-reduction.md).

The checks establish the following finite identities and inequalities in exact arithmetic:

- The conditional probabilities sum to one.
- Every evaluated branch fidelity lies between zero and one.
- With $`r=\lambda_1-m`$ and $`g=m-k`$, the branch infidelity is at most $`r/(g+2r)`$.
- Every tail of $`\lambda_1-m`$ is bounded by the corresponding binary bridge tail.
- The averaged branch infidelity is at most the exact binary minimax risk.
- The symmetric bad partition $`\nu=(k)`$, including the empty case, attains equality.
- For all 90 permitted pairs $`N,k`$ in the range, the exact binary risk obeys the stated nonasymptotic bounds and is nondecreasing in $`k`$. The one-fault identity $`\varepsilon_{N,1}=1/N^2`$ is checked whenever applicable.

There are 1,929 bad-partition cases and 10,142 branches in this scope. In 1,333 cases the averaged infidelity is strictly smaller than the binary value. Selected exact values at $`N=9,k=3,d=4`$ are recorded in the JSON output.

This suite evaluates the cited CG expression. It does not construct a Clebsch–Gordan transform as a matrix, independently derive its coefficients, or simulate the recovery circuit. Agreement between expressions that use that formula is not an independent verification of the formula itself.

## Direct RSK and recording-tableau enumeration

The second suite checks the combinatorial step that turns the induced shape law into a binary bridge comparison. It enumerates actual words and applies row insertion. It does not generate shapes from the proposed probabilities.

For each selected semistandard insertion tableau $`P`$ of bad shape $`\nu`$, the suite enumerates every word over $`\{1,\ldots,d\}`$. It retains precisely the words with $`m`$ occurrences of the largest letter $`d`$ for which deleting all occurrences of $`d`$ leaves a word with insertion tableau $`P`$.

Independently, standard tableaux are enumerated recursively: the largest label must occupy a removable corner, so delete that corner and recurse. This second method does not call the hook-length formula. The checks compare sets of recording tableaux, rather than only their cardinalities.

For each retained word, and then for each observed shape, the suite verifies:

- Restricting the full insertion tableau to letters below $`d`$ gives exactly the fixed tableau $`P`$.
- The full shape is a horizontal-strip extension of $`\nu`$.
- Every standard recording tableau of each allowed full shape appears exactly once, and no other full shapes appear.
- The total number of retained words is $`\binom Nm f^\nu`$, where $`f^\nu`$ is obtained by explicit tableau enumeration.
- The empirical conditional shape probabilities equal $`f^\lambda/[\binom Nm f^\nu]`$, with both dimensions obtained by tableau enumeration.
- For each individual word, $`0\le\lambda_1-m\le M`$, where $`M`$ is computed directly from its good/bad prefix counts. Equality is checked for the binary alphabet.
- Every binary placement pattern occurs. Direct counting of these patterns verifies the reflection-principle tail $`\Pr(M\ge r)=\binom N{k-r}/\binom Nk`$.

The selected cases are:

| Case | $`N`$ | $`k`$ | $`d`$ | Bad shape $`\nu`$ | Retained full words |
|---|---:|---:|---:|---|---:|
| No faults | 3 | 0 | 2 | Empty | 1 |
| Binary row | 7 | 3 | 2 | $`(3)`$ | 35 |
| Hook with repeated letters | 7 | 3 | 3 | $`(2,1)`$ | 70 |
| Hook with distinct letters | 7 | 3 | 4 | $`(2,1)`$ | 70 |
| Column | 7 | 3 | 4 | $`(1,1,1)`$ | 35 |
| Rectangle | 9 | 4 | 3 | $`(2,2)`$ | 252 |
| Four-box hook | 9 | 4 | 3 | $`(3,1)`$ | 378 |
| Three rows | 9 | 4 | 4 | $`(2,1,1)`$ | 378 |

The two hook cases use different fixed insertion tableaux with the same shape. Their identical shape distributions also check the claimed independence from that choice in these examples. The complete tableaux, shape counts, rational probabilities, and bridge counts are in [results.json](results.json).

Across these eight cases, the code visits 336,601 full words and retains 1,219. These are complete enumerations within the selected cases, rather than samples from a random process.

## What the checks do not establish

The mathematical proofs cover arbitrary permitted $`N`$ and $`d`$. Finite enumeration does not extend those quantifiers. The word checks support the RSK restriction and counting argument in small cases; they do not by themselves prove that an arbitrary correlated quantum input has the induced-representation law. That step is established in the [sector reduction](../science/sector-reduction.md).

The verification also does not establish asymptotic limits, circuit complexity, a physical implementation, or optimality against all channels. The [minimax proof](../science/minimax-proof.md) supplies the channel converse, and [accuracy and boundaries](../science/accuracy-and-boundaries.md) supplies the analytic limits and the coherent-occupation boundary. The numerical checks corroborate these proofs only to the extent stated above.
