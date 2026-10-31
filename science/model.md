# Unknown-state recovery from a strict majority

Suppose several preparations are intended to produce the same unknown pure quantum state. More than half succeed exactly. The other preparations have support orthogonal to the target, but their states and their correlations are unrestricted. Can a collective operation return one accurate target state without knowing which preparations succeeded?

The answer has an exact finite-sample form. For every register dimension, the optimal worst-case fidelity equals the known qubit benchmark. A larger orthogonal subspace and entanglement confined to the faulty registers impose no additional minimax cost. The locations of the good registers must be classical unknowns, or a mixture of such configurations. [Allowing coherent superpositions of those locations changes the optimum](accuracy-and-boundaries.md).

## 1. Input and output

Let $`H=\mathbb C^d`$, with $`d\ge2`$, and let

```math
N=m+k,\qquad m>k\ge0,\qquad g=m-k=N-2k.
```

Here $`m`$ is the number of good registers and $`k`$ is the number of faults. Write $`P_\psi=|\psi\rangle\langle\psi|`$ for an unknown unit vector. For a fixed target, the admissible input set is

```math
\mathcal A_{\psi,N,k}
=\operatorname{conv}\!\left\{
U_\pi\left(P_\psi^{\otimes m}\otimes\omega\right)U_\pi^\dagger:
\pi\in S_N,\ 
\omega\in\mathsf D\!\left((\psi^\perp)^{\otimes k}\right)
\right\}.
```

The permutation $`U_\pi`$ rearranges tensor factors. The convex hull permits a classical mixture of locations and faulty states, including correlations between these two choices. Every component has the same target $`\psi`$. The faulty density operator $`\omega`$ may be mixed and entangled across all its $`k`$ registers.

An actual pure good marginal forces that register to factor from the remaining systems. This is why each component has the displayed tensor-product form. The promise does not allow coherence between distinct sets of good locations. It also does not permit a faulty register with an arbitrary nonorthogonal component along the target.

The processor receives the quantum registers. It knows $`N`$ and $`d`$, but receives no target description, target projector, preparation inverse, reflection oracle, or list of fault locations. It outputs one $`d`$-dimensional register through a deterministic completely positive trace-preserving map

```math
\Phi:\mathsf L(H^{\otimes N})\longrightarrow\mathsf L(H).
```

Arbitrary ancillary systems, measurements and feed-forward are allowed. Success is evaluated unconditionally; a heralded successful branch alone does not meet this output contract. Fidelity means overlap with the pure target,

```math
F_\psi(\Phi,\rho)
=\langle\psi|\Phi(\rho)|\psi\rangle,
```

without a square root.

## 2. Exact recovery theorem

Define the minimax fidelity

```math
F^\star_{N,k,d}
=\sup_{\Phi\ {\rm CPTP}}\ 
\inf_{\substack{\psi\\ \rho\in\mathcal A_{\psi,N,k}}}
F_\psi(\Phi,\rho).
```

The optimization even allows the processor to know $`k`$. The channel constructed below does not require that knowledge.

**Theorem 1: exact dimension universality.** For every $`d\ge2`$ and $`0\le k<N/2`$,

```math
F^\star_{N,k,d}=F_N(k)
=\sum_{j=0}^{k}
\frac{\binom Nj-\binom N{j-1}}{\binom Nk}
\frac{N-k-j}{N-2j},
\qquad \binom N{-1}=0.
```

One universal channel $`\Phi_{N,d}`$ attains this value for every strict-majority fault count. Its worst case includes the family in which all faulty registers equal the same unknown pure state orthogonal to the target. The same value holds for the promise of at most $`k`$ faults.

