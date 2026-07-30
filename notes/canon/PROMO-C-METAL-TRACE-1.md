# PROMO-C-METAL-TRACE-1

Self-contained promotion proposal. A public fold can consume this without reading
anything else. This document carries no authority; it becomes canon only after the
public pipeline reproduces the verifier on two architectures byte-identical and the
owner opens the fold PR.

## 1. Identity, status, scope

```
candidate id        C-METAL-TRACE-1
public claim id     METAL-TRACE-CASCADE
proposed status     T   (public maximum; no T-LOCK on the public line)
proposed scope      the two simplest metals, trace t in {1, 2}
target line         Public Canon v10 -> fold to v11, mathorn1973/twist-j main
canon section       4. The two places
action layer        L2 (manifold / field arithmetic)
```

The promoted claim is the exact ARITHMETIC cascade only. The physical reading
(run vs record, reversible run against irreversible write, the arithmetic seat of the
arrow) is H and is explicitly NOT promoted by this proposal.

## 2. Exact statement (METAL-TRACE-CASCADE [T])

Write the golden and silver ratios as the two roots of x^2 = t x + 1 with integer trace
t. Gold is t = 1 (phi^2 = phi + 1); silver is t = 2 (delta^2 = 2 delta + 1); both are
units of norm -1. The single integer t fixes the metal:

(a) disc(x^2 - t x - 1) = t^2 + 4 gives 5 for gold and 8 for silver, and the ramified
    prime of each metal divides its own discriminant (5 | 5, 2 | 8). The two places
    already registered (DEGREES-BY-PRIME, Z2-PLACES-SPLIT) are exactly the ramified
    primes of these two metallic laws.
(b) growth is the metal's own integer recurrence: Fibonacci F_(n+1) = F_n + F_(n-1) with
    phi^n = F_n phi + F_(n-1) for gold, and Pell P_(n+1) = 2 P_n + P_(n-1) with
    delta^n = P_n delta + P_(n-1) for silver.
(c) the silver pure form 1 + m_8^2 = 1 + i = sqrt2 * m_8 = sqrt(2i) has (1 + i)^2 = 2i,
    amplitude sqrt2 = m_8 + m_8^-1 and phase pi/4, and is NOT a unit,
    N_{Q(zeta_8)}(1 + i) = 4, in contrast with the golden pure form J = 1 + zeta_5^2,
    which is a unit, N(J) = 1 (J-UNIT).

Scope: t in {1, 2}. The trace-to-field map is not injective for general t (t = 4 also
lands in Q(sqrt5), disc 20, squarefree kernel 5), so no all-t claim is made.

## 3. Falsifier

Exact and binary. Fires if, on independent recomputation, any frozen identity is false
(disc != t^2 + 4 for t in {1, 2}; N(phi) != -1; N(delta) != -1; (1 + i)^2 != 2i;
sqrt2 * m_8 != 1 + i in Z[zeta_8]; N_{Q(zeta_8)}(1 + i) != 4; N(J) != 1), OR if the
pinned verifier stdout is not byte-identical across aarch64 and x86_64. A single
differing byte fires. As a T row it carries no FRONTIER falsifier entry; the falsifier
above is the recomputation gate.

## 4. Verifier and pins

```
PREREG              PREREG_C-METAL-TRACE-1.md
                    sha256 2d8beb61055346a50b7b70802143550e8f78a920fb2c17bcd1e868a740a68f09
                    4509 bytes

verifier of record  C-METAL-TRACE-1_verifier.py
                    sha256 57501a2975ff71a43a1e5f98e7f976e35d27dd6252143fb5d20ce715375fff2a
                    4938 bytes
verifier stdout     EXPECTED_verifier.txt
                    sha256 8f1567fd0d9f2ac766d8242821ec8bff6277a3c40fcd467a284662dd9de54d12
                    result: ALL OK, 19 checks

independent break   C-METAL-TRACE-1_break.py   (companion-matrix path + scope probe)
                    sha256 f7feb2798eda1337f2e4b7da275bc29d1c1feb33f51a57c74219e132d6e55fb1
                    4657 bytes
break stdout        EXPECTED_break.txt
                    sha256 2c8065bf1a94a82ac9eb4a799e2bf1b3fee9ffcded94c1040de0bb31d307ab91
                    result: CORE SURVIVES, 31 assertions, 0 failures; scope boundary
                            t=1 / t=4 located and pinned

run environment     LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
this session        x86_64, Python 3.12.3  (one platform; aarch64 is the open step)
```

