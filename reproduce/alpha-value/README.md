# Alpha value witness

The alpha sector at the committed form, in exact arithmetic:
integers, rationals, Q(sqrt5) pairs, the cyclotomic ring Z[zeta_5],
and rigorous integer interval arithmetic for the finite precision
evaluation. No floats anywhere. Decimal digit strings appear only as
labeled witnesses of the committed form; the CODATA comparison is a
fenced measured witness with a declared rational input, and no value
is claimed beyond the committed form.

Verified: the prefactor chord 1 + J Jbar = 3 - phi = |1 - zeta|^2
exactly in Z[zeta_5], so the Queen prefactor sqrt(s) =
(3 - phi)^(1/4) = (1 + J Jbar)^(1/4) is the gravity modulus inside
the electromagnetic number; the generalized Bernoulli value
B_{2,chi5} = 4/5 exactly by definition; the Gauss sum tau =
zeta - zeta^2 - zeta^3 + zeta^4 = 2 phi - 1 = sqrt5 exactly in
Z[zeta_5] with tau^2 = 5, so the L value normalization is computed,
not cited; the prefactor unification L(2, chi5) = 4 pi^2/(25 sqrt5)
and 80 sqrt5 L(2, chi5) = (8 pi)^2/5 exactly in Q, so the
preregistration witness formula and the Queen formula are one
formula and no independent L value enters the alpha sector; the
Queen structure alpha^-1 = (8 pi)^2 (3 - phi)^(1/4) (1 + X/5)^5 / 5
with X = 1/(32 pi^2 phi^4) the same slip as the Weinberg correction,
every pi degree even; the enclosure of the committed form by exact
integer intervals at scale 10^50 (Machin arctangents, integer square
roots, outward rounding) to width below 10^-20, reading
137.0359991899 unrounded and 137.035999190 rounded at the ninth
decimal place; and the fenced CODATA 2022 window (137.035999177(21)
declared): the form sits above the central value and within one part
per billion of it.

Evidence for registry claims ALPHA-PREFACTOR-UNIFICATION,
ALPHA-FORM, ALPHA-VALUE-DIGITS. Check map: 01 to 04
ALPHA-PREFACTOR-UNIFICATION; 05 ALPHA-FORM; 06 and 07
ALPHA-VALUE-DIGITS (07 is the fenced measured window and moves no
status).

Run from the repository root:

```
python3 reproduce/alpha-value/verify.py
```

Expected: byte identical to EXPECTED.txt, RESULT 7/7 ALL PASS,
exit 0, no stderr.
