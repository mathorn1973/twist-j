### QDD Route A dictionary

The quadratic/Born leg of `D_matter` is registered as an explicit dictionary
on the finite balanced piston carrier. Everything below is L1 exact algebra
except the single L6 reading named at the end. Nothing here derives the
architecture from J, selects an apparatus, or claims totality, uniqueness or
completeness of `D_matter`.

Definitions.

```
DEF-QDD-DOMAIN-K0
    K_QDD = {kappa_x = (U^n(0,x))_(n>=0) : x in F_5^6}, equality of complete
    pointed forward sequences, distinguished head n = 0; the common total
    domain of the quadratic D_matter leg.
DEF-QDD-BALANCED-PISTON
    ell(0,1,2,3,4) = (0,1,2,-2,-1); for x = (p1,p4,p1p,p4p,q,r),
    beta_QDD(kappa_x) = (ell(p1),ell(p4),ell(p1p),ell(p4p))^T in
    V_eff = ell(F_5)^4 subset Q^4; q, r, every later checkpoint, the counter,
    environment, randomness and dynamic evaluation are forbidden inputs.
DEF-QDD-AMPLITUDE-B0
    B0 = (1, zeta, zeta^2, zeta^3), zeta = zeta_5;
    iota_B0(v) = v_0 + v_1 zeta + v_2 zeta^2 + v_3 zeta^3 in K = Q(zeta);
    Amp_QDD = iota_B0 o beta_QDD.
DEF-QDD-COEFFICIENT-Q
    coefficient ring Q with the trivial involution on the matrix side; the
    amplitude field K with bar = sigma_4 (zeta -> zeta^4) and Tr = Tr_(K/Q);
    inv_Q, bar and the Gram adjoint are three distinct typed operations.
DEF-QDD-TRACE-PAIRING
    <x,y>_tr = (1/5) Tr(x sigma_4(y)); (1/5) Tr(zeta^(a-b)) = delta_(a,b) - 1/5,
    so the matrix of <.,.>_tr in B0 is G = I_4 - (1/5) 1 1^T.
DEF-QDD-GRAM
    G = I_4 - (1/5) 1 1^T on V_eff, G^-1 = I_4 + 1 1^T, G^-1 1 = 5 1;
    Gram adjoint A^sharp = G^-1 A^T G.
DEF-QDD-DAGGER
    v^dagger = v^T on Q^4.
DEF-QDD-TRANSPOSE
    transpose(A) = A^T on M_4(Q).
DEF-QDD-QPAIR
    Q_QDD(v) = (A_dagger, A_T) = (v v^dagger, v v^T), an ordered pair of two
    typed slots.
DEF-QDD-QCARRIER-EQUALITY
    QCarrier_QDD = im(Q_QDD | V_eff) subset M_4(Q) x M_4(Q), ordered
    componentwise rational matrix equality; equal coordinate values do not
    collapse the two typed slots.
DEF-QDD-LOW-LINE
    lambda_B = 1 + zeta + zeta^2 + zeta^3 = -zeta^4, Tr(lambda_B) = 1,
    <lambda_B,lambda_B>_tr = 4/5; the LOW LINE is Q lambda_B. It is neither
    the rational line Q.1 nor the trace kernel of K.
DEF-QDD-PROJECTOR-LOW
    E_low = (1/4) 1 1^T; ALGEBRAIC_READOUT, not a physical apparatus
    selection, not a realized outcome, not a post-state instrument.
DEF-QDD-PROJECTOR-HIGH
    E_high = I_4 - E_low; the same labels.
DEF-QDD-BRANCH-WEIGHT-PAIRING
    on the transpose slot A_T = v v^T: m(A_T) = Tr(A_T G),
    w_low(A_T) = Tr(E_low A_T G), w_high(A_T) = Tr(E_high A_T G);
    on the cyclotomic side, for w = Amp_QDD(kappa):
    m_tr(w) = <w,w>_tr,
    pi_low(w) = (<w,lambda_B>_tr / <lambda_B,lambda_B>_tr) lambda_B,
    pi_high(w) = w - pi_low(w),
    w_low(w) = <pi_low,pi_low>_tr, w_high(w) = <pi_high,pi_high>_tr,
    T_w(x) = w <x,w>_tr with MATRIX_B0(T_w) = v v^T G.
DEF-QDD-MATTER-RECORD
    MatterData_QDD = (support_state, total_weight, branch_weights,
    density_state, normalized_weight_state), ordered branch pair (LOW, HIGH),
    no swap;
    ZERO branch (w = 0): (ZERO_SUPPORT, 0, (0,0), ZERO_DENOMINATOR,
        ZERO_DENOMINATOR), no division performed;
    NONZERO branch: (SUPPORTED, m, (w_low, w_high), DENSITY(A_T G / m),
        MEASURE((w_low, w_high)/m)).
    support_state, total_weight, branch_weights and density_state are
    L1-derived D_matter fields; only normalized_weight_state on the NONZERO
    branch is an L6 measure.
DEF-QDD-DIRECT-WRITE
    D_QDD_direct = R_cyc o iota_B0 o beta_QDD : K_QDD -> MatterData_QDD,
    written from field arithmetic, sigma_4, Tr, the trace pairing, lambda_B,
    pi_low, pi_high, T_w and MATRIX_B0 only; it does not name Q_QDD, F_QDD or
    a shared factorization helper.
DEF-QDD-FACTOR-MAP
    F_QDD : QCarrier_QDD -> MatterData_QDD by the displayed Gram/projector
    formulas on the transpose slot.
DEF-BRIDGE-QDD-TR4-EFFECT-SELECTION
    the explicit dictionary bridge Tr_4 line -> ordered LOW, ker Tr_4 ->
    ordered HIGH; a bridge row between the linear leg's Tr_4 line and the
    quadratic leg's ordered outcomes, never inherited from a shared decoder
    stage; a dictionary choice, not derived from J.
```

