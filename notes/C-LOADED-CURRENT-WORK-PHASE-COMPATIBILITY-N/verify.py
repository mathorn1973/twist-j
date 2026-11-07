# SPDX-License-Identifier: Apache-2.0
"""Exact local collision audit; no lattice propagation or physical phase claim.

This source is prospective until a separately recorded immutable pin and run.
All arithmetic is rational. The finite inventories are explicit in main().
The new centered carry is not the source-only carry of issue #1924.
"""
from dataclasses import dataclass, replace
from fractions import Fraction as F
from itertools import product

ASSERTIONS = 0


def check(condition, label):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(label)


def eq(actual, expected, label):
    check(actual == expected, label)


def ring(values):
    if isinstance(values, (int, F)):
        return (F(values), F(0), F(0), F(0))
    if len(values) != 4:
        raise ValueError("four coefficients required")
    return tuple(F(v) for v in values)


ZERO = ring(0)
ONE = ring(1)
JROOT = ring((0, 1, 0, 0))


def add(a, b):
    return tuple(a[k] + b[k] for k in range(4))


def neg(a):
    return tuple(-v for v in a)


def sub(a, b):
    return add(a, neg(b))


def scale(a, n):
    return tuple(F(n) * v for v in a)


def mul(a, b):
    coeff = [F(0)] * 7
    for r in range(4):
        for s in range(4):
            coeff[r + s] += a[r] * b[s]
    for degree in range(6, 3, -1):
        value = coeff[degree]
        coeff[degree] = F(0)
        for offset in range(1, 5):
            coeff[degree - offset] -= value
    return tuple(coeff[:4])


JPOW = [ONE]
for _ in range(4):
    JPOW.append(mul(JPOW[-1], JROOT))
RHO = JPOW[2]
RHO_INV = JPOW[3]
J = add(ONE, RHO)
PHI = neg(add(JPOW[2], JPOW[3]))


def conj(a):
    result = ZERO
    for k, coefficient in enumerate(a):
        result = add(result, scale(JPOW[(-k) % 5], coefficient))
    return result


def hermitian(a):
    return mul(a, conj(a))


def ab(a):
    value = hermitian(a)
    if value[1] != 0 or value[2] != value[3]:
        raise ArithmeticError("non-real Hermitian product")
    return value[0], -value[2]


def q(a):
    return (5 * sum(v * v for v in a) - sum(a) ** 2) / 2


def twice_g(a, b):
    return q(add(a, b)) - q(a) - q(b)


def omega(a, b):
    return sum(a[k] * b[k + 1] - a[k + 1] * b[k]
               for k in range(3))


def integral(a):
    return all(v.denominator == 1 for v in a)


def mod5(value):
    value = F(value)
    if value.denominator % 5 == 0:
        raise ArithmeticError("mod-five value has a forbidden denominator")
    return value.numerator * pow(value.denominator, -1, 5) % 5


def fhat(a):
    a0, a1, a2, a3 = map(mod5, a)
    z0 = (a0 + a1 + a2 + a3) % 5
    z1 = (a1 + 2 * a2 + 3 * a3) % 5
    z2 = (3 * a1 + 2 * a2 + 2 * a3) % 5
    z3 = (a1 + 3 * a2 + 2 * a3) % 5
    return (2 * z0 * z3 + z1 * z2) % 5


def centered_carry(d):
    if not integral(d):
        raise ArithmeticError("centered carry requires integral displacement")
    _, beta = ab(d)
    numerator = beta - 2 * (fhat(mul(RHO, d)) - fhat(d))
    value = numerator / 5
    if value.denominator != 1:
        raise ArithmeticError("nonintegral centered carry")
    return int(value)


@dataclass(frozen=True)
class Core:
    x: tuple
    y: tuple
    e: tuple
    field: tuple


def displacement(s):
    return scale(add(sub(scale(s.y, 2), s.x),
                     sub(s.field, s.e)), F(1, 4))


def source_energy(s):
    return q(s.x) + q(s.y) + q(s.e) + q(sub(s.y, s.e))


def core_energy(s):
    # At a=1 and fixed A=0 the marked field term is Q(field).
    return source_energy(s) + q(s.field)


