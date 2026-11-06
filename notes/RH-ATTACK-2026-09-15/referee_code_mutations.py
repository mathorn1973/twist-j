"""Referee (code lens) mutation harness for verify_epsilon_guard.py.
Imports the lane verifier as a module and re-runs selected groups under deliberate
corruptions; a check is non-vacuous only if it turns to FAIL under the mutation.
int/Fraction only. Asserts nothing about mathematics."""
import importlib.util, io, contextlib, sys
from fractions import Fraction as F
spec = importlib.util.spec_from_file_location("veg", "verify_epsilon_guard.py")
veg = importlib.util.module_from_spec(spec); sys.modules["veg"] = veg; spec.loader.exec_module(veg)

def run(group):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        group()
    return [l for l in buf.getvalue().splitlines() if l.startswith(("PASS", "FAIL"))]

def report(name, lines, ids):
    got = {l.split(":")[0].split()[1]: l.split()[0] for l in lines}
    print(f"{name}: " + ", ".join(f"{i}={got.get(i,'?')}" for i in ids))

# baseline
report("baseline G4", run(veg.group_G4), ["G4a","G4b","G4c","G4d","G4e","G4g","G4f"])

# M1: G4c must FAIL if a test polynomial leaves V_N (constant term != 0)
orig_tp = veg.test_polynomials
veg.test_polynomials = lambda: [("1+t", [F(1), F(1)])]
report("M1 constant term added (expect G4c FAIL, G4d FAIL)", run(veg.group_G4), ["G4b","G4c","G4d"])
veg.test_polynomials = orig_tp

# M2: G4a must FAIL if R_n is perturbed
orig_R = veg.R
veg.R = lambda n: [v + (1 if k == 0 and n == 3 else 0) for k, v in enumerate(orig_R(n))]
report("M2 R_3 perturbed (expect G4a FAIL, G4g FAIL)", run(veg.group_G4), ["G4a","G4g","G4e"])
veg.R = orig_R

# M3: G1a must FAIL if mobius is wrong at one squarefree value
orig_mob = veg.mobius
veg.mobius = lambda n: (0 if n == 6 else orig_mob(n))
report("M3 mu(6):=0 (expect G1a FAIL, G1b FAIL)", run(veg.group_G1), ["G1a","G1b","G1c","G1d"])
veg.mobius = orig_mob

# M4: G8a must FAIL if one published digit is off by one
veg.PUBLISHED[(F(1, 4), 32)] = (608193475645, 608193475646)
report("M4 published N=32 shifted by 1e-12 (expect G8a FAIL)", run(veg.group_G8), ["G8a"])
veg.PUBLISHED[(F(1, 4), 32)] = (608193475644, 608193475645)

# M5: G3d/G3e sensitivity: is the 'simple zero at 1-eps' derived or built in?
# In the lane model Y = ls(-1, ...) has its pole order as INPUT; ls_inv gives lo=+1 by
# construction, so ls_coef(Q,0)==0 and ls_coef(Q,-1)==0 hold for every z, y.  Test by
# feeding random-looking z, y: if G3d/G3e still PASS for all of them, they test only the
# Laurent-arithmetic bookkeeping, not any property of zeta.
orig_ls = veg.ls
def ls_scrambled(lo, coeffs):
    c = [F(x) for x in coeffs]
    if lo == 0 and len(c) >= 8 and c[0] == F(-7, 3):  # the z model
        c = [F(5, 7), F(-3), F(11, 2), F(1, 9), F(2), F(0), F(1), F(4)]
    return orig_ls(lo, c)
veg.ls = ls_scrambled
report("M5 z-model scrambled (G3d/G3e PASS regardless: bookkeeping only)", run(veg.group_G3), ["G3a","G3b","G3c","G3d","G3e"])
veg.ls = orig_ls

# M6: G7b must FAIL if the margin is negative (theta >= sigma1)
orig_check = veg.check
def g7_bad():
    theta, sigma1 = F(5, 8), F(5, 8) - F(1, 100)
    eta1 = (sigma1 - theta) / 2; Rbig = 1 - theta; r = 1 + eta1 - sigma1; r1 = eta1 / 2; r2 = (r + Rbig) / 2
    return bool(0 < r1 < r < r2 < Rbig <= F(1, 2))
print("M6 G7b geometry with theta > sigma1 evaluates to", g7_bad(), "(expect False)")

# scope counts promised by the markdown verifier map
print("scope: test polynomials =", len(orig_tp()), "(markdown: 36); stand-in arrays =", len(veg.stand_in_arrays()), "(markdown: four)")
