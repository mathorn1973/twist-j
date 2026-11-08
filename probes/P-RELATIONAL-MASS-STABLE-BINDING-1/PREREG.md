# P-RELATIONAL-MASS-STABLE-BINDING-1

Status: PROSPECTIVE, NON-CANONICAL, NEW_DECLARED L1
Owner: A. M. Thorn, session relational-mass-stable-binding-2026-10-20
Ownership: https://github.com/mathorn1973/twist-j/issues/1688
Base: 8a2e6a3b1f35bfc2e2616c340086a7182ffbc050

## Question, carrier and new choice

Continue the common action of #1687 with a genuine relative-position
interaction. Two occupied groups have unit multiplicity and total P=0.
Their center is fixed; r=(x1-x2)/2 and rho=2p1=-2p2 are a canonical pair.
G is a real SPD symmetric inverse metric, Pi symmetric, and rho is nonzero.
Use Frobenius pairing, including both off-diagonal entries, and declare

    theta=tr(Pi dG)+rho^T dr,
    K=tr(G Pi G Pi)/2, E=sqrt(rho^T G rho),
    V=kappa r^T G^-1 r, H=K+E+V, kappa>0,
    S=integral [theta(zdot)-H]dt.

The positive harmonic proper-separation potential and kappa are NEW choices.
E is exactly the sum of the two individual massless energies. Antipodal
momenta belong to the continuously varied ambient carrier of #1687, not
to its marked five-direction catalogue. No native realization or physical
calibration is inferred. SOURCE.md records authority and occupied lanes.

Write R=G^-1. The equations to derive and audit are

    Gdot=G Pi G,
    Pidot=-Pi G Pi-rho rho^T/(2E)+kappa R r r^T R,
    rdot=G rho/E, rhodot=-2 kappa R r.

Define J=2G Pi+r rho^T, delta=det(J)-(tr J)^2/4,
C=tr(G Pi), z=r^T rho, D=E^2 and d2=4r^T R r. The individual source
momenta evolve, so the previous constant-momentum completeness proof is
not silently reused. The new theorem supplies its own protection from zero.

## Prospective universal claims and stability scope

PROOF.md proves the common variation, GL(2) covariance, H and J conservation,
and exact exchange. With

    A=rho^T G Pi G rho/(2E), B=kappa r^T Pi r, W=2kappa z/E,

the balances are Edot=A-W, Vdot=W-B, Kdot=-A+B,
Cdot=-E/2+V and zdot=E-2V. No metric-only GL-congruence-invariant potential
can bind this carrier: congruence is transitive on SPD, so it is constant.

For the open elliptic sector delta>0, the sharp algebraic inequality is
E^2 V>=4kappa delta. Consequently, on a fixed energy surface H=h0,

    E >= 2sqrt(kappa delta/h0)>0,
    16delta/h0^2 <= d2 <= 4h0/kappa.

Energy bounds on the metric kinetic term and the positive energy floor
give unique complete smooth flow for all real time. These bounds describe
proper pair separation and remain uniform under perturbations with delta
bounded below and H bounded above inside the fixed two-group P=0 sector.
They do not assert coordinate-distance bounds, uniformly bounded G,
arbitrary small-P robustness, necessity of delta>0, or orbital stability
merely from bounded separation. At Pi=0, delta=-(r^T rho)^2/4<=0; the
certified sector requires nonzero metric momentum already in its initial data.

A stronger, separately proved statement fixes tr J=0 and delta>0. With
y=G^-1/2 r, q=G^1/2 rho, a=|y wedge q|/2>=sqrt(delta), the sharp lower bound is

    H >= f(a)=3 kappa^(1/3) a^(2/3)
                  +(a-sqrt(a^2-delta))^2/4.

Its minimizer is unique. Setting u=sqrt(1-delta/a^2), its equation is
delta^2(1-u)^4=64kappa u^3(1+u)^2. The left side decreases and the right
side increases on (0,1). For the specific kappa=3 and J=J* example below,
equality, compact energy sublevels after quotienting the fixed-J* centralizer,
and the energy minimum give nonlinear Lyapunov stability modulo that group
on the exact J=J* level. This is not ordinary
stability of one coordinate-radius orbit or stability under arbitrary-J
perturbations. Neutral scale is an exact symmetry, not a dissipative mode.

