#!/usr/bin/env python3
"""CW-ALG-1 bounded verifier. Import-safe; no scientific work at import time.

This verifies the finite checks in CHECK-MAP.md, not the expanded compiler.
Full native state: (x0,x1,x2,x3,rx,y0,y1,y2,y3,ry,eta,qx,qy).
Piston interface: p=(x0,x1,x2,x3,y0,y1,y2,y3). All arithmetic is in F5.
"""

from collections import Counter, deque
from functools import lru_cache
from itertools import permutations, product
from pathlib import Path
import hashlib
import json
import sys

VERSION = "CW-ALG-1"
SPEC_SHA256 = "bcf48fbece05e445a1e6d958b749dfc0ff4d0b6f05f702d699f08fb142bfa656"
PREREG_SHA256 = "fe924d5074700aeaabf427e3071844a65a407de37ed8e4335f115932a4eb587c"
TERMINALS = ("a_x", "b_x", "c_x", "d_x", "e_x", "a_y", "b_y", "c_y", "d_y", "e_y", "P", "P^-1", "Q", "Q^-1", "W_a", "W_b")
MACRO_ORDER = ("bar_a_x", "bar_b_x", "bar_c_x", "bar_d_x", "bar_e_x", "bar_a_y", "bar_b_y", "bar_c_y", "bar_d_y", "bar_e_y", "P", "P^-1", "Q", "Q^-1", "W_a", "W_b")
WALSH = ((1, 1, 1, 1), (1, 1, -1, -1), (1, -1, 1, -1), (1, -1, -1, 1))
M = ((0, 3, 0), (4, 4, 4), (0, 3, 3))
MI = ((0, 4, 3), (2, 0, 0), (3, 0, 2))
B_READ = ((1, 4, 2), (4, 0, 1), (3, 4, 4))
L5 = ((3, 3, 2), (3, 4, 2), (3, 2, 0))
K = ((0, 0, 0, 3), (0, 0, 2, 0), (0, 2, 0, 0), (3, 0, 0, 0))
WORK = (4, 1, 9)  # xi1=rx, xi2=vx, xi3=ry, in 10-dimensional Walsh order.
EXTERNAL = (0, 5, 2, 7, 6, 3, 8)
L_ZERO = (1, 0, 1, 0, 0, 0, 1)
PI_ZERO = (0, 0, 0)


class AuditFailure(Exception):
    def __init__(self, assertion, witness):
        super().__init__(assertion)
        self.assertion = assertion
        self.witness = witness


def require(condition, assertion, witness=None):
    if not condition:
        raise AuditFailure(assertion, witness)


def eye(n):
    return tuple(tuple(int(i == j) for j in range(n)) for i in range(n))


def matmul(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(len(b))) % 5
                       for j in range(len(b[0]))) for i in range(len(a)))


def matvec(a, v):
    return tuple(sum(x * y for x, y in zip(row, v)) % 5 for row in a)


def matinv(a):
    n = len(a)
    rows = [list(a[i]) + list(eye(n)[i]) for i in range(n)]
    for j in range(n):
        pivot = next((i for i in range(j, n) if rows[i][j] % 5), None)
        if pivot is None:
            raise ValueError("singular matrix")
        rows[j], rows[pivot] = rows[pivot], rows[j]
        inv = pow(rows[j][j], -1, 5)
        rows[j] = [(x * inv) % 5 for x in rows[j]]
        for i in range(n):
            if i != j:
                c = rows[i][j]
                rows[i] = [(x - c * y) % 5 for x, y in zip(rows[i], rows[j])]
    return tuple(tuple(row[n:]) for row in rows)


def matpow(a, n):
    if n < 0:
        return matpow(matinv(a), -n)
    out = eye(len(a))
    for _ in range(n):
        out = matmul(out, a)
    return out


def det2(a):
    return (a[0] * a[3] - a[1] * a[2]) % 5


def mul2(a, b):
    return ((a[0]*b[0]+a[1]*b[2]) % 5, (a[0]*b[1]+a[1]*b[3]) % 5,
            (a[2]*b[0]+a[3]*b[2]) % 5, (a[2]*b[1]+a[3]*b[3]) % 5)


def gram(p):
    x, y = p[:4], p[4:]
    return (det2(x), (3*(x[0]*y[3]+x[3]*y[0])+2*(x[1]*y[2]+x[2]*y[1])) % 5, det2(y))


def kappa(g):
    return (g[1]*g[1]-g[0]*g[2]) % 5


def width(g):
    """Input is the three-coordinate Gram, not kappa."""
    return (5, 6, 4, 4, 6)[kappa(g)]


def orbit_width(g):
    return 5 if g[0] == 2*g[1] % 5 and g[2] == 3*g[1] % 5 else 6


def target(g):
    return (3*g[1] % 5, 4*sum(g) % 5, 3*(g[1]+g[2]) % 5)


def target_inverse(g):
    return ((4*g[1]-2*g[2]) % 5, 2*g[0] % 5, (2*g[2]-2*g[0]) % 5)


def chart(g):
    for t in range(3):
        a = (g[0]+2*t*g[1]+t*t*g[2]) % 5
        if a:
            return t, a, (g[1]+t*g[2]) % 5
    raise ValueError("chart undefined for zero Gram")


def atlas_encode(p):
    g = gram(p)
    if g == PI_ZERO:
        return None
    t, a, b = chart(g)
    ia = pow(a, -1, 5)
    x, y = p[:4], p[4:]
    xx = tuple((u+t*v) % 5 for u, v in zip(x, y))
    l = (xx[0], xx[1]*ia % 5, xx[2], xx[3]*ia % 5)
    li = (l[3], -l[1] % 5, -l[2] % 5, l[0])
    z = mul2(li, y)
    xi, lam, mu = (a*z[0]-b) % 5, a*z[1] % 5, z[2]
    require(det2(l) == 1 and z[3] == (b-xi) % 5 and (xi*xi+lam*mu) % 5 == kappa(g),
            "atlas.conic", p)
    j, n = (lam-1, xi) if lam else (4+int(xi >= 3), mu)
    require(0 <= j < width(g), "atlas.slot_range", (p, j))
    return g, l, n, j


def atlas_decode(g, l, n, j):
    if g == PI_ZERO or not 0 <= j < width(g) or not 0 <= n < 5 or det2(l) != 1:
        raise ValueError("invalid atlas coordinates")
    t, a, b = chart(g)
    ia = pow(a, -1, 5)
    kap = kappa(g)
    if j < 4:
        lam, xi = j+1, n
        mu = (kap-n*n)*pow(lam, -1, 5) % 5
    else:
        lam, mu = 0, n
        xi = (0, 1, 0, 0, 2)[kap]
        if j == 5:
            xi = -xi % 5
    z = ((xi+b)*ia % 5, lam*ia % 5, mu, (b-xi) % 5)
    y = mul2(l, z)
    xx = (l[0], a*l[1] % 5, l[2], a*l[3] % 5)
    x = tuple((u-t*v) % 5 for u, v in zip(xx, y))
    return x+y


def pi_step(p, eta, inverse=False):
    encoded = atlas_encode(p)
    if encoded is None:
        return tuple(p), eta
    g, l, n, j = encoded
    ell = j+width(g)*eta
    if ell >= orbit_width(g):
        return tuple(p), eta
    gp = target_inverse(g) if inverse else target(g)
    mp = width(gp)
    ep = int(ell >= mp)
    return atlas_decode(gp, l, n, ell-mp*ep), ep


