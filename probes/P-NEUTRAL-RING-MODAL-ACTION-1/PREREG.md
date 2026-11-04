# P-NEUTRAL-RING-MODAL-ACTION-1

NON-CANONICAL / L1 / exact proof and finite audit.
Owner: A. M. Thorn, neutral-ring-modal-action-20261104.
Reservation: https://github.com/mathorn1973/twist-j/issues/1893.
Base: ACTIVE Public Canon v109, main
650029c20408f1dd665983d72225d0d195fd030e.

## 1. Question and prospective boundary

Can the same admitted integral contact be given an explicit arithmetic
discrete action, and what modal energy and common-action choices remain?
The analytical expectations below were exposed before this pin. This is
an audit of explicit constructions and proofs, not a blind discovery.
The previous sealed receiver probe is an input, not resumed work.

Before any scientific execution, commit and push all seven source files:
PREREG.md, README.md, PROVENANCE.md, SOURCES.tsv, ENERGY.md, ACTION.md and
verify.py. Read back their exact bytes at the public commit and record
hashes. Only source inspection, syntax parsing and metadata checks are
allowed before that pin. Thereafter their bytes and thresholds are frozen.
After a completed genuine run add only EXPECTED.txt, RUN.md and RESULT.md.
A failed pin is preserved under the governing disposition rules; it is
never repaired or reused under this identifier.

## 2. Carrier and equations

Let O=Z[j], Phi_5(j)=1+j+j^2+j^3+j^4=0, p=j^2, a=1-j and u_k=a*p^k.
Use coefficients in (1,j,j^2,j^3) and

    Q(x)=[5 sum x_i^2-(sum x_i)^2]/2,
    H(x)=x conjugate(x).

The total contact is

    C(x,y)=(x,y)                         if x-y not in 2O;
    C(x,y)=((x+y+p(x-y))/2,
            (x+y-p(x-y))/2)             otherwise.

Its inverse uses p^(-1)=j^3 on the same admitted branch. Define
I_plus=Q(x+y)/2 and I_minus=Q(x-y)/2. ENERGY.md proves their invariance,
the common quadratic-cost classification and the funded bank extension.
ACTION.md specifies Omega0, B, M and G and proves their identities and
the rational Q-flow obstruction. Those proofs state their full scope;
finite samples do not establish universal impossibility claims.

verify.py imports only fractions and itertools. It reads no data or
other verifier and uses no float, empirical constant, random seed or
fitted tolerance. All scientific tests are guarded by main().

## 3. Frozen finite audit

### Modal accounts and signed contact controls

For sign in {-1,+1}, c in {-3,-1,1,3}, k,r in {0,...,4}, test
(sign*u_k,c*u_r). There are 200 cases: 40 matches and 160 refusals.
Admission must be exactly k=r. Check complete sum, H and Q conservation,
both modal accounts, C^5=I and both inverse directions. Output power-basis
coefficients must have absolute value at most 12 in this family.

On a match require

    (I_plus,I_minus)=(5(sign+c)^2/2,5(sign-c)^2/2),
    Q(output_1)=Q(output_2)=5(1+c^2)/2,
    source Q gain=5(c^2-1)/2.

The Hermitian source gain must equal the scalar 5(c^2-1)/4 in O, so each
embedding has that exact gain. On a mismatch require full state identity.
At sign=+1, all five phases must give the modal pairs (40,10), (10,40),
(0,10) for c=3,-3,-1 respectively, with Q gains 20,20,0. These are fifteen
mandatory controls. Also test the ten pure-mode states (u_k,+/-u_k):
each has total Q=10, the symmetric one is fixed, and the antisymmetric
one rotates by p. The equal-amplitude native energy gap is zero.

### Common Hermitian-cost finite audit

For each path of size N=2,3,4,5, form every adjacent-edge rational
projector P=(e_i-e_j)(e_i-e_j)^T/2. Solve all commutator equations exactly
by rational row reduction, separately on the real symmetric and imaginary
skew-symmetric bases of Hermitian matrices. Require symmetric nullity 2,
skew nullity 0, and every computed symmetric kernel matrix equal to
A I+D11^T. Check I and 11^T themselves against every edge. The proof for
all connected graphs is analytical; these four paths are a finite audit.

### Primitive form and discrete action

