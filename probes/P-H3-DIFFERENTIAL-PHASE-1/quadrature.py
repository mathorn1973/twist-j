# SPDX-License-Identifier: Apache-2.0
"""Native phase encoding at zero material work and signed radiation controls."""

from native import cell, h3, ledger, put, reverse, step


NX, NY = 8, 8
ZERO, ONE, RHO, J = h3.ZERO, h3.ONE, h3.RHO, h3.J
PI = h3.sub(ONE, RHO)
PHI = h3.scale(-1, h3.add(RHO, h3.RHO_INV))
TARGET, REFERENCE = (0, 0), (4, 0)


def neg(word):
    return h3.scale(-1, word)


def empty():
    return [ZERO] * (4 * NX * NY)


def antipodal(word):
    return word, neg(word)


def site(field, position):
    return cell(field, NY, *position)


def record(field, position):
    r0, r2, clk, corr = site(field, position)
    material_h = h3.add(h3.h(r0), h3.h(r2))
    return {
        "words": (r0, r2, clk, corr),
        "material_h": material_h,
        "material_q": h3.scalar_account(material_h),
        "radiation_h": h3.add(h3.h(clk), h3.h(corr)),
    }


def quotient(a, b):
    return h3.mul(a, h3.inverse(b)) if b != ZERO else None


def encode(word):
    return [[v.numerator, v.denominator] for v in word] if word is not None else None


def checked(field, bit):
    c, b, tags = step(field, NY, bit)
    h3.require(reverse(b, NY, bit) == tuple(field) and ledger(c) == ledger(b) == ledger(field),
               "whole native inverse and accounts")
    return c, b, tags


def signed_launch(sign):
    field = empty()
    u = h3.mul(PI, h3.add(ONE, PI))
    r = h3.scale(2 * sign, u)
    put(field, NY, *TARGET, antipodal(PI) + antipodal(r))
    put(field, NY, *REFERENCE, antipodal(PI) + (ZERO, ZERO))
    bias = h3.scale(-4, h3.mul(J, PI))
    put(field, NY, 0, 1, (ZERO, ZERO, bias, ZERO))
    return tuple(field)


def signed_radiation():
    launches = [signed_launch(sign) for sign in (1, -1)]
    h3.require(ledger(launches[0]) == ledger(launches[1]), "matched signed-source launch")
    results = []
    j_pi = h3.mul(J, PI)
    expected_center = neg(h3.mul(PI, j_pi))
    for sign, initial in zip((1, -1), launches):
        c, b, tags = checked(initial, 0)
        clk, corr = site(c, TARGET)[2:]
        f = quotient(h3.sub(clk, corr), h3.scale(2, ONE))
        center = quotient(h3.add(clk, corr), h3.scale(2, ONE))
        expected_f = j_pi if sign == 1 else neg(h3.mul(j_pi, h3.add(ONE, h3.scale(2, PI))))
        before, after = record(c, TARGET), record(b, TARGET)
        delta_h = h3.sub(after["material_h"], before["material_h"])
        delta_field = h3.sub(after["radiation_h"], before["radiation_h"])
        reference = site(b, REFERENCE)
        ratio = quotient(site(b, TARGET)[0], reference[0])
        phase = quotient(ratio, h3.conj(ratio)) if ratio is not None else None
        expected_tags = ((0, 0, 1),) if sign == 1 else ()
        checks = {
            "branch": tags == expected_tags,
            "incident_gap_and_center": f == expected_f and center == expected_center,
            "matter_locked_before_b": site(c, TARGET)[:2] == antipodal(PI),
            "reference_fixed": reference == site(initial, REFERENCE),
            "relative_ratio": ratio == (J if sign == 1 else ONE),
            "pure_phase_coordinate": phase == (RHO if sign == 1 else ONE),
            "zero_scalar_work": before["material_q"] == after["material_q"] == 10,
            "exact_hermitian_work": delta_h == (
                h3.sub(h3.scale(2, ONE), h3.scale(4, PHI)) if sign == 1 else ZERO
            ) and delta_field == neg(delta_h),
        }
        results.append({
            "passed": all(checks.values()), "checks": checks, "sign": sign, "tags": tags,
            "incident_gap": encode(f), "incident_center": encode(center),
            "incident_h": encode(h3.h(f)) if f is not None else None,
            "before_b": before, "after_b": after, "delta_material_h": delta_h,
            "delta_radiation_h": delta_field, "reference": reference,
            "material_reference_ratio": encode(ratio), "relative_phase_squared": encode(phase),
        })
    return {"passed": all(row["passed"] for row in results), "rows": results}


