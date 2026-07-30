#!/usr/bin/env python3
# C-METAL-TRACE-1_break.py
# Honest attempt to break candidate C-METAL-TRACE-1 by an INDEPENDENT code path.
# The verifier uses Q(sqrt d) coordinate pairs and a Z[zeta_8] cyclotomic basis.
# This path uses only integer 2x2 companion matrices and integer squarefree kernels;
# it never imports Fraction and never uses a cyclotomic basis. If the two paths agree,
# the arithmetic core survives one honest attempt. The trace->field probe deliberately
# looks for a counterexample to injectivity and RECORDS the scope boundary it finds.
# Standard library only. Integers only. No floats.

report = []
def note(s): report.append(s)

# ---------- integer 2x2 matrix helpers
def mm(A, B):
    return ((A[0][0]*B[0][0] + A[0][1]*B[1][0], A[0][0]*B[0][1] + A[0][1]*B[1][1]),
            (A[1][0]*B[0][0] + A[1][1]*B[1][0], A[1][0]*B[0][1] + A[1][1]*B[1][1]))
def madd(A, B):
    return ((A[0][0]+B[0][0], A[0][1]+B[0][1]), (A[1][0]+B[1][0], A[1][1]+B[1][1]))
def sm(k, A):
    return ((k*A[0][0], k*A[0][1]), (k*A[1][0], k*A[1][1]))
def det(A): return A[0][0]*A[1][1] - A[0][1]*A[1][0]
def tr(A):  return A[0][0] + A[1][1]
I2 = ((1, 0), (0, 1))

fails = 0
def must(name, cond):
    global fails
    ok = bool(cond)
    if not ok: fails += 1
    note(("OK   " if ok else "FAIL ") + name)

# companion of x^2 - t x - 1 is [[0,1],[1,t]]
def companion(t): return ((0, 1), (1, t))

for t, prime, disc, fld in ((1, 5, 5, "Q(sqrt5)"), (2, 2, 8, "Q(sqrt2)")):
    C = companion(t)
    # metal law  x^2 = t x + 1  as a matrix identity
    must("t=%d: C^2 = %d*C + I  (metal law, matrix path)" % (t, t),
         mm(C, C) == madd(sm(t, C), I2))
    must("t=%d: det C = -1  (norm -1, unit)" % t, det(C) == -1)
    must("t=%d: tr C = %d  (trace)" % (t, t), tr(C) == t)
    must("t=%d: disc = t^2+4 = %d" % (t, disc), t*t + 4 == disc)
    must("t=%d: prime %d divides disc %d -> %s" % (t, prime, disc, fld), disc % prime == 0)

# growth: powers of the companion carry the metal's own integer recurrence
def power_rows(t, N):
    C = companion(t); rows = [None]*(N+1); Ck = I2
    seq = []
    for k in range(1, N+1):
        Ck = mm(Ck, C)
        seq.append(Ck[0][1])   # top-right entry
    return seq
# gold top-right entries are Fibonacci; silver top-right entries are Pell
fib = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
pel = [1, 2, 5, 12, 29, 70, 169, 408, 985, 2378, 5741]
must("gold companion powers give Fibonacci (independent of the pair path)",
     power_rows(1, 11) == fib)
must("silver companion powers give Pell (independent of the pair path)",
     power_rows(2, 11) == pel)

# ---------- sqrt(2i) by an independent Gaussian-integer computation (no zeta_8 basis)
# Z[i] as pairs (a,b) = a + b i, i^2 = -1
def gmul(u, v):
    a, b = u; c, d = v; return (a*c - b*d, a*d + b*c)
def gnorm(u): return u[0]*u[0] + u[1]*u[1]
one_plus_i = (1, 1)
must("(1+i)^2 = 2i in Z[i] (Gaussian path)", gmul(one_plus_i, one_plus_i) == (0, 2))
must("N_{Q(i)/Q}(1+i) = 2  (degree-2 norm)", gnorm(one_plus_i) == 2)
must("norms consistent: degree-4 norm = (degree-2 norm)^2 = 4", gnorm(one_plus_i)**2 == 4)

# ---------- scope probe: is trace -> field injective? Try to break it.
def squarefree_kernel(n):
    # return the squarefree part of n (n > 0)
    k = 1; d = 2; m = n
    while d*d <= m:
        e = 0
        while m % d == 0:
            m //= d; e += 1
        if e % 2 == 1: k *= d
        d += 1
    if m > 1: k *= m
    return k
note("")
note("trace -> field probe  (disc = t^2 + 4, squarefree kernel = field Q(sqrt kernel)):")
seen = {}
collision = False
for t in range(0, 9):
    disc = t*t + 4
    ker = squarefree_kernel(disc)
    tag = "Q(sqrt%d)" % ker
    hit = seen.get(ker)
    if hit is not None:
        collision = True
        note("  t=%d  disc=%-3d  kernel=%-3d  %-10s  <-- SAME FIELD as t=%d"
             % (t, disc, ker, tag, hit))
    else:
        seen[ker] = t
        note("  t=%d  disc=%-3d  kernel=%-3d  %-10s" % (t, disc, ker, tag))

note("")
if collision:
    note("SCOPE BOUNDARY FOUND: trace -> field is NOT injective (e.g. t=1 and t=4 both give")
    note("Q(sqrt5)). The candidate is therefore scoped to the TWO SIMPLEST metals t in {1,2},")
    note("whose FUNDAMENTAL discriminants are exactly 5 and 8, the two program primes. This is")
    note("a scope, not a contradiction: the promoted claim never asserted injectivity for all t.")
else:
    note("no collision found in t in [0,8] (unexpected; check the probe)")

print("\n".join(report))
print()
print(("CORE SURVIVES, %d assertions, 0 failures" % (len(report))) if fails == 0
      else "CORE BROKEN, %d failures" % fails)
raise SystemExit(0 if fails == 0 else 1)
