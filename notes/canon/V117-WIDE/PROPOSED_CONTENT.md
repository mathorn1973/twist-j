# Content for review

**NON-CANONICAL.** The following entries are proposed for the first sealed
fold after v116, subject to the source merges, the outside review of the
alternative-count note and the release gates described in the
[proposal](README.md). The first entry replaces the text proposed in #2062.

## Canon section 2, after the rank-43 relay continuation

> ### C-H3-ROW0-PULSE-RETURN-N [C]
>
> Use the periodic 288 by 2 H3 station defined in the frozen code of
> P-H3-ROW0-PULSE-RETURN-1, with scattering receivers at x12 and x13, the
> common reference at x23, and the predecessor reader with its
> exact-control veto and row-1 onset correction as frozen there. Observe
> at the x13 to x14 port both transfer words on even ticks 98 through 256,
> reducing each word by the positive gcd of its integer coefficients and
> preserving its sign and zero. For an abstention that passes the veto,
> add a positive decision at tick 256 if the row-0 activity on even ticks
> 98 through 120 spells `000111110001`.
>
> In the two preregistered fresh panels the predecessor correctly signs
> 1597 of 1600 intact packets and abstains on three positives. The rule
> recovers all three, each directed 0 to 1 at mask phase 2, at signed
> gains -1216, +1088 and +1216. Every prior sign is kept, by construction
> of the rule. Each of the 20 directed intact groups scores 80 of 80. The
> 1600 exchanged tails score 1600 correct donor signs. The 3200 isolated
> presentations and 20 quiet controls receive no write.
>
> Of the 3226 fresh abstentions before the rule, 224 pass the veto: the
> three intact packets, their three exchanged copies and 218 isolated
> tails. No control matches the pattern and no true negative abstains, so
> the forecast against a new plus on a negative had no opportunity. Among
> intact packets the pattern occurs on 120 of 800 positives and on 0 of
> 800 negatives.
>
> All six silent positives of the opened and fresh panels share one raw
> late row-0 sequence. Each fresh rescue has the gain of an opened rescue
> shifted by 2048 with the sign reversed, and the same first late row-1
> tick: -1216 with +832 at 144, +1088 with -960 at 186, +1216 with -832
> at 238. The three full two-row primitive projections differ from one
> another and fall outside the 735 distinct projections of the two opened
> panels through their row-1 words, which the rule does not read.
>
> The rule, the verifier and the fresh rosters were public before the
> result was published. The reader is deterministic, so the committed
> answer order is a custody check. All eleven registered predicates pass;
> two of them hold by construction of the reader. This is finite L1
> orientation decoding for this station and these rosters. Q9 remains
> open.

## Canon section 2, with the QDD channel theorems

