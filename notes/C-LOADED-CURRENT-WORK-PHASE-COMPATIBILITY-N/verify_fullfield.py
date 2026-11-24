# SPDX-License-Identifier: Apache-2.0
"""Prospective full-field audit from public equations; standard library only.

A new declared 27-site quotient implementation, not a replay of missing
#1926/#1927 sources. No private reconstruction code is imported or copied.
B denotes electric drift z*M^-1*E, not the next vector potential.
The two fifth-root pairs encode a label in Z/25, not a primitive 25th
root as one cyclotomic coordinate. Its character reading is supplied.
The four-tick return below is modulo FIVE only, never exact field return.
"""
from dataclasses import dataclass
from fractions import Fraction
from itertools import product

F = Fraction
CHECKS = 0


def require(value, label):
    global CHECKS
    CHECKS += 1
    if not value:
        raise AssertionError(label)


def same(a, b, label):
    require(a == b, label)


def number(value):
    if isinstance(value, (int, F)):
        return (F(value), F(0), F(0), F(0))
    return tuple(F(x) for x in value)


NIL = number(0)
UNIT = number(1)
ROOT = number((0, 1, 0, 0))


def plus(a, b):
    return tuple(x + y for x, y in zip(a, b))


def minus(a, b):
    return tuple(x - y for x, y in zip(a, b))


def times_scalar(a, scalar):
    return tuple(x * scalar for x in a)


def times(a, b):
    # Cyclic five-coefficient multiplication, then choose coefficient four=0.
    cyclic = [F(0)] * 5
    for r, x in enumerate(a):
        for s, y in enumerate(b):
            cyclic[(r + s) % 5] += x * y
    return tuple(cyclic[k] - cyclic[4] for k in range(4))


def conjugate(a):
    cyclic = [F(0)] * 5
    for k, x in enumerate(a):
        cyclic[(-k) % 5] += x
    return tuple(cyclic[k] - cyclic[4] for k in range(4))


def trace(a):
    return 4 * a[0] - sum(a[1:])


def g(a, b):
    return trace(times(a, conjugate(b))) / 2


def Q(a):
    return g(a, a)


def Omega(a, b):
    return (a[0] * b[1] - a[1] * b[0]
            + a[1] * b[2] - a[2] * b[1]
            + a[2] * b[3] - a[3] * b[2])


ROOTS = [UNIT]
for _ in range(4):
    ROOTS.append(times(ROOTS[-1], ROOT))
RHO = ROOTS[2]
RHO_BACK = ROOTS[3]
J = plus(UNIT, RHO)
PHI = times_scalar(plus(ROOTS[2], ROOTS[3]), -1)


def norm_coefficients(a):
    h = times(a, conjugate(a))
    if h[1] or h[2] != h[3]:
        raise ArithmeticError("Hermitian product did not lie in real subfield")
    return h[0], -h[2]


def is_integral(a):
    return all(x.denominator == 1 for x in a)


def residue(value, modulus):
    value = F(value)
    if value.denominator % 5 == 0:
        raise ArithmeticError("denominator is not invertible at five")
    return value.numerator * pow(value.denominator, -1, modulus) % modulus


WEIGHTS = {2: 6, 4: 1, 8: 15, 10: 1, 16: 1}
SHELL = tuple(v for v in product(range(-4, 5), repeat=3)
              if sum(v) % 2 == 0 and sum(x * x for x in v) in WEIGHTS)
DIRECTIONS = tuple(v for v in SHELL if next(x for x in v if x) > 0)
COEFF = tuple(F(WEIGHTS[sum(x * x for x in v)], 324) for v in DIRECTIONS)
SITES = tuple(product(range(3), repeat=3))
SITE_INDEX = {site: i for i, site in enumerate(SITES)}
ORIGIN = SITE_INDEX[(0, 0, 0)]
MARK_DIRECTION = DIRECTIONS.index((1, 1, 0))
MARK = (MARK_DIRECTION, ORIGIN)
MODE_DIRECTION = DIRECTIONS.index((1, -1, 0))
Z = F(1, 27)


def translated(site_index, displacement):
    site = SITES[site_index]
    return SITE_INDEX[tuple((site[k] + displacement[k]) % 3 for k in range(3))]


