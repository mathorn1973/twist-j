<!-- SPDX-License-Identifier: Apache-2.0 -->

# Sources and public scope

**NON-CANONICAL / L1.** This source guide was edited for public intake after
the original local execution; PUBLICATION.md records the original and intake
hashes.

## Authority and baseline

- Public repository: [mathorn1973/twist-j](https://github.com/mathorn1973/twist-j).
- Intake base: main at a8482d068156c8f42a390a81e817566b1c5abeda.
- Original mathematical baseline: d4d363722f052141a4ce65e9da39f11a74b43b95.
- Public Canon v109; tag object a33f63339b16b69725bf856e403610614143f81f,
  peeled activation 650029c20408f1dd665983d72225d0d195fd030e.
- Content commit: 2b0f94ec1e0874bff9141259e0b7da80e6681ea6.
- canon/CANON.md: 1464066 bytes;
  SHA-256 035408ec79219cc72a7d3613cf1568154cca185137d2a2daa43b896aae0c6383.

The intake changes no Canon file or scientific status.

## Public predecessor specifications

1. [Loaded contact, current-work identity and phase receiver, PR #1930](https://github.com/mathorn1973/twist-j/pull/1930),
   head f975ee0056d85583623bfc27cb41a18dda18907f,
   C-LOADED-CURRENT-WORK-PHASE-COMPATIBILITY-N.
   Used premises: $O=\mathbb Z[j]$, $\rho=j^2$, the Hermitian account and the
   loaded contact law $d=(2v-x-e+F)/4$, $i=(\rho-1)d$.
2. [Co-located loaded carrier, PR #1956](https://github.com/mathorn1973/twist-j/pull/1956),
   head 60b6652a41289a7d3672519499472eceb6afead4,
   C-COLOCATED-LOADED-WRITER-1.
   Used premises: the two-vertex topology, zero uncharged references,
   $F+x=0$, $F-\sum_Bv=0$, reduction to $d=(v-x)/2$, and complete
   scalar/Hermitian accounts $2\sum Q$ and $2\sum h$.
3. [During-path record, PR #1957](https://github.com/mathorn1973/twist-j/pull/1957),
   head fddf662982e6239e2ea14df7ae96361489bbbfc5,
   C-COLOCATED-READOUT-PATH-1.
   Used premises: target states $a_0=1-\rho$ and $a_1=(1-\rho)\rho^4$,
   helper preparation at $c=a/J$, and the two-selector port.
   This note audits that port on its declared input states. It does not
   independently replay the complete P27/P35 paths or replace their source
   audit, which records corrected post-failure checks.

## Self-contained conditional premises

The preserved proof also refers to an earlier local note titled
C-NATIVE-ENERGY-OCCURRENCE-DERIVATION-N and its label (9a). No public pin for
that predecessor is asserted here. The mathematical ingredients used from
it are stated explicitly and derived in PROOF.md, Sections 6 and 7:

- $W_k=N_k\bar w_k$, hence channel-independent positive $\bar w_k$
  implies $W_k/\sum_iW_i=N_k/\sum_iN_i$.
- The declared modes have $\cos\omega=5/8$ and $7/12$.
  With $(a_0,b)=(5,4)$ or $(7,6)$,
  $P_0=2$, $P_1=a_0$ and $P_{n+1}=a_0P_n-b^2P_{n-1}$.
  The coprimality argument establishes reduced denominator $2b^n$.

These are conditional algebraic inputs. This package does not establish a
physical selection of those modes or an occurrence law. Private coordination
identifiers and source locations are excluded from this public guide.
