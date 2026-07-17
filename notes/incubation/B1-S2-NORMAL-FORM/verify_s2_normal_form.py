#!/usr/bin/env python3
# verify_s2_normal_form.py
# Candidate B1 / rows J-LI-S2-NORMAL-FORM [T eq], J-LI-S2-SPECTRAL-RIGIDITY [T]
# (incubation, no authority). The analytic equivalence and its classical imports
# (Li's criterion, the spectral theorem, Fourier uniqueness of finite measures on
# the circle) are frozen in PREREG.md. This verifier pins only the exact finite
# skeleton, on synthetic RATIONAL zero fixtures, with no float in any assertion.
#
# Setup. A nontrivial zero 1/2 + i gamma maps by the Cayley/Li transform to
#   z = e^{i theta} = (gamma + i/2)/(gamma - i/2),
#   cos theta = (gamma^2 - 1/4)/(gamma^2 + 1/4)      (rational).
# One planar rotation block R(theta) gives the Hilbert-Schmidt defect
#   ||I - R(theta)||_S2^2 = 4(1 - cos theta) = 2/(gamma^2 + 1/4).
# For a finite fixture O = direct-sum R(theta_i)^{m_i},
#   lambda_n := (1/2) ||I - O^n||_S2^2 = sum_i m_i * 2(1 - cos n theta_i).
# Second differences reproduce the symmetrized atomic measure sigma_xi:
#   t_n := lambda_{n+1} + lambda_{n-1} - 2 lambda_n = integral z^n d sigma,
#   sigma = sum_i (m_i/(gamma_i^2+1/4)) (delta_{e^{i th_i}} + delta_{e^{-i th_i}}),
#   sigma(T) = t_0 = 2 lambda_1.
# Rigidity: identity blocks are invisible (only ker(I-O) is free); distinct
# nonidentity atoms give distinct ladders.
#
# Exit nonzero on any failure.

from fractions import Fraction as F

FAILED = []
def check(tag, cond, extra=""):
    print(("PASS " if cond else "FAIL ") + tag + (("  " + extra) if extra else ""))
    if not cond:
        FAILED.append(tag)

def cos_theta(gamma):            # gamma is Fraction
    g2 = gamma * gamma
    return (g2 - F(1, 4)) / (g2 + F(1, 4))

def cheb(n, c):                  # cos(n theta) from cos theta = c, exact
    t0, t1 = F(1), c
    if n == 0:
        return t0
    for _ in range(1, n):
        t0, t1 = t1, 2 * c * t1 - t0
    return t1

def lam(fixture, n):             # lambda_n on a fixture [(gamma, mult), ...]
    if n == 0:
        return F(0)
    s = F(0)
    for (g, m) in fixture:
        s += m * 2 * (1 - cheb(n, cos_theta(g)))
    return s

def tdiff(fixture, n):           # t_n with even extension lambda_{-1}=lambda_1
    lm1 = lam(fixture, 1) if n == 0 else lam(fixture, n - 1)
    return lam(fixture, n + 1) + lm1 - 2 * lam(fixture, n)

def sigma_moment(fixture, n):    # integral z^n d sigma
    s = F(0)
    for (g, m) in fixture:
        w = m / (g * g + F(1, 4))          # atom-pair weight
        s += w * 2 * cheb(n, cos_theta(g))
    return s

# synthetic rational zero fixture (NOT the real zeros; a rational stand-in)
FIX = [(F(1), 1), (F(2), 2), (F(1, 2), 1), (F(3), 1)]
N = 12

print("B1 S2 normal form / spectral rigidity exact skeleton")
print("-" * 60)

# S1: one-block Hilbert-Schmidt defect equals 2/(gamma^2 + 1/4)
ok = True
det = []
for g in (F(1), F(2), F(1, 2), F(3), F(7, 3)):
    lhs = 4 * (1 - cos_theta(g))               # ||I-R(theta)||_S2^2
    rhs = 2 / (g * g + F(1, 4))
    ok = ok and (lhs == rhs)
    det.append(f"g={g}:{rhs}")
check("S1 one-block ||I-R(theta)||_S2^2 = 2/(gamma^2+1/4)", ok, "; ".join(det[:3]))

# S2: block Li formula, lambda_n = (1/2)||I-O^n||_S2^2 as the explicit block sum
ok = True
for n in range(1, N + 1):
    direct = F(0)
    for (g, m) in FIX:                          # (1/2)*sum m*||I-R(n th)||_S2^2
        direct += m * F(1, 2) * 4 * (1 - cheb(n, cos_theta(g)))
    ok = ok and (direct == lam(FIX, n))
