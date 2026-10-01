# Conditional reserve certifier for the v96 proposal

**NON-CANONICAL / DEVELOPMENT.** This package supplies the C96-02 working
implementation under unchanged #1316/#1318 pins. It does not reserve a new
scientific ID, execute a prospective scientific gate, qualify hardware or
authorize a fold. Public Canon v95 remains authoritative.

- [RESERVE_THEOREM.md](RESERVE_THEOREM.md): the precise conditional relation,
  proof, true-energy versus meter uncertainty, and remaining physical debts.
- [budgets-v1.json](budgets-v1.json): versioned hypothetical exact input bounds.
- [certify.py](certify.py): Fraction affine propagation through 11 banks,
  baselines, donor-fed auxiliary starts/resets, whole-cartridge swaps, fixed
  read windows, all four configurations and both 200 s inverse orders.
- [check_report.py](check_report.py): separately implemented rational checking
  of report arithmetic and category maxima. It does not import the generator
  or certify the physical assumptions/affine recurrence.
- [test_reserve.py](test_reserve.py): known-case SOFTWARE development regressions.

Requires Python 3.12 standard library only; development checks used Python
3.12.10. No package installation, instrument, external solver or HDL simulator
is involved. From the repository root, for example on PowerShell:

```powershell
python -B -m unittest discover -s notes/v96-reserve -p test_reserve.py -v
python -B notes/v96-reserve/certify.py --output "$env:TEMP\twistj-v96-reserve-development.json"
python -B notes/v96-reserve/check_report.py "$env:TEMP\twistj-v96-reserve-development.json" --sha256 HASH_FROM_CERTIFIER_STDOUT
```

On Linux use an output such as `/tmp/twistj-v96-reserve-development.json`.
The CLI rejects an output path inside this worktree. The report can be tens of
megabytes because it retains every rational inequality and all layer support
coefficients. It is generated development material, never a tracked raw log or
an `EXPECTED.txt`/`RUN.md`. The stdout records its exact byte count and hash.
Changing an input produces a new report and hash; no old result is overwritten
in scientific evidence. Supply a different output filename to preserve local
development comparisons.

The supplied model returns `CONDITIONAL` for 12 logical energy classes and
812 snapshots (initial preparation plus every layer). Positive/cut classes
cover the 20 known H(w)=1 seeds; offimage remains its one declared preparation.
This is not 400 trials or end-to-end tuning. The known holdout's mathematics
is included in a pure energy-class check, not a physical system test.

The report contains:

- exact bounds for every bank, serial identity, baseline-inclusive stored
  energy, donor auxiliary peak/reset and independent dissipation/injection;
- an exact zero residual for the **conditional bank/auxiliary balance**,
  separate from unperformed measured apparatus closure;
- separate encoding and signed source-work constraints, plus negative
  integral-absolute-work bounds over G and every non-G interval supplied as
  explicit assumptions (the hypothetical non-G input is zero, not measured);
- the first failed constraint and attaining abstract corner where applicable;
- each category's maximum allowed budget with other categories fixed, its
  limiting configuration, mode, bank, operation and time;
- the mandatory 9.560 J versus 9.780 J broad-decoding counterexample.

These individual maxima are sufficient-enclosure limits, not efficiency
predictions. They cannot all be selected simultaneously. No numerical budget
has been fitted to a measurement; every physical premise remains UNQUALIFIED.

For the supplied hypothetical inputs, the exact conversion-loss maximum with
all other bounds fixed is `2423399/190000000 J` per accepted G. The limiting
bank is B0 in cut0, forward-then-inverse, at 198 s. Each individual startup,
tail or switching budget has maximum `2465199/6080000000 J` per donor start.
With the separate 1 mJ hold-difference uncertainty, the idle bound is at most
`7/78125 J/s`, and the per-swap dissipation bound
at most `729/1000000 J`. These are derived sufficient limits under the stated
assumptions, not component specifications. The default source-attributable
accepted-work lower bound is `5584923/5750000 J`, above the fixed 0.950 J
criterion. Gross uncontrolled injection is zero in this supplied example.

The next concrete blocker is qualification of the per-serial stored-energy
maps and continuous-time envelope, and the complete donor-fed equalizer's
loss/residual/deadline bounds over the cut0 stress sequence. In particular,
<=32 transfers in <=1.7 s is an assumed apparatus contract, not established
convergence. The actual FPGA, mechanical pointer, independent VI acquisition,
external fixture/host rail ledger and safety approval are outside this package.
The separate proof/propagation review, two resulting repairs and final
coordinator replay are recorded in [REVIEW.md](REVIEW.md). A separately
reserved formal audit remains necessary before proposing earned Canon
status for a reserve claim.