> #### QDD-PAIR-INTERVENTION-LOCALIZATION [T]
>
> Model. The input is C^5 with basis e_0,...,e_4. The physical subsystem P
> contains five corresponding orthonormal levels and may contain more.
> An isometry V: C^5 -> P tensor E represents everything up to one cut,
> with E holding all stocks, all memory and a purification of everything
> discarded. One isometry W: P tensor E -> R tensor F represents everything
> after the cut. J: C^5 -> R is an isometry. The same V, W and J are used
> in every trial. Fix 0<c<1 and s with c^2+s^2=1, s nonzero, and put
> U=cI+isX on C^2, where X exchanges the two coordinates. For a pair
> {a,b} of logical levels let L_ab: C^2 -> C^5 include the ordered pair,
> Q_ab project P onto its two levels, and G_ab act as U on Q_ab P and as
> the identity on the rest of P and on E. The idle trial applies W after
> V. The trial for {a,b} inserts G_ab at the cut. Received channels are
> the partial traces over F on the complete output R, with all coherences,
> leakage levels and loss flags.
>
> Statement. Let S be a set of logical pairs. Suppose the idle channel on
> each pair input equals the isometric channel of J L_ab, and for each
> pair in S the intervention channel equals the isometric channel of
> J L_ab U.
>
> 1. If the graph S on the five levels is connected, then V = I_P tensor eta
>    for one unit vector eta in E, where I_P includes the logical levels.
>    The same holds for inputs entangled with a passive reference.
> 2. If S is disconnected, the conclusion can fail with every hypothesis
>    holding exactly, even if arbitrary unitaries on each pair of S may be
>    applied repeatedly and all channels are known completely. In
>    particular four pair settings are necessary, and four suffice exactly
>    when they form a spanning tree.
> 3. For the star S={{0,k}: k=1,...,4} with c=4/5, s=3/5: if the
>    normalized Choi state of each of the five received channels, idle on
>    C^5 and the four pair settings, is within half trace distance t of
>    its ideal and t <= 1/16000, then some unit eta satisfies
>
>    ```
>    || V - I_P tensor eta ||_op <= sqrt(14160 t) + 1 - sqrt(1 - 2360 t/3).
>    ```
>
>    The interventions G_0k are exact in this statement. An independently
>    bounded pulse error must first be propagated into t.
> 4. Items 1 to 3 hold with the real rotation [[c,-s],[s,c]] in place of U.
>
> **Proof of 1.** A received channel that equals an isometric channel has
> a pure Choi state, so the Choi vector of the complete branch map is a
> product: W V L_ab = J L_ab tensor z_0 and W G_ab V L_ab = J L_ab U tensor
> z_ab for unit vectors z_0, z_ab in F. Here z_0 does not depend on the
> pair when the idle hypothesis holds on C^5; in general write z_0(ab).
> Put V_ab = V L_ab. Since W is an isometry,
>
> ```
> M = V_ab^* G_ab V_ab = (W V_ab)^* (W G_ab V_ab) = lambda U,
> lambda = <z_0, z_ab>.
> ```
>
> The Hermitian part of G_ab is cI+(1-c)(I-Q_ab). Taking real traces,
>
> ```
> 2c + (1-c) || (I-Q_ab) V_ab ||_HS^2 = 2c Re lambda.
> ```
>
> As 0<c<1 and |lambda| <= 1, the leakage term vanishes and lambda=1.
> Hence z_ab=z_0, and injectivity of W gives G_ab V_ab = V_ab U. Zero
> leakage puts V e_a and V e_b into span{e_a,e_b} tensor E. A connected
> graph on five vertices has a vertex v on two edges {v,a} and {v,b};
> the two spans meet in e_v tensor E, so V e_v = e_v tensor eta with eta
> a unit vector. If V e_x = e_x tensor eta and {x,y} is in S, the column
> of G_xy V_xy = V_xy U belonging to x reads
>
> ```
> (c e_x + i s e_y) tensor eta = c V e_x + i s V e_y,
> ```
>
> in either ordering of the pair because X is symmetric. As s is nonzero,
> V e_y = e_y tensor eta. Connectivity carries this to every level. A
> passive reference tensors every operator with an identity.
>
> **Proof of 2.** Let C(j) be the connected component of j and let f_C be
> orthonormal flags in E. Put V e_j = e_j tensor f_C(j), and let W send
> e_j tensor f_C(j) to J e_j tensor g for one unit g, extended to an
> isometry. Every unitary on a pair of S acts inside one component, so it
> preserves the range of V and acts there as V G, with G the corresponding
> logical unitary. Each received map is therefore J G tensor g exactly,
> for the idle trial and for every finite sequence of such unitaries. Two
> components give two orthogonal flags, so || V - I_P tensor eta ||_op is
> at least 1/sqrt(2) for every eta. Three or fewer edges on five vertices
> are disconnected.
>
> **Proof of 3.** Let f=<p,tau p> for the ideal Choi vector p and the
> received Choi state tau of a branch on an n-dimensional input. The
> difference |p><p|-tau is traceless Hermitian with trace norm at most
> 2t, so its operator norm is at most t and f >= 1-t. Split the branch
> isometry A = C_z tensor z + C_perp, where z is the unit environment
> direction of the component of the vectorized A along p and C_perp is
> supported on the complement of z. The off-diagonal block
> (I-|p><p|) tau p has norm at most t, which gives, for the ideal isometry
> J_A,
>
> ```
> || C_z - J_A ||_op <= 1 - sqrt(f) + sqrt(n) t / sqrt(f),
> || C_perp ||_op <= sqrt(n t).
> ```
>
> For a pair k let lambda=<z_0,z_k> and h=1-Re lambda. Expanding
> M_k=(W V_k)^*(W G_k V_k) in aligned and perpendicular parts with n=5
> for idle and n=2 for the pair, and using t <= 1/4, the aligned product
> differs from lambda U by at most (2+(sqrt5+sqrt2)/sqrt(3/4)) t, each
> aligned-perpendicular term is at most sqrt(2h) sqrt(n t) for its own
> n, and the perpendicular product is at most sqrt(10) t. Hence
>
> ```
> || M_k - lambda U ||_op <= 10 t + 4 sqrt(2 t h).
> ```
>
> With l_k = ||(I-Q_k)V_k||_HS^2 the exact real trace identity gives
> c h + (1-c) l_k/2 <= 10 t + 4 sqrt(2 t h). From
> 4 sqrt(2 t h) <= (2/5) h + 20 t follows h <= 75 t. As 4 sqrt(150) < 49,
> put a=59 t; then || M_k - lambda U ||_op <= a, l_k <= 10 a, c h <= a,
> and D_k = G_k V_k - V_k U satisfies
>
> ```
> || D_k ||_HS^2 = 4 - 2 Re Tr(U^* M_k) <= 4 h + 4 a <= 9 a.
> ```
>
> Write v_rj for the E-component of V e_j at physical level r, v=v_00,
> A_0 for the squared norm of column zero outside row zero, and B for the
> squared norm of the columns k>0 outside rows 0 and k. A wrong logical
> row of column zero is counted in three leakage sums and an extra row in
> four, so 3 A_0 + B <= 40 a. Rows k and 0 of the first column of D_k are
> i s (v - v_kk) and i s (v_k0 - v_0k), so
>
> ```
> sum_k ( ||v_kk - v||^2 + ||v_0k||^2 ) <= 2 A_0 + (2/s^2) sum_k ||D_k||_HS^2
>                                       <= 2 A_0 + 200 a.
> ```
>
> Adding A_0+B bounds the squared Hilbert-Schmidt error of V - I_P tensor v
> by 240 a = 14160 t. Since ||v||^2 = 1-A_0 >= 1-40a/3 > 0, replacing v by
> eta=v/||v|| costs at most 1-sqrt(1-2360t/3) in operator norm.
>
> **Proof of 4.** Choose a sign function d on the five levels with values
> 1 and i that differ across every edge of a spanning tree, and D the
> corresponding diagonal unitary, extended by the identity on extra
> levels. Conjugating V by D and W by D and by the unitary D_R with
> D_R J = J D turns the real rotation on each tree edge into U or its
> adjoint and preserves every Choi distance and the final norm. For the
> star, D=diag(1,i,i,i,i).
>
> The theorem certifies the encoded state at one cut inside this model.
> Physical addressing of the pairs, the shared coordinate frame, the
> common preparation and receiver process, and the identification of any
> apparatus with the model are separate obligations. It does not
> discharge QDD-INSTRUMENT-APPARATUS, QDD-INSTRUMENT-CLASS-COMPLETENESS
> or QDD-TERMINAL-EVENT-SEMANTICS.

