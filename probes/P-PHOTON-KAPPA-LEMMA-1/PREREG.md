# P-PHOTON-KAPPA-LEMMA-1 preregistration

Status: `PREREGISTERED CANDIDATE / IMMUTABLE THREE-FILE PIN PENDING
REMOTE READBACK / NO FORMAL RUN`

This document freezes one exact L4 negative-certificate probe. It contains no
formal gate output and earns no scientific, Registry, Canon, dependency,
evidence, frontier, or release status. Formal execution is forbidden until
this document, `verify.py`, and the witness JSON are committed together,
pushed as one immutable pin, read back byte-for-byte from the public remote,
and a later owner comment on issue #200 explicitly authorizes the run.

## Public identity, authority, and immutable input

```text
public lock:          issue #200
public lock URL:      https://github.com/mathorn1973/twist-j/issues/200
probe owner:          A. M. Thorn
probe:                P-PHOTON-KAPPA-LEMMA-1
branch:               probe/P-PHOTON-KAPPA-LEMMA-1
path:                 probes/P-PHOTON-KAPPA-LEMMA-1/
action layer:         L4 support only

STATE:                ACTIVE
Public Canon:         v35
authority:            mathorn1973/twist-j main
tag:                  canon-v35
activation commit:    7c5e1560d56ddf801bf55079674a90682c4b58ee
content commit:       c94fc18ed3b5be1706397e4cc8666b6123858918
Canon SHA-256:        f301ba047ddd3ce1a17d155baed7506a2f889ac48f660797c666b422b49be099
Canon bytes:          173294
initial branch base:  ac264113fd1596ab09d8d31daff93d7a7c7aab19

accepted source:      notes/kappa-witness-2026-08-03/verify_probe_candidate.py
accepted source SHA:  7a3c8e1e3a1658f8b2538a2aa069f1ea678d358a66f56c158a09bc96161ca976
verify.py bytes:      29777
witness filename:     witness_6_3_6_6.json
witness SHA-256:      9b664f16830d2b562949933e40b4f1460d9da5645a88beff7bca347b70320313
witness bytes:        280106
```

The owner froze the definition surface after public readback in issue #200
comment `5175681684`, then accepted the exact verifier hash and authorized
only this immutable pin in comment `5175862160`. The second comment still
forbids formal execution until remote pin readback and a later, separate run
authorization.

The initial pin inventory is exactly:

```text
PREREG.md
verify.py
witness_6_3_6_6.json
```

No `EXPECTED.txt`, `RUN.md`, `RESULT.md`, architecture record, formal stdout,
or result is part of the pin.

## 1. Equation

Use the finite-support cubical chain complex on the infinite lattice
`Z^4`. An oriented edge `(v,d)`, `d in {0,1,2,3}`, runs from `v` to
`v+e_d`. An oriented face `(v,a,b)`, `0 <= a < b <= 3`, has boundary

```text
partial f_(a,b)(v) = e_a(v) + e_b(v+e_a)
                     - e_a(v+e_b) - e_b(v).
```

All chain equalities are coefficientwise over `Z`, and
`partial(partial(.))=0`.

Freeze:

```text
BaseCurrent = {j in C_1^c(Z^4; {0,+1,-1}) :
               j != 0 and partial j = 0}

Fill(j)     = {n in C_2^c(Z^4; {0,+1,-1}) :
               partial n = 5j}

ParentWorldline
             = {j in BaseCurrent : Fill(j) != empty}

CertificateCurrent
             = {j in ParentWorldline :
                supp(j) is connected as an undirected graph}

L(j)         = |supp(j)|

F_occ(j)     = min {|supp(n)| : n in Fill(j)}
               for j in ParentWorldline.
```

`F_occ(j)` is a positive integer: `Fill(j)` is nonempty on its domain, and
the support-cardinality set is a nonempty subset of the positive integers.
No extended-integer or `+infinity` convention is used.

Let `kappa=a/b`, where `a,b` are coprime positive integers. The universal
occupancy and exact threshold gates are

```text
(K1)  b F_occ(j) >= a L(j) for every j in ParentWorldline,

(K2)  2^(4a) > 2401^b, where 2401=7^4.
```

No floating-point approximation of `log_2(7)` is admissible.

### Frozen singleton exclusion lemma

Let `j in ParentWorldline` and `n in Fill(j)` satisfy

```text
2^F <= 7^L,  L=L(j)>=1,  F=|supp(n)|.
```

