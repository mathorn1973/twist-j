"""Audit the current-state reference reader on the frozen native family."""

from hashlib import sha256
from itertools import product
from pathlib import Path
from runpy import run_path


NATIVE_SHA256 = "8b98125d9dcd0043b098aee93d2529649a50e2a3c49e31aadd4e67e02052b308"
HORIZON = 64
MODULUS = 5
BLANK = ("BLANK",)


def require(condition, detail):
    if not condition:
        raise AssertionError(detail)


def load_frozen_native():
    path = Path(__file__).resolve().with_name("native_verify.py")
    digest = sha256(path.read_bytes()).hexdigest()
    if digest != NATIVE_SHA256:
        raise SystemExit(f"STOP: wrong SHA-256 for the frozen native verifier: {digest}")
    return run_path(str(path))


def phase_coordinates(checkpoint):
    p1, p4, p1p, p4p, _, _ = checkpoint
    return p1 + p1p, p1 - p1p - 2, p4 + p4p, p4 - p4p - 1


def read_reference(checkpoint):
    """Use only current coordinates. The native clock is outside the interface."""
    if sum(checkpoint) % MODULUS not in (1, 4):
        return BLANK
    a, c, b, d = phase_coordinates(checkpoint)
    receiver_sum = a * b
    receiver_difference = 3 * c * d
    r1 = 3 * (receiver_sum + receiver_difference + 1) % MODULUS
    r4 = 3 * (receiver_sum - receiver_difference - 1) % MODULUS
    return "PRESENT", r1, r4


def audit_zero_control(native, prepared_ring_zero):
    apply_generator = native["apply_generator"]
    native_letter = native["native_letter"]
    checkpoint = (0, 0, 0, 0, 0, 0)
    require(prepared_ring_zero == (2, 0, 0, 0, 3, 0), "unexpected prepared ring zero")
    require(checkpoint != prepared_ring_zero, "the raw control equals the prepared zero")
    prefix = []
    blank_count = 0
    present_count = 0
    for n in range(HORIZON + 1):
        reading = read_reference(checkpoint)
        if n < 3:
            require(reading == BLANK, ("raw zero before synchronization", n, checkpoint))
            blank_count += 1
        else:
            require(reading == ("PRESENT", 0, 3), ("raw zero after synchronization", n, reading))
            present_count += 1
        if n == 3:
            require(prefix == list("ace"), ("raw zero prefix", prefix))
            require(checkpoint == (0, 0, 1, 3, 1, 1), ("raw zero cut three", checkpoint))
        if n == HORIZON:
            break
        letter = native_letter(n, checkpoint)
        if n < 3:
            prefix.append(letter)
        checkpoint = apply_generator(letter, checkpoint)
    return blank_count, present_count


def audit():
    native = load_frozen_native()
    apply_generator = native["apply_generator"]
    native_letter = native["native_letter"]
    native_preparation = native["native_preparation"]
    polynomial_targets = native["polynomial_targets"]
    theta = native["theta"]
    inputs = set(product(range(MODULUS), repeat=2))
    complete_cuts = [set() for _ in range(HORIZON + 1)]
    piston_projections = {2: set(), 8: set()}
    projected_tags = {2: set(), 8: set()}
    recorded_pairs = set()
    edges = 0
    blanks = 0
    present = 0
    reference_checks = 0
    product_checks = 0
    zero_pair_readings = 0

    for u, v in sorted(inputs):
        _, profile = polynomial_targets(u, v)
        _, r1, _, _, r4 = profile
        checkpoint = native_preparation(u, v)
        prefix = []
        for n in range(HORIZON + 1):
            complete_cuts[n].add(checkpoint)
            reading = read_reference(checkpoint)
            if n in piston_projections:
                piston_projections[n].add(checkpoint[:4])
                projected_tags[n].add(reading[0])

            if n < 3:
                expected_z = (0, 0, 2)[n]
                require(sum(checkpoint) % MODULUS == expected_z,
                        ("BLANK checkpoint phase", u, v, n, checkpoint))
                require(reading == BLANK, ("BLANK record", u, v, n, reading))
                blanks += 1
            else:
                require(reading == ("PRESENT", r1, r4), ("PRESENT record", u, v, n, reading))
                recorded_pairs.add(reading[1:])
                present += 1
                if reading[1:] == (0, 0):
                    require((u, v) == (0, 0), ("zero record alias", u, v, n))
                    zero_pair_readings += 1

                a, c, b, d = phase_coordinates(checkpoint)
                sign_a = (-1) ** (n - 3)
                sign_c = 2 * (-1) ** (n + theta(n - 1))
                require((a - sign_a) % MODULUS == (c - sign_c) % MODULUS == 0,
                        ("current reference signs", u, v, n, a, c))
                reference_checks += 1
                require((a * b - r1 - r4) % MODULUS == (3 * c * d - r1 + r4 + 1) % MODULUS == 0,
                        ("paired invariant products", u, v, n, a, c, b, d))
                product_checks += 1

            if n == 3:
                expected_cut = (0, r1, 1, r4, 4, (1 + 2 * u) % MODULUS)
                require(prefix == list("ace"), ("actual prefix", u, v, prefix))
                require(checkpoint == expected_cut, ("literal complete write cut", u, v, checkpoint))
            if n == HORIZON:
                break

            letter = native_letter(n, checkpoint)
            if n < 3:
                prefix.append(letter)
            checkpoint = apply_generator(letter, checkpoint)
            edges += 1

    require(all(len(cut) == len(inputs) for cut in complete_cuts), "a full cut merged inputs")
    require(recorded_pairs == inputs, "the complete set of relative words was not retained")
    require(piston_projections[2] == piston_projections[8], "unequal four-piston projections")
    require(len(piston_projections[2]) == 25, "four-piston projection has wrong size")
    require(projected_tags == {2: {"BLANK"}, 8: {"PRESENT"}}, "wrong projected readiness tags")
    control_blanks, control_presents = audit_zero_control(native, native_preparation(0, 0))

    print(f"Complete native cuts and edges: {sum(map(len, complete_cuts))}, {edges}")
    print(f"Counter-free BLANK and PRESENT readings: {blanks}, {present}")
    print(f"Reference signs and invariant coordinate products: {reference_checks}, {product_checks}")
    print(f"Distinct recorded pairs: {len(recorded_pairs)}, zero-pair readings: {zero_pair_readings}")
    print(f"Four-piston readiness collision: {len(piston_projections[2])} equal projections at cuts 2 and 8")
    print(f"Raw all-zero control: BLANK at {control_blanks} cuts, PRESENT(0,3) at {control_presents} cuts")
    print("PASS")


if __name__ == "__main__":
    audit()
