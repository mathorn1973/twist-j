# Photon v91 limit handoff after covariance review

**Working item:** C-PHOTON-V91-LIMIT-HANDOFF-N  
**Owner issue:** #1141  
**Author:** A. M. Thorn  
**Date:** 22 September 2026  
**Scope:** PUBLIC, NON-CANONICAL; no authority  
**Scientific ceiling:** candidate-T for written analytical consequences already proved in the cited public items; candidate-C for exact one-architecture certificates. No phase promotion.

## 0. Purpose

This note is the corrected restart surface after the photon chain #1122, #1125,
#1135-#1140 and a user-supplied review of #1139 dated 22 September 2026.

It does four things only:

1. records which #1139 results survived review;
2. withdraws one unsupported matrix bound from the working summary;
3. incorporates the stronger later finite-depth result #1140 without changing its status;
4. freezes the smallest remaining theorem targets for continuation.

Public Canon v91 is unchanged. No Canon, Registry, Frontier, GATES, workflow,
formal probe or release file is modified here.

The supplied review was not a blind independent review and did not supply a
second-architecture gate. It did replay the exact #1139 certificate and
recompute the scalar packet geometry separately. Its local source fingerprint
at intake was SHA-256

    07ba1b35d994b8e775689b7d052606980826a75ad97dea605075a5be13b81ddd

for 8773 UTF-8 bytes. The review text is not treated as normative authority.

## 1. Authority and inherited public basis

At authorship time:

    STATE: ACTIVE
    CANON: Public Canon v91
    main = canon-v91
         = 11b66d4755a697031157f0e10dc1898a7d5b6379
    declared content commit
         = b89b0c80bb5cebddade567f31a979aaf42f1d9dd

The normative hashes in canon/SHA256SUMS agree with STATUS. The existing
publication readback job reports the required policy, unit, Canon, ledger,
gate-contract and activation checks successful. This note is new science under
notes/ only and does not reinterpret that evidence.

The relevant non-canonical chain is:

- #1122: exact current-source Hessian and the coefficient split
  `Delta_0 = b - 25 chi`;
- #1125: reduction of P1/P2 and the closure-limit audit;
- #1135: localized exact/coexact packets whose ordered packet limit is Delta
  under the original S1/P2 hypotheses;
- #1136/#1137: exact positive full-covariance seed at R=1 and its review;
- #1139: one-link conditional covariance subtraction `Q=D+S`;
- #1140: finite-depth conditional-resampling removal and the remaining
  signed slow component.

No status in this note exceeds those sources.

## 2. Review correction to #1139

### 2.1 Results retained

[candidate-T] In the original fixed W measure,

    Q_L = D_L + S_L,
    D_L >= 0,
    S_L >= 0,

where D_L is the averaged one-link conditional covariance and has finite range,
while S_L is the covariance of the actual conditional means. This is one
measure, not two independent fields.

For the original triangular packets,

    C_R[Q_L] = C_R[S_L] + ell_(R,L),

with the exact scalar formula

    ell_(R,L)
      = 3 w_L/(8R)
        + 3(4 z_L-w_L)/(4(2R^2+1)).

Here w_L and z_L are actual opposite and adjacent entries of the averaged
six-plaquette star conditional covariance.

The all-radius scalar bound survives:

    |ell_(R,L)|
      <= 3/(8R) + 15/(4(2R^2+1)).

So ell_R tends to zero after the prescribed local thermodynamic limit, and
its dyadic variation is summable.

[candidate-C] The unchanged exact local certificates also survive:

    ell_(1,L) > 1/25,
    ell_(1,L) < 3/8,
    C_1[S_L] > -1/20,

for every even L>=4 at the certified scope.

The original full-covariance seed

    C_1[Q_L] > 1/40

is not falsified. It is simply not an infrared lower bound because a strictly
positive part larger than 1/25 lies in D_L and D_L has zero packet contrast in
the large-window limit.

The weight itself has only the zeroth and first harmonics:

    W(f) = 2 + zeta_5^f + zeta_5^(-f),

so in the inherited transform convention

    W_hat = (10,5,0,0,5) = 5(2,1,0,0,1).

This is consistent with the exact current representation already used in the
#1121/#1122 lineage.

### 2.2 Matrix statement withdrawn from the working theorem set

The review found a concrete defect in #1139 section 6.

