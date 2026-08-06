# PREREG. P-TM-SYM2-SPECTRAL-COHERENCE-1

Status: ACCEPTED FOR IMMUTABLE PIN; FORMAL GATE NOT RUN.

This preregistration belongs to public probe lock issue #278, created
before the branch, probe path, or any formal execution under this probe id.

FULL DISCLOSURE OF PROVENANCE. This probe is not blind and does not claim
blind discovery. The identical verifier bytes were executed in the owner's
non-public incubation for candidate C-TM-SYM2-SPECTRAL-COHERENCE-1, with a
frozen incubation preregistration of SHA-256
74c6c574564f1d636e4adb665955de75ba1ddee4ec2216426fe73729f71e4cfc, verifier
SHA-256 equal to the `verify.py` pinned here, and an observed transcript of
SHA-256 410679552c329e420f7e7196e039c04e57708d5c9ff0975b260a2352c070b255
with two-architecture byte identity. That history is provenance, not
evidence. The formal value of this probe is the public pin, the public
two-architecture reproduction under `tools/check_verifier.py`, and the armed
falsifier below. Under this probe id the formal execution count starts at
zero.

## 1. Public authority and identity

```text
probe:                  P-TM-SYM2-SPECTRAL-COHERENCE-1
branch:                 probe/P-TM-SYM2-SPECTRAL-COHERENCE-1
path:                   probes/P-TM-SYM2-SPECTRAL-COHERENCE-1/
owner:                  A. M. Thorn / this owner session
public lock:            issue #278
branch parent:          bff109aa0272cb61e33df60682f2e30358dc9765
Public Canon:           v36 ACTIVE
tag:                    canon-v36
content commit:         df64035f6f0cadbeb17f539eaeec5d8d0f444515
Canon SHA-256:          c8f50d0ce4686d7eedc11599a95debee15c71a2cf13c52c93c3f0605890fa2d5
Canon bytes:            175814
proposed new claim:     TM-SYM2-SPECTRAL-COHERENCE, target status T at a
                        later separately reviewed fold
supported row:          TM-SYM2-PHYSICAL-MEASURE [O], no status change
layer:                  L5 only
```

The collision audit immediately before issue #278 found no remote
branch, no probe path, no registry claim, no open issue, and no open pull
request for this id.

## 2. Frozen public input surface

The verifier reads no files at run time. It embeds the registered constants
as source literals. Their public sources on the branch parent are inputs,
not outputs:

```text
notes/canon/P-TM-SYM2-MEASURE-1-SELECTOR-CLASS-INPUT.md
  bytes   17584
  sha256  5d779ae2ebbdf5c82e5ee3648dd16f6265da855f479427f81d4633d946723105
  blob    4fc11130dfdba3a2d792411a49d52a7a4089bf56
  role    the six registered lines, fixed labels, exact coordinates, and
          the owner-adopted pairing sigma_line

probes/P-TM-SYM2-MEASURE-1/PREREG.md
  bytes   13985
  sha256  c504d7962786436eb68376875f9239c6bc086b57617ced86f4de95a74c7f57d7
  blob    5b692ffe5fe5f4e4ea38489a798267b148c98daa
  role    the frozen exact transfer on W3 and the class definition
```

Before the formal run, public readback must confirm the v36 adoption
surface:

```text
REGISTRY:
  GOLDEN-SIX-LINE-SYM2-FRAME      T
  TM-SYM2-MEASURE                 F
  TM-SYM2-PROJECTIVE-FOURFOLD     T
  TM-SYM2-SEMILINEAR-TWOFOLD      T
  TM-SYM2-REVERSAL-CLOSURE        T
  TM-SYM2-PHYSICAL-MEASURE        O
FRONTIER:
  TM-SYM2-PHYSICAL-MEASURE queue ROOT; STOP; FORMAL, requiring a source
  that retains epsilon_read = chi_Q chi_F as typed L5 data, selects no
  representative, enlarges no gauge, and proves coherence across all 48
  selectors
```

This probe does not open, close, or modify the O row. It registers an
independent L5 claim whose result a future bridge may cite.

## 3. Frozen carrier, class, and operator

The frozen window carrier and drive structure:

