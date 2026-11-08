#!/usr/bin/env python3
"""Fully expanded two-digit compiler audit on one addressed memory.

NON-CANONICAL / L1. The compiler and prior integration results are exposed.
Only its pinned schedule builder is used. This module interprets the six
discrete basis-register primitives directly and constructs their inverse
independently. No ADD/H macro, pulse lowering, native inverse, floating-point
arithmetic, network operation or scientific import-time execution is used.

run(native_zero_tick) returns a deterministic summary and prints nothing.
"""
from collections import Counter
from hashlib import sha256
import importlib.util
from itertools import product
import json
from pathlib import Path
import sys


COMPILER_SHA256 = "0e3668a7e664f572e6c6c34c49bf454e8d931e6dd05b8f2ebaf3c1b0cd761027"
COMPILER_COMMIT = "227ef4cd42834a67f175ff1141e52b19ef8a49c4"
COMPILER_BLOB = "dab2f3b49aa0e7e3beec9310aecc86e1c0a58bef"
COMPILER_BYTES = 13728
EXPECTED_INVENTORY = {
    "EQ": 30368, "MUL": 5840, "REFLECT": 1168,
    "SCALE": 2, "SHIFT": 112, "SUM": 2858,
}


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def compact(value):
    return json.dumps(value, separators=(",", ":"), sort_keys=True).encode("ascii")


def load_compiler():
    path = Path(__file__).with_name("arithmetic_compiler.py")
    payload = path.read_bytes()
    require(len(payload) == COMPILER_BYTES, "compiler byte count")
    require(sha256(payload).hexdigest() == COMPILER_SHA256, "compiler exact source hash")
    spec = importlib.util.spec_from_file_location("pinned_two_digit_compiler", path)
    require(spec is not None and spec.loader is not None, "compiler source loader")
    module = importlib.util.module_from_spec(spec)
    # -I ignores PYTHONDONTWRITEBYTECODE from the environment. Prevent import
    # caching explicitly; loading this source does not call its guarded main.
    previous = sys.dont_write_bytecode
    sys.dont_write_bytecode = True
    try:
        spec.loader.exec_module(module)
    finally:
        sys.dont_write_bytecode = previous
    return module


def freeze_gate(block, cells):
    """Validate a primitive, its exact fields and distinct control/target wires."""
    require(isinstance(block, dict), "primitive must be a dictionary")
    op = block.get("op")
    schemas = {
        "SUM": {"op", "x", "target", "k"},
        "EQ": {"op", "x", "value", "target", "k"},
        "MUL": {"op", "x", "y", "target", "sign"},
        "SHIFT": {"op", "target", "k"},
        "REFLECT": {"op", "target"},
        "SCALE": {"op", "target", "k"},
    }
    require(op in schemas and set(block) == schemas[op], "primitive alphabet and exact fields")
    target = block["target"]
    require(type(target) is int and 0 <= target < cells, "primitive target")
    controls = [block[name] for name in ("x", "y") if name in block]
    require(all(type(w) is int and 0 <= w < cells for w in controls), "primitive controls")
    require(len(set(controls + [target])) == len(controls) + 1, "distinct primitive wires")
    if op in ("SUM", "EQ", "SHIFT", "SCALE"):
        require(type(block["k"]) is int, "integer primitive coefficient")
        coefficient = block["k"] % 5
    if op == "SUM":
        return op, block["x"], target, coefficient
    if op == "EQ":
        value = block["value"]
        require(type(value) is int and 0 <= value < 5, "equality comparison digit")
        return op, block["x"], value, target, coefficient
    if op == "MUL":
        require(type(block["sign"]) is int and block["sign"] in (-1, 1), "product sign")
        return op, block["x"], block["y"], target, block["sign"] % 5
    if op == "SHIFT":
        return op, target, coefficient
    if op == "REFLECT":
        return op, target
    require(coefficient != 0, "invertible local scale")
    return op, target, coefficient


def freeze_word(blocks, cells):
    return tuple(freeze_gate(block, cells) for block in blocks)


def inverse_gate(gate):
    op = gate[0]
    if op == "REFLECT":
        return gate
    if op == "SCALE":
        return op, gate[1], pow(gate[2], -1, 5)
    require(op in ("SUM", "EQ", "MUL", "SHIFT"), "known primitive inverse")
    return gate[:-1] + ((-gate[-1]) % 5,)


