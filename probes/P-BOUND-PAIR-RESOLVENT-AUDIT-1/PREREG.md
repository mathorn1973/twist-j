# P-BOUND-PAIR-RESOLVENT-AUDIT-1 prospective contract

**NON-CANONICAL / L1. Prospective execution contract.**

Author: A. M. Thorn <thorn@twistj.com>.
SPDX-License-Identifier: Apache-2.0.
Reservation: [#1816](https://github.com/mathorn1973/twist-j/issues/1816).
Owner: A. M. Thorn, the single continuing authorized session.

This contract freezes a new exact original-operator audit. The absolute
capture result of #1815 has already been seen. This is a disclosed
second derivation and different exact check, not a blind prediction or
external independent acceptance. No scientific execution of this new
verifier preceded its complete public pin and readback.

## 1. Authority, equation and purpose

```text
public authority:       mathorn1973/twist-j main
Public Canon:           v106
main / peeled tag:      a193e389fb1ddb0bdc89165b015c95a17eb1e425
content commit:         9242db4f040d67d9417eacd06612230b74248cff
Canon SHA-256:          52302c640033dd15d4a7a075cad16fa48b1473b7396d1f7413536a9ec45422e7
Canon bytes:            1370107
audit target:           PR1815 at 32306016908c0097650277aa416fc0152b2f81a4
conditional predecessor: PR1813 at 8298af04f7385ec24f61a1b7c84d861cae017529
branch:                 probe/P-BOUND-PAIR-RESOLVENT-AUDIT-1
probe path:             probes/P-BOUND-PAIR-RESOLVENT-AUDIT-1/
analytical path:        notes/C-BOUND-PAIR-RESOLVENT-AUDIT-N/
action layer:           L1 only
```

The new branch starts at this public main. Its original model and
source/event definitions are the three public homogeneous-capture proof
files identified by exact bytes, SHA-256 and Git blobs in SOURCES.md.
Neither draft predecessor becomes Canon by being audited.

The original free symbol is

\[
F(P,k)=\operatorname{diag}(w,z,z^{-1},w^{-1})\frac15
\begin{pmatrix}
1&2i&2i&-4\\2i&1&-4&2i\\2i&-4&1&2i\\-4&2i&2i&1
\end{pmatrix},\quad w=e^{iP},\ z=e^{ik}.
\]

The original contact is `W=Gamma F`, with phase `gamma=exp(-ig)` on
all four coins at relative site zero. The ports are
`A=(1,0,0,-1)/sqrt(2)` and `iB=i(0,1,-1,0)/sqrt(2)`.
The question is whether the complete contact resolvents used in #1815
follow from this original operator, with its exterior sheet and the
stated full scattering normalization.

The analytical targets are, with `d=-3/5`, `ell=2/5`, `v=cos(P)`,

\[
t=v-\frac52(\lambda+\lambda^{-1}),\quad
2q^2-tq+2=0,\quad R=t-4q,\quad x=\lambda/\gamma,
\]
\[
N=x^2-d(v+q)x+vq,\qquad
D=x^3-(\ell v+dq)x^2+(d+\ell vq)x-q,
\]
\[
f_A=2xN/D-1,\qquad
f_B=\frac{R+2(x-x^{-1})}{t+2(x+x^{-1})}.
\]

The physical root is the exterior analytic root
`q=-4/(5lambda)-8v/(25lambda^2)+O(lambda^-3)`. The written proof
derives its global continuation, the boundary/coarea and PV signs,
and the primary stationary-scattering convention conversion. The
finite executable checks the exact algebraic identities and the
first two direct return moments. These two kinds of evidence are
explicitly distinct.

## 2. Carrier/data, code and complete input inventory

The carrier, product coin, contact order and two source vectors above
are fixed. The capture core is

\[
C_{\rm core}=\frac15\begin{pmatrix}3&-4\\4&3\end{pmatrix}.
\]

The original pulse symbol, both pulse branches, all carrier labels,
receiver and memory/reference semantics are unchanged. The audit uses
formal phase variables; its universal identities specialize to
`g=2pi/5`. It introduces no measured or fitted constants, finite lattice
cutoff, momentum sampling, numerical integration or pointwise fit.

The sole scientific entry point, from the repository root, is

```text
python3 probes/P-BOUND-PAIR-RESOLVENT-AUDIT-1/verify.py
```

| Executable input | SHA-256 |
|---|---|
| `probes/P-BOUND-PAIR-RESOLVENT-AUDIT-1/verify.py` | `13934b6e27d91b9f74f426970e42fa3f093df32c18f870ffdbe34bc3c9b32c47` |

There are no helper modules, runtime fixtures, environment-controlled
parameters, command-line numerical overrides or external inputs. The
code imports only Python standard-library `fractions` and `itertools`.
All scientific objects are constructed inside `main()`. Neither
predecessor code nor its interval engine is imported or executed.

The complete new public pin also contains this PREREG and exactly these
analytical documents under the note path:

- `PROOF.md`: original-operator derivation and analytic conventions;
- `SOURCES.md`: immutable public source/dependency inventory;
- `FINITE_PROTOCOL.md`: separate analytical finite-source/readout
  approximation and the explicitly unresolved fixed-state time modulus.

All five files are publicly read back and hashed before the first
scientific execution. No file is required to contain its own hash.
The finite-protocol note is not a runtime input and its conditional
time certificate is not a computational gate in this probe.

## 3. Exact arithmetic and finite algorithm

Coefficients are `fractions.Fraction`; no binary floating point is
used. A sparse polynomial dictionary has exponent coordinates
`(lambda,w,z,gamma,q,i)`. The first four variables admit Laurent
powers. Powers of `i` are reduced by `i^2=-1`; `q` has nonnegative
integer degree. A quotient check explicitly computes the unique
degree-at-most-one remainder under the monic relation

\[
q^2-\frac{w+w^{-1}-5\lambda-5\lambda^{-1}}4q+1=0.
\]

Its recurrence is `q^n=(t/2)q^(n-1)-q^(n-2)`. There is no numerical
root choice in this reduction. Checks that require no q relation
are evaluated as ordinary Laurent-polynomial identities.

The code constructs the original 4 by 4 symbol, computes its determinant
by all permutations and its adjugate by 3 by 3 cofactors, then transforms
by the unnormalized Bell matrix `H` as `H^T adj H/2`. It extracts the
coefficients of `z^0,z^1,z^-1`, verifies no unsupported harmonics remain,
and forms the complete integrated numerator

\[
M=B_{\cos}N_0+(a-\Sigma)N_c,\qquad
\Sigma=-\tfrac25\lambda(\lambda^2-1)(t-4q).
\]

Here `a-Bcos*cos(k)` is the determinant obtained from the raw symbol.
The scalar denominator is `Bcos*Sigma`. Both left and right even
inverse identities are checked against this original adjugate, not
solely inside the proposed scalar formulas.

The direct moment routine enumerates two actual original lattice steps
from each real A/B vector. Streaming changes relative position by
`(0,-1,+1,0)` in the original coin order; the target at relative zero
receives `gamma`. Only after this path enumeration are its contact
moments compared with the large-lambda scalar expansion. The common
normalizing factor is one half. The i phase of the incoming iB vector
cancels in its diagonal expectation.

For the expansion checks, substitute
`q_small=-4/(5lambda)-8v/(25lambda^2)`. The A numerator residual is
required to vanish in every lambda degree at least 1, since its
denominator has order lambda cubed. The B residual is required to
vanish in every degree at least -1, since its denominator has order
lambda. These are precisely the two-moment comparisons through
`lambda^-2`; the analytic small-root remainder is supplied by PROOF.

The two scattering functions are treated as independent formal complex
numbers for the final identities. Their real and imaginary parts reuse
four otherwise unused variable names within those groups; q reduction
is not applied there. This is an algebraic change of labels, not an
assumption that F1 or F2 is a unit phase.

## 4. Frozen gates and failure threshold

There are **23 groups and 130 exact scalar conditions** in the accepted
code, counting both negative controls. The fixed groups are:

1. Unitarity of the original streaming/product-coin symbol.
2. Both raw adjugate identities.
3. The full determinant and original Schur factors.
4. The complete relative Laurent support of the raw adjugate.
5. Radical and integration identities modulo the q relation.
6. Both complete even contact inverse identities.
7. Odd separation and the BB cofactor derived from the original matrix.
8. The complete free odd Caratheodory function.
9. The all-coin contact determinant and A cofactor.
10. The complete interacting odd function.
11. The positive even continuum numerator.
12. The exact H/G representation in a gap.
13. The compact A identity at v=-1.
14. The compact A identity at v=1.
15. First and second return moments from the original lattice walk.
16. The small exterior root expansion through its second coefficient.
17. Scalar resolvent moments compared with the direct walk moments.
18. Negative control: the other radical sheet must violate the moment
    condition.
19. Negative control: omitting the contact phase must violate the direct
    first A moment identity.
20. The complete rank-two scattering determinant and transition matrix.
21. The denominator-cleared on-shell transition unitarity identity.
22. The complete-denominator positive identity.
23. Determinant, trace and unitarity of the original pulse symbol.

Every positive condition must have the identically zero exact remainder.
Every negative control must have a nonzero exact remainder. There is no
tolerance or numerical success threshold. A nonzero positive remainder
or zero negative-control remainder fires the frozen falsifier. The
executable prints the failing group, entry number, exact term count
and the first three lexicographically ordered nonzero terms where
present; it continues through the remaining fixed groups.

The completed disposition is **CERTIFIED** exactly when every condition
has the required zero/nonzero status, and **FALSIFIED** otherwise. Both
completed dispositions exit zero, write no stderr and retain their
exact stdout. A falsified algebraic target is not repaired by editing
the pinned code or redefining a threshold.

Ordinary programming exceptions, nonzero process exits, a timeout or
failure to produce a completed disposition are technical failures,
not completed scientific falsification. The consumed identifier then
receives the policy-required ABANDONED record without manufactured
EXPECTED or RUN files. Any successor requires its own reservation,
contract and public pin.

## 5. Systematics and interpretation limits

The explicit systematic risks are wrong basis/phase order, a lost
adjugate term, an erroneous branch of the radical, a contact update
applied to only one coin or with q evaluated at x, canceled/omitted
bound poles, a wrong PV sign, and a normalization or time-convention
error in selected scattering.

The original-matrix comparison addresses the algebraic route; the
written contour, spectral and stationary derivations address the
analytic parts. Exact identities modulo the q relation alone do not
select a physical sheet. Two moments alone are not a global analytic
continuation theorem. They also do not distinguish Gamma F from
F Gamma: those contact-compressed Green matrices agree by scalar
contact conjugacy. The ordered proof nevertheless starts with the
actual defining law.

The analytic pole proof retains all visible bound poles of the full
contact resolvent. This executable does not rerun the predecessor's
interval root census or numerical principal-value quadrature. A
passing audit supports the formula derivation at its stated scope;
it is not a second enclosure of P0 or acceptance of every line of
the predecessor interval implementation.

The source and selected event retain the original flat energy measure,
unconditioned standing-token total-momentum measure, bound projector,
positive right-moving pulse, spectral windows and complete memory
transfer. No selected channel replaces F1 or F2 in the denominator.
The primary stationary theorem is applied fiberwise; the homogeneous
undecomposed perturbation is not claimed globally trace class.

FINITE_PROTOCOL supplies explicit analytical approximation errors,
not a numerical scattering time or a native autonomous preparer.
Existing owners #1741, #1745 and #1749 remain distinct. The no-reciprocity
derivation and finite-source/readout lemmas are mathematical proposals
in the note; a CERTIFIED stdout applies only to the listed finite gates.

## 6. Prospective custody and completion

Before execution, compilation and static human/model review are allowed.
No scientific import, trial run, sampled numerical check or predecessor
replay is allowed to choose this audit's output. The accepted verifier
and all documents are committed and pushed together. Public readback
must precede the first scientific process start; exact bytes, hashes
and both times belong to the subsequent first-run record.

The first process is run once from a repository-root-shaped directory
materialized from the read-back pin, under deterministic UTF-8/C locale
settings, with a 600-second limit. Capture stdout, stderr and the
actual exit code without altering scientific bytes. Timing and
environment metadata remain outside scientific stdout.

After a completed clean disposition, add only EXPECTED.txt, RUN.md and
RESULT.md in this probe. The result records the actual scope and any
fired falsifier. Open a draft PR changing this one probe and its own
notes. The required x86_64 and aarch64 workflow jobs must reproduce the
same exact stdout and verifier hash. A replay confirms reproducibility;
it does not replace the first-run record or authorize a rerun to tune.

No post-pin amendment, rebase, force-push, scientific input change,
Canon edit, merge, release or physical particle identification is
authorized by this contract.
