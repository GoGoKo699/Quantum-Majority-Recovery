# Thirty milestones for quantum majority recovery

This map follows the scientific dependencies of the project. Its understanding targets are the same for every reader. The educational anchor is John Watrous, [*The Theory of Quantum Information* (2018)](https://cs.uwaterloo.ca/~watrous/TQI/). The [Watrous bridge](watrous-bridge.md) translates its notation and supplies the representation and combinatorial steps needed here. Section pointers below refer to the author's linked manuscript. They select useful parts of the book; the whole book is not a prerequisite.

The allocation is **13 background/preliminaries milestones and 17 narrative/innovation milestones**. The background must connect three kinds of objects: quantum states and channels, symmetry sectors, and classical tableau/path distributions. Its final milestone assembles these into the recovery problem. The narrative then follows the actual argument from correlated faults to an exact minimax law, before integrating the accuracy regimes, coherent-position boundary, implementation costs, and evidence limits. The allocation reflects those dependencies rather than the book's chapter lengths.

| Phase | Milestones | Local starting point | Final synthesis |
|---|---|---|---|
| Background/preliminaries | M01 through M13 | A target state, a register, and an orthogonal subspace | The operational model and the proof framework |
| Narrative/innovation | M14 through M30 | The recovery channel and one faulty symmetry sector | The exact contribution, its costs, boundaries, and evidence |

The mathematical conventions are those of [the model](../science/model.md): $`N=m+k`$, $`m>k`$, $`g=m-k`$, $`k`$ faults, and overlap fidelity. Research papers linked through the scientific pages provide attribution and proof dependencies. They are not additional educational anchors. Watrous supplies the operational and symmetry foundations; mixed Schur branching, Pieri induction, RSK, and the exact recovery argument are supplied by the project and its cited primary literature.

## Background/preliminaries: M01 through M13

<a id="M01"></a>
### M01: A target state and its orthogonal alternatives

**Central question:** What does it mean for a quantum register to contain the target, or to be supported entirely away from it?

**Understanding target:** Interpret a pure state, its projector $`P_\psi`$, a density operator, and the orthogonal space $`\psi^\perp`$. Distinguish an unknown target from a supplied classical description of that target.

**Dependencies and story role:** No earlier milestones. This establishes the local objects from which the input promise is built.

**Conceptual connection:** Orthogonality is a support constraint on faulty states. It does not give the processor an oracle for identifying those states.

**Sources:** Watrous [§2.1.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf#page=4); [model, §1](../science/model.md#1-input-and-output); bridge, [states and faults](watrous-bridge.md#states-and-faults).

<a id="M02"></a>
### M02: Joint inputs and entangled faults

**Central question:** How can faults be fully correlated while the good registers remain exact copies of a pure state?

**Understanding target:** Read tensor products and reduced states, distinguish a product state from a general joint density operator, and explain why a pure good marginal factors from the remaining registers. Entanglement may still be arbitrary within the faulty subsystem.

**Dependencies and story role:** [M01](#M01). This extends the single-register model to a physically meaningful joint input.

**Conceptual connection:** The tensor factorization of the good subsystem follows from purity. Independence of the faulty registers is a separate assumption and is not made.

**Sources:** Watrous [§2.1.3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf#page=10) and [§6.1.1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.6.pdf); [model, §1](../science/model.md#1-input-and-output); [sector reduction, §1](../science/sector-reduction.md#1-spaces-partitions-and-symmetries).

<a id="M03"></a>
### M03: Unknown placement and coherent placement

**Central question:** Why is a classical mixture of fault locations different from a coherent superposition of those locations?

**Understanding target:** Distinguish a convex mixture of fixed-placement density operators from a superposed state vector. Recognize that identical target-occupation counts need not imply identical joint input promises.

**Dependencies and story role:** [M01](#M01), [M02](#M02). This makes the model's most consequential boundary visible before using symmetry.

**Conceptual connection:** Permutation symmetry of an averaged density operator does not establish that its support lies in the symmetric-vector subspace or that all placement coherence is allowed.

**Sources:** Watrous [§2.1.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf#page=4) and [§7.1.1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.7.pdf#page=2); [the precise good-register promise](../science/accuracy-and-boundaries.md#what-pure-good-registers-requires); bridge, [states and faults](watrous-bridge.md#states-and-faults).

<a id="M04"></a>
### M04: The deterministic recovery contract

**Central question:** Which physical operations are allowed to turn the input block into one output register?

**Understanding target:** Explain complete positivity and trace preservation as the conditions on the recovery map. Include ancillary systems, measurements, and feed-forward within that model, while distinguishing an unconditional output guarantee from a selected successful branch.

**Dependencies and story role:** [M01](#M01), [M02](#M02). This identifies the full class of processors against which optimality will be claimed.

**Conceptual connection:** The optimization is over quantum-output channels, including collective operations. It is not restricted to measuring a classical estimate and preparing a replacement state.

**Sources:** Watrous [§2.2.1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf#page=15); [model, §1](../science/model.md#1-input-and-output); bridge, [channels and discarding](watrous-bridge.md#channels-and-discarding).

<a id="M05"></a>
### M05: Representing a channel by an isometry and an environment

**Central question:** How can discarding part of a larger reversible transformation implement recovery?

**Understanding target:** Connect the channel, Stinespring, and Choi descriptions of an operation. Interpret an isometric embedding followed by partial trace without treating the discarded system as an observed classical answer.

**Dependencies and story role:** [M02](#M02), [M04](#M04). This supplies the local architecture used by the extraction channel and the later covariant converse.

**Conceptual connection:** The same channel can be described by a physical dilation for achievability and by positivity constraints for optimality.

**Sources:** Watrous [§2.2.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf#page=20); [recovery channel, §1](../science/recovery-channel.md#1-schur-sectors); bridge, [channels and discarding](watrous-bridge.md#channels-and-discarding).

<a id="M06"></a>
### M06: Fidelity, infidelity, and perturbations

**Central question:** What quantity measures recovery accuracy, and how does it relate to Watrous's convention?

**Understanding target:** Translate Watrous's root fidelity into the project's pure-target overlap $`\langle\psi|\sigma|\psi\rangle`$. Interpret $`\varepsilon_{N,k}=1-F_N(k)`$ and distinguish this accuracy from trace-distance input uncertainty or channel-implementation error.

**Dependencies and story role:** [M01](#M01), [M04](#M04). This fixes the common score used throughout the proof and its stability statements.

**Conceptual connection:** A fidelity convention changes the numerical expression. A norm bound controls how much the same operational score can change under perturbation.

**Sources:** Watrous [§3.2, Definition 3.11](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf#page=16); [model, §5](../science/model.md#5-resources-and-stability); bridge, [fidelity convention](watrous-bridge.md#fidelity-convention).

<a id="M07"></a>
### M07: Uniform guarantees and minimax reasoning

**Central question:** What separates a successful recovery channel from a proof that no channel can do better?

**Understanding target:** Read the supremum over CPTP maps and the infimum over admissible targets and inputs. Explain how linearity extends a bound to convex mixtures, and how a restricted hard input family can bound every allowed channel.

**Dependencies and story role:** [M03](#M03), [M04](#M04), [M06](#M06). This establishes the logical structure of achievability and converse before either is proved.

**Conceptual connection:** A worst case for one chosen channel does not automatically establish the minimax optimum.

**Sources:** Watrous [§1.2.1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf#page=35) and [§2.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf#page=15); [model, §2](../science/model.md#2-exact-recovery-theorem); [minimax proof, §7](../science/minimax-proof.md#7-matching-minimax-converse).

<a id="M08"></a>
### M08: Symmetry as an analytical reduction

**Central question:** When can the proof average over permutations or unitaries without changing the recovery score?

**Understanding target:** Distinguish permutation invariance from unitary covariance. Explain why averaging over the target's stabilizer preserves target fidelity, and why choosing $`\psi=|d\rangle`$ in an argument does not require learning that basis physically.

**Dependencies and story role:** [M03](#M03), [M04](#M04), [M06](#M06). This connects the operational task to symmetry methods without introducing target-dependent access.

**Conceptual connection:** An analytical twirl preserves the quantity being evaluated. It need not reproduce the actual preparation process or become a step in the circuit.

**Sources:** Watrous [§7.1.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.7.pdf#page=11) and [§7.2.1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.7.pdf#page=19); [sector reduction, §1](../science/sector-reduction.md#1-spaces-partitions-and-symmetries); bridge, [symmetry and twirling](watrous-bridge.md#symmetry-and-twirling).

<a id="M09"></a>
### M09: Mixed symmetry sectors

**Central question:** What information is retained when a tensor-power space is decomposed into Schur sectors?

**Understanding target:** Interpret a partition $`\lambda`$, the unitary-representation factor $`Q_\lambda^{(d)}`$, and the permutation factor $`V_\lambda`$. Distinguish a permutation-invariant operator from a vector confined to the fully symmetric sector.

**Dependencies and story role:** [M02](#M02), [M08](#M08). This organizes the entire input block into the coordinates used by recovery.

**Conceptual connection:** Entangled faults can occupy mixed symmetry sectors. Restricting attention to symmetric tensor powers would omit allowed inputs.

**Sources:** Watrous [§7.1.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.7.pdf#page=11) supplies the operator-symmetry foundation; [recovery channel, §1](../science/recovery-channel.md#1-schur-sectors) and bridge, [mixed Schur sectors](watrous-bridge.md#mixed-schur-bridge), supply the decomposition used here.

<a id="M10"></a>
### M10: Branching and horizontal strips

**Central question:** How does separating one distinguished state from its orthogonal subspace constrain the possible partitions?

**Understanding target:** Read the interlacing inequalities between $`\lambda`$ and $`\nu`$, interpret a horizontal strip, and distinguish the multiplicity of an irreducible representation from its dimension. Identify where unitary branching and Pieri's rule enter.

**Dependencies and story role:** [M01](#M01), [M09](#M09). This joins the local target/fault split to the global representation labels.

**Conceptual connection:** A combinatorial condition on boxes simultaneously describes target occupation and the allowed representation summands. These specialized rules are supplied locally, rather than assumed to follow from the anchor's symmetric-subspace discussion.

**Sources:** Watrous [§7.1.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.7.pdf#page=11) for context; [sector reduction, §§1 and 3](../science/sector-reduction.md#1-spaces-partitions-and-symmetries); bridge, [mixed Schur sectors](watrous-bridge.md#mixed-schur-bridge).

<a id="M11"></a>
### M11: Words, insertion tableaux, and recording tableaux

**Central question:** How can a word encode both a partition shape and the number of ways that shape occurs?

**Understanding target:** Distinguish the semistandard insertion tableau $`P`$ from the standard recording tableau $`Q`$. Explain the role of row insertion, the RSK bijection, and the longest weakly increasing subsequence in determining the first row.

**Dependencies and story role:** [M09](#M09), [M10](#M10). This supplies the discrete language that will realize the quantum sector law as a classical distribution.

**Conceptual connection:** A tableau shape is not merely a diagram of a representation; through RSK it also records a property of an ordered word.

**Sources:** Watrous [§1.2.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf#page=47) supplies probability background; the RSK facts are supplied in [minimax proof, §3](../science/minimax-proof.md#3-an-exact-rsk-coupling-for-each-bad-partition) and bridge, [exact recovery](watrous-bridge.md#exact-recovery-bridge).

<a id="M12"></a>
### M12: Comparing distributions through a shared construction

**Central question:** Why is a pointwise inequality under a coupling stronger than comparing two average values?

**Understanding target:** Interpret a uniform fixed-count binary path, its prefix sums and maximum, tail probabilities, and expectations of increasing functions. Explain how one construction can realize two random quantities and order them for every outcome.

**Dependencies and story role:** [M07](#M07), [M11](#M11). This turns the combinatorial language into a method for proving uniform performance guarantees.

**Conceptual connection:** The proof will compare the first-row excess with a binary maximum under a coupling, rather than approximate a correlated input by iid samples.

**Sources:** Watrous [§1.2.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf#page=47); [minimax proof, §4](../science/minimax-proof.md#4-binary-domination-of-the-first-row-excess); bridge, [exact recovery](watrous-bridge.md#exact-recovery-bridge).

<a id="M13"></a>
### M13: Background synthesis: the full recovery framework

**Central question:** How do the physical promise, channel model, symmetry decomposition, and classical comparison fit together?

**Understanding target:** Give one connected account of an unknown pure majority with orthogonal entangled faults, a fixed quantum-output channel, a fidelity objective, representation-sector averaging, and a possible pathwise bound. Identify which steps require a construction and which require a converse.

**Dependencies and story role:** [M03](#M03), [M05](#M05), [M06](#M06), [M08](#M08), [M10](#M10), [M11](#M11), [M12](#M12). This completes the background phase by assembling its local ingredients.

**Conceptual connection:** Quantum processing, representation theory, and classical probability describe different parts of the same task. None alone establishes recovery or optimality.

**Sources:** Watrous [§§2.1–2.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf), [§3.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf#page=16), and [§7.1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.7.pdf); [model, §§1–4](../science/model.md); bridge, [reading route](watrous-bridge.md#reading-route).

## Narrative/innovation: M14 through M30

<a id="M14"></a>
### M14: The exact question beyond the established benchmarks

**Central question:** What does the project establish after the known qubit optimum and purity-amplification channel are credited?

**Understanding target:** State the all-dimension, all-fault-sector minimax claim with its exact orthogonal-fault promise. Distinguish this contribution from the known qubit law, the known three-input result, and iid purification guarantees.

**Dependencies and story role:** [M13](#M13). This identifies the contribution that the narrative must justify.

**Conceptual connection:** The operational difference is robustness to arbitrary entanglement within the faulty subsystem at the same exact finite-sample cost. The channel and the qubit accuracy sequence remain inherited ingredients.

**Sources:** Watrous [§2.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf#page=15) and [§3.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf#page=16) for the operational comparison; [model, §2](../science/model.md#2-exact-recovery-theorem); [related-work comparison](../references/RELATED_WORK.md#the-closest-results).

<a id="M15"></a>
### M15: A channel fixed by the input size and dimension

**Central question:** How is the recovered register extracted without knowing the target or fault count?

**Understanding target:** Follow Schur-label measurement, disposal of the permutation factor, the overhang rule, the isometric intertwiner, and the final partial trace. Explain why defining the map on tied sectors matters even though the promised inputs will have a strict first-row gap.

**Dependencies and story role:** [M05](#M05), [M09](#M09), [M10](#M10), [M14](#M14). This gives the concrete operation whose performance will be proved.

**Conceptual connection:** A representation decomposition becomes an allowed physical channel only when its action and completion are specified independently of the hidden input.

**Sources:** Watrous [§2.2.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf#page=20); [recovery channel, §1](../science/recovery-channel.md#1-schur-sectors); bridge, [channels and discarding](watrous-bridge.md#channels-and-discarding).

<a id="M16"></a>
### M16: Reducing arbitrary entangled faults

**Central question:** Why can every faulty joint state be analyzed through a mixture indexed by one partition $`\nu`$?

**Understanding target:** Follow the two analytical twirls over faulty-register permutations and $`U(d-1)`$. Explain why both representation factors become maximally mixed within each bad sector while the weights $`q_\nu`$ remain unrestricted.

**Dependencies and story role:** [M08](#M08), [M09](#M09), [M14](#M14), [M15](#M15). This is the first reduction that addresses the full correlated input class.

**Conceptual connection:** The scalar fidelity is unchanged by the twirl. The original entangled state is not being declared equal to an iid state or to its twirled version.

**Sources:** Watrous [§7.1.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.7.pdf#page=11) and [§7.2.1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.7.pdf#page=19); [sector reduction, §2](../science/sector-reduction.md#2-twirling-the-faulty-subsystem); bridge, [symmetry and twirling](watrous-bridge.md#symmetry-and-twirling).

<a id="M17"></a>
### M17: Unknown locations produce an induced representation

**Central question:** What is the exact state obtained by averaging the possible placements of one faulty sector?

**Understanding target:** Explain why different placement spaces are orthogonal, why their averaged state is a normalized projector, and how the cosets of $`S_m\times S_k`$ identify the induced permutation representation.

**Dependencies and story role:** [M03](#M03), [M10](#M10), [M16](#M16). This converts unknown fault locations into a global representation statement with a controlled normalization.

**Conceptual connection:** Exact orthogonality permits a direct sum over placements. This is the point where replacing a mixture by coherent placement would change the argument.

**Sources:** Watrous [§2.1.3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf#page=10) and [§7.1.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.7.pdf#page=11) for the state and symmetry foundations; [sector reduction, §3](../science/sector-reduction.md#3-averaging-placements-gives-an-induced-representation); bridge, [mixed Schur sectors](watrous-bridge.md#mixed-schur-bridge).

<a id="M18"></a>
### M18: The conditional shape law and conditional quantum state

**Central question:** Why does the law of the measured shape have no ambient-dimension factor?

**Understanding target:** Derive and interpret $`p(\lambda\mid\nu)=f^\lambda/[\binom Nm f^\nu]`$ on horizontal-strip extensions. Track the cancellation of $`\dim Q_\nu^{(d-1)}`$, and identify the normalized branching-block state remaining after the measurement.

**Dependencies and story role:** [M10](#M10), [M17](#M17). This supplies the exact distribution needed for the recovery calculation, separately for every faulty sector.

**Conceptual connection:** Knowing a label's probability is insufficient for quantum-output recovery. The conditional state's symmetry also makes the inherited component-fidelity formula applicable.

**Sources:** Watrous [§7.1.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.7.pdf#page=11) for the commuting-actions context; [sector reduction, §4 and its character verification](../science/sector-reduction.md#4-the-conditional-law-and-conditional-state); bridge, [mixed Schur sectors](watrous-bridge.md#mixed-schur-bridge).

<a id="M19"></a>
### M19: A component bound that retains the majority margin

**Central question:** How does the first-row excess control the output error in one representation branch?

**Understanding target:** Interpret $`r=\lambda_1-m`$, the overhangs $`b_j`$, and their sum. Combine the inherited product formula with $`\lambda_1-\lambda_2\ge g+2r`$ to obtain $`1-a_{\lambda,\nu}\le r/(g+2r)`$.

**Dependencies and story role:** [M10](#M10), [M15](#M15), [M18](#M18). This connects representation geometry to the accuracy score before averaging.

**Conceptual connection:** Retaining $`2r`$ in the denominator is what allows the subsequent argument to recover the exact binary minimax value, rather than only its order of decay.

**Sources:** Watrous [§3.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf#page=16) for the score; [recovery channel, §2](../science/recovery-channel.md#2-exact-component-fidelity); [sector support and gap](../science/sector-reduction.md#5-supported-sectors-have-a-strict-first-row-gap).

<a id="M20"></a>
### M20: Realizing the quantum law through RSK

**Central question:** How can a fixed insertion tableau and random placements reproduce the conditional quantum shape law exactly?

**Understanding target:** Follow the choice of $`P_0`$, uniform $`Q_0`$, inverse RSK, and insertion of $`m`$ largest letters. Explain the restriction lemma and why each allowed full shape has precisely $`f^\lambda`$ recording tableaux.

**Dependencies and story role:** [M11](#M11), [M18](#M18). This is the exact coupling that connects the quantum sector reduction to a classical construction.

**Conceptual connection:** The construction works for each $`\nu`$ and each permitted $`P_0`$. No unknown iid spectrum is introduced to justify the averaging.

**Sources:** Watrous [§1.2.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf#page=47) for distributions; [minimax proof, restriction lemma and coupling](../science/minimax-proof.md#3-an-exact-rsk-coupling-for-each-bad-partition); bridge, [exact recovery](watrous-bridge.md#exact-recovery-bridge).

<a id="M21"></a>
### M21: Every faulty sector is dominated by a binary path

**Central question:** Why can more orthogonal fault directions never increase the worst recovery error beyond the binary comparison?

**Understanding target:** Cut a weakly increasing subsequence at its last selected bad letter to prove $`0\le r\le M`$ for each constructed word. Apply the monotonicity of $`h_g(x)=x/(g+2x)`$ and average over the arbitrary weights $`q_\nu`$.

**Dependencies and story role:** [M12](#M12), [M19](#M19), [M20](#M20). This joins the local branch bound and the conditional law into one uniform guarantee.

**Conceptual connection:** The same binary path dominates every bad symmetry sector. This is the mechanism behind the lack of an additional dimension or faulty-entanglement penalty.

**Sources:** Watrous [§1.2.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf#page=47); [minimax proof, §4](../science/minimax-proof.md#4-binary-domination-of-the-first-row-excess); bridge, [exact recovery](watrous-bridge.md#exact-recovery-bridge).

<a id="M22"></a>
### M22: Counting the exact binary risk

**Central question:** How does reflecting a path turn the comparison bound into an explicit finite-sample formula?

**Understanding target:** Explain the bijection behind $`\Pr(M\ge r)=\binom N{k-r}/\binom Nk`$, obtain the mass function by subtracting adjacent tails, and interpret $`\varepsilon_{N,k}=\mathbb E[M/(g+2M)]`$.

**Dependencies and story role:** [M12](#M12), [M21](#M21). This converts the comparison mechanism into a directly evaluable accuracy law.

**Conceptual connection:** The exact fixed-count bridge retains finite-sample information that a concentration inequality or an iid approximation would discard.

**Sources:** Watrous [§1.2.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf#page=47); [minimax proof, §5](../science/minimax-proof.md#5-reflection-law-for-the-binary-bridge); [accuracy, exact risk](../science/accuracy-and-boundaries.md#exact-risk-and-a-binary-bridge).

<a id="M23"></a>
### M23: An input family that attains the bound

**Central question:** When are all the inequalities in the recovery analysis equalities?

**Understanding target:** Follow identical pure faults $`|\phi\rangle^{\otimes k}`$ with $`\phi\perp\psi`$, the sector $`\nu=(k)`$, the binary identity $`r=M`$, and equality in the component bound. Interpret the three-register fidelity $`8/9`$ as a complete small instance.

**Dependencies and story role:** [M15](#M15), [M19](#M19), [M20](#M20), [M22](#M22). This identifies a worst case for the chosen channel before addressing all competing channels.

**Conceptual connection:** A larger fault space does not have to be used by the worst input. The exact bound is already attained inside a two-dimensional subspace.

**Sources:** Watrous [§2.1.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf#page=4) and [§3.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf#page=16); [minimax proof, §6](../science/minimax-proof.md#6-equality-for-identical-orthogonal-faults); bridge, [three-register example](watrous-bridge.md#three-register-example).

<a id="M24"></a>
### M24: The qubit converse against every allowed channel

**Central question:** Why can another collective qubit channel not outperform the binary benchmark?

**Understanding target:** Follow the permutation and rotation average, the positive-magnetization spin sectors, and the two extremal covariant channels. Explain why the trace extreme wins separately in every supported sector, including for even $`N`$ with strict majority.

**Dependencies and story role:** [M05](#M05), [M07](#M07), [M08](#M08), [M09](#M09), [M23](#M23). This supplies the unrestricted qubit lower bound, not merely optimality within one proposed circuit.

**Conceptual connection:** Symmetry turns a large channel optimization into a sectorwise comparison, while preserving the full minimax task.

**Sources:** Watrous [§2.2.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf#page=20) and [§2.2.4](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf#page=39); [minimax proof, §§7.1–7.2](../science/minimax-proof.md#7-matching-minimax-converse); [qubit-majority attribution](../references/RELATED_WORK.md#BLMO2023).

<a id="M25"></a>
### M25: Exact dimension universality

**Central question:** Why do additional output dimensions fail to evade the qubit converse?

**Understanding target:** Construct the projection-back channel with replacement of leaked weight and explain why it cannot lower fidelity with an embedded target. Combine this converse with the all-sector guarantee to conclude $`F^\star_{N,k,d}=F_N(k)`$ for every $`d\ge2`$.

**Dependencies and story role:** [M07](#M07), [M21](#M21), [M22](#M22), [M23](#M23), [M24](#M24). This assembles the mathematical contribution from achievability and converse.

**Conceptual connection:** The reduction bounds arbitrary output channels in the larger space. It does not assume that a competing processor voluntarily confines its output to the qubit subspace.

**Sources:** Watrous [§2.2.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf#page=20); [minimax proof, §7.3](../science/minimax-proof.md#7-matching-minimax-converse); [model, Theorem 1](../science/model.md#2-exact-recovery-theorem).

<a id="M26"></a>
### M26: Unknown fault count and the at-most promise

**Central question:** Does the same operation remain optimal when only an upper bound on the number of faults is known?

**Understanding target:** Couple nested uniform faulty subsets, track how the bridge maximum and majority margin change, and establish that $`\varepsilon_{N,k}`$ is nondecreasing in $`k`$. Explain why the channel's independence from $`k`$ is essential to the guarantee.

**Dependencies and story role:** [M12](#M12), [M22](#M22), [M25](#M25). This extends the exact-count theorem to the operationally useful bounded-fault promise.

**Conceptual connection:** Monotonicity and a common channel are both needed. Separate optimal channels for separate counts would not alone solve the unknown-count problem.

**Sources:** Watrous [§1.2.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf#page=47); [minimax proof, §8](../science/minimax-proof.md#8-one-channel-for-every-fault-count-and-the-at-most-promise); [accuracy, monotonicity](../science/accuracy-and-boundaries.md#more-faults-make-the-task-harder).

<a id="M27"></a>
### M27: Reading the majority margin correctly

**Central question:** Which kinds of majority lead to accurate recovery as the input block grows?

**Understanding target:** Distinguish a fixed positive fault fraction strictly below one half, a fixed positive fault count, and a nearly tied input. Explain the respective $`1/N`$ and $`k/N^2`$ infidelity laws, the near-$`1/2`$ fidelity regime, and why fidelity tending to one requires $`g/\sqrt N\to\infty`$.

**Dependencies and story role:** [M06](#M06), [M12](#M12), [M22](#M22), [M26](#M26). This interprets the exact law as an accuracy statement with explicit scaling assumptions.

**Conceptual connection:** Increasing the number of registers does not by itself strengthen the promise. The majority margin must be tracked alongside the sample size.

**Sources:** Watrous [§1.2.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf#page=47) and [§3.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf#page=16); [finite bounds and asymptotic regimes](../science/accuracy-and-boundaries.md#bounds-for-every-sample-size); [nearly tied inputs](../science/accuracy-and-boundaries.md#nearly-tied-inputs).

<a id="M28"></a>
### M28: The coherent-position boundary

**Central question:** What fails if the promise allows coherent superpositions of good-register locations?

**Understanding target:** Compare the admissible convex hull with the full fixed-occupation subspace. Use the symmetric Dicke family and spin-sector converse to obtain the upper bound $`m/N`$, and match it by returning a uniformly random register.

**Dependencies and story role:** [M02](#M02), [M03](#M03), [M08](#M08), [M24](#M24), [M25](#M25). This identifies the exact boundary of the robustness theorem after its positive result is established.

**Conceptual connection:** Arbitrary entanglement among faulty registers is compatible with optimal recovery. Coherence between faulty-location sectors changes the minimax problem and prevents fidelity tending to one at a fixed positive fault fraction.

**Sources:** Watrous [§2.1.3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf#page=10) and [§7.1.1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.7.pdf#page=2); [occupation achievability and converse](../science/accuracy-and-boundaries.md#achievability); bridge, [boundaries and attribution](watrous-bridge.md#boundaries-and-attribution).

<a id="M29"></a>
### M29: Implementation, resources, and error allowances

**Central question:** What is paid to implement the ideal recovery map at a specified accuracy?

**Understanding target:** Separate input preparation, collective quantum storage, gate complexity, auxiliary workspace, and implementation precision. Interpret the inherited $`O(N^4\log^q(dN/\delta))`$ gate upper bound and the fidelity allowance from diamond-norm error. Distinguish optimal copy complexity from an unproved optimal gate or memory cost.

**Dependencies and story role:** [M04](#M04), [M05](#M05), [M06](#M06), [M15](#M15), [M25](#M25), [M27](#M27). This converts the ideal capability into an honestly charged algorithmic statement.

**Conceptual connection:** Analytical symmetry reductions supply no free target projector or preparation inverse. Channel approximation and joint-input uncertainty require their own error allowances.

**Sources:** Watrous [§2.2.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf#page=20) and [§3.3.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf#page=43); [recovery channel, §§3–4](../science/recovery-channel.md#3-a-target-independent-circuit); [model, stability](../science/model.md#5-resources-and-stability).

<a id="M30"></a>
### M30: Narrative synthesis: the contribution, evidence, and limits

**Central question:** What can now be concluded about recovering an unknown quantum majority, and what supports that conclusion?

**Understanding target:** Present the complete claim with its input promise, exact minimax value, entangled-fault reduction, binary worst case, accuracy regimes, coherent-position boundary, and charged resources. Explain which ingredients are inherited and why finite rational and direct RSK checks corroborate specific proof steps without proving all dimensions, asymptotic limits, or channel optimality.

**Dependencies and story role:** [M14](#M14), [M18](#M18), [M21](#M21), [M25](#M25), [M26](#M26), [M27](#M27), [M28](#M28), [M29](#M29). This completes the narrative phase by relating the mathematical result to its operational meaning and actual evidence.

**Conceptual connection:** The central insight is an exact absence of additional minimax cost from ambient dimension or entanglement confined to orthogonal faults. Its force depends on the stated promise, the matching converse, and accurate attribution.

**Sources:** Watrous [§2.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf#page=15), [§3.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf#page=16), and [§7.1.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.7.pdf#page=11) for the unified operational foundation; [model](../science/model.md), [additional argument and attribution](../references/RELATED_WORK.md#the-additional-argument), and [verification scope](../verification/README.md#what-the-checks-do-not-establish).
