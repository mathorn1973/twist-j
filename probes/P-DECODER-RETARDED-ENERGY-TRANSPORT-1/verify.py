#!/usr/bin/env python3
"""Immutable exact audit. The uniform claim is proved in PROOF.md."""
import ast
import hashlib
from dataclasses import FrozenInstanceError, fields
from fractions import Fraction as F
from pathlib import Path

import transport as t
import audit_transport


EXPECTED_DEPENDENCIES = {'transport.py': '983d22690e061128d287f23ef4672fbd72954faa28f1a3fde9ce38b0d6660a60', 'audit_transport.py': '6d9740ac000f014d6cecb7963fc27d3d0ab4454d6eeed49470ffd075237514cb', 'PROOF.md': '8115805719a468bf2ecef2add97640d100b74660ecdbc6e5ee9acc046219143b', 'CONTRACT.md': '89909f2a6b83d751092d1d233b634db523e80e44264932a9bbbd28c05b02527c'}


def check_apertures():
    origin, adjacent, distant = (0, 0, 0), (1, 1, 0), (40, 0, 0)
    pair = t.Pair(t.field({origin: F(2, 3)}), t.field({adjacent: F(-3, 5)}))
    region = t.Aperture((origin, adjacent))
    changed = t.Pair(t.add(pair.previous, t.field({distant: 7})),
                     t.add(pair.current, t.field({distant: -11})))
    assert distant not in t.halo(region.sites)
    assert t.readout(pair, region) == t.readout(changed, region)
    full = t.readout(pair, region)
    first, second = (t.readout(pair, t.Aperture((x,))) for x in region.sites)
    assert full.total == first.total + second.total
    a, b = {origin, adjacent}, {adjacent, (2, 0, 0)}
    read = lambda s: t.readout(pair, t.Aperture(tuple(sorted(s)))).total
    assert read(a | b) + read(a & b) == read(a) + read(b)
    assert t.readout(pair, t.Aperture(())).total == 0
    assert t.readout(pair, t.Aperture((distant,))).kind == "ZERO_READING"
    assert t.energy(pair) > 0
    # The balance also ignores values outside its declared local footprint.
    forcing = t.field({origin: F(1, 7)})
    nxt = t.step(pair, forcing).current
    arbitrary_nxt = t.add(nxt, t.field({distant: 19}))
    arbitrary_force = t.add(forcing, t.field({distant: 23}))
    assert t.balance(pair, nxt, forcing, region) == t.balance(
        changed, arbitrary_nxt, arbitrary_force, region)


def check_prefix():
    aperture = t.Aperture(((0, 0, 0), (1, 1, 0), (2, 0, 0)))
    for v in ((0, 0, 0, 0), (1, 0, 0, 0), (F(1, 2), -2, 1, F(-1, 3))):
        history = t.prefix(v, aperture, 3)
        assert history.aperture == aperture
        for length in (0, 1, 2, 3):
            assert t.prefix(v, aperture, length).frames == history.frames[:length]
        pair = t.prepare(v)
        rebuilt = t.History(aperture, ())
        old = None
        for cut, frame in enumerate(history.frames):
            assert frame.cut == cut and frame.reading == t.readout(pair, aperture)
            if old is None:
                assert frame.balance_from_previous is None
            else:
                assert frame.balance_from_previous == t.balance(old, pair.current, (), aperture)
                assert frame.balance_from_previous.residual == frame.balance_from_previous.work == 0
            prior = rebuilt
            rebuilt = t.append_history(rebuilt, frame)
            assert prior.frames == rebuilt.frames[:-1]
            old, pair = pair, t.step(pair)
        assert rebuilt == history
        encoded = t.exact_json(history)
        assert encoded["type"] == "History"
        assert encoded["frames"][0]["reading"]["total"] == {
            "numerator": history.frames[0].reading.total.numerator,
            "denominator": history.frames[0].reading.total.denominator}
        try:
            history.frames = ()
        except FrozenInstanceError:
            pass
        else:
            raise AssertionError("mutable history")
    for cls in (t.Pair, t.Aperture, t.Reading, t.Balance, t.Frame, t.History):
        assert cls.__dataclass_params__.frozen
        assert fields(cls)


