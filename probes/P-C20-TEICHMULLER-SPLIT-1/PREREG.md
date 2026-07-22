# PREREG. P-C20-TEICHMULLER-SPLIT-1

Public lock: owner directive of 2026-07-22 ("Chci ho take verejne... dej
oboji ven"), recorded with the incubation candidate C-C20-TEICHMULLER-SPLIT-1
in the project lane; the promotion queue holds only this pair of probes and
no competing claim exists. The owner attaches the issue number at
pull-request time; this session is the single probe owner. Base: Public
Canon v15, tag canon-v15, Canon content commit
`a850753348583e611bf7ccd5aa074030dc7e12f5`, branch base `origin/main`
`434e02a01903ef7a237053eac1231dbe7496bbf5`.

```text
LAYER:  L1 state arithmetic in the thick ramified fiber. No lift to L2-L6.
TARGET: the exact Teichmueller-times-unipotent split of the J-cycle in
        Z[zeta_5]/5, its forced C_4 two-part at every nilpotent depth, and
        the independent matrix confirmation from the raw axiom step.
```

No scientific status is earned by this preregistration. Any eventual Canon,
registry, dependency, or frontier disposition is separate reviewed work.

## Frozen model

Work in the exact ring model

```text
R = Z[zeta_5]/5, basis (1, j, j^2, j^3), j^5 = 1,
reduction j^4 = -(1 + j + j^2 + j^3), coefficients mod 5,
J = 1 + j^2.
```

R is local: the unique maximal ideal is the kernel of the residue map
j -> 1 onto F_5, so x is a unit iff its coefficient sum is nonzero mod 5.
The independent leg uses only the raw axiom step map on Z^4 mod 5,

```text
step(a,b,c,d) = (a - c + d, b - c, a, b - c + d),
```

and its matrix M (columns = images of the basis), with no ring
multiplication reused.

## Frozen statement

```text
(A) CYCLE     ord(J) = 20 in R, and J^10 = -1.
(B) WHEEL     J^5 = 2 exactly, a scalar constant with 2^4 = 1; the fifth
              powers walk the Teichmueller wheel J^5, J^10, J^15 =
              2, -1, 3 = phi_lambda. The scalar 2 is the i_5 of the
              registered row TIME-QUANTUM-TOWER at k = 1 (M_J^5 = i_5 I):
              the Teichmueller component of the J-cycle is the time
              quantum scalar.
(C) SPLIT     u := J^16 = 3J is unipotent of order exactly 5 with
              nilpotency index exactly 4 ((u-1)^4 = 0, (u-1)^3 != 0), the
              split J = J^5 * J^16 is exact (5 + 16 = 21 = 1 mod 20), and
              <2> intersect <u> = {1}: <J> = C_4 x C_5 internally,
              Teichmueller times unipotent.
(D) TWO-PART  the 2-part of <J> is <J^5> = C_4, and over all 625 elements
              of R, x^8 = 1 iff x^4 = 1 iff x is a nonzero constant: no
              element of order 8 exists in R.
(E) DEPTH     |units(R)| = 500 = 4 * 5^3, and for every nilpotent depth m
              the unit count 4 * 5^(m-1) has 2-valuation exactly 2, so 8
              never divides it: the eight-phase is forbidden at every depth
              of the ramified fiber by Lagrange.
(F) MATRIX    independently, the raw step matrix satisfies M^5 = 2I,
              M^10 = -I, M^16 = 3M, ord(M) = 20, and (M - 2I)^4 = 0 with
              (M - 2I)^3 != 0 (a single Jordan block J_4(2)), in exact
              column agreement with the ring walk for k = 0..19.
```

Reading at the frozen scope (carries no more than the clauses): the
machine's own mod-5 cycle carries the five of process and the four of
phase; the eight of the half-phase can live only one quadratic floor up.

## Frozen proof

1. The model is the standard presentation of Z[zeta_5]/5; locality and the
   unit criterion follow from 5 = unit * (1 - j)^4, so the maximal ideal is
   (1 - j) and the residue map is j -> 1.
2. (B) implies (A): J^5 = 2 gives J^20 = 2^4 = 1 and J^10 = 2^2 = -1;
   J^4 != 1 and J^10 != 1 exclude the proper divisors of 20 (every proper
   divisor of 20 divides 4 or 10). J^5 = 2 itself is a finite exact
   computation in R, executed by the verifier.
3. (C): u = J^16 = (J^5)^3 J = 3J; u^5 = (3J)^5 = 3^5 J^5 = 3 * 2 = 1, and
   u != 1, so ord(u) = 5.
   The residue of u is 3 * 2 = 1, so u - 1 lies in the maximal ideal and
   (u-1)^4 in its fourth power, which is (5) = 0; the verifier witnesses
   (u-1)^3 != 0, fixing the index at 4. J^5 * J^16 = J^21 = J by (A). The
   subgroups <2> and <u> have coprime orders 4 and 5, so they intersect
   trivially and generate C_20 internally.
4. (D): a solution of x^4 = 1 is a unit whose unipotent part has order
   dividing both 4 and a power of 5, hence is trivial; so x is a
   Teichmueller constant, and those are exactly the four nonzero scalars.
   x^8 = 1 gives (x^4)^2 = 1 with x^4 also a fourth root, and the verifier
   settles both censuses exhaustively over all 625 elements.
5. (E): units(F_5[t]/t^m) = F_5^* x (1 + m-ideal) has order 4 * 5^(m-1);
   5^(m-1) is odd, so v_2(4 * 5^(m-1)) = 2 for every m >= 1. The verifier
   witnesses m <= 12 and the 500 count for R itself.
6. (F): M is the multiplication-by-J matrix, so (A)-(C) transfer; the
   verifier re-derives all matrix facts by matrix arithmetic alone and
   checks the column agreement against the raw step map, closing the loop
   between the axiom step, the matrix, and the ring.

The proof, not the finite audit, is the proposed basis for theorem status
at the frozen L1 scope; clauses (D) and (E) are additionally settled by
complete finite enumeration inside the verifier.

## The six frozen fields

```text
EQUATION     Statements (A)-(F) exactly as written above. The novel content
             is the exact internal split J = J^5 * J^16 with its
             Teichmueller-equals-time-quantum identification, the
             nilpotency index 4 of the unipotent component, the two-part
             census at every depth, and the closed ring-matrix-step
             agreement. FIB-ROOT-TIES and TIME-QUANTUM-TOWER are
             consistency anchors, not premises.

CODE         verify.py, SHA-256
             c0909d286b634edeaae867767549a5f8d98a8e80102462a10ea6b368e7ec43fe
             (5393 bytes). Python standard library only; exact integers
             only; deterministic; no floats, files, network, or
             subprocesses. Run from the repository root with LC_ALL=C
             LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC.

CARRIER      all 625 elements of R for the censuses; the full cyclic group
             <J>; depths m = 1..12 as arithmetic witnesses of the proven
             all-m clause; the matrix leg over k = 0..19. No external
             dataset.

SYSTEMATICS  exact arithmetic throughout; no numerical approximation
             anywhere. Source material, not formal evidence: incubation
             candidate C-C20-TEICHMULLER-SPLIT-1 (project lane, frozen and
             executed 2026-07-22: prereg sha256 848a4e9c..., verifier
             16de9709..., stdout 0101e016..., 12/12; independent matrix
             break run 1 fired a false FAIL from an unnormalized matrix
             literal, diagnosed and disclosed, run 2 survived 11/11,
             ecfad05a.../7f028324...), and one informal x86_64 dry run of
             this verify.py with stdout sha256
             5f4822f9b49d3936d98289f9374de291d2810d27daeada2a16a468670fd05e9e.
             A defect found in
             PREREG.md or verify.py after the pin invalidates this named
             probe: execution stops, neither frozen file is amended, and a
             new named probe and pin are required.

THRESHOLD    KILL the theorem candidate on any incorrect cycle, wheel,
             split, unipotence, two-part, depth, or matrix statement; any
             element of order 8 anywhere in R; any disagreement between the
             ring walk, the matrix powers, and the raw step map; a proof
             gap or dependency conflict; or any unreconciled FAIL in gates
             01-06. A formal leg passes only with exit 0, empty stderr, all
             six PASS lines, the RESULT 6/6 ALL PASS line, and
             byte-identical stdout on the recorded aarch64 and GitHub
             x86_64 runs.

LAYER        L1 only. No clock reading, tick identification, physical
             carrier, SI scale, or lift to L2-L6 is asserted.
```

## Dependencies and scope firewall

Frozen premises:

```text
PENTIT-ROOT-FACTS [T]     J_lambda = 2 and phi_lambda = 3 at the residue
```

Consistency anchors, not premises: `FIB-ROOT-TIES [T]` (Jordan block
J_4(2), towers 20 = 4p and 10 = 2p, -I at half), `TIME-QUANTUM-TOWER [C]`
(M_J^(5^k) = i_5 I, period 4 * 5^k), `RAMIFIED-TM-LIFT [T]`
(char(M_J) = (x - 2)^4 mod 5). The verifier is self-contained and
re-derives everything it asserts.

This probe does not read a clock, does not identify a tick, does not touch
the METRO rows, and does not assert any physical carrier for the split. The
sibling probe P-C8-BILINEAR-SHADOW-1 concerns the quadratic floor above;
neither probe depends on the other.

Before the first formal execution, this file and `verify.py` must be
committed and pushed together. After that public pin they are immutable for
this probe.
