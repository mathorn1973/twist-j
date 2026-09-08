"""Non-canonical, exact two-exposure software adapter; no physical certificate.

APPEND is total on EventRecord*. Chronological admission is a separate
predicate carrying an explicit protocol position and action journal. The
unchanged sealed TRC1 engine is imported only when this module is executed.
"""

from dataclasses import dataclass, fields, is_dataclass
from fractions import Fraction
from math import gcd
import hashlib
import importlib.util
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
CORE_PATH = "probes/P-TRC1-END-TO-END-IDENTIFIABILITY-1/chain.py"
CORE_SHA256 = "d6f23db8a6f28ee6b90e2544a71608e2f320770046ecdeea94418d0f64468a99"
PROFILE = "RRP1-TWO-EXPOSURE-RESERVED-BANKS/1"


def _load_core():
    path = ROOT / CORE_PATH
    if hashlib.sha256(path.read_bytes()).hexdigest() != CORE_SHA256:
        raise RuntimeError("STOP_INTEGRITY: sealed TRC1 source changed")
    name = "rrp1_two_exposure_sealed_core"
    if name in sys.modules:
        raise RuntimeError("STOP_INTEGRITY: core module name already occupied")
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError("STOP_INTEGRITY: core loader unavailable")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    if Path(module.__file__).resolve() != path.resolve():
        raise RuntimeError("STOP_INTEGRITY: core origin mismatch")
    return module


core = _load_core()


class DomainError(ValueError):
    """An input outside a declared partial-map domain, not a reset output."""


class UnsupportedPlan(DomainError):
    """Well-formed source plan excluded from this nonzero-source profile."""


def _declared_field(value, name):
    """Only missing input fields become domain errors; internal bugs propagate."""
    try:
        return object.__getattribute__(value, name)
    except AttributeError as error:
        raise TypeError("incomplete " + type(value).__name__ + ": missing " + name) from error


def _preflight(value):
    """Check complete immutable finite input graphs before sealed validators.

    No semantic replay occurs here. Per-call visited sets handle immutable
    sharing; a cycle or a mutable child is outside the declared carrier.
    """
    seen, active = set(), set()

    def visit(item):
        if type(item) in (int, bool, str, type(None)):
            return
        if type(item) is Fraction:
            numerator = _declared_field(item, "_numerator")
            denominator = _declared_field(item, "_denominator")
            if (type(numerator) is not int or type(denominator) is not int or denominator <= 0
                    or gcd(numerator, denominator) != 1):
                raise TypeError("malformed Fraction")
            return
        identity = id(item)
        if identity in active:
            raise TypeError("cyclic value outside finite immutable carrier")
        if identity in seen:
            return
        active.add(identity)
        if type(item) is tuple:
            children = item
        elif is_dataclass(item) and not isinstance(item, type):
            if not type(item).__dataclass_params__.frozen:
                raise TypeError("mutable dataclass outside immutable carrier")
            children = tuple(_declared_field(item, field.name) for field in fields(item))
        else:
            raise TypeError("unsupported or mutable child in immutable carrier")
        for child in children:
            visit(child)
        active.remove(identity)
        seen.add(identity)

    visit(value)


def _natural(value):
    if type(value) is not int or value < 0:
        raise DomainError("exact nonnegative integer required")


def _index(value):
    _natural(value)
    if value not in (0, 1):
        raise DomainError("exactly two reserved banks")


def validate_plan(plan):
    if type(plan) is not tuple or len(plan) != 2:
        raise DomainError("immutable ordered pair of full heads required")
    for head in plan:
        core.native.validate_head(head)
    if any(not any(core.signed_head(head)) for head in plan):
        raise UnsupportedPlan("ZERO_AMPLITUDE_SESSION_PLAN")
    return plan


@dataclass(frozen=True)
class ContextKey:
    core_context: object
    profile: str = PROFILE

    def __post_init__(self):
        _preflight(self)
        core._context(self.core_context)
        if type(self.profile) is not str or self.profile != PROFILE:
            raise DomainError("fixed two-bank protocol identity required")


def _context(value):
    if type(value) is not ContextKey:
        raise TypeError("ContextKey required")
    ContextKey.__post_init__(value)
    return value


@dataclass(frozen=True)
class Unprepared:
    index: int

    def __post_init__(self):
        _preflight(self)
        _index(self.index)


@dataclass(frozen=True)
class ApparatusState:
    plan: tuple
    context: ContextKey
    phase: str
    index: int
    banks: tuple

    def __post_init__(self):
        validate_apparatus(self)


