# C-QDD-DIRECT-QUADRATIC-LINEARIZATION-1-N

Status: NON-CANONICAL incubation. No public authority.
Target line: PUBLIC basis, no repository write.
Basis: Public Canon v61.
Main readback: bbfaec744ab635b75a195be46b6799f9eaf07dbd.
Content commit: 76b405033b41397cd62217bf3998ac9c26111964.
Canon SHA-256: e9ee0781e489e1c3951b978be567a19c5c7370708095631f966561efe03b6cb5.
Canon bytes: 334100.

## Question

Does the frozen Born-independent direct QDD write uniquely force its rational-linear quadratic factor data once the public balanced-piston carrier and Q(v)=vv^T are fixed?

## Frozen carrier and direct raw map

Let

- L = {-2,-1,0,1,2},
- V_eff = L^4 subset Q^4,
- S = Sym_4(Q),
- q(v)=v v^T in S,
- K=Q(zeta_5), B0=(1,zeta_5,zeta_5^2,zeta_5^3),
- <x,y>_tr=(1/5)Tr_K/Q(x sigma_4(y)),
- lambda_B=1+zeta_5+zeta_5^2+zeta_5^3,
- w=iota_B0(v),
- pi_low(w)=(<w,lambda_B>/<lambda_B,lambda_B>)lambda_B,
- pi_high(w)=w-pi_low(w),
- m(v)=<w,w>,
- l(v)=<pi_low(w),pi_low(w)>,
- h(v)=<pi_high(w),pi_high(w)>,
- T_w(x)=w<x,w>,
- N(v)=MATRIX_B0(T_w).

The direct raw map is R_raw(v)=(m(v),l(v),h(v),N(v)). It is the field-arithmetic branch only. Q_QDD, Gram, dagger, transpose, effects, Born pairing and factor map are not construction inputs.

## Preregistered targets

T1. q(V_eff) spans S, hence has rational rank 10.

T2. There is exactly one rational-linear map

    Lambda: S -> Q x Q x Q x M_4(Q)

such that Lambda(q(v))=R_raw(v) for every v in V_eff.

T3. The unique map is

    G      = I_4 - (1/5) 1 1^T,
    E_low  = (1/4) 1 1^T,
    E_high = I_4 - E_low,

    m_Q(A) = Tr(A G),
    l_Q(A) = Tr(E_low A G),
    h_Q(A) = Tr(E_high A G),
    N_Q(A) = A G.

T4. G and the ordered projector pair are reconstructible from the direct raw linear data:

    G is the representing matrix of m_Q,
    H_low is the representing matrix of l_Q,
    E_low = H_low G^{-1},
    E_high = I-E_low.

The recovered matrices satisfy E_a^2=E_a, E_low E_high=0, E_low+E_high=I and G-self-adjointness.

T5. On QCarrier=q(V_eff), the tagged normalized record is uniquely determined by Lambda: ZERO at A=0; otherwise m_Q(A)>0, density=N_Q(A)/m_Q(A), and normalized weights=(l_Q(A),h_Q(A))/m_Q(A).

T6. q(V_eff) has 313 elements. On the pointed orbit domain with 25 free (q,r) heads per piston, the zero fibre has size 25 and each of 312 nonzero fibres has size 50.

## Required guards

- No claim that the direct write, B0, lambda_B, V_eff, or the architecture is forced by J.
- No Born, probability, measure, event, apparatus, observer, physical effect, decoder ownership, total decoder, L5, L6, SI, or higher-layer claim.
- “Unique” means unique rational-linear extension from S after the frozen direct raw data and types are fixed.
- Without rational linearity, uniqueness outside the finite image is false and must be recorded as a negative control.
- The two typed Q_QDD slots coincide on the rational V_eff carrier; no general Hermitian/symmetric identification is claimed.

## Falsifiers

F1. rank span(q(V_eff)) != 10.
F2. two distinct rational-linear maps on S match all direct raw values.
F3. any reconstructed formula differs from direct field arithmetic on one v in V_eff.
F4. G or the recovered effects fail the stated identities.
F5. m_Q(q(v)) <= 0 for one nonzero v.
F6. the 313 or 25/50 fibre census differs.
F7. an alleged uniqueness conclusion survives after rational linearity is removed.

## Status rule

- Written derivation plus exact audit passing all T1-T6 and all guards: candidate-T.
- Finite audit without a complete derivation: candidate-C.
- Any F1-F6: candidate-F for the frozen proposal.
- F7 firing is expected as a scope guard, not a falsification of T1-T6.
