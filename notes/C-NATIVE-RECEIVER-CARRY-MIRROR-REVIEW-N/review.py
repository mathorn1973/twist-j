#!/usr/bin/env python3
"""NON-CANONICAL / L1. Independent review checker for PR #1884.

Candidate C-NATIVE-RECEIVER-CARRY-MIRROR-REVIEW-N. This file is the
code-independent exact checker specified by the review preregistration
PREREG.md in this directory. Its target is the probe
P-NATIVE-RECEIVER-CARRY-MIRROR-1 of PR #1884 (head
c9bd0bc5ac97ad034be399e6619695c7fc2c4a61, scientific source pin
aaf3ec7e925c2c0261604179ee4166d542233e14). It implements the frozen checks
R1 to R11. It changes no Canon text, registry row, status or release, and
it is not a Canon fold.

Source boundary followed by the writer of this file
---------------------------------------------------
Read:
  * target PROOF.md, PREREG.md and PROVENANCE.md at the pin;
  * target arithmetic_compiler.py. It is used here only for layout(2),
    multiplier_blocks(2, app) and expand_program(..., app,
    level='primitive'). Its execute() was read only to learn the meaning
    of the six primitives SUM, EQ, MUL, SHIFT, REFLECT and SCALE;
  * canon/CANON.md lines 470-520 (definition of U) and 600-620 (generator
    table in the coordinates (p1,p4,p1p,p4p,q,r));
  * the review PREREG.md in this directory.
Not opened, searched, listed or imported: target verify.py,
compiled_audit.py, EXPECTED.txt, RUN.md, RESULT.md, RUNTIME_SOURCES.json,
any other review checker, the coordinator's scratch files, and any PR or
CI text. The compiler's execute, inverse and reversed_blocks are never
called. The six-primitive interpreter and the inverse-word construction
below are this file's own. Before its public pin this file was only
byte-compiled and linted; no part of it was executed.

Method
------
All arithmetic is exact integer arithmetic; there is no floating point.
Every failed condition raises AssertionError through require(); there is
no bare assert, and an optimized interpreter (-O) is refused.

* Native U is encoded from the canonical CANON.md table and, separately,
  from the PROOF.md (A,B,C,D,q,r) transcription; the two are compared on
  all 5^6 states. U(n,x) = (n+1, g_{(sum x + 2 theta_n) mod 5}(x)) with
  theta_n = popcount(n) mod 2. Every first execution is at counter 0.
* O = Z[j] is represented by integer 4-vectors in the basis 1,j,j^2,j^3,
  reduced only with j^4 = -1-j-j^2-j^3. The norm N(y) is the exact integer
  determinant (fraction-free Bareiss elimination) of multiplication by y,
  and v_lambda(y) = v_5(N(y)) for y != 0. Every ideal-membership decision
  (residues, classes modulo lambda^2, second carry coefficients) uses this
  valuation. An exact quotient by lambda=1-j is formed as
  y*(1-j^2)(1-j^3)(1-j^4)/5 and certified by multiplying back by lambda.
* The compiled word is taken from the declared compiler after its byte
  length and SHA-256 are verified; the verified bytes themselves are
  executed through an importlib loader. Every primitive dictionary is
  validated and converted to an integer-opcode tuple. The inverse word is
  built here by reversing the order and inverting each primitive. This
  file's interpreter executes every word.
* R10 executes the occupied circuit (shear, word, swap gadget, inverse
  word, inverse shear) twice in succession on the same mutable memory for
  all 625 occupied states. R11 executes the PROOF section 8 schedule on
  the 62-cell carrier for all 625 piston tuples.

Output is one line of compact JSON with sorted keys, ending with
"status":"PASS". It contains no paths, times or platform values.

Command, from the repository root:
  python3 notes/C-NATIVE-RECEIVER-CARRY-MIRROR-REVIEW-N/review.py [--compiler PATH]
"""

import argparse
import hashlib
import importlib.abc
import importlib.util
import itertools
import json
import sys

DEFAULT_COMPILER = 'probes/P-NATIVE-RECEIVER-CARRY-MIRROR-1/arithmetic_compiler.py'
COMPILER_SIZE = 13728
COMPILER_SHA256 = '0e3668a7e664f572e6c6c34c49bf454e8d931e6dd05b8f2ebaf3c1b0cd761027'

WORD_LENGTH = 40348
WORD_INVENTORY = {'EQ': 30368, 'MUL': 5840, 'REFLECT': 1168, 'SCALE': 2,
                  'SHIFT': 112, 'SUM': 2858}

# 62-cell integrated carrier (PROOF section 8, review PREREG R11).
N_CELLS = 62
COMPILER_CELLS = 50
LOW = 0
HIGH = 1
WORK = tuple(range(2, 50))
ARCHIVE = 50
PRIMARY = (51, 52, 53, 54, 0, 55)
SECONDARY = (56, 57, 58, 59, 60, 61)
RECEIVER_R = 55
ZERO_WORK = [0] * 48
# External sentinel for R9: fixed nonzero values in cells 50..61.
SENTINEL = [1 + (i % 4) for i in range(N_CELLS - COMPILER_CELLS)]

ROUTING_PER_INPUT = 9
OCCUPIED_PER_PASS = 2 * WORD_LENGTH + 8
INTEGRATED_PER_INPUT = 2 * WORD_LENGTH + ROUTING_PER_INPUT

COUNTING = (0, 1, 2, 3, 4)
BALANCED = (-2, -1, 0, 1, 2)


def require(cond, label):
    """Raise AssertionError carrying the label when a condition fails."""
    if not cond:
        raise AssertionError(label)


def sha256_text(text):
    return hashlib.sha256(text.encode('ascii')).hexdigest()


# ------------------------------------------------------------------ F5 tools

def chi(v):
    """Quadratic character of F5, computed from the set of nonzero squares."""
    v %= 5
    if v == 0:
        return 0
    squares = {(t * t) % 5 for t in range(1, 5)}
    return 1 if v in squares else -1


def q_reader(q):
    """Native receiver reader R_q: q=1 -> -1, q in {0,2} -> +1."""
    require(q in (0, 1, 2), 'q-reader used only inside its declared contract')
    return -1 if q == 1 else 1


def carry_sign(residue_value):
    """Fixed carry-sign reader -chi(res C)."""
    return -chi(residue_value)


def inv5(v):
    v %= 5
    require(v != 0, 'inverse of a nonzero F5 element')
    hits = [w for w in range(1, 5) if (v * w) % 5 == 1]
    require(len(hits) == 1, 'unique F5 inverse')
    return hits[0]


# ----------------------------------------------------------------- native U
# Canonical generator table, canon/CANON.md, x = (p1,p4,p1p,p4p,q,r).

def gen_a(x):
    p1, p4, p1p, p4p, q, r = x
    return (p4 % 5, p1 % 5, p4p % 5, p1p % 5, q % 5, r % 5)


def gen_b(x):
    p1, p4, p1p, p4p, q, r = x
    return ((-p1p) % 5, (-p4p) % 5, (-p1) % 5, (-p4) % 5, (-q) % 5, (-r) % 5)


def gen_c(x):
    p1, p4, p1p, p4p, q, r = x
    return ((-p1p + 2) % 5, (-p4p + 1 + r) % 5, (-p1 + 2) % 5,
            (-p4 + 1 - r) % 5, (1 - q) % 5, (-r) % 5)


def gen_d(x):
    p1, p4, p1p, p4p, q, r = x
    return ((2 - p1) % 5, (1 - p4) % 5, (3 - p1p) % 5, (4 - p4p) % 5,
            (1 - q) % 5, (1 - r) % 5)


def gen_e(x):
    p1, p4, p1p, p4p, q, r = x
    return ((2 - p1) % 5, (1 - p4) % 5, (3 - p1p) % 5, (4 - p4p) % 5,
            (2 - q) % 5, (1 - r) % 5)


