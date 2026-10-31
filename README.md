# Quantum Majority Recovery

**Can a majority of correct quantum outputs recover an unknown state when the faulty outputs are entangled?**

This project establishes an exact recovery law. Of $`N=m+k`$ registers in dimension $`d`$, an unknown set of $`m>k`$ registers contains exact copies of one unknown pure state. The other $`k`$ registers have support in its orthogonal complement and may be arbitrarily entangled with one another. A fixed collective channel returns one approximation to the target.

The optimal worst-case fidelity is **exactly the qubit benchmark in every dimension**. Identical pure orthogonal faults already realize the worst case. The channel is inherited from quantum purity amplification; the result here is its sharp guarantee for every faulty symmetry sector and the matching unrestricted converse.

The promise permits classical mixtures of fault locations. Coherent superpositions of those locations lead to a different answer.

## Principal results

Let $`g=m-k=N-2k>0`$, and let $`M`$ be the maximum partial sum of a uniformly random path with $`k`$ up steps and $`m`$ down steps, including time zero. The exact optimal infidelity is

```math
\varepsilon_{N,k}
=\mathbb E\frac{M}{g+2M},
\qquad
\Pr(M\ge r)=\frac{\binom N{k-r}}{\binom Nk}.
```

The same channel is optimal for every strict-majority count, for even or odd $`N`$, and for an upper bound on the number of faults. It needs no target description or fault locations.

| Input promise or regime | Optimal recovery behavior |
|---|---|
| Exact good copies, orthogonal faulty registers, classical hidden locations | Exact qubit fidelity, independent of $`d`$ and entanglement within the faulty subset |
| Fixed faulty fraction $`k/N\to p\in(0,1/2)`$ | Infidelity $`p/[N(1-2p)^2]+o(N^{-1})`$ |
| One faulty register | Infidelity exactly $`1/N^2`$ |
| Small positive margin $`g=o(\sqrt N)`$ | Fidelity $`1/2+(\sqrt{\pi/8}+o(1))g/\sqrt N`$ |
| Arbitrary coherent state with exactly $`m`$ target occupations | Fidelity exactly $`m/N`$ |

The qubit fidelity sequence is established prior work. The three-input all-dimension value $`8/9`$ is also known. [Related work](references/RELATED_WORK.md) separates these results and the inherited Schur/RSK machinery from the correlated-input minimax theorem.

## Read the science

Start with the [model and exact theorem](science/model.md). The proof has two main parts: an exact representation law for arbitrary faulty states, and a coupling that bounds every such law by the binary case.

| To understand | Read |
|---|---|
| Inputs, output fidelity, quantifiers and resource assumptions | [Model](science/model.md) |
| The collective operation and its implementation cost | [Recovery channel](science/recovery-channel.md) |
| How entangled faults reduce to an exact conditional Schur law | [Sector reduction](science/sector-reduction.md) |
| Why identical orthogonal faults are exactly worst case | [Minimax proof](science/minimax-proof.md) |
| Accuracy, majority margins and the coherence boundary | [Accuracy and boundaries](science/accuracy-and-boundaries.md) |
| Imported ingredients and closest comparisons | [Related work](references/RELATED_WORK.md) and [bibliography](references/references.bib) |
| Exact finite checks and their limits | [Verification](verification/README.md) |

The [LLM reading guide](llms.txt) maps questions to these authoritative files.

## Reproduce the checks

From the repository root, run:

```bash
python3 verification/run_all.py
```

The suite uses only Python's standard library and compares its output with the committed [results](verification/results.json). It checks 1,929 faulty-sector cases and 10,142 representation branches with exact rational arithmetic. A separate word enumeration checks the RSK coupling and the complete recording-tableau sets for eight fixed insertion tableaux.

These finite checks corroborate the formulas and combinatorial construction. The general reduction, channel converse and asymptotic limits are established by the written proofs and attributed ingredients.

## Scope and costs

The theorem requires exact pure good registers, orthogonal faults, and classical uncertainty over their locations. It does not assume that faulty registers are independent or identical. The [coherent-occupation converse](science/accuracy-and-boundaries.md) shows why changing the location promise can prevent amplification.

The output is one quantum register, produced deterministically. The input-copy cost is $`N`$, with every preparation charged when the theorem is used to combine algorithm outputs. The inherited circuit is polynomial in $`N`$ and $`\log d`$ at finite precision. It requires collective quantum storage and a separate gate budget; dimension-independent copy complexity does not remove those costs. No QRAM, target projector or reversible preparation oracle is supplied.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