Theorems and readings.

```
QDD-ALGEBRAIC-FACTORIZATION [T]
    D_QDD_direct = F_QDD o Q_QDD o beta_QDD field by field on all 15625
    checkpoints; the record is total (25 ZERO_SUPPORT heads, 15600
    SUPPORTED), exactly normalized, independent of q and r, dependent on each
    piston coordinate, constant on each of the 313 Q_QDD-fibres (one of size
    25 and 312 of size 50) and injective on QCarrier_QDD; controls: the
    rational-line reading mismatches on 480 of 625 pistons and omitting G on
    540 of 625. An identity of the adopted definitions, not an independent
    readout.
QDD-PROJECTOR-PAIR-TR4 [T]
    E_low is the unique G-self-adjoint idempotent with kernel ker Tr_4, since
    a G-self-adjoint idempotent has image (ker)^perp_G and G^-1 1 = 5 1
    gives (ker Tr_4)^perp_G = span(1); {E_low, E_high} is the G-orthogonal
    resolution of Q^4 along the piston character Tr_4; closed forms
    m = |v|^2 - s^2/5, w_low = s^2/20, w_high = |v|^2 - s^2/4, s = sum v_i.
    Linear algebra only; no apparatus and no uniqueness-from-J.
QDD-QCARRIER-DIAGONAL-BOUNDARY [T]
    on the frozen V_eff, A_dagger = A_T = v v^T. Both slots remain typed and
    declared; the current domain does not test their difference; no physical
    central phase is derived from this equality. The cyclotomic pair
    (w sigma_4(w), w^2) has 90 distinct Hermitian slots and 313 distinct
    pairs on the 625 pistons, and 80 Hermitian slots carry more than one
    record; neither Herm-only nor use of both slots is asserted.
QDD-BORN-READOUT-MEASURE [D]
    on the NONZERO branch, normalized_weight_state = (p_low, p_high) is read
    as a finite two-outcome measure on the ordered pair (LOW, HIGH) through
    GATE-L1-L6-QDD-BORN-READOUT, LOW reading the Tr_4 line and HIGH its
    G-orthogonal complement by DEF-BRIDGE-QDD-TR4-EFFECT-SELECTION; the ZERO
    branch is the tag ZERO_DENOMINATOR and is not a measure. Over the 312
    nonzero classes p_low takes 22 values, 42 classes at 0 and 2 at 1; the
    value 1/6 at 12 classes is a numerical witness with no input, threshold,
    normalization, confirmation or dependency role.
QDD-INSTRUMENT-APPARATUS [O]
    the physical instrument family {K_a} with E_a = K_a^sharp K_a realizing
    the ordered LOW/HIGH effect shadow from a public apparatus carrier, ready
    state, coupling, pointer and reduction, with occurrence law, sampling,
    post-state and completeness; registered separately so that QDD carries no
    unregistered blocker.
```

The gate `GATE-L1-L6-QDD-BORN-READOUT` (owner QDD-BORN-READOUT-MEASURE,
kind DICTIONARY_LIFT) is a direct L1 to L6 lift because the construction
uses no L2 manifold, L3 boundary, L4 support or L5 stream: it reads the
pre-update L1 head and writes the tagged record whose NONZERO branch carries
the normalized two-outcome measure. It passes exactly when the direct write is
total into the tagged record, the ZERO branch is complete without division,
the NONZERO weights are nonnegative, `w_low + w_high = total_weight`, the
normalized weights sum to 1, all five fields agree with the factor route, the
dependency graph is complete and acyclic, and no L2 to L5 claim is implicitly
appropriated; it closes negatively on any supported head with a value outside
[0,1] or a pair not summing to 1, or on two heads with equal `Q_QDD` and
different pairs.

Scope of QUADRATIC-DECODER-DATA after this insertion: the coefficient ring,
effective carrier, common total domain, orbit-to-amplitude bridge, Gram,
dagger, transpose, QCarrier equality, `Q`, effect shadow, Born pairing,
MatterData schema, write map and complete dependency graph are the public
definitions above; the row is a dictionary [D]. It owns the effect shadow,
the Born trace evaluation and the MatterData_QDD write. It does not own the
linear CODEC-TR4 or binary Thue-Morse/census legs, cross-leg or state
reconstruction, the hybrid label extension, the physical instrument family,
occurrence law, sampling or post-state instrument uniqueness.

Completion-contract scope. For slots of `DEF-DECODER-COMPLETION-CONTRACT`
owned exclusively by `D_geom`, `D_clock`, `D_linear`, `D_binary`,
source-current-propagator-detector physics, metrology, scheme selection or
completion-wide terminality, a submission may use the typed constructor
`SCOPE_EXCLUDED(expected_kind_id, submitted_scope_id, owning_requirement_id,
public_basis_item_id)`, admissible only when the public registry scope
explicitly excludes the owning requirement and all four fields resolve; it is
not a blanket waiver and cannot exclude one of the fourteen QDD requirements.
The QDD submission uses `SCOPE-QDD-DMATTER-DQUADRATIC`.

Disclosure. `|QCarrier_QDD| = 313 = 1 + (5^4 - 1)/2` arises from the sign
identification `v ~ -v`, with fibres 25 and 50. CENSUS-313 has the same count
and the same 25/50 profile from a different origin, and the two partitions of
`F_5^6` share no block. No cross-leg identity is claimed. Evidence:
`reproduce/qdd-route-a`, byte-identical on the public x86_64 and aarch64
jobs, RESULT 15/15 ALL PASS.