The function $`F_N(k)`$ is the qubit benchmark obtained from the covariant-channel characterization in [BLMO2023](../references/RELATED_WORK.md#BLMO2023). Their majority statement uses odd $`N`$; the same characterization gives the even-$`N`$ strict-majority case, as derived in [the converse](minimax-proof.md). The result here is its exact extension to the input class $`\mathcal A_{\psi,N,k}`$. Neither the qubit formula nor the underlying collective channel is new.

An equivalent form makes the recovery mechanism and accuracy easier to inspect. Let $`M`$ be the maximum, including time zero, of a uniformly random path with $`k`$ steps $`+1`$ and $`m`$ steps $`-1`$. Then the optimal infidelity is

```math
\varepsilon_{N,k}
=1-F_N(k)
=\mathbb E\frac{M}{g+2M},
\qquad
\Pr(M\ge r)=\frac{\binom N{k-r}}{\binom Nk},
\quad 1\le r\le k.
```

Equivalently,

```math
\varepsilon_{N,k}
=\sum_{r=0}^{k}
\frac{\binom N{k-r}-\binom N{k-r-1}}{\binom Nk}
\frac{r}{g+2r}.
```

All denominators are positive under the strict-majority assumption. In particular, $`F_N(0)=1`$ and $`F_3(1)=8/9`$. The latter all-dimension value was already established by [GO2024](../references/RELATED_WORK.md#GO2024).

## 3. What the theorem changes

For a fixed faulty fraction $`k/N\to p\in(0,1/2)`$,

```math
\varepsilon_{N,k}
=\frac{p}{(1-2p)^2N}+o(N^{-1}).
```

Thus a constant majority yields arbitrarily accurate recovery with copy count proportional to the inverse target infidelity, uniformly in the Hilbert-space dimension. The rate itself is inherited from the qubit benchmark. The theorem establishes that it remains optimal under arbitrary correlations inside the orthogonal faulty subset, with the same exact finite-sample value.

A one-register majority has a different behavior: when $`N`$ is odd and $`g=1`$, the fidelity is only $`1/2+\Theta(N^{-1/2})`$. A positive majority and a majority separated from one half are therefore distinct promises. [Accuracy and boundaries](accuracy-and-boundaries.md) derives the regimes directly from the exact law.

The input promise can describe a bounded number of joint replacement faults after preparing copies of a state. The collector need not know where replacement occurred. It is a structured error model. General noise in a preparation algorithm need not satisfy exact orthogonality or classical placement, so the theorem is not an unconditional method for amplifying every quantum-output algorithm.

## 4. Proof route and attribution

The [recovery channel](recovery-channel.md) measures a Schur label and extracts one fundamental representation by removing a box from the first row. This channel and its exact component fidelity are established ingredients of quantum purity amplification.

The [sector reduction](sector-reduction.md) handles the new correlated-input class. Covariance allows an analytical twirl over the target stabilizer and permutations of the faulty registers. Each faulty sector $`\nu`$ induces the exact law

```math
\Pr(\lambda\mid\nu)
=\frac{f^\lambda}{\binom Nm\,f^\nu},
\qquad \lambda/\nu\text{ is a horizontal strip of size }m.
```

The [minimax proof](minimax-proof.md) couples this law to the binary path maximum. The first-row excess $`r=\lambda_1-m`$ satisfies $`r\le M`$ in that coupling. An inherited component bound gives infidelity at most $`r/(g+2r)`$, so the binary family dominates every faulty sector. Equality for identical pure orthogonal faults and the known qubit converse close the minimax result.

The exact component formula, first-row defect identity, scalar bound and use of RSK in purification are explicitly credited to [SSW2026](../references/RELATED_WORK.md#SSW2026) and [LTHC2026](../references/RELATED_WORK.md#LTHC2026). The consequential additional statement is the sharp bound for every faulty symmetry sector, including sectors produced by entangled faulty inputs.

## 5. Resources and stability

The theorem counts supplied quantum registers. When those registers arise from repeated preparations, their preparation costs must be charged $`N`$ times. No QRAM or free classical data loading is assumed.

The inherited collective implementation has a gate bound polynomial in $`N`$ and $`\log d`$, with a separate circuit-precision parameter. It uses quantum storage for the input block and auxiliary registers. Dimension-independent copy complexity does not mean dimension-independent storage or a constant gate cost. [The channel account](recovery-channel.md) gives the explicit implementation bound and its scope.

The model has a direct continuity guarantee. If $`\widetilde\rho`$ is within half trace distance $`\eta`$ of an admissible $`\rho`$, then contractivity and $`0\le P_\psi\le I`$ imply

```math
\langle\psi|\Phi_{N,d}(\widetilde\rho)|\psi\rangle
\ge F_N(k)-\eta.
```

This is stability with respect to distance from the entire admissible input class. It does not convert arbitrary nonorthogonal corruption into an admissible fault, nor does a bound on each marginal alone imply the required joint-state distance.

## Reading route

| Question | Authoritative account |
|---|---|
| Which operation achieves recovery, and what does it cost? | [Recovery channel](recovery-channel.md) |
| Why does arbitrary faulty entanglement reduce to partitions? | [Sector reduction](sector-reduction.md) |
| Why is the binary family exactly worst case? | [Minimax proof](minimax-proof.md) |
| How does accuracy depend on the margin, and where does recovery fail? | [Accuracy and boundaries](accuracy-and-boundaries.md) |
| Which ingredients and neighboring results are established? | [Related work](../references/RELATED_WORK.md) |
| What has been checked by exact finite computation? | [Verification](../verification/README.md) |
