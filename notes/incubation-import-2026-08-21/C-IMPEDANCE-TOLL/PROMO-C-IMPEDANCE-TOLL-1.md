# PROMO-C-IMPEDANCE-TOLL-1

Promotion proposal. One document a fold can consume without reading anything
else. It carries no authority and promotes nothing by itself.

Basis, verified in the session that produced this package: Public Canon v25,
STATE ACTIVE, AUTHORITY mathorn1973/twist-j main, TAG canon-v25 and
CONTENT_COMMIT b914755b422bf79a8be637993b2edaa12a4333f8 both ancestors of
main, CANON_SHA256 53fa5acc9f2d910b26293d5152d93deac6596abd012997c7ff195397d9e476bb,
CANON_BYTES 136831, canon/SHA256SUMS 5 of 5 OK.

The internal line was NOT reachable from that session. Nothing in this
proposal cites it, and nothing in it needs to: every row below is proved by
the accompanying public probe or is an identity of declared definitions.

## 1. What is proposed, and at what status

```
OMEGA3-UNIQUE                    T   new
TOLL-BISECTOR-ROOT               T   new
IMPEDANCE-DEFINITIONAL-IDENTITY  T   new
IMPEDANCE-TOLL                   D   new
IMPEDANCE-CHANNEL-COUNT          O   new, with falsifier
```

Nothing existing changes status. No LOCK is touched. No row is retired.

## 2. Why the shape is this shape

The obvious move would have been a single row saying that the ratio of the
two constants is 2 alpha. That row would be wrong to publish, and this
proposal is built to make it impossible to publish it by accident.

```
Z_0 / R_K = 2 alpha is an IDENTITY of the standard definitions of alpha,
R_K and Z_0. It is true in any theory whatsoever. It predicts nothing.
```

So the proposal splits the object into four honest pieces and one honest gap:

```
the mathematics that is really new      OMEGA3-UNIQUE
the algebra behind the bisector         TOLL-BISECTOR-ROOT
the guard against overclaim             IMPEDANCE-DEFINITIONAL-IDENTITY
the reading that TWIST-J actually adds  IMPEDANCE-TOLL, at D
what the reading rests on and does not
  derive                                IMPEDANCE-CHANNEL-COUNT, at O
```

The load-bearing new mathematics is OMEGA3-UNIQUE, and it is a real theorem
with an infinite tail closed by a closed form rather than by a scan. The
reading IMPEDANCE-TOLL is what the programme contributes, and it is carried
at D because the two step counts p and 2p are inputs. That is registered as
an open obligation with its own falsifier rather than being smuggled into the
D row.

## 3. The exact statements

```
OMEGA3-UNIQUE
    Omega_d = 2 pi^(d/2) / Gamma(d/2), the surface measure of the unit
    sphere in R^d. Over the integers d >= 2,
        Omega_d / Omega_(d-1) = 2   if and only if   d = 3.
    Odd branch, d = 2m + 1: the ratio is the pure rational
        r(m) = 4^m m! (m-1)! / (2m)!,  r(1) = 2,
        r(m+1) / r(m) = 2m / (2m + 1) < 1 for every m >= 1,
    so r decreases strictly and reaches 2 only at m = 1. Even branch: the
    ratio is a nonzero rational multiple of pi, which equals 2 only if pi is
    rational. One external import, labelled: pi is irrational.

TOLL-BISECTOR-ROOT
    In Z[x]/(x^(2p) - 1) at p = 5, for every integer k,
        (x^k + x^(-k)) . x^k = x^(2k) + 1.
    The archimedean reading is 1 + e^(i theta) = 2 cos(theta/2) e^(i theta/2).

IMPEDANCE-DEFINITIONAL-IDENTITY
    With alpha = e^2/(4 pi eps_0 hbar c), R_K = 2 pi hbar/e^2 and
    Z_0 = 1/(eps_0 c), as monomials in the free abelian group on
    (e, eps_0, hbar, c, pi):
        Z_0 = 4 pi alpha hbar / e^2      and      Z_0 / R_K = 2 alpha.

IMPEDANCE-TOLL
    On the primitive scale arg J = 2 pi / p, a channel closing after p steps
    carries the cycle factor p (2 pi / p) = 2 pi and a channel closing after
    2 p steps carries 2 p (2 pi / p) = 4 pi. Reading R_K as one closure of
    the first kind and Z_0 as one closure of the second puts the ratio at
    2 alpha, with that 2 the same integer OMEGA3-UNIQUE makes available as a
    geometric closure step in exactly one dimension.

IMPEDANCE-CHANNEL-COUNT
    The derivation of the two step counts p and 2p on the public
    architecture from the primitive scale alone. Not asserted by any row of
    this fold.
```

