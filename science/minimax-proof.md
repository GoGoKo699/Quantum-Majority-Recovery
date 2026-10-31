# Exact minimax fidelity of quantum majority recovery

The worst orthogonal fault state is already realized by identical copies of one orthogonal vector. Neither a larger local dimension nor entanglement among the faulty registers increases the minimax error. This file proves that statement at every finite input size with a strict majority.

The operational promise is in [model.md](model.md), the recovery channel is in [recovery-channel.md](recovery-channel.md), and the exact conditional Schur law is proved in [sector-reduction.md](sector-reduction.md). Accuracy regimes and the boundary of the promise are discussed in [accuracy-and-boundaries.md](accuracy-and-boundaries.md).

The channel, its Clebsch–Gordan component formula, the overhang-defect bound, and the use of RSK in purity amplification are inherited from prior work, particularly [SSW2026](../references/RELATED_WORK.md#SSW2026) and [LTHC2026](../references/RELATED_WORK.md#LTHC2026). The qubit minimax formula is due to [BLMO2023](../references/RELATED_WORK.md#BLMO2023). The argument below applies these ingredients to the conditional law for every bad partition and obtains an exact worst-case identity.

## 1. Statement of the theorem

Let $`d\ge2`$, $`N\ge1`$, and $`0\le k<N/2`$ be integers. Write

```math
m=N-k,
\qquad g=m-k=N-2k>0.
```

For a unit vector $`|\psi\rangle\in\mathbb C^d`$, write $`P_\psi=|\psi\rangle\langle\psi|`$. Let $`\mathcal A_{\psi,N,k}`$ be the convex hull of the states obtained by putting $`P_\psi^{\otimes m}`$ on an arbitrary $`m`$-element set of registers and an arbitrary density operator supported on $`(\psi^\perp)^{\otimes k}`$ on its complement. Convex mixtures keep the same target $`\psi`$.

The optimal worst-case fidelity is

```math
F^\star_{N,k,d}
=\sup_{\Lambda\,\mathrm{CPTP}}
\inf_{\|\psi\|=1}
\inf_{\rho\in\mathcal A_{\psi,N,k}}
\langle\psi|\Lambda(\rho)|\psi\rangle,
```

where $`\Lambda`$ maps $`N`$ registers of dimension $`d`$ to one such register. Fidelity here is the overlap with the pure target, without a square root.

**Theorem.** The single channel $`\Phi_{N,d}`$ of [recovery-channel.md](recovery-channel.md) is optimal for every $`k<N/2`$, and

```math
\boxed{
F^\star_{N,k,d}=F_N(k)
=\frac1{\binom Nk}
\sum_{j=0}^k
\left[\binom Nj-\binom N{j-1}\right]
\frac{N-k-j}{N-2j}.
}
\tag{1}
```

Use the convention $`\binom Nt=0`$ for $`t<0`$ or $`t>N`$. The theorem holds for even and odd $`N`$. The channel does not need to know $`m`$ or $`k`$.

An equivalent expression is obtained from a uniformly random word of $`m`$ good symbols and $`k`$ bad symbols. Give a good symbol increment $`-1`$ and a bad symbol increment $`+1`$, and let $`M`$ be the maximum partial sum, including the initial zero. Then

```math
\boxed{
\varepsilon_{N,k}:=1-F_N(k)
=\mathbb E\!\left[\frac{M}{g+2M}\right],
\qquad
\Pr(M\ge s)=\frac{\binom N{k-s}}{\binom Nk}\quad(1\le s\le k).
}
\tag{2}
```

The same value is optimal for the promise of at most $`k`$ faults. Sections 2 through 6 prove achievability and its equality case. Sections 7 and 8 prove optimality and the at-most-$`k`$ assertion.

## 2. The branch estimate used in the proof

Fix a bad partition $`\nu\vdash k`$, with $`\ell(\nu)\le d-1`$. By [sector-reduction.md](sector-reduction.md), the input reduces to a mixture of supported pairs $`(\lambda,\nu)`$, where $`\lambda/\nu`$ is a horizontal $`m`$-strip, with probability

```math
p(\lambda\mid\nu)=\frac{f^\lambda}{\binom Nm f^\nu}.
\tag{3}
```

Here $`f^\lambda`$ is the dimension of the Specht module of shape $`\lambda`$. The first-row excess

```math
r=\lambda_1-m
```

satisfies $`0\le r\le k`$ and $`\lambda_1-\lambda_2\ge g+2r>0`$.

The inherited branch fidelity, specialized to one output and first-row removal, is

```math
a_{\lambda,\nu}
=\prod_{i=1}^{d-1}
\frac{\lambda_1-\nu_i+i-1}
{\lambda_1-\lambda_{i+1}+i-1}.
\tag{4}
```

This is the single-output case of [SSW2026](../references/RELATED_WORK.md#SSW2026), Lemma 3.1, Eq. (19), and of [LTHC2026](../references/RELATED_WORK.md#LTHC2026), Theorem 4, Eq. (33). It is a component formula, so its use does not require an iid input.

For completeness, set

```math
b_i=\nu_i-\lambda_{i+1},
\qquad
D_i=\lambda_1-\lambda_{i+1}+i-1.
```

Interlacing gives $`0\le b_i\le D_i`$, and

```math
\sum_{i=1}^{d-1}b_i
=k-(N-\lambda_1)=r,
\qquad
D_i\ge\lambda_1-\lambda_2\ge g+2r.
```

The product inequality $`1-\prod_i(1-x_i)\le\sum_i x_i`$ for $`0\le x_i\le1`$ yields

```math
1-a_{\lambda,\nu}
\le\sum_{i=1}^{d-1}\frac{b_i}{D_i}
\le\frac{r}{g+2r}.
\tag{5}
```

The product-to-sum step and the identity for $`\sum b_i`$ are already used in [SSW2026](../references/RELATED_WORK.md#SSW2026), Eq. (24) and the subsequent calculation before Eq. (27). Here the fixed-count relation keeps the denominator $`g+2r`$ coupled to the numerator. This will permit equality with the binary instance.

## 3. An exact RSK coupling for each bad partition

We use row-insertion RSK for words over the ordered alphabet $`\{1,\ldots,d\}`$. The insertion tableau $`P(w)`$ has weakly increasing rows and strictly increasing columns. The recording tableau $`Q(w)`$ is standard. In row insertion, an inserted letter replaces the first strictly larger entry in a row and bumps that entry to the next row; if no such entry exists, it is appended.

The RSK correspondence is a bijection between words and pairs $`(P,Q)`$ of the same shape, with $`P`$ semistandard and $`Q`$ standard. The first row of the resulting shape has the length of a longest weakly increasing subsequence. These are the RSK facts used in the purification analysis of [SSW2026](../references/RELATED_WORK.md#SSW2026), Section 2.1.

### Restriction lemma

For a word $`w`$, let $`w_{<d}`$ be the word obtained by deleting every occurrence of $`d`$. Let $`P(w)_{<d}`$ be the insertion tableau with its boxes labeled $`d`$ deleted. Then

```math
P(w)_{<d}=P(w_{<d}).
\tag{6}
```

**Proof.** Proceed through the letters of $`w`$ and compare the insertion processes. Inserting $`d`$ appends it to the first row, so the restriction to smaller letters is unchanged. When inserting $`x<d`$, every bump of an entry smaller than $`d`$ agrees with the insertion process in the restricted tableau. At the first row where the restricted process would append a letter and stop, the full process either also appends it, or replaces the first $`d`$ in that row. In the second case the bumped $`d`$ appends to the next row. This last change disappears on restricting to letters smaller than $`d`$. Thus both restricted tableaux agree after each insertion, proving (6).

### Construction of the coupling

Fix any semistandard tableau $`P_0`$ of shape $`\nu`$ on $`\{1,\ldots,d-1\}`$. Such a tableau exists because $`\ell(\nu)\le d-1`$; filling row $`i`$ with $`i`$ is one choice. Its choice will not affect the shape law below.

Sample the following two objects independently:

1. A uniformly random standard tableau $`Q_0`$ of shape $`\nu`$. Inverse RSK gives the unique word $`u`$ with pair $`(P_0,Q_0)`$.
2. A uniformly random $`k`$-element set $`B\subseteq[N]`$. Place the successive letters of $`u`$ into the positions in $`B`$, in their original order, and put the symbol $`d`$ in all other positions. Call the resulting length-$`N`$ word $`w`$.

There are exactly $`f^\nu\binom Nk`$ equally likely choices. Different choices give different words: $`B`$ is recovered as the set of positions whose letters are smaller than $`d`$, and $`Q_0`$ is recovered from RSK of that subword. Thus the constructed word is uniform on

```math
\Omega(P_0,m)
=\{w:\#\{t:w_t=d\}=m,\ P(w_{<d})=P_0\}.
```

By (6), the full insertion tableau restricts to $`P_0`$. Its additional boxes are all labeled $`d`$. Strict increase down columns means that no column contains two added boxes. Hence its shape $`\lambda`$ satisfies the horizontal-strip condition.

Conversely, for each horizontal strip $`\lambda/\nu`$ of size $`m`$, there is exactly one possible full insertion tableau: retain $`P_0`$ on $`\nu`$ and fill every box of $`\lambda/\nu`$ with $`d`$. This tableau is semistandard. The added boxes form row-end suffixes, and the horizontal-strip condition ensures that no added $`d`$ lies above another occupied box in the same column. All entries above an added box are smaller than $`d`$.

For every standard tableau $`Q`$ of shape $`\lambda`$, inverse RSK of this full insertion tableau and $`Q`$ produces a word in $`\Omega(P_0,m)`$, again by (6). There are therefore exactly $`f^\lambda`$ constructed words of shape $`\lambda`$. It follows that

```math
\Pr(\operatorname{shape}(P(w))=\lambda)
=\frac{f^\lambda}{\binom Nk f^\nu}
=p(\lambda\mid\nu).
\tag{7}
```

This realizes the conditional quantum shape law as an exact classical coupling. It holds for each fixed $`\nu`$ and $`P_0`$. It does not sample letters from an iid spectrum.

## 4. Binary domination of the first-row excess

For the constructed word, let $`B_t`$ and $`G_t`$ count its bad and good positions among $`1,\ldots,t`$. Define

```math
S_t=B_t-G_t,
\qquad S_0=0,
\qquad
M=\max_{0\le t\le N}S_t.
```

The path has $`k`$ increments $`+1`$, $`m`$ increments $`-1`$, and endpoint $`S_N=-g`$. Its law is uniform among such paths because $`B`$ was sampled uniformly. It is independent of the choice of $`P_0`$ and of the bad recording tableau $`Q_0`$.

Consider any weakly increasing subsequence of $`w`$. If it contains no bad letter, its length is at most $`m`$. Otherwise let $`t`$ be the position of its last selected bad letter. Every selected bad letter occurs in the prefix ending at $`t`$, and every selected good letter must occur after $`t`$, since $`d`$ is larger than every bad letter. Its length is therefore at most

```math
B_t+(m-G_t)=m+S_t\le m+M.
```

The subsequence containing all $`d`$ letters has length $`m`$. By the longest-subsequence property of RSK,

```math
\boxed{0\le r=\lambda_1-m\le M}
\tag{8}
```

for every word in the coupling. This is a pathwise comparison, rather than a comparison of expectations.

Define $`h_g(x)=x/(g+2x)`$ for $`x\ge0`$. Since $`g>0`$, this function is increasing. Combining (5), (7), and (8) gives, separately for every bad partition,

```math
\sum_\lambda p(\lambda\mid\nu)(1-a_{\lambda,\nu})
\le\mathbb E[h_g(r)]
\le\mathbb E[h_g(M)].
\tag{9}
```

The right side no longer depends on $`\nu`$ or $`d`$. Averaging (9) with the arbitrary weights $`q_\nu`$ from the sector reduction proves the same error bound for every permitted faulty density operator. Linearity also proves it for mixtures of fault locations and fault states.

## 5. Reflection law for the binary bridge

Fix an integer $`1\le s\le k`$. A path counted by $`\{M\ge s\}`$ has a first hitting time of level $`s`$. Reverse the signs of all increments up to and including that hitting time, leaving the remaining increments unchanged.

The reflected prefix has $`s`$ fewer positive increments than the original prefix. The resulting length-$`N`$ path therefore has $`k-s`$ positive increments and $`m+s`$ negative increments. Its endpoint is $`-g-2s`$.

This transformation is a bijection onto all paths with those new increment counts. To invert it, take such a path, whose endpoint is below $`-s`$, and reflect the prefix ending at its first visit to $`-s`$. Before that first visit the reflected prefix stays below $`s`$, so the inverse path first visits $`s`$ at the corresponding time. The two constructions undo each other.

There are $`\binom Nk`$ original paths and $`\binom N{k-s}`$ reflected paths. Thus

```math
\Pr(M\ge s)=\frac{\binom N{k-s}}{\binom Nk}.
\tag{10}
```

Taking the difference of consecutive tails, with the tail at zero equal to one and the tail at $`k+1`$ equal to zero, gives

```math
\Pr(M=r)
=\frac{\binom N{k-r}-\binom N{k-r-1}}{\binom Nk},
\qquad 0\le r\le k.
\tag{11}
```

Equations (9) and (11) prove that $`\Phi_{N,d}`$ has error at most the expression in (2). Reindexing $`j=k-r`$ gives the fidelity formula in (1), since

```math
1-\frac{r}{g+2r}
=\frac{N-k-j}{N-2j}.
```

## 6. Equality for identical orthogonal faults

Choose any unit vector $`|\phi\rangle\perp|\psi\rangle`$ and use the fault state $`\omega=(|\phi\rangle\langle\phi|)^{\otimes k}`$. This is supported entirely in the bad partition $`\nu=(k)`$, including its stabilizer twirl. In the coupling choose $`P_0`$ to be a single row of $`k`$ copies of the letter $`1`$. Every constructed word then contains only $`1`$ and $`d`$.

For any cut position $`t`$, all bad letters in its prefix followed by all good letters in its suffix form a weakly increasing subsequence of length $`m+S_t`$. Maximizing over $`t`$ shows that the upper bound (8) is exact:

```math
r=M,
\qquad
\lambda=(m+M,k-M).
```

There are at most two rows because the word uses only two letters. In (4), only the first factor can differ from one. It has $`b_1=M`$ and $`D_1=g+2M`$, so

```math
1-a_{\lambda,(k)}=\frac{M}{g+2M}.
```

Both inequalities in (9) are equalities. Consequently

```math
\inf_{\|\psi\|=1}\inf_{\rho\in\mathcal A_{\psi,N,k}}
\langle\psi|\Phi_{N,d}(\rho)|\psi\rangle
=F_N(k).
\tag{12}
```

For $`k=0`$, all the distributions are concentrated at $`M=r=0`$ and the fidelity is one. For $`N=3,k=1`$, (1) gives $`8/9`$, agreeing with the higher-dimensional three-input case in [GO2024](../references/RELATED_WORK.md#GO2024). Equation (12) identifies the worst input for the stated channel. The converse below shows that no other channel improves its worst-case fidelity.

## 7. Matching minimax converse

### 7.1 Qubit symmetry reduction

First consider $`d=2`$ and inputs obtained by placing $`m`$ copies of $`|0\rangle`$ and $`k`$ copies of $`|1\rangle`$ in arbitrary positions, then applying the same unknown $`U\in SU(2)`$ to every register. The target is $`U|0\rangle`$.

For any qubit-output channel $`\Lambda`$, average it over input permutations and simultaneous rotations, undoing the output rotation:

```math
\overline\Lambda(X)
=\int_{SU(2)}\frac1{N!}\sum_{\pi\in S_N}
U^\dagger\Lambda\!\left(
U^{\otimes N}U_\pi XU_\pi^\dagger(U^\dagger)^{\otimes N}
\right)U\,dU.
```

This is a CPTP map. Its target fidelity is an average of fidelities of $`\Lambda`$ on the same hard input family, so its worst-case fidelity is at least that of $`\Lambda`$. It is permutation invariant and $`SU(2)`$ covariant. Restricting the minimax optimization to such channels therefore loses nothing.

The permutation average of the unrotated input is the normalized projector onto the computational subspace with exactly $`k`$ ones. Let

```math
z=\frac{m-k}{2}>0,
\qquad
J=\frac N2-j.
```

In the Schur decomposition, $`\lambda=(N-j,j)`$ carries spin $`J`$. Its magnetic-weight-$`z`$ subspace is one-dimensional when $`0\le j\le k`$ and absent otherwise. The averaged input is therefore a mixture of the pure spin states $`|J,z\rangle`$, with a maximally mixed Specht factor and probabilities

```math
p_j=\frac{f^{(N-j,j)}}{\binom Nk}
=\frac{\binom Nj-\binom N{j-1}}{\binom Nk},
\qquad 0\le j\le k.
\tag{13}
```

The last equality follows from the two-row hook-length formula:

```math
f^{(N-j,j)}
=\frac{N!(N-2j+1)}{(N-j+1)!j!}
=\binom Nj-\binom N{j-1}.
```

The dimensions in (13) sum to $`\binom Nk`$, as required. A permutation-invariant channel discards the Specht factor, and each spin sector has its own covariant CPTP map to the output qubit.

### 7.2 Optimal channel within a spin sector

Every sector in (13) has $`J\ge z>0`$. The Choi operator of a covariant spin-$`J`$-to-qubit channel commutes with the representation on $`Q_{1/2}\otimes\overline{Q_J}`$. This tensor product splits into spins $`J-1/2`$ and $`J+1/2`$, each with multiplicity one. Its positive invariant Choi operators are thus nonnegative linear combinations of the two corresponding projectors.

The partial trace of the spin-$`L`$ projector is $`(2L+1)/(2J+1)`$ times the input identity, by Schur's lemma and its trace. The trace-preserving constraint consequently makes the admissible Choi operators the convex hull of the two normalized projectors. Equivalently, every covariant channel is a mixture of the channels whose Stinespring environment spins are $`J-1/2`$ and $`J+1/2`$.

The Clebsch–Gordan coefficients give the target-up output probabilities

```math
A_-(J,z)=\frac{J+z}{2J},
\qquad
A_+(J,z)=\frac{J-z+1}{2J+2}.
\tag{14}
```

For example, the first is obtained by the isometry

```math
|J,z\rangle\longmapsto
\sqrt{\frac{J+z}{2J}}\,
|\uparrow\rangle|J-\tfrac12,z-\tfrac12\rangle
+
\sqrt{\frac{J-z}{2J}}\,
|\downarrow\rangle|J-\tfrac12,z+\tfrac12\rangle.
```

For the second isometry the squared up coefficient is $`(J-z+1)/(2J+2)`$ and the squared down coefficient is $`(J+z+1)/(2J+2)`$; their relative phase does not affect the output overlap. Tracing out the environment yields (14).

Since $`z>0`$,

```math
A_-(J,z)-A_+(J,z)
=\frac z2\left(\frac1J+\frac1{J+1}\right)>0.
```

The first channel is optimal for every allowed positive magnetic weight, not just for one averaged input. Substituting $`J=N/2-j`$ and $`z=(N-2k)/2`$ gives

```math
A_-(J,z)=\frac{N-k-j}{N-2j}.
```

Averaging with (13) proves that the qubit optimum is exactly (1). The pointwise sector optimization is the one in [BLMO2023](../references/RELATED_WORK.md#BLMO2023), Section 5.2, Eqs. (5.5) through (5.7). Their published majority theorem is stated for odd $`N`$. The derivation here applies their covariant-channel characterization also to even $`N`$: spins may be integers or half-integers, and strict majority guarantees $`J\ge z>0`$ in either case. No tie sector occurs in the support.

### 7.3 Embedding the qubit hard family in dimension $`d`$

Fix an isometry $`V:\mathbb C^2\to\mathbb C^d`$ and let $`P=VV^\dagger`$. Every embedded qubit hard input is an allowed $`d`$-dimensional input, since its faulty vector is orthogonal to its target.

Given any $`d`$-dimensional output channel $`\Lambda_d`$, construct a qubit channel by embedding each input with $`V`$, applying $`\Lambda_d`$, and using the output map

```math
\mathcal R_V(Y)
=V^\dagger YV+\operatorname{Tr}((I-P)Y)\,\tau,
```

where $`\tau`$ is any fixed qubit density operator. This map is CPTP: it preserves the component in the embedded qubit subspace and replaces the probability outside that subspace by $`\tau`$.

For every target qubit $`|u\rangle`$ and output $`Y`$,

```math
\langle u|\mathcal R_V(Y)|u\rangle
=\langle Vu|Y|Vu\rangle
+\operatorname{Tr}((I-P)Y)\langle u|\tau|u\rangle
\ge\langle Vu|Y|Vu\rangle.
```

Thus a $`d`$-dimensional channel with worst-case fidelity larger than $`F_N(k)`$ would give a qubit channel with the same improvement on the qubit hard family, contradicting Sections 7.1 and 7.2. Hence $`F^\star_{N,k,d}\le F_N(k)`$. Together with (12), this proves the theorem.

## 8. One channel for every fault count and the at-most promise

The recovery channel chooses its removal corner from $`\lambda`$ alone. Neither $`k`$ nor $`m`$ appears in that choice. For every strict-majority promise, the supported sectors satisfy $`\lambda_1>\lambda_2`$ by the sector-reduction theorem, so the selected corner is in the first row. The same channel $`\Phi_{N,d}`$ therefore attains (1) simultaneously for all $`0\le k<N/2`$.

To pass to an upper bound on the fault count, first show that $`\varepsilon_{N,k}`$ is nondecreasing in $`k`$. Choose a uniformly random permutation of the $`N`$ positions and declare its first $`\ell`$ positions bad. This couples uniform bad sets $`B^{(\ell)}`$ for all $`\ell`$, with

```math
B^{(\ell)}\subseteq B^{(\ell+1)}.
```

Changing the newly selected position from good to bad adds two to every subsequent partial sum. Thus

```math
M^{(\ell+1)}\ge M^{(\ell)},
\qquad
g_{\ell+1}=N-2(\ell+1)=g_\ell-2.
```

As long as both counts satisfy strict majority, their $`g`$ values are positive. The function $`x/(g+2x)`$ is increasing in $`x`$ and nonincreasing in $`g`$. Therefore, pathwise,

```math
\frac{M^{(\ell+1)}}{g_{\ell+1}+2M^{(\ell+1)}}
\ge
\frac{M^{(\ell)}}{g_\ell+2M^{(\ell)}}.
```

Taking expectations in (2) proves the required monotonicity. The at-most-$`k`$ class is the convex hull of the exact-$`\ell`$ classes for $`0\le\ell\le k`$. Linearity of fidelity and the same-channel guarantee give error at most $`\varepsilon_{N,k}`$ throughout that class. The exact-$`k`$ qubit hard family is contained in it, so the matching converse remains valid. Its optimum is therefore also $`F_N(k)`$.

## References

- [BLMO2023](../references/RELATED_WORK.md#BLMO2023): qubit quantum majority, its covariant-channel optimization, and the exact fixed-count fidelity.
- [GO2024](../references/RELATED_WORK.md#GO2024): optimization with unitary-equivariant constraints and the three-input higher-dimensional majority case.
- [SSW2026](../references/RELATED_WORK.md#SSW2026): the Clebsch–Gordan product, the overhang-defect estimate, and RSK analysis of iid purity amplification.
- [LTHC2026](../references/RELATED_WORK.md#LTHC2026): overhang-removal channels, component fidelities, and their implementation.

Full bibliographic entries are in [references.bib](../references/references.bib).
