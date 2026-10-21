# Role contacts, coupled translation and energy selection

**PUBLIC / NON-CANONICAL / L1. Analytical contract.** A. M. Thorn.
Claim [#1624](https://github.com/mathorn1973/twist-j/issues/1624).
Sole branch/path: `notes/C-ROLE-CONTACT-GRAPH-ENERGY-SELECTION-N`.

This is a result-exposed analytical successor to #1621 and #1623. The
arguments and explicit word were discovered manually in this session.
This contract and SOURCES.md are frozen before final proof drafting,
not before discovery. No new scientific program, import, compilation,
enumeration, numerical calculation or experiment is planned. Source
programs are read only. Administrative Git/hash operations and unchanged
repository infrastructure checks are not scientific executions.

## 1. Equation and question

Keep the exact prepared three-cell carrier and source contact of #1623.
Write each cell content as h_i=(mu_i,lambda_i) in F5^2, i=0,1,2,
and u=(2,0), w=(1,1). Define

- A_j(rho): h_j=rho+u and h_l=rho for l!=j;
- B_i(rho): h_i=rho and h_l=rho+w for l!=i;
- T_ij, i!=j: transpose A_j(rho),B_i(rho) for every rho and fix every
  other triple, the counter and all shared controllers.

The source maps are T0=T_01 and T1=T_10. The other four roles are
separately supplied mathematical contacts, not inferred physical gates.

Determine the exact contact graph, composed transport and invariant
functions, then determine what those contacts select in three explicitly
different price families. Compare the entire contact law with the
already canonical affine/CSUM coupled alphabet, including an explicit
word realizing its nominated endpoints and the account on that word's
complete five-cycle.

## 2. Method

Use exact substitution in the original affine letters, commutator
identities, connected finite graphs, real linear algebra, positivity
and affine fixed-point bounds. Derive finite counts combinatorially;
no state enumeration or numerical sample is evidence. Supply the full
changed/fixed branches, composition convention, inverse domains and
fixed-context hypotheses. The 39-leaf construction is an algebraic
factorization, not the result of a word search or a minimum-length claim.

## 3. Carriers, readings and equality

### Prepared native chart

The source's actual 500-state cell H has coordinates
gamma=(A,z,r) in {1,4}^2 x F5 and h=(mu,lambda) in F5^2.
Three cells share gamma and one original counter n. There are
20*25^3=312500 prepared checkpoints at fixed n; both trace sheets
are included. At fixed gamma there are 25^3 content triples. The
source's inverse chart recovers every piston and q,r; it is reproduced
in the proof. At fixed gamma it is affine in contents, and
k=Az is either 1 or -1. Native U changes n,gamma and fixes all h_i.
Its inverse restrictions are inherited unchanged.

Equality of energy readings is pointwise equality on the same labelled
complete prepared state. A different choice of interaction prices is
not identified by relabelling states. The common calibration is
h0=0,h1=h2=(1,0), with account 4. Nonnegative readings vanish only
on the common-content diagonal in the positive families below.

### Price families

F6: for each unordered cell pair e=01,02,12 independently choose
f_e(0)=0, f_e(+-1)=alpha_e>0 and f_e(+-2)=beta_e>0. Use the same
f_e for both content coordinates on that edge and set

E=2 sum_{e={i,j}} sum_{l=1,2} f_e(h_i,l-h_j,l).

All six positive prices are independent before contact constraints.
No changing bank, preparation, reference-only or controller term is
included in this comparison. Such fixed terms cannot affect a contact
balance, and an independently changing term would alter the hypothesis.

Fcommon is the subfamily beta_e=kappa*alpha_e with one kappa>0 and
three independent positive alpha_e. The #1623 family additionally fixes
alpha_01=alpha_02=1, alpha_12=eta>=0 and beta_e=kappa*alpha_e;
the source's zero-edge case eta=0 is retained separately from strict F6.

Fpair is a deliberately broader comparison: one arbitrary even
g:F5^2->R with g(0)=0, E_g=sum_{i<j}g(h_i-h_j). This includes
coordinate-nonseparable pair functions. It is not claimed to exhaust
physical readings. The discrete whole-content account
2*#{i<j:h_i!=h_j} will delimit uniqueness outside F6.

### Declared coupled alphabet

Use the canonical KERNEL-CONNECT-ALL-K raw carrier (F5^6)^3, diagonal
original letters D_g, and complete-cell ring additions
R_i:x_(i+1)->x_(i+1)+x_i, indices modulo three. Its source permits
both orientations; the exhibited word needs only R_0,R_1 and D_a,D_c,D_d.
Every six-vector, including q,r, participates. This carrier has no
native counter or automatic gate calendar. Fixing an appended n is a
mathematical extension, not a derivation of physical timing.

Compile at a fixed parameter epsilon in {1,-1}. The nominated endpoint
family has actual k=Az=epsilon. The word's raw action is defined on the
entire coupled carrier; intermediate states need not have common Gamma
or lie in H. Its endpoint energy table applies only at complete-word
boundaries on the stated preparation. A putative nonnegative bank is
priced independently in the same chosen unit before its balance is
tested; no bank coordinate or law is supplied here.

The smaller common-letter class consists of the same original letter
applied to every cell sharing Gamma=(z,q,r), together with whole-cell
permutations. Arbitrary state-dependent choice within that smaller
class is allowed in its obstruction. CSUM and independent local W are
not silently included in this class.

## 4. Exact targets and systematics

1. Prove the 25 disjoint C6 branch graphs and remaining 15475 fixed
   content triples at fixed n,gamma. Any subfamily acts as the product
   of symmetric groups on its graph components, diagonally over rho.
   In particular T_01,T_10 have disjoint supports; all six generate a
   diagonal S6, not S6^25. Classify arbitrary real content invariants
   by these components, with dimension 15625-25*min(s,5) for s
   different roles. Prove explicit finite transport words, clearly
   distinguishing prepared mu deviations from lambda records and
   independent new messages. Equal energy need not imply reachability.
2. For F6, put a_i=sum_{e incident i}alpha_e and
   y_i=(sum_{e incident i}beta_e)/2. Prove full-carrier conservation
   of T_ij iff a_i=y_j. The six equations form the same C6.
   Establish rank min(s,5), price-space dimension 6-min(s,5), and
   dimension 5-min(s,5) after the common calibration. Any five roles
   select alpha_e=1,beta_e=2; fewer do not, even with all prices
   strictly positive. Exhibit a calibrated four-role counterfamily.
3. In Fcommon any three distinct roles force kappa=2 and equal edge
   weights, with three sharp. Preserve #1623's two-contact result
   in its smaller declared family. State this hierarchy without
   pretending that the comparison families are physically complete.
4. For Fpair conservation by the role family is equivalent to
   g(u)=g(w). Exhibit the discrete whole-content account, with the
   same calibration and all relevant role/translation/coordinate-swap
   symmetries, but values differing from the selected F6 account.
5. With v_d=(2,1,3,4,1,1), establish
   S_i(t)=D_d R_(i-1)^(-t) D_d R_(i-1)^t
   =translation by t*v_d in cell i. Products act right to left.
   Exhibit

   L_epsilon=S_1(epsilon) S_2(2epsilon)
     D_a [S_1(-epsilon) S_2(2epsilon)] D_a
     D_c S_2(-epsilon) D_c.

   Prove its exact raw displacement, 39 canonical leaves under
   positive-power expansion, order five, inverse, controller/reference
   restoration at boundaries, and X_rho->Y_rho on k=epsilon.
   Give the corresponding construction for every role without
   assuming a physically available relabelling gate. The sign choice
   is fixed at compilation; state-dependent selection is additional.
6. On L_epsilon^t X_rho prove the complete table
   E_t=2[f_kappa(2-t)+3f_kappa(t)+eta f_kappa(2-2t)], t=0..4.
   In particular E_2-E_0=4*kappa>0. The star sequence is
   8,8,24,26,14 and the equal-triangle sequence 8,8,16,16,12.
   Record necessary bank changes and any sharp lower bounds at these
   macro boundaries only. No microscopic funding or bank admission
   is inferred; closed-cycle differences telescope exactly.
7. Prove the distinct implementation boundaries: original prepared U
   fixes contents; common letters plus whole-cell permutations keep
   all-pair magnitude counts separately and cannot take X to Y;
   no fixed affine/CSUM word realizes the full sparse contact, by
   its 623 fixed points on F5^4. The last statement also covers
   affine auxiliary preparations followed by a fixed affine raw
   output projection, and does not require the auxiliaries restored.
   Separately, at fixed gamma,rho, an affine map conserving the
   entire E_(kappa,eta) family member for kappa>0, kappa!=1 cannot
   take X to Y: unique zero plus doubling forces both weighted
   magnitude counts conserved. Do not claim the excluded kappa=1
   case, arbitrary nonlinear controls or differently typed readings.
8. Preserve the canonical coupling theorem and distinguish its
   transitivity from energy conservation by a closed dynamics. Name
   the existing supplied nonlinear residual-contact architecture,
   its factor/full-state distinction and native-admission owner.
   No transport between its carrier and this contact is assumed.

## 5. Failure conditions

An incorrect generator/word identity, branch or inverse; an overlap of
the claimed disjoint state families; a rank error or positive calibrated
price below the claimed sharp threshold; a violation of a stated
account symmetry; an exact affine counterexample to the stated full
domain obstruction; or source evidence that identifies the declared
gate word with autonomous U invalidates the relevant conclusion.
Retain and correct such a failure openly. Narrow subclass obstructions
cannot close a broader native owner negatively.

## 6. Layer and delivery

L1 only. Pin and publicly read back these two files before final proof
drafting. Then add only PROOF.md, README.md, REVIEW.md and CHECKS.md;
the pinned files remain unchanged. Review the exact final proof in
three result-exposed same-session lanes, with no claim of blind or
external independent confirmation. Required x86_64/aarch64 CI checks
repository infrastructure, not a scientific replay.

Canon v103, #1621, #1623 and existing physical-admission owners remain
unchanged. No native autonomous contact, physical energy, occurrence,
new-message supply, microscopic bank, SI scale, entropy interpretation,
or particle/bank conversion is derived. In particular no dimensionless
number here is identified with payment 10, the Dirac gap or m/arctan(m).
No merge, release or Canon promotion is part of this delivery.