def pi(p, eta):
    return pi_step(p, eta, False)


def pi_inverse(p, eta):
    return pi_step(p, eta, True)


def reachable(p, eta):
    encoded = atlas_encode(p)
    if encoded is None:
        return eta == 0
    g, _, _, j = encoded
    return j+width(g)*eta < orbit_width(g)


def walsh(p):
    return matvec(WALSH, p)


def unwalsh(w):
    return tuple(4*x % 5 for x in matvec(tuple(zip(*WALSH)), w))


def native_cell(c, letter):
    """Independent direct piston implementation; c=(p4,q,r)."""
    p0, p1, p2, p3, q, r = c
    if letter == "a":
        out = (p1, p0, p3, p2, q, r)
    elif letter == "b":
        out = (-p2, -p3, -p0, -p1, -q, -r)
    elif letter == "c":
        out = (2-p2, 1+r-p3, 2-p0, 1-r-p1, 1-q, -r)
    elif letter in ("d", "e"):
        out = (2-p0, 1-p1, 3-p2, 4-p3, (1 if letter == "d" else 2)-q, 1-r)
    else:
        raise ValueError("unknown cell letter")
    return tuple(x % 5 for x in out)


def state_piston(state):
    return tuple(state[:4])+tuple(state[5:9])


def make_state(p, rx=0, ry=0, eta=0, qx=0, qy=0):
    return tuple(p[:4])+(rx,)+tuple(p[4:])+(ry, eta, qx, qy)


def native_apply(state, leaf):
    z = list(state)
    if leaf in ("P", "P^-1", "Q", "Q^-1"):
        sign = -1 if leaf.endswith("^-1") else 1
        src, dst = ((0, 1, 2, 3, 4, 11), (5, 6, 7, 8, 9, 12))
        if leaf.startswith("Q"):
            src, dst = dst, src
        for a, b in zip(src, dst):
            z[b] = (z[b]+sign*z[a]) % 5
        return tuple(z)
    if leaf in ("W_a", "W_b"):
        h = gram(state_piston(state))[1]
        if not h:
            return tuple(state)
        sigma = int(h >= 3)
        if sigma ^ z[10]:
            z = list(native_apply(native_apply(z, leaf[-1]+"_y"), leaf[-1]+"_x"))
        z[10] = sigma
        return tuple(z)
    letter, cell = leaf.split("_")
    indices = (0, 1, 2, 3, 11, 4) if cell == "x" else (5, 6, 7, 8, 12, 9)
    out = native_cell(tuple(z[i] for i in indices), letter)
    for i, value in zip(indices, out):
        z[i] = value
    return tuple(z)


# Exact syntax DAG. No factor-equivalence simplification or exponent reduction.
def leaf(name):
    if name not in TERMINALS:
        raise ValueError("non-native terminal")
    return ("leaf", name)


def seq(*words):
    return ("mul", tuple(words))


def inv(word):
    return ("inv", word)


def power(word, n):
    return ("pow", word, n)


def comm(a, b):
    return seq(a, b, inv(a), inv(b))


def conjugate(a, b):
    return seq(a, b, inv(a))


def native_word_apply(word, state, budget=10000):
    """Only for bounded words; refuses unbudgeted expansion."""
    remaining = [budget]

    def visit(w, z, reverse=False):
        kind = w[0]
        if kind == "leaf":
            remaining[0] -= 1
            if remaining[0] < 0:
                raise ValueError("native leaf budget exceeded")
            name = w[1]
            if reverse and name in ("P", "P^-1", "Q", "Q^-1"):
                name = name[:-3] if name.endswith("^-1") else name+"^-1"
            return native_apply(z, name)
        if kind == "inv":
            return visit(w[1], z, not reverse)
        if kind == "pow":
            for _ in range(abs(w[2])):
                z = visit(w[1], z, reverse ^ (w[2] < 0))
            return z
        for child in (w[1] if reverse else reversed(w[1])):
            z = visit(child, z, reverse)
        return z

    return visit(word, tuple(state))


@lru_cache(maxsize=None)
def bar(letter, cell):
    raw = leaf(letter+"_"+cell)
    tq = seq(leaf("e_"+cell), leaf("d_"+cell))
    if letter in ("a", "b"):
        return raw
    return seq(power(tq, -2 if letter == "e" else -1), raw)


def small_translations():
    p, q = leaf("P"), leaf("Q")
    ys = {}
    for letter in ("c", "d"):
        dg = seq(bar(letter, "x"), bar(letter, "y"))
        ys[letter] = seq(dg, inv(p), dg, p)
    ac = conjugate(leaf("a_y"), ys["c"])
    ad = conjugate(leaf("a_y"), ys["d"])
    bd = conjugate(leaf("b_y"), ys["d"])
    s = seq(power(ys["c"], 3), power(ac, 3))
    u = seq(power(ys["c"], 4), ac)
    t = seq(ad, inv(ys["d"]))
    r = seq(power(bd, 2), power(ys["d"], -2))
    v = seq(ys["d"], power(t, -2), inv(r))
    y_words = (s, v, u, t, r)
    return tuple(comm(q, word) for word in y_words)+y_words


def tau(vector, translations):
    return seq(*(power(translations[i], int(v) % 5) for i, v in enumerate(vector)))


def unit(n, i, value=1):
    return tuple(value if j == i else 0 for j in range(n))


def signed_rotation_data():
    j12 = ((0, 4, 0), (1, 0, 0), (0, 0, 1))
    j23 = ((1, 0, 0), (0, 0, 4), (0, 1, 0))
    generators = (j12, matinv(j12), j23, matinv(j23))
    # Append on the right so path labels have exactly the SPEC string order.
    paths = {eye(3): ()}
    queue = deque([eye(3)])
    while queue:
        a = queue.popleft()
        for i, b in enumerate(generators):
            ab = matmul(a, b)
            if ab not in paths:
                paths[ab] = paths[a]+(i,)
                queue.append(ab)
    chosen = {}
    for i in range(3):
        for j in range(3):
            if i == j:
                continue
            choices = [(len(w), w, a) for a, w in paths.items()
                       if a[i][0] in (1, 4) and a[j][1] in (1, 4)]
            _, word, a = min(choices)
            chosen[(i, j)] = (word, 1 if a[i][0] == 1 else -1, 1 if a[j][1] == 1 else -1, a)
    return generators, paths, chosen


