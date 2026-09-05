"""Independent exact finite audits of the chosen reservoir interaction.

The immutable wave operator is an input. Coupling is checked by a pointwise
solve, not by replaying the implementation's correction to its free step.
No scientific checks run on import.
"""
from fractions import Fraction as F

import coupling as candidate


ORIGIN = (0, 0, 0)
P = (1, 1, 0)
MINUS_P = (-1, -1, 0)
FAR = (40, 0, 0)


def _freeze(values):
    return tuple(sorted((x, F(a)) for x, a in values.items() if a))


def _shift(x, z):
    return tuple(a + b for a, b in zip(x, z))


def _halo(sites, offsets):
    sites = set(sites)
    return sites | {_shift(x, z) for x in sites for z, _ in offsets}


def _lap_at(values, x, offsets):
    return sum((c * (values.get(x, F(0)) - values.get(_shift(x, z), F(0)))
                for z, c in offsets), F(0))


def _forward(pair, context, incoming, offsets):
    u, v, gamma, a = map(dict, (pair.previous, pair.current, context.gamma, incoming))
    domain = _halo(set(u) | set(v), offsets) | set(gamma)
    w = {}
    for x in domain:
        g = gamma.get(x, F(0))
        w[x] = (2 * v.get(x, F(0)) - _lap_at(v, x, offsets)
                - (1 - g / 2) * u.get(x, F(0)) + 2 * g * a.get(x, F(0))) / (1 + g / 2)
    b, forcing, transfer = {}, {}, {}
    for x, g in gamma.items():
        midpoint_velocity = (w.get(x, F(0)) - u.get(x, F(0))) / 2
        b[x] = a.get(x, F(0)) - midpoint_velocity
        forcing[x] = g * (a.get(x, F(0)) + b[x])
        transfer[x] = g * (b[x] ** 2 - a.get(x, F(0)) ** 2)
    return (candidate.wave.Pair(pair.current, _freeze(w)),
            _freeze(b), _freeze(forcing), _freeze(transfer))


def _backward(after, context, outgoing, offsets):
    v, w, gamma, b = map(dict, (after.previous, after.current, context.gamma, outgoing))
    domain = _halo(set(v) | set(w), offsets) | set(gamma)
    u = {}
    for x in domain:
        g = gamma.get(x, F(0))
        u[x] = (2 * v.get(x, F(0)) - _lap_at(v, x, offsets)
                - (1 - g / 2) * w.get(x, F(0)) + 2 * g * b.get(x, F(0))) / (1 + g / 2)
    incoming = {x: b.get(x, F(0)) + (w.get(x, F(0)) - u.get(x, F(0))) / 2
                for x in gamma}
    return candidate.wave.Pair(_freeze(u), after.previous), _freeze(incoming)


def _port_energy(value, gamma):
    values = dict(value)
    return sum((g * values.get(x, F(0)) ** 2 for x, g in gamma), F(0))


def _contexts():
    return tuple(candidate.Context(_freeze(gamma), F(1)) for gamma in (
        {}, {ORIGIN: F(1, 2)}, {ORIGIN: F(2)}, {ORIGIN: F(4)},
        {ORIGIN: F(1, 2), P: F(4)}, {ORIGIN: F(2), P: F(1, 2)},
    ))


def _pairs():
    return tuple(candidate.wave.Pair(_freeze(u), _freeze(v)) for u, v in (
        ({}, {}), ({}, {ORIGIN: F(1)}),
        ({ORIGIN: F(1, 2), P: F(-1, 3)}, {ORIGIN: F(-2, 5), P: F(3, 7)}),
    ))


def _g01_coupling():
    offsets = candidate.wave.stencil()
    for context in _contexts():
        warm = _freeze({x: F(2, 3) if x == ORIGIN else F(-3, 5)
                        for x, _ in context.gamma})
        inputs = ((), warm) if warm else ((),)
        for pair in _pairs():
            for incoming in inputs:
                expected = _forward(pair, context, incoming, offsets)
                actual = candidate.couple(pair, context, incoming)
                assert (actual.after, actual.outgoing, actual.forcing, actual.transfer) == expected
                assert candidate.wave.step(pair, actual.forcing) == actual.after
                reference_inverse = _backward(actual.after, context, actual.outgoing, offsets)
                assert reference_inverse == (pair, incoming)
                assert candidate.reverse(actual.after, context, actual.outgoing) == reference_inverse
                arbitrary_inverse = candidate.reverse(pair, context, incoming)
                assert arbitrary_inverse == _backward(pair, context, incoming, offsets)
                restored = candidate.couple(arbitrary_inverse[0], context, arbitrary_inverse[1])
                assert (restored.after, restored.outgoing) == (pair, incoming)
                energy_in = _port_energy(incoming, context.gamma)
                energy_out = _port_energy(actual.outgoing, context.gamma)
                assert candidate.port_energy(incoming, context) == energy_in
                assert candidate.port_energy(actual.outgoing, context) == energy_out
                assert candidate.wave.energy(actual.after) + energy_out == candidate.wave.energy(pair) + energy_in
                assert sum(dict(actual.transfer).values(), F(0)) == energy_out - energy_in
                if not pair.previous and not pair.current and incoming:
                    assert sum(dict(actual.transfer).values(), F(0)) < 0
                if not context.gamma:
                    assert (actual.outgoing, actual.forcing, actual.transfer) == ((), (), ())
                    assert actual.after == candidate.wave.step(pair)


