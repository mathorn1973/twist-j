"""First exact audit of the frozen integer phase contact, issue #1419.

Original standard-library integer source. A. M. Thorn, Apache-2.0.
No external inputs, coefficient clipping, numerical approximation or writes.
"""

from itertools import combinations, product
import sys


ZERO = (0, 0, 0, 0)
ONE = (1, 0, 0, 0)
JROOT = (0, 1, 0, 0)
H = ((1, 1, 1, 1), (1, -1, 1, -1),
     (1, 1, -1, -1), (1, -1, -1, 1))


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def scale(a, n):
    return tuple(n * x for x in a)


def mul(a, b):
    c = [0] * 7
    for i in range(4):
        for k in range(4):
            c[i + k] += a[i] * b[k]
    for degree in range(6, 3, -1):
        coeff = c[degree]
        for offset in range(1, 5):
            c[degree - offset] -= coeff
        c[degree] = 0
    return tuple(c[:4])


ROOTS = [ONE]
for _ in range(4):
    ROOTS.append(mul(ROOTS[-1], JROOT))
ROOTS = tuple(ROOTS)


def conjugate(a):
    out = ZERO
    for k, coeff in enumerate(a):
        out = add(out, scale(ROOTS[-k % 5], coeff))
    return out


def trace(a):
    return 4 * a[0] - sum(a[1:])


def cost(a):
    twice = trace(mul(a, conjugate(a)))
    assert twice % 2 == 0
    return twice // 2


def cost_formula(a):
    return 2 * sum(x * x for x in a) - sum(
        a[i] * a[k] for i, k in combinations(range(4), 2))


def hadamard(b):
    return tuple(tuple(sum(H[i][k] * b[k][d] for k in range(4))
                       for d in range(4)) for i in range(4))


