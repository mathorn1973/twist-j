# Exact two-use machine with record-only source reading

PUBLIC / NON-CANONICAL / L1. A. M. Thorn. Apache-2.0.
Reservation #1522, parent #1506. Source-derived completion of I2's reader;
not a third independent implementation and not a physical apparatus.

From the repository root:

```sh
python3 probes/P-TWO-USE-TYPED-READOUT-CLOSURE-1/verify.py
```

This command checks all19 frozen stages, actual witness trajectories and the
unchanged1200-record I2/V2 reference digest. No result is declared until the
pinned run is recorded in RESULT. Optional --witnesses and --compare reproduce
only their own declared portions after a successful full run.

Python interface (run only after the preregistration pin):

```python
from fractions import Fraction
# Import apparatus.py from this exact probe directory.
start = apparatus.prepare_ready_state((1,0,0,0), (4,0,0,0), Fraction(4,5))
end = apparatus.run_seven_steps(start)
record = apparatus.extract_direct_port_readout(end, include_d=True)
reading = apparatus.direct_source_reader(record)
```

record contains exactly two actual tape cuts and declared acceptance/context.
reading distinguishes accepted zero, refused input and missing information.
The separate decode_port_vectors helper is numerical Q^4 algebra, not the
record-only entrypoint. The record tag is NOT authentication of data origin.
A physical reading still needs physical acquisition, not just a software type.

Read CONTRACT/PROOF for exact scope; SOURCE_PROOF is the unchanged attributed
V2 proof. MIGRATION and full REUSE.diff show every code change. SOURCES.tsv
binds immutable public inputs. The stopped I2 and V1 records remain preserved.
Its unsupported PROMO geometry partitions and extraneous matrix/symplectic
claims are not copied or accepted here. No Canon, workflow, sibling source,
old threshold or old scientific pin is changed. Native receiver work
#1519/#1520/#1521 has another owner and does not inherit this contact law.
