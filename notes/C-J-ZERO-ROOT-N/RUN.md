# Execution record

NON-CANONICAL / candidate-C finite audits. No public promotion.

## Prospective pins

- Parent PREREG: 42aa800e6e87cca234491b386ac0fe412f7ebb4d.
- Four-coordinate source: da533d7abbac3822564311b307b7f7d720b14baa.
- Five-coordinate source: 4cf5a28c71ce5ad8f62b00b8f11554c7b328187a.
- Native supplement and source: 8c31f9d7f9d770d0a16a79960c69da2f5abc316c.
- Initial integrated source tree: 281e5ea8b6613bcd4a224d01de17f2c727e0f208.
- Reference supplement and source: d6e08fd106731794283e6f97e2e8abcc31617d35.
- Integrated reference tree: 792ef3259625c3ff74738dcf56388dc8da7ecff7.

All source bytes were fetched from immutable GitHub commits and checked
against the supplied SHA-256 values before execution. The accepted code
was never imported or executed before its public pin. The two arithmetic
helpers wrote independently from the same exposed specification and did
not read each other's program. This is same-session cross-checking.

## First local execution

Date: 2026-11-25.
Platform: Linux. Architecture: x86_64.
Python: CPython 3.12.14. Isolated interpreter option: `-I`.

The exact immutable source blobs were materialized without modification
for this local run. Reproduction commands from the repository root:

```sh
python3 -I notes/C-J-ZERO-ROOT-N/verify.py
python3 -I notes/C-J-ZERO-ROOT-N/break.py
python3 -I notes/C-J-ZERO-ROOT-N/native_verify.py
python3 -I notes/C-J-ZERO-ROOT-N/reference_verify.py
```

Both arithmetic outputs match the one EXPECTED.txt byte for byte.
Native output matches NATIVE-EXPECTED.txt and the prospectively printed
summary. The later reference audit matches REFERENCE-EXPECTED.txt and its
prospectively printed summary. Every process exited zero and wrote zero
stderr bytes.

| Source | SHA-256 | stdout bytes | stdout SHA-256 |
| --- | --- | ---: | --- |
| verify.py | f784dafa77e808b45479e08b9c4d92b1da813f8240163ad5cf84ed13c4a7576e | 451 | 42b8f6c64d9a6a223da7f38b25f9b427ec1800bb698f34287205de40ce117284 |
| break.py | 57c7e55f1f614ff121b1397bdba6cfa638586f2d61cd2c92a8aaab6d37ef03d2 | 451 | 42b8f6c64d9a6a223da7f38b25f9b427ec1800bb698f34287205de40ce117284 |
| native_verify.py | 8b98125d9dcd0043b098aee93d2529649a50e2a3c49e31aadd4e67e02052b308 | 295 | c7bfa8a63c2d184334356a5a9355f06ba7a49ffb48b133898e1d2a5c462d592a |
| reference_verify.py | e5fd1cd53818e51765ffdd93d446a4ec0e5c64400b43ab3d106c85a511dc49c4 | 345 | ea3be6729ec51b52c7447000e5b8f02849873058ec36511cbda83d78930fef1d |

The finite native horizon is 64. Every admitted input is checked at every
cut 0 through 64, including complete states and inverse words. Universal
time and precision claims rely on the written proofs, not extrapolation.
The local lane is x86_64 only. Repository CI checks are recorded separately
and do not imply execution of these note scripts on two architectures.
The reference audit was pinned and read back after the first three audits.
Its own source was not executed before that pin. It reuses the native
generators and target evaluator with an explicit source hash check, and
adds the fixed reference reader and its negative controls. This reuse is
not a second independent audit of the reused code.

No failed run, source repair or moved threshold occurred in these audits.
