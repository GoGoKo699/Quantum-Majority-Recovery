# Learning Quantum Majority Recovery

The task is to recover one unknown quantum state from a collection of outputs. A strict majority contains exact copies of the target. The remaining outputs are orthogonal to it and can be entangled with one another. The recovery operation must work without being told the target or the good positions.

The selected educational anchor is **John Watrous, *The Theory of Quantum Information* (Cambridge University Press, 2018)**. The [author's page](https://cs.uwaterloo.ca/~watrous/TQI/) provides the book manuscript and individual chapters for personal use. The relevant sections are identified in the [Watrous bridge](watrous-bridge.md); reading the whole book is not a prerequisite.

## Choose a reading route

| Starting question | Route |
|---|---|
| What is recovered, and why is the guarantee surprising? | Read the [repository overview](../README.md), the opening of the [bridge](watrous-bridge.md), and its three-register example. |
| How do I build the background and connect it to the proof? | Follow the [30 milestones](milestones.md) with the [bridge](watrous-bridge.md). Use the cited Watrous sections when a foundational concept needs more detail. |
| Where is the exact theorem and its complete proof? | Read [model](../science/model.md), [channel](../science/recovery-channel.md), [sector reduction](../science/sector-reduction.md), and [minimax proof](../science/minimax-proof.md), in that order. |
| What does a majority buy, and when does recovery fail to improve fidelity? | Read [accuracy and boundaries](../science/accuracy-and-boundaries.md), including the coherent-occupation theorem. |
| Which ingredients are established literature, and which conclusion is added here? | Read [related work](../references/RELATED_WORK.md), then the conditional-law and coupling arguments in the scientific account. |
| How can I reproduce the finite calculations? | Follow [verification](../verification/README.md). |

## How the pieces connect

Watrous supplies a language for states, quantum channels, fidelity and symmetry. The bridge translates that language into this project's input promise and output task. It then explains the extra machinery needed here: Schur sectors, representation dimensions, the Pieri rule and the Robinson–Schensted–Knuth correspondence. The primary research sources remain necessary for attribution of the extraction channel and its component formula.

The [milestone map](milestones.md) contains exactly 30 understanding targets. Its **13 background milestones** connect individual quantum and combinatorial objects into the framework of the problem. Its **17 narrative milestones** connect the reduction, coupling and converse into the exact recovery law, then interpret the accuracy and resource limits. Each target identifies earlier dependencies and the authoritative scientific source. The map is a common guide to the project; it does not attempt to cover every technical lemma or every chapter of the anchor.

The scientific pages are the authoritative homes of the full statements and proofs. The learning pages explain how to reach those statements and why the steps fit together. A small worked example illustrates the mechanism; the general theorem depends on the complete reduction and converse.

## Conventions that matter

Fidelity in this repository is the overlap with the pure target,

```math
F=\langle\psi|\rho_{\mathrm{out}}|\psi\rangle.
```

Watrous defines root fidelity, so its square gives the quantity above when one state is pure. The bridge states this translation before using a fidelity comparison.

The recovery channel outputs a quantum register. An accurate classical description of the target is a different task. Symmetry averaging is part of the proof that the channel is optimal; it does not supply an oracle for the unknown target.

The promise is also precise. Good registers are exact pure copies, each faulty register has orthogonal support, and the hidden positions are classical. Faults can be jointly entangled. An arbitrary coherent state with the same number of target occupations belongs to a larger input class and has a different optimum. These distinctions persist through every reading route.

Return to the [project overview](../README.md) or use the [LLM reading guide](../llms.txt) to locate a specific claim.
