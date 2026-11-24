# SPDX-License-Identifier: Apache-2.0
"""A stationary, finite-stock H3 emitter, with feedback included throughout the hold."""

from anchored import (BASES, BIAS, DELTA, J, J_INV, L, NY, ONE, ZERO,
                      account, collisions, contacts, dense, power)
from native import h3, ledger, transport

CENTER = h3.add(ONE, h3.scale(2, h3.add(h3.RHO, h3.mul(h3.RHO, h3.RHO))))
GAP = h3.mul(L, h3.mul(h3.RHO, J))
RECEIVER_BIAS = h3.mul(h3.add(J,J_INV), GAP)
HORIZON = 32


def prepare(r, q, p, pilot):
    state = {}
    emitters, readers = [], []
    for i, (base, distance) in enumerate(zip(BASES, (r, 2*r, r))):
        x = base+20
        reader = x-distance
        src = x+38 if i == 2 else x
        emitters.append(src)
        readers.append(reader)
        state[src,0,0] = DELTA
        state[src,0,1] = h3.scale(-1,DELTA)
        for rail, v in ((2,h3.add(CENTER,J)),(3,h3.sub(CENTER,J))):
            state[src,0,rail] = h3.scale(q,h3.mul(DELTA,v))
        # Cancel the emitter's signed linear radiation stock outside the causal window.
        state[base+65,2,2] = h3.scale(-2*q,h3.mul(DELTA,CENTER))
        if not pilot:
            state[reader,0,0] = GAP
            state[reader,0,1] = h3.scale(-1,GAP)
            state[reader,0,2] = h3.scale(p,RECEIVER_BIAS)
            state[base+65,3,2] = h3.scale(-p,RECEIVER_BIAS)
    return state, emitters, readers


def run_arm(r,q,p,pilot):
    start, emitters, readers = prepare(r,q,p,pilot)
    state = start
    stock = account(state)
    counts = [0]*3
    arrivals = [None]*3
    first_tags = [None]*3
    phase_path = [(0,0,0)]
    source_events = [[] for _ in emitters]
    changes = [[] for _ in emitters]
    emitted_to_left = [[] for _ in emitters]
    first_source_divergence = None
    for t in range(1,HORIZON+1):
        bit = (t-1)%2
        pre = contacts(state,bit)
        post,tags = collisions(pre)
        assert account(pre)==account(post)==stock
        back,_ = collisions(post)
        assert back == pre and contacts(back,bit,True)==state
        if r==1 and p==q==1 and t<=2:
            dc = transport(dense(state), NY, bit)
            assert dc==dense(pre) and h3.collide(dc,NY)[0]==dense(post) and ledger(dc)==stock
        source_cells = []
        for i,(x,rx) in enumerate(zip(emitters,readers)):
            source_tag = tags.get((x,0),0)
            if source_tag:
                source_events[i].append((t,source_tag))
            v1 = state.get((x-1,0,3),ZERO)
            v2 = pre.get((x-1,0,3),ZERO)
            if bit==1 and v1 != v2:
                emitted_to_left[i].append(t)
            source_cells.append(tuple(post.get((x,0,s),ZERO) for s in range(4)))
            tag = tags.get((rx,0),0)
            incoming = pre.get((rx,0,3),ZERO)
            if incoming != ZERO and arrivals[i] is None:
                arrivals[i],first_tags[i] = t,tag
            if not pilot:
                old = counts[i]
                counts[i] += {0:0,1:1,2:-1}[tag]
                for cut, n in ((pre,old),(post,counts[i])):
                    expected = h3.mul(GAP,power(J if n >= 0 else J_INV,abs(n)))
                    assert cut[rx,0,0]==expected and cut[rx,0,1]==h3.scale(-1,expected)
                if counts[i] != old:
                    changes[i].append((t,tag))
        if source_cells[0] != source_cells[1] and first_source_divergence is None:
            first_source_divergence = t
        phase_path.append(tuple(counts))
        state = post
    for t in range(HORIZON,0,-1):
        pre,_ = collisions(state)
        state = contacts(pre,(t-1)%2,True)
    assert state == start

    def difference(t):
        return phase_path[t][0]-phase_path[t][1]

    holds = {}
    for t in sorted({0,1,1+2*r,1+4*r,HORIZON}):
        holds[t] = difference(t)
    far = arrivals[1]
    return stock, {"r":r, "q":q,"p":p,"first_corr":arrivals,"first_B":first_tags,
                   "source_B":source_events,"left_neighbor_C_changes":emitted_to_left,
                   "reader_B":changes,"contrast_at_cuts":holds,
                   "hold_after_nominal_far":difference(1+4*r)-difference(1+2*r),
                   "hold_after_observed_far":difference(far+2*r)-difference(far)
                       if far is not None and far+2*r <= HORIZON else None,
                   "free_reference_fixed":not changes[2],
                   "near_far_source_states_first_differ":first_source_divergence}


def run():
    rows, pilots = [],[]
    common = None
    for r in (1,2,3,4):
        _,time = run_arm(r,1,1,True)
        pilots.append({"r":r,"first_corr":time["first_corr"],"source_B":time["source_B"][0]})
        for q in (-1,1):
            for p in (-1,1):
                stock,row = run_arm(r,q,p,False)
                if common is None:
                    common = stock
                assert stock == common
                rows.append(row)
    return {"stock":common,"horizon":HORIZON,"pilot":pilots,"rows":rows,
            "one_bond_sign_read":all(
                row["first_corr"][0]==2 and row["first_B"][0]==(1 if row["p"]==row["q"] else 2)
                for row in rows if row["r"]==1)}
