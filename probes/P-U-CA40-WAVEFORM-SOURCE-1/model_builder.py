#!/usr/bin/env python3
"""Frozen-theory waveform construction; stdlib only. Never runs on import.

This is an engineering floating-point model, not an exact verifier or an
apparatus calibration. The first numerical call belongs after the public pin.
"""
import argparse
import cmath
import json
import math
from pathlib import Path


DEFAULTS = {
    "ions": 7, "segments": 16, "cycles": 5,
    "axial_hz": 1_000_000.0, "beatnote_offset_hz": 20_000.0,
    "loop_seconds": 100e-6, "wavelength_m": 397e-9,
    "mass_kg": 40.0 * 1.66053906660e-27,
    "hbar_Js": 1.054571817e-34,
    "elementary_charge_C": 1.602176634e-19,
    "epsilon0_F_per_m": 8.8541878128e-12,
    "peak_drive_cap_rad_s": 2.0 * math.pi * 5e6,
    "nbar": 0.05,
    "newton_gradient_tolerance": 5e-13,
    "jacobi_relative_tolerance": 2e-15,
    "closure_rank_tolerance": 1e-10,
    "closure_rank_margin": 1e-8,
    "null_residual_tolerance": 1e-11,
    "phase_nonzero_relative_tolerance": 1e-10,
}


class ModelIncomplete(RuntimeError):
    pass


def dot(a, b):
    return math.fsum(x * y for x, y in zip(a, b))


def norm(a):
    return math.sqrt(max(0.0, dot(a, a)))


def matvec(a, x):
    return [dot(row, x) for row in a]


def quadratic(a, x):
    return dot(x, matvec(a, x))


def coulomb_potential(x):
    return 0.5 * dot(x, x) + math.fsum(
        1.0 / (x[j] - x[i]) for i in range(len(x))
        for j in range(i + 1, len(x)))


def coulomb_derivatives(x):
    n = len(x)
    g = x[:]
    h = [[float(i == j) for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            d = x[j] - x[i]
            if d <= 0:
                raise ModelIncomplete("Ion order lost")
            inv2, inv3 = 1.0 / (d * d), 2.0 / (d * d * d)
            g[i] += inv2
            g[j] -= inv2
            h[i][i] += inv3
            h[j][j] += inv3
            h[i][j] -= inv3
            h[j][i] -= inv3
    return g, h


def solve_spd(a, rhs):
    n = len(rhs)
    l = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1):
            t = a[i][j] - math.fsum(l[i][k] * l[j][k] for k in range(j))
            if i == j:
                if t <= 0:
                    raise ModelIncomplete("Nonpositive Newton Hessian pivot")
                l[i][j] = math.sqrt(t)
            else:
                l[i][j] = t / l[j][j]
    y = [0.0] * n
    for i in range(n):
        y[i] = (rhs[i] - math.fsum(l[i][k] * y[k] for k in range(i))) / l[i][i]
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - math.fsum(l[k][i] * x[k] for k in range(i + 1, n))) / l[i][i]
    return x


def equilibrium(cfg):
    x = [float(i - 3) for i in range(7)]
    for iteration in range(100):
        g, h = coulomb_derivatives(x)
        residual = max(map(abs, g))
        if residual <= cfg["newton_gradient_tolerance"]:
            return x, h, {"iterations": iteration, "gradient_inf": residual}
        step = solve_spd(h, [-v for v in g])
        old_v, slope = coulomb_potential(x), dot(g, step)
        accepted = False
        for backtrack in range(60):
            scale = 2.0 ** (-backtrack)
            trial = [v + scale * d for v, d in zip(x, step)]
            # The solution is reflection symmetric. This fixed projection
            # suppresses roundoff drift; it is not fitted to run results.
            trial = [0.5 * (trial[i] - trial[6 - i]) for i in range(7)]
            if any(trial[i] >= trial[i + 1] for i in range(6)):
                continue
            trial_g, _ = coulomb_derivatives(trial)
            armijo = coulomb_potential(trial) <= old_v + 1e-4 * scale * slope
            roundoff_descent = (residual < 1e-7 and
                                max(map(abs, trial_g)) < residual)
            if armijo or roundoff_descent:
                x, accepted = trial, True
                break
        if not accepted:
            raise ModelIncomplete("Newton line search stalled")
    raise ModelIncomplete("Newton iteration cap")