class Grammar:
    """Finite DAG of the seed/atom grammar, never the gigantic CW output."""
    def __init__(self):
        self.translations = small_translations()
        self.ea = seq(leaf("W_a"), leaf("a_x"), leaf("a_y"), leaf("W_a"))
        self.eb = seq(leaf("W_b"), leaf("b_x"), leaf("b_y"), leaf("W_b"))
        self.k0 = seq(self.ea, self.eb)
        self.z = {r: power(comm(self.k0, self.translations[r]), 2) for r in (4, 9)}
        h0 = seq(tau((-1, 0, -2, 0, 0, 0, 0, 0, 0, 0), self.translations), bar("c", "x"), leaf("b_x"))
        self.n21 = seq(h0, leaf("a_x"), h0, leaf("a_x"))
        self.n23 = inv(comm(leaf("Q"), self.n21))
        self.j12 = seq(self.n21, inv(self.base(4, 1, 1)), self.n21)
        self.j23 = seq(self.base(9, 1, 1), inv(self.n23), self.base(9, 1, 1))
        self.rotation_generators, self.rotation_paths, self.rotations = signed_rotation_data()
        controls = tuple(zip(EXTERNAL, L_ZERO))
        self.f = self.indicator_product(0, 1, controls+((WORK[2], 0),))
        self.g = self.indicator_product(2, 1, controls+((WORK[0], 0),))
        self.h = self.indicator_product(0, 2, controls+((WORK[1], 0),))
        self.k1 = comm(self.f, self.g)
        self.psi = comm(self.k1, self.h)
        tw = tau(unit(10, 4, 2), self.translations)
        self.psi_prime = seq(leaf("W_a"), tw, self.psi, inv(tw), leaf("W_a"))
        self.seed = comm(self.psi, self.psi_prime)

    def diff(self, word, vector):
        return seq(tau(tuple(-x for x in vector), self.translations), word,
                   tau(vector, self.translations), inv(word))

    @lru_cache(maxsize=None)
    def base(self, r, chi, k):
        if k == 0:
            return self.translations[r]
        c = chi % 5
        if c == 4:
            raise ValueError("base requires piston coordinate")
        opposite = 5 if chi < 5 else 0
        shift_p = matvec(matinv(K), WALSH[c])
        shift_w = walsh(shift_p)
        vector = [0]*10
        vector[opposite:opposite+4] = shift_w
        u4 = self.z[r]
        for _ in range(4):
            u4 = self.diff(u4, tuple(vector))
        if k == 4:
            return u4
        d1 = self.diff(u4, unit(10, chi))
        d2 = self.diff(d1, unit(10, chi))
        d3 = self.diff(d2, unit(10, chi))
        u0 = self.translations[r]
        u1 = power(seq(d3, inv(u0)), 4)
        if k == 1:
            return u1
        u2 = power(seq(d2, power(u1, -4), power(u0, -4)), 3)
        if k == 2:
            return u2
        return power(seq(d1, inv(u2), power(u1, -4), inv(u0)), 4)

    def route(self, i, chi, k):
        if k == 0:
            return "A1/A2"
        if i in (0, 2) and chi % 5 != 4:
            return "A6/A7"
        if i == 1 and chi in (4, 9) and k == 1:
            return "A8" if chi == 4 else "A9"
        return "A12" if chi in EXTERNAL else "A11"

    @lru_cache(maxsize=None)
    def atom(self, i, chi, k):
        if chi == WORK[i] and k:
            raise ValueError("control equals target")
        route = self.route(i, chi, k)
        if route == "A1/A2":
            return self.translations[WORK[i]]
        if route == "A6/A7":
            return self.base(WORK[i], chi, k)
        if route == "A8":
            return self.n21
        if route == "A9":
            return self.n23
        if route == "A12":
            return conjugate(self.j12, self.base(4, chi, k))
        j = WORK.index(chi)
        path, ei, ej, _ = self.rotations[(i, j)]
        alphabet = (self.j12, inv(self.j12), self.j23, inv(self.j23))
        rij = seq(*(alphabet[k] for k in path))
        return power(conjugate(rij, self.base(4, 1, k)), ei*ej**k)

    @lru_cache(maxsize=None)
    def indicator(self, i, chi, c):
        shift = tau(unit(10, chi, c), self.translations)
        return seq(self.translations[WORK[i]], inv(conjugate(shift, self.atom(i, chi, 4))))

    @lru_cache(maxsize=None)
    def indicator_product(self, j, i, controls):
        if any(c in (WORK[i], WORK[j]) for c, _ in controls):
            raise ValueError("control overlaps target/helper")
        if len(controls) == 1:
            return self.indicator(j, *controls[0])
        f, g = controls[:-1], controls[-1:]
        eif = self.indicator_product(i, j, f)
        eig = self.indicator_product(i, j, g)
        qij = self.atom(j, WORK[i], 2)
        kg = comm(eig, qij)
        kminusg = comm(inv(eig), qij)
        rg = seq(kg, inv(kminusg))
        return inv(comm(eif, rg))


def syntax_inventory(roots):
    seen, active, leaves, nodes, powers = set(), set(), Counter(), Counter(), Counter()

    def visit(w):
        wid = id(w)
        require(wid not in active, "grammar.acyclic")
        if wid in seen:
            return
        active.add(wid)
        kind = w[0]
        nodes[kind] += 1
        if kind == "leaf":
            require(w[1] in TERMINALS, "grammar.native_leaf", w[1])
            leaves[w[1]] += 1
        elif kind == "mul":
            for child in w[1]:
                visit(child)
        elif kind in ("inv", "pow"):
            if kind == "pow":
                require(type(w[2]) is int, "grammar.integer_power", w[2])
                powers[str(w[2])] += 1
            visit(w[1])
        else:
            raise AuditFailure("grammar.node_kind", kind)
        active.remove(wid)
        seen.add(wid)

    for root in roots:
        visit(root)
    return {"nodes_by_kind": dict(nodes), "distinct_object_nodes": len(seen),
            "terminals": sorted(leaves), "syntactic_exponents": sorted(map(int, powers))}


def full_walsh_from_state(z):
    return walsh(z[:4])+(z[4], z[11])+walsh(z[5:9])+(z[9], z[12])


def state_from_full_walsh(v):
    return make_state(unwalsh(v[:4])+unwalsh(v[6:10]), v[4], v[10], 0, v[5], v[11])


@lru_cache(maxsize=None)
def affine_leaf(name):
    if name.startswith("W_"):
        raise ValueError("nonaffine W forbidden in affine evaluator")
    zero = full_walsh_from_state(native_apply(state_from_full_walsh((0,)*12), name))
    columns = []
    for i in range(12):
        out = full_walsh_from_state(native_apply(state_from_full_walsh(unit(12, i)), name))
        columns.append(tuple((a-b) % 5 for a, b in zip(out, zero)))
    return tuple(tuple(columns[j][i] for j in range(12))+(zero[i],) for i in range(12))+(tuple([0]*12+[1]),)


def affine_word(word, cache=None):
    if cache is None:
        cache = {}
    wid = id(word)
    if wid in cache:
        return cache[wid]
    kind = word[0]
    if kind == "leaf":
        out = affine_leaf(word[1])
    elif kind == "inv":
        out = matinv(affine_word(word[1], cache))
    elif kind == "pow":
        out = matpow(affine_word(word[1], cache), word[2])
    else:
        out = eye(13)
        for child in word[1]:
            out = matmul(out, affine_word(child, cache))
    cache[wid] = out
    return out


def translation_matrix(index):
    a = [list(row) for row in eye(13)]
    a[index][12] = 1
    return tuple(map(tuple, a))


