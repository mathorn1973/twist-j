#!/usr/bin/env python3
"""Exact verifier for P-CURVATURE-COLUMN-GOLDEN-FRAME-1.

Do not execute or import before the immutable preregistration pin is pushed
and read back. The frozen historical construction is imported from one pinned
public verifier after its SHA-256 is checked byte for byte.
"""
from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from fractions import Fraction
from hashlib import sha256
from importlib.util import module_from_spec, spec_from_file_location
from itertools import combinations
from math import gcd
from pathlib import Path
import sys

TAG = "canon-v71"
CONTENT = "a77d720433c19976f9ab663d023ec9364eac34eb"
CANON_SHA256 = "0306abb2e7f855ceb4fcbfdf14265a9d2c5c8bd23b35868b74a92aae16b5e279"
BASE = "d627733fbf0cd2fe3733b668140c2c0bcdc81b61"
DEP_REL = "probes/P-CURVATURE-GAUSS-SPLIT-1/verify.py"
DEP_SHA256 = "4080da59872a923b0ce4204a93184e17307f6923243d97f0f3105c771c48b8bd"
TRACE = Fraction(-881, 8)
RANK = 292
NULLITY_V = 526
ACTIVE = 26034
GOLD = Fraction(1, 5)

Col = dict[int, int]
Matrix = tuple[Col, ...]
Clique = tuple[int, ...]


def load_dependency():
    path = Path(__file__).resolve().parents[2] / DEP_REL
    data = path.read_bytes()
    if sha256(data).hexdigest() != DEP_SHA256:
        raise ValueError("dependency hash")
    spec = spec_from_file_location("curvature_gauss_split_frozen", path)
    if spec is None or spec.loader is None:
        raise ValueError("dependency loader")
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def clean(c: dict[int, int]) -> Col:
    return {i: v for i, v in c.items() if v}


def columns_push(orbits, labels, ac, ca) -> Matrix:
    out = [defaultdict(int) for _ in orbits]
    for j, orbit in enumerate(orbits):
        for x in orbit:
            out[j][labels[ac[x]]] += 1
            out[j][labels[ca[x]]] -= 1
    return tuple(clean(c) for c in out)


def columns_pull(orbits, labels, ac, ca) -> Matrix:
    out = [defaultdict(int) for _ in orbits]
    for i, orbit in enumerate(orbits):
        for x in orbit:
            out[labels[ca[x]]][i] += 1
            out[labels[ac[x]]][i] -= 1
    return tuple(clean(c) for c in out)


def skew_and_zero(matrix: Matrix) -> bool:
    n = len(matrix)
    rows = [0] * n
    for j, col in enumerate(matrix):
        if sum(col.values()):
            return False
        for i, v in col.items():
            rows[i] += v
            if matrix[i].get(j, 0) != -v:
                return False
    return not any(rows)


def trace_square(matrix: Matrix, sizes: tuple[int, ...]) -> Fraction:
    return -sum((Fraction(v * v, sizes[i] * sizes[j])
                 for j, col in enumerate(matrix) for i, v in col.items()), Fraction())


