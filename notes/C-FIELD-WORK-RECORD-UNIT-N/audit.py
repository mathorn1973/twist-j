"""Prospective exact audit of a known analytical construction, not the user ZIP."""

from hashlib import sha256
from itertools import product
from pathlib import Path
from types import ModuleType

import primary as a
import challenger as b


LENGTHS = (2, 3, 4, 7, 16)
A_FIELD = ((1, 0, 1, 0), (0, 1, 0, 1), (-2, 1, -1, 1), (1, -3, 1, -2))


def base_adapter():
    path = Path(__file__).resolve().parents[1] / "C-FIELD-FINITE-CHAIN-FIRST-DELIVERY-N" / "audit_challenger.py"
    data = path.read_bytes()
    assert sha256(data).hexdigest() == "eaf429421c7e57c16dd1be97a469cbb63313b48597e44a4efd65a87f9087a267"
    module = ModuleType("unchanged_chain_projection")
    module.__file__ = str(path)
    exec(compile(data, str(path), "exec"), module.__dict__)
    return module


def cell_flat(cell):
    m, spectators, z, r = cell
    return tuple(x for row in m+spectators for x in row)+z+(r,)


def legal(flat, n):
    assert len(flat) == 32*n and all(type(v) is int for v in flat)
    assert all(flat[31*i+30] >= 0 for i in range(n))
    assert all(v >= 0 for v in flat[31*n:-1])
    assert 0 <= flat[-1] < 5


def account(state, flat, n):
    value = a.accounts(state, n)
    assert value == b.accounts(flat, n)
    return value


def checked_step(state, flat, n, baseline, old, cut=None, frozen=None):
    aa = list(a.layers(state, n, cut))
    bb = list(b.layers(flat, n, cut))
    oo = list(old.layers(flat[:-1], n, cut))
    assert len(aa) == len(bb) == len(oo) == 4
    for (kind, x), (_, y), (_, z) in zip(aa, bb, oo):
        out = a.flatten(x, n)
        legal(out, n)
        assert out == tuple(y) and out[:-1] == tuple(z)
        assert account(x, y, n) == baseline
        if frozen is not None:
            assert (x[0][cut+1:], x[1][cut+1:], x[2]) == frozen
        if cut is not None:
            assert x[1][cut] == state[1][cut]
    x, y = aa[-1][1], bb[-1][1]
    assert a.step(x, n, cut, True) == state
    assert a.step(a.step(state, n, cut, True), n, cut) == state
    assert b.step(y, n, cut, True) == tuple(flat)
    assert b.step(b.step(flat, n, cut, True), n, cut) == tuple(flat)
    return x, y


def closed_base(n, w, k, offimage=False):
    """Direct full-coordinate oracle through first base reset, or all offimage times."""
    assert offimage or 0 <= k <= n+1
    v = (0, 0, 1, -2) if offimage else tuple(w)
    for _ in range(k % 5):
        v = tuple(sum(x*y for x, y in zip(row, v)) for row in A_FIELD)
    if not offimage and k == 0:
        x,y,z,t = v
        v = (x-3*y-z-2*t, -3*x+4*y-2*z+t, 5*y+z+2*t, 5*x-5*y+2*z-t)
    x,y,z,t = v
    source_field = (x-y,-x,y,y,z,t)
    ready = (1,-2,1,0)+(0,)*8
    active = (1,0,0,0,0,-1,0,0,0,-1,1,0)
    flat = []
    for i in range(n):
        m = (ready if offimage or k == 0 else active) if i == 0 else (0,)*12
        if i == n-1:
            m = active if not offimage and k == n else ready
        r = 2 if not offimage and 1 <= k <= n-1 and i == k else 0
        flat.extend(m+(0,)*12+(source_field if i == 0 else (0,)*6)+(r,))
    q = (0,)*(n-2)+(2 if not offimage and k == n+1 else 0,)
    return tuple(flat)+q


def local_cases(p):
    fields = (p.Z6,p.join(p.W),p.join(p.mv(p.L,p.W)),p.join((0,0,1,-2)),
              (1,0,0,0,0,0),p.join(p.mv(p.L,p.V)),p.join(p.V))
    matter = (p.R,p.AM,p.ZM,p.AM[1:]+p.AM[:1])
    backgrounds = ((p.ZM,(0,0)), (((1,-1,0,0),(0,2,0,-1),(1,0,-2,0)),(1,-1)))
    count = 0
    for m,z,r,j,bg in product(matter,fields,(0,1,2,3,6,7,10),range(5),backgrounds):
        spectators,static = bg
        cell = (m,spectators,tuple(x+y for x,y in zip(z,p.mv(p.S,static))),r)
        flat = cell_flat(cell)
        for inverse in (False,True):
            out, q = a.local_gate(cell,j,inverse)
            other, v = b.local_gate(flat,j,inverse)
            assert cell_flat(out) == tuple(other) and q == v
            assert a.local_gate(out,q,not inverse) == (cell,j)
            assert b.local_gate(other,v,not inverse) == (flat,j)
            before, after = (out,cell) if inverse else (cell,out)
            event = int(before[0] == p.R and after[0] == p.AM)
            assert q == (j+(-event if inverse else event)) % 5
            assert p.cell_energy(out) == p.cell_energy(cell)
            assert p.rho(out) == p.rho(cell) and p.defect(out) == p.defect(cell)
        count += 1
    start = ((p.R,p.ZM,p.Z6,2),0)
    state = start
    seen = set()
    for k in range(10):
        assert state not in seen
        seen.add(state)
        state = a.local_gate(*state)
        if k == 1:
            assert state[0] == start[0] and state[1] == 1 and state != start
    assert state == start
    return count


