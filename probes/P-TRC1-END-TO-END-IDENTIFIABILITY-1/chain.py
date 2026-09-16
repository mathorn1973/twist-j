"""MODEL-side TRC1 composition; import only after the complete public pin.

The source is kicked once. Native checkpoints label coupled transitions but do
not force the wave. All occurrence weights are an explicit preparation input.
Pure finite caches change no mathematical output. No physical certificate,
FOREIGN_NIST processor, or conforming #539 reset is implemented here.
Matter, Geometry, Prediction and Posterior are output containers, not validated
request carriers. Public transition/record APIs admit generated model states.
"""

from dataclasses import dataclass, fields
from fractions import Fraction as F
from functools import lru_cache
import hashlib
import importlib.util
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
DEPENDENCIES = (
    ("probes/P-DECODER-POINTED-BATCH-CONFORMANCE-1/kernel.py",
     "8fe60efb5f1c8888ac455332ec8305bc531687836f5c604aedd2e483ed534ba9"),
    ("probes/P-DECODER-RETARDED-ENERGY-TRANSPORT-1/transport.py",
     "983d22690e061128d287f23ef4672fbd72954faa28f1a3fde9ce38b0d6660a60"),
    ("probes/P-DECODER-RESERVOIR-COUPLING-1/coupling.py",
     "54f8b03762639e2573f02210b07e0d19b28935c2bc68c7f5988b15efbe26d403"),
)
for _relative, _sha256 in DEPENDENCIES:
    if hashlib.sha256((ROOT / _relative).read_bytes()).hexdigest() != _sha256:
        raise RuntimeError("STOP_INTEGRITY: inherited source identity mismatch")


def _load(name, relative):
    if name in sys.modules:
        raise RuntimeError("STOP_INTEGRITY: module name already occupied")
    path = (ROOT / relative).resolve()
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError("STOP_INTEGRITY: no source module loader")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    if Path(module.__file__).resolve() != path:
        raise RuntimeError("STOP_INTEGRITY: inherited module origin mismatch")
    return module


native = _load("trc1_identifiability_native", DEPENDENCIES[0][0])
reservoir = _load("trc1_identifiability_reservoir", DEPENDENCIES[2][0])
wave = reservoir.wave
if Path(wave.__file__).resolve() != (ROOT / DEPENDENCIES[1][0]).resolve():
    raise RuntimeError("STOP_INTEGRITY: inherited transport origin mismatch")


def _natural(value, name):
    if type(value) is not int or value < 0:
        raise ValueError(name + " must be an exact nonnegative integer")


@dataclass(frozen=True)
class Context:
    gamma: tuple
    quantum: F
    horizon: int

    def __post_init__(self):
        wave.validate_field(self.gamma)
        if any(value <= 0 for _, value in self.gamma):
            raise ValueError("active conductances must be strictly positive")
        if type(self.quantum) is not F or self.quantum <= 0:
            raise ValueError("threshold must be a positive Fraction")
        _natural(self.horizon, "horizon")


def _context(value):
    if type(value) is not Context:
        raise TypeError("TRC1 Context required")
    Context.__post_init__(value)
    return value


@lru_cache(maxsize=128)
def _core_context(context):
    _context(context)
    return reservoir.Context(context.gamma, context.quantum)


def _pair(value):
    if type(value) is not wave.Pair:
        raise TypeError("inherited exact wave Pair required")
    wave.validate_field(value.previous)
    wave.validate_field(value.current)


def _port(value, context, nonnegative=False):
    reservoir.port(value, _core_context(context))
    if nonnegative and any(amount < 0 for _, amount in value):
        raise ValueError("negative heat or deposit")


def _counts(value, context):
    if type(value) is not tuple or len(value) != len(context.gamma):
        raise TypeError("one immutable count per active site required")
    for item, (site, _) in zip(value, context.gamma):
        if type(item) is not tuple or len(item) != 2 or item[0] != site:
            raise ValueError("count sites must equal the ordered active sites")
        wave.site(item[0])
        _natural(item[1], "count")


def _crossings(value, context):
    if type(value) is not tuple or any(type(item) is not reservoir.Crossing for item in value):
        raise TypeError("immutable inherited Crossing tuple required")
    sites = tuple(item.site for item in value)
    if sites != tuple(sorted(set(sites))) or not set(sites) <= set(dict(context.gamma)):
        raise ValueError("crossing sites must be sorted distinct active sites")
    for item in value:
        reservoir.Crossing.__post_init__(item)


