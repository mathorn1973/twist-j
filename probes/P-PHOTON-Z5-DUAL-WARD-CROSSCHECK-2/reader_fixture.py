#!/usr/bin/env python3
"""Synthetic L2/L3 fixture for the independent CROSSCHECK-2 state reader."""

from __future__ import annotations

import base64
from fractions import Fraction
import hashlib
import math
from pathlib import Path
import sys
from types import SimpleNamespace
from typing import Callable, Sequence

import analyze_crosscheck2 as analyzer
import state_reader as reader


INHERITED_SOURCE_HASHES = {
    "PREREG.md": "b7cd4112e46417f71a4a9ef9a07b0d3a1ec3eefafc3e91e25ecd736ce3df19a8",
    "dual_chain.py": "eea3e0de57660ecc881da191c5be0a49d64c379abc8d7161aaafc70e7fab1e34",
    "analyze_crosscheck.py": "2b41c4f15878d81a05d0edaef20ac643f9a411fd6f8e2c9941ba5dd1c657a8be",
    "primal_replay.cpp": "1cbf58eeb772ce5bd038324d6b57ee46fc2d0a1dafbb90595c74bf5c542490ce",
}


def site_index(L: int, coordinates: Sequence[int]) -> int:
    result = 0
    for coordinate in coordinates:
        result = result * L + coordinate % L
    return result


def shift(L: int, coordinates: Sequence[int], axis: int, distance: int = 1) -> tuple[int, ...]:
    result = list(coordinates)
    result[axis] = (result[axis] + distance) % L
    return tuple(result)


def plaquette_index(L: int, coordinates: Sequence[int], pair: tuple[int, int]) -> int:
    return site_index(L, coordinates) * len(reader.PAIRS) + reader.PAIRS.index(tuple(sorted(pair)))


def add_cycles(*cycles: dict[int, int]) -> dict[int, int]:
    result: dict[int, int] = {}
    for cycle in cycles:
        for plaquette, coefficient in cycle.items():
            value = (result.get(plaquette, 0) + coefficient) % 5
            if value:
                result[plaquette] = value
            else:
                result.pop(plaquette, None)
    return result


def scale_cycle(cycle: dict[int, int], scalar: int) -> dict[int, int]:
    return {index: (coefficient * scalar) % 5 for index, coefficient in cycle.items() if (coefficient * scalar) % 5}


def cube_boundary(L: int, coordinates: Sequence[int], axes: Sequence[int]) -> dict[int, int]:
    ordered = tuple(sorted(axes))
    result: dict[int, int] = {}
    base = tuple(coordinates)
    for position, axis in enumerate(ordered):
        face = tuple(value for value in ordered if value != axis)
        sign = 1 if position % 2 == 0 else -1
        for anchor, coefficient in ((shift(L, base, axis), sign), (base, -sign)):
            plaquette = plaquette_index(L, anchor, face)
            value = (result.get(plaquette, 0) + coefficient) % 5
            if value:
                result[plaquette] = value
            else:
                result.pop(plaquette, None)
    return result


def cycle_state(L: int, cycle: dict[int, int]) -> list[int]:
    state = [0] * reader.state_size(L)
    for plaquette, coefficient in cycle.items():
        state[plaquette] = coefficient
    return state


def harmonic_L2() -> list[int]:
    L = 2
    state = [0] * reader.state_size(L)
    for x0 in range(L):
        for x1 in range(L):
            state[plaquette_index(L, (x0, x1, 0, 0), (0, 1))] = 1
    return state


