#!/usr/bin/env python3
"""Exact arithmetic on frozen, rounded literature summaries, not a data fit.

NON-CANONICAL. One local execution is at most candidate-C. No NS-TILT
status change, p-value, likelihood ratio, or independent-data combination.
Original code: A. M. Thorn. SPDX-License-Identifier: Apache-2.0
"""
from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path
import re
import sys
from typing import Any

Q = Fraction
DECIMAL = re.compile(r"-?[0-9]+\.[0-9]+\Z")
ROW_IDS = ("PLANCK18", "P_ACT_DR6", "SPA_BK", "SPA_BK_DESI_DR2")


def decimal_input(value: Any) -> Q:
    if not isinstance(value, str) or not DECIMAL.fullmatch(value):
        raise ValueError("a decimal input must be a plain decimal string")
    return Q(value)


def half_last_unit(value: str) -> Q:
    decimal_input(value)
    return Q(1, 2 * 10 ** len(value.split(".")[1]))


def fixed_decimal(value: Q, places: int, upper: bool) -> str:
    """Outward rounding, including negative inputs, using integers only."""
    scale = 10 ** places
    num = value.numerator * scale
    den = value.denominator
    integer = -((-num) // den) if upper else num // den
    sign = "-" if integer < 0 else ""
    whole, part = divmod(abs(integer), scale)
    return f"{sign}{whole}.{part:0{places}d}"


def interval(lo: Q, hi: Q, places: int = 12) -> dict[str, Any]:
    if lo > hi:
        raise ValueError("reversed interval")
    low_text = fixed_decimal(lo, places, False)
    high_text = fixed_decimal(hi, places, True)
    if not (Q(low_text) <= lo <= hi <= Q(high_text)):
        raise ArithmeticError("outward rounding failed")
    return {
        "lower": str(lo), "upper": str(hi),
        "computed_outward_decimal": [low_text, high_text],
    }


def ratio_box(nlo: Q, nhi: Q, dlo: Q, dhi: Q) -> tuple[Q, Q]:
    if nlo > nhi or not (0 < dlo <= dhi):
        raise ValueError("invalid ratio box")
    corners = (nlo / dlo, nlo / dhi, nhi / dlo, nhi / dhi)
    return min(corners), max(corners)


def arithmetic_controls() -> None:
    """Same-program controls. These are not independent confirmation."""
    cases = (
        ((Q(1), Q(2), Q(2), Q(4)), (Q(1, 4), Q(1))),
        ((Q(-2), Q(-1), Q(2), Q(4)), (Q(-1), Q(-1, 4))),
        ((Q(-1), Q(1), Q(2), Q(4)), (Q(-1, 2), Q(1, 2))),
        ((Q(0), Q(0), Q(2), Q(4)), (Q(0), Q(0))),
    )
    for box, expected in cases:
        if ratio_box(*box) != expected:
            raise ArithmeticError("ratio control failed")
    for value in (Q(-1, 3), Q(0), Q(1, 3), Q(-2), Q(2)):
        interval(value, value, 6)
    if half_last_unit("0.0032") != Q(1, 20000):
        raise ArithmeticError("last-digit control failed")


def main() -> None:
    arithmetic_controls()
    raw = Path(__file__).with_name("inputs.json").read_bytes()
    data = json.loads(raw)
    if data["candidate_id"] != "C-NS-TILT-EMPIRICAL-AUDIT-N":
        raise ValueError("wrong input contract")
    p = data["prediction"]
    if p["coefficient"] != 5 or p["status"] != "H":
        raise ValueError("the fixed hypothesis must not be refitted")
    alo = decimal_input(p["inverse_alpha_lower"])
    ahi = decimal_input(p["inverse_alpha_upper"])
    if (alo, ahi) != (Q("137.0359991895"), Q("137.0359991905")):
        raise ValueError("the source enclosure changed")
    if not (5 < alo <= ahi):
        raise ValueError("invalid inverse-alpha enclosure")
    nlo, nhi = 1 - Q(5) / alo, 1 - Q(5) / ahi
    # Cross-multiplication checks independent identities, not a second audit.
    if (1 - nlo) * alo != 5 or (1 - nhi) * ahi != 5:
        raise ArithmeticError("prediction identity failed")
    rows = data["measurements"]
    if tuple(row["id"] for row in rows) != ROW_IDS:
        raise ValueError("the frozen row order or membership changed")
    results = []
    for row in rows:
        mean, width = decimal_input(row["mean"]), decimal_input(row["sigma"])
        hm, hs = half_last_unit(row["mean"]), half_last_unit(row["sigma"])
        if decimal_input(row["pivot_Mpc_inverse"]) != Q(1, 20):
            raise ValueError("unmapped comparison pivot")
        if not (0 < mean < 2 and width > hs > 0):
            raise ValueError("invalid measured summary")
        nominal = ratio_box(mean - nhi, mean - nlo, width, width)
        rounded = ratio_box(mean - hm - nhi, mean + hm - nlo,
                            width - hs, width + hs)
        if not (rounded[0] <= nominal[0] <= nominal[1] <= rounded[1]):
            raise ArithmeticError("rounding box lost the nominal interval")
        results.append({
            "id": row["id"], "measured_mean": row["mean"],
            "measured_68_percent_halfwidth": row["sigma"],
            "mean_rounding_halfunit": str(hm),
            "halfwidth_rounding_halfunit": str(hs),
            "nominal_signed_summary_distance": interval(*nominal),
            "rounding_envelope_signed_summary_distance": interval(*rounded),
        })
    result = {
        "candidate_id": data["candidate_id"],
        "status": "NON-CANONICAL; candidate-C arithmetic only",
        "hypothesis_status_unchanged": "H",
        "interpretation": "Gaussian summary diagnostic, not a rejection gate",
        "inputs_sha256": sha256(raw).hexdigest(),
        "prediction_n_star": interval(nlo, nhi, 15),
        "prediction_interval_kind": "numerical enclosure, not theory uncertainty",
        "same_program_arithmetic_controls": "PASS",
        "rows": results,
        "pooled_result": None,
        "p_value": None,
        "formal_falsification": "NOT EVALUATED",
    }
    print(json.dumps(result, indent=2, sort_keys=True, ensure_ascii=True))


if __name__ == "__main__":
    try:
        main()
    except (ValueError, KeyError, TypeError, OSError, ArithmeticError) as exc:
        print(f"AUDIT ERROR: {type(exc).__name__}: {exc}", file=sys.stderr)
        raise SystemExit(1)
