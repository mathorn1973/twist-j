# Integration rehearsal and supplemental replay

**NON-CANONICAL / L1 / completed source validation, independent acceptance pending.**
Author: A. M. Thorn <thorn@twistj.com>.
SPDX-License-Identifier: Apache-2.0.

## Immutable input and scope

Source-integration commit: `1dd574c2193f61a350f7c20e542ba1023a5b77c3`.
It contains the four unchanged source bundles, whose 35 exact file identities
are in SOURCES.tsv. Its Canon, STATUS, policy, workflow and tools equal v106
main. Each source program was already publicly pinned before this rehearsal.
No verifier, expected output, threshold, runtime budget or historical replay
context was changed.

Two fresh detached Linux checkouts were clean before execution. Captures were
outside the checkouts. x86_64 used Python 3.12.3; aarch64 used Python
3.11.2. The aarch64 run is supplementary computation evidence, not a
claim to be the required GitHub Python 3.12 job. That workflow is separate.

## Repository and relevant-source checks

On both architectures, the following passed:

- policy, all 211 unit tests, Canon v106, ledger and explicit gate contracts;
- genesis reconciliation, external-source dispositions and preregistration
  drafts;
- generated Canon views against their committed files.

Four directly relevant scientific programs exited 0, wrote empty stderr and
matched their committed EXPECTED files byte for byte on both architectures:

| Program | Verifier SHA-256 | Stdout bytes | Common stdout SHA-256 |
| --- | --- | ---: | --- |
| contact | `0089529bd6f4a9488cbc74197a55912453fc48a1967859bce87c3986cea4951e` | 776 | `89e49565965d9d417cebefd6eb7b36bea864788e8356bbad8901043f1ad66890` |
| gram | `71f0cd9f73cf6a1ae0cded830e575e043d8f70b9b065be806f7617929dd8e3e3` | 681 | `79db6a2aa751b0362b5609e2293d33279510f59f7cbe5a51f5ac9ce0a09f1c12` |
| gram-break | `a4f86eef9e3440c368f82a560bcad2bf762ac953c55d0fbf045a4b56cb987b42` | 1628 | `66a8d32d76aff04e579daecd9f4d7fa30dc65a7ba5df0ceb7d731144afdc8032` |
| minimum | `461b29dc6d3282a00fcccfd0cc194b198f856b688f78841658c93e49ecccac8f` | 1755 | `95ee2135ecb491ab7f0702d603ea94013d00beb28e70668a3c418c0f21478178` |

The names denote the contact verifier, Gram verifier, Gram breaker, and
four-slot minimum probe in the integrated source directories. The command
for each is `python3 -B <its repository-relative script>`. Their deterministic
environment included PYTHONHASHSEED=0, PYTHONDONTWRITEBYTECODE=1,
PYTHONIOENCODING=utf-8 and LC_ALL=C.UTF-8. These four source programs admit that
environment; the separate historical full-sweep issue below is retained.

The PR #1847 mini-verifier also passed on both architectures, with empty stderr,
matching the three exact lines already declared in its frozen README.
It has no committed EXPECTED file; that distinction is not hidden.

- verifier SHA-256: `21eb41e3e8709f534224635acc2dbc58e8fb032d8b9fdaf0177b014b7122746b`;
- stdout: 180 bytes, SHA-256
  `34e8235a680ed52ce2ec3ab90e32b5e8945e1f21d271c52519de59e84d406455`.

This is the different 15-power signed witness, not the 14-power eta-bank word
used in the proposed minimum proof. These are replay counts, not shortest
lengths. All five programs retain their original source pins and evidential
limits. In particular, the Gram/archive pair now has actual aarch64 replay
in addition to its source's x86_64 record, but no mathematical promotion.

## Complete public-probe inventory: initial failure and resolution

The unchanged `python3 -B -u tools/check_verifier.py`, without `--base`,
visited all 309 public probe directories: 281 completed probes and 28 retained
ABANDONED dispositions. The initial aggregate exited 1. It reported 280
successful exact replays and one failure:

`P-PHOTON-Z5-DUAL-WARD-ENGINE-QUALIFICATION-2`.