That argument identified two packet gradient/adjoint-gradient Grams as having
the same diagonal gamma_R. For the coexact packet this identification is false:

    d* g_R = 0,

while

    ||d* f_R||^2/N_R
      = gamma_R
      = 3/R + 18/(2R^2+1).

At R=1 the relevant partial Laplacian witnesses are 5 and 4, not gamma_1=9.

Therefore the displayed #1139 bound

    -243 gamma_R G_R
      <= A_D-B_D
      <= 243 gamma_R G_R

is **not accepted as a theorem from the written #1139 proof**.

No counterexample to that inequality itself was produced. The correction is to
the proof status, not an assertion that the inequality is false.

This correction does not touch the exact scalar formula for ell_R or its
all-radius bound, because those results do not use the defective matrix step.

For continuation, do not cite the constant 243 as established evidence.

## 3. What #1140 adds after that correction

#1140 uses a different finite-depth locality/Bernstein argument and does not
need the invalid #1139 section-6 identification for its main scalar theorem.

Let P_L be the average of the eight genuine link-colour conditional expectation
projections in L2(mu_L), and V_L h = X(h). Define

    Q_(n,L) = V_L* P_L^n V_L,
    H_(n,L) = Q_L-Q_(n,L).

Then

    H_(n,L)
      = sum_(k=0)^(n-1) V_L* P_L^k (I-P_L) V_L,
    0 <= Q_(n+1,L) <= Q_(n,L) <= Q_L.

At n=1,

    H_(1,L)=D_L,
    Q_(1,L)=S_L.

[candidate-T] Every finite H_(n,L) has finite base range. The written #1140
argument gives, for admitted R,n,L,

    |C_R[Q_L]-C_R[Q_(n,L)]|
      <= a_L min{
           1,
           32(n+2)^2 gamma_R
         },

    gamma_R = 3/R + 18/(2R^2+1).

In particular, with n=m and R=m^4,

    |C_(m^4)[Q]-C_(m^4)[Q_m]|
      <= min{a,1536 a/m^2}

after taking the original local thermodynamic limit first.

This is useful because a growing number of finite-range layers may be removed
with an explicit vanishing scalar error. It does **not** determine the sign of
the remaining contrast.

The exact depth-two identity is

    Q_2 = S Q^(-1) S + M,

    M = V* P (I-Pi) P V >= 0,
    Pi = V Q^(-1) V*.

The positive operator M is nonlinear memory outside the original linear score
span. Its exact-minus-coexact contrast has no sign from M>=0 alone. Therefore
iterating the one-step compressed score covariance while dropping M is not
justified.

The mixed-matrix estimates in #1140 remain candidate-T and deserve a separate
review. This handoff does not use them to establish P1.

## 4. What cannot close the phase

The following routes are now explicitly excluded as sufficient arguments.

### 4.1 The R=1 full-covariance seed

    C_1[Q] > 1/40

is a true local candidate-C result at its scope, but more than 1/25 of local
positive contrast can sit in the finite-range D sector that vanishes in the
infrared. The seed is therefore not a protected continuum residue.

### 4.2 Perimeter tension without separation

The exact current-sector activity bound controls support size, but two small
loops can remain small while their separation tends to infinity. Therefore it
does not by itself give a current second moment or chi_*.

### 4.3 A uniform auxiliary resampling gap

If one proved a volume-uniform centered spectral gap g>0 for the auxiliary P,
then the #1140 bounds would instead force the ordered packet contrast to zero.
With actual P2 this would imply Delta=0.

Therefore a generic rapid-mixing proof for this auxiliary update is not a
positive photon proof.

### 4.4 q_min as a continuum coefficient

The lowest mode does not replace the ordered limit. The established restart
still requires the local thermodynamic limit before the infrared scaling
limit, or a separately proved equivalence theorem.

## 5. The clean direct P1 target

The strongest model-specific reduction remains the #1122 coefficient split.

For the complete admitted periodic limit set define

    b_*
      = inf liminf S_(n,02,02)(t e_1),

    chi_*
      = sup limsup S_(j,00)(t e_1)/lambda(t e_1).

When the current second moment exists,

    chi_j
      = -1/2 sum_x x_1^2 C_j(00;x).

The exact sufficient condition is

    boxed:
    b_* > 25 chi_*
      => AXIS-POS
      => positive phase coefficient at the stated candidate scope.

Equivalently, in the fixed split,

    Delta_0 = b - 25 chi.

