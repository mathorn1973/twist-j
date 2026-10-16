#!/usr/bin/env python3
"""Pinned-source regression and honest failure-phase adapter audit (#1526).

PUBLIC / NON-CANONICAL / L1.
Probe: P-TWO-USE-READOUT-FAILURE-REGRESSION-1, parent #1506.
Original work and attributed source reuse Apache-2.0, A. M. Thorn, 2026-10-15.
"""

from __future__ import annotations

import ast
from dataclasses import dataclass
from fractions import Fraction
import hashlib
import inspect
from pathlib import Path
import sys
from typing import Callable, Dict, List, Optional, Sequence, Tuple

sys.dont_write_bytecode = True

THIS_DIR = Path(__file__).resolve().parent
ROOT = THIS_DIR.parents[1]
UPSTREAM_DIR = ROOT / "probes" / "P-TWO-USE-TYPED-READOUT-CLOSURE-1"


def _verify_pre_import_custody() -> Tuple[int, int]:
    code_sums_path = THIS_DIR / "CODE_SHA256SUMS"
    local_count = 0
    for line in code_sums_path.read_text(encoding="ascii").splitlines():
        expected_hash, rel_name = line.split("  ", 1)
        target = THIS_DIR / rel_name
        raw = target.read_bytes()
        actual_hash = hashlib.sha256(raw).hexdigest()
        if actual_hash != expected_hash:
            raise SystemExit(
                f"local custody mismatch for {rel_name}: expected={expected_hash}, actual={actual_hash}"
            )
        local_count += 1

    sources_path = THIS_DIR / "SOURCES.tsv"
    lines = sources_path.read_text(encoding="ascii").splitlines()
    if not lines or lines[0] != "commit\tpath\tsha256\tbytes":
        raise SystemExit("SOURCES.tsv header mismatch")
    upstream_count = 0
    for row in lines[1:]:
        commit_sha, rel_path, expected_sha256, expected_bytes_str = row.split("\t")
        if commit_sha != "b79143fb00839b870686f6cea34e174959060df1":
            raise SystemExit(f"unexpected source commit in SOURCES.tsv: {commit_sha}")
        target = ROOT / rel_path
        raw = target.read_bytes()
        if len(raw) != int(expected_bytes_str):
            raise SystemExit(
                f"source byte count mismatch for {rel_path}: expected={expected_bytes_str}, actual={len(raw)}"
            )
        actual_sha256 = hashlib.sha256(raw).hexdigest()
        if actual_sha256 != expected_sha256:
            raise SystemExit(
                f"source sha256 mismatch for {rel_path}: expected={expected_sha256}, actual={actual_sha256}"
            )
        upstream_count += 1
    return local_count, upstream_count


LOCAL_CUSTODY_COUNT, UPSTREAM_CUSTODY_COUNT = _verify_pre_import_custody()

if str(UPSTREAM_DIR) not in sys.path:
    sys.path.insert(0, str(UPSTREAM_DIR))

import apparatus as app  # noqa: E402


EXPECTED_DOMAIN_SHA256 = (
    "2e9b77cf8c507b9bc6675d9a07bf8e27ad88921c72c1efc22dcf5bdb41d8a7c0"
)
EXPECTED_COMPARE_RECORDS = 1200
EXPECTED_COMPARE_DIGEST = (
    "670f270e88386e2f1f507e24ec0ae71daf1ff6638ea44783b793479291af3dbc"
)

CANONICAL_STAGE_NAMES: Tuple[str, ...] = (
    "run_t01_geometry_stencil_and_operators",
    "run_t02_generators_and_v_non_invertibility",
    "run_t03_single_head_625_census_and_recovery",
    "run_t04_paired_factorization_390625",
    "run_t05_certificate_f_bijectivity_and_energy",
    "run_t06_certificate_hb_involutions_and_lbuf",
    "run_t07_certificate_bilinear_work_and_mu",
    "run_t08_25_pair_work_table_and_capacities",
    "run_t09_order_witness_14_vs_41",
    "run_t10_certificate_four_cut_operators_and_archives",
    "run_t11_direct_chronological_and_source_readers",
    "run_t12_store_bounds_refusal_and_negative_work",
    "run_t13_accepted_zero_and_clarification_ii",
    "run_t14_seven_eight_boundary_and_energy_invariants",
    "run_t15_ready_image_left_inverse_all_branches",
    "run_t16_calibration_prediction_and_clarification_i",
    "run_t17_comparator_indistinguishability_and_separations",
    "run_t18_invalid_endpoint_and_type_rejection_suite",
    "run_t19_typed_record_factorization",
)