def checkpoint_at(head, tick):
    native.validate_head(head)
    _natural(tick, "relative tick")
    checkpoint = head
    for _ in range(tick):
        checkpoint = native.u_step(checkpoint)
    return checkpoint


def signed_head(head):
    return native.balanced_head(head)


def support(head):
    native.validate_head(head)
    return ("SUPPORTED" if any(signed_head(head)) else "ZERO_SOURCE", head)


@dataclass(frozen=True)
class Matter:
    source_head: tuple
    signed_source: tuple
    support_state: str
    total_weight: F
    branch_weights: tuple
    density_state: object
    normalized_weight_state: object
    linear_tr4: int
    binary_theta: int


def matter_at(head, context, tick):
    native.validate_head(head)
    _context(context)
    _natural(tick, "query cut")
    if tick > context.horizon:
        raise ValueError("query outside fixed context horizon")
    current = checkpoint_at(head, tick)
    qdd = native.direct_qdd(head)
    return Matter(head, signed_head(head), qdd.support_state, qdd.total_weight,
                  qdd.branch_weights, qdd.density_state, qdd.normalized_weight_state,
                  native.linear_tr4(current), native.theta(current[0]))


@dataclass(frozen=True)
class Apparatus:
    source: tuple
    context: Context
    tick: int
    tape: tuple
    heat: tuple

    def __post_init__(self):
        native.validate_head(self.source)
        _context(self.context)
        _natural(self.tick, "apparatus tick")
        if self.tick > self.context.horizon or type(self.tape) is not tuple or len(self.tape) != self.tick:
            raise ValueError("tape length, tick and horizon disagree")
        _port(self.heat, self.context, nonnegative=True)
        heat = ()
        for outgoing in self.tape:
            _port(outgoing, self.context)
            amplitudes = dict(outgoing)
            heat = wave.add(heat, wave.field((x, gamma * amplitudes.get(x, F(0)) ** 2)
                                            for x, gamma in self.context.gamma))
        if self.heat != heat:
            raise ValueError("heat differs from the complete signed tape account")


def _apparatus(value):
    if type(value) is not Apparatus:
        raise TypeError("complete TRC1 Apparatus required")
    Apparatus.__post_init__(value)


@lru_cache(maxsize=128)
def _transition_values(source, context, checkpoint, pair, apparatus):
    """Complete pure cold transition, cached only by its immutable inputs."""
    native.validate_head(source)
    _context(context)
    native.validate_head(checkpoint)
    _pair(pair)
    _apparatus(apparatus)
    tick = apparatus.tick
    if apparatus.source != source or apparatus.context != context or tick >= context.horizon:
        raise ValueError("incompatible source/context or completed horizon")
    if checkpoint != checkpoint_at(source, tick):
        raise ValueError("checkpoint is not the native orbit label at this cut")
    interaction = reservoir.couple(pair, _core_context(context))
    heat = wave.add(apparatus.heat, interaction.transfer)
    after = Apparatus(source, context, tick + 1,
                      apparatus.tape + (interaction.outgoing,), heat)
    core = _core_context(context)
    ranges = reservoir.crossings(apparatus.heat, heat, core)
    outcome = "THRESHOLD_CROSSINGS" if ranges else "NO_CROSSINGS"
    return (source, context, tick, checkpoint, native.u_step(checkpoint),
            pair, interaction.after, apparatus, after, interaction.outgoing,
            interaction.transfer, apparatus.heat, heat,
            reservoir.threshold_counts(apparatus.heat, core),
            reservoir.threshold_counts(heat, core), reservoir.remainders(heat, core),
            ranges, outcome)


@lru_cache(maxsize=256)
def _generated_boundary(source, context, tick):
    """Replay the fixed source to a cut without constructing event objects."""
    native.validate_head(source)
    _context(context)
    _natural(tick, "generated boundary tick")
    if tick > context.horizon:
        raise ValueError("generated boundary exceeds horizon")
    checkpoint = source
    pair = wave.prepare(signed_head(source))
    apparatus = Apparatus(source, context, 0, (), ())
    for _ in range(tick):
        values = _transition_values(source, context, checkpoint, pair, apparatus)
        checkpoint, pair, apparatus = values[4], values[6], values[8]
    return checkpoint, pair, apparatus