def current_witness_L3() -> list[int]:
    L = 3
    central_coordinates = (1, 1, 1, 1)
    central = plaquette_index(L, central_coordinates, (0, 1))
    incidents: list[dict[int, int]] = []
    for axis in (2, 3):
        axes = (0, 1, axis)
        for base in (central_coordinates, shift(L, central_coordinates, axis, -1)):
            cube = cube_boundary(L, base, axes)
            coefficient = cube.get(central, 0)
            if coefficient not in (1, 4):
                raise AssertionError("fixture incident cube missed central face")
            incidents.append(scale_cycle(cube, 1 if coefficient == 1 else 4))
    if len(incidents) != 4 or any(cycle.get(central) != 1 for cycle in incidents):
        raise AssertionError("fixture incident alignment failed")
    before = cycle_state(L, incidents[0])
    tristar = add_cycles(*incidents[1:])
    after = list(before)
    for plaquette, coefficient in tristar.items():
        after[plaquette] = (after[plaquette] + coefficient) % 5
    if any(value not in (0, 1, 4) for value in after):
        raise AssertionError("fixture current witness left hard support")
    return after


def checkpoint(L: int, state: Sequence[int], index: int = 1) -> dict[str, object]:
    encoded = reader.pack_residues(state)
    unpacked = bytes(state)
    state_hash = hashlib.sha256(unpacked).hexdigest()
    derived = reader.derive_state(L, encoded, state_hash)
    return {
        "L": L,
        "checkpoint": index,
        "current_hash": derived.current_hash,
        "current_nonzero": int(derived.j_nonzero != 0),
        "homology": list(derived.homology),
        "j_nnz": derived.j_nonzero,
        "j2_sum": derived.j2_sum,
        "n_sum": derived.n_sum,
        "packed_state_sha256": derived.packed_state_sha256,
        "post_warm_bottom_attempt": index,
        "state_2bit_base64": encoded,
        "state_sha256": state_hash,
        "support": derived.support,
        "swap_accepted": 0,
        "transition": index,
        "type": "checkpoint",
        "walker_id": 0,
    }


def must_fail(label: str, action: Callable[[], object]) -> None:
    try:
        action()
    except reader.StateIntegrityError:
        return
    raise AssertionError(f"reader corruption gate did not fail: {label}")


class FixtureStats:
    @staticmethod
    def series_stats(values: Sequence[float]) -> SimpleNamespace:
        mean = sum(values) / len(values)
        return SimpleNamespace(mean=mean, mcse=0.01, ess=float(len(values)), variance=1.0)

    @staticmethod
    def half_drift_z(values: Sequence[float]) -> float:
        return 0.0

    @staticmethod
    def rank_folded_rhat(series: Sequence[Sequence[float]]) -> tuple[float, float]:
        return 1.0, 1.0

    @staticmethod
    def bulk_tail_ess(series: Sequence[Sequence[float]]) -> tuple[float, float]:
        return 1000.0, 500.0

    @staticmethod
    def conservative_group_mean_se(entries: Sequence[SimpleNamespace]) -> tuple[float, float]:
        return sum(float(entry.mean) for entry in entries) / len(entries), 0.01

    @staticmethod
    def z_difference(*values: float) -> float:
        return 0.0