def check_grammar_and_affine():
    gr = Grammar()
    expected_order = tuple("bar_"+c+"_"+i for i in ("x", "y") for c in "abcde")+("P", "P^-1", "Q", "Q^-1", "W_a", "W_b")
    require(MACRO_ORDER == expected_order, "grammar.macro_order", {"actual": MACRO_ORDER, "expected": expected_order})
    routes = Counter()
    atoms = []
    for i in range(3):
        for chi in range(10):
            if chi == WORK[i]:
                continue
            for k in range(1, 5):
                route = gr.route(i, chi, k)
                atoms.append(gr.atom(i, chi, k))
                routes[route] += 1
    require(dict(routes) == {"A6/A7": 64, "A8": 1, "A9": 1, "A11": 14, "A12": 28}, "grammar.priority_counts", dict(routes))
    for i in range(3):
        require(gr.atom(i, 0, 0) is gr.translations[WORK[i]], "grammar.constant_priority", i)
    for r in (4, 9):
        require(gr.z[r] == power(comm(gr.k0, gr.translations[r]), 2), "grammar.original_A4", r)
    require(gr.psi_prime[1][0] == leaf("W_a") and gr.psi_prime[1][-1] == leaf("W_a"), "grammar.original_A18")
    inventory = syntax_inventory([gr.seed]+atoms+[bar(c, i) for i in ("x", "y") for c in "abcde"])
    cache = {}
    factor_to_full = (0, 1, 2, 3, 4, 6, 7, 8, 9, 10)
    for i, word in enumerate(gr.translations):
        require(affine_word(word, cache) == translation_matrix(factor_to_full[i]), "A1_A2.full_affine_translation", i)
    n21 = [list(row) for row in eye(13)]
    n21[1][4] = 1
    n23 = [list(row) for row in eye(13)]
    n23[1][10] = 1
    require(affine_word(gr.n21, cache) == tuple(map(tuple, n21)), "A8.full_affine_N21")
    require(affine_word(gr.n23, cache) == tuple(map(tuple, n23)), "A9.full_affine_N23")
    shift_checks = 0
    require(tuple(zip(*K)) == K, "A6.symmetric_K")
    for chi in (0, 1, 2, 3, 5, 6, 7, 8):
        ell = WALSH[chi % 5]
        shift_p = matvec(matinv(K), ell)
        require(matvec(K, shift_p) == tuple(x % 5 for x in ell), "A6.shift_linear_identity", chi)
        require(unwalsh(walsh(shift_p)) == shift_p, "A6.shift_coordinate_conversion", chi)
        shift_checks += 1
    paths = gr.rotation_paths
    require(len(paths) == 24 and max(map(len, paths.values())) <= 23, "A4.rotation_group_size", len(paths))
    # Every edge obeys the optimal shortlex relaxation inequality. In conjunction
    # with reachable BFS paths this independently certifies all first words.
    for a, w in paths.items():
        for i, b in enumerate(gr.rotation_generators):
            new = w+(i,)
            best = paths[matmul(a, b)]
            require((len(best), best) <= (len(new), new), "A4.rotation_shortlex", (w, i))
    return gr, {"atomic_routes": dict(routes), "atoms": 108, "constants": 3,
                "full_affine_matrices": 12, "A6_linear_shift_identities": shift_checks,
                "rotation_matrices": 24, "rotation_edges": 96,
                "R_ij": [{"i": i+1, "j": j+1, "word": v[0], "signs": v[1:3]}
                         for (i, j), v in sorted(gr.rotations.items())], "syntax": inventory}


def check_native_cells():
    cases = 0
    homogeneous_cases = 0
    for cell in product(range(5), repeat=6):
        p, q, r = cell[:4], cell[4], cell[5]
        s, v, u, t = walsh(p)
        expected_w = {"a": (s, v, -u, -t, r), "b": (-s, v, -u, t, -r),
                      "c": (1-s, v+2*r, 2-u, t-2*r, -r),
                      "d": (-s, 1-v, -u, 2-t, 1-r),
                      "e": (-s, 1-v, -u, 2-t, 1-r)}
        for c in "abcde":
            out = native_cell(cell, c)
            actual_w = walsh(out[:4])+(out[5],)
            require(actual_w == tuple(x % 5 for x in expected_w[c]), "native.cell_walsh", (cell, c))
            expected_q = {"a": q, "b": -q, "c": 1-q, "d": 1-q, "e": 2-q}[c] % 5
            require(out[4] == expected_q, "native.cell_q", (cell, c))
            require(native_cell(out, c) == cell, "native.cell_involution", (cell, c))
            cases += 1
        # A fixed nonzero spectator detects accidental writes to the other cell.
        z = make_state(p+(1, 2, 3, 4), r, 2, 1, q, 3)
        tq = seq(leaf("e_x"), leaf("d_x"))
        expected = list(z)
        expected[11] = (q+1) % 5
        require(native_word_apply(tq, z) == tuple(expected), "native.tau_q", cell)
        for c in "cde":
            direct = native_apply(z, c+"_x")
            expected = list(direct)
            expected[11] = -q % 5
            word = bar(c, "x")
            out = native_word_apply(word, z)
            require(out == tuple(expected), "native.homogeneous", (cell, c))
            require(native_word_apply(word, out) == z, "native.homogeneous_involution", (cell, c))
            homogeneous_cases += 1
    require(cases == 78125 and homogeneous_cases == 46875, "native.case_counts",
            {"actual": (cases, homogeneous_cases), "expected": (78125, 46875)})
    # The other cell uses exactly the same native_cell routine and index table;
    # explicitly check the cell-exchange conjugacy for all terminals on a basis.
    def swap(z):
        return tuple(z[5:9])+(z[9],)+tuple(z[:4])+(z[4], z[10], z[12], z[11])
    swap_cases = 0
    for c in "abcde":
        for cell in product(range(5), repeat=6):
            z = make_state(cell[:4]+(1, 2, 3, 4), cell[5], 2, 1, cell[4], 3)
            require(swap(native_apply(z, c+"_x")) == native_apply(swap(z), c+"_y"), "native.cell_exchange", (cell, c))
            swap_cases += 1
    for p in product(range(5), repeat=4):
        require(unwalsh(walsh(p)) == p, "native.Walsh_roundtrip", p)
    require(matmul(B_READ, M) == matmul(L5, B_READ), "source.readout_matrix")
    require(matmul(M, MI) == eye(3) and matmul(MI, M) == eye(3), "source.target_inverse")
    sl2_count = sum(det2(p) == 1 for p in product(range(5), repeat=4))
    require(sl2_count == 120, "source.SL2_size", sl2_count)
    return {"cell_letter_cases": cases, "homogenized_cases": homogeneous_cases,
            "tau_q_cases": 15625, "cell_exchange_cases": swap_cases, "Walsh_inputs": 625,
            "matrix_identities": 3, "SL2_candidates": 625, "SL2_size": sl2_count}


def suffix_model(z, name):
    """Exact quotient of paired a,b,W and r translations.

    z=(h,eta,tag_a,tag_b,rx,ry,qx,qy). The tags track commuting paired
    piston involutions. Arbitrary initial tags follow by XOR translation.
    """
    h, eta, ta, tb, rx, ry, qx, qy = z
    if name in ("a", "b"):
        if name == "a":
            return (-h % 5, eta, ta ^ 1, tb, rx, ry, qx, qy)
        return (-h % 5, eta, ta, tb ^ 1, -rx % 5, -ry % 5, -qx % 5, -qy % 5)
    if name in ("Wa", "Wb"):
        if h == 0:
            return z
        sigma = int(h >= 3)
        out = suffix_model(z, name[-1]) if sigma ^ eta else z
        return (out[0], sigma)+out[2:]
    if name.startswith("r"):
        _, axis, amount = name.split(":")
        out = list(z)
        pos = 4+int(axis)
        out[pos] = (out[pos]+int(amount)) % 5
        return tuple(out)
    raise ValueError("unknown suffix model operation")


def model_sequence(z, names):
    for name in reversed(names):
        z = suffix_model(z, name)
    return z


