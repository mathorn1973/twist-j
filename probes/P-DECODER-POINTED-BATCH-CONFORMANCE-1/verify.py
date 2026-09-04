#!/usr/bin/env python3
"""Pinned exact audit of one chosen mathematical decoder, not physical closure."""

import ast
from dataclasses import fields
from fractions import Fraction as F
from itertools import product
import hashlib
import json
from pathlib import Path

import apparatus
import audit_apparatus
import audit_geometry
import decoder
import geometry
import kernel


# Filled once from the accepted static-reviewed sources before the public pin.
EXPECTED_DEPENDENCIES = {
    "kernel.py": "8fe60efb5f1c8888ac455332ec8305bc531687836f5c604aedd2e483ed534ba9",
    "geometry.py": "e485201def16cf7c237ee662167ddf9de787fd89f9af32c5e2622e2ce25f4e4c",
    "apparatus.py": "b9efc44e415c250f7a7c4639a05601ad97713ac20d5e49e14da894bc05581e79",
    "decoder.py": "85809a77013791ef9fa175484bc3a85e7b515eaeda20fd3ba36fdc5d6627b912",
    "audit_geometry.py": "4e4a07e384600eaa3480d3c026fcaaa04ec3f2a5cf780eae4254edf6fa740d9a",
    "audit_apparatus.py": "26afd62aed517289624dec8a9f6a167ccb4a6c99e573803877a20c5f646aa87b",
    "PROFILE.json": "2007c0a68d663eb4214341c75f7310d1430ca8e2cf4620f9bac03616aae6f79e"
}


def reference_generator(index, x):
    """Independent affine-matrix presentation over F5."""
    identity = [[int(i == j) for j in range(6)] for i in range(6)]
    matrix = [[0] * 6 for _ in range(6)]
    offset = [0] * 6
    if index == 0:
        for row, col in enumerate((1, 0, 3, 2, 4, 5)):
            matrix[row][col] = 1
    elif index in (1, 2):
        for row, col in enumerate((2, 3, 0, 1, 4, 5)):
            matrix[row][col] = -1
        if index == 2:
            matrix[1][5] += 1
            matrix[3][5] -= 1
            offset = [2, 1, 2, 1, 1, 0]
    else:
        matrix = [[-value for value in row] for row in identity]
        offset = [2, 1, 3, 4, 1 + int(index == 4), 1]
    return tuple((sum(row[j] * x[j] for j in range(6)) + c) % 5
                 for row, c in zip(matrix, offset))


def reference_u(checkpoint):
    n, x = checkpoint
    parity = 0
    remaining = n
    while remaining:
        parity ^= remaining % 2
        remaining //= 2
    return n + 1, reference_generator((sum(x) + 2 * parity) % 5, x)


def check_kernel():
    for x in product(range(5), repeat=6):
        for index in range(5):
            y = kernel.generator(index, x)
            assert y == reference_generator(index, x)
            assert kernel.generator(index, y) == x
        for n in (0, 1):
            assert kernel.u_step((n, x)) == reference_u((n, x))
        assert kernel.linear_tr4((0, x)) == sum(x[:4]) % 5
    for n in range(4096):
        assert kernel.theta(2 * n) == kernel.theta(n)
        assert kernel.theta(2 * n + 1) == 1 - kernel.theta(n)
    for n in (2, 3, 7, 8, 2**80 + 3):
        assert kernel.u_step((n, (1, 3, 2, 4, 1, 0))) == reference_u(
            (n, (1, 3, 2, 4, 1, 0)))