FORWARD = tuple(tuple(translated(n, v) for n in range(27)) for v in DIRECTIONS)
BACKWARD = tuple(tuple(translated(n, tuple(-x for x in v)) for n in range(27))
                 for v in DIRECTIONS)
SHELL_FORWARD = tuple(tuple(translated(n, v) for n in range(27)) for v in SHELL)
SHELL_COEFF = tuple(F(WEIGHTS[sum(x * x for x in v)], 324) for v in SHELL)


def accumulate(out, key, value):
    if value == NIL:
        return
    result = plus(out.get(key, NIL), value)
    if result == NIL:
        out.pop(key, None)
    else:
        out[key] = result


def field_add(a, b, factor=1):
    out = dict(a)
    for key, value in b.items():
        accumulate(out, key, times_scalar(value, factor))
    return out


def field_scale(a, factor):
    if factor == 0:
        return {}
    return {key: times_scalar(value, factor) for key, value in a.items()
            if times_scalar(value, factor) != NIL}


def field_ring_scale(a, factor):
    return {key: times(value, factor) for key, value in a.items()
            if times(value, factor) != NIL}


def diagonal(a, inverse=False):
    return {key: times_scalar(value, 1 / COEFF[key[0]] if inverse else COEFF[key[0]])
            for key, value in a.items()}


def gradient(vertex):
    result = {}
    for v in range(30):
        for n in range(27):
            value = minus(vertex.get(FORWARD[v][n], NIL), vertex.get(n, NIL))
            if value != NIL:
                result[(v, n)] = value
    return result


def divergence(a):
    # Euclidean adjoint of the forward shift gradient.
    result = {}
    for (v, n), value in a.items():
        accumulate(result, FORWARD[v][n], value)
        accumulate(result, n, times_scalar(value, -1))
    return result


def scalar_laplacian(vertex):
    out = {}
    for n in range(27):
        value = NIL
        for shifts, coeff in zip(SHELL_FORWARD, SHELL_COEFF):
            diff = minus(vertex.get(n, NIL), vertex.get(shifts[n], NIL))
            value = plus(value, times_scalar(diff, coeff))
        if value != NIL:
            out[n] = value
    return out


def component_laplacian(a):
    out = {}
    present = sorted({v for v, _ in a})
    for v in present:
        component = {n: value for (direction, n), value in a.items() if direction == v}
        for n, value in scalar_laplacian(component).items():
            out[(v, n)] = value
    return out


def D_operator(a):
    # Public identity M^-1 K = L - d0 d0* M.
    return field_add(component_laplacian(a), gradient(divergence(diagonal(a))), -1)


def K_operator(a):
    return diagonal(D_operator(a))


def K_from_curl(a):
    # Independent direct d1* diag(c_v c_w) d1, no dense matrices.
    out = {}
    present = {v for v, _ in a}
    for v in range(30):
        for w in range(v + 1, 30):
            if v not in present and w not in present:
                continue
            weight = COEFF[v] * COEFF[w]
            for n in range(27):
                curl = minus(
                    minus(a.get((w, FORWARD[v][n]), NIL), a.get((w, n), NIL)),
                    minus(a.get((v, FORWARD[w][n]), NIL), a.get((v, n), NIL)))
                h = times_scalar(curl, weight)
                accumulate(out, (w, FORWARD[v][n]), h)
                accumulate(out, (w, n), times_scalar(h, -1))
                accumulate(out, (v, FORWARD[w][n]), times_scalar(h, -1))
                accumulate(out, (v, n), h)
    return out


def pairing(a, b, form=g):
    return sum((form(value, b[key]) for key, value in a.items() if key in b), F(0))


def field_energy(a, b):
    ka = K_operator(a)
    return (pairing(b, diagonal(b)) + pairing(a, ka) - pairing(b, ka)) / (2 * Z)


def field_form(a, b, other_a, other_b):
    k_other_a = K_operator(other_a)
    k_other_b = K_operator(other_b)
    return (pairing(b, diagonal(other_b), Omega)
            + pairing(a, k_other_a, Omega)
            - (pairing(b, k_other_a, Omega)
               + pairing(a, k_other_b, Omega)) / 2) / (2 * Z)


def free_step(a, b, backwards=False):
    if not backwards:
        new_b = field_add(b, D_operator(a), -1)
        return field_add(a, new_b), new_b
    old_a = field_add(a, b, -1)
    return old_a, field_add(b, D_operator(old_a))