@lru_cache(maxsize=None)
def model_word_q_lift(h, eta, names):
    """Compute actual q matrix by leaf-by-leaf affine composition.

    r translations have q identity, certified by A1/A2 full matrices. All
    entries here have t=0. The model branch is independent of input q and r.
    """
    z = (h, eta, 0, 0, 0, 0, 0, 0)
    matrix = eye(2)
    translation = (0, 0)
    for name in reversed(names):
        selected_b = name == "b" or (name == "Wb" and z[0] != 0 and (int(z[0] >= 3) ^ z[1]))
        local = ((4, 0), (0, 4)) if selected_b else eye(2)
        matrix = matmul(local, matrix)
        translation = matvec(local, translation)
        z = suffix_model(z, name)
    return matrix, translation


def check_contact_macros():
    cases = 0
    e_cases = 0
    wa_wb_cases = 0
    k0 = ("Wa", "a", "Wa", "Wb", "b", "Wb")
    k0_inverse = tuple(reversed(k0))
    for h, eta, rx, ry, qx, qy in product(range(5), range(2), range(5), range(5), range(5), range(5)):
        z = (h, eta, 0, 0, rx, ry, qx, qy)
        for name in ("Wa", "Wb"):
            require(suffix_model(suffix_model(z, name), name) == z, "W.suffix_involution", (z, name))
            wa_wb_cases += 1
        for c in ("a", "b"):
            ew = ("W"+c, c, "W"+c)
            out = model_sequence(z, ew)
            expected = suffix_model(z, c) if h == 0 else (h, eta ^ 1)+z[2:]
            require(out == expected, "A3.E_complete_suffix", (z, c))
            hm, tv = model_word_q_lift(h, eta, ew)
            predicted_q = tuple((a+b) % 5 for a, b in zip(matvec(hm, (qx, qy)), tv))
            require(out[6:] == predicted_q, "A3.E_q_affine_recurrence", (z, c))
            e_cases += 1
        out = model_sequence(z, k0)
        expected = model_sequence(z, ("a", "b")) if h == 0 else z
        require(out == expected, "A3.K0_complete_suffix", z)
        hm, tv = model_word_q_lift(h, eta, k0)
        require(out[6:] == tuple((a+b) % 5 for a, b in zip(matvec(hm, (qx, qy)), tv)), "A3.K0_q_affine_recurrence", z)
        for axis in range(2):
            plus, minus = "r:"+str(axis)+":1", "r:"+str(axis)+":-1"
            # Original A4, literally [K0,tau]^2: no Z20/Z48 substitution.
            commutator = k0+(plus,)+k0_inverse+(minus,)
            out = model_sequence(model_sequence(z, commutator), commutator)
            expected = list(z)
            expected[4+axis] = (expected[4+axis]+int(h == 0)) % 5
            require(out == tuple(expected), "A4.Z_complete_suffix", (z, axis))
            hm, tv = model_word_q_lift(h, eta, commutator+commutator)
            require(hm == eye(2) and tv == (0, 0) and out[6:] == matvec(hm, (qx, qy)),
                    "A4.Z_q_affine_recurrence", (z, axis))
            cases += 1
    require(cases == 12500 and e_cases == 12500 and wa_wb_cases == 12500, "A3_A4.case_counts",
            {"actual": (cases, e_cases, wa_wb_cases), "expected": (12500, 12500, 12500)})
    return {"suffix_inputs": 6250, "W_involution_cases": wa_wb_cases,
            "E_cases": e_cases, "K0_cases": 6250, "Z_cases": cases,
            "extension_proof": "paired piston actions commute; h changes sign; suffix branch depends only on h,eta; tags cancel for every piston input"}


def delta(x, c=0):
    return (1-pow((x-c) % 5, 4, 5)) % 5


def functional_difference(values, step=1):
    return tuple((values[(x+step) % 5]-values[x]) % 5 for x in range(5))


def check_polynomial_macros(gr):
    a5 = 0
    # Arbitrary function tables prove the finite-difference identity including
    # occupied target values. Four factors tau^-1 U tau U^-1 are executed.
    for values in product(range(5), repeat=5):
        for x, r in product(range(5), repeat=2):
            xx, rr = x, r
            rr = (rr-values[xx]) % 5
            xx = (xx+1) % 5
            rr = (rr+values[xx]) % 5
            xx = (xx-1) % 5
            require((xx, rr) == (x, (r+values[(x+1) % 5]-values[x]) % 5), "A5.function_identity", (values, x, r))
            a5 += 1
    for h, chi in product(range(5), repeat=2):
        values = tuple((1-pow((h+k*chi) % 5, 4, 5)) % 5 for k in range(5))
        for _ in range(4):
            values = functional_difference(values)
        require(values[0] == pow(chi, 4, 5), "A6.fourth_difference", (h, chi))
    u4 = tuple(pow(x, 4, 5) for x in range(5))
    d1 = functional_difference(u4)
    d2 = functional_difference(d1)
    d3 = functional_difference(d2)
    u1 = tuple(4*(x-1) % 5 for x in d3)
    u2 = tuple(3*(d2[x]-4*u1[x]-4) % 5 for x in range(5))
    u3 = tuple(4*(d1[x]-u2[x]-4*u1[x]-1) % 5 for x in range(5))
    for k, values in enumerate((u1, u2, u3), 1):
        for x in range(5):
            require(values[x] == pow(x, k, 5), "A7.lower_monomial", (k, x))
    conjugacy_cases = 0
    for (i, j), (_, ei, ej, rij) in sorted(gr.rotations.items()):
        ri = matinv(rij)
        for k in range(1, 5):
            sign = ei*ej**k
            for v in product(range(5), repeat=3):
                z = list(matvec(ri, v))
                z[0] = (z[0]+sign*pow(z[1], k, 5)) % 5
                out = matvec(rij, z)
                expected = list(v)
                expected[i] = (expected[i]+pow(v[j], k, 5)) % 5
                require(out == tuple(expected), "A11.conjugated_monomial", (i, j, k, v))
                conjugacy_cases += 1
    external_cases = 0
    j12 = gr.rotation_generators[0]
    for chi in EXTERNAL:
        for k in range(1, 5):
            for v in product(range(5), repeat=3):
                for value in range(5):
                    z = list(matvec(matinv(j12), v))
                    z[0] = (z[0]+pow(value, k, 5)) % 5
                    out = matvec(j12, z)
                    expected = list(v)
                    expected[1] = (expected[1]+pow(value, k, 5)) % 5
                    require(out == tuple(expected), "A12.external_monomial", (chi, k, v, value))
                    external_cases += 1
    # Work-plane maps used here are precisely the shears certified by A6-A12.
    def e(v, amount):
        return ((v[0]+amount) % 5, v[1])

    def qmap(v, sign):
        return (v[0], (v[1]+sign*v[0]*v[0]) % 5)

    def kg(v, g, inverse=False):
        if inverse:
            # Q E(g) Q^-1 E(-g)
            v = e(v, -g)
            v = qmap(v, -1)
            v = e(v, g)
            return qmap(v, 1)
        v = qmap(v, -1)
        v = e(v, -g)
        v = qmap(v, 1)
        return e(v, g)

    def rg(v, g, inverse=False):
        if inverse:
            return kg(kg(v, g, True), -g)
        return kg(kg(v, -g, True), g)

    multiplication_cases = 0
    for x, y, f, g in product(range(5), repeat=4):
        v = (x, y)
        require(kg(v, g) == (x, (y-2*x*g+g*g) % 5), "A13.K_identity", (x, y, f, g))
        require(rg(v, g) == (x, (y+x*g) % 5), "A13.R_identity", (x, y, f, g))
        # [E(f),R(g)]^-1 = R(g) E(f) R(g)^-1 E(f)^-1.
        out = rg(e(rg(e(v, -f), g, True), f), g)
        require(out == (x, (y+f*g) % 5), "A14.product_identity", (x, y, f, g))
        multiplication_cases += 1
    for x, c in product(range(5), repeat=2):
        require(delta(x, c) == int(x == c), "A15.indicator", (x, c))
    active_count = 0
    for values in product(range(5), repeat=7):
        flag = 1
        for value, c in zip(values, L_ZERO):
            flag = flag*delta(value, c) % 5
        require(flag == int(values == L_ZERO), "A16.seven_controls", values)
        active_count += flag
    require(active_count == 1, "A16.unique_L", {"actual": active_count, "expected": 1})
    return {"A5_function_cases": a5, "A6_cases": 25, "A7_cases": 15,
            "A11_cases": conjugacy_cases, "A12_cases": external_cases,
            "A13_A14_cases": multiplication_cases, "A15_cases": 25,
            "A16_control_tuples": 78125, "A16_active_tuples": active_count,
            "native_expansion": False}


