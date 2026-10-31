# Reduction to an exact conditional Schur law

The faulty registers may contain an arbitrary entangled state. The reduction below shows why their effect on the recovery fidelity can nevertheless be analyzed one bad Schur sector at a time. It also identifies the conditional state after Schur sampling, not only the probability of its label.

The input promise is specified in [model.md](model.md). The channel $`\Phi_{N,d}`$ and its branch fidelity are specified in [recovery-channel.md](recovery-channel.md). The conditional law proved here is used in [minimax-proof.md](minimax-proof.md). The twirls are used only to evaluate fidelity; the physical operation is the target-independent recovery channel.

## 1. Spaces, partitions, and symmetries

Let $`\mathcal H=\mathbb C^d`$, let $`|\psi\rangle\in\mathcal H`$ be a unit vector, and write

```math
P_\psi=|\psi\rangle\langle\psi|,
\qquad
\mathcal L=\mathrm{span}\,\{|\psi\rangle\},
\qquad
\mathcal K=\mathcal L^\perp.
```

Fix integers $`N=m+k`$ with $`m>k\ge0`$, and put $`g=m-k`$. Initially take the good positions to be $`G_0=\{1,\ldots,m\}`$. Their complement is $`B_0`$. The input is

```math
\rho_{\psi,\omega}
=P_\psi^{\otimes m}\otimes\omega,
\qquad
\omega\in\mathsf D(\mathcal K^{\otimes k}).
```

Here $`\mathsf D(\mathcal V)`$ denotes the density operators on $`\mathcal V`$. No product or commutativity condition is imposed on $`\omega`$. Other good-position sets are obtained by permuting the registers.

For a partition $`\lambda\vdash N`$, let $`V_\lambda`$ be the Specht module of $`S_N`$ and let $`f^\lambda=\dim V_\lambda`$. Let $`Q_\lambda^{(d)}`$ be the polynomial irreducible representation of $`U(d)`$ with highest weight $`\lambda`$. We use the Schur decomposition in the order

```math
\mathcal H^{\otimes N}
\cong
\bigoplus_{\substack{\lambda\vdash N\\\ell(\lambda)\le d}}
Q_\lambda^{(d)}\otimes V_\lambda.
```

Partitions are padded with zeros when indexed beyond their length. The notation $`\lambda/\nu`$ is a *horizontal $`m`$-strip* means that $`\nu\subseteq\lambda`$, the difference has $`m`$ boxes, and no two of these boxes occupy the same column. With $`\nu`$ padded to length $`d-1`$, this is equivalent to

```math
\lambda_1\ge\nu_1\ge\lambda_2\ge\nu_2
\ge\cdots\ge\lambda_{d-1}\ge\nu_{d-1}\ge\lambda_d\ge0,
\qquad
|\lambda|-|\nu|=m.
```

Write $`U_\pi`$ for the action of a register permutation $`\pi\in S_N`$. The recovery channel has the two properties

```math
\Phi_{N,d}(U_\pi XU_\pi^\dagger)=\Phi_{N,d}(X),
```

```math
\Phi_{N,d}(U^{\otimes N}X(U^\dagger)^{\otimes N})
=U\Phi_{N,d}(X)U^\dagger,
\qquad U\in U(d).
```

These properties imply that its target fidelity

```math
\mathcal F_\psi(X)
=\langle\psi|\Phi_{N,d}(X)|\psi\rangle
```

