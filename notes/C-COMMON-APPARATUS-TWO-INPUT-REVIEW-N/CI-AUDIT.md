# CI audit for PR #1871

Status: NON-CANONICAL / L1. Read-only audit of existing public CI evidence; no scientific rerun, Canon promotion or apparatus-owner decision.

## Identity and access order

- Repository: `mathorn1973/twist-j`.
- PR: [#1871](https://github.com/mathorn1973/twist-j/pull/1871), open when checked.
- PR head: `26731e2bd7f1394b4d274528525e6d78cbe6bbf9`.
- Base: `0c33e2b281e39127c269ef5dd7f5b529a62e9e65`.
- Scientific source pin: `4e448bb3b13c4e8f0338524e7c69ade1c01caf0f`, an ancestor of the head. The eight source files are unchanged; the subsequent commit adds only EXPECTED.txt, RUN.md and RESULT.md.
- [Actions run 41592761170](https://github.com/mathorn1973/twist-j/actions/runs/41592761170), attempt 1, event `pull_request`, completed successfully for that PR head and base.

Author source/output evidence and scientific job logs remained unopened by this audit lane until the parent reported both the public independent-review freeze `8199bb6297178ebeb001820d51b1a3882796ba29` and completion of its own scientific run. Earlier access was limited to metadata, source/provenance records and the general repository runner. This audit did not execute the author verifier or the independent reviewer.

## Actual checkout and runner

Both job logs print checkout commit `b8a9d8f505f338df77b4e2266b2fb075d643a450`, the generated test merge with parents exactly the base and head above. This is not a claim that checkout HEAD equals the PR head. The tested scientific source is bound separately by the verifier hash and source-pin check.

The base is an ancestor of the target PR head. Direct public Git-object comparison gives the identical full repository tree `b5642dce6af67ce8009b25e68b226c956a694d5c` for both the generated test merge and target head `26731e2bd7f1394b4d274528525e6d78cbe6bbf9`. Thus the tested scientific source/context tree is byte-identical to the target head; commit identity differs. Both architecture jobs tested this same tree. The different commit identity is not a gate failure.

At that actual checkout, the relevant unchanged Git blobs are:

| Path | Git blob |
|---|---|
| `.github/workflows/policy.yml` | `bb3a3a188a1453d3a57218f6e64100edddcf4fef` |
| `tools/check_verifier.py` | `c19343cb43c612f3ab79012445976b12dfdb7a74` |
| `tools/probe_replay_contexts.json` | `c9f7a5f9c9eb9c92333aa02516171f2acded7230` |

The workflow supplies distinct `ubuntu-latest` x86_64 and `ubuntu-24.04-arm` aarch64 jobs with Python 3.12 and invokes `python tools/check_verifier.py --base "$BASE_SHA"`. This new probe has no registered historical replay-context substitution.

The inspected runner checks the current verifier against its recorded source pin and requires that pin to be an ancestor. It checks EXPECTED.txt against RUN.md's hash, byte count and line count. Before printing `VERIFY PASS`, it requires actual exit code zero, empty actual stderr and direct byte equality `result.stdout == expected`. Its final two fields are the SHA-256 of the verifier and of actual scientific stdout. See the [pinned runner](https://github.com/mathorn1973/twist-j/blob/b8a9d8f505f338df77b4e2266b2fb075d643a450/tools/check_verifier.py), especially its `reproduce` execution and comparison logic.

## Two architecture evidence

| Architecture | Job | Scientific step | Log evidence |
|---|---|---|---|
| x86_64 | [125773030309](https://github.com/mathorn1973/twist-j/actions/runs/41592761170/job/125773030309) | `Reproduce changed public probes`: success | `VERIFY ARCHITECTURE ... x86_64`; exact `VERIFY PASS` below |
| aarch64 | [125773030002](https://github.com/mathorn1973/twist-j/actions/runs/41592761170/job/125773030002) | `Reproduce changed public probes`: success | `VERIFY ARCHITECTURE ... aarch64`; exact `VERIFY PASS` below |

Both logs contain this identical scientific-pass line:

```text
VERIFY PASS P-RELATIVE-CONTACT-INDEPENDENT-RELOAD-1 fbee888930ac613c517c2ec0b4312c5b7b9860d1e1f21be21e9d12ba03cf0884 40a71401c28406605aea666a40fec5f773505d3a5b56b82897cdc09ad4c1952c
```

The x86_64 line is timestamped `2026-11-03T06:54:48.3009795Z`; the aarch64 line is timestamped `2026-11-03T06:54:43.5248475Z`. No runner environment or unrelated job-log material is reproduced here.

Independent static hashing of the public Git objects at the PR head confirms:

| File | Bytes | SHA-256 |
|---|---:|---|
| `verify.py` | 23140 | `fbee888930ac613c517c2ec0b4312c5b7b9860d1e1f21be21e9d12ba03cf0884` |
| `EXPECTED.txt` | 2807 | `40a71401c28406605aea666a40fec5f773505d3a5b56b82897cdc09ad4c1952c` |

The verifier bytes are identical at the scientific pin and PR head. Consequently the two logged passes establish replay of that same pinned verifier, exit zero, empty stderr and scientific stdout byte-identical to the same 2807-byte EXPECTED.txt on both architectures. This is more specific than two green repository jobs; it is the named probe's scientific replay gate.

The aggregate [check job 125773399920](https://github.com/mathorn1973/twist-j/actions/runs/41592761170/job/125773399920) also completed successfully. The publication job was skipped, as expected for this pull-request event.

## Unit-test scope and limits

Each architecture log separately confirms the command `python -m unittest discover -s tools -p 'test_*.py'`, followed by `Ran 218 tests` and `OK`. These are repository-tool unit tests. They are distinct from the scientific probe's admitted input cases and are not 218 independent apparatus implementations or independent mathematical reviews.

The audit confirms the existing two-architecture scientific reproduction at the frozen finite scope. It does not independently discover the construction, establish a stronger input or reuse horizon, compile the five declared slot swaps into native contacts, supply external post-start loading or indefinite renewal, identify physical time/energy, or promote a Canon claim. The separate independent mathematical and runtime review retains its own provenance and conclusions.

