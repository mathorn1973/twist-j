# Three-cell delayed neutral work transfer

NON-CANONICAL L1 candidate C-FIELD-THREE-CELL-DELAYED-TRANSFER-N, issue #1309.
This minimal reproduction audits an explicit 95-integer state: three disjoint
L5 field/matter cells and two neutral stored channels. Four fixed local layers
give a middle storage boundary at step1, target arrival at step2 and paid
target reaction at step3. Full inverse, complete energy and pointwise Gauss
defects are retained. This is a chosen architecture, not native-U derivation,
physical speed or permanent memory.

The frozen preregistration, self-contained proof and two implementations are
in notes/C-FIELD-THREE-CELL-DELAYED-TRANSFER-N/. The primary reuses reviewed
local arithmetic from the earlier candidate; the challenger is independently
authored from the frozen definitions without primary/proof/predecessor code
or output access. Exposed target mathematics is shared, not blind discovery.

The thin bridge checks literal SHA-256 of PREREG.md and both programs, then
executes BOTH sequentially with runpy. Each audits the 6120 preregistered
indexed states, exact certificates and short fixed witnesses/cuts/occupied
contents/order controls. Universal conclusions come from the proof, not
finite sampling. EXPECTED.txt contains prospective bytes frozen before the
first run; RUN.md later records whether execution actually matched them.

From a clean pinned checkout use the existing repository runner:

```text
python3 tools/check_reproduce.py --base b8ba1a07ad776cdd8d878fe0a407e07312c0e263
```

No dependencies beyond Python standard library; exact integer/rational
arithmetic, no network, data import, random search or files written by the
scientific programs. The unchanged runner enforces its whole-bridge120-second
limit, exit0, empty stderr and byte-identical output. Required public jobs
replay the same pinned sources on x86_64 and aarch64. No checker/workflow is
copied, weakened or replaced. Retain the finite-shell recurrence boundary and
all preparation/architecture choices with any future promotion.
