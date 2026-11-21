# P-SOURCE-RANGE2-ENERGY-1 preregistration

**NON-CANONICAL. L1. Prospective exact finite certificate.**
Author: A. M. Thorn. Date: 2026-10-26. Apache-2.0.
Reservation: [#1786](https://github.com/mathorn1973/twist-j/issues/1786).
Branch: probe/P-SOURCE-RANGE2-ENERGY-1.
Promotion dossier: PROMO-P-SOURCE-RANGE2-ENERGY-1.

## 1. Authority, carrier and source pins

The sole authority is ACTIVE Public Canon v105. Public main and peeled
canon-v105 are 892a0b11089d34e241e1eb76d2c03247022d18e6; the content
commit is b8cdfd6ea58ae798545bc6000c817147fa0f0dcc. STATUS was read
first. POLICY, AGENTS, CORE and FRONTIER remain unchanged from their
complete preceding reads. All five normative hashes and required
architecture, aggregate and publication checks passed. A fresh explicit
remote scan contains 313 branch heads; current issues, branches,
notes/probes and registry were checked before reservation. Attachments
from the retired internal Canon line are not authority.

Use the exact original occupation model and receiver law of that Canon,
Q=E0f(U_rec), E0>0, f(exp(-i theta))=theta for 0<=theta<2pi, f(1)=0.
The original active source is PR1777 at
191ab035be823bd9d6fdc9effba81528fa026e49; its nominated logarithm
is pinned in PR1772 at 3abf054e435e31c51e6e50528b09fe3cf7cffe13.
The finite necessary-test derivation is PR1785 at
19f1c74a27684a22bf038c1e6fc1133f638fb613, FILTERED_TAIL.md (T12)-(T13).
That predecessor has no recorded external review at this reservation.
Its result and this test retain their conditional source premises.

    chi=|R=97,r=0,iB;c=97,token label0> tensor Xi,
    B=(e2-e3)/sqrt(2),
    psi_sigma=[I+sigma(U²-U^-²)]chi/sqrt(Z),
    sigma=+1 and -1,
    Z=(39521+154sqrt(5))/15625.

All 26 old-memory labels and arbitrary passive references are admitted.
The original physical occupation isometry and its phases are unchanged.
The receiver is at 100. A fixed position-preserving conjugation removes
the receiver calibration only from the calculated norm, as proved in
[PROOF.md](PROOF.md); it does not discard memory or output branches.

## 2. Equation and fixed scientific comparison

Freeze rho=2, ell=2, N=8, maximum seed power K=12, and
P=1_(carrier c<=90 or c>=104). The target vector for each sign is

    v_sigma=(-3i/2) sum_(n=5)^10
       P(U^n-U^-n)psi_sigma/[(n-2)(n-1)n(n+1)(n+2)].

The proved uniform Fourier remainder is r=1/15840. Every admitted
bare-encoding comparator H_tilde with physical term diameter<=2 obeys

    ||H_tilde Vpsi_sigma-VQpsi_sigma||/E0 >= ||v_sigma||-r.

The source energy-action target is strictly below E0/1200. A sign
therefore supplies a sufficient obstruction precisely when this test
establishes the STRICT inequality

    ||v_sigma||² > (1/1200+1/15840)²
                  =5041/6272640000.

The threshold on the unsquared norm is 71/79200. No source, branch,
sign, geometric projection, degree, threshold or arithmetic comparison
may be changed after the pin. Both signs are reported, including every
failed sufficient comparison. No parameter search is admitted.

## 3. Accepted code, arithmetic and systematics

Accepted executable: [verify.py](verify.py), standard library only.
SHA-256:
`17206c5fa79a0d9f0f3adbdffc0623e1b58bef930274ca8ba7ab2f3dd5c710c8`.
The executable, this preregistration and PROOF.md are committed and
pushed together; the full pin commit is recorded in RUN.md. Public
byte-for-byte readback must finish before scientific execution.

Command from repository root:

    python3 probes/P-SOURCE-RANGE2-ENERGY-1/verify.py

The code has no runtime arguments, external data, network, randomness,
filesystem writes or floating point. Exact integer cyclotomic arithmetic
requires enabled assertions; optimized Python execution is rejected.
The arithmetic
uses the fixed internal coin coordinates G=diag(1,i,i,1), not a changed
physical encoding. A=25G*U_uncal G and A* propagate integer sparse
states. The normalized physical source is restored by its exact
sqrt(2Z) and 25-power factors. Squared norms lie in Q(sqrt(5)); signs
are decided by exact integer sign and square comparisons.

The fixed code checks:

1. Cyclotomic reduction, conjugation, norm identities and quadratic
   ordering; no selected numerical precision is involved.
2. Free and contact coin unitarity and the pulse adjoint, with the
   combined denominator 25 justified by M2(C-I)=C-I.
3. Every iterate from 0 through 12 in both directions: exact norm,
   support, object parity and valid state fields. Every nonzero iterate
   is returned to its predecessor by the opposite step with factor 625.
4. The exact second seed moment 12/25, real fourth moment
   (3677-77sqrt(5))/15625, and source norm 2Z for BOTH signs.
5. Complete six-term expansion of each source polynomial, common
   integer denominator, fixed carrier projection, nonnegative exact
   final norms and both strict squared-threshold comparisons.

The physical support model, both inverse and forward factor orders,
contact signs, denominator and normalization are explicit in PROOF.md
and code. The finite coordinate calculations contain all paths inside
the exact finite propagation cone; no boundary truncation is introduced.
The opposite-step integrity check can visit an intermediate radius-13
box before exact cancellation; the scientific source horizon remains 12.
No scientific function, import-time matrix construction or gate was run
before the pin. Syntax compilation and source inspection alone are
allowed before execution.

## 4. Outputs, failure thresholds and dispositions

The verifier emits exactly 19 deterministic UTF-8 lines, each key=value:

    probe
    arithmetic
    parameters
    carrier_projection
    source_Z
    remainder
    norm_threshold
    squared_threshold
    common_denominator
    positive_support_counts
    negative_support_counts
    integrity
    plus_norm_squared
    plus_comparison
    plus_disposition
    minus_norm_squared
    minus_comparison
    minus_disposition
    overall_disposition

The two support lists include powers 0 through 12. Each exact squared
norm is printed as (a+(b)*sqrt(5))/d with a common positive integer
denominator and the triple reduced by its gcd. Comparison is GT, EQ
or LT. GT gives CERTIFIED_OBSTRUCTION for that sign; EQ or LT gives
INCONCLUSIVE. The overall disposition is CERTIFIED_OBSTRUCTION iff
at least one sign is GT, otherwise INCONCLUSIVE. A passing sign does
not establish failure of the other sign.

All integrity checks must pass before any stdout is emitted. A valid
completed calculation exits zero with empty stderr, including when the
scientific disposition is INCONCLUSIVE. Any assertion, exception,
nonzero exit, missing output or inconsistent custody is an integrity
failure, not a positive or negative physical result. It must not be
repaired by changing and rerunning this pinned identifier. An incomplete
gate is disposed under the repository abandoned-pin policy; any successor
requires a fresh identifier and pin.

The first completed stdout is preserved unchanged in EXPECTED.txt.
RUN.md records the full pin, exact command, neutral operating-system,
architecture and Python fields, exit code, stdout byte/line counts and
SHA-256, and empty-stderr count/hash. RESULT.md reports both comparisons
and the correct scientific scope. Required clean x86_64 and aarch64
jobs rerun the unchanged verifier and require byte-identical stdout.
The repository verifier timeout is 600 seconds; it is not increased here.

## 5. Acceptance boundary

INCONCLUSIVE means this fixed sufficient certificate did not settle the
diameter-two question. It does not prove that a local Hamiltonian exists,
that the true forbidden energy tail is small, or that the source may be
changed. Any later method is separately declared and pinned.

A certified obstruction concerns original energy action on the actual
source with fixed data-independent ancillary readiness and stated
matrix-element convergence. It does not exclude dressed encodings,
another declared energy, good time evolution alone or larger interaction
diameter. No empirical scale, thermal preparation, funded terminal readout,
renewal or native six-pentit derivation is provided. Same-session code
reviews and reproduction are not independent external scientific
acceptance. No Canon, predecessor, policy, workflow or ledger is changed.
