#!/usr/bin/env python3
"""Prospectively pinned exact local LS construction audit. No floats or search."""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F
from functools import lru_cache
import hashlib
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
INPUTS_SHA256 = "66691a0298ed37e8e56dfaa6ffd9db9468b863fd430eab404dca2f8e2d65f3a5"


def require(ok, message):
    if not ok:
        raise AssertionError(message)


@dataclass(frozen=True)
class C8:
    """Q[z]/(z^4+1), z=exp(i*pi/4), in a fixed rational basis."""
    v: tuple[F, F, F, F]

    def __add__(self, other):
        return C8(tuple(a + b for a, b in zip(self.v, other.v)))

    def __neg__(self):
        return C8(tuple(-a for a in self.v))

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        values = [F(0)] * 4
        for a, x in enumerate(self.v):
            if not x:
                continue
            for b, y in enumerate(other.v):
                if y:
                    values[(a + b) % 4] += x * y * (1 if a + b < 4 else -1)
        return C8(tuple(values))

    def conj(self):
        a, b, c, d = self.v
        return C8((a, -d, -c, -b))


ZERO = C8((F(0),) * 4)
ONE = C8((F(1), F(0), F(0), F(0)))
II = C8((F(0), F(0), F(1), F(0)))
HALFROOT = C8((F(0), F(1, 2), F(0), F(-1, 2)))
IPOW = (ONE, II, -ONE, -II)


def eye(n=5):
    return {(j, j): ONE for j in range(n)}


def add_entry(out, key, value):
    value = out.get(key, ZERO) + value
    if value == ZERO:
        out.pop(key, None)
    else:
        out[key] = value


def multiply(left, right):
    out = {}
    for (i, k), a in left.items():
        for (l, j), b in right.items():
            if k == l:
                add_entry(out, (i, j), a * b)
    return out


def dagger(matrix):
    return {(j, i): x.conj() for (i, j), x in matrix.items()}


@lru_cache(maxsize=None)
def rotation(a, b, angle, phase):
    """Angle and phase are integer multiples of pi/2; positive time only."""
    require(0 <= a < 5 and 0 <= b < 5 and a != b, "rotation levels")
    require(angle in (1, 2, 4), "rotation area outside frozen library")
    cosine, sine = {1: (HALFROOT, HALFROOT), 2: (ZERO, ONE),
                    4: (-ONE, ZERO)}[angle]
    matrix = eye()
    for j in (a, b):
        matrix.pop((j, j))
        if cosine != ZERO:
            matrix[j, j] = cosine
    if sine != ZERO:
        matrix[a, b] = (-II) * sine * IPOW[(-phase) % 4]
        matrix[b, a] = (-II) * sine * IPOW[phase % 4]
    return matrix


def pulse(j, angle, phase=0):
    require(j in (1, 2, 3, 4), "not a documented star edge")
    return ("R", j, angle, phase % 4)


def inverse(word):
    require(all(token[0] == "R" for token in word), "inverse needs carrier word")
    return [pulse(j, angle, phase + 2) for _, j, angle, phase in reversed(word)]


def local_matrix(word):
    result = eye()
    for _, j, angle, phase in word:
        result = multiply(rotation(0, j, angle, phase), result)
    return result


def compile_pair(c, j, angle, phase):
    if j == 0:
        return [pulse(c, angle, -phase)]
    # Chronological T_c^dagger, R_0j, T_c implements T_c R_0j T_c^dagger.
    return [pulse(c, 2, 2), pulse(j, angle, phase - 1), pulse(c, 2, 0)]


def compile_permutation(permutation):
    """Canonical disjoint cycles, each translated into star transpositions."""
    require(sorted(permutation) == list(range(5)), "not a permutation")
    visited = set()
    word = []
    for start in range(5):
        if start in visited:
            continue
        cycle = []
        k = start
        while k not in visited:
            visited.add(k)
            cycle.append(k)
            k = permutation[k]
        require(k == start, "malformed cycle")
        if len(cycle) == 1:
            continue
        labels = cycle[1:] if start == 0 else cycle + [start]
        word.extend(pulse(j, 2) for j in labels)
    return word


def basis(k):
    return {k: ONE}


def apply_collective(matrix, state):
    columns = {j: [] for j in range(5)}
    for (i, j), value in matrix.items():
        columns[j].append((i, value))
    out = {}
    for column, amplitude in state.items():
        j, k = divmod(column, 5)
        for r, x in columns[j]:
            for s, y in columns[k]:
                add_entry(out, 5 * r + s, amplitude * x * y)
    return out