```text
W3 = {001, 010, 011, 100, 101, 110} in lexicographic order,
N(w) = bitwise complement of w,
NPERM = the induced index permutation (5, 4, 3, 2, 1, 0).
```

The six registered projective lines over Q(sqrt5), with phi = (1+sqrt5)/2:

```text
v1 = (0, 1, phi)    v2 = (0, 1, -phi)
v3 = (1, phi, 0)    v4 = (1, -phi, 0)
v5 = (phi, 0, 1)    v6 = (phi, 0, -1)
sigma_line = (v1 v2)(v3 v4)(v5 v6)
```

The class and the registered structure, all already public:

```text
Sel_class = {s : W3 -> Lines bijective: s(N(w)) = sigma_line(s(w))},
|Sel_class| = 48 (TM-SYM2-PROJECTIVE-FOURFOLD),
G = frozen projective-linear postcomposition gauge, order 12, free,
    four orbits of size 12,
chi_Q, chi_F = the additive characters of W = Cent(sigma_line)
    (TM-SYM2-SEMILINEAR-TWOFOLD),
epsilon_read = chi_Q chi_F.
```

The frozen exact transfer:

```text
001 -> 101 + 011    010 -> 110 + 100
011 -> 110 + 101    100 -> 001 + 010
101 -> 001 + 011    110 -> 010 + 100
```

For a selector s the signed transfer operator on the six windows is

```text
(L_s)[x, w] = v_{s(w)} . v_{s(x)}  on the 12 transfer edges w -> x,
(L_s)[x, w] = 0                    elsewhere.
```

Every transfer edge lies on a closed walk of even sign multiplicity, so
every similarity invariant of L_s is independent of the projective
representative signs of the lines; the verifier additionally enforces this
by an explicit flip spot check.

## 4. Claim under test

SPECTRAL COHERENCE, five clauses, all asserted by the verifier:

```text
C1  For every unordered pair of selectors {s, t} there exist a window
    permutation P in {id, NPERM} and a diagonal sign matrix D with
    L_t = D P^-1 L_s P D. All 1128 pairs carry explicit witnesses.
C2  All 48 selectors share one exact characteristic polynomial. The
    transcript prints its exact coefficients; the claim includes the
    exact values c_4 = -(6 + 2 sqrt5) and c_2 = (21 + 9 sqrt5)/2, all
    odd coefficients and the constant term zero, equivalently
    det(xI - L_s) = x^2 (x^2 - phi^2)(x^2 - 3 phi^2),
    spectrum {0, 0, +phi, -phi, +sqrt3 phi, -sqrt3 phi}.
C3  No frozen-battery functional separates the two epsilon_read classes:
    the edge-sign product F1 equals +1 on all four orbits, the
    transfer-triangle tau sum equals 0 on all four orbits, the
    all-triple tau sum equals 0 on all four orbits, and the
    characteristic polynomial is one value on all 48.
C4  The exponent-one semilinear realizability count over all 720 line
    permutations is exactly 60, its intersection with the 48-element
    centralizer W has exactly 12 members, and the linear count is
    exactly 60.
C5  The two-graph of the six lines splits the 20 triples exactly 10 and
    10, and Galois conjugation flips every pairwise dot sign.
```

The factorization in C2 is elementary exact arithmetic from the printed
coefficients; byte identity of the committed transcript enforces the
coefficients themselves.

Consequence carried with the claim, as reading prose only: every invariant
of L_s under signed window permutation similarity is constant on the whole
48-member class and carries no epsilon_read witness; the residual bit is
not signed-transfer-spectral data and is carried as typed L5 data. Any
Canon treatment of this reading is at most D-grade prose in a later fold.

## 5. Frozen code

```text
file:     probes/P-TM-SYM2-SPECTRAL-COHERENCE-1/verify.py
sha256:   43be70746bdbf9a005e96143152d1506b543f91ca594e3a75df81a89b0690652
bytes:    13528
command:  python3 probes/P-TM-SYM2-SPECTRAL-COHERENCE-1/verify.py
```

Python standard library only. Exact arithmetic in Q(sqrt5) as Fraction
pairs a + b sqrt5. No float in any assertion. No file reads, no network,
no arguments, deterministic iteration orders. The verifier emits 19
certificate lines, the exact characteristic polynomial coefficients, one
witness-split line, and one terminal RESULT line. Measured wall time is
about 9 seconds on x86_64; the external limit is 600 seconds.