def compose_apply(z, operations):
    for operation in reversed(operations):
        z = operation(z)
    return z


def comm_apply(z, f, fi, g, gi):
    return compose_apply(z, (f, g, fi, gi))


def workspace_shear(v, which, sign=1, active=1):
    x, t, y = v
    if which == "F":
        x = (x+sign*active*delta(y)) % 5
    elif which == "G":
        y = (y+sign*active*delta(x)) % 5
    elif which == "H":
        x = (x+sign*active*delta(t)) % 5
    else:
        raise ValueError("unknown workspace shear")
    return x, t, y


def workspace_k1(v, active=1, inverse=False):
    f = lambda z: workspace_shear(z, "F", 1, active)
    fi = lambda z: workspace_shear(z, "F", -1, active)
    g = lambda z: workspace_shear(z, "G", 1, active)
    gi = lambda z: workspace_shear(z, "G", -1, active)
    return comm_apply(v, g, gi, f, fi) if inverse else comm_apply(v, f, fi, g, gi)


def workspace_psi(v, active=1, inverse=False):
    f = lambda z: workspace_k1(z, active)
    fi = lambda z: workspace_k1(z, active, True)
    g = lambda z: workspace_shear(z, "H", 1, active)
    gi = lambda z: workspace_shear(z, "H", -1, active)
    return comm_apply(v, g, gi, f, fi) if inverse else comm_apply(v, f, fi, g, gi)


def cycle_apply(point, cycle):
    if point not in cycle:
        return point
    return cycle[(cycle.index(point)+1) % len(cycle)]


def factor_psi(z, inverse=False):
    wx, wy = walsh(z[:4]), walsh(z[5:9])
    f = wx+(z[4],)+wy+(z[9],)
    active = int(tuple(f[i] for i in EXTERNAL) == L_ZERO)
    work = (z[4], wx[1], z[9])
    new = workspace_psi(work, active, inverse)
    wnew = (wx[0], new[1], wx[2], wx[3])
    return make_state(unwalsh(wnew)+tuple(z[5:9]), new[0], new[2], z[10], z[11], z[12])


def factor_psi_prime(z, inverse=False):
    z = native_apply(z, "W_a")
    zz = list(z)
    zz[4] = (zz[4]-2) % 5
    z = factor_psi(tuple(zz), inverse)
    zz = list(z)
    zz[4] = (zz[4]+2) % 5
    return native_apply(tuple(zz), "W_a")


def check_seed_support():
    kcycle = ((0, 0), (1, 0), (0, 1))
    pcycle = ((0, 0), (1, 0), (1, 1), (2, 0), (0, 1))
    cases = 0
    for active, eta in product(range(2), repeat=2):
        for x, t, y in product(range(5), repeat=3):
            v = (x, t, y)
            kr = cycle_apply((x, y), kcycle) if active else (x, y)
            pr = cycle_apply((x, y), pcycle) if active and t == 0 else (x, y)
            require(workspace_k1(v, active) == (kr[0], t, kr[1]), "A16.K1_support", (active, eta, v))
            out = workspace_psi(v, active)
            require(out == (pr[0], t, pr[1]), "A17.Psi_support", (active, eta, v))
            require(workspace_psi(out, active, True) == v, "A17.Psi_inverse", (active, eta, v))
            cases += 1
    p = (3, 0, 3, 0, 4, 1, 1, 4)
    z = make_state(p)
    ap = state_piston(native_apply(native_apply(z, "a_x"), "a_y"))
    require(ap != p and gram(p)[1] == 2, "A18.base_piston")
    universe = [make_state(pp, rx, ry, eta) for pp in (p, ap)
                for rx, ry, eta in product(range(5), range(5), range(2))]
    support_psi, support_prime, support_seed = set(), set(), set()
    zetas = tuple(make_state(p, rx, ry, 0) for rx, ry in ((2, 0), (0, 1), (3, 0)))
    for z in universe:
        f = factor_psi(z)
        g = factor_psi_prime(z)
        if f != z:
            support_psi.add(z)
        if g != z:
            support_prime.add(z)
        out = comm_apply(z, factor_psi, lambda a: factor_psi(a, True),
                         factor_psi_prime, lambda a: factor_psi_prime(a, True))
        require(out == cycle_apply(z, zetas), "A18.Cstar_orientation", z)
        if out != z:
            support_seed.add(z)
    require(len(universe) == 100 and len(support_psi) == len(support_prime) == 10,
            "A18.support_sizes", (len(universe), len(support_psi), len(support_prime)))
    require(support_psi & support_prime == {zetas[0]} and support_seed == set(zetas), "A18.support_intersection",
            {"intersection": sorted(support_psi & support_prime), "seed_support": sorted(support_seed),
             "expected_intersection": [zetas[0]], "expected_seed": zetas})
    return {"workspace_cases": cases, "piston_r_bit_cases": 100, "Psi_support": 10,
            "Psi_prime_support": 10, "intersection": 1, "Cstar_support": 3,
            "scope": "factor only; full q lift remains the fixed native grammar",
            "complement_proof": "A16 indicators force Psi to the fixed piston and xi2=0; conjugation by Wa and rx translation confines Psi_prime to the two enumerated pistons"}