def free_gamma(a, b):
    transformed_b = field_add(field_scale(b, 4), D_operator(b), -1)
    return pairing(a, K_operator(transformed_b), Omega) / (16 * Z)


def field_mod(a, modulus):
    result = {}
    for key, value in a.items():
        reduced = tuple(residue(x, modulus) for x in value)
        if any(reduced):
            result[key] = reduced
    return result


@dataclass(frozen=True)
class State:
    x: tuple
    y: tuple
    e: tuple
    a: dict
    b: dict


def state_energy(s):
    return (Q(s.x) + Q(s.y) + Q(s.e) + Q(minus(s.y, s.e))
            + field_energy(s.a, s.b))


def state_form(s, t):
    return (Omega(s.x, t.x) + Omega(s.y, t.y) + Omega(s.e, t.e)
            + Omega(minus(s.y, s.e), minus(t.y, t.e))
            + field_form(s.a, s.b, t.a, t.b))


def gamma(s, t):
    return state_form(s, t) / 4


def electric(s):
    return field_scale(diagonal(s.b), 1 / Z)


def gauss_defect(s):
    # Preserved defect; no assertion that every occupied fixture has zero defect.
    result = divergence(electric(s))
    accumulate(result, ORIGIN, times_scalar(s.x, -1))
    accumulate(result, FORWARD[MARK_DIRECTION][ORIGIN], times_scalar(s.y, -1))
    return result


def contact(s, backwards=False):
    ka = K_operator(s.a)
    f_mark = minus(times_scalar(s.b.get(MARK, NIL), COEFF[MARK_DIRECTION] / Z),
                   times_scalar(ka.get(MARK, NIL), 1 / (2 * Z)))
    d = times_scalar(plus(minus(minus(times_scalar(s.y, 2), s.x), s.e),
                          f_mark), F(1, 4))
    if not is_integral(d):
        return s, False, d, NIL
    current = minus(times(RHO_BACK if backwards else RHO, d), d)
    b = field_add(s.b, {MARK: times_scalar(current, Z / COEFF[MARK_DIRECTION])})
    return State(minus(s.x, current), plus(s.y, current), s.e, s.a, b), True, d, current


def free_state(s, backwards=False):
    a, b = free_step(s.a, s.b, backwards)
    return State(s.x, s.y, s.e, a, b)


def ordinary_pair(p, q):
    relative = times_scalar(minus(p, q), F(1, 2))
    if not is_integral(relative):
        return p, q
    center = times_scalar(plus(p, q), F(1, 2))
    if not is_integral(center):
        raise ArithmeticError("contact parity inconsistency")
    relative = times(RHO, relative)
    return plus(center, relative), minus(center, relative)


def pair_power(p, q, power):
    for _ in range(power % 5):
        p, q = ordinary_pair(p, q)
    return p, q


