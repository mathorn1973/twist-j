# C96-04 first cartridge development

NON-CANONICAL / STATIC + SOFTWARE + SYNTHETIC. A1 incomplete; A2 not measured.

The package supplies a concrete dual-pole sensing candidate, a selected-parts BOM and point-to-point netlist,
dimensioned D1 prototype, driver/time limiter and removable service heads, conditional 100/200 s divider-load calculation,
strict 34465A external-trigger SCPI adapter, empirical-map interpolation,
covariance-aware energy-difference uncertainty and hold evaluator. The design
and prospective protocol name the remaining circuit, fixture, safety,
metrology and independent acquisition gaps. There is no procurement list or
energization instruction approved for use.

```text
python -B -m unittest discover -s notes/v96-cartridge -p test_stage_a.py -v
python -B notes/v96-cartridge/stage_a.py
python -B notes/v96-cartridge/stage_a.py --hold APPROVED_EXTERNAL_HOLD.json
```

Development observation 2026-10-01, Python 3.12.10 on Windows x86_64:
24 tests completed with exit 0. They cover the exact divider budget, synthetic
provenance, injection masking, unchanged 200 s threshold, missing uncertainty,
timing/duty/charger/saturation faults, covariance, no extrapolation or CV2
substitution, actual SCPI command sequence, frozen identity and error handling,
overload, missing samples and trigger timestamps. No hardware was connected.

Sources were checked on 2026-10-01. Supplier PDF URLs/revisions are in
DESIGN.md and BOM.tsv. Their original bytes still need archival hashes in the
approved physical-gate evidence manifest before a manufacturing/qualification
pin. No external supplier PDF or raw laboratory data is copied into Canon.

Next blocker: the laboratory must provide the independent actual pole-state
and aperture observation chain with physical wiring and uncertainty/coupling
bounds. GPIO or coil current does not establish contact isolation. The D1
hardware candidate is ready for circuit/mechanical review; as-built fit,
protection, configured dielectric temperature probe and calibrated timing
remain unverified. The strict software timing contract currently requires
exact 200 ms probe intervals, 1 NPLC, independent trigger/completion times and
all apertures inside the final 100 ms. Physical compatibility is not proven.
Then actual assembled data must establish <=20 mJ with uncertainty at both
horizons. Software and catalogue figures cannot discharge that debt.

Read BUILD.md and NETLIST.tsv alongside DESIGN.md; REVIEW.md records the
separate fail-closed software review. No A1-complete or physical PASS claim.

Static D1 verification on 2026-10-01: BOM/NETLIST tabular field counts agree
(30/46 rows), each U1-U7/R1-R22/C1-C6/CT1-CT10 pin appears exactly once,
and the enclosure SVG parses as XML. This checks document consistency only;
it is not ERC, circuit simulation, mechanical fit or physical qualification.
The 24 development tests were rerun after documentation reconciliation with
exit 0; no hardware call occurred.
