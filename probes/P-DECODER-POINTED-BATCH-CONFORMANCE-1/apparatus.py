"""Exact ideal five-cell batch apparatus; no physical or probability claim.

The complete Cartesian incidence and one atomic write per cut are model
choices.  A passive address lookup reads a completed batch.  It is not a
sequence of new interactions.  The caller owns the autonomous U transition:
this module checks checkpoint types and counters, never substitutes A for U.

All scientific computations occur only when a function or property is called.
"""

from dataclasses import dataclass
from fractions import Fraction
from typing import TypeAlias


KernelPoint: TypeAlias = tuple[int, int, int, int, int, int]
SourceId: TypeAlias = tuple[int, KernelPoint]
Checkpoint: TypeAlias = tuple[int, KernelPoint]
Vector4: TypeAlias = tuple[int, int, int, int]
Vector5: TypeAlias = tuple[int, int, int, int, int]

CONTEXT_ID = "C5-POINTED-HEAD-FULL-INCIDENCE-ATOMIC-BATCH-1"
READY_STATE_ID = "EMPTY_READY"
ZERO_DENOMINATOR = "ZERO_DENOMINATOR"


def _natural(value: object, name: str) -> None:
    if type(value) is not int or value < 0:
        raise ValueError(name + " must be an exact nonnegative integer")


def _integer_tuple(value: object, length: int, name: str) -> None:
    if (type(value) is not tuple or len(value) != length
            or any(type(item) is not int for item in value)):
        raise ValueError(name + " must be an exact integer tuple of length "
                         + str(length))


def _point(value: object, name: str) -> None:
    _integer_tuple(value, 6, name)
    if any(item < 0 or item >= 5 for item in value):
        raise ValueError(name + " must use the representatives 0,1,2,3,4")


def _checkpoint(value: object, name: str) -> None:
    if type(value) is not tuple or len(value) != 2:
        raise ValueError(name + " must be (counter, kernel_point)")
    _natural(value[0], name + ".counter")
    _point(value[1], name + ".kernel_point")


def _source_cut(source_id: object, relative_cut: object) -> None:
    _checkpoint(source_id, "source_id")
    _natural(relative_cut, "relative_cut")


def _augmentation(value: object, name: str) -> None:
    _integer_tuple(value, 5, name)
    if sum(value) != 0:
        raise ValueError(name + " must have coordinate sum zero")


def _context(context_id: object) -> None:
    if type(context_id) is not str or context_id != CONTEXT_ID:
        raise ValueError("context_id is not the selected singleton context")


def centered_head(v: Vector4) -> Vector5:
    """The declared integer adapter 5*(v,0)-sum(v)*1, on Z^4."""
    _integer_tuple(v, 4, "v")
    total = sum(v)
    return tuple(5 * item - total for item in v) + (-total,)


def mix_a(a: Vector5) -> Vector5:
    """A=I+g^2-g^3-g^4, with g*e_k=e_(k+1), on Z^5."""
    _integer_tuple(a, 5, "a")
    return tuple(a[k] + a[(k - 2) % 5] - a[(k - 3) % 5]
                 - a[(k - 4) % 5] for k in range(5))


@dataclass(frozen=True, slots=True)
class UnitRecord:
    source_id: SourceId
    relative_cut: int
    cell: int
    tag: str
    sign: int
    ordinal: int

    def __post_init__(self) -> None:
        _source_cut(self.source_id, self.relative_cut)
        _natural(self.cell, "cell")
        if self.cell >= 5:
            raise ValueError("cell must be less than five")
        if type(self.tag) is not str or self.tag not in ("S", "R"):
            raise ValueError("unit tag must be S or R")
        if type(self.sign) is not int or self.sign not in (-1, 1):
            raise ValueError("a nonempty unit has sign -1 or 1")
        _natural(self.ordinal, "ordinal")
        if self.ordinal == 0:
            raise ValueError("unit ordinals start at one")


