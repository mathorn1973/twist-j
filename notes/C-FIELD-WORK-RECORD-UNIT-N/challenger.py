"""NON-CANONICAL L1: flat challenger for the declared work-record unit.

The carrier has exactly 32*n integer coordinates: n complete 31-coordinate
cells, n-1 stored neutral channels, and one receiver pointer in {0,...,4}.
Each old cell remains matter[12], spectators[12], raw field[6], resource[1].
The pointer is a literal stored coordinate with energy one at every value.

The local scalar arithmetic is reused from the exact public three-cell
challenger. Its authorship and earlier exposure are not fresh independence.
This adapter implements the new pointer coupling on the flat carrier and
does not import the new primary implementation. No unavailable original
ZIP is used or claimed to have been replicated. Only the named, hash-checked
repository dependency is read; its main and network audits are not called.
"""

from functools import lru_cache
from hashlib import sha256
from pathlib import Path
from types import ModuleType


PREDECESSOR_SHA256 = "fc435a7efffea8edd4bd8e11aa12e16c2d1489a39c74997ae0b204837b7445b1"
POINTER_SIZE = 5


@lru_cache(maxsize=1)
def _local():
    """Load exact exposed arithmetic under a name that disables its main."""
    source_path = (Path(__file__).resolve().parents[1]
                   / "C-FIELD-THREE-CELL-DELAYED-TRANSFER-N" / "break.py")
    source = source_path.read_bytes()
    if sha256(source).hexdigest() != PREDECESSOR_SHA256:
        raise RuntimeError("inherited challenger source hash mismatch")
    module = ModuleType("work_record_inherited_challenger_local")
    module.__file__ = str(source_path)
    exec(compile(source, str(source_path), "exec"), module.__dict__)
    return module


def _length(n):
    if type(n) is not int or n < 2:
        raise ValueError("chain length must be an integer at least two")


def _pointer(pointer):
    assert type(pointer) is int and 0 <= pointer < POINTER_SIZE


def _cell(cell):
    assert len(cell) == 31
    assert all(type(value) is int for value in cell)
    assert cell[30] >= 0


def _legal(state, n):
    _length(n)
    assert len(state) == 32*n
    assert all(type(value) is int for value in state)
    assert all(state[31*i+30] >= 0 for i in range(n))
    assert all(value >= 0 for value in state[31*n:-1])
    _pointer(state[-1])


def _cut(cut, n):
    if cut is not None and (type(cut) is not int or not 0 <= cut < n-1):
        raise ValueError("cut must name one channel or be None")


def initial(n, w, offimage=False, pointer=0):
    """Prepare the inherited chain and the specified stored pointer.

    The positive preparation uses PLw with integer H(w)=1. The off-image
    control instead uses P(0,0,1,-2), independently of the supplied seed.
    The receiver, intermediate cells and every resource start unchanged.
    """
    _length(n)
    _pointer(pointer)
    w = tuple(w)
    assert len(w) == 4 and all(type(value) is int for value in w)
    local = _local()
    if offimage:
        raw_source = local.pfield((0, 0, 1, -2))
    else:
        assert local.hform(w) == 1
        raw_source = local.pfield(local.stretch(w))
    source = local.R[:] + [0]*12 + raw_source + [0]
    target = local.R[:] + [0]*19
    state = tuple(source + [0]*(31*(n-2)) + target
                  + [0]*(n-1) + [pointer])
    _legal(state, n)
    return state


def flatten(state):
    """Return all coordinates, including the final stored pointer."""
    return tuple(state)


def read_target(state, n=None):
    """Read only whether the receiver's current pointer is nonzero.

    The optional n validates the carrier; it never selects the read value.
    No time, old state, history, field or matter coordinate affects the bit.
    """
    if n is not None:
        _legal(state, n)
    _pointer(state[-1])
    return int(state[-1] != 0)


def accounts(state, n):
    """Return total energy, charges, defects, spectators and matter sums.

    The pointer contributes one energy unit in every one of its five states,
    and contributes no actual charge. All other accounts retain exactly the
    predecessor's flattened increasing-cell order.
    """
    _legal(state, n)
    local = _local()
    cells = [local.cell_accounts(tuple(state[31*i:31*i+31])) for i in range(n)]
    energy = sum(cell[0] for cell in cells) + sum(state[31*n:-1]) + 1
    return (energy,
            tuple(value for cell in cells for value in cell[1]),
            tuple(value for cell in cells for value in cell[2]),
            tuple(value for cell in cells for value in cell[3]),
            tuple(value for cell in cells for value in cell[4]))


def local_gate(cell, pointer, inverse=False):
    """Apply the target reaction and its event-controlled pointer update.

    Forward: (c,p) -> (G(c), p+event(c) mod 5), where event(c) is exactly
    a funded R-to-AM transition of G. Reverse first recovers c=G(c') and
    subtracts event(c). A forward AM-to-R transition does not decrement p;
    the complete inverse, rather than the forward gate, subtracts events.
    All old cell coordinates have precisely the inherited G image.
    """
    _cell(cell)
    _pointer(pointer)
    local = _local()
    before = list(cell)
    after = local.reaction(before)
    if inverse:
        event = after[:12] == local.R and before[:12] == local.AM
        pointer = (pointer - int(event)) % POINTER_SIZE
    else:
        event = before[:12] == local.R and after[:12] == local.AM
        pointer = (pointer + int(event)) % POINTER_SIZE
    return tuple(after), pointer


def layers(state, n, cut=None, inverse=False):
    """Yield the complete state after every chronological layer.

    Forward order is G; A; B; F. Reverse order is F^-1; B; A; G^-1.
    Only the target G includes the pointer. All other gates and contacts
    ignore it. A cut removes both contacts while retaining the cut channel.
    """
    _legal(state, n)
    _cut(cut, n)
    local = _local()
    current = list(state)
    order = (("F^-1", "B", "A", "G^-1") if inverse
             else ("G", "A", "B", "F"))
    for kind in order:
        if kind in ("G", "G^-1"):
            for i in range(n):
                base = 31*i
                if i == n-1:
                    cell, pointer = local_gate(current[base:base+31], current[-1],
                                               inverse=(kind == "G^-1"))
                    current[base:base+31] = cell
                    current[-1] = pointer
                else:
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
    """Apply the full extension, or reverse every factor in exact order."""
    current = tuple(state)
    for _, current in layers(current, n, cut=cut, inverse=inverse):
        pass
    return current
