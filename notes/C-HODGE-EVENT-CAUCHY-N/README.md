# Propagating scalar field on windowed Hodge events

PUBLIC NON-CANONICAL. Author: A. M. Thorn <thorn@twistj.com>.
Owner #1239. No Canon authority.

Read RESULT.md for the result and limitations, PROOF.md for the complete
arguments, and PREREG.md for the prospective scope. RUN.md records custody
and reproduction. This is a newly selected field on an embedded subcarrier,
not a change to the previous all-event operator.

Run from the public repository root with Python 3.12 or newer:

    python3 notes/C-HODGE-EVENT-CAUCHY-N/verify.py

`model.py` implements the actual-event coordinates and sparse exact wave
updates. A field is a dictionary from integer spatial triples to Q(sqrt5)
values; every value is represented by two rational coefficients. Import it
with importlib from its path and instantiate Model(). For example:

```python
from importlib.util import spec_from_file_location, module_from_spec
spec = spec_from_file_location('event_model',
    'notes/C-HODGE-EVENT-CAUCHY-N/model.py')
module = module_from_spec(spec)
spec.loader.exec_module(module)
M = module.Model()
f0, f1 = {}, {(0, 0, 0): M.Q(1)}
f2 = M.step(f0, f1)
assert M.energy(f0, f1) == M.energy(f1, f2) == M.Q(1) / 2
assert M.admitted(M.event_label(8, 2, (1, 0, 0)))
```

`step` accepts an optional already-scaled drive delta^2*j. It does not
rescale that argument. Field values are only on the selected image of
(m,z), not every point of the containing event set. A physical SI unit,
photon, native preparation, sampling law and strict microscopic light-cone
support are not implemented or claimed.
