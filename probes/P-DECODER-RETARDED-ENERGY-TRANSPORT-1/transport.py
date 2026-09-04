"""Chosen exact source, D3 wave and passive local energy reader. L1 only."""
from dataclasses import dataclass, fields, is_dataclass
from fractions import Fraction as F
from itertools import product
from math import comb


SHELL_WEIGHTS = ((2, 6), (4, 1), (8, 15), (10, 1), (16, 1))
SOURCE_SITES = ((0, 0, 0), (1, 1, 0), (1, 0, 1), (0, 1, 1), (2, 0, 0))


def rational(value):
    if type(value) not in (int, F):
        raise TypeError("exact integer or Fraction required")
    return F(value)


def site(value):
    if (type(value) is not tuple or len(value) != 3
            or any(type(x) is not int for x in value) or sum(value) % 2):
        raise ValueError("D3 site must be an even-sum integer triple")
    return value


def field(mapping):
    """Canonical finite field; accepts a mapping or distinct site/value pairs."""
    entries = mapping.items() if isinstance(mapping, dict) else mapping
    result = {}
    seen = set()
    for x, value in entries:
        site(x)
        if x in seen:
            raise ValueError("duplicate field site")
        seen.add(x)
        value = rational(value)
        if value:
            result[x] = value
    return tuple(sorted(result.items()))


def validate_field(value):
    if type(value) is not tuple or field(value) != value:
        raise ValueError("noncanonical field")
    if any(type(a) is not F for _, a in value):
        raise TypeError("canonical coefficients must be Fractions")


def shifted(x, z):
    return tuple(x[i] + z[i] for i in range(3))


def stencil():
    weights = dict(SHELL_WEIGHTS)
    return tuple((z, F(weights[sum(a * a for a in z)], 324))
                 for z in product(range(-4, 5), repeat=3)
                 if sum(a * a for a in z) in weights)


def halo(sites):
    sites = {site(x) for x in sites}
    offsets = stencil()
    return sites | {shifted(x, z) for x in sites for z, _ in offsets}


def add(*values):
    result = {}
    for value in values:
        for x, a in value:
            result[x] = result.get(x, F(0)) + a
    return field(result)


def scale(value, factor):
    factor = rational(factor)
    return field((x, factor * a) for x, a in value)


def laplacian(value):
    result = {}
    offsets = stencil()
    for x, a in value:
        for z, c in offsets:
            y = shifted(x, z)
            result[x] = result.get(x, F(0)) + c * a
            result[y] = result.get(y, F(0)) - c * a
    return field(result)


def inner(left, right):
    right = dict(right)
    return sum((a * right.get(x, F(0)) for x, a in left), F(0))


def norm2(value):
    return inner(value, value)


@dataclass(frozen=True)
class Pair:
    previous: tuple
    current: tuple

    def __post_init__(self):
        validate_field(self.previous)
        validate_field(self.current)


def step(pair, forcing=()):
    validate_field(forcing)
    return Pair(pair.current, add(scale(pair.current, 2),
                scale(pair.previous, -1), scale(laplacian(pair.current), -1), forcing))


def coefficients(v):
    if type(v) is not tuple or len(v) != 4:
        raise ValueError("four exact source coefficients required")
    return tuple(rational(a) for a in v)


def qdd_mass(v):
    v = coefficients(v)
    return sum((a * a for a in v), F(0)) - sum(v, F(0)) ** 2 / 5


def source(v):
    v = coefficients(v)
    mean = sum(v, F(0)) / 5
    return field(zip(SOURCE_SITES, (a - mean for a in v + (F(0),))))


def prepare(v):
    return Pair((), source(v))


def energy(pair):
    difference = add(pair.current, scale(pair.previous, -1))
    return (norm2(difference) + inner(pair.previous, laplacian(pair.current))) / 2


def _density(u, v, x, offsets):
    ux, vx = u.get(x, F(0)), v.get(x, F(0))
    result = F(5, 18) * (vx - ux) ** 2
    for z, c in offsets:
        y = shifted(x, z)
        result += c / 8 * ((v.get(y, F(0)) - ux) ** 2
                           + (u.get(y, F(0)) - vx) ** 2)
    return result


def density(pair, x):
    return _density(dict(pair.previous), dict(pair.current), site(x), stencil())


def density_field(pair):
    u, v, offsets = dict(pair.previous), dict(pair.current), stencil()
    return field((x, _density(u, v, x, offsets)) for x in sorted(halo(set(u) | set(v))))


def _current(u, v, w, x, y, c):
    ux, uy = u.get(x, F(0)), u.get(y, F(0))
    vx, vy = v.get(x, F(0)), v.get(y, F(0))
    wx, wy = w.get(x, F(0)), w.get(y, F(0))
    return (c / 4 * (vx - vy) * (wx - ux + wy - uy)
            + c / 8 * ((wx - vx) ** 2 - (vx - ux) ** 2
                       - (wy - vy) ** 2 + (vy - uy) ** 2))


def current(pair, next_field, x, y):
    site(x)
    site(y)
    c = dict(stencil()).get(tuple(y[i] - x[i] for i in range(3)), F(0))
    return _current(dict(pair.previous), dict(pair.current), dict(next_field), x, y, c)


def local_work(pair, next_field, forcing, x):
    site(x)
    return ((dict(next_field).get(x, F(0)) - dict(pair.previous).get(x, F(0)))
            * dict(forcing).get(x, F(0)) / 2)