def collision(s, direction=1):
    if direction not in (-1, 1):
        raise ValueError("direction")
    d = displacement(s)
    if not integral(d):
        return s, False, d, ZERO
    rotation = RHO if direction == 1 else RHO_INV
    current = sub(mul(rotation, d), d)
    out = Core(sub(s.x, current), add(s.y, current),
               s.e, add(s.field, current))
    return out, True, d, current


def ordinary_contact(p, r):
    midpoint = scale(add(p, r), F(1, 2))
    relative = scale(sub(p, r), F(1, 2))
    if not integral(relative):
        return p, r
    if not integral(midpoint):
        raise ArithmeticError("parity inconsistency")
    turned = mul(RHO, relative)
    return add(midpoint, turned), sub(midpoint, turned)


def pointer_power(p, r, power):
    for _ in range(power % 5):
        p, r = ordinary_contact(p, r)
    return p, r


@dataclass(frozen=True)
class Lift:
    core: Core
    p: tuple
    r: tuple


def lifted_step(s, direction=1):
    out, admitted, d, current = collision(s.core, direction)
    if not admitted:
        return s, 0, current
    if direction == 1:
        carry = centered_carry(d)
    else:
        carry = -centered_carry(mul(RHO_INV, d))
    p, r = pointer_power(s.p, s.r, 3 * carry)
    return Lift(out, p, r), carry, current


def lifted_energy(s):
    return core_energy(s.core) + q(s.p) + q(s.r)


@dataclass(frozen=True)
class Funded:
    """Single running-total register, not a retained work history."""
    lifted: Lift
    archive: int
    funding: int
    direction: int


def reflected(s):
    return replace(s, direction=-s.direction)


def funded_step(s):
    proposed, _, _ = lifted_step(s.lifted, s.direction)
    work = q(proposed.core.field) - q(s.lifted.core.field)
    if work.denominator != 1:
        raise ArithmeticError("nonintegral archived work")
    archive = s.archive + int(work)
    funding = s.funding - (archive * archive - s.archive * s.archive)
    if funding < 0:
        return reflected(s), False
    return Funded(proposed, archive, funding, s.direction), True


def funded_inverse(s):
    out, _ = funded_step(reflected(s))
    return reflected(out)


def funded_energy(s):
    return lifted_energy(s.lifted) + s.archive ** 2 + s.funding



@dataclass(frozen=True)
class Calendar:
    """Three distinct finite-horizon record ports with a cyclic Z/4 calendar."""
    lifted: Lift
    archives: tuple
    clock: int


def calendar_proposal(s, direction):
    if len(s.archives) != 3 or s.clock not in range(4):
        raise ValueError("three archives and clock modulo four required")
    archives = list(s.archives)
    if direction == 1:
        next_lift, _, _ = lifted_step(s.lifted, 1)
        signed_work = q(next_lift.core.field) - q(s.lifted.core.field)
        port = s.clock
        clock = (s.clock + 1) % 4
    elif direction == -1:
        # Recover the old calendar port, then reverse the lifted step ONCE.
        port = (s.clock - 1) % 4
        next_lift, _, _ = lifted_step(s.lifted, -1)
        signed_work = q(next_lift.core.field) - q(s.lifted.core.field)
        clock = port
    else:
        raise ValueError("direction")
    if signed_work.denominator != 1:
        raise ArithmeticError("nonintegral calendar work")
    if port < 3:
        archives[port] += int(signed_work)
    return Calendar(next_lift, tuple(archives), clock)


def archive_price(s):
    return sum(value * value for value in s.archives)


@dataclass(frozen=True)
class CalendarFunded:
    calendar: Calendar
    funding: int
    direction: int


def calendar_reflected(s):
    return replace(s, direction=-s.direction)


def calendar_funded_step(s):
    proposed = calendar_proposal(s.calendar, s.direction)
    funding = s.funding - (archive_price(proposed) - archive_price(s.calendar))
    if funding < 0:
        return calendar_reflected(s), False
    return CalendarFunded(proposed, funding, s.direction), True


