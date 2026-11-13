#!/usr/bin/env python3
"""Exact, exposed-source j/inverse-j audit of the unchanged two-use receiver.

PUBLIC / NON-CANONICAL / L1. A. M. Thorn, Apache-2.0.
The apparatus is imported unchanged after custody checks, not reimplemented.
"""

from dataclasses import asdict
from fractions import Fraction as Q
import hashlib
import importlib.util
from itertools import product
import json
from pathlib import Path
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SOURCE = ROOT / "probes/P-TWO-USE-TYPED-READOUT-CLOSURE-1"
DEPENDENCIES = {
    "apparatus.py": "f0edfd80157c8993322a5338e88120c552908d3830fe5f9ea7536257213c6173",
    "DOMAIN.tsv": "2e9b77cf8c507b9bc6675d9a07bf8e27ad88921c72c1efc22dcf5bdb41d8a7c0",
}
PLUS = (0, 1, 0, 0)
MINUS = (4, 4, 4, 4)
CONTROL = (2, 0, 0, 0)
ONE = (1, 0, 0, 0)
ELL = (0, 1, 2, -2, -1)


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def load_apparatus():
    for name, digest in DEPENDENCIES.items():
        require(hashlib.sha256((SOURCE / name).read_bytes()).hexdigest() == digest,
                "frozen dependency changed: " + name)
    spec = importlib.util.spec_from_file_location("phase_port_source", SOURCE / "apparatus.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def mul(a, b):
    """Exact Z[t]/(1+t+t^2+t^3+t^4), coefficient order 1,t,t^2,t^3."""
    c = [0] * 7
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] += x * y
    for degree in range(6, 3, -1):
        value = c[degree]
        for offset in range(1, 5):
            c[degree - offset] -= value
    return tuple(c[:4])


def power_j(n):
    value = ONE
    for _ in range(n % 5):
        value = mul(value, PLUS)
    return value


def auto(a, k):
    out = [0] * 4
    for i, coefficient in enumerate(a):
        for l, value in enumerate(power_j(k * i)):
            out[l] += coefficient * value
    return tuple(out)


def quotient(x):
    return (sum(x) % 5, x[4], x[5])


def quotient_generator(g, v):
    z, q, r = v
    choices = ((z, q, r), (-z, -q, -r), (2-z, 1-q, -r),
               (2-z, 1-q, 1-r), (3-z, 2-q, 1-r))
    return tuple(t % 5 for t in choices[g])


def receiver(state):
    """All receiver and protocol coordinates; no hidden source pistons."""
    return (state.n, state.c, state.to_apparatus_substate())


def exact_json(value):
    if isinstance(value, Q):
        return [value.numerator, value.denominator]
    if hasattr(value, "__dataclass_fields__"):
        return exact_json(asdict(value))
    if isinstance(value, dict):
        return {key: exact_json(val) for key, val in value.items()}
    if isinstance(value, (tuple, list)):
        return [exact_json(val) for val in value]
    return value


def digest(value):
    data = json.dumps(exact_json(value), sort_keys=True, separators=(",", ":")).encode("ascii")
    return hashlib.sha256(data).hexdigest()


def emit(label, value):
    print(label + " " + json.dumps(exact_json(value), sort_keys=True, separators=(",", ":")))


def algebra():
    roots = [power_j(k) for k in range(5)]
    for k, a in enumerate(roots):
        p = tuple(c % 5 for c in a)
        require(tuple(ELL[c] for c in p) == a, "root is not its balanced lift")
        require(sum(p) % 5 == 1, "root changed augmentation")
        require(mul(a, auto(a, 4)) == ONE, "first norm differs from one")
        require(auto(mul(a, auto(a, 4)), 2) == ONE, "second norm differs from one")
        require(mul(a, auto(a, 3)) == power_j(-k), "mixed term has wrong phase")
    require(roots[1] == PLUS and tuple(ELL[x] for x in MINUS) == roots[4],
            "the declared native preparations do not represent j and j^-1")
    require(roots[1] != roots[4], "phase witness collapsed")
    # Multiplication by j fixes the augmentation modulo 5 on a basis,
    # hence on the whole residue ring by F5-linearity.
    for i in range(4):
        basis = tuple(int(l == i) for l in range(4))
        require(sum(mul(PLUS, basis)) % 5 == 1, "augmentation does not factor")
    emit("ALGEBRA", {"roots": 5, "A_B": [1, 1], "p_plus": PLUS,
                     "p_minus": MINUS, "C_plus": roots[4], "C_minus": roots[1]})


def native_factor(app):
    checks = 0
    for x in product(range(5), repeat=6):
        q = quotient(x)
        for bit in (0, 1):
            g = (q[0] + 2 * bit) % 5
            # n=0 and n=1 realize the two possible native driver bits.
            n1, actual = app.native_tick_single(bit, x)
            require(n1 == bit + 1, "native counter changed")
            require(quotient(actual) == quotient_generator(g, q),
                    "autonomous quotient mismatch")
            checks += 1
    emit("NATIVE_FACTOR", {"checkpoints": 15625, "selected_steps": checks})