@dataclass(frozen=True, slots=True)
class FiberRange:
    """Finite ordinal range [1,size]; size zero denotes the empty fibre."""

    source_id: SourceId
    relative_cut: int
    cell: int
    tag: str
    sign: int
    size: int

    def __post_init__(self) -> None:
        _source_cut(self.source_id, self.relative_cut)
        _natural(self.cell, "cell")
        _natural(self.size, "size")
        if self.cell >= 5:
            raise ValueError("cell must be less than five")
        if type(self.tag) is not str or self.tag not in ("S", "R"):
            raise ValueError("fibre tag must be S or R")
        if type(self.sign) is not int:
            raise ValueError("fibre sign must be an exact integer")
        if ((self.size == 0 and self.sign != 0)
                or (self.size > 0 and self.sign not in (-1, 1))):
            raise ValueError("fibre sign and size disagree")

    def unit_at(self, ordinal: int) -> UnitRecord:
        _natural(ordinal, "ordinal")
        if not 1 <= ordinal <= self.size:
            raise ValueError("ordinal is outside the finite fibre")
        return UnitRecord(self.source_id, self.relative_cut, self.cell,
                          self.tag, self.sign, ordinal)


@dataclass(frozen=True, slots=True)
class PairRecord:
    system: UnitRecord
    record: UnitRecord

    def __post_init__(self) -> None:
        if type(self.system) is not UnitRecord or type(self.record) is not UnitRecord:
            raise ValueError("pair endpoints must be UnitRecord values")
        left, right = self.system, self.record
        if left.tag != "S" or right.tag != "R":
            raise ValueError("an ordered pair has S and R endpoints")
        if ((left.source_id, left.relative_cut, left.cell, left.sign)
                != (right.source_id, right.relative_cut, right.cell, right.sign)):
            raise ValueError("pair endpoints must share source, cut, cell and sign")

    @property
    def cell(self) -> int:
        return self.system.cell


@dataclass(frozen=True, slots=True)
class PairBank:
    """Complete within-cell products, represented by five finite ranges."""

    source_id: SourceId
    relative_cut: int
    a: Vector5

    def __post_init__(self) -> None:
        _source_cut(self.source_id, self.relative_cut)
        _augmentation(self.a, "a")

    @property
    def counts(self) -> Vector5:
        return tuple(value * value for value in self.a)

    @property
    def total_count(self) -> int:
        return sum(self.counts)

    @property
    def fibers(self) -> tuple[tuple[FiberRange, FiberRange], ...]:
        result = []
        for cell, value in enumerate(self.a):
            sign = (value > 0) - (value < 0)
            result.append(tuple(FiberRange(self.source_id, self.relative_cut,
                                           cell, tag, sign, abs(value))
                                for tag in ("S", "R")))
        return tuple(result)

    def pair_at(self, index: int) -> PairRecord:
        """Zero-based rank in lexicographic (cell,S ordinal,R ordinal) order."""
        _natural(index, "index")
        remainder = index
        for cell, value in enumerate(self.a):
            size = abs(value)
            if remainder < size * size:
                i, j = divmod(remainder, size)
                sign = (value > 0) - (value < 0)
                return PairRecord(
                    UnitRecord(self.source_id, self.relative_cut, cell,
                               "S", sign, i + 1),
                    UnitRecord(self.source_id, self.relative_cut, cell,
                               "R", sign, j + 1),
                )
            remainder -= size * size
        raise ValueError("index is outside the finite pair bank")

    def index_of(self, pair: PairRecord) -> int:
        """Inverse of pair_at on this exact bank, with all identity tags checked."""
        if type(pair) is not PairRecord:
            raise ValueError("pair must be a PairRecord")
        unit = pair.system
        if (unit.source_id, unit.relative_cut) != (self.source_id, self.relative_cut):
            raise ValueError("pair belongs to another source or cut")
        value = self.a[unit.cell]
        size = abs(value)
        sign = (value > 0) - (value < 0)
        if (unit.sign != sign or unit.ordinal > size
                or pair.record.ordinal > size):
            raise ValueError("pair does not belong to this residual fibre")
        return (sum(self.counts[:unit.cell]) + (unit.ordinal - 1) * size
                + pair.record.ordinal - 1)


