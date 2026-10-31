# The recovery channel and its resources

The optimal recovery operation is a known unitary-covariant channel. Its definition does not require the target state or the number of faults. The theorem in [the model](model.md) concerns what this operation achieves on correlated orthogonal-contamination inputs.

## 1. Schur sectors

Schur–Weyl duality decomposes the input block as

```math
(\mathbb C^d)^{\otimes N}
\cong
\bigoplus_{\substack{\lambda\vdash N\\ \ell(\lambda)\le d}}
Q_\lambda^{(d)}\otimes V_\lambda.
```

Here $`Q_\lambda^{(d)}`$ is the polynomial irreducible representation of $`U(d)`$ and $`V_\lambda`$ is the Specht representation of $`S_N`$. Write $`f^\lambda=\dim V_\lambda`$. A partition is padded with zeros when its indices exceed its length.

The channel first measures the partition $`\lambda`$ and discards the permutation multiplicity space $`V_\lambda`$. Both actions are independent of the unknown basis. For every partition, define

```math
c(\lambda)=\max\{i:\lambda_i=\lambda_1\},
\qquad
\mu(\lambda)=\lambda-e_{c(\lambda)}.
```

This removes the corner at the bottom of the block of equally long first rows. It is the first-eigenstate, single-output specialization of the overhang rule in [LTHC2026](../references/RELATED_WORK.md#LTHC2026), Definition 2, Eq. (10). The resulting $`\mu(\lambda)`$ is a valid partition of $`N-1`$ for every $`N\ge1`$.

For every sector that occurs under a strict-majority promise,

```math
\lambda_1\ge m>k\ge\lambda_2.
```

The [sector reduction](sector-reduction.md) proves this support condition. Consequently $`c(\lambda)=1`$ and $`\mu(\lambda)=\lambda-e_1`$ on all admissible inputs. The fundamental Pieri rule gives a multiplicity-one isometric intertwiner

```math
J_\lambda:
Q_\lambda^{(d)}
\longrightarrow
Q_{\mu(\lambda)}^{(d)}\otimes\mathbb C^d.
```

Its phase is irrelevant to the induced channel. Apply $`J_\lambda`$ and discard its first output factor. The remaining fundamental representation is the recovered register:

```math
\Phi_\lambda(X)
=\mathrm{Tr}_{Q_{\mu(\lambda)}^{(d)}}
\left(J_\lambda XJ_\lambda^\dagger\right).
```

Combining the measured sectors defines $`\Phi_{N,d}`$ on the entire input space, including tied sectors. Keeping the cited overhang rule on those unused sectors makes the global channel and its implementation-precision statement unambiguous.

The resulting channel is invariant under input permutations and covariant under a common unitary:

```math
\Phi_{N,d}(U_\pi XU_\pi^\dagger)=\Phi_{N,d}(X),
\qquad
\Phi_{N,d}(U^{\otimes N}X(U^\dagger)^{\otimes N})
=U\Phi_{N,d}(X)U^\dagger.
```

The construction is the single-output, first-row-removal specialization of the channels used in [SSW2026](../references/RELATED_WORK.md#SSW2026) and [LTHC2026](../references/RELATED_WORK.md#LTHC2026). This repository does not claim a new collective circuit.

## 2. Exact component fidelity

For analysis, set $`\psi=|d\rangle`$. This choice uses covariance; it is not a basis change the processor must learn or implement. Restrict $`Q_\lambda^{(d)}`$ to the stabilizer $`U(d-1)`$ acting on $`\psi^\perp`$. The sector with $`m`$ target occupations branches into partitions $`\nu\vdash k`$ with

```math
\lambda_1\ge\nu_1\ge\lambda_2\ge\nu_2
\ge\cdots\ge\lambda_d\ge\nu_d=0.
```

Equivalently, $`\lambda/\nu`$ is a horizontal strip with $`m`$ boxes. Branching is multiplicity free. The effect $`\Phi_\lambda^\ast(P_\psi)`$ commutes with the stabilizer, so its expectation is constant on each irreducible $`\nu`$ block. The inherited Clebsch–Gordan formula is

```math
a_{\lambda,\nu}
=
\prod_{j=1}^{d-1}
\frac{\lambda_1-\nu_j+j-1}
{\lambda_1-\lambda_{j+1}+j-1}.
```

This is a component identity, not an iid averaging assertion. See [SSW2026](../references/RELATED_WORK.md#SSW2026), Lemma 3.1, Eq. (19), with one output, and [LTHC2026](../references/RELATED_WORK.md#LTHC2026), Theorem 4, Eq. (33). Their state models do not have to be imposed on this representation identity.

Set

```math
r=\lambda_1-m,\qquad
b_j=\nu_j-\lambda_{j+1},\qquad
D_j=\lambda_1-\lambda_{j+1}+j-1.
```

Interlacing gives $`b_j\ge0`$, and

```math
\sum_{j=1}^{d-1}b_j
=k-(N-\lambda_1)=r,
\qquad
D_j\ge\lambda_1-\lambda_2.
```

The factors lie between zero and one. Therefore

```math
1-a_{\lambda,\nu}
\le\sum_j\frac{b_j}{D_j}
\le\frac{r}{\lambda_1-\lambda_2}
\le\frac{r}{g+2r}.
```

The final step uses $`\lambda_2\le N-\lambda_1=k-r`$. This bound is an immediate specialization of the established component analysis, in particular Eq. (24) and the first-row defect identity in SSW2026. The new task is to average it sharply over every possible faulty sector. That is done in [the minimax proof](minimax-proof.md), without an iid input assumption.

## 3. A target-independent circuit

A formal Schur basis is not by itself a low-cost physical implementation. LTHC2026, Supplement Theorem S3.2, supplies an implementation using generalized quantum phase estimation for the permutation action. Its operations are:

1. Resolve the Schur label and permutation representation with generalized quantum phase estimation.
2. Measure the label and prepare the appropriate Specht resource state.
3. Apply the inverse transform and discard the environment registers.

The resource-state preparation is included in their Lemma S3.1 and in the gate count. It is not supplied as a free oracle.

The construction implements a channel on an arbitrary input block. The iid assumption in the accompanying correctness bound controls the probability of a representation-sector failure event. For first-eigenstate, single-output extraction, that event is $`\lambda_1\lt 1`$, which is impossible for every partition of $`N\ge1`$. The rule $`\mu(\lambda)`$ above therefore inherits the global implementation guarantee. On admissible inputs it always reduces to first-row removal, so the component analysis in Section 2 applies.

This is a transfer of an existing channel implementation to a new input class. It uses the representation-sector action and its norm approximation, not an inference that an iid fidelity bound automatically holds for correlated inputs.

## 4. Charged resources

Let $`\delta>0`$ denote an implementation precision. The cited construction gives a channel approximation with diamond-norm error at most $`\delta`$ using

```math
T
=O\!\left(
N^4\log^q\!\frac{dN}{\delta}
\right),
\qquad q\approx1.44,
```

one- and two-qubit gates from a universal gate set. The exponent comes from the cited synthesis method; this is an upper bound, not a claim of optimal gate complexity. The normalization and complexity are taken from LTHC2026, Theorem S3.2, Eqs. (S73)–(S75).

| Resource | What is charged |
|---|---|
| Supplied states | $`N`$ input registers, with preparation cost paid for each |
| Data register | $`N\lceil\log_2d\rceil`$ qubits for the collective input block |
| Gates | The bound $`T`$ above, including representation-resource preparation |
| Auxiliary workspace | Finite working registers for the transforms, control and resource state; a conservative bound is $`O(N\log d+T)`$ total qubits |
| Accuracy | Ideal risk $`\varepsilon_{N,k}`$ plus a separate implementation allowance |
| State-dependent access | None: no target projector, preparation inverse, QRAM or classical target description |

The conservative workspace bound follows by allocating the data wires and the finitely many additional wires touched by the gate sequence. It is not an optimized space bound. The theorem does not assert that all copies can be processed with constant quantum memory.

If $`\|\widetilde\Phi_{N,d}-\Phi_{N,d}\|_\diamond\le\delta`$, then the difference between the two output density operators has trace norm at most $`\delta`$. Since it is traceless, the target overlap changes by at most $`\delta/2`$. In particular, the conservative guarantee

```math
\langle\psi|\widetilde\Phi_{N,d}(\rho)|\psi\rangle
\ge F_N(k)-\delta
```

always holds. With half-trace-distance input uncertainty $`\eta`$ as in [the model](model.md), a sharper combined bound is $`F_N(k)-\eta-\delta/2`$.

For a fixed faulty fraction $`k/N\to p\in(0,1/2)`$, achieving total infidelity $`\epsilon`$ is possible with $`N=O(\epsilon^{-1})`$ and $`\delta=O(\epsilon)`$. Substitution yields

```math
T=O\!\left(
\epsilon^{-4}\log^q\!\frac{d}{\epsilon}
\right)
```

for the inherited construction, with constants depending on the promised majority fraction. The exact ideal minimax converse establishes the corresponding $`\Theta(\epsilon^{-1})`$ copy requirement. It does not establish a matching gate or workspace lower bound.

## 5. Operational meaning

The task preserves quantum output. Measuring each register to estimate a classical description and preparing a new state is an allowed competing strategy, but the minimax optimization does not restrict processors to such strategies. The collective channel extracts one register while discarding the rest.

All stabilizer twirls and the choice $`\psi=|d\rangle`$ used in the proof are analytical reductions. They do not add an uncharged operation depending on the unknown target. The physical channel is fixed by $`N`$ and $`d`$, and its circuit precision can be chosen independently of the hidden input.