def symmetric_eigen(a, tolerance):
    """Maximum-pivot Jacobi; ties resolved by increasing index order."""
    n = len(a)
    b = [row[:] for row in a]
    v = [[float(i == j) for j in range(n)] for i in range(n)]
    scale = max(max(map(abs, row)) for row in b)
    if scale == 0:
        return [0.0] * n, [[float(i == j) for i in range(n)] for j in range(n)]
    for _ in range(100 * n * n):
        p, q = max(((i, j) for i in range(n) for j in range(i + 1, n)),
                   key=lambda ij: abs(b[ij[0]][ij[1]]))
        if abs(b[p][q]) <= tolerance * scale:
            break
        tau = (b[q][q] - b[p][p]) / (2.0 * b[p][q])
        t = math.copysign(1.0, tau) / (abs(tau) + math.hypot(1.0, tau))
        c, s = 1.0 / math.sqrt(1.0 + t * t), 0.0
        s = t * c
        app, aqq, apq = b[p][p], b[q][q], b[p][q]
        b[p][p], b[q][q] = app - t * apq, aqq + t * apq
        b[p][q] = b[q][p] = 0.0
        for k in range(n):
            if k != p and k != q:
                kp, kq = b[k][p], b[k][q]
                b[k][p] = b[p][k] = c * kp - s * kq
                b[k][q] = b[q][k] = s * kp + c * kq
            vp, vq = v[k][p], v[k][q]
            v[k][p], v[k][q] = c * vp - s * vq, s * vp + c * vq
    else:
        raise ModelIncomplete("Jacobi iteration cap")
    values, vectors = [], []
    for j in sorted(range(n), key=lambda j: (b[j][j], j)):
        vec = [v[i][j] for i in range(n)]
        anchor = max(range(n), key=lambda i: abs(vec[i]))
        if vec[anchor] < 0:
            vec = [-x for x in vec]
        values.append(b[j][j])
        vectors.append(vec)
    return values, vectors


def orthogonal_residual(v, basis):
    out = v[:]
    for _ in range(2):
        for q in basis:
            c = dot(out, q)
            out = [x - c * y for x, y in zip(out, q)]
    return out


def closure_nullspace(rows, cfg):
    normalized = []
    for row in rows:
        size = norm(row)
        if not size > 0:
            raise ModelIncomplete("Zero closure row")
        normalized.append([x / size for x in row])
    remaining, basis, pivots = list(range(14)), [], []
    while remaining:
        residuals = [(j, orthogonal_residual(normalized[j], basis)) for j in remaining]
        j, residual = max(residuals, key=lambda item: norm(item[1]))
        size = norm(residual)
        if size <= cfg["closure_rank_tolerance"]:
            raise ModelIncomplete("Closure rank below 14")
        pivots.append(size)
        basis.append([x / size for x in residual])
        remaining.remove(j)
    if min(pivots) < cfg["closure_rank_margin"]:
        raise ModelIncomplete("Closure rank insufficiently separated from tolerance")
    null = []
    for _ in range(2):
        choices = []
        for j in range(16):
            e = [float(i == j) for i in range(16)]
            choices.append(orthogonal_residual(e, basis + null))
        residual = max(choices, key=norm)
        size = norm(residual)
        if size < cfg["closure_rank_margin"]:
            raise ModelIncomplete("Nullspace complement degenerate")
        null.append([x / size for x in residual])
    error = max(abs(dot(row, q)) for row in normalized for q in null)
    if error > cfg["null_residual_tolerance"]:
        raise ModelIncomplete("Closure nullspace residual exceeds threshold")
    return null, {"rank": 14, "nullity": 2, "normalized_row_pivots": pivots,
                  "normalized_null_residual": error,
                  "rank_tolerance": cfg["closure_rank_tolerance"],
                  "rank_margin": cfg["closure_rank_margin"]}


