# First execution receipts

NON-CANONICAL / L1. S3-CONSTRUCTIVE-3.
Public prospective pin: 5a925abb110707e333121b9960370dae8e58d236.
All six source files were independently fetched from that public commit
and compared byte-for-byte and by Git blob with a clean local checkout
BEFORE the first scientific import or execution. No frozen file changed.

Environment for all three first runs: Windows 11 build 10.0.26300,
x86_64 (AMD64), Python 3.12.10, assertions enabled.
PYTHONHASHSEED=0, PYTHONDONTWRITEBYTECODE=1, LC_ALL=C, LANG=C, TZ=UTC.
The commands and input relation are exactly those in PREREG.md.
Each program ran once. There was no retry, failed scientific run, discarded
output, modified bound or source repair.

| Program | Start UTC | Measured seconds, approximately | Exit | stderr bytes | stdout bytes | Output |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| verify.py | 2026-11-08 11:41:06.771662 | 0.094 | 0 | 0 | 4165 | EXPECTED.txt |
| audit.py | 2026-11-08 11:41:06.927023 | 0.078 | 0 | 0 | 3707 | AUDIT_EXPECTED.txt |
| assembly.py | 2026-11-08 11:41:07.001268 | 0.766 | 0 | 0 | 2906 | ASSEMBLY_EXPECTED.txt |

No timeout fired. Scientific output files contain the original captured
one-line ASCII JSON with explicit LF bytes, copied without normalization.

Output SHA256:
- EXPECTED.txt: 724329795a84ff5f00a908a72ab31ab9ccf8be486def5e58c43a09fcc64c2203
- AUDIT_EXPECTED.txt: 163342bdcd442a962d2281fd9406cb50dc946ebf0fa7e8d0e526b23446a2e9db
- ASSEMBLY_EXPECTED.txt: fcc72a214caf784942ffdc5a0ed1c05b48c69c8a1558148d6987382c7b9ae74f

Frozen source SHA256:
- verify.py: 356e0c8320fab781b1587f763e759a5356b66630d4a370e152cb92f92ec4345c
- audit.py: b362fb0e6094ca67a02469bb53b8508ea966484352f511eb98c01ca2795d5fc9
- assembly.py: 0d0743ec8ffba6e0a122beb812492cfa43521c5790d3691d2e80e45e94d192a1

All three outputs report PASS. The primary compiler audited 3790 primitive
cuts; the independently implemented cyclic audit checked 4075 cuts,
including its separately structured marker preprocessing.
Both verified all five full compiler endpoints and inverses, 20 marker
cases and 24 writer cases. The independent audit explicitly compared the
primary word, stock, complete states, admission traces and accounts.

The literal assembly executed 14 cases and 19 cycles, with 2597775 contact
cuts and 50 SWAP cuts including complete inverses. All 114 complete-state
boundary checks passed. Per-cut pair invariants reuse exact cached
certificates on identical pairs, as preregistered; cut counts are actual
executed primitives, not counts of distinct arithmetic assertions.
Every completed archive was protected by address immediately after copying.

Only x86_64 ran these scientific programs. Their different output formats
are not expected to be byte-identical to each other. Agreement concerns the
exact certificate states and traces checked by audit.py.
Repository CI on two architectures is not a replay of these notes programs
and is not claimed as a scientific two-architecture gate.
