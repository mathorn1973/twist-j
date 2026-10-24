# Exact first execution record

pin_commit: 751b7f219ccc65f7dba5b04ba248ab0df93bd526
prereg_sha256: da48bc3dcccdb4f383fc7d52f83fa616b4d92cecf433a9cf366de839417ede17
verifier_sha256: 22394150562fdb24b48a2d0c8eea43c4741f4d724b8640d9b394de60f2e3da20
command: python3 probes/P-SOURCE-PHASE-NATIVE-1/verify.py
platform: Ubuntu 24.04.1 LTS
architecture: x86_64
python: CPython 3.12.3
start_utc: 2026-10-24T12:43:04.966924+00:00
exit_code: 0
stdout_sha256: e203ed14efde161bc6c6e97fa440edc8f50891c8efed6beb4f8b0a6d7876dec2
stdout_bytes: 787
stdout_lines: 15
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0

The accepted source was committed and pushed before execution. A fetch
confirmed the public branch head at the pin above. A separate clean Linux
clone checked its HEAD, working-tree cleanliness and all eight source
hashes against the frozen pre-execution manifest. Each checked-out file
also equalled its Git blob byte for byte.

The first execution of the accepted verifier completed with exit 0,
787 stdout bytes and empty stderr. EXPECTED.txt contains exactly the
captured stdout, including its fifteen LF terminators. All eight pinned
files were unchanged and the checkout remained clean after execution.

## Pinned source bytes

| Path | SHA-256 |
|---|---|
| probes/P-SOURCE-PHASE-NATIVE-1/PREREG.md | da48bc3dcccdb4f383fc7d52f83fa616b4d92cecf433a9cf366de839417ede17 |
| probes/P-SOURCE-PHASE-NATIVE-1/verify.py | 22394150562fdb24b48a2d0c8eea43c4741f4d724b8640d9b394de60f2e3da20 |
| notes/canon/C-SOURCE-PHASE-NATIVE-1/CORE.proposed.md | 5b9579ca83e3792b06f96b4aa9b5b5f5ef22be19ab6e4efe3144cc5e7a8e3752 |
| notes/canon/C-SOURCE-PHASE-NATIVE-1/DEPENDENCIES.proposed.tsv | 0c64cda4f4fb6c7be7d0a2c34162b84ac2520658cf0f44f048663d4938c19c4d |
| notes/canon/C-SOURCE-PHASE-NATIVE-1/INTEGRATION.md | 419d3ea5ef6d04dc87cfb2b98ca111be3c09677357507dad4b72bb2f442cc128 |
| notes/canon/C-SOURCE-PHASE-NATIVE-1/NORMATIVE.proposed.tsv | b42e6de81ea13a0e2b870adc53ef0d5056d557b55c1e8dcd9701242a3758615f |
| notes/canon/C-SOURCE-PHASE-NATIVE-1/PROPOSAL.md | c24b564de831b7202038eb7da4601b31a3eabe3de352aded2872f1074b7391a4 |
| notes/canon/C-SOURCE-PHASE-NATIVE-1/REGISTRY.proposed.tsv | 1265c95c3773518f7208f6c69c12635c05c596460b48b6fccdc393caecdfe352 |

## Pre-execution readback abort

An earlier readback wrapper stopped before invoking the verifier because
its copied comparison string for CORE.proposed.md omitted one hexadecimal
character. The immutable pre-pin manifest, local file and fetched Git blob
all agreed on the 64-character SHA-256 recorded in the table above.
The malformed wrapper value was:

    5b9579ca83e3792b06f96b4aa9b5b5fef22be19ab6e4efe3144cc5e7a8e3752

The readback failure was:

    Traceback (most recent call last):
      File "<stdin>", line 15, in <module>
    AssertionError: notes/canon/C-SOURCE-PHASE-NATIVE-1/CORE.proposed.md
    exit 1

Only that external comparison string was corrected. No pinned file,
mathematical assertion, threshold or accepted verifier changed. The
scientific command had not been reached and produced no scientific stdout.
The successful fresh-clone readback then preceded the first verifier run
recorded above.

## Reproducibility and review status

This record describes one x86_64 execution. Required CI jobs must replay
the same pinned verifier on x86_64 and aarch64 and compare the exact stdout.
Their actual status is available on the associated pull request; this
record does not anticipate their outcome.

A formal run and cross-architecture replay do not provide independent
theorem-grade acceptance. The independent proof review remains pending.
