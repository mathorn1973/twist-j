# First execution and custody

NON-CANONICAL. One local x86_64 audit, candidate-C only. No independent
agent/human review, no second scientific architecture, no physical gate.

Public pre-run pin: `1b29f4b576df721797c642dd36d093a367bf199b`.
The source files were committed, the branch published, and both public blob
IDs/byte counts read back before execution. Pin receipt: issue #1402,
comment 6026818146. Before that point only syntax compilation ran.

| Input | Bytes | Git blob | SHA-256 |
|---|---:|---|---|
| CONTRACT.md | 7025 | 5d088fa816d72ea0073619d28fd1eb3cb3dc7c7c | 118d02780251b37e57a2b21bd246b1d9b16852269f1ce6571b6eccfe02e49b98 |
| audit.py | 8461 | 3ddc2868725060e5255bd027e0ce234d768691ab | 9c1f83c776968a47e94d988be8f3e1625e4e3cb48688009f383931b64398a2fc |

Command, from the note directory:

```text
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
python3 -I audit.py
```

The supervising subprocess had an enforced 45-second timeout. Its first
execution completed without timeout or retry.

```text
platform:       Debian GNU/Linux 13 (trixie)
architecture:   x86_64
Python:         3.13.5
start UTC:      2026-10-06T22:45:10.154909+00:00
exit:           0
stdout bytes:   922
stderr bytes:   0
stdout SHA-256: 075b64b7d3445c55adcc595ee15f712efa4d34eba66bf0ce987b0829f4758291
stderr SHA-256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

Elapsed 1.307655 seconds is an engineering witness
only. EXPECTED.txt is the exact first stdout, saved after this execution.
The contract and audit were unchanged. No error output is omitted.

Analytical expectations, including the intended integer-step instability,
were disclosed before computation. PROOF.md was written out after the
finite audit; it is not represented as a pre-run independent proof pin.
Its fixed-lattice corollary is a mathematical consequence of the frozen
spectrum, not a later numerical rerun or altered threshold.

The two calculations (real-space incidence ranks and Bloch Newton identities)
are separately implemented routes inside the same coordinator's program,
not two independent agents. The source is read for face orientation, Gaussian
integer arithmetic, time/source signs, zero modes and instability controls;
this same-author check is not a separate review.

The public base is main 7d7f588c42422c2cf37b04d76ebc13ca55eb96dc, Canon v100.
Its successful repository run 37518751601 includes both architecture jobs,
Canon/hash, ledger and gate checks. No new local full-repository replay is
claimed: direct Git DNS was unavailable. Connector readback and comparison
established the base and unchanged normatives; remote heads were explicitly
enumerated through the connector after the failed direct head scan.

The original prose/code use Apache-2.0. No paper, private data, credentials,
external executable or raw private log is redistributed. Only the seven named
note files are intended for publication. Existing workflows are untouched.
Ordinary repository CI validates repository rules; it does NOT execute this
notes audit and cannot promote it to a scientific two-architecture gate.
