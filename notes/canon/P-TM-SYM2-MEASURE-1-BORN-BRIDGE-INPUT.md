# P-TM-SYM2-MEASURE-1 Born bridge and layer input (NON-CANONICAL)

```text
C-TM-BORN-BRIDGE-1
NON-CANONICAL / PARTIAL DEFINITION INPUT
STOP-PREDEFINITION / NO-PROBE / NO PUBLIC STATUS
```

This note is a result-neutral definition input for `TM-SYM2-MEASURE [H]`
and issue #119. It consumes the selector-class input
`P-TM-SYM2-MEASURE-1-SELECTOR-CLASS-INPUT.md` but does not adopt that
input, amend the Canon, register a gate or dependency, authorize a probe,
or assert an evaluation result. It proposes one exact coefficient-side
Born bridge and names the layer records that a later owner definition would
have to adopt. The lane remains `STOP`.

## Authority pin

```text
Canon:                 Public Canon v15
state:                 ACTIVE
tag:                   canon-v15
activation commit:     8f4e176c5d76f519d3493e56e438aba7856e1f01
content commit:        a850753348583e611bf7ccd5aa074030dc7e12f5
Canon SHA-256:         53237ec25b3782e833367c998c049d19459189a21c2a36638dd9e1600335976b
Canon bytes:           89288
public-main readback:  434e02a01903ef7a237053eac1231dbe7496bbf5
owner row:             TM-SYM2-MEASURE [H]
scheduler:             MEASURE / ROOT / STOP / FORMAL
public lock:           issue #119
```

## 1. Ruling on the factor slots offered by the selector input

Section 8 of the selector input offered a leading-pair density as `third`
and a continuation weight as `half`. That pair is not adopted as the
universal factorization. For the extreme leading pairs `00` and `11`,
cube-freeness leaves one continuation, so the continuation weight is `1`,
not a universal two-branch factor.

This note instead proposes the factorization already exposed by the two
fixed-point-free involutions in the candidate:

```text
window involution:  N(w) = wbar on W3,
line involution:    sigma_line on Lines,
quotient carrier:   Q := W3 / <N>,
sheet carrier:      B_2 := {0,1}.
```

The name `sigma_line` is used here to avoid collision with the registered
generator selector `sigma(omega)` of `DEF-SELECTOR`; when qualification is
needed below, that registered selector is called `sigma_index`. The proposed
line involution neither replaces nor strengthens the registered selector.

The intended meanings are:

```text
third  = the stationary weight of an N-orbit in Q,
half   = the coefficient-side Born weight of one sheet of the proposed
         coefficient representative of the registered spectral verb,
```

not two scalars inserted because their product is wanted.

## 2. Exact three-by-two carrier

For the registered Thue-Morse cut, every block of three consecutive bits
contains a pair `(theta_(2m), theta_(2m+1))` of complementary bits. Hence
neither `000` nor `111` occurs. The six other words occur already in

```text
(q(1),q(2),q(3),q(4),q(5),q(6))
  = (011,110,101,010,100,001).
```

Thus the candidate language is

```text
W3 = {001, 010, 011, 100, 101, 110}.
```

Negation is free and gives exactly three orbits:

```text
O_A = {001,110},
O_B = {010,101},
O_C = {011,100},
Q = {O_A,O_B,O_C}.
```

Let `bit(w)` be the middle bit of `w`. Every N-orbit contains exactly one
word with `bit=0` and one with `bit=1`, so

```text
W3 -> Q x B_2,     w |-> ([w], bit(w))
```

is a canonical bijection relative to the declared middle-bit convention.
No representative of an N-orbit is selected.

Every `s` in the proposed `Sel_class` is a surjection between two
six-element sets, hence a bijection. Its equivariance

```text
s(N(w)) = sigma_line(s(w))
```

therefore induces a bijection

```text
s_bar : Q -> Lines / <sigma_line>.
```

This is a typed quotient statement. It does not establish that the W3
carrier or `sigma_line` is forced by the public architecture.

## 3. The quotient law and the proposed meaning of `third`

Let `varpi : W3 -> Q` be the orbit map. The exact left and right child
maps `L,R : W3 -> W3` of the selector input obey

```text
L(N(w)) = N(L(w)),       R(N(w)) = N(R(w)).
```

They therefore descend to `Q`. Direct substitution gives

```text
O_A -> O_B + O_C,
O_B -> O_A + O_C,
O_C -> O_A + O_B.
```

Let `T` be the six-window column transfer of the selector input and
`T_Q` this quotient column transfer. The exact descent identity is