## Canon section 2, after QUADRATIC-L5-NATIVE-OBSTRUCTIONS

> ### QUADRATIC-L5-SOURCE-SYMMETRY [T]
>
> Use the carrier, marked reading and target of DEF-QUADRATIC-MEMORY-L5
> with symmetric C of rank at least four, and
> G(x,y)=(x^T C x, x^T C y, y^T C y), M(a,b,c)=(3b, 4a+4b+4c, 3b+3c).
>
> 1. C has a vector u with u^T C u=1. Put R(v)=2(u^T C v)u-v and let S
>    act by R on both cells and trivially on ignored memory. S is a
>    C-isometric involution with fixed space span(u) in each cell. Every
>    complete transition T that commutes with S fails at the ready state
>    z=(u,0,0): its image is S-fixed, so both output cells are multiples
>    of u and the output Gram has rank at most one, while the required
>    Gram M(1,0,0)=(0,4,0) has rank two. The argument allows nonlinear T,
>    arbitrary full-state words and any ignored register on which S acts
>    trivially, and needs no reversibility. Hence every contact that
>    succeeds at z satisfies S(Tz) != T(Sz), and no alphabet whose complete
>    primitive maps all commute with S realizes the target.
> 2. There is a complete permutation T of the carrier that commutes with
>    the common scalar action s(x,y,eta)=(sx,sy,eta) of F5^*, satisfies the
>    readout equation on its reachable set from the ready layer, and has
>    the minimum reachable size of QUADRATIC-L5-INITIALIZED-CAPACITY. It
>    has T^20=I, and T^10 acts as -1 on the chosen nonzero orbits. Common
>    scalar symmetry is therefore no obstruction. The matching that defines
>    T is derived from the target and is not a native primitive.
>
> **Proof.** The two sections "A source reflection must be broken" and "A
> minimal abstract lift can keep common scalar symmetry" of the merged
> source note, with two additions from its review: R is minus the
> reflection in the complement of u, and n(g)=n(-g) is even because -1 and
> 2 act freely on the nonzero Gram fibres.

