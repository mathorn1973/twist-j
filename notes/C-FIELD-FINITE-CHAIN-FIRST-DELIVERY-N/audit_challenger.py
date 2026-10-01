"""NON-CANONICAL L1: generic finite-chain flat-state audit adapter.

The local scalar arithmetic is inherited, with its exact public source hash,
from the independently authored challenger of the three-cell predecessor.
This adapter is new, but makes no claim of fresh implementation independence.
It never calls the predecessor main or its hardcoded three-cell network.
Only the named repository source is read; no private or external input is used.

A state is a tuple of 32*n-1 integers: n complete 31-coordinate cells followed
by n-1 stored channels. The local cell layout is matter[12], spectators[12],
raw field[6], resource[1]. Literal tuple equality is full-state equality.
"""

from functools import lru_cache
from hashlib import sha256
from pathlib import Path
from types import ModuleType


PREDECESSOR_SHA256 = "fc435a7efffea8edd4bd8e11aa12e16c2d1489a39c74997ae0b204837b7445b1"


@lru_cache(maxsize=1)
def _local():
    """Load only hash-checked public definitions, under a non-main name."""
    source_path = (Path(__file__).resolve().parents[1]
                   / "C-FIELD-THREE-CELL-DELAYED-TRANSFER-N" / "break.py")
    source = source_path.read_bytes()
    if sha256(source).hexdigest() != PREDECESSOR_SHA256:
        raise RuntimeError("inherited challenger source hash mismatch")
    module = ModuleType("finite_chain_inherited_challenger_local")
    module.__file__ = str(source_path)
    exec(compile(source, str(source_path), "exec"), module.__dict__)
    return module


def _length(n):
    if type(n) is not int or n < 2:
        raise ValueError("chain length must be an integer at least two")


def _legal(state, n):
    _length(n)
    assert len(state) == 32*n-1
    assert all(type(value) is int for value in state)
    assert all(state[31*i+30] >= 0 for i in range(n))
    assert all(value >= 0 for value in state[31*n:])


def _cut(cut, n):
    if cut is not None and (type(cut) is not int or not 0 <= cut < n-1):
        raise ValueError("cut must name one channel or be None")


def initial(n, w):
    """Return the neutral preparation for an integer seed with H(w)=1."""
    _length(n)
    w = tuple(w)
    assert len(w) == 4 and all(type(value) is int for value in w)
    local = _local()
    assert local.hform(w) == 1
    source = local.R[:] + [0]*12 + local.pfield(local.stretch(w)) + [0]
    target = local.R[:] + [0]*19
    state = tuple(source + [0]*(31*(n-2)) + target + [0]*(n-1))
    _legal(state, n)
    return state


def flatten(state):
    """The running carrier already contains every coordinate in order."""
    return tuple(state)


def accounts(state, n):
    """Return total energy, node charges, defects, spectators and matter sums.

    Each component after energy is flattened in increasing cell order.
    The inherited local account computes energy from every raw coordinate.
    """
    _legal(state, n)
    local = _local()
    cells = [local.cell_accounts(tuple(state[31*i:31*i+31])) for i in range(n)]
    energy = sum(cell[0] for cell in cells) + sum(state[31*n:])
    return (energy,
            tuple(value for cell in cells for value in cell[1]),
            tuple(value for cell in cells for value in cell[2]),
            tuple(value for cell in cells for value in cell[3]),
            tuple(value for cell in cells for value in cell[4]))


def layers(state, n, cut=None, inverse=False):
    """Yield (name, complete_state) after each of four chronological layers.

    Forward order is G; A; B; F. Inverse order is F^-1; B; A; G.
    Each contact exchanges complete old values. A cut omits both contacts
    incident on that channel, retaining its separately stored content.
    """
    _legal(state, n)
    _cut(cut, n)
    local = _local()
    current = list(state)
    order = ("F^-1", "B", "A", "G") if inverse else ("G", "A", "B", "F")
    for kind in order:
        if kind == "G":
            for i in range(n):
                base = 31*i
                current[base:base+31] = local.reaction(current[base:base+31])
        elif kind in ("F", "F^-1"):
            transform = local.field_backward if kind == "F^-1" else local.field_forward
            for i in range(n):
                base = 31*i+24
                current[base:base+6] = transform(current[base:base+6])
        else:
            for j in range(n-1):
                if j == cut:
                    continue
                resource = 31*(j if kind == "A" else j+1)+30
                channel = 31*n+j
                current[resource], current[channel] = current[channel], current[resource]
        boundary = tuple(current)
        _legal(boundary, n)
        yield kind, boundary


def step(state, n, cut=None, inverse=False):
    """Apply the declared macrostep or its exact reverse to the full state."""
    current = tuple(state)
    for _, current in layers(current, n, cut=cut, inverse=inverse):
        pass
    return current
