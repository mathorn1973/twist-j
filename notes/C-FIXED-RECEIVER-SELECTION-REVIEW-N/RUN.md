# Independent checker run

NON-CANONICAL / L1. This file records the single formal execution under
PREREG.md section 9, and every change made to the checker before its pin.

## Pin and public readback

| Field | Value |
| --- | --- |
| prereg_commit | acf69adba32e838a7891bb8b3c1e4386abaf690f (PREREG.md frozen before review.py existed) |
| pin_commit | fc384a5c9600fbcc60b61ac7d6c22f5c32c57d7e |
| PREREG.md | 22180 bytes, SHA-256 c4663f4ed3c40026125551b5d46b3aa63ab658d62f94ffe5103523e3e3e89455 |
| PREREG-AMENDMENT-1.md | 2386 bytes, SHA-256 310d5b20b8551ad180d1011803981aa7a43749e4d51faaa100ff09ec49361f34 |
| review.py | 64472 bytes, SHA-256 c37dee03041e892bfbe2c4113b5adbc201df8a9677ecba71a050687d87819a4f |
| MATHEMATICAL-REVIEW.md (pre-run) | 26287 bytes, SHA-256 6cccc45a98df2c79ed2d7f506edd25b635c12b27eaec3f70377a405ca0c20d79 |
| target head | 3d8d364cb981bb5d53bbede432fb5a4ac4181709 |

The pin commit was pushed to `origin/claude/affectionate-pasteur-35hovw`.
It was then read back in two independent ways:

- from a fresh clone, fetching the pin commit: all ten files of the review
  directory matched the local bytes;
- from `raw.githubusercontent.com/mathorn1973/twist-j/<pin_commit>/…`:
  review.py, PREREG.md, PREREG-AMENDMENT-1.md, MATHEMATICAL-REVIEW.md and
  SHA256SUMS matched.

Only after this readback did the first execution start.

## The checker before the pin

**Writer.** review.py was written in a fresh agent context. It read the
sources PREREG section 3 allows, and nothing else. The writer reports two
further actions. It listed the review directory with `ls` (file names
only), and on review.py itself it ran `file`, `grep`, `awk` and `sed`, to inspect line
endings and to search for division and float literals. The only Python it
ran was `ast.parse`, and no bytecode was written.

**What review.py adds beyond the literal text.** These are all true
statements implied by PREREG:

- both forms of Q on every evaluation;
- a separate admission predicate, used to check every refused contact;
- accounts on input and output states;
- a domain-size guard on every enumeration;
- trial-division primality of both moduli;
- membership of the 20 maps j^i V^k in the commutant.

**What it leaves to hand review.** The writer listed four statements as
not computable. They are covered in MATHEMATICAL-REVIEW.md:

- the strict increase of 4 sin^2(pi d/25) on d=0..12;
- the minimum neutral account 4 on all of O, of which R1 checks only the
  finite part;
- dimension 20 of the commutant, as a deduction from the rank and nullity
  premises;
- the completeness inequality 4*44/5<36, whose computational support is
  R1's check on the outer shell of [-8,8]^4.

**Static conformance round.** Two readers, each in its own fresh context,
read PREREG.md and review.py and executed nothing beyond `ast.parse`. They
reported no blocker or major finding and six minor ones. The writer
applied all six, so no second round was needed:

1. R4: the name control became a contrast control. The five names leave
   the input state equal to the label-13 preparation and reproduce its
   output. The five actual re-encodings are distinct preparations with
   distinct outputs. The identity half is marked as true by construction.
2. R1: on all 6561 pairs, "the pair moved" is tied both ways to "admitted
   and x != y".
3. R10: a comment marks the monotonicity of 4 sin^2(pi d/25) as a
   hand-review premise.
4. R4: a check that the names equal the re-encoded labels. This was merged
   with item 1.
5. R5: two new checks on the fixtures. The neutral account equals
   2 sum Q(z_k), and every nonzero amplitude has Q >= 2.
