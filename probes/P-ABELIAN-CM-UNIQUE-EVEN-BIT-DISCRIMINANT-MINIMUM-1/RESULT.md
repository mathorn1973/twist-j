# P-ABELIAN-CM-UNIQUE-EVEN-BIT-DISCRIMINANT-MINIMUM-1 result

Status: FORMAL PROBE RESULT; TWO-ARCHITECTURE COMPUTATION GATE PASS;
THEOREM-CERTIFIED AT THE FROZEN L1 PROBE SCOPE; PUBLIC CLAIM UNREGISTERED

## Recorded decision

```text
initial transcript:    RESULT 7/7 ALL PASS
initial exit code:     not captured; integrity incident preserved
corrective local leg:  RESULT 7/7 ALL PASS; exit 0; empty stderr
GitHub x86_64:         VERIFY PASS
GitHub aarch64:        VERIFY PASS
aggregate check:       TWO-ARCHITECTURE CHECK PASS
owner proof acceptance: complete at the exact frozen L1 scope
NEGATIVE:              no exact frozen falsifier fired
current STOP:          none
final verdict:         THEOREM-CERTIFIED at the frozen L1 probe scope
```

The authorized first execution reached every frozen PASS line and the exact
frozen SCOPE and RESULT lines, but its wrapper did not preserve a numeric
child-process exit code: the intended status file contains only `n`. That
integrity defect remains recorded and is not reinterpreted.

The explicitly authorized corrective execution used a status-propagating
wrapper validated beforehand with both failure and success controls. It
directly returned exit 0, produced empty stderr, and reproduced the initial
stdout and `EXPECTED.txt` byte for byte. The first capture incident is not
reinterpreted; the separate corrective execution supplies the accepted local
formal leg.

Both required GitHub architectures then reproduced the frozen verifier and
stdout hashes, and their aggregate gate passed. The owner explicitly accepted
the complete written proof and every named classical theorem input at exactly
the preregistered L1 scope on 2026-08-03. The frozen `THEOREM-CERTIFIED`
threshold is therefore satisfied for this probe result.

No Canon edit, registry entry, frontier movement, physical selection,
`TWO-PLACE-PHYSICS` promotion, or L2--L6 claim follows. Public `[T]`
registration remains a separate Canon fold.

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

## GitHub two-architecture close gate

```text
pull request:          263
formal evidence head: 7ec01dd32bd02c2a16a3a92df6a98130c16f9ab6
workflow run:          30838735427

x86_64 job:            91770280503, SUCCESS
x86_64 runner image:   GitHub-hosted ubuntu-24.04, 20260720.247.2
x86_64 Python:         CPython 3.12.13

aarch64 job:           91770280525, SUCCESS
aarch64 runner image:  GitHub-hosted ubuntu-24.04-arm, 20260719.67.1
aarch64 Python:        CPython 3.12.13

aggregate job:         91770337315, SUCCESS
aggregate result:      TWO-ARCHITECTURE CHECK PASS
verifier SHA-256:      955ea322ff4f59904e6d216d8bcc61e6aae5f8cbe89c9136e33a2853b51c2e34
stdout SHA-256:        b1547b0a0291466fa9927be4ec81f125a6449dafb1cc95f2af0a65dd347983b9
stdout bytes/lines:    928 / 9
byte identity:         PASS on x86_64 and aarch64
```

Each architecture job checked the PR tree derived from the named formal
evidence head, preserved the frozen verifier hash, exited zero with empty
stderr, and reproduced the committed `EXPECTED.txt` byte for byte. Policy, all
99 tool unit tests, Public Canon v33, and the public ledger passed in both
jobs. The aggregate required context also passed.

## Proof and audit verdict

The complete written proof closes the registered chain. The even-bit condition
places CM conjugation in `G_K^2` and supplies an order-four root, so four
divides the field degree. The exact totally imaginary Minkowski bound excludes
every possible smaller or tied competitor of degree at least eight. Degree
four and the unique nontrivial quadratic character then force cyclic Galois
group `C_4`.

Kronecker--Weber and the abelian character-field correspondence produce an odd
primitive quartic character `psi` with even quadratic square `epsilon`. The
conductor-discriminant theorem gives the field identity

```text
absDisc(K) = f(psi)^2 f(epsilon).
```

The primitive conductor bounds give `f(psi)>=5` and `f(epsilon)>=5`; the pure
2-primary branch has the stronger floor `(16,8)` and discriminant at least
`2048`. Hence `absDisc(K)>=125`. Equality forces both conductors to be five,
where a quartic character is faithful and cuts out the full field
`Q(zeta_5)`. The positive control has field discriminant `125`, so it is the
unique minimizer in the frozen class.

## Scope firewall

The preserved transcript concerns only L1 exact arithmetic in the frozen class
of finite abelian Galois CM extensions with exactly one nontrivial quadratic
character and with every quadratic character even on CM conjugation. It does
not establish that this class or discriminant minimization is physically
selected, derive `J`, move `TWO-PLACE-PHYSICS`, or make any L2--L6 claim.
