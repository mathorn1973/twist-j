# PREREG. P-TM-SYM2-MEASURE-1

Status: ACCEPTED FOR IMMUTABLE PIN; FORMAL GATE NOT RUN.

This preregistration belongs to public probe lock issue #130, created before
the branch, probe path, verifier, or formal data. Closed issue #119 is the
completed definition lock; it is not reused as the formal-probe lock.

No evaluation output, expected gauge order, expected orbit count, expected
partition, expected scientific route, or output hash is known to this
preregistration. The owner-definition history discloses non-public incubation
and break work, which is provenance only and not evidence. This probe is the
first public formal decision under the frozen `S_TM`; it does not claim
globally blind discovery.

## 1. Public authority and identity

```text
probe:                  P-TM-SYM2-MEASURE-1
branch:                 probe/P-TM-SYM2-MEASURE-1
path:                   probes/P-TM-SYM2-MEASURE-1/
owner:                  A. M. Thorn / this owner session
public lock:            issue #130
branch parent:          390c1d254b0c3939ff7fc9e6b900eac8bd1b877a
Public Canon:           v16 ACTIVE
annotated tag target:   ffed1ff536972113cbc3d8f74830172206b3a489
content commit:         a96f6c7a8ed63c2234977cb1c7a3432fd315bd7a
Canon SHA-256:          836b8d642f5209d46a5b833a3a1e7a1acc14a249e83066af1adb21845242d4a9
Canon bytes:            89364
owner row:              TM-SYM2-MEASURE [H]
scheduler:              MEASURE / ROOT / READY / FORMAL
layers:                 MULTI, L1 -> L5 -> L6
```

The tag is annotated, dereferences to the stated target, and is an ancestor of
the branch parent. The parent workflow
`https://github.com/mathorn1973/twist-j/actions/runs/29984465093` is green.
The collision audit immediately before issue #130 found no remote branch,
probe path, formal pull request, or distinct formal issue for this id and no
open pull request.

## 2. Frozen public input surface

The following bytes on the branch parent are inputs, not outputs:

```text
notes/canon/P-TM-SYM2-MEASURE-1-PREDEFINITION.md
  bytes   9749
  sha256  956f9b9eeb6fc3e033f126d1dc6d1a3b6106ce38391f9094e9108fecd50365da
  blob    c82ff6333386fdadab17e44a67f7f000c2ef4930

notes/canon/P-TM-SYM2-MEASURE-1-SELECTOR-CLASS-INPUT.md
  bytes   17584
  sha256  5d779ae2ebbdf5c82e5ee3648dd16f6265da855f479427f81d4633d946723105
  blob    4fc11130dfdba3a2d792411a49d52a7a4089bf56

notes/canon/P-TM-SYM2-MEASURE-1-BORN-BRIDGE-INPUT.md
  bytes   21114
  sha256  af6741bb969450e3f2c41d66ef38d832cad6e3008db18aa7faa9b427b5c49af0
  blob    b1988abd918db04866c2d49c6aadf714da07e06d

notes/canon/P-TM-SYM2-MEASURE-1-OWNER-DEFINITION.md
  bytes   40352
  sha256  c9471fecf854badf75fdf5ade81ea436e82d37f5d13116227a22834152903022
  blob    68f3e96a6962e975b14ba1e432db557357466ac3

notes/canon/P-TM-SYM2-MEASURE-1-DEFINITION-CHECKER.py
  bytes   69159
  sha256  f0499d1cd42ae199edff048277841bcea3074e28c9b73c8c12895b731d35100c
  blob    06e5c5bc8851d10a905740ae88f3e2a53b3e2c20
```

The v16 adoption surface is separately load-bearing. Before the formal run,
public readback must confirm:

