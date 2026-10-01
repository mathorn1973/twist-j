"""NON-CANONICAL L1: flat-state challenger for bounded receiver recording.

The complete running carrier is 32*n-1 integers: n 31-coordinate cells,
followed by n-1 stored channels. A cell has matter[12], spectators[12],
raw field[6], resource[1]. Literal equality retains every coordinate.

The generic adapter follows the already public first-delivery challenger.
Local scalar arithmetic is reused from the hash-pinned, independently
authored three-cell challenger. This is honest reuse, not newly independent
local-law authorship. This file never imports the new primary implementation
or calls the inherited main, hardcoded network, inventories or certificates.
The new target cycle and five-layer composition are implemented here on the
flat carrier. Only the named repository dependency is read at runtime.
"""

from functools import lru_cache
from hashlib import sha256
from pathlib import Path
from types import ModuleType


PREDECESSOR_SHA256 = "fc435a7efffea8edd4bd8e11aa12e16c2d1489a39c74997ae0b204837b7445b1"

# Literal ordered registers, each four coordinates long. These are states
# already in the inherited carrier, not auxiliary registers or reader data.
M0 = (1, 0, 0, 0, 0, -1, 0, 0, 0, -1, 1, 0)
M1 = (0, -1, 0, 0, 0, -1, 1, 0, 1, 0, 0, 0)
M2 = (0, -1, 1, 0, 1, 0, 0, 0, 0, -1, 0, 0)
PHASES = (M0, M1, M2)


@lru_cache(maxsize=1)
def _local():
    """Load only the exact public dependency, with its main guard inactive."""
    source_path = (Path(__file__).resolve().parents[1]
                   / "C-FIELD-THREE-CELL-DELAYED-TRANSFER-N" / "break.py")
    source = source_path.read_bytes()
    if sha256(source).hexdigest() != PREDECESSOR_SHA256:
        raise RuntimeError("inherited challenger source hash mismatch")
    module = ModuleType("receiver_record_inherited_challenger_local")
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
    """Return the unchanged neutral preparation for integer H(w)=1."""
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
    """The running carrier is already flat and contains every coordinate."""
    return tuple(state)


def read_cell(cell):
    """Fixed local bit: inspect only the twelve ordered matter coordinates.

    No length, step, old state, resource, field or phase age is an input to
    this membership decision. The complete cell may be supplied for ease
    of addressing; its remaining coordinates do not affect the result.
    """
    return int(tuple(cell[:12]) in PHASES)


def read_target(state, n):
    """Address the designated target, then apply the same local reader."""
    _legal(state, n)
    base = 31*(n-1)
    return read_cell(state[base:base+31])


def accounts(state, n):
    """Return energy, actual charges, defects, spectators and matter sums.

    Components after total energy are flattened in increasing cell order.
    Each local energy includes every matter, spectator and raw-field entry.
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


def _target_cycle(current, n, inverse):
    """Change only a literal target phase; all other full inputs are fixed."""
    base = 31*(n-1)
    matter = tuple(current[base:base+12])
    if matter in PHASES:
        direction = -1 if inverse else 1
        index = (PHASES.index(matter) + direction) % 3
        current[base:base+12] = PHASES[index]


def layers(state, n, cut=None, inverse=False, record=True):
    """Yield (layer name, full state) after each chronological layer.

    Forward: G; K_target; A; B; F. Reverse: F^-1; B; A; K_target^-1; G.
    K is a literal three-cycle, so its inverse is not K. With record=False,
    omit K entirely and recover the inherited four-layer law. A cut omits
    both contacts of one channel while retaining its full stored content.
    """
    _legal(state, n)
    _cut(cut, n)
    local = _local()
    current = list(state)
    order = (("F^-1", "B", "A", "K^-1", "G") if inverse
             else ("G", "K", "A", "B", "F"))
    for kind in order:
        if kind in ("K", "K^-1") and not record:
            continue
        if kind == "G":
            for i in range(n):
                base = 31*i
                current[base:base+31] = local.reaction(current[base:base+31])
        elif kind in ("K", "K^-1"):
            _target_cycle(current, n, inverse=(kind == "K^-1"))
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


def step(state, n, cut=None, inverse=False, record=True):
    """Apply the complete declared law or its exact reverse."""
    current = tuple(state)
    for _, current in layers(current, n, cut=cut, inverse=inverse, record=record):
        pass
    return current