def check_trajectory(app, trajectory):
    require(len(trajectory) == 8, "wrong number of boundaries")
    require([(s.n, s.c) for s in trajectory]
            == [(0,0),(1,1),(1,2),(2,3),(3,4),(3,5),(4,6),(5,7)],
            "program timing changed")
    for s in trajectory:
        require(0 <= s.b <= s.B == Q(4, 5), "stock left its interval")
        require(s.b + s.W == Q(4, 5), "stock/work account failed")
        require(app.full_classical_energy(s.X) == s.W, "wave/tape account failed")
    require(trajectory[2].sigma_A == -1 and trajectory[5].sigma_B == -1,
            "both contacts must actually accept")
    final = trajectory[-1]
    cuts = (trajectory[3].X.B0, trajectory[4].X.B0,
            trajectory[6].X.B0, trajectory[7].X.B0)
    require((final.X.A0, final.X.A1, final.X.B1, final.X.B0) == cuts,
            "actual first-use cuts did not survive the second use")
    require(any(cuts[0]) and any(cuts[2]), "record witness must be nonzero")
    port = app.extract_direct_port_readout(final, include_d=False, include_sigma_B=True)
    decoded = app.direct_source_reader(port)
    require(decoded["alpha_A"] == decoded["alpha_B"] == 1,
            "record-only reader did not report both acceptances")
    return cuts, port, decoded


def main():
    app = load_apparatus()
    print("P-J-PHASE-PORT-SEPARATION-1 exact exposed-source audit")
    algebra()
    native_factor(app)
    geometry = app.get_geometry()
    require(geometry.n_sites == 705 and geometry.wave_tape_basis_dim == 1426,
            "carrier changed")
    trajectories = {}
    readings = {}
    for label_a, pa in (("+", PLUS), ("-", MINUS)):
        for label_b, pb in (("+", PLUS), ("-", MINUS)):
            label = label_a + label_b
            ready = app.prepare_ready_state(pa, pb, Q(4, 5))
            trajectory = app.run_seven_steps(ready, return_boundaries=True)
            trajectories[label] = trajectory
            readings[label] = check_trajectory(app, trajectory)
    reference = trajectories["++"]
    for label, trajectory in trajectories.items():
        require([receiver(s) for s in trajectory] == [receiver(s) for s in reference],
                "phase became distinguishable in complete receiver: " + label)
        for s, r in zip(trajectory, reference):
            require(quotient(s.x_A) == quotient(r.x_A)
                    and quotient(s.x_B) == quotient(r.x_B), "source quotient differs")
        require(readings[label] == readings["++"], "actual record-only phase read differs")
    require(reference[0].x_A != trajectories["-+"][0].x_A,
            "source states were accidentally identified")
    require(reference[-1].x_A != trajectories["-+"][-1].x_A,
            "source distinction should remain outside this receiver")
    source = (Q(1,2), Q(0), Q(0), Q(0))
    require(app.eta_lift(app.receiver_of(reference[1].x_A)) == source,
            "phase source is not the expected nonzero input")
    require(readings["++"][2]["z_A"] == readings["++"][2]["z_B"] == source,
            "decoded source is not the actual contact source")
    emit("PHASE_RECEIVER", {"ordered_pairs": 4, "boundaries_each": 8,
          "sites": geometry.n_sites, "wave_tape_coordinates": geometry.wave_tape_basis_dim,
          "quotient_history_A": [quotient(s.x_A) for s in reference],
          "same_complete_receiver": True,
          "receiver_history_sha256": digest([receiver(s) for s in reference])})
    emit("PHASE_RECORD", {"cuts": readings["++"][0], "port": readings["++"][1],
          "decoded": readings["++"][2], "work": reference[-1].W,
          "stock": reference[-1].b, "first_cost": reference[2].W,
          "second_cost": reference[5].W-reference[4].W})

    # Change only the second source to a different existing sum class.
    control = app.run_seven_steps(app.prepare_ready_state(PLUS, CONTROL, Q(4,5)),
                                  return_boundaries=True)
    control_read = check_trajectory(app, control)
    require([receiver(s) for s in control[:2]] == [receiver(s) for s in reference[:2]],
            "control receiver must be common before the first capture")
    require(control[2].d != reference[2].d, "second-source control was not captured")
    require([s.X for s in control[:5]] == [s.X for s in reference[:5]],
            "second input changed wave/tape before its contact")
    require(control[5].X != reference[5].X, "accepted second contact has no effect")
    require(control_read[0][:2] == readings["++"][0][:2], "old records changed")
    require(control_read[0][2] != readings["++"][0][2], "second record is insensitive")
    require(control_read[2]["z_B"] == (Q(1,2), Q(1,2), Q(0), Q(0)),
            "control second-source readout failed")
    require(control_read[2]["z_A"] == source, "control changed first-source readout")
    emit("CONTROL", {"p_B": CONTROL, "first_receiver_difference_boundary": 2,
          "first_wave_difference_boundary": 5, "second_record": control_read[0][2],
          "decoded": control_read[2], "work": control[-1].W,
          "stock": control[-1].b})
    # The existing eighth row only advances the phase calendar.
    rollover = app.coupled_step(reference[-1])
    require(rollover.c == 0 and rollover.n == reference[-1].n
            and rollover.to_apparatus_substate() == reference[-1].to_apparatus_substate()
            and (rollover.x_A, rollover.x_B) == (reference[-1].x_A, reference[-1].x_B),
            "rollover unexpectedly injected a new input or renewed apparatus")
    print("CLOSURE phase-distinction=NOT_TRANSMITTED second-contact=ACCEPTED control=DISTINGUISHED")
    print("BOUNDARY fixed-U-port only; new late arrival and physical photon/mass reading NOT_ESTABLISHED")
    for name, expected in DEPENDENCIES.items():
        require(hashlib.sha256((SOURCE / name).read_bytes()).hexdigest() == expected,
                "dependency changed during execution")
    print("AUDIT PASS")


if __name__ == "__main__":
    main()