```text
QUOTIENT-DESCENT:       varpi_* T = T_Q varpi_*.
```

A normalized stationary law `pi_Q` satisfies `T_Q pi_Q = 2 pi_Q`.
Subtracting any two of its three equations forces the corresponding
coordinates to be equal, and normalization gives the unique law. Define

```text
third_Q(O) := pi_Q(O),                         O in Q,
third_f(O) := sum_(w in O) f_w,                O in Q,
```

where `f` is the unique normalized stationary window law certified by the
selector input. The values are derived from the transfers, not supplied as
targets.

The descent identity makes `varpi_* f` a normalized stationary law of
`T_Q`; uniqueness therefore proves

```text
QUOTIENT-STREAM-COMPATIBILITY:
third_f(O) = third_Q(O) for every O in Q.
```

Likewise the two child identities make `N_* f` a normalized stationary
law of `T`. Uniqueness proves

```text
COMPLEMENT-BALANCE:     N_* f = f,
                        f_w = f_(N(w)) = third_f([w]) / 2.
```

These are conditional exact consequences of the frozen transfer and
stationarity premises. A future checker must certify the implications;
missing, inexact, or unsound proofs route `STOP`. They are not independent
science predicates and may not be used to change `W3`, `sigma_line`, or
`Sel_class` after an evaluation.

## 4. Coefficient-side Born carrier

Let

```text
Rat      := the rational field,
K_B      := Rat(zeta_5),
K_B^re   := {x in K_B : star(x) = x} = Rat(zeta_5 + zeta_5^(-1)),
I_5      := Z/5Z,
C_pos    := Rat^(I_5) \ {0},
star(zeta_5) := zeta_5^(-1).
```

The order `<=_pr` on `K_B^re` is the order in its principal real
embedding, fixed by

```text
zeta_5 + zeta_5^(-1) |-> (sqrt(5) - 1) / 2.
```

No total-positivity claim is made. For a finite set `S`, define

```text
Delta_Rat(S) := {p in Rat^S : p_x >= 0 for all x, sum_x p_x = 1},

Delta_(K_B^re,pr)(S)
  := {p in (K_B^re)^S : 0 <=_pr p_x for all x, sum_x p_x = 1},

Eq_Born,S(p,p')  iff  p_x = p'_x coordinatewise for every x in S.
```

For `a = (a_r)_(r in I_5)` in `C_pos`, define the exact coefficient
norm, Fourier map, and normalized quadratic readings

```text
Z_pos(a)       := sum_r a_r^2,
F(a)_k         := sum_r a_r zeta_5^(r k),

Born_pos  : C_pos -> Delta_Rat(I_5),
Born_pos(a)_r  := a_r^2 / Z_pos(a),

Born_spec : C_pos -> Delta_(K_B^re,pr)(I_5),
Born_spec(a)_k := star(F(a)_k) F(a)_k / (5 Z_pos(a)).
```

The principal-order nonnegativity is part of the exact type certificate.
The denominator in `Born_spec` is fixed by exact Plancherel:

```text
sum_k star(F(a)_k) F(a)_k = 5 Z_pos(a).
```

Take the proposed coefficient representative of the registered spectral
verb,

```text
v := delta_0 + delta_1,          Supp(v) := {0,1}.
```

Then

```text
F(v)_k = 1 + zeta_5^k,
```

so the spectral reading of `v` is exactly the five-slot registered verb of
`MEASURE-BORN-VERB`, with the exact weights of `BORN-FACE-WEIGHTS` and
the Plancherel statement of `SUBSTRATE-KNIT`. The coefficient reading is a
new candidate read basis. It is not silently supplied by any of those rows.

Because `Born_pos(v)` vanishes off `Supp(v)`, its restriction is already
normalized. Define

```text
Born_supp(v) := Born_pos(v)|_(Supp(v)) in Delta_Rat(Supp(v)).
```

For each two-element orbit `O` in `Q`, let
`tau_O : Supp(v) -> O` be either bijection and set

```text
half_O := (tau_O)_* Born_supp(v) in Delta_Rat(O).
```

Both support coefficients are equal. Hence the two possible bijections give
the same distribution under `Eq_Born,O`; `half_O` is independent of the
support orientation. The value is derived by the quadratic coefficient
reading, not inserted into the selector class or read back from a line
frequency.

The new and still unadopted dictionary choice is exactly this one:

```text
the free N-sheet of the TM window carrier is read in the coefficient
support basis of the proposed coefficient representative of the registered
spectral verb.
```

