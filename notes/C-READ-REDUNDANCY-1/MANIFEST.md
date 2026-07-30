# MANIFEST: C-READ-REDUNDANCY-1 bundle

```text
bundle        C-READ-REDUNDANCY-1, incubation lane, 2026-07-29
authority     none. Candidate labels only. Nothing here closes, moves or
              anchors a public row.
basis         Public Canon v27, mathorn1973/twist-j main, STATE ACTIVE,
              tag canon-v27, CONTENT_COMMIT
              116b62edf505914d96fcd65318d97f3675c53f85, CANON_SHA256
              c7c4c7e6d5a3116e356b060eaf696963285b0f2f465d5f2e1dcda5c094a309f6,
              150959 bytes, canon/SHA256SUMS 5 of 5 OK, verified by clone
question      route precondition 5 of
              notes/canon/ADOPT-COIN-MINIMAL-READ-2026-07-29.md section 5:
              does absence of feedback alone bound admissible read
              redundancy?
answer        NO alone (exhibition), YES under anonymity plus totality
              (prime-support theorem). Flipping clause located.
platform      one, Linux x86_64. The second architecture leg belongs to the
              later public probe.
```

## Files, in reading order

```text
PLAN-DECODER-SECTOR-POST-V27_2026-07-29.md
  the sector plan this candidate is workstream A of. Read for context and
  for the sequencing of workstreams B, C, D.
PREREG-C-READ-REDUNDANCY-1.md
  the frozen preregistration, six fields, frozen before any execution.
  sha256 334cb3bf9ef6feaccaa7e48c809e0f2f880c6686c025eee96474fb31c743d0d2
verify_read_redundancy_1.py
  the verifier. 13 checks. stdlib only, int and Fraction, no float.
verify_read_redundancy_1.stdout.txt
  its pinned stdout. exit 0, 13/13 PASS.
break_read_redundancy_1.py
  the breaker. Independent code path, semantic evaluation, brute force.
break_read_redundancy_1.stdout.txt
  its pinned stdout. exit 0, NO FALSIFIER FIRED.
C-READ-REDUNDANCY-1_RESULT_2026-07-29.md
  the result with candidate labels, the break round and the residuals.
PROMO-C-READ-REDUNDANCY-1.md
  the promotion proposal a public fold can consume alone.
SHA256SUMS.txt
  hashes of every file above, including this manifest's siblings.
```

## Reproduction

```sh
env LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
    python3 verify_read_redundancy_1.py
env LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
    python3 break_read_redundancy_1.py
sha256sum -c SHA256SUMS.txt
```

Expected: verifier exit 0 with stdout sha256
`05d567dc19a3705e7de6fcae4a91cc85964c1b2207d7c2da4fead959d901f3ef`;
breaker exit 0 with stdout sha256
`4e4aa7b5b1f7ac0fac1f8df754ec68774d4ac55176103cbd655e35dd54b3f2da`.
The stdout hashes cover the two files as shipped; a rerun that differs in
any byte is a finding and must be preserved, not repaired.

## Falsifier for this bundle

Wrong if any hash in SHA256SUMS.txt differs from its file, if either
script exits nonzero on a clean rerun under the declared environment, if
the declared basis differs from mathorn1973/twist-j main at tag
canon-v27, or if any file listed above is absent.