def check_qdd():
    assert tuple(field.name for field in fields(kernel.QDDRecord)) == (
        "support_state", "total_weight", "branch_weights", "density_state",
        "normalized_weight_state")
    gram = tuple(tuple(F(int(i == j)) - F(1, 5) for j in range(4))
                 for i in range(4))
    for pentits in product(range(5), repeat=4):
        v = tuple(z if z <= 2 else z - 5 for z in pentits)
        source = (0, pentits + (0, 0))
        result = kernel.direct_qdd(source)
        for n, q, r in ((1, 4, 2), (2**80 + 3, 1, 3)):
            assert kernel.direct_qdd((n, pentits + (q, r))) == result
        total = sum(v)
        m = sum(F(v[i]) * gram[i][j] * v[j] for i in range(4) for j in range(4))
        assert result.total_weight == m
        if not any(v):
            assert result == kernel.QDDRecord("ZERO_SUPPORT", F(0), (F(0), F(0)),
                                             "ZERO_DENOMINATOR", "ZERO_DENOMINATOR")
            continue
        assert m > 0 and result.support_state == "SUPPORTED"
        low = F(total * total, 20)
        high = sum(F(z * z) for z in v) - F(total * total, 4)
        assert result.branch_weights == (low, high)
        assert low >= 0 and high >= 0 and low + high == m
        expected = tuple(tuple(F(v[i]) * sum(gram[j][k] * v[k] for k in range(4)) / m
                               for j in range(4)) for i in range(4))
        assert result.density_state == kernel.Density(expected)
        assert sum(expected[i][i] for i in range(4)) == 1
        assert tuple(tuple(sum(expected[i][k] * expected[k][j] for k in range(4))
                           for j in range(4)) for i in range(4)) == expected
        assert result.normalized_weight_state == kernel.Normalized((low / m, high / m))
    # The direct-write dependency closure is isolated from the factor audit.
    tree = ast.parse(Path(kernel.__file__).read_text(encoding="utf-8"))
    functions = {node.name: node for node in tree.body if isinstance(node, ast.FunctionDef)}
    closure, queue = set(), ["direct_qdd"]
    while queue:
        name = queue.pop()
        if name in closure:
            continue
        closure.add(name)
        for node in ast.walk(functions[name]):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                if node.func.id in functions:
                    queue.append(node.func.id)
    assert closure == {"direct_qdd", "balanced_head", "validate_head", "trace_pairing",
                       "field_trace", "field_mul", "field_conjugate"}
    forbidden = {"gram", "dagger", "transpose", "projector", "F_QDD", "Q_QDD"}
    assert not any(isinstance(node, ast.Name) and node.id in forbidden
                   for name in closure for node in ast.walk(functions[name]))


