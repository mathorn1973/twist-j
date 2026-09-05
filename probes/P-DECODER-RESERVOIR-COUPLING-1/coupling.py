"""Chosen rational reservoir coupling and calorimetric records; L1 only."""
from dataclasses import dataclass
from fractions import Fraction as F
from pathlib import Path
import hashlib
import sys


WAVE_PATH = Path(__file__).resolve().parents[1] / "P-DECODER-RETARDED-ENERGY-TRANSPORT-1" / "transport.py"
WAVE_SHA256 = "983d22690e061128d287f23ef4672fbd72954faa28f1a3fde9ce38b0d6660a60"
if hashlib.sha256(WAVE_PATH.read_bytes()).hexdigest() != WAVE_SHA256:
    raise RuntimeError("immutable wave dependency mismatch")
sys.path.insert(0, str(WAVE_PATH.parent))
try:
    import transport as wave
finally:
    sys.path.pop(0)
if Path(wave.__file__).resolve() != WAVE_PATH:
    raise RuntimeError("unexpected wave module origin")


def nonnegative(value):
    wave.validate_field(value)
    if any(a < 0 for _, a in value):
        raise ValueError("nonnegative field required")


@dataclass(frozen=True)
class Context:
    gamma: tuple
    quantum: F

    def __post_init__(self):
        nonnegative(self.gamma)
        object.__setattr__(self, "quantum", wave.rational(self.quantum))
        if self.quantum <= 0:
            raise ValueError("positive rational threshold required")


def port(value, context):
    wave.validate_field(value)
    if not set(dict(value)) <= set(dict(context.gamma)):
        raise ValueError("port or memory lies outside declared channels")
    return dict(value)


def port_energy(value, context):
    value = port(value, context)
    return sum((g * value.get(x, F(0)) ** 2 for x, g in context.gamma), F(0))


@dataclass(frozen=True)
class Interaction:
    after: wave.Pair
    outgoing: tuple
    forcing: tuple
    transfer: tuple

    def __post_init__(self):
        if type(self.after) is not wave.Pair:
            raise TypeError("wave pair required")
        for value in (self.outgoing, self.forcing, self.transfer):
            wave.validate_field(value)


def couple(pair, context, incoming=()):
    incoming = port(incoming, context)
    u, v = dict(pair.previous), dict(pair.current)
    w = dict(wave.step(pair).current)
    outgoing, forcing, transfer = {}, {}, {}
    for x, g in context.gamma:
        ux = u.get(x, F(0))
        a = incoming.get(x, F(0))
        w[x] = (w.get(x, F(0)) + g * ux / 2 + 2 * g * a) / (1 + g / 2)
        p = (w[x] - ux) / 2
        outgoing[x] = b = a - p
        forcing[x] = g * (2 * a - p)
        transfer[x] = g * (b * b - a * a)
    return Interaction(wave.Pair(pair.current, wave.field(w)), wave.field(outgoing),
                       wave.field(forcing), wave.field(transfer))


def reverse(after, context, outgoing):
    outgoing = port(outgoing, context)
    v, w = dict(after.previous), dict(after.current)
    u = dict(wave.step(wave.Pair(after.current, after.previous)).current)
    incoming = {}
    for x, g in context.gamma:
        wx = w.get(x, F(0))
        b = outgoing.get(x, F(0))
        u[x] = (u.get(x, F(0)) + g * wx / 2 + 2 * g * b) / (1 + g / 2)
        incoming[x] = b + (wx - u[x]) / 2
    return wave.Pair(wave.field(u), after.previous), wave.field(incoming)


