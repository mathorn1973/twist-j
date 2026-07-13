# P-CURVATURE-TRACE-VALUE-1: Owner Ruling (NON-CANONICAL)

```text
Program:          CURVATURE-TRACE-VALUE
Probe:            P-CURVATURE-TRACE-VALUE-1
Track:            C
Owner:            master C, public lock issue 17
Date:             2026-07-13
Basis:            Public Canon 1, tag canon-v1, activation commit
                  f4fb064c2a08cd21b9a2bc2bcfd4daf46da47bcb
Public base:      36670179c76e9ad13babad0adca40f952079ea8f
Content commit:   39065e0315cfd260f47c9f179bba21d7c471f70c
Canon SHA-256:    e75eae45be3a5433980272a670d3a3cd140c40f39d9bbaed5c5ee56a6b9a7f2c
Canon bytes:      53118
Source workpack:  919bd69a3f87aeb4f278605b77b9063036f992e9be52a50b0eeb000b819be9fe
Status:           RULING CANDIDATE BEFORE MERGE; PINNED NON-CANONICAL
                  OWNER RULING AFTER REVIEWED MERGE AND PUBLIC BYTE READBACK
Scientific claim: remains O
Action layer:     L2
Public record:    mathorn1973/twist-j issue 17
Computation:      NOT AUTHORIZED
Result:           NONE
Supersedes:       ruling draft SHA-256
                  2e6b8fbf181c04c6aeaaa5ef54404f65e1ac8b11de095669cb1f755acc6a2168
                  (6376 bytes, 259 lines)
Incorporates:     pre-analysis SHA-256
                  fd6667856e8d11ebecaa4fa8bc2f491e7d60ae1782cb753dbf83483392d0cade
                  and disclosed exploratory audit SHA-256
                  d210038e514f930a33916465dd1b4171fccded6dd188b3b7d230543d5873acae
```

## 0. Owner decision and base reconciliation

The public obligation combines two questions that must not be answered by
one target-driven computation:

1. whether the inherited proposed trace `-21/8` survives a faithful,
   explicitly typed reconstruction of the historical operator; and
2. which curvature operator, if any, is forced by Public Canon 1.

This ruling accepts route 1 for `P-CURVATURE-TRACE-VALUE-1`. Selection of a
new canonical curvature operator is deferred to a separately named
obligation. The future probe must not search projectors, representations,
normalizations, or quotients for one that returns a desired scalar or golden
spectrum.

D1 through D8 are an owner-selected, pre-output repair of the inherited
wording. This ruling does not assert that `K` is uniquely forced by Public
Canon 1 or that it reconstructs every private legacy convention. It decides
only the exact public operator frozen below. Canonical operator selection
remains the separately named deferred task.

The off-repository workpack was prepared at public `main` commit
`5d20a194201bec46b0a6d11c028a02f3fa5cf447`. Before this ruling candidate,
public `main` advanced to `36670179c76e9ad13babad0adca40f952079ea8f` by
adding exactly the five files of `P-SPIN-LIFT-FORCED-1`. The five normative
Canon files, `STATUS.md`, the registered `CURVATURE-TRACE-VALUE` row, the
checkpoint generators, and the `canon-v1` tag did not change. The curvature
surface below is therefore carried forward on the true current base without
reinterpretation.

No computation is authorized by this ruling candidate. The formal verifier
may be executed only after this ruling is merged and pinned, `PREREG.md` and
the accepted exact `verify.py` pass reciprocal byte review, and both are
committed and pushed as an immutable preregistration pin.

## 1. Falsifier and routing first

Let `kappa` be the observable frozen in D7. The integrity tally is evaluated
before any scientific decision is printed.

```text
DECISION NEGATIVE
  every integrity gate passes and kappa != -21/8.
  CURVATURE-TRACE-VALUE closes negatively at the frozen historical operator.

DECISION TRACE-SURVIVES
  every integrity gate passes and kappa = -21/8.
  The trace branch survives, but positive closure is not earned because the
  registry also requires a proved spectrum. A separately named
  P-CURVATURE-SPECTRUM-1 gate is then required.

DECISION STOP
  any integrity, typing, exactness, determinism, stderr, or execution gate
  fails, or the public witness W is not reproduced exactly.
```

