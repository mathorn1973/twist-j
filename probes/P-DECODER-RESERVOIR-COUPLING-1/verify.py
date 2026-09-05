#!/usr/bin/env python3
"""Exact pinned conformance audit for the chosen reservoir adapter."""
import ast
from dataclasses import FrozenInstanceError
from fractions import Fraction as F
import hashlib
from pathlib import Path

import coupling as c
import audit_coupling


EXPECTED_DEPENDENCIES = {'coupling.py': '54f8b03762639e2573f02210b07e0d19b28935c2bc68c7f5988b15efbe26d403', 'audit_coupling.py': '28cf0f018ecdc756f58f70e8dfb63f72c033750c62c59feba98df56f283a1385', 'PROOF.md': 'b4608f99bff54cb89ce9c5292f79f8738d8df8245a6a9e275afb48295f7731d0', 'CONTRACT.md': '935ccb861096328ae523145b55135541029dba4d000c14f2aa51acddd5ca36c8'}


def check_prefix():
    w = c.wave
    context = c.Context(w.field({(0, 0, 0): 2, (1, 1, 0): F(1, 2)}), F(1, 100))
    for source in ((0, 0, 0, 0), (1, 0, 0, 0), (F(1, 2), -2, 1, F(-1, 3))):
        long = c.prefix(source, context, 3)
        assert long.initial == w.prepare(source)
        assert c.prefix(source, context, 0).state == c.ready(long.initial)
        for length in range(4):
            short = c.prefix(source, context, length)
            assert short.batches == long.batches[:length]
            assert c.extend(short, 3 - length) == long
        heat_total = sum((v for _, v in long.state.heat), F(0))
        initial_energy = w.energy(long.initial)
        assert w.energy(long.state.pair) + heat_total == initial_energy
        assert 2 * initial_energy == w.qdd_mass(source)
        counts = dict(c.threshold_counts(long.state.heat, context))
        residual = sum((v for _, v in c.remainders(long.state.heat, context)), F(0))
        assert context.quantum * sum(counts.values()) + residual == heat_total
        assert sum(counts.values()) <= initial_energy // context.quantum
        emitted = {x: [] for x, _ in context.gamma}
        for batch in long.batches:
            for crossing in batch.crossings:
                emitted[crossing.site].extend(range(crossing.first, crossing.last + 1))
        for x, count in counts.items():
            assert emitted[x] == list(range(1, count + 1))
        # The complete signed reservoir tape reverses the generated wave history.
        pair = long.state.pair
        for batch in reversed(long.batches):
            pair, incoming = c.reverse(pair, context, batch.outgoing)
            assert incoming == ()
        assert pair == long.initial
        try:
            long.batches = ()
        except FrozenInstanceError:
            pass
        else:
            raise AssertionError("mutable history")


def check_types():
    w = c.wave
    origin, other = (0, 0, 0), (1, 1, 0)
    context = c.Context(w.field({origin: 2}), F(1))
    pair = w.Pair(w.field({origin: 1}), ())
    history = c.history_from_pair(pair, context, 1)
    bad = [lambda: c.Context(w.field({origin: -1}), F(1)),
           lambda: c.Context(w.field({origin: 2}), 0),
           lambda: c.Context((), True), lambda: c.Context((), 0.5),
           lambda: c.couple(pair, context, w.field({other: 1})),
           lambda: c.reverse(pair, context, w.field({other: 1})),
           lambda: c.State(pair, w.field({origin: -1}), 0),
           lambda: c.State(pair, (), True),
           lambda: c.advance(c.State(pair, w.field({other: 1}), 0), context),
           lambda: c.Crossing(origin, 0, 1), lambda: c.Crossing(origin, 2, 1),
           lambda: c.Crossing(origin, True, 1),
           lambda: c.extend(history, -1), lambda: c.extend(history, True),
           lambda: c.threshold_counts(w.field({origin: -1}), context),
           lambda: c.History(context, pair, history.state, ()),
           lambda: c.History(context, pair, c.State(history.state.pair, (), 1), history.batches),
           lambda: c.History(context, pair, c.State(history.state.pair, history.state.heat, 2), history.batches * 2)]
    for function in bad:
        try:
            function()
        except (ValueError, TypeError):
            pass
        else:
            raise AssertionError("ill-typed or inconsistent input accepted")