def matter_launch(sign):
    field = empty()
    for row in range(4):
        value = h3.scale(2 * (sign if row == 0 else 1), ONE)
        put(field, NY, 0, row, antipodal(value) + (ZERO, ZERO))
    return tuple(field)


def hermitian_weights(field):
    return [h3.ring_sum(h3.h(word) for word in field[index:index + 2])
            for index in range(0, len(field), 4)]


def cold_phase():
    results = []
    for sign in (1, -1):
        initial = matter_launch(sign)
        c1, b1, tags1 = checked(initial, 0)
        c2, b2, tags2 = checked(b1, 1)
        target, reference = (0, 1), (0, 2)
        target_ref = quotient(site(b1, target)[0], site(b1, reference)[0])
        signals = [record(c2, position) for position in (target, reference)]
        words = tuple(signal["words"][0] for signal in signals)
        rho2 = h3.mul(RHO, RHO)
        expected = (h3.scale(2, ONE),) * 2 if sign == 1 else (
            h3.add(ONE, rho2), h3.sub(h3.add(ONE, h3.scale(2, RHO)), rho2))
        weights = [signal["material_q"] for signal in signals]
        checks = {
            "all_site_hermitian_weights_retained_at_encoding": (
                hermitian_weights(initial) == hermitian_weights(c1) == hermitian_weights(b1)
            ),
            "phase_ratio": target_ref == (ONE if sign == 1 else RHO),
            "no_b": c1 == b1 and c2 == b2 and not tags1 and not tags2,
            "read_words": words == expected,
            "read_weights": weights == ([16, 16] if sign == 1 else [6, 26]),
        }
        results.append({
            "passed": all(checks.values()), "checks": checks, "sign_at_row_zero": sign,
            "encoded_ratio": encode(target_ref), "read_site_weights": weights,
            "read_site_words": words,
        })
    return {"passed": all(row["passed"] for row in results), "rows": results}


def transform(field, unit, center):
    return tuple(h3.add(h3.mul(unit, word), center) if i % 4 >= 2 else word
                 for i, word in enumerate(field))


def global_controls():
    results = []
    for label, unit, center in (("GLOBAL_SIGN", neg(ONE), ZERO),
                                ("GLOBAL_SIGN_WITH_OFFSET", neg(ONE), PI),
                                ("GLOBAL_UNIT_PHASE_WITH_OFFSET", RHO, h3.ONE)):
        origin = signed_launch(1)
        transformed = transform(origin, unit, center)
        comparisons = []
        for tick in range(1, 7):
            bit = (tick - 1) % 2
            c, b, tags = checked(origin, bit)
            other_c, other_b, other_tags = checked(transformed, bit)
            comparisons.append({
                "tick": tick,
                "C_equivariant": other_c == transform(c, unit, center),
                "B_equivariant": other_b == transform(b, unit, center),
                "same_tags": tags == other_tags,
            })
            origin, transformed = b, other_b
        results.append({
            "label": label, "unit": unit, "offset": center, "cuts": comparisons,
            "passed": all(row[key] for row in comparisons
                          for key in ("C_equivariant", "B_equivariant", "same_tags")),
        })
    return {"passed": all(row["passed"] for row in results), "rows": results}


def run():
    signed = signed_radiation()
    cold = cold_phase()
    affine = global_controls()
    return {"passed": signed["passed"] and cold["passed"] and affine["passed"],
            "geometry": [NX, NY], "signed_reference": signed,
            "cold_phase": cold, "global_affine_controls": affine}
