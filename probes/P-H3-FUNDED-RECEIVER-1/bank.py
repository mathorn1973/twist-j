# SPDX-License-Identifier: Apache-2.0
"""Equal-account bank and native preimage constructions on the public ingress stock."""
from functools import cache
from itertools import product

import kernel as k
from fixture import stock
from funding import stock_forward

TARGET, BANK1, BANK2 = 31, 16, 17
PAYERS = (29, 8, 9, 30, 4, 5)
ROOTS = tuple(k.power(3 * i) for i in range(5))
UNITS = ROOTS + tuple(k.scale(-1, a) for a in ROOTS)
# Ordered receivers prioritize the two guards and several phases of the radiation rail.
PREFERENCES = ((2, 5, 0), (1, 1, 0), (2, 3, 0), (2, 9, 0),
               (1, 1, 1), (2, 3, 1), (2, 5, -1), (1, 0, -1))
ALL = tuple(range(248)) + tuple(range(300, 364)) + tuple(range(400, 416))
ANCHORS = (0, 42, 300, 400)


def residual_table():
    words = sorted(product(range(-1, 2), repeat=4), key=lambda w: (sum(map(abs, w)), w))
    norms = {}
    for coeffs in words:
        a = k.from_j(*coeffs)
        norms.setdefault(k.norm(a), a)
    result = {}
    for a, left in norms.items():
        for b, right in norms.items():
            result.setdefault(k.add(a, b), (left, right))
    return result


BALANCES = residual_table()


@cache
def decomposition(q, guard, unit_index, background):
    t = UNITS[unit_index]
    u, f = (t, k.multiply(k.J, t)) if guard == 1 else (k.multiply(k.J, t), t)
    corr = k.scale(background, t)
    clk = k.add(corr, k.scale(2, f))
    remainder = k.subtract(q, k.add(clk, corr))
    surplus = k.subtract(k.norm(q), k.add(k.norm(remainder), k.norm(clk), k.norm(corr),
                                           k.scale(2, k.norm(u))))
    if not k.even(surplus) or k.half(surplus) not in BALANCES:
        return None
    v, w = BALANCES[k.half(surplus)]
    return u, clk, corr, remainder, v, w


def funded_cut(field, preference):
    if any(v != k.ZERO for v in field[TARGET]):
        raise AssertionError("target requires four empty words")
    if any(field[i][j] != k.ZERO for i in (BANK1, BANK2) for j in (k.R0, k.R2)):
        raise AssertionError("balance sites require empty matter")
    typ, root, bg = PREFERENCES[preference]
    # Prefer the specified target even when another payer is needed.
    # Keep every choice a function of the cut, including the deterministic fallback.
    order = [(typ, root, bg)]
    order.extend((g, i, z) for z in (bg, 0, 1, -1, 2, -2)
                 for g in (typ, 3 - typ) for i in ((root+n) % 10 for n in range(10)))
    for guard, index, background in dict.fromkeys(order):
        for donor in PAYERS:
            solution = decomposition(field[donor][k.CORR], guard, index, background)
            if solution is None:
                continue
            u, clk, corr, remainder, v, w = solution
            out = [list(c) for c in field]
            out[TARGET] = [u, k.scale(-1, u), clk, corr]
            out[donor][k.CORR] = remainder
            for pos, x in ((BANK1, v), (BANK2, w)):
                out[pos][:2] = (x, k.scale(-1, x))
            result = tuple(map(tuple, out))
            if k.account(result) != k.account(field):
                raise AssertionError("funded cut account")
            return result, (donor, guard, index, background)
    return None, None


@cache
def base91(bare):
    field = stock(bare)
    for tick in range(1, 91):
        field = k.native_step(field, tick % 2)[1]
    return k.transport(field, k.HEIGHT, 1)


@cache
def back_launch(bare, pref):
    cut, spec = funded_cut(base91(bare), pref)
    if cut is None:
        return None, None
    field = k.transport(cut, k.HEIGHT, 1, -1)
    for tick in range(90, 0, -1):
        field = k.inverse_step(field, tick % 2)
    check = field
    for tick in range(1, 91):
        check = k.native_step(check, tick % 2)[1]
    if k.transport(check, k.HEIGHT, 1) != cut or k.account(field) != k.account(cut):
        raise AssertionError("native preimage")
    return field, spec


def direct_bank(bare, pref, phase):
    field, spec = funded_cut(stock(bare), pref)
    if field is None:
        raise AssertionError("unfunded direct stock")
    if phase:
        field = [list(c) for c in field]
        neighbor = 28 if phase <= 4 else 30
        field[TARGET][k.CLK], field[neighbor][k.CLK] = k.contact(
            field[TARGET][k.CLK], field[neighbor][k.CLK], 1 + (phase - 1) % 4)
        field = tuple(map(tuple, field))
    return field, spec


def prepare_info(bare, rank, mode):
    if mode < 248:
        return stock_forward(bare, rank, mode), "swap" if mode else "baseline"
    if 300 <= mode < 364:
        pref, phase = divmod(mode - 300, 8)
        field, spec = direct_bank(bare, pref, phase)
        return field, ("bank", *spec, phase)
    if 400 <= mode < 416:
        pref = (mode - 400) % 8
        back, spec = back_launch(bare, pref)
        if back is not None and back[TARGET][0] != back[TARGET][1]:
            if mode < 408:
                return back, ("preimage", *spec)
            # Rebuild only the target column's initial matter + CLK profile and
            # the target CORR, keeping the original launch clocks and source.
            orig = stock(bare)
            if any(x != k.ZERO for i in range(28,32) for x in orig[i][:3]):
                raise AssertionError("target column is not empty")
            col = [back[i][:3] for i in range(28, 32)]
            z = back[TARGET][k.CORR]
            if k.add(*(a for cell in col for a in cell[:2])) == k.ZERO:
                cost = k.add(*(k.norm(a) for cell in col for a in cell), k.norm(z))
                debit = k.add(*(cell[k.CLK] for cell in col), z)
                bank = orig[29][k.CORR]
                rem = k.subtract(bank, debit)
                credit = k.subtract(k.norm(bank), k.add(cost, k.norm(rem)))
                if k.even(credit) and k.half(credit) in BALANCES:
                    out = [list(cell) for cell in orig]
                    for idx, triple in enumerate(col, 28):
                        out[idx][:3] = triple
                    out[TARGET][k.CORR] = z
                    out[29][k.CORR] = rem
                    for pos, a in zip((BANK1, BANK2), BALANCES[k.half(credit)]):
                        out[pos][:2] = (a, k.scale(-1, a))
                    result = tuple(map(tuple, out))
                    if k.account(result) != k.account(orig):
                        raise AssertionError("projected launch balance")
                    return result, ("column_only", *spec)
        f, fallback = direct_bank(bare, pref, 0)
        return f, ("fallback_to_bank", *fallback)
    raise ValueError(mode)


def prepare(bare, rank, mode):
    return prepare_info(bare, rank, mode)[0]