def ray(col: Col) -> tuple[tuple[int, int], ...]:
    d = 0
    for v in col.values():
        d = gcd(d, abs(v))
    p = {i: v // d for i, v in col.items()}
    if p[min(p)] < 0:
        p = {i: -v for i, v in p.items()}
    return tuple(sorted(p.items()))


def ray_family(matrix: Matrix):
    src = defaultdict(list)
    for j, col in enumerate(matrix):
        if col:
            src[ray(col)].append(j)
    keys = tuple(sorted(src))
    return tuple(dict(k) for k in keys), tuple(tuple(src[k]) for k in keys)


def dot(a: Col, b: Col, weights: tuple[int, ...]) -> int:
    if len(a) > len(b):
        a, b = b, a
    return sum(v * b.get(i, 0) * weights[i] for i, v in a.items())


def graph_and_hist(vectors: tuple[Col, ...], weights: tuple[int, ...]):
    norms = tuple(dot(v, v, weights) for v in vectors)
    hist = Counter()
    adj = [set() for _ in vectors]
    for i, j in combinations(range(len(vectors)), 2):
        q = dot(vectors[i], vectors[j], weights)
        c2 = Fraction(q * q, norms[i] * norms[j])
        if not Fraction(0) <= c2 < Fraction(1):
            raise ValueError("cosine bounds")
        hist[c2] += 1
        if c2 == GOLD:
            adj[i].add(j); adj[j].add(i)
    return norms, hist, tuple(frozenset(x) for x in adj)


def digest_hist(hist: Counter[Fraction]) -> str:
    text = "".join(f"{q.numerator}/{q.denominator}:{hist[q]}\n" for q in sorted(hist))
    return sha256(text.encode("ascii")).hexdigest()


def cliques_set(adj):
    def rec(prefix, candidates):
        need = 6 - len(prefix)
        if need == 0:
            yield prefix; return
        if len(candidates) < need:
            return
        for k, v in enumerate(candidates):
            nxt = tuple(x for x in candidates[k + 1:] if x in adj[v])
            if len(nxt) >= need - 1:
                yield from rec(prefix + (v,), nxt)
    yield from rec(tuple(), tuple(range(len(adj))))


def cliques_bits(adj):
    masks = []
    for v, ns in enumerate(adj):
        m = 0
        for n in ns:
            if n > v: m |= 1 << n
        masks.append(m)
    def rec(prefix, candidates):
        need = 6 - len(prefix)
        if need == 0:
            yield prefix; return
        if candidates.bit_count() < need:
            return
        rest = candidates
        while rest:
            low = rest & -rest; rest ^= low
            v = low.bit_length() - 1
            nxt = rest & masks[v]
            if nxt.bit_count() >= need - 1:
                yield from rec(prefix + (v,), nxt)
    yield from rec(tuple(), (1 << len(adj)) - 1)


def rank_q(rows: list[list[Fraction]]) -> int:
    rank = 0
    for c in range(len(rows[0]) if rows else 0):
        p = next((r for r in range(rank, len(rows)) if rows[r][c]), None)
        if p is None: continue
        rows[rank], rows[p] = rows[p], rows[rank]
        z = rows[rank][c]; rows[rank] = [x / z for x in rows[rank]]
        for r in range(len(rows)):
            if r != rank and rows[r][c]:
                z = rows[r][c]
                rows[r] = [x - z * y for x, y in zip(rows[r], rows[rank])]
        rank += 1
        if rank == len(rows): break
    return rank


def golden(clique: Clique, vectors, norms, weights) -> bool:
    gram = [[dot(vectors[i], vectors[j], weights) for j in clique] for i in clique]
    if rank_q([[Fraction(x) for x in row] for row in gram]) != 3:
        return False
    for j in range(6):
        out = defaultdict(Fraction)
        for i in range(6):
            a = Fraction(gram[i][j], gram[i][i])
            for k, v in vectors[clique[i]].items(): out[k] += a * v
        if clean(out) != {k: Fraction(2 * v) for k, v in vectors[clique[j]].items()}:
            return False
    return True


@dataclass(frozen=True)
class Summary:
    count: int; digest: str; golden_count: int; golden_digest: str; least: Clique | None


def summarize(stream, vectors, norms, weights) -> Summary:
    h = sha256(); gh = sha256(); count = gc = 0; least = prev = None
    for c in stream:
        if prev is not None and c <= prev: raise ValueError("clique order")
        prev = c; b = (",".join(map(str, c)) + "\n").encode("ascii")
        h.update(b); count += 1
        if golden(c, vectors, norms, weights):
            gh.update(b); gc += 1
            if least is None: least = c
    return Summary(count, h.hexdigest(), gc, gh.hexdigest(), least)


def witness(c, vectors, sources, norms, weights) -> str:
    if c is None: return "none"
    ds = [dot(vectors[i], vectors[j], weights) for i, j in combinations(c, 2)]
    return ("rays=" + ",".join(map(str, c)) + " sources=" +
            ",".join(str(min(sources[i])) for i in c) + " norms=" +
            ",".join(str(norms[i]) for i in c) + " dots=" + ",".join(map(str, ds)))


def compute():
    g = load_dependency()
    authority = TAG == "canon-v71" and CONTENT == "a77d720433c19976f9ab663d023ec9364eac34eb" and CANON_SHA256 == "0306abb2e7f855ceb4fcbfdf14265a9d2c5c8bd23b35868b74a92aae16b5e279" and BASE == "d627733fbf0cd2fe3733b668140c2c0bcdc81b61"
    group = g.group_closure((g.B_GEN, g.D_GEN)); orbits, labels = g.orbit_partition(group)
    group_partition = g.group_is_exact(group) and g.orbit_partition_is_exact(orbits, labels)
    census = Counter(map(len, orbits)); sizes = tuple(map(len, orbits))
    pa = g.affine_permutation(g.A_GEN); pc = g.affine_permutation(g.C_GEN)
    ac = g.compose_permutations(pa, pc); ca = g.compose_permutations(pc, pa)
    a = columns_push(orbits, labels, ac, ca); b = columns_pull(orbits, labels, ac, ca)
    dep_matrix = tuple({i: Fraction(v) for i, v in col.items()} for col in a)
    cert = g.exact_rank_certificate(dep_matrix)
    anchors = (len(a) == 819 and census == Counter({5:1,10:74,20:744}) and
               sum(map(len, a)) == ACTIVE and skew_and_zero(a) and
               trace_square(a, sizes) == TRACE and cert.rank == RANK and
               cert.nullity == NULLITY_V + 1 and cert.kernel_ok)
    vectors, sources = ray_family(a); multiplicity = Counter(map(len, sources))
    weights = tuple(20 // s for s in sizes)
    norms, hist, adj = graph_and_hist(vectors, weights)
    pairs = len(vectors) * (len(vectors)-1) // 2
    golden_pairs = hist.get(GOLD, 0)
    s1 = summarize(cliques_set(adj), vectors, norms, weights)
    s2 = summarize(cliques_bits(adj), vectors, norms, weights)
    quotient = (sum(map(len, sources)) == sum(bool(c) for c in a) and
                all(tuple(sorted(x)) == x for x in sources))
    audits = [authority, group_partition, a == b, anchors, quotient,
              sum(hist.values()) == pairs, all(20 % s == 0 for s in sizes), s1 == s2]
    if not all(audits): decision = "STOP"
    elif golden_pairs == 0: decision = "ABSENT"
    elif s1.golden_count == 0: decision = "PAIR-ONLY"
    elif s1.golden_count == 1: decision = "UNIQUE-GOLDEN6"
    else: decision = "MULTIPLE-GOLDEN6"
    return audits, census, cert, a, vectors, sources, multiplicity, norms, weights, hist, s1, decision


def main() -> int:
    try:
        audits, census, cert, matrix, vectors, sources, mult, norms, weights, hist, s, decision = compute()
    except Exception as exc:
        print("P-CURVATURE-COLUMN-GOLDEN-FRAME-1")
        print(f"DECISION STOP exception={type(exc).__name__}")
        print("RESULT INVALID"); return 1
    ok = all(audits)
    print("P-CURVATURE-COLUMN-GOLDEN-FRAME-1")
    print(f"AUTHORITY tag={TAG} content={CONTENT} canon_sha256={CANON_SHA256} base={BASE}")
    print(f"SOURCE path={DEP_REL} sha256={DEP_SHA256}")
    print("AUDIT " + " ".join(f"I{i+1:02d}={'P' if x else 'F'}" for i,x in enumerate(audits)))
    print(f"AUDIT {'PASS' if ok else 'STOP'} {sum(audits)}/{len(audits)}")
    print(f"H order=20 orbits={len(matrix)} census=5:{census[5]},10:{census[10]},20:{census[20]}")
    print(f"K_HIST active_entries={sum(map(len,matrix))} trace=-881/8 rank={cert.rank} nullity_full={cert.nullity} nullity_V={cert.nullity-1} mod2={cert.mod2_lower} mod3={cert.mod3_lower}")
    print(f"RAYS nonzero_columns={sum(bool(c) for c in matrix)} distinct={len(vectors)} multiplicity=" + ",".join(f"{k}:{mult[k]}" for k in sorted(mult)))
    print(f"COSINES pairs={sum(hist.values())} bins={len(hist)} zero={hist.get(Fraction(0),0)} golden_c2_1_5={hist.get(GOLD,0)} sha256={digest_hist(hist)}")
    print(f"CLIQUE6 count={s.count} sha256={s.digest} methods=AGREE")
    print(f"GOLDEN6 count={s.golden_count} sha256={s.golden_digest}")
    print("WITNESS " + witness(s.least, vectors, sources, norms, weights))
    print(f"DECISION {decision}")
    print("RESULT VALID" if ok else "RESULT INVALID")
    return 0 if ok else 1

if __name__ == "__main__":
    sys.exit(main())
