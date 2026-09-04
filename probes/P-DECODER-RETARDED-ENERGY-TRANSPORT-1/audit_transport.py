"""Independent exact finite audits; execution belongs to the pinned verifier.

The references use signed shell permutations, pointwise recurrence, unordered
edge sums and a recursive impulse response. No scientific work runs on import.
"""
from fractions import Fraction as F
from itertools import permutations, product

import transport as candidate


ORIGIN = (0, 0, 0)
P = (1, 1, 0)
Q = (2, 0, 0)
FAR = (40, 0, 0)
SOURCE_SITES = (ORIGIN, P, (1, 0, 1), (0, 1, 1), Q)


def _shift(x, z):
    return tuple(a + b for a, b in zip(x, z))


def _freeze(values):
    return tuple(sorted((x, F(a)) for x, a in values.items() if a))


def _shells():
    answer = {}
    specifications = (((1, 1, 0), 6), ((2, 0, 0), 1),
                      ((2, 2, 0), 15), ((3, 1, 0), 1), ((4, 0, 0), 1))
    for prototype, weight in specifications:
        shell = {tuple(a * s for a, s in zip(p, signs))
                 for p in permutations(prototype)
                 for signs in product((-1, 1), repeat=3)}
        for z in shell:
            assert z not in answer
            answer[z] = F(weight, 324)
    return tuple(sorted(answer.items()))


def _halo(sites, offsets):
    sites = set(sites)
    return sites | {_shift(x, z) for x in sites for z, _ in offsets}


def _edges(sites, offsets):
    """Every undirected edge with at least one endpoint in sites, once."""
    answer = {}
    for x in sites:
        for z, coefficient in offsets:
            y = _shift(x, z)
            edge = (x, y) if x < y else (y, x)
            if edge in answer:
                assert answer[edge] == coefficient
            answer[edge] = coefficient
    return tuple((x, y, c) for (x, y), c in sorted(answer.items()))


def _next(u, v, forcing, offsets):
    """Independent pointwise recurrence, including newly reached sites."""
    result = {}
    for x in _halo(set(u) | set(v) | set(forcing), offsets):
        vx = v.get(x, F(0))
        av = sum((c * (vx - v.get(_shift(x, z), F(0)))
                  for z, c in offsets), F(0))
        result[x] = 2 * vx - u.get(x, F(0)) - av + forcing.get(x, F(0))
    return dict(_freeze(result))


def _mixed_energy(u, v, offsets):
    kinetic = sum(((v.get(x, F(0)) - u.get(x, F(0))) ** 2
                   for x in set(u) | set(v)), F(0)) / 2
    potential = sum((c * (u.get(x, F(0)) - u.get(y, F(0)))
                     * (v.get(x, F(0)) - v.get(y, F(0)))
                     for x, y, c in _edges(set(u) | set(v), offsets)), F(0)) / 2
    return kinetic + potential


def _positive_density(u, v, offsets):
    """The midpoint/velocity sum of squares, accumulated by undirected edge."""
    support = set(u) | set(v)
    delta = {x: v.get(x, F(0)) - u.get(x, F(0)) for x in support}
    sums = {x: v.get(x, F(0)) + u.get(x, F(0)) for x in support}
    answer = {x: F(5, 18) * delta[x] ** 2 for x in support}
    for x, y, c in _edges(support, offsets):
        edge_energy = c / 16 * ((delta.get(x, F(0)) + delta.get(y, F(0))) ** 2
                               + (sums.get(x, F(0)) - sums.get(y, F(0))) ** 2)
        answer[x] = answer.get(x, F(0)) + edge_energy
        answer[y] = answer.get(y, F(0)) + edge_energy
    return dict(_freeze(answer))


def _r(u, v, x, y, c):
    dx = v.get(x, F(0)) - u.get(x, F(0))
    dy = v.get(y, F(0)) - u.get(y, F(0))
    return c * (dx * dx - dy * dy) / 8


def _current(u, v, w, x, y, c):
    centered_velocity = (w.get(x, F(0)) - u.get(x, F(0))
                         + w.get(y, F(0)) - u.get(y, F(0))) / 2
    natural = c * (v.get(x, F(0)) - v.get(y, F(0))) * centered_velocity / 2
    return natural + _r(v, w, x, y, c) - _r(u, v, x, y, c)


def _translated(values, shift):
    return {_shift(x, shift): a for x, a in values.items()}