@dataclass(frozen=True)
class RecordDelta:
    source: tuple
    context: Context
    tick: int
    start_checkpoint: tuple
    completed_checkpoint: tuple
    pair_before: object
    pair_after: object
    apparatus_before: Apparatus
    apparatus_after: Apparatus
    outgoing: tuple
    deposit: tuple
    heat_before: tuple
    heat_after: tuple
    counts_before: tuple
    counts_after: tuple
    remainder_after: tuple
    crossings: tuple
    outcome: str

    def __post_init__(self):
        _validate_delta(self)


DELTA_FIELDS = tuple(field.name for field in fields(RecordDelta))


def _delta_tuple(delta):
    return tuple(getattr(delta, name) for name in DELTA_FIELDS)


def _validate_delta(delta):
    if type(delta) not in (RecordDelta, Event):
        raise TypeError("complete RecordDelta or Event required")
    native.validate_head(delta.source)
    _context(delta.context)
    _natural(delta.tick, "event tick")
    native.validate_head(delta.start_checkpoint)
    native.validate_head(delta.completed_checkpoint)
    _pair(delta.pair_before)
    _pair(delta.pair_after)
    _apparatus(delta.apparatus_before)
    _apparatus(delta.apparatus_after)
    _port(delta.outgoing, delta.context)
    for value in (delta.deposit, delta.heat_before, delta.heat_after, delta.remainder_after):
        _port(value, delta.context, nonnegative=True)
    _counts(delta.counts_before, delta.context)
    _counts(delta.counts_after, delta.context)
    _crossings(delta.crossings, delta.context)
    if type(delta.outcome) is not str:
        raise TypeError("outcome tag must be a string")
    if (delta.start_checkpoint, delta.pair_before, delta.apparatus_before) != (
            _generated_boundary(delta.source, delta.context, delta.tick)):
        raise ValueError("record before-state is not generated by the declared source")
    expected = _transition_values(delta.source, delta.context, delta.start_checkpoint,
                                  delta.pair_before, delta.apparatus_before)
    if _delta_tuple(delta) != expected:
        raise ValueError("record is not the exact cold transition image")


@dataclass(frozen=True)
class Event(RecordDelta):
    transition_complete: bool = True

    def __post_init__(self):
        RecordDelta.__post_init__(self)
        if type(self.transition_complete) is not bool or not self.transition_complete:
            raise ValueError("complete model transition tag required")


def validate_event(event):
    if type(event) is not Event:
        raise TypeError("emitted TRC1 Event required")
    Event.__post_init__(event)
    return event


@dataclass(frozen=True)
class StepOutput:
    outcome: str
    next_pair: object
    next_apparatus: Apparatus
    delta: RecordDelta

    def __post_init__(self):
        if type(self.delta) is not RecordDelta:
            raise TypeError("STEP owns an un-emitted RecordDelta")
        _validate_delta(self.delta)
        _pair(self.next_pair)
        _apparatus(self.next_apparatus)
        if type(self.outcome) is not str:
            raise TypeError("STEP outcome tag must be a string")
        if (self.outcome, self.next_pair, self.next_apparatus) != (
                self.delta.outcome, self.delta.pair_after, self.delta.apparatus_after):
            raise ValueError("STEP tuple and complete delta disagree")


@dataclass(frozen=True)
class CompleteState:
    source: tuple
    context: Context
    checkpoint: tuple
    pair: object
    apparatus: Apparatus
    history: tuple

    @property
    def tick(self):
        return self.apparatus.tick

    def __post_init__(self):
        validate_state(self)