`STOP` is an invalid execution, not a scientific result. A valid `NEGATIVE`
or `TRACE-SURVIVES` exits zero. `STOP` exits nonzero. The verifier must never
print a scientific decision on a failing audit path.

## 2. Prior exploratory knowledge disclosure

Before any public ruling or preregistration pin, a NON-CANONICAL exact audit
reported:

```text
historical printed-spectrum checksum     -22
raw full-space commutator trace           -31250
<b,d> Reynolds compression                -881/8
<b,d,e> Reynolds compression              -181/8
```

These values are disclosed prior knowledge, not formal evidence and not
integrity thresholds. In particular, the future verifier must not hard-code
`-881/8` or any other exploratory value as a required pass condition. It must
compute `kappa` independently by both frozen routes, require only their exact
agreement and the structural gates, and then apply the registered comparison
with `-21/8`.

The printed-spectrum checksum is a static audit of one historical formula.
It is not asserted as the spectrum of the operator below and does not replace
a spectrum computation.

## 3. Frozen historical reconstruction

### D1. State carrier and public generators

```text
X = F_5^6
x = (p1, p4, p1p, p4p, q, r)
|X| = 5^6 = 15625
```

All arithmetic is modulo 5. Use the Public Canon 1 checkpoint generators
exactly:

```text
a(p1,p4,p1p,p4p,q,r) = (p4,p1,p4p,p1p,q,r)

b(p1,p4,p1p,p4p,q,r) = (-p1p,-p4p,-p1,-p4,-q,-r)

c: piston -> b4(piston) + (2,1,2,1) + r(0,1,0,-1)
   q       -> 1-q
   r       -> -r

d(x) = (2,1,3,4,1,1) - x
e(x) = (2,1,3,4,2,1) - x
```

Here `b4` is the piston part of `b`. All five maps must be reconstructed as
total affine maps and checked as involutions on the full carrier. Only
`a,b,c,d` enter the frozen operator. The map `e` does not enter `kappa` or the
scientific comparison; failure of its public-generator integrity check is
`STOP`.

### D2. Composition and Koopman convention

Affine-map composition is

```text
(g o h)(x) = g(h(x)).
```

Let

```text
F = Q^X,
(T_g f)(x) = f(g^-1 x),
<f,h> = sum_{x in X} f(x) h(x).
```

With this convention,

```text
T_g T_h = T_(g o h).
```

The formal output and unit gates must state and verify this convention. No
opposite word convention may be substituted after the pin.

### D3. Raw commutator

```text
C0 = T_a T_c - T_c T_a
   = T_(a o c) - T_(c o a).
```

Since `a` and `c` are involutions, their permutation operators are
self-adjoint and `C0* = -C0`.

### D4. Historical symmetry group

```text
H = <b,d>
```

The verifier derives rather than assumes:

```text
|H| = 20
H-orbit census on X = 1 orbit of size 5
                      74 orbits of size 10
                      744 orbits of size 20
dim F^H = 819.
```

The ruling does not rely on the ambiguous label `D10`; the affine group
generated by the exact public maps `b` and `d` is the object. No Klein-four
wording is admissible on the full checkpoint carrier.

Define

```text
x ~_H y  iff  y = h(x) for some h in H.
```

Then `F^H` is exactly the rational-valued function space on the finite orbit
set `X/H`. Orbits and their representatives are ordered lexicographically by
their least state.

### D5. Orthogonal projectors

Let `1_X` be the constant-one function and define

```text
Pi_1(f) = (1/|X|) (sum_{x in X} f(x)) 1_X,
P0      = I - Pi_1,
R_H     = (1/20) sum_{h in H} T_h,
P       = P0 R_H = R_H P0.
```

`R_H` is the counting-metric orthogonal projector onto `F^H`; `P0` is the
orthogonal projector off constants. Their commutation and the identities

