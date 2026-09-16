"""NON-CANONICAL accepted terminal energy account; no occurrence law.

Immutable signed reservoir payloads are the energy store. Counts and
remainders describe that same energy; neither is a second store.
No gate in this file may run before the accepted public probe pin.
"""
from dataclasses import dataclass, replace
from fractions import Fraction as F


def rational(value):
    if type(value) not in (int, F):
        raise TypeError("exact rational required")
    return F(value)


def vector(value):
    if type(value) is not tuple or len(value) != 5:
        raise TypeError("immutable five-cell vector required")
    result = tuple(rational(x) for x in value)
    if sum(result, F(0)) != 0:
        raise ValueError("sum-zero system carrier required")
    return result


def norm2(value):
    return sum((x*x for x in vector(value)), F(0))


@dataclass(frozen=True)
class Context:
    setup: str
    channels: tuple
    quantum: F

    def __post_init__(self):
        if type(self.setup) is not str or not self.setup:
            raise ValueError("a fixed setup identifier is required")
        if (type(self.channels) is not tuple or not self.channels
                or any(type(x) is not str or not x for x in self.channels)
                or len(set(self.channels)) != len(self.channels)):
            raise ValueError("distinct ordered channel identifiers required")
        object.__setattr__(self, "quantum", rational(self.quantum))
        if self.quantum <= 0:
            raise ValueError("positive rational threshold required")


@dataclass(frozen=True)
class MarkRange:
    channel: str
    first: int
    last: int


@dataclass(frozen=True)
class Batch:
    run: int
    pulse: int
    amplitudes: tuple
    input_energy: F
    marks: tuple
    counts: tuple
    remainders: tuple


@dataclass(frozen=True)
class Run:
    index: int
    initial_lifetime: tuple
    batches: tuple
    closed: bool = False


@dataclass(frozen=True)
class State:
    context: Context
    archives: tuple
    active: Run


def ready(context):
    if type(context) is not Context:
        raise TypeError("typed context required")
    return State(context, (), Run(0, (0,)*len(context.channels), ()))


def totals(run, count):
    return tuple(sum((norm2(batch.amplitudes[i]) for batch in run.batches), F(0))
                 for i in range(count))


def validate(state):
    """Reject structurally or algebraically inconsistent histories, including archives."""
    if (type(state) is not State or type(state.context) is not Context
            or type(state.archives) is not tuple or type(state.active) is not Run):
        raise TypeError("typed immutable state required")
    context = state.context
    channels, epsilon = context.channels, context.quantum
    lifetime = (0,)*len(channels)
    for index, run in enumerate(state.archives + (state.active,)):
        if (type(run) is not Run or type(run.index) is not int or run.index != index
                or type(run.closed) is not bool or type(run.batches) is not tuple
                or type(run.initial_lifetime) is not tuple
                or any(type(x) is not int for x in run.initial_lifetime)
                or run.initial_lifetime != lifetime):
            raise ValueError("invalid run identity or lifetime boundary")
        if index < len(state.archives) and not run.closed:
            raise ValueError("archived run must be closed")
        energy = [F(0)]*len(channels)
        old = (0,)*len(channels)
        for tick, batch in enumerate(run.batches):
            if (type(batch) is not Batch or type(batch.run) is not int
                    or type(batch.pulse) is not int or batch.run != index
                    or batch.pulse != tick or type(batch.amplitudes) is not tuple
                    or len(batch.amplitudes) != len(channels)):
                raise ValueError("incomplete or mistyped pulse sequence")
            deposit = tuple(norm2(v) for v in batch.amplitudes)
            if rational(batch.input_energy) != sum(deposit, F(0)):
                raise ValueError("input/store energy mismatch")
            energy = [a+b for a,b in zip(energy, deposit)]
            counts = tuple(int(x // epsilon) for x in energy)
            remainder = tuple(x-epsilon*n for x,n in zip(energy, counts))
            marks = tuple(MarkRange(name, lifetime[i]+old[i]+1,
                                    lifetime[i]+counts[i])
                          for i,name in enumerate(channels) if counts[i] > old[i])
            if (type(batch.counts) is not tuple
                    or any(type(x) is not int for x in batch.counts)
                    or type(batch.remainders) is not tuple
                    or any(type(x) is not F for x in batch.remainders)
                    or type(batch.marks) is not tuple
                    or any(type(x) is not MarkRange or type(x.first) is not int
                           or type(x.last) is not int for x in batch.marks)
                    or batch.counts != counts or batch.remainders != remainder
                    or batch.marks != marks):
                raise ValueError("incorrect energy account or lifetime ordinals")
            old = counts
        lifetime = tuple(a+b for a,b in zip(lifetime, old))
    return state


def deposit(state, amplitudes, input_energy):
    """Terminal swap into fresh zero sites, followed by exact energy accounting."""
    validate(state)
    if state.active.closed:
        raise ValueError("cannot append after END; explicitly RESET first")
    if type(amplitudes) is not tuple or len(amplitudes) != len(state.context.channels):
        raise ValueError("all declared output channels must be present")
    amplitudes = tuple(vector(v) for v in amplitudes)
    input_energy = rational(input_energy)
    additions = tuple(norm2(v) for v in amplitudes)
    if input_energy != sum(additions, F(0)):
        raise ValueError("terminal input energy must equal the entire stored output")
    context, run = state.context, state.active
    old_energy = totals(run, len(context.channels))
    new_energy = tuple(a+b for a,b in zip(old_energy, additions))
    old = tuple(int(x // context.quantum) for x in old_energy)
    counts = tuple(int(x // context.quantum) for x in new_energy)
    remainder = tuple(x-context.quantum*n for x,n in zip(new_energy, counts))
    marks = tuple(MarkRange(name, run.initial_lifetime[i]+old[i]+1,
                            run.initial_lifetime[i]+counts[i])
                  for i,name in enumerate(context.channels) if counts[i] > old[i])
    batch = Batch(run.index, len(run.batches), amplitudes, input_energy,
                  marks, counts, remainder)
    return validate(replace(state, active=replace(run, batches=run.batches+(batch,))))


def end(state):
    """A software boundary, explicitly not a physical completion law."""
    validate(state)
    return replace(state, active=replace(state.active, closed=True))


def reset(state):
    """Archive everything and prepare a new counter run; export no energy."""
    validate(state)
    run = replace(state.active, closed=True)
    old = run.batches[-1].counts if run.batches else (0,)*len(state.context.channels)
    lifetime = tuple(a+b for a,b in zip(run.initial_lifetime, old))
    return validate(State(state.context, state.archives+(run,),
                          Run(run.index+1, lifetime, ())))


def read(state):
    """Read the identical complete state; do not produce another batch."""
    return validate(state)


def stored_energy(state):
    validate(state)
    return sum((norm2(v) for run in state.archives+(state.active,)
                for batch in run.batches for v in batch.amplitudes), F(0))


def accounting_energy(state):
    validate(state)
    epsilon = state.context.quantum
    return sum((epsilon*sum(run.batches[-1].counts)
                +sum(run.batches[-1].remainders, F(0))
                for run in state.archives+(state.active,) if run.batches), F(0))


def threshold_interval(lower, upper, quantum):
    """Exact enclosure for a cumulative energy; no rounding to a chosen mark."""
    lower, upper, quantum = map(rational, (lower, upper, quantum))
    if lower < 0 or upper < lower or quantum <= 0:
        raise ValueError("ordered nonnegative enclosure and positive threshold required")
    first, last = int(lower // quantum), int(upper // quantum)
    return ("DETERMINED", first) if first == last else ("AMBIGUOUS", first, last)