Check Omega0's Pfaffian and determinant are 1, det(B)=-1, B^(-1) integral,
B^T Omega0 B=J, B^(-1) P B=M, and preservation of Omega0, J and the Q Gram
matrix (5I-11^T)/2 under the appropriate maps. Both P^5 and M^5 must be I;
P's four columns must agree with actual multiplication by p in O.

For all 625 old Darboux vectors (q1,q2,pi1,pi2) in {-2,-1,0,1,2}^4,
apply M and evaluate the displayed quadratic G(pi,q'). Exact central
differences of this degree-two polynomial must give q=-partial_pi G
and pi'=-partial_q' G. Require 2G integral with parity q2 modulo 2,
exactly 250 half-integral G values, |2G|<=44 and output coordinates of
absolute value at most 6. Compare Q evaluated in O with its transformed
Gram matrix, including positivity on this finite family. No transcendental
flow, logarithm or quantum phase is numerically evaluated.

### Funded interaction extension

Use triples v=(x,y,z), F=C_12 and

    E_lambda(v)=Q(x)+Q(y)+Q(z)+lambda Q(y-z).

For bank b>=0 and direction d in {-1,+1}, propose F^d v and debit its
energy increment. If the resulting bank would be negative, keep v,b and
flip d. Inverse uses the opposite travel direction with the same rule.
This is a new declared bank extension, not a native-contact compilation.

Freeze lambda in {1,2}, v=F^stage(u_k,-u_r,u_r) for all 25 phase pairs,
stage in {0,1}, b in {0,5,10,20,40} and both directions: 1000 preparation
cases, with repeated states allowed. The initial interaction Q(y-z) is 10
exactly when stage=1 and k=r, and 20 otherwise. Take 20 forward steps
and then 20 inverse steps on every full state, for 20000 forward and
20000 reverse continuation steps. At each forward
step check left and right inverse and the direction-reversal conjugacy.
Reverse the saved history exactly. Check every visited site Q=5,
coefficient absolute values <=2, total E_lambda+b<=95 and 0<=b<=70.
At least one reflection must occur.

For each lambda separately require the explicit transition
(u,-u,u;0,+1)->(pu,-pu,u;10lambda,+1), where Q(y-z) falls 20 to 10.
Require an unfunded reverse attempt from (pu,-pu,u;0,-1) to reflect
without changing triple or bank, and check its inverse. These are four
explicit gain/reflection controls. No unique lambda is expected or fitted.

## 4. Failure threshold and retained scope

Tolerance is zero. Any failed identity, output or count, unexpected
admission, wrong modal account, nullity, matrix identity, action gradient,
positivity bound, bank conservation or inverse rejects the corresponding
finite expectation. Preserve all discrepancies. Do not change source,
thresholds or sampled families after the pin.

The seven stdout lines are emitted only after every audit succeeds.
Their fields report the frozen counts, controls and final PASS. A program
failure is not relabelled as a completed scientific conclusion.

The mathematical conclusions concern L1 only. The discrete action is for
the admitted branch; the complete parity gate lacks a derived global
variational selection rule. The funded account does not prove its energy
generates that action. The constant-rational-form obstruction concerns
an autonomous Q-flow, not every possible action or carrier. The
common-fixed-generator obstruction excludes neither scheduled controls
nor enlarged apparatus. No Planck quantum, physical energy calibration,
charged response, electron identification or alpha value is earned here.

## 5. Execution and custody

From a clean Linux checkout of the public pin run

    python3 probes/P-NEUTRAL-RING-MODAL-ACTION-1/verify.py

Use the unchanged 600-second limit, assertions enabled, LC_ALL=C, LANG=C,
PYTHONDONTWRITEBYTECODE=1, PYTHONHASHSEED=0 and TZ=UTC. Remove inherited
PYTHONOPTIMIZE, PYTHONIOENCODING, PYTHONUNBUFFERED and TWISTJ_EVIDENCE_DIR.
Save raw stdout/stderr without newline conversion.

RUN.md records the actual full pin, verifier hash, exact command, neutral
platform/architecture/Python, exit status, bytes, lines and SHA-256 values.
EXPECTED.txt is actual stdout, never a prewritten expected transcript.
RESULT.md separates finite evidence, analytical candidates and open
physical obligations. Open one draft PR changing only this probe directory.
Required x86_64 and aarch64 jobs replay identical source/output bytes.
Same-session review is disclosed and is not independent acceptance.