def check_profile():
    profile = json.loads(Path(__file__).with_name("PROFILE.json").read_text(encoding="utf-8"))
    required = {"candidate_id", "public_pin_id", "read_convention_id", "history_equivalence_id",
                "region_id", "coarse_graining_id", "carrier_manifest", "record_field_manifest",
                "stage_manifest", "leg_manifest", "bridge_manifest", "quadratic_manifest",
                "apparatus_manifest", "physics_manifest", "measure_manifest", "closure_manifest",
                "obligation_manifest"}
    assert required <= set(profile)
    assert profile["candidate_id"] == decoder.CANDIDATE_ID
    assert {stage["stage_id"] for stage in profile["stage_manifest"]} == {
        "D_matter", "D_geom", "D_clock"}
    assert {leg["leg_id"] for leg in profile["leg_manifest"]} == {
        "D_linear", "D_binary", "D_quadratic"}
    records = profile["record_field_manifest"]
    keys = [(record["record_id"], record["field_id"]) for record in records]
    assert len(keys) == len(set(keys))
    assert len({record["field_id"] for record in records}) == len(records)
    classes = (kernel.QDDRecord, kernel.Density, kernel.Normalized,
               decoder.MatterRecord, decoder.GeometryFrame, decoder.ClockRecord,
               decoder.Frame, decoder.History, geometry.GeometryRecord,
               geometry.TesseractRecord, geometry.TorusRecord, apparatus.BatchRecord,
               apparatus.PairBank, apparatus.FiberRange, apparatus.UnitRecord,
               apparatus.PairRecord, apparatus.Support, apparatus.Controller)
    classes_by_name = {cls.__name__: cls for cls in classes}
    schemas = profile["record_schema_manifest"]
    assert len(schemas) == len(classes_by_name)
    assert {schema["python_record"] for schema in schemas} == set(classes_by_name)
    for schema in schemas:
        cls = classes_by_name[schema["python_record"]]
        names = tuple(field.name for field in fields(cls))
        assert tuple(schema["stored_field_names"]) == names
        assert schema["wire_type_tag"] == cls.__name__
        assert schema["module_path"] == (
            "probes/P-DECODER-POINTED-BATCH-CONFORMANCE-1/" + cls.__module__ + ".py")
        assert cls.__dataclass_params__.frozen
        declared = [record["python_field"] for record in records
                    if record["python_record"] == cls.__name__
                    and record["representation"] == "STORED_DATACLASS_FIELD"]
        assert len(declared) == len(names) and set(declared) == set(names)
    definitions = profile["definitions"]
    for record in records:
        assert record["stage_id"] in {"D_matter", "D_geom", "D_clock"}
        assert record["role"] in {"READOUT", "AUXILIARY"}
        if record["role"] == "READOUT":
            assert record["leg_id"] in {"D_linear", "D_binary", "D_quadratic"}
        else:
            assert record["leg_id"] == "NOT_APPLICABLE"
            assert record["absence_basis_item_id"] in definitions
        cls = classes_by_name[record["python_record"]]
        if record["representation"] == "PURE_DERIVED_PROPERTY_OF_COMPACT_BATCH":
            assert isinstance(getattr(cls, record["python_field"]), property)
        for key in ("field_type_id", "carrier_id", "domain_id", "normalization_id",
                    "equality_id", "source_item_id", "write_map_id", "emit_rule_id"):
            assert record[key] in definitions
    for leg in profile["leg_manifest"]:
        expected_ids = {record["field_id"] for record in records
                        if record["role"] == "READOUT" and record["leg_id"] == leg["leg_id"]}
        assert set(leg["owned_field_ids"]) == expected_ids
        assert len(leg["owned_field_ids"]) == len(expected_ids)
    assert profile["closure_manifest"]["feeds_U"] == "FALSE"
    assert any(item["value_state"] == "UNRESOLVED" for item in profile["obligation_manifest"])
    assert "UNRESOLVED" in json.dumps(profile["apparatus_manifest"])
    assert "UNRESOLVED" in json.dumps(profile["physics_manifest"])
    # U's module may depend only on standard exact-arithmetic/type facilities.
    tree = ast.parse(Path(kernel.__file__).read_text(encoding="utf-8"))
    imports = {node.module for node in tree.body if isinstance(node, ast.ImportFrom)}
    assert imports == {"dataclasses", "fractions"}
    assert not any(isinstance(node, ast.Import) for node in ast.walk(tree))