def apply_word(word, state, omit_ls=False):
    for token in word:
        if token[0] == "G":
            if not omit_ls:
                state = {k: value * (ONE if k // 5 == k % 5 else -II)
                         for k, value in state.items()}
        else:
            _, j, angle, phase = token
            state = apply_collective(rotation(0, j, angle, phase), state)
    return state


def block(c, j):
    word = [("G",)]
    for phase in (1, 0):
        v = compile_pair(c, j, 1, phase)
        word.extend(inverse(v) + [("G",)] + v)
    return word


def contact(c):
    word = []
    for j in range(5):
        if j != c:
            word.extend(block(c, j))
    word.extend(pulse(j, 4) for j in range(1, 5) if j != c)
    return word


def manifest():
    raw = (ROOT / "INPUTS.json").read_bytes()
    require(hashlib.sha256(raw).hexdigest() == INPUTS_SHA256, "input manifest changed")
    data = json.loads(raw)
    for row in data["files"]:
        require(Path(row["path"]).name == row["path"], "unexpected manifest path")
        payload = (ROOT / row["path"]).read_bytes()
        require(len(payload) == row["bytes"], "input length: " + row["path"])
        require(hashlib.sha256(payload).hexdigest() == row["sha256"],
                "input hash: " + row["path"])


def main():
    manifest()
    require(HALFROOT * HALFROOT + HALFROOT * HALFROOT == ONE, "cyclotomic normalization")
    require(II * II == -ONE and II.conj() == -II, "cyclotomic imaginary unit")
    for j in range(1, 5):
        for angle in (1, 2, 4):
            for phase in range(4):
                matrix = rotation(0, j, angle, phase)
                require(multiply(dagger(matrix), matrix) == eye(), "carrier unitarity")
                word = [pulse(j, angle, phase)]
                require(local_matrix(inverse(word)) == dagger(matrix), "positive-time inverse")

    affine = [tuple((a * j + b) % 5 for j in range(5))
              for a in range(1, 5) for b in range(5)]
    require(len(set(affine)) == 20, "affine family size")
    compiler_lengths = []
    for p in affine:
        word = compile_permutation(p)
        matrix = local_matrix(word)
        require(len(word) <= 6, "permutation carrier bound")
        require(local_matrix(inverse(word)) == dagger(matrix), "permutation inverse phases")
        require(multiply(dagger(matrix), matrix) == eye(), "permutation unitarity")
        for j in range(5):
            column = [(i, x) for (i, k), x in matrix.items() if k == j]
            require(len(column) == 1 and column[0][0] == p[j], "compiled permutation labels")
        compiler_lengths.append(len(word))

    # Exact polynomial coefficients of sum_p (d_p(j)-d_p(k))^2.
    # Index (u,v), u<=v, means the monomial d_u*d_v, no chosen spectral values.
    monomials = [(u, v) for u in range(5) for v in range(u, 5)]
    for j in range(5):
        counts = [sum(p[j] == u for p in affine) for u in range(5)]
        require(counts == [4] * 5, "stationary local-phase cancellation")
        for k in range(5):
            polynomial = {m: 0 for m in monomials}
            visits = {(u, v): 0 for u in range(5) for v in range(5) if u != v}
            for p in affine:
                u, v = p[j], p[k]
                polynomial[u, u] += 1
                polynomial[v, v] += 1
                polynomial[tuple(sorted((u, v)))] -= 2
                if u != v:
                    visits[u, v] += 1
            expected = {m: (0 if j == k else (8 if m[0] == m[1] else -4))
                        for m in monomials}
            require(polynomial == expected, "fixed-profile quadratic echo identity")
            if j != k:
                require(set(visits.values()) == {1}, "ordered-pair transitivity")

    actual_counts = {}
    echo_carriers = 2 * sum(compiler_lengths)
    for c in (1, 4):
        for j in range(5):
            if c == j:
                continue
            for phase in (0, 1):
                compiled = local_matrix(compile_pair(c, j, 1, phase))
                require(compiled == rotation(c, j, 1, phase), "D-D compilation phase")
            # Full-sector action of the three *raw* G(-pi/2) echoes.
            for a in range(5):
                for b in range(5):
                    inside = {c, j}
                    if a in inside and b in inside:
                        expected = {5 * b + a: -II}
                    elif a == b:
                        expected = {5 * a + b: ONE}
                    else:
                        expected = {5 * a + b: II}
                    require(apply_word(block(c, j), basis(5 * a + b)) == expected,
                            "embedded exchange or spectator phase")
        word = contact(c)
        for s in range(5):
            require(apply_word(word, basis(5 * s + c)) == basis(5 * c + s),
                    "actual coherent contact target")
        others = [j for j in range(5) if j != c]
        a, b = others[:2]
        outside = apply_word(word, basis(5 * a + b))
        require(set(outside) == {5 * a + b}, "stronger full SWAP was not required")
        omitted_success = sum(set(apply_word(word, basis(5 * s + c), True)) == {5 * c + s}
                              for s in range(5))
        require(omitted_success == 1, "same-wait omitted-LS negative control")
        n_echo = sum(token[0] == "G" for token in word)
        local = [token for token in word if token[0] == "R"]
        carriers = n_echo * echo_carriers + len(local)
        angle_pi = F(n_echo * echo_carriers) + sum((F(t[2], 2) for t in local), F(0))
        require(n_echo == 12 and n_echo * 20 == 240, "LS pulse count")
        require(carriers <= 2923 and angle_pi <= 2918, "resource bounds")
        actual_counts[str(c)] = dict(ls_loops=240, carrier_pulses=carriers,
                                     carrier_angle_pi=str(angle_pi),
                                     coherent_inputs=5, omitted_ls_success=1)

    independent = subprocess.run([sys.executable, "-I", str(ROOT / "verify_independent.py")],
                                 capture_output=True, timeout=300, check=False)
    require(independent.returncode == 0 and independent.stderr == b"", "independent audit exit/stderr")
    require(json.loads(independent.stdout)["status"] == "PASS", "independent result")
    print("P-U-ION-LS-LOCAL-EXCHANGE-1")
    print("STATUS NON-CANONICAL EXACT IDEAL LOCAL CONSTRUCTION")
    print("PROFILE fixed non-scalar; one shared intensity; no independent level shifts")
    print("TWIRL 20 affine permutations; 25 symbolic quadratic identities")
    print("CARRIERS compiled positive-time 0-j star pulses only")
    print("CONTACTS " + json.dumps(actual_counts, sort_keys=True, separators=(",", ":")))
    print("MOTION operator closure analytic; inherited input cutoff n<=10; no reset")
    print("PHYSICAL ERROR / FULL HISTORY / FINITE CONTROLLER DILATION NOT CERTIFIED")
    print("INDEPENDENT_SHA256 " + hashlib.sha256(independent.stdout).hexdigest())
    print("LOCAL CONSTRUCTION AUDIT PASS")


if __name__ == "__main__":
    main()