def inherited_contract() -> tuple[object, object]:
    base = Path(__file__).resolve().parent
    inherited = base.parent / "P-PHOTON-Z5-DUAL-WARD-CROSSCHECK-1"
    source_bytes: dict[str, bytes] = {}
    for name, expected in INHERITED_SOURCE_HASHES.items():
        try:
            raw = (inherited / name).read_bytes()
        except OSError as error:
            raise AssertionError(f"inherited source missing: {name}") from error
        if hashlib.sha256(raw).hexdigest() != expected:
            raise AssertionError(f"inherited source hash: {name}")
        source_bytes[name] = raw
    old_chain = analyzer.load_hashed_module(
        inherited / "dual_chain.py",
        INHERITED_SOURCE_HASHES["dual_chain.py"],
        "crosscheck2_fixture_old_chain",
    )
    old_analysis = analyzer.load_hashed_module(
        inherited / "analyze_crosscheck.py",
        INHERITED_SOURCE_HASHES["analyze_crosscheck.py"],
        "crosscheck2_fixture_old_analysis",
    )
    if tuple(old_analysis.FAMILIES) != tuple(analyzer.FAMILIES):
        raise AssertionError("inherited families")
    if old_analysis.BLOCK != analyzer.PRIMAL_BLOCK or old_analysis.SAMPLES != analyzer.PRIMAL_SAMPLES:
        raise AssertionError("inherited primal blocking")
    if old_analysis.KAPPA2.hex() != analyzer.KAPPA2.hex() or old_analysis.INV_KAPPA2.hex() != analyzer.INV_KAPPA2.hex():
        raise AssertionError("inherited character constants")
    if old_analysis.PILOT_HASHES != analyzer.PILOT_HASHES or old_analysis.PRIMAL_SPECS != analyzer.PRIMAL_SPECS:
        raise AssertionError("inherited primal inputs")
    if (
        analyzer.CONTACT_PRECISION_LIMIT != 0.03
        or analyzer.OFFCONTACT_PRECISION_LIMIT != 0.02
        or analyzer.STANDARD_ERROR_BUDGET != 4.0
        or analyzer.DICTIONARY_SLACK != 5e-15
        or analyzer.WARD_ESS_MIN != 64.0
        or analyzer.WARD_PRIMAL_RHAT_MAX != 1.10
        or analyzer.WARD_DUAL_RHAT_MAX != 1.05
        or analyzer.WARD_BULK_ESS_MIN != 200.0
        or analyzer.WARD_DRIFT_Z_MAX != 4.0
        or analyzer.WARD_START_Z_MAX != 4.0
        or analyzer.WARD_UNIQUE_MIN != 0.99
    ):
        raise AssertionError("inherited Ward budgets")
    expected_terminals = {
        "BREAK_DUAL_DICTIONARY",
        "STOP_DUAL_INTEGRITY",
        "STOP_DUAL_MIXING",
        "DUAL_CROSSCHECK_PASS",
    }
    if analyzer.TERMINAL_VOCABULARY != expected_terminals:
        raise AssertionError("inherited terminal vocabulary")
    analysis_source = source_bytes["analyze_crosscheck.py"].decode("ascii")
    prereg_source = source_bytes["PREREG.md"].decode("ascii")
    for literal in (
        "halfwidth = 4.0 * se",
        "abs(residual) <= halfwidth + 5e-15",
        'format_identity(L, "contact", *contact, 0.03)',
        "format_identity(L, family, *residual, 0.02)",
    ):
        if literal not in analysis_source:
            raise AssertionError(f"inherited analysis literal: {literal}")
    for terminal in expected_terminals:
        if terminal not in analysis_source and terminal not in prereg_source:
            raise AssertionError(f"inherited terminal literal: {terminal}")
    return old_chain, old_analysis