def validate_apparatus(value):
    if type(value) is not ApparatusState:
        raise TypeError("complete ApparatusState required")
    _preflight(value)
    validate_plan(value.plan)
    _context(value.context)
    _index(value.index)
    if type(value.phase) is not str or value.phase not in ("READY", "RUNNING", "COMPLETE"):
        raise DomainError("unknown phase")
    if type(value.banks) is not tuple or len(value.banks) != 2:
        raise DomainError("two immutable reserved banks required")
    n = value.context.core_context.horizon
    for i, bank in enumerate(value.banks):
        unprepared = i > value.index or (i == value.index and value.phase == "READY")
        if unprepared:
            if type(bank) is not Unprepared or bank.index != i:
                raise DomainError("reserved bank must remain UNPREPARED")
            Unprepared.__post_init__(bank)
        else:
            core.validate_state(bank)
            if bank.source != value.plan[i] or bank.context != value.context.core_context:
                raise DomainError("bank source/context mismatch")
            if i < value.index or value.phase == "COMPLETE":
                if bank.tick != n:
                    raise DomainError("completed bank must retain its full history")
            elif not 0 <= bank.tick < n:
                raise DomainError("RUNNING requires an unfinished active bank")
    return value


def _initial(plan, context):
    return ApparatusState(plan, context, "READY", 0, (Unprepared(0), Unprepared(1)))


@dataclass(frozen=True)
class Selection:
    plan: tuple
    context: ContextKey
    index: int
    resource: str = "COLD_FRESH_RESERVED_BANK"

    def __post_init__(self):
        _preflight(self)
        validate_plan(self.plan)
        _context(self.context)
        _index(self.index)
        if type(self.resource) is not str or self.resource != "COLD_FRESH_RESERVED_BANK":
            raise DomainError("reserved fresh-bank descriptor required")


def _selection(plan, context, index):
    """Selection has no custody, event, tape, amplitude or outcome argument."""
    return Selection(plan, context, index)


@dataclass(frozen=True)
class ReadyState:
    selection: Selection
    custody: ApparatusState

    def __post_init__(self):
        _preflight(self)
        if type(self.selection) is not Selection:
            raise TypeError("separate Selection required")
        Selection.__post_init__(self.selection)
        validate_apparatus(self.custody)
        if self.custody.phase != "READY" or self.selection != _selection(
                self.custody.plan, self.custody.context, self.custody.index):
            raise DomainError("ready selection and exact custody disagree")


@dataclass(frozen=True)
class WaveProjection:
    index: int
    tag: str
    pair: object = None

    def __post_init__(self):
        _preflight(self)
        _index(self.index)
        if type(self.tag) is not str:
            raise TypeError("support tag required")
        if self.tag == "UNPREPARED":
            if self.pair is not None:
                raise DomainError("unprepared support is not a zero pair")
        elif self.tag == "PREPARED":
            core._pair(self.pair)
        else:
            raise DomainError("unknown support tag")


@dataclass(frozen=True)
class SupportCarrier:
    banks: tuple

    def __post_init__(self):
        _preflight(self)
        if type(self.banks) is not tuple or len(self.banks) != 2:
            raise DomainError("two tagged immutable wave projections required")
        for i, item in enumerate(self.banks):
            if type(item) is not WaveProjection or item.index != i:
                raise DomainError("ordered bank projection required")
            WaveProjection.__post_init__(item)


def support(apparatus):
    validate_apparatus(apparatus)
    return SupportCarrier(tuple(
        WaveProjection(i, "UNPREPARED") if type(bank) is Unprepared else
        WaveProjection(i, "PREPARED", bank.pair)
        for i, bank in enumerate(apparatus.banks)))


def ready_select(plan, context):
    validate_plan(plan)
    _context(context)
    return ReadyState(_selection(plan, context, 0), _initial(plan, context))


def ready_request(plan, context):
    """Input diagnostics only: no invalid request is a mathematical Ready value."""
    try:
        return "READY", ready_select(plan, context)
    except UnsupportedPlan as error:
        return "REJECTED", str(error)
    except (TypeError, ValueError) as error:
        return "INVALID_REQUEST", str(error)


def _prepare_bank(head, context):
    """Core generation consumes only the scheduled head and fixed context."""
    return core.prepare(head, context.core_context)


def _step_bank(bank):
    """Core generation consumes only the active bank, never inactive custody."""
    event = core.emit(core.step(bank))
    return core.append(bank, event), event


