#!/usr/bin/env python3
"""Residue interface between the 322-contact loader and the 31-slot read core.

NON-CANONICAL / L1 exact audit for notes/STAVBA-STROJE-2026-11-08. It creates
no claim. It asks one typed question about two merged constructions on the
same carrier O = Z[j], j^5 = 1, 1 + j + j^2 + j^3 + j^4 = 0:

  Can a fixed word of total contacts C_rho (rho = j^2, admission x - y in 2O)
  and whole-slot swaps carry the loader output pair (u + tB, u - tB),
  u = 1 - j, B = 1 - j^2 (probes/P-POLE-HEIGHT-FIVE-INPUT-REPLAY-1), into the
  clock pair X_r = (rho^r w, -rho^r w), w = 1 + rho, or into the source triple
  Y_n of the read core (probes/P-RELATIVE-CONTACT-VARIABLE-ARRIVAL-1,
  canon/CANON.md "A common finite apparatus with an independently variable
  second input")?

The registered invariant RELATIVE-CONTACT-FIXED-WORD-RESIDUE-BOUNDARY [T]
says that every fixed word changes the vector of slot residues modulo 1 - j
by one input-independent permutation. The script recomputes the residues of
both input dialects, checks the invariant exhaustively on a finite box, and
prints the consequence: the loader pair has residues (0, 0) and the clock
pair has residues (2, 3), so no contact-only word converts one into the other
on the pair alone; any conversion must borrow slots of residues 2 and 3 and
park the residue-0 pair elsewhere. Python standard library only, exact
integers, no randomness, deterministic output.
"""

from __future__ import annotations

from itertools import product

# Elements of O in the power basis (a, b, c, d) = a + b j + c j^2 + d j^3,
# with j^4 = -1 - j - j^2 - j^3.

Elt = tuple[int, int, int, int]


def add(x: Elt, y: Elt) -> Elt:
    return tuple(p + q for p, q in zip(x, y))  # type: ignore[return-value]


def sub(x: Elt, y: Elt) -> Elt:
    return tuple(p - q for p, q in zip(x, y))  # type: ignore[return-value]


def neg(x: Elt) -> Elt:
    return tuple(-p for p in x)  # type: ignore[return-value]


def times_j(x: Elt) -> Elt:
    a, b, c, d = x
    return (-d, a - d, b - d, c - d)


def times_rho(x: Elt) -> Elt:
    return times_j(times_j(x))


def scale(k: int, x: Elt) -> Elt:
    return tuple(k * p for p in x)  # type: ignore[return-value]


def halve(x: Elt) -> Elt:
    assert all(p % 2 == 0 for p in x), x
    return tuple(p // 2 for p in x)  # type: ignore[return-value]


def in_2O(x: Elt) -> bool:
    return all(p % 2 == 0 for p in x)


def residue(x: Elt) -> int:
    """Image in O/(1 - j) = F_5, where j maps to 1."""
    return sum(x) % 5


def account(x: Elt) -> int:
    s = sum(x)
    return (5 * sum(p * p for p in x) - s * s) // 2


def contact(x: Elt, y: Elt) -> tuple[Elt, Elt]:
    if not in_2O(sub(x, y)):
        return x, y
    s = halve(add(x, y))
    t = halve(sub(x, y))
    rt = times_rho(t)
    return add(s, rt), sub(s, rt)


ONE: Elt = (1, 0, 0, 0)
J: Elt = (0, 1, 0, 0)
RHO: Elt = times_rho(ONE)
U_LOADER: Elt = sub(ONE, J)              # u = 1 - j
B_LOADER: Elt = sub(ONE, RHO)            # B = 1 - j^2
W_CLOCK: Elt = add(ONE, RHO)             # w = 1 + rho
ZERO: Elt = (0, 0, 0, 0)
TWO: Elt = (2, 0, 0, 0)


def main() -> None:
    print("carrier O = Z[j], residue map j -> 1 onto F_5")

    # 1. Exhaustive check of the invariant on a finite box: every admitted or
    #    refused contact preserves each slot residue and the pair account sum.
    rng = range(-2, 3)
    box = [tuple(v) for v in product(rng, repeat=4)]
    checked = admitted = 0
    for x in box:
        for y in box:
            x2, y2 = contact(x, y)  # type: ignore[arg-type]
            checked += 1
            if (x2, y2) != (x, y):
                admitted += 1
            assert residue(x2) == residue(x) and residue(y2) == residue(y)
            assert account(x2) + account(y2) == account(x) + account(y)
            assert add(x2, y2) == add(x, y)
    print(f"contact pairs checked on the box [-2,2]^4 x [-2,2]^4: {checked}; "
          f"state-changing: {admitted}; residue, account sum and ring sum preserved: yes")

    # 2. The two input dialects.
    print("loader output pair (u + tB, u - tB), u = 1 - j, B = 1 - j^2:")
    for t in range(-2, 3):
        p = add(U_LOADER, scale(t, B_LOADER))
        q = sub(U_LOADER, scale(t, B_LOADER))
        print(f"  t={t:+d}: residues ({residue(p)}, {residue(q)}), accounts ({account(p)}, {account(q)})")

    print("read-core clock pair X_r = (rho^r w, -rho^r w), w = 1 + rho:")
    x = W_CLOCK
    for r in range(5):
        print(f"  r={r}: residues ({residue(x)}, {residue(neg(x))}), accounts ({account(x)}, {account(neg(x))})")
        x = times_rho(x)

    print("read-core source triple Y_n = F^n (0, 2, 0), F = C_01 C_12 acting left first:")
    y = [ZERO, TWO, ZERO]
    seen = []
    for n in range(10):
        res = tuple(residue(v) for v in y)
        seen.append(tuple(y))
        print(f"  n={n}: residues {res}, accounts {tuple(account(v) for v in y)}")
        y0, y1 = contact(y[0], y[1])
        y1, y2 = contact(y1, y[2])
        y = [y0, y1, y2]
    assert seen[9] == seen[0], "period of the source orbit is not nine"
    print("  period of the source orbit under F: 9")

    # 3. Consequence for a fixed word on the pair alone, and the minimal stock.
    loader_res = sorted((0, 0))
    clock_res = sorted((2, 3))
    assert all(sorted((residue(add(U_LOADER, scale(t, B_LOADER))),
                       residue(sub(U_LOADER, scale(t, B_LOADER))))) == loader_res for t in range(-2, 3))
    print("consequence: a fixed contact/swap word permutes the residue vector of the complete state "
          "(RELATIVE-CONTACT-FIXED-WORD-RESIDUE-BOUNDARY [T]);")
    print(f"  loader pair residues {tuple(loader_res)} versus clock pair residues {tuple(clock_res)}: "
          "no word on the pair alone maps one into the other for any t")
    print("  a conversion needs borrowed slots of residues 2 and 3 and a parking place for the "
          "residue-0 pair; it is a relabeling with stock, not a transformation of the pair")
    print("  the source triple keeps residues (0, 2, 0) on its whole orbit, so the loader pair "
          "cannot become a source triple either")
    print("LOADER-INTERFACE RESIDUE AUDIT PASS")


if __name__ == "__main__":
    main()