Public Canon v15 does not choose this basis bridge. Until an owner ruling
adopts it, this section is a candidate definition and the lane remains
`STOP`.

## 5. Candidate Born measure and structural compatibility

For the exact stationary window law `f`, define a candidate Born measure
on `W3` and its line pushforward by

```text
mu_B^f(w) := third_f([w]) half_[w](w),
mu_B,s    := s_* mu_B^f.
```

This is normalized because the N-orbits partition `W3` and each
`half_O` is normalized on `O`. Its definition contains no target line,
target weight, selector-class count, moment coefficient, or GYRON value.
It is a classical-base times conditional-Born composition:
`third_f` is the L5 quotient law and `half_O` is the coefficient-side
quadratic kernel. The generic public Born dictionary does not by itself
authorize this composition; that authorization is part of the lane-specific
gate proposal below.

The stream-side law and the Born-side law remain differently typed.
Nevertheless, `COMPLEMENT-BALANCE` and the exact two-slot reading imply,
rather than empirically test,

```text
BORN-STREAM-COMPATIBILITY:
Eq_Born,W3(mu_B^f, f).
```

Indeed each side assigns `third_f(O)/2` to each member of `O`. A missing,
inexact, or unsound implication proof routes `STOP`; there is no second
scientific branch in which the same green premises yield a false equality.

For a representative `s`, the stream-side line moment operator is

```text
M_s(A) := sum_w f_w Tr(P_(s(w)) A) P_(s(w)).
```

The selector input's original N3 decision is evaluated before any scalar
coefficient is read. Only on its exact commutant branch define
`scalar_coeff(M_s)` as the unique `alpha` in

```text
M_s = alpha P1 + beta P5.
```

On that branch, `M_s(I_3) = alpha I_3`; normalization and the rank-one
projectors give

```text
3 alpha = sum_w f_w Tr(P_(s(w))) = 1.
```

The quotient law independently gives `third_f(O)=1/3` for every `O`.
Consequently

```text
SCALAR-LINK:
third_f(O) = scalar_coeff(M_s) for every O in Q
```

is a structural implication after N3 passes, not an unguarded predicate.
Outside the commutant branch, N3 has already routed `NEGATIVE`.

## 6. Event-level GYRON bridge

Freeze both census conventions. For `N >= 1` and `M >= 2`, let

```text
c_w(N)        := #{n in [1,N] : q(n) = w},
c_pair,ab(M)  := #{j in [0,M-2] : (theta_j,theta_(j+1)) = ab}.
```

Since `pi_12(q(n)) = (theta_(n-1),theta_n)`, the exact finite identity is

```text
sum_(w : pi_12(w)=ab) c_w(N) = c_pair,ab(N+1)
for every ab in {00,01,10,11} and every N >= 1.
```

Thus, with the selector law
`f_w = lim_(N->infinity) c_w(N)/N` and the public pair-law convention

```text
rho_ab := lim_(N->infinity) c_pair,ab(N+1)/N,
```

one obtains the typed pushforward identity
`(pi_12)_* f(ab)=rho_ab`. Define

```text
pi_12 : W3 -> {00,01,10,11},
pi_12(w_1,w_2,w_3) := (w_1,w_2),
E_00 := pi_12^(-1)({00}) = {001}.
```

For each representative `s`, its bijectivity gives

```text
p_s : Lines -> {00,01,10,11},     p_s := pi_12 o s^(-1).
```

The bridge is the commuting square

```text
W3  --s-->  Lines
 |           |
pi_12        p_s
 |           |
Pairs --id-> Pairs,
```

and the selected-line event is
`s(E_00)=p_s^(-1)({00})`. Combining the finite census identity, its limit,
and `BORN-STREAM-COMPATIBILITY` proves

```text
GYRON-PUSHFORWARD:
mu_B,s(s(E_00)) = mu_B^f(E_00) = f(E_00) = rho_00.
```

This is a map-and-event bridge to `GYRON-DENSITY`, not a rule equating two
rational numbers because they happen to match. The public density is not
used to choose `s`, `f`, `third`, or `half`. The finite identity and
limit passage are structural certificate obligations; a missing, inexact,
or unsound proof routes `STOP`.

## 7. Exact layer endpoints and gauge-correct output

Let `U` be the registered autonomous update and freeze the shifted source
slice

```text
Omega_1 := {(1,psi) : psi in F_5^6}.
```