def validate_state(state):
    """Validate the generated-history domain, including all signed transitions."""
    if type(state) is not CompleteState:
        raise TypeError("ordinary complete model state required")
    native.validate_head(state.source)
    _context(state.context)
    native.validate_head(state.checkpoint)
    _pair(state.pair)
    _apparatus(state.apparatus)
    if type(state.history) is not tuple or len(state.history) > state.context.horizon:
        raise ValueError("immutable generated history within horizon required")
    pair = wave.prepare(signed_head(state.source))
    apparatus = Apparatus(state.source, state.context, 0, (), ())
    checkpoint = state.source
    for tick, event in enumerate(state.history):
        validate_event(event)
        if (event.source, event.context, event.tick, event.start_checkpoint,
                event.pair_before, event.apparatus_before) != (
                state.source, state.context, tick, checkpoint, pair, apparatus):
            raise ValueError("history violates source, native cut or state continuity")
        checkpoint, pair, apparatus = (event.completed_checkpoint,
                                       event.pair_after, event.apparatus_after)
    if (state.checkpoint, state.pair, state.apparatus) != (checkpoint, pair, apparatus):
        raise ValueError("current complete state differs from its generated history")
    return state


def prepare(head, context):
    native.validate_head(head)
    _context(context)
    return CompleteState(head, context, head, wave.prepare(signed_head(head)),
                         Apparatus(head, context, 0, (), ()), ())


def prepare_request(head, context):
    """Tag malformed requests while preserving implementation failures."""
    try:
        native.validate_head(head)
        _context(context)
    except (TypeError, ValueError) as error:
        return "UNSUPPORTED_REQUEST", str(error), (head, context)
    return "PREPARED_MODEL", prepare(head, context)


def step(state):
    validate_state(state)
    delta = RecordDelta(*_transition_values(state.source, state.context, state.checkpoint,
                                           state.pair, state.apparatus))
    return StepOutput(delta.outcome, delta.pair_after, delta.apparatus_after, delta)


def emit(output):
    if type(output) is not StepOutput:
        raise TypeError("EMIT requires the complete STEP output")
    StepOutput.__post_init__(output)
    return Event(*_delta_tuple(output.delta), True)


def persist(old, event):
    _apparatus(old)
    validate_event(event)
    if old != event.apparatus_before:
        raise ValueError("PERSIST old apparatus does not equal the record snapshot")
    return event.apparatus_after


def append(state, event):
    validate_state(state)
    validate_event(event)
    expected = emit(step(state))
    if event != expected:
        raise ValueError("APPEND requires exactly the next generated transition")
    after = persist(state.apparatus, event)
    return CompleteState(state.source, state.context, event.completed_checkpoint,
                         event.pair_after, after, state.history + (event,))


@dataclass(frozen=True)
class EndState:
    payload: CompleteState

    def __post_init__(self):
        validate_state(self.payload)
        if self.payload.tick != self.payload.context.horizon:
            raise ValueError("END must retain a completed state")


def advance(state):
    if type(state) is EndState:
        EndState.__post_init__(state)
        return state
    validate_state(state)
    if state.tick == state.context.horizon:
        return EndState(state)
    return append(state, emit(step(state)))


def apparatus_of(state):
    if type(state) is EndState:
        EndState.__post_init__(state)
        return state.payload.apparatus
    validate_state(state)
    return state.apparatus


def reread(event):
    validate_event(event)
    return event


def reset_request(state):
    if type(state) is Apparatus:
        _apparatus(state)
    elif type(state) is EndState:
        EndState.__post_init__(state)
    else:
        validate_state(state)
    return "REJECTED_RESET_DISABLED", state


def physical_request(value):
    """No certificate is admitted here; this is an administrative boundary."""
    return "STOP_PHYSICAL", value


def run(head, context, k=None):
    _context(context)
    k = context.horizon if k is None else k
    _natural(k, "requested prefix")
    if k > context.horizon:
        raise ValueError("prefix exceeds the fixed context horizon")
    state = prepare(head, context)
    for _ in range(k):
        state = advance(state)
    return state


fold = run


@dataclass(frozen=True)
class CurrentField:
    """Exact finite antisymmetric edge field, represented by its defining pairs."""
    before: object
    after: object

    def __post_init__(self):
        _pair(self.before)
        _pair(self.after)
        if self.after.previous != self.before.current:
            raise ValueError("current descriptor needs adjacent wave pairs")

    def value(self, x, y):
        return wave.current(self.before, self.after.current, x, y)

    def entries(self):
        """Nonzero x<y values; reverse orientations have the opposite value."""
        u, v, w = dict(self.before.previous), dict(self.before.current), dict(self.after.current)
        edges = {}
        for x in set(u) | set(v) | set(w):
            for offset, coefficient in wave.stencil():
                y = wave.shifted(x, offset)
                left, right = sorted((x, y))
                edges[(left, right)] = coefficient
        values = []
        for (x, y), coefficient in sorted(edges.items()):
            value = wave._current(u, v, w, x, y, coefficient)
            if value:
                values.append((x, y, value))
        return tuple(values)