> ### QUADRATIC-L5-AFFINE-ALTERNATIVE-COUNT [T]
>
> Use the carrier, marked reading and target of DEF-QUADRATIC-MEMORY-L5.
> Let C be symmetric of rank r. Let the ready data projection select, by
> any rule, among m affine maps f_i(z)=A_i z+t_i on V^2. An input z is
> covered when some f_i satisfies G(f_i(z))=M G(z).
>
> 1. For 3 <= r <= 6, no five affine maps cover the complete common-ready
>    layer. This holds for singular and translated maps, for arbitrary
>    selection rules and for any ignored memory.
> 2. If r=4 and the nondegenerate part of C has square determinant, six
>    linear maps cover the layer, so six is the least number. This class
>    contains C=K+0_2 of DEF-RESIDUAL-CONTACT-ARCHITECTURE. For C=I_4+0_2
>    the six maps are
>
>    ```
>    f(x,y) = ( x + 2y + psi(3x+4y),  2x + 3y + psi(4x+2y) ),
>    psi = alpha L_i + beta L_j,
>    (alpha,beta) in {(3,0),(0,1),(1,1),(2,3),(4,2),(4,3)},
>    L_i = [[0,4,0,0],[1,0,0,0],[0,0,0,4],[0,0,1,0]],
>    L_j = [[0,0,4,0],[0,0,0,1],[1,0,0,0],[0,4,0,0]],
>    ```
>
>    acting on the nondegenerate coordinates, with any action on the
>    radical.
> 3. In the class of item 2 one affine map agrees on at most 29/125 of
>    the layer, and (x,y) -> (x+2y, 2x+3y) attains this.
> 4. For the other classes of rank four, five and six the least number is
>    at least six. Its exact value is open there.
>
> The six-map selector of item 2 has forced fibres of size four. A binary
> contact needs fibres of size at most two, so the cover is not the data
> projection of a binary contact and supplies no realization for
> QUADRATIC-MEMORY-NATIVE-CONTACT.
>
> **Proof.** The merged alternative-count note: the reduction of the
> target to q(x')=q(x)+q(y), B(x',y')=B(x,y), q(y')=q(y); the
> classification of the maps whose second and third residuals vanish
> identically; the bound 4*5^(2r-2) for every other affine map; the count
> in three cases; and the explicit cover. The bound of item 3 is the
> scalar count of the source note of QUADRATIC-L5-SOURCE-SYMMETRY.

## Addition to QUADRATIC-MEMORY-NATIVE-CONTACT

Append to the paragraph that lists what the data projection of a
successful binary contact must satisfy:

> By QUADRATIC-L5-SOURCE-SYMMETRY the complete transition must fail to
> commute with the source reflection at the ready state (u,0,0). By
> QUADRATIC-L5-AFFINE-ALTERNATIVE-COUNT the ready data projection is not
> a selection among five or fewer affine maps. Neither statement closes
> this owner.

The registry scope and falsifier of the owner are unchanged.

## Registry and evidence

- **C-H3-ROW0-PULSE-RETURN-N**, status `C`, section
  `2. Time, space, and the decoder`, layer `L1`, `COMPUTATION`.
  - **Scope** At L1 on the periodic 288 by 2 H3 station frozen in
    P-H3-ROW0-PULSE-RETURN-1, a row-0 pulse-return rule at the x13 to x14
    port recovers all three previously silent positives in the 1600
    preregistered fresh intact presentations and keeps every prior sign;
    all 1600 exchanged tails score their donor sign and all 3220 isolated
    or quiet controls stay silent; 224 of 3226 abstentions were eligible
    for the new write and no true negative abstained; the three rescues
    repeat the raw late row-0 sequence of the opened rescues at gains
    congruent to theirs modulo 2048 with reversed sign.
  - **Falsifier** An exact replay of the frozen station and rosters that
    gives a FULL or SWAP call different from the transcript, a write on a
    control, an altered predecessor sign or a different canonical answer
    hash rejects the finite claim. A custody, runtime or stdout-byte
    failure without such a contradiction is STOP. A new roster is a new
    probe.
  - **Evidence** `EV-C-H3-ROW0-PULSE-RETURN-N`, kind `PUBLIC_PROBE`, at
    `probes/P-H3-ROW0-PULSE-RETURN-1`, `bundle-manifest-sha256-v1`,
    `two-architecture`, recomputed at the merged source.