## 5. Break record (step 4 of the candidate discipline)

The break attempt used an independent code path: integer 2x2 companion matrices
[[0,1],[1,t]] and integer squarefree kernels, never importing Fraction and never using a
cyclotomic basis; sqrt(2i) was rechecked directly in Z[i]. It reproduced every core
identity (metal law as C^2 = t C + I, det = -1, trace = t, Fibonacci and Pell from
matrix powers, (1+i)^2 = 2i, degree-2 norm 2 squaring to degree-4 norm 4) and then
probed injectivity of trace -> field, finding the t = 1 / t = 4 collision on Q(sqrt5).
That collision is a scope, not a contradiction: the claim is stated only for t in {1, 2}.
The candidate survives one honest attempt to break it.

## 6. Dependency edges

Rests on / connects to (public v10, keeps the claim at or below its sources):
```
DEGREES-BY-PRIME   [T]  sqrt5 at zeta_5, sqrt2 = m_8 + m_8^-1 and i = m_8^2 at zeta_8
Z2-PLACES-SPLIT    [T]  the two places, 5 = (2 + i)(2 - i)
SILVER-SIBLING     [D]  m_8 = zeta_8 = sqrt(i) at prime 2, silver unit 1 + sqrt2 norm -1
SILVER-RING-FACTS  [C]  F_25 = F_5(sqrt2), tau = sqrt(J), ord(tau) = 8
J-UNIT             [T]  N(J) = 1
J-MODULUS-CHORD    [T]  phi facts in Q(sqrt5)
```
Internal source (sealed v184, keeps public <= internal):
```
v184 Part XIII   rapidity ln phi, Fibonacci/Lucas parity of the boost ladder
v184 Part XIV    the qubit and the magic boundary, native prime 5 vs foreign prime 2
SS-MN            the silver sibling (m_8 = zeta_8, delta = 1 + sqrt2, sqrt(i) as sqrt of axiom)
T-PRIME-SPLIT-READING [T-LOCK, v133]  the reading splits by prime, quadratic -> 2
```

## 7. Exact edits the fold would make

FRONTIER.md: no manual edit. It is generated from REGISTRY.tsv and lists only live H and
O rows; METAL-TRACE-CASCADE is a T row and does not appear.

REGISTRY.tsv: add one row (tab-separated, six columns; falsifier column empty for a T row):
```
METAL-TRACE-CASCADE	T	gold and silver as the two roots of x^2 = t x + 1 with integer trace t, gold t = 1 (phi^2 = phi + 1) and silver t = 2 (delta^2 = 2 delta + 1), both units of norm -1; disc = t^2 + 4 gives 5 and 8 with the ramified prime dividing its own discriminant (5 | 5, 2 | 8); growth is Fibonacci phi^n = F_n phi + F_(n-1) for gold and Pell delta^n = P_n delta + P_(n-1) for silver; the silver pure form 1 + m_8^2 = 1 + i = sqrt2 m_8 = sqrt(2i) has (1 + i)^2 = 2i, amplitude sqrt2 = m_8 + m_8^-1, phase pi/4, and N_{Q(zeta_8)}(1 + i) = 4 is not a unit while N(J = 1 + zeta_5^2) = 1 is; scope t in {1, 2}, the trace-to-field map is not injective for general t (t = 4 also lands in Q(sqrt5))	4. The two places	reproduce/metal-trace	
```