def inverse_word(word):
    return tuple(inverse_gate(gate) for gate in reversed(word))


def execute(word, memory, counters):
    """Visit each supplied primitive; no macro or complete-state cache exists."""
    for gate in word:
        op = gate[0]
        if op == "SUM":
            _, source, target, coefficient = gate
            memory[target] = (memory[target] + coefficient * memory[source]) % 5
        elif op == "EQ":
            _, source, value, target, coefficient = gate
            memory[target] = (memory[target] + coefficient * (memory[source] == value)) % 5
        elif op == "MUL":
            _, x, y, target, coefficient = gate
            memory[target] = (memory[target] + coefficient * memory[x] * memory[y]) % 5
        elif op == "SHIFT":
            _, target, coefficient = gate
            memory[target] = (memory[target] + coefficient) % 5
        elif op == "REFLECT":
            memory[gate[1]] = 4 - memory[gate[1]]
        elif op == "SCALE":
            _, target, coefficient = gate
            memory[target] = coefficient * memory[target] % 5
        else:
            raise AssertionError("unrecognized primitive reached interpreter")
    counters["primitive_gates"] += len(word)


def clean(memory, work):
    require(all(memory[w] == 0 for w in work), "compiler work cells must return zero")


def native_tick(memory, wires, native_zero_tick, counters):
    current = tuple(memory[w] for w in wires)
    result = native_zero_tick(current)
    require(len(result) == 6 and all(type(v) is int and 0 <= v < 5 for v in result),
            "native tick must return six F5 coordinates")
    for wire, value in zip(wires, result):
        memory[wire] = value
    counters["native_ticks"] += 1


def secondary_expected(mark):
    """Closed native-origin rows for (mark-1,0,0,0,0,1), used only as an oracle."""
    rows = {
        1: (0, 0, 0, 0, 0, 4),
        2: (2, 2, 1, 0, 1, 4),
        3: (0, 1, 3, 4, 1, 0),
        4: (4, 1, 3, 4, 2, 0),
    }
    require(mark in rows, "nonzero secondary input mark")
    return rows[mark]