The execution wrapper set PYTHONIOENCODING=utf-8, which the runner inherited.
This older probe's
frozen launch contract rejects that variable before running its computation.
A direct diagnostic with the same source and ambient variables exited 2,
with zero stdout and the exact stderr:

```text
VERIFY_ERROR python_ambient:PYTHONIOENCODING
```

This is an execution-environment error in this session's wrapper. It is not
a changed scientific result, a reason to edit the probe, or permission to
waive its admission check. The initial aggregate result is preserved:

| Initial aggregate field | Observed value |
| --- | --- |
| Exit | 1 |
| Stdout bytes | 74103 |
| Stdout SHA-256 | `767b4850fafa7cc47ecd2f5da1d92d68ba8a027eab21d98e7fe82ab5c90a94e1` |
| Stderr bytes | 0 |

The ordinary runner's error message reports the child exit code without its
captured stderr; empty outer stderr therefore did not diagnose the child.

Only the failing probe was then replayed through the original runner function,
under its prescribed clean environment:

```sh
env -i PATH=/usr/bin:/bin LC_ALL=C LANG=C TZ=UTC \
  PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 \
  /usr/bin/python3 -c "from tools.check_verifier import reproduce, PROBES; reproduce(PROBES / 'P-PHOTON-Z5-DUAL-WARD-ENGINE-QUALIFICATION-2')"
```

That replay passed the original custody, verifier-hash and exact-stdout checks,
exited 0 and wrote empty stderr. The scientific verifier SHA-256 remains
`d01b594d1e546fbc3480b48e8f59ca361913b1fc39b7e9de8977509b3f5601b4`;
its scientific stdout matches the committed 891 bytes with SHA-256
`bd919866d3ffc40f7022530dcb099a267a904cbd4c9a111f3ff7f082235cbb35`.
The supplemental runner stdout is 260 bytes, SHA-256
`0ef151bc57f9dc80acb692cad52e7f80dcd4a080099d7835878ad6a76bade2ba`.
The worktree remained clean.

Thus every completed probe has a successful unchanged-source replay in the
combined full-sweep and supplemental evidence. **The first aggregate invocation
did not pass, and no second clean aggregate invocation is claimed.** Abandoned
records are dispositions, not scientific executions. The future release-form
gate must still run the complete inventory in its prescribed environment.

## Minimal reproductions

The unchanged `python3 -u tools/check_reproduce.py`, with `--base` omitted,
completed all **37** minimal reproductions on the same x86_64 integration
checkout. The confirmed aggregate exited 0 with empty stderr. Each underlying
scientific program exited 0, wrote empty stderr and matched its committed
EXPECTED file byte for byte.

The confirmed runner stdout is 6131 bytes, SHA-256
`3ec2856bb7256481617273b75c4696d2cdc168bae895c88b9aa3caeded97b4fa`.
The final worktree remained clean. The captured transcript also matches the
earlier completed reproduction transcript byte for byte; the confirmed run
explicitly records the aggregate exit status.

The aggregate ran under PATH=/usr/bin:/bin, LC_ALL=C, LANG=C, TZ=UTC,
PYTHONDONTWRITEBYTECODE=1 and PYTHONHASHSEED=0, with other ambient variables
absent. This includes the existing status-separation audit without altering
any of its 192 predicates.

## Public CI and remaining release gates

The proposal/source head `f8f1f96204d2bb7e78cd4ab8b4a8876c7a53e39d`
passed both required GitHub architecture jobs and aggregate check in
[run 41287194442](https://github.com/mathorn1973/twist-j/actions/runs/41287194442).
That workflow reruns the changed public minimum probe; it does not select
the notes programs. Their actual replays are documented above.

The subsequent changes to this package are validation records and editorial
spacing. They do not change any of the 35 source files. Required checks on
the final PR head remain visible in the PR itself.

This is source-integration evidence, not the future v107 release-form full gate.
Independent mathematical acceptance is pending the author's separate session.
No Canon fold, activation manifest, tag or release is claimed. Final publication
requires the accepted fold, complete release-form replay, reviewed merge, tag
readback and verified draft assets described in RELEASE_PLAN.md.