def green(value, age):
    if type(age) is not int or age < 0:
        raise ValueError("Green age must be a nonnegative integer")
    powers = [value]
    for _ in range(age):
        powers.append(add(scale(powers[-1], 2), scale(laplacian(powers[-1]), -1)))
    return add(*(scale(powers[age - 2 * j], (-1) ** j * comb(age - j, j))
                 for j in range(age // 2 + 1)))


def forced_history(forcings):
    result = (Pair((), ()),)
    for forcing in forcings:
        result += (step(result[-1], forcing),)
    return result


@dataclass(frozen=True)
class Aperture:
    sites: tuple

    def __post_init__(self):
        if (type(self.sites) is not tuple
                or tuple(sorted({site(x) for x in self.sites})) != self.sites):
            raise ValueError("aperture must be a sorted tuple of distinct D3 sites")


@dataclass(frozen=True)
class Reading:
    site_energy: tuple
    total: F
    kind: str

    def __post_init__(self):
        if type(self.site_energy) is not tuple:
            raise TypeError("immutable site readings required")
        Aperture(tuple(x for x, _ in self.site_energy))
        if any(type(a) is not F or a < 0 for _, a in self.site_energy):
            raise ValueError("nonnegative rational site energies required")
        if type(self.total) is not F or self.total != sum((a for _, a in self.site_energy), F(0)):
            raise ValueError("incorrect aperture total")
        if self.kind != ("ENERGY_READING" if self.total else "ZERO_READING"):
            raise ValueError("incorrect mathematical reading tag")


def readout(pair, aperture):
    u, v, offsets = dict(pair.previous), dict(pair.current), stencil()
    values = tuple((x, _density(u, v, x, offsets)) for x in aperture.sites)
    total = sum((a for _, a in values), F(0))
    return Reading(values, total, "ENERGY_READING" if total else "ZERO_READING")


@dataclass(frozen=True)
class Balance:
    change: F
    outward_flux: F
    work: F
    residual: F

    def __post_init__(self):
        if any(type(a) is not F for a in (self.change, self.outward_flux, self.work, self.residual)):
            raise TypeError("exact rational balance required")
        if self.residual != self.change + self.outward_flux - self.work:
            raise ValueError("incorrect balance residual")


def balance(pair, next_field, forcing, aperture):
    """An arbitrary triple has a residual; recurrence triples have residual zero."""
    validate_field(next_field)
    validate_field(forcing)
    u, v, w, f = dict(pair.previous), dict(pair.current), dict(next_field), dict(forcing)
    offsets, sites = stencil(), set(aperture.sites)
    change = flux = work = F(0)
    for x in aperture.sites:
        change += _density(v, w, x, offsets) - _density(u, v, x, offsets)
        work += (w.get(x, F(0)) - u.get(x, F(0))) * f.get(x, F(0)) / 2
        for z, c in offsets:
            y = shifted(x, z)
            if y not in sites:
                flux += _current(u, v, w, x, y, c)
    return Balance(change, flux, work, change + flux - work)


@dataclass(frozen=True)
class Frame:
    cut: int
    reading: Reading
    balance_from_previous: object

    def __post_init__(self):
        if type(self.cut) is not int or self.cut < 0:
            raise ValueError("cut must be a nonnegative integer")
        if type(self.reading) is not Reading:
            raise TypeError("Reading required")
        if self.cut == 0:
            if self.balance_from_previous is not None:
                raise ValueError("cut zero has no preceding free cut")
        elif type(self.balance_from_previous) is not Balance:
            raise TypeError("subsequent cuts require a balance")


@dataclass(frozen=True)
class History:
    aperture: Aperture
    frames: tuple

    def __post_init__(self):
        if type(self.aperture) is not Aperture or type(self.frames) is not tuple:
            raise TypeError("immutable aperture/history required")
        for cut, frame in enumerate(self.frames):
            if type(frame) is not Frame or frame.cut != cut:
                raise ValueError("history must begin at zero with consecutive cuts")
            if tuple(x for x, _ in frame.reading.site_energy) != self.aperture.sites:
                raise ValueError("aperture changed within history")
            if cut:
                account = frame.balance_from_previous
                if account.change != frame.reading.total - self.frames[cut - 1].reading.total:
                    raise ValueError("history energy difference mismatch")
                if account.residual or account.work:
                    raise ValueError("free history requires zero work and residual")


def append_history(history, frame):
    return History(history.aperture, history.frames + (frame,))


def prefix(v, aperture, length):
    if type(length) is not int or length < 0:
        raise ValueError("prefix length must be a nonnegative integer")
    pair = prepare(v)
    history = History(aperture, ())
    old_pair = None
    for cut in range(length):
        account = None if old_pair is None else balance(old_pair, pair.current, (), aperture)
        history = append_history(history, Frame(cut, readout(pair, aperture), account))
        if cut + 1 < length:
            old_pair, pair = pair, step(pair)
    return history


def exact_json(value):
    if type(value) is F:
        return {"numerator": value.numerator, "denominator": value.denominator}
    if is_dataclass(value):
        return {"type": type(value).__name__, **{f.name: exact_json(getattr(value, f.name))
                for f in fields(value)}}
    if type(value) is tuple:
        return [exact_json(a) for a in value]
    if value is None or type(value) in (str, int):
        return value
    raise TypeError("unsupported exact presentation type")


def main():
    import argparse
    import json
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", nargs=4, type=F, required=True)
    parser.add_argument("--aperture-json", required=True)
    parser.add_argument("--cuts", type=int, required=True)
    args = parser.parse_args()
    aperture = Aperture(tuple(tuple(x) for x in json.loads(args.aperture_json)))
    print(json.dumps(exact_json(prefix(tuple(args.source), aperture, args.cuts)),
                     sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