For `omega_1 in Omega_1` and `k >= 0`, the counter of
`U^k(omega_1)` is `k+1`, so all windows and selections below lie in
`Dom(Sel)`. For a representative `s`, define

```text
ell_s(k;omega_1)
  := s(q(counter(U^k(omega_1)))),

lambda_v^s(k;omega_1)
  := [ell_s(k;omega_1) = v],                    v in Lines,

xi_O(k;omega_1)
  := [q(counter(U^k(omega_1))) in O],           O in Q.
```

The `lambda` and `xi` objects are shifted/restricted binary orbit records.
They are not the registered total `DEF-LOG-STREAM` Logs, and this note does
not claim that the generic log-projection gate covers them.

The candidate layer records are

```text
L1 source
  Omega_1, Dom(Sel), q, W3, N, Sel_class, G, sigma_line.

L5 representative record
  R_s^5 := (ell_s, (lambda_v^s)_v, (xi_O)_O, f, s_*f, M_s, p_s).

L5 gate output after a CANONICAL selector classification
  R_[s]^5 := {R_(g o s)^5 : g in G}; an orbit record, never a chosen
             representative.

Candidate L6 evaluation orbit, defined only after GAUGE-COHERENCE and N3 pass
  E_s^6 := (R_s^5, mu_B,s, BORN-STREAM-COMPATIBILITY, SCALAR-LINK,
            GYRON-PUSHFORWARD),
  E_[s]^6 := {E_(g o s)^6 : g in G}.

L6 measure endpoint
  [mu_B,s]_G := {mu_B,(g o s) : g in G}, after the structural Born and
  GYRON implications are certified, GAUGE-COHERENCE and N3 pass, and the
  lane-specific gate is adopted.
```

The representative formulas obey the exact relabellings

```text
ell_(g o s) = g o ell_s,
lambda_v^(g o s) = lambda_(g^(-1)v)^s,
(g o s)_*f = g_*(s_*f),
mu_B,(g o s) = g_*mu_B,s,
p_(g o s) = p_s o g^(-1).
```

No result-dependent section of the selector orbit is allowed. The checker
must evaluate the complete original N3 record for every representative.
Name the exact scientific descent condition

```text
GAUGE-COHERENCE:
the N3 truth value, and on its passing branch the registered commutant
coefficients, agree for every R_(g o s)^5 in R_[s]^5.
```

A complete exact disagreement is a scientific `NEGATIVE`: the proposed
physical reading does not descend through its own declared gauge. A missing,
inexact, or incomplete all-representative decision record is `STOP`.

All L5 objects are read-only derived records and have no physical measure
status before the L5-to-L6 gate. Calling a finite normalized vector a
probability vector does not itself perform that gate.

## 8. Candidate gate records

The generic `GATE-L1-L5-LOG-PROJECTION` covers the registered total binary
Log. It does not register this candidate's shifted six-valued selector
stream, selector-orbit output, canonicality class, or quotient records. The
generic `GATE-L5-L6-BORN-READING` states the public Born dictionary, but
does not supply this candidate's coefficient bridge or authorize its
classical-base times conditional-Born composition.

The smallest lane-specific gate proposals are:

```text
gate_id:             GATE-L1-L5-TM-SYM2-SELECTOR-STREAM
owner_item_id:       TM-SYM2-MEASURE
from_layer:          L1
to_layer:            L5
gate_kind:           OPEN_LIFT
decision_condition:  emits the exact typed gauge-orbit record R_[s]^5, never
                     a representative, only when the frozen carrier/class
                     audit and canonicality classification are complete;
                     EMPTY or NONCANONICAL routes scientific NEGATIVE,
                     incompleteness or inexactness routes STOP

gate_id:             GATE-L5-L6-TM-SYM2-BORN-MEASURE
owner_item_id:       TM-SYM2-MEASURE
from_layer:          L5
to_layer:            L6
gate_kind:           OPEN_LIFT
decision_condition:  closes this candidate block only when the Born
                     carrier, coefficient and spectral readings, support
                     pushforwards, structural compatibility implications,
                     gauge-coherence record, original N3 record, GYRON
                     bridge, normalization, and exact checker are complete;
                     an exact scientific N3 or gauge disagreement routes
                     NEGATIVE, while missing, incomplete, or inexact
                     typing or proof routes STOP
```

These identifiers and rows are proposal-local. This note does not edit
`canon/GATES.tsv`. The second proposal depends on the registered generic
Born reading; it does not replace or strengthen it.

## 9. Candidate dependency delta

The existing direct parent edges remain unchanged. A later owner fold that
adopts this candidate would have to review at least these additional direct
edges:

