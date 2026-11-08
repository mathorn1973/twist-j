<!-- SPDX-License-Identifier: Apache-2.0 -->

# C-COLOCATED-RESONANT-RECORD-TWO-PLACE-ACCOUNT-N

**NON-CANONICAL / L1.** Conditional analytical results are proposed as
candidate-T; the finite audit remains candidate-C on one x86_64 architecture.
Independent scientific acceptance is pending.

This public intake was prepared after the original local execution. Read
[PUBLICATION.md](PUBLICATION.md) for the byte mapping and
[ERRATA.md](ERRATA.md) for corrections to the original summaries and one
intermediate sign in the preserved proof. The preserved PREREG.md is an
original local preregistration, not a prospective public pin.

## Exact result

Fix $O=\mathbb Z[j]$, $1+j+j^2+j^3+j^4=0$, $\rho=j^2$,
$J=1+\rho$, and $\phi=-j^2-j^3$, so $\phi^2=\phi+1$.
Write $h(c)=c\bar c=A_c+B_c\phi$ and $Q(c)=2A_c+B_c$.

The two conjugate contact factors satisfy
$$
Q((1-j^2)c)=5(A_c+B_c),\qquad Q((1-j^4)c)=5A_c,
$$
and their sum is $5Q(c)$. The two terms are equal iff $B_c=0$;
then each is $\frac52Q(c)$.

On the co-located Gauss carrier, $F=-x$ and a contact with a slot $v$
is admitted exactly when $d=(v-x)/2\in O$. Its current is
$i=(\rho-1)d$, and it updates $(x,v,F)$ to $(x-i,v+i,F+i)$.
An untouched neutralizing companion supplies the other Gauss equation.
The complete scalar account is $2(Q(x)+\sum_{v\in B}Q(v))$.

For $c\ne0$, the two-contact word $C(x,z)\circ C(x,h)$ on
$(a,a+2c,0)$ admits its second contact and restores $(x,F)=(a,-a)$
iff $a=Jc$. At resonance,
$$
(Jc,(3+\rho)c,0)\longmapsto(2c,2Jc,0)
\longmapsto(Jc,2Jc,(1-\rho)c).
$$
The helper pays for the record:
$$
h((3+\rho)c)=h(2Jc)+h((1-\rho)c).
$$

For $c\ne0$, a fixed bank of five phase channels leaves all off-target helpers
and records untouched, writes the target record and restores the signal for all five
resonant inputs iff $c\notin2O$. This uses
$O/2O\cong\mathbb F_{16}$. Each click deposits the same
$w_0(c)=5(A_c+B_c)>0$.

For the selector in [PR #1957](https://github.com/mathorn1973/twist-j/pull/1957),
$$
c=(1-\rho)J^{-1}=-1-2j-2j^2=(-1,-2,-2,0),\qquad h(c)=3+4\phi.
$$
Consequently $Q(c)=10$, the helper drops from $55$ to $20$, and the
record quantum is $35$. The two-selector port gives $(0,35)$ and $(35,0)$
for its two declared input states. This audit does not replay the complete
predecessor paths.

## Scope and boundaries

For a fixed odd seed, prescribed resonant arrivals and a freshly prepared
bank at each event, cumulative record shares equal event-count shares:
$$
\frac{W_{\mathrm{rec},k}}{\sum_iW_{\mathrm{rec},i}}
=\frac{N_k}{\sum_iN_i},\qquad \sum_iN_i>0.
$$
The same equality holds for the two-place Hermitian account. It is a
conditional constant-quantum identity, not an occurrence-probability law.

Repeat operation needs a fresh record slot and helper recharge. A discharged
helper with a blank record refuses both contacts. Leaving the old record in
place instead produces
$$
x'=(1+\rho^2)c\rho^m,\qquad z'=(1-\rho^2)c\rho^m.
$$
The two declared rational free modes have reduced denominators $2\cdot4^n$
and $2\cdot6^n$ for $n\ge1$; primitive integral polarizations therefore require
finite-horizon scaling.

No Born rule, autonomous preparation/recharge mechanism, native-U
implementation, physical action scale or coupling selection is derived.

## Evidence

- [PROOF.md](PROOF.md), read with [ERRATA.md](ERRATA.md): preserved analytical argument.
- [PREREG.md](PREREG.md): preserved local source contract.
- [SOURCES.md](SOURCES.md): public source pins and self-contained premises.
- [RESULT.md](RESULT.md) and [RUN.md](RUN.md): exact finite scope and replay record.
- [REVIEW.md](REVIEW.md): limits of model consultation and the present review.
- [PUBLICATION.md](PUBLICATION.md): original-to-intake file mapping.
- [SHA256SUMS](SHA256SUMS): this intake's file hashes.

Both unchanged scripts exit zero with empty stderr and report 676464 checks.
On Windows their raw outputs agree with each other but use CRLF (585 bytes).
Conversion of those nine line endings to LF gives the committed 576-byte
outputs exactly. This conversion is explicit; raw byte identity with the
committed files is not claimed.
