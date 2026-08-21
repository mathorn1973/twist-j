# C-CASIMIR-COEFFICIENT-1, RESULT [C / R] — NON-CANONICAL, NO AUTHORITY

Incubation lane, this project. Claimed, preregistered, executed and broken in
one session, 2026-07-28. Promotes nothing. Edits no registry.

Basis (currency gate, verified in-session): Public Canon v25, STATE ACTIVE,
AUTHORITY mathorn1973/twist-j main, TAG canon-v25 (ancestor of main),
CONTENT_COMMIT b914755b422bf79a8be637993b2edaa12a4333f8 (ancestor of main),
CANON_SHA256 53fa5acc9f2d910b26293d5152d93deac6596abd012997c7ff195397d9e476bb,
CANON_BYTES 136831, canon/SHA256SUMS 5 of 5 OK. The internal line
mathorn1973/twistj-jam was NOT reachable from this session; the v184 pin is
assumed, not verified, and nothing here rests on it.

Prior art disclosed at preregistration: the owner had previously explored a
Casimir reading of the coefficient 240 along a zeta_5 to 2I / A_5 path. That
exploration was in neither Canon, nor the public registry, nor this project.
This lane was opened to decide it, not to confirm it.

## Verdict, first

```
EXACT, survived        pi^2/240 = p L / (d(d+1))              [C]
                       pi^2/720 = zeta(2) zeta(-3)            [C]
                       zeta(-3) = 1/(p(p^2-1)) at p = 5       [C, p=5 only]
                       d = p-2 => D = p-1 => p | denom(B_D)   [C, family]
BROKEN                 "the letters are forced"               [R] F4 fired
BROKEN                 "240 is 2 |2I|"                        [R] F3 fired
NOT CLAIMED            any derivation of the Casimir effect, any force, any
                       length, any SI quantity, anything touching
                       METRO-EDGE-SCALE
```

The arithmetic is exact and reproduces on two architectures. The reading does
not survive its own control. That is the result.

## What was frozen before computing

Preregistration `claude/PREREG-C-CASIMIR-COEFFICIENT-1.md`, six fields plus
falsifiers F1 to F5, plus Amendment 1 (written before first execution, adding
the cyclotomic family gate G3b that the original G3 would have missed) and
Amendment 2 (disclosed, implementation only, after the first pinned verifier
FAILED; see below). Author's scratch expectation was disclosed in the prereg
and bound nothing: it predicted G1 and G2 pass, G3 fail, G5 return
multiplicity two or more. All three came true.

The decisive gates were written to kill, not to confirm:

```
G3  family scan: does the identification extend over d, or is it a d = 3
    accident? Threshold frozen: a structural family must hold for at least
    three consecutive d.
G5  search-space control: how many ways does the frozen Canon integer set S
    hit the target ratio 5/12? Threshold frozen: multiplicity >= 2 caps the
    reading at R.
G6  scope guard: the verifier asserts that no SI quantity, no length and no
    plate separation appears anywhere in its own output.
```

The integer set S (36 members) was frozen in the prereg before any count and
was not grown afterwards.

## The exact content

Canon inputs, all already sealed, none re-derived: p = 5, d = 3,
L = Re Li_2(J) = pi^2/(2p)^2 = pi^2/100 (Stone 2, LOCK), rho_0 = 1/6
(SS104, T-LOCK), |2I| = |SL(2,F_5)| = p(p^2-1) = 120 (T-COLOR-CORE-2I),
(V,F,E) = (2(p+1), p(p-1), p(p+1)) = (12,20,30) (T-VFE-PRIME),
k = d(d+1) = 12, D-TT-VECTOR-DOUBLET for the polarization 2.

External import, labeled as import everywhere it appears: ideal parallel
perfect conductors, zero temperature, massless EM field,
E/A = -pi^2 hbar c/(720 a^3), F/A = -pi^2 hbar c/(240 a^4); massless scalar
with Dirichlet boundary conditions is exactly half of each.

```
C1   pi^2 / 240 = p L / (d (d + 1))         EXACT in Q[pi^2]
C2   pi^2 / 720 = rho_0 pi^2 / |2I| = zeta(2) zeta(-3)    EXACT
C3   zeta(-3) = -B_4/4 = 1/(p(p^2-1)) = 1/120 at p = 5    EXACT
C4   denominator(B_4) = 30 = p(p+1), and equals the von Staudt-Clausen
     product over primes q with (q-1) | 4, whose prime set is exactly
     {2, 3, 5} = {2, d, p}                                EXACT
```

Both routes to zeta(-3) agree exactly: the direct route -B_4/4 and the
reflection route 2 (2pi)^-4 cos(2pi) Gamma(4) zeta(4).

## The one family that holds, and why it is still not evidence

Amendment 1 named it and it passed:

```
In Canon d = dim ker(Tr_(p-1)) = p - 2, because the degree of Q(zeta_p) over
Q is p - 1 and the trace kernel drops one dimension. Hence the spacetime
dimension is D = d + 1 = p - 1. Von Staudt-Clausen says the denominator of
B_D is the product of primes q with (q - 1) | D. Since (p - 1) = D divides
itself, p DIVIDES denominator(B_(p-1)) necessarily.

Verified for p in {3, 5, 7, 11, 13, 17, 19, 23}: 8 of 8.
At p = 5: d = 3, D = 4, denominator(B_4) = 30 = 2 . 3 . 5 = 2 . d . p.
```

That is theorem-shaped and it is not a fit. But the breaker measured its
evidential value and it is zero for the purpose at hand: the statement holds
for EVERY prime, so it separates no prime. Verified on the first twelve
primes, 12 of 12. It says the prime must appear in the Casimir constant of a
cyclotomic program; it does not say which prime, does not fix 240 against
720, and at p = 5 it is a postdiction of a known integer. It is a corollary
of von Staudt-Clausen wearing Canon letters.

## The break, by an independent code path

`claude/break_casimir_coefficient_1.py`. Independent of the verifier at every
step where independence is possible: Bernoulli numbers by the
Akiyama-Tanigawa triangle rather than the binomial recursion; Bernoulli
denominators constructed from von Staudt-Clausen rather than read off a
Fraction; the coefficient rebuilt from the mode-sum side rather than copied
from the published value. 13 of 13.

```
BREAK1  the shape class. The verifier searched only a L / b (8 hits).
        Widening to the shapes a/(b c) and (a b)/c over the same frozen S
        gives 123 and 86 more. TOTAL 217 hits of the target 5/12.
        The C1 identity is a REWRITING. Evidential weight zero.
BREAK2  the G3b family holds for all 12 tested primes, hence separates none.
BREAK3  240 admits seven Canon-flavoured readings: 2|2I|, the E8 root count,
        2^4 . 3 . 5, 16 . 15, 4|A_5|, 8 . icosahedral edges, d(d+1) . faces.
        No reading is forced.
BREAK4  the sharper statement (von Staudt-Clausen prime set exactly {2,3,5})
        holds at D = 4 AND D = 8. D = 4 is the smallest, not the only one.
```

## Two-platform gate

Byte-identical stdout on both fleet legs, exit 0, 20 of 20 gates:

```
Linux aarch64 leg    aarch64  Python 3.12.3
Linux x86_64 leg  x86_64   Python 3.13.5
```

## Pins

```
prereg    f12075734094094f0a6a1cc3cf88d190e0b2d1175a045899eab0b537a9eff91f
verifier  02c78f742813e1afdf83ba60cd6f1bff73fd8835f287bf8df28ba44dba5e2595
stdout    d599e8d1361e5238fc16f274b0a732bfa7c0ad9dd4fd186f4592ebd4a6ed2420
          3561 bytes, byte identical on aarch64 and x86_64
first pin 956f083dee04092565ea7c3116d971ccad78f9c3b57a8e514373b111fb03657c
          FAILED at G3a and is RETAINED as evidence: it asserted "exactly one
          hit", which is stricter than the preregistered threshold "at least
          three consecutive d". The failure was real: denominator(B_8) = 30
          as well as denominator(B_4) = 30, so the count is two, not one.
          Amendment 2 replaced the assertion with the preregistered threshold.
          No gate semantics, no falsifier and no threshold were changed.
breaker   39e22d650c265b8d700f1c17fa16509972744ec6a5dc4dfa6acacb85b95879c5
brk stdout 86969207e1ac7efcd58dfa34eb23969b3adceba005359dfe0d9532d67324985b
          2126 bytes
```

Environment on every leg:
`LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC`.
Python standard library only. Fraction and int. No float in any assertion.
pi carried as a formal symbol with an integer exponent.

## What survives, and the named successor

One equation survives with content rather than as a rewriting:

```
pi^2 / 720 = zeta(2) . zeta(-3)      exactly
```

The Casimir constant is a product of two zeta values. TWIST-J already derives
ONE of them dynamically rather than by inspection: T-BASEL-TM-GATE gives
zeta(2) = pi^2/6 with the six as the clock density f_00 = 1/6, the same six
as the gyron density rho_0, and D-BASEL-CLOCK-OBSERVABLE reads the mechanism
as the clock RAISING the polylogarithm weight by one at unit argument.

So the live question is not whether 240 is twice 120. It is whether the
Basel gate iterates. Named, not opened, no authority, no prereg:

```
C-BASEL-WEIGHT-4-1   does the TM clock gate lift weight 2 to weight 4, i.e.
                     produce zeta(4) = pi^4/90 as it produced zeta(2) = pi^2/6
    falsifier        if a second application of the gate at any declared gate
                     structure fails to produce 1/90 as relative content, or
                     produces it only for a density chosen after the fact, the
                     lane dies and Casimir is written off the programme
    why it matters   if the gate iterates, the Casimir constant is a
                     consequence of the clock; if it does not, the constant is
                     an import and 240 stays a coincidence with seven readings
```

## Non-claims

No derivation of the Casimir effect. No force. No length, no plate separation,
no SI quantity, no lattice constant for J. METRO-EDGE-SCALE untouched and
still open. No public registry row proposed. No promotion of any kind.
