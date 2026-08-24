# Bridge audit: the Fibonacci lane against the stuck photon kernel lift

```
SESSION:  audit-fib-photon-bridge-2026-07-27
STATUS:   AUDIT. NON-CANONICAL. No authority. Promotes nothing, adopts no
          lift, opens no branch, edits no public row.
QUESTION: how the Fibonacci modular tensor category relates to
          C-PHOTON-SPATIAL-SYMBOL-1 and to the UNTYPED predefinition result
          on P-KERNEL-LIFT-DERIVATION-1 (public issue #193).
BASIS:    claude/AUDIT-C-FIB-MTC-J-LOCK-1_2026-07-27.md,
          claude/DECISION-PROPOSAL-C-PHOTON-SPATIAL-SYMBOL-1_2026-07-27.md,
          claude/AUDIT-EXTERNAL-DECISION-PROPOSAL-PHOTON-SPATIAL-SYMBOL_2026-07-27.md
```

## 0. Currency and what is taken on report

Public head verified by fresh clone earlier this session: main ef1d2d91,
STATE ACTIVE, Public Canon v25, CONTENT_COMMIT b914755b, CANON_SHA256
53fa5acc, 136831 B, canon/SHA256SUMS 5 of 5 OK.

Issue #193 fetched: title "[V25 CLAIM] P-KERNEL-LIFT-DERIVATION-1 - canonical
trace-kernel lift", state OPEN, PREDEFINITION / NO FORMAL RUN AUTHORIZED, with
the frozen outcome vocabulary UNTYPED, EMPTY, NONUNIQUE, UNIQUE-A3,
UNIQUE-A5-LIFT, UNIQUE-OTHER. The comment body did not render through the
fetch, so the verdict UNTYPED is taken from the owner's report and from the
owner's statement that the public readback is verified. No probe branch, no
formal pin, no verifier run, no Canon change: consistent with what the fetch
shows.

## 1. Verdict, falsification first

```
CONFIRMED   the two lanes touch the same object, the order-5 structure over
            Q(zeta_5) and over F_5, from opposite sides of the ramified
            prime 5.
FIRED       the reading "the photon carrier contains A_5, therefore the
            icosahedral / golden / Fibonacci structure is in the kernel" is
            FALSE. The A_5 in O(F_5^3, q_bar) carries no golden data at all.
DECIDED     UNIQUE-A5-LIFT is not merely unreached. It is IMPOSSIBLE for every
            rank-3 integer lift, by the crystallographic restriction. The
            frozen vocabulary of issue #193 asks a rank-3 object a question
            that only a rank-6 object can answer, so UNTYPED is the correct
            and the only honest outcome available to it.
NAMED       the obstruction is exactly the irrationality of phi = d_tau, the
            Fibonacci quantum dimension. This is the connection, and it is a
            theorem, not an analogy.
BLOCKED     nothing here reopens PHIBIT-NOT-TAU [F]. No TWIST-J object is
            claimed to be a tau anyon.
```

## 2. What the Fibonacci lane already established (characteristic 0)

From claude/AUDIT-C-FIB-MTC-J-LOCK-1_2026-07-27.md, quoted, not re-derived:
the fusion rule tau tensor tau = 1 + tau plus modularity forces
theta + theta^-1 = -d and d^2 = d + 1, hence x^2 + phi x + 1 =
(x - zeta_5^2)(x - zeta_5^3), hence theta_tau in {zeta_5^2, zeta_5^3} and
1 + theta_tau in {J, conj J}. J = 1 + theta_tau is a DERIVATION. The four
modular categories on the golden ring carry spins {zeta_5^a}, so {1 + theta}
over the four is the full Galois orbit of J and N(J) = 1 closes it.

Its discriminator claim fired: p = 11 rival, SU(2)_9 at j = 2,
J_11 = 1 + zeta_11^6, LOCK exact, 10 of 10 Galois conjugates realised. Only
MINIMALITY survives. That fence stands and is not touched here.

The relevant structural point for this audit: every one of those facts lives in
characteristic 0, in Q(zeta_5) and Z[phi], where zeta_5 is primitive and
phi differs from -1/phi.

## 3. What the photon carrier is (characteristic 5), verified exactly

Nine gates, own code path, stdlib only, no float in any assertion.

```
G1  O(F_5^3, q_bar) has order profile {1:1, 2:51, 3:20, 4:60, 5:24, 6:60,
    10:24}, exactly that of Z_2 x S_5. The "240" is Z_2 x S_5 and the "A_5
    inside" is Omega_3(5) = PSL(2,5) = A_5, the generic isomorphism for odd q.
    It is present at q = 7, 9, 11 too, as PSL(2,q). No golden content.
G2  all 24 elements of order 5 satisfy (M - I)^3 = 0 and have trace 3. They
    are UNIPOTENT, not rotations. There is no zeta_5 eigenvalue.
G3  x^5 - 1 = (x - 1)^5 over F_5, and 5 divides no |F_5^k *|: a primitive
    fifth root of unity exists in NO field of characteristic 5.
G4  x^2 - x - 1 = (x - 3)^2 mod 5. phi and -1/phi COLLIDE at 3. The
    discriminant is 5 and it vanishes: the golden pair degenerates exactly at
    the prime the program is built on.
G5  characteristic 0: the traces of the two classes of icosahedral order-5
    rotation are exactly phi and 1 - phi = -1/phi, that is, the two roots of
    d^2 = d + 1, that is, the Fibonacci and the Lee-Yang quantum dimensions.
    Both reduce mod 5 to 3, the unipotent trace. Consistent, and the golden
    DISTINCTION is precisely what the reduction destroys.
G6  |Aut_Z| = 48 = 2^4 * 3 is exactly the 5'-part of 240 = 2^4 * 3 * 5. The
    integral point group is a Hall 5'-subgroup, Z_2 x S_4 inside Z_2 x S_5,
    and the index 5 is [S_5 : S_4]. The earlier "index 5 at p = 5, recorded
    as arithmetic, no claim" is now explained and can be retired as a curiosity.
G7  J - 1 = zeta_5^2 = theta_tau and (J - 1)^3 = zeta_5. Characteristic 0.
G8  x^5 - 1 = Phi_1 * Phi_5, deg Phi_5 = 4, irreducible over Q (no rational
    root, no integer quadratic factorisation). The only degree-3 cyclotomic
    characteristic polynomial is (x - 1)^3. Therefore NO rank-3 Z-lattice has
    an automorphism of order 5. Not this one. Any.
G9  the trace of an order-5 icosahedral rotation is phi; a finite-order
    automorphism of a rank-3 Z-lattice has integer trace; phi is not an
    integer. The minimal faithful Z-rank of the icosahedral 3-dimensional
    representation is 6, because its character value is phi, not rational.
```

