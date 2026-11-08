#!/usr/bin/env python3
"""Exact affine classification of the fixed contact word over integer inputs.

A node represents t = r + 2^k n, n in Z, and six slots A+nD.
Only n parity can affect a contact admission. Every split keeps both children.
"""

from dataclasses import dataclass
from fractions import Fraction
from hashlib import sha256
import importlib.util
import json
from pathlib import Path


WORD_SHA256 = "6fed5cf015526726db5e47b060e583db00af77db21b54c5dbe47b79de78b65a7"
CHECKER_SHA256 = "553404d4cd8facd1dee7f842bae8d454504e20a64f6143f8b6c2c60351174d72"
WORD_BYTES = 966
CONTACTS = 322
MAX_STEPS = 1 << 20
MAX_LEAVES = 1 << 16
MAX_SOLUTIONS = 4096
ZERO = (0, 0, 0, 0)
ZERO_STATE = (ZERO,) * 6
LABELS = {str(i + 1) + str(k + 1): (i, k)
          for i in range(6) for k in range(i + 1, 6)}


def encoded(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode("ascii")


def emit(kind, **fields):
    print(encoded(dict(kind=kind, **fields)).decode("ascii"))


def preparation(r, stride):
    a = ((r, 0, -r, 0), (-r, 0, r, 0), (1, -1, 0, 0),
         (1, -1, 0, 0), (1, 1, 0, -2), (2, 0, 0, 0))
    d = ((stride, 0, -stride, 0), (-stride, 0, stride, 0),
         ZERO, ZERO, ZERO, ZERO)
    return a, d


def target(r, stride):
    a = ((1 + r, -1, -r, 0), (1 - r, -1, r, 0),
         ZERO, ZERO, (1, 1, 0, -2), (2, 0, 0, 0))
    return a, preparation(r, stride)[1]


def admissions(a, d, edge):
    i, k = edge
    x = tuple(a[i][q] - a[k][q] for q in range(4))
    y = tuple(d[i][q] - d[k][q] for q in range(4))
    return (all(v % 2 == 0 for v in x),
            all((x[q] + y[q]) % 2 == 0 for q in range(4)))


def refine(a, d, epsilon):
    return (tuple(tuple(x + epsilon * y for x, y in zip(v, w)) for v, w in zip(a, d)),
            tuple(tuple(2 * x for x in v) for v in d))


def pair_step(x, y):
    delta = tuple(x[q] - y[q] for q in range(4))
    if any(v % 2 for v in delta):
        raise ArithmeticError("nonintegral admitted power coefficient")
    a, b, c, d = (v // 2 for v in delta)
    p = (d - c, -c, a - c, b - c)  # multiplication by j^2
    s = tuple((x[q] + y[q]) // 2 for q in range(4))
    return (tuple(s[q] + p[q] for q in range(4)),
            tuple(s[q] - p[q] for q in range(4)))


def step(a, d, edge, admitted):
    if admissions(a, d, edge) != (admitted, admitted):
        raise ArithmeticError("nonuniform power branch")
    if not admitted:
        return a, d
    i, k = edge
    out_a, out_d = list(a), list(d)
    out_a[i], out_a[k] = pair_step(a[i], a[k])
    out_d[i], out_d[k] = pair_step(d[i], d[k])
    return tuple(out_a), tuple(out_d)


def polynomial_invariants(a, d):
    sums = (tuple(sum(v[q] for v in a) for q in range(4)),
            tuple(sum(v[q] for v in d) for q in range(4)))
    q0 = q1 = q2 = 0
    for x, y in zip(a, d):
        sx, sy = sum(x), sum(y)
        q0 += (5 * sum(v * v for v in x) - sx * sx) // 2
        q1 += 5 * sum(v * w for v, w in zip(x, y)) - sx * sy
        q2 += (5 * sum(v * v for v in y) - sy * sy) // 2
    return sums, (q0, q1, q2), tuple((sum(x) % 5, sum(y) % 5) for x, y in zip(a, d))


def expected_invariants(r, stride):
    return (((5, -1, 0, -2), ZERO),
            (10 * r * r + 33, 20 * r * stride, 10 * stride * stride),
            ((0, 0),) * 5 + ((2, 0),))


def affine_errors(a, d, r, stride):
    goal_a, goal_d = target(r, stride)
    return (tuple(tuple(x - y for x, y in zip(v, w)) for v, w in zip(a, goal_a)),
            tuple(tuple(x - y for x, y in zip(v, w)) for v, w in zip(d, goal_d)))


def classify(a, d, r, k):
    e, f = affine_errors(a, d, r, 1 << k)
    equations = [(x, y) for v, w in zip(e, f) for x, y in zip(v, w)]
    if any(x and not y for x, y in equations):
        return dict(kind="empty", t=None, reason="constant_conflict"), e, f
    varying = [(x, y) for x, y in equations if y]
    if not varying:
        return dict(kind="full", t=None, reason="identically_zero"), e, f
    numerator, denominator = -varying[0][0], varying[0][1]
    if denominator < 0:
        numerator, denominator = -numerator, -denominator
    if any(x * denominator + y * numerator for x, y in equations):
        return dict(kind="empty", t=None, reason="inconsistent_roots"), e, f
    if numerator % denominator:
        return dict(kind="empty", t=None, reason="nonintegral_root"), e, f
    root = numerator // denominator
    return dict(kind="singleton", t=r + (1 << k) * root,
                n=root, reason="one_integer_root"), e, f


class ScientificFailure(Exception):
    pass


class Audit:
    def __init__(self, checker):
        self.checker = checker
        self.checks = 0

    def require(self, condition, name, context=None):
        self.checks += 1
        if not condition:
            raise ScientificFailure(encoded(dict(check=name, context=context)).decode("ascii"))

    def states(self, a, d, u, v, context):
        self.require(a == self.checker.to_power(u), "constant_representation", context)
        self.require(d == self.checker.to_power(v), "slope_representation", context)

    def invariants(self, a, d, u, v, r, stride, context):
        expected = expected_invariants(r, stride)
        self.require(polynomial_invariants(a, d) == expected, "power_invariant_polynomials", context)
        self.require(self.checker.polynomial_invariants(u, v) == expected,
                     "u_invariant_polynomials", context)

    def classification(self, a, d, u, v, r, k, context):
        result, e, f = classify(a, d, r, k)
        independent = self.checker.classify(u, v, r, k)
        self.require((result["kind"], result["t"]) == independent,
                     "independent_classification", context)
        return result, e, f


@dataclass
class Node:
    pos: int
    r: int
    k: int
    a: tuple
    d: tuple
    u: tuple
    v: tuple
    trace: bytes


def branch_flags(audit, node, edge, phase):
    flags = admissions(node.a, node.d, edge)
    audit.require(flags == audit.checker.admissions(node.u, node.v, edge),
                  "independent_admission", (phase, node.r, node.k, node.pos))
    return flags


def child(audit, node, epsilon, canonical):
    a, d = refine(node.a, node.d, epsilon)
    u, v = audit.checker.refine(node.u, node.v, epsilon)
    r = node.r + epsilon * (1 << node.k)
    k = node.k + 1
    audit.require(k <= CONTACTS, "dyadic_depth_bound", (r, k, node.pos))
    if canonical:
        audit.require(0 <= r < (1 << k), "canonical_cylinder", (r, k))
    audit.states(a, d, u, v, ("refine", r, k, node.pos))
    return Node(node.pos, r, k, a, d, u, v, node.trace)


def advance(audit, node, edge, admitted):
    a, d = step(node.a, node.d, edge, admitted)
    u, v = audit.checker.step(node.u, node.v, edge, admitted)
    audit.states(a, d, u, v, ("step", node.r, node.k, node.pos))
    return Node(node.pos + 1, node.r, node.k, a, d, u, v,
                node.trace + (b"A" if admitted else b"R"))


def initial_node(audit, r):
    a, d = preparation(r, 1)
    u, v = audit.checker.preparation(r, 1)
    audit.states(a, d, u, v, ("initial", r))
    audit.invariants(a, d, u, v, r, 1, ("initial", r))
    return Node(0, r, 0, a, d, u, v, b"")


def anchored_branches(audit, word):
    branches = []
    for t0 in (-2, -1, 0, 1, 2):
        node = initial_node(audit, t0)
        splits = []
        for pos, edge in enumerate(word):
            flags = branch_flags(audit, node, edge, "anchor")
            if flags[0] != flags[1]:
                splits.append(pos + 1)
                node = child(audit, node, 0, False)
                flags = branch_flags(audit, node, edge, "anchor_refined")
                audit.require(flags[0] == flags[1], "one_split_resolves_contact", (t0, pos))
            node = advance(audit, node, edge, flags[0])
        stride = 1 << node.k
        audit.invariants(node.a, node.d, node.u, node.v, t0, stride, ("anchor_terminal", t0))
        result, e, f = audit.classification(node.a, node.d, node.u, node.v, t0, node.k,
                                          ("anchor_terminal", t0))
        audit.require(node.a == target(t0, stride)[0], "prior_five_input_replay", t0)
        emit("ANCHORED", t0=t0, r=t0 % stride, k=node.k,
             coordinate="t=t0+2^k*n", endpoint_A=node.a, endpoint_D=node.d,
             error_A=e, error_D=f, classification=result, split_contacts=splits,
             admission_sha256=sha256(node.trace).hexdigest())
        branches.append(node)
    return branches


def reverse_bits(r, k):
    value = 0
    for _ in range(k):
        value = 2 * value + (r & 1)
        r >>= 1
    return value


def coverage(audit, leaves, frontier):
    domains = [(r, k, CONTACTS, True) for r, k, _ in leaves]
    domains += [(n.r, n.k, n.pos, False) for n in frontier]
    max_k = max(k for _, k, _, _ in domains)
    denominator = 1 << max_k
    intervals = []
    for r, k, pos, terminal in domains:
        audit.require(0 <= r < (1 << k), "coverage_canonical_domain", (r, k, pos))
        width = 1 << (max_k - k)
        low = reverse_bits(r, k) * width
        intervals.append((low, low + width, terminal, r, k, pos))
    intervals.sort()
    cursor = covered = remaining = 0
    digest = sha256()
    for low, high, terminal, r, k, pos in intervals:
        audit.require(low == cursor and high > low, "partition_disjoint_adjacent", (r, k, pos))
        cursor = high
        if terminal:
            covered += high - low
        else:
            remaining += high - low
        digest.update(encoded((low, high, terminal, r, k, pos)) + b"\n")
    audit.require(cursor == denominator, "partition_full_cover")
    audit.require(covered + remaining == denominator, "partition_measure")
    kraft = sum((Fraction(1, 1 << k) for _, k, _, _ in domains), Fraction(0))
    audit.require(kraft == 1, "independent_kraft_sum")
    c, r = Fraction(covered, denominator), Fraction(remaining, denominator)
    return dict(max_k=max_k, intervals=len(intervals), partition_sha256=digest.hexdigest(),
                covered_domain_measure=[c.numerator, c.denominator],
                remaining_domain_measure=[r.numerator, r.denominator])


def full_tree(audit, word, anchors):
    stack = [initial_node(audit, 0)]
    leaves, solutions = [], []
    reasons = {}
    certificate = sha256()
    steps = splits = 0
    maximum_stack = 1
    stop = None
    while stack:
        node = stack.pop()
        if node.pos == CONTACTS:
            if len(leaves) >= MAX_LEAVES:
                stack.append(node)
                stop = "terminal_leaf_cap"
                break
            result, e, f = audit.classification(node.a, node.d, node.u, node.v,
                                              node.r, node.k, ("tree_terminal", node.r, node.k))
            if result["kind"] != "empty" and len(solutions) >= MAX_SOLUTIONS:
                stack.append(node)
                stop = "nonempty_record_cap"
                break
            audit.invariants(node.a, node.d, node.u, node.v, node.r, 1 << node.k,
                             ("tree_terminal", node.r, node.k))
            leaves.append((node.r, node.k, result))
            reasons[result["reason"]] = reasons.get(result["reason"], 0) + 1
            record = dict(r=node.r, k=node.k, A=node.a, D=node.d, error_A=e,
                          error_D=f, classification=result,
                          admission_sha256=sha256(node.trace).hexdigest())
            record_hash = sha256(encoded(record)).hexdigest()
            certificate.update(encoded(record) + b"\n")
            if result["kind"] != "empty":
                solution = dict(r=node.r, k=node.k, classification=result,
                                certificate_sha256=record_hash)
                solutions.append(solution)
                emit("SOLUTION", **solution)
            for anchor in anchors:
                if (anchor.r - node.r) % (1 << node.k) == 0:
                    n = (anchor.r - node.r) // (1 << node.k)
                    endpoint = tuple(tuple(x + n * y for x, y in zip(v, w))
                                     for v, w in zip(node.a, node.d))
                    audit.require(endpoint == anchor.a, "tree_anchor_endpoint", anchor.r)
                    audit.require(node.trace == anchor.trace, "tree_anchor_admission", anchor.r)
                    audit.require(result["kind"] == "full" or result["t"] == anchor.r,
                                  "tree_anchor_classification", anchor.r)
            continue
        if steps >= MAX_STEPS:
            stack.append(node)
            stop = "node_contact_cap"
            break
        steps += 1  # Includes a splitting parent and each child at the same position.
        flags = branch_flags(audit, node, word[node.pos], "tree")
        if flags[0] != flags[1]:
            splits += 1
            stack.append(child(audit, node, 1, True))
            stack.append(child(audit, node, 0, True))
        else:
            stack.append(advance(audit, node, word[node.pos], flags[0]))
        maximum_stack = max(maximum_stack, len(stack))
        audit.require(len(stack) <= CONTACTS + 1, "depth_first_stack_bound")
    for node in stack:
        audit.invariants(node.a, node.d, node.u, node.v, node.r, 1 << node.k,
                         ("tree_frontier", node.r, node.k, node.pos))
    cover = coverage(audit, leaves, stack)
    frontier = [dict(pos=n.pos, r=n.r, k=n.k) for n in reversed(stack)]
    emit("TREE", status="COMPLETE" if not stack else "PARTIAL", stop=stop,
         node_contact_steps=steps, splits=splits, terminal_leaves=len(leaves),
         nonempty_records=len(solutions), maximum_stack=maximum_stack,
         reason_counts=reasons, terminal_certificate_sha256=certificate.hexdigest(),
         frontier=frontier, **cover)
    return leaves, solutions, stack, stop


def scalar_replay(audit, word, t, initial=None, initial_u=None):
    a = preparation(t, 0)[0] if initial is None else initial
    u = audit.checker.preparation(t, 0)[0] if initial_u is None else initial_u
    zero_u = audit.checker.preparation(0, 0)[1]
    trace = bytearray()
    for pos, edge in enumerate(word):
        i, k = edge
        admitted = all((x - y) % 2 == 0 for x, y in zip(a[i], a[k]))
        audit.require(audit.checker.admissions(u, zero_u, edge) == (admitted, admitted),
                      "scalar_admission", (t, pos))
        if admitted:
            updated = list(a)
            updated[i], updated[k] = pair_step(a[i], a[k])
            a = tuple(updated)
        u, zero_u = audit.checker.step(u, zero_u, edge, admitted)
        audit.require(a == audit.checker.to_power(u), "scalar_representation", (t, pos))
        trace.append(ord("A") if admitted else ord("R"))
    audit.invariants(a, ZERO_STATE, u, zero_u, t, 0, ("scalar_terminal", t))
    return a, u, bytes(trace)


def scalar_audits(audit, word, anchors, leaves, solutions, frontier):
    cache = {}
    inverse = tuple(edge for edge in reversed(word) for _ in range(4))

    def forward(t):
        if t not in cache:
            cache[t] = scalar_replay(audit, word, t)
        return cache[t]

    for t in range(-5, 6):
        endpoint, u, trace = forward(t)
        hit = endpoint == target(t, 0)[0]
        if -2 <= t <= 2:
            audit.require(hit, "prior_five_scalar_target", t)
        back, _, _ = scalar_replay(audit, inverse, t, endpoint, u)
        audit.require(back == preparation(t, 0)[0], "complete_scalar_inverse", t)
        emit("POINT", t=t, endpoint=endpoint, target=hit, inverse=True,
             admitted=trace.count(b"A"), refused=trace.count(b"R"),
             admission_sha256=sha256(trace).hexdigest())
    for node in anchors:
        observations = []
        for n in (-1, 0, 1):
            t = node.r + (1 << node.k) * n
            endpoint, _, trace = forward(t)
            affine = tuple(tuple(x + n * y for x, y in zip(v, w))
                           for v, w in zip(node.a, node.d))
            audit.require(endpoint == affine, "anchored_neighbor_affine", (node.r, n))
            audit.require(trace == node.trace, "anchored_neighbor_admission", (node.r, n))
            observations.append(dict(n=n, t=t, target=endpoint == target(t, 0)[0]))
        emit("ANCHORED_POINTS", t0=node.r, observations=observations)
    for solution in solutions:
        result = solution["classification"]
        if result["kind"] == "singleton":
            t = result["t"]
            endpoint, _, _ = forward(t)
            audit.require(endpoint == target(t, 0)[0], "tree_singleton_scalar", t)
    # Prefix lookup costs at most 323 dictionary probes per scalar input.
    domains = {(r, k): result for r, k, result in leaves}
    domains.update({(n.r, n.k): None for n in frontier})
    depths = sorted({k for _, k in domains})
    for t, (endpoint, _, _) in cache.items():
        matching = [domains[(t % (1 << k), k)] for k in depths
                    if (t % (1 << k), k) in domains]
        audit.require(len(matching) == 1, "scalar_partition_membership", t)
        result = matching[0]
        if result is not None:
            classified = result["kind"] == "full" or result["t"] == t
            audit.require(classified == (endpoint == target(t, 0)[0]), "scalar_classification", t)
    return len(cache)


def load_sources():
    directory = Path(__file__).resolve().parent
    raw = (directory / "WORD.txt").read_bytes()
    if len(raw) != WORD_BYTES or sha256(raw).hexdigest() != WORD_SHA256:
        raise ValueError("WORD.txt custody mismatch")
    labels = raw.decode("ascii").split()
    if (len(labels) != CONTACTS or any(label not in LABELS for label in labels)
            or raw != (" ".join(labels) + "\n").encode("ascii")):
        raise ValueError("WORD.txt canonical encoding mismatch")
    checker_path = directory / "checker.py"
    if sha256(checker_path.read_bytes()).hexdigest() != CHECKER_SHA256:
        raise ValueError("checker.py custody mismatch")
    spec = importlib.util.spec_from_file_location("integer_domain_checker", checker_path)
    checker = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(checker)
    return tuple(LABELS[label] for label in labels), checker


def main():
    word, checker = load_sources()
    audit = Audit(checker)
    emit("SOURCE", word_sha256=WORD_SHA256, checker_sha256=CHECKER_SHA256,
         contacts=CONTACTS, max_node_contacts=MAX_STEPS, max_terminal_leaves=MAX_LEAVES,
         max_nonempty_records=MAX_SOLUTIONS, domain="all integer t")
    try:
        anchors = anchored_branches(audit, word)
        leaves, solutions, frontier, stop = full_tree(audit, word, anchors)
        points = scalar_audits(audit, word, anchors, leaves, solutions, frontier)
        emit("RESULT", status="COMPLETE" if not frontier else "PARTIAL", falsifiers=0,
             checks=audit.checks, scalar_inputs=points, scalar_inverse_inputs=11,
             complete_domain=not frontier, stop=stop,
             scope="NON-CANONICAL L1 exact integer success domain of one fixed 322-contact word")
    except (ScientificFailure, ArithmeticError) as error:
        # Integrity errors above are nonzero infrastructure failures. A completed
        # mathematical audit failure is retained as deterministic stdout. Unexpected
        # execution/resource defects remain nonzero failures without a scientific result.
        emit("RESULT", status="F", falsifiers=1, checks=audit.checks,
             error_type=type(error).__name__, detail=str(error))


if __name__ == "__main__":
    main()
