"""Exact cubical chain machinery on Z^4.

face_boundary, faces_of_edge, and chain_d are byte-compatible with
reproduce/photon-electron/verify.py:

    edge  e = (v, d)        v in Z^4, direction d in 0..3
    face  f = (v, a, b)     a < b
    partial f(v,a,b) = e_a(v) + e_b(v+e_a) - e_a(v+e_b) - e_b(v)

edge_d has no public counterpart; it is the unique 1-boundary
(edge (v,d) oriented v -> v+e_d, tail -c, head +c) making the complex
a chain complex with the shared face boundary.  All arithmetic exact
integers."""


def unit4(d, s=1):
    v = [0, 0, 0, 0]
    v[d] = s
    return tuple(v)


def addv(a, b):
    return tuple(x + y for x, y in zip(a, b))


def face_boundary(f):
    v, a, b = f
    return (((v, a), 1), ((addv(v, unit4(a)), b), 1),
            ((addv(v, unit4(b)), a), -1), ((v, b), -1))


def faces_of_edge(e):
    v, d = e
    out = []
    for j in range(4):
        if j == d:
            continue
        a, b = min(d, j), max(d, j)
        out.append((v, a, b))
        out.append((addv(v, unit4(j, -1)), a, b))
    return out


def chain_d(nfaces):
    """boundary of a 2-chain given as {face: coeff}."""
    dn = {}
    for f, c in nfaces.items():
        for e, inc in face_boundary(f):
            dn[e] = dn.get(e, 0) + c * inc
    return {e: c for e, c in dn.items() if c != 0}


def edge_d(jedges):
    """boundary of a 1-chain given as {edge: coeff} -> {vertex: coeff}."""
    dv = {}
    for (v, d), c in jedges.items():
        w = addv(v, unit4(d))
        dv[w] = dv.get(w, 0) + c
        dv[v] = dv.get(v, 0) - c
    return {v: c for v, c in dv.items() if c != 0}


def is_ternary(chain):
    return all(c in (-1, 1) for c in chain.values())


def check_connected_edge_simple(jedges):
    """j must be ternary and closed with connected support; then the
    directed multigraph (each support edge once, oriented by sign) has
    in-degree = out-degree everywhere, so one closed walk traverses
    every support edge exactly once (edge-simple).  Returns (L, walk)
    where walk is an explicit Hierholzer traversal certificate."""
    assert is_ternary(jedges), "not ternary"
    assert edge_d(jedges) == {}, "not closed"
    out = {}
    for (v, d), c in jedges.items():
        w = addv(v, unit4(d))
        a, b = (v, w) if c > 0 else (w, v)
        out.setdefault(a, []).append((b, (v, d)))
        out.setdefault(b, [])
    # connectivity of the support graph
    start = next(iter(out))
    seen = {start}
    stack = [start]
    und = {}
    for (v, d) in jedges:
        w = addv(v, unit4(d))
        und.setdefault(v, []).append(w)
        und.setdefault(w, []).append(v)
    while stack:
        v = stack.pop()
        for w in und[v]:
            if w not in seen:
                seen.add(w)
                stack.append(w)
    assert len(seen) == len(und), "disconnected support"
    # Hierholzer closed walk using every directed edge once
    it = {v: 0 for v in out}
    st = [start]
    est = []
    circuit = []
    while st:
        v = st[-1]
        if it[v] < len(out[v]):
            w, e = out[v][it[v]]
            it[v] += 1
            st.append(w)
            est.append(e)
        else:
            st.pop()
            if est:
                circuit.append(est.pop())
    circuit.reverse()
    assert len(circuit) == len(jedges), "walk misses edges"
    assert len(set(circuit)) == len(circuit), "edge reused"
    return len(jedges), circuit