def check_types():
    bad = [lambda: t.field({(0, 0, 0): 0.5}),
           lambda: t.field({(0, 0, 0): True}),
           lambda: t.field({(1, 0, 0): 1}),
           lambda: t.field((((0, 0, 0), 1), ((0, 0, 0), 2))),
           lambda: t.Pair((), (((0, 0, 0), 1),)),
           lambda: t.Aperture(((1, 1, 0), (0, 0, 0))),
           lambda: t.Aperture(((0, 0, 0), (0, 0, 0))),
           lambda: t.Aperture(((True, 1, 0),)),
           lambda: t.source((1, 2, 3)), lambda: t.source((1, 2, 3, 0.5)),
           lambda: t.green((), -1), lambda: t.green((), True),
           lambda: t.prefix((0, 0, 0, 0), t.Aperture(()), True),
           lambda: t.prefix((0, 0, 0, 0), t.Aperture(()), -1)]
    history = t.prefix((1, 0, 0, 0), t.Aperture(((0, 0, 0),)), 2)
    bad.extend((lambda: t.append_history(history, history.frames[0]),
                lambda: t.History(history.aperture, (history.frames[1],)),
                lambda: t.History(t.Aperture(()), history.frames)))
    for call in bad:
        try:
            call()
        except (ValueError, TypeError):
            pass
        else:
            raise AssertionError("ill-typed or inconsistent input accepted")


def check_boundaries():
    origin, neighbor = (0, 0, 0), (1, 1, 0)
    pair = t.Pair((), t.field({origin: 1}))
    next_pair = t.step(pair)
    assert t.norm2(next_pair.current) != t.norm2(pair.current)
    assert t.energy(next_pair) == t.energy(pair)
    assert dict(pair.current).get(neighbor, F(0)) == 0
    assert t.density(pair, neighbor) > 0  # Bond energy has a declared one-hop halo.
    bad_next = t.add(next_pair.current, t.field({origin: 1}))
    assert t.balance(pair, bad_next, (), t.Aperture((origin,))).residual != 0
    tree = ast.parse(Path(t.__file__).read_text(encoding="utf-8"))
    functions = {node.name: node for node in tree.body if isinstance(node, ast.FunctionDef)}
    closure, queue = set(), ["readout", "balance"]
    while queue:
        name = queue.pop()
        if name in closure:
            continue
        closure.add(name)
        queue.extend(node.func.id for node in ast.walk(functions[name])
                     if isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
                     and node.func.id in functions)
    assert not closure & {"source", "prepare", "qdd_mass", "prefix", "green", "step"}
    imports = {node.module for node in ast.walk(tree) if isinstance(node, ast.ImportFrom)}
    imports |= {alias.name for node in ast.walk(tree) if isinstance(node, ast.Import)
                for alias in node.names}
    assert imports == {"dataclasses", "fractions", "itertools", "math", "argparse", "json"}


def gate(name, function):
    try:
        function()
    except AssertionError:
        return name, False
    return name, True


def main():
    if not __debug__:
        raise RuntimeError("assertion audit requires non-optimized Python")
    if set(EXPECTED_DEPENDENCIES) != {"transport.py", "audit_transport.py", "PROOF.md", "CONTRACT.md"}:
        raise RuntimeError("accepted dependency hash table incomplete")
    for name, expected in EXPECTED_DEPENDENCIES.items():
        if hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest() != expected:
            raise RuntimeError("immutable dependency mismatch: " + name)
    gates = audit_transport.run_checks()
    gates.extend((gate("G06_APERTURES", check_apertures), gate("G07_PREFIX", check_prefix),
                  gate("G08_TYPES", check_types), gate("G09_BOUNDARIES", check_boundaries)))
    print("PROBE P-DECODER-RETARDED-ENERGY-TRANSPORT-1")
    print("MODE CHOICE-EXPLICIT QDD-NORM-EXPOSED PROOF-FIRST L1")
    for name, passed in gates:
        print("CHECK", name, "PASS" if passed else "FIRED")
    passed = all(value for _, value in gates)
    print("CLAIM DECODER-RETARDED-LOCAL-ENERGY-TRANSPORT", "CONFIRMED" if passed else "FIRED")
    print("PHYSICAL_SOURCE_DETECTOR UNRESOLVED")
    print("BORN_FREQUENCY UNTESTED STOP")
    print("PUBLIC_CLAIMS UNREGISTERED CANON_UNCHANGED")
    print("TERMINAL", "CONFIRMED" if passed else "SCIENTIFIC-FIRED")


if __name__ == "__main__":
    main()