def _g02_cold_balance():
    wave = candidate.wave
    offsets = wave.stencil()
    context = candidate.Context(_freeze({ORIGIN: F(1, 2), P: F(2)}), F(2, 3))
    for pair in _pairs():
        expected_pair, outgoing, forcing, deposit = _forward(pair, context, (), offsets)
        state = candidate.ready(pair)
        successor, batch = candidate.advance(state, context)
        assert state == candidate.State(pair, (), 0)
        assert successor == candidate.State(expected_pair, deposit, 1)
        assert (batch.tick, batch.outgoing, batch.deposit) == (0, outgoing, deposit)
        u, w, gamma = dict(pair.previous), dict(expected_pair.current), dict(context.gamma)
        losses = {x: g * (w.get(x, F(0)) - u.get(x, F(0))) ** 2 / 4
                  for x, g in gamma.items()}
        assert deposit == _freeze(losses)
        assert all(a >= 0 for a in losses.values())
        assert wave.energy(successor.pair) + sum(losses.values(), F(0)) == wave.energy(pair)
        support = set(dict(pair.previous)) | set(dict(pair.current)) | set(w) | set(gamma)
        domain = _halo(support, offsets)
        regions = [tuple((x,)) for x in sorted(domain)]
        regions.extend(((), (ORIGIN, P), tuple(sorted(domain)), (FAR,)))
        before_density, after_density = map(dict, (wave.density_field(pair), wave.density_field(expected_pair)))
        for sites in regions:
            aperture = wave.Aperture(sites)
            account = wave.balance(pair, expected_pair.current, forcing, aperture)
            local_loss = sum((losses.get(x, F(0)) for x in sites), F(0))
            expected_change = sum((after_density.get(x, F(0)) - before_density.get(x, F(0))
                                   for x in sites), F(0))
            assert account.change == expected_change
            assert account.work == -local_loss
            assert account.residual == 0
            assert account.change + account.outward_flux + local_loss == 0


