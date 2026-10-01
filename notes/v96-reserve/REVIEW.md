# Independent reserve review and corrections

**NON-CANONICAL / SOFTWARE DEVELOPMENT.** This review checks the conditional
mathematics and implementation against the fixed #1318 design and test plan.
It does not qualify a cartridge, converter, uncertainty budget or measured
work result. The reviewer did not author the original certifier. The reviewer
did author the two corrections below, which require the integrating reviewer's
final read and regenerated report receipt.

## Scope and finding disposition

Read `RESERVE_THEOREM.md`, `certify.py`, `budgets-v1.json`, the independent
arithmetic checker, development tests and README, together with the unchanged
`C-WORK-RECORD-CARTRIDGE-DEVICE-N/DESIGN.md` section 4 and `TEST_PLAN.md`
sections 2, 3 and the staged qualification requirements. The inherited law
remains at #1316 `312d0a90b24d5f9e743096f0ee2a477cda719a10`; apparatus rules
remain at #1318 `4756a3df650b91fb1d30806b0fb2aaac00e50cc2`.

Two missing conservative terms were found and corrected:

1. **Whole-horizon negative absolute work omitted non-G intervals.** The old
   block bound summed ten G-slot bounds. The fixed test plan also requires
   leakage/switching bounds outside G and an absolute-work limit over the
   entire 100 s. An out-and-back target-port current during A/B/F can leave
   every endpoint energy unchanged yet violate that limit. The schema now
   requires `negative_abs_work_outside_G_per_macrostep`, an upper bound on
   integral absolute target-port work **including uncertainty** over all eight
   non-G seconds. At each complete macrostep boundary the block bound sums
   both categories and resets only at the fixed 100 s block boundary. Both
   forward and inverse chronology are covered. The supplied zero is an
   unqualified hypothetical input, not an implication of isolation or small
   signed work. A regression with 2.1 mJ per non-G interval and zero G work
   produces 21 mJ at 100 s and again in the second 100 s block, while its
   encoding constraints remain conditional.
2. **Swap disturbance omitted the complete slot's passive/read terms.** The
   frozen predicate bounds the same physical cartridge's endpoint energy
   difference and does not authorize subtracting fitted passive drift.
   The sufficient bound now includes the 2.5 s idle loss, one read load and
   signed read coupling, as well as contact loss/coupling and `2*U_swap`.
   A regression that previously accepted 4.998 mJ from the contact and
   uncertainty terms now rejects its complete 5.0015 mJ slot bound.

No additional defect was found in the reviewed support propagation,
first-work inequalities or individual-budget optimization. This statement is
limited to the declared finite traces and conditional transition relation.

## Mathematical checks

For `Xi(b)={x:sum(x)=0, abs(x_i)<=b}`, the six permutations of `(-b,0,b)`
are the vertices, so its support is exactly `b*(max(a)-min(a))`. The
implementation retains each group's identity through addition, proportional
redistribution and serial permutations, cancels shared opposite coefficients
before taking supports, and sums supports only across independent groups.
The scalar loss `[0,b]` and signed `[-b,b]` support rules are also correct.
The 125-direction vertex regression independently enumerates all six corners.

The accepted-G recurrence is the affine image of the assumed relation:
`E'_a=(n'_a/S)*(sum(E)-D)+xi_a`. Its sum returns `sum(E)-D` because xi has
exactly zero sum, including zero-count accounts. A negative zero-account
increment is explicitly a deviation from its fixed physical baseline. It
is not omitted from the ledger or assigned negative absolute energy. Rejected
G is identity before the declared passive/read disturbance; accepted `S=0`
is rejected before division. Each accepted operation is charged the full
bounded startup/tail/switching cost of up to 32 starts, with READY zero at
both ends. Correlated return credit is not manufactured.

