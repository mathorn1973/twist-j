# Cosmology register witness

The cosmology register at the committed forms, in exact arithmetic:
integers, rationals, polynomial rings over Q, and exact Thue-Morse
pair counting with its substitution recursion. No floats anywhere;
pi and ln phi are formal symbols. The measured comparisons of the
register against observation stay fenced in the Canon text, and no
value is claimed beyond the committed forms.

Verified: the deformation J -> J e^(i eps) freezes the modulus
exactly (the phase monomial cancels in (J u)(Jbar u^-1) while the
argument moves), so the tensor channel carries zero at linear order
and r = 0 about the isotropic background; the bilinear TT decoder
identity det(I + H) - 1 = -|h|^2 for the traceless symmetric doublet,
with no linear term, so induced tensor power begins at quadratic
field order; the exact Thue-Morse pair census (the sliding pair
counts obey the substitution recursion at every dyadic scale 2^6 to
2^16, the invariant 6 c_00(4N) - 4N = 6 c_00(N) - N holds exactly,
and the pair substitution has the unique stationary vector
(1, 2, 2, 1)/6 with M v = 2 v, rank(M - 2I) = 3, and M^3 positive),
so the gyron gate (0, 0) has density rho = 1/6 = 1/(p + 1) exactly
and 1/rho = 6 is the proton prefactor of the mass ladder; the Basel
gate booking f_00 pi^2 = pi^2/6 on the phase 5 Li_1(J) = i pi, with
Li_2(1) = zeta(2) = pi^2/6 cited to Euler; the parity of the
committed register forms (w = -14/15, Omega_b = pi^2/200,
Omega_DM/Omega_b = 18 p^3 ln^2(phi)/pi^4 = 2250 ln^2(phi)/pi^4, the
tilt form n_s - 1 = -5 alpha), every one pi even and delta free,
with the dark matter reading 5 : 1 equal to (1 - f_00)/f_00 exactly;
and the conformal prefactor chain K_chi5 = k/(12 V_cell) =
1/(864 pi) with c_hom = 12 K_chi5 = 1/(72 pi) and 864 = 12 x 72.

Evidence for registry claims TT-LINEAR-ZERO, TT-QUADRATIC-INDUCED,
GYRON-DENSITY, COSMOLOGY-REGISTER, CONFORMAL-PREFACTOR. Check map:
01 TT-LINEAR-ZERO; 02 TT-QUADRATIC-INDUCED; 03 to 05 GYRON-DENSITY;
06 COSMOLOGY-REGISTER; 07 CONFORMAL-PREFACTOR.

Run from the repository root:

```
python3 reproduce/cosmology-register/verify.py
```

Expected: byte identical to EXPECTED.txt, RESULT 7/7 ALL PASS,
exit 0, no stderr.