@dataclass(frozen=True)
class Geometry:
    pair_sequence: tuple
    port_sequence: tuple
    energy_sequence: tuple
    local_current_sequence: tuple


def geometry(state):
    validate_state(state)
    pairs = (wave.prepare(signed_head(state.source)),) + tuple(event.pair_after for event in state.history)
    return Geometry(pairs, tuple(event.outgoing for event in state.history),
                    tuple(wave.energy(pair) for pair in pairs),
                    tuple(CurrentField(event.pair_before, event.pair_after) for event in state.history))


@dataclass(frozen=True)
class Packet:
    origin: str
    source_run_context_refs: tuple
    interval_id: int
    ordered_evidence_refs: tuple
    category: str
    multiplicities: tuple
    coverage_evidence: str
    calibration_refs: str
    event_ref: Event

    def __post_init__(self):
        validate_event(self.event_ref)
        _natural(self.interval_id, "packet interval")
        _counts(self.multiplicities, self.event_ref.context)
        if type(self.source_run_context_refs) is not tuple or type(self.ordered_evidence_refs) is not tuple:
            raise TypeError("immutable packet identity and evidence required")
        if len(self.source_run_context_refs) != 2:
            raise ValueError("packet identity must contain source and context")
        native.validate_head(self.source_run_context_refs[0])
        _context(self.source_run_context_refs[1])
        if any(type(item) is not Event for item in self.ordered_evidence_refs):
            raise TypeError("packet evidence must consist of complete model events")
        for item in self.ordered_evidence_refs:
            validate_event(item)
        if any(type(tag) is not str for tag in (
                self.origin, self.category, self.coverage_evidence, self.calibration_refs)):
            raise TypeError("packet tags must be strings")
        if tuple(getattr(self, field.name) for field in fields(Packet)) != _packet_values(self.event_ref):
            raise ValueError("packet differs from the complete model observation")


def _packet_values(event):
    before, after = dict(event.counts_before), dict(event.counts_after)
    multiplicities = tuple((x, after[x] - before[x]) for x, _ in event.context.gamma)
    total = sum(value for _, value in multiplicities)
    if not any(signed_head(event.source)):
        category = "ZERO_SOURCE_ACCOUNTING"
    else:
        category = ("NO_THRESHOLD_CROSSING" if total == 0 else
                    "SINGLE_THRESHOLD_CROSSING" if total == 1 else "MULTIPLE_THRESHOLD_CROSSINGS")
    return ("MODEL_RRP1", (event.source, event.context), event.tick, (event,), category,
            multiplicities, "MODEL_TRANSITION_COMPLETE", "UNRESOLVED", event)


def model_read(event):
    validate_event(event)
    return Packet(*_packet_values(event))


@dataclass(frozen=True)
class Visible:
    context: Context
    tick: int
    kind: str
    multiplicities: tuple
    crossings: tuple

    def __post_init__(self):
        _context(self.context)
        _natural(self.tick, "visible tick")
        if self.tick >= self.context.horizon:
            raise ValueError("visible packet outside interaction horizon")
        _counts(self.multiplicities, self.context)
        _crossings(self.crossings, self.context)
        counts = {item.site: item.count for item in self.crossings}
        if any(value != counts.get(x, 0) for x, value in self.multiplicities):
            raise ValueError("visible multiplicities differ from complete ordinal ranges")
        total = sum(counts.values())
        expected = "NO_CROSSING" if total == 0 else "SINGLE_CROSSING" if total == 1 else "MULTIPLE_CROSSINGS"
        if type(self.kind) is not str or self.kind != expected:
            raise ValueError("visible kind differs from its multiplicity")


def visible(packet):
    if type(packet) is not Packet:
        raise TypeError("VISIBLE requires a MODEL packet")
    Packet.__post_init__(packet)
    event = packet.event_ref
    total = sum(value for _, value in packet.multiplicities)
    kind = "NO_CROSSING" if total == 0 else "SINGLE_CROSSING" if total == 1 else "MULTIPLE_CROSSINGS"
    return Visible(event.context, event.tick, kind, packet.multiplicities, event.crossings)