@dataclass(frozen=True, slots=True)
class Support:
    """A well-typed cut; the decoder proves its U and A reachability."""

    source_id: SourceId
    relative_cut: int
    checkpoint: Checkpoint
    a: Vector5

    def __post_init__(self) -> None:
        _source_cut(self.source_id, self.relative_cut)
        _checkpoint(self.checkpoint, "checkpoint")
        _augmentation(self.a, "a")
        if self.checkpoint[0] != self.source_id[0] + self.relative_cut:
            raise ValueError("checkpoint counter disagrees with source and cut")


@dataclass(frozen=True, slots=True)
class BatchRecord:
    source_id: SourceId
    relative_cut: int
    absolute_counter: int
    a: Vector5
    provenance_checkpoint: Checkpoint
    context_id: str = CONTEXT_ID

    def __post_init__(self) -> None:
        _source_cut(self.source_id, self.relative_cut)
        _natural(self.absolute_counter, "absolute_counter")
        _checkpoint(self.provenance_checkpoint, "provenance_checkpoint")
        _augmentation(self.a, "a")
        _context(self.context_id)
        if self.absolute_counter != self.source_id[0] + self.relative_cut:
            raise ValueError("absolute counter disagrees with source and cut")
        if self.provenance_checkpoint[0] != self.absolute_counter:
            raise ValueError("provenance checkpoint has a different counter")

    @property
    def pair_bank(self) -> PairBank:
        return PairBank(self.source_id, self.relative_cut, self.a)

    @property
    def counts(self) -> Vector5:
        return tuple(value * value for value in self.a)

    @property
    def total_count(self) -> int:
        return sum(self.counts)

    @property
    def ratio(self) -> tuple[Fraction, ...] | str:
        total = self.total_count
        if total == 0:
            return ZERO_DENOMINATOR
        return tuple(Fraction(count, total) for count in self.counts)

    @property
    def outcome(self) -> str:
        return "ZERO_EVENT" if self.total_count == 0 else "BATCH_EVENT"

    def pair_at(self, index: int) -> PairRecord:
        return self.pair_bank.pair_at(index)


@dataclass(frozen=True, slots=True)
class Controller:
    next_cut: int
    cache: BatchRecord | None = None

    def __post_init__(self) -> None:
        _natural(self.next_cut, "next_cut")
        if self.cache is not None:
            if type(self.cache) is not BatchRecord:
                raise ValueError("cache must be a BatchRecord or None")
            if self.next_cut != self.cache.relative_cut + 1:
                raise ValueError("cached batch must immediately precede next_cut")


def context_of(source_id: SourceId) -> str:
    _checkpoint(source_id, "source_id")
    return CONTEXT_ID


def ready_select(source_id: SourceId, context_id: str = CONTEXT_ID) -> str:
    _checkpoint(source_id, "source_id")
    _context(context_id)
    return READY_STATE_ID


def prepare(source_id: SourceId, v: Vector4,
            checkpoint: Checkpoint | None = None,
            context_id: str = CONTEXT_ID) -> tuple[Support, Controller]:
    """Start one pointed run, including zero support, with relative cut zero.

    The supplied v must be the balanced first four coordinates of its head.
    Counter reset into the separate anchored QDD adapter is the decoder's job.
    """
    _checkpoint(source_id, "source_id")
    _integer_tuple(v, 4, "v")
    _context(context_id)
    balanced = tuple(value if value <= 2 else value - 5
                     for value in source_id[1][:4])
    if v != balanced:
        raise ValueError("v must be the balanced piston of the pointed head")
    if checkpoint is None:
        checkpoint = source_id
    _checkpoint(checkpoint, "checkpoint")
    if checkpoint != source_id:
        raise ValueError("preparation checkpoint must equal the pointed head")
    return Support(source_id, 0, checkpoint, centered_head(v)), Controller(0)