def check_q_lift():
    # Formal polynomial identity for arbitrary U,V affine coefficients and q.
    # Polynomials are sparse integer/F5 coefficients indexed by 14 exponent
    # vectors: U's 4 H entries+2 t, V's 4 H entries+2 t, q's two entries.
    def var(i):
        return {unit(14, i): 1}

    def add(*ps):
        result = {}
        for p in ps:
            for monomial, coefficient in p.items():
                result[monomial] = (result.get(monomial, 0)+coefficient) % 5
        return {m: c for m, c in result.items() if c}

    def multiply(p, q):
        result = {}
        for a, c in p.items():
            for b, d in q.items():
                m = tuple(x+y for x, y in zip(a, b))
                result[m] = (result.get(m, 0)+c*d) % 5
        return {m: c for m, c in result.items() if c}

    hu = ((var(0), var(1)), (var(2), var(3)))
    tu = (var(4), var(5))
    hv = ((var(6), var(7)), (var(8), var(9)))
    tv = (var(10), var(11))
    q = (var(12), var(13))
    vq = tuple(add(*(multiply(hv[i][j], q[j]) for j in range(2)), tv[i]) for i in range(2))
    composed = tuple(add(*(multiply(hu[i][j], vq[j]) for j in range(2)), tu[i]) for i in range(2))
    hprod = tuple(tuple(add(*(multiply(hu[i][k], hv[k][j]) for k in range(2))) for j in range(2)) for i in range(2))
    tprod = tuple(add(*(multiply(hu[i][j], tv[j]) for j in range(2)), tu[i]) for i in range(2))
    recurrence = tuple(add(*(multiply(hprod[i][j], q[j]) for j in range(2)), tprod[i]) for i in range(2))
    require(composed == recurrence, "q.symbolic_composition",
            {"direct_terms": [sorted(poly.items()) for poly in composed],
             "recurrence_terms": [sorted(poly.items()) for poly in recurrence]})
    maps, points, matrices = 0, 0, 0
    for entries in product(range(5), repeat=4):
        if not det2(entries):
            continue
        h = (entries[:2], entries[2:])
        hi = matinv(h)
        require(matmul(hi, h) == matmul(h, hi) == eye(2), "q.matrix_inverse", entries)
        matrices += 1
        for t in product(range(5), repeat=2):
            ti = tuple(-v % 5 for v in matvec(hi, t))
            images = set()
            for q0 in product(range(5), repeat=2):
                out = tuple((a+b) % 5 for a, b in zip(matvec(h, q0), t))
                back = tuple((a+b) % 5 for a, b in zip(matvec(hi, out), ti))
                require(back == q0, "q.affine_inverse", (entries, t, q0))
                images.add(out)
                points += 1
            require(len(images) == 25, "q.fiber_bijection", (entries, t))
            maps += 1
    require((matrices, maps, points) == (480, 12000, 300000), "q.counts",
            {"actual": (matrices, maps, points), "expected": (480, 12000, 300000)})
    return {"formal_composition_components": 2, "coefficient_indeterminates": 14,
            "invertible_matrices": matrices, "affine_maps": maps, "inverse_points": points,
            "native_H_T_evaluated": False, "H_T_identity_claimed": False,
            "proof_dependency": "SPEC full triangular lift: F_U depends only on factor; matrix polynomial coefficients are evaluated at F_V(f) and f respectively"}


def reduced_step(z, inverse=False):
    g, j, eta = z
    ell = j+width(g)*eta
    if ell >= orbit_width(g):
        return z
    gp = target_inverse(g) if inverse else target(g)
    mp = width(gp)
    ep = int(ell >= mp)
    return gp, ell-mp*ep, ep


def check_reduced_orbits():
    grams = tuple(product(range(5), repeat=3))
    seen, orbit_lengths = set(), Counter()
    for start in grams:
        require(target_inverse(target(start)) == target(target_inverse(start)) == start,
                "M.inverse_points", start)
        a = start
        orbit = []
        while a not in orbit:
            orbit.append(a)
            a = target(a)
            require(len(orbit) <= 10, "M.orbit_bound", start)
        require(a == start, "M.orbit_closed", start)
        if start != PI_ZERO:
            require(max(width(g) for g in orbit) == orbit_width(start), "M.orbit_width", start)
        if start not in seen:
            seen.update(orbit)
            orbit_lengths[len(orbit)] += 1
    require(dict(orbit_lengths) == {1: 1, 2: 2, 10: 12}, "M.orbit_histogram", dict(orbit_lengths))
    # Independent Jordan-coordinate check of the SPEC derivation, all 125 g.
    basis = ((2, 2, 2), (1, 0, 0), (3, 2, 3))
    jordan_cases = 0
    for a, b, c in product(range(5), repeat=3):
        g = matvec(basis, (a, b, c))
        require(kappa(g) == (b*b+3*a*c-c*c) % 5, "M.kappa_coordinates", (a, b, c))
        cur = g
        for k in range(10):
            require(kappa(cur) == (kappa(g)+k*c*c) % 5, "M.kappa_iteration", (a, b, c, k))
            cur = target(cur)
            jordan_cases += 1
    states = tuple((g, j, eta) for g in grams if g != PI_ZERO
                   for j in range(width(g)) for eta in range(2))
    state_set = set(states)
    reachable_set = {z for z in states if z[1]+width(z[0])*z[2] < orbit_width(z[0])}
    prepared = {z for z in states if z[2] == 0}
    closure = set(prepared)
    queue = deque(sorted(prepared))
    while queue:
        out = reduced_step(queue.popleft())
        require(out in state_set, "Pi.closure_stays_in_reduced_carrier", out)
        if out not in closure:
            closure.add(out)
            require(len(closure) <= 1280, "Pi.closure_bound")
            queue.append(out)
    require(closure == reachable_set, "Pi.reduced_exact_reachability",
            {"closure_count": len(closure), "domain_count": len(reachable_set),
             "first_missing": min(reachable_set-closure, default=None),
             "first_extra": min(closure-reachable_set, default=None)})
    permutations_seen, cycles = set(), Counter()
    for start in states:
        out, back = reduced_step(start), reduced_step(start, True)
        require(out in state_set and back in state_set, "Pi.reduced_closed", start)
        require(reduced_step(out, True) == reduced_step(back) == start, "Pi.reduced_inverse", start)
        require((out in reachable_set) == (start in reachable_set) == (back in reachable_set), "Pi.reduced_domain", start)
        if start not in permutations_seen:
            current, cycle = start, []
            while current not in cycle:
                require(current in state_set and len(cycle) < 1280, "Pi.reduced_cycle_bound", start)
                cycle.append(current)
                current = reduced_step(current)
            require(current == start, "Pi.reduced_cycle", start)
            permutations_seen.update(cycle)
            cycles[len(cycle)] += 1
    require((len(states), len(prepared), len(reachable_set)) == (1280, 640, 740), "Pi.reduced_counts",
            {"actual": (len(states), len(prepared), len(reachable_set)), "expected": (1280, 640, 740)})
    require(dict(cycles) == {1: 540, 2: 10, 10: 72}, "Pi.reduced_cycles", dict(cycles))
    # Parity proof is independent of this even reduced permutation: 15000
    # repetitions of any reduced cycle make the full factor sign positive.
    return {"gram_points": 125, "M_orbits": dict(sorted(orbit_lengths.items())),
            "Jordan_iteration_cases": jordan_cases, "reduced_states": 1280,
            "prepared": 640, "reachable": 740, "cycles": dict(sorted(cycles.items())),
            "factor_replication": 15000, "parity_extension_type": "proof_from_even_replication"}


