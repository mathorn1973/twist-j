# SPDX-License-Identifier: Apache-2.0
"""Phase and signed branch counts of two simultaneous spatially isolated matter probes."""

from native import h3, ledger, transport

NX, NY = 240, 4
BASES = (0, 80, 160)
RANGES = (1, 2, 3, 4)
ONE, ZERO, J, J_INV = h3.ONE, h3.ZERO, h3.J, h3.J_INV
L = h3.sub(ONE, h3.RHO)


def power(word, exponent):
    value = ONE
    for _ in range(exponent):
        value = h3.mul(value, word)
    return value


D = power(L, 8)
BIAS = h3.mul(h3.add(J, J_INV), D)
DELTA = h3.sub(J_INV, J)


def source_word(distance):
    return h3.scale(2**distance, h3.mul(power(L, 8-distance), DELTA))


def set_word(state, key, value):
    if value == ZERO:
        state.pop(key, None)
    else:
        state[key] = value


def prepare(r, q, p, compensate=False, pilot=False):
    state = {}
    for arm, (base, distance) in enumerate(zip(BASES, (r, 2*r, r))):
        slot = distance if compensate else 8
        for i in range(1, 9):
            word = h3.scale(q, source_word(i))
            park = base + 30 + 2*i
            x = base if i == slot and arm < 2 else park
            state[x, 0, 3] = word
            state[park + 1, 0, 3] = h3.scale(-1, word)
        if not pilot:
            x = base + distance
            state[x, 0, 0] = D
            state[x, 0, 1] = h3.scale(-1, D)
            state[x, 0, 2] = h3.scale(p, BIAS)
            state[base+50, 0, 2] = h3.scale(-p, BIAS)
    return state


def contacts(state, bit, inverse=False, nx=NX, ny=NY):
    pairs = set()
    for x, y, rail in state:
        if rail == 3:
            start = (x-(x-bit)%2) % nx
            pair = ((start,y,rail), ((start+1)%nx,y,rail))
        else:
            start = (y-(y-bit)%2) % ny
            pair = ((x,start,rail), (x,(start+1)%ny,rail))
        pairs.add(pair)
    out = {}
    for a, b in pairs:
        left, right = h3.transport_pair(state.get(a,ZERO), state.get(b,ZERO), inverse)
        set_word(out, a, left)
        set_word(out, b, right)
    return out


def collisions(state):
    out = state.copy()
    tags = {}
    for x, y in {(x,y) for x,y,i in state if i < 2}:
        cell = tuple(state.get((x,y,i),ZERO) for i in range(4))
        words, tag = h3.collision(cell)
        for i, word in enumerate(words):
            set_word(out,(x,y,i),word)
        if tag:
            tags[x,y] = tag
    return out, tags


def account(state):
    values = list(state.values())
    h = h3.ring_sum(h3.h(v) for v in values)
    return (h3.ring_sum(v for (_,_,i), v in state.items() if i < 2),
            h3.ring_sum(v for (_,_,i), v in state.items() if i >= 2),
            h, h3.scalar_account(h))


def dense(state):
    return tuple(state.get((x,y,i),ZERO) for x in range(NX) for y in range(NY) for i in range(4))


def counts_to_word(n):
    return h3.mul(D, power(J if n >= 0 else J_INV, abs(n)))


def follow(r, q, p, compensate, pilot=False, crosscheck=False):
    initial = prepare(r,q,p,compensate,pilot)
    current = initial
    stock = account(initial)
    targets = tuple(base+d for base,d in zip(BASES,(r,2*r,r)))
    counts = [0,0,0]
    arrivals = [None,None,None]
    initial_hits = [None,None,None]
    samples = []
    for t in range(1,4*r+1):
        bit = (t-1)%2
        pre = contacts(current,bit)
        post, tags = collisions(pre)
        assert account(pre) == account(post) == stock
        restored_c, _ = collisions(post)
        assert restored_c == pre and contacts(restored_c,bit,True) == current
        if crosscheck and t in (1, 2):
            dc = transport(dense(current), NY, bit)
            db, _ = h3.collide(dc, NY)
            assert dc == dense(pre) and db == dense(post) and ledger(db) == stock
        for i, x in enumerate(targets):
            incoming = pre.get((x,0,3),ZERO)
            tag = tags.get((x,0),0)
            if arrivals[i] is None and incoming != ZERO:
                arrivals[i] = t
                initial_hits[i] = tag
            if not pilot:
                old = counts[i]
                counts[i] += {0:0,1:1,2:-1}[tag]
                assert pre[x,0,0] == counts_to_word(old) and post[x,0,0] == counts_to_word(counts[i])
                assert post[x,0,1] == h3.scale(-1,post[x,0,0])
        samples.append(tuple(counts))
        current = post
    for t in range(4*r,0,-1):
        pre, _ = collisions(current)
        current = contacts(pre,(t-1)%2,True)
    assert current == initial
    a, b = samples[2*r-1], samples[-1]
    differ = [row[0]-row[1] for row in samples]
    return stock, {"arrival":arrivals, "first_arrival_B":initial_hits,
                   "branch_count_by_tick":samples, "near_minus_far_at_2r":a[0]-a[1],
                   "near_minus_far_at_4r":b[0]-b[1],
                   "postarrival_hold_increment":differ[-1]-differ[2*r-1],
                   "has_intermediate_contrast":any(n%5 for n in differ),
                   "free_reference_fixed":all(row[2] == 0 for row in samples),
                   "endpoint_matter_Q":[h3.scalar_account(h3.scale(2,h3.h(counts_to_word(t))))
                                        for t in b] if not pilot else None}


def run():
    rows, pilots = [], []
    initial_stock = None
    for r in RANGES:
        _, time = follow(r,1,1,False,pilot=True)
        pilots.append({"r":r, "arrival":time["arrival"],"clock_matches":time["arrival"] == [r,2*r,None]})
        for compensate in (False,True):
            for q in (-1,1):
                for p in (-1,1):
                    stock, row = follow(r,q,p,compensate,crosscheck=(r==1 and q==p==1))
                    if initial_stock is None:
                        initial_stock = stock
                    assert stock == initial_stock
                    rows.append(dict(r=r,source=q,bias=p,range_compensated=compensate,**row))
    return {"pilot":pilots, "stock":initial_stock,"rows":rows,
            "equal_clock_arrivals":all(p["clock_matches"] for p in pilots),
            "compensated_first_hits_select_product":all(
                row["first_arrival_B"] == [1 if row["source"]*row["bias"]==1 else 2]*2+[None]
                for row in rows if row["range_compensated"])}