def _g01_stencil():
    reference = _shells()
    assert candidate.stencil() == reference
    assert len(reference) == 60
    assert {n: sum(sum(a * a for a in z) == n for z, _ in reference)
            for n in (2, 4, 8, 10, 16)} == {2: 12, 4: 6, 8: 12, 10: 24, 16: 6}
    weights = dict(reference)
    assert all(sum(z) % 2 == 0 and weights[tuple(-a for a in z)] == c
               and c > 0 for z, c in reference)
    assert sum(weights.values(), F(0)) == F(8, 9)
    assert candidate.halo((ORIGIN, P)) == _halo((ORIGIN, P), reference)
    assert candidate.halo(()) == set()


def _g02_source():
    cases = tuple(product(range(-2, 3), repeat=4)) + (
        (F(1, 2), F(-2, 3), F(0), F(5, 7)),
        (F(1, 3), F(1, 3), F(1, 3), F(1, 3)),
        (F(-7, 5), F(0), F(2, 9), F(4, 11)),
    )
    for v in cases:
        total = sum(v, F(0))
        coefficients = tuple(F(a) - total / 5 for a in v + (0,))
        reference = _freeze(dict(zip(SOURCE_SITES, coefficients)))
        actual = candidate.source(v)
        assert actual == reference
        assert sum(dict(actual).values(), F(0)) == 0
        assert tuple(dict(actual).get(x, F(0)) - dict(actual).get(Q, F(0))
                     for x in SOURCE_SITES[:4]) == v
        mass = sum((F(a) ** 2 for a in v), F(0)) - total ** 2 / 5
        assert sum((a * a for _, a in reference), F(0)) == mass
        assert candidate.qdd_mass(v) == candidate.norm2(actual) == mass
        prepared = candidate.prepare(v)
        assert prepared == candidate.Pair((), reference)
        assert 2 * candidate.energy(prepared) == mass
        assert (mass == 0) == all(a == 0 for a in v)


def _g03_energy():
    offsets = _shells()
    cases = (({}, {}), ({}, {ORIGIN: F(1)}),
             ({ORIGIN: F(1, 2), P: F(-1, 3)},
              {ORIGIN: F(-2, 5), P: F(3, 7)}))
    for u, v in cases:
        pair = candidate.Pair(_freeze(u), _freeze(v))
        w = _next(u, v, {}, offsets)
        successor = candidate.step(pair)
        assert successor == candidate.Pair(_freeze(v), _freeze(w))
        original_energy = _mixed_energy(u, v, offsets)
        for left, right, actual_pair in ((u, v, pair), (v, w, successor)):
            reference = _positive_density(left, right, offsets)
            assert all(a > 0 for a in reference.values())
            assert candidate.density_field(actual_pair) == _freeze(reference)
            assert sum(reference.values(), F(0)) == _mixed_energy(left, right, offsets)
            assert candidate.energy(actual_pair) == original_energy
            for x in (ORIGIN, P, FAR):
                assert candidate.density(actual_pair, x) == reference.get(x, F(0))
        assert (original_energy == 0) == (not u and not v)


def _g04_local_balance():
    offsets = _shells()
    forcing = {ORIGIN: F(1, 3), Q: F(-2, 5)}
    cases = (({}, {}), ({ORIGIN: F(1, 2)}, {P: F(2, 3)}))
    for u, v in cases:
        pair = candidate.Pair(_freeze(u), _freeze(v))
        w = _next(u, v, forcing, offsets)
        next_field, force_field = _freeze(w), _freeze(forcing)
        assert candidate.step(pair, force_field) == candidate.Pair(_freeze(v), next_field)
        before = _positive_density(u, v, offsets)
        after = _positive_density(v, w, offsets)
        support = set(u) | set(v) | set(w) | set(forcing)
        domain = _halo(support, offsets)
        edges = _edges(support, offsets)
        divergence = {}
        currents = []
        for x, y, c in edges:
            flux = _current(u, v, w, x, y, c)
            assert _current(u, v, w, y, x, c) == -flux
            currents.append((x, y, flux))
            divergence[x] = divergence.get(x, F(0)) + flux
            divergence[y] = divergence.get(y, F(0)) - flux
        work = {x: (w.get(x, F(0)) - u.get(x, F(0))) * forcing.get(x, F(0)) / 2
                for x in domain}
        for x in sorted(domain):
            change = after.get(x, F(0)) - before.get(x, F(0))
            assert change + divergence.get(x, F(0)) == work[x]
            assert candidate.local_work(pair, next_field, force_field, x) == work[x]
            account = candidate.balance(pair, next_field, force_field, candidate.Aperture((x,)))
            assert (account.change, account.outward_flux, account.work, account.residual) == (
                change, divergence.get(x, F(0)), work[x], F(0))
        # Cover every shell and orientation without repeating public-current setup
        # on all boundary bonds. Full divergence was independently checked above.
        for anchor in (ORIGIN, P):
            for z, c in offsets:
                y = _shift(anchor, z)
                expected = _current(u, v, w, anchor, y, c)
                assert candidate.current(pair, next_field, anchor, y) == expected
                assert candidate.current(pair, next_field, y, anchor) == -expected
        assert candidate.current(pair, next_field, ORIGIN, FAR) == 0
        assert candidate.current(pair, next_field, ORIGIN, ORIGIN) == 0
        apertures = ((), (ORIGIN,), tuple(sorted((ORIGIN, P))),
                     tuple(sorted((Q, FAR))), tuple(sorted((ORIGIN, P, Q))),
                     tuple(sorted(domain)))
        for sites in apertures:
            region = set(sites)
            change = sum((after.get(x, F(0)) - before.get(x, F(0)) for x in region), F(0))
            outward = sum((flux * (int(x in region) - int(y in region))
                           for x, y, flux in currents), F(0))
            work_sum = sum((work.get(x, F(0)) for x in region), F(0))
            account = candidate.balance(pair, next_field, force_field, candidate.Aperture(sites))
            assert (account.change, account.outward_flux, account.work, account.residual) == (
                change, outward, work_sum, F(0))
            assert change + outward == work_sum
        assert candidate.energy(candidate.Pair(_freeze(v), next_field)) - candidate.energy(pair) == sum(work.values(), F(0))