def sinc(x):
    if abs(x) < 1e-4:
        y = x * x
        return 1.0 + y * (-1.0 / 6.0 + y * (1.0 / 120.0 - y / 5040.0))
    return math.sin(x) / x


def segment_integral(delta, start, duration):
    return duration * sinc(delta * duration / 2.0) * cmath.exp(
        1j * delta * (start + duration / 2.0))


def segment_self_phase(delta, duration):
    x = delta * duration
    if abs(x) < 1e-3:
        return duration * duration * x * (1.0 / 6.0 + x * x *
               (-1.0 / 120.0 + x * x * (1.0 / 5040.0 - x * x / 362880.0)))
    return duration * duration * (x - math.sin(x)) / (x * x)


def loop_phase_matrix(delta, duration, segments):
    dt = duration / segments
    ints = [segment_integral(delta, k * dt, dt) for k in range(segments)]
    q = [[0.0] * segments for _ in range(segments)]
    for k in range(segments):
        q[k][k] = segment_self_phase(delta, dt)
        for j in range(k):
            q[k][j] = q[j][k] = 0.5 * (ints[k] * ints[j].conjugate()).imag
    return ints, q


def make_modes(cfg):
    x, hessian, diagnostic = equilibrium(cfg)
    values, vectors = symmetric_eigen(hessian, cfg["jacobi_relative_tolerance"])
    residual = max(abs(y - val * x) for val, vec in zip(values, vectors)
                   for x, y in zip(vec, matvec(hessian, vec)))
    orthogonality = max(abs(dot(a, b) - float(i == j))
                        for i, a in enumerate(vectors) for j, b in enumerate(vectors))
    if min(values) <= 0 or residual > 1e-10 or orthogonality > 1e-12:
        raise ModelIncomplete("Axial eigensystem validation failed")
    omega_z = 2.0 * math.pi * cfg["axial_hz"]
    length = (cfg["elementary_charge_C"] ** 2 /
              (4.0 * math.pi * cfg["epsilon0_F_per_m"] * cfg["mass_kg"] * omega_z ** 2)) ** (1.0 / 3.0)
    frequencies = [omega_z * math.sqrt(v) for v in values]
    delta_k = 2.0 * math.pi / cfg["wavelength_m"]
    eta = [[delta_k * component * math.sqrt(cfg["hbar_Js"] /
            (2.0 * cfg["mass_kg"] * omega)) * cmath.exp(1j * delta_k * length * x[i])
            for i, component in enumerate(vec)] for omega, vec in zip(frequencies, vectors)]
    diagnostic.update({"eigen_residual_inf": residual,
                       "eigen_orthogonality_inf": orthogonality})
    return {"positions_dimensionless": x, "length_scale_m": length,
            "positions_m": [length * u for u in x],
            "hessian_dimensionless": hessian, "eigenvalues": values,
            "vectors_by_mode": vectors, "omega_rad_s": frequencies,
            "eta_by_mode_ion": [[[z.real, z.imag] for z in row] for row in eta],
            "diagnostics": diagnostic}


def complex_eta(modes):
    return [[complex(*z) for z in row] for row in modes["eta_by_mode_ion"]]


