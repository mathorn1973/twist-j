# RUN - C-OMEGA-HODGE-EVENT-BRIDGE-N

Status: PUBLIC NON-CANONICAL candidate-C corroboration only.
Owner: #1243. No formal public-probe gate is claimed.

## Public custody

Prospective pin: 6ad742a24fa821c16a27a929e38927007a44cf31

The prospective files were publicly read back byte-for-byte before execution.

PREREG.md SHA256 078225f594f2180b0c972a705f3b414eb24c82603c2f25c7d949243dce8c6331
bridge.py SHA256 79c8dde449b5d95c95fe3f28fcbc904abd5c6f89df6c5787a883cf84022b9ab3
verify.py SHA256 bec93421d96f18bdb5bb4ff9923e14dfabf3b4c380009c9e4d16c8e7ed9764ab

Inherited source hashes are frozen in PREREG.md and rechecked by bridge.py.

## Runtime STOP control

The first execution used the host default Python 3.9.6 and exited 1 before
scientific stdout because the inherited verifier uses int.bit_count(), which
that interpreter does not provide. This was environment/runtime STOP, not a
mathematical counterexample. No source, class, threshold or expected result
changed before the successful replay.

Salient error:

    AttributeError: 'int' object has no attribute 'bit_count'

## Successful exact audit

platform: Darwin
architecture: arm64
python: 3.13.13
exit_code: 0
stdout_bytes: 618
stdout_sha256: 8406d69d9fd11d394dfb89bfe3c26eb702d68c7bc804dcf63b556d37803a3f0b
stderr_bytes: 0

Exact stdout:

PASS G1: faithful F5^5 integer lift is bijective onto 25x25x5 = 3125 sites
PASS G2: ell_0 has 3125 fibres of five heads; stable reachable slices have 3125 states
PASS G3: native/event bridge commutation sample checks=4545
PASS G4: actual rounded-event spacelike/timelike witness checks=252
PASS G5: faithful lift is nonadditive; additive torsion-free bridge must be zero by proof
PASS G6: whole-Omega separable quotient has exactly 13 Q classes
PASS G7: bounded-batch cube capacity arithmetic verified through R=50
NON-CANONICAL: exact address bridge exists but target, resolution and spatial assignment remain inputs


Universal results rest on PROOF.md. This finite audit is same-session
corroboration, not independent confirmation and not a two-architecture public
computation gate.