- **QDD-PAIR-INTERVENTION-LOCALIZATION**, status `T`, section
  `2. Time, space, and the decoder`, layer `L1`, `THEOREM`.
  - **Scope** At L1 in the stated isometric intervention model with a
    common preparation, a common receiver process and exact pair
    rotations acting only on the physical subsystem, exact agreement of
    the idle and pair channels with their ideals forces the preparation
    to be the logical inclusion tensored with one environment vector
    exactly when the addressed pairs form a connected graph on the five
    levels; for the star with c=4/5 and Choi distance t at most 1/16000
    the operator-norm error is at most
    sqrt(14160 t)+1-sqrt(1-2360 t/3); the same holds for real rotations;
    physical addressing, a shared frame and the identification of an
    apparatus with the model are not supplied.
  - **Falsifier** A model instance with a connected pair graph, exact
    ideal channels and a preparation that is not of the stated form; an
    instance within the stated tolerance that violates the bound; or a
    disconnected pair graph for which the hypotheses force the
    conclusion.
  - **Evidence** `EV-QDD-PAIR-INTERVENTION-LOCALIZATION`, kind
    `INLINE_CANON`, location `inline`, `registry-scope-sha256-v1`,
    `none`.
- **QUADRATIC-L5-SOURCE-SYMMETRY**, status `T`, same section, layer
  `L1`, `THEOREM`.
  - **Scope** At L1 for symmetric C of rank at least four and the fixed
    quadratic target, every complete transition commuting with the
    diagonal source reflection S of a norm-one vector u fails at the
    ready state (u,0,0), for nonlinear transitions and any ignored
    memory on which S acts trivially; separately a complete permutation
    commuting with the common scalar action attains the minimum
    reachable size with T^20=I; the reflection result is a necessary
    condition on native contacts and the lift is an abstract existence
    statement, not a native realization.
  - **Falsifier** A transition commuting with S that sends (u,0,0) to
    the required Gram value; or a failure of the stated lift to be a
    permutation, to commute with the scalars, to satisfy the readout
    equation on its reachable set or to have the stated reachable size.
  - **Evidence** `EV-QUADRATIC-L5-SOURCE-SYMMETRY`, `INLINE_CANON`,
    `inline`, `registry-scope-sha256-v1`, `none`.
- **QUADRATIC-L5-AFFINE-ALTERNATIVE-COUNT**, status `T`, same section,
  layer `L1`, `THEOREM`.
  - **Scope** At L1 for symmetric C of rank three to six and the fixed
    quadratic target, no selection among five affine data maps covers
    the complete common-ready layer; for rank four with square
    determinant of the nondegenerate part, which includes K+0_2, six
    explicit linear maps cover it and one affine map agrees on at most
    29/125 of it; in the other classes of rank four to six the least
    number is at least six and otherwise open; the six-map selector has
    forced fibres of size four and is not a binary contact.
  - **Falsifier** Five affine maps covering every ready input for some
    C of rank three to six; an input of the stated class not covered by
    the six listed maps; or an affine map agreeing on more than 29/125
    of the layer in that class.
  - **Evidence** `EV-QUADRATIC-L5-AFFINE-ALTERNATIVE-COUNT`,
    `INLINE_CANON`, `inline`, `registry-scope-sha256-v1`, `none`. The
    exact verifier of the source note is a supplementary audit.
- **Dependencies** `QUADRATIC-L5-SOURCE-SYMMETRY` REQUIRES
  `DEF-QUADRATIC-MEMORY-L5` and `QUADRATIC-L5-INITIALIZED-CAPACITY`.
  `QUADRATIC-L5-AFFINE-ALTERNATIVE-COUNT` REQUIRES
  `DEF-QUADRATIC-MEMORY-L5`. `QUADRATIC-MEMORY-NATIVE-CONTACT` is
  BOUNDED_BY both new theorems, with the basis used for its existing
  three edges. All of these items are at L1, so no gate is needed. The
  QDD theorem has no dependency edge.
- **History** Four `DECLARE` events with previous status `-`, release
  `canon-v117`, the finalized scope hashes and the actual fold date.

## Build from the integrated sources

Apply the four sections and the owner paragraph, append the ledger rows
and add a v117 changelog entry. Regenerate the Canon views and normative
checksums. Keep the core selection, frontier, gate rows and reproduction
directory count. The inventory becomes 638 claims with 482 T and 50 C;
`evidence_none` becomes 204 and `evidence_two-architecture` 394. Update
the assertions in `tools/test_architecture_map_report.py` accordingly.

Extend the status-separation reverse-delta chain to reconstruct the exact
v116 inputs from the final v117 files, and audit the four new
registrations against the frozen sources. Then run policy, units, Canon,
ledger, gate-contract and static activation checks before freezing and
running the release candidate. The release-form commit carries the new
`STATUS.md`, `README.md` and `CITATION.cff` only.