Algorithmic independence from the earlier owner checker lineage:
structural (rho, bits) parametrization of the selector class; gauge built
from the determinant +1 signed coordinate matrices filtered by line-set
preservation; characteristic polynomial by signed permutation expansion of
det(xI - L); realizability by the direct 18 x 9 cross-product linear
system.

## 6. Frozen decision and failure thresholds

Integrity is evaluated before science. Wrong formal environment, an
exception, a nonzero exit without exactly one FIRED-OR-STOP line, nonempty
stderr, nondeterminism, timeout, a transcript that deviates from the
committed `EXPECTED.txt` at pull-request time, or cross-architecture byte
mismatch routes STOP. STOP carries no scientific conclusion, seals the
branch, and is never rerun under this name.

With integrity green, the routes are:

```text
exit 0 and terminal line RESULT: PASS (19 certificates green)
  -> POSITIVE
exit 2 and exactly one FIRED-OR-STOP line naming a certificate that
implements one of the clauses below
  -> NEGATIVE (fired falsifier)
```

The falsifier fires if ANY of:

```text
(a) some selector pair {s, t} admits no witness (P, D) with P in
    {id, NPERM};
(b) more than one characteristic polynomial occurs among the 48;
(c) any frozen-battery member (F1, transfer-triangle tau sum, all-triple
    tau sum, characteristic polynomial) separates the two epsilon
    classes;
(d) the exponent-one count over all 720 permutations differs from 60, or
    its W-intersection differs from 12, or the linear count differs from
    60;
(e) the two-graph split differs from 10 and 10.
```

A valid NEGATIVE is archived verbatim, returned to issue #278, seals
the public pin branch, and is not eligible for a probe pull request under
the checker's exit-zero contract. No threshold moves after the pin. A
frozen-file defect invalidates this probe id rather than authorizing an
amendment, rerun, or repaired threshold.

## 7. Action layer and scope firewall

Layer L5 only. No L1 lift and no L6 claim; the registered TM-SYM2 gates
are untouched. A POSITIVE result closes only the operator-similarity and
blindness statement above for the frozen carrier, pairing, transfer, and
gauge. It proves no L5-to-L6 bridge, no physical measure, no Born reading,
and no uniqueness beyond this scope, and it is not empirical validation.
A NEGATIVE result would falsify only this coherence claim; it would not
falsify GOLDEN-SIX-LINE-SYM2-FRAME, TM-SYM2-PROJECTIVE-FOURFOLD, the
semilinear or reversal records, or the O row.

Coherence under pairings other than the registered sigma_line was observed
in incubation and is outside this probe's scope; any classification over
other pairings is a separate lane.

No outcome automatically edits Canon, registry, frontier, gates, status,
or any other probe. Such treatment is a later separately reviewed fold.

## 8. Formal execution budget and immutable order

Before the first formal execution, this file and `verify.py` receive
syntax, hash, line-ending, import, exact-arithmetic, and content and
security review without any formal execution. The initial commit contains
exactly these two files and is pushed and publicly read back with full
commit, SHA-256, bytes, and Git blobs.

Only then is one formal run authorized:

```text
platform:       Ubuntu 24.04
architecture:   aarch64
run budget:     exactly one deterministic formal execution
environment:    LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1
                PYTHONHASHSEED=0 TZ=UTC
external limit: 600 seconds
```

The formal run uses a fresh fetch and a clean detached checkout of the
exact public pin, executed from the repository root. It records UTC start
and finish, pre and post clean status, command, Python version, exit,
stdout and stderr bytes and SHA-256, LF, CR, and final-byte metadata, and
`deterministic_executions: 1`. If process start becomes ambiguous, it is a
STOP and there is no rerun.

Only after that run may `EXPECTED.txt`, `RUN.md`, and `RESULT.md` be added
and a draft pull request opened. The required GitHub check reruns the
identical pinned verifier on both x86_64 and aarch64 runners and must exit
zero with empty stderr and stdout byte-identical to `EXPECTED.txt`.

The branch is never amended, rebased, squashed, or force-pushed after the
pin. Any update from `main` uses a merge commit. The probe pull request
changes only this one probe directory and is merged, if eligible, only by
merge commit.