def emit(support: Support) -> BatchRecord:
    """Construct one completed atomic model batch; all pair addresses are present."""
    if type(support) is not Support:
        raise ValueError("support must be a Support")
    return BatchRecord(support.source_id, support.relative_cut,
                       support.checkpoint[0], support.a, support.checkpoint)


def persist(controller: Controller, event: BatchRecord) -> Controller:
    if type(controller) is not Controller or type(event) is not BatchRecord:
        raise ValueError("persist requires Controller and BatchRecord")
    if controller.next_cut != event.relative_cut:
        raise ValueError("event cut disagrees with the controller")
    if controller.cache is not None and controller.cache.source_id != event.source_id:
        raise ValueError("cached record belongs to a different pointed run")
    return Controller(controller.next_cut + 1, event)


def step(support: Support, controller: Controller,
         expected_next_checkpoint: Checkpoint
         ) -> tuple[Support, Controller, BatchRecord]:
    """One batch and one fresh cut.  Caller certifies the supplied U successor.

    No individual outcome is selected.  The next bank is defined from fresh
    residual fibres, not by transporting identities from the current bank.
    """
    if type(support) is not Support or type(controller) is not Controller:
        raise ValueError("step requires Support and Controller")
    if support.relative_cut != controller.next_cut:
        raise ValueError("support cut disagrees with the controller")
    _checkpoint(expected_next_checkpoint, "expected_next_checkpoint")
    if expected_next_checkpoint[0] != support.checkpoint[0] + 1:
        raise ValueError("the supplied checkpoint must advance the counter once")
    if controller.cache is not None:
        if controller.cache.source_id != support.source_id:
            raise ValueError("cached record belongs to a different pointed run")
        if mix_a(controller.cache.a) != support.a:
            raise ValueError("support is not the A successor of the cached cut")
    event = emit(support)
    next_support = Support(support.source_id, support.relative_cut + 1,
                           expected_next_checkpoint, mix_a(support.a))
    return next_support, persist(controller, event), event


def reset(controller: Controller) -> tuple[str, Controller]:
    """Clear scratch only.  Neither the cut cursor nor any history is rewound."""
    if type(controller) is not Controller:
        raise ValueError("reset requires a Controller")
    return READY_STATE_ID, Controller(controller.next_cut)


def passive_read(event: BatchRecord, index: int) -> PairRecord:
    """Pure lookup of an existing record; no state, history or occurrence change."""
    if type(event) is not BatchRecord:
        raise ValueError("passive_read requires a BatchRecord")
    return event.pair_at(index)


def zero_support(support: Support) -> BatchRecord:
    if type(support) is not Support or any(support.a):
        raise ValueError("zero_support requires a zero Support")
    return emit(support)


def terminal(event: BatchRecord) -> bool:
    """Completion of an atomic model write; this is not a saturation law."""
    if type(event) is not BatchRecord:
        raise ValueError("terminal requires a BatchRecord")
    return True


def append_history(history: tuple[BatchRecord, ...], event: BatchRecord
                   ) -> tuple[BatchRecord, ...]:
    """Append to one pointed run's complete consecutive finite prefix."""
    if type(history) is not tuple or type(event) is not BatchRecord:
        raise ValueError("append_history requires a tuple and BatchRecord")
    for cut, previous in enumerate(history):
        if (type(previous) is not BatchRecord or previous.relative_cut != cut
                or previous.source_id != event.source_id):
            raise ValueError("history is not one consecutive pointed prefix")
    if event.relative_cut != len(history):
        raise ValueError("event is not the next cut of this history")
    return history + (event,)