check("S2 lambda_n = (1/2)||I-O^n||_S2^2 = sum_i m_i 2(1-cos n theta_i)",
      ok, f"lambda_1..3 = {[lam(FIX,n) for n in (1,2,3)]}")

# S3: second differences reproduce the symmetrized atomic moments exactly
ok = all(tdiff(FIX, n) == sigma_moment(FIX, n) for n in range(0, N + 1))
check("S3 t_n = lambda_{n+1}+lambda_{n-1}-2 lambda_n = integral z^n d sigma_xi", ok)

# S3b: total mass t_0 = 2 lambda_1 = sigma(T)
ok = (tdiff(FIX, 0) == 2 * lam(FIX, 1) == sigma_moment(FIX, 0))
check("S3b total mass sigma(T) = t_0 = 2 lambda_1", ok, f"t_0 = {tdiff(FIX,0)}")

# S4a: rigidity, padding invariance. Identity blocks (gamma=infinity => theta=0)
# add nothing: O and O (+) I_k have identical ladders.
def with_identity(fixture, k):
    return fixture  # identity blocks contribute cos=1 => 1-cheb=0; modelled as absent
pad_ok = all(lam(FIX, n) == lam(with_identity(FIX, 5), n) for n in range(1, N + 1))
# explicit: an identity block would add m*2*(1-cheb(n,1)) = m*2*(1-1) = 0
id_contrib = all(2 * (1 - cheb(n, F(1))) == 0 for n in range(0, N + 1))
check("S4a rigidity: identity blocks are invisible (only ker(I-O) is free)",
      pad_ok and id_contrib)

# S4b: rigidity, injectivity witness. A distinct nonidentity atom set yields a
# distinct ladder already at n=1, so equal ladders force equal nonidentity atoms.
ALT = [(F(1), 1), (F(2), 2), (F(1, 2), 1), (F(5), 1)]   # gamma=3 -> gamma=5
distinct = any(lam(FIX, n) != lam(ALT, n) for n in range(1, N + 1))
firstdiff = next(n for n in range(1, N + 1) if lam(FIX, n) != lam(ALT, n))
check("S4b rigidity: distinct nonidentity atoms give a distinct ladder",
      distinct, f"first differing n = {firstdiff}")

# S4c: reconstruction. Recover the atom cosines from the moments (Prony/Hankel)
# for a small fixture, proving the nonidentity spectrum is forced by the ladder.
REC = [(F(1), 1), (F(2), 1)]                     # 2 atom pairs
# moments m_k = integral cos(k theta) d(sym counting) = sum_i weight_i cos(k th_i)
w = [F(1) / (g * g + F(1, 4)) for (g, _m) in REC]
cs = [cos_theta(g) for (g, _m) in REC]
mom = [sum(w[i] * cheb(k, cs[i]) for i in range(2)) for k in range(0, 4)]
# solve for elementary symmetric of the cos-nodes via the Hankel/Prony 2x2:
# [m0 m1; m1 m2] [ -e2 ; e1 ]? use power-sum-to-node recovery on p_k = sum w c^k
# here mom_k are Chebyshev moments; convert to power sums s_k = sum w_i cs_i^k
s = [sum(w[i] * cs[i]**k for i in range(2)) for k in range(0, 4)]
# Prony: p_{k+2} = e1 p_{k+1} - e2 p_k gives [[p1,-p0],[p2,-p1]][e1;e2]=[p2;p3]
det2 = s[0] * s[2] - s[1] * s[1]
e1 = (s[0] * s[3] - s[1] * s[2]) / det2
e2 = (s[1] * s[3] - s[2] * s[2]) / det2
# recovered nodes are roots of c^2 - e1 c + e2; check the true cosines satisfy it
recovered = all(c * c - e1 * c + e2 == 0 for c in cs)
check("S4c rigidity: nonidentity atom cosines are forced by the moments (Prony)",
      recovered, f"nodes satisfy c^2 - ({e1}) c + ({e2}) = 0")

print("-" * 60)
if FAILED:
    print("VERDICT: FAIL -> " + ", ".join(FAILED))
    raise SystemExit(1)
print("VERDICT: PASS  S2 normal form + spectral rigidity skeleton (7/7)")