def make_pulses(cfg, modes):
    mu = 2.0 * math.pi * (cfg["axial_hz"] + cfg["beatnote_offset_hz"])
    deltas = [w - mu for w in modes["omega_rad_s"]]
    matrices, rows = [], []
    for delta in deltas:
        integrals, q = loop_phase_matrix(delta, cfg["loop_seconds"], 16)
        rows.extend([[z.real for z in integrals], [z.imag for z in integrals]])
        matrices.append(q)
    null, diagnostic = closure_nullspace(rows, cfg)
    pair = [[math.fsum(2.0 * (eta[3] * eta[4].conjugate()).real * q[k][j]
                      for eta, q in zip(complex_eta(modes), matrices))
             for j in range(16)] for k in range(16)]
    projected = [[dot(a, matvec(pair, b)) for b in null] for a in null]
    vals, vecs = symmetric_eigen(projected, cfg["jacobi_relative_tolerance"])
    selected = max(range(2), key=lambda j: abs(vals[j]))
    scale = max(norm(row) for row in pair)
    if scale == 0 or abs(vals[selected]) <= cfg["phase_nonzero_relative_tolerance"] * scale:
        raise ModelIncomplete("Closed-envelope pair phase is zero or ill-conditioned")
    shape = [math.fsum(vecs[selected][j] * null[j][k] for j in range(2))
             for k in range(16)]
    shape_norm = norm(shape)
    shape = [x / shape_norm for x in shape]
    anchor = max(range(16), key=lambda j: abs(shape[j]))
    if shape[anchor] < 0:
        shape = [-x for x in shape]
    beta_unit = quadratic(pair, shape)
    optical_cos = math.cos((2.0 * math.pi / cfg["wavelength_m"]) *
                          (modes["positions_m"][3] - modes["positions_m"][4]))
    if abs(optical_cos) < 1e-8:
        raise ModelIncomplete("Pair optical spatial phase cancels interaction")
    diagnostic.update({"pair_optical_phase_cosine": optical_cos,
                       "projected_pair_phase_eigenvalues_s2": vals,
                       "selected_eigenvalue_index": selected,
                       "unit_l2_pair_phase_s2": beta_unit,
                       "shape_l2_squared": dot(shape, shape),
                       "shape_closure_integral_abs_s": max(abs(complex(dot(rows[2*m], shape),
                           dot(rows[2*m+1], shape))) for m in range(7))})
    pulses = []
    for sign in (1, -1):
        theta = sign * 4.0 * math.pi / 5.0
        beta_target = (-theta) % (2.0 * math.pi)
        if beta_unit < 0:
            beta_target -= 2.0 * math.pi
        amplitude = math.sqrt(beta_target / beta_unit)
        waveform = [amplitude * a for a in shape]
        peak = max(map(abs, waveform))
        if peak > cfg["peak_drive_cap_rad_s"]:
            raise ModelIncomplete("Required drive exceeds declared theoretical cap")
        pulses.append({"sign": sign, "theta_rad": theta,
                       "beta_target_rad": beta_target,
                       "unit_l2_shape": shape[:], "scale_rad_s": amplitude,
                       "amplitudes_rad_s": waveform, "peak_abs_rad_s": peak,
                       "rms_rad_s": amplitude / 4.0,
                       "loop_l2_integral_rad2_per_s": amplitude * amplitude * cfg["loop_seconds"] / 16.0,
                       "loop_seconds": cfg["loop_seconds"], "segments": 16,
                       "block_seconds": 5.0 * cfg["loop_seconds"]})
    return pulses, diagnostic


def frozen_contexts(cfg):
    return [
        {"id": "nominal", "detuning_shift_rad_s": 0.0, "amplitude_factor": 1.0,
         "spectator_differential": 0.0, "nbar": cfg["nbar"]},
        {"id": "detuning_plus_100Hz", "detuning_shift_rad_s": 2.0 * math.pi * 100.0,
         "amplitude_factor": 1.0, "spectator_differential": 0.0, "nbar": cfg["nbar"]},
        {"id": "amplitude_plus_0p5percent", "detuning_shift_rad_s": 0.0,
         "amplitude_factor": 1.005, "spectator_differential": 0.0, "nbar": cfg["nbar"]},
        {"id": "hidden_D_differential", "detuning_shift_rad_s": 0.0,
         "amplitude_factor": 1.0, "spectator_differential": 0.002, "nbar": cfg["nbar"]},
    ]


