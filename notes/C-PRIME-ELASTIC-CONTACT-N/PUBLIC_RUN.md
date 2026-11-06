# Public execution and import custody

Author: A. M. Thorn. Date: 2026-10-30. Issue: #1838.
Status: NON-CANONICAL / L1. No formal public P-probe or promotion.

## Prospective chart pin

    4c51644d9ef0b26a984909b23f856735ecb1d927

This commit was publicly pushed and fetched back before chart_verify.py
was executed. The connector also read back CHART_FROZEN.sha256 at that
commit before execution. Every scientific input hash was checked again
immediately before each run. CHART.md, CHART_PREREG.md and chart_verify.py
have not changed since the pin. The hypotheses were analytically exposed
before the pin; the audit is not a blind prediction.

The original nine-file contact packet was already executed locally before
this public submission. Its files and SHA256SUMS are preserved unchanged.
Running verify.py now is faithful reproduction, not its first execution.
A Git reference import carried the exact bytes into a fresh main-based
branch. The reference root commit is not a competing scientific authority.
The public pin has the prescribed author and committer identity:
A. M. Thorn <thorn@twistj.com>.

## Actual execution environments

Both programs ran once in this publication session on each architecture:

| Architecture | Operating system | Python |
|---|---|---|
| aarch64 | Debian GNU/Linux 12 (bookworm) | 3.11.2 |
| x86_64 | Debian GNU/Linux 13 (trixie) | 3.13.5 |

Commands, executed from this note directory with a 120-second process limit:

    python3 -I chart_verify.py
    python3 -I verify.py

Environment: LC_ALL=C, LANG=C, TZ=UTC, PYTHONHASHSEED=0,
PYTHONDONTWRITEBYTECODE=1. Standard library only, exact integers and
Fraction arithmetic. No scientific input or threshold changed after pin.

All four processes exited 0 and produced empty stderr.

| Program | stdout bytes | stdout SHA-256, equal on both architectures |
|---|---:|---|
| chart_verify.py | 529 | 014f873b70b3b6e9468be29836adfe89985de29e0063ab040e632eba96e4b711 |
| verify.py | 731 | 6170ec64df9d8b7f77050f4c4953402a1e3ed1573c85e757b0a6a949ddd4b40d |

The original contact EXPECTED.txt was compared byte-for-byte on both
architectures, not merely by its displayed hash. The newly committed
CHART_EXPECTED.txt is the actual aarch64 stdout and matches the x86_64
stdout hash and byte count. Its complete visible stdout also agrees.

The unchanged old script prints 'single x86_64 lane' as part of its
historical original scope sentence. This record explicitly supplements
that historical run with the actual aarch64 reproduction; the script and
its expected bytes are not edited to manufacture a new history.

## Meaning of PASS and negative disposition

PASS means that the stated exact identities, finite controls and reported
obstructions were reproduced. It does NOT mean that the proposed full
Dirac chart exists. The scientific decision printed by the chart audit is
FULL_DIRECT_CHART=REJECTED and O_PLUS_MASS2_BRIDGE=REST_ONLY.
The universal classification is the written proof in CHART.md; its finite
rung and coefficient tests are supplementary checks.

Two architectures reproduce the same programs. They are not independent
authors, external peer review or a public Canon T promotion. Repository
CI does not run notes scientific programs and is not counted as another
scientific replay. Independent mathematical review remains outstanding.

The old FROZEN.sha256 and SHA256SUMS and the new CHART_FROZEN.sha256 remain
unchanged. PUBLIC_SHA256SUMS covers the completed publication except itself.
