# BREAKER: P-U-COUNTER-AMPLITUDE-CLASS-1

pin_commit: e38ee8049797a9ae60935753eb2c68e5a53f2492
verifier_sha256: da313d414eaa0ffac582539df1cf5290dd938c36c0f595571318df4713cb0b7a
command: python3 probes/P-U-COUNTER-AMPLITUDE-CLASS-1/break.py
exit_code: 0
stdout_sha256: 98f9fea84d6daaccba7edb5574c750a4e9805cea4b5f0e2f9e988daed9e816c9
stdout_bytes: 510
stdout_lines: 9
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
platform: Ubuntu 24.04.3 LTS
architecture: x86_64
python: 3.12.14

prereg_sha256: d69d98c58d417ca3f760394ab639096076863a3be1b3335d515539b570297de3
proof_sha256: e2e2e42dcb66d007d2f7eeb52178cff50eb4000c3a350e0368b54759bec32725

The first execution followed byte-identical public readback of all four
pinned files. The repository-relative command ran with LC_ALL=C, LANG=C,
PYTHONDONTWRITEBYTECODE=1, PYTHONHASHSEED=0 and TZ=UTC.

This record describes the local x86_64 execution. Later public verifier
acceptance is recorded separately in ACCEPTANCE.md, with exact tested
head and job URLs; this local record is not rewritten as a CI run.

BREAKERS=PASS. The breaker was independently written from the proof and
canonical formulas before output comparison, without reading the builder
or incubation code. Known predictions were exposed. No blind discovery
or second-architecture breaker execution is claimed. Exact stdout is
BREAKER-EXPECTED.txt.
