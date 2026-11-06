# Authority and source custody

NON-CANONICAL. This is an operational authority and source-custody record
for the L1 probe P-NATIVE-P-RECURRENCE-BOUNDARY-1. It establishes no new
scientific status. SPDX-License-Identifier: Apache-2.0.

Audit date: 2026-10-18. Public issue:
https://github.com/mathorn1973/twist-j/issues/1630

## Active public basis

The audit read STATUS.md through the GitHub connector first, followed by
POLICY.md and AGENTS.md. A new isolated checkout was obtained from public
main. A final remote ref readback during source-manifest preparation still
returned the same main commit.

| Field | Verified value |
| --- | --- |
| State | ACTIVE |
| Canon | Public Canon v103 |
| Authority | mathorn1973/twist-j main |
| Main and activation commit | dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d |
| Declared tag | canon-v103 |
| Annotated tag object | e78420dcd80c4e55e3fe39ddd06c004a6810890b |
| Peeled tag target | dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d |
| Content commit | 01fb76f6b3b14a6a5ec05d0017ea922390ab6f66 |
| canon/CANON.md SHA-256 | d87657aeccc568dd668718fb9cbea6136643e5db32dd4e289a4de328e64f824b |
| canon/CANON.md bytes | 1052518 |

Both the content commit and the peeled activation tag are ancestors of
the audited main. The content-to-activation delta consists exactly of
CITATION.cff, README.md and STATUS.md. The authority checkout was clean.

Sources:

- https://github.com/mathorn1973/twist-j/blob/dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d/STATUS.md
- https://api.github.com/repos/mathorn1973/twist-j/git/ref/heads/main
- https://api.github.com/repos/mathorn1973/twist-j/git/tags/e78420dcd80c4e55e3fe39ddd06c004a6810890b

## Repository authority checks actually performed

These commands ran in the clean authority checkout at the main commit
above. They are authority and integrity checks, not executions of this
probe's verify.py or break.py.

```text
sha256sum -c canon/SHA256SUMS
canon/CANON.md: OK
canon/CORE.md: OK
canon/FRONTIER.md: OK
canon/REGISTRY.tsv: OK
canon/CHANGELOG.md: OK

python3 tools/check_activation.py --post-activation --expected-tag canon-v103
POLICY PASS
CANON PASS v103 claims=530
LEDGER PASS claims=530 items=594 dependencies=1105 evidence=530 history=1077 gates=26 programs=7
GENESIS RECON PASS decisions=9 child_gates=19
EXTERNAL SOURCES PASS sources=6 dispositions=9
PREREGISTRATION DRAFTS PASS drafts=6
ACTIVATION PASS mode=active full=False

python3 tools/check_gate_contract.py
GATE CONTRACT PASS gates=26 kinds=DEFINITION_PROJECTION:2,DICTIONARY_LIFT:13,FIRED_NEGATIVE:3,OPEN_DECISION:1,OPEN_LIFT:5,OPEN_SELECTION:2
```

The local activation check did not request full scientific replay. The
already completed full publication runs and the two architecture jobs
were inspected remotely at their actual commit, as recorded below.

## Required remote checks and immutable release

| Event | Run | Verified jobs |
| --- | --- | --- |
| Exact main activation commit | 39022927713 | architecture-x86_64 success; architecture-aarch64 success; check success |
| Immutable tag publication | 39022952253 | publication success |
| Published release | 39033710211 | publication success |

Run sources:

- https://github.com/mathorn1973/twist-j/actions/runs/39022927713
- https://github.com/mathorn1973/twist-j/actions/runs/39022952253
- https://github.com/mathorn1973/twist-j/actions/runs/39033710211

The published release canon-v103 was read back with immutable=true,
draft=false and prerelease=false. Both public release assets were
downloaded, hashed and checked against the exact activation checkout.

| Asset | Bytes | SHA-256 |
| --- | ---: | --- |
| activation-manifest.json | 843270 | 4fd935eea8ca1e5c3ddd6eb2d74103c5a17345df2d57f93634e4a60134d6de68 |
| SHA256SUMS | 415 | 0579c7174198fdea2af8357512c1d746584da9bd58ec3b584c8b8d54884d1fb4 |

tools/check_release_manifest.py accepted the downloaded published manifest
with --expected-tag canon-v103 and reported:

```text
RELEASE MANIFEST PASS content=01fb76f6b3b14a6a5ec05d0017ea922390ab6f66 activation=dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d
```

This validates its complete file inventory. The downloaded SHA256SUMS
was byte-identical to the tagged canon/SHA256SUMS. No locally generated
manifest was substituted for a published asset.

Release source:
https://github.com/mathorn1973/twist-j/releases/tag/canon-v103

## Frozen source inventory

SOURCES.tsv uses exactly these columns:

```text
commit\tpath\tgit_blob\tbytes\tsha256
```

Each row was produced from git show COMMIT:PATH bytes, with its Git blob
obtained from that same commit and path. The blob identifier was also
checked directly against the Git blob header and content. These are
custody calculations only; no source scientific executable was imported
or run while preparing this inventory.

The active public sources and inspected operational checkers are pinned
to dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d. The six consumed source
documents under notes/C-NATIVE-P-CONTACT-REALIZATION-N are pinned to
217cfc13befc3ab4b14444aed49e3fce7f50a7b7 from PR #1629. That note is a
separate NON-CANONICAL source and has no authority over the active Canon.
No foreign source bundle is copied into this probe.

Reference source:
https://github.com/mathorn1973/twist-j/pull/1629

## First execution and subsequent replay

The first scientific execution remains governed by POLICY.md section 3
and AGENTS.md section 6. The accepted verifier, independent executable,
preregistration and custody material must be pinned, pushed and read back
as required by PREREG.md before either executable is executed or imported.
This authority audit performed no such scientific execution.

The inspected tools/check_verifier.py is a replay checker. Its reproduce
entry point requires EXPECTED.txt and RUN.md before executing a verifier;
its command-line interface supplies only --base and has no first-run
recording mode. The first-run command prescribed by AGENTS.md section 6
for this probe is:

```text
python3 probes/P-NATIVE-P-RECURRENCE-BOUNDARY-1/verify.py
```

The runner's deterministic execution environment and limit remain defined
by the pinned repository checker. A first-run record is created only from
an actually completed successful execution, under the repository record
procedure. Once the real EXPECTED.txt and RUN.md exist in the recorded
descendant, the scoped repository replay command is:

```text
python3 tools/check_verifier.py --base dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d
```

No runner, policy, threshold or replay registration is changed. The prior
authority runs do not satisfy the new probe's two-architecture gate and
do not establish either new scientific result or native contact admission.
