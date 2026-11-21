# Two overlapping contacts under one Hamiltonian law

NON-CANONICAL / L1. P-OVERLAPPING-CONTACT-WORK-CLOCK-1.
Owner: A. M. Thorn, overlapping-contact session 2026-11-05.
Public reservation: #1914.

## 1. Equation and analytical contract

Use O=Z[j], Phi_5(j)=0, rho=j^2 and Q(a)=Tr(a*conjugate(a))/2. For three
labelled slots z=(x,y,z3), the total contact C_e applies the admitted linear
rotation only when the pair difference belongs to 2O; otherwise it is identity.
The target is the chronological composition C12 followed by C23, with one
shared bank and clock, and one counted canonical controller pair reset after
each contact. The data generally do not return after one two-contact block.

Freeze R=sum Q, I=Q(x-y)+Q(y-z3), controller coordinates (q,p), and

    C_ctrl=4*((q-1/2)^2+p^2), E_lambda=R+lambda*I+C_ctrl,
    H=E_lambda+b, lambda>=0.

The prepared domain has z in O^3, (q,p)=(0,0), clock phase0, and
b>=lambda*(3R-I). For integer snapshots lambda,b are nonnegative integers.
This is a declared funded domain, not a HOLD policy for insufficient funds.
The exact identity 3R-I=Q(x+y+z3)+Q(x-z3) supplies a uniform whole-path bound.

The new real completion uses the same primitive per-site form as #1910,
one canonical controller form dq wedge dp, and a circle clock of period6tau.
For the four power coefficients of a pair difference, select

    f_e(z)=product_c (1+cos(pi*(z_i,c-z_j,c)))/2,
    g(q)=(1-cos(pi*q))/2,
    K(q,p)=(pi/2)*((q-1/2)^2+p^2).

On every integral data state f_e is exactly its admission Boolean and has
zero gradient. On controller bits0,1, g is the bit and g'=0. Six disjoint
smooth unit-area pulses generate compute12, contact12, uncompute12,
compute23, contact23, uncompute23. Compute/uncompute use f_e*K; contacts use
g(q)*h_e, where h_e is the unit-time phase generator specified in PROOF.md.
The pulse sequence defines one periodic smooth function h(z,q,p,t).

Freeze the full form and Hamiltonian once:

    B=b+E_lambda-h, Omega=omega+dq wedge dp+dt wedge dB,
    H=E_lambda+b=B+h.

In product coordinates the equations include dot t=1 and dot B=-partial_t h.
The resulting bank equation is dot b=-dE_lambda/ds. The proof must establish
exact control, the overlapping-contact endpoint, controller reset, inverse,
whole-path funding and arbitrary repeated blocks on the prepared family.
It also identifies the failure of naively reusing the isolated-pair form,
a stale-parity counterexample, and the remaining free work coefficient.

## 2. Accepted code and exact audits

verify.py and checker.py use only the Python standard library. The primary
route uses four j coefficients; the independent checker uses four u=1-j
coefficients, polynomial reduction and the trace Gram form. Both routes
check complete three-slot/controller snapshots and exact bank payments.
No predecessor executable is imported. All assertions use integers or
Fractions; transcendental continuous-flow claims require the written proof.

The finite audit checks contact and half-step matrices, symplectic and Q
preservation, contact fifth powers, half-step tenth powers and exact inverse.
It checks the generic extended-form/Hamilton equation with formal gradients,
including the time derivative in product coordinates. Boolean selector
values and critical-point identities are checked in their exact endpoint
algebra; no floating-point trigonometric evaluation is evidence.

At each of six pulse types, inspect the endpoint and its half-area midpoint.
For an admitted contact the midpoint multiplier is -j; in the inverse it is
(-j)^(-1). Compute/uncompute midpoints have q=1/2,p=+/-1/2 when active.
A sampled half-window is also half pulse area by the fixed symmetric profile.
Clock snapshots use twelve half-window labels; the actual clock is continuous.
Continuous nonnegative funding is proved analytically, not inferred from
these samples.

## 3. Frozen finite family

Use all 343 ordered triples from

    S={0,1,2,u,-u,B0,-B0}, u=1-j, B0=1-j^2.

