# SPDX-License-Identifier: Apache-2.0
"""Equal-account worker preparations with a predicted matter-sensitive B guard."""
from itertools import product
from functools import cache

import kernel as k
import stock as s


@cache
def balance_table():
    norms = {}
    for c in sorted(product(range(-1, 2), repeat=4), key=lambda a: (sum(map(abs,a)),a)):
        v = k.from_j(*c)
        norms.setdefault(k.norm(v),v)
    balances = {}
    for h,v in norms.items():
        for g,z in norms.items():
            balances.setdefault(k.add(h,g),(v,z))
    return balances


def options():
    units = s.UNITS
    candidates = {k.from_j(*c) for c in product(range(-1,2),repeat=4)}
    candidates.update(k.add(old,k.scale(2,u)) for old in (s.W,s.T) for u in units)
    balances = balance_table()
    budget = k.add(k.scale(2,k.norm(s.V)),k.norm(s.Q_REST))
    for a in sorted(candidates):
        live = k.contact(a,s.W)[0]
        alt = k.contact(a,s.T)[0]
        if k.norm(live)==k.norm(alt):
            continue
        for unit, tag in product(units,(1,2)):
            gap = k.multiply(unit,k.multiply(k.J if tag==1 else k.INV_J,live))
            b = k.scale(2,gap)
            for c in (k.ZERO,*units):
                payer = k.subtract(s.Q_REST,k.add(b,c))
                left = k.subtract(budget,k.add(k.scale(2,k.norm(a)),k.norm(b),k.norm(c),k.norm(payer)))
                if not k.even(left):
                    continue
                credit = k.half(left)
                for escrow in (True,False):
                    residual = k.subtract(credit,k.ONE) if escrow else credit
                    if residual not in balances:
                        continue
                    yield a,b,c,payer,escrow,*balances[residual],tag
                    break


# Storing b on CLK or on CORR gives two realizations. The norm guards use h,
# hence changing the sign of the corresponding half-gap preserves its guard.
DESIGNS = dict(enumerate(product(options(),(28,30),(k.CLK,k.CORR)),start=2000))
ALL = tuple(s.MODELS)+tuple(DESIGNS)


def decorate(field, mode):
    if mode in s.MODELS:
        return s.decorate(field,mode)
    (a,b,c,q,paid,v,z,tag),worker,lane=DESIGNS[mode]
    if (field[17][:2]!=s.pair(s.V) or field[29][3]!=s.Q_REST or
            any(field[i][:2]!=s.EMPTY for i in (worker,16,19)) or
            field[worker][lane]!=k.ZERO or (c!=k.ZERO and field[18][3]!=k.ZERO)):
        return None
    result=[list(cell) for cell in field]
    for i,x in ((worker,a),(17,s.T if paid else k.ZERO),(16,v),(19,z)):
        result[i][:2]=s.pair(x)
    result[worker][lane]=b
    result[29][3]=q
    if c!=k.ZERO:
        result[18][3]=c
    result=tuple(map(tuple,result))
    if k.account(result)!=k.account(field):
        raise AssertionError(("worker funding",mode))
    return result


def label(mode):
    if mode in s.MODELS:
        return s.MODELS[mode].label
    design,worker,lane=DESIGNS[mode]
    return f"guard{design[-1]}_site{worker}_rail{lane}_escrow{int(design[4])}"


def direct(bare, mode):
    result=decorate(s.baseline(bare),mode)
    if result is None:
        raise AssertionError(("launch ineligible",mode))
    return result
