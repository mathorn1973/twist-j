# Provenance of the earlier informal check

**NON-CANONICAL / L1. Disclosed provenance only. Not a preregistered test,
not evidence of independent acceptance.**

This folder publishes, unchanged, the two scripts behind the informal check
that was reported to the owner in chat on 2026-11-07, before this review
existed. The target's REVIEW-RESPONSE.md section 4 correctly notes that this
check's source and execution provenance were not available in public. They
are now. That publication does not turn the earlier execution into a
preregistered test. PREREG.md in the parent folder governs the only formal
run.

## What was executed, and when

The coordinator of this review (the same Claude Code session) wrote both
scripts and ran each once. Both runs used x86_64 Linux with Python 3.13.18.
No environment variables were set beyond the session defaults, and neither
run was preceded by any pin, specification or failure rule.

| File | Bytes | SHA-256 | Command (from the folder holding the file) |
| --- | ---: | --- | --- |
| check_receiver_indep.py | 16889 | 97c5f2ae764c00d15dcbdfa05b8afe782f0e0d7e28df7dc46a79a8661cc98478 | `python3 -I check_receiver_indep.py` |
| stock_scan.py | 863 | bc363dd6d1aaf02a0e2961309f7bc58d8158628dc7020ab525ff94333b921fb3 | `python3 -I stock_scan.py check_receiver_indep.py` |

The bytes above are the executed bytes. Neither file was edited after its
run.

The coordinator wrote check_receiver_indep.py from these sources only:

- the definitions in the target's RECEIVER-CONTACT.md, RECEIVER-DYNAMICS.md
  and RECEIVER-OBSTRUCTION.md at 3843abf4e25ff9ba61ed596796dd69c6fc9ed7a0;
- the canonical RELATIVE-CONTACT-INTEGRAL-LAW.

Its writer had already seen the target's published tables in the owner's
message and in RECEIVER-EXPECTED.txt. It had not read the body of the
target's verify_receiver.py, only that file's import lines (a text search
for imports and file or process access). stock_scan.py was written after
the first script had run, to test whether a stock cheaper than Q=32 exists.

## Observed stdout

The stdout was not saved to a file. It is transcribed here from the session
record, line for line.

check_receiver_indep.py, exit 0, empty stderr:

```text
independent receiver check
receiver_table [32, 17, 2, 7, 27]
one_tick [32, 17, 2, 7, 27] thirteen_tick [2, 32, 7, 17, 27]
fixed_state_names [2, 2, 2, 2, 2] reencoded [2, 32, 7, 17, 27]
stock_work [0, 15, 30, 25, 5]
gauge: law m with R == law 0 with j^-m R : True
H_m argmin t [0, 4, 3, 2, 1]
stocks in [-2,2]^4 with injective response: 32/625; min Q among them = 22; examples [(22, (-2, -1, 0, 2), [17, 22, 12, 2, 7]), (22, (-2, 0, 1, 2), [7, 17, 22, 12, 2]), (22, (-2, 0, 2, 1), [7, 2, 12, 22, 17])]
assertions 121374
PASS
```

stock_scan.py, exit 0, empty stderr:

```text
22 40 [((-4, -2, -2, -3), [17, 12, 7, 22, 2]), ((-4, -1, -2, -2), [7, 22, 2, 17, 12])]
28 40 [((-4, -3, -2, -4), [8, 28, 3, 23, 13]), ((-4, -2, -3, -4), [23, 3, 28, 8, 13])]
32 40 [((-4, -2, -1, -4), [27, 2, 32, 7, 17]), ((-4, -1, -2, -4), [7, 32, 2, 27, 17])]
```

## Known weaknesses, found on static re-reading before this review

They are recorded so that the reported count of 121374 is not read as a
measure of coverage.

1. **One weak assertion.** It is the check labelled
   "admission count sanity", the `ok(...)` call immediately after the
   pair loop. It passes whenever any pair is admitted, so it does not test
   the index-16 statement.
2. **Five vacuous assertions.** In the experiment loop,
   `ok(add(...) == ZERO or True, "")` runs once per m and always passes.
3. **Floating point in the spectral section.** It uses complex
   floating-point arithmetic with tolerance 1e-12. The argmin margin check
   (`> 0.1`) is a heuristic, not an exact comparison.
4. **The commutant check is one-sided.** It computes the nullity of the
   commutation system modulo two primes. That gives only an upper bound on
   the rational commutant dimension. The matching lower bound, K[V], is not
   computed.
5. **The count is mostly repetition.** Most of the 121374 assertions repeat
   low-level checks (ring identities, unit covariance) over small boxes.
6. **The completeness bound was not proved.** stock_scan.py enumerates
   [-8,8]^4 filtered by sum of squares <= 64. That bound follows from
   Q(c) >= (sum c_i^2)/2, so the scan is complete for Q <= 32, but the
   script does not state or check the bound itself. It also loads the
   ring code by executing a source prefix of the other file.
7. **No reproducibility controls.** Random fixtures use `random.seed(1930)`.
   No resource limits or environment pins were applied.

## Status under the new review

PREREG.md reruns both files once, byte for byte, after its pin, and
compares their stdout with the transcription above. That rerun is a
prospective rerun with exposed expectations. It is a reproducibility check
of the published bytes, not an independent test of the target. The primary
formal evidence of the review is the separately written review.py.