def _replace_active(apparatus, bank):
    banks = tuple(bank if i == apparatus.index else old
                  for i, old in enumerate(apparatus.banks))
    phase = "COMPLETE" if bank.tick == apparatus.context.core_context.horizon else "RUNNING"
    return ApparatusState(apparatus.plan, apparatus.context, phase, apparatus.index, banks)


def prepare(plan, context, ready):
    validate_plan(plan)
    _context(context)
    if type(ready) is not ReadyState:
        raise TypeError("ReadyState required")
    ReadyState.__post_init__(ready)
    old = ready.custody
    if old.plan != plan or old.context != context:
        raise DomainError("prepare source/context mismatch")
    bank = _prepare_bank(plan[old.index], context)
    after = _replace_active(old, bank)
    return support(after), after


def reset(apparatus, context):
    validate_apparatus(apparatus)
    _context(context)
    if apparatus.context != context:
        raise DomainError("reset context mismatch")
    if apparatus.phase != "COMPLETE" or apparatus.index != 0:
        raise DomainError("reset requires completed first exposure and unused second bank")
    after = ApparatusState(apparatus.plan, context, "READY", 1, apparatus.banks)
    return ReadyState(_selection(apparatus.plan, context, 1), after), after


@dataclass(frozen=True)
class RecordDelta:
    index: int
    core_event: object
    before: ApparatusState
    after: ApparatusState

    def __post_init__(self):
        _preflight(self)
        _index(self.index)
        validate_apparatus(self.before)
        validate_apparatus(self.after)
        core.validate_event(self.core_event)
        if self.before.phase != "RUNNING" or self.index != self.before.index:
            raise DomainError("delta requires an active exposure")
        expected_bank = core.append(self.before.banks[self.index], self.core_event)
        if self.after != _replace_active(self.before, expected_bank):
            raise DomainError("delta is not the exact complete step image")


@dataclass(frozen=True)
class StepOutput:
    outcome: str
    next_support: SupportCarrier
    next_apparatus: ApparatusState
    delta: RecordDelta

    def __post_init__(self):
        _preflight(self)
        if type(self.delta) is not RecordDelta:
            raise TypeError("unemitted RecordDelta required")
        RecordDelta.__post_init__(self.delta)
        if type(self.next_support) is not SupportCarrier:
            raise TypeError("SupportCarrier required")
        SupportCarrier.__post_init__(self.next_support)
        validate_apparatus(self.next_apparatus)
        if type(self.outcome) is not str or (
                self.outcome, self.next_support, self.next_apparatus) != (
                self.delta.core_event.outcome, support(self.delta.after), self.delta.after):
            raise DomainError("STEP output and complete delta disagree")


def step(carrier, apparatus, context):
    validate_apparatus(apparatus)
    _context(context)
    if type(carrier) is not SupportCarrier:
        raise TypeError("SupportCarrier required")
    SupportCarrier.__post_init__(carrier)
    if context != apparatus.context or carrier != support(apparatus):
        raise DomainError("step support/context does not describe this joint state")
    if apparatus.phase != "RUNNING":
        raise DomainError("step requires an unfinished exposure")
    bank, event = _step_bank(apparatus.banks[apparatus.index])
    after = _replace_active(apparatus, bank)
    delta = RecordDelta(apparatus.index, event, apparatus, after)
    return StepOutput(event.outcome, support(after), after, delta)


@dataclass(frozen=True)
class EventRecord:
    delta: RecordDelta

    def __post_init__(self):
        _preflight(self)
        if type(self.delta) is not RecordDelta:
            raise TypeError("full step delta required")
        RecordDelta.__post_init__(self.delta)


def _event(value):
    if type(value) is not EventRecord:
        raise TypeError("session EventRecord required")
    EventRecord.__post_init__(value)
    return value


def emit(output):
    if type(output) is not StepOutput:
        raise TypeError("complete StepOutput required")
    StepOutput.__post_init__(output)
    return EventRecord(output.delta)


def persist(apparatus, outcome, event):
    validate_apparatus(apparatus)
    _event(event)
    if type(outcome) is not str or (apparatus, outcome) != (
            event.delta.before, event.delta.core_event.outcome):
        raise DomainError("PERSIST arguments differ from exact step image")
    return event.delta.after


def reread(event):
    _event(event)
    return event


def _history(history):
    if type(history) is not tuple:
        raise TypeError("HistoryState is an immutable EventRecord tuple")
    for event in history:
        _event(event)
    return history


def append(history, event):
    """Total EventRecord* x EventRecord -> EventRecord* concatenation.

    This intentionally accepts valid duplicate, reversed and cross-session
    events. Protocol admission is a separate predicate, never this carrier map.
    """
    _history(history)
    _event(event)
    return history + (event,)