def check_prefix():
    heads = ((0, (0, 0, 0, 0, 0, 0)), (7, (0, 0, 0, 0, 4, 3)),
             (0, (1, 0, 0, 0, 0, 0)), (0, (1, 1, 1, 1, 0, 0)),
             (7, (1, 3, 2, 4, 1, 0)), (2**80 + 3, (1, 3, 2, 4, 1, 0)))
    for head in heads:
        chosen = decoder.Decoder(head)
        history = chosen.prefix(3)
        assert history.source_header == head and len(history.frames) == 3
        assert chosen.prefix(0).frames == ()
        for length in (1, 2):
            assert chosen.prefix(length).frames == history.frames[:length]
        checkpoint = head
        qdd = kernel.direct_qdd(head)
        batch_history = ()
        v = kernel.balanced_head(head)
        a = tuple(5 * z - sum(v) for z in v + (0,))
        for cut, frame in enumerate(history.frames):
            assert frame.clock.checkpoint == checkpoint
            assert frame.clock.source_header == head
            assert frame.clock.elapsed_cut == cut
            assert frame.clock.absolute_counter == head[0] + cut
            assert frame.clock.tick_cycles == F(head[0] + cut, 5)
            assert frame.matter.qdd == qdd and frame.matter.anchored_piston == v
            assert frame.matter.linear_tr4 == sum(checkpoint[1][:4]) % 5
            assert frame.matter.binary_theta == kernel.theta(checkpoint[0])
            assert frame.geometry.seed == history.frames[0].geometry.seed
            assert frame.clock.batch.a == a
            assert frame.clock.batch.provenance_checkpoint == checkpoint
            assert frame.clock.terminal_batch is True
            batch_history = apparatus.append_history(batch_history, frame.clock.batch)
            checkpoint = reference_u(checkpoint)
            a = tuple(a[k] + a[(k + 3) % 5] - a[(k + 2) % 5] - a[(k + 1) % 5]
                      for k in range(5))
        assert len(batch_history) == 3
        assert history.frames[0].geometry.wave == history.frames[1].geometry.wave
        assert history.frames[2].geometry.wave == geometry.wave_step(
            history.frames[0].geometry.wave, history.frames[1].geometry.wave)
        # Presentation includes exact integer fractions and provenance, no floats.
        encoded = decoder.exact_json(history)
        assert encoded["source_header"] == [head[0], list(head[1])]
    # QDD LOW/HIGH and five-cell populations must remain different interfaces.
    frame = decoder.Decoder((0, (1, 1, 1, 1, 0, 0))).prefix(1).frames[0]
    assert frame.matter.qdd.normalized_weight_state.weights == (F(1), F(0))
    assert frame.clock.batch.ratio == (F(1, 20),) * 4 + (F(4, 5),)


def check_invalid():
    invalid_heads = ((-1, (0,) * 6), (True, (0,) * 6), (0, (0,) * 5),
                     (0, (0, 0, 0, 0, 0, 5)), (0, [0] * 6),
                     (0, (0, 0, 0, 0, 0, False)))
    for head in invalid_heads:
        try:
            decoder.Decoder(head)
        except (ValueError, TypeError):
            pass
        else:
            raise AssertionError("ill-typed head accepted")
    for cuts in (-1, True, F(1, 2), "1"):
        try:
            decoder.Decoder((0, (0,) * 6)).prefix(cuts)
        except (ValueError, TypeError):
            pass
        else:
            raise AssertionError("ill-typed prefix length accepted")


def gate(name, function):
    try:
        function()
    except AssertionError:
        return name, False
    return name, True


def main():
    if not __debug__:
        raise RuntimeError("the assertion audit requires non-optimized Python")
    if len(EXPECTED_DEPENDENCIES) != 7:
        raise RuntimeError("accepted dependency hash table is incomplete")
    for name, expected in EXPECTED_DEPENDENCIES.items():
        actual = hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
        if actual != expected:
            raise RuntimeError("immutable dependency mismatch: " + name)
    gates = [gate("G01_KERNEL", check_kernel), gate("G02_DIRECT_QDD", check_qdd),
             gate("G03_PROFILE_OWNERSHIP", check_profile)]
    gates.extend(audit_geometry.run_checks())
    gates.extend(audit_apparatus.run_checks())
    gates.extend([gate("G09_PREFIX", check_prefix), gate("G10_TYPES", check_invalid)])
    print("PROBE P-DECODER-POINTED-BATCH-CONFORMANCE-1")
    print("MODE RESULT-EXPOSED CHOICE-EXPLICIT PROOF-FIRST L1")
    for name, passed in gates:
        print("CHECK", name, "PASS" if passed else "FIRED")
    passed = all(value for _, value in gates)
    print("CLAIM POINTED-DECODER-PREFIX-CONSISTENCY", "CONFIRMED" if passed else "FIRED")
    print("PHYSICAL_COMPLETION UNRESOLVED")
    print("COINCIDENCE_RECORD_FREQUENCY UNTESTED STOP")
    print("PUBLIC_CLAIMS UNREGISTERED CANON_UNCHANGED")
    print("TERMINAL", "CONFIRMED" if passed else "SCIENTIFIC-FIRED")


if __name__ == "__main__":
    main()
