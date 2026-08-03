# P-ABELIAN-CM-UNIQUE-EVEN-BIT-DISCRIMINANT-MINIMUM-1 result

Status: CORRECTIVE LOCAL FORMAL LEG PASS; TWO-ARCHITECTURE GATE AND OWNER PROOF
ACCEPTANCE PENDING; PUBLIC CLAIM UNREGISTERED

## Recorded decision

```text
initial transcript:   RESULT 7/7 ALL PASS
initial exit code:    not captured; integrity STOP preserved
corrective transcript: RESULT 7/7 ALL PASS
corrective exit/stderr: 0 / empty
byte identity:        initial = corrective = EXPECTED.txt
NEGATIVE:             no exact frozen falsifier observed
current formal leg:   PASS on local x86_64
pending:              GitHub x86_64, GitHub aarch64, owner proof acceptance
final verdict:        LOCAL FORMAL LEG ACCEPTED; THEOREM NOT YET CERTIFIED
```

The authorized first execution reached every frozen PASS line and the exact
frozen SCOPE and RESULT lines, but its wrapper did not preserve a numeric
child-process exit code: the intended status file contains only `n`. That
integrity defect remains recorded and is not reinterpreted.

The explicitly authorized corrective execution used a status-propagating
wrapper validated beforehand with both failure and success controls. It
directly returned exit 0, produced empty stderr, and reproduced the initial
stdout and `EXPECTED.txt` byte for byte. This satisfies the frozen local formal
x86_64 leg. It does not by itself satisfy the required GitHub two-architecture
gate or owner acceptance of the complete written proof.

No theorem certification, Canon edit, registry entry, frontier movement,
physical selection, `TWO-PLACE-PHYSICS` promotion, or L2--L6 claim follows.

## Immutable pin and preserved attempt

```text
public lock:          issue 262
base commit:          61f33e61bdde5adf355fb605f620f1601e154fc2
preregistration pin: d0739111c7c83e558574525598673a1cb128c20b
PREREG.md SHA-256:    96e18d21b61aef4ecb3a93d30c9a833d2337c026376be2675be68692c7e36de3
verify.py SHA-256:    955ea322ff4f59904e6d216d8bcc61e6aae5f8cbe89c9136e33a2853b51c2e34
platform:             Ubuntu 24.04.3 LTS
architecture:         x86_64
Python:               CPython 3.12.3
checkout:             clean before and after; detached at the exact public pin
verifier executions: 2; initial capture defect plus authorized corrective run
accepted execution:  corrective execution 2
exit/stderr:          0 / 0 bytes on the accepted execution
stdout SHA-256:       b1547b0a0291466fa9927be4ec81f125a6449dafb1cc95f2af0a65dd347983b9
stdout bytes/lines:   928 / 9
transcript result:    7/7 ALL PASS
```

## Scope firewall

The preserved transcript concerns only L1 exact arithmetic in the frozen class
of finite abelian Galois CM extensions with exactly one nontrivial quadratic
character and with every quadratic character even on CM conjugation. It does
not establish that this class or discriminant minimization is physically
selected, derive `J`, move `TWO-PLACE-PHYSICS`, or make any L2--L6 claim.
