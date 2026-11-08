# Local auxiliary Noether completion

Status: PASS in the first formal local audit.
Scope: NON-CANONICAL, NEW_DECLARED L1, conditional candidate-T, a=0 and E_hom=0.
Ownership: https://github.com/mathorn1973/twist-j/issues/1663

The existing constrained auxiliaries tau and p admit a temporally local
second-order completion on the unchanged carrier. The action has
multiplier-pair radius at most one. Its raw transformations satisfy the
off-shell Ward identity; a local skew Euler-gradient correction also makes
the generators commute off shell through order two. The predecessor's
field-only obstruction remains valid in its original class.

This is a coefficient identity and formal consistency result. It supplies
neither an all-order or finite-epsilon symmetry nor new gravitational bulk
dynamics, physical preparation, a metric selection, or native-U realization.

## Replay

From the repository root, with Python 3.12 and its standard library:

```sh
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
python3 probes/P-INTEGER-LOCAL-AUXILIARY-NOETHER-1/verify.py
```

The primary launches the standalone breaker automatically. A successful
replay exits zero, writes no stderr, and produces stdout byte-identical to
EXPECTED.txt. Both programs verify the five frozen normative Canon files.

Prospective pin: `45648ac0d495a55a6c76e90dfd0fe56e042bf224`. The six-file
public readback receipt preceded the first execution. PREREG.md fixes the
contract; PROOF.md supplies the universal derivation; SOURCE.md records
authority and choices; RUN.md and RESULT.md record the completed local
audit; REVIEW.md records its review and limits.

The audit covers 12 rational states, 237 parameter/commutator cases, 900
distant multiplier pairs and eight detected defects. At this first-run
record, required x86_64/aarch64 pull-request replay is pending. The local
result alone does not satisfy that two-architecture gate or promote Canon.
