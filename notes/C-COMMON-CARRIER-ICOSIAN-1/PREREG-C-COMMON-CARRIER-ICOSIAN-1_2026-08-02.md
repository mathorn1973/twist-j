# PREREG C-COMMON-CARRIER-ICOSIAN-1

NON-CANONICAL. Incubation-lane preregistration, not a public probe.
Recorded before the recorded run legs of this bundle.

```text
CANDIDATE  C-COMMON-CARRIER-ICOSIAN-1
DATE       2026-08-02
OWNER      claude incubation session 2026-08-02
TARGET     the icosian ring as one carrier of the public A5 (via 2I),
           the J-step, and the canonical CM-Hermitian form; the ramified
           glue and the integrality of the loxodromic tick
BASIS      Public Canon v30, STATE ACTIVE, AUTHORITY mathorn1973/twist-j
           main, TAG canon-v30, CONTENT_COMMIT
           857223fcd5e7bc8c8e68f1df768d6e8222b24ee0, CANON_SHA256
           2a32dcbd61ee7792fc2cb990b7f223e08876d71bf7ddcf5ec432acd055f3986a,
           CANON_BYTES 157167, SHA256SUMS 5 of 5 OK, tag and content
           commit verified ancestors of origin/main this session
```

## Equation and claim set

Frozen as the numbered claim set of C-COMMON-CARRIER-ICOSIAN-1.md,
sections 1 through 5, pinned one-to-one by the 45 gates of the verifier
and the 6 refuted-break gates of the breaker. Headline exact statements:

1. h(x,y) = pi_K(x ybar) on B = K + K e is Hermitian, definite; right 2I
   h-unitary; left K h-similitude (J multiplier 2 - phi); actions commute.
2. O = Z[q].1 + Z[q].omega free; [O : Z[q].1 + Z[q].e] = 5 at
   p5 = (q - q^4) for every admissible e; h(O,O) in p5^-1 Z[zeta5].
3. diag(D1, D2) preserves O iff res_p5(D1) = res_p5(D2) in F5;
   res(J) = 2 = J_lambda; the integral even tick is diag(J, -J^-1) with
   phase 1 - J (the registered tenth root); no F-rational half tick:
   nrd(y) = +-phi^-1 fails total positivity; K(sqrt J) = K(sqrt phi).
4. Tr_{F/Q}(phi trd(x ybar)/sqrt5) makes O the E8 lattice; untwisted
   determinant 5^4.
5. rho (right action in the free basis) is an integral Z[zeta5] model of
   2I with the same (order, trace) class function as COLOR-INTEGRAL-LIFT,
   hence GL2(K)-conjugate; class of q = registered 5a; conjugation
   3-space = canon row 3a; residue 5a/5b labels are basis gauge.

## Code

```text
verify_common_carrier_icosian.py
  sha256 fd02057af557cbd61ed26983e486bfee023082cd40c72c20387f32508d63e016
  27672 bytes, 45 gates
break_common_carrier_icosian.py
  sha256 7db04e4accd6a69ead7d02c73079e235f2da432f8f4d851c357eb8d2728667c5
  8185 bytes, 6 gates
```

Python 3 standard library only, exact arithmetic (Fraction over Q(sqrt5),
Q(zeta5), integer lattices), fully deterministic, no randomness, no
tolerance anywhere.

## Carrier and data

Exact synthetic objects only: the 120 icosians generated in exact golden
arithmetic; no external data, no floats, no sampling.

## Systematics

Deterministic picks are frozen inside the gates: q = smallest icosian of
order 5 with trd = phi - 1 (unique class, Q5); e = smallest pure
inverting icosian; omega = (1+i+j+k)/2 fixed. The residue sweep family
{+-q^a, +-q^a J} (400 ordered pairs) is frozen in gate T3.

## Failure thresholds

Any FAIL line of either script fires the named falsifier F-ICO-1 or
F-ICO-2 of the claim doc; both scripts must exit 0 with empty stderr.
No numeric thresholds exist (exact arithmetic only).

## Action layer

L4 support-level structure (carrier, order, group actions, lattice glue),
with one L4-to-L1 corollary chain (tick integrality). No L5 stream, no
L6 measure, no lift between layers is claimed; COLOR-MEASURE-SELECTION
and QUADRATIC-DECODER-DATA remain untouched open rows.
