# First formal run

pin_commit: e6e4feeef50bc86ba79cc1355f2b9ea15642eecd
verifier_sha256: a92ca9a7196a7366fbdfc02be2cc6b46d478968fc4951f3d4da64fb2b2893544
command: python3 probes/P-RELATIONAL-MASS-BOOST-COMPLETION-1/verify.py
platform: Linux, glibc 2.36
architecture: aarch64
python: 3.11.2
exit_code: 0
stdout_bytes: 177
stdout_lines: 8
stdout_sha256: d383ba5ad2c59d0c86bc233db72ea2d22f2c3c71b1152323f76984267bd435d6
stderr_bytes: 0
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
started_utc: 2026-10-20T18:38:54.103556+00:00
finished_utc: 2026-10-20T18:38:55.872378+00:00
elapsed_seconds: 1.769
timeout_seconds: 60

The command above is both the actual first execution and the repository's
canonical replay command. The public pin and branch agreed, and the exact-pin
worktree was clean before and after execution. All six prospective files were
fetched by exact public commit; full text and independently calculated Git
blob identities matched before the first scientific process. The manifest
was checked again immediately before execution.

Public Git blobs at the pin:

| File | Blob |
| --- | --- |
| PREREG.md | 0a26730868cd5db400fd31cbb39e7ed252f87eae |
| PROOF.md | bd5af7ca37f71b0d749479b77d7bcbb13d30a521 |
| SOURCE.md | 7c3ef6f743d0c42e61977a17b4e04ef896c091a4 |
| FIXTURES.md | 2dc94b1b8ccf481da4e144caaf95a455b2421473 |
| verify.py | 95d948c9d2ef427cdd825bfcc65f5c3671c7df29 |
| FROZEN.sha256 | 3805197255d48658b827fb536decc4522c8e4e10 |

Only source reading, analytical derivation, static review, AST parsing and
hashing preceded the public pin/readback. No scientific import or trial run
occurred. The child used LC_ALL=C, LANG=C, TZ=UTC,
PYTHONDONTWRITEBYTECODE=1, PYTHONHASHSEED=0 and the existing executable PATH.
Exact stdout/stderr and metadata were captured outside the tracked tree.
EXPECTED.txt is copied byte for byte from this actual stdout. No edited
retry occurred; all six prospective files remain unchanged. Public required
PR architecture replays are a separate gate and do not replace this record.