For every coprime positive `(a,b)` satisfying K2, K1 fails at this `j`.
Indeed, `F_occ(j)<=F`. If K1 held, then

```text
bF >= b F_occ(j) >= aL.
```

K2 is equivalent, by strict monotonicity of fourth powers on positive
integers, to `2^a>7^b`. Therefore

```text
2^(bF) >= 2^(aL) > 7^(bL),
```

which contradicts `(2^F)^b <= (7^L)^b`. Thus one admitted pair excludes
every positive rational `kappa` passing K2 from satisfying universal K1.
The proof uses only exact positive-integer comparisons. It neither computes
nor claims the minimum filling.

The pinned pair has

```text
L=3240,
F=7993,
partial j=0,
partial n=5j,
2^7993 <= 7^3240.
```

The frozen counterexample family is the expressly admitted singleton
`W={(j_*,n_*)}`.

## 2. Code

`verify.py` is the accepted exact verifier. Its pin is

```text
bytes:    29777
SHA-256:  7a3c8e1e3a1658f8b2538a2aa069f1ea678d358a66f56c158a09bc96161ca976
```

It is self-contained and uses only the Python standard library. It accepts no
arguments, resolves the adjacent witness relative to `__file__`, performs no
network or subprocess operation, writes no file, uses no randomness, clock,
floating point, adaptive threshold, `eval`, `exec`, or scientific `assert`,
and buffers successful stdout before emitting it as ASCII with LF line ends.
A gate failure emits zero stdout, one sanitized STOP line on stderr, and exit
1. An argument emits zero stdout, exact `usage: verify.py` plus LF on stderr,
and exit 2.

The formal command, when later authorized, is exactly

```text
python3 -B probes/P-PHOTON-KAPPA-LEMMA-1/verify.py
```

from the repository root.

The verifier attempts refutation at every frozen gate:

```text
C1  strict UTF-8 without BOM; canonical JSON bytes; exact ordered keys
    P,m,C,D,L,F,j,n; no duplicate object names or support keys; every
    numeric atom has type int; exact list shapes; directions and face
    orientations valid; coefficients exactly -1 or +1; strict raw-list
    order for j and n

C2  j is a nonzero ternary current and partial j=0

C3  supp(j) is connected; all undirected degrees are even; coefficient
    signs give a balanced directed support; an explicit orientation-matching
    closed Hierholzer traversal is contiguous, has 3240 steps, uses every
    support edge exactly once, and reuses none

C4  n is ternary and has support cardinality 7993

C5  two separately implemented boundary paths both give partial n=5j;
    their nonzero support has 3240 edges with values exactly {-5,+5};
    independent expansion gives partial(partial n)=0

C6  declared and computed L,F are 3240,7993; witness bytes are 280106;
    witness SHA-256 is the frozen value

C7  exact big integers give 2^F<=7^L; B=max{m:2^m<=7^L}=9095;
    F<=B and B-F=1102
```

The verifier source records, but does not import, these public provenance
hashes:

```text
notes/kappa-witness-2026-08-03/verify_witness.py
  ff462d724f8c724e5df1987d32bbfa3e71518fbec547b00bc1195b567d9c74c0

notes/kappa-witness-2026-08-03/adversarial_check_fresh.py
  c6ae055d30aaf8ec55020db4df1e250f5a65f805b73e521b3db52b59f5c7b9cb

reproduce/photon-electron/verify.py at Public Canon v35
  d980aa17cd2e597a2924273ea7079333b63419ff472560a395382fa293667e74
```

## 3. Carrier or data

The parent quantifier is all of `ParentWorldline`, not only its connected
subclass. Its support may have any finite number of components. A
`BaseCurrent` with `Fill(j)=empty` is outside `ParentWorldline`; K1 and
`F_occ` are not evaluated there.

`CertificateCurrent` is the first frozen falsifier subclass and is explicitly
a subset of `ParentWorldline`. On this subclass:

- the support graph is connected;
- repeated vertices, crossings, and every even support degree up to 8 are
  allowed;
- support-edge coefficients obey `|j_e|<=1`, so repeated support edges are
  absent;
- chains, not walks, are primary; walk backtracks, repeated traversal, and
  coefficients outside `{0,+1,-1}` are not carrier inputs;
- the checker derives an Euler traversal only as a membership certificate;
- coefficientwise chain equality is used;
- translated currents are distinct chains, while all frozen predicates are
  translation invariant;