def visible_history(state):
    validate_state(state)
    return tuple(visible(model_read(event)) for event in state.history)


def transition(state):
    after = advance(state)
    return (after, "END") if type(after) is EndState else (after, visible(model_read(after.history[-1])))


def kernel_mass(state, successor, observation):
    return F(int((successor, observation) == transition(state)))


def validate_ensemble(ensemble):
    if type(ensemble) is not tuple or not ensemble:
        raise ValueError("nonempty immutable source ensemble required")
    heads = []
    total = F(0)
    for item in ensemble:
        if type(item) is not tuple or len(item) != 2:
            raise TypeError("ensemble atom must be (head, Fraction)")
        head, weight = item
        native.validate_head(head)
        if type(weight) is not F or weight <= 0:
            raise ValueError("zero atoms must be omitted; positive Fraction weights required")
        heads.append(head)
        total += weight
    if tuple(heads) != tuple(sorted(set(heads))) or total != 1:
        raise ValueError("ensemble heads must be distinct sorted and weights normalized")
    return ensemble


def _visible_key(value):
    return (value.context.gamma, value.context.quantum, value.context.horizon, value.tick,
            value.kind, value.multiplicities,
            tuple((item.site, item.first, item.last) for item in value.crossings))


def pushforward(ensemble, context, k=None):
    validate_ensemble(ensemble)
    _context(context)
    k = context.horizon if k is None else k
    _natural(k, "prediction prefix")
    if k > context.horizon:
        raise ValueError("prediction exceeds fixed context horizon")
    masses = {}
    for head, weight in ensemble:
        output = visible_history(run(head, context, k))
        masses[output] = masses.get(output, F(0)) + weight
    return tuple(sorted(masses.items(), key=lambda item: tuple(_visible_key(value) for value in item[0])))


def full_pushforward(ensemble, context, k=None):
    """Full ordered events; first occurrence order follows the canonical source list."""
    validate_ensemble(ensemble)
    _context(context)
    k = context.horizon if k is None else k
    _natural(k, "prediction prefix")
    if k > context.horizon:
        raise ValueError("prediction exceeds fixed context horizon")
    masses = {}
    for head, weight in ensemble:
        output = run(head, context, k).history
        masses[output] = masses.get(output, F(0)) + weight
    return tuple(masses.items())


@dataclass(frozen=True)
class Prediction:
    context_ref: Context
    ensemble_ref: tuple
    horizon: int
    packet_prefix_mass_table: tuple


def prediction(ensemble, context, k=None):
    table = pushforward(ensemble, context, k)
    return Prediction(context, ensemble, context.horizon if k is None else k, table)


@dataclass(frozen=True)
class Posterior:
    status: str
    evidence_mass: F
    atoms: tuple
    next_law: tuple
    states: tuple


def posterior(ensemble, context, prefix):
    validate_ensemble(ensemble)
    _context(context)
    if type(prefix) is not tuple or len(prefix) > context.horizon:
        raise ValueError("immutable visible prefix within horizon required")
    for tick, item in enumerate(prefix):
        if type(item) is not Visible:
            raise TypeError("posterior evidence must have the MODEL visible type")
        Visible.__post_init__(item)
        if item.context != context or item.tick != tick:
            raise ValueError("evidence violates context or ordered tick ownership")
    surviving = []
    mass = F(0)
    for head, weight in ensemble:
        state = run(head, context, len(prefix))
        if visible_history(state) == prefix:
            surviving.append((head, weight, state))
            mass += weight
    if mass == 0:
        return Posterior("IMPOSSIBLE_UNDER_FIXED_MODEL", F(0), (), (), ())
    atoms = tuple((head, weight / mass) for head, weight, _ in surviving)
    next_masses = {}
    for _, weight, state in surviving:
        _, observation = transition(state)
        next_masses[observation] = next_masses.get(observation, F(0)) + weight / mass
    law = tuple(sorted(next_masses.items(), key=lambda item: () if item[0] == "END" else _visible_key(item[0])))
    return Posterior("CONDITIONAL_MODEL_LAW", mass, atoms, law,
                     tuple(state for _, _, state in surviving))
