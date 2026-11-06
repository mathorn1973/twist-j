# Review of the first pinned exact-audit result

**NON-CANONICAL; 2026-10-04. Disposition: accept the recorded first-run
result at its stated conditional ideal-model scope.** This is a review
of existing evidence, not another scientific execution or a theorem-grade
status promotion. Canon v97 and the physical HOLD remain unchanged.

The reviewer read EXPECTED.txt, RUN.md and RESULT.md against the
preregistered program, support proof and previously reviewed verifier
sources. Neither verifier was executed or imported during this review.
Only this new review record was written; no frozen source was changed.

## Custody and execution record

The immutable candidate is
`308eaf9be2358d2ad2bbcae5d44698de6b0cd680`. RUN.md records public
ten-file byte readback before scientific execution. The reviewer checked
that Git reports no difference from that pin in any of the ten frozen
files. Separately, all eight support files match their manifest byte
counts and SHA-256 values. The manifest and primary hashes are:

```text
INPUTS.json: 3163b277d88b641328f74783b10e820504f17cf65a01c3a8c4948fc145b3b8e8
verify.py:   a8d1f95ad89995ebc287b3fbf6b0839100b00f0888786206661658ac4e4d3b95
```

The embedded primary manifest hash matches the actual manifest. The
reviewer independently measured EXPECTED.txt as 906 bytes and eleven
lines, with SHA-256
`a53dc82cdf385144b47eb556c92e7a791339243a05f91226ae2918cfc3e2c9db`,
matching RUN.md and RESULT.md. Its final line reports audit PASS.

The execution record states Linux x86_64, CPython 3.10.12, exit zero,
empty stderr and completion within the frozen timeouts. The primary
records independent JSON stdout SHA-256
`2da764ca2ecf7b3e6241d99986782467066dd9daf3ca9e3653214fc978d67241`.
Its reviewed source requires the independent process to exit zero, emit
no stderr, report PASS and agree on all twelve shared audit fields
before producing the final primary PASS line.

RUN.md transparently distinguishes an earlier administrative wrapper
stop while resolving a Windows-created worktree path under Linux. It
records that this occurred before either verifier was invoked, and that
only the wrapper outside the repository was corrected. The scientific
record therefore identifies the subsequent completed invocation as the
first scientific run. The frozen-file checks disclose no changed
scientific input or threshold associated with that correction.

## Result consistency

The reported exact forward resources are:

| Quantity | Recorded result |
| --- | ---: |
| G blocks | 64 |
| Completed global LS loops | 32000 |
| Carrier pulses | 3916931 |
| Absolute carrier angle / pi | 3916903 |
| Switching boundaries including both ends | 3948932 |
| Omitted-LS complete target successes | 0/25 |

These values satisfy every frozen prospective bound. The unchanged G
frames contribute 64*61200=3916800 carrier pi pulses; the other compiled
operations contribute 131 pulses and 103*pi of absolute angle. The
92-unit margins below both prospective carrier bounds reflect actual
canonical permutation lengths, not a changed compiler or post-pin
optimization. The switching count equals carrier pulses plus 32000 LS
loops plus one.

The edge exponents (4,4,16,16,20,4) agree with the common scalar in the
preregistration. The output records 25 complete inputs, 200 signed
exchange columns, 600 signed mask columns and 100 signed singleton
columns. These are the declared helper counts, including the exchange's
outside equal-label phase. The full program's two uniform sign choices
are correctly distinguished from the analytical composition argument
for mixed edge signs; no exhaustive 64-sign run is claimed.

The reported 0/25 omitted-LS result is consistent with the frozen
negative-control proof: memory remains zero, while the two unconditional
writes survive. This does not reuse or alter the predecessor's 5/25
control. The inverse result is expressly algebraic, obtained from the
assembled operators. It establishes no physically executable reverse
schedule or inverse resource budget.

## Scope of acceptance

The record supports a passing exact audit of the fixed 64-block
conditional construction on the supplied coherent input span. The
common scalar and laboratory phase convention are retained, as are
the memory distinction and counted counter. No observed falsifier is
reported or concealed by changing a frozen bound.

This review accepts one recorded local architecture run. Required new
public x86_64 and aarch64 CI checks are separate evidence on the final
PR head; this review does not assert their completion or inherit any
check from #1369. It is also not another independent implementation or
an independently earned theorem-grade result.

No numerical laboratory duration, physical calibration, accumulated
error, all-mode closure, preceding preparation, finite quantum
controller/work-source trajectory, occupied-memory reuse or full later
history follows from these exact counts. RESULT.md preserves these
limits and leaves the physical HOLD intact.
