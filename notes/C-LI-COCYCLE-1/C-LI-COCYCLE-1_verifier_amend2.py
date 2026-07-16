#!/usr/bin/env python3
# C-LI-COCYCLE-1_verifier_amend2.py
# Amendment 2: cross-lane consolidation of the finite-carrier no-go
# (owner row J-LI-CYCLIC-CARRIER-DIMENSION, commit a62b040, independently
# re-derived here) and the measure dictionary.
#
# Statements frozen before the single run:
#   CC1  Exemplar instance (no atom at 1): U = primitive 10th roots,
#        v = (1,1,1,1), cycle cocycle b(n) = sum_{k<n} U^k v. The exact
#        ladder f(n) = ||b(n)||^2 is integral, equals
#        (0,4,10,14,20,24,20,14,10,4,0) on n = 0..10, has period 10 through
#        n = 40, maximum 24, and f(10m) = 0: a_* = mu_v({1}) = 0, the
#        ladder is BOUNDED. A finite J-native carrier realizes a bounded
#        cycle ladder and can never host lambda_n.
#   CC2  Atom instance: U' = C_4 regular representation (eigenvalues
#        1, i, -1, -i), v = (1,1,1,1). Exact ladder g(n) = n^2 + r(n) with
#        r periodic (0,3,4,3) and g(4m) = 16 m^2: a_* = mu({1}) = 1
#        exactly. Together CC1 + CC2 witness the dichotomy
#        ||b(n)||^2 = a_* n^2 + O(1) for finite spectra, the core of the
#        no-go (general proof: Dirichlet kernel split, atom at 1 gives
#        n^2 * mass, atoms away from 1 are bounded by mass/sin^2(theta/2);
#        imported analysis labeled in the candidate doc).
#   CC3  The telescoping dictionary, ladder-independent identity:
#        sum_{m=1..N} t_m = psi(N+1) - psi(N) - psi(1) and
#        t_0 + 2 sum_{m=1..N} t_m = 2 (psi(N+1) - psi(N)), for
#        t_m = psi(m+1) + psi(m-1) - 2 psi(m), psi even, psi(0) = 0;
#        checked exactly on two different ladders (the exemplar ladder and
#        psi(n) = n^2). With Wiener's theorem (imported) this gives
#        mu_v({1}) = lim 2 (lambda_{N+1} - lambda_N) / (2N + 1):
#        the no-atom condition is EQUIVALENT to lambda_{N+1} - lambda_N
#        = o(N).
#   CC4  The 1_G versus chi_0^(5) distinction (owner audit commit 1678d7b):
#        L(s, 1_G) = zeta while L(s, chi_0) drops the 5-Euler factor;
#        coefficientwise five_tower * chi_0 = all-ones for n <= 200, exact.
#   CC5  Dichotomy summary asserts: max f over n <= 40 equals the period
#        maximum 24; g(n) - n^2 bounded by 4 for n <= 40.
#
# Discipline: stdlib only, exact arithmetic in every assertion, no floats
# in this file. Environment: LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1
# PYTHONHASHSEED=0 TZ=UTC.

FAILED = []

def check(name, ok):
    print(("PASS " if ok else "FAIL ") + name)
    if not ok:
        FAILED.append(name)

# ---- Z[zeta_20] ----
def z20mul(a, b):
    c = [0] * 15
    for i in range(8):
        for j in range(8):
            c[i + j] += a[i] * b[j]
    for d in range(14, 7, -1):
        k = c[d]
        if k:
            c[d] = 0
            c[d - 2] += k
            c[d - 4] -= k
            c[d - 6] += k
            c[d - 8] -= k
    return tuple(c[:8])
def z20pow(a, n):
    r = (1, 0, 0, 0, 0, 0, 0, 0)
    for _ in range(n):
        r = z20mul(r, a)
    return r
def z20add(a, b): return tuple(x + y for x, y in zip(a, b))
Z20 = (0, 1, 0, 0, 0, 0, 0, 0)
z10 = z20pow(Z20, 2)
def z20conj(a):
    out = (0,) * 8
    for e in range(8):
        if a[e]:
            out = z20add(out, tuple(a[e] * x for x in z20pow(Z20, (19 * e) % 20)))
    return out

# CC1: exemplar cycle ladder
def f_of(n):
    tot = (0,) * 8
    for j in (1, 3, 7, 9):
        s = (0,) * 8
        for k in range(n):
            s = z20add(s, z20pow(z10, (j * k) % 10))
        tot = z20add(tot, z20mul(s, z20conj(s)))
    return tot