def run(native_zero_tick):
    """Audit the exposed compiler and new integrated finite register contract."""
    require(callable(native_zero_tick), "native-origin function")
    compiler = load_compiler()
    app = compiler.layout(2)
    require(app["N"] == 2 and app["cells"] == 50, "two-digit layout size")
    require(app["data"] == [0, 1] and app["buffer"] == [2, 3] and app["zero"] == 49,
            "exact data/buffer/zero wire layout")
    low, high, archive = 0, 1, 50
    work = tuple(range(2, 50))
    require(len(work) == 48, "complete compiler workspace count")
    original = list(compiler.expand_program(compiler.multiplier_blocks(2, app),
                                             app, level="primitive"))
    forward = freeze_word(original, 50)
    require(len(forward) == 40348, "exact expanded multiplier length")
    inventory = dict(sorted(Counter(g[0] for g in forward).items()))
    require(inventory == EXPECTED_INVENTORY, "exact primitive inventory")
    backward = inverse_word(forward)
    require(freeze_word(compiler.reversed_blocks(original), 50) == backward,
            "independent primitive inverse agrees with compiler declaration")
    require(inverse_word(backward) == forward, "double primitive reversal")
    # Every compiler edge was checked against 0..49. It cannot touch archive,
    # primary pistons/r, or secondary receiver. Only low aliases native q.
    swap = freeze_word([
        {"op": "SUM", "x": high, "target": archive, "k": 1},
        {"op": "SUM", "x": archive, "target": high, "k": -1},
        {"op": "SUM", "x": high, "target": archive, "k": 1},
        {"op": "SCALE", "target": high, "k": -1},
    ], 51)
    swap_inverse = inverse_word(swap)
    require(len(swap) == len(swap_inverse) == 4, "archive transfer primitive count")
    counters = {"primitive_gates": 0, "native_ticks": 0}
    component_digest = sha256()

    # Exhaust all 25 two-digit inputs in each direction, with a nonzero
    # unaddressed archive sentinel. Compare all 51 cells, not only the data.
    for b, c in product(range(5), repeat=2):
        for direction, word in (("forward", forward), ("inverse", backward)):
            memory = [0] * 51
            memory[low], memory[high], memory[archive] = b, c, 4
            execute(word, memory, counters)
            clean(memory, work)
            pair = ((2*b) % 5, (3*b+2*c) % 5) if direction == "forward" else (
                (3*b) % 5, (3*b+3*c) % 5)
            expected = [0] * 51
            expected[low], expected[high], expected[archive] = pair[0], pair[1], 4
            require(memory == expected, "complete two-digit multiplier result and isolation")
            component_digest.update(compact([direction, b, c, memory]))

    # The actual high wire is moved into the actual archive. Nothing is
    # overwritten with a formula before the inverse multiplier executes.
    mirror_rows = []
    for b in range(5):
        memory = [0] * 51
        memory[low] = b
        initial = memory.copy()
        execute(forward, memory, counters)
        clean(memory, work)
        emitted, forward_high = memory[low], memory[high]
        require((emitted, forward_high, memory[archive]) == (2*b % 5, 3*b % 5, 0),
                "blank-high forward checkpoint")
        execute(swap, memory, counters)
        clean(memory, work)
        require((memory[low], memory[high], memory[archive]) == (emitted, 0, forward_high),
                "actual high-to-archive transfer")
        execute(backward, memory, counters)
        clean(memory, work)
        expected = [0] * 51
        expected[low], expected[high], expected[archive] = b, b, 3*b % 5
        require(memory == expected, "complete marked mirror endpoint")
        mirror_rows.append([b, emitted, forward_high, memory[low], memory[high], memory[archive]])
        component_digest.update(compact(["mirror", b, memory]))
        execute(forward, memory, counters)
        clean(memory, work)
        execute(swap_inverse, memory, counters)
        clean(memory, work)
        execute(backward, memory, counters)
        clean(memory, work)
        require(memory == initial, "literal complete component undo")
    require(counters["primitive_gates"] == 2824400 and counters["native_ticks"] == 0,
            "complete component gate count")
    component_gates = counters["primitive_gates"]

    primary = (51, 52, 53, 54, low, 55)
    secondary = (56, 57, 58, 59, 60, 61)
    require(len(set(primary + secondary + (high, archive) + work)) == 62,
            "complete disjoint layout apart from declared low/native-q alias")
    require(set(primary + secondary + (high, archive) + work) == set(range(62)),
            "every apparatus cell is accounted for")
    require(primary[4] == low, "primary q is multiplier low from initialization")
    shear = freeze_word([
        {"op": "SUM", "x": primary[-1], "target": low, "k": 1},
        {"op": "SHIFT", "target": low, "k": 2},
    ], 62)
    unshear = inverse_word(shear)
    write_secondary = freeze_word([
        {"op": "SUM", "x": low, "target": secondary[0], "k": 1},
    ], 62)
    require(len(shear) + len(unshear) + len(swap) + len(write_secondary) == 9,
            "nine non-multiplier routing primitives")
    live_word = shear + forward + write_secondary + swap + backward + unshear
    require(len(live_word) == 80705, "reversible-gate count excluding two native ticks")

    # The native ticks are inserted before shear and after write_secondary.
    # Their timing is supplied; the second tick is not reversed afterwards.
    prepared_auxiliaries = set()
    seen = Counter()
    endpoint_digest = sha256()
    integrated_cases = 0
    post_tick_receivers = {1: (0, 4), 2: (1, 4), 3: (1, 0), 4: (2, 0)}
    character = (0, 1, -1, -1, 1)
    input_pistons = primary[:4]
    for pistons in product(range(5), repeat=4):
        s = (sum(pistons) + 1) % 5
        if s == 0:
            continue  # The core verifier checks the separately declared zero controls.
        memory = [0] * 62
        for wire, value in zip(primary, pistons + (0, 1)):
            memory[wire] = value
        memory[secondary[0]], memory[secondary[-1]] = 4, 1
        prepared_auxiliaries.add(tuple(memory[i] for i in range(62) if i not in input_pistons))
        before_gates = counters["primitive_gates"]
        before_ticks = counters["native_ticks"]
        native_tick(memory, primary, native_zero_tick, counters)
        checkpoint = tuple(memory[w] for w in primary)
        require(checkpoint[-2:] == post_tick_receivers[s], "native source receiver class")

        execute(shear, memory, counters)
        clean(memory, work)
        loaded = memory[low]
        execute(forward, memory, counters)
        clean(memory, work)
        emitted, forward_high = memory[low], memory[high]
        require(memory[archive] == 0, "compiler must preserve initially blank archive")
        execute(write_secondary, memory, counters)
        clean(memory, work)
        require(tuple(memory[w] for w in secondary) == ((4+emitted) % 5, 0, 0, 0, 0, 1),
                "secondary input comes from the actual live low wire")
        native_tick(memory, secondary, native_zero_tick, counters)
        secondary_checkpoint = tuple(memory[w] for w in secondary)
        require(secondary_checkpoint == secondary_expected(emitted),
                "complete secondary native-origin result")

        execute(swap, memory, counters)
        clean(memory, work)
        require((memory[low], memory[high], memory[archive]) == (emitted, 0, forward_high),
                "integrated actual high transfer")
        execute(backward, memory, counters)
        clean(memory, work)
        returned = memory[low]
        execute(unshear, memory, counters)
        clean(memory, work)
        require((loaded, emitted, forward_high, returned) == (s, 2*s % 5, 3*s % 5, s),
                "compiled live input/output/mirror digits")
        require(tuple(memory[w] for w in primary) == checkpoint,
                "entire primary native post-tick checkpoint restored")

        expected = [0] * 62
        for wire, value in zip(primary, checkpoint):
            expected[wire] = value
        for wire, value in zip(secondary, secondary_expected(emitted)):
            expected[wire] = value
        expected[high], expected[archive] = s, 3*s % 5
        require(memory == expected, "complete 62-cell endpoint, retained second output and clean work")
        q1, r1 = checkpoint[-2:]
        sign = -1 if q1 == 1 else 1
        paired_sign = -1 if memory[secondary[-2]] == 1 else 1
        require(sign == character[s] == -character[memory[archive]], "primary/carry sign")
        require(paired_sign == -sign == -character[memory[high]], "paired native/carry sign")
        require(counters["primitive_gates"] - before_gates == 80705, "per-case primitive count")
        require(counters["native_ticks"] - before_ticks == 2, "per-case two native origins")
        seen[(s, q1, r1, emitted, memory[archive], memory[high], sign, paired_sign)] += 1
        endpoint_digest.update(compact([pistons, memory]))
        integrated_cases += 1

    require(integrated_cases == 500 and len(prepared_auxiliaries) == 1, "500 inputs/common preparation")
    require(len(seen) == 4 and set(seen.values()) == {125}, "four boundary classes of multiplicity125")
    require(counters["primitive_gates"] - component_gates == 40352500, "integrated primitive total")
    require(counters == {"primitive_gates": 43176900, "native_ticks": 1000}, "whole compiled audit counts")
    return {
        "status": "PASS",
        "scope": "L1 supplied discrete basis-register gates; no pulse simulation or native inverse",
        "compiler_source_commit": COMPILER_COMMIT,
        "compiler_source_blob": COMPILER_BLOB,
        "compiler_source_sha256": COMPILER_SHA256,
        "compiler_source_bytes": COMPILER_BYTES,
        "compiler_cells": 50,
        "compiler_clean_work_cells": 48,
        "component_archive_cells": 1,
        "integrated_cells": 62,
        "initially_varying_cells": 4,
        "common_initialized_cells": 58,
        "multiplier_primitive_gates": len(forward),
        "multiplier_inventory": inventory,
        "forward_word_sha256": sha256(compact(forward)).hexdigest(),
        "inverse_word_sha256": sha256(compact(backward)).hexdigest(),
        "component_input_words_per_direction": 25,
        "component_marked_mirrors_and_full_undos": 5,
        "component_primitive_gates": component_gates,
        "component_endpoint_sha256": component_digest.hexdigest(),
        "mirror_rows": mirror_rows,
        "integrated_admitted_heads": integrated_cases,
        "integrated_distinct_boundary_classes": len(seen),
        "integrated_boundary_rows_with_multiplicity": [list(row) + [count] for row, count in sorted(seen.items())],
        "integrated_primitive_gates_each": 80705,
        "integrated_native_ticks_each": 2,
        "integrated_primitive_gates": 40352500,
        "integrated_native_ticks": counters["native_ticks"],
        "integrated_complete_endpoint_sha256": endpoint_digest.hexdigest(),
        "total_primitive_gates": counters["primitive_gates"],
    }
