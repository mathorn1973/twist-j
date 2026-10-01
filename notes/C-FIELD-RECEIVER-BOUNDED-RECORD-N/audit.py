#!/usr/bin/env python3
"""Exact audit of the prospectively frozen receiver record candidate.

Universal claims rest on PROOF.md. Two representations reuse independently
authored public predecessor arithmetic; no fresh clean-room claim is made.
"""

from hashlib import sha256
import importlib.util
from itertools import product
from pathlib import Path

import audit_challenger as challenger

HERE = Path(__file__).resolve().parent
PREDECESSOR = HERE.parent / "C-FIELD-THREE-CELL-DELAYED-TRANSFER-N"
PRIMARY_SHA = "42ec10cd001028ec126045647eea89347ec12bbf3612c40e1aa204ab77913a59"
CONNECTED_N = tuple(range(2, 17)) + (31, 32, 33, 64)
CUT_N = tuple(range(2, 17)) + (32,)
A_FIELD = ((1, 0, 1, 0), (0, 1, 0, 1), (-2, 1, -1, 1), (1, -3, 1, -2))


def load_primary():
    path = PREDECESSOR / "verify.py"
    data = path.read_bytes()
    assert sha256(data).hexdigest() == PRIMARY_SHA, "predecessor changed"
    spec = importlib.util.spec_from_file_location("pinned_local_primary", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


p = load_primary()
PHASES = (p.AM, p.AM[1:] + p.AM[:1], p.AM[2:] + p.AM[:2])


def initial(n, w):
    assert n >= 2
    cells = [(p.ZM, p.ZM, p.Z6, 0) for _ in range(n)]
    cells[0] = (p.R, p.ZM, p.join(p.mv(p.L, w)), 0)
    cells[-1] = (p.R, p.ZM, p.Z6, 0)
    return tuple(cells) + (0,) * (n - 1)


def flatten(state, n):
    return tuple(v for m, b, z, r in state[:n]
                 for v in tuple(x for row in m + b for x in row) + z + (r,)) + state[n:]


def record_gate(cell, inverse=False):
    m, b, z, r = cell
    if m in PHASES:
        m = PHASES[(PHASES.index(m) + (-1 if inverse else 1)) % 3]
    return m, b, z, r


def read_target(state, n):
    return int(state[n-1][0] in PHASES)


def layers(state, n, cut=None, inverse=False, record=True):
    assert len(state) == 2*n-1
    assert cut is None or 0 <= cut < n-1
    order = ("FBAKG" if inverse else "GKABF") if record else ("FBAG" if inverse else "GABF")
    for kind in order:
        out = list(state)
        if kind in "GF":
            for i in range(n):
                out[i] = p.gate(state[i]) if kind == "G" else p.free(state[i], inverse)
        elif kind == "K":
            if record:
                out[n-1] = record_gate(state[n-1], inverse)
        else:
            for j in range(n-1):
                if j != cut:
                    i = j if kind == "A" else j+1
                    out[i] = p.with_resource(state[i], state[n+j])
                    out[n+j] = state[i][3]
        state = tuple(out)
        yield state


def step(state, n, cut=None, inverse=False, record=True):
    for state in layers(state, n, cut, inverse, record):
        pass
    return state


def accounts(state, n):
    cells = state[:n]
    return (sum(p.cell_energy(c) for c in cells) + sum(state[n:]),
            tuple(v for c in cells for v in p.rho(c)),
            tuple(v for c in cells for v in p.defect(c)),
            tuple(v for c in cells for row in c[1] for v in row),
            tuple(v for c in cells for v in p.vector_sum(c[0])))


def expected(n, w, k, record=True):
    """Closed formula, not a simulation of the network gates or contacts."""
    assert 0 <= k <= (n+3 if record else n+1)
    phase = tuple(w)
    # A_field^5=I is separately certified; the field oracle uses its matrix.
    for _ in range(k % 5):
        phase = tuple(sum(a*b for a, b in zip(row, phase)) for row in A_FIELD)
    if k == 0:
        a, b, c, d = phase
        phase = (a-3*b-c-2*d, -3*a+4*b-2*c+d,
                 5*b+c+2*d, 5*a-5*b+2*c-d)
    a, b, c, d = phase
    raw_source = (a-b, -a, b, b, c, d)
    ready = (1, -2, 1, 0) + (0,)*8
    active = (1, 0, 0, 0, 0, -1, 0, 0, 0, -1, 1, 0)
    flat = []
    for i in range(n):
        matter = (ready if k == 0 else active) if i == 0 else (0,)*12
        if i == n-1:
            phase_index = k-n+1
            rotations = (active, active[4:]+active[:4], active[8:]+active[:8])
            matter = rotations[phase_index % 3] if record and n <= k <= n+2 else (active if not record and k == n else ready)
        resource = 2 if 1 <= k <= n-1 and i == k else 0
        flat.extend(matter + (0,)*12 + (raw_source if i == 0 else (0,)*6) + (resource,))
    channels = (0,)*(n-2) + (2 if k == (n+3 if record else n+1) else 0,)
    return tuple(flat) + channels


def legal(flat, n):
    assert len(flat) == 32*n-1
    assert all(type(x) is int for x in flat)
    assert all(flat[31*i+30] >= 0 for i in range(n))
    assert all(x >= 0 for x in flat[31*n:])


def both_accounts(state, other, n):
    first = accounts(state, n)
    assert first == challenger.accounts(other, n)
    return first


def checked_step(state, other, n, baseline, cut=None, frozen_right=None, record=True):
    left_layers = list(layers(state, n, cut, record=record))
    right_layers = [s for _, s in challenger.layers(other, n, cut, record=record)]
    assert len(left_layers) == len(right_layers) == (5 if record else 4)
    for new, other_new in zip(left_layers, right_layers):
        flat = flatten(new, n)
        legal(flat, n)
        assert flat == tuple(other_new)
        assert both_accounts(new, other_new, n) == baseline
        if cut is not None:
            assert new[n+cut] == state[n+cut]
            if frozen_right is not None:
                assert (new[cut+1:n], new[n+cut+1:]) == frozen_right
    final, other_final = left_layers[-1], right_layers[-1]
    assert step(final, n, cut, True, record) == state
    assert step(step(state, n, cut, True, record), n, cut, record=record) == state
    assert tuple(challenger.step(other_final, n, cut, True, record)) == tuple(other)
    assert tuple(challenger.step(challenger.step(other, n, cut, True, record), n, cut, record=record)) == tuple(other)
    if cut is None:
        post_g = left_layers[0]
        r = tuple(cell[3] for cell in post_g[:n])
        q = post_g[n:]
        expected_resources = (q[0],) + r[:-1] + q[1:] + (r[-1],)
        post_contacts = left_layers[3 if record else 2]
        actual = tuple(cell[3] for cell in post_contacts[:n]) + post_contacts[n:]
        assert actual == expected_resources
    return final, other_final


def seeds():
    result = []
    for w in product(range(-2, 3), range(-3, 4), range(-2, 3), range(-4, 5)):
        assert p.active_energy(w) == challenger._local().hform(w)
        if p.active_energy(w) == 1:
            result.append(w)
    assert result and p.W in result
    return tuple(result)


def symbolic_contacts(n):
    r = [f"r{i}" for i in range(n)]
    q = [f"q{i}" for i in range(n-1)]
    before = r + q
    for i in range(n-1):
        r[i], q[i] = q[i], r[i]
    for i in range(n-1):
        q[i], r[i+1] = r[i+1], q[i]
    assert r + q == ["q0"] + [f"r{i}" for i in range(n-1)] + [f"q{i}" for i in range(1, n-1)] + [f"r{n-1}"]
    assert sorted(r + q) == sorted(before)
    for i in range(n-1):
        q[i], r[i+1] = r[i+1], q[i]
    for i in range(n-1):
        r[i], q[i] = q[i], r[i]
    assert r + q == before


def occupied_contacts():
    cases = 0
    for n in range(2, 65):
        symbolic_contacts(n)
        state = tuple((p.ZM, p.ZM, p.Z6, i) for i in range(n)) + tuple(range(n, 2*n-1))
        other = flatten(state, n)
        baseline = both_accounts(state, other, n)
        for cut in (None,) + tuple(range(n-1)):
            after = step(state, n, cut)
            flat = flatten(after, n)
            assert flat == tuple(challenger.step(other, n, cut))
            assert both_accounts(after, flat, n) == baseline
            assert step(after, n, cut, True) == state
            assert step(step(state, n, cut, True), n, cut) == state
            assert tuple(challenger.step(flat, n, cut, True)) == other
            assert tuple(challenger.step(challenger.step(other, n, cut, True), n, cut)) == other
            resources = tuple(c[3] for c in after[:n]) + after[n:]
            assert sorted(resources) == list(range(2*n-1))
            if cut is None:
                assert resources == (n,) + tuple(range(n-1)) + tuple(range(n+1, 2*n-1)) + (n-1,)
            else:
                assert after[n+cut] == state[n+cut]
            cases += 1
    return cases


def generic_states():
    """Fixed off-preparation backgrounds; no inferred robustness claim."""
    cases = 0
    for n in (2, 3, 12):
        for m in (p.ZM, p.R) + PHASES + ((p.AM[0],)*3,):
            for z in (p.Z6, p.join(p.W), p.join(p.mv(p.L, p.W))):
                for r in (0, 2, 7):
                    cells = tuple((p.ZM,
                                   ((i+1, -1, 0, 0), (0, 2, 0, -1), (1, 0, -2, 0)),
                                   (i, 1, -1, 2, -2, 1), i+1) for i in range(n))
                    target = (m, cells[-1][1], z, r)
                    state = cells[:-1] + (target,) + tuple(range(3, n+2))
                    other = flatten(state, n)
                    baseline = both_accounts(state, other, n)
                    assert record_gate(record_gate(record_gate(target))) == target
                    assert record_gate(record_gate(target, True)) == target
                    assert record_gate(record_gate(target), True) == target
                    for cut in (None,) + tuple(range(n-1)):
                        checked_step(state, other, n, baseline, cut)
                        cases += 1
    return cases


def main():
    p.certificates()
    ws = seeds()
    assert len(ws) == 20
    boundaries = 0
    for n in CONNECTED_N:
        for w in ws:
            state, other = initial(n, w), challenger.initial(n, w)
            baseline = both_accounts(state, other, n)
            assert baseline[0] == 41
            assert baseline[1] == baseline[2] == (0,)*(3*n)
            arrival = reaction = None
            readable = []
            for k in range(n+4):
                flat = flatten(state, n)
                assert flat == tuple(other) == expected(n, w, k), (n, w, k)
                legal(flat, n)
                assert both_accounts(state, other, n) == baseline
                boundaries += 1
                bit = read_target(state, n)
                assert bit == challenger.read_target(other, n) == int(n <= k <= n+2)
                if bit:
                    readable.append(k)
                if state[n-1][3] and arrival is None:
                    arrival = k
                if k < n+3:
                    post_g = next(layers(state, n))[n-1]
                    if post_g[0] != state[n-1][0] and reaction is None:
                        reaction = k+1
                        assert post_g == (p.AM, p.ZM, p.Z6, 0)
                    state, other = checked_step(state, other, n, baseline)
            assert (arrival, reaction) == (n-1, n)
            assert readable == [n, n+1, n+2]
    cut_cases = cut_boundaries = 0
    for n in CUT_N:
        for cut in range(n-1):
            state, other = initial(n, p.W), challenger.initial(n, p.W)
            baseline = both_accounts(state, other, n)
            frozen = (state[cut+1:n], state[n+cut+1:])
            for k in range(n+4):
                assert flatten(state, n) == tuple(other)
                assert (state[cut+1:n], state[n+cut+1:]) == frozen
                assert state[n+cut] == 0
                assert read_target(state, n) == challenger.read_target(other, n) == 0
                cut_boundaries += 1
                if k < n+3:
                    state, other = checked_step(state, other, n, baseline, cut, frozen)
            cut_cases += 1
    controls = 0
    for n in CONNECTED_N:
        state, other = initial(n, p.W), challenger.initial(n, p.W)
        ready = state[n-1]
        baseline = both_accounts(state, other, n)
        for k in range(n+2):
            assert flatten(state, n) == tuple(other) == expected(n, p.W, k, False)
            assert read_target(state, n) == challenger.read_target(other, n) == int(k == n)
            if k < n+1:
                state, other = checked_step(state, other, n, baseline, record=False)
        assert state[n-1] == ready
        assert state[-1] == 2
        controls += 1
    occupied = occupied_contacts()
    generic = generic_states()
    assert (boundaries, cut_cases, cut_boundaries, controls, occupied, generic) == (7420, 151, 2956, 19, 2079, 918)
    print("AUDIT PASS: receiver bounded record; NON-CANONICAL candidate-T L1")
    print(f"H=1 seeds: {len(ws)}; connected lengths: {len(CONNECTED_N)}; full boundaries: {boundaries}")
    print(f"single-cut cases: {cut_cases}; cut boundaries: {cut_boundaries}; identity-K controls: {controls}")
    print(f"occupied contact cases: {occupied}; generic background cases: {generic}")
    print("first arrival=N-1; first reaction=first read=N; read=1 at N,N+1,N+2; first reset=N+3")
    print("energy=41; coordinates=32N-1; five layers; stored three-state phase mechanism")
    print("full-state oracle, two adapters, layer invariants and both inverse identities pass")
    print("All-N and all-time cut conclusions rest on the proof; no permanent or robust memory claim.")


if __name__ == "__main__":
    main()
