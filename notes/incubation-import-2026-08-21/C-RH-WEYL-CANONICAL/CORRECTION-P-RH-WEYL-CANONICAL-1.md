# CORRECTION P-RH-WEYL-CANONICAL-1

```text
STATUS:      NON-CANONICAL CORRECTION RECORD, no authority
DATE:        2026-08-20 (UTC)
TRIGGER:     owner review of PR #6, four findings. Each finding is
             audited below against the pinned bytes and answered with
             evidence. Verdicts: E1 CONFIRMED and discharged, E2
             CONFIRMED (latent this run), E3 NOT REPRODUCED with an
             adjacent true defect found and recorded, E4 interpretation
             NARROWED, E5 rank-two threshold theory ADOPTED
             [candidate-T], E6 detection semantics fixed for successors.
PROTOCOL:    the pinned probe artifacts are NOT amended. Never amend a
             pinned branch. This record and breaker 1b are additive
             commits on the same branch. The recorded probe verdict
             (6 of 7 PASS, FW3 fired first-class, lane open with the
             detection claim dropped) STANDS.
FIREWALL:    no RH claim, no zeta claim. Model statements only.
             J7 SOURCE [O]. RH [O]. Public Canon v55 untouched.

PINNED ARTIFACTS (unchanged):
  PREREG-P-RH-WEYL-CANONICAL-1.md
    sha256 3530477a1c841795b9ab44b971d9d1e6324585ae4c7512f863e56d28f53e48fb
  verify_rh_weyl_canonical_1.py
    sha256 0b78aaf882fe32a1780162c9e356833596f966106582b94365c137150f99e5f1
  verify_rh_weyl_canonical_1.stdout.txt (3967 bytes, two legs)
    sha256 1f154a417b94cbb38f42a09eacff1c608df6b0a3009ffad39b6115daa266320a
  breaker_rh_weyl_canonical_1.py
    sha256 b0d1439016d65f5f9e7a3c8d020eea5dac18f00574a6d5ce1e3b8ca4abe0301e
  breaker_rh_weyl_canonical_1.stdout.txt
    sha256 cbe3f0da90148aa1b9cec5e761d4bdb8d8e2d56c94fe13dbbeb84d05b12a65a2

CORRECTION ARTIFACTS (new, this commit):
  breaker_rh_weyl_canonical_1b.py (10295 bytes)
    sha256 f3764bad6f60812234f1d56f1cfe1037fe3ac3556c8b7aa029096e65423d0574
  breaker_rh_weyl_canonical_1b.stdout.txt (3908 bytes)
    sha256 da3cf5c17e974e109ac210614ec781e94c1a725f6b8fff2854058bebaa66a3e3
    single leg Linux x86_64 CPython 3.11.15, env LC_ALL=C LANG=C
    PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC, FINDINGS: 0.
    Breaker class, no authority, floats never gate; every identity it
    asserts is checked in exact Q(i) or Q(sqrt 3) arithmetic and the
    float columns are witnesses only.
```

## E1. The promised FW5 never ran. CONFIRMED, now discharged.

The prereg (Field 2) promised in the breaker an "independent
recomputation of the moment table by float resolvent powers (FW5
check)", and FW5 reads "any exact Taylor-coefficient value at c = 2
whose certified enclosure disagrees with the independent breaker path."