6. R6: the attachment rule comes from a single function, attach_pair(n),
   and is checked against the frozen occupied pairs.

No frozen expected value was changed.

**Coordinator inspection.** The coordinator read review.py statically and
checked its constants against PREREG.md with the Python `ast` module; no
part of review.py was run. Every frozen R6 table and both digests equal
PREREG and the target's STOCK-EXPECTED.txt. The coordinator found one
defect. The R7 "For T" checks implemented a false equality from the
frozen text, so they had to fail. PREREG-AMENDMENT-1.md records the
correction, and the coordinator edited the R7 block as stated there,
before the pin. The two code-free reviewers S7 and S8 had found the same
defect. No other change was requested.

## Execution

A wrapper script recorded times, exits and hashes. It invoked exactly the
commands below and nothing else. The common environment was:

```text
env -i PATH=/usr/local/bin:/usr/bin:/bin LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1
```

The run started at 2026-11-07T11:36:55Z and finished at 11:37:05Z, on
Linux x86_64 with Python 3.13.18. Both worktrees were clean before and
after:

- review: the repository at pin_commit;
- target: a detached worktree at 3d8d364.

The run created no `__pycache__` in the review directory or the target
worktree.

| Step | Command (cwd) | Exit | Stdout | Stderr |
| --- | --- | ---: | --- | --- |
| 1 Target binding | `sha256sum -c TARGET-SHA256SUMS` (target directory) | 0 | 19 lines "OK", 429 bytes | 0 bytes |
| 2 Review checker | `timeout 900 prlimit --as=2147483648 python3 -I -B notes/C-FIXED-RECEIVER-SELECTION-REVIEW-N/review.py` (repository root) | 0 | 1699 bytes, 1 line, SHA-256 1160b89bc8560bc9859b881095733d928d08b70f30fdacb870ccd9d9e2d795dd | 0 bytes |
| 3a Target replay | `timeout 300 prlimit --as=1073741824 python3 verify_receiver.py` (target directory) | 0 | 626 bytes, SHA-256 a13b76b5dd5418b1a252914a19c43eac5ce71093fd87cc68230417fa884fabf3, byte-identical to RECEIVER-EXPECTED.txt | 0 bytes |
| 3b Target replay | `timeout 300 prlimit --as=1073741824 python3 verify_stock_census.py` (target directory) | 0 | 1438 bytes, SHA-256 1afa34959c24feb5c8a2d83196e61959c0789a90b893a58b843f42df2955f280, byte-identical to STOCK-EXPECTED.txt | 0 bytes |
| 4a Informal rerun | `python3 -I check_receiver_indep.py` (INFORMAL/) | 0 | 524 bytes, SHA-256 d3cd2454be7ac7df31a97916a66321dfafc6e9cda9f7276b55df71fe2194234f, identical to the transcription in INFORMAL/PROVENANCE.md | 0 bytes |
| 4b Informal rerun | `python3 -I stock_scan.py check_receiver_indep.py` (INFORMAL/) | 0 | 261 bytes, SHA-256 4d6ca41631023636f1f62eb52f9599da70e1c4aaa594e9a1847ef8c24430fd4d, identical to the transcription | 0 bytes |

Every empty stderr has SHA-256
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855.

Engineering wall times were step 2 2.7 s, step 3a 1.0 s, step 3b 3.7 s, step
4a 1.7 s and step 4b 0.3 s. They are not part of any check. The checker's
own estimate of 30 to 120 s was conservative.

EXPECTED.txt is the exact stdout of step 2. This was the first and only
formal execution. There was no failed attempt, no retry, and no change to
the checker or its thresholds after the pin. The target verifier
SHA-256 values match TARGET-SHA256SUMS: verify_receiver.py is 39aa493e…
and verify_stock_census.py is f63c11cd…. This was the coordinator's first
execution of verify_stock_census.py.

The run used one architecture. It is a reproduction, not a
two-architecture gate. A replay of the same pinned bytes on aarch64 would
be welcome. If one is done, it should be recorded separately.
