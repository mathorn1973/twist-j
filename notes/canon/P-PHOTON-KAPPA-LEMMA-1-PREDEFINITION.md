# P-PHOTON-KAPPA-LEMMA-1 predefinition ruling (NON-CANONICAL)

Status: `DRAFT / STOP-PREDEFINITION / ISSUE-RESERVED / NO-PROBE / NO-FORMAL-RUN`

Date: 2026-07-29

Public definition lock:
[issue #200](https://github.com/mathorn1973/twist-j/issues/200).

This note audits and freezes the decisions still required before the
`PHOTON-KAPPA-LEMMA` reconciliation child can become a formal probe. It is
not Canon, evidence, `PREREG.md`, a verifier, a formal run, a result, or a
status proposal. It changes no public claim and authorizes no execution.

## 1. Authority, collision, and routing pin

```text
Canon:                    Public Canon v26
state:                    ACTIVE
authority:                mathorn1973/twist-j main
tag:                      canon-v26
activation/tag target:    48213275d0ace92d8f034166179a9fee4d53d908
content commit:           138eec5b22a823469e1fa651505815a3d5b36761
Canon SHA-256:            3a62711e30b1f3e9c4ade71533354fdf669266f60f4a57ade84e31a8f2878cfd
Canon bytes:              141941
parent owner:             PHOTON-WINDOW-PROOF [O]
scheduler:                PHOTON_CONTINUUM / ROOT / READY / FORMAL
reconciliation child:     PHOTON-KAPPA-LEMMA [O]
reconciliation layer:     NOT_APPLICABLE
definition issue:         #200
definition branch:        notes/p-photon-kappa-lemma-1-predefinition
this file:                notes/canon/P-PHOTON-KAPPA-LEMMA-1-PREDEFINITION.md
reserved future probe:    P-PHOTON-KAPPA-LEMMA-1
reserved formal branch:   probe/P-PHOTON-KAPPA-LEMMA-1
reserved formal path:     probes/P-PHOTON-KAPPA-LEMMA-1/
formal pin/run/result:    ABSENT / NOT AUTHORIZED
```

`PHOTON-KAPPA-LEMMA` appears only in the non-normative reconciliation table
`notes/genesis/recon/FRONTIER_SPLITS.tsv`. It is not a Registry claim,
dependency, gate, or evidence item. Issue #200 is a collision lock, not
permission to create the reserved formal branch or path.

The sibling lock
`PHOTON-ROUGHENING-CERTIFICATE` in issue #201 is disjoint. Neither child can
close or redefine the other.

The reconciliation layer is literally `NOT_APPLICABLE`. This is valid for a
non-normative routing row and does not itself create an error or protocol
placement. Repository policy nevertheless requires a future formal
preregistration to freeze an action layer from L1 through L6. On the
support-chain surface selected below, the prospective probe is L4 only.
Any later use of a tick, stream, or measure quantity requires a separately
named cross-layer gate.

## 2. Exact inherited inventory and firewalls

| Source | Inherited exact content | What it does not supply |
| --- | --- | --- |
| `PHOTON-WINDOW-PROOF [O]` | asks for a universal bound `F_occ >= kappa L` with `2^(4 kappa) > 2401` | definitions of the generic worldline carrier, `L`, or `F_occ` |
| `MONOPOLE-FIFTHS [T]` | one 4D edge meets six faces; ternary face coefficients give mod-5-closed boundary values only in `{0,+5,-5}` | a generic filling space, existence theorem, or minimum |
| `MONOPOLE-COST [C]` | the unit-square charge-5 loop has a lower bound 17 and an explicit 21-face filling | an exact minimum, another loop, or an all-loop reduction |
| `KAPPA-BOUNDS [T]` | straight-run incidence, the `1 x K` ladder formula, and the greedy incidence identity | a universal coefficient or proof that the greedy bound clears the photon threshold |
| `KAPPA-SHAPES [C]` | nine edge-simple examples and their greedy lower-bound table, with minimum `31/8` | actual filling minima or any statement about arbitrary shapes |
| `DEF-ARCHITECTURE` | the declared architecture on which the photon dictionary is conditional | a derived continuum carrier or a worldline-class selection theorem |
| `FRONTIER_SPLITS.tsv` | non-normative reconciliation routing | evidence, status, definitions, or formal authorization |

The exact cubical conventions presently visible in
`reproduce/photon-electron/verify.py` are useful inherited syntax only:

```text
positive oriented edge:       e_mu(x)
positive oriented plaquette:  f_(mu,nu)(x), mu < nu

partial f_(mu,nu)(x)
  = e_mu(x) + e_nu(x+e_mu)
    - e_mu(x+e_nu) - e_nu(x).
```

The verifier constructs a traversal list in `loop_edges_of`, immediately
converts that list to a set in `greedy_lb`, and later uses
`L = len(steps)` for the nine examples. Those two lengths agree only because
the registered examples are edge-simple. The code therefore does not define
the generic denominator in the parent quantifier.

## 3. Carrier-coherence obstruction

At least three different exact objects are currently conflated:

```text
W        a closed nearest-neighbor walk;
j_W      the signed integral 1-chain induced by W;
E_W      supp(j_W), or alternatively the set of traversed unoriented edges.
```

They have different natural lengths:

```text
L_walk(W) = number of steps,
L_1(j)    = sum_e |j_e|,
L_supp(j) = |supp(j)|.
```

If `L=L_walk` while `F_occ` depends only on a reduced chain or edge support,
then inserting arbitrarily many immediate backtracks leaves `F_occ` fixed
and sends `F_occ/L` to zero. Repeating the same reduced loop gives the same
obstruction.

If multiplicity is instead retained in `j`, a repeated primitive charge
current `j=r j_0`, `r>=2`, is not fillable by the present ternary face
alphabet under `partial n=5j`: every edge boundary satisfies
`|partial n(e)|<=6`, whereas a charged repeated edge would require at least
10. Thus repetition is not harmless under that typing either.

Before any candidate coefficient or computation, a public
`KAPPA-CARRIER-COHERENCE` decision must freeze:

1. the map, if any, from walks to chains;
2. which multiplicities, backtracks, repetitions, components, crossings,
   and winding classes are admissible;
3. which one of the three lengths is the denominator;
4. whether the verifier must reject, preserve, or reduce each non-simple
   input; and
5. proof that the code numerator and denominator refer to the same frozen
   object.

Until then the current public wording is not an executable universal
statement. This is `STOP`, not yet a scientific negative closure.

## 4. Definition object that must be frozen

A valid definition package must publish one exact tuple

```text
S_kappa = (
    lattice, cells, orientations, partial,
    Worldline, worldline_equality, components,
    multiplicity, backtracks, repetitions, crossings, winding,
    walk_to_chain,
    L, L_domain,
    face_alphabet, Filling, charge_equation,
    filling_existence, empty_filling_rule,
    face_support, F, F_occ,
    kappa_domain, coefficient_normalization,
    universal_reduction, completeness_method,
    counterexample_family,
    deterministic_order,
    certificate_schema, certificate_checker
).
```

| Block | Required decision | Current ruling |
| --- | --- | --- |
| ambient complex | infinite finite-support `Z^4`, a finite box with named boundary conditions, a 4-torus, or another exact cubical complex | `UNRESOLVED` |
| orientation | complete edge, face, and boundary sign conventions and chain coefficient ring | `UNRESOLVED` |
| worldline | exact finite carrier and equality; one connected loop or a general conserved current | `UNRESOLVED` |
| topology | treatment of components, self-intersections, repeated vertices or edges, backtracks, and winding | `UNRESOLVED` |
| multiplicity | coefficient alphabet for `j` and relationship to a traversal | `UNRESOLVED` |
| length | total exact function `L` and proof that it matches the quantified carrier | `UNRESOLVED` |
| faces | coefficient alphabet and whether distinct translated/oriented faces are identified | `UNRESOLVED` |
| charge | exact equation, including the sign and whether it is equality over `Z` or only modulo 5 | `UNRESOLVED` |
| fillings | finite/infinite support, boundary conditions, admissibility, and existence domain | `UNRESOLVED` |
| occupancy | exact support convention and whether `F_occ` is an input filling count or a minimum over fillings | `UNRESOLVED` |
| empty minimum | exclusion, `+infinity`, or a separate unfillable outcome | `UNRESOLVED` |
| coefficient | exact domain and normalization of `kappa`; no fitted or floating threshold | `UNRESOLVED` |
| completeness | theorem-grade reduction or exhaustive bound covering every admitted worldline | `UNRESOLVED` |
| falsification | exact family predicate and checker distinguishing one failed coefficient from failure of every admissible coefficient | `UNRESOLVED` |

A natural possible surface, not authorized by v26, would use finite cubical
chains on `Z^4`,

```text
n_f in {0,+1,-1},
partial n = 5j,
j_e in {0,+1,-1},
partial j = 0,
L(j) = ||j||_1,
F(n) = |supp(n)|,
Phi(j) = min{F(n): partial n=5j}.
```

Even on this surface an owner must still choose between connected simple
degree-2 support and general conserved currents. Narrowing to simple loops is
not implied by Public Canon v26.

## 5. Exact candidate statement

The future coefficient must be exact. For coprime positive integers `a,b`,
put `kappa=a/b`. A positive closure has the integer form

```text
b F_occ(j) >= a L(j)             for every admitted j,       (K1)
2^(4a) > 2401^b.                                           (K2)
```

Here `2401=7^4`. No decimal approximation to `log_2(7)` is a threshold
certificate. The coefficient and the complete quantified carrier must be
frozen before a formal result is read.

The definition must also say whether `F_occ` means `F(n)` for every admitted
filling, the minimum `Phi(j)`, or another quantity. Those statements have
different logical strength.

## 6. What the inherited greedy bound actually proves

On a surface with edge-simple support `E=supp(j)`, define

```text
r_f = |partial f intersect E|,
P(E) = sum_f (r_f-1)_+,
LB(E) = 5|E| - P(E).
```

At every charged edge, `partial n=5j` and ternary face coefficients force
exactly five of its six incident faces to be occupied. Counting those
incidences and subtracting every possible cofacial reuse gives

```text
F(n) >= LB(E)
```

for every admitted ternary filling. This is the inherited incidence lemma.
It is a lower bound, not an exhibited filling and not the minimum `Phi(j)`.
The nine `KAPPA-SHAPES` values are values of `LB`, not certified values of
`Phi`.

## 7. Non-formal adversarial audit

The following exact checks expose required scope and proof decisions. They
are not a probe run, evidence, or a public status result.

### 7.1 A simple connected family defeats the greedy route

Let

```text
S_n = {0,1} x {0,...,n-1}^2,       n>=3,
M   = |S_n| = 2n^2,
A   = number of internal nearest-neighbor edges of S_n
    = 5n^2-4n.
```

Choose a row-serpentine Hamiltonian cycle on `S_n` and split its alternate
edges into perfect matchings `M_0,M_1`. In `Z x S_n`, take every
longitudinal edge of `K` parallel strands and close the two ends with
`M_0` and `M_1`. Alternating a matching edge and a strand follows the
Hamiltonian cycle, so the result is one connected degree-2 edge-simple
polygon.

Direct face counting gives

```text
L_(n,K)  = 2n^2(K+1),
P_(n,K)  = (K+1)(5n^2-4n)+1,
LB_(n,K) = (K+1)(5n^2+4n)-1,

LB_(n,K)/L_(n,K)
  = 5/2 + 2/n - 1/(2n^2(K+1)).
```

For `n=8`,

```text
L  = 128(K+1),
LB = 352(K+1)-1,
4 LB < 11 L,
2^11 = 2048 < 2401 = 7^4,
```

so `2^LB < 7^L` for every `K>=1`. Therefore the inherited greedy incidence
bound cannot by itself prove the required energy/entropy race, even on one
simple connected family. This does not upper-bound `Phi`; a stronger filling
lower bound could still succeed.

### 7.2 A torus filling is a scope-contingent negative control

On the indexed 4-torus

```text
Lambda_N = product_(mu=0)^3 Z/N_mu Z,
```

take `N_0>=3` and even `N_1,N_2,N_3>=4`, and define

```text
sigma(x)   = (-1)^(x_1+x_2+x_3),
n_01(x)    = sigma(x),
n_02(x)    = sigma(x),
n_03(x)    = (sigma(x)-1)/2,
n_(mu,nu)  = 0 otherwise.
```

All face coefficients are ternary. With the boundary convention in section
2,

```text
(partial n)_0(x)
  = sum_(r=1)^3 [n_(0r)(x)-n_(0r)(x-e_r)]
  = 2sigma(x)+2sigma(x)+sigma(x)
  = 5sigma(x),

(partial n)_r(x)
  = n_(0r)(x-e_0)-n_(0r)(x)
  = 0.
```

Thus `partial n=5j`, where `j_0(x)=sigma(x)`, all other components vanish,
and `partial j=0`. With `V=product_mu N_mu`,

```text
F(n) = V + V + V/2 = 5V/2,
L(j) = V.
```

This current is not a nonzero-homology obstruction. It is the signed sum of
`N_1 N_2 N_3` individually winding `x_0` loops, and

```text
[j] = (sum_(x_1,x_2,x_3) sigma(x)) [gamma_0] = 0
```

because every spatial period is even. The displayed equation
`partial n=5j` independently proves that the total signed current has an
admissible filling. The individual winding components do not bound, but their
homology classes cancel in the total current.

Hence `Phi(j)<=5V/2` if this carrier and minimum are adopted, while every
coefficient satisfying (K2) is strictly larger than `5/2` because
`2^10=1024<2401`. This family would exclude every admissible threshold
coefficient if toroidal carriers and disconnected winding currents were in
scope.

It is excluded by finite-support `Z^4`, and it is excluded by a
connected-simple requirement because it has `N_1N_2N_3` winding components.
Until the carrier choice is frozen, this is a `STOP` scope warning, not a
`BELOW-THRESHOLD` result.

## 8. Future outcomes

The formal lane must preserve exactly these issue-locked routes:

```text
KAPPA-PROVED
    One frozen exact coefficient a/b satisfies (K1) on the complete carrier
    and clears (K2), with a theorem-grade completeness certificate.

BELOW-THRESHOLD
    An exact complete result proves that the best available universal
    coefficient on the frozen carrier cannot clear (K2).

CANDIDATE-REFUTED
    An exact admitted worldline refutes one pinned coefficient. This does not
    exclude another above-threshold coefficient unless the certificate
    proves the required universal impossibility.

STOP
    A carrier, length, filling, minimum, coefficient, completeness proof,
    certificate, checker, layer disposition, or exact reproduction is
    missing or ambiguous.
```

The simple family in section 7.1 refutes only the sufficiency of the current
greedy proof route. The torus family in section 7.2 becomes a scientific
negative only if its carrier survives the prior scope freeze.

## 9. Owner disposition for the v27 queue

This non-canonical note records the owner-selected next route. It changes no
public parent scope or status:

```text
R0A  retain the inherited ternary face alphabet and exact charge equation
R1A  support/support on the candidate chain carrier
R2A  finite-support cubical chains on infinite Z^4
R3A  do not narrow the public parent; use connected edge-simple currents only
      as the first falsifier subclass
R5B  falsification before a universal construction
```

The exact candidate search surface is

```text
j in C_1^c(Z^4; {0,+1,-1}),
j != 0,
partial j = 0,

Fill(j) = {
    n in C_2^c(Z^4; {0,+1,-1}) : partial n = 5j
},

Fill(j) != empty,
L(j) = |supp(j)|,
F_occ(j) = min_{n in Fill(j)} |supp(n)|.
```

Chain equality is coefficientwise. Walk length, immediate backtracks,
repeated traversal, and coefficients outside `{0,+1,-1}` are not part of
this search carrier. The support and `l1` grades coincide on this ternary
surface. An unrestricted integer-face model is not an alternative reading of
the same registered rows: it would allow the unit square filling `5Q` on one
face and contradict `MONOPOLE-COST [C]`, `MONOPOLE-FIFTHS [T]`, and the
incidence argument. Likewise, for `j=k partial Q`, `k>=2`, a ternary filling
would require magnitude at least 10 on a charged edge while six incident
ternary faces give magnitude at most 6.

The first exact falsifier certificate is an explicit connected edge-simple
pair `(j,n)` on this surface satisfying

```text
partial n = 5j,
2^|supp(n)| <= 7^|supp(j)|.
```

It needs no minimum solver: `F_occ(j)<=|supp(n)|` already excludes every
universal `kappa` with `2^(4 kappa)>2401`. Failure to find such a pair in any
finite family or range proves nothing about the broad parent. The greedy
family in section 7.1 is therefore a refuted proof route, not a registered
public `[F]` row. The torus construction in section 7.2 is retained only as
an out-of-carrier regression control after R2A.

## 10. Future preregistration skeleton, still forbidden

Only after public review may a later immutable preregistration fill:

```text
EQUATION:    exact K1/K2 statement and all definitions it consumes
CODE:        accepted exact checker, if computation is used
CARRIER:     complete S_kappa carrier and equality
SYSTEMATICS: orientation, boundary, multiplicity, topology, reduction,
             completeness, and counterexample controls
THRESHOLD:   exact outcome predicates above, frozen before output
LAYER:       L4 support on the owner-selected candidate surface
```

The reconciliation table may continue to record `NOT_APPLICABLE`; it creates
no protocol placement. The future preregistration itself must freeze L4.
Any newly discovered inter-layer map or dependency requires separate
authorization and a named gate.

## 11. Pre-pin acceptance checklist

The formal branch and path remain forbidden until:

1. this definition note is reviewed, merged, and read back publicly;
2. every field of `S_kappa` is exact and no `UNRESOLVED` slot remains;
3. walk, chain, support, and length are coherent under repetitions and
   backtracks;
4. `F_occ`, filling existence, and the empty-minimum rule are total;
5. the coefficient domain and integer threshold are frozen;
6. the universal proof or counterexample method is complete for the whole
   carrier;
7. all four outcomes remain reachable and their falsifiers are exact;
8. the formal preregistration freezes L4 and names every required lift;
9. issue, branch, probe, path, and short-ID collisions are rechecked;
10. an accepted verifier, if any, is committed and pushed with `PREREG.md`
    before the first formal gate execution; and
11. remote hashes, byte counts, and LF-normalized readback are confirmed
    before any run.

## 12. Debt firewall

This note selects a non-canonical candidate search surface but does not change
the public parent carrier or status, prove a universal kappa, claim that the
torus family belongs to the parent scope, equate `LB` with `F_occ`, strengthen
`KAPPA-SHAPES`, infer a massless photon or Coulomb phase, change
`CENTER-SPLIT-SELECTION`, edit the Canon, or authorize a probe. It records why
the current inherited evidence is insufficient and makes the next definition
decision falsifiable.
