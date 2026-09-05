"""Exact finite-horizon energy forms of the chosen cold reservoir model."""
from dataclasses import dataclass
from fractions import Fraction as F
from pathlib import Path
import hashlib
import sys


COUPLING_PATH = Path(__file__).resolve().parents[1] / "P-DECODER-RESERVOIR-COUPLING-1" / "coupling.py"
COUPLING_SHA256 = "54f8b03762639e2573f02210b07e0d19b28935c2bc68c7f5988b15efbe26d403"
WAVE_PATH = Path(__file__).resolve().parents[1] / "P-DECODER-RETARDED-ENERGY-TRANSPORT-1" / "transport.py"
WAVE_SHA256 = "983d22690e061128d287f23ef4672fbd72954faa28f1a3fde9ce38b0d6660a60"
for _path, _expected in ((COUPLING_PATH, COUPLING_SHA256), (WAVE_PATH, WAVE_SHA256)):
    if hashlib.sha256(_path.read_bytes()).hexdigest() != _expected:
        raise RuntimeError("STOP_INTEGRITY: immutable inherited dependency mismatch")
sys.path.insert(0, str(COUPLING_PATH.parent))
try:
    import coupling as reservoir
finally:
    sys.path.pop(0)
if Path(reservoir.__file__).resolve() != COUPLING_PATH:
    raise RuntimeError("STOP_INTEGRITY: unexpected coupling module origin")
wave = reservoir.wave
if Path(wave.__file__).resolve() != WAVE_PATH:
    raise RuntimeError("STOP_INTEGRITY: unexpected wave module origin")


def matrix(value):
    if type(value) is not tuple or len(value) != 4:
        raise ValueError("four immutable matrix rows required")
    return tuple(wave.coefficients(row) for row in value)


def validate_matrix(value):
    if matrix(value) != value or any(type(a) is not F for row in value for a in row):
        raise TypeError("canonical rational matrix required")


def identity():
    return tuple(tuple(F(i == j) for j in range(4)) for i in range(4))


def gram():
    return tuple(tuple(F(i == j) - F(1, 5) for j in range(4)) for i in range(4))


def gram_inverse():
    return tuple(tuple(F(i == j) + 1 for j in range(4)) for i in range(4))


def transpose(value):
    validate_matrix(value)
    return tuple(tuple(value[j][i] for j in range(4)) for i in range(4))


def add_matrices(*values):
    for value in values:
        validate_matrix(value)
    return tuple(tuple(sum((v[i][j] for v in values), F(0)) for j in range(4)) for i in range(4))


def scale_matrix(value, factor):
    validate_matrix(value)
    factor = wave.rational(factor)
    return tuple(tuple(factor * a for a in row) for row in value)


def matmul(left, right):
    validate_matrix(left)
    validate_matrix(right)
    return tuple(tuple(sum((left[i][k] * right[k][j] for k in range(4)), F(0))
                       for j in range(4)) for i in range(4))


def outer(row):
    row = wave.coefficients(row)
    return tuple(tuple(a * b for b in row) for a in row)


def quadratic(value, z):
    validate_matrix(value)
    z = wave.coefficients(z)
    return sum((z[i] * value[i][j] * z[j] for i in range(4) for j in range(4)), F(0))


@dataclass(frozen=True)
class Slot:
    tick: int
    site: tuple
    row: tuple
    matrix: tuple

    def __post_init__(self):
        if type(self.tick) is not int or self.tick < 0:
            raise ValueError("nonnegative integer slot tick required")
        wave.site(self.site)
        if wave.coefficients(self.row) != self.row or any(type(a) is not F for a in self.row):
            raise TypeError("canonical rational port row required")
        validate_matrix(self.matrix)


