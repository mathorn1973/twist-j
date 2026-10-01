#!/usr/bin/env python3
"""Local exact formula audit; universal claims are proved in PROOF.md.

Known user-supplied targets; no formal public execution or fresh clean-room
claim. Reuses pinned local arithmetic, never the old fixed-three-cell runner.
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


def initial(n, w):
    assert n >= 2
    cells = [(p.ZM, p.ZM, p.Z6, 0) for _ in range(n)]
    cells[0] = (p.R, p.ZM, p.join(p.mv(p.L, w)), 0)
    cells[-1] = (p.R, p.ZM, p.Z6, 0)
    return tuple(cells) + (0,) * (n - 1)


def flatten(state, n):
    return tuple(v for m, b, z, r in state[:n]
                 for v in tuple(x for row in m + b for x in row) + z + (r,)) + state[n:]


def layers(state, n, cut=None, inverse=False):
    assert len(state) == 2*n-1
    assert cut is None or 0 <= cut < n-1
    order = "FBAG" if inverse else "GABF"
    for kind in order:
        out = list(state)
        if kind in "GF":
            for i in range(n):
                out[i] = p.gate(state[i]) if kind == "G" else p.free(state[i], inverse)
        else:
            for j in range(n-1):
                if j != cut:
                    i = j if kind == "A" else j+1
                    out[i] = p.with_resource(state[i], state[n+j])
                    out[n+j] = state[i][3]
        state = tuple(out)
        yield state


def step(state, n, cut=None, inverse=False):
    for state in layers(state, n, cut, inverse):
        pass
    return state


def accounts(state, n):
    cells = state[:n]
    return (sum(p.cell_energy(c) for c in cells) + sum(state[n:]),
            tuple(v for c in cells for v in p.rho(c)),
            tuple(v for c in cells for v in p.defect(c)),
            tuple(v for c in cells for row in c[1] for v in row),
            tuple(v for c in cells for v in p.vector_sum(c[0])))


def expected(n, w, k):
    """Closed formula, not a simulation of the network gates or contacts."""
    assert 0 <= k <= n
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
            matter = active if k == n else ready
        resource = 2 if 1 <= k <= n-1 and i == k else 0
        flat.extend(matter + (0,)*12 + (raw_source if i == 0 else (0,)*6) + (resource,))
    return tuple(flat) + (0,)*(n-1)


def legal(flat, n):
    assert len(flat) == 32*n-1
    assert all(type(x) is int for x in flat)
    assert all(flat[31*i+30] >= 0 for i in range(n))
    assert all(x >= 0 for x in flat[31*n:])


def both_accounts(state, other, n):
    first = accounts(state, n)
    assert first == challenger.accounts(other, n)
    return first


def checked_step(state, other, n, baseline, cut=None, frozen_right=None):
    left_layers = list(layers(state, n, cut))
    right_layers = [s for _, s in challenger.layers(other, n, cut)]
    assert len(left_layers) == len(right_layers) == 4
    for new, other_new in zip(left_layers, right_layers):
        flat = flatten(new, n)
        legal(flat, n)
        assert flat == tuple(other_new)
        assert both_accounts(new, other_new, n) == baseline
        if cut is not None:
            assert new[n+cut] == state[n+cut]
            assert (new[cut+1:n], new[n+cut+1:]) == frozen_right
    final, other_final = left_layers[-1], right_layers[-1]
    assert step(final, n, cut, True) == state
    assert step(step(state, n, cut, True), n, cut) == state
    assert tuple(challenger.step(other_final, n, cut, True)) == tuple(other)
    assert tuple(challenger.step(challenger.step(other, n, cut, True), n, cut)) == tuple(other)
    if cut is None:
        post_g = left_layers[0]
        r = tuple(cell[3] for cell in post_g[:n])
        q = post_g[n:]
        expected_resources = (q[0],) + r[:-1] + q[1:] + (r[-1],)
        post_contacts = left_layers[2]
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


def main():
    p.certificates()
    ws = seeds()
    digest = sha256()
    boundaries = 0
    for n in CONNECTED_N:
        for w in ws:
            state, other = initial(n, w), challenger.initial(n, w)
            baseline = both_accounts(state, other, n)
            assert baseline[0] == 41
            assert baseline[1] == baseline[2] == (0,)*(3*n)
            arrival = reaction = None
            for k in range(n+1):
                flat = flatten(state, n)
                assert flat == tuple(other) == expected(n, w, k), (n, w, k)
                legal(flat, n)
                assert both_accounts(state, other, n) == baseline
                digest.update((repr((n, w, k, flat)) + "\n").encode("ascii"))
                boundaries += 1
                if state[n-1][3] and arrival is None:
                    arrival = k
                if state[n-1][0] != p.R and reaction is None:
                    reaction = k
                if k < n:
                    state, other = checked_step(state, other, n, baseline)
            assert (arrival, reaction) == (n-1, n)
    cut_cases = cut_boundaries = 0
    for n in CUT_N:
        for cut in range(n-1):
            state, other = initial(n, p.W), challenger.initial(n, p.W)
            baseline = both_accounts(state, other, n)
            frozen = (state[cut+1:n], state[n+cut+1:])
            for k in range(n+3):
                assert flatten(state, n) == tuple(other)
                assert (state[cut+1:n], state[n+cut+1:]) == frozen
                assert state[n+cut] == 0
                cut_boundaries += 1
                if k < n+2:
                    state, other = checked_step(state, other, n, baseline, cut, frozen)
            cut_cases += 1
    occupied = occupied_contacts()
    print("LOCAL AUDIT PASS: NON-CANONICAL candidate-T L1; no public computation gate")
    print(f"H=1 seeds: {len(ws)}; connected lengths: {len(CONNECTED_N)}; full boundaries: {boundaries}")
    print(f"single-cut cases: {cut_cases}; cut boundaries: {cut_boundaries}; occupied contact cases: {occupied}")
    print("first boundary arrival=N-1; first target reaction=N; energy=41; coordinates=32N-1")
    print("two generic full-state adapters agree; layer invariants and both inverse identities pass")
    print("connected full-state SHA-256: " + digest.hexdigest())
    print("All-N and all-time cut conclusions rest on the proof, not these finite checks.")


if __name__ == "__main__":
    main()
