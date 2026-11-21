# P-SOURCE-PARITY-RANGE2-1 preregistration

**NON-CANONICAL. L1. Prospective exact finite certificate.**
A. M. Thorn. 2026-10-26. Apache-2.0.
Reservation: [#1788](https://github.com/mathorn1973/twist-j/issues/1788).
Branch: probe/P-SOURCE-PARITY-RANGE2-1.
Dossier: PROMO-P-SOURCE-PARITY-RANGE2-1.

## Authority and predecessor disposition

The sole authority is ACTIVE Public Canon v105, public main and peeled
canon-v105 `892a0b11089d34e241e1eb76d2c03247022d18e6`, content commit
`b8cdfd6ea58ae798545bc6000c817147fa0f0dcc`. STATUS was read first;
POLICY, AGENTS, CORE and FRONTIER are unchanged from their complete reads
in this session. Public main was fetched and checked, all five normative
hashes matched, and main architecture, aggregate and publication checks
were green. A fresh explicit remote scan contained 314 branch heads.
Open issues/PRs, remote branches, probes, notes and registry were checked
before reserving this distinct lane. Retired internal attachments are not
authority.

The completed predecessor [PR1787](https://github.com/mathorn1973/twist-j/pull/1787)
at `165964849b2d8f3ca6278e88755c1a8e03d6d842` is INCONCLUSIVE for both
settings. Its exact post-run bound proves that increasing the Fourier
cutoff alone cannot rescue its same filtered-carrier projection. This is
a different declared dual test using object parity and mandatory changes
of occupation. No predecessor file, output or threshold is replaced.
PR1785 at `19f1c74a27684a22bf038c1e6fc1133f638fb613` supplies the earlier
conditional diameter-one obstruction. Neither predecessor has a recorded
external review at this reservation; their conditional premises are retained.

## Original physical inputs and comparator class

Use the unchanged source of PR1777 at
`191ab035be823bd9d6fdc9effba81528fa026e49` and nominated logarithm of
PR1772 at `3abf054e435e31c51e6e50528b09fe3cf7cffe13`:

    U=U_rec, Q=E0 f(U), E0>0,
    f(exp(-i theta))=theta, 0<=theta<2pi, f(1)=0,
    chi=|R=97,r=0,iB;c=97,token label0> tensor Xi,
    B=(e2-e3)/sqrt(2),
    psi_sigma=[I+sigma(U²-U^-²)]chi/sqrt(Z), sigma=+1,-1,
    Z=(39521+154sqrt(5))/15625.

The occupation isometry, all 26 old-memory labels and arbitrary passive
references remain unchanged. A comparator is a sum of terms supported on
physical sites of diameter at most two, with source action and the stated
matrix-element limits defined. Additional ancillas have a fixed normalized
data-independent ready state, possibly entangled across their own sites.
No positivity, charge conservation or coupling-norm bound is needed by the
obstruction. Both original signs must be reported, even if one succeeds.

## Fixed projection and sufficient inequality

Let S0 be the UNION of the exact nonzero spatial/carrier-kind supports of
both source vectors, after collecting all equal-basis coefficients. Coin
indices are omitted only after that collection. Source object positions
R+r and R-r are odd; source carrier positions lie in [95,99].

For a target alpha=(R,r,c,kind) with both object positions even and every
source beta in S0, form the mandatory changed-site set

    D_obj={R_alpha+r_alpha,R_alpha-r_alpha,
           R_beta+r_beta,R_beta-r_beta},
    D_car={} if (c_alpha,kind_alpha)=(c_beta,kind_beta),
          {c_alpha,c_beta} otherwise,
    D=D_obj union D_car.

F projects onto a target iff its object positions are even AND
`max(D)-min(D)>2` for EVERY beta in S0. Carrier kinds are token, pulse bank1
and pulse bank2. Labels and memory are ignored by this conservative test;
they can add physical differences but cannot remove the mandatory ones.
The same F is used for both signs. It commutes with receiver calibration.

Freeze rho=2, polynomial index n=4 and maximum seed power K=12. Put

    A=(U-U*)/(2i), C=(U+U*)/2,
    S=[f(U)-f(-U)]/pi,
    p4(A)=A[1+C²/2+3C⁴/8+5C⁶/16+35C⁸/128],
    W_sigma=||F p4(A)psi_sigma||²,
    R_sigma=||C^10 psi_sigma||²,
    t=1/1800, d_sigma=W_sigma-R_sigma-t²,
    e_sigma=d_sigma²-4t² R_sigma.

PROOF.md establishes the error lower bound

    ||H_tilde Vpsi_sigma - VQpsi_sigma||/E0
       >= (pi/2)(sqrt(W_sigma)-sqrt(R_sigma)).

The fixed sufficient certificate is `d_sigma>0 AND e_sigma>0`, exactly
equivalent to `sqrt(W_sigma)-sqrt(R_sigma)>1/1800`. Since pi>3, success
excludes energy-action error at most E0/1200 for that original setting.
The selected cut values S(1)=-1 and S(-1)=+1 are included in the proof;
no absence-of-atoms premise is used.

## Accepted implementation and custody

Accepted executable: [verify.py](verify.py), standard library only.
Its final SHA-256 and exact output schema are recorded below before pinning.
The executable, this preregistration and [PROOF.md](PROOF.md) are committed
and pushed together and publicly read back byte for byte BEFORE execution.
The full pin commit is recorded in RUN.md.

Command from repository root:

    python3 probes/P-SOURCE-PARITY-RANGE2-1/verify.py

The fixed arithmetic coin coordinates are G=diag(1,i,i,1), as in PR1787.
This changes arithmetic coordinates only, not the physical encoding.
The unchanged exact walk uses sparse integer vectors over Z[zeta5], with
25 per seed step and chi0=sqrt(2)G*chi=e2-e3. The common denominator is
`65536*25^12`. Multiplication by i in the witness polynomial preserves
its norm; no complex phase is dropped from a physical matrix element.
The remainder uses the full unprojected vector C^10 psi for each sign.
Squared norms and both comparison expressions are evaluated in Q(sqrt(5))
by exact integer arithmetic, with no numerical roots or chosen precision.

Every iterate through powers -12 to 12 must pass exact norm, finite-support,
parity and inverse-step checks. Both source normalizations and the original
second and real fourth moments are checked. Coefficient identities, common
denominators, geometry and quadratic-field comparisons have explicit
integrity assertions. The reverse-step check may visit intermediate
radius13 before exact cancellation; no boundary truncation is applied.

This new scientific verifier is not executed or imported before the pin.
Static source review and syntax compilation alone are permitted. The prior
public program and its completed output are exposed predecessors, not a
blind comparison or an independent acceptance of this successor.

## Fixed outputs and failure dispositions

Verifier SHA-256:
`43b2f564b97833d1d222d5a06c429d5f9ebee51f929828af67cd48a95a246aad`.

The verifier emits exactly 29 deterministic UTF-8 key=value lines:

    probe
    arithmetic
    parameters
    projection
    source_Z
    norm_gap_threshold
    energy_action_target
    common_denominator
    source_spatial_support
    positive_support_counts
    negative_support_counts
    integrity
    plus_witness_norm_squared
    plus_remainder_norm_squared
    plus_gap_test_d
    plus_gap_test_d_sign
    plus_gap_test_e
    plus_gap_test_e_sign
    plus_gap_comparison
    plus_disposition
    minus_witness_norm_squared
    minus_remainder_norm_squared
    minus_gap_test_d
    minus_gap_test_d_sign
    minus_gap_test_e
    minus_gap_test_e_sign
    minus_gap_comparison
    minus_disposition
    overall_disposition

The source-support line sorts the exact union lexicographically and encodes
each (R,r,c,kind) tuple with colons, separating tuples with semicolons.
Both support-count lists include seed powers 0 through 12. Algebraic values
are printed as (a+(b)*sqrt(5))/d with positive denominator and a gcd-reduced
integer triple. The signs of d and e are -1, 0 or 1. The gap comparison is
GT, EQ or LT for sqrt(W)-sqrt(R) versus 1/1800; root elimination includes
the zero-remainder boundary. Equality of the two independently computed
FULL remainder norms is required because the source spectral laws agree.

All integrity assertions must pass before any stdout is emitted. A setting
is CERTIFIED_OBSTRUCTION iff both d and e have sign 1 (gap comparison GT);
otherwise it is INCONCLUSIVE. Overall disposition is
CERTIFIED_OBSTRUCTION iff at least one setting passes. No selection among
sources, degrees, projections or thresholds is allowed after pinning.

A completed scientific INCONCLUSIVE result exits zero with empty stderr.
It means this sufficient test failed to decide the diameter-two question;
it does not establish a local realization or a small true forbidden tail.
Any exception, assertion failure, nonzero exit, timeout, missing output or
custody mismatch is an integrity failure. It cannot be repaired by changing
and rerunning this pinned identifier. An incomplete gate is disposed under
the abandoned-pin policy; any successor needs its own identifier and pin.

Preserve the first completed stdout unchanged in EXPECTED.txt. RUN.md must
record the pin, verifier hash, exact command, neutral platform/architecture/
Python descriptors, exit code, stdout bytes/lines/hash and empty-stderr
bytes/hash. The unchanged repository replay and clean GitHub x86_64 and
aarch64 jobs must require byte identity. The existing 600-second verifier
timeout is not increased. RESULT.md preserves both settings and the scope.

## Acceptance boundary

A successful result excludes only the stated bare-occupation diameter-two
energy-action class on the original prepared source. It does not exclude
the local discrete step, accurate time evolution alone, dressed encodings,
another energy reading or larger diameter. Empirical units, native-law
derivation, thermal preparation, terminal event selection, replenishment
and unlimited record retention remain outside this test. Same-session
reviews and reproduction are not independent external scientific acceptance.
No Canon, registry, policy, workflow or predecessor change is authorized here.
