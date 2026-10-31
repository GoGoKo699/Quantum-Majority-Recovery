# Related work and attribution

The [recovery theorem](../science/model.md) extends the exact qubit majority benchmark to arbitrary register dimension and arbitrary entanglement among the faulty registers. The promise is specific: more than half of the registers are exact copies of one unknown pure state, every faulty register lies in its orthogonal complement, and uncertainty about the good locations is classical. The result concerns the minimax performance of an established collective channel.

The distinction from earlier work is the sharp guarantee for every faulty symmetry sector. The channel, its component fidelity, the first-row defect estimate, and the Schur and RSK tools all have antecedents. The [sector reduction](../science/sector-reduction.md) and [minimax proof](../science/minimax-proof.md) identify the additional argument.

## The closest results

| Reference | Input promise and established result | Relation to this theorem |
|---|---|---|
| [BLMO2023](#BLMO2023) | Unknown-basis qubit strings; optimal quantum majority and its fidelity profile | Supplies the qubit benchmark, covariant-channel characterization and converse |
| [GO2024](#GO2024) | Arbitrary local dimension; exact three-input majority fidelity $`8/9`$ | Dimension independence for three inputs is already known |
| [SSW2026](#SSW2026) | Independent identical copies of a mixed state with arbitrary spectrum; dimension-independent nonasymptotic purification bounds | Supplies an exact component formula and the scalar branch inequality used here |
| [LTHC2026](#LTHC2026) | Independent identical copies; purification toward a selected eigenstate with multiple outputs | Supplies general overhang-removal channels, representation formulas and implementations |

The entries below refer to specific versions. Bibliographic records are in [references.bib](references.bib). The comparison was checked on 31 October 2026.

<a id="BLMO2023"></a>

## BLMO2023: quantum majority for qubits

Harry Buhrman, Noah Linden, Laura Mančinska, Ashley Montanaro and Maris Ozols, *Quantum Majority Vote*, ITCS 2023, LIPIcs 251, article 29. [Publisher record](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2023.29); [full preprint, arXiv:2211.11729v1](https://arxiv.org/html/2211.11729v1).

The inputs are qubits drawn from an unknown orthonormal pair. Sections 4.3 and 4.4 characterize the relevant covariant channels. Equations (4.25)–(4.27) give the sector probabilities and component fidelities; Section 5.2 and Appendix F analyze majority. These are the sources of the exact qubit benchmark used here. The paper formulates total symmetric equivariant Boolean functions for odd input count. Its same sector characterization gives the strict-majority benchmark for even input count when ties are excluded.

Section 1.4, item 3, asks about larger alphabets. This repository treats strict majority with a larger orthogonal error space, including entangled faulty inputs. It does not settle general plurality.

The ITCS item is a one-page abstract, page 29:1. The section and equation pointers above refer to the full preprint.

<a id="GO2024"></a>

## GO2024: three-input majority in every dimension

Dmitry Grinko and Maris Ozols, *Linear Programming with Unitary-Equivariant Constraints*, Communications in Mathematical Physics **405**, article 278, 72 pages (2024). [Official repository record](https://ir.cwi.nl/pub/34781); [final article](https://ir.cwi.nl/pub/34781/34781.pdf); [DOI](https://doi.org/10.1007/s00220-024-05108-1).

The paper gives a general framework for reducing symmetry-constrained semidefinite programs to linear programs. Its majority application in Section 7.2, printed pages 44–47, explicitly takes three inputs and one output. Equation (156) also allows the all-distinct case to return any present symbol. The final paragraph obtains optimal fidelity $`8/9`$ for every $`d\ge2`$.

That result already establishes the three-input, dimension-independent benchmark. The present theorem extends the exact strict-majority value to arbitrary sample size and jointly entangled orthogonal faults. It does not replace the broader relation treated for three inputs. The paper's general optimization framework is inherited machinery; its application does not state an arbitrary-sample sharp majority law. Earlier citations sometimes call this work GO22, referring to its 2022 preprint.

<a id="SSW2026"></a>

## SSW2026: nonasymptotic purity amplification

Thilo Scharnhorst, Jack Spilecki and John Wright, *Nonasymptotic bounds for quantum purity amplification*, [arXiv:2605.27262v1](https://arxiv.org/html/2605.27262v1), 26 May 2026.

Theorem 1.1 gives dimension-independent finite-sample bounds for principal-eigenstate purification from $`\rho^{\otimes n}`$, with arbitrary spectrum and multiple outputs. Section 2.4 defines the collective extraction channel. Lemma 3.1, Eq. (19), gives its fidelity on each tableau, before the iid average. The paper credits the single-output expression to [Fu2016](#Fu2016).

The branch estimate used here is an immediate consequence of their Eq. (24) and the defect identity following Eq. (26). With the notation of the [channel account](../science/recovery-channel.md), set

```math
r=\lambda_1-m,\qquad g=m-k,\qquad N=m+k.
```

Their bound and $`\lambda_2\le N-\lambda_1`$ give

```math
1-a_{\lambda,\nu}
\le\frac{\lambda_1-m}{\lambda_1-\lambda_2}
\le\frac{r}{g+2r}.
```

This is inherited component analysis. Their proof averages using iid word probabilities and Young-diagram concentration. The additional step here is the sharp average for every faulty sector, including sectors arising from entangled faulty states.

<a id="LTHC2026"></a>

## LTHC2026: selected eigenstates and multiple outputs

Zhaoyi Li, Elias Theil, Aram W. Harrow and Isaac Chuang, *Quantum Purity Amplification for Arbitrary Eigenstates and Multiple Outputs*, [arXiv:2605.21570v2](https://arxiv.org/html/2605.21570v2), 29 September 2026.

Section II, Eqs. (2)–(5), specifies the iid input model. The paper studies overhang removal, selected eigenstates, multiple outputs and optimality in several regimes. Its component formulas are representation identities that can be used beyond that input model. Theorem 4, Eq. (33), and Supplement Lemma S5.29 are relevant to the extraction fidelity. Supplement Theorem S3.2 supplies the generalized-phase-estimation implementation used in the [resource account](../science/recovery-channel.md).

Corollary S5.33, Eq. (S475), still uses spectral weights of the iid state. It does not state a guarantee uniform over arbitrary correlated faults. The present theorem transfers the established channel to that distinct input class and proves its exact minimax value. It does not introduce the overhang-removal construction or its circuit.

## The additional argument

For $`N=m+k`$ with $`m>k`$, the faulty state first reduces by symmetry to sectors $`\nu\vdash k`$. The [sector reduction](../science/sector-reduction.md) proves the conditional state and the exact law

```math
\Pr(\lambda\mid\nu)
=\frac{f^\lambda}{\binom Nm f^\nu},
\qquad
\lambda/\nu\text{ is a horizontal strip of size }m.
```

Here $`f^\lambda`$ is the dimension of the corresponding symmetric-group representation. The multiplicity-free decomposition is classical Pieri theory. The application identifies the distribution induced by every admissible correlated faulty sector.

The [minimax proof](../science/minimax-proof.md) then couples this distribution to a uniform binary word with $`k`$ up steps and $`m`$ down steps. Its path maximum $`M`$ dominates the first-row excess $`r=\lambda_1-m`$ for every $`\nu`$. The inherited branch bound therefore gives

```math
1-F\le\mathbb E\frac{M}{g+2M},
\qquad
\Pr(M\ge s)=\frac{\binom N{k-s}}{\binom Nk}
\quad(1\le s\le k).
```

Identical pure orthogonal faults attain the binary value. The embedded qubit converse proves that no channel can improve it. The result is the exact statement that dimension and entanglement within the faulty subset add no minimax cost under this promise.

An iid average alone cannot establish this uniform conclusion: an average of conditional errors does not bound each conditional error by the same number. Entangled faulty states also need not be positive mixtures of identical pure tensor powers. Antisymmetric faulty sectors already distinguish those classes. The per-component identity from SSW2026 remains valid; the new averaging argument is what extends it to the present model.

## Further foundations and neighboring results

<a id="CEM1999"></a>

**CEM1999.** J. I. Cirac, A. K. Ekert and C. Macchiavello, *Optimal purification of single qubits*, Physical Review Letters **82**, 4344–4347 (1999). [DOI](https://doi.org/10.1103/PhysRevLett.82.4344); [preprint](https://arxiv.org/abs/quant-ph/9812075). This is foundational work on optimal purification of independent noisy qubits.

<a id="Fu2016"></a>

**Fu2016.** Honghao Fu, *Quantum State Purification*, Master of Mathematics thesis, University of Waterloo (2016). [Official thesis record](https://uwspace.uwaterloo.ca/items/7cdca652-878a-4322-bcd6-5bd13254567c). This develops purification through Schur and Clebsch–Gordan methods. The attribution of the single-output component formula above follows SSW2026's explicit credit to this thesis.

<a id="LFISC2025"></a>

**LFISC2025.** Zhaoyi Li, Honghao Fu, Takuya Isogawa, Caio Silva and Isaac Chuang, *Optimal Quantum Purity Amplification*, [arXiv:2409.18167v4](https://arxiv.org/abs/2409.18167v4), 25 December 2025; first posted in 2024. This is an antecedent for optimal qudit purification and efficient collective implementations. The cited version has five authors, including Caio Silva.

<a id="CFLLOV2025"></a>

**CFLLOV2025.** Andrew M. Childs, Honghao Fu, Debbie Leung, Zhi Li, Maris Ozols and Vedang Vyas, *Streaming quantum state purification*, Quantum **9**, 1603 (2025). [Publisher record](https://quantum-journal.org/papers/q-2025-01-21-1603/); [full preprint, version 4](https://arxiv.org/html/2309.16387v4). Its main model uses iid depolarized inputs. Section 4.3 explicitly distinguishes fixed-composition majority from iid purification and discusses the limited higher-dimensional majority results then available. Its discussion of nonidentical copies does not allow arbitrary entangled faults.

<a id="MT2025"></a>

**MT2025.** Laura Mančinska and Elias Theil, *Classification and implementation of unitary-equivariant and permutation-invariant quantum channels*, [arXiv:2510.08154v1](https://arxiv.org/abs/2510.08154v1), 9 October 2025. This supplies general channel structure and implementation methods. Its discussion identifies higher-dimensional quantum majority as an application; it does not provide the sharp correlated-fault law proved here.

<a id="Sagan2001"></a>

**Sagan2001.** Bruce E. Sagan, *The Symmetric Group: Representations, Combinatorial Algorithms, and Symmetric Functions*, second edition, Graduate Texts in Mathematics 203, Springer (2001). [Publisher record](https://link.springer.com/book/10.1007/978-1-4757-6804-6); [official contents](https://link.springer.com/content/pdf/bfm:978-1-4757-6804-6/1). Relevant background is in Section 1.12 on induction, Sections 2.3 and 2.5 on Specht modules and their dimensions, Sections 3.1 and 3.3 on Robinson–Schensted and subsequences, and Sections 4.7–4.9 on the characteristic map, Knuth's algorithm and Littlewood–Richardson theory. Pieri's rule is the one-row specialization of the latter theory. These are classical tools, rather than new identities introduced by this repository.