```text
REGISTRY: TM-SYM2-MEASURE has status H and the v16-frozen S_TM falsifier.
FRONTIER_PROGRAMS:
  TM-SYM2-MEASURE  MEASURE  ROOT  READY  FORMAL
NORMATIVE:
  TM-SYM2-MEASURE  HYPOTHESIS  TM-SYM2-MEASURE  H  MULTI
  GATE-L1-L5-TM-SYM2-SELECTOR-STREAM;
  GATE-L5-L6-TM-SYM2-BORN-MEASURE
GATES:
  GATE-L1-L5-TM-SYM2-SELECTOR-STREAM, L1 -> L5, OPEN_LIFT
  GATE-L5-L6-TM-SYM2-BORN-MEASURE, L5 -> L6, OPEN_LIFT
DEPENDENCIES:
  the exact nine parents DEF-ARCHITECTURE, DEF-AUTONOMOUS-STATE,
  GOLDEN-SIX-LINE-SYM2-FRAME, GYRON-DENSITY, MEASURE-BORN-VERB,
  DEF-ACTION-LAYERS, RAMIFIED-TM-LIFT, SUBSTRATE-KNIT, and
  ABELIAN-FACE-DICTIONARY; no DEF-LOG-STREAM edge.
```

This readback is required because the owner checker's B7 audit adds four
delta edges in memory and checks its two gate records as constants. B7 alone
is not treated as proof that v16 publicly adopted those rows.

## 3. Frozen carrier, selector class, and gauge

The frozen window carrier is

```text
W3 = {001, 010, 011, 100, 101, 110},
N(w) = bitwise complement of w.
```

The six registered projective lines, their fixed labels, the owner-adopted
pairing

```text
sigma_line = (v1 v2)(v3 v4)(v5 v6),
```

and the exact `Q(phi)` coordinates are those in the frozen inputs. The class
and equivalence are unchanged:

```text
Sel_class = {s : W3 -> Lines total and surjective:
             s(N(w)) = sigma_line(s(w)) for every w}.

G = Aut(Lines, sigma_line):
    all projective-linear transformations over Q(phi) preserving the
    six-line set and commuting with sigma_line as a line permutation.

s ~ g o s for g in G.
```

Projective signs are absorbed in the line representation. The window-side
map `N` is drive structure, not gauge. Semilinear or Galois transformations,
other carriers, noncontiguous or variable windows, different sampling
geometries, different pairings, and different magnetic axioms are outside
this probe. In particular, the checker does not evaluate a semilinear or
Galois extension of `G`.

## 4. Frozen pre-evaluation reduction (non-routing theorem)

This theorem is public before the pin and reduces, but does not answer, the
information-bearing computation.

The quotient `W3/<N>` consists of the three pairs

```text
{001,110}, {010,101}, {011,100},
```

and `Lines/<sigma_line>` also has three pairs. Every member of `Sel_class`
is a surjection between two six-element sets and hence a bijection.
Equivariance therefore gives one permutation of the three quotient pairs
and one orientation bit in each pair. Conversely each such choice gives one
selector. Thus

```text
|Sel_class| = 3! * 2^3 = 48.
```

Let `A = Aut_set(Lines, sigma_line)`, so `A` is the wreath product
`C2 wr S3` of order 48 and `Sel_class` is an `A`-torsor. The frozen
projective gauge satisfies `G <= A`. Its postcomposition action is free:
if `g o s = s`, surjectivity of `s` forces `g = id`. The public
signed-coordinate subgroup `H <= G` has certified order 12. Hence

```text
|G| is one of 12, 24, 48;
number of G-orbits is 48 / |G|, one of 4, 2, 1;
the selector class is CANONICAL exactly when |G| = 48.
```

No value of `G`, orbit count, orbit partition, or result route is supplied.
The complete exact projective-linear enumeration of `G` is the sole new
information-bearing calculation.

The exact transfer sends

```text
001 -> 101 + 011    010 -> 110 + 100
011 -> 110 + 101    100 -> 001 + 010
101 -> 001 + 011    110 -> 010 + 100.
```