def threshold_counts(heat, context):
    nonnegative(heat)
    values = port(heat, context)
    return tuple((x, int(values.get(x, F(0)) // context.quantum)) for x, _ in context.gamma)


def remainders(heat, context):
    counts = dict(threshold_counts(heat, context))
    return wave.field((x, dict(heat).get(x, F(0)) - context.quantum * counts[x])
                      for x, _ in context.gamma)


@dataclass(frozen=True)
class Crossing:
    site: tuple
    first: int
    last: int

    def __post_init__(self):
        wave.site(self.site)
        if type(self.first) is not int or type(self.last) is not int or not 1 <= self.first <= self.last:
            raise ValueError("positive nonempty lifetime ordinal range required")

    @property
    def count(self):
        return self.last - self.first + 1


def crossings(before, after, context):
    old, new = dict(threshold_counts(before, context)), dict(threshold_counts(after, context))
    if any(new[x] < old[x] for x in old):
        raise ValueError("threshold ordinal cannot be reset")
    return tuple(Crossing(x, old[x] + 1, new[x]) for x in old if new[x] > old[x])


@dataclass(frozen=True)
class State:
    pair: wave.Pair
    heat: tuple
    tick: int

    def __post_init__(self):
        if type(self.pair) is not wave.Pair:
            raise TypeError("wave pair required")
        nonnegative(self.heat)
        if type(self.tick) is not int or self.tick < 0:
            raise ValueError("nonnegative integer tick required")


@dataclass(frozen=True)
class Batch:
    tick: int
    outgoing: tuple
    deposit: tuple
    crossings: tuple
    kind: str

    def __post_init__(self):
        if type(self.tick) is not int or self.tick < 0:
            raise ValueError("nonnegative integer tick required")
        wave.validate_field(self.outgoing)
        nonnegative(self.deposit)
        if type(self.crossings) is not tuple or any(type(c) is not Crossing for c in self.crossings):
            raise TypeError("immutable crossing ranges required")
        sites = tuple(c.site for c in self.crossings)
        if sites != tuple(sorted(set(sites))):
            raise ValueError("one sorted range per channel required")
        if self.kind != ("THRESHOLD_CROSSINGS" if self.crossings else "NO_CROSSINGS"):
            raise ValueError("incorrect crossing tag")


def ready(pair):
    return State(pair, (), 0)


def advance(state, context):
    port(state.heat, context)
    interaction = couple(state.pair, context)
    nonnegative(interaction.transfer)
    heat = wave.add(state.heat, interaction.transfer)
    ranges = crossings(state.heat, heat, context)
    batch = Batch(state.tick, interaction.outgoing, interaction.transfer, ranges,
                  "THRESHOLD_CROSSINGS" if ranges else "NO_CROSSINGS")
    return State(interaction.after, heat, state.tick + 1), batch


@dataclass(frozen=True)
class History:
    context: Context
    initial: wave.Pair
    state: State
    batches: tuple

    def __post_init__(self):
        if (type(self.context) is not Context or type(self.initial) is not wave.Pair
                or type(self.state) is not State or type(self.batches) is not tuple):
            raise TypeError("typed immutable history required")
        if self.state.tick != len(self.batches):
            raise ValueError("history length/tick mismatch")
        heat = ()
        for tick, batch in enumerate(self.batches):
            if type(batch) is not Batch or batch.tick != tick:
                raise ValueError("history has a skipped or duplicate tick")
            amplitudes = port(batch.outgoing, self.context)
            expected = wave.field((x, g * amplitudes.get(x, F(0)) ** 2)
                                  for x, g in self.context.gamma)
            if batch.deposit != expected:
                raise ValueError("deposit does not match stored reservoir amplitude")
            new_heat = wave.add(heat, batch.deposit)
            if batch.crossings != crossings(heat, new_heat, self.context):
                raise ValueError("incorrect lifetime threshold ranges")
            heat = new_heat
        if self.state.heat != heat:
            raise ValueError("heat does not match complete reservoir tape")


def extend(history, steps):
    if type(steps) is not int or steps < 0:
        raise ValueError("nonnegative integer continuation length required")
    state, batches = history.state, history.batches
    for _ in range(steps):
        state, batch = advance(state, history.context)
        batches += (batch,)
    return History(history.context, history.initial, state, batches)


def history_from_pair(pair, context, steps):
    return extend(History(context, pair, ready(pair), ()), steps)


def prefix(v, context, steps):
    # Preparation completes before the first cold coupling. It is not damped.
    return history_from_pair(wave.prepare(v), context, steps)