- finite support in `Z^4` makes winding trivial.

An admitted certificate pair is `(j,n)` with
`j in CertificateCurrent` and `n in Fill(j)`. The serialized `n` witnesses
that `j in ParentWorldline`.

The only data input is the adjacent canonical JSON witness. Its inert
construction metadata is

```text
P=6, m=3, C=6, D=6.
```

Those fields are schema-checked and frozen by the whole-file hash but support
no scientific inference. The file has no terminal LF. Its `j` and `n` lists
are strictly lexicographically ordered by `(vertex,direction)` and
`(vertex,a,b)`, respectively.

Counterexample families are, by owner definition for this lane, finite
nonempty sets of admitted pairs satisfying `2^|supp(n_i)|<=7^L(j_i)`.
Singletons are allowed. No pump, asymptotic sequence, second family member,
optimal filling, or minimum solver is required or claimed.

## 4. Systematics

All five systematics are mandatory and execute inside the accepted verifier.

### S1 - registered shape regression

Embed the public face-incidence algorithm and require closed edge-simple
loops, exact `LB`, exact `2^LB>7^L`, and this ordered table:

```text
square-1x1       L=4   LB=17
ladder-1x2       L=6   LB=26
ladder-1x3       L=8   LB=35
ladder-1x4       L=10  LB=44
ladder-1x5       L=12  LB=53
ladder-1x6       L=14  LB=62
square-2x2       L=8   LB=36
skew-hexagon     L=6   LB=24
staircase        L=8   LB=31
```

The exact minimum `LB/L` is `31/8`. `LB` remains only the registered greedy
incidence bound and is never identified with `F_occ`.

### S2 - out-of-carrier torus control

On periods `(3,4,4,4)`, freeze

```text
sigma(x)=(-1)^(x1+x2+x3),
j0(x)=sigma(x),
n01(x)=sigma(x),
n02(x)=sigma(x),
n03(x)=(sigma(x)-1)/2.
```

Require modular `partial j=0`, modular `partial n=5j`, and 64 support
components. Reinterpret the same representative keys with ordinary
nonperiodic `Z^4` boundaries and require `partial j!=0`. It is rejected both
by the ambient carrier and by the connected certificate subclass; it proves
nothing about the broader parent by disconnectedness alone.

### S3 - exact in-memory mutation controls

The controls bypass only C6's raw fixture pin and expose no CLI bypass:

```text
flip [[0,-2,-1,0],0,2,+1] to coefficient -1
  C1-C4 PASS, then C5_BOUNDARY

delete [[0,-2,0,0],0,-1]
  C1 PASS, then C2_NOT_CLOSED

duplicate the first face immediately adjacent
  C1_DUPLICATE_FACE

change the first edge coefficient from -1 to 2
  C1_COEFFICIENT
```

For the fifth control use bridge descriptor
`((1,1,0,0),d01=0,d23=3)`:

```text
delete  ((1,1,0,0), direction 3, coefficient +1)
delete  ((2,1,0,0), direction 3, coefficient -1)
restore ((1,1,0,0), direction 0, coefficient +1)
restore ((1,1,0,1), direction 0, coefficient -1)
re-sort j strictly by (vertex,direction)
```

Require C1-C2 PASS, preserved `partial j=0`, and exact failure
`C3_DISCONNECTED`.

### S4 - determinism

Read and evaluate the pinned raw input twice from fresh immutable state,
compare the two result records, render twice, and require byte-identical
transcripts. The later committed `EXPECTED.txt` and both architecture jobs
provide the stronger cross-process and cross-architecture check.

### S5 - vocabulary

A successful transcript contains exactly one outcome line, exactly

```text
OUTCOME BELOW-THRESHOLD
```

and no `CANDIDATE-REFUTED` token.

## 5. Threshold and decision map

The four predicates are lane-wide:

```text
KAPPA-PROVED
  a complete exact universal proof supplies an admissible a/b satisfying
  K1 on all ParentWorldline and satisfying K2

BELOW-THRESHOLD
  an exact admitted counterexample family, where a singleton is allowed,
  excludes every admissible a/b satisfying K2 from universal K1

CANDIDATE-REFUTED
  a separately pinned coefficient, reduction, or positive proof fails,
  but the exact result does not exclude every a/b satisfying K2

STOP
  authority, collision, carrier, typing, pin, proof-completeness, security,
  hash, systematics, execution, transcript, or reproduction requirements
  fail
```

