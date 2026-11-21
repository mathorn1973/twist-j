#!/usr/bin/env python3
"""Exact finite audit; PUBLIC / NON-CANONICAL / L1 / candidate-T.

P-NATIVE-TWO-CELL-WORK-ADMISSION-1. Standard library only. Scientific
execution is permitted only after this file and PREREG.md are publicly
pinned. No files, network, floating-point arithmetic, or random choices.
The native U and the declared integer work machine remain different types.

Public antecedents: https://github.com/mathorn1973/twist-j/issues/994
for centered native exchange, and
https://github.com/mathorn1973/twist-j/issues/975
for nonselection of an energy budget. The corresponding native block
mechanism and nonselection principle are inherited, not claimed as new.
"""

from itertools import product


AF = ((1, 0, 1, 0), (0, 1, 0, 1),
      (-2, 1, -1, 1), (1, -3, 1, -2))
PSTAR = (1, 3, 4, 2)
ZERO = (0, 0, 0, 0)
V0 = (2, -1, 0, 0)
# Complete H=1 list from the public integer-field unit-shell certificate.
# It is an explicit fixture, not the output of a new shell search.
UNITS = (
    (-1, 0, 1, -1), (-1, 0, 1, 0),
    (-1, 1, 1, -2), (-1, 1, 2, -2),
    (0, -1, -1, 1), (0, -1, -1, 2),
    (0, -1, 0, 1), (0, -1, 0, 2),
    (0, 0, -1, 0), (0, 0, 0, -1),
    (0, 0, 0, 1), (0, 0, 1, 0),
    (0, 1, 0, -2), (0, 1, 0, -1),
    (0, 1, 1, -2), (0, 1, 1, -1),
    (1, -1, -2, 2), (1, -1, -1, 2),
    (1, 0, -1, 0), (1, 0, -1, 1),
)


def check(condition, label):
    if not condition:
        raise AssertionError(label)


def mod5(values):
    return tuple(v % 5 for v in values)


def z(x):
    return sum(x) % 5


def native_letter(index, x):
    a, b, c, d, q, r = x
    if index == 0:
        y = (b, a, d, c, q, r)
    elif index == 1:
        y = (-c, -d, -a, -b, -q, -r)
    elif index == 2:
        y = (2-c, 1-d+r, 2-a, 1-b-r, 1-q, -r)
    elif index == 3:
        y = (2-a, 1-b, 3-c, 4-d, 1-q, 1-r)
    elif index == 4:
        y = (2-a, 1-b, 3-c, 4-d, 2-q, 1-r)
    else:
        raise AssertionError("native letter index")
    return mod5(y)


def native_step(x, bit):
    index = (z(x) + 2 * bit) % 5
    return native_letter(index, x), index


def actual_history(x, last):
    states = [x]
    letters = []
    for n in range(last):
        x, index = native_step(x, n.bit_count() % 2)
        states.append(x)
        letters.append(index)
    return states, letters


def native_quotient(x):
    return (z(x), x[4], x[5])


def quotient_letter(index, value):
    zz, q, r = value
    images = ((zz, q, r), (-zz, -q, -r),
              (2-zz, 1-q, -r), (2-zz, 1-q, 1-r),
              (3-zz, 2-q, 1-r))
    return mod5(images[index])


def centered_blocks(x):
    p = mod5(x[i] - PSTAR[i] for i in range(4))
    return p[:2], p[2:]


def negate(v):
    return mod5(-a for a in v)


def orbit(v):
    return min(v, negate(v))


def balanced(a):
    return a if a <= 2 else a - 5


def block_energy(v, weight=(1, 1)):
    return sum(w * balanced(a)**2 for w, a in zip(weight, v))


def mv(matrix, y):
    return tuple(sum(a*b for a, b in zip(row, y)) for row in matrix)


def af_power(y, n):
    for _ in range(n % 5):
        y = mv(AF, y)
    return y