The exact periodic example is fixed prospectively at

    kappa=3, G=I, Pi=[[0,-1],[-1,0]], r=(1,0), rho=(0,6),
    J=[[0,4],[-2,0]], delta=8,
    K=1, E=6, V=3, H=10, D=36, d2=4,
    Omega=[[0,-2],[1,0]]=-J/2, Omega^2=-2I.

For A(t)=exp(t Omega), the exact solution is
G=A A^T, Pi=A^-T Pi0 A^-1, r=A r0, rho=A^-T rho0. Its full labeled
period is sqrt(2)pi. It attains the minimum at a=3,b=sqrt(a^2-delta)=1,
u=1/3. Kappa=3 is an explicitly chosen simple member of the positive
coefficient family, not a derived physical constant. No stable-particle,
Lorentz, continuum, native-U or cross-layer claim is introduced.

## Exact finite audit

All finite calculations use rational arithmetic, no floating point, tolerances,
numerical trajectories or outcome tables. The universal theorem is real.
Both programs independently calculate formal FLOW series through degree four.
Initial E roots are given below and must be checked by positivity and squaring.
Formal roots are expanded about those positive roots. All state and invariant
coefficients, including zeros and nonzeros, are computed before serialization.

The main box, in the following outer-to-inner order, is:

    ki: kappa in (1/2,1,2),
    ri: r in ((1,0),(2,0)),
    qi: rho in ((0,1),(0,2),(0,-2),(3,4),(3,-4)),
        respective initial E in (1,2,2,5,5),
    bi: Pi in the following seven matrices:
        0 [[0,0],[0,0]],
        1 [[0,-1/2],[-1/2,0]],
        2 [[0,1/2],[1/2,0]],
        3 [[1/2,-1/2],[-1/2,0]],
        4 [[0,-1/2],[-1/2,-1/2]],
        5 [[1/2,-1],[-1,-1/2]],
        6 [[-1/2,1],[1,1/2]].

Initial G=I for all 210 cases. Include every case, regardless of delta sign.
Classify its computed delta0 as POS, ZERO or NEG, and derive the three
counts; require they sum to 210 and each is positive. Only POS cases are
within the global-binding theorem. The other cases are legitimate local
formal audits and do not establish a nonbinding theorem.

For every case:

- Compute G,Pi,r,rho and inverse G through degree four; verify symmetry,
  initial data, matrix inverse and root identities at the full order.
- Check all vector-field equations through degree three. Compute actual
  K,E,V,D,d2,C,J,delta and gap=E^2 V-4kappa delta at degrees 0..4.
- Check all positive-degree H,J,delta coefficients vanish. Check the three
  energy exchange equations and Cdot,zdot through degree three.
- Check D=E^2, d2=4V/kappa and tr J=2C+z at the full order.
- With Q=tr(G^-1 J G J^T), check the exact full-order identity
  gap=kappa[z^2+tr(J^2)+Q-(tr J)^2]. At the initial point verify gap>=0.
  For POS cases also verify E0^2 H0>=4kappa delta0,
  d2_0 H0^2>=16delta0, d2_0<=4H0/kappa, and E0>0.
- Check initial directional derivatives of the actual perturbed H in each
  symmetric G and Pi direction E00,E11,[[0,1],[1,0]], and both component
  directions of r and rho, against the Hamilton gradients above. Compute
  derivatives from perturbed expressions, not inserted gradient values.

There are 1050 main coefficient rows. No finite truncation is interpreted
as a proof of long-time binding or nonlinear stability.

## Covariance, periodic orbit and minimum checks

Use two main base indices (ki,ri,qi,bi), in order:
(1,0,1,1), then (2,1,2,6). For each use, in order,

    A0=[[1,1],[0,1]], A1=[[0,1],[1,0]], A2=[[2,0],[0,1]].

These are six covariance cases c=0..5. Transform every actual state
coefficient as G'=A G A^T, Pi'=A^-T Pi A^-1, r'=Ar, rho'=A^-T rho.
Re-evaluate the equations and invariants on the transformed coefficients;
check K,E,V,D,d2,C,delta,gap unchanged and J'=A J A^-1. No separate
trajectory solver is required for transformed cases.

For the periodic example above, independently solve FLOW through degree four
and compare every state coefficient with the group solution obtained by
expanding exp(plus/minus t Omega) through that order. Check the infinitesimal
group equation directly at the initial point as well as Omega^2=-2I.
Check the actual K,E,V,D,d2,C,J,delta and gap. K,E,V,D,d2 are individually
constant on this special orbit; C=0. Compute their values, do not substitute
the predicted constants into the serialized trajectory.