```text
P^2 = P,
P* = P,
rank(P) = 818
```

are integrity gates, not assumptions.

The frozen curvature carrier is

```text
V = im(P) = F^H intersect 1_X^perp,
dim(V) = 818.
```

### D6. Curvature operator and compression identity

The historical wording as a restriction is not well typed because `C0` does
not preserve `F^H`. Freeze the orthogonal compression

```text
K = (P C0 P)|_V : V -> V.
```

Because `C0 1_X = 0` and `C0* = -C0`,

```text
P0 C0 = C0 P0 = C0,
K = R_H C0 R_H.
```

The verifier proves these identities. They justify both the orbit formula
and the Reynolds group-word formula; they are not post-result simplifications.

### D7. Observable

```text
kappa = Tr_V(K^2) = Tr_F((P C0 P)^2).
```

This is the ordinary operator trace induced by the counting inner product.
There is no division by dimension, rescaling, metric weight, fitted scalar,
or other normalization.

Because `C0 1_X = 0`, `C0` is skew-adjoint, and `P0` commutes with `R_H`,

```text
Tr_V(K^2) = Tr_F((P C0 P)^2) = Tr_F(R_H C0 R_H C0).
```

Route A may therefore work in the normalized orbit-indicator basis of
`F^H`. That basis contains the one-dimensional constant direction, but `K`
annihilates it, so its presence does not change the trace on `V`.

### D8. Spectrum boundary and deferred selection

This first probe is trace-only. It may print the exact checksum implied by
the historically stated ten nonzero modes

```text
{+/- i phi^n : n = -2,-1,0,1,2},
```

but it does not assert that multiset for `K` and does not compute the
characteristic polynomial of `K`.

If the trace survives, `P-CURVATURE-SPECTRUM-1` must freeze the exact proposed
spectrum as a complete multiset with every multiplicity and denominator.
Selection of a new canonical curvature operator, a boundary block, a
representation block, or a 37-dimensional golden block is outside this
ruling and requires its own gate.

## W. Pinned restriction-failure witness

The future verifier reconstructs `H` from D4 and the orbit

```text
O0 = H . (0,0,0,0,0,0).
```

It then uses the exact states

```text
x = (0,0,1,3,0,1),
y = (2,1,2,1,1,0).
```

The required witness facts are

```text
x and y lie in the same H-orbit,
C0 1_O0(x) = 0,
C0 1_O0(y) = -1.
```

Thus `C0 1_O0` is not `H`-invariant and raw `C0` is not an endomorphism of
`F^H`. Failure to reconstruct this witness exactly is `STOP`. The witness
justifies compression rather than restriction; it does not determine
`kappa`.

## 4. Integrity gates

```text
I1   X has 15625 states; a,b,c,d,e are the exact public total affine
     involutions on all states.
I2   affine composition and the Koopman product law of D2 hold exactly.
I3   H=<b,d> has order 20 and the D4 orbit census is exact.
I4   R_H and P0 are commuting orthogonal projectors; P has rank 818.
I5   witness W proves that raw C0 does not preserve F^H.
I6   C0 is skew-adjoint, kills constants on both sides, and the D6
     compression identities hold.
I7   K is a total endomorphism of im(P) and is skew-adjoint there.
I8   the orbit-incidence matrix is exactly skew and Route A gives an exact
     Fraction.
I9   Route B counts every affine fixed-point trace exactly over F_5 and gives
     an exact Fraction.
I10  Route A and Route B agree exactly before comparison with -21/8.
I11  the static historical-spectrum checksum is derived exactly and is kept
     separate from the spectrum of K.
I12  only Python standard library, integers and Fraction; no float,
     tolerance, randomness, sampling, external data, or external package.
I13  deterministic sorted stdout, empty stderr, and the audit tally is
     complete before decision routing.
```

## 5. Action-layer ruling

This probe acts on a discrete geometric operator over the full checkpoint
manifold and is assigned to `L2`.

A distinguished boundary, representation, or golden block would be an `L3`
lift and requires a separate named gate. No physical decoder or continuum
curvature statement is inferred from this finite trace probe.