Every row and column has sum 2, so the uniform vector is stationary; the
frozen exact rank certificate gives uniqueness:

```text
f = (1/6, 1/6, 1/6, 1/6, 1/6, 1/6).
```

Every selector is a bijection, so every pushforward has the same six line
weights. The registered cardinal-frame theorem then gives, for every
selector,

```text
nu_s = (1/6)^6,
M_s = (1/3) P1 + (2/15) P5.
```

Thus, under green structural premises, EMPTY/N1, gauge disagreement, and
N3 are mathematically forced not to fire. They remain unchanged in the
checker as first-class defensive routes; this theorem does not delete,
reorder, override, or reinterpret any branch.

The quotient transfer gives `third = 1/3`. Conditional on the
owner-adopted phaseful dictionary and its explicitly supplied magnetic
axiom pair, literal Fourier inversion gives `delta_0 + delta_1` and
`half = 1/2`; the Born measure is `mu_B^f = f`, and the event
`E_00 = {001}` has measure `1/6 = rho_00`.

The all-`N` census identity is theorem-grade, not inferred from the nine
checker spot checks: `n -> n-1` is a bijection from `[1,N]` to `[0,N-1]`
and `pi_12(q(n)) = (theta_(n-1), theta_n)` identically.

## 5. Frozen code and data

The accepted verifier is a zero-argument Python-standard-library wrapper:

```text
file:     probes/P-TM-SYM2-MEASURE-1/verify.py
sha256:   30b581a2b84e0ac8b3b333e5731f7ecdcfa9bfb975585da0603f02ab3e8ed6eb
bytes:    137120
command:  python3 probes/P-TM-SYM2-MEASURE-1/verify.py
```

For historical hermeticity, `verify.py` transparently embeds as raw ASCII
bytes the exact owner checker, `canon/NORMATIVE.tsv`, and
`canon/DEPENDENCIES.tsv` from the branch parent. Their identities are:

```text
owner checker:
  bytes   69159
  sha256  f0499d1cd42ae199edff048277841bcea3074e28c9b73c8c12895b731d35100c
  blob    06e5c5bc8851d10a905740ae88f3e2a53b3e2c20
NORMATIVE.tsv:
  bytes   22453
  sha256  78bd84df4be6ba777c2d721d722b335b29b5f13644aae891814d51c6e080ad54
  blob    6518651db3e62df2b4a3378ffaf314d8dd409b0f
DEPENDENCIES.tsv:
  bytes   39547
  sha256  eb3b993015fa4e1a97a5fe9b78fa39e91391c5ffaf88f6a357458c03c6c137d1
  blob    86529ac216c7c970c530fc5b3d25da84916c42a5
```

The wrapper verifies those identities, materializes only the two tables in a
temporary repository-shaped root, compiles the exact checker bytes, sets its
internal argv to `--evaluate`, and calls its exact `main()` once in-process.
Checker stdout and stderr are buffered until completion, so an external
timeout cannot leave a detached evaluation or publish a partial scientific
transcript. An integrity-clean transcript is released byte-for-byte; nonempty
stderr is preserved while stdout becomes one deterministic wrapper STOP route.
No wrapper success line is added.

The wrapper embeds no expected gauge order, orbit count, partition, route,
weight vector, stdout, or output hash. It only enforces input integrity,
the exact formal environment, exact byte transport, and that a completed
checker transcript has exactly one route in the frozen route grammar.

## 6. Frozen decision and failure thresholds

Integrity is evaluated before science. Any input hash/byte mismatch,
non-ASCII or malformed embedded payload, wrong formal environment,
exception, incomplete transcript, missing/multiple/unknown `ROUTE:`,
failed B1-B7/S1-S4/F1-F3/I1-I5 certificate, incomplete selector or gauge
enumeration, invalid v16 adoption readback, nonempty stderr, nondeterminism,
timeout, or cross-architecture byte mismatch routes `STOP`. STOP carries no
scientific conclusion and is never rerun under this name.