def _action_index(apparatus):
    validate_apparatus(apparatus)
    n = apparatus.context.core_context.horizon
    if apparatus.phase == "READY":
        index = 0 if apparatus.index == 0 else n + 2
    else:
        index = apparatus.banks[apparatus.index].tick + (1 if apparatus.index == 0 else n + 3)
    return index


def _action_image(kind, before):
    validate_apparatus(before)
    if type(kind) is not str:
        raise TypeError("action kind required")
    if kind == "PREPARE":
        ready = ReadyState(_selection(before.plan, before.context, before.index), before)
        return prepare(before.plan, before.context, ready)[1]
    if kind == "RESET":
        return reset(before, before.context)[1]
    if kind == "STEP":
        return step(support(before), before, before.context).next_apparatus
    raise DomainError("unknown action; passive rereads do not advance positions")


@dataclass(frozen=True)
class JournalEntry:
    kind: str
    before: ApparatusState
    after: ApparatusState

    def __post_init__(self):
        _preflight(self)
        validate_apparatus(self.before)
        validate_apparatus(self.after)
        if self.after != _action_image(self.kind, self.before):
            raise DomainError("journal entry is not the exact action image")
        if _action_index(self.after) != _action_index(self.before) + 1:
            raise DomainError("journal action must advance one exact protocol position")


def validate_journal(journal, apparatus):
    if type(journal) is not tuple:
        raise TypeError("immutable journal required")
    validate_apparatus(apparatus)
    if len(journal) != _action_index(apparatus):
        raise DomainError("journal length, apparatus and protocol position disagree")
    current = _initial(apparatus.plan, apparatus.context)
    for entry in journal:
        if type(entry) is not JournalEntry:
            raise TypeError("JournalEntry required; events are a separate carrier")
        JournalEntry.__post_init__(entry)
        if entry.before != current:
            raise DomainError("journal lost an administrative or exposure transition")
        current = entry.after
    if current != apparatus:
        raise DomainError("journal does not end at this complete apparatus")
    return journal


def journal_append(journal, kind, before, after):
    validate_journal(journal, before)
    return journal + (JournalEntry(kind, before, after),)


def _journal_events(journal):
    return tuple(EventRecord(RecordDelta(entry.before.index,
                                        entry.after.banks[entry.before.index].history[-1],
                                        entry.before, entry.after))
                 for entry in journal if entry.kind == "STEP")


@dataclass(frozen=True)
class ProtocolPosition:
    apparatus: ApparatusState
    journal: tuple

    def __post_init__(self):
        _preflight(self)
        validate_journal(self.journal, self.apparatus)

    @property
    def action_index(self):
        return _action_index(self.apparatus)


def admissible_append(position, history, event):
    """Chronological predicate at the BEFORE-step position; no mutations.

    A false result rejects protocol admission, not total sequence concatenation.
    Full journal validation retains administrative positions even when N=0.
    """
    try:
        _history(history)
        _event(event)
        if type(position) is not ProtocolPosition:
            raise TypeError("ProtocolPosition required")
        ProtocolPosition.__post_init__(position)
        apparatus, journal = position.apparatus, position.journal
        return (apparatus.phase == "RUNNING" and event.delta.before == apparatus
                and history == _journal_events(journal))
    except (TypeError, ValueError):
        return False


# The shared contract's carrier spelling denotes this same frozen value.
ProtocolState = ProtocolPosition


def admissible_extension(protocol, history, event):
    """Three-argument shared-contract spelling of the same predicate."""
    return admissible_append(protocol, history, event)


def source_eq(left, right):
    validate_plan(left)
    validate_plan(right)
    return left == right


def context_eq(left, right):
    _context(left)
    _context(right)
    return left == right


def apparatus_eq(left, right):
    validate_apparatus(left)
    validate_apparatus(right)
    return left == right


def support_eq(left, right):
    if type(left) is not SupportCarrier or type(right) is not SupportCarrier:
        raise TypeError("SupportCarrier required")
    SupportCarrier.__post_init__(left)
    SupportCarrier.__post_init__(right)
    return left == right


def ready_eq(left, right):
    if type(left) is not ReadyState or type(right) is not ReadyState:
        raise TypeError("ReadyState required")
    ReadyState.__post_init__(left)
    ReadyState.__post_init__(right)
    return left == right


def event_eq(left, right):
    _event(left)
    _event(right)
    return left == right


def history_eq(left, right):
    _history(left)
    _history(right)
    return left == right