PHASE_STATES: Tuple[str, ...] = (
    "AUDIT",
    "WITNESS_BUILDING",
    "COMPARISON_STARTED",
    "COMPARISON_FAILED",
    "COMPLETED",
)

ADAPTER_COMPLETION_MARKER = "ADAPTER_HARNESS_COMPLETE status=ALL_STAGES_PASS"


def require_eq(actual: object, expected: object, label: str) -> None:
    if actual != expected:
        raise AssertionError(f"{label}: expected={expected!r}, actual={actual!r}")


def require_true(
    cond: bool, label: str, *, expected: object = True, actual: object = False
) -> None:
    if not cond:
        raise AssertionError(f"{label}: expected={expected!r}, actual={actual!r}")


def fmt_frac(val: Fraction) -> str:
    return (
        f"{val.numerator}/{val.denominator}"
        if val.denominator != 1
        else f"{val.numerator}"
    )


def fmt_vec4(vec: Optional[Sequence[Fraction]]) -> str:
    if vec is None:
        return "None"
    return "(" + ",".join(fmt_frac(x) for x in vec) + ")"


# ---------------------------------------------------------------------------
# Isolated honest failure-phase reporting adapter (zero dynamical coupling)
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class AdapterReport:
    phase_state: str
    current_stage: str
    first_failed_stage: Optional[str]
    original_error: Optional[str]
    audit_status: str
    witness_status: str
    comparison_status: str
    remaining_dependent_checks: str
    executed_stages: Tuple[str, ...]
    witness_called: bool
    comparison_called: bool
    completion_marker_emitted: bool
    strict_exit_code: int
    harness_replay_exit_code: int
    emitted_lines: Tuple[str, ...]


def run_reporting_adapter(
    audit_stages: Sequence[Tuple[str, Callable[[], str]]],
    witness_fn: Callable[[], str],
    compare_fn: Callable[[], Tuple[str, int, str]],
    *,
    expected_domain_sha: str,
    expected_count: int,
    expected_digest: str,
) -> AdapterReport:
    """Execute staged callbacks with honest phase-state and comparison reporting."""
    phase_state = "AUDIT"
    current_stage = "not_started"
    audit_status = "IN_PROGRESS"
    witness_status = "NOT_RUN"
    comparison_status = "NOT_RUN"
    remaining_dependent_checks = "NOT_RUN"
    executed: List[str] = []
    witness_called = False
    comparison_called = False
    lines: List[str] = []

    try:
        for stage_name, stage_fn in audit_stages:
            current_stage = stage_name
            executed.append(stage_name)
            msg = stage_fn()
            lines.append(msg)
        audit_status = "PASS"

        phase_state = "WITNESS_BUILDING"
        current_stage = "witness_boundary_trajectories"
        witness_status = "IN_PROGRESS"
        witness_called = True
        witness_msg = witness_fn()
        lines.append(witness_msg)
        witness_status = "PASS"
        remaining_dependent_checks = "NONE"

        phase_state = "COMPARISON_STARTED"
        current_stage = "full_state_comparison"
        comparison_status = "STARTED"
        comparison_called = True
        domain_sha, count, digest = compare_fn()
        if domain_sha != expected_domain_sha:
            raise AssertionError(
                f"COMPARISON.domain_sha256: expected={expected_domain_sha!r}, actual={domain_sha!r}"
            )
        if count != expected_count:
            raise AssertionError(
                f"COMPARISON.count: expected={expected_count!r}, actual={count!r}"
            )
        if digest != expected_digest:
            raise AssertionError(
                f"COMPARISON.unchanged_I2_V2_state_stream: expected={expected_digest!r}, actual={digest!r}"
            )
        comparison_status = "PASS"
        phase_state = "COMPLETED"
        lines.append(
            f"TWOUSE-COMPARE-v2 domain_sha256={domain_sha} records={count} sha256={digest}"
        )
        lines.append(
            "ADAPTER_DIAGNOSTIC phase_state=COMPLETED audit=PASS witnesses=PASS "
            "comparison=PASS remaining_dependent_checks=NONE"
        )
        lines.append(ADAPTER_COMPLETION_MARKER)
        return AdapterReport(
            phase_state=phase_state,
            current_stage=current_stage,
            first_failed_stage=None,
            original_error=None,
            audit_status=audit_status,
            witness_status=witness_status,
            comparison_status=comparison_status,
            remaining_dependent_checks=remaining_dependent_checks,
            executed_stages=tuple(executed),
            witness_called=witness_called,
            comparison_called=comparison_called,
            completion_marker_emitted=True,
            strict_exit_code=0,
            harness_replay_exit_code=0,
            emitted_lines=tuple(lines),
        )
    except AssertionError as exc:
        err_text = str(exc)
        if phase_state == "AUDIT":
            audit_status = "FAIL"
            witness_status = "NOT_RUN"
            comparison_status = "NOT_RUN"
            remaining_dependent_checks = "NOT_RUN"
        elif phase_state == "WITNESS_BUILDING":
            witness_status = "FAIL"
            comparison_status = "NOT_RUN"
            remaining_dependent_checks = "NOT_RUN"
        elif phase_state == "COMPARISON_STARTED":
            phase_state = "COMPARISON_FAILED"
            comparison_status = "FAIL"
            remaining_dependent_checks = "NONE"
        lines.append(f"FALSIFIER phase={phase_state} stage={current_stage} {err_text}")
        lines.append(
            f"ADAPTER_DIAGNOSTIC phase_state={phase_state} audit={audit_status} "
            f"witnesses={witness_status} comparison={comparison_status} "
            f"remaining_dependent_checks={remaining_dependent_checks}"
        )
        return AdapterReport(
            phase_state=phase_state,
            current_stage=current_stage,
            first_failed_stage=current_stage,
            original_error=err_text,
            audit_status=audit_status,
            witness_status=witness_status,
            comparison_status=comparison_status,
            remaining_dependent_checks=remaining_dependent_checks,
            executed_stages=tuple(executed),
            witness_called=witness_called,
            comparison_called=comparison_called,
            completion_marker_emitted=False,
            strict_exit_code=1,
            harness_replay_exit_code=0,
            emitted_lines=tuple(lines),
        )