def _g05_retarded():
    offsets = _shells()
    forcings = ({ORIGIN: F(1)}, {P: F(1, 2), Q: F(-1, 3)}, {ORIGIN: F(-1)})
    public_forcings = tuple(_freeze(f) for f in forcings)
    reference_history = [candidate.Pair((), ())]
    u, v = {}, {}
    for forcing in forcings:
        w = _next(u, v, forcing, offsets)
        reference_history.append(candidate.Pair(_freeze(v), _freeze(w)))
        u, v = v, w
    actual_history = candidate.forced_history(public_forcings)
    assert actual_history == tuple(reference_history)
    for length in range(4):
        assert candidate.forced_history(public_forcings[:length]) == actual_history[:length + 1]
    changed_future = public_forcings[:2] + (_freeze({FAR: F(7, 9)}),)
    assert candidate.forced_history(changed_future)[:3] == actual_history[:3]
    # G_0 f=f, G_1 f=Hf, G_(r+1)f=H G_r f-G_(r-1)f.
    # This recursive reference does not use the candidate binomial expression.
    responses = {}
    for f in forcings[:2]:
        previous, current = {}, f
        allowed = set(f)
        for age in range(4):
            response = candidate.green(_freeze(f), age)
            assert response == _freeze(current)
            assert set(dict(response)) <= allowed
            translated = candidate.green(_freeze(_translated(f, FAR)), age)
            assert translated == _freeze(_translated(current, FAR))
            assert dict(translated).get(ORIGIN, F(0)) == 0
            responses[(_freeze(f), age)] = response
            if age < 3:
                previous, current = current, _next(previous, current, {}, offsets)
                allowed = _halo(allowed, offsets)
    for cut in range(1, 4):
        summed = {}
        allowed = set()
        for forcing_index in range(cut):
            age = cut - 1 - forcing_index
            forcing = forcings[forcing_index]
            response = responses.get((_freeze(forcing), age))
            if response is None:
                response = candidate.green(_freeze(forcing), age)
            for x, a in response:
                summed[x] = summed.get(x, F(0)) + a
            source_domain = set(forcing)
            for _ in range(age):
                source_domain = _halo(source_domain, offsets)
            allowed |= source_domain
        assert actual_history[cut].current == _freeze(summed)
        assert set(dict(actual_history[cut].current)) <= allowed
    assert candidate.green((), 3) == ()
    assert candidate.forced_history(()) == (candidate.Pair((), ()),)


def run_checks():
    """An assertion is a fired gate; unexpected implementation errors propagate."""
    checks = (("G01_STENCIL", _g01_stencil), ("G02_SOURCE", _g02_source),
              ("G03_ENERGY", _g03_energy), ("G04_LOCAL_BALANCE", _g04_local_balance),
              ("G05_RETARDED", _g05_retarded))
    results = []
    for name, check in checks:
        try:
            check()
        except AssertionError:
            results.append((name, False))
        else:
            results.append((name, True))
    return results