The true-energy enclosure is distinct from a meter estimate. Under the
explicit assumption `abs(estimate-true)<=U`, guaranteeing
`abs(estimate-target)+U<=tolerance` requires the conservative `2U` used here.
The same logic applies to first signed work, source equality, swap endpoint
differences and idle differences. The separate 1 mJ idle-difference input is
present; its near-20 mJ regression correctly fails at 21 mJ. Negative absolute
work inputs already include their uncertainty, so they are summed as supplied
and are not doubled again. Expanded uncertainty is not thereby proved to be
a deterministic physical error bound; that is a qualification premise.

First receiving work uses the entire G slot's signed terminal balance,
adding removed passive/read energy and local B heat and subtracting non-port
probe injection. It does not equate a resource decrement or gross servo pulse
with net delivered work. Treating the B-heat bound independently of total G
loss enlarges the possible set and is conservative. The other-energy upper
bound includes all initial model-zero resource/channel errors, receiver Z2,
all positive injection since preparation, and the explicit unresolved term;
it cannot be reduced by dissipation. The stronger source-attribution
inequality is separate from the target-work lower bound. No-commanded-baseline
withdrawal and absence of additional energy routes remain physical premises.

Swaps permute complete affine forms and serial identities before local
disturbances. The uniform calibration envelope is checked for every endpoint
and every serial, so the global voltage claim does not depend on identifying
the incoming and outgoing serial at one role as the same capacitor. The
continuous path inside an endpoint hull plus sag/overshoot is explicitly
assumed, not inferred from endpoint samples. Cumulative idle/read dissipation
is charged before any injection credit and kept below the same 20 mJ ceiling
at both 100 s and 200 s.

For one varying budget the retained supports give linear rational
inequalities. Positive coefficients impose upper endpoints, negative
coefficients lower endpoints, and a violated constant row makes the interval
infeasible. `maximum_budgets` implements those rules with all other budgets
fixed. The resulting maxima refer to this sufficient enclosure, not a
physical optimum, and cannot be combined componentwise. The separate report
checker correctly describes itself as an arithmetic check of supplied rows,
not an independent proof that all required rows were generated.

## Executed checks and final-report handoff

Actual reviewer execution on Windows/Python 3.12.10:

```text
python -B -m unittest discover -s notes/v96-reserve -p test_reserve.py -v
Ran 17 tests in 1.627s -- OK
git diff --check -- notes/v96-reserve
exit 0
```

The reviewed post-correction file hashes are:

| File | SHA-256 |
| --- | --- |
| certify.py | f42eea97a315b28be2d9c8c1e184949e7e1f1e5b32dc48cbbfd8facc5df8fc14 |
| budgets-v1.json | 2bd9889668a3e3694a79ea115ce8228911543d170e32ef9c6e960e201d4940f3 |
| test_reserve.py | 6f6f9b7d28815b3758e70e9ef0d64eb239cea4944e7f0d838a928a4b672494b3 |

The earlier full report predates these corrections and cannot authenticate
the final generator/input pair. The reviewer deliberately did not regenerate
the roughly 55 MB report in parallel. The integrating reviewer must run the
documented generator and arithmetic checker once against these final files,
record the new byte hash, and confirm all 12 classes. No scientific run,
physical trial, Canon fold or publication follows from this handoff.

### Completed integration read and regeneration

The coordinator separately reviewed both changed constraints, including their
forward/inverse boundary placement, and replayed all 17 tests (CPython
3.12.10 / Windows x86_64, exit 0). The final generator then completed for
all 12 classes and 812 snapshots with status CONDITIONAL and qualification
NOT_PERFORMED. The generated certificate is 55,208,887 bytes, SHA-256
`8070517d9108058ea598ebef3bf691da17e042486e8068ae9530dba8cdf2a83d`.
The separately implemented checker accepted that exact hash and all 72,156
rational inequalities, exit 0. The certificate remains outside Git.
This completes the integration handoff for these source bytes; earlier
development certificates are superseded, not physical counterevidence.