def _counts(heat, context):
    values = dict(heat)
    answer = []
    for x, _ in context.gamma:
        ratio = values.get(x, F(0)) / context.quantum
        answer.append((x, ratio.numerator // ratio.denominator))
    return tuple(answer)


def _g03_memory():
    gamma = _freeze({ORIGIN: F(2), P: F(1, 2)})
    context = candidate.Context(gamma, F(3, 5))
    heat_cases = ({}, {ORIGIN: F(2, 5), P: F(3, 5)},
                  {ORIGIN: F(9, 5), P: F(21, 10)},
                  {ORIGIN: F(17, 5), P: F(3, 35)})
    for values in heat_cases:
        heat = _freeze(values)
        reference_counts = _counts(heat, context)
        reference_remainders = {x: values.get(x, F(0)) - context.quantum * n
                                for x, n in reference_counts}
        assert candidate.threshold_counts(heat, context) == reference_counts
        assert candidate.remainders(heat, context) == _freeze(reference_remainders)
        assert all(0 <= r < context.quantum for r in reference_remainders.values())
        assert context.quantum * sum(n for _, n in reference_counts) + sum(reference_remainders.values(), F(0)) == sum(values.values(), F(0))
    # A single valid State can start with nonzero heat. Its budget includes that
    # initial heat; only histories generated from ready have a wave-only budget.
    context = candidate.Context(gamma, F(1))
    cases = ((F(1), {}, 0),
             (F(1), {ORIGIN: F(1, 2), P: F(1, 3)}, 7),
             (F(2), {}, 0),
             (F(3), {ORIGIN: F(3, 4)}, 2),
             (F(3), {ORIGIN: F(11, 4)}, 2),
             (F(0), {ORIGIN: F(2)}, 9))
    for amplitude, initial_heat, tick in cases:
        pair = candidate.wave.Pair(_freeze({ORIGIN: amplitude}), ())
        initial = candidate.State(pair, _freeze(initial_heat), tick)
        successor, batch = candidate.advance(initial, context)
        amount = amplitude ** 2 / 2
        expected_heat = dict(initial_heat)
        expected_heat[ORIGIN] = expected_heat.get(ORIGIN, F(0)) + amount
        assert successor == candidate.State(candidate.wave.Pair((), ()), _freeze(expected_heat), tick + 1)
        assert batch.tick == tick
        assert batch.deposit == _freeze({ORIGIN: amount})
        assert batch.outgoing == _freeze({ORIGIN: amplitude / 2})
        old_counts = dict(_counts(initial.heat, context))
        new_counts = dict(_counts(successor.heat, context))
        reference_events = tuple((x, ordinal) for x in sorted(new_counts)
                                 for ordinal in range(old_counts[x] + 1, new_counts[x] + 1))
        observed_events = tuple((crossing.site, ordinal) for crossing in batch.crossings
                                for ordinal in range(crossing.first, crossing.last + 1))
        assert observed_events == reference_events
        assert all(c.count == c.last - c.first + 1 for c in batch.crossings)
        assert sum(c.count for c in batch.crossings) == sum(new_counts.values()) - sum(old_counts.values())
        assert batch.kind == ("THRESHOLD_CROSSINGS" if reference_events else "NO_CROSSINGS")
        remainder = candidate.remainders(successor.heat, context)
        initial_budget = candidate.wave.energy(pair) + sum(initial_heat.values(), F(0))
        assert candidate.wave.energy(successor.pair) + context.quantum * sum(new_counts.values()) + sum(dict(remainder).values(), F(0)) == initial_budget
        again, empty_batch = candidate.advance(successor, context)
        assert again == candidate.State(successor.pair, successor.heat, tick + 2)
        assert (empty_batch.tick, empty_batch.deposit, empty_batch.outgoing,
                empty_batch.crossings, empty_batch.kind) == (tick + 1, (), (), (), "NO_CROSSINGS")
    # Fixed site ledgers are additive as records; flooring a pooled heat is not.
    values = _freeze({ORIGIN: F(3, 5), P: F(3, 5)})
    assert sum(n for _, n in candidate.threshold_counts(values, context)) == 0
    pooled = sum(dict(values).values(), F(0)) / context.quantum
    assert pooled.numerator // pooled.denominator == 1


def _g04_boundaries():
    wave = candidate.wave
    context = candidate.Context(_freeze({ORIGIN: F(2)}), F(1))
    odd_pair = wave.Pair((), _freeze({P: F(1), MINUS_P: F(-1)}))
    assert wave.energy(odd_pair) == 1
    assert wave.density(odd_pair, ORIGIN) == F(1, 216)
    state = candidate.ready(odd_pair)
    for tick in range(3):
        state, batch = candidate.advance(state, context)
        assert state.tick == tick + 1 and batch.tick == tick
        assert state.heat == () and wave.energy(state.pair) == 1
        assert (batch.outgoing, batch.deposit, batch.crossings, batch.kind) == ((), (), (), "NO_CROSSINGS")
        for value in (state.pair.previous, state.pair.current):
            coefficients = dict(value)
            assert coefficients.get(ORIGIN, F(0)) == 0
            assert all(coefficients.get(tuple(-a for a in x), F(0)) == -b
                       for x, b in value)
    perfect_pair = wave.Pair(_freeze({ORIGIN: F(2)}), ())
    state = candidate.ready(perfect_pair)
    state, first = candidate.advance(state, context)
    assert state.pair == wave.Pair((), ())
    assert state.heat == first.deposit == _freeze({ORIGIN: F(2)})
    assert first.outgoing == _freeze({ORIGIN: F(1)})
    assert first.crossings == (candidate.Crossing(ORIGIN, 1, 2),)
    assert first.kind == "THRESHOLD_CROSSINGS"
    assert candidate.reverse(state.pair, context, first.outgoing) == (perfect_pair, ())
    for tick in (1, 2):
        state, batch = candidate.advance(state, context)
        assert state.tick == tick + 1 and batch.tick == tick
        assert state.pair == wave.Pair((), ()) and state.heat == _freeze({ORIGIN: F(2)})
        assert (batch.outgoing, batch.deposit, batch.crossings, batch.kind) == ((), (), (), "NO_CROSSINGS")
    # Nonzero local energy can also be instantaneously invisible because the
    # centered velocity is zero; this does not assert perpetual invisibility.
    blind_pair = wave.Pair(_freeze({ORIGIN: F(5, 9)}), _freeze({ORIGIN: F(1)}))
    assert wave.density(blind_pair, ORIGIN) > 0
    _, blind_batch = candidate.advance(candidate.ready(blind_pair), context)
    assert (blind_batch.outgoing, blind_batch.deposit, blind_batch.crossings) == ((), (), ())


def run_checks():
    """Only assertion failures become fired gates; unexpected errors propagate."""
    checks = (("G01_COUPLING", _g01_coupling), ("G02_COLD_BALANCE", _g02_cold_balance),
              ("G03_MEMORY", _g03_memory), ("G04_BOUNDARIES", _g04_boundaries))
    answer = []
    for name, function in checks:
        try:
            function()
        except AssertionError:
            answer.append((name, False))
        else:
            answer.append((name, True))
    return answer