# ---------------------------------------------------------------------------
# Gate R01: Custody & historical verifier AST preservation check
# ---------------------------------------------------------------------------


def run_r01_custody_and_historical_verifier_ast() -> List[str]:
    require_eq(LOCAL_CUSTODY_COUNT, 4, "R01.local_custody_count")
    require_eq(UPSTREAM_CUSTODY_COUNT, 19, "R01.upstream_custody_count")

    upstream_verify_path = UPSTREAM_DIR / "verify.py"
    upstream_source = upstream_verify_path.read_text(encoding="utf-8")
    tree = ast.parse(upstream_source)

    run_full_audit_fn: Optional[ast.FunctionDef] = None
    main_fn: Optional[ast.FunctionDef] = None
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name == "run_full_audit":
            run_full_audit_fn = node
        elif isinstance(node, ast.FunctionDef) and node.name == "main":
            main_fn = node
    require_true(run_full_audit_fn is not None, "R01.found_run_full_audit")
    require_true(main_fn is not None, "R01.found_main")
    assert run_full_audit_fn is not None and main_fn is not None

    # Verify that in historical run_full_audit(), build_witness_trajectories()
    # is called before CURRENT_STAGE = "full_state_comparison" without a separate
    # witness CURRENT_STAGE assignment.
    stage_assignments: List[Tuple[int, str]] = []
    witness_call_lineno: Optional[int] = None
    for sub in ast.walk(run_full_audit_fn):
        if isinstance(sub, ast.Assign):
            for target in sub.targets:
                if isinstance(target, ast.Name) and target.id == "CURRENT_STAGE":
                    if isinstance(sub.value, ast.Constant) and isinstance(
                        sub.value.value, str
                    ):
                        stage_assignments.append((sub.lineno, sub.value.value))
                    elif isinstance(sub.value, ast.Attribute):
                        stage_assignments.append((sub.lineno, f"attr:{sub.value.attr}"))
        if isinstance(sub, ast.Call) and isinstance(sub.func, ast.Name):
            if sub.func.id == "build_witness_trajectories":
                witness_call_lineno = sub.lineno

    require_eq(
        stage_assignments,
        [(1845, "attr:__name__"), (1853, "full_state_comparison")],
        "R01.historical_stage_assignments",
    )
    require_eq(witness_call_lineno, 1850, "R01.historical_witness_call_lineno")

    # Verify that historical main() prints comparison=NOT_RUN on any AssertionError.
    except_prints: List[str] = []
    for sub in ast.walk(main_fn):
        if isinstance(sub, ast.ExceptHandler):
            for stmt in sub.body:
                if (
                    isinstance(stmt, ast.Expr)
                    and isinstance(stmt.value, ast.Call)
                    and isinstance(stmt.value.func, ast.Name)
                    and stmt.value.func.id == "print"
                    and stmt.value.args
                    and isinstance(stmt.value.args[0], ast.Constant)
                    and isinstance(stmt.value.args[0].value, str)
                ):
                    except_prints.append(stmt.value.args[0].value)
    require_eq(
        except_prints,
        ["TYPED_CLOSURE_FAIL remaining_dependent_checks=NOT_RUN comparison=NOT_RUN"],
        "R01.historical_unconditional_not_run_diagnostic",
    )
    return [
        f"R01 PASS: local_custody={LOCAL_CUSTODY_COUNT}/4 upstream_custody={UPSTREAM_CUSTODY_COUNT}/19 "
        "historical_verify_ast=(witness_lineno=1850_under_T19,comparison_diagnostic=unconditional_NOT_RUN) "
        "upstream_files_modified=0"
    ]


