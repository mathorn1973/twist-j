# Result

Status: PASS  
Scope: NON-CANONICAL, L1  
Probe: P-INTEGER-RECIPROCAL-SOURCE-ACTION-2  
Ownership: https://github.com/mathorn1973/twist-j/issues/1642  
Pin: 3ae3ea66e1e3c633c048ece10e3baf43f144d8c7

## Observed completed result

The first formal primary run completed with exit zero and empty stderr.
Its independent polynomial-ring and Gaussian-elimination breaker also completed
with exit zero and empty stderr and generated an identical 25-line certificate, after which verify.py appended its two terminal lines.
The 844-byte, 27-line final stdout has SHA-256
857a26b1a8caf10e90b56f0f2df222ea1d8557eb2f60a24ff6b32a8093d1bdd8.
EXPECTED.txt contains those exact bytes. RUN.md records custody and the local
environment.

No preregistered falsifier fired. No fixture or threshold was changed after the
public pin. This is a completed gate, not an abandoned pin. The frozen six-file
bundle remains unchanged.

| Finite audit | Observed result |
| --- | --- |
| Actual normative authority files | All 5 hashes and sizes match Public Canon v103 |
| Hermitian transports | 133 entries pass closure, inverse, determinant and cost checks |
| Full-carrier fixtures | 399 cores, 9576 funded entries, all declared inverse/account branches |
| Corrupt field images | 38 rejected by exact congruence; lower boundary also reflects |
| Coupling-selection audit | 34 representation-symmetry, parity-uniqueness and dipole checks pass |
| Field history | 750 records through counter 24 across a in {-1, 0, +1}, all exact primitive denominators and metric bounds |
| History payload SHA-256 | e3831741acc15d0ec25bf84565e25e46cf23723191d80dd36a91a25594d3e3b2 |
| Joint reciprocal action | 720 exact central variations (600 metric + 120 source/multiplier) vanish |
| Complete funded cycles | Least periods 14,26,28,14,14,14,18,14 |
| Negative controls | Zero-seed backreaction, disabled backreaction, disabled metric coupling, omitted inverse backreaction, omitted inverse source, wrong first multiplier and unrestricted metric degeneracy behave as preregistered |
| Primary/breaker certificate | Unmodified 25-line certificate stdout bytes identical |

## Concrete reciprocal witnesses

1. **Same-counter source-to-metric witness (k=2) and reciprocal backreaction (k=3):**
   At word 0010, the same initial field data and common bank 347059 allow both
   ready source signs to reach k=2 with primitive numerators

       P2(-)=(487,167,-230,130,94),
       P2(+)=(491,163,-230,130,94),
       h2(+)-h2(-)=(1,-1,0,0,0)/162,

   and sharp first-block banks 344409 and 347059 (leaving final banks 2650 and 0).
   Continuing through the second block to k=3 gives primitive numerators

       P3(-)=(120111,-6141,-59422,98366,57038),
       P3(0)=(120977,-7007,-59350,98366,56966),
       P3(+)=(121843,-7873,-59278,98366,56894).

2. **Pure gravitational backreaction witness on the zero-seed source (a=0):**
   Starting from H_0=0, R_0=0, D_0=0 at word 0010, the phase-6 field-to-source
   backreaction shear S^(beta(w)) injects beta(0010)=+1 into (H-R)_01 at k=1,
   which is transported by phase 0 of block 2 into chi_2(0)=+1. At k=2, the
   forced metric differs from the unbackreacted free K1 metric by

       h2(0)-h2(free)=(1,-1,0,0,0)/104976.

   When gravitational backreaction on the source is disabled (kappa_back=0),
   this contrast vanishes identically while the canonical free K1 field remains
   intact.

## What the proof adds beyond the finite audit

PROOF.md establishes B1-B5 at the explicitly declared scope:

- **Coupling-selection uniqueness (B1):** Under the four explicit structural
  conditions CS1-CS4 (order-6 transport covariance and dagger-oddness on
  Herm_2(Z[j]), support on the marked pair {0,1} with zero-mode orthogonality,
  minimal even-numerator parity for d_n=2*324^(n-1), and step-covariant integer
  recurrence scaling), the functional chi(H,R)=coeff_j((H-R)_01), the marked
  dipole ell=(1,-1,0,0,0) (up to sign), the factor 2, and the attenuation
  324^(-n) are uniquely determined.
- **Exact reciprocal reversibility (B2):** Because the phase-6 field-to-source
  shear S^(beta(P)) commutes with its inverse and P is unchanged during phase 6,
  the seven-phase reciprocal step is injective on the full 38-integer core with
  exact partial inverse Core^-1, and funded reflection yields a total bijection
  F^-1 = Rev F Rev conserving E+b.
- **All-counter primitive denominator and reciprocal difference equation (B3):**
  Despite the two-way recurrence chi_n(a;w)=a*chi_n^aut + beta_{n-1}(w), the
  least common denominator remains exactly d_n=2*324^(n-1) for all n>=1 and all
  ten canonical words.
- **All-counter Lorentz signature (B4):** Because |beta_n(w)|<=2 implies
  |chi_n(a;w)|<=4, the zero-sum operator bound establishes
  ||h_n - h_n^free||_inf < 499/313956 < 1/629 and
  -299/500 < h_n(r) < 499/500 for all n>=1, all ten words, and all three source
  branches a in {-1,0,+1}, proving g_n(r) has signature (-,+,+,+) and
  det g_n(r) < -999/250000 < 0.
- **Joint reciprocal action stationarity (B5):** Varying the joint discrete
  action A_joint[V,N^(1),N_i^(1),q,p] with respect to all six spatial metric
  components V_ab, lapse N^(1), shift N_i^(1), multiplier p_n, and source
  amplitude q_n simultaneously yields both the forced TT metric equation and
  the backreacted source recurrence on the TT representative V=diag(h,-h,0).

## Interpretation and open obligations

The construction is a selected discrete reciprocal source-and-TT-metric model
with exact integer storage, reversible admission, a conditional uniqueness
theorem for the coupling quadruplet, and a joint quadratic action principle
for two-way source-metric dynamics. It does not assign a new canonical status.
The structural axioms CS1-CS4, the coarse-grained integer parity-dipole link
beta(P), the adjoint source multiplier p_n in the joint action, and the bank
account remain NEW_DECLARED L1 modeling choices.

Passing from the selected linear TT sector to full nonlinear general relativity,
realizing the coupled update inside the native micro-law U without an external
schedule, and establishing a continuum manifold limit remain separate open
obligations.
