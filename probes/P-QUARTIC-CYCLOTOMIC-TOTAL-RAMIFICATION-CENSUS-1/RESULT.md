# P-QUARTIC-CYCLOTOMIC-TOTAL-RAMIFICATION-CENSUS-1 result

Status: FORMAL AARCH64 LEG PASS; INDEPENDENT BLIND BREAKER NO BREAK FOUND;
REQUIRED GITHUB TWO-ARCHITECTURE GATE PENDING; PUBLIC CLAIM UNREGISTERED

## Recorded decision

```text
formal verifier: RESULT 9/9 ALL PASS
blind breaker:   NO BREAK FOUND 10/10
exit/stderr:     0 / empty
NEGATIVE:        no frozen falsifier fired
final verdict:   pending the required GitHub x86_64 and aarch64 replays
```

The frozen proof and its exact finite audit have survived the authorized first
formal leg. This file does not yet assign `THEOREM-CERTIFIED`: under the frozen
threshold that verdict becomes available only after both required GitHub
architectures reproduce the single `EXPECTED.txt` byte for byte and the
reviewed proof/scope disposition is accepted. No Canon, registry, frontier,
dependency, dictionary, release, or authority change is made here.

## Immutable pin and formal leg

```text
public lock:          issue 256
base commit:          f8c4cc64ba4fc21723fc3e715b5a40036ef7b404
preregistration pin: 7291c079811a2a0191ab536590f7a5d723a9a7c7
PREREG.md SHA-256:    f8ac045f4f35a87a04a4f8578b1bb1a8b69c75f8434d981fc6d77e71ffea9e72
verify.py SHA-256:    60fd58dc3eeab0e40bf0b2ab04e05690b4a1cc088cade4ce500007ce930c1539

run started:          2026-08-03T09:19:55Z
run finished:         2026-08-03T09:19:55Z
platform:             Ubuntu 24.04.4 LTS
architecture:         aarch64
Python:               CPython 3.12.3
checkout:             clean before and after; detached at the exact public pin
deterministic runs:   1
exit/stderr:          0 / 0 bytes
stdout SHA-256:       88413e040ab1c10d88dc64611a0f7e7d259c3ac6301b3f213707107c06d9822a
stdout bytes/lines:   1031 / 11
result:               9/9 ALL PASS
```

`EXPECTED.txt` is the exact ASCII, LF-only transcript of this formal leg and
has a final LF. The pin files remained byte-identical and the remote worktree
remained clean.

## Independent blind breaker

The fresh blind breaker was frozen publicly before this formal execution:

```text
commit:               3d550f27a326aa1a49c34ac111f6723806562c50
break.py SHA-256:     316f014dfe579136e20d84907ad0e9b6362ec3e101174deee9c68e3d35bf4875
break.py bytes:       16858
break.py Git blob:    4b5a5075d0e43396585153aa1683bae395288f93
breaker exit/stderr:  0 / empty
breaker stdout hash:  f6fec277be2d7984c1b541cc86cdb67eadfee307dd9879a72aef2bdf528384ef
breaker stdout bytes: 1393
breaker result:       NO BREAK FOUND 10/10
```

The breaker record states that it used only the frozen `PREREG.md`, Public
Canon v32, and declared dependencies and did not read the builder verifier or
any expected output. The builder formal checkout did not fetch or open
`break.py`. A later implementation comparison is optional and has not been
performed; it is not a frozen decision gate.

## Proof and audit verdict

The complete written proof establishes `phi(n)=4` exactly for
`n in {5,8,10,12}`, identifies `Q(zeta_10)=Q(zeta_5)`, and separates the
three fields `K_5`, `K_8`, and `K_12` by their discriminants. The integral
basis and Dedekind steps turn the four exact modular factorizations into the
profiles

```text
(K_5,5):  (e,f,g)=(4,1,1)
(K_8,2):  (e,f,g)=(4,1,1)
(K_12,2): (e,f,g)=(2,2,1)
(K_12,3): (e,f,g)=(2,2,1).
```

Discriminant support excludes every other ramified rational prime. Thus the
candidate total-ramification locus is exactly
`{(K_5,5),(K_8,2)}`. The audited residue-unit outputs are `C_4` and `C_1` at
the total primes, with the `K_12` controls `C_3` and `C_8`; the inherited
reduction `J mod (1-zeta_5)=2` passes and generates `F_5^x`. All nine frozen
audit gates pass, and no exact NEGATIVE witness was found by the independent
ten-gate attack.

## Scope firewall

The result remains confined to L1 exact arithmetic in the frozen class of
full quartic cyclotomic fields. It does not select degree four, prove that
cyclotomic fields exhaust another admissible class, classify ramification in
all number fields, or identify either residue as a decoder, Born measure,
physical bit, clock, force, observable, or physical place. It does not make
`TWO-PLACE-PHYSICS` unique or theorem-status and makes no lift to L2-L6.

The required GitHub x86_64 and aarch64 jobs, reviewed probe pull request, and
any later Canon fold remain separate pending steps.