def chart(b):
    hb = hadamard(b)
    if any(x % 4 for slot in hb for x in slot):
        raise ValueError("state is outside H O^4")
    return tuple(tuple(x // 4 for x in slot) for slot in hb)


def contact(b, r):
    a = list(chart(b))
    a[0] = mul(ROOTS[r % 5], a[0])
    return hadamard(tuple(a))


def costs(b):
    return tuple(cost(slot) for slot in b)


def total(b):
    return sum(costs(b))


def add_state(b, c):
    return tuple(add(x, y) for x, y in zip(b, c))


def pairing(b, c):
    return sum(trace(mul(x, conjugate(y))) for x, y in zip(b, c))


def full_norm(b):
    out = ZERO
    for slot in b:
        out = add(out, mul(slot, conjugate(slot)))
    return out


def placed(slot, value):
    a = [ZERO] * 4
    a[slot] = value
    return tuple(a)


def t(k):
    return 4 if k % 5 == 0 else -1


def predicted(r, s):
    return (26 + 2 * t(r) + 3 * t(r + s) - t(r - s),
            26 + 2 * t(r) + 3 * t(r - s) - t(r + s),
            6 - 2 * t(r) - t(r + s) - t(r - s),
            6 - 2 * t(r) - t(r + s) - t(r - s))


def run():
    assert mul(ROOTS[4], JROOT) == ONE
    assert all(trace(ROOTS[k]) == t(k) for k in range(5))
    phi = scale(add(ROOTS[2], ROOTS[3]), -1)
    radial_j = add(ONE, ROOTS[2])
    assert mul(phi, radial_j) == JROOT
    for i in range(4):
        for k in range(4):
            assert sum(H[i][a] * H[a][k] for a in range(4)) == 4 * (i == k)

    scalar_count = phase_count = 0
    for alpha in product(range(-2, 3), repeat=4):
        assert conjugate(conjugate(alpha)) == alpha
        assert cost(alpha) == cost_formula(alpha)
        assert cost(alpha) >= 0
        assert (cost(alpha) == 0) == (alpha == ZERO)
        assert 2 * cost(alpha) >= sum(x * x for x in alpha)
        for r in range(5):
            assert cost(mul(ROOTS[r], alpha)) == cost(alpha)
            phase_count += 1
        scalar_count += 1

    basis = tuple(hadamard(placed(i, ROOTS[k]))
                  for i in range(4) for k in range(4))
    inverse_count = gram_count = 0
    for r in range(5):
        images = tuple(contact(b, r) for b in basis)
        for b, image in zip(basis, images):
            assert hadamard(chart(image)) == image
            assert contact(image, -r) == b
            assert contact(contact(b, -r), r) == b
            assert full_norm(image) == full_norm(b)
            assert total(image) == total(b)
            inverse_count += 1
        for i, k in product(range(16), repeat=2):
            assert pairing(images[i], images[k]) == pairing(basis[i], basis[k])
            assert full_norm(add_state(images[i], images[k])) == full_norm(
                add_state(basis[i], basis[k]))
            gram_count += 1

    triple_count = 0
    for r, s, v in product(range(5), repeat=3):
        for b in basis:
            assert contact(contact(contact(b, v), s), r) == contact(b, r + s + v)
            triple_count += 1
    for b in basis:
        image = b
        for _ in range(5):
            image = contact(image, 1)
        assert image == b

    atoms = (ZERO,) + ROOTS + tuple(scale(a, -1) for a in ROOTS)
    assert len(set(atoms)) == 11
    dirty_count = 0
    for i, k in combinations(range(4), 2):
        for alpha, beta, r in product(atoms, atoms, range(5)):
            a = add_state(placed(i, alpha), placed(k, beta))
            b = hadamard(a)
            assert chart(b) == a
            image = contact(b, r)
            assert contact(image, -r) == b
            assert full_norm(image) == full_norm(b)
            assert total(image) == total(b)
            dirty_count += 1

    accounts = []
    for s, r in product((1, -1), range(5)):
        b = (scale(ONE, 4), scale(ROOTS[s % 5], 4), ZERO, ZERO)
        assert hadamard(chart(b)) == b
        assert costs(b) == (32, 32, 0, 0)
        delta = mul(add(ROOTS[r], scale(ONE, -1)), add(ONE, ROOTS[s % 5]))
        expected = (add(b[0], delta), add(b[1], delta), delta, delta)
        image = contact(b, r)
        assert image == expected
        energy = costs(image)
        assert energy == predicted(r, s)
        assert sum(energy) == 64
        df = energy[0] + energy[2] - 32
        dm = energy[1] + energy[3] - 32
        assert df == 2 * (t(r + s) - t(r - s))
        assert df == 10 * ((r + s) % 5 == 0) - 10 * ((r - s) % 5 == 0)
        assert dm == -df
        split_before = add(mul(b[0], conjugate(b[0])), mul(b[2], conjugate(b[2])))
        split_after = add(mul(image[0], conjugate(image[0])),
                          mul(image[2], conjugate(image[2])))
        odd_product = mul(add(ROOTS[r], scale(ROOTS[-r % 5], -1)),
                          add(ROOTS[s % 5], scale(ROOTS[-s % 5], -1)))
        assert add(split_after, scale(split_before, -1)) == scale(odd_product, 2)
        accounts.append((r, s, energy, df, dm))

    large = 10**12 + 39
    for s in (1, -1):
        b = (scale(ONE, 4), scale(ROOTS[s % 5], 4), ZERO, ZERO)
        big = tuple(scale(slot, large) for slot in b)
        assert contact(big, 1) == tuple(scale(slot, large) for slot in contact(b, 1))
        assert costs(contact(big, 1)) == tuple(large**2 * x for x in predicted(1, s))
        assert total(big) == 64 * large**2

    rejected = False
    try:
        contact((ONE, ZERO, ZERO, ZERO), 1)
    except ValueError:
        rejected = True
    assert rejected
    unwrapped = hadamard(placed(0, scale(ONE, 4)))
    wrapped = tuple(tuple((x + 2) % 5 - 2 for x in slot) for slot in unwrapped)
    assert total(unwrapped) == 128 and total(wrapped) == 8
    assert cost(ONE) == 2 and cost(radial_j) == 3
    bare_before = hadamard(placed(0, ONE))
    bare_after = hadamard(placed(0, radial_j))
    assert total(bare_before) == 8 and total(bare_after) == 12
    for s in (1, -1):
        b = (scale(ONE, 4), scale(ROOTS[s % 5], 4), ZERO, ZERO)
        unmixed = (mul(JROOT, b[0]), b[1], b[2], b[3])
        assert costs(unmixed) == costs(b)
        assert costs(contact(b, 1)) != costs(b)
    plus = (scale(ONE, 4), scale(ROOTS[1], 4), ZERO, ZERO)
    minus = (scale(ONE, 4), scale(ROOTS[4], 4), ZERO, ZERO)
    assert plus != minus and costs(plus) == costs(minus)

    lines = [
        "PASS integer cyclotomic phase-work contact; NON-CANONICAL",
        f"scalar_fixtures={scalar_count}; scalar_phase_checks={phase_count}",
        f"lattice_basis=16; contact_inverse_cases={inverse_count}; gram_pairings={gram_count}",
        f"triple_group_basis_cases={triple_count}; dirty_two_slot_cases={dirty_count}",
        "initial_channel_costs=(32,32,0,0); total=64",
    ]
    for r, s, energy, df, dm in accounts:
        lines.append(f"r={r}; s={s:+d}; costs={energy}; DeltaF={df}; DeltaM={dm}")
    lines.extend([
        "PASS large integer scaling; no coefficient cutoff",
        "PASS negative controls: nonadmission; wrapping; bare-J; unmixed phase; lost phase datum",
        "PASS full-state inverse and positive common energy; native physical bridge OPEN",
    ])
    sys.stdout.buffer.write(("\n".join(lines) + "\n").encode("ascii"))


if __name__ == "__main__":
    run()