For the minimum test, verify a=3,b=1,u=1/3, b^2=a^2-delta,
the stationary polynomial, (E+V)^3=27kappa a^2, and the equality conditions
z=0, |y|=1, |q|=6, symmetric-part alignment at G=I. Differentiate the
one-variable lower bound algebraically at that point: f'=0 and f''=88/9.
Use b'=a/b and c=(kappa/a)^(1/3)=1 there, so these are rational formulas.

Also compute the displaced fixed-J state at kappa=3, G=I, Pi unchanged,
r=(2,0), rho=(0,3). Check J and delta unchanged, H=16>10. This is an
energy comparison, not an asserted second periodic orbit.

## Eight negative controls

Each control detects an exact discrepancy in a declared false alternative.
Control-only states are explicit additions to, not changes of, the main box.

1. NC01: G=I,Pi=0,r=(1,0),rho=(3,4),kappa=1. Omit both binding forces
   but retain V in the energy account. Compute actual Hdot=6/5 instead of zero.
2. NC02: G=I,rho=(0,2). Individual momenta are plus/minus rho/2 and their
   energies sum to E=2. Treating one individual energy as the pair energy
   incorrectly gives one. Check the normalization by direct norm squares.
3. NC03: the first covariance base and A=2I. Proper d2 and H are unchanged,
   while Euclidean coordinate separation squared is multiplied by four.
   This falsifies identification of proper and fixed-coordinate distance,
   not a theorem that any particular trajectory escapes in coordinates.
4. NC04: G=I,r=(1,0),rho=(0,2),Pi=0 gives delta=0; restoring Pi from
   main bi=1 gives delta=1. A source pair alone does not provide the certified
   elliptic charge when metric momentum is zero.
5. NC05: G=I,r=(1,0),rho=(0,2),Pi=I,kappa=1 gives delta=0, detJ=4.
   Replacing delta by detJ makes E^2 V>=4kappa detJ false.
6. NC06: the same state as NC05. Omit only +kappa G^-1 r r^T G^-1 in
   Pidot while keeping the source force. Compute actual Hdot=-1.
7. NC07: the full correct flow at NC01's state has Edot=-6/5, Vdot=6/5
   and Kdot=0. Separate conservation of the source energy is false.
8. NC08: the periodic minimum and displaced fixed-J state have the same
   delta=8 but energies 10 and 16. Ellipticity alone does not imply the
   minimum orbit or the stronger orbital-stability theorem's equality set.

## Implementation separation and deterministic payload

The two isolated authors receive only this contract and PROOF.md, plus
repository policy. Neither reads a companion or predecessor scientific
program. No common scientific module, expected digest or imported outcome
is permitted. Primary: Python Fraction arithmetic, triangular Taylor
coefficient recursion y_m=rhs_(m-1)/m, binomial roots and adjugate/determinant
matrix inversion. Breaker: independently written normalized integer-pair
rationals, four formal Picard passes, root-square recurrences and matrix
inverse coefficient recurrence. Both are standard-library-only.

Serialize every rational as a reduced integer or numerator/positive
denominator, matching Fraction string form. Arrays are comma-separated,
matrices row-major, vectors component order. All records are ASCII and LF
terminated. Construct and hash the payload in memory; do not write it.

The thirteen state fields, in order, are

    G(4)|Pi(4)|r(2)|rho(2)|K|E|V|D|d2|C|J(4)|delta|gap.

First emit the 18 reference records in this order:

    G|<I>
    B|<bi>|<Pi>                     # seven bi=0..6
    Q|<qi>|<rho>|<E0>               # five qi=0..4
    R|<ri>|<r>                      # two ri=0..1
    K|<ki>|<kappa>                  # three ki=0..2

For each of the 210 main cases in declared nested order emit

    C|<ki>|<ri>|<qi>|<bi>|<kappa>|<delta0>|POS/ZERO/NEG
    S|<ki>|<ri>|<qi>|<bi>|<m>|<thirteen state fields>

Emit all five S rows m=0..4 before the next case. Then each covariance case:

    A|<c>|<ki,ri,qi,bi>|<A>
    Y|<c>|<m>|<thirteen state fields> # five m=0..4

Finally emit

    W|3|<Omega>|3|1|1/3|88/9
    T|<m>|<thirteen actual periodic-state fields> # five m=0..4
    F|RADIAL_DISPLACEMENT|<thirteen actual displaced-state fields>
    N|NC01|DETECTED
    ... through N|NC08|DETECTED.

