"""Nested complete-state implementation of the known C5 event-record law.

Reuses hash-pinned public #1310 local arithmetic; never invokes its main.
No source from the unavailable user ZIP is claimed or substituted for it.
"""

from functools import lru_cache
from hashlib import sha256
from pathlib import Path
from types import ModuleType


@lru_cache(maxsize=1)
def local():
    path = Path(__file__).resolve().parents[1] / "C-FIELD-THREE-CELL-DELAYED-TRANSFER-N" / "verify.py"
    data = path.read_bytes()
    if sha256(data).hexdigest() != "42ec10cd001028ec126045647eea89347ec12bbf3612c40e1aa204ab77913a59":
        raise RuntimeError("inherited primary hash mismatch")
    module = ModuleType("work_record_local_primary")
    module.__file__ = str(path)
    exec(compile(data, str(path), "exec"), module.__dict__)
    return module


def local_gate(cell, pointer, inverse=False):
    assert type(pointer) is int and 0 <= pointer < 5
    p = local()
    changed = p.gate(cell)
    before, after = (changed, cell) if inverse else (cell, changed)
    event = int(before[0] == p.R and after[0] == p.AM)
    return changed, (pointer + (-event if inverse else event)) % 5


def initial(n, w, offimage=False, pointer=0):
    assert type(n) is int and n >= 2 and 0 <= pointer < 5
    p = local()
    assert p.active_energy(tuple(w)) == 1
    source = (0, 0, 1, -2) if offimage else p.mv(p.L, w)
    cells = [(p.ZM, p.ZM, p.Z6, 0) for _ in range(n)]
    cells[0] = (p.R, p.ZM, p.join(source), 0)
    cells[-1] = (p.R, p.ZM, p.Z6, 0)
    return tuple(cells), (0,)*(n-1), pointer


def flatten(state, n):
    cells, channels, pointer = state
    assert len(cells) == n and len(channels) == n-1
    return tuple(v for m, b, z, r in cells
                 for v in tuple(x for row in m+b for x in row)+z+(r,)) + channels + (pointer,)


def read_cell(pointer):
    assert type(pointer) is int and 0 <= pointer < 5
    return int(pointer != 0)


def read_target(state, n=None):
    return read_cell(state[2])


def accounts(state, n):
    p = local()
    cells, channels, pointer = state
    read_cell(pointer)
    return (sum(p.cell_energy(c) for c in cells)+sum(channels)+1,
            tuple(v for c in cells for v in p.rho(c)),
            tuple(v for c in cells for v in p.defect(c)),
            tuple(v for c in cells for row in c[1] for v in row),
            tuple(v for c in cells for v in p.vector_sum(c[0])))


def layers(state, n, cut=None, inverse=False):
    assert cut is None or 0 <= cut < n-1
    p = local()
    for kind in ("FBAG" if inverse else "GABF"):
        old_cells, old_channels, pointer = state
        cells, channels = list(old_cells), list(old_channels)
        if kind == "G":
            for i in range(n-1):
                cells[i] = p.gate(old_cells[i])
            cells[-1], pointer = local_gate(old_cells[-1], pointer, inverse)
        elif kind == "F":
            cells = [p.free(cell, inverse) for cell in old_cells]
        else:
            for j in range(n-1):
                if j != cut:
                    i = j if kind == "A" else j+1
                    cells[i] = p.with_resource(old_cells[i], old_channels[j])
                    channels[j] = old_cells[i][3]
        state = tuple(cells), tuple(channels), pointer
        yield kind, state


def step(state, n, cut=None, inverse=False):
    for _, state in layers(state, n, cut, inverse):
        pass
    return state
