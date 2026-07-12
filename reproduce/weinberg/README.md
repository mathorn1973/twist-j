# Weinberg witness

The Weinberg sector at the exact layer, in exact arithmetic:
integers, rationals, Q(sqrt5) pairs, the cyclotomic ring Z[zeta_5],
and a formal pi graded ring with Q(sqrt5) coefficients. No floats
anywhere; pi is a formal symbol. The measured comparison of
sin^2 theta_W against experiment is a fenced witness in the Canon
text and is deliberately outside this file: no value is claimed
beyond the committed form.

Verified: the face degree deg_f = Tr(J) = 3 on the power basis of
Z[zeta_5] (Tr(1) = 4, Tr(zeta^m) = -1); the trace kernel of dimension
3 over Q with 125 = 5^3 points over F_5 by full enumeration, so
B_quark = 1/3 = 1/dim ker(Tr); the tree value 3/13 = deg_f/(V + 1)
with V = 12 = d(d + 1) by two agreeing routes; the hypercharge law
Y_F = (B - L) + 2 T_3^R reproducing all seven standard model
hypercharges exactly in Q (quark doublet 1/3, u_R 4/3, d_R -2/3,
lepton doublet -1, nu_R 0, e_R -2, Higgs 1); the correction term
phi^-4 = 5 - 3 phi = (7 - 3 sqrt5)/2, exactly positive, over
32 = 2^5; and the parity of the committed form (pi degrees {0, -2}
both even: pi even and delta free on the register), with the single
positive correction placing the form above the tree value at the
form level.

Evidence for registry claims WEINBERG-TREE, HYPERCHARGE-LAW,
WEINBERG-FORM. Check map: 01 to 03 WEINBERG-TREE; 04
HYPERCHARGE-LAW; 05 and 06 WEINBERG-FORM.

Run from the repository root:

```
python3 reproduce/weinberg/verify.py
```

Expected: byte identical to EXPECTED.txt, RESULT 6/6 ALL PASS,
exit 0, no stderr.
