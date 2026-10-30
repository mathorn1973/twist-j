# Actual scientific executions

Candidate: C-W-P0-SCATTERING-N. Issue: #1840. Date: 2026-10-30.
Status: NON-CANONICAL / L1 / exact finite audit, no formal P-probe.

## Prospective public custody

Accepted pin: f6fb4b580244012bc3139c19eef58553ff52b31e.
Base: a193e389fb1ddb0bdc89165b015c95a17eb1e425, Public Canon v106.
The pin and every input in FROZEN.sha256 were pushed and fetched back
before execution. The GitHub connector separately read the frozen
manifest at that pin before the first run. No scientific source was
imported or executed before that public readback. Static AST/hash and
repository-policy checks only preceded the pin.

Both commits use A. M. Thorn <thorn@twistj.com> as author and committer.
The analytical formulas were exposed before the pin; no blind-prediction
claim. The user packet numbers were already known, but no packet script
was used or rerun in this audit.

## Runs

Command from this directory: python3 -I verify.py.
Process limit: 120 seconds per run, unchanged.
Environment: LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0
PYTHONDONTWRITEBYTECODE=1; standard-library exact arithmetic only.

| Architecture | Operating system | Python | Exit | stderr |
|---|---|---|---:|---:|
| x86_64 | Debian GNU/Linux13 (trixie) | 3.13.5 | 0 | 0 bytes |
| aarch64 | Debian GNU/Linux12 (bookworm) | 3.11.2 | 0 | 0 bytes |

Each architecture ran the unchanged source once. Both outputs have
1272 bytes and SHA-256
4bae49d56916a26714df0aeb3ce17d7a86c08fe1512d5efcd9b478c7e181eb57.
EXPECTED.txt contains actual aarch64 stdout. It is compared with the
original x86_64 bytes after public result readback. No failed scientific
run, source amendment, threshold move or range change occurred.

Inventory:64 exact spectral/contact cases;2560 direct original four-channel
stationary equations; inverse-free transparent point;12 compact-projector
basis controls;8 rational reflection intervals of width1/10^9; prime-
normalization controls. The universal statements are proved in PROOF.md.

## Evidence boundary

Two architecture runs reproduce the same program. This is not independent
mathematical authorship, blind-agent confirmation, a formal public probe
or Public Canon T promotion. The direct original-operator path is a
same-session cross-check, not a second independently authored program.
Notes-only repository CI does not run verify.py and is not counted as a
scientific replay. Independent review remains outstanding.

The run uses one selected eigenphase band at a time and exact stationary
waves. It does not certify the user's finite-width/time packet setup.
Physical occurrence, sampling and detector semantics are not inferred.
