# Prospective one-cartridge Stage A protocol

NON-CANONICAL / DESIGN PROTOCOL / NOT EXECUTED. A1 remains incomplete as
enumerated in BUILD.md and DESIGN.md. A qualified human must finish circuit/protection,
manufacturing and safe laboratory procedures before construction or energy
application. This file is not an authorization to operate equipment.

1. Freeze the specimen/dock identifiers, component and wiring revisions,
   calibrations, raw-data and reduction schema, waveform/filter settings,
   environmental range, history/settling rules, window schedule, leakage and
   injection measurement method, uncertainty/covariance model, receipt trust
   policy and immutable external evidence destination. Record every attempt.
2. Confirm all source/instrument certificates and warm-up requirements. With
   the capacitor discharged by the selected removable 10 kohm service fixture after engineering review, inspect
   polarity, both disconnect poles, shrouds, retention and vent path. Confirm
   the service charging/discharging circuit cannot remain connected during a
   hold. Reject any permanent bleeder or unnoticed grounded sense return.
3. Characterize specimen-specific energy versus voltage, temperature and
   approach history with signed metered work and bounded losses. Separate
   charge and discharge histories; settle with the frozen actual read schedule.
   Do not choose new settling time after seeing a favorable hold. If histories
   cannot be covered by a valid single-valued map for the declared protocol,
   reject that encoding rather than fit a convenient nominal capacitance.
4. Screen one specimen first, visibly as SCREENING. This may expose a poor
   capacitor quickly but qualifies no level, dock population or complete chain.
   Preserve failures and their calibrated observations. Screening data do not
   become confirmatory data by renaming the files.
5. For full Stage A, cover n=0..41, each of 20, 23 and 26 C, approached from
   charging and discharging, at both 100 and 200 s: at least 504 condition cells
   for one specimen/dock pairing. Replication and drift blocks must be frozen
   before qualification; 504 distinct conditions is not an adequate statistical
   uncertainty study by itself. Repeat for every used specimen/dock pairing.
6. In each initiated hold, prepare within abs(E_inc-0.500*n)+U_E<=0.020 J.
   Physically disconnect preparation equipment at both terminals before the
   timed hold, retain the actual initial energy/voltage/read record, then use
   exactly the intended 100 ms read windows and candidate 100 ms front-end
   settling intervals. Record actual pole feedback, probe on-time, trigger and measurement-complete
   timestamps independently. The present adapter demands an exactly 200 ms
   observed interval, 1 NPLC and timing uncertainty wholly within the final
   100 ms. Qualify compatibility or preregister a reviewed contract revision;
   do not disguise command timestamps as contact observations.
7. Meter/bound total voltage-dependent leakage, surface paths, input charging,
   switch transients and both signs of measurement-supply coupling. Record the
   full voltage range, temperature, all samples/gaps/saturation and timing.
   Bound injection before evaluating loss; a flat final voltage sustained by
   an unknown supply is not evidence of low loss.
8. Reduce with frozen maps and propagated difference covariance. Require loss
   upper bound <=0.020 J at both horizons, U_E<=0.020 J, valid Dec at every
   actual read, voltages with their expanded uncertainty wholly within 4.7..50 V, and
   original timing/quality bounds. Missing voltage_U_V is indeterminate. All
   failed or indeterminate attempts stay visible; no replacement loop. Whole
   Stage A status requires the complete preregistered condition roster and
   authenticated evidence, not one SATISFIED numerical helper result.
9. After the hold ends, follow the separately approved interlocked discharge
   and access procedure. Verify safe state by independent measurement before
   access; the Python adapter does not control discharge or declare hardware
   safe. Record any failure of interlock or energy accounting.

Only actual full Stage A acceptance permits Stage B design construction.
Passing one capacitor housing does not qualify the remaining B/Z/r banks,
their dock pairings or the 400-trial apparatus. The first physical blocker is
an assembled cartridge loss measurement under the exact duty cycle, after
the A1 hardware gaps have been closed.