The record count is 18+210*6+6*6+6+1+8=1329. The common certificate is
exactly 18 LF-terminated lines, all counts derived and checked:

    CERTIFICATE=P-RELATIONAL-MASS-STABLE-BINDING-1
    AUTHORITY_FILES=5
    COUPLINGS=3
    SEPARATIONS=2
    MOMENTA=5
    METRIC_MOMENTA=7
    TRAJECTORY_CASES=210
    ELLIPTIC_CASES=<computed POS count>
    PARABOLIC_CASES=<computed ZERO count>
    HYPERBOLIC_CASES=<computed NEG count>
    FORMAL_ORDER=4
    COEFFICIENT_ROWS=1050
    COVARIANCE_CASES=6
    PERIODIC_CASES=1
    NEGATIVE_CONTROLS=8
    PAYLOAD_RECORDS=1329
    PAYLOAD_SHA256=<computed lower-case SHA-256>
    CERTIFICATE_RESULT=PASS

breaker.py emits only the common certificate on success. verify.py first
constructs it independently, then invokes its sibling with the same Python
interpreter and -I, no shell, closed standard input, a fixed minimal
environment with the deterministic settings below, captured stdout/stderr
and a 540-second timeout.
Require zero exit, empty stderr and raw certificate byte identity. Only
then emit the common certificate followed by

    BREAKER_RAW_BYTES=IDENTICAL
    RESULT=PASS

The outer primary budget is 600 seconds. Neither program reads expected
stdout, RUN/RESULT/REVIEW text, network, secrets or scientific predecessor
code. Apart from launching the breaker, runtime input reads are limited to
the five fixed authority files below. No scientific filesystem writes.

## Authority, falsifiers and pin

Both programs verify exact bytes and SHA-256 before computation:

    canon/CANON.md 1052518 d87657aeccc568dd668718fb9cbea6136643e5db32dd4e289a4de328e64f824b
    canon/CORE.md 30714 9d5617a163bc7a4e1964d41861ff7f2f44009117c61debe08a4e1547c88be728
    canon/FRONTIER.md 27382 8574c3d4b0cc70278dec7d64e2a51022718cc54497c64025d9e6021775fcbaf0
    canon/REGISTRY.tsv 532811 5cd008147435bf1facfe93b2e05d9d7e41554d73f647ad09659aac002195890d
    canon/CHANGELOG.md 207770 79f6bd8f30b1f845ae918b7374049f4bf8e0a2270e89b4c5223469a93855f078

One exact discrepancy fails. Explicit audit failures exit zero and emit

    FALSIFIER=<first failing code>
    RESULT=FAIL

Codes: F01_AUTHORITY, F02_GEOMETRY, F03_FLOW, F04_EXCHANGE,
F05_CHARGE, F06_BOUND, F07_COVARIANCE, F08_PERIODIC,
F09_MINIMUM, F10_NEGATIVE_CONTROL, F11_PAYLOAD, F12_BREAKER.
Breaker nonzero exit, stderr, timeout or certificate mismatch is F12_BREAKER
in a completed primary run. Unexpected primary exceptions remain uncaught
and mean an incomplete abandoned pin, not a scientific FAIL or PASS.

Before ANY scientific execution, import or finite fixture evaluation,
commit and push PREREG.md, PROOF.md, SOURCE.md, verify.py, breaker.py and
FROZEN.sha256. The manifest binds the other five files. Fetch all six
complete public files at the immutable pin, compare bytes/blob identities,
post and read back a public receipt, then run from the clean exact pin:

    python3 probes/P-RELATIONAL-MASS-STABLE-BINDING-1/verify.py

Use LC_ALL=C, LANG=C, PYTHONDONTWRITEBYTECODE=1, PYTHONHASHSEED=0,
TZ=UTC. Source reading, analytical derivation, AST parsing and byte/hash
checks are allowed beforehand; no scientific dry run is allowed.

After a completed run add EXPECTED.txt, RUN.md, RESULT.md, REVIEW.md and
README.md with neutral platform, Python/architecture, command, pin,
start/end, exit, byte counts and hashes. Keep completed FAIL unchanged.
An incomplete pin consumes the identifier and requires abandonment without
EXPECTED/RUN; no repair or resume. Required x86_64/aarch64 byte-identical
replay, policy/Canon/ledger/gate checks, security review and preserved pin
ancestry are merge gates. No outcome changes the model, domain, thresholds
or proof scope, and no result promotes Canon without a separate public fold.
