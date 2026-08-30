# P-CURVATURE-COLUMN-GOLDEN-FRAME-2 preregistration

Status: ACCEPTED FOR PIN, FORMAL GATE NOT RUN

This file freezes an exact L2 decision on the already registered historical
commutator. It earns no scientific status. Neither this verifier nor any code
that imports it may run before `PREREG.md` and `verify.py` are committed,
pushed, and read back as the immutable pin.

## Consumed predecessor

`P-CURVATURE-COLUMN-GOLDEN-FRAME-1` is permanently consumed and merged as
`ABANDONED`. Its single pinned attempt stopped before scientific computation
because its dynamic dependency loader failed to register the dependency module
in `sys.modules` before applying `@dataclass` under postponed annotations.
This successor is a new probe, not a repair or resumption. Its scientific
carrier, target, thresholds, routes, and ceiling are unchanged. The sole
implementation delta is the normal Python import registration in
`load_dependency()`.

## Identity and authority

```text
issue:          678
probe:          P-CURVATURE-COLUMN-GOLDEN-FRAME-2
branch:         probe/P-CURVATURE-COLUMN-GOLDEN-FRAME-2
path:           probes/P-CURVATURE-COLUMN-GOLDEN-FRAME-2/
owner:          A. M. Thorn / current owner session
layer:          L2, frozen historical operator only
base:           ebdc91f8d7545fdec5c6a61bf2b3a8bd81b4bf50
Canon:          Public Canon v71
content commit: a77d720433c19976f9ab663d023ec9364eac34eb
Canon SHA-256:  0306abb2e7f855ceb4fcbfdf14265a9d2c5c8bd23b35868b74a92aae16b5e279
```

Collision search found no competing issue, branch, probe, registry row, or
object under this identifier. `CURVATURE-OPERATOR-CANONICAL [O]` is separate
and remains STOP. This probe cannot select a curvature operator.

## Frozen source and implementation dependency

The mathematical carrier is exactly the tuple already owned by
`CURVATURE-HISTORICAL-TRACE [T]` and
`CURVATURE-HISTORICAL-GAUSS-SPLIT [T]`:

```text
X = F_5^6, F = Q^X with counting inner product,
H = <b,d>, R_H = H-Reynolds projection,
P_0 = constant removal, P = P_0 R_H,
V = F^H intersect 1_X^perp,
A = T_a, C = T_c,
K_hist = P[A,C]P restricted to V.
```

To avoid copying and silently drifting the 42 kB historical implementation,
the accepted verifier imports one existing public evidence file only after
checking its bytes:

```text
path:    probes/P-CURVATURE-GAUSS-SPLIT-1/verify.py
SHA-256: 4080da59872a923b0ce4204a93184e17307f6923243d97f0f3105c771c48b8bd
```

That frozen dependency supplies the exact affine maps, `H` closure, orbit
partition, permutation convention, and fraction-free rational rank and kernel
certificate. Importing it does not execute its `main`. The new verifier builds
both historical incidence matrices, the ray quotient, all angles, and both
clique routes itself. A dependency hash mismatch is STOP.

Inherited integrity anchors, not new targets:

```text
|X|=15625, |H|=20,
H-orbits = 5:1, 10:74, 20:744,
dim V=818,
Tr_V(K_hist^2)=-881/8,
rank K_hist=292,
nullity on V=526,
nullity of the redundant 819-column presentation=527,
active orbit-incidence entries=26034.
```

## Typed column rays

Order the `H`-orbits `O_0,...,O_818` by least state and define

```text
chi_j = 1_{O_j} - (|O_j|/|X|)1_X in V,
nu_j  = K_hist chi_j in V.
```

Centering is load-bearing because `K_hist` is typed on `V`. Every Koopman
permutation fixes `1_X`, hence `[A,C]1_X=0`; the concrete incidence column from
`1_{O_j}` is exactly the same `nu_j`.

Discard zero columns and quotient nonzero columns by exact rational projective
equality. The result is

```text
R_col = {[nu_j] : nu_j != 0}.
```