For every triple and lambda in {0,1,2,7}, take the distinct banks

    beta=lambda*(3R-I), beta+1, 72*lambda.

All are funded: R<=24 on this family, so the common bank72lambda suffices.
Execute two consecutive six-pulse blocks and their complete reverse, checking
all midpoint/endpoint states, controller readiness, R/C_ctrl/H, bank
nonnegativity, fresh pair admission and complete inverse recovery. Emit
deterministic counts and hashes of the audited records.

Additionally freeze these exact witnesses:

- (2,0,0): the second-pair parity changes from admitted to refused after C12;
  using the old tag would produce a nonintegral admitted-branch output.
- (2,0,B0): the second-pair parity changes from refused to admitted after C12.
- (2,2,0): the C23 endpoint changes the first-pair phase generator, exhibiting
  the defect of reusing the isolated C12 form.
- (u,-u,-j*u): the first contact has I=35,40,35 at start/midpoint/end.
  An endpoint-only bank0 misses the interior debit5lambda; the safe uniform
  guard here is10lambda. This concerns that first contact's chosen path.
- (2u,-2u,2u): both contacts are active, with R=60 and successive I values
  160,120,135. A common initial bank60 is funded for lambda=1,2 and should
  end at85 and110, while the projected data/controller/clock motion agrees.

These values are analytical pre-pin predictions, not results of a prior
scientific run. There is no search, optimization, random seed, data fitting,
external data dependency or adaptive budget. The existing 600-second timeout
is operational only.

## 4. Systematics and prospective custody

The exposed predecessor #1910, source pin
bf0d4e2c187e79daa66dc22950d38667463a965b and result head
afbafb9c84f93d4a7ea544ef08ec6c05c8467db0, explicitly leaves overlapping
contact control open. Its form/flow and funding-bound arguments were read
before this probe; they are attributed inputs. #1912's fixed-word integer
domain is known but is not used in this construction.

Commit and push PREREG.md, PROOF.md, PROVENANCE.md, verify.py and checker.py;
read back their public contents, Git blobs, bytes and SHA-256 before the first
execution or import. Static inspection and AST parsing are permitted before
the pin. Then use a clean Linux-compatible checkout, assertions enabled,
LC_ALL=C, LANG=C, TZ=UTC, PYTHONHASHSEED=0 and PYTHONDONTWRITEBYTECODE=1:

    python3 probes/P-OVERLAPPING-CONTACT-WORK-CLOCK-1/verify.py

Preserve first stdout as EXPECTED.txt and record the source pin, all hashes,
command, neutral environment and output sizes in RUN.md. Only EXPECTED.txt,
RUN.md and RESULT.md may be appended after the pin. No silent correction,
threshold change or outcome-changing retry. The existing CI reproduces the
same verifier and exact stdout on x86_64 and aarch64.

## 5. Failure thresholds and disposition

Any failed exact matrix, coefficient, invariant, control, bank, inverse,
Hamilton identity or named witness fires the corresponding verification
falsifier. Completed diagnosed mathematical failure is emitted as F and
preserved with exit zero. Input/source custody errors, unexpected exceptions
or timeout are execution/integrity failures, not mathematical no-go results.
A failed construction rejects only this route and its frozen scope.

Passing finite audits alone gives at most candidate-C on one architecture.
Byte-identical x86_64/aarch64 output satisfies the computation gate at the
stated finite scope. The universal conditional claims require PROOF.md and
independent review; finite samples are not extrapolated into their proof.
No result automatically changes the Canon or establishes physical meaning.

## 6. Action layer and boundaries

L1 only. The real extension is an explicitly added mathematical carrier,
not a registered cross-layer physical reading. Its canonical controller,
coefficientwise cosine selectors, selected positive contact phase representatives, smooth pulse
profile, clock scale and energy-dependent full form are declared choices.
Intermediate points need not be integral. The controller contributes its
account1 at readiness and throughout the prepared trajectory.

The nonnegative-bank guarantee is for funded integral/ready preparations
and their trajectories, not arbitrary real or off-ready states. No complete
underfunded HOLD law, native-U implementation, physical action quantum,
electromagnetic coupling, alpha value or minimal-resource claim is included.
Changing lambda changes the full form even when the on-shell action agrees.
Predecessors, Canon, registry and workflows remain unchanged.