def check_atlas_and_piston_bit():
    block_counts = Counter()
    gram_counts = Counter()
    reachable_count = 0
    occupied_reachable = 0
    zero_count = 0
    piston_count = 0
    bit_count = 0
    wa_cases = 0
    # Stream the complete 5^8 set; never materialize the original full carrier.
    for p in product(range(5), repeat=8):
        g = gram(p)
        gram_counts[g] += 1
        enc = atlas_encode(p)
        if enc is None:
            zero_count += 1
        else:
            ge, l, n, j = enc
            require(ge == g and atlas_decode(ge, l, n, j) == p, "atlas.full_roundtrip", p)
            block_counts[(g, j)] += 1
        x, y = p[:4], p[4:]
        polarization = 3*(det2(tuple((a+b) % 5 for a, b in zip(x, y)))-det2(x)-det2(y)) % 5
        bilinear = sum(x[i]*K[i][j]*y[j] for i in range(4) for j in range(4)) % 5
        require(g[1] == polarization == bilinear, "Gram.polarization", p)
        for c in ("a", "b"):
            paired = native_apply(native_apply(make_state(p), c+"_x"), c+"_y")
            require(gram(state_piston(paired)) == tuple(-x % 5 for x in g), "Gram.paired_sign", (p, c))
        for eta in range(2):
            state = make_state(p, eta=eta)
            for gate in ("W_a", "W_b"):
                out_state = native_apply(state, gate)
                require(native_apply(out_state, gate) == state, "W.piston_bit_involution", (p, eta, gate))
                h = g[1]
                if h == 0:
                    expected = state
                else:
                    sigma = int(h >= 3)
                    expected = state
                    if sigma ^ eta:
                        c = gate[-1]
                        expected = native_apply(native_apply(expected, c+"_x"), c+"_y")
                    expected = expected[:10]+(sigma,)+expected[11:]
                require(out_state == expected, "W.piston_bit_formula", (p, eta, gate))
                wa_cases += 1
            out_p, out_eta = pi(p, eta)
            back_p, back_eta = pi_inverse(p, eta)
            require(pi_inverse(out_p, out_eta) == (p, eta), "Pi.left_inverse", (p, eta))
            require(pi(back_p, back_eta) == (p, eta), "Pi.right_inverse", (p, eta))
            dom = reachable(p, eta)
            require(reachable(out_p, out_eta) == dom == reachable(back_p, back_eta), "Pi.domain_invariance", (p, eta))
            if dom:
                require(gram(out_p) == target(g), "Pi.target_readout", (p, eta))
                second_p, second_eta = pi(out_p, out_eta)
                require(gram(second_p) == target(target(g)) and reachable(second_p, second_eta), "Pi.second_step", (p, eta))
                reachable_count += 1
                occupied_reachable += eta
            else:
                require((out_p, out_eta) == (p, eta) == (back_p, back_eta), "Pi.inactive_fixation", (p, eta))
            if enc is not None:
                out_enc = atlas_encode(out_p)
                require(out_enc is not None and out_enc[1:3] == enc[1:3], "Pi.L_n_preserved", (p, eta))
                require(out_enc[3]+width(out_enc[0])*out_eta == enc[3]+width(enc[0])*eta, "Pi.slot_preserved", (p, eta))
            bit_count += 1
        piston_count += 1
    require((piston_count, bit_count, zero_count, wa_cases) == (390625, 781250, 6625, 1562500),
            "atlas.enumeration_counts", (piston_count, bit_count, zero_count, wa_cases))
    require(len(block_counts) == 640 and set(block_counts.values()) == {600}, "atlas.block_multiplicity", dict(Counter(block_counts.values())))
    for g, count in gram_counts.items():
        require(count == (6625 if g == PI_ZERO else 600*width(g)), "atlas.gram_counts", (g, count))
    require((reachable_count, occupied_reachable) == (450625, 60000), "Pi.piston_domain_counts", (reachable_count, occupied_reachable))
    return {"piston_pairs": piston_count, "piston_bit_states": bit_count, "zero_Gram_pairs": zero_count,
            "nonzero_blocks": len(block_counts), "pistons_per_block": 600,
            "W_piston_bit_cases": wa_cases, "reachable_piston_bit": reachable_count,
            "occupied_reachable_piston_bit": occupied_reachable,
            "T_closure_from_r_zero_with_q": reachable_count*25,
            "T_closure_with_arbitrary_r_q": reachable_count*625,
            "prepared_r_eta_zero_with_q": 5**10,
            "extension_proofs": ["Pi definition copies both r unchanged", "native triangular q lift is bijective on all 25 q values", "reduced-cycle closure verified separately"],
            "expanded_native_T_executed": False}


def source_bindings(directory):
    expected = {"SPEC.md": SPEC_SHA256, "PREREG-DRAFT.md": PREREG_SHA256}
    result = {}
    for name, sha in expected.items():
        actual = hashlib.sha256((directory/name).read_bytes()).hexdigest()
        require(actual == sha, "source.sha256", {"file": name, "expected": sha, "actual": actual})
        result[name] = actual
    # No circular self-hash constants: these exact bytes are bound externally
    # by the accepted verifier pin and are reported in deterministic stdout.
    for name in ("verify.py", "compiler_identity_checks.py"):
        result[name] = hashlib.sha256((directory/name).read_bytes()).hexdigest()
    return result


def emit_json(value):
    data = (json.dumps(value, sort_keys=True, ensure_ascii=True, separators=(",", ":"))+"\n").encode("utf-8")
    sys.stdout.buffer.write(data)


def main():
    try:
        require(sys.version_info[:2] == (3, 12), "runtime.Python_3_12", tuple(sys.version_info[:2]))
        directory = Path(__file__).resolve().parent
        sources = source_bindings(directory)
        # This helper is deliberately not imported when composition imports
        # the atlas API from a byte-identical algebra_dependency.py copy.
        sys.dont_write_bytecode = True
        import compiler_identity_checks
        checks = {}
        checks["native"] = check_native_cells()
        gr, checks["grammar_affine"] = check_grammar_and_affine()
        checks["contact_macros"] = check_contact_macros()
        checks["polynomial_macros"] = check_polynomial_macros(gr)
        checks["seed_support"] = check_seed_support()
        checks["compiler_identities"] = compiler_identity_checks.run_checks()
        checks["q_lift"] = check_q_lift()
        checks["reduced_orbits"] = check_reduced_orbits()
        checks["atlas_piston_bit"] = check_atlas_and_piston_bit()
        result = {"schema": "twistj.algebra.bounded-verifier.v1", "status": "PASS",
                  "compiler": VERSION, "sources_sha256": sources, "checks": checks,
                  "proof_dependencies": [
                      "SPEC 5.1: primitivity and complete block-system argument",
                      "SPEC 5.3: connected conjugate-support hypergraph by word-length N",
                      "SPEC A1-A18: transfer of checked local identities to the exact native syntax",
                      "SPEC B1-B7: termination N-3 and universal fixed-word compiler",
                      "SPEC triangular lift: factor-independent q branching, homogeneous macro endpoints",
                      "SPEC reachability: complete q fibers and unchanged r, not preparation between steps"],
                  "not_claimed": ["execution of expanded Cstar or T_alg", "computed complete H_T", "q identity", "native period 10", "practical gate count", "joint V proof", "public acceptance"]}
        emit_json(result)
        return 0
    except AuditFailure as exc:
        emit_json({"schema": "twistj.algebra.bounded-verifier.v1", "status": "FAIL", "compiler": VERSION,
                   "assertion": exc.assertion, "witness": exc.witness})
        return 1
    except ValueError as exc:
        payload = exc.args[0] if exc.args else "ValueError without message"
        emit_json({"schema": "twistj.algebra.bounded-verifier.v1", "status": "FAIL", "compiler": VERSION,
                   "assertion": "invalid_value_or_helper_assertion", "witness": payload})
        return 1
    except Exception as exc:
        # An unexpected implementation bug is a failure, never a skipped test.
        emit_json({"schema": "twistj.algebra.bounded-verifier.v1", "status": "FAIL", "compiler": VERSION,
                   "assertion": "unexpected_verifier_error", "error_type": type(exc).__name__, "message": str(exc)})
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
