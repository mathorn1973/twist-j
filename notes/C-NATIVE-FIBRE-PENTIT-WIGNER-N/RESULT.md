# RESULT: C-NATIVE-FIBRE-PENTIT-WIGNER-N

**NON-CANONICAL. Candidate labels only. Action layer L1. No registry, frontier
or Canon row is changed.** Date 2026-10-02. Authority at freeze and at run:
Public Canon v97, tag `canon-v97`, main
`738e0421bd15aaea5bb6ef2a56f1cab752d44de5`.

Outcome in one sentence: the native fibre carries an exact phase-point
representation, line states are counted exactly as points, and the declared
real QDD reading lies entirely outside nonnegative point counting with line
reading. Outcome for occurrence: **`STOP_APPLICABILITY / H_NOT_TESTED` of
`C-OCCURRENCE-CYCLE-COUNT-N` is unchanged.**

## 1. Custody

```text
PIN recorded 2026-10-02T16:59:20Z, before the first execution
  cbda8c9f0fbc7da3b5baeed685d9e8592ecffaa6b70617633a271056ca94757c  PREREG
  ddf883612cd6fff00b227d8fca76668fc876ef1873f819da724ee0e66426dd63  verifier
First execution of the pinned verifier, from the repository root at canon-v97
  exit 0, stderr empty, 38 of 38 checks PASS, about 2 seconds
  stdout 4476 bytes
  3b2bdc432e1bfebcd453b83a6766a2863b6a1d54243180cbc20e0b1ce4ea39ad  stdout
  platform Ubuntu 24.04, architecture x86_64, CPython 3.12.3
  rerun on the same architecture: byte-identical (reproduced, not a second leg)
Breaker, written after the first run, independent code path, no repository import
  c48073764b881238f9dc980ddc1b6467dc2b60637f5ddcc22881a7e9f711ddf6  breaker
  f1044cc3c1371342ca3bfc5b921460332fa7c07a17999874e556dc1891cf6f0f  breaker stdout
  exit 0, stderr empty, 21 of 21 checks PASS, 2660 bytes, rerun byte-identical
Recon that preceded the freeze (exposure declared in PREREG section 2)
  55648d730c13eaaed832215dd70af4be1049584c874842e5608899d900a320aa  recon script
  3694834d1d7d4312f9b0e17c9c5d4f970c33975143e3093790ceb4f9345bdcaf  recon stdout
```

The pinned files were re-hashed after the run and are unchanged. The breaker
was edited twice before its own first run (one loop made cheaper, one
vacuous conjunct removed); it was never run in the earlier form.

## 2. Results by claim

| Claim | Content | Label | Evidence |
| --- | --- | --- | --- |
| A1 | generators affine; fibre action is identity for `a`, point reflections for `b,c,d,e` with centres (0,0),(3,0),(3,3),(1,3), the four exceptional readies | candidate-T | direct from the formulas; exhaustive on 15625 states |
| A2 | the reflections generate exactly the 50 maps `u -> +-u + t`; no direction of lines is ever changed | candidate-C | closure, two representations |
| A3 | `A_u` over `Z[zeta_5]`: Hermitian involutions, trace 1, `Tr(A_uA_v)=5 delta`, `A_sA_uA_s=A_(2s-u)`, sum `5I`; conjugation at the native centres is the native fibre map | candidate-T | inline proof; monomial and dense audits |
| A4 | invariant alternating forms on `F_5^6`: nonzero only for multiplier triples (1,1,1),(4,1,1),(1,4,4),(4,4,4), dims 3,3,1,1; strictly invariant forms are span{dkappa^dq, dkappa^dr, dq^dr}; all 256 nonzero solutions have rank 2; common radical is the 3-dim space kappa=q=r=0 | candidate-C | exact linear algebra over all 64 triples; Pfaffian cross-check |
| A5 | `U(0,000000)=U(0,212110)`; one-step images 6250 and 9375; sync to 3125 states, five preimages each; from tick 3 one common generator by the clock-pair rule (`b` on a change, `d` after 11, `e` after 00), bijective on the 3125-state set | candidate-T for the collision and the rule; candidate-C for the audited ranges | substitution; proof from `KERNEL-Z6-SYNCHRONIZATION [T]`; ticks 3 to 1026 and 3 to 1500 |
| B1 | each of the 30 line operators is a rank-one projector and an eigenprojector of the Weyl operator of its direction; `Tr(Pi_L Pi_M) = |L cap M|/5` | candidate-T for the trace formula; candidate-C for the projector audit | inline proof; idempotence audit and independent 2x2-minor audit |
| B2 | point counting with line reading is unique: `mu(u) = (sum_(L through u) p(L) - 1)/5`, equal to `W_rho` | candidate-T | inline proof; audited on LOW and 624 preparations from dense projectors |
| B3 | every nonzero real sum-zero state, any odd `d`: row `r=0` of `W` sums to zero and is not zero, so `W` has a negative entry; negativity at least `1/(2 sqrt(d(d-1)))`, which is `sqrt5/20` at `d=5` | candidate-T | self-contained inline proof; audits at d=5 and on boxes at d=3,7,9 |
| B4 | LOW: values 1/5 x1, 3/20 x4, -1/20 x4, (1+sqrt5)/40 x8, (1-sqrt5)/40 x8; negativity `sqrt5/5` | candidate-C | two routes agree |
| B5 | `|<l,v~>|^2/|v~|^2 = s^2/(4(5Q-s^2)) = 5 sum_u W_v(u) W_l(u)` | candidate-T | inline proof; 624 audited |
| B6 | census of the 624: all negative; minimum `(1+sqrt5)/10`, attained by 32 preparations including `1400`; maximum `29/220 + (8/55) sqrt5`, attained by 16; 39 distinct values; table sha256 `c423a1edf376c9cdbd0653b4e89a284ed16e9bfea69586c3cb1c5e208351c905` | candidate-C | parity route and Weyl route give the same table bytes |
| C1 | applicability | disposition, no label | `STOP_APPLICABILITY / H_NOT_TESTED` unchanged |

