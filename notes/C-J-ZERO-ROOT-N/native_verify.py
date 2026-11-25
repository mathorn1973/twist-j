"""Exact prospective audit of the two-residue native write."""

from itertools import product


MODULUS = 5
HORIZON = 64
ROOT = (0, 1, 0, 0)
ONE = (1, 0, 0, 0)
ELL = (1, -1, 0, 0)
LETTERS = "abcde"
BLANK = ("BLANK",)


def require(condition, detail):
    if not condition:
        raise AssertionError(detail)


def ring_multiply(left, right):
    """Multiply over Z and reduce by the monic Phi_5."""
    coefficients = [0] * 7
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            coefficients[i + j] += a * b
    for degree in range(6, 3, -1):
        leading = coefficients[degree]
        for lower in range(degree - 4, degree):
            coefficients[lower] -= leading
    return tuple(coefficients[:4])


def ring_power(base, exponent):
    value = ONE
    for _ in range(exponent):
        value = ring_multiply(value, base)
    return value


def field_trace(value):
    """Sum the four field embeddings as exact cyclotomic polynomials."""
    trace = [0] * 4
    for embedding in range(1, 5):
        for degree, coefficient in enumerate(value):
            power = ring_power(ROOT, embedding * degree)
            for index, component in enumerate(power):
                trace[index] += coefficient * component
    require(trace[1:] == [0, 0, 0], ("trace did not descend to Z", value, trace))
    return trace[0]


def polynomial_targets(u, v):
    ell_squared = ring_power(ELL, 2)
    ell_cubed = ring_power(ELL, 3)
    lift = tuple(u * a + v * b for a, b in zip(ell_squared, ell_cubed))
    initial = field_trace(lift)
    profile = []
    for k in range(5):
        rotated = ring_multiply(ring_power(ROOT, 2 * k), lift)
        numerator = 2 * (field_trace(rotated) - initial)
        quotient, remainder = divmod(numerator, MODULUS)
        require(remainder == 0, ("relative difference not divisible by 5", u, v, k))
        profile.append(quotient % MODULUS)
    return lift, tuple(profile)


def mod5(coordinates):
    return tuple(coordinate % MODULUS for coordinate in coordinates)


def theta(n):
    return n.bit_count() % 2


def native_letter(n, state):
    return LETTERS[(sum(state) + 2 * theta(n)) % MODULUS]


def apply_generator(letter, state):
    p1, p4, p1p, p4p, q, r = state
    if letter == "a":
        return mod5((p4, p1, p4p, p1p, q, r))
    if letter == "b":
        return mod5((-p1p, -p4p, -p1, -p4, -q, -r))
    if letter == "c":
        return mod5((2 - p1p, 1 - p4p + r, 2 - p1, 1 - p4 - r, 1 - q, -r))
    if letter == "d":
        return mod5((2 - p1, 1 - p4, 3 - p1p, 4 - p4p, 1 - q, 1 - r))
    if letter == "e":
        return mod5((2 - p1, 1 - p4, 3 - p1p, 4 - p4p, 2 - q, 1 - r))
    raise ValueError(letter)


def native_preparation(u, v):
    return mod5((-2 * u - v - 3, 0, v, 0, 3, 2 * u))


def receiver(state):
    return state[1], state[3], state[4]


def read_record(n, p4, p4p):
    if n < 3:
        return BLANK
    initial_sum = (-1) ** (n - 3) * (p4 + p4p)
    initial_difference = (-1) ** (n + theta(n - 1)) * (p4 - p4p - 1)
    r1, r4 = mod5((3 * (initial_sum + initial_difference + 1),
                   3 * (initial_sum - initial_difference - 1)))
    return "PRESENT", r1, r4


def decode_input(r1, r4):
    v = -r4
    return mod5((3 * (v - r1), v))


def profile_from_record(r1, r4):
    u, v = decode_input(r1, r4)
    return mod5((0, r1, 4 * u + 2 * v, -2 * u - 2 * v, r4))


def synchronized_letter(n):
    previous = theta(n - 1)
    current = theta(n)
    if current != previous:
        return "b"
    return "d" if current == 1 else "e"


def receiver_successor(n, current):
    p4, p4p, q = current
    letter = synchronized_letter(n)
    if letter == "b":
        return mod5((-p4p, -p4, -q))
    offset = 1 if letter == "d" else 2
    return mod5((1 - p4, 4 - p4p, offset - q))


def recover_whole_state(n, r1, r4):
    u, _ = decode_input(r1, r4)
    checkpoint = mod5((0, r1, 1, r4, 4, 1 + 2 * u))
    for t in range(3, n):
        checkpoint = apply_generator(synchronized_letter(t), checkpoint)
    return checkpoint