CANON.md: append this paragraph at the end of section 4 (The two places), immediately
before "## 5. The force is the curvature":
```
The two places are the two simplest metals, and one integer names each. Write the
golden and silver ratios as the two roots of x^2 = t x + 1 with integer trace t; gold
is t = 1 with phi^2 = phi + 1, silver is t = 2 with delta^2 = 2 delta + 1, and both are
units of norm -1 (METAL-TRACE-CASCADE [T], reproduce/metal-trace). The single integer t
fixes the metal. Its discriminant is t^2 + 4, so gold carries 5 and silver carries 8,
and the ramified prime of each metal divides its own discriminant (5 | 5, 2 | 8); the
two places of DEGREES-BY-PRIME [T] and Z2-PLACES-SPLIT [T] are exactly the ramified
primes of these two laws. Its growth is the metal's own integer recurrence: the
Fibonacci law F_(n+1) = F_n + F_(n-1) with phi^n = F_n phi + F_(n-1) for gold, and the
Pell law P_(n+1) = 2 P_n + P_(n-1) with delta^n = P_n delta + P_(n-1) for silver. The
silver pure form is the doubling atom sqrt(2i): 1 + m_8^2 = 1 + i = sqrt2 m_8 has
(1 + i)^2 = 2i, amplitude sqrt2 = m_8 + m_8^-1 and phase pi/4, and it is not a unit,
N_{Q(zeta_8)}(1 + i) = 4, in contrast with the golden pure form J = 1 + zeta_5^2, which
is a unit, N(J) = 1 (J-UNIT [T]). The mirror of the axiom carries over letter by letter,
m_8 = delta (m_8 / delta) against j = phi J (SILVER-SIBLING [D]). The trace-to-field map
is not injective for general t, so the claim is scoped to the two simplest metals
t in {1, 2}, whose fundamental discriminants are 5 and 8; any physical reading of this
split as a reversible run against an irreversible record is a separate dictionary
reading and is not asserted here.
```

reproduce/: add C-METAL-TRACE-1_verifier.py as the reproduce/metal-trace target, wired
into the repository verification harness (section 19).

CHANGELOG.md: add one entry recording the v10 -> v11 fold and the new claim.

STATUS.md and canon/SHA256SUMS: this is a normative-file change, hence a sealed
integer-versioned fold. Bump CANON to Public Canon v11; recompute and update
CONTENT_COMMIT, CANON_SHA256, CANON_BYTES in STATUS.md and the five hashes in
canon/SHA256SUMS. The new hashes are produced by the fold in-repo, not in this proposal.

## 8. Validation gate (public probe protocol, not done here)

One named public session against mathorn1973/twist-j under POLICY.md and AGENTS.md:
claim METAL-TRACE-CASCADE in an issue; branch probe/metal-trace, path probes/metal-trace/;
push PREREG.md and verify.py (the verifier of record), record commit and file SHA-256;
run on two architectures byte-identical (aarch64 local with neutral public environment
fields, and the GitHub x86_64 check at PR time); record EXPECTED.txt, RUN.md, RESULT.md;
then fold. This session supplies the x86_64 leg (Python 3.12.3); the aarch64 leg is the
one remaining obligation before T is earned.

## 9. Currency stamp (Step 0, this session)

```
Public Canon v10 ACTIVE; AUTHORITY mathorn1973/twist-j main; tag canon-v10; cutover 2026-07-13
CONTENT_COMMIT  817275c4ef460d2d500a947db34c975baa651c40
CANON_SHA256    8884b598ddbc785d31f57dac57c093c3cb215f160a99c06012c8254a767623a2  (70397 bytes)
canon/SHA256SUMS  5 of 5 OK (CANON.md, CORE.md, FRONTIER.md, REGISTRY.tsv, CHANGELOG.md)
verified against the repository this session
```

## 10. Security

All artifacts are standard-library Python and markdown: no secrets, API keys, .env
files, private hostnames, machine nicknames, private logs, or binary models. Commit as
A. M. Thorn <thorn@twistj.com>.