def h(y):
    a, b, c, d = y
    return (2*a*a - 2*a*b + 3*b*b + c*c + d*d
            + 2*a*c - a*d - b*c + 3*b*d)


def bstar(y):
    a, b, c, d = y
    return (-c, -d, -a, -b)


def delta(y):
    a, b, c, d = y
    return (c-d)**2 + d*d - (a-b)**2 - b*b


def source_contact(y, resource):
    change = delta(y)
    if resource < change:
        return y, resource
    return bstar(y), resource-change


# Complete reduced coordinates on the declared invariant Sigma_2 carrier:
# (source active field, source resource, receiver resource, channel,
#  receiver matter indicator 0=R/1=AM, pointer in C5).
# The omitted coordinates are exactly the fixed zero spectators/static
# fields, zero receiver active field, source matter ZM, and listed R/AM.
def work_energy(state):
    y, rs, rr, q, matter, pointer = state
    return h(y) + rs + rr + q + 18 + 2*matter + 1


def work_admitted(state):
    y, rs, rr, q, matter, pointer = state
    return (len(y) == 4 and all(isinstance(v, int) for v in y)
            and min(rs, rr, q) >= 0 and matter in (0, 1)
            and 0 <= pointer < 5 and work_energy(state) == 34)


def receiver_forward(rr, matter, pointer):
    if matter == 1:
        return rr+2, 0, pointer
    if rr >= 2:
        return rr-2, 1, (pointer+1) % 5
    return rr, matter, pointer


def receiver_inverse(rr, matter, pointer):
    if matter == 1:
        return rr+2, 0, (pointer-1) % 5
    if rr >= 2:
        return rr-2, 1, pointer
    return rr, matter, pointer


def work_forward(state):
    y, rs, rr, q, matter, pointer = state
    y, rs = source_contact(y, rs)
    rr, matter, pointer = receiver_forward(rr, matter, pointer)
    rs, q = q, rs
    q, rr = rr, q
    return (mv(AF, y), rs, rr, q, matter, pointer)


def work_inverse(state):
    y, rs, rr, q, matter, pointer = state
    y = af_power(y, 4)
    q, rr = rr, q
    rs, q = q, rs
    rr, matter, pointer = receiver_inverse(rr, matter, pointer)
    y, rs = source_contact(y, rs)
    return (y, rs, rr, q, matter, pointer)


def affine_value(coeff, y, resource):
    return (sum(a*b for a, b in zip(coeff[:4], y))
            + coeff[4]*resource + coeff[5]) % 5


def nonlinear_bank(y, resource):
    _, after = source_contact(y, resource)
    # 3 is the inverse of 2 in F5. Rejected inputs have zero reading.
    return 3*(resource-after) % 5


def low_energy_states():
    for y in (ZERO,) + UNITS:
        for matter in (0, 1):
            total = 15-h(y)-2*matter
            for rs in range(total+1):
                for rr in range(total-rs+1):
                    q = total-rs-rr
                    for pointer in range(5):
                        yield (y, rs, rr, q, matter, pointer)


