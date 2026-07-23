# P-TM-SYM2-SEMILINEAR-GAUGE-1 predefinition (NON-CANONICAL)

Status: DEFINITION/THEOREM SURFACE ONLY; NO FORMAL EVALUATION; NO CLAIM
CHANGE

This note freezes a theorem-grade successor definition for public issue
[#132](https://github.com/mathorn1973/twist-j/issues/132). It is not a
preregistration, probe result, Canon patch, or permission to execute a
verifier.

## 1. Authority, public antecedent, and present authorization

The authority at the definition-branch parent is:

```text
state:               ACTIVE
Canon:               Public Canon v16
tag:                 canon-v16
definition parent:   284b3e28cba9daa80ec757592656e2ecbbfddfe0
definition issue:    #132
definition branch:   definition/P-TM-SYM2-SEMILINEAR-GAUGE-1
future probe id:     P-TM-SYM2-SEMILINEAR-GAUGE-1
```

The owner authorization in issue #132 permits only the present definition
work. In particular, it does not authorize the reserved `probe/` branch,
a `probes/` directory, an evaluation, or a formal result. Those actions
require a later, separate public formal-lock issue after this definition is
merged and read back.

The completed public antecedent is
`probes/P-TM-SYM2-MEASURE-1/`, opened under issue #130 and merged by PR
#131. Its two-architecture exact result is taken as an input and is not
replayed:

```text
Sel_class cardinality:            48
projective-linear gauge G order:  12
postcomposition action:           free
G-orbits:                         4
orbit sizes:                      12, 12, 12, 12
route:                            NEGATIVE / N2
```

The archived raw output, orbit blocks, and hashes are evidence already
public under that antecedent. This note derives consequences from them by
proof. It neither imports nor executes the old evaluator.

## 2. Frozen carriers and oriented-pair coordinates

Let

```text
K   := Q(sqrt(5)) = Q(phi),       phi := (1 + sqrt(5))/2,
tau : K -> K,                     tau(a + b sqrt(5)) := a - b sqrt(5).
```

Thus `tau(phi) = 1 - phi`. The registered ordered projective lines are

```text
v1 = (0,1,phi),       v2 = (0,1,-phi),
v3 = (1,phi,0),       v4 = (1,-phi,0),
v5 = (phi,0,1),       v6 = (phi,0,-1),
```

and the owner-adopted involution is

```text
sigma_line = (v1 v2)(v3 v4)(v5 v6).
```

Freeze the following orientations of the three domain pairs and three
target pairs:

```text
D0 = (001,110),       E0 = (v1,v2),
D1 = (010,101),       E1 = (v3,v4),
D2 = (011,100),       E2 = (v5,v6).
```

Write `D_(i,b)` and `E_(j,b)`, with `b in F2`, for the first member when
`b=0` and the second member when `b=1`. Then bit negation and
`sigma_line` add `1` to the corresponding second index.

Let

```text
W := Cent_Sym(Lines)(sigma_line).
```

Every `a in W` is represented uniquely by

```text
pi_a in S3,       delta_a = (delta_a,0,delta_a,1,delta_a,2) in F2^3
```

through

```text
a(E_(j,b)) = E_(pi_a(j), b + delta_a,j).
```

Conversely every such pair gives a permutation commuting with
`sigma_line`. Hence

```text
W ~= C2 wr S3 = F2^3 semidirect S3,
|W| = 2^3 3! = 48.
```

This is an abstract permutation centralizer. It is not adopted as gauge.

Every member of the frozen selector class is likewise represented uniquely
by

```text
pi_s in S3,       epsilon_s in F2^3,
s(D_(i,b)) = E_(pi_s(i), b + epsilon_s,i).
```

Define the convention-only base selector

```text
s0(D_(i,b)) := E_(i,b).
```

In the archived tuple convention this is `(0,2,4,5,3,1)`. It is a
coordinate origin, not a preferred microscopic selector. Every selector is
uniquely `w o s0` for `w in W`; thus `Sel_class` is a `W`-torsor and the
two selector functions below are precisely the pullbacks of the two group
characters along this base identification.

## 3. The two residual-orientation characters

For `a in W`, define the two group characters

```text
chi_Q(a) := sgn(pi_a),
chi_F(a) := (-1)^(delta_a,0 + delta_a,1 + delta_a,2).
```

For `s in Sel_class`, define the corresponding torsor coordinates

```text
chi_Q(s) := sgn(pi_s),
chi_F(s) := (-1)^(epsilon_s,0 + epsilon_s,1 + epsilon_s,2).
```

The latter are functions on the selector torsor, not homomorphisms from a
group of selectors. Their covariance under the `W` action is the
load-bearing statement.

If `a,b in W`, then

```text
pi_(a b) = pi_a pi_b,
delta_(a b),j = delta_b,j + delta_a,pi_b(j)       in F2.
```

Therefore permutation of the three summands leaves their sum unchanged and

```text
chi_Q(a b) = chi_Q(a) chi_Q(b),
chi_F(a b) = chi_F(a) chi_F(b).
```

Similarly,

```text
pi_(a o s) = pi_a pi_s,
epsilon_(a o s),i = epsilon_s,i + delta_a,pi_s(i),
```

so

```text
(chi_Q,chi_F)(a o s)
  = (chi_Q,chi_F)(a) (chi_Q,chi_F)(s)
```

componentwise. Both characters are surjective and independent: pair
transposition changes only `chi_Q`, while one within-pair flip changes only
`chi_F`. Consequently

```text
K0 := ker(chi_Q) intersect ker(chi_F)
|K0| = 48/4 = 12.
```

Each of the four selector fibers of `(chi_Q,chi_F)` also has exactly 12
members.

## 4. Identification of the old linear gauge and its four orbits

Let `H` be the effective signed-coordinate stabilizer adopted in the v16
owner definition. Its publicly certified order is 12, and the old
definition gives `H <= G <= W`.

There is also a direct character proof that `H <= K0`. Number the coordinate
axes cyclically and write `e_r` for the coordinate basis, with indices
modulo 3. The three zero-coordinate pairs are

```text
F_r = {
  [e_(r+1) + phi e_(r+2)],
  [e_(r+1) - phi e_(r+2)]
}.
```

In the frozen target order, `(F_0,F_1,F_2) = (E0,E2,E1)`. A coordinate
permutation preserving this line set must preserve the cyclic placement of
the coefficients `1,phi`. A reversal would exchange their ratio with its
inverse, which is not a registered ratio because `phi^2 != 1`. Thus its
coordinate permutation is cyclic and hence even. Conjugating by the fixed
reordering `(F_0,F_1,F_2) = (E0,E2,E1)` does not change parity, so
`chi_Q=+1`.

For diagonal coordinate signs `(eta_0,eta_1,eta_2)`, the three relative
pair-orientation multipliers are, up to the cyclic relabelling,

```text
eta_1 eta_2,       eta_2 eta_0,       eta_0 eta_1.
```

Their product is `+1`; a cyclic coordinate permutation itself preserves
the displayed first/second convention. Hence an even number of target
pairs is flipped and `chi_F=+1`. This proves `H <= K0`.

Equivalently, the effective group is generated explicitly by

```text
r  : (x,y,z) |-> (z,x,y),       (pi_r,delta_r) = ((0 2 1),000),
dx : (x,y,z) |-> (-x,y,z),                     delta_dx = 011,
dy : (x,y,z) |-> (x,-y,z),                     delta_dy = 110,
dz : (x,y,z) |-> (x,y,-z),                     delta_dz = 101.
```

The three sign flips are read modulo the ineffective common sign `-I`;
their effective permutations form the Klein four group, and `r` cycles its
three nonidentity elements. This gives `H=V4 semidirect C3` directly, and
every displayed generator has `chi_Q=chi_F=+1`.

The public antecedent now supplies the two order equalities:

```text
|H| = 12,       |G| = 12.
```

Since `H <= G` and `H <= K0`, while `|K0|=12`, it follows without a new
evaluation that

```text
G = H = K0 = ker(chi_Q) intersect ker(chi_F).
```

Moreover

```text
K0 ~= {delta in F2^3 : sum delta_i = 0} semidirect A3
   ~= (C2 x C2) semidirect C3
   ~= A4.
```

Here the `C3` factor cyclically permutes the three nonidentity elements of
the Klein four subgroup, which is the standard `A4` action.

Because the old `G` action is free, each old orbit has 12 elements.
Character covariance makes every old orbit lie in one 12-element character
fiber. It must therefore equal that fiber. This proves that the four old N2
blocks are exactly the four fibers of `(chi_Q,chi_F)`, not merely four
blocks that happen to have the same size.

This character description is a post-N2 theorem that coordinatizes the
already-public orbit partition. It is not represented as a preregistered
discriminator, a pre-N2 selector principle, or a derivation of one preferred
selector.

For explicit readback, interpret an archived selector tuple in the window
order

```text
(001,010,011,100,101,110)
```

and use line indices `0,...,5` for `v1,...,v6`. The four archived minimal
representatives give:

```text
old block   minimal representative       chi_Q   chi_F
1           (0,2,4,5,3,1)                  +       +
2           (0,2,5,4,3,1)                  +       -
3           (0,4,2,3,5,1)                  -       +
4           (0,4,3,2,5,1)                  -       -
```

The signs name the fibers relative to the frozen orientations in section 2.
They are not physical signs and do not prefer one fiber.

## 5. Selector-independent macro observables

The following facts were already established on the public antecedent and
are independent of the four microscopic character fibers.

The unique normalized stationary window law is

```text
f_w = 1/6       for every w in W3.
```

Every `s in Sel_class` is a bijection. Therefore its line pushforward is

```text
nu_s(v_i) = 1/6       for i=1,...,6,
```

regardless of `(chi_Q(s),chi_F(s))`. With the registered line projectors,

```text
M_s(B) := sum_w f_w Tr(P_(s(w)) B) P_(s(w))
        = (1/6) sum_i Tr(P_i B) P_i
        = (1/3) P1(B) + (2/15) P5(B).
```

Thus the exact commutant and its `5:2` coefficient ratio are common to all
48 selectors.

On `Q = W3/<N>`, the quotient transfer has the uniform stationary law, so

```text
third_f(O) = 1/3       for every O in Q.
```

Within the frozen owner-adopted phaseful coefficient dictionary, the
two-point coefficient support gives the typed sheet law

```text
half_O = (1/2,1/2)
```

and hence `mu_B^f=f`. The exact leading-pair pushforward is, in the order
`00,01,10,11`,

```text
(pi_12)_* f = (1,2,2,1)/6.
```

In particular the typed event `E_00={001}` has weight `1/6`. Changing `s`
only relabels its line-side image.

These are macro-level invariants of the uniform law, the bijective selector
class, and the already-adopted coefficient dictionary. They do not:

- choose a selector or a `(chi_Q,chi_F)` fiber;
- turn a cardinal average into a canonical microscopic selection;
- repair the old N2 canonicality failure;
- open either registered layer gate;
- supply an L6 physical-probability theorem.

## 6. Adversarial priorness and overfit audit

The successor question is legitimate but must not be confused with a
pre-existing answer.

1. **The boundary predates the N2 output; the present definition does not.**
   The pre-N2 selector-class input explicitly left “whether Galois
   conjugation of `Q(phi)` preserves the structure” as an output for a
   future evaluation. The immutable preregistration then explicitly
   excluded semilinear and Galois transformations from the first probe.
   Thus the boundary was publicly named and remained unevaluated before
   N2. The exact group, character interpretation, route taxonomy, and scan
   contract in this note are new post-N2 definitions and are not presented
   as having been preregistered.

2. **Ordered labels only name the characters.** The registered list order,
   the order of the three pairs, and each first/second convention make
   `chi_Q,chi_F` writable. Reversing one pair convention or applying an odd
   pair relabelling changes a sign name. No such convention proves that a
   particular sign value is selected.

3. **Zero patterns do not provide a quotient bijection.** The target lines
   have three zero-coordinate pairs, but the old owner root adopted only
   the pairing `sigma_line`. It did not adopt a map from the three domain
   `N`-orbits to those three target pairs, nor an orientation within a
   target pair.

4. **A minority-bit/zero-coordinate dictionary would be new.** One may
   manufacture a selector by matching a window's minority coordinate to a
   target zero coordinate and then using a bit to choose a sheet. Neither
   the matching chirality nor the sheet sign was a registered map before
   N2. Adopting either after reading the four blocks would add an owner
   root; it is not a deduction in this lane.

5. **The child maps do not select a fiber.** The Thue-Morse child maps
   `L,R` commute with `N` and descend to `Q`, but they are not bijections of
   `W3`. No registered target-side pair of maps on `Lines` was frozen for
   an intertwining equation. Inventing such target dynamics now would be a
   distinct bridge hypothesis.

6. **Uniform data are maximally non-discriminating here.** The stationary
   law is constant and is preserved by all of `W`, not only by `G`. The
   pushforward weights, moment, pair law, `third`, and typed `half`
   therefore cannot distinguish the four character fibers.

7. **Gram and averaged Galois stability are insufficient.** All fifteen
   line pairs have the same squared cosine `1/5`. The registered moment is
   Galois-stable as an averaged rational endomorphism, but that does not
   assert that Galois conjugation is realized by a permutation of the six
   individual lines. The latter is exactly the future information-bearing
   question.

8. **Registered lift signs have the wrong type for a selector.**
   `RAMIFIED-TM-LIFT` supplies the L1 sign quotient and explicitly says the
   quotient alone is inversion-blind. `SQRT-PHI-DIGIT-LIFT` explicitly
   supplies no sign-branch selection. Neither row maps a window pair to a
   zero-coordinate pair or maps its sign to one of `v_(2j+1),v_(2j+2)`.
   `TIME-CUT-READING` also claims no forcing or uniqueness.

9. **The full wreath product is not a repair.** Declaring all of `W` to be
   gauge would collapse the selector torsor by definition. No registered
   projective or semilinear realization supports that enlargement, and it
   is outside this lane.

This audit is part of the definition. A future result may enlarge the
effective gauge only by the exact semilinear realizations below; it may not
choose additional roots after seeing the Galois-coset output.

## 7. Semilinear realization group and effective gauge

It is important not to identify a priori a projective-semilinear
transformation with its permutation on the six lines. Define first the
realization group

```text
tilde_Gamma_sl := {
  ([B],e) : e in F2, B in GL_3(K),
  [v] |-> [B tau^e(v)] induces a permutation of Lines
  commuting with sigma_line
}.
```

For fixed `e`, matrices are identified exactly by

```text
(B,e) ~ (c B,e),       c in K^*.
```

There is no scalar identification between different exponents. Exact
composition and inverse are

```text
([B],e)([C],f) = ([B tau^e(C)], e+f),
([B],e)^(-1)   = ([tau^e(B^(-1))], e),
```

where exponents are reduced modulo two.

Let

```text
rho : tilde_Gamma_sl -> W
```

send a realization to its induced line permutation, and define the
candidate effective semilinear equivalence group

```text
Gamma_sl := image(rho) <= W.
```

The exponent-zero subgroup of `tilde_Gamma_sl` is the old projective-linear
group `G`. The next lemma proves that, for this particular registered
six-line configuration, `rho` is faithful. Thus the realization group and
effective gauge may be canonically identified only after the lemma, not by
definition.

### Faithfulness lemma

No exponent-one projective-semilinear transformation fixes all six
registered lines pointwise.

Proof. Use the exact projective frame

```text
b1 := -phi v1,       b2 := -phi v2,       b3 := v3.
```

Direct substitution gives

```text
v4 = b1 + b2 + b3,
v5 = (phi-1)b1 + b2 + phi b3.
```

Suppose `h=([B],1)` fixed every registered line. Since it fixes the three
basis lines, write `h(b_j)=alpha_j b_j`. Since it also fixes
`[b1+b2+b3]` and `tau(1)=1`, independence of the `b_j` forces
`alpha_1=alpha_2=alpha_3`. A common projective rescaling therefore makes
`h` act in this frame by coefficientwise `tau`.

It would then send the displayed frame coordinates of `v5` to

```text
(tau(phi-1),1,tau(phi)) = (-phi,1,1-phi).
```

For this to be proportional to `(phi-1,1,phi)`, the middle coordinate
forces proportionality factor `1`; the first coordinate would then require
`-phi=phi-1`, which is false in `K`. This contradiction proves the lemma.

If two elements of `tilde_Gamma_sl` induced the same line permutation,
their quotient would fix all six lines. At exponent zero, fixing the
projective frame forces the identity; at exponent one, the lemma excludes
the quotient. Hence `rho` is injective and

```text
tilde_Gamma_sl ~= Gamma_sl.
```

This proof is a static projective-frame theorem. It does not enumerate the
exponent-one incidence systems and does not decide whether a nontrivial
Galois coset exists.

## 8. Analytic ceiling, dichotomy, and scientific routes

The exponent map

```text
exp : tilde_Gamma_sl -> Gal(K/Q) ~= C2
```

is a homomorphism with kernel `G`. Its image is either trivial or all of
`C2`. Together with faithfulness and `|G|=12`, this proves before any
formal pin:

```text
|Gamma_sl| is exactly 12 or 24.
```

This bound follows from the exact sequence

```text
1 -> G -> tilde_Gamma_sl -> image(exp) -> 1,
```

not from freeness of the selector action. If an exponent-one element `h`
exists, all exponent-one elements form the single coset `hG` (equivalently
`Gh`) of size 12. Its effective permutation
is not in `G`; therefore

```text
(chi_Q(h),chi_F(h)) != (+1,+1).
```

Postcomposition by `h` translates the four character fibers by that one
nonzero character vector and pairs them into two blocks. More explicitly,
encode the signs additively by

```text
q(a) = 0 if chi_Q(a)=+1, else 1,
f(a) = 0 if chi_F(a)=+1, else 1.
```

All elements of the exponent-one coset have one common value

```text
c := (q(h),f(h)) in F2^2 \ {(0,0)},
```

because multiplication by `G=ker(chi_Q) intersect ker(chi_F)` does not
change it. This `c` is new information and the verifier must emit it
result-neutrally when the coset exists. The exact invariant separating the
two resulting selector orbits is then:

```text
c              toggled character(s)   residual two-orbit invariant
(1,0)          chi_Q                  chi_F
(0,1)          chi_F                  chi_Q
(1,1)          chi_Q and chi_F        chi_Q chi_F
```

None of the three cases is expected here. Since every subgroup of `W` acts
freely on the `W`-torsor `Sel_class`, the only two non-STOP scientific
routes are:

```text
LINEAR-ONLY
  no exponent-one realization exists;
  Gamma_sl = G, |Gamma_sl| = 12;
  four free selector orbits of size 12 remain.

SEMILINEAR-DOUBLE
  an exponent-one realization exists;
  Gamma_sl = G disjoint-union hG, |Gamma_sl| = 24;
  two free selector orbits of size 24 remain.
```

In `SEMILINEAR-DOUBLE`, the computed nontrivial value
`c=(q(h),f(h))` and the corresponding residual two-orbit invariant are
mandatory transcript fields. No value or one of the three cases is expected
or embedded here.

The third route is

```text
STOP
```

for any source/hash mismatch, inexact or incomplete scan, failure of the
field, incidence, determinant, group, faithfulness, action, completeness,
or result-neutrality certificates, nondeterminism, nonzero exit, nonempty
stderr, or cross-architecture byte mismatch.

Because `|Gamma_sl| <= 24 < 48`, a one-orbit result is analytically
impossible in this lane. Neither live scientific route makes the selector
canonical.

`SEMILINEAR-DOUBLE` classifies a candidate enlarged equivalence only. It
does not retroactively replace the frozen `S_TM` gauge or the N2 result.
Adopting `Gamma_sl` as a normative gauge would require a separate owner and
Canon fold after the result.

## 9. Contract for the future exact scan

No scan is performed in this definition issue. A later result-neutral
verifier must implement all of the following as one complete exact
calculation.

### 9.1 Frozen reconstruction

From pinned public source bytes, independently reconstruct:

1. `K=Q(sqrt(5))` with exact normalized rational-pair arithmetic;
2. `tau`, `phi`, the six ordered vectors, and projective proportionality;
3. `sigma_line`, the oriented pairs `D_i,E_i`, and all 48 selectors;
4. the complete 48-element centralizer `W`, generated by all
   `(pi,delta) in S3 x F2^3`;
5. `chi_Q`, `chi_F`, their covariance, and the exact 12-element common
   kernel;
6. the old exponent-zero gauge, which must agree exactly with that common
   kernel and the public order-12 antecedent.

A mismatch is `STOP`, not a permission to alter an input.

The exponent-zero reconstruction is an inherited-support integrity check.
It is not a new scientific replay of issue #130 and must not invoke or
import the sealed `P-TM-SYM2-MEASURE-1` wrapper.

### 9.2 Complete incidence enumeration

For every

```text
e in {0,1},       p in W
```

solve over `K` the homogeneous incidence equations

```text
B tau^e(v_i) = lambda_i v_(p(i)),       i=1,...,6,
```

in the nine entries of `B` and six scalars `lambda_i`. These are all 96
exponent/permutation cases. No heuristic candidate generation may replace
the complete centralizer scan.

For each case the verifier must:

1. build the full exact coefficient matrix and compute deterministic RREF;
2. publish/check its rank or nullity certificate;
3. obtain a canonical exact basis of the solution space;
4. form the determinant polynomial of the matrix part on that solution
   space and accept the permutation exactly when this polynomial is not
   identically zero;
5. when accepted, choose a deterministic invertible witness and normalize
   it by dividing by the first nonzero matrix entry in the frozen flattening
   order;
6. verify all six vector equalities, nonzero determinant, nonzero
   `lambda_i`, induced permutation `p`, and commutation with `sigma_line`
   directly.

One complete deterministic way to witness a nonzero determinant polynomial
is to test the lexicographically ordered grid `{0,1,2,3}^d` for a
`d`-dimensional nullspace. The determinant has degree at most three in each
parameter, so a nonzero polynomial cannot vanish on that whole grid. If a
different exact method is frozen, its completeness proof must be included
before the formal pin.

The projective-frame uniqueness argument must be checked independently:
for fixed `(e,p)` there is at most one accepted projective realization.
The faithfulness lemma of section 7 must also be encoded as a theorem
certificate, not inferred from the observed scan output.

### 9.3 Group, completeness, and action certificates

The verifier must prove both directions:

- every accepted incidence witness is an element of
  `tilde_Gamma_sl`;
- every element of `tilde_Gamma_sl` induces one of the 48 scanned
  centralizer permutations and therefore appears in the accepted list.

It must then verify exact composition and inverses using the semilinear
formula, injectivity of `rho`, and the exponent-zero equality with `G`.
It must enumerate postcomposition on all 48 selectors, prove freeness,
compute the complete orbit partition, and verify the conditional
12/4-versus-24/2 theorem of section 8. When the exponent-one coset exists,
it must emit its common nonzero character `c` and verify the corresponding
residual two-orbit invariant from the three-case table.

### 9.4 Result neutrality and transcript

The immutable pin must not contain an expected value for any of:

```text
existence of the exponent-one coset;
accepted exponent-one permutation or matrix;
Gamma_sl order;
coset character;
residual two-orbit invariant;
semilinear orbit count, sizes, partition, representatives, or pairing case;
scientific route.
```

The verifier must be zero-argument, deterministic, exact, and silent on
stderr. Its transcript must separate structural `PASS` certificates from
the scientific route. Both `LINEAR-ONLY` and `SEMILINEAR-DOUBLE` are valid
exit-zero scientific results; `STOP` is not recoded as either.

The future pin must also contain exact support snapshots and SHA-256 hashes,
a preregistration freezing every route and threshold, and an independent
static checker that can reject an embedded expected result. That checker
must not itself solve or enumerate the exponent-one incidence systems.
The one zero-argument formal command must perform the evaluator and its
independent in-process certificate checks in a single execution; a second
evaluator invocation would violate the one-run budget.

## 10. Separate formal lock and execution order

After this definition is merged and publicly read back, formal work still
requires a new public issue that explicitly authorizes:

```text
branch: probe/P-TM-SYM2-SEMILINEAR-GAUGE-1
path:   probes/P-TM-SYM2-SEMILINEAR-GAUGE-1/
```

The immutable public pin must precede every formal evaluation and contain
the complete preregistration, accepted verifier, independent checker,
support snapshots, and hashes. The sole formal aarch64 execution may then
occur on JAS 2 or JAS 4. A clean GitHub Linux x86_64 replay must use the
identical pin and reproduce stdout byte for byte. No Studio execution is
part of this lane.

The old `P-TM-SYM2-MEASURE-1` run budget is sealed and is never reused.

## 11. Debt firewall

This definition and either future scientific route leave
`TM-SYM2-MEASURE [H]` unchanged. They do not:

- edit `canon/CANON.md`, the registry, frontier, status, dependencies, or
  gates;
- alter `W3`, `sigma_line`, the old selector class, or the old result;
- turn domain negation into gauge;
- enlarge gauge to the abstract wreath product;
- choose a character fiber, selector representative, sign branch, or
  minority-coordinate dictionary;
- adopt `Gamma_sl` as the frozen gauge without a later owner/Canon fold;
- claim that equal macro weights prove microscopic canonicality;
- open L5-to-L6 or establish physical measure.

`LINEAR-ONLY` would show that Galois conjugation adds no effective line
symmetry. `SEMILINEAR-DOUBLE` would show that it merges the four old fibers
in pairs. Neither can remove the final twofold-or-greater microscopic
ambiguity, so any later progress requires a genuinely new registered bridge
or theorem rather than an administrative fold.
