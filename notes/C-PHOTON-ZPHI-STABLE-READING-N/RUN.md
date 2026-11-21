# First execution and engineering receipt

NON-CANONICAL. One local exact audit, candidate-C only. Reservation #1404.
The full PROOF.md was frozen before this run; it has not been independently
reviewed. No second scientific architecture or native physical validation.

## Immutable inputs

Base main: 7d7f588c42422c2cf37b04d76ebc13ca55eb96dc, Public Canon v100.
Pre-execution pin: 21d8955f16f1ddf2c3db116a997dd7a242746dba.
Pinned tree: 3f0a75f095faffab7a2ad654a9cb737fa16a161f.
Public pre-run receipt: issue #1404, comment 6038124478.

| File | Bytes | Git blob | SHA-256 |
|---|---:|---|---|
| CONTRACT.md | 6693 | b822486a2f2f0117de84a55d6eb6869bf1fe455d | 307ad25cb0fed7e1c1bd134d4fe4beb27c345b7897d9e762630d4d12c5dbffc3 |
| PROOF.md | 15184 | 989c28c5c3c07a0810c50c15011869c482fbcb01 | 144cde086af42b008d55258944efdb9c8535ed527f2cd995954b51df6f91e560 |
| audit.py | 12669 | 25de956e6258082a7af062c0d163eb8f0d0ead7c | a14cbb64d4d7a7c3f47d6e2dfe8ff79331914a8bc73d4134517d4d193aab294a |

The public directory was read back by exact commit, and its blobs/byte counts
matched locally recomputed object IDs before execution. Only syntax/security
and byte checks preceded the pin. Preparatory uncommitted object versions
are not used by this run; no scientific execution occurred on them.

## Command and enforced budget

Working directory: the candidate note directory.

    LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
    python3 -I audit.py

The launching subprocess imposed timeout=45 seconds. A once-only receipt
was created before launch and rejects accidental repetition. The complete
stdout and stderr were captured. No scientific code was imported/executed
by static checking or by result packaging.

## First result

    platform: Debian GNU/Linux 13 (trixie)
    architecture: x86_64
    Python: CPython 3.13.5
    started UTC: 2026-10-07T12:41:52.193601+00:00
    ended UTC:   2026-10-07T12:41:53.602078+00:00
    elapsed: approximately 1.408 seconds (engineering timing only)
    enforced timeout: 45 seconds
    exit: 0
    stdout: 2605 bytes
    stderr: 0 bytes
    stdout SHA-256: 434ffc464975ca88f9315429539b544bda381f441dcf3619afde7e11cfdc08f9
    empty stderr SHA-256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855

EXPECTED.txt is exactly this first stdout. No corrective run, assertion
change, altered threshold or repeated scientific execution occurred.
The positive and negative controls retained their frozen meanings.

## Engineering scope

Only seven named files in notes/C-PHOTON-ZPHI-STABLE-READING-N/ are proposed.
The three pinned input files are unchanged. The predecessor #1403 and all
canonical/probe/workflow files remain untouched. Source main's existing
successful repository run 37518751601 is not new-branch CI or a fresh local
repository replay. Public PR CI and its eventual result will be recorded
separately, without altering this first-execution receipt.

The program uses standard-library integer/Fraction arithmetic, reads no
external file/network and writes stdout. Its source was inspected for
unexpected execution, secrets and external dependencies. Both computational
routes belong to this coordinator, not independent reviewers. Original new
prose/code are Apache-2.0. The author explicitly permits the connected
GitHub noreply commit identity temporarily. No personal infrastructure or
third-party archive is included.
