<!-- SPDX-License-Identifier: Apache-2.0 -->

# Corrections and scope clarifications

**NON-CANONICAL / L1.** These corrections were prepared after the original
local execution. The original local source and outcome commits are preserved;
PUBLICATION.md maps their bytes to this intake. The exact code and expected
outputs are unchanged. This file does not retroactively revise a prospective
test or turn the local run into a public preregistration.

## E1. Explicit seed in the original README

The original README, A4, wrote
$c=(1-\rho)/J=1+2j+2j^2+j^3$. The right-hand polynomial is incorrect.
The exact value used by PROOF.md, PREREG.md and both scripts is
$$
c=-1-2j-2j^2=(-1,-2,-2,0).
$$
The erroneous polynomial has $h(c)=2+3\phi$, $Q(c)=7$ and recorded
quantum $25$, whereas the correct seed has $h(c)=3+4\phi$,
$Q(c)=10$ and quantum $35$. The intake README uses the correct value.

## E2. Golden-ratio convention and equal contributions

The original REVIEW.md used $\phi^2=1-\phi$ and
$\operatorname{Tr}(\phi)=-1$ with $\phi=-j^2-j^3$. Correctly,
$$
\phi^2=\phi+1,\qquad \operatorname{Tr}(\phi)=1.
$$
Consequently
$$
h((1-j^2)c)=(2A_c+B_c)+(A_c+3B_c)\phi,
$$
$$
h((1-j^4)c)=(3A_c-B_c)+(2B_c-A_c)\phi.
$$
The condition $B_c=0$ equates the two contributions to each other;
each then equals $\frac52Q(c)$, not $5Q(c)$.
For $c=1$, $B_c=0$ but $Q((1-j^2)c)=5$ and $5Q(c)=10$.
The preserved proof and both scripts use the correct formulas.

## E3. Complete five-channel account

The original REVIEW.md incorrectly expanded the corrected expression
$4Q(Jc)+20Q((3+\rho)c)$ as $200A_c+60B_c$. Since
$Q(Jc)=3A_c-B_c$ and $Q((3+\rho)c)=17A_c+B_c$, it is
$$
E_{\mathrm{full}}=352A_c+16B_c.
$$
The preserved proof states the unexpanded expression correctly. The complete
carrier account includes the field and all neutralizing companions:
$E_{\mathrm{full}}=2(Q(x)+\sum_{v\in B}Q(v))$.
A partial expression $Q(x)+2Q(h)+2Q(z)$ is not the per-cut invariant.

## E4. Intermediate sign in preserved PROOF.md

In Section 3, the first line of the proof of Theorem 2 contains
$$
x_2=x_1-(\rho-1)d_2=-2d_2+(\rho-1)d_2=-Jd_2.
$$
The middle plus must be a minus:
$$
x_2=-2d_2-(\rho-1)d_2=-(1+\rho)d_2=-Jd_2.
$$
The final expression, subsequent argument, theorem statement and executable
step already use the correct sign. PROOF.md is retained byte for byte;
this correction is part of its required reading.

## E5. Replay metadata and claims about consultation

- The output contains nine lines, not eleven.
- The preserved PREREG.md has 7441 bytes, not the 6521 reported in the
  original RUN.md. Its recorded SHA-256 was correct.
- Direct Windows output uses nine CRLF endings and has 585 bytes.
  The stored output has LF endings and 576 bytes. Only the explicitly
  newline-normalized replay matches the stored bytes; see RUN.md.
- A model's report that it found no static reason for an exception does not
  prove that the programs have zero bugs or guarantee a first-pass result.
  The preserved pre-freeze consultation required corrections before freezing.
  REVIEW.md states that narrower record.
- The first consultation used $\rho=j^4$; the final specification uses
  $\rho=j^2$. Their contact factors must not be quoted without that distinction.

## E6. Boundaries that a summary must retain

Off-target rejection in the fixed five-channel bank requires $c\notin2O$.
For the different family $(a,a+2c,0)$, the first contact is always admitted;
resonance is the condition for admission of the second contact together with
signal return. These are different statements.

With a discharged helper and an occupied record, the correct subsequent
state is
$$
x'=(1+\rho^2)c\rho^m,\qquad z'=(1-\rho^2)c\rho^m,
$$
as in the preserved proof and scripts. It is not
$(-\rho^{m+1}c,c\rho^m)$.

The finite odd-seed inventory contains the 80 nonzero elements of
$\{-1,0,1\}^4$ plus $(-1,-2,-2,0)$, making 81 seeds.
The declared free-mode pairs are $(a_0,b)=(5,4),(7,6)$.
The constant-quantum share identity assumes a fixed odd seed, prescribed
resonant arrivals, fresh record slots and helper recharge or fresh banks.
It provides no distribution for the arrival counts.
