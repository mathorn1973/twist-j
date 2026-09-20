# Run record: P-QDD-NATIVE-POINT-PORT-CAPACITY-1

```text
pin_commit: f12f5bdf6dd2c1b2259f535eaf8e5d00d8369c3c
verifier_sha256: fd1bdd42563479c5517c184dfe809d6c49771e7450bc0beac851614fba59534a
command: python3 probes/P-QDD-NATIVE-POINT-PORT-CAPACITY-1/verify.py
platform: Ubuntu 22.04.5 LTS
architecture: x86_64
python: CPython 3.10.12
exit_code: 0
stdout_sha256: e7f5050f75518276a6646cd5ee13e68003ce89d2deb3d57854f56aeb801df598
stdout_bytes: 7314
stdout_lines: 1
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
environment: LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1
```

## Prospective public custody

```text
pin_parent: e57d4506d5b28bf8cb4979c4e29db6b10b2441f2
public_claim_lock: issue 1042
formal_date: 2026-09-19
started_utc: 2026-09-19T16:00:34.538772+00:00
```

The six accepted files were committed and pushed to the named public
branch, then fetched back before the first scientific execution.
HEAD and FETCH_HEAD equaled the stated pin; its sole parent was the exact
public v88 main above. The local checkout was clean. Every local accepted
file matched its fetched Git blob byte for byte and these SHA-256 values.

| Pinned file | Bytes | SHA-256 |
| --- | ---: | --- |
| PREREG.md | 10703 | `03525a9e8d833ef77ccbe414158188ee48d48cb36f006eb806183ea8734423d2` |
| PROOF.md | 11734 | `3797ea92ab515c44694dbca863c20deb66e17f325a1a72493ae8e42a0628f6db` |
| SOURCE.md | 4532 | `709bdf48cce135bf2929d6570357ab0b23d04656a5d6fe138f375f00c7a1b48a` |
| verify.py | 12900 | `fd1bdd42563479c5517c184dfe809d6c49771e7450bc0beac851614fba59534a` |
| BREAKER.py | 7087 | `4f038471633689013c63fa477d28284247011528b3e789dca9b40c107de9e3b0` |
| BREAKER-PREREG.md | 6081 | `14b65260cdcdc3f4fc0d36eccdbb9d1250fda492431e7ef3ac3056e90a81b5fe` |
"
The first scientific execution at this pin was the independent standalone
breaker, described in REVIEW.md and preserved in BREAKER-EXPECTED.txt.
The displayed combined verifier command followed it and invoked the same
independent check again as a required output component. Both ran from the
unchanged pinned checkout. The Linux capture wrapper checked every accepted
file's byte count and hash before and after each command, used the existing
600-second process ceiling, and captured stdout and stderr separately
outside the repository. Both commands exited zero with empty stderr.
Native Git afterward still reported a clean checkout at the same pin.
Only then were the actual byte streams written verbatim to EXPECTED.txt and
BREAKER-EXPECTED.txt. No prior incubation stdout was substituted.

The combined audit checks 78,125 native generator edges, 31,250 selected
edges, 125,000 inherited finite ready-history regressions, and all 625
quadratic inputs with the null kept separate. Its complete target table has
22 values across 624 supported sources. The free optimum is 9/128, all five
faithful cases attain 27/64, and the constructed full permutation has the
separate 124-supported-source null collision. The independent coefficient
convolution, full-cover optimization and five faithful constructions also
pass. These exact checks support the proofs at their declared scope; they
do not promote finite prefixes to all-time evidence or supply physical
occurrence, preparation, records, reset or a layer bridge.

This local x86_64 run alone is not the required two-architecture gate.
The public PR must pass both x86_64 and aarch64 Python 3.12 jobs, each
replaying the exact verifier and independent companion against this one
committed EXPECTED.txt. Proof review is recorded separately in REVIEW.md.
