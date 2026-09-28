# Native-prefix generator of selected Hodge geometry

PUBLIC NON-CANONICAL. Author: A. M. Thorn <thorn@twistj.com>.
Owner #1247. No Canon authority.

Start with RESULT.md and PROOF.md. PREREG.md freezes the class before the
scientific runs; RUN.md records the unchanged pin and actual reproductions.
The previous N candidate was stopped at static review before execution and
is preserved separately; use this N2 candidate, not its abandoned code.

Run from the public repository root with Python 3.12 or newer:

    python3 notes/C-OMEGA-GENERATIVE-GEOMETRY-N2/verify.py

## Minimal executable example

```python
import importlib.util
import sys

path = 'notes/C-OMEGA-GENERATIVE-GEOMETRY-N2/generate.py'
spec = importlib.util.spec_from_file_location('geometry_generator', path)
g = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = g
spec.loader.exec_module(g)

# One completed native transition emits one immutable spatial record.
space = g.Generator((0, 0, 0, 0, 0, 0), h=3, mode='space')
small = space.run_to(g.spatial_size(1))   # exactly 27 vertices
large = space.run_to(g.spatial_size(2))   # exactly 125 vertices
assert large[:len(small)] == small

# Separate mode: actual spacetime events and exact scalar values.
# Default initial data: f0=0, f1 is a unit impulse at the origin; no source.
field = g.Generator((0, 0, 0, 0, 0, 0), h=3, mode='field')
records = field.run_to(g.spacetime_size(2))  # exactly 153 events
assert all(r.value is not None for r in records)
```

To consume an externally supplied LEGAL native prefix instead, call
`g.decode_prefix([x0, x1, ..., xN], h=3, mode='space')`. Invalid transitions
raise ValueError. The values xj are six-tuples of residues 0,...,4. The helper
`Generator.advance()` calculates the next unchanged native transition itself;
`advance(next_checkpoint)` verifies a supplied one before appending.

Coordinates and scalar values are immutable tuples of rational coefficient
pairs (a,b), denoting a+b*sqrt5. `squared_spatial_distance` computes the fixed
positive spatial-projection metric using the stored exact coordinates.
`prior_links` refers only to earlier records. Spatial edges are undirected
and counted once at their later endpoint. Field links name all predecessors.

Custom `initial(m,z)` for m=0,1 and `source(m,z)` are separately selected total
deterministic exact functions. Source values are j itself; this generator
applies the required h^-2 factor. A caller must not mutate the writer's public
working dictionaries or initial/source definitions during an archive.

Generation order is not event time, and fixed append count is not a fixed
CPU/bit budget. The implementation does not derive its metric or window from
native U, implement physical archive memory, fix microscopic cone support,
or supply a vector photon or curved geometry.