F_EXPECT = [0, 4, 10, 14, 20, 24, 20, 14, 10, 4, 0]
fv = []
ok = True
for n in range(0, 41):
    v = f_of(n)
    ok = ok and (v[1:] == (0,) * 7) and (v[0] >= 0)
    fv.append(v[0])
ok = ok and (fv[0:11] == F_EXPECT)
ok = ok and all(fv[n] == fv[n + 10] for n in range(31))
ok = ok and (fv[10] == 0 and fv[20] == 0 and fv[30] == 0 and fv[40] == 0)
ok = ok and (max(fv) == 24)
check("CC1 exemplar cycle cocycle: ladder integral, (0,4,10,14,20,24,...), period 10, zeros at 10m, max 24, a_* = 0: the finite J-native carrier is bounded and can never host lambda", ok)

# CC2: C_4 regular representation with the atom at 1
def cxadd(a, b): return (a[0] + b[0], a[1] + b[1])
I4 = [(1, 0), (0, 1), (-1, 0), (0, -1)]
def g_of(n):
    tot = 0
    for j in range(4):
        s = (0, 0)
        for k in range(n):
            s = cxadd(s, I4[(j * k) % 4])
        tot += s[0] * s[0] + s[1] * s[1]
    return tot
R_EXPECT = [0, 3, 4, 3]
ok = True
gv = [g_of(n) for n in range(0, 41)]
for n in range(0, 41):
    ok = ok and (gv[n] - n * n == R_EXPECT[n % 4])
ok = ok and all(gv[4 * m] == 16 * m * m for m in range(11))
check("CC2 C_4 instance: g(n) = n^2 + (0,3,4,3)-periodic remainder, g(4m) = 16 m^2 exactly: a_* = mu({1}) = 1, the n^2 law of an atom at 1", ok)

# CC3: telescoping dictionary on two ladders
def dico(psi, N):
    def p(m): return psi[abs(m)]
    t = [p(m + 1) + p(m - 1) - 2 * p(m) for m in range(N + 2)]
    ok1 = all(sum(t[1:Nn + 1]) == p(Nn + 1) - p(Nn) - p(1) for Nn in range(1, N + 1))
    ok2 = all(t[0] + 2 * sum(t[1:Nn + 1]) == 2 * (p(Nn + 1) - p(Nn)) for Nn in range(1, N + 1))
    return ok1 and ok2
psi_ex = fv[0:15]                      # exemplar ladder
psi_sq = [n * n for n in range(15)]    # a second, growing ladder
check("CC3 telescoping dictionary (ladder-independent): sum t_m = psi(N+1)-psi(N)-psi(1) and t_0 + 2 sum t_m = 2(psi(N+1)-psi(N)); Wiener reading: mu({1}) = lim 2(lambda_(N+1)-lambda_N)/(2N+1), so no atom iff increments are o(N)",
      dico(psi_ex, 12) and dico(psi_sq, 12))

# CC4: 1_G versus chi_0^(5): five_tower * chi_0 = all-ones, n <= 200
N4 = 200
tower = [0] * (N4 + 1)
k = 1
while k <= N4:
    tower[k] = 1
    k *= 5
chi0 = [0] + [(1 if n % 5 else 0) for n in range(1, N4 + 1)]
conv = [0] * (N4 + 1)
for d in range(1, N4 + 1):
    if tower[d]:
        for n in range(d, N4 + 1, d):
            conv[n] += chi0[n // d]
check("CC4 1_G vs chi_0^(5) (owner audit 1678d7b): (1-5^-s)^-1 L(chi_0) = zeta = L(1_G) coefficientwise for n <= 200; the two 'trivial' objects differ exactly on the 5-tower",
      all(conv[n] == 1 for n in range(1, N4 + 1)))

# CC5: dichotomy summary
check("CC5 dichotomy witnessed: bounded ladder (max over 40 = period max = 24) against n^2 + O(1) ladder (remainder bounded by 4); with Li + Lagarias (imported) lambda_n = n log n / 2 + O(n) is unbounded and o(n^2), excluding every finite carrier",
      max(fv) == 24 and max(gv[n] - n * n for n in range(41)) == 4)

print("FAILED: " + (", ".join(FAILED) if FAILED else "none"))
print("VERDICT: " + ("PASS amendment 2 of C-LI-COCYCLE-1" if not FAILED else "FAIL"))