is unchanged by register permutations and by simultaneous unitaries that fix $`P_\psi`$. The symmetry reduction and Schur-channel framework are established tools in [BLMO2023](../references/RELATED_WORK.md#BLMO2023), [GO2024](../references/RELATED_WORK.md#GO2024), and [LTHC2026](../references/RELATED_WORK.md#LTHC2026).

## 2. Twirling the faulty subsystem

Identify $`\mathcal K`$ with $`\mathbb C^{d-1}`$. For $`U\in U(d-1)`$, extend its action to $`\mathcal H`$ as $`\widetilde U=I_{\mathcal L}\oplus U`$. Acting with $`\widetilde U^{\otimes N}`$ leaves the good registers fixed and applies $`U^{\otimes k}`$ to the faulty subsystem. Permutations in $`S_k`$ acting on $`B_0`$ are also register permutations in $`S_N`$. Consequently

```math
\mathcal F_\psi(P_\psi^{\otimes m}\otimes\omega)
=\mathcal F_\psi(P_\psi^{\otimes m}\otimes\mathcal T_{\rm bad}(\omega)),
```

where the normalized twirl is

```math
\mathcal T_{\rm bad}(\omega)
=\frac1{k!}\sum_{\tau\in S_k}\int_{U(d-1)}
U^{\otimes k}U_\tau\omega U_\tau^\dagger(U^\dagger)^{\otimes k}
\,dU.
```

Schur duality on $`\mathcal K^{\otimes k}`$ gives

```math
\mathcal K^{\otimes k}
\cong
\bigoplus_{\substack{\nu\vdash k\\\ell(\nu)\le d-1}}
Q_\nu^{(d-1)}\otimes V_\nu.
```

Put $`D_\nu=\dim Q_\nu^{(d-1)}`$ and let $`P_\nu^{\mathcal K}`$ be the orthogonal projector onto the corresponding summand. The permutation twirl removes coherence between different $`\nu`$ and makes each $`V_\nu`$ factor maximally mixed. The unitary twirl then makes its $`Q_\nu^{(d-1)}`$ factor maximally mixed. Thus

```math
\begin{aligned}
\mathcal T_{\rm bad}(\omega)
&=\sum_\nu q_\nu\,\omega_\nu,\\
q_\nu&=\mathrm{Tr}(P_\nu^{\mathcal K}\omega),\\
\omega_\nu&=\frac{P_\nu^{\mathcal K}}{D_\nu f^\nu}.
\end{aligned}
\tag{1}
```

The weights satisfy $`q_\nu\ge0`$ and $`\sum_\nu q_\nu=1`$. Equation (1) is a consequence of Schur's lemma for the commuting $`U(d-1)`$ and $`S_k`$ actions. It applies to an arbitrary density operator $`\omega`$, including one with entanglement among all faulty registers.

For $`k=0`$, use the empty partition, $`D_\varnothing=f^\varnothing=1`$, and the one-dimensional empty tensor product. All formulas below retain their meaning.

## 3. Averaging placements gives an induced representation

Fix a bad partition $`\nu`$. Set

```math
\rho_\nu^0=P_\psi^{\otimes m}\otimes\omega_\nu,
\qquad
P_\nu^0=P_\psi^{\otimes m}\otimes P_\nu^{\mathcal K},
```

so that $`\rho_\nu^0=P_\nu^0/(D_\nu f^\nu)`$. Let $`H=S_m\times S_k\le S_N`$ be the subgroup preserving $`G_0`$ and $`B_0`$. The state $`\rho_\nu^0`$ is invariant under $`H`$.

For each $`m`$-element set $`G\subseteq[N]`$, choose a permutation $`t_G`$ with $`t_G(G_0)=G`$. Invariance under $`H`$ makes $`U_{t_G}P_\nu^0U_{t_G}^\dagger`$ independent of the chosen representative. Therefore the full permutation average is

```math
\begin{aligned}
\overline\rho_\nu
&=\frac1{N!}\sum_{\pi\in S_N}U_\pi\rho_\nu^0U_\pi^\dagger\\
&=\frac1{\binom Nm D_\nu f^\nu}
\sum_{|G|=m}U_{t_G}P_\nu^0U_{t_G}^\dagger.
\end{aligned}
\tag{2}
```

The summands in the last numerator are mutually orthogonal projectors. To see this, each is supported on the placement space

```math
\mathcal E_G
=\bigotimes_{i=1}^N\mathcal H_i(G),
\qquad
\mathcal H_i(G)=
\begin{cases}
\mathcal L,&i\in G,\\
\mathcal K,&i\notin G.
\end{cases}
```

If $`G\ne G'`$, some register belongs to one good set and not the other. Its two factors are $`\mathcal L`$ and $`\mathcal K`$, which are orthogonal. Hence $`\mathcal E_G\perp\mathcal E_{G'}`$.

Let $`\mathcal S_\nu`$ be the direct sum of the ranges of the projectors in (2). Its dimension is $`\binom Nm D_\nu f^\nu`$, and (2) is exactly the normalized identity on $`\mathcal S_\nu`$.

As a representation of $`U(d-1)\times S_N`$, this space is

```math
\begin{aligned}
\mathcal S_\nu
&\cong
Q_\nu^{(d-1)}\otimes
\mathrm{Ind}_{S_m\times S_k}^{S_N}\,
(\mathbf1\otimes V_\nu).
\end{aligned}
\tag{3}
```

An explicit identification is obtained by placing a vector $`q\otimes v\in Q_\nu^{(d-1)}\otimes V_\nu`$ into $`B_0`$, adjoining $`|\psi\rangle^{\otimes m}`$, and applying the coset representative $`t_G`$. Changing that representative by an element of $`S_m\times S_k`$ produces precisely the equivalence relation in the induced module: $`S_m`$ acts trivially and $`S_k`$ acts on $`V_\nu`$. Distinct cosets give orthogonal placement spaces, so this identification preserves inner products. The simultaneous $`U(d-1)`$ action commutes with all register permutations and acts on the common factor $`Q_\nu^{(d-1)}`$.

Pieri's rule now gives the multiplicity-free decomposition

```math
\begin{aligned}
\mathrm{Ind}_{S_m\times S_k}^{S_N}\,
(\mathbf1\otimes V_\nu)
&\cong
\bigoplus_{\lambda:\,\lambda/\nu\text{ horizontal }m\text{-strip}}
V_\lambda.
\end{aligned}
\tag{4}
```

Every partition occurring here has at most $`\ell(\nu)+1\le d`$ rows, so all of these summands occur in $`\mathcal H^{\otimes N}`$.

## 4. The conditional law and conditional state

The multiplicity-free branching rule for $`U(d)\downarrow U(d-1)`$ places a copy of $`Q_\nu^{(d-1)}`$ inside $`Q_\lambda^{(d)}`$ precisely when $`\lambda/\nu`$ is horizontal. Denote this branching subspace by $`\mathcal W_{\lambda,\nu}`$ and its projector by $`\Pi_{\lambda,\nu}`$. In the present case it has exactly $`m=|\lambda|-|\nu|`$ occupations of the distinguished vector $`|\psi\rangle`$. Its dimension is $`D_\nu`$.

Combining (2), (3), and (4), the normalized state has the following exact expression in Schur coordinates:

```math
\overline\rho_\nu
\cong
\bigoplus_{\lambda:\,\lambda/\nu\text{ horizontal }m\text{-strip}}
p(\lambda\mid\nu)
\left(
\frac{\Pi_{\lambda,\nu}}{D_\nu}
\otimes
\frac{I_{V_\lambda}}{f^\lambda}
\right),
```

```math
\boxed{
p(\lambda\mid\nu)
=\frac{f^\lambda}{\binom Nm f^\nu}
\quad\text{if }\lambda/\nu\text{ is a horizontal }m\text{-strip},
}
\tag{5}
```

with zero probability otherwise. In particular,

```math
\begin{aligned}
\sum_{\lambda:\,\lambda/\nu\text{ horizontal }m\text{-strip}}
f^\lambda
&=\binom Nm f^\nu.
\end{aligned}
\tag{6}
```

Equation (6) is also the dimension identity for (4). The factor $`D_\nu`$ cancels between the dimension of a Schur block and the total dimension. This explains why the conditional probability in (5) does not depend on $`d`$, apart from the admissibility condition $`\ell(\nu)\le d-1`$.

Conditioned on $`\lambda`$, the Weyl-module input to the recovery channel is $`\Pi_{\lambda,\nu}/D_\nu`$. The fidelity effect of the branch channel commutes with $`U(d-1)`$. Schur's lemma makes it a scalar on the irreducible space $`\mathcal W_{\lambda,\nu}`$. Thus its target overlap is the same on every unit vector in that branching space, and equals the component $`a_{\lambda,\nu}`$ in [recovery-channel.md](recovery-channel.md). There is no further average over an unknown spectrum.

Consequently the fidelity for the original arbitrary fault state has the exact reduction

```math
\begin{aligned}
\mathcal F_\psi(\rho_{\psi,\omega})
&=\sum_\nu q_\nu
\sum_\lambda p(\lambda\mid\nu)\,a_{\lambda,\nu}.
\end{aligned}
\tag{7}
```

Both twirls preserve this scalar fidelity. Equation (7) does not assert that the original input equals its twirl.

### Independent character verification

The probability in (5) can also be checked directly, without counting the dimensions in (3). The central projector onto the $`\lambda`$ Schur sector is

```math
P_\lambda
=\frac{f^\lambda}{N!}
\sum_{\pi\in S_N}\chi_\lambda(\pi^{-1})U_\pi.
```

If $`\pi\notin H`$, then $`U_\pi`$ maps $`\mathcal E_{G_0}`$ to an orthogonal placement space. Hence $`\mathrm{Tr}(\rho_\nu^0U_\pi)=0`$. If $`\pi=(\sigma,\tau)\in S_m\times S_k`$, then

```math
\mathrm{Tr}(\rho_\nu^0U_{(\sigma,\tau)})
=\frac{\chi_\nu(\tau)}{f^\nu}.
```

Characters of symmetric groups are real. Character orthogonality and Frobenius reciprocity therefore give

```math
\begin{aligned}
\mathrm{Tr}(P_\lambda\rho_\nu^0)
&=\frac{f^\lambda}{N!f^\nu}
\sum_{(\sigma,\tau)\in S_m\times S_k}
\chi_\lambda((\sigma,\tau)^{-1})\chi_\nu(\tau)\\
&=\frac{f^\lambda m!k!}{N!f^\nu}
\left\langle
\mathrm{Res}_{S_m\times S_k}^{S_N}\,\chi_\lambda,
\mathbf1\otimes\chi_\nu
\right\rangle\\
&=\frac{f^\lambda}{\binom Nm f^\nu}\,c^\lambda_{(m),\nu}.
\end{aligned}
```

Pieri's rule states that $`c^\lambda_{(m),\nu}`$ is one for a horizontal $`m`$-strip and zero otherwise. This reproduces (5), including its normalization factors.

## 5. Supported sectors have a strict first-row gap

For a supported pair $`(\lambda,\nu)`$, interlacing gives

```math
k=\sum_{i=1}^{d-1}\nu_i
\ge\sum_{i=1}^{d-1}\lambda_{i+1}
=N-\lambda_1.
```

Thus $`\lambda_1\ge m`$. Define $`r=\lambda_1-m`$. Then

```math
\begin{aligned}
&0\le r\le k,\\
&\lambda_2\le N-\lambda_1=k-r,\\
&\boxed{\lambda_1-\lambda_2\ge g+2r>0.}
\end{aligned}
\tag{8}
```

The first-row removal used by $`\Phi_{N,d}`$ is therefore valid on every sector that can occur under the promise. This conclusion holds for each bad partition separately and requires no concentration estimate.

## References and scope

The representation-theoretic facts used here are Schur duality, multiplicity-free unitary branching, Frobenius reciprocity, and Pieri's rule. The inherited quantum-channel framework and the surrounding majority and purification results are documented in [BLMO2023](../references/RELATED_WORK.md#BLMO2023), [GO2024](../references/RELATED_WORK.md#GO2024), [SSW2026](../references/RELATED_WORK.md#SSW2026), and [LTHC2026](../references/RELATED_WORK.md#LTHC2026). Full bibliographic entries are in [references.bib](../references/references.bib).

The reduction proved in this file concerns a fixed pure good subsystem and arbitrary orthogonal faults, together with their convex mixtures. Orthogonality of the placement spaces is essential to (2). Coherent superpositions of different placement spaces are treated separately in [accuracy-and-boundaries.md](accuracy-and-boundaries.md).