def calendar_funded_inverse(s):
    out, _ = calendar_funded_step(calendar_reflected(s))
    return calendar_reflected(out)


def calendar_energy(s):
    return lifted_energy(s.calendar.lifted) + archive_price(s.calendar) + s.funding


def make_core(d, seed):
    x, y, e = seed
    field = add(sub(scale(d, 4), scale(y, 2)), add(x, e))
    return Core(x, y, e, field)


def main():
    eq(mul(JROOT, JPOW[4]), ONE, "j order five")
    eq(mul(PHI, PHI), add(ONE, PHI), "golden relation")
    eq(ab(J), (F(2), F(-1)), "J Hermitian coefficients")
    eq(ab(PHI), (F(1), F(1)), "phi Hermitian coefficients")
    ds = tuple(ring(v) for v in product((-1, 0, 1), repeat=4))
    seeds = (
        (ZERO, ZERO, ZERO),
        (ONE, neg(ONE), ONE),
        (J, neg(J), J),
        (ONE, ZERO, ZERO),
        (ZERO, ONE, PHI),
        (PHI, J, ONE),
        (add(ONE, J), sub(PHI, J), PHI),
    )
    pointers = (
        (ZERO, ZERO),
        (ONE, ZERO),
        (ONE, neg(ONE)),
        (J, neg(J)),
        (add(ONE, J), sub(ONE, J)),
    )
    collision_cases = 0
    occupied_pointer_cases = 0
    for d in ds:
        alpha, beta = ab(d)
        eq(q(d), 2 * alpha + beta, "half-trace metric")
        eq(omega(d, mul(RHO, d)), beta, "marked alternating form")
        eq(mod5(2 * (fhat(mul(RHO, d)) - fhat(d))),
           mod5(beta), "centered modular potential")
        check(isinstance(centered_carry(d), int), "integer carry")
        current_d = sub(mul(RHO, d), d)
        eq(q(current_d) - q(mul(J, current_d)), 5 * beta,
           "actual-current two-metric identity")
        for seed in seeds:
            collision_cases += 1
            core = make_core(d, seed)
            eq(displacement(core), d, "fixture displacement")
            new, accepted, observed_d, current = collision(core)
            check(accepted, "declared fixture admission")
            eq(observed_d, d, "actual displacement")
            eq(current, current_d, "actual current")
            eq(add(new.x, new.y), add(core.x, core.y), "source continuity")
            eq(sub(new.field, new.y), sub(core.field, core.y),
               "field-source offset")
            eq(new.e, core.e, "spectator retention")
            eq(displacement(new), mul(RHO, d), "centered rotation")
            eq(core_energy(new), core_energy(core), "complete local account")
            work = q(new.field) - q(core.field)
            check(work.denominator == 1, "integral field work")
            eq(work, source_energy(core) - source_energy(new),
               "source pays signed field work")
            weighted_area = (
                omega(core.x, new.x) + omega(core.y, new.y)
                + omega(sub(core.y, core.e), sub(new.y, new.e))
                + omega(core.field, new.field))
            eq(weighted_area, 4 * beta, "complete weighted alternating identity")
            second, second_accepted, _, second_current = collision(new)
            check(second_accepted, "second fixed-center admission")
            eq(second_current, mul(RHO, current), "actual second current")
            cumulative_second_work = q(second.field) - q(core.field)
            eq(work - cumulative_second_work
               + twice_g(core.field, second_current), 5 * beta,
               "occupied fixed-center corrected work identity")
            ai, bi = ab(current)
            eq(((3 * ai - bi) / 5, (2 * bi - ai) / 5),
               (alpha, beta), "transported current Hermitian metric")
            eq(q(d), ai, "transported current half-trace")
            eq(5 * beta, 2 * bi - ai, "current coefficient divisibility")
            eq(mul(J, current), add(current, second_current),
               "fixed-center accumulated two-contact current")
            back, accepted_back, _, _ = collision(new, -1)
            check(accepted_back, "inverse admission")
            eq(back, core, "literal collision inverse")
            ready = Lift(core, ONE, neg(ONE))
            walk = ready
            carry_sum = 0
            work_sum = F(0)
            for _ in range(5):
                previous = walk
                walk, carry, _ = lifted_step(walk)
                carry_sum += carry
                work_sum += q(walk.core.field) - q(previous.core.field)
                eq(lifted_energy(walk), lifted_energy(ready),
                   "lifted account")
            eq(walk.core, core, "five-collision base return")
            eq(carry_sum, beta, "five-collision carry")
            eq(work_sum, F(0), "closed field work")
            eq(walk.p, JPOW[int(beta) % 5], "prepared pointer phase")
            eq(walk.r, neg(walk.p), "neutral pointer")
            for _ in range(20):
                walk, _, _ = lifted_step(walk)
            eq(walk, ready, "twenty-five-collision complete return")
            for p, r in pointers:
                occupied_pointer_cases += 1
                initial = Lift(core, p, r)
                advanced, _, _ = lifted_step(initial)
                returned, _, _ = lifted_step(advanced, -1)
                eq(returned, initial, "occupied lifted inverse")
                eq(add(advanced.p, advanced.r), add(p, r),
                   "occupied pointer sum")
                eq(q(advanced.p) + q(advanced.r), q(p) + q(r),
                   "occupied pointer account")

    refusal_fields = (ONE, J, PHI, scale(ONE, F(1, 2)))
    for field in refusal_fields:
        state = Core(ZERO, ZERO, ZERO, field)
        for direction in (-1, 1):
            out, admitted, _, current = collision(state, direction)
            check(not admitted, "nonintegral collision refusal")
            eq(out, state, "refused base identity")
            eq(current, ZERO, "refused current")
            lift = Lift(state, J, neg(J))
            advanced, carry, _ = lifted_step(lift, direction)
            eq(advanced, lift, "refused lift identity")
            eq(carry, 0, "refused carry")

    # Exact failure of the UNCHANGED source-only modular carry.
    obstruction = Core(ONE, neg(ONE), ONE, add(scale(J, 4), scale(ONE, 4)))
    target, admitted, d, current = collision(obstruction)
    check(admitted, "obstruction admitted")
    eq(d, J, "obstruction displacement")
    eq(current, ring((-2, -1, -1, -1)), "obstruction current")
    eq(target.x, ring((3, 1, 1, 1)), "obstruction source endpoint")
    area = (omega(obstruction.x, target.x)
            + omega(obstruction.y, target.y)) / 2
    psi_change = (fhat(target.x) + fhat(target.y)
                  - fhat(obstruction.x) - fhat(obstruction.y))
    eq(area, F(1), "old source area")
    eq(psi_change, 8, "old source potential change")
    eq(area - psi_change, F(-7), "old carry numerator")
    check((area - psi_change) / 5 != int((area - psi_change) / 5),
          "old source-only carry fails")
    eq((q(obstruction.field), q(target.field)), (F(128), F(93)),
       "obstruction field accounts")
    eq(q(target.field) - q(obstruction.field), F(-35),
       "obstruction actual field work")
    eq(q(sub(obstruction.y, obstruction.e))
       - q(sub(target.y, target.e)), F(-15),
       "obstruction potential work")

    # Both are exact local five-cycles. No free-field tick is inserted.
    zero_phase_outputs = []
    for d, beta, current_norm in ((J, -1, 5), (PHI, 1, 10)):
        core = Core(neg(d), d, ZERO, d)
        state = Lift(core, ONE, neg(ONE))
        eq(core_energy(core), F(12), "zero-work core account")
        eq(lifted_energy(state), F(16), "zero-work complete account")
        accumulated = 0
        for _ in range(5):
            prior = state
            state, carry, current = lifted_step(state)
            accumulated += carry
            eq(q(state.core.field) - q(prior.core.field), F(0),
               "zero field work")
            eq(q(sub(state.core.y, state.core.e)),
               q(sub(prior.core.y, prior.core.e)), "zero potential work")
            eq(q(current), F(current_norm), "zero-work actual current norm")
            eq(ordinary_contact(prior.core.x, prior.core.y),
               (state.core.x, state.core.y), "literal ordinary source contact")
            old_area = (omega(prior.core.x, state.core.x)
                        + omega(prior.core.y, state.core.y)) / 2
            old_delta_psi = (
                fhat(state.core.x) + fhat(state.core.y)
                - fhat(prior.core.x) - fhat(prior.core.y))
            old_carry = (old_area - old_delta_psi) / 5
            check(old_carry.denominator == 1, "inherited integer source carry")
            eq(old_carry, carry, "inherited and centered carries agree")
        eq(state.core, core, "zero-work base cycle")
        eq(accumulated, beta, "zero-work nontrivial carry")
        eq(state.p, JPOW[beta % 5], "zero-work pointer phase")
        zero_phase_outputs.append(state.p)
    check(zero_phase_outputs[0] != zero_phase_outputs[1],
          "equal scalar work does not fix centered phase")

    funded_ds = (ZERO, ONE, neg(ONE), J, neg(J), PHI, neg(PHI),
                 add(ONE, J), neg(add(ONE, J)))
    funded_cases = 0
    affordable = 0
    unaffordable = 0
    for d, seed, archive, funding, direction in product(
            funded_ds, seeds[:3], (-2, 0, 3), (0, 1, 25), (-1, 1)):
        funded_cases += 1
        lifted = Lift(make_core(d, seed), add(ONE, J), sub(ONE, J))
        initial = Funded(lifted, archive, funding, direction)
        advanced, accepted = funded_step(initial)
        affordable += int(accepted)
        unaffordable += int(not accepted)
        check(advanced.funding >= 0, "nonnegative archive funding")
        eq(funded_energy(advanced), funded_energy(initial),
           "funded total account")
        eq(funded_inverse(advanced), initial, "complete funded inverse")
    check(affordable > 0 and unaffordable > 0,
          "funded inventory covers both branches")
    cold = Lift(Core(J, neg(J), J, ZERO), ONE, neg(ONE))
    refused = Funded(cold, 0, 24, 1)
    out, accepted = funded_step(refused)
    check(not accepted, "one-unit funding shortfall")
    eq(out, reflected(refused), "funding refusal changes only direction")
    adequate = Funded(cold, 0, 25, 1)
    out, accepted = funded_step(adequate)
    check(accepted, "sharp first-record funding")
    eq((out.archive, out.funding), (5, 0), "first running-total work record")
    eq(funded_energy(adequate), F(50), "cold source pointer archive account")
    eq(funded_inverse(out), adequate, "accepted archive inverse")


    # This receiver retains the first three actual works in DISTINCT ports.
    archive_seeds = ((0, 0, 0), (1, -2, 3), (-3, 2, -1))
    calendar_cases = 0
    calendar_affordable = 0
    calendar_unaffordable = 0
    for d, seed, archives, funding, clock, direction in product(
            funded_ds, seeds[:3], archive_seeds, (0, 1, 25),
            range(4), (-1, 1)):
        calendar_cases += 1
        occupied = Lift(make_core(d, seed), add(ONE, J), sub(ONE, J))
        calendar = Calendar(occupied, archives, clock)
        proposal = calendar_proposal(calendar, direction)
        recovered = calendar_proposal(proposal, -direction)
        eq(recovered, calendar, "unfunded calendar literal inverse")
        expected_lift, _, _ = lifted_step(occupied, direction)
        eq(proposal.lifted, expected_lift, "exactly one lifted step per calendar")
        initial = CalendarFunded(calendar, funding, direction)
        advanced, accepted = calendar_funded_step(initial)
        calendar_affordable += int(accepted)
        calendar_unaffordable += int(not accepted)
        check(advanced.funding >= 0, "nonnegative calendar funding")
        eq(calendar_energy(advanced), calendar_energy(initial),
           "retained-port complete account")
        eq(calendar_funded_inverse(advanced), initial,
           "retained-port occupied inverse")
        if not accepted:
            eq(advanced, calendar_reflected(initial),
               "retained-port refusal changes only direction")
    check(calendar_affordable > 0 and calendar_unaffordable > 0,
          "calendar inventory covers both affordability branches")

    refused_calendar_cases = 0
    for field, clock, direction in product(refusal_fields, range(4), (-1, 1)):
        refused_calendar_cases += 1
        lift = Lift(Core(ZERO, ZERO, ZERO, field), ONE, neg(ONE))
        calendar = Calendar(lift, (1, -2, 3), clock)
        initial = CalendarFunded(calendar, 0, direction)
        advanced, accepted = calendar_funded_step(initial)
        check(accepted, "zero-work refused collision remains affordable")
        eq(advanced.calendar.lifted, lift, "refused collision leaves lift fixed")
        eq(advanced.calendar.archives, calendar.archives,
           "refused collision writes zero")
        eq(advanced.calendar.clock, (clock + direction) % 4,
           "calendar also advances on collision refusal")
        eq(calendar_funded_inverse(advanced), initial,
           "refused-collision calendar inverse")

    ready_calendar_cases = 0
    positive_cost_cases = 0
    for d, seed in product(ds, seeds):
        ready_calendar_cases += 1
        ready_lift = Lift(make_core(d, seed), ONE, neg(ONE))
        preview = ready_lift
        works = []
        for _ in range(3):
            previous = preview
            preview, _, _ = lifted_step(preview)
            value = q(preview.core.field) - q(previous.core.field)
            check(value.denominator == 1, "ready-horizon integer work")
            works.append(int(value))
        price = sum(value * value for value in works)
        ready_calendar = Calendar(ready_lift, (0, 0, 0), 0)
        ready = CalendarFunded(ready_calendar, price, 1)
        state = ready
        prefix_price = 0
        for count in range(1, 4):
            previous = state
            state, accepted = calendar_funded_step(state)
            check(accepted, "sharp horizon funding suffices at every prefix")
            prefix_price += works[count - 1] ** 2
            eq(state.calendar.archives,
               tuple(works[:count] + [0] * (3 - count)),
               "distinct ports retain each acquired actual work")
            eq(state.calendar.archives[:count - 1],
               previous.calendar.archives[:count - 1],
               "earlier acquired ports remain unchanged")
            eq(state.calendar.clock, count, "acquisition calendar")
            eq(state.funding, price - prefix_price, "exact prefix funding")
            eq(calendar_energy(state), calendar_energy(ready),
               "ready-horizon complete account")
        eq(state.calendar.lifted, preview, "three actual lifted steps")
        eq(state.funding, 0, "sharp endpoint funding exhausted")
        for _ in range(3):
            state = calendar_funded_inverse(state)
        eq(state, ready, "three-step complete receiver inverse")
        if price > 0:
            positive_cost_cases += 1
            short = CalendarFunded(ready_calendar, price - 1, 1)
            first_refusal = max(k for k, value in enumerate(works) if value != 0)
            for k in range(first_refusal + 1):
                previous = short
                short, accepted = calendar_funded_step(short)
                eq(accepted, k < first_refusal, "one-unit shortfall threshold")
            eq(short, calendar_reflected(previous),
               "first unaffordable record is preserved as refusal")
            eq(calendar_funded_inverse(short), previous,
               "funding-reflection inverse")
    check(positive_cost_cases > 0, "ready inventory includes nonzero record cost")

    print("scope=NON-CANONICAL L1 local a=1 collision; no free-field replay")
    print("ring_displacements=%d collision_cases=%d occupied_pointer_cases=%d"
          % (len(ds), collision_cases, occupied_pointer_cases))
    print("refused_cores=%d zero_work_cycles=2 running_total_cases=%d"
          % (len(refusal_fields), funded_cases))
    print("old_source_carry_numerator=-7; new_centered_cycle_carry=B(d)")
    print("actual_current_identity=Q(i)-Q(J*i)=5B(d)")
    print("zero_work_phases=J:j^-1,phi:j; complete_account=16")
    print("running_total_branches=accepted:%d,refused:%d"
          % (affordable, unaffordable))
    print("calendar_occupied=%d refused_collision_calendar=%d ready_horizons=%d"
          % (calendar_cases, refused_calendar_cases, ready_calendar_cases))
    print("calendar_branches=accepted:%d,refused:%d positive_cost_horizons=%d"
          % (calendar_affordable, calendar_unaffordable, positive_cost_cases))
    print("assertions=%d PASS" % ASSERTIONS)


if __name__ == "__main__":
    main()
