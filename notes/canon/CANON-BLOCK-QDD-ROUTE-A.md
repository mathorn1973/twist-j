### QDD Route A dictionary

The quadratic leg of `D_matter` gains its exact algebra as public definitions
and theorems on the finite balanced piston carrier. Everything below is L1
exact algebra. Nothing here fills the decoder completion contract, claims an
L6 reading, selects an apparatus, derives the architecture or the effect pair
from J, or changes `QUADRATIC-DECODER-DATA`, which remains an open obligation
[O]: the physical effect selection and the completion contract stay open under
the EFFECT_SHADOW_MINIMAL owner freeze, and the physical instrument family is
the separate obligation `QDD-INSTRUMENT-APPARATUS`.

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
    E_low = (1/4) 1 1^T; the first member of the frozen ordered effect pair
    of the EFFECT_SHADOW_MINIMAL owner freeze; ALGEBRAIC_READOUT, not a
    physical apparatus selection, not a realized outcome, not a post-state
    instrument, and not claimed to be forced by J.
DEF-QDD-PROJECTOR-HIGH
    E_high = I_4 - E_low; the second member of the frozen ordered pair; the
    same labels.
DEF-QDD-BRANCH-WEIGHT-PAIRING
    on the transpose slot A_T = v v^T: m(A_T) = Tr(A_T G),
    w_low(A_T) = Tr(E_low A_T G), w_high(A_T) = Tr(E_high A_T G); this is the
    owner-frozen Born trace pairing of the EFFECT_SHADOW_MINIMAL freeze, an
    adopted dictionary input, not derived from J or from the projector
    identities; on the cyclotomic side, for w = Amp_QDD(kappa):
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
        NORMALIZED((w_low, w_high)/m)).
    All five fields are L1-derived exact data; normalized_weight_state on the
    NONZERO branch is an exactly normalized rational pair, and no L6 measure
    reading of it is claimed by this block.
DEF-QDD-DIRECT-WRITE
    D_QDD_direct = R_cyc o iota_B0 o beta_QDD : K_QDD -> MatterData_QDD,
    written from field arithmetic, sigma_4, Tr, the trace pairing, lambda_B,
    pi_low, pi_high, T_w and MATRIX_B0 only; it does not name Q_QDD, F_QDD,
    the effect pair, the Born pairing, or a helper shared with the factor
    branch (the independence firewall of the EFFECT_SHADOW_MINIMAL freeze).
DEF-QDD-FACTOR-MAP
    F_QDD : QCarrier_QDD -> MatterData_QDD by the displayed Gram/projector
    formulas on the transpose slot.
```

Theorems and the separate apparatus obligation.

```
QDD-ALGEBRAIC-FACTORIZATION [T]
    D_QDD_direct = F_QDD o Q_QDD o beta_QDD field by field on all 15625
    checkpoints; the record is total (25 ZERO_SUPPORT heads, 15600
    SUPPORTED), exactly normalized, independent of q and r, dependent on each
    piston coordinate, constant on each of the 313 Q_QDD-fibres (one of size
    25 and 312 of size 50) and injective on QCarrier_QDD; controls: the
    rational-line reading mismatches on 480 of 625 pistons and omitting G on
    540 of 625. An identity of the adopted definitions, not an independent
    readout, not a physical selection, and not a completion, totality or
    uniqueness claim for D_matter.
QDD-PROJECTOR-PAIR-TR4 [T]
    E_low is the unique G-self-adjoint idempotent with kernel ker Tr_4, since
    a G-self-adjoint idempotent has image (ker)^perp_G and G^-1 1 = 5 1
    gives (ker Tr_4)^perp_G = span(1); {E_low, E_high} is the G-orthogonal
    resolution of Q^4 along the piston character Tr_4; closed forms
    m = |v|^2 - s^2/5, w_low = s^2/20, w_high = |v|^2 - s^2/4, s = sum v_i,
    so w_low and w_high are the squared trace-pairing lengths of the
    projections onto span(1) and onto ker Tr_4. Linear algebra only; no
    apparatus, no physical reading, and no uniqueness-from-J: the theorem
    identifies the pair inside the stated algebraic class and does not force
    the choice of that class.
QDD-QCARRIER-DIAGONAL-BOUNDARY [T]
    on the frozen V_eff, A_dagger = A_T = v v^T. Both slots remain typed and
    declared; the current domain does not test their difference; no physical
    central phase is derived from this equality. The cyclotomic pair
    (w sigma_4(w), w^2) has 90 distinct Hermitian slots and 313 distinct
    pairs on the 625 pistons, and 80 Hermitian slots carry more than one
    record; neither Herm-only nor use of both slots is asserted.
QDD-INSTRUMENT-APPARATUS [O]
    the physical instrument family {K_a} with E_a = K_a^sharp K_a realizing
    the frozen ordered pair (E_low, E_high) as physical effects, from a
    public apparatus carrier, ready state, coupling, pointer and reduction,
    with occurrence law, sampling, post-state and completeness of the
    admissible class; registered separately from QUADRATIC-DECODER-DATA and
    filling no field of the decoder completion contract; reverse inference
    from effects to instruments is forbidden and equality of effects does not
    identify post-state instruments.
```

Disclosure. `|QCarrier_QDD| = 313 = 1 + (5^4 - 1)/2` arises from the sign
identification `v ~ -v`, with fibres 25 and 50. CENSUS-313 has the same count
and the same 25/50 profile from a different origin, and the two partitions of
`F_5^6` share no block. No cross-leg identity is claimed. Over the 312
nonzero classes the normalized pair takes 22 values; the value 1/6 on 12
classes is a numerical witness with no input, threshold, normalization,
confirmation or dependency role. Evidence: `reproduce/qdd-route-a`,
byte-identical on the public x86_64 and aarch64 jobs, RESULT 15/15 ALL PASS.