def check_locality_choices():
    w = c.wave
    origin, near, far = (0, 0, 0), (1, 1, 0), (40, 0, 0)
    context = c.Context(w.field({origin: 2, near: F(1, 2)}), F(1))
    pair = w.Pair(w.field({origin: F(1, 3)}), w.field({near: F(2, 5)}))
    initial = c.couple(pair, context)
    altered = w.Pair(w.add(pair.previous, w.field({far: 7})),
                     w.add(pair.current, w.field({far: 11})))
    remote = c.couple(altered, context)
    assert far not in w.halo(dict(context.gamma))
    assert initial.outgoing == remote.outgoing
    assert initial.transfer == remote.transfer and initial.forcing == remote.forcing
    for x, _ in context.gamma:
        assert dict(initial.after.current).get(x, F(0)) == dict(remote.after.current).get(x, F(0))
    factor = F(-3, 2)
    scaled = c.couple(w.Pair(w.scale(pair.previous, factor), w.scale(pair.current, factor)), context)
    assert scaled.after == w.Pair(w.scale(initial.after.previous, factor), w.scale(initial.after.current, factor))
    assert scaled.outgoing == w.scale(initial.outgoing, factor)
    assert scaled.transfer == w.scale(initial.transfer, factor ** 2)
    # Threshold changes the record, never the fixed wave/reservoir coupling.
    small = c.Context(context.gamma, F(1, 1000))
    large = c.Context(context.gamma, F(1000))
    s1, b1 = c.advance(c.ready(pair), small)
    s2, b2 = c.advance(c.ready(pair), large)
    assert s1 == s2 and b1.outgoing == b2.outgoing and b1.deposit == b2.deposit
    assert b1.crossings != b2.crossings
    # Per-site counters are additive on a fixed ledger; re-pooling heat is not.
    heat = w.field({origin: F(3, 5), near: F(3, 5)})
    assert sum(dict(c.threshold_counts(heat, context)).values()) == 0
    assert sum(dict(heat).values()) // context.quantum == 1
    a, b = {origin}, {origin, near}
    counts = dict(c.threshold_counts(w.scale(heat, 3), context))
    count = lambda region: sum(counts.get(x, 0) for x in region)
    assert count(a) + count(b) == count(a | b) + count(a & b)
    # The wave map has no heat, count, threshold, history or U input dependency.
    tree = ast.parse(Path(c.__file__).read_text(encoding="utf-8"))
    functions = {node.name: node for node in tree.body if isinstance(node, ast.FunctionDef)}
    assert tuple(a.arg for a in functions['couple'].args.args) == ('pair', 'context', 'incoming')
    attrs = {node.attr for node in ast.walk(functions['couple']) if isinstance(node, ast.Attribute)}
    assert not attrs & {'heat', 'quantum', 'batches', 'crossings', 'tick'}


def gate(name, function):
    try:
        function()
    except AssertionError:
        return name, False
    return name, True


def main():
    if not __debug__:
        raise RuntimeError("assertion audit requires non-optimized Python")
    if set(EXPECTED_DEPENDENCIES) != {'coupling.py', 'audit_coupling.py', 'PROOF.md', 'CONTRACT.md'}:
        raise RuntimeError("dependency hash table incomplete")
    for name, expected in EXPECTED_DEPENDENCIES.items():
        if hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest() != expected:
            raise RuntimeError("immutable dependency mismatch: " + name)
    gates = audit_coupling.run_checks()
    gates.extend((gate('G05_PREFIX_TAPE', check_prefix), gate('G06_TYPES', check_types),
                  gate('G07_LOCALITY_CHOICES', check_locality_choices)))
    print('PROBE P-DECODER-RESERVOIR-COUPLING-1')
    print('MODE CHOICE-EXPLICIT PROOF-FIRST L1')
    for name, passed in gates:
        print('CHECK', name, 'PASS' if passed else 'FIRED')
    passed = all(value for _, value in gates)
    print('CLAIM DECODER-RESERVOIR-RECORD-ACCOUNTING', 'CONFIRMED' if passed else 'FIRED')
    print('PHYSICAL_APPARATUS_OCCURRENCE UNRESOLVED')
    print('BORN_FREQUENCY UNTESTED STOP')
    print('PUBLIC_CLAIMS UNREGISTERED CANON_UNCHANGED')
    print('TERMINAL', 'CONFIRMED' if passed else 'SCIENTIFIC-FIRED')


if __name__ == '__main__':
    main()