This probe is only the pinned negative-certificate route. Its complete frozen
map is

```text
C1-C7 and S1-S5 PASS on the pinned singleton witness,
and every execution, transcript, and reproduction gate passes
  -> BELOW-THRESHOLD

any schema, carrier, boundary, count, inequality, hash, systematics,
execution, transcript, or reproduction failure
  -> STOP
```

`KAPPA-PROVED` and `CANDIDATE-REFUTED` are not outputs of this probe. A
missing, altered, or failing witness proves nothing about another coefficient
or proof and is STOP, never a scientific refutation. STOP has priority over
any scientific interpretation.

A valid `BELOW-THRESHOLD` route exits zero with empty stderr and proceeds
through the same exact transcript and architecture checks. Before those gates
complete, no public status is earned. A STOP exits nonzero, preserves its
diagnostic, seals this probe name, and authorizes no repair, threshold move,
reinterpretation, or rerun.

## 6. Action layer

This probe consumes only L4 finite support chains, boundaries, and support
cardinalities. It consumes no tick, history, stream, Born multiplier,
probability, or measure. There is no transition to L1, L2, L3, L5, or L6 and
no named cross-layer gate is required.

The result, whichever route fires, does not establish a roughening
certificate, Froehlich-Spencer import hypothesis, massless phase, Coulomb
window, continuum limit, photon propagator, or physical photon statement. It
does not introduce a physical photon carrier, FCC lattice, spatial lift,
displacement support, shell weight, polarization, holonomy, time bridge,
measure, or SI statement. It does not change `CENTER-SPLIT-SELECTION`, and it
does not promote `KAPPA-SHAPES [C]`, `MONOPOLE-COST [C]`, or any other row.

Issue #201 and the roughening route are not executed, proved, falsified,
closed, reopened, or reworded here.

## Pin, execution, and result order

1. Statically inspect this exact three-file tree. Do not import, compile, or
   execute formal `verify.py`.
2. Commit the three files once and push the exact branch. Do not amend,
   rebase, squash, or force-push after this commit.
3. Record the full pin commit and parent, exact inventory, three SHA-256
   values, byte counts, Git blob IDs, LF/CR/NUL metadata, and final-byte
   metadata in issue #200.
4. Read all three files back from the public remote at the exact pin commit
   and require local/remote byte identity. Do not open a pull request.
5. Only after that readback and a later explicit owner authorization on issue
   #200, run exactly once from a clean Linux or Linux-compatible checkout at
   the immutable pin. Record neutral environment fields. The environment is
   fixed to `LC_ALL=C`, `LANG=C`, `PYTHONDONTWRITEBYTECODE=1`,
   `PYTHONHASHSEED=0`, and `TZ=UTC`; the command is the exact command in
   section 2.
6. If exit is zero and stderr is empty, preserve the raw stdout byte-for-byte
   as `EXPECTED.txt`; add `EXPECTED.txt`, `RUN.md`, and `RESULT.md` in one
   result commit without changing any pinned file.
7. Push the additive result commit, then open one draft pull request changing
   only `probes/P-PHOTON-KAPPA-LEMMA-1/`.
8. Require clean GitHub x86_64 and aarch64 jobs to use the same verifier hash,
   exit zero with empty stderr, and match the one committed `EXPECTED.txt`
   byte-for-byte. Preserve a fired scientific falsifier.
9. Merge without squash or rebase only after review, security audit, and the
   aggregate required check pass. A later separate Canon fold decides any
   Registry, parent, frontier, evidence, dependency, or release change.

The initial three-file pin is intentionally not a pull-request head because a
complete probe pull request requires the result files. No post-pin edit to
`PREREG.md`, `verify.py`, or the witness is permitted.

## Pre-pin development disclosure

The definition package, candidate witness, two reference checkers, and exact
verifier source were developed, adversarially reviewed, and run only on the
explicitly non-formal `notes/` surface before this pin. Their known 911-byte
review transcript and its hash are not formal evidence and are not
retroactively formalized. The owner authorized that preparation in issue
#200. No execution under this probe path or branch occurred before the pin.

## Scope firewall

This preregistration creates no Canon claim or status. In particular it makes
no assertion that the formal result will pass, that `F=F_occ`, that the
exhibited filling is optimal, that a pump family exists, that the parent
photon route closes, or that roughening succeeds or fails. Any broader result
requires a separate owner disposition and a later sealed Canon fold.
