# First pinned Linux run

NON-CANONICAL / L1 / completed exact orbit audit.

pin_commit: 4c3a5aae1237c66e40798b18eb8bfb09dfc0e77a
verifier_sha256: 4275266074bdcbfe0b107a5217c1a021efec4ac3ca4a35503086e16949d14a25
command: python3 probes/P-POLE-HEIGHT-ODD-ORBIT-1/verify.py
platform: Ubuntu 22.04.5 LTS, Linux WSL2
architecture: x86_64
python: 3.10.12
exit_code: 0
stdout_sha256: dca5a40b9b68712f9ebe80ed35b54ac6a70a6dfb1ffafecdb3558a9fa058099c
stdout_bytes: 2941
stdout_lines: 11
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0

All six immutable source files were publicly read back byte for byte and
by Git blob before execution. A clean Linux clone fetched the exact pin,
verified every source hash and remained clean after this run. This was
the verifier's first scientific execution; no failed attempt or retry
occurred. Supplied review outcomes were exposed before authoring, as
recorded in PROVENANCE.md. No source or threshold changed after pinning.

Assertions were enabled. LC_ALL=C, LANG=C, PYTHONDONTWRITEBYTECODE=1,
PYTHONHASHSEED=0 and TZ=UTC were set. Inherited PYTHONOPTIMIZE,
PYTHONIOENCODING, PYTHONUNBUFFERED and TWISTJ_EVIDENCE_DIR were removed.
The fixed process limit was 600 seconds. Actual measured wall duration was
approximately 0.351 seconds, operational metadata rather than physical time.
Neither traversal reached the 100000-state limit.

## Pinned source custody

| File | Bytes | SHA-256 |
| --- | ---: | --- |
| PREREG.md | 6484 | `e829e58ee76149a06d037a32f638da46657a2df6fdc607881fb3f0ac46faccbe` |
| PROOF.md | 6984 | `25f9bd27a455c20ca8e8ec32cf573680b094300e348f1f171fedaa9f7232de1b` |
| PROVENANCE.md | 2215 | `42538ba2324d1bb9b3c9c9557df5ae7ac33daee9767b0c85f8a01c88035279c2` |
| README.md | 1657 | `25a6809807c39ab7e4935ec35b38fdd9954f4786a08b0026b432d0db0685fe1d` |
| SOURCES.tsv | 2392 | `34751ce036774999722131213c4315b40fded8df24440d53a5afe12f0f67ada7` |
| verify.py | 16596 | `4275266074bdcbfe0b107a5217c1a021efec4ac3ca4a35503086e16949d14a25` |

This records the author Linux x86_64 run. Required GitHub x86_64 and
aarch64 outcomes are reported only after the relevant jobs complete.
The two arithmetic routes and static review belong to the same authoring
session and do not constitute independent-session acceptance.