Computation-grade items stay at candidate-C in this lane. They become eligible
for T only with byte-identical stdout on a second architecture.

No falsifier fired in the pinned run or in the breaker.

## 3. What was found that had not been seen before the freeze

1. Multipliers 2 and 3 admit no nonzero form, as the involution lemma predicts.
2. The census has 39 distinct negativity values, 32 minimizers and 16 maximizers.
3. Breaker search S2: among all 1450 nonzero integer sum-zero vectors with
   entries in the box from -3 to 3, none has negativity below `(1+sqrt5)/10`;
   the lowest value is attained at a difference of two basis vectors.
4. Breaker search S1: 17150 vectors with entries from -6 to 6, no violation of
   the row-zero statement or of the bound.
5. Breaker search S3: the row-zero statement and the bound hold on the tested
   boxes in dimensions 3, 7 and 9.
6. Breaker S4: the complex sum-zero Fourier vector is a line state. Reality of
   the amplitudes is what B3 uses.

## 4. Negative content, stated once

1. No nondegenerate alternating form on `F_5^6` is preserved, even up to a
   multiplier, by the linear parts of the generators. A symplectic three-pentit
   reading of this invariant linear and affine realization is excluded. Wider
   realizations are not addressed.
2. No nonnegative distribution on the 25 fibre points returns, by plain
   membership, the 30 line probabilities of any nonzero real sum-zero state. In
   the declared reading this covers every QDD preparation and the LOW direction.
3. The selected step is not a generator: it is not injective on `X`, and the
   synchronized common reflection is driven by the clock.

## 5. What is not claimed

No occurrence law. No passage through Gate 0. No contextuality theorem on one
pentit. No statement about larger carriers, other readings, contextual
apparatus, or models that reproduce only LOW and HIGH. No explanation or
minimality of the 31 channels. No complete apparatus class for
`QDD-INSTRUMENT-CLASS-COMPLETENESS`. No physical dimension from the parity
split 3 + 2. No change to any registered row.

The reading of the QDD four-vector in the real sum-zero sector is a declared
premise. If it is not adopted, B3 to B6 remain statements about the pentit.

## 6. Open items

1. `[O]` sharp bound: is `(1+sqrt5)/10` the infimum of the negativity over all
   nonzero real sum-zero states at `d=5`? Proven: `sqrt5/20`. Evidence for the
   sharp value: census and box search only. Falsifier: one real sum-zero vector
   with negativity below `(1+sqrt5)/10`.
2. Second architecture leg (aarch64) for the computation-grade items. Not
   available to this session.
3. A native contract of actual repeated events for line states: finite
   autonomous carrier or factor, preparations in more than one direction,
   event transducer, renewal. New identifier if attempted.
4. Owner decision: whether the real sum-zero reading of the QDD four-vector is
   to be adopted as a dictionary premise or kept as a conditional.
