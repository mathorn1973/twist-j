# Run record: P-J-TWO-TRACE-RESIDUE-DECODER-1

PUBLIC formal L1 probe. This first local run is one architecture; required
GitHub scientific replay is a separate gate. No Canon authority.

```text
pin_commit: 9b0f7cec517eb5cd722af98aa87b21af7ccad6a6
verifier_sha256: 88de9568e8cb8e65ded78ffd6863c46674e88a5b2c9e85489d9c19a0cd5aa469
command: python3 probes/P-J-TWO-TRACE-RESIDUE-DECODER-1/verify.py
platform: Ubuntu 24.04.3 LTS
architecture: x86_64
python: 3.12.14
exit_code: 0
stdout_sha256: d17ff82883dca610813187679221cb315b7636c79f9013062de691b5988d744d
stdout_bytes: 1616
stdout_lines: 14
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
environment: LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1
timeout_seconds: 600
```

The first completed formal execution began at 2026-09-29T06:22:24.215274+00:00.
It exited zero, wrote no stderr and completed within the frozen budget.
EXPECTED.txt is its exact stdout, not a manually reconstructed transcript.

## Input custody

All seven inputs were publicly read back at the pin before execution.
The checkout was clean. verify.py checks the SHA-256 of the other six
inputs before importing either implementation. The repository runner checks
verify.py against its public ancestor pin.

| Input | SHA-256 | Bytes |
| --- | --- | ---: |
| PREREG.md | 2639f6d00d855ce36e73c1f74738275816b45d010577d81db6336434cf31e569 | 9346 |
| PROOF.md | 491f568d1c03c20578af7858cccae40a97f0ff5b83af272e2ec49295a96a3fc0 | 11139 |
| REVIEW.md | 3a7e9ddc2b947f9d30667b7c395140505b50d40412d23f0411776dc065ad37ac | 12187 |
| decoder.py | 45b0b37ec2ef1cd99e92260b7666653dbcbb1ffc99142766b2c267bab97a0ebc | 4155 |
| primary.py | dc97abd593cc78b7116006d012b31096109b000114a34a9e7ab92bce01fa7cdd | 5599 |
| break.py | 57a3c7e03d683bbc5fae074ef5611fd21bce1a5a3922e69eaa8b32b1831ef112 | 13396 |
| verify.py | 88de9568e8cb8e65ded78ffd6863c46674e88a5b2c9e85489d9c19a0cd5aa469 | 4025 |

## Independent-agent and exposure record

The mathematical reviewer had full conversation context, including historical
implementation excerpts. It performed a static proof review and ran no code;
it is not described as implementation-blinded. REVIEW.md preserves the actual
capacity-scope defect and its pre-pin correction.

The breaker author was a separate fresh-context agent. Its only scientific
input was the preregistration, already frozen as public Git blob
ce445357ae8a4efb33f56149e65ceabb7afb4d50. Target counts were disclosed.
The author read neither the primary code, old breaker, proofs nor outputs.
It used cyclic polynomial multiplication, Galois products and an independent
real-coordinate descent inverse with different fixed test exponents.

The resulting break.py was frozen at SHA-256
57a3c7e03d683bbc5fae074ef5611fd21bce1a5a3922e69eaa8b32b1831ef112,
13396 bytes, and published as blob e023ef10856a89775f5d4debe3ac93309dd9f917
before the owner inspected it alongside the primary code. Before the complete
public pin, only AST parsing/compilation and static review occurred. No
scientific test or module import preceded that pin.

Implementation separation is independently authored; the numerical targets
are not blinded. Rerunning this frozen combined verifier is reproduction,
not a third independent implementation.

Public commits use A. M. Thorn's connected GitHub identity; the connector
supplies the account's privacy email, as in the predecessor notes commit.
No author override is exposed by that connector.

## Repository replay

The first local execution follows AGENTS.md section 6. Changed-probe replay
uses the existing repository runner, with the unchanged main basis:

    python3 tools/check_verifier.py --base 789399eebba3ea17a2e59af237bb3280173fbff2

The required pull-request workflow must replay this same pinned verifier and
EXPECTED.txt on Python 3.12 x86_64 and aarch64. Repository checks alone do not
stand in for that scientific execution; this probe is included in the actual
changed-probe runner. No source or threshold may change after the pin.