def generic_cases(p,old):
    count = 0
    for n in (2,3,7):
        for m,z,r,j in product((p.R,p.AM,p.ZM,p.AM[1:]+p.AM[:1]),
                               (p.Z6,p.join(p.W),(1,0,0,0,0,0)),(0,2,7),range(5)):
            cells = tuple((p.ZM,((i+1,-1,0,0),(0,2,0,-1),(1,0,-2,0)),
                           (i,1,-1,2,-2,1),i+1) for i in range(n))
            cells = cells[:-1]+((m,cells[-1][1],z,r),)
            state = cells,tuple(range(3,n+2)),j
            flat = a.flatten(state,n)
            baseline = account(state,flat,n)
            for cut in (None,)+tuple(range(n-1)):
                checked_step(state,flat,n,baseline,old,cut)
                count += 1
    return count


def main():
    p,old = a.local(),base_adapter()
    p.certificates()
    seeds = tuple(w for w in product(range(-2,3),range(-3,4),range(-2,3),range(-4,5)) if p.active_energy(w) == 1)
    assert len(seeds) == 20
    boundaries = 0
    for n,w in product(LENGTHS,seeds):
        state,flat = a.initial(n,w),b.initial(n,w)
        baseline = account(state,flat,n)
        assert baseline[0] == 42 and baseline[1] == baseline[2] == (0,)*(3*n)
        arrival = first_event = None
        hits = 0
        for k in range(n+8):
            assert a.flatten(state,n) == tuple(flat)
            legal(flat,n)
            assert flat[-1] == hits % 5
            assert a.read_target(state) == b.read_target(flat,n) == int(k >= n)
            if k <= n+1:
                assert flat[:-1] == closed_base(n,w,k)
            if state[0][-1][3] > 0 and arrival is None:
                arrival = k
            if k == n+1:
                assert state[0][-1] == (p.R,p.ZM,p.Z6,0) and state[2] == 1
            boundaries += 1
            if k < n+7:
                c = state[0][-1]
                event = int(c[0] == p.R and p.gate(c)[0] == p.AM)
                hits += event
                if event and first_event is None:
                    first_event = k+1
                state,flat = checked_step(state,flat,n,baseline,old)
        assert (arrival,first_event) == (n-1,n) and 1 <= hits <= 4
    cuts = cut_boundaries = off_boundaries = 0
    for n in LENGTHS:
        for cut in range(n-1):
            state,flat = a.initial(n,p.W),b.initial(n,p.W)
            baseline = account(state,flat,n)
            frozen = state[0][cut+1:],state[1][cut+1:],0
            for k in range(n+8):
                assert a.flatten(state,n) == tuple(flat) and state[2] == 0
                cut_boundaries += 1
                if k < n+7:
                    state,flat = checked_step(state,flat,n,baseline,old,cut,frozen)
            cuts += 1
        state,flat = a.initial(n,p.W,True),b.initial(n,p.W,True)
        baseline = account(state,flat,n)
        assert baseline[0] == 42
        for k in range(n+8):
            assert a.flatten(state,n) == tuple(flat)
            assert tuple(flat[:-1]) == closed_base(n,p.W,k,True) and flat[-1] == 0
            off_boundaries += 1
            if k < n+7:
                state,flat = checked_step(state,flat,n,baseline,old)
    local_count = local_cases(p)
    generic_count = generic_cases(p,old)
    assert (boundaries,cuts,cut_boundaries,off_boundaries,local_count,generic_count) == (1440,27,518,72,1960,2160)
    print("AUDIT PASS: complete work-record unit; NON-CANONICAL candidate-T L1")
    print(f"H=1 seeds: {len(seeds)}; lengths: {len(LENGTHS)}; positive full boundaries: {boundaries}")
    print(f"single cuts: {cuts}; cut boundaries: {cut_boundaries}; offimage boundaries: {off_boundaries}")
    print(f"local full cases: {local_count}; generic full states/cuts: {generic_count}; local period: 10")
    print("first arrival=N-1; first work=first HIT=N; old target reset=N+1")
    print("HIT guaranteed at N..N+7: eight boundaries, seven elapsed steps; no exact reset claim")
    print("energy=42; coordinates=32N; exact old projection; four layers; both full inverses pass")
    print("Known proof audited by new code; original ZIP unverified; physical realization remains open.")


if __name__ == "__main__":
    main()