With integrity green, the one checker route binds in this order:

```text
EMPTY / N1
  -> NEGATIVE
NONCANONICAL / N2, with its complete exact orbit partition
  -> NEGATIVE
valid all-representative GAUGE-COHERENCE disagreement
  -> NEGATIVE
valid N3 failure: unequal weights, noncommutant M_s, or changed 5:2 ratio
  -> NEGATIVE
exact step-6 Born/layer terminal, followed by checker RESULT: PASS,
together with the separately verified Public Canon v16 adoption surface
  -> probe result POSITIVE
```

`RESULT: PASS (all certificates green in mode --evaluate)` and exit zero
mean checker integrity only; they do not by themselves select POSITIVE.
Every integrity-clean emitted checker route is archived verbatim. If wrapper
integrity fails before release, its single wrapper STOP route and any stderr
are archived instead. A valid NEGATIVE is a successful formal computation and
must exit zero. A structural STOP may exit nonzero. Such a nonzero STOP is
returned to issue #130, seals the public pin branch, and is not eligible for a
probe pull request under `tools/check_verifier.py`'s exit-zero contract; it is
not rerun or repaired under this name.

No threshold moves after the pin. A frozen-file defect invalidates this
probe id rather than authorizing an amendment, rerun, or repaired threshold.

## 7. Action layers and scope firewall

The only layer path is the pair of already registered v16 gates:

```text
L1 -> L5  GATE-L1-L5-TM-SYM2-SELECTOR-STREAM
L5 -> L6  GATE-L5-L6-TM-SYM2-BORN-MEASURE
```

A POSITIVE result closes only the frozen `S_TM` candidate relative to the
owner-adopted fixed-length contiguous bijective carrier family, centered
window, coordinate-axis pairing root, projective-linear gauge, and the
conditional phaseful dictionary. It proves no uniqueness among different
carriers, sampling geometries, pairings, semilinear gauges, magnetic axioms,
or physical models and is not empirical validation.

A NEGATIVE/N2 result falsifies canonical selector choice inside that frozen
definition. It does not falsify `GOLDEN-SIX-LINE-SYM2-FRAME [T]`, the
Thue-Morse language or stationary law, the registered face weights,
`GYRON-DENSITY`, or every possible TM-to-measure definition.

No outcome automatically edits Canon, registry, frontier, gates, status,
release metadata, physical claims, or any other probe. Such treatment is a
later separately reviewed fold.

## 8. Formal execution budget and immutable order

Before the first formal execution, this file and `verify.py` receive syntax,
AST, embedded-byte, hash, blob, line-ending, import, exact-arithmetic,
route-grammar, and content/security review without importing or executing the
wrapper or the embedded checker. The initial commit contains exactly these
two files and is pushed and publicly read back with full commit, SHA-256,
bytes, and Git blobs.

Only then is one formal run authorized:

```text
platform:       Ubuntu 24.04
architecture:   aarch64
run budget:     exactly one deterministic evaluate execution
environment:    LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1
                PYTHONHASHSEED=0 TZ=UTC
external limit: 600 seconds
```

The formal run uses a fresh fetch and clean detached checkout of the exact
public pin. It records UTC start and finish, pre/post clean status, command,
Python version, exit, stdout/stderr bytes and SHA-256, LF/CR/final-byte
metadata, exact route, all frozen identities, and
`deterministic_executions: 1`. If process start becomes ambiguous, it is a
STOP and there is no rerun.

Only after that run may `EXPECTED.txt`, `RUN.md`, and `RESULT.md` be added
and a draft pull request opened. The required GitHub x86_64 check must use
the same verifier hash, exit zero, empty stderr, and byte-identical stdout.

The branch is never amended, rebased, squashed, or force-pushed after the
pin. Any update from `main` uses a merge commit. The probe PR changes only
this one probe directory and is merged, if eligible, only by merge commit.