# ---------------------------------------------------------------------------
# Gate R02: Five semantic rejection branches (S1-S5) and positive controls (P1-P5)
# ---------------------------------------------------------------------------


def run_r02_semantic_rejections_and_positive_controls() -> List[str]:
    z: Tuple[int, int, int, int] = (0, 0, 0, 0)
    e: Tuple[int, int, int, int] = (1, 0, 0, 0)
    zero_q4 = app.zero_q4()
    e_q4 = app.basis_q4(0)
    ops = app.get_derived_operators()

    semantic_specimens: Tuple[Tuple[str, app.DirectPortReadout, str], ...] = (
        (
            "S1_REFUSED_A_NONZERO_B0",
            app.DirectPortReadout(e, z, sigma_A=1),
            "Inconsistent refused sigma_A=+1 with non-zero b0",
        ),
        (
            "S2_ZERO_B_SOURCE_NONZERO_RESIDUAL",
            app.DirectPortReadout(z, e, d=(0, 4)),
            "Inconsistent d=(0,4) with non-zero b2 - D2(alpha_A z_A)",
        ),
        (
            "S3_RESIDUAL_INCOMPATIBLE_WITH_D",
            app.DirectPortReadout(z, e, d=(1, 4)),
            "Residual b2 - D2(alpha_A z_A) does not match d on ready family",
        ),
        (
            "S4_SIGMA_B_CONTRADICTS_ZERO_COST_D",
            app.DirectPortReadout(z, z, sigma_B=1, d=(0, 4)),
            "Mismatch between sigma_B and (d, b0, b2) acceptance readout",
        ),
        (
            "S5_REFUSED_B_NONZERO_RESIDUAL",
            app.DirectPortReadout(z, e, sigma_B=1),
            "Inconsistent refused Contact B with non-zero residual b2",
        ),
    )

    out_lines: List[str] = []
    for spec_id, record, expected_msg in semantic_specimens:
        require_true(
            type(record) is app.DirectPortReadout,
            f"R02.{spec_id}.constructed_type",
        )
        try:
            app.direct_source_reader(record)
        except ValueError as exc:
            actual_msg = str(exc)
            require_eq(actual_msg, expected_msg, f"R02.{spec_id}.message")
            out_lines.append(
                f"SEMANTIC_REJECT id={spec_id} b0={fmt_vec4(record.b0)} b2={fmt_vec4(record.b2)} "
                f"sigma_A={record.sigma_A} sigma_B={record.sigma_B} d={record.d} "
                f"error=ValueError:{actual_msg!r}"
            )
        else:
            raise AssertionError(
                f"R02.{spec_id}: contradictory DirectPortReadout accepted without ValueError"
            )

    # Positive controls P1-P5
    # P1: Accepted zero
    rec_p1 = app.DirectPortReadout(z, z, sigma_A=-1, sigma_B=-1, d=(0, 4))
    dec_p1 = app.direct_source_reader(rec_p1)
    require_eq(
        (
            dec_p1["alpha_A"],
            dec_p1["alpha_B"],
            dec_p1["alpha_B_from_d_b0_b2"],
            dec_p1["z_A"],
            dec_p1["z_B"],
            dec_p1["alpha_A_z_A"],
            dec_p1["alpha_B_z_B"],
        ),
        (1, 1, 1, zero_q4, zero_q4, zero_q4, zero_q4),
        "R02.P1_ACCEPTED_ZERO",
    )
    out_lines.append(
        f"POSITIVE_CONTROL id=P1_ACCEPTED_ZERO alpha_A={dec_p1['alpha_A']} alpha_B={dec_p1['alpha_B']} "
        f"z_A={fmt_vec4(dec_p1['z_A'])} z_B={fmt_vec4(dec_p1['z_B'])}"
    )

    # P2: Refused input (refusal is never returned as accepted zero source)
    rec_p2 = app.DirectPortReadout(z, z, sigma_A=1, sigma_B=1, d=(1, 4))
    dec_p2 = app.direct_source_reader(rec_p2)
    require_eq(
        (
            dec_p2["alpha_A"],
            dec_p2["alpha_B"],
            dec_p2["alpha_B_from_d_b0_b2"],
            dec_p2["z_A"],
            dec_p2["z_B"],
            dec_p2["alpha_A_z_A"],
            dec_p2["alpha_B_z_B"],
        ),
        (0, 0, 0, None, None, zero_q4, zero_q4),
        "R02.P2_REFUSED_INPUT",
    )
    out_lines.append(
        f"POSITIVE_CONTROL id=P2_REFUSED_INPUT alpha_A={dec_p2['alpha_A']} alpha_B={dec_p2['alpha_B']} "
        f"z_A={fmt_vec4(dec_p2['z_A'])} z_B={fmt_vec4(dec_p2['z_B'])}"
    )

    # P3: Unknown acceptance at zero record
    rec_p3 = app.DirectPortReadout(z, z)
    dec_p3 = app.direct_source_reader(rec_p3)
    require_eq(
        (
            dec_p3["alpha_A"],
            dec_p3["alpha_B"],
            dec_p3["alpha_B_from_d_b0_b2"],
            dec_p3["z_A"],
            dec_p3["z_B"],
            dec_p3["alpha_A_z_A"],
            dec_p3["alpha_B_z_B"],
        ),
        (None, None, None, None, None, zero_q4, zero_q4),
        "R02.P3_UNKNOWN_ACCEPTANCE_ZERO",
    )
    out_lines.append(
        f"POSITIVE_CONTROL id=P3_UNKNOWN_ACCEPTANCE_ZERO alpha_A={dec_p3['alpha_A']} "
        f"alpha_B={dec_p3['alpha_B']} z_A={fmt_vec4(dec_p3['z_A'])} z_B={fmt_vec4(dec_p3['z_B'])}"
    )

    # P4: Deliberately partial contract on nonzero b2 = R0 z^(1) without sigma_B or d
    z1_vec = app.eta_lift((1, 4))
    r0_z1 = app.mat_vec_4(ops.R0, z1_vec)
    require_eq(
        r0_z1,
        (
            Fraction(-1421, 12960),
            Fraction(59, 2160),
            Fraction(59, 2160),
            Fraction(29, 1080),
        ),
        "R02.P4.r0_z1_value",
    )
    rec_p4 = app.DirectPortReadout(z, r0_z1)
    dec_p4 = app.direct_source_reader(rec_p4)
    require_eq(
        (
            dec_p4["alpha_A"],
            dec_p4["alpha_B"],
            dec_p4["alpha_B_from_d_b0_b2"],
            dec_p4["z_A"],
            dec_p4["z_B"],
            dec_p4["alpha_A_z_A"],
            dec_p4["alpha_B_z_B"],
        ),
        (None, None, None, None, None, zero_q4, z1_vec),
        "R02.P4_PARTIAL_CONTRACT_NONZERO_B2_NO_CONTEXT",
    )
    out_lines.append(
        f"POSITIVE_CONTROL id=P4_PARTIAL_CONTRACT_NONZERO_B2_NO_CONTEXT alpha_B={dec_p4['alpha_B']} "
        f"z_B={fmt_vec4(dec_p4['z_B'])} alpha_B_z_B={fmt_vec4(dec_p4['alpha_B_z_B'])} "
        "partial_contract_not_indistinguishability=TRUE"
    )

    # P5: Valid explicit integer-valued Q^4 record vs raw unlabelled tuple rejection
    rec_p5 = app.DirectPortReadout(e, z)
    dec_p5 = app.direct_source_reader(rec_p5)
    expected_r0_inv_e = (
        Fraction(-154224, 21535),
        Fraction(-1296, 365),
        Fraction(-1296, 365),
        Fraction(-75168, 21535),
    )
    require_eq(
        app.mat_vec_4(ops.R0_inv, e_q4),
        expected_r0_inv_e,
        "R02.P5.r0_inv_e0",
    )
    require_eq(dec_p5, app.decode_port_vectors(e, z), "R02.P5.matches_decode_port_vectors")
    require_eq(
        (
            dec_p5["alpha_A"],
            dec_p5["alpha_B"],
            dec_p5["alpha_B_from_d_b0_b2"],
            dec_p5["z_A"],
            dec_p5["z_B"],
        ),
        (1, None, None, expected_r0_inv_e, None),
        "R02.P5_VALID_EXPLICIT_INTEGER_Q4_RECORD",
    )
    try:
        app.direct_source_reader(e)  # type: ignore[arg-type]
    except TypeError as exc:
        require_eq(
            str(exc),
            "readout type mismatch (expected=DirectPortReadout, actual=tuple)",
            "R02.P5.raw_tuple_rejected",
        )
    else:
        raise AssertionError("R02.P5: raw integer 4-tuple accepted by direct_source_reader")
    out_lines.append(
        f"POSITIVE_CONTROL id=P5_VALID_EXPLICIT_INTEGER_Q4_RECORD alpha_A={dec_p5['alpha_A']} "
        f"z_A={fmt_vec4(dec_p5['z_A'])} raw_tuple_rejected=TypeError provenance_authenticated=FALSE"
    )
    out_lines.append(
        "R02 PASS: semantic_rejections=5/5 positive_controls=5/5 "
        "partial_contract_boundary=VERIFIED provenance_authentication=NOT_CLAIMED"
    )
    return out_lines