@dataclass(frozen=True)
class Partition:
    gamma: tuple
    horizon: int
    slots: tuple
    residual: tuple

    def __post_init__(self):
        reservoir.Context(self.gamma, F(1))
        if type(self.horizon) is not int or self.horizon < 0:
            raise ValueError("nonnegative integer horizon required")
        if type(self.slots) is not tuple or any(type(s) is not Slot for s in self.slots):
            raise TypeError("immutable complete slots required")
        expected = tuple((tick, x) for tick in range(self.horizon) for x, _ in self.gamma)
        if tuple((s.tick, s.site) for s in self.slots) != expected:
            raise ValueError("slots must cover every tick and channel exactly once")
        gamma = dict(self.gamma)
        if any(s.matrix != scale_matrix(outer(s.row), 2 * gamma[s.site]) for s in self.slots):
            raise ValueError("slot form does not equal twice its port energy")
        validate_matrix(self.residual)
        if self.residual != transpose(self.residual):
            raise ValueError("symmetric residual form required")


def energy_form(pairs):
    """Direct bilinear form of actual final waves, independent of deposit sums."""
    if type(pairs) is not tuple or len(pairs) != 4 or any(type(p) is not wave.Pair for p in pairs):
        raise TypeError("four wave pairs required")
    differences = tuple(wave.add(p.current, wave.scale(p.previous, -1)) for p in pairs)
    laplacians = tuple(wave.laplacian(p.current) for p in pairs)
    return tuple(tuple(wave.inner(differences[i], differences[j])
                       + (wave.inner(pairs[i].previous, laplacians[j])
                          + wave.inner(pairs[j].previous, laplacians[i])) / 2
                       for j in range(4)) for i in range(4))


def build_prefix(context, horizon):
    if type(context) is not reservoir.Context:
        raise TypeError("frozen reservoir context required")
    if type(horizon) is not int or horizon < 0:
        raise ValueError("nonnegative integer horizon required")
    pairs = tuple(wave.prepare(tuple(int(i == j) for i in range(4))) for j in range(4))
    slots = ()
    answer = (Partition(context.gamma, 0, slots, energy_form(pairs)),)
    for tick in range(horizon):
        interactions = tuple(reservoir.couple(p, context) for p in pairs)
        outgoing = tuple(dict(i.outgoing) for i in interactions)
        for x, gamma in context.gamma:
            row = tuple(values.get(x, F(0)) for values in outgoing)
            slots += (Slot(tick, x, row, scale_matrix(outer(row), 2 * gamma)),)
        pairs = tuple(i.after for i in interactions)
        answer += (Partition(context.gamma, tick + 1, slots, energy_form(pairs)),)
    return answer


def build(context, horizon):
    return build_prefix(context, horizon)[-1]


def fine_forms(partition):
    if type(partition) is not Partition:
        raise TypeError("Partition required")
    return tuple(s.matrix for s in partition.slots) + (partition.residual,)


def group_forms(partition, groups):
    """Group every deposit slot once; keep the residual as the last output."""
    if type(partition) is not Partition or type(groups) is not tuple:
        raise TypeError("Partition and immutable groups required")
    if any(type(group) is not tuple or any(type(i) is not int for i in group) for group in groups):
        raise TypeError("immutable integer slot-index groups required")
    indices = tuple(i for group in groups for i in group)
    if sorted(indices) != list(range(len(partition.slots))):
        raise ValueError("groups must partition all deposit slots without repetition")
    return tuple(add_matrices(*(partition.slots[i].matrix for i in group)) for group in groups) + (partition.residual,)


def normalized_shares(partition, z, groups=None):
    z = wave.coefficients(z)
    forms = fine_forms(partition) if groups is None else group_forms(partition, groups)
    mass = quadratic(gram(), z)
    if mass == 0:
        return "ZERO_DENOMINATOR"
    return tuple(quadratic(value, z) / mass for value in forms)


def operator_forms(partition, groups=None):
    forms = fine_forms(partition) if groups is None else group_forms(partition, groups)
    inverse = gram_inverse()
    return tuple(matmul(inverse, value) for value in forms)


def state_operator(z):
    z = wave.coefficients(z)
    metric = gram()
    mass = quadratic(metric, z)
    if mass == 0:
        return "ZERO_DENOMINATOR"
    covector = tuple(sum((z[i] * metric[i][j] for i in range(4)), F(0)) for j in range(4))
    return tuple(tuple(z[i] * covector[j] / mass for j in range(4)) for i in range(4))


def trace(value):
    validate_matrix(value)
    return sum((value[i][i] for i in range(4)), F(0))