def cycle_profiles(cycle, context, arm):
    """Physical S response is 1; active D response is 0.

    Spectator logical 0 is parked in auxiliary a throughout. In sham E,
    other spectator levels undergo the (incorrect) global 0..4 X5 echo.
    The differential D perturbation applies to spectators only.
    """
    profiles = []
    for ion in range(7):
        if ion in (3, 4):
            profiles.append([float((label + cycle) % 5 == 0) for label in range(5)])
        else:
            epsilon = context["spectator_differential"]
            if arm == "E":
                row = [-2.0 * epsilon]
                for label in range(1, 5):
                    physical = (label + cycle) % 5
                    row.append(1.0 if physical == 0 else epsilon * (physical - 2))
                profiles.append(row)
            else:
                profiles.append([epsilon * (label - 2) for label in range(5)])
    return profiles


def feature_force(eta, profiles):
    """Features [1, x_1,1,...,x_7,4]; x_i,l is original-label indicator."""
    common = sum((eta[i] * profiles[i][0] for i in range(7)), 0j)
    return [common] + [
        eta[i] * (profiles[i][label] - profiles[i][0])
        for i in range(7) for label in range(1, 5)]


def loop_response(delta, amplitudes, duration):
    """Unit-profile displacement and phase of the actual 16-segment loop."""
    dt, displacement, phase = duration / 16.0, 0j, 0.0
    for k, amplitude in enumerate(amplitudes):
        increment = -1j * amplitude * segment_integral(delta, k * dt, dt)
        phase += amplitude * amplitude * segment_self_phase(delta, dt)
        phase += (increment * displacement.conjugate()).imag
        displacement += increment
    return displacement, phase


def coefficient_table(cfg, modes, pulse, context, arm="G"):
    """Factor each loop, then retain every inter-cycle Weyl cross term.

    No motion reset occurs. Independent validation must use the full 80
    absolute-time segments, not call this factored calculation again.
    """
    if arm not in ("G", "E", "I"):
        raise ValueError("Unknown arm")
    mu = 2.0 * math.pi * (cfg["axial_hz"] + cfg["beatnote_offset_hz"])
    deltas = [w - mu + context["detuning_shift_rad_s"] for w in modes["omega_rad_s"]]
    amplitudes = [u * context["amplitude_factor"] if arm != "I" else 0.0
                  for u in pulse["amplitudes_rad_s"]]
    if max(map(abs, amplitudes)) > cfg["peak_drive_cap_rad_s"]:
        raise ModelIncomplete("Stress-context drive exceeds declared theoretical cap")
    profiles = [cycle_profiles(cycle, context, arm) for cycle in range(5)]
    alpha = []
    phase = [[0.0] * 29 for _ in range(29)]
    loop_responses = []
    for mode, eta in enumerate(complex_eta(modes)):
        delta = deltas[mode]
        loop_displacement, loop_phase = loop_response(delta, amplitudes, cfg["loop_seconds"])
        loop_responses.append({"alpha": [loop_displacement.real, loop_displacement.imag],
                               "phi": loop_phase})
        cumulative = [0j] * 29
        for cycle in range(5):
            force = feature_force(eta, profiles[cycle])
            common = loop_displacement * cmath.exp(1j * delta * cycle * cfg["loop_seconds"])
            increment = [common * x for x in force]
            for f in range(29):
                for g in range(f, 29):
                    phase[f][g] += loop_phase * (force[f] * force[g].conjugate()).real + 0.5 * (
                        increment[f] * cumulative[g].conjugate() +
                        increment[g] * cumulative[f].conjugate()).imag
            cumulative = [x + y for x, y in zip(cumulative, increment)]
        alpha.append(cumulative)
    unary = [[0.0] + [2.0 * phase[0][1 + 4 * i + l] + phase[1 + 4 * i + l][1 + 4 * i + l]
              for l in range(4)] for i in range(7)]
    pairs = [{"ions_zero_based": [i, j], "values": [[0.0] * 5] + [
                 [0.0] + [2.0 * phase[1 + 4 * i + a][1 + 4 * j + b] for b in range(4)]
                 for a in range(4)]}
             for i in range(7) for j in range(i + 1, 7)]
    table = {"alpha_common": [[v[0].real, v[0].imag] for v in alpha],
            "alpha": [[[[0.0, 0.0]] + [[v[1+4*i+l].real, v[1+4*i+l].imag] for l in range(4)]
                             for i in range(7)] for v in alpha],
            "phi_common_raw": phase[0][0], "phi_unary": unary, "phi_pair": pairs,
            "endpoint_permutation": "identity_on_all_seven_labels",
            "duration_seconds": 5.0 * cfg["loop_seconds"]}
    return table, {"delta_rad_s": deltas, "profiles": profiles,
                   "applied_amplitudes_rad_s": amplitudes,
                   "loop_responses_by_mode": loop_responses}


