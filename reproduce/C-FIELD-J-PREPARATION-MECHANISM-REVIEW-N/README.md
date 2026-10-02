# Independent preparation mechanism audit

PUBLIC, NON-CANONICAL; original work, Apache-2.0. This standard-library
exact audit supplements the independent analytic proof in
`notes/C-FIELD-J-PREPARATION-MECHANISM-REVIEW-N/PROOF.md`. Its admitted
source, finite domains, falsifiers and exposure record are fixed in the
adjacent review PREREG.md, against successor specification
`7809098069d4c4ff9f362048cf92c3e8b4714493`.

From repository root, after the coordinator's public source freeze:

```text
python3 reproduce/C-FIELD-J-PREPARATION-MECHANISM-REVIEW-N/verify.py
```

Python 3.10+; no dependencies, input files, predecessor imports, randomness
or floating point. Required execution envelope: 120 seconds, exit zero,
empty stderr. The coordinator captures actual stdout into EXPECTED.txt
and records exact source/environment custody in RUN.md after execution.
The stock `tools/check_reproduce.py` must reproduce identical bytes on the
required x86_64 and aarch64 CI jobs. No execution is represented by this
source-only README.

The finite audit covers local dilations, rational sweep certificates,
finite densities, retained correlated baths, phase/dirty controls,
dyadic nonexactness and a small controlled-translation error interface.
It does not simulate the sufficient L=613 budget or reconstruct Stage C.
Universal contraction and trace-distance conclusions rely on the written
proof. Scope: approximate pointer preparation; occurrence NOT DERIVED.