CANON_GENERATORS = (gen_a, gen_b, gen_c, gen_d, gen_e)
GENERATOR_NAMES = ('a', 'b', 'c', 'd', 'e')


def proof_generator(i, x):
    """The PROOF.md section 1 transcription in (A,B,C,D,q,r), typed separately."""
    require(type(i) is int and 0 <= i <= 4, 'PROOF generator index')
    A, B, C, D, q, r = x
    if i == 0:
        y = (B, A, D, C, q, r)
    elif i == 1:
        y = (-C, -D, -A, -B, -q, -r)
    elif i == 2:
        y = (2 - C, 1 - D + r, 2 - A, 1 - B - r, 1 - q, -r)
    elif i == 3:
        y = (2 - A, 1 - B, 3 - C, 4 - D, 1 - q, 1 - r)
    else:
        y = (2 - A, 1 - B, 3 - C, 4 - D, 2 - q, 1 - r)
    return tuple(v % 5 for v in y)


def theta(n):
    require(type(n) is int and n >= 0, 'native counter lies in N_0')
    return bin(n).count('1') % 2


def selector(n, x):
    return (sum(x) + 2 * theta(n)) % 5


def native_U(n, x):
    require(len(x) == 6, 'native checkpoint has six coordinates')
    return n + 1, CANON_GENERATORS[selector(n, x)](x)


# -------------------------------------------------------------- ring O=Z[j]
# Elements are integer 4-vectors (c0,c1,c2,c3) = c0+c1 j+c2 j^2+c3 j^3,
# reduced only with the defining relation j^4 = -1-j-j^2-j^3.

ZERO = (0, 0, 0, 0)
ONE = (1, 0, 0, 0)
JGEN = (0, 1, 0, 0)


def emb(n):
    return (n, 0, 0, 0)


def radd(a, b):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2], a[3] + b[3])


def rsub(a, b):
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2], a[3] - b[3])


def rneg(a):
    return (-a[0], -a[1], -a[2], -a[3])


def rscale(n, a):
    return (n * a[0], n * a[1], n * a[2], n * a[3])


def rmul(a, b):
    c = [0] * 7
    for i in range(4):
        ai = a[i]
        if ai:
            for k in range(4):
                c[i + k] += ai * b[k]
    # j^deg = j^(deg-4) * j^4 = -(j^(deg-4) + j^(deg-3) + j^(deg-2) + j^(deg-1))
    for deg in (6, 5, 4):
        top = c[deg]
        if top:
            c[deg] = 0
            for e in range(deg - 4, deg):
                c[e] -= top
    return (c[0], c[1], c[2], c[3])


def rpow(a, e):
    require(type(e) is int and e >= 0, 'nonnegative ring exponent')
    out = ONE
    for _ in range(e):
        out = rmul(out, a)
    return out


BASIS = tuple(rpow(JGEN, i) for i in range(4))
LAMBDA = rsub(ONE, JGEN)
# (1-j^2)(1-j^3)(1-j^4) = 5/lambda, since the product over k=1..4 of (1-j^k) is 5.
LAMBDA_COFACTOR = rmul(rmul(rsub(ONE, rpow(JGEN, 2)), rsub(ONE, rpow(JGEN, 3))),
                       rsub(ONE, rpow(JGEN, 4)))


def det_bareiss(rows):
    """Exact integer determinant by fraction-free Bareiss elimination."""
    a = [list(row) for row in rows]
    n = len(a)
    require(n >= 1 and all(len(row) == n for row in a), 'square integer matrix')
    sign = 1
    prev = 1
    for k in range(n - 1):
        if a[k][k] == 0:
            pivot = -1
            for i in range(k + 1, n):
                if a[i][k] != 0:
                    pivot = i
                    break
            if pivot < 0:
                return 0
            a[k], a[pivot] = a[pivot], a[k]
            sign = -sign
        row_k = a[k]
        akk = row_k[k]
        for i in range(k + 1, n):
            row_i = a[i]
            aik = row_i[k]
            for col in range(k + 1, n):
                quo, rem = divmod(row_i[col] * akk - aik * row_k[col], prev)
                require(rem == 0, 'Bareiss step divides exactly')
                row_i[col] = quo
            row_i[k] = 0
        prev = akk
    return sign * a[n - 1][n - 1]


def mult_matrix(y):
    cols = [rmul(y, e) for e in BASIS]
    return [[cols[c][r] for c in range(4)] for r in range(4)]


def norm(y):
    return det_bareiss(mult_matrix(y))


def v5(n):
    require(type(n) is int and n != 0, 'v_5 of a nonzero integer')
    n = abs(n)
    v = 0
    while n % 5 == 0:
        n //= 5
        v += 1
    return v


def v_lambda(y):
    require(y != ZERO, 'v_lambda of a nonzero element')
    N = norm(y)
    require(N != 0, 'a nonzero element of Z[j] has nonzero norm')
    return v5(N)


def in_lambda_power(y, k):
    """Membership of y in (lambda^k), decided by the exact norm valuation."""
    return y == ZERO or v_lambda(y) >= k


