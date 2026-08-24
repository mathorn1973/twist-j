# P-RECORD-QUOTIENT-CALCULUS-1 formal run record

Date: 2026-08-22

Status: local formal record. The public two-architecture gate is completed by
the repository pull-request workflow, which reruns the pinned verifier on
x86_64 and aarch64 and compares stdout byte for byte against EXPECTED.txt.

The flat fields below are the machine-readable record required by
tools/check_verifier.py.

~~~text
pin_commit: 8a1386ad95ef7210a0d4f957f1fd3e0ae76c1a33
verifier_sha256: f877b01a8633f97434645fbb020c408c5732245cc852c38a31e9d4f97f4481d7
command: python3 probes/P-RECORD-QUOTIENT-CALCULUS-1/verify.py
platform: Ubuntu 22.04.5 LTS
architecture: x86_64
python: CPython 3.10.12
exit_code: 0
stdout_sha256: 654fff6a85141b5cd762c0c1bb9944dc36d371c62ef67e0a995e1cd5088f597b
stdout_bytes: 5208
stdout_lines: 60
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
~~~

The platform and architecture are neutral public descriptors. The local
declaration is audit metadata; the required gate rests on the workflow's
byte identity against the one committed EXPECTED.txt.

## Pin audit

~~~text
parent_commit: 9b73d772ce9b8c9479d80e3b10f673b1f5af78f1
prereg_sha256: 97837ac31a7302d08201346fd16b21367e7e2f67462310f6d3827785dd0c78fc
prereg_bytes: 15604
prereg_lines: 433
prereg_blob: 6ab1c81c0aed30db5fd807cf38e2b0f762cd81ef
verify_bytes: 23325
verify_lines: 650
verify_blob: d82a5c4705318927b1bbd091d3651fab1dcded37
public_pin_comment: issue 524 comment 5381537602
pre_pin_static_comment: issue 524 comment 5381528227
~~~

PREREG.md and verify.py were committed together and pushed before any formal
execution. They were then fetched from the public remote into a second clean
checkout at the exact pin. The remote origin, pin and parent matched; the
worktree was clean; the probe directory contained exactly the two pinned
files. SHA-256 values, byte counts, LF-only endings, final LF, ASCII decoding
and Git object identifiers all matched the source bytes.

Before the pin, the accepted verifier was never imported or executed. Static
reading, AST parsing and syntax compilation passed. The static audit found 31
gate calls, zero float literals, one standard-library import, no file or
network operations, and no trailing whitespace. It also found and repaired the
pre-pin kernel, quotient-map and shared-route gaps recorded publicly in issue
524. Neither pinned file changed after publication.

## Formal execution

The accepted verifier was executed exactly once from the repository root of
the clean public readback checkout.

~~~text
start_utc: 2026-08-22T16:56:45.7856302Z
end_utc: 2026-08-22T16:56:47.1026889Z
elapsed_ms: 1315
~~~

The interpreter was started from an emptied environment carrying only:

~~~text
PATH=/usr/bin:/bin
LC_ALL=C
LANG=C
PYTHONDONTWRITEBYTECODE=1
PYTHONHASHSEED=0
TZ=UTC
~~~

The frozen command followed those environment assignments exactly. Standard
output and standard error were redirected separately into memory by the parent
process; no capture file and no repository file was written. EXPECTED.txt is
the complete raw standard output with LF endings and a final LF. Standard error
was empty. The verifier was not rerun, and the pinned checkout remained clean.

## Accepted result

~~~text
checks: 31/31 PASS
decision: RECORD-QUOTIENT-CALCULUS-CONFIRMED
boolean: Idem(R/I) is canonically the power set of Supp(I), and radical
         reduction preserves idempotents
thickness: layer k has order product {N(P):e_P>k}; Loewy length is max e_P
reductions: the unital R-algebra map is the canonical projection exactly for
            I contained in J; every strict quotient has no unital section
no_go: fixed support, radical, reduced record and Boolean algebra do not
       determine filtration depth
audit_carrier: eleven ideals; 64 ordered Hom pairs; I_L for L=1..5
global_scope: L1 only; no selector, apparatus, event, atom choice, decoder,
              measure, coarse-graining, RG, continuum or L2-L6 lift
sampling: not provided
~~~

The universal statements and unboundedness rest on the written proof in
PREREG.md. The finite carrier is an audit, not their quantifier.
