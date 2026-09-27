# PREREG: C-PHOTON-CONTACT-TURN-SKELETON-N

**PUBLIC, NON-CANONICAL. No authority.**
Author: A. M. Thorn <thorn@twistj.com>
Date: 27 September 2026. License: Apache-2.0.
Owner: issue #1192, session photon-contact-turn-skeleton-20260927.
Branch: `notes/photon-contact-turn-skeleton-20260927`.

## 1. Authority and inputs

Public Canon v92 is authoritative on public main.
Activation/tag: `8b1132d828d94f83e653dab34d686a7e68394939`.
Content: `d7eb6de16c11f6a105996de02ffd7afa32683a93`.
Canon SHA-256: `31783fcd8e5ad2a697efd92a6d9fb92c2a21c101b95b9c282ea50fa7cb245f68`.
Canon bytes: 797365. The five normative hashes, ancestry, main architecture
checks and publication checks were verified before this item was claimed.

Read at the above main commit:
- `notes/C-PHOTON-BCHI-DIRECT-BOUND-N/FULL-MEASURE.md`, section 10:
  the full-measure source estimate for a simple current cycle;
- `notes/C-PHOTON-BCHI-DIRECT-BOUND-N/CONNECTED-CURRENT.md`, sections 1-2:
  the exact one-copy paired representation and unique current-edge owner;
- `notes/C-PHOTON-BCHI-DIRECT-BOUND-N/SIGNED-SLICES.md`, section 1:
  the axial primitive and the definition of Xi_L.

These are non-canonical mathematical inputs, not a new physical action or
an assertion that their statements have been folded. The core source and
rooting arguments are restated in PROOF.md. Draft product/prism claims in
#1189 and #1191 are not mathematical dependencies. No file outside this new
notes directory is changed.

## 2. Scope and frozen objects

Layer L6, inside the fixed selected finite measure only. For every even
L>=4, V=L^4, use the periodic four-dimensional cubical complex and

    mu_L(n)=Z_L^-1 2^(-|supp n|) 1{partial n=0 mod5},
    n_p in {-1,0,1}, j=partial n/5.

Use the unchanged one-copy paired augmentation. A component K has current
J_K=partial eta_K/5 and cost ell_K defined by the integer cyclic primitive
of its orientation-zero current summed over slices x_1=r. Define

    Xi_quarter(L)=(1/V) E_aug sum_K
       1{J_K is one unit simple cycle, 4c_K<=m_K} ell_K^2.

Here m is cycle length and c counts changes of coordinate axis, INCLUDING
the closing vertex. A cycle is simple when no vertex repeats except its
closing vertex. A component current which is a single simple cycle has zero
winding because it is a boundary. No restriction on contact number, contact
sign, planarity, prism representation, neutral area or exterior current is
made in Xi_quarter.

The full Xi_L is NOT replaced by Xi_quarter.

## 3. Deterministic targets

A. At most six opposite parallel edge neighbors exist per edge, giving
O=O_++O_-<=3m. On a simple zero-winding cycle all reinforcing contacts split
uniquely into maximal straight two-strand ribbons (proper cyclic intervals
along the strand axis). If R_+ counts them, prove

    O_+=sum_i length_i,       R_+<=6c.

This implies: if O_+>6c(R-1), some such ribbon has length at least R.
It does not assert existence of one global prism or a disjoint costed cover.

B. For direction counts n0,n1, prove

    ell(gamma)<=n0*n1/4<=m^2/16.

The proof must explicitly periodize a finite-support primitive of a closed
lift, so no claim of an exterior zero interval on the torus is needed. It
must remain valid if the lift spans more than one period. Every simple
zero-winding cycle has c>=4, hence the quarter-turn class has m>=16.

## 4. Frozen source and counting certificate

At h=log 2 the existing source inequality gives for both current signs

    P(E_gamma union E_-gamma)<=2 a^m r^(c+O),
    a=15625/131072, r=34/25.

Freeze B=a r^3 and the turn tilt v=1/16. Since O<=3m and 4c<=m,

    a^m r^(c+O) <= B^m r^c
                   <= (2B)^m (rv)^c.

Since rv<1, deleting the closing-turn factor increases the tilted weight.
Starting along one fixed positive edge, an open nonbacktracking description
has one straight and six perpendicular continuations. Therefore

    W_m <= A q^(m-1),
    A=4B=4913/4096,
    q=2B(1+6rv)=741863/819200<1.

