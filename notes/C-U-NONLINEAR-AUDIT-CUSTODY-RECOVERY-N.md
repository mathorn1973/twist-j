# Nonlinear AUDIT-1: recovered historical negative result

PUBLIC / NON-CANONICAL / L1 record correction. A. M. Thorn; Apache-2.0.
Date: 2026-10-16. Owner issue: [#1534](https://github.com/mathorn1973/twist-j/issues/1534).

## Disposition

**RECOVERED SCIENTIFIC_FAIL.** The original capture of the second AUDIT-1
invocation has been recovered. Python 3.13.13 returned zero with empty stderr
and the handled negative verdict printed below. The historical
`Status: ABANDONED` declaration remains preserved, but its explanation that
no completed result existed does not describe this second invocation.

This is an additive, source-exposed custody correction. It records a completed
negative verdict under the frozen failure contract, not a passing audit or
completion of every audit stage. The identifier remains consumed. This note
creates no new run, `EXPECTED.txt`, `RUN.md`, scientific promotion, or Canon
change. Its acceptance resolves the missing-original-capture obligation;
acceptance of the successor remains qualified as stated below.

## Immutable public sources

- AUDIT-1 [input pin `8edb5ea97bf38337d9c65f08964a0ae9e2ed7743`](https://github.com/mathorn1973/twist-j/tree/8edb5ea97bf38337d9c65f08964a0ae9e2ed7743/probes/P-U-NONLINEAR-RECEIVER-INDEPENDENT-AUDIT-1), parent `b79143fb00839b870686f6cea34e174959060df1`.
- Its preserved [ABANDONED declaration at `d9a20f7bba60ae868aa467b5b076960ac5e88b7d`](https://github.com/mathorn1973/twist-j/blob/d9a20f7bba60ae868aa467b5b076960ac5e88b7d/probes/P-U-NONLINEAR-RECEIVER-INDEPENDENT-AUDIT-1/RESULT.md).
- Successor [PR #1537](https://github.com/mathorn1973/twist-j/pull/1537), source head `d36c23e0789e74c8d052de3d2061bd1717acbb74`, input pin `731d825d966d9b6df5678c4c059ea1e3d068c67a`.
- Mathematical and custody [correction #1540](https://github.com/mathorn1973/twist-j/pull/1540), source head `6577ef457f6413e848309936c20d4577babbbf7c`, input pin `50512dd2345acff01a219c29c394abfdd7bcaa58`; its [CUSTODY.md](https://github.com/mathorn1973/twist-j/blob/6577ef457f6413e848309936c20d4577babbbf7c/probes/P-U-NONLINEAR-AUDIT-ERRATA-1/CUSTODY.md) stated the recovery obligation resolved here.

No original source blob or historical result is replaced by this note.
The recovered capture and its source-exposed review were publicly recorded
in [the recovery receipt](https://github.com/mathorn1973/twist-j/issues/1534#issuecomment-6217789271).

## The two invocations

Times below are the original tool-result start/completion metadata, in UTC.
The verifier return code is distinct from the enclosing capture command's
return code, which was zero in both cases.

| Recorded interval, 2026-10-15 UTC | Runtime / architecture | Verifier return code | stdout | stderr |
|---|---|---:|---|---|
| 19:49:23–19:49:28 | Python 3.9.6 / arm64 | 1 | 270 bytes, 4 lines | 975 bytes |
| 19:49:58–19:50:03 | Python 3.13.13 / arm64 | 0 | 782 bytes, 10 lines | 0 bytes |

The first stdout SHA-256 is
`07d3eef0195df6dba59a3d8d6b1faffdd999c560a6aaca74c0c8c89b13f26722`;
its stderr SHA-256 is
`192a9e59f22dfa7c7ffa754adc586b503172f190eafdf9bd2339351b56952d6b`.
The original capture did not print that stderr body. The later `bit_count`
explanation is therefore not presented as a recovered traceback. Python 3.9.6
also falls outside the pinned Python >=3.10 contract.

The second command invoked the pinned `verify.py` through the same Python
3.13 executable as its capture wrapper, with `capture_output=True`, timeout
600 seconds, `LC_ALL=C`, `LANG=C`, `TZ=UTC`, `PYTHONHASHSEED=0`, and
`PYTHONDONTWRITEBYTECODE=1`. The recorded runtime is Python 3.13.13 / arm64.
The original stored output artifact is 1110 bytes, SHA-256
`14764c1ac052d8d772de5f9a8940c2b4d658e15a16db8bc3f5dfac085c96c5fc`.

The scientific stdout payload was extracted from that historical capture,
removing the tool wrapper and normalizing terminal CRLF rendering to LF. Its
782 bytes, ten lines and final LF reproduce the SHA-256 printed by the
original capture: `4562bbc333d7572d37aa0b17d16eaa57ce864b1b062eb7b8b4d5cdca952cc0dc`.
No output line was supplied by a new execution. The observed zero-byte stderr
has SHA-256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.
Only the scientific payload and neutral metadata are published here; private
session logs, paths and conversation text are excluded.

```text
PROBE P-U-NONLINEAR-RECEIVER-INDEPENDENT-AUDIT-1
STAGE custody PASS files=6 sources=10
STAGE generators_and_quotient PASS gen=78125 inv=78125 aff=78125 quot=78125 sel=31250
STAGE nonlinear_chart_claim1 PASS aff_rt=31250 phi_rt=31250 poly=15625 fibres=25x625 a0_z14=1250
STAGE prefix_claim2 PASS pairs=25 selectors=(2,2,4) traces=(2,0,2,1) x2_eq_x0=25
STAGE synchronized_invariants_claim3 PASS states=5000 edges=10000 fibres=25x200
STAGE prepared_tail_and_regression_claim4 PASS tail_sets=25x20 union=500 edges=1000 checkpoints=25625 updates=25600
STAGE access_boundary_and_quotient_claim5 FAIL expected_tail_zqr size 20 != 10
STAGE nonaffinity_and_minimality_claims6_7 NOT_RUN
VERDICT SCIENTIFIC_FAIL stage=access_boundary_and_quotient_claim5 reason=expected_tail_zqr size 20 != 10
```

## Input identity and later record handling

The contemporaneous pin readback compared local bytes with public Git-object
bytes. The seven recorded identities were checked again against the immutable
pin during recovery:

| File | Bytes | SHA-256 |
|---|---:|---|
| `INPUTS.sha256` | 456 | `ba3b5ccdabaf79ca3b506e45d581c05f52569f91e01a7890f1b356120d005b26` |
| `PREREG.md` | 11460 | `99240e984cdbe3645d9796ddb059cc4f572473a912896534cebd1037bed89329` |
| `PROOF.md` | 21563 | `70da74df1771d39ad004e32580dbe225b160e64b44f7024c8fae39850b65bc4d` |
| `README.md` | 1757 | `f897c2e9a8dbd3f085449bc5e09b1a82ed1068eac0c322a81450e634047ae811` |
| `SOURCES.tsv` | 1349 | `5b4fe3faa7f50692ff143d3e31ab0347ff80eda3c98e3342742ed4639e9fbe84` |
| `break.py` | 37059 | `162a97d52de4f8ac909fa8f0605babfe6a0a64122676fd8292dfe5cd47b30d6b` |
| `verify.py` | 649 | `6e9da6dc57af0e83ef579635c698c1979e09a0a92b64ef47334ace86e778b985` |

The recorded command chain contains no source or manifest edit between that
readback and either invocation. The custody stage hashes six files against
`INPUTS.sha256`; its `sources=10` counts and syntax-checks source rows, not an
independent runtime comparison of ten external Git objects. There is no
separate immediate pre-run Git-status snapshot. Input identity rests on the
exact readback, recorded command chain and six-file custody check, with that
limit retained.

The second capture command writes `EXPECTED.txt` when the verifier returns
zero with empty stderr; those conditions are met in the recorded output.
A later recorded command removes `EXPECTED.txt` before the ABANDONED commit.
There is no separate intermediate file readback, so the removal command's
success alone is not treated as proof of prior file existence. No AUDIT-1
`RUN.md` creation or removal is recorded in the recovered session.

## Scope after recovery

The pinned failure contract catches this failed size predicate and returns
`SCIENTIFIC_FAIL` with process code zero. Thus the second invocation is a
completed negative verdict; it is not the earlier nonzero Python 3.9.6 event.
The exact failure concerns the audit's false ten-element expectation for a
twenty-element set. It does not refute the primary coordinate-readout
existence proof. The final nonaffinity/minimality stage did not run.

This recovery removes the missing-capture premise of the historical
`HOLD_PENDING_ORIGINAL_CAPTURE` disposition in correction #1540. It does not
retroactively create a Linux or two-architecture reproduction, make the
original audit blind or error-free, or erase its historical ABANDONED record.
No historical verifier was executed during this recovery.

AUDIT-2 in #1537 must be read together with #1540's E1–E3 replacements: the
whole twenty-point tail maps two-to-one onto a ten-point output phase,
bijection holds only with the stated known input phase, distinct prepared
messages require the repaired common-generator-word argument, and the
particular global polynomial reader has degree nine. Its old blanket
zero-discrepancy statement is not adopted. This note changes historical
custody disposition only; #1540's mathematical qualifications remain binding.

## Current record precedence and qualified successor acceptance

This note supplies the current classification of the recorded second AUDIT-1
invocation: **completed SCIENTIFIC_FAIL**, with the exact failed and NOT_RUN
stages above. The original ABANDONED text remains a preserved historical
declaration, not the accepted current classification of that invocation.
It is not imported into the current probe inventory as an abandoned gate.

| Preserved historical text | Current reading |
|---|---|
| AUDIT-1 `RESULT.md` at `d9a20f7bba60ae868aa467b5b076960ac5e88b7d` | Superseded as a completed-run classification by this recovered negative receipt. Both the original pin and the declaration remain available at their original Git identities. |
| AUDIT-2 `PREREG.md`, `PROOF.md`, `README.md` and `RESULT.md` references to the abandoned predecessor | Retained as the predecessor description used at the time; they do not override the recovered AUDIT-1 result. |
| AUDIT-2 `PROOF.md` sections 5.1(3), 6.1(3), 7.1(2), the degree-five label in `RESULT.md`, and its blanket zero-discrepancy conclusion | Read with #1540's E1–E3 corrections. The complete tail is not a bijection under a fixed selected update, the selected global map is not established as bijective, and the displayed reader's degree is nine. |
| ERRATA-1 `CUSTODY.md` and `RESULT.md` missing-capture/HOLD statements | Their evidence limitation was true when written; this recovered record resolves it. Their mathematical corrections and historical statements about what that correction itself executed remain unchanged. |

AUDIT-2 is accepted as the preserved completed eight-stage finite computation
at its exact tested scope, together with the corrected written L1 conclusions
under the preceding rule. The original code, expected output, preregistration,
proof and run record remain byte-identical. Its `sources=12` line is not an
external source-byte audit; those twelve source objects were checked
separately during corrective review. Its forward-closure and trajectory
checks are not proofs of the superseded bijectivity or degree-five sentences.
This qualified acceptance does not claim the original proof was error-free,
create a new independent run, promote the evidence to Canon, or admit a
physical receiver.

Once this additive note and the preserved AUDIT-2 packet are reviewed,
integrated and read back with their required checks, #1534 can be closed as
a completed audit delivery with a corrected negative predecessor record.
The historical failure and unexecuted AUDIT-1 stage remain visible; neither
is relabelled as PASS.
