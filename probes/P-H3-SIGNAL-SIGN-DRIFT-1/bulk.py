# SPDX-License-Identifier: Apache-2.0
"""Measure stock transported by a freely propagating material pulse with fixed residue marks."""

from anchor import DIVIDEND, residue
from light import packet_launch
from native import h3, step

HEIGHT = 384
ZERO = h3.ZERO


def material_step(row, bit, backward=False):
    out = row.copy()
    for y in range(bit, HEIGHT, 2):
        z = (y + 1) % HEIGHT
        out[y], out[z] = h3.transport_pair(row[y], row[z], backward)
    return out


def dense(row):
    field = [ZERO] * (2 * HEIGHT * 4)
    for y, value in enumerate(row):
        field[4*y:4*y+2] = value, h3.scale(-1, value)
    return tuple(field)


def h_stock(row, region):
    return h3.scale(2,h3.ring_sum(h3.h(row[i]) for i in region))


def nonnegative(word, place):
    # Exact sign of 2*(a+b*phi) = (2a+b) +/- b*sqrt(5).
    h3.require(word[1] == 0 and word[2] == word[3], "real stock")
    a, b = word[0], -word[2]
    x, y = 2*a + b, b if place == 1 else -b
    if x == 0 or y == 0 or (x > 0) == (y > 0):
        return (x or y) >= 0
    return (x > 0) == (x*x >= 5*y*y)


def fraction_floor(part, whole, embedding):
    low, high = 0, 10001
    while high - low > 1:
        mid = (low + high) // 2
        if nonnegative(h3.sub(h3.scale(10000,part), h3.scale(mid,whole)), embedding):
            low = mid
        else:
            high = mid
    return low


def marks(row):
    normalized = row
    k = 0
    while not any(residue(word) for word in normalized):
        divided = [h3.mul(w, DIVIDEND) for w in normalized]
        h3.require(all(all(v % 5 == 0 for v in w) for w in divided), "bulk normalization")
        normalized = [tuple(v // 5 for v in w) for w in divided]
        k += 1
    return k, {i for i,w in enumerate(normalized) if residue(w)}


def run():
    row = [ZERO] * HEIGHT
    for (x,y,r),word in packet_launch(0).items():
        if r == 3 and y == 0:
            row[x] = word
    initial = row.copy()
    support = {i for i,w in enumerate(initial) if w != ZERO}
    initial_marks = marks(initial)
    outside = set(range(HEIGHT)) - support
    whole = h_stock(row, range(HEIGHT))
    fixed = True
    dense_agree = True
    rows = []
    for tick in range(1,81):
        bit = (tick - 1) % 2
        new = material_step(row,bit)
        if tick in (1,2,40,80):
            c,b,tags = step(dense(row),HEIGHT,bit)
            dense_agree &= c == b == dense(new) and not tags
        h3.require(material_step(new,bit,True) == row and h_stock(new,range(HEIGHT)) == whole,
                   "free material full account and inverse")
        fixed &= marks(new) == initial_marks
        row = new
        if tick in (40,80):
            moved = h_stock(row,outside)
            held = h_stock(row,initial_marks[1])
            rows.append({"tick":tick,"outside_start_H":moved,"on_marks_H":held,
                         "outside_start_fraction_floor_10000":[fraction_floor(moved,whole,s) for s in (1,2)],
                         "on_marks_fraction_floor_10000":[fraction_floor(held,whole,s) for s in (1,2)]})
    for tick in range(80,0,-1):
        row = material_step(row,(tick-1)%2,True)
    h3.require(row == initial, "bulk full 80-tick return")
    return {"primitive_exponent":initial_marks[0],"marked_rows":sorted(initial_marks[1]),
            "initial_support_size":len(support),"whole_H":whole,"Q":h3.scalar_account(whole),
            "fixed_at_all_cuts":fixed,"full_native_agreement":dense_agree,"cuts":rows}