# ---------------------------------------------------------------------------
# Gate R03: Honest failure-phase reporting adapter harness (H1-H6)
# ---------------------------------------------------------------------------


def _make_stage_callbacks(
    fail_stage_index: Optional[int] = None,
    fail_message: Optional[str] = None,
) -> List[Tuple[str, Callable[[], str]]]:
    callbacks: List[Tuple[str, Callable[[], str]]] = []
    for idx, name in enumerate(CANONICAL_STAGE_NAMES):
        if fail_stage_index is not None and idx == fail_stage_index:
            msg = fail_message or f"injected_failure_at_{name}"

            def _fail(m: str = msg) -> str:
                raise AssertionError(m)

            callbacks.append((name, _fail))
        else:
            callbacks.append((name, lambda n=name: f"STAGE_OK {n}"))
    return callbacks


def run_r03_honest_failure_phase_reporting_adapter() -> List[str]:
    require_eq(
        PHASE_STATES,
        (
            "AUDIT",
            "WITNESS_BUILDING",
            "COMPARISON_STARTED",
            "COMPARISON_FAILED",
            "COMPLETED",
        ),
        "R03.phase_states",
    )
    app_keys_before = tuple(sorted(app.__dict__.keys()))

    def _witness_ok() -> str:
        return "WITNESS_OK count=6"

    def _witness_fail() -> str:
        raise AssertionError("H3.injected_witness_failure: expected=6, actual=5")

    def _compare_ok() -> Tuple[str, int, str]:
        return (EXPECTED_DOMAIN_SHA256, EXPECTED_COMPARE_RECORDS, EXPECTED_COMPARE_DIGEST)

    def _compare_bad_count() -> Tuple[str, int, str]:
        return (EXPECTED_DOMAIN_SHA256, 1199, EXPECTED_COMPARE_DIGEST)

    def _compare_bad_digest() -> Tuple[str, int, str]:
        return (EXPECTED_DOMAIN_SHA256, EXPECTED_COMPARE_RECORDS, "0" * 64)

    scenarios = (
        (
            "H1_AUDIT_MID_STAGE_T11_FAIL",
            _make_stage_callbacks(
                10, "H1.injected_audit_failure: expected=True, actual=False"
            ),
            _witness_ok,
            _compare_ok,
            "AUDIT",
            "run_t11_direct_chronological_and_source_readers",
            "H1.injected_audit_failure: expected=True, actual=False",
            "FAIL",
            "NOT_RUN",
            "NOT_RUN",
            "NOT_RUN",
            11,
            False,
            False,
            False,
            1,
        ),
        (
            "H2_AUDIT_FINAL_STAGE_T19_FAIL",
            _make_stage_callbacks(
                18, "H2.injected_t19_failure: expected=450, actual=449"
            ),
            _witness_ok,
            _compare_ok,
            "AUDIT",
            "run_t19_typed_record_factorization",
            "H2.injected_t19_failure: expected=450, actual=449",
            "FAIL",
            "NOT_RUN",
            "NOT_RUN",
            "NOT_RUN",
            19,
            False,
            False,
            False,
            1,
        ),
        (
            "H3_WITNESS_BUILDING_FAIL",
            _make_stage_callbacks(),
            _witness_fail,
            _compare_ok,
            "WITNESS_BUILDING",
            "witness_boundary_trajectories",
            "H3.injected_witness_failure: expected=6, actual=5",
            "PASS",
            "FAIL",
            "NOT_RUN",
            "NOT_RUN",
            19,
            True,
            False,
            False,
            1,
        ),
        (
            "H4_COMPARISON_COUNT_MISMATCH",
            _make_stage_callbacks(),
            _witness_ok,
            _compare_bad_count,
            "COMPARISON_FAILED",
            "full_state_comparison",
            "COMPARISON.count: expected=1200, actual=1199",
            "PASS",
            "PASS",
            "FAIL",
            "NONE",
            19,
            True,
            True,
            False,
            1,
        ),
        (
            "H5_COMPARISON_DIGEST_MISMATCH",
            _make_stage_callbacks(),
            _witness_ok,
            _compare_bad_digest,
            "COMPARISON_FAILED",
            "full_state_comparison",
            "COMPARISON.unchanged_I2_V2_state_stream: "
            f"expected={EXPECTED_COMPARE_DIGEST!r}, actual={'0' * 64!r}",
            "PASS",
            "PASS",
            "FAIL",
            "NONE",
            19,
            True,
            True,
            False,
            1,
        ),
        (
            "H6_COMPLETED_POSITIVE_CONTROL",
            _make_stage_callbacks(),
            _witness_ok,
            _compare_ok,
            "COMPLETED",
            None,
            None,
            "PASS",
            "PASS",
            "PASS",
            "NONE",
            19,
            True,
            True,
            True,
            0,
        ),
    )

    out_lines: List[str] = []
    for (
        scen_id,
        stages,
        w_fn,
        c_fn,
        exp_phase,
        exp_failed_stage,
        exp_err,
        exp_audit,
        exp_witness,
        exp_comp,
        exp_rem,
        exp_exec_len,
        exp_w_called,
        exp_c_called,
        exp_marker,
        exp_strict_exit,
    ) in scenarios:
        rep = run_reporting_adapter(
            stages,
            w_fn,
            c_fn,
            expected_domain_sha=EXPECTED_DOMAIN_SHA256,
            expected_count=EXPECTED_COMPARE_RECORDS,
            expected_digest=EXPECTED_COMPARE_DIGEST,
        )
        require_eq(rep.phase_state, exp_phase, f"R03.{scen_id}.phase_state")
        require_eq(
            rep.first_failed_stage, exp_failed_stage, f"R03.{scen_id}.first_failed_stage"
        )
        require_eq(rep.original_error, exp_err, f"R03.{scen_id}.original_error")
        require_eq(rep.audit_status, exp_audit, f"R03.{scen_id}.audit_status")
        require_eq(rep.witness_status, exp_witness, f"R03.{scen_id}.witness_status")
        require_eq(rep.comparison_status, exp_comp, f"R03.{scen_id}.comparison_status")
        require_eq(
            rep.remaining_dependent_checks,
            exp_rem,
            f"R03.{scen_id}.remaining_dependent_checks",
        )
        require_eq(
            len(rep.executed_stages), exp_exec_len, f"R03.{scen_id}.executed_stages_len"
        )
        require_eq(rep.witness_called, exp_w_called, f"R03.{scen_id}.witness_called")
        require_eq(
            rep.comparison_called, exp_c_called, f"R03.{scen_id}.comparison_called"
        )
        require_eq(
            rep.completion_marker_emitted,
            exp_marker,
            f"R03.{scen_id}.completion_marker_emitted",
        )
        require_eq(
            ADAPTER_COMPLETION_MARKER in rep.emitted_lines,
            exp_marker,
            f"R03.{scen_id}.marker_in_lines",
        )
        require_eq(
            rep.strict_exit_code, exp_strict_exit, f"R03.{scen_id}.strict_exit_code"
        )
        require_eq(
            rep.harness_replay_exit_code,
            0,
            f"R03.{scen_id}.harness_replay_exit_code",
        )
        if exp_marker:
            require_eq(
                rep.emitted_lines[-1],
                ADAPTER_COMPLETION_MARKER,
                f"R03.{scen_id}.terminal_marker_line",
            )
        else:
            require_true(
                rep.emitted_lines[-2].startswith(
                    f"FALSIFIER phase={exp_phase} stage={exp_failed_stage} "
                ),
                f"R03.{scen_id}.falsifier_line_prefix",
            )
            require_eq(
                rep.emitted_lines[-1],
                f"ADAPTER_DIAGNOSTIC phase_state={exp_phase} audit={exp_audit} "
                f"witnesses={exp_witness} comparison={exp_comp} "
                f"remaining_dependent_checks={exp_rem}",
                f"R03.{scen_id}.diagnostic_line",
            )
        out_lines.append(
            f"HARNESS_SCENARIO id={scen_id} phase_state={rep.phase_state} "
            f"first_failed_stage={rep.first_failed_stage} audit={rep.audit_status} "
            f"witnesses={rep.witness_status} comparison={rep.comparison_status} "
            f"remaining={rep.remaining_dependent_checks} "
            f"completion_marker={rep.completion_marker_emitted} strict_exit={rep.strict_exit_code}"
        )

    app_keys_after = tuple(sorted(app.__dict__.keys()))
    require_eq(app_keys_after, app_keys_before, "R03.app_module_namespace_unchanged")
    post_local, post_upstream = _verify_pre_import_custody()
    require_eq((post_local, post_upstream), (4, 19), "R03.post_harness_custody")
    out_lines.append(
        "R03 PASS: harness_scenarios=6/6 witness_separated_from_T19=TRUE "
        "post_start_comparison_mismatch=FAIL not_started_comparison=NOT_RUN "
        "failed_emits_completion_marker=FALSE"
    )
    return out_lines


