# Accuracy and the input promise

The recovery theorem has an exact finite-sample answer. Its dependence on the majority margin also explains why a strict majority alone need not give high fidelity. This page derives useful bounds and limiting regimes, then identifies the boundary between unknown fault locations and coherent superpositions of fault locations.

Throughout, $`N=m+k`$, $`m>k`$, $`g=m-k=N-2k`$, and $`d\ge2`$. There are $`k`$ orthogonal faults. Fidelity means the overlap $`\langle\psi|\sigma|\psi\rangle`$ with the pure target, without taking a square root. The exact qubit fidelity sequence is due to [Buhrman et al.](../references/RELATED_WORK.md#BLMO2023). The [minimax proof](minimax-proof.md) establishes the same answer in arbitrary dimension with entangled orthogonal faults. The channel and pointwise fidelity formulas used there come from the purity-amplification literature, including [Li et al.](../references/RELATED_WORK.md#LTHC2026) and [Scharnhorst et al.](../references/RELATED_WORK.md#SSW2026).

## Exact risk and a binary bridge

Let $`M`$ be the maximum, including its initial value zero, of a uniform path containing $`k`$ up steps and $`m`$ down steps. Define

```math
T_r=\Pr(M\ge r)
=\frac{\binom N{k-r}}{\binom Nk},
\qquad 0\le r\le k,
\qquad T_{k+1}=0.
```

Reflection of the prefix ending at the first visit to level $`r`$ proves this formula: the reflected path has $`k-r`$ up steps. The optimal infidelity is

```math
\varepsilon_{N,k}
=\mathbb E\!\left[\frac{M}{g+2M}\right]
=\sum_{r=0}^{k}
  \frac{\binom N{k-r}-\binom N{k-r-1}}{\binom Nk}
  \frac{r}{g+2r}.
```

Here $`\binom N{-1}=0`$. Write $`F_N(k)=1-\varepsilon_{N,k}`$. This identity determines accuracy for every permitted $`N,k,d`$; the limits below are consequences of it, not separate improvements over the qubit optimum.

## Bounds for every sample size

For $`1\le r\le k`$,

```math
T_r
=\prod_{i=1}^{r}\frac{k-i+1}{m+i}
\le\left(\frac{k}{m+1}\right)^r.
```

Summing the tails gives

```math
\mathbb E[M]\le\frac{k}{g+1}.
```

The following bounds are valid also for $`k=0`$, when both sides are zero:

```math
\frac{k}{(m+1)(g+2)}
\le \varepsilon_{N,k}
\le
\min\left\{
  \frac{k}{(g+1)(g+2)},
  \frac{k}{g^2+N}
\right\}.
```

For the lower bound, $`M\ge1`$ occurs with probability $`k/(m+1)`$, and $`r/(g+2r)`$ is increasing. For the first upper bound, $`r/(g+2r)\le r/(g+2)`$ for every integer $`r\ge1`$. For the second, the function $`r/(g+2r)`$ is increasing and concave, so Jensen's inequality yields

```math
\varepsilon_{N,k}
\le\frac{\mathbb E[M]}{g+2\mathbb E[M]}
\le\frac{k}{g(g+1)+2k}
=\frac{k}{g^2+N}.
```

The simpler bound $`\varepsilon_{N,k}\le k/[g(g+1)]`$ follows directly by replacing $`g+2M`$ with $`g`$. The bounds above retain more information at small sample sizes and small majority margins.

Returning a uniformly random input register has infidelity $`k/N`$ under the original promise. The bound $`\varepsilon_{N,k}\le k/(g^2+N)`$ is strictly smaller whenever $`k>0`$. For $`k=0`$, recovery is exact. For one fault, the exact expression simplifies to

```math
\varepsilon_{N,1}=\frac1{N^2},\qquad N\ge3.
```

For $`N=3`$, this gives fidelity $`8/9`$. The all-dimension three-input value was already established by [Grinko and Ozols](../references/RELATED_WORK.md#GO2024).

## More faults make the task harder

The exact risk is nondecreasing in $`k`$ throughout the strict-majority range. This can be seen without differentiating a sum or using an asymptotic approximation.

Choose a uniform $`k`$-subset of the $`N`$ positions as the up-step positions. Add one uniformly chosen element of its complement. The resulting subset is uniform among the $`(k+1)`$-subsets. Changing a down step to an up step leaves earlier partial sums unchanged and raises every later partial sum by two. Therefore the new maximum $`M'`$ is at least $`M`$. At the same time, the margin changes from $`g`$ to $`g-2`$. Whenever both counts have a strict majority,

```math
\frac{M'}{g-2+2M'}\ge\frac{M}{g+2M}.
```

Taking expectations proves $`\varepsilon_{N,k+1}\ge \varepsilon_{N,k}`$. The same recovery channel works for every count. Consequently, the exact minimax value for an at-most-$`k`$ orthogonal-fault promise is also $`\varepsilon_{N,k}`$: the guarantee follows from monotonicity, and the exact-$`k`$ hard family remains admissible.

## Fixed fault fraction

Suppose $`k/N\to\alpha`$ for a fixed $`0\lt\alpha\lt1/2`$. Then

```math
\varepsilon_{N,k}
=\frac{\alpha}{(1-2\alpha)^2}\frac1N
 +o(N^{-1}).
```

For each fixed integer $`r`$, the bridge tail converges to

```math
T_r\longrightarrow q^r,
\qquad q=\frac{\alpha}{1-\alpha}\lt1.
```

Thus $`M`$ converges to a geometric variable on $`\{0,1,\ldots\}`$ whose mean is $`q/(1-q)=\alpha/(1-2\alpha)`$. The geometric tail bound above is uniform once $`N`$ is sufficiently large. It therefore justifies passage to the expectation in

```math
N \varepsilon_{N,k}
=\mathbb E\!\left[\frac{NM}{g+2M}\right]
\longrightarrow
\frac1{1-2\alpha}\frac{\alpha}{1-2\alpha}.
```

A fixed majority fraction above one half therefore gives infidelity of order $`1/N`$, with the displayed leading coefficient. These are copy-accuracy statements. They do not claim dimension-independent gate or workspace costs.

## A fixed number of faults

For every fixed positive integer $`k`$,

```math
\varepsilon_{N,k}\sim\frac{k}{N^2}
\qquad (N\to\infty).
```

This follows by squeezing the risk between $`k/[(m+1)(g+2)]`$ and $`k/[(g+1)(g+2)]`$: both denominators are asymptotic to $`N^2`$. For $`k=0`$ the exact risk is zero, so a relative asymptotic expression is unnecessary.

## Nearly tied inputs

Let the positive integer margin satisfy $`g=o(\sqrt N)`$, with the parity required by $`k=(N-g)/2`$. Then

```math
F_N(k)
=\frac12+
 \left(\sqrt{\frac\pi8}+o(1)\right)\frac{g}{\sqrt N}.
```

In particular, the narrowest odd-$`N`$ majority has $`g=1`$ and fidelity $`1/2+\Theta(N^{-1/2})`$, consistent with the qubit majority result of [Buhrman et al.](../references/RELATED_WORK.md#BLMO2023). Strict majority by itself does not imply fidelity tending to one.

Here is a derivation that also controls the contribution from paths with a small maximum. The exact relation

```math
T_r-T_{r+1}
=T_r\frac{g+2r+1}{m+r+1}
```

and the identity $`r/(g+2r)=1/2-g/[2(g+2r)]`$ give

```math
F_N(k)-\frac12
=\frac g2\sum_{r=0}^{k}\frac{T_r}{m+r+1}
 +\frac g2\sum_{r=0}^{k}
   \frac{T_r}{(m+r+1)(g+2r)}.
```

For every fixed $`x\ge0`$, the tail product implies

```math
T_{\lfloor x\sqrt N\rfloor}\longrightarrow e^{-2x^2}
\qquad\text{when }g=o(\sqrt N).
```

The elementary bound $`\log(1-u)\le-u`$ also gives

```math
T_r\le\exp\!\left[-\frac{rg+r^2}{N}\right],
```

which supplies integrable domination for the corresponding Riemann sums. Since $`m\sim N/2`$, the first sum contributes

```math
\frac g{\sqrt N}\int_0^\infty e^{-2x^2}\,dx
=\sqrt{\frac\pi8}\frac g{\sqrt N}.
```

The second sum is $`O(N^{-1}+g\log N/N)`$, by bounding $`T_r\le1`$ and using a harmonic sum. It is $`o(g/\sqrt N)`$ for every positive integer $`g`$ in this regime. This proves the stated leading coefficient.

The same argument describes the transition scale. If $`g/\sqrt N\to a\in[0,\infty)`$, then

```math
F_N(k)\longrightarrow
\frac12+
a\sqrt{\frac\pi8}\,e^{a^2/2}
\mathrm{erfc}\!\left(\frac a{\sqrt2}\right).
```

Here $`\mathrm{erfc}(z)=(2/\sqrt\pi)\int_z^\infty e^{-t^2}\,dt`$. In the Riemann sum, the limiting tail is now $`e^{-2x(x+a)}`$. This gives a positive limiting error for every finite $`a`$. Together with $`\varepsilon_{N,k}\le k/(g^2+N)`$, it follows that fidelity tends to one precisely when $`g/\sqrt N\to\infty`$. This statement concerns sequences of strict-majority instances.

## What “pure good registers” requires

For a fixed target $`\psi`$, let $`P_\psi=|\psi\rangle\langle\psi|`$ and $`Q_\psi=I-P_\psi`$. The admissible exact-count class is the convex hull of states

```math
\rho=U_\pi\bigl(P_\psi^{\otimes m}\otimes\omega\bigr)U_\pi^\dagger,
\qquad
\mathrm{supp}\,\omega\subseteq
\mathrm{ran}(Q_\psi)^{\otimes k}.
```

The permutation $`U_\pi`$ and the bad state $`\omega`$ may be unknown and classically correlated. The bad registers can be entangled with one another. If a register has a pure reduced state, it factors from the rest of the system. Thus actual pure good registers necessarily factor from the bad registers in each fixed-placement component.

The convex hull permits classical uncertainty about placement. It does not include every coherent state with exactly $`m`$ target occupations. The difference changes the optimal accuracy by a finite amount at a fixed fault fraction.

## Coherent fixed occupation has optimum $`m/N`$

Consider the larger class of density operators supported on the eigenvalue-$`m`$ subspace of

```math
\mathcal N_\psi
=\sum_{i=1}^{N}(P_\psi)_i.
```

For this class, the exact universal minimax fidelity is

```math
F^{\mathrm{occupation}}_{N,k}=\frac mN.
```

### Achievability

Choose one of the $`N`$ input registers uniformly and return it. For every state in the stated subspace, the resulting fidelity is

```math
\frac1N\sum_{i=1}^{N}\mathrm{Tr}[(P_\psi)_i\rho]
=\frac1N\mathrm{Tr}(\mathcal N_\psi\rho)
=\frac mN.
```

This works with arbitrary coherence and correlations. If the occupation promise is at least $`m`$, the same calculation gives fidelity at least $`m/N`$.

### Converse

It suffices to consider a fixed embedded qubit subspace and its symmetric Dicke states

```math
|D_{N,k}^{\psi,\phi}\rangle
=\binom Nk^{-1/2}
\sum_{\substack{B\subseteq[N]\\|B|=k}}
|\psi\rangle_{B^c}^{\otimes m}
|\phi\rangle_B^{\otimes k},
\qquad \langle\psi|\phi\rangle=0.
```

These form a covariant qubit family in the spin-$`J`$ representation with $`J=N/2`$ and spin component $`z=g/2`$. Averaging any candidate channel over $`SU(2)`$ cannot decrease its worst-case fidelity on this family. A covariant channel from spin $`J`$ to one qubit is a convex combination of two extremal channels, the trace channel and the universal-NOT channel. This characterization and the channels are given in [Buhrman et al., Section 4.3 and Corollary 4.5](../references/RELATED_WORK.md#BLMO2023).

Their fidelities on a spin state with component $`z`$ are

```math
F_{\mathrm{Tr}}=\frac{J+z}{2J}=\frac mN,
\qquad
F_{\mathrm{UNOT}}=\frac{J-z+1}{2J+2}=\frac{k+1}{N+2}.
```

For $`g>0`$, the first is larger, because

```math
\frac mN-\frac{k+1}{N+2}
=\frac{g(N+1)}{N(N+2)}>0.
```

Every convex combination therefore has fidelity at most $`m/N`$. Extra output dimensions cannot improve this qubit converse: project the output onto the embedded qubit subspace and replace the discarded weight by any fixed qubit state. This is a trace-preserving channel and can only increase fidelity with a target in that subspace. An improvement in dimension $`d`$ would consequently produce an impossible improvement for the qubit family. The [minimax proof](minimax-proof.md) writes this projection channel explicitly.

The Dicke family lies in the exact-occupation class and also in the at-least-$`m`$ class. Thus the converse matches the random-register guarantee for both. At a fixed positive fault fraction, $`m/N`$ stays bounded away from one. This is a limitation of every universal channel for the enlarged promise, rather than only a limitation of the recovery channel analyzed here.

## Verification scope

The proofs establish statements for all permitted dimensions and sample sizes. The independent finite checks in [verification](../verification/README.md) corroborate selected consequences: exact rational branch calculations through $`N=18`$, and direct RSK enumeration for small fixed insertion tableaux. Those checks do not establish an asymptotic limit, an infinite-dimensional statement, or the representation-theoretic reduction by themselves.