This is only the complete orbit-column extraction. It is not the set of all
image lines, eigenlines, singular lines, or admissible geometric readings.

For `s_i=|O_i|`, put

```text
N_ij = #{x in O_j : ac(x) in O_i}
       - #{x in O_j : ca(x) in O_i}.
```

Then `nu_j` has value `N_ij/s_i` on `O_i`, and

```text
<nu_j,nu_k> = sum_i N_ij N_ik/s_i.
```

The verifier multiplies the metric by 20 and uses integer weights
`20/s_i in {4,2,1}`. This changes no projective equality, squared cosine,
rank, or orthogonal projector.

## Frozen target

For distinct rays define

```text
c2([u],[v]) = <u,v>^2/(<u,u><v,v>) in Q.
```

A six-ray subset is `GOLDEN6` iff

```text
G1. every distinct pair has c2=1/5;
G2. the six representatives span dimension 3;
G3. their six rank-one orthogonal projectors sum to 2 I on that span.
```

This is the abstract criterion realized by
`GOLDEN-SIX-LINE-SYM2-FRAME [T]`. No vector, selector, code, count, or witness
from that probe is imported. The values `1/5`, `3`, and `2` are frozen before
computation.

## Complete verifier obligations

The accepted verifier must, exactly and deterministically:

1. hash-check and load the frozen dependency;
2. verify the exact group and orbit partition;
3. construct all columns by independent pushforward and pullback routes;
4. require entrywise route equality;
5. verify skewness, constant kernels, active entries, trace, rank, and kernel;
6. form the complete primitive projective ray quotient;
7. compute the complete exact pairwise squared-cosine histogram and digest;
8. construct the `c2=1/5` graph;
9. enumerate every six-clique independently by set and bit-mask routes;
10. compare both ordered streams by count, digest, `GOLDEN6` count, digest,
    and least witness;
11. check exact rank and projector tightness on every six-clique;
12. print deterministic ASCII stdout and route every defect to STOP.

Accepted file:

```text
verify.py SHA-256: 0a7d13a4ca4db78b86bd47caa379cb5564bbac87c2b93c59cde6090b0078f6df
bytes:                11529
lines:                291
```

It uses the Python standard library, integers, and `Fraction`. There are no
floats, tolerances, randomness, network calls, subprocesses, timestamps,
target counts, or hard-coded scientific witnesses. Its sole file read is the
frozen dependency above.

## Frozen routes

```text
UNIQUE-GOLDEN6    exactly one GOLDEN6 subset exists.
MULTIPLE-GOLDEN6  at least two GOLDEN6 subsets exist.
PAIR-ONLY         at least one c2=1/5 pair exists, but no GOLDEN6 subset.
ABSENT            no distinct c2=1/5 pair exists.
STOP              any authority, dependency, carrier, route, exactness,
                  inherited-anchor, quotient, completeness, rank, projector,
                  pin, execution, stderr, or architecture gate fails.
```

The four scientific routes exit zero. STOP exits nonzero and carries no
scientific conclusion. No route or threshold may move after the pin.

## Ceiling

A valid result can support at most a theorem about this frozen historical
column-ray family. It cannot select `K_hist`, close
`CURVATURE-OPERATOR-CANONICAL [O]`, prove extraction uniqueness, identify a
frame with physical space or hyperbolic length, create a pseudoconvolution or
decoder bridge, cross to L5/L6, alter any physics dictionary, add a parameter,
write Canon, move the Registry, or authorize a release.

## Formal gate

```text
command: python3 probes/P-CURVATURE-COLUMN-GOLDEN-FRAME-2/verify.py
Python:  3.12 in public jobs
stdout:  deterministic ASCII, byte-identical on x86_64 and aarch64
stderr:  empty
exit:    0 for scientific routes, nonzero for STOP
```

Because the connector writes one path per commit, the two accepted files are
pushed sequentially with no execution between them. The second commit is the
immutable pin. After remote readback exactly one clean local formal execution
may create `EXPECTED.txt`, `RUN.md`, and `RESULT.md`. Neither pinned file may
then be amended, rebased, repaired, or reused.