def div_lambda(y):
    """Exact quotient y/lambda, certified by multiplying back."""
    require(in_lambda_power(y, 1), 'numerator lies in (lambda)')
    w = rmul(y, LAMBDA_COFACTOR)
    require(all(c % 5 == 0 for c in w), 'cofactor product divisible by 5')
    quo = (w[0] // 5, w[1] // 5, w[2] // 5, w[3] // 5)
    require(rmul(LAMBDA, quo) == y, 'quotient by lambda certified by multiplying back')
    return quo


def residue(y):
    """The unique c in F5 with y-c in (lambda), found by valuation search."""
    hits = [c for c in range(5) if in_lambda_power(rsub(y, emb(c)), 1)]
    require(len(hits) == 1, 'unique residue modulo lambda')
    return hits[0]


def class_rep(lo, hi):
    return radd(emb(lo), rscale(hi, LAMBDA))


def class_mod_lambda2(y):
    """The unique (lo,hi) in F5^2 with y-(lo+hi*lambda) in (lambda^2)."""
    hits = [(lo, hi) for lo in range(5) for hi in range(5)
            if in_lambda_power(rsub(y, class_rep(lo, hi)), 2)]
    require(len(hits) == 1, 'unique class lo+hi*lambda modulo lambda^2')
    return hits[0]


def section_rep(section, r):
    hits = [e for e in section if (e - r) % 5 == 0]
    require(len(hits) == 1, 'one section representative per residue')
    return hits[0]


def second_coefficient(carry, lift):
    """u = res((C - v_lift)/lambda) for the lift of v = res(C) in a section."""
    v = residue(carry)
    v_lift = section_rep(lift, v)
    return residue(div_lambda(rsub(carry, emb(v_lift))))


# ------------------------------------------------- six-primitive interpreter

OP_NAMES = ('EQ', 'MUL', 'SUM', 'REFLECT', 'SHIFT', 'SCALE')
OP_CODES = {name: code for code, name in enumerate(OP_NAMES)}
OP_FIELDS = {
    'SUM': ('op', 'x', 'target', 'k'),
    'EQ': ('op', 'x', 'value', 'target', 'k'),
    'MUL': ('op', 'x', 'y', 'target', 'sign'),
    'SHIFT': ('op', 'target', 'k'),
    'REFLECT': ('op', 'target'),
    'SCALE': ('op', 'target', 'k'),
}


def compact_primitive(block, n_wires):
    """Validate one primitive dictionary and return (opcode, x, y, target, k).

    Opcodes: 0 EQ (y is the compared value), 1 MUL, 2 SUM, 3 REFLECT,
    4 SHIFT, 5 SCALE. k is the coefficient or sign reduced modulo 5.
    """
    require(type(block) is dict, 'primitive is a dictionary')
    op = block.get('op')
    require(op in OP_FIELDS, 'primitive in the six-primitive alphabet')
    require(set(block) == set(OP_FIELDS[op]), 'primitive has exactly its fields')
    for key in OP_FIELDS[op][1:]:
        require(type(block[key]) is int, 'primitive field is an integer')
    t = block['target']
    x = y = 0
    k = 0
    if op == 'SUM':
        x = block['x']
        wires = (x, t)
        k = block['k'] % 5
    elif op == 'EQ':
        x = block['x']
        y = block['value']
        require(0 <= y <= 4, 'EQ compares with an F5 value')
        wires = (x, t)
        k = block['k'] % 5
    elif op == 'MUL':
        x = block['x']
        y = block['y']
        wires = (x, y, t)
        k = block['sign'] % 5
    elif op == 'SHIFT':
        wires = (t,)
        k = block['k'] % 5
    elif op == 'REFLECT':
        wires = (t,)
    else:
        wires = (t,)
        k = block['k'] % 5
        require(k != 0, 'SCALE coefficient is invertible')
    require(len(set(wires)) == len(wires), 'primitive wires are distinct')
    require(all(0 <= w < n_wires for w in wires), 'primitive wires inside the carrier')
    return (OP_CODES[op], x, y, t, k)


def invert_word(word):
    """Reverse the order and invert each primitive."""
    out = []
    for op, x, y, t, k in reversed(word):
        if op in (0, 1, 2, 4):
            out.append((op, x, y, t, (-k) % 5))
        elif op == 5:
            out.append((op, x, y, t, pow(k, -1, 5)))
        else:
            require(op == 3, 'known primitive to invert')
            out.append((op, x, y, t, k))
    return out


def run_word(word, m):
    """Execute a compact word on memory m in place; return primitives executed."""
    for op, x, y, t, k in word:
        if op == 0:                                   # EQ
            if m[x] == y:
                m[t] = (m[t] + k) % 5
        elif op == 1:                                 # MUL
            m[t] = (m[t] + k * m[x] * m[y]) % 5
        elif op == 2:                                 # SUM
            m[t] = (m[t] + k * m[x]) % 5
        elif op == 3:                                 # REFLECT
            m[t] = 4 - m[t]
        elif op == 4:                                 # SHIFT
            m[t] = (m[t] + k) % 5
        elif op == 5:                                 # SCALE
            m[t] = (k * m[t]) % 5
        else:
            require(False, 'opcode in the interpreter alphabet')
    return len(word)


def word_inventory(word):
    counts = {}
    for item in word:
        name = OP_NAMES[item[0]]
        counts[name] = counts.get(name, 0) + 1
    return dict(sorted(counts.items()))


def word_text(word):
    lines = []
    for op, x, y, t, k in word:
        if op == 2:
            fields = (x, t, k)
        elif op in (0, 1):
            fields = (x, y, t, k)
        elif op == 3:
            fields = (t,)
        else:
            fields = (t, k)
        lines.append(OP_NAMES[op] + ' ' + ' '.join(str(v) for v in fields))
    return '\n'.join(lines) + '\n'


def memory_line(label, m):
    return label + ' ' + ','.join(str(v) for v in m)


def origin_tick(m, cells, counters, name):
    """One native tick of the machine at the given cells, from counter 0."""
    require(counters[name] == 0, 'every first execution is at counter zero')
    x = tuple(m[c] for c in cells)
    n1, y = native_U(counters[name], x)
    counters[name] = n1
    for c, v in zip(cells, y, strict=True):
        m[c] = v
    return y


# ------------------------------------------------------------ compiler load

class VerifiedSourceLoader(importlib.abc.Loader):
    """Execute exactly the verified compiler bytes as a module."""

    def __init__(self, data):
        self._data = data

    def create_module(self, spec):
        return None

    def exec_module(self, module):
        code = compile(self._data, 'arithmetic_compiler.py', 'exec',
                       dont_inherit=True, optimize=0)
        exec(code, module.__dict__)


def load_compiler(path):
    with open(path, 'rb') as handle:
        data = handle.read()
    require(len(data) == COMPILER_SIZE, 'R9 compiler file has 13728 bytes')
    digest = hashlib.sha256(data).hexdigest()
    require(digest == COMPILER_SHA256, 'R9 compiler file SHA-256')
    sys.dont_write_bytecode = True
    loader = VerifiedSourceLoader(data)
    spec = importlib.util.spec_from_loader('twistj_review_declared_compiler', loader)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    for name in ('layout', 'multiplier_blocks', 'expand_program'):
        require(callable(getattr(module, name, None)), 'compiler provides ' + name)
    return module, {'bytes': len(data), 'sha256': digest}


# ----------------------------------------------------------------------- R1

def check_r1(states):
    comparisons = 0
    for i in range(5):
        g = CANON_GENERATORS[i]
        for x in states:
            require(g(x) == proof_generator(i, x),
                    'R1 canonical and PROOF.md generator forms agree')
            comparisons += 1
    require(comparisons == 5 * 15625, 'R1 all five generators on all 5^6 states')
    ready = []
    receivers = {s: set() for s in range(5)}
    per_s = {s: 0 for s in range(5)}
    for pist in itertools.product(range(5), repeat=4):
        x = pist + (0, 1)
        s = (pist[0] + pist[1] + pist[2] + pist[3] + 1) % 5
        require(selector(0, x) == s, 'R1 s=A+B+C+D+1 selects the generator at counter zero')
        n1, y = native_U(0, x)
        require(n1 == 1, 'R1 the counter advances from 0 to 1')
        require(y == CANON_GENERATORS[s](x), 'R1 the first tick applies g_s')
        receivers[s].add((y[4], y[5]))
        per_s[s] += 1
        ready.append((pist, s, y))
    require(len(ready) == 625, 'R1 625 ready states')
    declared = {0: (0, 1), 1: (0, 4), 2: (1, 4), 3: (1, 0), 4: (2, 0)}
    rows = {}
    for s in range(5):
        require(per_s[s] == 125, 'R1 each s has 125 preparations')
        require(len(receivers[s]) == 1, 'R1 the post-tick receiver is constant on each sheet')
        rows[s] = next(iter(receivers[s]))
        require(rows[s] == declared[s], 'R1 declared post-tick receiver row')
    require(len(set(rows.values())) == 5, 'R1 the five receiver pairs are distinct')
    derived = {
        'generator_by_s': {str(s): GENERATOR_NAMES[s] for s in range(5)},
        'preparations_per_s': {str(s): per_s[s] for s in range(5)},
        'receiver_rows': {str(s): list(rows[s]) for s in range(5)},
        'zero_piston_tuple_sheet': ready[0][1],
    }
    return ready, rows, derived, comparisons


# ----------------------------------------------------------------------- R2

def check_r2(ready, rows):
    admitted_rows = [(s, rows[s]) for s in (1, 2, 3, 4)]
    hits = []
    maps = 0
    for alpha, beta, gamma in itertools.product(range(5), repeat=3):
        maps += 1
        if all((alpha * q + beta * r + gamma) % 5 == s for s, (q, r) in admitted_rows):
            hits.append((alpha, beta, gamma))
    require(maps == 125, 'R2 all 125 affine maps')
    require(hits == [(1, 1, 2)], 'R2 (1,1,2) is the unique affine port on the admitted rows')
    q0, r0 = rows[0]
    port_s0 = (q0 + r0 + 2) % 5
    require(port_s0 == 3, 'R2 the port sends the s=0 row to 3')
    reader = {}
    for s, (q, _r) in admitted_rows:
        require(q_reader(q) == chi(s), 'R2 the q-reader equals chi(s) on the admitted rows')
        reader[str(q)] = q_reader(q)
    n_admitted = n_controls = 0
    for _pist, s, y in ready:
        value = (y[4] + y[5] + 2) % 5
        if s == 0:
            require(value == 3, 'R2 the port routes every s=0 control to 3')
            n_controls += 1
        else:
            require(value == s, 'R2 the port returns s on every admitted preparation')
            require(q_reader(y[4]) == chi(s),
                    'R2 the q-reader equals chi(s) on every admitted preparation')
            n_admitted += 1
    require(n_admitted == 500 and n_controls == 125, 'R2 500 admitted and 125 controls')
    derived = {'affine_port': list(hits[0]), 'port_value_on_s0_row': port_s0,
               'q_reader': reader, 'chi': {str(v): chi(v) for v in range(5)}}
    return derived, maps


# ----------------------------------------------------------------------- R3

def check_r3(states):
    forms = ((1, 0), (-1, 0), (-1, 2), (-1, 2), (-1, 3))
    form_names = ('z', '-z', '2-z', '2-z', '3-z')
    trace_by_generator = []
    for i in range(5):
        g = CANON_GENERATORS[i]
        table = {}
        for x in states:
            z = sum(x) % 5
            tr = sum(g(x)) % 5
            require(table.setdefault(z, tr) == tr, 'R3 the trace of g_i depends only on z')
        require(sorted(table) == [0, 1, 2, 3, 4], 'R3 trace table covers F5')
        eps, c = forms[i]
        for z in range(5):
            require(table[z] == (eps * z + c) % 5, 'R3 trace forms z,-z,2-z,2-z,3-z')
        trace_by_generator.append([table[z] for z in range(5)])
    tau = {}
    closure = 0
    for t in (0, 1):
        require(theta(t) == t, 'R3 counters 0 and 1 carry clock bits 0 and 1')
        table = {}
        for x in states:
            y = native_U(t, x)[1]
            z = sum(x) % 5
            tr = sum(y) % 5
            require(table.setdefault(z, tr) == tr, 'R3 trace closure on all 5^6 states')
            closure += 1
        require(sorted(table) == [0, 1, 2, 3, 4], 'R3 tau table covers F5')
        tau[t] = tuple(table[z] for z in range(5))
    require(closure == 2 * 15625, 'R3 both clock bits on all 5^6 states')
    require(tau[0] == (0, 4, 0, 4, 4), 'R3 tau_0 = (0,4,0,4,4)')
    require(tau[1] == (2, 1, 1, 3, 1), 'R3 tau_1 = (2,1,1,3,1)')
    images = {}
    for t in (0, 1):
        image = sorted({tau[t][s] for s in (1, 2, 3, 4)})
        require(len(image) == 2, 'R3 image cardinality two on {1,2,3,4}')
        images[str(t)] = image

    # Sanity check 1: trace level, every binary clock word of length 1..10.
    target = tuple((2 * s) % 5 for s in (1, 2, 3, 4))
    trace_words = 0
    for length in range(1, 11):
        for word in itertools.product((0, 1), repeat=length):
            vals = [1, 2, 3, 4]
            for t in word:
                vals = [tau[t][v] for v in vals]
            require(tuple(vals) != target, 'R3 no clock word realizes s -> 2s (trace level)')
            trace_words += 1
    require(trace_words == 2046, 'R3 2046 clock words of length 1 to 10')

    # Sanity check 2: state level on the 500 admitted ready states, same words.
    admitted = [pist + (0, 1) for pist in itertools.product(range(5), repeat=4)
                if (sum(pist) + 1) % 5 != 0]
    require(len(admitted) == 500, 'R3 500 admitted ready states')
    goals = [(2 * sum(x)) % 5 for x in admitted]
    state_words = 0
    stack = [(admitted, 0)]
    while stack:
        current, depth = stack.pop()
        for t in (0, 1):
            nxt = [native_U(t, x)[1] for x in current]
            hit = all(sum(y) % 5 == goal for y, goal in zip(nxt, goals, strict=True))
            require(not hit, 'R3 no clock word realizes s -> 2s (state level)')
            state_words += 1
            if depth + 1 < 10:
                stack.append((nxt, depth + 1))
    require(state_words == 2046, 'R3 state-level words of length 1 to 10')

    # The actual origin-zero native clock word is one of them.
    native_bits = ''.join(str(theta(n)) for n in range(10))
    current = [(0, x) for x in admitted]
    for _length in range(1, 11):
        current = [native_U(n, x) for n, x in current]
        hit = all(sum(x) % 5 == goal for (_n, x), goal in zip(current, goals, strict=True))
        require(not hit, 'R3 the origin-zero native clock does not realize s -> 2s')
    derived = {
        'native_clock_word': native_bits,
        'tau_0': list(tau[0]),
        'tau_1': list(tau[1]),
        'tau_images_on_nonzero': images,
        'trace_by_generator': {GENERATOR_NAMES[i]: trace_by_generator[i] for i in range(5)},
        'trace_forms': {GENERATOR_NAMES[i]: form_names[i] for i in range(5)},
    }
    return derived, closure, trace_words, state_words


# ----------------------------------------------------------------------- R4

def check_r4():
    J = radd(ONE, rpow(JGEN, 2))
    JINV = rneg(radd(JGEN, rpow(JGEN, 2)))
    require(rpow(JGEN, 5) == ONE and JGEN != ONE, 'ring self-test: j^5 = 1 and j != 1')
    require(rmul(LAMBDA, LAMBDA_COFACTOR) == emb(5), 'ring self-test: lambda*(5/lambda) = 5')
    require(rmul(J, JINV) == ONE, 'R4 J*J^-1 = 1')
    l2 = rmul(LAMBDA, LAMBDA)
    J_lambda = (2, -2, 1)
    JINV_lambda = (-2, 3, -1)
    lam_powers = (ONE, LAMBDA, l2)
    J_from = ZERO
    JINV_from = ZERO
    for coef, power in zip(J_lambda, lam_powers, strict=True):
        J_from = radd(J_from, rscale(coef, power))
    for coef, power in zip(JINV_lambda, lam_powers, strict=True):
        JINV_from = radd(JINV_from, rscale(coef, power))
    require(J_from == J, 'R4 J = 2-2l+l^2')
    require(JINV_from == JINV, 'R4 J^-1 = -2+3l-l^2')
    norms = {'5': norm(emb(5)), 'J': norm(J), 'J_inverse': norm(JINV),
             'lambda': norm(LAMBDA), 'lambda^2': norm(l2)}
    require(norms['lambda'] == 5, 'ring self-test: N(lambda) = 5')
    require(norms['J'] == 1 and norms['J_inverse'] == 1, 'ring self-test: J and J^-1 have norm 1')
    require(norms['5'] == 625, 'ring self-test: N(5) = 625')
    require(norms['lambda^2'] == 25, 'R4 index of (lambda^2) is 25')
    v_five = v_lambda(emb(5))
    require(v_five == 4, 'R4 v_lambda(5) = 4')
    reps = [((lo, hi), class_rep(lo, hi)) for lo in range(5) for hi in range(5)]
    pairs = 0
    for (_k1, y1), (_k2, y2) in itertools.combinations(reps, 2):
        d = rsub(y1, y2)
        require(d != ZERO and v_lambda(d) < 2,
                'R4 the 25 classes lo+hi*lambda are pairwise incongruent mod lambda^2')
        pairs += 1
    require(pairs == 300, 'R4 all 300 class pairs')
    F = {}
    I = {}
    for lo, hi in itertools.product(range(5), repeat=2):
        y = class_rep(lo, hi)
        F[(lo, hi)] = class_mod_lambda2(rmul(J, y))
        I[(lo, hi)] = class_mod_lambda2(rmul(JINV, y))
        require(F[(lo, hi)] == ((2 * lo) % 5, (3 * lo + 2 * hi) % 5),
                'R4 F(lo,hi) = (2lo,3lo+2hi) recovered by valuation search')
        require(I[(lo, hi)] == ((3 * lo) % 5, (3 * lo + 3 * hi) % 5),
                'R4 I(lo,hi) = (3lo,3lo+3hi) recovered by valuation search')
    for key in F:
        require(I[F[key]] == key and F[I[key]] == key, 'R4 F and I are mutually inverse')
    derived = {
        'F': [[lo, hi, F[(lo, hi)][0], F[(lo, hi)][1]]
              for lo, hi in itertools.product(range(5), repeat=2)],
        'I': [[lo, hi, I[(lo, hi)][0], I[(lo, hi)][1]]
              for lo, hi in itertools.product(range(5), repeat=2)],
        'J_j_basis': list(J),
        'J_inverse_j_basis': list(JINV),
        'J_inverse_lambda_coefficients': list(JINV_lambda),
        'J_lambda_coefficients': list(J_lambda),
        'lambda_cofactor_j_basis': list(LAMBDA_COFACTOR),
        'norms': norms,
        'v_lambda_5': v_five,
    }
    return J, JINV, F, I, derived, pairs


# ----------------------------------------------------------------------- R5

def check_r5(F, I):
    def shear(state, sign):
        q, r, h, k = state
        return ((q + sign * (r + 2)) % 5, r, h, k)

    def apply_F(state):
        q, r, h, k = state
        lo, hi = F[(q, h)]
        return (lo, r, hi, k)

    def apply_I(state):
        q, r, h, k = state
        lo, hi = I[(q, h)]
        return (lo, r, hi, k)

    def swap(state):
        q, r, h, k = state
        return (q, r, k, h)

    L = {}
    for state in itertools.product(range(5), repeat=4):
        L[state] = shear(apply_I(swap(apply_F(shear(state, 1)))), -1)
    require(len(L) == 625, 'R5 all 625 (q,r,h,k)')
    for state, image in L.items():
        q, r, h, k = state
        b = (q + r + 2) % 5
        require(image == (q, r, (b + 3 * k) % 5, (3 * b + 2 * h) % 5),
                'R5 L(q,r,h,k) = (q,r,b+3k,3b+2h)')
        require(L[image] == state, 'R5 L^2 = id')
    P = {state: apply_F(shear(state, 1)) for state in L}
    P_inv = {}
    for state, image in P.items():
        require(image not in P_inv, 'R5 shear followed by F is injective')
        P_inv[image] = state
    require(len(P_inv) == 625, 'R5 shear followed by F is a bijection')
    for state in L:
        require(P_inv[swap(P[state])] == L[state],
                'R5 L is the conjugate of SWAP(h,k) by F after the shear')
    for q, r in itertools.product(range(5), repeat=2):
        b = (q + r + 2) % 5
        loaded = shear((q, r, 0, 0), 1)
        require(loaded == (b, r, 0, 0), 'R5 loaded b = q+r+2')
        forward = apply_F(loaded)
        require(forward == ((2 * b) % 5, r, (3 * b) % 5, 0), 'R5 forward output (a,v) = (2b,3b)')
        swapped = swap(forward)
        require(swapped == ((2 * b) % 5, r, 0, (3 * b) % 5),
                'R5 after the swap: low a, high 0, archive v')
        inverse = apply_I(swapped)
        require(inverse == (b, r, b, (3 * b) % 5), 'R5 inverse output (b,w) = (b,b)')
        final = shear(inverse, -1)
        require(final == (q, r, b, (3 * b) % 5) and final == L[(q, r, 0, 0)],
                'R5 final receiver (q,r), high w=b, archive v=3b')
    for b in range(5):
        require(F[(b, 0)] == ((2 * b) % 5, (3 * b) % 5), 'R5 F(b,0) = (2b,3b)')
        require(I[F[(b, 0)]] == (b, 0), 'R5 full-word control I(F(b,0)) = (b,0)')
    derived = {'L_closed_form': '(q,r,b+3k,3b+2h) with b=q+r+2',
               'blank_intermediates': '(b,0)->(2b,3b)->(2b,0|3b)->(b,b)'}
    return L, derived


# ----------------------------------------------------------------------- R6

def check_r6(J, JINV):
    sections = {'balanced': BALANCED, 'counting': COUNTING}
    tables = {}
    slopes_J = set()
    slopes_JINV = set()
    for name in ('counting', 'balanced'):
        section = sections[name]
        require(section_rep(section, 0) == 0, 'R6 zero is represented by zero')
        rows = []
        for b in section:
            bb = b % 5
            yJ = rmul(J, emb(b))
            out_res = residue(yJ)
            require(out_res == (2 * b) % 5, 'R6 output residue of J is 2b')
            a = section_rep(section, out_res)
            C = div_lambda(rsub(yJ, emb(a)))
            yI = rmul(JINV, emb(a))
            ret_res = residue(yI)
            require(ret_res == (3 * a) % 5, 'R6 output residue of J^-1 at a is 3a')
            b_ret = section_rep(section, ret_res)
            require(b_ret == b, 'R6 the paired return is exactly b')
            C_mirror = div_lambda(rsub(yI, emb(b)))
            require(C_mirror == rneg(rmul(JINV, C)), 'R6 C_mirror = -J^-1 C exactly')
            v = residue(C)
            w = residue(C_mirror)
            require(v == (3 * b) % 5, 'R6 res C = 3b')
            require(w == bb, 'R6 res C_mirror = b')
            require(w == (2 * v) % 5, 'R6 w = 2v')
            require(carry_sign(v) == chi(b), 'R6 forward sign chi(b)')
            require(carry_sign(w) == -chi(b), 'R6 paired inverse sign -chi(b)')
            yS = rmul(JINV, emb(b))
            same_res = residue(yS)
            require(same_res == (3 * b) % 5, 'R6 output residue of J^-1 at b is 3b')
            a_minus = section_rep(section, same_res)
            C_same = div_lambda(rsub(yS, emb(a_minus)))
            v_same = residue(C_same)
            require(v_same == (3 * b) % 5, 'R6 same-input control has residue 3b')
            require(carry_sign(v_same) == carry_sign(v),
                    'R6 same-input control sign agrees with the forward sign')
            u_rows = {}
            for lift_name in ('counting', 'balanced'):
                lift = sections[lift_name]
                u_plus = second_coefficient(C, lift)
                u_minus = second_coefficient(C_same, lift)
                require(u_plus == bb, 'R6 second coefficient u = b for J')
                require(u_minus == (-b) % 5, 'R6 second coefficient u = -b for J^-1')
                u_rows[lift_name] = [u_plus, u_minus]
                if bb != 0:
                    slope_plus = (u_plus * inv5(v)) % 5
                    slope_minus = (u_minus * inv5(v_same)) % 5
                    require(slope_plus == 2, 'R6 u/v = 2 for J')
                    require(slope_minus == 3, 'R6 u/v = 3 for J^-1')
                    slopes_J.add(slope_plus)
                    slopes_JINV.add(slope_minus)
            if b == 0:
                require(C == ZERO and C_mirror == ZERO and C_same == ZERO,
                        'R6 every carry is zero when b = 0')
            rows.append({'C': list(C), 'C_mirror': list(C_mirror), 'C_same_input': list(C_same),
                         'a': a, 'a_same_input': a_minus, 'b': b, 'u_J_Jinv_by_lift': u_rows,
                         'v': v, 'v_same_input': v_same, 'w': w})
        tables[name] = rows
    require(slopes_J == {2} and slopes_JINV == {3}, 'R6 slopes 2 (J) and 3 (J^-1)')

    # Proof-argument stress test: every integer b and every integer lift a of
    # the output residue with |b|,|a| <= 30.
    stress_J = stress_JINV = 0
    for b in range(-30, 31):
        bb = b % 5
        yJ = rmul(J, emb(b))
        yS = rmul(JINV, emb(b))
        out_plus = residue(yJ)
        out_minus = residue(yS)
        require(out_plus == (2 * b) % 5, 'R6 stress: output residue of J is 2b')
        require(out_minus == (3 * b) % 5, 'R6 stress: output residue of J^-1 is 3b')
        for a in range(-30, 31):
            if (a - out_plus) % 5 == 0:
                C = div_lambda(rsub(yJ, emb(a)))
                C_mirror = div_lambda(rsub(rmul(JINV, emb(a)), emb(b)))
                require(C_mirror == rneg(rmul(JINV, C)), 'R6 stress: C_mirror = -J^-1 C')
                require(residue(C) == (3 * b) % 5, 'R6 stress: res C = 3b')
                require(residue(C_mirror) == bb, 'R6 stress: res C_mirror = b')
                for lift in (COUNTING, BALANCED):
                    require(second_coefficient(C, lift) == bb, 'R6 stress: u = b for J')
                stress_J += 1
            if (a - out_minus) % 5 == 0:
                C_same = div_lambda(rsub(yS, emb(a)))
                require(residue(C_same) == (3 * b) % 5, 'R6 stress: same-input residue 3b')
                for lift in (COUNTING, BALANCED):
                    require(second_coefficient(C_same, lift) == (-b) % 5,
                            'R6 stress: u = -b for J^-1')
                stress_JINV += 1
    require(stress_J == 745 and stress_JINV == 745, 'R6 stress: 745 cases per multiplier')
    derived = {'carry_tables': tables, 'slopes': {'J': 2, 'J_inverse': 3}}
    return derived, stress_J, stress_JINV


# ----------------------------------------------------------------------- R7

def check_r7(ready):
    wrong = agree = admitted = 0
    agree_sheets = set()
    for _pist, s, y in ready:
        if s == 0:
            continue
        admitted += 1
        mark = (y[4] + y[5]) % 5
        if mark != s:
            wrong += 1
        if chi(mark) == chi(s):
            agree += 1
            agree_sheets.add(s)
    require(admitted == 500, 'R7 500 admitted preparations')
    require(wrong == 500, 'R7 q+r without +2 gives the wrong mark on all 500')
    require(agree == 125 and agree_sheets == {1},
            'R7 sign-only comparison agrees for exactly the 125 preparations of s=1')
    return {'sign_only_agreement_sheets': sorted(agree_sheets), 'sign_only_agreements': agree,
            'wrong_marks': wrong}


# ----------------------------------------------------------------------- R8

def check_r8():
    rows = {}
    ticks = 0
    for a in (1, 2, 3, 4):
        pistons = [4, 0, 0, 0]
        pistons[0] = (pistons[0] + a) % 5
        x = tuple(pistons) + (0, 1)
        require(sum(x) % 5 == a, 'R8 the prepared trace equals a')
        n1, y = native_U(0, x)
        require(n1 == 1, 'R8 origin tick')
        ticks += 1
        require(q_reader(y[4]) == chi(a), 'R8 one origin tick gives q-reader chi(a)')
        rows[a] = y
    for b in (1, 2, 3, 4):
        a = (2 * b) % 5
        require(q_reader(rows[a][4]) == -chi(b), 'R8 for a=2b the reader equals -chi(b)')
    derived = {str(a): {'checkpoint': list(rows[a]), 'q_reader': q_reader(rows[a][4])}
               for a in (1, 2, 3, 4)}
    return derived, ticks


# ----------------------------------------------------------------------- R9

def check_r9(compiler, F, I):
    app = compiler.layout(2)
    require(type(app) is dict, 'R9 layout(2) is a dictionary')
    require(app.get('data') == [0, 1], 'R9 layout(2) data cells 0,1')
    require(app.get('cells') == COMPILER_CELLS, 'R9 layout(2) has 50 compiler cells')
    blocks = list(compiler.expand_program(compiler.multiplier_blocks(2, app), app,
                                          level='primitive'))
    fwd = [compact_primitive(block, COMPILER_CELLS) for block in blocks]
    require(len(fwd) == WORD_LENGTH, 'R9 word length 40348')
    inventory = word_inventory(fwd)
    require(inventory == WORD_INVENTORY, 'R9 primitive inventory')
    inv = invert_word(fwd)
    require(len(inv) == WORD_LENGTH and word_inventory(inv) == WORD_INVENTORY,
            'R9 inverse word has the same length and inventory')
    require(invert_word(inv) == fwd, 'R9 inverse-word construction is an involution')
    wires_used = sorted({w for op, x, y, t, k in fwd
                         for w in ((x, t) if op in (0, 2) else (x, y, t) if op == 1 else (t,))})
    require(wires_used[0] >= 0 and wires_used[-1] <= 49, 'R9 wires inside 0..49')

    base = [0] * N_CELLS
    base[COMPILER_CELLS:] = SENTINEL
    F_compiled = {}
    I_compiled = {}
    lines = []
    executed = 0
    for lo, hi in itertools.product(range(5), repeat=2):
        for label, word, table in (('forward', fwd, F_compiled), ('inverse', inv, I_compiled)):
            m = list(base)
            m[LOW] = lo
            m[HIGH] = hi
            executed += run_word(word, m)
            require(m[2:50] == ZERO_WORK, 'R9 cells 2..49 return to zero')
            require(m[COMPILER_CELLS:] == SENTINEL, 'R9 external sentinel unchanged')
            table[(lo, hi)] = (m[LOW], m[HIGH])
            lines.append(memory_line('%s %d %d' % (label, lo, hi), m))
    require(F_compiled == F, 'R9 the compiled word gives F on all 25 inputs')
    require(I_compiled == I, 'R9 the independent inverse word gives I on all 25 inputs')
    for lo, hi in itertools.product(range(5), repeat=2):
        require(F_compiled[(lo, hi)] == ((2 * lo) % 5, (3 * lo + 2 * hi) % 5),
                'R9 compiled forward equals declared F')
        require(I_compiled[(lo, hi)] == ((3 * lo) % 5, (3 * lo + 3 * hi) % 5),
                'R9 compiled inverse equals declared I')
    require(executed == 25 * 2 * WORD_LENGTH, 'R9 primitive count')
    info = {
        'component_endpoints_sha256': sha256_text('\n'.join(lines) + '\n'),
        'forward_word_sha256': sha256_text(word_text(fwd)),
        'inverse_word_sha256': sha256_text(word_text(inv)),
        'inventory': inventory,
        'length': len(fwd),
        'wires_used': len(wires_used),
    }
    return fwd, inv, info, executed


def build_routing():
    def word(dicts):
        return [compact_primitive(d, N_CELLS) for d in dicts]
    shear = word([{'op': 'SUM', 'x': RECEIVER_R, 'target': LOW, 'k': 1},
                  {'op': 'SHIFT', 'target': LOW, 'k': 2}])
    feed = word([{'op': 'SUM', 'x': LOW, 'target': SECONDARY[0], 'k': 1}])
    gadget = word([{'op': 'SUM', 'x': HIGH, 'target': ARCHIVE, 'k': 1},
                   {'op': 'SUM', 'x': ARCHIVE, 'target': HIGH, 'k': -1},
                   {'op': 'SUM', 'x': HIGH, 'target': ARCHIVE, 'k': 1},
                   {'op': 'SCALE', 'target': HIGH, 'k': -1}])
    inverse_shear = invert_word(shear)
    total = len(shear) + len(feed) + len(gadget) + len(inverse_shear)
    require(total == ROUTING_PER_INPUT, 'nine routing primitives per integrated input')
    return {'feed': feed, 'gadget': gadget, 'inverse_shear': inverse_shear, 'shear': shear}


# ---------------------------------------------------------------------- R10

def check_gadget(gadget):
    executed = 0
    exchanges = 0
    for h, k in itertools.product(range(5), repeat=2):
        m = [i % 5 for i in range(N_CELLS)]
        m[HIGH] = h
        m[ARCHIVE] = k
        start = list(m)
        executed += run_word(gadget, m)
        require(m[HIGH] == k and m[ARCHIVE] == h, 'R10 the gadget exchanges (h,k)')
        require(all(m[i] == start[i] for i in range(N_CELLS) if i not in (HIGH, ARCHIVE)),
                'R10 the gadget touches only high and archive')
        exchanges += 1
    require(exchanges == 25 and executed == 25 * 4, 'R10 gadget on all 25 (h,k)')
    return exchanges, executed


def check_r10(fwd, inv, routing, L):
    shear = routing['shear']
    gadget = routing['gadget']
    inverse_shear = routing['inverse_shear']
    base = [0] * N_CELLS
    base[COMPILER_CELLS:] = SENTINEL
    executed = 0
    lines = []
    for q, r, h, k in itertools.product(range(5), repeat=4):
        m = list(base)
        m[LOW] = q
        m[RECEIVER_R] = r
        m[HIGH] = h
        m[ARCHIVE] = k
        start = list(m)
        for pass_no in (1, 2):
            n = run_word(shear, m)
            require(m[2:50] == ZERO_WORK, 'R10 clean work cells at forward-word entry')
            n += run_word(fwd, m)
            require(m[2:50] == ZERO_WORK, 'R10 clean work cells at forward-word exit')
            n += run_word(gadget, m)
            require(m[2:50] == ZERO_WORK, 'R10 clean work cells at inverse-word entry')
            n += run_word(inv, m)
            require(m[2:50] == ZERO_WORK, 'R10 clean work cells at inverse-word exit')
            n += run_word(inverse_shear, m)
            require(n == OCCUPIED_PER_PASS, 'R10 primitives per occupied pass')
            executed += n
            if pass_no == 1:
                got = (m[LOW], m[RECEIVER_R], m[HIGH], m[ARCHIVE])
                require(got == L[(q, r, h, k)], 'R10 the compiled occupied circuit equals closed L')
                require(m[51:55] == start[51:55] and m[56:62] == start[56:62],
                        'R10 cells outside the four registers and workspace unchanged')
                lines.append(memory_line('occupied %d %d %d %d' % (q, r, h, k), m))
        require(m == start, 'R10 a second pass restores the complete state')
    require(executed == 625 * 2 * OCCUPIED_PER_PASS, 'R10 primitive count')
    return sha256_text('\n'.join(lines) + '\n'), executed


# ---------------------------------------------------------------------- R11

def check_r11(fwd, inv, routing, L):
    shear = routing['shear']
    feed = routing['feed']
    gadget = routing['gadget']
    inverse_shear = routing['inverse_shear']
    layout_cells = ([LOW, HIGH] + list(WORK) + [ARCHIVE]
                    + [c for c in PRIMARY if c != LOW] + list(SECONDARY))
    require(sorted(layout_cells) == list(range(N_CELLS)), 'R11 the 62-cell layout is a partition')
    require(PRIMARY[4] == LOW, 'R11 primary q is compiler low cell 0')
    piston_cells = PRIMARY[:4]
    non_piston = [c for c in range(N_CELLS) if c not in piston_cells]
    require(len(non_piston) == 58, 'R11 58 non-piston cells')
    common = [0] * N_CELLS
    common[RECEIVER_R] = 1
    for c, v in zip(SECONDARY, (4, 0, 0, 0, 0, 1), strict=True):
        common[c] = v
    common_nonzero = {str(c): common[c] for c in non_piston if common[c] != 0}

    executed = 0
    ticks = 0
    lines = []
    classes = {}
    class_sheets = {}
    controls = {}
    controls_restored = 0
    for pist in itertools.product(range(5), repeat=4):
        m = list(common)
        for c, v in zip(piston_cells, pist, strict=True):
            m[c] = v
        require([m[c] for c in non_piston] == [common[c] for c in non_piston],
                'R11 one common preparation of the 58 non-piston cells')
        s = (sum(pist) + 1) % 5
        require(tuple(m[c] for c in PRIMARY) == pist + (0, 1),
                'R11 primary ready state (A,B,C,D,0,1)')
        counters = {'primary': 0, 'secondary': 0}
        n = 0
        post = origin_tick(m, PRIMARY, counters, 'primary')
        n += run_word(shear, m)
        entry = (m[LOW], m[HIGH], m[ARCHIVE])
        mark = m[LOW]
        require(m[2:50] == ZERO_WORK, 'R11 work cells zero at forward-word entry')
        n += run_word(fwd, m)
        require(m[2:50] == ZERO_WORK, 'R11 work cells zero at forward-word exit')
        forward_out = (m[LOW], m[HIGH])
        n += run_word(feed, m)
        secondary_pre = tuple(m[c] for c in SECONDARY)
        secondary_post = origin_tick(m, SECONDARY, counters, 'secondary')
        n += run_word(gadget, m)
        after_swap = (m[LOW], m[HIGH], m[ARCHIVE])
        require(m[2:50] == ZERO_WORK, 'R11 work cells zero at inverse-word entry')
        n += run_word(inv, m)
        require(m[2:50] == ZERO_WORK, 'R11 work cells zero at inverse-word exit')
        inverse_out = (m[LOW], m[HIGH])
        n += run_word(inverse_shear, m)
        require(n == INTEGRATED_PER_INPUT, 'R11 80705 primitives per piston tuple')
        require(counters == {'primary': 1, 'secondary': 1}, 'R11 two native origin ticks')
        executed += n
        ticks += counters['primary'] + counters['secondary']

        final_primary = tuple(m[c] for c in PRIMARY)
        final_regs = (m[LOW], m[RECEIVER_R], m[HIGH], m[ARCHIVE])
        predicted = L[(post[4], post[5], 0, 0)]
        require(entry == ((post[4] + post[5] + 2) % 5, 0, 0),
                'R11 loaded mark q+r+2 with blank high and archive')
        require(final_regs == predicted, 'R11 four-register endpoint equals the closed L')
        require(final_primary == post, 'R11 the primary post-tick checkpoint is restored')
        expected = [0] * N_CELLS
        for c, v in zip(PRIMARY, post, strict=True):
            expected[c] = v
        expected[HIGH] = predicted[2]
        expected[ARCHIVE] = predicted[3]
        for c, v in zip(SECONDARY, secondary_post, strict=True):
            expected[c] = v
        require(m == expected, 'R11 complete 62-cell endpoint')
        lines.append(memory_line('integrated %d %d %d %d' % pist, m))
        key = ((post[4], post[5]), mark, forward_out, secondary_pre, secondary_post,
               after_swap, inverse_out, final_regs)
        if s != 0:
            require(mark == s, 'R11 the marked digit is s')
            require(forward_out == ((2 * s) % 5, (3 * s) % 5), 'R11 forward output (2s,3s)')
            require(after_swap == ((2 * s) % 5, 0, (3 * s) % 5),
                    'R11 after the swap: low a, high 0, archive v')
            require(inverse_out == (s, s), 'R11 inverse output (s,s)')
            require(m[ARCHIVE] == (3 * s) % 5, 'R11 the archive holds 3s')
            require(m[HIGH] == s, 'R11 the high cell holds s')
            reference_pre = ((4 + 2 * s) % 5, 0, 0, 0, 0, 1)
            require(secondary_pre == reference_pre,
                    'R11 secondary prepared state (4+2s,0,0,0,0,1)')
            require(secondary_post == native_U(0, reference_pre)[1],
                    'R11 secondary checkpoint equals U at the origin of (4+2s,0,0,0,0,1)')
            native_sign = q_reader(post[4])
            forward_sign = carry_sign(m[ARCHIVE])
            paired_sign = carry_sign(m[HIGH])
            secondary_sign = q_reader(secondary_post[4])
            require(native_sign == chi(s), 'R11 primary native reader gives chi(s)')
            require(forward_sign == chi(s), 'R11 forward carry sign chi(s)')
            require(paired_sign == -chi(s), 'R11 paired inverse carry sign -chi(s)')
            require(secondary_sign == paired_sign and secondary_sign == -native_sign,
                    'R11 the secondary receiver gives the opposite sign')
            classes[key] = classes.get(key, 0) + 1
            class_sheets.setdefault(key, set()).add(s)
        else:
            predicted_mark = (post[4] + post[5] + 2) % 5
            require((predicted_mark, predicted[2], predicted[3]) == (3, 3, 4),
                    'R11 closed L predicts mark 3, high 3, archive 4 for s=0')
            require(mark == 3 and m[HIGH] == 3 and m[ARCHIVE] == 4,
                    'R11 s=0 control: mark 3, high 3, archive 4')
            require(final_primary == post, 'R11 s=0 control: checkpoint restored')
            controls_restored += 1
            controls[key] = controls.get(key, 0) + 1
    require(executed == 625 * INTEGRATED_PER_INPUT, 'R11 primitive count')
    require(ticks == 2 * 625, 'R11 native tick count')
    require(len(classes) == 4 and sorted(classes.values()) == [125, 125, 125, 125],
            'R11 four boundary classes of 125')
    require(all(len(sheets) == 1 for sheets in class_sheets.values()),
            'R11 each boundary class lies on one sheet')
    require(sorted(next(iter(sheets)) for sheets in class_sheets.values()) == [1, 2, 3, 4],
            'R11 the boundary classes are the four admitted sheets')
    require(len(controls) == 1 and list(controls.values()) == [125] and controls_restored == 125,
            'R11 the 125 s=0 controls form one restored class')

    def describe(key, multiplicity):
        receiver, mark, forward_out, sec_pre, sec_post, after_swap, inverse_out, final = key
        return {'after_swap_low_high_archive': list(after_swap),
                'final_q_r_high_archive': list(final),
                'forward_output': list(forward_out),
                'inverse_output': list(inverse_out),
                'mark': mark,
                'multiplicity': multiplicity,
                'receiver': list(receiver),
                'secondary_checkpoint': list(sec_post),
                'secondary_prepared': list(sec_pre)}

    boundary = []
    for key in sorted(classes, key=lambda item: next(iter(class_sheets[item]))):
        record = describe(key, classes[key])
        s = next(iter(class_sheets[key]))
        record['s'] = s
        record['signs'] = {'forward_carry': carry_sign(key[7][3]),
                           'native': q_reader(key[0][0]),
                           'paired_carry': carry_sign(key[7][2]),
                           'secondary': q_reader(key[4][4])}
        boundary.append(record)
    control_key = next(iter(controls))
    control_summary = describe(control_key, controls[control_key])
    control_summary['archive'] = control_key[7][3]
    control_summary['checkpoint_restored'] = controls_restored
    control_summary['high'] = control_key[7][2]
    control_summary['s'] = 0
    info = {'boundary_classes': boundary, 'common_preparation_nonzero': common_nonzero,
            'integrated_endpoints_sha256': sha256_text('\n'.join(lines) + '\n')}
    return info, control_summary, executed, ticks


# --------------------------------------------------------------------- main

def main():
    require(sys.flags.optimize == 0, 'refuse to run under -O: assertions must stay enabled')
    require(sys.version_info >= (3, 12), 'Python 3.12 or newer')
    sys.dont_write_bytecode = True
    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument('--compiler', default=DEFAULT_COMPILER)
    args = parser.parse_args()
    compiler, compiler_info = load_compiler(args.compiler)

    states = list(itertools.product(range(5), repeat=6))
    require(len(states) == 15625, 'all 5^6 native states')

    ready, rows, d1, generator_comparisons = check_r1(states)
    d2, affine_maps = check_r2(ready, rows)
    d3, closure_states, trace_words, state_words = check_r3(states)
    J, JINV, F, I, d4, class_pairs = check_r4()
    L, d5 = check_r5(F, I)
    d6, stress_J, stress_JINV = check_r6(J, JINV)
    d7 = check_r7(ready)
    d8, ticks_r8 = check_r8()
    fwd, inv, d9, prims_r9 = check_r9(compiler, F, I)
    routing = build_routing()
    exchanges, prims_gadget = check_gadget(routing['gadget'])
    occupied_digest, prims_r10 = check_r10(fwd, inv, routing, L)
    d11, controls_s0, prims_r11, ticks_r11 = check_r11(fwd, inv, routing, L)

    counts = {
        'admitted': 500,
        'affine_maps': affine_maps,
        'class_pairs': class_pairs,
        'clock_words_state_level': state_words,
        'clock_words_trace_level': trace_words,
        'controls': 125,
        'gadget_exchanges': exchanges,
        'generator_comparisons': generator_comparisons,
        'native_states': len(states),
        'native_ticks_R11': ticks_r11,
        'native_ticks_R8': ticks_r8,
        'occupied_states': len(L),
        'primitives_R10': prims_r10,
        'primitives_R11': prims_r11,
        'primitives_R9': prims_r9,
        'primitives_gadget_test': prims_gadget,
        'primitives_per_integrated_input': INTEGRATED_PER_INPUT,
        'primitives_per_occupied_pass': OCCUPIED_PER_PASS,
        'primitives_total': prims_r9 + prims_gadget + prims_r10 + prims_r11,
        'ready_states': len(ready),
        'routing_primitives_per_integrated_input': ROUTING_PER_INPUT,
        'stress_cases_J': stress_J,
        'stress_cases_J_inverse': stress_JINV,
        'trace_closure_evaluations': closure_states,
        'word_inventory': d9['inventory'],
        'word_length': d9['length'],
    }
    require(INTEGRATED_PER_INPUT == 80705, 'PREREG: 80705 primitives per integrated input')
    require(OCCUPIED_PER_PASS == 80704, 'occupied pass: 2 x 40348 plus 8 routing primitives')
    require(prims_r9 == 2017400, 'R9 total 25 x 2 x 40348')
    require(prims_r10 == 100880000, 'R10 total 625 x 2 x 80704')
    require(prims_r11 == 50440625, 'R11 total 625 x 80705')
    require(ticks_r11 == 1250 and ticks_r8 == 4, 'native tick totals')

    out = {
        'candidate': {'id': 'C-NATIVE-RECEIVER-CARRY-MIRROR-REVIEW-N', 'pr': 1884,
                      'probe': 'P-NATIVE-RECEIVER-CARRY-MIRROR-1',
                      'scientific_source_pin': 'aaf3ec7e925c2c0261604179ee4166d542233e14'},
        'checks': ['R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'R8', 'R9', 'R10', 'R11'],
        'compiler': compiler_info,
        'controls_s0': controls_s0,
        'counts': counts,
        'derived': {
            'R1_native_rows': d1,
            'R2_port': d2,
            'R3_trace': d3,
            'R4_ring': d4,
            'R5_circuit': d5,
            'R6_carries': d6,
            'R7_omitted_offset': d7,
            'R8_second_device': d8,
            'R11_integrated': {'boundary_classes': d11['boundary_classes'],
                               'common_preparation_nonzero': d11['common_preparation_nonzero']},
        },
        'digests': {
            'component_endpoints_sha256': d9['component_endpoints_sha256'],
            'forward_word_sha256': d9['forward_word_sha256'],
            'integrated_endpoints_sha256': d11['integrated_endpoints_sha256'],
            'inverse_word_sha256': d9['inverse_word_sha256'],
            'occupied_endpoints_sha256': occupied_digest,
        },
        'status': 'PASS',
    }
    sys.stdout.write(json.dumps(out, sort_keys=True, separators=(',', ':')) + '\n')


if __name__ == '__main__':
    main()
