# P-METAL-TRACE-1 preregistration

Status: PRE-PIN DRAFT

This document defines the complete decision surface for the first public
attack on the metallic-trace cascade. It contains no gate output and earns
no scientific status. The formal gate must not run until this document and
the accepted verifier have been committed and pushed as the immutable
preregistration pin.

## Public identity

- Claim: `METAL-TRACE-CASCADE` (new claim id; no registry row exists yet)
- Candidate: `C-METAL-TRACE-1` (incubation lane)
- Public lock: issue 70
- Owner: one named session (issue 70)
- Branch: `probe/P-METAL-TRACE-1`
- Path: `probes/P-METAL-TRACE-1/`
- Initial base: `72a04e1e2dae8df66f170b169328611b75a8a1af`
- Action layer: L2, manifold / field arithmetic
- Target on promotion: Public Canon v10 fold to v11, section 4, The two
  places; the fold is a separate sealed change and is NOT part of this probe

## Provenance and prior pins

The five frozen fields below are carried from the incubation candidate
`C-METAL-TRACE-1`, whose artifacts were pinned before this probe opened:

```
PREREG_C-METAL-TRACE-1.md      sha256 2d8beb61055346a50b7b70802143550e8f78a920fb2c17bcd1e868a740a68f09  4509 bytes
C-METAL-TRACE-1_verifier.py    sha256 57501a2975ff71a43a1e5f98e7f976e35d27dd6252143fb5d20ce715375fff2a  4938 bytes
C-METAL-TRACE-1_break.py       sha256 f7feb2798eda1337f2e4b7da275bc29d1c1feb33f51a57c74219e132d6e55fb1  4657 bytes
```

The verifier of record is committed here byte-identical as `verify.py`
(same SHA-256 as the candidate pin; only the file name differs). The
independent break path is non-formal audit material and lives under
`notes/`, not in this probe directory. The prior explorations
(`verify_metals_deep.py`, `notes/metal-trace/verify_metal_trace.py`) are
non-formal and are not gates.

## Equation (frozen field 1)

Write the golden and silver ratios as the two roots of x^2 = t x + 1 with
integer trace t. Gold is t = 1 (phi^2 = phi + 1); silver is t = 2
(delta^2 = 2 delta + 1); both are units of norm -1. The single integer t
fixes the metal:

(a) disc(x^2 - t x - 1) = t^2 + 4, giving 5 for gold and 8 for silver; the
    ramified prime of each metal divides its own discriminant (5 | 5,
    2 | 8), so the two program primes are the ramified primes of the two
    simplest metallic laws.
(b) growth is the metal's own integer recurrence: Fibonacci
    F_(n+1) = F_n + F_(n-1) for gold with phi^n = F_n phi + F_(n-1), and
    Pell P_(n+1) = 2 P_n + P_(n-1) for silver with
    delta^n = P_n delta + P_(n-1).
(c) the silver pure form 1 + m_8^2 = 1 + i = sqrt2 * m_8 = sqrt(2i)
    satisfies (1 + i)^2 = 2i with amplitude sqrt2 = m_8 + m_8^-1 and phase
    pi/4, and is NOT a unit: N_{Q(zeta_8)}(1 + i) = 4; the golden pure
    form J = 1 + zeta_5^2 is a unit, N(J) = 1.

The run/record physical reading (combine vs copy, reversible run vs
irreversible write, the arithmetic seat of the arrow) is H and is NOT part
of this frozen claim.

## Code version (frozen field 2)

Verifier of record: `verify.py`, byte-identical to
`C-METAL-TRACE-1_verifier.py`,
sha256 `57501a2975ff71a43a1e5f98e7f976e35d27dd6252143fb5d20ce715375fff2a`,
4938 bytes. Python standard library only, exact arithmetic
(Fraction / integer cyclotomic), no floats in any assertion. Run from the
repository root with
`LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC`.

## Carrier (frozen field 3)

No external dataset. Q(sqrt5) and Q(sqrt2) as coordinate pairs; Z[zeta_8]
on the basis (1, m, m^2, m^3) with m^4 = -1; Z[zeta_5] on (1, j, j^2, j^3)
with 1 + j + j^2 + j^3 + j^4 = 0; Z[i] as Gaussian pairs; integer 2x2
companion matrices [[0,1],[1,t]] in the break path. Growth laws verified to
n = 11. Field norms taken over the stated field.

## Systematics (frozen field 4)

- The trace-to-field map is NOT injective for general t: t = 4 also gives
  Q(sqrt5) (disc 20, squarefree kernel 5). The claim is therefore scoped to
  the two simplest metals t in {1, 2}, whose FUNDAMENTAL discriminants are
  exactly 5 and 8. No all-t claim is made.
- Norm degree is stated explicitly: N(1 + i) = 2 over Q(i) and = 4 over
  Q(zeta_8); the (c) claim uses the degree-4 field norm.
- The growth identities are theorems stated for all n but verified here at
  finite n <= 11; the finite verification is the witness, not a claim that
  n <= 11 is the scope.

## Failure threshold (frozen field 5)

Exact and binary. The candidate fails if, on independent recomputation, any
assertion in the verifier of record is false, OR if the pinned verifier
stdout is not byte-identical across the two validation architectures
(aarch64 and x86_64). A single differing byte fires. No threshold is moved
after the fact.

## Explicit falsifier

If any of the frozen exact identities is false on independent
recomputation, for example disc(x^2 - t x - 1) != t^2 + 4 for t in {1, 2},
or N(phi) != -1, or N(delta) != -1, or (1 + i)^2 != 2i, or
sqrt2 * m_8 != 1 + i in Z[zeta_8], or N_{Q(zeta_8)}(1 + i) != 4, or
N(J) != 1, OR if the two-platform stdout of the pinned verifier is not
byte-identical, then the candidate is falsified and archived, not deleted.
The H reading is out of scope for this falsifier.

## Two-architecture plan

This session supplies the formal local leg on x86_64; the required GitHub
check reruns the pinned verifier on x86_64 `ubuntu-latest`. Same
architecture agreement is a reproduction, not a two-architecture gate, so
at pull-request time a computation-only claim stands at most at C. The
aarch64 local leg is the declared remaining step to the two-architecture
computation gate; following the P-KERNEL-CONNECT-ALL-K-1 precedent, it is
appended as a neutral leg record in `RESULT.md` without changing any
pinned file. Independent theorem-grade proof of the same identities may
establish T, with this verifier as its audit.