def audit():
    inputs = tuple(product(range(MODULUS), repeat=2))
    complete_cuts = [set() for _ in range(HORIZON + 1)]
    tail_receiver_pairs = [set() for _ in range(HORIZON - 2)]
    control_receiver_cuts = [set() for _ in range(HORIZON + 1)]
    input_residues = set()
    target_pairs = set()
    differences_from_preloaded_coordinate = [False] * 6
    edges = 0
    inverse_edges = 0
    tail_readings = 0
    full_recoveries = 0

    for u, v in inputs:
        lift, target = polynomial_targets(u, v)
        ring_residue = mod5(lift)
        input_residues.add(ring_residue)
        _, r1, _, _, r4 = target
        require(target == mod5((0, v - 2 * u, 4 * u + 2 * v, -2 * u - 2 * v, -v)),
                ("polynomial profile", u, v, target))
        target_pairs.add((r1, r4))

        launch = native_preparation(u, v)
        require(receiver(launch) == (0, 0, 3), ("noncommon raw receiver", u, v, launch))
        require(sum(launch) % MODULUS == 0, ("unbalanced native selector sum", u, v))
        require(mod5((3 * launch[5], launch[2])) == (u, v), ("launch inverse", u, v))
        for index, coordinate in enumerate(launch):
            if coordinate != r1:
                differences_from_preloaded_coordinate[index] = True

        require(sum(ring_residue) % MODULUS == 0, ("control piston sum", u, v))
        control_state = ring_residue + (0, 1)
        state = launch
        applied_letters = []
        balancing = -2 * u - v - 3
        write_cuts = (
            launch,
            mod5((0, balancing, 0, v, 3, 2 * u)),
            mod5((2, 1 - v + 2 * u, 2, 1 - balancing - 2 * u, 3, -2 * u)),
            mod5((0, r1, 1, r4, 4, 1 + 2 * u)),
        )
        for n in range(HORIZON + 1):
            complete_cuts[n].add(state)
            control_receiver_cuts[n].add(control_state[4:])
            p4, p4p, _ = receiver(state)
            output = read_record(n, p4, p4p)
            if n < 3:
                require(output == BLANK, ("read cutoff", u, v, n, output))
            else:
                require(output == ("PRESENT", r1, r4), ("tail read", u, v, n, output))
                require(decode_input(*output[1:]) == (u, v), ("tail input inverse", u, v, n))
                require(profile_from_record(*output[1:]) == target, ("tail profile", u, v, n))
                recovered_state = recover_whole_state(n, *output[1:])
                require(recovered_state == state, ("whole state reconstruction", u, v, n))
                tail_receiver_pairs[n - 3].add((p4, p4p))
                tail_readings += 1
                full_recoveries += 1

            if n < len(write_cuts):
                require(state == write_cuts[n], ("literal write cut", u, v, n, state, write_cuts[n]))
            if n == 3:
                require(applied_letters == list("ace"), ("native prefix", u, v, applied_letters))
            if n >= 3:
                synchronized_z = (4 + 2 * theta(n - 1)) % MODULUS
                require(sum(state) % MODULUS == synchronized_z, ("synchronized z", u, v, n))
            if n == HORIZON:
                break

            letter = native_letter(n, state)
            successor = apply_generator(letter, state)
            applied_letters.append(letter)
            edges += 1
            require(apply_generator(letter, successor) == state, ("complete edge inverse", u, v, n))
            inverse_edges += 1
            if n >= 3:
                require(letter == synchronized_letter(n), ("synchronized selector", u, v, n))
                require(receiver(successor) == receiver_successor(n, receiver(state)),
                        ("closed receiver continuation", u, v, n))
            state = successor
            control_state = apply_generator(native_letter(n, control_state), control_state)

        for letter in reversed(applied_letters):
            state = apply_generator(letter, state)
        require(state == launch, ("complete word inverse", u, v, HORIZON))

    require(len(input_residues) == 25, ("layer coverage", len(input_residues)))
    require(target_pairs == set(inputs), ("all two-digit target words", target_pairs))
    require(all(differences_from_preloaded_coordinate), "a launch coordinate preloads r1")
    require(all(len(cut) == 25 for cut in complete_cuts), "a complete cut merged input states")
    require(all(cut == set(inputs) for cut in tail_receiver_pairs), "tail pair lost a record")
    require(all(len(cut) == 1 for cut in control_receiver_cuts), "control port split equal sums")

    print(f"Polynomial targets and distinct literal write words: {len(target_pairs)}")
    print(f"Complete native cuts and edges: {sum(map(len, complete_cuts))}, {edges}")
    print(f"Tail readings and whole-state reconstructions: {tail_readings}, {full_recoveries}")
    print(f"Complete inverse edges and complete inverse words: {inverse_edges}, {len(inputs)}")
    print(f"Natural coefficient control: {len(inputs)} inputs, "
          f"{len(control_receiver_cuts)} cuts, one common port history")
    print("PASS")


if __name__ == "__main__":
    audit()