```text
TM-SYM2-MEASURE -> DEF-ACTION-LAYERS
TM-SYM2-MEASURE -> RAMIFIED-TM-LIFT
TM-SYM2-MEASURE -> SUBSTRATE-KNIT
```

No direct edge to `DEF-LOG-STREAM` is proposed: section 7 deliberately
defines shifted/restricted orbit records, not the registered total Log.
The existing edge through `MEASURE-BORN-VERB` already reaches
`BORN-FACE-WEIGHTS`. The short W3 language proof in section 2 avoids
importing `TIME-CUT-READING` and its unrelated spatial dependency tree.
No dependency is registered by this note.

## 10. Certificate and deterministic routing extension

A future checker must extend the selector certificates without embedding an
expected selector-orbit count or stream-weight vector. At minimum it must
certify:

```text
B1  the six-word language, free N action, three exact quotient orbits, and
    the conditional theorem that every s in Sel_class induces
    s_bar : Q -> Lines/<sigma_line>; B1 requires no concrete s or s_bar;

B2  both complement/child identities, the quotient transfer, exact descent,
    unique stationary-law proof, QUOTIENT-STREAM-COMPATIBILITY, and
    COMPLEMENT-BALANCE as derived implications;

B3  C_pos, both distribution codomains and Eq_Born, principal-order
    positivity, coefficient norm, Fourier map, star, Plancherel identity,
    the proposed coefficient representative, and exact agreement of its
    spectral reading with the registered five face weights;

B4  the support restriction and every support pushforward, orientation
    independence, normalization of mu_B^f, BORN-STREAM-COMPATIBILITY, and
    the guarded SCALAR-LINK implication after an N3 commutant pass;

B5  one exact tagged branch record:
    EMPTY_NOT_APPLICABLE(classification_certificate),
    NONCANONICAL_NOT_APPLICABLE(classification_certificate), or
    CANONICAL(R_[s]^5, all-representative GAUGE-COHERENCE and N3
    decision records, including exact witnesses for every false scientific
    payload);

B6  the finite all-N census-index identity, limit pushforward, event square,
    and GYRON-PUSHFORWARD as structural implications;

B7  both proposal-local gate records and the complete acyclic dependency
    graph, including the explicit absence of a DEF-LOG-STREAM edge.
```

For B5, integrity requires the tag to agree with the exact selector
classification. Orbit and all-representative payloads are required only on
the `CANONICAL` branch; the other two tags make those payloads explicitly
not applicable. A canonical decision record must be exact, complete, and
witness-backed, but its scientific Boolean payload need not be true.
Structural implication certificates B1-B4 and B6-B7, by contrast, must be
sound; a failed implication is an invalid evaluation, not a second
scientific answer.

The evaluation order is fixed:

```text
1  any missing, inexact, unsound, or incomplete selector/B1-B7
   certificate or structural implication                         -> STOP;
2  Sel_class is EMPTY                                             -> NEGATIVE;
3  selector classification is NONCANONICAL                       -> NEGATIVE;
4  a valid exact GAUGE-COHERENCE record reports disagreement      -> NEGATIVE;
5  a valid exact N3 record exhibits unequal line weights,
   noncommutant M_s, or a changed 5:2 coefficient ratio           -> NEGATIVE;
6  otherwise this candidate satisfies the Born/layer block.
```

Step 6 is not by itself an overall `POSITIVE`: parent closure still
requires owner adoption of the W3 carrier, `sigma_line`, the
coefficient-support bridge, both gate records, the full checker, and every
remaining field of the predefinition tuple.

## 11. Residual definition debt and firewall

This input makes the meanings of one candidate `third`, `half`, Born
carrier, density bridge, and layer endpoints exact. It does not establish:

```text
carrier priorness       that radius-1 W3 is the architecture's complete or
                        uniquely admissible selector quotient;
line-pair priorness     that sigma_line is forced by the registered frame;
basis priorness         that the N-sheet must be read in the coefficient
                        support basis of the registered verb;
gate authority          adoption of either proposal-local gate;
checker completeness    a pinned checker or proof that B1-B7 plus the
                        selector certificates are complete;
owner adoption          a complete S_TM with no unresolved field.
```

No Canon, registry, frontier, gate, dependency, evidence, probe, verifier,
run record, or public status changes. No value computed in an incubation
lane is imported. `TM-SYM2-MEASURE [H]` remains `MEASURE / ROOT / STOP /
FORMAL`, and issue #119 remains open.