def build_model(config=None):
    cfg = dict(DEFAULTS)
    if config:
        unknown = set(config) - set(cfg)
        if unknown:
            raise ValueError("Unknown config keys: " + ", ".join(sorted(unknown)))
        cfg.update(config)
    if (cfg["ions"], cfg["segments"], cfg["cycles"]) != (7, 16, 5):
        raise ValueError("This frozen construction requires 7 ions, 16 segments, 5 cycles")
    for key, value in cfg.items():
        if not isinstance(value, (float, int)) or not math.isfinite(value) or value <= 0:
            raise ValueError("Config must contain positive finite numbers: " + key)
    result = {"schema": "ca40-waveform-model-v1", "status": "INCOMPLETE",
              "scope": "declared_harmonic_axial_theory_only", "config": cfg,
              "assumptions": ["Seven axial harmonic modes; radial modes omitted",
                  "eta includes traveling-wave phase exp(i Delta_k x_i); no phase compensation",
                  "Ideal instantaneous carrier permutations; no heating, scattering or decay",
                  "Ca40 mass approximated by exactly 40 times declared atomic mass unit",
                  "5 MHz drive cap is hypothetical, not measured optical calibration",
                  "Stress contexts use the frozen nominal waveform without redesign"],
              "active_ions_one_based": [4, 5],
              "spectator_ions_one_based": [1, 2, 3, 6, 7],
              "source_ions_one_based": [1, 6, 7]}
    try:
        modes = make_modes(cfg)
        result["modes"] = modes
        pulses, diagnostics = make_pulses(cfg, modes)
        result.update({"pulses": pulses, "construction_diagnostics": diagnostics})
        contexts = frozen_contexts(cfg)
        result["contexts"] = contexts
        jobs = []
        for pulse in pulses:
            nominal_global = None
            for context in contexts:
                for arm in ("G", "E", "I"):
                    table, chronology = coefficient_table(cfg, modes, pulse, context, arm)
                    if context["id"] == "nominal" and arm == "G":
                        nominal_global = table["phi_common_raw"]
                    correction = nominal_global if arm != "I" else 0.0
                    table["nominal_global_correction_subtract_rad"] = correction
                    table["phi_common_corrected"] = table["phi_common_raw"] - correction
                    job = {"name": ("plus" if pulse["sign"] == 1 else "minus") + "_" + context["id"] + "_" + arm,
                           "sign": pulse["sign"], "context": context["id"], "arm": arm,
                           "theta_target_rad": pulse["theta_rad"] if arm != "I" else 0.0,
                           "nbar_by_mode": [context["nbar"]] * 7, "coefficients": table}
                    job.update(chronology)
                    jobs.append(job)
        result["jobs"] = jobs
        result["status"] = "MODEL_BUILT_NOT_VALIDATED"
    except ModelIncomplete as exc:
        result["reason"] = str(exc)
    # Reject a nonfinite derived number before any JSON is emitted.
    json.dumps(result, allow_nan=False)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, help="New JSON path; never overwrite")
    args = parser.parse_args()
    if Path(args.output).exists():
        raise FileExistsError(args.output)
    result = build_model()
    with Path(args.output).open("x", encoding="utf-8", newline="\n") as handle:
        json.dump(result, handle, sort_keys=True, indent=2, allow_nan=False)
        handle.write("\n")
    print(json.dumps({"status": result["status"], "output": args.output,
                      "reason": result.get("reason")}, sort_keys=True, allow_nan=False))
    return 0 if result["status"] == "MODEL_BUILT_NOT_VALIDATED" else 2


if __name__ == "__main__":
    raise SystemExit(main())