No optimization or adaptive parameter search is allowed. The same bound
holds separately for each root direction; orientation-specific ell rooted
expectations are NOT asserted equal.

Exact rooting over all 4V positive edges must then prove

    Xi_quarter(L) <= C_quarter
      =(A/64) sum_(m>=16) m^3 q^(m-1).

The verifier evaluates C_quarter by both exact formulas:

    sum_(m>=16) m^3 q^(m-1)
      =(1+4q+q^2)/(1-q)^4-sum_(m=1)^15 m^3 q^(m-1),

    T_R(q)=q^(R-1) [R^3/(1-q)+3R^2 q/(1-q)^2
                +3R q(1+q)/(1-q)^3
                +q(1+4q+q^2)/(1-q)^4].

For every R>=16 the latter also gives the uniform length-tail bound
Xi_quarter,>=R(L)<=(A/64)T_R(q). No limit exchange or full-Xi bound is claimed.
Print the reduced fraction and its least strict integer upper bound. This
integer is descriptive output, not a fitted acceptance threshold.

## 5. Frozen non-product family and finite audit

For every integer n>=5 let gamma_n be the planar L-strip boundary with
successive corners

    (0,0), (n+1,0), (n+1,1), (1,1), (1,n+1), (0,n+1).

Join these by unit steps and close. The intended all-n formulas are

    m=4n+4, c=6, O_+=2n, O_-=0, ell=2n+1,
    R_+=2, ribbon lengths n,n.

They are quarter-turn cycles. Prove that they violate the earlier signed
contact condition (41/25)^O_+(9/25)^O_- <= (73/70)^m for all n>=5, by
checking n=5 exactly and a strict all-n multiplicative step. Their
nonrectangular two-axis supports are outside the specific fixed-displacement
ribbon and product-prism constructions previously described. No broader
admissible prism class is said to be classified or excluded.

Frozen examples:
- all axis-aligned rectangles with side lengths 1,...,8;
- gamma_n for n=2,...,20 (n<5 audits geometry only);
- the four-dimensional nonplanar cycle
  (0,0,0,0),(1,0,0,0),(1,1,0,0),(1,1,1,0),(1,1,1,1),
  (0,1,1,1),(0,0,1,1),(0,0,0,1), then back to the origin;
- one staircase ribbon with base steps +e0,+e1 repeated n times,
  offset e2, for n=2,...,10. This tests many short contact ribbons, not
  a claimed long-prism exclusion theorem.

For every example test the integer lift and a sufficiently large even torus,
then translate it through the periodic seam and apply all ordered choices
of the two observed coordinate directions. Compute contacts by actual
plaquette boundary incidence, straight contact runs, turns, divergence,
primitive, winding and the deterministic inequalities. Verify source local
cosh inequalities for every sign choice on up to four selected edges, at
h=log 2, using exact rational cosh values. On integer pairs 0<=c<=m<=128
with 4c<=m verify the fourth-power version of the tilted inequality.
Check the path polynomial by exact four-dimensional direction transfer for
lengths 1,...,10 against (1+6rv)^(m-1); no cycle census or probability
measurement is performed.

Additionally periodize the synthetic finite profiles
H(r)=1 on [0,2L], H(r)=(-1)^r on [0,2L], and
H(r)=2 on [0,L-1], -1 on [L,2L-1], for L=4,6,8.
Check Delta(periodize H)=periodize(Delta H) and the l1 contraction. These
are algebraic primitive tests, not realizable current-cycle claims.
Check the cubic generating series through degree 32 and both T_R formulas
for R=1,...,24. All operations are integer or Fraction.

## 6. Freeze, execution and decision

Commit PREREG.md, PROOF.md and verify.py together and read them back before
the first scientific execution. Only static compilation/source review is
permitted before pinning. Execute the pinned standard-library verifier once
under an actual 45-second subprocess timeout, deterministic hash seed and
single-thread environment; record OS, architecture, Python, exact output
bytes and hashes. No source edits or retries are allowed under this pin.

Any assertion failure, exception, nonzero exit, nonempty stderr or timeout
fails the complete audit. Preserve failure; do not promote earlier output.
PASS corroborates the finite exact audits only, at candidate-C on one
architecture. PROOF.md is candidate-T pending separate mathematical review.
The builder also wrote the audit: no independent agent confirmation is claimed.

Full Xi_L, Xi_L^(2), high-turn cycles, multiple cycles in one paired
component, non-simple networks, P1, massless phase and physical photon remain
open. A later public fold is required for any promotion.