This route bypasses the fragile R=1 seed. It asks directly whether the
transverse surface response survives more strongly than the charge-five
current stiffness.

## 6. Smallest missing theorem pair

The next attack should be named around these two quantities, not around another
local variance.

### P1a. Current stiffness upper bound

Prove, for the actual fixed W and uniformly along the accepted even periodic
sequence, a separation-dependent connected-sector estimate strong enough to
give a finite and explicit current second moment. One sufficient form is

    |I_L(j_1,tau_x j_2)|
      <= C(j_1,j_2) exp(-m |x|),

where

    I_L(j_1,j_2)
      = log [
          Q_(j_1+j_2) Q_0
          /
          (Q_(j_1) Q_(j_2))
        ]

when the involved sectors are nonzero, with the corresponding signed
combinations for j_1-j_2.

Exponential decay is sufficient, not declared necessary. Any explicit
distance bound implying the required weighted second moment is admissible.

The required output is an actual number or exact expression

    chi_* <= chi_upper.

### P1b. Transverse surface lower bound

Prove in the same accepted limit profile

    b_* >= b_lower > 0,

with an explicit finite-volume error budget and no q_min substitution.

The decisive certificate is then

    b_lower - 25 chi_upper > 0.

This is the shortest direct analytical closure of P1 presently visible.

## 7. P2 and spectral consequences after P1

P1 alone is not the whole photon program.

The #1126/#1130 lineage reduces the Euclidean scaling problem to actual
finite-volume/local-limit control of the derived defect kernels and their
second moments. #1130 gives the conditional finite-to-infinite comparison that
removes the spurious 1/epsilon^2 amplification when those finite-volume tails
are proved.

The #1131 spectral positive-filter construction then supplies the spectral
bridge only after its actual Euclidean hypotheses have been established and
reviewed.

Thus the honest dependency order is

    fixed-W P1:
       b_* > 25 chi_*
            |
            v
    actual S1 + P2 defect/limit hypotheses
            |
            v
    ordered Euclidean massless tensor
            |
            v
    spectral S7 positive-measure/pole-band bridge
            |
            v
    only then a photon-phase conclusion at that declared action scope.

The current Public Canon frontier has a still broader
PHOTON-MASSLESS-PHASE L4-to-L6 obligation. A positive result for this single
fixed W does not by itself close that Canon row unless the action-carrier and
bridge contract required there are also supplied.

## 8. Recommended next owner

The highest-value next item is not another packet-size sweep.

Suggested working identifier:

    C-PHOTON-BCHI-DIRECT-BOUND-N

Freeze before computation:

1. the exact definitions of b_* and chi_* from #1122;
2. one finite-volume approximation for each with explicit errors;
3. one separation-dependent current interaction target;
4. one transverse surface lower-bound target;
5. the single falsifier

       b_lower - 25 chi_upper <= 0

   for that chosen bound strategy.

A failed bound strategy is not a negative phase theorem unless its admissible
class is frozen complete.

## 9. Status table

| Item | Status after this handoff |
|---|---|
| #1139 scalar split Q=D+S | candidate-T retained |
| exact ell_R formula and all-radius scalar bound | candidate-T retained |
| #1139 local exact certificates | candidate-C retained |
| #1139 matrix constant 243 proof | **not accepted / proof gap recorded** |
| #1140 finite-depth scalar removal bound | candidate-T retained |
| #1140 depth-two nonlinear memory identity | candidate-T retained |
| positive C_1[S] | OPEN |
| b_* > 25 chi_* | OPEN |
| actual full S1 | OPEN |
| actual P2 finite-volume/second-moment hypotheses | OPEN |
| spectral S7 application to fixed W | OPEN |
| PHOTON-MASSLESS-PHASE | OPEN |

## 10. Source custody

Public sources:

- issue #1122, current-source Hessian and `b_*>25 chi_*`;
- issue #1125, P1/P2 reduction and closure-limit audit;
- issues #1135-#1137, localized packet construction and full-covariance seed;
- issue #1139, conditional covariance split;
- issue #1140, finite-depth residual relaxation;
- issue #1141, owner of this corrected handoff.

The supplied #1139 review is a review input, not a public authority object. Its
mathematical correction is restated self-contained above so continuation does
not depend on private or uploaded bytes.

No superseded source object is deleted. Negative and corrected results remain
first-class audit history.

Original new text: Apache-2.0.
