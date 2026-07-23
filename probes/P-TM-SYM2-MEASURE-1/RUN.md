# P-TM-SYM2-MEASURE-1 formal run record

pin_commit: 69ff42438154bc165a74d03e914988efda9bccf9
base_commit: 390c1d254b0c3939ff7fc9e6b900eac8bd1b877a
prereg_sha256: c504d7962786436eb68376875f9239c6bc086b57617ced86f4de95a74c7f57d7
prereg_bytes: 13985
prereg_git_blob: 5b692ffe5fe5f4e4ea38489a798267b148c98daa
verifier_sha256: 30b581a2b84e0ac8b3b333e5731f7ecdcfa9bfb975585da0603f02ab3e8ed6eb
verifier_bytes: 137120
verifier_git_blob: 7f55053971b93bbd16bf433f07014156bff62eee
checker_sha256: f0499d1cd42ae199edff048277841bcea3074e28c9b73c8c12895b731d35100c
checker_bytes: 69159
checker_git_blob: 06e5c5bc8851d10a905740ae88f3e2a53b3e2c20
normative_snapshot_sha256: 78bd84df4be6ba777c2d721d722b335b29b5f13644aae891814d51c6e080ad54
normative_snapshot_bytes: 22453
normative_snapshot_git_blob: 6518651db3e62df2b4a3378ffaf314d8dd409b0f
dependencies_snapshot_sha256: eb3b993015fa4e1a97a5fe9b78fa39e91391c5ffaf88f6a357458c03c6c137d1
dependencies_snapshot_bytes: 39547
dependencies_snapshot_git_blob: 86529ac216c7c970c530fc5b3d25da84916c42a5
command: python3 probes/P-TM-SYM2-MEASURE-1/verify.py
environment: LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
platform: Ubuntu 24.04.4 LTS
architecture: aarch64
python: 3.12.3
run_started_utc: 2026-07-23T08:51:03Z
run_finished_utc: 2026-07-23T08:51:05Z
pre_run_clean: yes
post_run_clean: yes
deterministic_executions: 1
exit_code: 0
stdout_sha256: 395209f15d0943f38b1d8af4f6d20769c5e113c65bac9455944613ab3b40726f
stdout_bytes: 9879
stdout_lines: 79
stdout_cr_bytes: 0
stdout_final_byte: 0a
stdout_git_blob: b2b3250550dd78af0479db114499392c86812b13
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
route_count: 1
route: ROUTE: NEGATIVE (N2: the canonicality test returns NONCANONICAL)
checker_integrity: PASS
scientific_route: NEGATIVE / N2
result: NEGATIVE / N2 / NONCANONICAL
architecture_gate: formal aarch64 leg complete; required GitHub x86_64 leg pending
public_lock: issue 130
public_pin_comment: 5056315987
public_run_return: issue comment 5056393829
public_metadata_erratum: 5056438053

The formal run used a fresh fetch and a clean detached checkout of the exact
public pin. The immutable inputs matched their public SHA-256, byte, Git blob,
parent, and two-file inventory records before process start. The wrapper
called the embedded checker exactly once in-process with `--evaluate`.
The captured raw streams are retained outside the working tree; only neutral
platform and architecture descriptors are recorded here.

`EXPECTED.txt` is the exact 9879-byte LF-only stdout. It contains all 79
lines, has no CR bytes, ends in LF, and has SHA-256
`395209f15d0943f38b1d8af4f6d20769c5e113c65bac9455944613ab3b40726f`.
Stderr is the exact empty byte string.

The complete metadata and raw stdout were returned publicly on issue #130
before these records were created. Comment `5056438053` transparently
corrects a transcription error in the environment line of comment
`5056393829`: the exact variable is `PYTHONDONTWRITEBYTECODE=1`. No command,
transcript byte, hash, route, result, or execution count changed, and no rerun
was performed.

The required GitHub Linux x86_64 pull-request check must use the identical
pinned verifier, exit zero with empty stderr, and reproduce `EXPECTED.txt`
byte for byte. Until that check passes, the two-architecture computation gate
is pending.