What the pinned breaker actually did (breaker_rh_weyl_canonical_1.py,
section B3): central finite differences of the closed LIMIT function
m_inf(z) = 2(-z + sqrt(z^2 - 1)) at z = 2, compared against the limit
coefficients. It never recomputed any finite-R moment
e1^T (J_R - c)^{-(k+1)} e1. The finite side of FW5 therefore had an
empty comparison: CHECK 5's finite-moment table was verified by one
code path only (the verifier's tridiagonal Thomas solve). The reviewer
finding is CONFIRMED.

Discharge, breaker 1b section C1. Independent path: dense Gaussian
elimination with partial pivoting over exact Fraction (structure-blind,
no tridiagonal shortcut), plus a dense float LU witness, on the same
matrices (J_R - 2), moments by repeated solves, R in {4, 8, 16, 32, 64},
k <= 6, 35 rows. Limit side recomputed independently in Q(sqrt 3) with
its own certified bracket (integer sqrt of 3 * 10^80). Results:

```text
dense-exact vs dense-float witness: relative gap <= 2.2e-16 over all
  35 (R, k) rows (float column is a witness, never a gate).
exact distance of the dense-exact moments to the independent Q(sqrt 3)
  limit enclosure: decreasing in R at fixed k; at R = 64 all seven
  values < 2e-40. This independently re-derives the pinned CHECK 5
  verdict (threshold < 1e-30 at R = 64) by a disjoint exact code path;
  it does not read the pinned values, it recomputes the certified
  quantities and re-earns the verdict.
```

FW5 verdict: the pinned CHECK 5 table survives its first real
independent attack. FW5 did not fire. [candidate-C at the frozen
ranges]

## E2. Decision-tree defect. CONFIRMED, latent in the recorded run.

The pinned verifier's verdict logic (lines 381 to 397) is exactly:

```text
fw2 = not (CHECK 3 and CHECK 4)     # gate machinery
fw4 = not CHECK 1                   # dictionary
no failure        -> "T2 LANE OPEN"
fw2 or fw4        -> "[F-bounded, T2 INSTRUMENTS]"
any other failure -> "lane opens with dropped claims"
```

A failure of CHECK 0 (enclosure certificates), CHECK 2 (normalization)
or CHECK 5 (moment convergence) falls into the last branch and would
have printed a lane-opening verdict while a foundation instrument was
broken. The reviewer finding is CONFIRMED.

Root cause is upstream of the code: the prereg's frozen stop-gate
paragraph assigns actions only to FW2, FW4 and FW3. FW1 (CHECK 0 or
CHECK 2) is declared as "fires the probe" with no frozen verdict
action, and FW5 has none either. The pinned code faithfully implements
the incomplete frozen text. Two mitigating facts, stated exactly: the
process exit code is 1 on ANY failed check, so no such run could have
passed silently; and in the recorded run the only failed check was
CHECK 6 (FW3), which is precisely the case the last branch was written
for. The defect was latent. The recorded verdict stands.

Correction, binding for every successor probe in this lane (the pinned
verifier is not amended):

```text
The lane opens if and only if the ONLY failed gates are the designated
droppable detection gates of that probe's prereg. Any failure among
the instrument gates (enclosures, dictionary, normalization,
Herglotz/Pick PSD, node convergence, moment convergence) is
[F-bounded, T2 INSTRUMENTS], regardless of which named firewall it
maps to. Every firewall named in a prereg must carry a frozen verdict
action, and the verifier's branch structure must cover every firewall
by name, with the instrument-failure branches tested before the
droppable-claim branch.
```

## E3. "D2 listed twice in the verifier." NOT REPRODUCED. Adjacent true defect found.

Audit of the pinned bytes (sha 0b78aaf8...): the frozen defect list
(lines 238 to 242) is

```text
DEFECTS = [
    ("D1", (1/3,  1/10),  1/10,  True),
    ("D2", (9/10, 1/10),  1/10,  False),
    ("D3", (1/3,  1/100), 1/100, False),
]
```

with exactly one D2 row; the DETECT output line (line 374) is a single
generic print executed once per defect; the pinned stdout carries
exactly one DETECT line for D2. The duplication is not reproduced at
source level or output level.

The same audit found the plausible source of the reading, and it is a
real defect: the banner at lines 249 to 250 prints "detection eps in
{1/10, 1/100}". No parameter named eps exists anywhere in the
detection path. The name is a leftover from the discarded rank-one
i*epsilon defect design that the prereg replaced with the conjugate
pole-pair defect before the pin; the values it prints are actually the
defect WEIGHTS w, and the weight set appears once in the banner and
again inside the DEFECTS list, which reads as a double count. The
banner is cosmetic, feeds no computation and no gate. Recorded as an
erratum of the pinned verifier; not amended, per protocol.

## E4. "Bulk masking" narrowed to "insufficient depth at N = 8".

The pinned RESULT read the fired FW3 as: a defect over the spectral
bulk "stays masked", consistent with a finite-span obstruction (C11).
That reading was too strong, and the rank-two threshold theory (E5)
plus the owner's exact computations replace it:

```text
Exact thresholds at N = 8 on the frozen chain (breaker 1b, C2,
enclosed by exact-sign bisection of the block quadratic):
  D1 (mu = 1/3 + i/10,  w = 1/10):   w* = 0.170975...  w < w*: no
      negative direction exists inside N = 8 at all. Non-detection was
      forced, not noisy.
  D2 (mu = 9/10 + i/10, w = 1/10):   w* = 0.018003...  w > w*:
      detection required; recorded N* = 6 agrees.
  D3 (mu = 1/3 + i/100, w = 1/100):  w* = 21.4172...   w << w*.
Owner-reported deeper landscape (owner computation, recorded here as
reported, to be frozen as qualitative predictions in the successor
prereg): D1 on the original chain reaches N* ~ 11; a range-matched
spread also ~ 11; lower-shifted node windows 9 to 10.
```

Narrowed reading, binding on how this lane cites FW3: FW3 at N = 8
demonstrated INSUFFICIENT DEPTH of the frozen 8-node design for the
bulk defect D1, not permanent masking of bulk defects. What stands as
data from the pinned run: detection at fixed N = 8 is
defect-position-dependent (edge defect caught at 6 of 8, bulk defect
threshold 1.71x above the frozen weight). Whether bulk-defect
detection depth grows without bound as delta shrinks remains exactly
the C11 question; this probe established nothing about it. The
successor probe P-RH-WEYL-CANONICAL-2 maps w*(x, delta; design, N)
exactly to N = 24.

## E5. The rank-two threshold theorem. ADOPTED [candidate-T].

Owner derivation, independently re-derived in this session and
machine-verified exactly in breaker 1b C2. This replaces weight
scanning as the lane's detection instrument.

Setting: distinct nodes z_1..z_N in the upper half plane, Q Herglotz
with Pick matrix P0 > 0, P0_{jk} = (Q(z_j) - conj Q(z_k))/(z_j -
conj z_k). Conjugate pole-pair defect with pole mu = x + i delta,
delta > 0, weight w > 0:

```text
Q_w(z) = Q(z) + w ( 1/(mu - z) + 1/(conj mu - z) )
```

(i) Rank-two structure. With A_j = 1/(mu - z_j), B_j = 1/(conj mu -
z_j), the kernel identities

```text
(A_j - conj B_k)/(z_j - conj z_k) = A_j conj B_k
(B_j - conj A_k)/(z_j - conj z_k) = B_j conj A_k
```

give exactly P(w) = P0 + w (A B* + B A*). The defect moves the Pick
matrix by a rank <= 2 symmetric update, for every N at once.

(ii) Determinant law. With alpha = A* P0^{-1} A > 0, beta = B* P0^{-1}
B > 0, gamma = A* P0^{-1} B (the convention the machine check uses;
only Re gamma and |gamma| enter, so the transpose convention changes
nothing), D = alpha beta - |gamma|^2:

```text
det P(w) / det P0 = 1 + 2 w Re(gamma) - w^2 D
```

(2x2 reduction on the span of P0^{-1}A, P0^{-1}B). D >= 0 is
Cauchy-Schwarz in the P0^{-1} inner product, with D = 0 iff A and B
are parallel (degenerate case, the law is then linear in w).

(iii) Single threshold. For D > 0 the quadratic has exactly one
positive root

```text
w* = ( Re(gamma) + sqrt( (Re gamma)^2 + D ) ) / D
```

positive even when Re(gamma) < 0 (D2 above is exactly this case:
Re(gamma) = -8.875..., detection still occurs because D is large).
Below w* the determinant ratio is positive, at w* it vanishes, above
it is negative.

(iv) Block structure and N*. Each leading principal m-block obeys its
own quadratic with block quantities alpha_m, beta_m, gamma_m, D_m and
threshold w*_m. By Sylvester, P(w) > 0 iff every block quadratic is
positive, i.e. iff w < min_m w*_m; and the first m whose quadratic
goes negative is the first negative LDL* pivot, so N*(w) = min { m :
w > w*_m }. Detection decisions at rational w are SIGN EVALUATIONS OF
RATIONAL QUADRATICS, sqrt-free and exact; w* itself needs only an
enclosure.

(v) At most one negative direction. From A B* + B A* = (1/2)[ (A+B)
(A+B)* - (A-B)(A-B)* ] >= -(1/2)(A-B)(A-B)*, we get P(w) >= P0 -
(w/2)(A-B)(A-B)*, a rank-one downward perturbation of a positive
matrix; by eigenvalue interlacing P(w) has at most one negative
eigenvalue for every w. Crossing w* creates exactly one negative
direction, never a cascade.

Machine verification (breaker 1b C2, exact over Q(i), N = 8, R = 64
background): for each frozen defect D1, D2, D3 the identity det
P(w)/det P0 = 1 + 2 w Re(gamma) - w^2 D holds EXACTLY at three
rational w values against a direct exact determinant; alpha, beta are
real and positive; D >= 0; the full-block quadratic sign at the frozen
weight reproduces the pinned detection outcome in all three cases; the
w* enclosures are the E4 table. FINDINGS: 0.

Status: [candidate-T] for the theorem statements (i) to (v) (finite
linear algebra with complete proof, machine-checked instances), inside
the incubation lane, no public authority.

## E6. Detection semantics and scope, binding for successors.

```text
1  Detection means a STRICTLY negative direction: block quadratic < 0,
   equivalently an exact LDL* pivot < 0. A zero value means w = w*_m
   exactly, the boundary; recorded as boundary, never as detection.
   (The pinned verifier's CHECK 6 used p <= 0; immaterial in the
   recorded run since D2's pivot was strictly negative and D1, D3 had
   none, but the semantics are fixed henceforth.)
2  Every result is restricted to the frozen node designs, defect grid
   and N range of its prereg. For every finite design and every defect
   position, w* > 0: no finite node design detects all arbitrarily
   weak defects. Uniform-detection claims are out of scope by
   construction, at every N.
```

## Consequence for the lane

Obligation O5 of the pinned RESULT is re-specified: not a weight-scan
landscape, but an exact w*(x, delta; design, N) map by block
quadratics, four frozen designs (original chain, range-matched spread,
shifted window, one-point derivative Hankel), N to 24, with the
owner-reported N* values frozen as qualitative predictions. That is
P-RH-WEYL-CANONICAL-2, to be pinned only above this correction.

End of correction record.