Pins:

```
fib_vs_photon_bridge.py
  sha256 cdcb8941a262d45c1f18e26fe0fba9c3495a7e5df819a36ac6b239cb93ea1a3f  11337 B
stdout
  sha256 456d068bbc96f2b02d7b25ac3e2cd0bff1fdf6776f16a7be42df8dba28697176   2850 B
exit 0, stderr empty, x86_64, LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1
PYTHONHASHSEED=0 TZ=UTC. Single architecture: candidate-C, not a two-platform pin.
```

## 4. The connection, stated once

The Fibonacci anyon is non-abelian, and universal for braiding, because its
quantum dimension is phi, an irrational number. A rank-3 integer lattice
cannot have an automorphism of order 5 because that automorphism would need
trace phi, an irrational number. The same irrationality that makes the
Fibonacci category interesting is what makes the icosahedral branch of the
photon carrier impossible.

The kernel ker(Tr_4) in Z^4 has rank 3. So the golden branch was never
available to it, under any lift, from any decoder action. GATE-LIFT-KERNEL-Z
was posed as a fork with two live branches, ADOPTED (A_3 with O_h) and
REOPENED (a phi-module carrying order-5 isometries). Those are not two
branches of one question. The first is a rank-3 crystal question. The second
is not a rank-3 question at all.

## 5. Why UNTYPED was the only outcome the vocabulary could return

UNIQUE-A3 and UNIQUE-A5-LIFT differ in Z-rank, not in the decoder action. A
predefinition pass looking for a lift TYPE on a rank-3 carrier finds that the
A5 alternative has no type there, and correctly refuses to return EMPTY or
NONUNIQUE, both of which would falsely imply the question was well posed and
merely unanswered. UNTYPED is the accurate report of a type error in the
vocabulary itself.

That is good news for the lane, not bad. The blockage is a definition, not a
computation, and definitions are cheap. No probe run would have moved it.

## 6. Two honest routes, neither adopted here

```
ROUTE A, crystal.  Accept rank 3. Then UNIQUE-A3 with O_h is the only typed
    branch a rank-3 carrier can ever return, and the FCC tables of
    C-PHOTON-SPATIAL-SYMBOL-1 stand at their existing grade. The golden and
    braid content then does NOT live in the spatial carrier: it lives in the
    fiber, the Z_5 holonomy and the argument channel. O-KERNEL-BRAID
    re-targets off space. Cost: the icosahedral shell tables of ADDENDUM-3
    are retired for this carrier, permanently, with a proof rather than a
    conditional.
ROUTE B, quasicrystal.  The golden branch requires a Z[phi]-module, rank 6
    over Z, read in R^3 through an irrational cut. That is the standard and
    the only realisation of icosahedral order in three dimensions, and it is
    the same structure the demonstration set already names (cut-and-project,
    quasicrystal diffraction, the Fibonacci chain). It is NOT a lift of
    ker(Tr_4). It is a different carrier that reduces onto it. It needs its
    own named gate, its own layer declaration, and its own candidate. It must
    not be smuggled in as an outcome of issue #193.
```

Falsifier for this audit, stated plainly: exhibit an integer 3 by 3 matrix of
order 5 preserving any positive definite integral form, or an order-5
automorphism of any rank-3 Z-lattice. Any such object kills section 4, 5 and 6
outright. G8 says none exists.

## 7. Recommended disposition of issue #193

Not a ruling; the ruling is the owner's.

```
1  Record UNTYPED as a TYPE finding, not a null result, with the reason: the
   outcome vocabulary mixes two Z-ranks.
2  Retire UNIQUE-A5-LIFT from the vocabulary with the G8/G9 proof attached,
   rather than leaving it as an unreached branch. An impossible branch left
   standing reads as an open possibility and will be re-proposed.
3  Re-freeze the remaining vocabulary on the rank-3 question only, where a
   formal run can decide something.
4  If the owner wants the golden branch alive, open it as ROUTE B with its
   own gate and its own rank declaration. Do not reopen it inside #193.
```

## 8. Non-claims

No promotion, no registry move, no public edit, no lift adopted, no probe
branch, no pin claimed on any immutable line. Single architecture. Nothing
here asserts any TWIST-J object is a tau anyon, and PHIBIT-NOT-TAU [F] stands
untouched. The internal line was not reachable this session and is not cited
as current.
