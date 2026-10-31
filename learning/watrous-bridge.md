# From quantum channels to majority recovery

The recovery problem asks for a quantum output. A collection of $`N`$ registers contains more than half exact copies of an unknown pure state $`|\psi\rangle`$. The remaining registers have support orthogonal to it and may be entangled with one another. Their locations are unknown. One collective operation must return a register close to $`|\psi\rangle`$, without receiving a description of the state or the good locations.

The exact guarantee is stronger than a dimension-independent scaling law: for every register dimension $`d\ge2`$, the optimal worst-case fidelity equals the known qubit value. Understanding this statement requires three connections. A channel formalizes what the processor can do; symmetry organizes the input without learning its unknown basis; and a counting argument shows why every allowed faulty state is bounded by the same binary example.

The educational anchor is John Watrous, *The Theory of Quantum Information* (Cambridge University Press, 2018). The [author's book page](https://cs.uwaterloo.ca/~watrous/TQI/) provides a prepublication manuscript and individual chapters. This bridge uses that one anchor and supplies the additional representation and combinatorial steps needed for the project. The [30 milestones](milestones.md) organize the background and the complete argument into understanding targets. The exact statements and proofs remain in the [scientific account](../science/model.md).

<a id="reading-route"></a>

## 1. A route through the anchor

Page numbers below are the printed page numbers in the author's manuscript. PDF viewers may number the individual chapter files differently.

| Watrous reading | Connection to the recovery problem |
|---|---|
| [§2.1, Registers and states, p. 58; §2.1.3, Reductions and purifications, p. 67](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf) | A register is a quantum system, and its density operator describes both classical mixing and quantum correlations. A pure good marginal imposes a stronger constraint than a large target occupation probability. |
| [§2.2, Quantum channels, p. 72; §2.2.2, Representations of channels, p. 77](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf) | The allowed processor is a deterministic channel. Corollary 2.27, p. 89, relates this definition to an isometry followed by discarding an environment, which is how the extraction step is defined. |
| [§3.2, The fidelity function, p. 139](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf) | Definition 3.11, Eq. (3.64), uses root fidelity. For a pure target, its square is the overlap optimized in this repository. |
| [§7.1, Permutation-invariant vectors and operators, p. 390; §7.1.2, The algebra of permutation-invariant operators, p. 400](https://cs.uwaterloo.ca/~watrous/TQI/TQI.7.pdf) | Permuting inputs and rotating their common basis are distinct symmetries. Theorem 7.15, p. 407, relates their commutants. Mixed Schur sectors, introduced below, resolve both actions. |
| [§7.2, Unitarily invariant probability measures; §7.2.1, Uniform spherical measure and Haar measure, p. 408](https://cs.uwaterloo.ca/~watrous/TQI/TQI.7.pdf) | Haar averaging makes a symmetry reduction precise. Proposition 7.20, p. 413, supplies the invariance behind the twirls used in the proof. |

The route is selective. The book supplies the operational foundation and symmetry language. The conditional Pieri law, the fixed-tableau RSK coupling, and the majority converse are supplied by the project and its cited research sources below.

<a id="states-and-faults"></a>

## 2. From registers to the fault promise

Let $`H=\mathbb C^d`$ be the state space of one register. A density operator is positive semidefinite and has trace one. The target is the rank-one projector $`P_\psi=|\psi\rangle\langle\psi|`$. For a fixed choice of good positions, the joint input has the form

```math
P_\psi^{\otimes m}\otimes\omega,
\qquad
N=m+k,\quad m>k,\quad
\omega\in\mathsf D((\psi^\perp)^{\otimes k}).
```

The tensor product in the space $`(\psi^\perp)^{\otimes k}`$ does not require $`\omega`$ to be a product state. It can contain arbitrary correlations and entanglement among the faulty registers. The support condition says that each faulty register belongs entirely to the subspace perpendicular to the target.

The good block factors from the rest because its marginals are pure. To see the constraint, suppose a joint state has marginal $`P_\psi`$ on its first register. Its weight on the complementary projector $`I-P_\psi`$ is zero. Positivity then excludes both support in that complementary subspace and cross terms connecting to it. The joint state must be $`P_\psi\otimes\sigma`$. Repeating this reasoning gives the good tensor factor above. An entangled state can have high overlap with $`P_\psi`$ in each marginal without satisfying this exact factorization.

Unknown positions are included by applying a permutation $`U_\pi`$ to the tensor factors. Classical uncertainty about positions and faulty states gives the admissible set

```math
\mathcal A_{\psi,N,k}
=\mathrm{conv}\left\{
U_\pi(P_\psi^{\otimes m}\otimes\omega)U_\pi^\dagger:
\pi\in S_N,\quad
\omega\in\mathsf D((\psi^\perp)^{\otimes k})
\right\}.
```

Every component uses the same target $`\psi`$. The mixture can correlate the chosen positions with the faulty state. The guarantee must hold for every such mixture, every $`\omega`$, and every unknown target. The channel receives only the quantum registers and the known parameters $`N,d`$.

This is a useful point to distinguish a mixture from a coherent superposition. A mixture averages density operators with ordinary nonnegative probabilities. A coherent superposition also has off-diagonal terms connecting configurations. Those terms can change the weights of the symmetry sectors and are excluded by the displayed input class. The [boundary example below](#boundaries-and-attribution) shows why that distinction affects the attainable fidelity.

<a id="channels-and-discarding"></a>

## 3. From channel representations to an extraction operation

A physical processor that always returns an output is a completely positive trace-preserving map

```math
\Phi:\mathsf L(H^{\otimes N})\longrightarrow\mathsf L(H).
```

Complete positivity ensures that the map remains valid when the input is correlated with an untouched system. Trace preservation accounts for every outcome. Measurements and outcome-dependent operations can occur inside the processor, but its final fidelity includes all branches.

Watrous's channel representations make this operational. An isometry $`A`$ can embed an input into an output register and an environment, after which the environment is discarded:

```math
\Phi(X)=\mathrm{Tr}_{E}(AXA^\dagger),
\qquad A^\dagger A=I.
```

The partial trace does not condition on a favorable outcome. It records what remains accessible when the environment is no longer available. The recovery channel uses precisely this form within each measured symmetry sector. A representation-theoretic isometry separates one physical $`d`$-dimensional output factor from a remaining factor; tracing out the latter produces the recovered state.

The output can still carry an unknown quantum state. The processor is not required to estimate a classical description of $`\psi`$. This distinction matters because a channel can rearrange and discard quantum information without resolving the unknown basis into classical data.

The word *purification* has two relevant uses. In Watrous §2.1.3, a purification is a pure state on a larger system whose reduced state is the given mixed state. In purity amplification, a channel consumes several input registers to improve the state of a retained output. The existence of a mathematical purification of an input does not supply that larger pure state to the recovery processor.

The channel optimization is convex. Mixing two allowed processors gives another processor, and target overlap is linear in the output state. These facts permit symmetry averaging in the converse. They do not imply that each branch of a measurement must have the same fidelity.

<a id="fidelity-convention"></a>

## 4. Translating notation and fidelity

| Watrous notation or convention | Convention used here |
|---|---|
| A complex Euclidean space such as $`\mathcal X`$ | The register space $`H=\mathbb C^d`$ |
| $`uu^\ast`$ for a pure state | $`P_\psi=\lvert\psi\rangle\langle\psi\rvert`$ |
| $`A^\ast`$ for the adjoint | $`A^\dagger`$ |
| A permutation operator $`W_\pi`$ in Chapter 7 | $`U_\pi`$ on input tensor factors |
| Root fidelity $`F(P,Q)=\lVert\sqrt P\sqrt Q\rVert_1`$ | Pure-target overlap $`\langle\psi\rvert\rho_{\mathrm{out}}\lvert\psi\rangle`$ |

For a pure target the conversion is exact:

```math
F_{\mathrm W}(P_\psi,\rho_{\mathrm{out}})
=\sqrt{\langle\psi|\rho_{\mathrm{out}}|\psi\rangle}.
```

The subscript on $`F_{\mathrm W}`$ here only distinguishes Watrous's convention. The repository uses $`F_{\mathrm W}^2`$ as its per-input fidelity score; $`F_N(k)`$ is the optimal worst-case value of that score. Its infidelity is $`\varepsilon_{N,k}=1-F_N(k)`$.

Overlap also has a direct operational interpretation: it is the probability that a hypothetical two-outcome measurement with acceptance effect $`P_\psi`$ accepts the output. This defines a quality criterion. It does not give the processor access to that unknown projector.

For the three-register example, the overlap is $`8/9`$, the root fidelity is $`2\sqrt2/3`$, and the infidelity in this repository is $`1/9`$. Keeping the convention fixed prevents a change in the claimed finite-sample error.

<a id="symmetry-and-twirling"></a>

## 5. What symmetry allows the proof to forget

The recovery channel $`\Phi_{N,d}`$ has two symmetries:

```math
\Phi_{N,d}(U_\pi XU_\pi^\dagger)=\Phi_{N,d}(X),
```

```math
\Phi_{N,d}(U^{\otimes N}X(U^\dagger)^{\otimes N})
=U\Phi_{N,d}(X)U^\dagger.
```

The first says that input labels do not matter. The second says that rotating every input by a common unitary rotates the output by that same unitary. Thus the operation treats every unknown target direction consistently.

These identities allow fidelity to be evaluated after analytical averaging. Permutations can average the placements. Unitaries that fix $`\psi`$ and rotate $`\psi^\perp`$ can average the internal orientation of the faulty state. Neither average changes the target overlap of this channel. The latter group is a copy of $`U(d-1)`$, and its normalized invariant average is the Haar twirl explained by Watrous §7.2.

The twirls are used only to evaluate fidelity; the physical operation is the target-independent recovery channel. In particular, choosing coordinates in which $`\psi=|d\rangle`$ does not mean that the processor knows or implements that coordinate change.

One must also distinguish permutation-invariant operators from the symmetric subspace. A density operator can commute with every permutation while having weight in several symmetry sectors. The symmetric subspace contains vectors fixed by every permutation and is only one sector. Averaging an input over permutations does not project it into that subspace. Watrous §7.1 treats both types of invariance; the distinction is essential for the example and the general proof.

<a id="mixed-schur-bridge"></a>

## 6. The mixed Schur sectors needed beyond the anchor

A partition $`\lambda=(\lambda_1,\lambda_2,\ldots)`$ of $`N`$ is a nonincreasing sequence of nonnegative integers summing to $`N`$. Draw it as left-justified rows of boxes. Schur–Weyl duality decomposes the input space as

```math
H^{\otimes N}
\cong
\bigoplus_{\substack{\lambda\vdash N\\\ell(\lambda)\le d}}
Q_\lambda^{(d)}\otimes V_\lambda.
```

The two factors have different jobs. A common basis rotation acts on $`Q_\lambda^{(d)}`$, the unitary-group representation. Permutations act on $`V_\lambda`$, the symmetric-group representation. Write $`f^\lambda=\dim V_\lambda`$. This is a Specht dimension, not the dimension of $`Q_\lambda^{(d)}`$. The distinction explains which dimensions later cancel.

The label $`\lambda=(N)`$ denotes the fully symmetric subspace. All other allowed shapes are also part of the decomposition. A collective measurement of $`\lambda`$ learns a symmetry type while leaving quantum information about the common basis in $`Q_\lambda^{(d)}`$.

The recovery channel measures this label, discards $`V_\lambda`$, and then extracts an output from $`Q_\lambda^{(d)}`$. On the promised inputs,

```math
\lambda_1\ge m>k\ge\lambda_2.
```

Thus removing the last box of the first row leaves a valid partition. A multiplicity-one branching rule supplies an isometry

```math
J_\lambda:Q_\lambda^{(d)}
\longrightarrow
Q_{\lambda-e_1}^{(d)}\otimes\mathbb C^d.
```

The processor keeps the last factor and discards the first. This is the isometry-and-environment picture of channels, now with the environment selected by symmetry. The [channel account](../science/recovery-channel.md) gives its global definition, including sectors outside the promise, and the inherited implementation.

The faulty subsystem has its own Schur labels $`\nu\vdash k`$ under $`U(d-1)`$ and $`S_k`$. Twirling both actions replaces an arbitrary faulty density operator by a mixture of normalized identities on these blocks. Entanglement is not assumed to disappear into a mixture of identical pure tensor powers. It can change the weights of the different $`\nu`$ blocks, including blocks absent from that restricted family.

The relevant branching relation is a horizontal strip: $`\lambda/\nu`$ consists of $`m`$ added boxes, with at most one added box in each column. Equivalently, after padding with zeros,

```math
\lambda_1\ge\nu_1\ge\lambda_2\ge\nu_2
\ge\cdots\ge\lambda_d\ge\nu_d=0.
```

This relation connects the faulty symmetry type to the full input symmetry type. It is the Pieri rule needed in the proof, supplied explicitly in the [sector reduction](../science/sector-reduction.md).

<a id="three-register-example"></a>

## 7. A complete example: three inputs and one fault

Take $`N=3`$, $`m=2`$, $`k=1`$, and orthogonal unit vectors $`\psi,\phi\in\mathbb C^d`$. Start with $`|\psi\psi\phi\rangle`$. Permutation invariance lets us evaluate the channel on the equal mixture of its three placements:

```math
\rho_{\mathrm{mix}}
=\frac13\left(
|\psi\psi\phi\rangle\langle\psi\psi\phi|
+|\psi\phi\psi\rangle\langle\psi\phi\psi|
+|\phi\psi\psi\rangle\langle\phi\psi\psi|
\right).
```

The symmetric component is proportional to

```math
|D\rangle
=\frac{|\psi\psi\phi\rangle
+|\psi\phi\psi\rangle
+|\phi\psi\psi\rangle}{\sqrt3}.
```

The symmetric projector is $`\Pi_{\mathrm{sym}}=(1/6)\sum_{\pi\in S_3}U_\pi`$, as in Watrous Proposition 7.1. Acting on the initial product vector gives $`|D\rangle/\sqrt3`$, so the probability of the symmetric label $`(3)`$ is $`1/3`$. A fully antisymmetric component vanishes because two input factors are identical. The remaining label $`(2,1)`$ therefore has probability $`2/3`$.

There is only one faulty partition, $`\nu=(1)`$. The inherited component formula in the [channel account](../science/recovery-channel.md) gives

```math
a_{(3),(1)}=\frac{3-1}{3-0}=\frac23,
\qquad
a_{(2,1),(1)}=\frac{2-1}{2-1}=1.
```

For $`d>2`$, all further factors in the product formula equal one. In the symmetric branch, extraction is the usual one-register reduction of $`|D\rangle`$. In the other branch, overlap one forces the output to be exactly the pure target.

| Measured label | Probability | Conditional output | Target overlap |
|---|---:|---|---:|
| $`(3)`$ | $`1/3`$ | $`(2/3)P_\psi+(1/3)P_\phi`$ | $`2/3`$ |
| $`(2,1)`$ | $`2/3`$ | $`P_\psi`$ | $`1`$ |

Both branches are retained in the performance calculation. The unconditional output and fidelity are

```math
\rho_{\mathrm{out}}
=\frac89P_\psi+\frac19P_\phi,
\qquad
F_3(1)=\frac13\frac23+\frac23\cdot1=\frac89.
```

Returning a uniformly random input register would have overlap $`2/3`$. The collective operation improves it because the mixed-symmetry branch contains a perfectly recoverable target factor. It consumes the input block to produce one output; it does not identify and preserve a known good input position.

The same result holds for a mixed faulty state supported on $`\psi^\perp`$: decompose that density operator into pure states and use linearity of the channel and overlap. The value $`8/9`$ in arbitrary dimension was already established by [GO2024](../references/RELATED_WORK.md#GO2024). This example illustrates the mechanism rather than supplying a new three-input result.

The binary counting description is also complete here. The three placement words are $`BGG,GBG,GGB`$. Read $`B`$ as a step $`+1`$ and $`G`$ as a step $`-1`$. Their maxima, including the starting value zero, are $`1,0,0`$. With $`g=m-k=1`$, the average error is

```math
\mathbb E\frac{M}{g+2M}
=\frac13\frac{1}{1+2}=\frac19.
```

This classical calculation reproduces the two quantum branches. The next section explains why the comparison survives arbitrary faulty symmetry types.

<a id="exact-recovery-bridge"></a>

## 8. From arbitrary faults to the exact binary law

### Conditional dimensions give the quantum probability law

Fix a faulty partition $`\nu`$ after the analytical twirl. Let $`D_\nu`$ be the dimension of its $`U(d-1)`$ representation. The normalized faulty block has dimension $`D_\nu f^\nu`$.

Different good-position sets occupy orthogonal subspaces. If two sets differ, some register lies in $`\mathrm{span}\,\{\psi\}`$ for one set and in $`\psi^\perp`$ for the other. Consequently, averaging all $`\binom Nm`$ placements gives a normalized identity on a direct sum of dimension

```math
\binom Nm D_\nu f^\nu.
```

Permutations move between the placements and act within each faulty block. This is the meaning of the induced representation

```math
Q_\nu^{(d-1)}\otimes
\mathrm{Ind}_{S_m\times S_k}^{S_N}\,
(\mathbf1\otimes V_\nu).
```

The good block carries the trivial representation because permuting identical pure copies changes nothing. Pieri decomposes the induced factor into one copy of each $`V_\lambda`$ for which $`\lambda/\nu`$ is a horizontal strip. The corresponding full block has dimension $`D_\nu f^\lambda`$. Dividing this by the total dimension gives

```math
p(\lambda\mid\nu)
=\frac{f^\lambda}{\binom Nm f^\nu}.
```

The unitary-representation dimension $`D_\nu`$ cancels. This cancellation is one reason the final bound can be independent of $`d`$. The [sector reduction](../science/sector-reduction.md) also proves the conditional state: after discarding $`V_\lambda`$, it is the normalized identity on the appropriate $`U(d-1)`$ branching block inside $`Q_\lambda^{(d)}`$. That state identification is needed to apply the component formula.

### RSK supplies a classical coupling with exactly this law

The Robinson–Schensted–Knuth correspondence, in its row-insertion form for words, assigns a pair of tableaux $`(P,Q)`$ of the same shape. The insertion tableau $`P`$ has weakly increasing rows and strictly increasing columns. The recording tableau $`Q`$ contains each integer from $`1`$ to the word length once, increasing along rows and columns. There are $`f^\lambda`$ possible recording tableaux of shape $`\lambda`$. Row insertion replaces the first strictly larger entry in a row and moves that entry to the next row; it appends when there is no larger entry.

Fix one insertion tableau $`P_0`$ of shape $`\nu`$ over letters $`1,\ldots,d-1`$. Choose a recording tableau of that shape uniformly. Inverse RSK gives a word of $`k`$ smaller letters. Interleave it with $`m`$ copies of the largest letter $`d`$, choosing the $`k`$ smaller-letter positions uniformly.

The key restriction property is

```math
P(w)_{\lt d}=P(w_{\lt d}).
```

Deleting the largest letters after insertion gives the same tableau as deleting them from the word first. During row insertion, a largest letter appends to the first row. When a smaller letter bumps a largest letter, the latter appends in the next row and does not change the insertion history of the smaller letters. This explains the restriction property; the [minimax proof](../science/minimax-proof.md) gives the induction.

For each possible shape $`\lambda`$, the full insertion tableau is uniquely determined: keep $`P_0`$ and fill the added boxes with $`d`$. Strict column increase permits this exactly for a horizontal strip. Every recording tableau of that shape produces one of the sampled words. Thus exactly $`f^\lambda`$ of the $`f^\nu\binom Nk`$ equally likely choices have shape $`\lambda`$. Their shape law is precisely $`p(\lambda\mid\nu)`$.

This is a probability coupling for a measured quantum label. It does not represent an entangled faulty input as a classical mixture of word states.

### A path maximum controls the branch error

Let $`B_t`$ and $`G_t`$ count smaller and largest letters in the first $`t`$ positions. Define

```math
S_t=B_t-G_t,\qquad
M=\max_{0\le t\le N}S_t,\qquad
g=m-k>0.
```

RSK identifies $`\lambda_1`$ with the length of a longest weakly increasing subsequence. In such a subsequence, smaller letters must come before any selected largest letters. If its last selected smaller letter occurs at position $`t`$, its length is at most

```math
B_t+(m-G_t)=m+S_t\le m+M.
```

Using all largest letters also gives a subsequence of length $`m`$. Therefore the first-row excess satisfies $`0\le r=\lambda_1-m\le M`$.

The inherited extraction formula and its scalar consequence are

```math
a_{\lambda,\nu}
=\prod_{i=1}^{d-1}
\frac{\lambda_1-\nu_i+i-1}
{\lambda_1-\lambda_{i+1}+i-1},
\qquad
1-a_{\lambda,\nu}\le\frac{r}{g+2r}.
```

To see the connection, set $`b_i=\nu_i-\lambda_{i+1}\ge0`$. The total numerator deficit is $`\sum_i b_i=r`$, and every denominator is at least $`\lambda_1-\lambda_2\ge g+2r`$. Bounding one minus a product of numbers in $`[0,1]`$ by the sum of their deficits gives the displayed inequality. This component analysis is inherited from [SSW2026](../references/RELATED_WORK.md#SSW2026) and [LTHC2026](../references/RELATED_WORK.md#LTHC2026).

Since $`r/(g+2r)`$ increases with $`r`$, every faulty partition obeys

```math
\sum_\lambda p(\lambda\mid\nu)(1-a_{\lambda,\nu})
\le\mathbb E\frac{M}{g+2M}.
```

The right side depends only on the uniformly chosen positions. It is the same for every $`\nu`$, so arbitrary mixtures of faulty sectors satisfy the bound.

### Reflection gives the finite law, and the binary family attains it

The path has $`k`$ up steps and $`m`$ down steps. For $`s\ge1`$, reflect its initial segment through the first visit to height $`s`$. This bijects paths that reach $`s`$ with paths having $`k-s`$ up steps. The inverse reflects through the first visit to $`-s`$, which every path in the image must reach. Counting the paths gives

```math
\Pr(M\ge s)=\frac{\binom N{k-s}}{\binom Nk},
\qquad 1\le s\le k.
```

Taking differences of adjacent tails gives the optimal infidelity

```math
\varepsilon_{N,k}
=\sum_{r=0}^{k}
\frac{\binom N{k-r}-\binom N{k-r-1}}{\binom Nk}
\frac{r}{g+2r},
\qquad \binom N{-1}=0.
```

If every faulty register equals the same pure $`\phi\perp\psi`$, the word uses only two letters. In that case a longest increasing subsequence has exactly $`m+M`$ letters, so $`r=M`$ and $`\lambda=(m+M,k-M)`$. The component error is exactly $`M/(g+2M)`$. This family attains the bound for the constructed channel.

Attainment by one channel is not yet optimality among all channels. The matching converse comes from the qubit majority problem of [BLMO2023](../references/RELATED_WORK.md#BLMO2023). A two-dimensional subspace of any $`\mathbb C^d`$ contains the whole binary hard family. If a $`d`$-dimensional output channel improved its worst-case fidelity, project its output back into that subspace and replace any leakage with a fixed qubit state. This is a valid channel and cannot decrease overlap with a target in the subspace. It would improve the qubit optimum, a contradiction.

The [minimax proof](../science/minimax-proof.md) derives the qubit sector converse for both odd and even strict-majority input counts from the cited channel characterization; the published majority statement itself uses odd input count. Combining achievability and converse gives

```math
F^\star_{N,k,d}=F_N(k)
=\sum_{j=0}^{k}
\frac{\binom Nj-\binom N{j-1}}{\binom Nk}
\frac{N-k-j}{N-2j}.
```

The physical channel depends on $`N,d`$, without needing $`k`$. Its same worst-case value applies to an at-most-$`k`$ promise: increasing the number of faults can only increase the binary maximum and reduce the positive majority margin, so the error is monotone. The full coupling argument is in the canonical proof.

<a id="boundaries-and-attribution"></a>

## 9. What the theorem permits, and what the argument imports

The coherent state $`|D\rangle`$ in the three-register example has the same one-register marginals as $`\rho_{\mathrm{mix}}`$, but it lies entirely in the symmetric sector. Its universal recovery optimum is $`2/3`$, whereas the classical-placement mixture permits $`8/9`$. The difference is the coherence between placements. More generally, the normalized equal superposition of configurations with $`m`$ target occupations and $`k`$ copies of a single orthogonal state has optimum $`m/N`$. The [coherent-occupation result](../science/accuracy-and-boundaries.md) supplies the all-channel converse. A count of target occupations alone does not imply the theorem's input promise.

Exact orthogonality also has a specific role. It made different placement spaces orthogonal and allowed their dimensions to add. For arbitrary nonorthogonal faults that step fails, so the displayed conditional law and minimax value do not automatically apply. This limitation does not assert that recovery under other noise models is impossible. The [model](../science/model.md) gives a continuity statement for a joint input close to the entire admissible class.

Dimension-independent accuracy concerns the number of supplied registers. Each preparation must be paid for, the input block requires quantum storage, and the collective circuit has a separate precision and gate cost. The [resource account](../science/recovery-channel.md) charges these costs and credits the inherited implementation. The processor receives no target projector, preparation inverse, or free data-loading operation.

The scientific attribution follows the structure of the proof:

- [BLMO2023](../references/RELATED_WORK.md#BLMO2023) supplies the qubit benchmark and covariant-channel converse. [GO2024](../references/RELATED_WORK.md#GO2024) already gives the all-dimension three-input value.
- [SSW2026](../references/RELATED_WORK.md#SSW2026) and [LTHC2026](../references/RELATED_WORK.md#LTHC2026) supply the collective extraction framework, component formulas, and related purity-amplification analysis. The Schur, Pieri, and RSK tools are established mathematics.
- The additional argument here is the exact conditional law for every faulty sector and its sharp fixed-count coupling to the binary maximum. Together with the inherited component bound and qubit converse, it proves that arbitrary dimension and entanglement confined to the orthogonal faulty subset add no minimax cost.

An iid average would not establish this conclusion: a bound on an average of sector errors need not bound every sector. The uniform conditional argument is what makes arbitrary faulty entanglement admissible.

For the complete chain, read [model](../science/model.md), [recovery channel](../science/recovery-channel.md), [sector reduction](../science/sector-reduction.md), and [minimax proof](../science/minimax-proof.md), then [accuracy and boundaries](../science/accuracy-and-boundaries.md). The [milestone map](milestones.md) connects these pages to the anchor, and [verification](../verification/README.md) distinguishes exact finite checks from the general proof.