def main():
    # Four diagonal and six polarized probes determine each homogeneous
    # quadratic identity. The fifth-power check explicitly multiplies AF;
    # it does not use the modulo-five shortcut in af_power.
    coordinate_vectors = tuple(tuple(int(i == j) for i in range(4))
                               for j in range(4))
    polarized = coordinate_vectors + tuple(
        tuple(coordinate_vectors[i][k]+coordinate_vectors[j][k]
              for k in range(4))
        for i in range(4) for j in range(i+1, 4))
    for y in polarized:
        check(h(mv(AF, y)) == h(y), "free quadratic identity")
        check(h(bstar(y))-h(y) == delta(y), "contact quadratic identity")
    for y in coordinate_vectors:
        power = y
        for _ in range(5):
            power = mv(AF, power)
        check(power == y and bstar(bstar(y)) == y,
              "free order five and signed-swap involution")

    # All native stable checkpoints and both controls. For a fixed bit,
    # the map on X1 union X4 is two-to-one, not globally invertible. The
    # inverse check below is sheet-restricted: retain the selected letter
    # from the known input sheet and apply that involution to its image.
    # In particular, do not recompute the selector from the image.
    orbits = tuple(sorted({orbit(v) for v in product(range(5), repeat=2)
                           if v != (0, 0)}))
    check(len(orbits) == 12, "twelve nonzero sign orbits")
    stable_count = edge_count = basis_count = 0
    for x in product(range(5), repeat=6):
        if z(x) not in (1, 4):
            continue
        stable_count += 1
        u, v = centered_blocks(x)
        for bit in (0, 1):
            xp, index = native_step(x, bit)
            edge_count += 1
            check(index in (1, 3, 4), "stable selected alphabet")
            check(z(xp) in (1, 4), "stable sheet closure")
            check(native_letter(index, xp) == x,
                  "known-sheet actual-letter inverse")
            check(native_quotient(xp) ==
                  quotient_letter(index, native_quotient(x)),
                  "literal quotient formula")
            up, vp = centered_blocks(xp)
            expected = ((negate(v), negate(u)) if index == 1 else
                        (negate(u), negate(v)))
            check((up, vp) == expected, "centered block action")
            for key in orbits:
                before = int(orbit(u) == key) + int(orbit(v) == key)
                after = int(orbit(up) == key) + int(orbit(vp) == key)
                check(before == after, "even-function basis conservation")
                basis_count += 1
    check((stable_count, edge_count, basis_count) ==
          (6250, 12500, 150000), "stable inventory")
    # Every nonzero sign orbit can be placed in one block, with the other
    # zero, on z=1. Thus the b conservation equations separately identify
    # the twelve coefficients of two normalized even block readings.
    for key in orbits:
        p = mod5(PSTAR[i] + (key + (0, 0))[i] for i in range(4))
        x = p + ((1-sum(p)) % 5, 0)
        xp, index = native_step(x, 0)
        check(index == 1 and centered_blocks(x) == (key, (0, 0)),
              "coefficient comparison input")
        check(centered_blocks(xp) == ((0, 0), negate(key)),
              "coefficient comparison transfer")

    # Five histories at the inherited common origin, boundaries 0..9.
    native_histories = []
    for a in range(5):
        states, letters = actual_history(mod5((a, -a, 0, 0, 0, 0)), 9)
        native_histories.append(states)
        check(letters[:3] == [0, 2, 4], "xi initial actual letters ace")
        check(states[3] == mod5((0, 0, 1-a, 3+a, 1, 1)),
              "xi checkpoint three")
        check(letters[3:5] == [1, 1] and states[3] == states[5],
              "xi actual two-tick checkpoint return")
        check(states[4] == states[6], "xi second checkpoint collision")
        for n in range(3, 10):
            check(((-1)**(n-3)*(states[n][0]+states[n][2])) % 5
                  == (1-a) % 5, "xi conserved piston phase label")
    for n in range(10):
        check(len({native_quotient(states[n])
                   for states in native_histories}) == 1,
              "xi common quotient history")

    # Inherited exact five-field orbit and all five N=2 preparations.
    fields = tuple(af_power(V0, a) for a in range(5))
    check(fields == ((2, -1, 0, 0), (2, -1, -5, 5),
                     (-3, 4, 5, -10), (2, -6, -5, 10),
                     (-3, 4, 5, -5)), "five prepared fields")
    check(tuple(delta(y) for y in fields) == (-10, 115, 260, 225, 60),
          "five source decisions")
    preparations = tuple((y, 0, 0, 0, 0, 0) for y in fields)
    first_hits = []
    work_histories = []
    for a, initial in enumerate(preparations):
        states = [initial]
        for _ in range(10):
            before = states[-1]
            after = work_forward(before)
            check(work_admitted(before) and work_admitted(after),
                  "prepared trajectory budget")
            check(work_inverse(after) == before, "prepared forward inverse")
            check(work_forward(work_inverse(before)) == before,
                  "prepared inverse forward")
            states.append(after)
        wait = (-a) % 5
        check(states[wait] == preparations[0], "literal delayed preparation")
        first_hits.append(next(n for n, state in enumerate(states)
                               if state[-1] != 0))
        work_histories.append(states)
    check(first_hits == [2, 6, 5, 4, 3], "five first receiver writes")
    emitted_field = (0, 0, -2, 1)
    after_first_free = (-2, 1, 3, -4)
    check(mv(AF, emitted_field) == after_first_free
          and delta(after_first_free) == 55,
          "first free image and next refused delta")
    check(work_histories[0][1] ==
          (after_first_free, 0, 10, 0, 0, 0),
          "complete first emitted work state")
    check(work_histories[0][2] ==
          (mv(AF, after_first_free), 0, 0, 8, 1, 1),
          "complete first written work state")
    check(work_histories[0][0][-1] == 0
          and work_histories[0][2][-1] == 1,
          "work BLANK HIT contradiction endpoints")
    check(native_histories[0][3] == native_histories[0][5],
          "fixed native reader has equal inputs")

    # Refusal obstructs a literal residue lift before any bank coding.
    late = fields[1]
    check(source_contact(late, 0) == (late, 0), "late refusal")
    check(mod5(late) == (2, 4, 0, 0)
          and mod5(bstar(late)) == (0, 0, 3, 1), "refusal residue mismatch")
    witness = (-3, 0, 1, 0)
    check(h(witness) == 13 and delta(witness) == -8,
          "literal bank witness energy")
    check(source_contact(witness, 2)[1] == 10
          and 10 % 5 != (-2) % 5, "literal bank residue mismatch")

    # A fixed affine native-b anti-invariant bank reader is forced to zero
    # by these six inputs, all lying in the declared energy budget.
    e1, e2, e3, e4 = ((1, 0, 0, 0), (0, 1, 0, 0),
                      (0, 0, 1, 0), (0, 0, 0, 1))
    witnesses = ((ZERO, 0), (ZERO, 1), (e3, 0), (e4, 0),
                 (e1, 0), (e2, 0))
    for y, resource in witnesses:
        check(h(y)+resource <= 15, "affine witness admitted")
    affine_survivors = []
    for coeff in product(range(5), repeat=6):
        if all((affine_value(coeff, *source_contact(y, resource))
                + affine_value(coeff, y, resource)) % 5 == 0
               for y, resource in witnesses):
            affine_survivors.append(coeff)
    check(affine_survivors == [(0, 0, 0, 0, 0, 0)],
          "affine anti-invariant bank classification")
    check(nonlinear_bank(e1, 0) == 2, "nonlinear bank is nonzero")

    # Full-coordinate audits on every state in the explicit H=0/1 subset.
    # This is 22305 states of Sigma_2, not an exhaustion of Sigma_2.
    check(len(UNITS) == len(set(UNITS)) == 20
          and all(h(y) == 1 for y in UNITS), "explicit unit-shell fixture")
    counts = {0: 0, 1: 0}
    for state in low_energy_states():
        y, rs, rr, q, matter, pointer = state
        counts[h(y)] += 1
        check(work_admitted(state), "low-field input admitted")
        kp, rp = source_contact(y, rs)
        check(source_contact(kp, rp) == (y, rs), "source involution")
        check(h(kp)+rp == h(y)+rs and rp >= 0, "source energy funding")
        check((nonlinear_bank(kp, rp)+nonlinear_bank(y, rs)) % 5 == 0,
              "nonlinear bank anti-invariance")
        forward, backward = work_forward(state), work_inverse(state)
        check(work_admitted(forward) and work_admitted(backward),
              "low-field continuation admitted")
        check(work_inverse(forward) == state
              and work_forward(backward) == state,
              "low-field both inverse compositions")
    check(counts == {0: 1205, 1: 21100}, "low-field cardinal count")
    check(sum(counts.values()) == 22305 > 5**6, "single checkpoint capacity")

    # Positive operational benchmark for a separately selected centered
    # block energy. Source-only preparation is at boundary 3, not 0.
    benchmark_energies = []
    benchmark_quartics = []
    for t in range(5):
        initial = mod5((0, 3, 2-t, 1+t, 0, 4))
        states, letters = actual_history(initial, 5)
        prepared = mod5((1+t, 3-t, 4, 2, 1, 0))
        check(letters == [0, 2, 4, 1, 1], "benchmark actual acebb")
        check(states[3] == prepared and states[5] == prepared,
              "benchmark prepared state and return")
        u3, v3 = centered_blocks(states[3])
        u4, v4 = centered_blocks(states[4])
        check(v3 == (0, 0) and u4 == (0, 0),
              "benchmark empty receiver then empty source")
        value = 2*balanced(t)**2
        check(block_energy(u3) == value == block_energy(v4),
              "benchmark chosen energy transfer")
        check(states[3][2:] == (4, 2, 1, 0),
              "benchmark common complete receiver at cut three")
        for n in (3, 4, 5):
            us, vr = centered_blocks(states[n])
            es, er = block_energy(us), block_energy(vr)
            check(es+er == value, "benchmark F2 conservation")
            check(es*es+er*er == value*value,
                  "benchmark F4 conservation")
        check(block_energy(u3)**2 == block_energy(v4)**2 == value*value,
              "benchmark F4 transfer")
        benchmark_energies.append(value)
        benchmark_quartics.append(value*value)
    check(benchmark_energies == [0, 2, 8, 8, 2], "benchmark energy list")
    check(benchmark_quartics == [0, 4, 64, 64, 4], "benchmark quartic list")

    # Two allowed positive even choices, equal normalization at (1,0),
    # give different work for the other component under the same b step.
    alternatives = []
    for u in ((1, 0), (0, 1)):
        p = mod5(PSTAR[i] + (u+(0, 0))[i] for i in range(4))
        x = p + (0, 0)
        check(z(x) == 1, "alternative preparation at native cut three")
        xp, index = native_step(x, (3).bit_count() % 2)
        check(index == 1, "alternative actual b")
        up, vp = centered_blocks(xp)
        check(up == (0, 0) and vp == negate(u), "alternative transfer")
        alternatives.append((block_energy(vp), block_energy(vp, (1, 2))))
    check(alternatives == [(1, 1), (1, 2)], "positive energy nonselection")

    print("P-NATIVE-TWO-CELL-WORK-ADMISSION-1")
    print("native_stable_states=6250 edges=12500 even_basis_checks=150000 coefficients=12")
    print("native_xi_histories=5 boundaries=0..9 checkpoint_returns=3:5,4:6")
    print("work_preparations=5 steps_each=10 first_hits=2,6,5,4,3")
    print("WORK_READER_REJECTED_FROZEN_ALIGNMENT")
    print("literal_b_lift=REFUSAL_MISMATCH literal_bank=PAYMENT_MISMATCH")
    print("affine_bank_coefficients=15625 witnesses=6 survivors=1 zero_only=true")
    print("nonlinear_bank=NONZERO_ANTI_INVARIANT no_full_native_lift_claimed")
    print("low_field_states=22305 H0=1205 H1=21100 both_inverse_compositions=PASS")
    print("single_checkpoint_capacity=22305>15625")
    print("native_benchmark=acebb F2=0,2,8,8,2 F4=0,4,64,64,4 preparation_cut=3 return_cut=5")
    print("positive_even_energy_nonselection=I:1,1 G:1,2")
    print("AUDIT PASS; native paid Ksrc admission and physical energy remain OPEN")


if __name__ == "__main__":
    main()