# ---------------------------------------------------------------------------
# Gate R04: Static AST isolation & non-interference verification
# ---------------------------------------------------------------------------


def run_r04_static_isolation_and_non_interference() -> List[str]:
    adapter_source = (
        inspect.getsource(AdapterReport) + "\n" + inspect.getsource(run_reporting_adapter)
    )
    adapter_tree = ast.parse(adapter_source)

    forbidden_dynamical_names = {
        "app",
        "CompositeState",
        "WaveTapeState",
        "ApparatusSubstate",
        "u",
        "v",
        "A0",
        "A1",
        "B0",
        "B1",
        "x_A",
        "x_B",
        "p_A",
        "p_B",
        "F_step",
        "F_inverse",
        "H_B_step",
        "native_tick_single",
        "native_selector",
        "prepare_ready_state",
        "run_seven_steps",
        "run_eight_steps",
    }

    imports_in_adapter = [
        node
        for node in ast.walk(adapter_tree)
        if isinstance(node, (ast.Import, ast.ImportFrom))
    ]
    require_eq(len(imports_in_adapter), 0, "R04.adapter_zero_imports")

    attr_stores_in_adapter = [
        node.attr
        for node in ast.walk(adapter_tree)
        if isinstance(node, ast.Attribute) and isinstance(node.ctx, ast.Store)
    ]
    require_eq(attr_stores_in_adapter, [], "R04.adapter_zero_attribute_stores")

    referenced_names_in_adapter = {
        node.id for node in ast.walk(adapter_tree) if isinstance(node, ast.Name)
    } | {
        node.attr for node in ast.walk(adapter_tree) if isinstance(node, ast.Attribute)
    }
    adapter_forbidden_hits = sorted(
        referenced_names_in_adapter & forbidden_dynamical_names
    )
    require_eq(adapter_forbidden_hits, [], "R04.adapter_zero_dynamical_or_head_refs")

    # Also verify on upstream apparatus.py that DirectPortReadout, decode_port_vectors,
    # and direct_source_reader have zero references to native heads or state transitions.
    app_source = (UPSTREAM_DIR / "apparatus.py").read_text(encoding="utf-8")
    app_tree = ast.parse(app_source)
    target_nodes: Dict[str, ast.AST] = {}
    for node in app_tree.body:
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)) and node.name in {
            "DirectPortReadout",
            "decode_port_vectors",
            "direct_source_reader",
        }:
            target_nodes[node.name] = node
    require_eq(
        sorted(target_nodes.keys()),
        ["DirectPortReadout", "decode_port_vectors", "direct_source_reader"],
        "R04.upstream_readout_nodes_present",
    )

    forbidden_in_readout = {
        "x_A",
        "x_B",
        "p_A",
        "p_B",
        "F_step",
        "F_inverse",
        "H_B_step",
        "native_tick_single",
        "native_selector",
        "prepare_ready_state",
        "run_seven_steps",
        "run_eight_steps",
    }
    for name, node in target_nodes.items():
        refs = {
            sub.id for sub in ast.walk(node) if isinstance(sub, ast.Name)
        } | {
            sub.attr for sub in ast.walk(node) if isinstance(sub, ast.Attribute)
        }
        hits = sorted(refs & forbidden_in_readout)
        require_eq(hits, [], f"R04.upstream_{name}_no_native_or_transition_refs")

    return [
        "R04 PASS: adapter_imports=0 adapter_attr_stores=0 adapter_dynamical_or_head_refs=0 "
        "upstream_readout_native_or_transition_refs=0"
    ]


def main(argv: Sequence[str]) -> int:
    if len(argv) != 1:
        sys.stderr.write(f"Usage: {argv[0]}\n")
        return 2
    print("P-TWO-USE-READOUT-FAILURE-REGRESSION-1 AUDIT START")
    for runner in (
        run_r01_custody_and_historical_verifier_ast,
        run_r02_semantic_rejections_and_positive_controls,
        run_r03_honest_failure_phase_reporting_adapter,
        run_r04_static_isolation_and_non_interference,
    ):
        for line in runner():
            print(line)
    print(
        "P-TWO-USE-READOUT-FAILURE-REGRESSION-1 AUDIT PASS: "
        "gates=4/4 semantic_rejections=5/5 positive_controls=5/5 "
        "harness_scenarios=6/6 upstream_modified=0 status=ALL_PASS"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