## 4. The falsifier

Only the O row is live and only it needs one:

```
IMPEDANCE-CHANNEL-COUNT closes positively when both step counts are derived
on the public architecture from the primitive scale alone; closes negatively
when an exhaustive exact classification of admissible channel closures on
that scale yields a count pair other than (p, 2p) or yields more than one
admissible pair; STOP while the admissible class is incomplete.
```

## 5. The verifier and its pins

```
probe        probes/P-IMPEDANCE-TOLL-1
prereg       PREREG.md, six fields, falsifiers F1 to F7 frozen first
verifier     verify.py, Python standard library, Fraction and int only,
             no float in any assertion, no filesystem read or write, no
             network, no randomness, no clock
gates        11 of 11 PASS
verifier sha256   1cc710b8b9b4dcfb6ec3d9c94039dcf04a460a59fca6e193df6997d173de6700
stdout   sha256   d6f589a8e3097c677eaf217ac8e242359348e686c299286fea8db874afbeb0dc
stdout   bytes    2345
stdout   lines    36
stderr           empty, exit 0
leg 1        Ubuntu 24.04, aarch64, Python 3.12.3
leg 2        Debian 13,    x86_64,  Python 3.13.5
```

Two of the eleven gates exist only to stop the fold from overclaiming:

```
G08  asserts that the probe output itself names the step counts as an open
     obligation and the constant ratio as an identity
G09  asserts that no unit word, no measured value and no length word appears
     anywhere in the probe output
```

## 6. Dependency edges

```
IMPEDANCE-TOLL  requires  OMEGA3-UNIQUE                    (the toll integer)
IMPEDANCE-TOLL  requires  TOLL-BISECTOR-ROOT               (the bisector root)
IMPEDANCE-TOLL  bounded by IMPEDANCE-CHANNEL-COUNT         (the step counts)
IMPEDANCE-TOLL  requires  IMPEDANCE-DEFINITIONAL-IDENTITY  (the guard)
```

The three T rows and the guard stand alone. Nothing outside this fold depends
on any of them, so the fold is removable in one revert if it is ever wrong.

## 7. The exact edits the fold makes

They are applied by `apply_fold.py` in this package and are reproduced
verbatim in `fold-v26.patch`. Summary:

```
canon/CANON.md            one paragraph at the end of section 15, title to v26
canon/REGISTRY.tsv        five rows appended
canon/NORMATIVE.tsv       five rows appended
canon/EVIDENCE.tsv        five rows appended, four PUBLIC_PROBE, one INLINE_CANON
canon/HISTORY.tsv         five DECLARE events at release canon-v26
canon/FRONTIER_PROGRAMS.tsv  one row, QUANTUM_EM, ROOT, READY, FORMAL
canon/FRONTIER.md         regenerated by tools/generate_canon_views.py
canon/CORE.md             release identity to v26
canon/CHANGELOG.md        the v25 counts block frozen as CANON25, a v26 section
                          added, the current counts block regenerated
canon/STATUS_COUNTS.tsv   regenerated
canon/SHA256SUMS          regenerated
probes/P-IMPEDANCE-TOLL-1 new, five files
reproduce/status-separation  the registry partition literal and EXPECTED.txt
STATUS.md README.md CITATION.cff   the release form, v26, tag canon-v26
```

Registry after the fold: 213 claims; 0 T-LOCK, 113 T, 41 D, 22 C, 3 H, 24 O,
10 F; 27 live H and O.

## 8. Gate evidence, already run

Every repository gate was run against a full dry fold of the real repository
head. All pass:

```
tools/check_canon.py            CANON PASS v26 claims=213
tools/check_ledger.py           LEDGER PASS claims=213 items=229
                                dependencies=330 evidence=213 history=702
                                gates=10 programs=8
tools/check_policy.py           POLICY PASS
tools/check_status_labels.py    STATUS LABELS PASS
tools/check_activation.py       ACTIVATION PASS mode=active full=False
tools/check_verifier.py         VERIFY PASS P-IMPEDANCE-TOLL-1
tools/check_reproduce.py        REPRODUCE PASS status-separation
tools/generate_canon_views.py   CANON VIEWS PASS
```

## 9. Non-claims

No value in any unit system. No measured comparison. No length, no plate
geometry, no lattice constant for J. METRO-EDGE-SCALE untouched and still
open. No claim that the ratio of the two constants is a prediction. No claim
that the step counts are derived. No summary produced from this fold may
exceed the status or scope of the rows above.