def compare_old_reader(old_chain: object, L: int, state: Sequence[int], derived: reader.DerivedState) -> None:
    lattice = old_chain.Torus4(L)
    old_current = tuple(old_chain.validate_state(lattice, state))
    if old_current != derived.current:
        raise AssertionError(f"L{L} inherited current")
    old_boundary = tuple(old_chain.integer_boundary(lattice, state))
    if old_boundary != tuple(5 * value for value in derived.current):
        raise AssertionError(f"L{L} inherited integer boundary")

    plaquettes = old_chain.plaquette_statistics(lattice, state)
    if plaquettes["n_sum"] != derived.n_sum or tuple(plaquettes["n_sum_by_orientation"]) != derived.n_sum_by_orientation:
        raise AssertionError(f"L{L} inherited n")
    if plaquettes["n2_sum"] != derived.n2_sum or tuple(plaquettes["n2_sum_by_orientation"]) != derived.n2_sum_by_orientation:
        raise AssertionError(f"L{L} inherited n2")
    old_pairs = plaquettes["pair_products"]
    if [entry["family"] for entry in old_pairs] != list(reader.FAMILY_NAMES):
        raise AssertionError(f"L{L} inherited pair order")
    for old, new in zip(old_pairs, derived.pair_sums):
        if old["sum"] != new.total or tuple(old["sum_by_orientation"]) != new.by_orientation:
            raise AssertionError(f"L{L} inherited pair {new.family}")

    currents = old_chain.current_statistics(lattice, old_current)
    exact_current_claims = (
        (currents["j_sum"], derived.j_sum),
        (tuple(currents["j_sum_by_direction"]), derived.j_sum_by_direction),
        (currents["j2_sum"], derived.j2_sum),
        (tuple(currents["j2_sum_by_direction"]), derived.j2_sum_by_direction),
        (currents["j_nonzero_count"], derived.j_nonzero),
        (tuple(currents["j_nonzero_count_by_direction"]), derived.j_nonzero_by_direction),
    )
    if any(left != right for left, right in exact_current_claims):
        raise AssertionError(f"L{L} inherited current statistics")

    modes = old_chain.low_momentum_statistics(lattice, old_current)["lowest_momenta"]
    for old, new in zip(modes, derived.lowest_momenta):
        if old["momentum_axis"] != new.momentum_axis:
            raise AssertionError(f"L{L} inherited momentum order")
        if not math.isclose(float(old["sj_trace"]), float(new.trace), rel_tol=0.0, abs_tol=2e-15):
            raise AssertionError(f"L{L} inherited momentum trace")
        if not math.isclose(float(old["longitudinal_power"]), float(new.longitudinal_power), rel_tol=0.0, abs_tol=2e-15):
            raise AssertionError(f"L{L} inherited longitudinal power")