## 6. Two independent exact verifier routes

### Route A. Orbit incidence

Enumerate `H`-orbits in deterministic order. For orbits `O_i` of sizes
`s_i`, define

```text
m_ij = #{x in O_j : (a o c)x in O_i}
       - #{x in O_j : (c o a)x in O_i}.
```

The normalized orbit indicators form an orthonormal basis of `F^H`, not of
`V`. In that basis the full-space compression has matrix entries

```text
K_ij = m_ij / sqrt(s_i s_j),
m_ji = -m_ij,
kappa_A = - sum_{i,j} m_ij^2 / (s_i s_j).
```

The square roots are notation for the orthonormal basis and never enter the
arithmetic. Compute `kappa_A` directly as a `Fraction`.

### Route B. Reynolds group words

Independently compute

```text
kappa_B = Tr(R_H C0 R_H C0)
        = (1/400) sum_{h,k in H} Tr(T_h C0 T_k C0).
```

Expand all four signed permutation words for every pair `(h,k)`. For each
affine word, count fixed points by exact Gaussian elimination over `F_5`.
No orbit-incidence matrix, floating eigenvalue, or stored exploratory output
may enter this route.

The two routes may share only the frozen public generator definitions,
composition convention, and exact construction of `H`. Their principal
trace algorithms are independent. Exact equality `kappa_A = kappa_B` is an
integrity gate.

## 7. Deterministic output and decision precedence

The accepted verifier prints, in a frozen order:

```text
ruling merge and ruling file pin
public generator integrity
composition and Koopman convention
H order and compressed orbit census
invariant dimension and rank(P)
restriction-failure witness W
projector and compression identities
skew-adjoint checks
Route A numerator and denominator
Route B numerator and denominator
route agreement
historical spectrum checksum audit
AUDIT passed/total
DECISION NEGATIVE, TRACE-SURVIVES, or STOP
RESULT
```

Every group, orbit, matrix entry, and printed collection is sorted by a
declared total order. No set or dictionary iteration order reaches a print
path.

Decision routing is binding:

```text
if any integrity gate fails:
    print DECISION STOP
    exit nonzero
elif kappa != -21/8:
    print DECISION NEGATIVE
    exit zero
else:
    print DECISION TRACE-SURVIVES
    exit zero
```

The formal harness separately requires empty stderr and byte identity with
`EXPECTED.txt`.

## 8. Stop rule

Static compilation and source review are allowed before the preregistration
pin. Formal execution, import of the verifier, `EXPECTED.txt`, `RUN.md`, and
`RESULT.md` are forbidden before that pin.

After the remote pin, no change is allowed to:

```text
D1 through D8
witness W
generator formulas
composition or inverse convention
operator word order
carrier or group
projectors
inner product or trace functional
normalization
spectrum-boundary semantics
threshold or decision routing
action layer
accepted verifier bytes
```

Any such change invalidates all run evidence and requires a new probe name.
No exploratory output is reused as formal evidence. No post-result
normalization, operator selection, threshold move, amend, rebase, squash, or
force-push is allowed in the immutable probe lineage.

## 9. Deferred task

A future `P-CURVATURE-OPERATOR-CANONICAL-1` may ask which, if any, operator is
forced by Public Canon 1 independently of `-21/8` and any desired spectrum.
Candidate selection must freeze a public carrier, total endomorphism, inner
product or trace, covariance rule, normalization, decoder type, and
uniqueness criterion before inspecting its numerical output.

## 10. Status transition

```text
Before reviewed merge:
  Owner ruling:             CANDIDATE, NOT PINNED
  PREREG/verify authoring:  NOT AUTHORIZED
  Formal computation:       NOT AUTHORIZED

After reviewed merge and public byte readback:
  Owner ruling:             PINNED by merge commit and ruling file pin
  PREREG/verify authoring:  AUTHORIZED FOR RECIPROCAL REVIEW
  Formal computation:       NOT AUTHORIZED until their separate immutable pin
  Scientific obligation:    O
  Result:                    NONE
```