def encoded(label):
    low, high = label % 5, (label // 5) % 5
    return (ROOTS[low], times_scalar(ROOTS[low], -1),
            ROOTS[high], times_scalar(ROOTS[high], -1))


def decoded(pointers):
    digits = []
    for k in (0, 2):
        found = next((r for r in range(5)
                      if pointers[k] == ROOTS[r]
                      and pointers[k + 1] == times_scalar(ROOTS[r], -1)), None)
        if found is None:
            return None
        digits.append(found)
    return digits[0] + 5 * digits[1]


def pointer_update(pointers, increment):
    label = decoded(pointers)
    if label is None:
        # Explicit supplied total extension outside the prepared orbit.
        return pointers
    target = (label + increment) % 25
    old_digits = (label % 5, label // 5)
    new_digits = (target % 5, target // 5)
    out = []
    for digit in range(2):
        delta = new_digits[digit] - old_digits[digit]
        out.extend(pair_power(pointers[2 * digit], pointers[2 * digit + 1], 3 * delta))
    return tuple(out)


def lifted_operation(s, pointers, kind, backwards=False):
    if kind == "contact":
        t, _, _, _ = contact(s, backwards)
    elif kind == "free":
        t = free_state(s, backwards)
    else:
        raise ValueError("operation")
    action = gamma(s, t)
    return t, pointer_update(pointers, residue(action, 25)), action


def macrostep(s, pointers, backwards=False):
    kinds = ("free", "contact") if backwards else ("contact", "free")
    total = F(0)
    for kind in kinds:
        s, pointers, action = lifted_operation(s, pointers, kind, backwards)
        total += action
    return s, pointers, total


def reader(pair):
    p, q = pair
    helpers = [times_scalar(root, -1) for root in ROOTS]
    twins = tuple(helpers)
    for k in range(5):
        p, helpers[k] = ordinary_pair(p, helpers[k])
    return p, q, tuple(helpers), twins


def reader_inverse(state):
    p, q, active, twins = state
    active = list(active)
    for k in range(4, -1, -1):
        p, active[k] = pair_power(p, active[k], 4)
    return p, q, tuple(active), twins


def reader_account(state):
    p, q, active, twins = state
    return Q(p) + Q(q) + sum((Q(v) for v in active + twins), F(0))


def first_changed(state):
    _, _, active, twins = state
    return next(k for k in range(5) if active[k] != twins[k])


def mode(amplitude):
    return {(MODE_DIRECTION, n): times_scalar(amplitude, 2 if sum(site) % 3 == 0 else -1)
            for n, site in enumerate(SITES)}


def exact_loaded_fixture(a, b, displacement, source):
    x, y, e = source
    ka = K_operator(a)
    target_f = plus(minus(times_scalar(displacement, 4), times_scalar(y, 2)),
                    plus(x, e))
    adjusted = dict(b)
    adjusted[MARK] = plus(times_scalar(target_f, 2),
                          times_scalar(ka.get(MARK, NIL), 1 / Z))
    if adjusted[MARK] == NIL:
        adjusted.pop(MARK)
    return State(x, y, e, a, adjusted)


def main():
    same(len(SHELL), 60, "complete shell size")
    same(len(DIRECTIONS), 30, "oriented direction count")
    same(tuple(sum(sum(x*x for x in v) == n for v in SHELL) for n in WEIGHTS),
         (12, 6, 12, 24, 6), "shell multiplicities")
    same(sum(SHELL_COEFF), F(8, 9), "full scalar diagonal")
    same(COEFF[MARK_DIRECTION], F(1, 54), "marked coefficient")
    same(Q(J), F(3), "cyclotomic metric normalization")
    same(Omega(UNIT, ROOT), F(1), "marked alternating orientation")
    delta = {MARK: UNIT}
    same(K_operator(delta).get(MARK), times_scalar(UNIT, F(23, 1458)),
         "published marked K diagonal")

    grad = gradient({ORIGIN: UNIT})
    shifted_grad = gradient({SITE_INDEX[(1, 0, 0)]: ROOT})
    alternate = (DIRECTIONS.index((1, 0, 1)), SITE_INDEX[(0, 1, 0)])
    third = (DIRECTIONS.index((2, 0, 0)), SITE_INDEX[(2, 0, 1)])
    fixtures = (
        ({}, {}),
        (mode(UNIT), mode(ROOT)),
        (mode(J), mode(PHI)),
        (delta, {}),
        ({}, {MARK: J}),
        (grad, shifted_grad),
        (field_add(delta, {alternate: PHI}),
         {third: J, alternate: times_scalar(UNIT, F(1, 2))}),
        (field_add(field_scale(mode(UNIT), F(1, 2)), field_scale(grad, F(1, 3))),
         field_scale(mode(ROOT), F(1, 3))),
    )
    for a, b in fixtures:
        same(K_operator(a), K_from_curl(a), "K identity versus direct curl on A")
        same(K_operator(b), K_from_curl(b), "K identity versus direct curl on B")
        new_a, new_b = free_step(a, b)
        same(free_step(new_a, new_b, True), (a, b), "full-field literal free inverse")
        same(field_energy(new_a, new_b), field_energy(a, b), "free field account")
        require(field_energy(a, b) >= 0, "fixture nonnegative field account")
        same(divergence(diagonal(new_b)), divergence(diagonal(b)), "free Gauss")
        same(field_form(a, b, a, b), F(0), "alternating self-pairing")
        same(field_form(a, b, new_a, new_b) / 4, free_gamma(a, b),
             "free Gamma direct versus reduced formula")
        residue(free_gamma(a, b), 25)

    a0, b0 = mode(UNIT), mode(ROOT)
    same(divergence(diagonal(a0)), {}, "explicit transverse A")
    same(divergence(diagonal(b0)), {}, "explicit transverse B")
    same(D_operator(a0), field_scale(a0, F(3, 4)), "exact mode eigenvalue A")
    same(D_operator(b0), field_scale(b0, F(3, 4)), "exact mode eigenvalue B")
    same(pairing(a0, diagonal(a0)), F(2), "explicit weighted half-trace mode norm")
    initial = State(NIL, NIL, NIL, a0, b0)
    same(state_energy(initial), F(837, 16), "explicit transverse witness account")
    state = initial
    pointer = encoded(0)
    actions = []
    pointer_history = []
    for _ in range(4):
        source_cut, admitted, d, current = contact(state)
        require(admitted, "source-zero witness collision admitted")
        same((source_cut, d, current), (state, NIL, NIL),
             "source-zero witness collision is exact identity")
        old = state
        state, pointer, action = lifted_operation(state, pointer, "free")
        actions.append(action)
        pointer_history.append(decoded(pointer))
        same(action, F(1053, 256), "explicit free action")
        same(gamma(state, old), -action, "reverse action orientation")
        same(state_energy(state), state_energy(initial), "four-tick account")
    same(field_mod(state.a, 5), field_mod(initial.a, 5), "A return modulo five")
    same(field_mod(state.b, 5), field_mod(initial.b, 5), "B return modulo five")
    require(state != initial, "four ticks are NOT an exact field return")
    same(residue(actions[0], 5), 3, "single action modulo five")
    same(residue(actions[0], 25), 13, "single action modulo twenty-five")
    same(residue(sum(actions), 5), 2, "closed residue path action obstruction")
    same(residue(sum(actions), 25), 2, "four-step encoded accumulated action")
    same(pointer_history, [13, 1, 14, 2], "actual controlled pointer history")
    for _ in range(4):
        state, pointer, _ = lifted_operation(state, pointer, "free", True)
    same((state, pointer), (initial, encoded(0)), "full free/pointer inverse replay")

    pointer_cases = 0
    for label, increment in product(range(25), repeat=2):
        pointer_cases += 1
        old = encoded(label)
        updated = pointer_update(old, increment)
        same(decoded(updated), (label + increment) % 25, "encoded digit addition")
        same(pointer_update(updated, -increment), old, "encoded digit inverse")
        same(sum((Q(v) for v in updated), F(0)), F(8), "two-pair account")
    complements = (
        (NIL, NIL, NIL, NIL),
        (UNIT, NIL, UNIT, times_scalar(UNIT, -1)),
        (UNIT, times_scalar(UNIT, -1), UNIT, NIL),
        (J, times_scalar(J, -1), UNIT, times_scalar(UNIT, -1)),
    )
    for old, increment in product(complements, range(25)):
        same(decoded(old), None, "pointer complement membership")
        same(pointer_update(old, increment), old, "explicit complement identity")

    reader_cases = 0
    for label in range(25):
        reader_cases += 1
        old = encoded(label)
        outputs = (reader(old[:2]), reader(old[2:]))
        same(first_changed(outputs[0]) + 5 * first_changed(outputs[1]),
             label, "actual two-reader digit readout")
        same(sum(reader_account(out) for out in outputs), F(48),
             "pointer and both reference accounts")
        for digit, out in enumerate(outputs):
            restored = reader_inverse(out)
            references = tuple(times_scalar(root, -1) for root in ROOTS)
            same(restored, (old[2*digit], old[2*digit+1], references, references),
                 "literal reader inverse with references restored")

    loaded_cases = 0
    for background, d, source in product(
            (fixtures[1], fixtures[5], fixtures[6]), (NIL, J, PHI),
            ((NIL, NIL, NIL), (UNIT, times_scalar(UNIT, -1), UNIT))):
        loaded_cases += 1
        base = exact_loaded_fixture(background[0], background[1], d, source)
        new, accepted, seen_d, current = contact(base)
        require(accepted, "engineered loaded admission")
        same(seen_d, d, "loaded displacement fixture")
        same(state_energy(new), state_energy(base), "complete loaded field account")
        same(gauss_defect(new), gauss_defect(base), "actual current Gauss compatibility")
        same(contact(new, True)[0], base, "loaded complete inverse")
        same(gamma(base, new), norm_coefficients(d)[1], "collision Gamma equals B(d)")
        field_work = field_energy(new.a, new.b) - field_energy(base.a, base.b)
        require(field_work.denominator == 1, "integral admitted full-field work")
        base_pointer = encoded(7)
        walked, pointer = base, base_pointer
        action_sum = F(0)
        for _ in range(5):
            walked, pointer, action = lifted_operation(walked, pointer, "contact")
            action_sum += action
        same(walked, base, "exact five-collision full-field base return")
        same(action_sum, 5 * norm_coefficients(d)[1], "exact collision-cycle action")
        same(decoded(pointer), (7 + 5 * int(norm_coefficients(d)[1])) % 25,
             "old five-root monodromy as encoded twenty-five label")
        advanced, phase, _ = macrostep(base, encoded(0))
        same(state_energy(advanced), state_energy(base), "source propagation common account")
        same(gauss_defect(advanced), gauss_defect(base), "macrostep Gauss compatibility")
        returned, returned_phase, _ = macrostep(advanced, phase, True)
        same((returned, returned_phase), (base, encoded(0)), "actual macrostep pointer inverse")

    refused_cases = 0
    for fractional in (F(1, 2), F(1, 3)):
        refused_cases += 1
        base = State(NIL, NIL, NIL, {}, {MARK: times_scalar(UNIT, fractional)})
        new, accepted, _, current = contact(base)
        require(not accepted, "fractional full-field collision refusal")
        same(new, base, "refused entire collision identity")
        same(current, NIL, "refused zero current")
        same(gamma(base, new), F(0), "refused zero action")
        advanced, pointer, _ = macrostep(base, encoded(9))
        back, pointer_back, _ = macrostep(advanced, pointer, True)
        same((back, pointer_back), (base, encoded(9)), "refused macrostep full inverse")

    history_outputs = []
    for amplitude, expected in ((1, [True, False, False]), (216, [True, True, False])):
        e = times_scalar(J, amplitude)
        initial = State(e, times_scalar(e, -1), e, {}, {})
        state, pointer = initial, encoded(0)
        decisions = []
        actual_work = []
        labels = []
        for tick in range(3):
            after_contact, admitted, proposed_d, _ = contact(state)
            if amplitude == 1 and tick == 1:
                same(proposed_d, number((F(85, 108), F(193, 216),
                                        F(-23, 216), F(193, 216))),
                     "published second cold J displacement")
            decisions.append(admitted)
            actual_work.append(field_energy(after_contact.a, after_contact.b)
                               - field_energy(state.a, state.b))
            state, pointer, _ = macrostep(state, pointer)
            labels.append(decoded(pointer))
            same(state_energy(state), state_energy(initial), "cold actual macrostep account")
            same(gauss_defect(state), gauss_defect(initial), "cold preserved Gauss defect")
        same(decisions, expected, "cold actual admission inventory")
        same(actual_work[0], F(5 * amplitude * amplitude),
             "published first funded field impulse")
        require(all(value.denominator == 1 for value in actual_work),
                "cold archived works are integers")
        for _ in range(3):
            state, pointer, _ = macrostep(state, pointer, True)
        same((state, pointer), (initial, encoded(0)), "cold entire inverse replay")
        history_outputs.append((amplitude, "".join("1" if x else "0" for x in decisions),
                                ",".join(str(x) for x in actual_work),
                                ",".join(str(x) for x in labels)))

    print("scope=NON-CANONICAL L1; new declared quotient, not original bundle replay")
    print("carrier=27 sites,30 labelled directions; exact Fraction cyclotomic arithmetic")
    print("field_fixtures=%d direct_curl_comparisons=%d loaded_cases=%d refused_cases=%d"
          % (len(fixtures), 2*len(fixtures), loaded_cases, refused_cases))
    print("Gamma=1053/256; residues_mod5=3,mod25=13; four_tick_sum_residue=2")
    print("four_tick_base_return=MOD5_ONLY; exact_field_return=FALSE")
    print("encoded_pointer_cases=%d complement_cases=100 reader_cases=%d reader_account=48"
          % (pointer_cases, reader_cases))
    for amplitude, bits, works, labels in history_outputs:
        print("cold_amplitude=%d admissions=%s field_works=%s pointer_labels=%s"
              % (amplitude, bits, works, labels))
    print("assertions=%d PASS" % CHECKS)


if __name__ == "__main__":
    main()