def run_fixture() -> list[str]:
    old_chain, _old_analysis = inherited_contract()
    state2 = harmonic_L2()
    record2 = checkpoint(2, state2)
    derived2 = reader.verify_checkpoint(2, record2)
    if derived2.homology != (1, 0, 0, 0, 0, 0) or derived2.j_nonzero != 0:
        raise AssertionError("L2 harmonic fixture census")
    if not all(isinstance(entry.trace, Fraction) for entry in derived2.lowest_momenta):
        raise AssertionError("L2 exact power type")
    compare_old_reader(old_chain, 2, state2, derived2)

    state3 = current_witness_L3()
    record3 = checkpoint(3, state3, 16)
    derived3 = reader.verify_checkpoint(3, record3)
    if derived3.j_nonzero == 0 or derived3.j2_sum == 0:
        raise AssertionError("L3 current fixture failed to carry current")
    if not all(isinstance(entry.trace, Fraction) for entry in derived3.lowest_momenta):
        raise AssertionError("L3 exact power type")
    compare_old_reader(old_chain, 3, state3, derived3)
    compact3 = reader.sufficient_record(record3, derived3)
    if "state_b64" not in compact3 or "state_2bit_base64" in compact3:
        raise AssertionError("audit state selection")
    parsed3 = analyzer._validate_sufficient_checkpoint(compact3, 3, 16)
    if float(parsed3["j2_mean"]) <= 0.0 or len(parsed3) != 15:
        raise AssertionError("analyzer sufficient-statistics adapter")
    ordinary3 = reader.sufficient_record(checkpoint(3, state3, 15), derived3)
    if "state_b64" in ordinary3:
        raise AssertionError("non-audit state leaked")
    analyzer._validate_sufficient_checkpoint(ordinary3, 3, 15)

    corrupt_hash = dict(record2)
    corrupt_hash["state_sha256"] = "0" * 64
    must_fail("state_hash", lambda: reader.verify_checkpoint(2, corrupt_hash))

    corrupt_support = dict(record2)
    corrupt_support["support"] = int(corrupt_support["support"]) + 1
    must_fail("support", lambda: reader.verify_checkpoint(2, corrupt_support))

    corrupt_homology = dict(record2)
    corrupt_homology["homology"] = [0] * 6
    must_fail("H2", lambda: reader.verify_checkpoint(2, corrupt_homology))

    corrupt_packed_hash = dict(record2)
    corrupt_packed_hash["packed_state_sha256"] = "0" * 64
    must_fail("packed_hash", lambda: reader.verify_checkpoint(2, corrupt_packed_hash))

    open_state = [0] * reader.state_size(2)
    open_state[0] = 1
    open_encoded = reader.pack_residues(open_state)
    open_hash = hashlib.sha256(bytes(open_state)).hexdigest()
    must_fail("closure", lambda: reader.derive_state(2, open_encoded, open_hash))

    packed3 = bytearray(base64.b64decode(record3["state_2bit_base64"], validate=True))
    packed3[-1] |= 1
    bad_tail = base64.b64encode(packed3).decode("ascii")
    must_fail("tail", lambda: reader.unpack_residues(3, bad_tail))

    packed2 = bytearray(base64.b64decode(record2["state_2bit_base64"], validate=True))
    packed2[0] = (packed2[0] & 0x3F) | 0xC0
    invalid_code = base64.b64encode(packed2).decode("ascii")
    must_fail("code_11", lambda: reader.unpack_residues(2, invalid_code))

    audit_count = sum(reader.should_audit(index) for index in range(1, reader.FORMAL_CHECKPOINTS + 1))
    if audit_count != 128 or not reader.should_audit(2048) or reader.should_audit(2047):
        raise AssertionError("formal audit selection")
    bound = reader.committed_size_upper_bound()
    if bound > reader.MAX_COMMITTED_STREAM_BYTES:
        raise AssertionError("committed schema exceeds cap")

    mixing_chains = tuple(
        analyzer.Chain(
            f"fixture_{start}_{replica}",
            3,
            start,
            replica,
            tuple(
                {"state_hash": f"{start}-{replica}-{index}", "n_mean": float(index & 1)}
                for index in range(analyzer.DUAL_SAMPLES)
            ),
        )
        for start in ("cold", "stratified")
        for replica in (1, 2)
    )
    mixing_line, mixing_failures = analyzer.ward_mixing_audit(
        FixtureStats(), 3, "dual", mixing_chains, ("n_mean",)
    )
    if mixing_failures or " PASS " not in mixing_line:
        raise AssertionError("Ward mixing fixture")

    return [
        f"STATE_READER_FIXTURE L=2 support={derived2.support} H2={','.join(map(str, derived2.homology))} j_nnz={derived2.j_nonzero} status=PASS",
        f"STATE_READER_FIXTURE L=3 support={derived3.support} H2={','.join(map(str, derived3.homology))} j_nnz={derived3.j_nonzero} j2_sum={derived3.j2_sum} status=PASS",
        "STATE_READER_CORRUPTION_GATES count=7 status=PASS",
        "INHERITED_WARD_CONTRACT sources=4 families=4 primal_block=32 primal_samples=512 status=PASS",
        f"AUDIT_SELECTION checkpoints=2048 stride=16 frames={audit_count} includes_2048=YES status=PASS",
        f"OUTPUT_BOUND upper_bytes={bound} max_bytes={reader.MAX_COMMITTED_STREAM_BYTES} audit_stride={reader.STATE_AUDIT_STRIDE} status=PASS",
        "STATE_READER_FIXTURE PASS",
    ]


def main() -> int:
    if len(sys.argv) != 1:
        print("usage: python3 reader_fixture.py", file=sys.stderr)
        return 64
    try:
        lines = run_fixture()
    except (AssertionError, reader.StateIntegrityError, ValueError) as error:
        print(f"STATE_READER_FIXTURE FAIL reason={str(error).replace(' ', '_')}")
        return 1
    sys.stdout.buffer.write(("\n".join(lines) + "\n").encode("ascii"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
