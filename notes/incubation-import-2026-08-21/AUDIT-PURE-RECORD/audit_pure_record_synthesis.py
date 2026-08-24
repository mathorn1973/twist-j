#!/usr/bin/env python3
# Independent audit of the [PUBLIC] synthesis "most stoji, ale ne cely".
# Fresh code path: own Fraction kernel, own cyclotomic arithmetic. Nothing
# imported from any probe directory. Exact arithmetic only, no float.
# Exit 0 = all gates pass. Exit 2 = findings (each printed).
from fractions import Fraction as F
import itertools, sys

FIND = []
def gate(name, ok, note=""):
    print("%-46s %s%s" % (name, "PASS" if ok else "FAIL",
                          (" " + note) if note else ""))
    if not ok:
        FIND.append(name)

# ---------- matrix kernel ----------
def mat(r): return tuple(tuple(F(x) for x in row) for row in r)
def mmul(A, B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(len(B)))
                 for j in range(len(B[0]))) for i in range(len(A)))
def mvec(A, v):
    return tuple(sum(A[i][k]*v[k] for k in range(len(v))) for i in range(len(A)))
def madd(A, B): return tuple(tuple(A[i][j]+B[i][j] for j in range(len(A[0]))) for i in range(len(A)))
def msub(A, B): return tuple(tuple(A[i][j]-B[i][j] for j in range(len(A[0]))) for i in range(len(A)))
def smul(c, A): return tuple(tuple(c*A[i][j] for j in range(len(A[0]))) for i in range(len(A)))
def tr(A): return sum(A[i][i] for i in range(len(A)))
def tp(A): return tuple(tuple(A[j][i] for j in range(len(A))) for i in range(len(A[0])))
def eye(n): return tuple(tuple(F(1 if i == j else 0) for j in range(n)) for i in range(n))
def outer(u, v): return tuple(tuple(u[i]*v[j] for j in range(len(v))) for i in range(len(u)))
def rank(A):
    R = [list(r) for r in A]; rk = 0; row = 0
    for col in range(len(R[0]) if R else 0):
        p = next((r for r in range(row, len(R)) if R[r][col] != 0), None)
        if p is None: continue
        R[row], R[p] = R[p], R[row]
        pv = R[row][col]; R[row] = [x/pv for x in R[row]]
        for r in range(len(R)):
            if r != row and R[r][col] != 0:
                f = R[r][col]; R[r] = [a-f*b for a, b in zip(R[r], R[row])]
        row += 1; rk += 1
    return rk

ones = tuple(F(1) for _ in range(4))
OO = outer(ones, ones)
I4 = eye(4)
G = msub(I4, smul(F(1, 5), OO))          # DEF-QDD-GRAM
Ginv = madd(I4, OO)                       # canon: G^-1 = I + 11^T
Elow = smul(F(1, 4), OO)                  # DEF-QDD-PROJECTOR-LOW
Ehigh = msub(I4, Elow)                    # DEF-QDD-PROJECTOR-HIGH
MJ = mat([[1,0,-1,1],[0,1,-1,0],[1,0,0,0],[0,1,-1,1]])
D = msub(MJ, I4)                          # the phase motor D_J

gate("A01-Ginv-and-projectors",
     mmul(G, Ginv) == I4 and mmul(Elow, Elow) == Elow
     and mmul(Ehigh, Ehigh) == Ehigh and mmul(Elow, Ehigh) == smul(F(0), I4))

def sharp(A): return mmul(Ginv, mmul(tp(A), G))   # Gram adjoint
def m_of(v): return sum(v[i]*mvec(G, v)[i] for i in range(4))
def rho_of(v):
    m = m_of(v)
    return smul(F(1)/m, mmul(outer(v, v), G))

# ---------- W, the basis, the reflection ----------
# W = HIGH support = {sum v = 0}; basis b_i = e_i - e_3, i = 0,1,2
B = [tuple(F(1 if k == i else 0) - F(1 if k == 3 else 0) for k in range(4))
     for i in range(3)]
H = tuple(tuple(sum(B[i][k]*mvec(G, B[j])[k] for k in range(4))
          for j in range(3)) for i in range(3))
Ostar = mat([[-1,-1,-1],[0,1,0],[0,0,1]])
gate("A02-H-is-2-1-1-simplex-gram",
     H == mat([[2,1,1],[1,2,1],[1,1,2]]))
gate("A03-Ostar-H-orthogonal-involution",
     mmul(tp(Ostar), mmul(H, Ostar)) == H and mmul(Ostar, Ostar) == eye(3))

def to_coords(v):        # v in W -> coords in basis B
    assert sum(v) == 0
    c = (v[0], v[1], v[2])
    assert tuple(sum(c[i]*B[i][k] for i in range(3)) for k in range(4)) == v
    return c
def from_coords(c):
    return tuple(sum(c[i]*B[i][k] for i in range(3)) for k in range(4))
def O_on_W(v):           # apply Ostar to v in W via the basis
    return from_coords(mvec(Ostar, to_coords(v)))

A = mmul(Ehigh, mmul(D, Ehigh))           # compressed motor
gate("A04-A-preserves-W-and-TrA",
     all(sum(mvec(A, b)) == 0 for b in B) and tr(A) == F(-3, 4))

# ---------- the breaker instance ----------
v = (F(0), F(0), F(1), F(-1))
xL = O_on_W(mvec(A, v))
xR = mvec(A, O_on_W(v))
xL_stated = tuple(F(c, 4) for c in (1, 1, 1, -3))
xR_stated = tuple(F(c, 4) for c in (1, 1, -3, 1))
gate("A05-ordered-outputs-match-stated", xL == xL_stated and xR == xR_stated)

mL, mR = m_of(xL), m_of(xR)
gate("A06-equal-scalar-weight-3-4", mL == F(3, 4) and mR == F(3, 4))

lamB = ones                               # lambda_B in B0 coords
def w_low(v):
    ip = sum(v[i]*mvec(G, lamB)[i] for i in range(4))
    nrm = sum(lamB[i]*mvec(G, lamB)[i] for i in range(4))
    p = tuple(ip/nrm*lamB[i] for i in range(4))
    return sum(p[i]*mvec(G, p)[i] for i in range(4))
gate("A07-branch-weights-0-and-3-4",
     w_low(xL) == 0 and w_low(xR) == 0
     and mL - w_low(xL) == F(3, 4) and mR - w_low(xR) == F(3, 4))

rL, rR = rho_of(xL), rho_of(xR)
rL_stated = smul(F(1, 12), mat([[1,1,1,-3],[1,1,1,-3],[1,1,1,-3],[-3,-3,-3,9]]))
rR_stated = smul(F(1, 12), mat([[1,1,-3,1],[1,1,-3,1],[-3,-3,9,-3],[1,1,-3,1]]))
gate("A08-densities-match-stated-and-differ",
     rL == rL_stated and rR == rR_stated and rL != rR)

Veff = {F(0), F(1), F(2), F(-2), F(-1)}
gate("A09-outputs-outside-Veff",
     any(c not in Veff for c in xL) and any(c not in Veff for c in xR))

# ---------- pure-record identities, generic sweep ----------
ok_id = ok_uni = True
vals = [F(-2), F(-1), F(0), F(1), F(2), F(1, 2)]
seen = {}
for w4 in itertools.product(vals, repeat=4):
    if all(c == 0 for c in w4): continue
    m = m_of(w4)
    if m == 0: continue    # G is PSD with kernel only at 0 on Q^4? m=0 iff v=0
    r = rho_of(w4)
    if not (mmul(r, r) == r and sharp(r) == r and rank(r) == 1
            and tr(r) == 1
            and outer(w4, w4) == smul(m, mmul(r, Ginv))):
        ok_id = False; break
    key = (m, r)
    if key in seen and seen[key] != w4 and seen[key] != tuple(-c for c in w4):
        ok_uni = False; break
    seen.setdefault(key, w4)
gate("A10-identities-on-1295-vector-sweep", ok_id)
gate("A11-record-fibres-are-sign-pairs", ok_uni)
gate("A12-G-definite-on-Q4",
     all(m_of(w4) > 0 for w4 in itertools.product((F(-1), F(0), F(1)), repeat=4)
         if any(c != 0 for c in w4)))

# ---------- scalar blindness is general: Ostar commutes with S = A#A ----------
S = mmul(sharp(A), A)
OW4 = tuple(tuple(O_on_W(B[j])[i] for j in range(3)) for i in range(4))
# build Ostar as a 4x4 map on W extended by 0 on lambda_B line:
O4 = mmul(tuple(tuple(OW4[i][j] for j in range(3)) for i in range(4)),
          tuple((tuple(F(1 if i == j else 0) - F(1, 4) for j in range(4)))
                for i in range(3)))
# simpler: check commutation and m-equality directly on basis sweeps
comm_S = all(O_on_W(mvec(S, b)) == mvec(S, O_on_W(b)) for b in B)
gate("A13-Ostar-commutes-with-S", comm_S)
blind = all(m_of(O_on_W(mvec(A, w))) == m_of(mvec(A, O_on_W(w)))
            for w in (from_coords(c) for c in
                      itertools.product((F(-2), F(-1), F(0), F(1), F(2)), repeat=3))
            )
gate("A14-scalar-channel-blind-on-125-coord-sweep", blind)
commAO = [msub(mmul(tuple(tuple(F(0) for _ in range(4)) for _ in range(4)),
                    I4), I4)]  # placeholder unused
CAB = tuple(tuple((O_on_W(mvec(A, B[j]))[i] - mvec(A, O_on_W(B[j]))[i])
            for j in range(3)) for i in range(4))
gate("A15-commutator-nonzero-rank-2", rank(CAB) == 2)

# ---------- the R_cyc leg: cyclotomic arithmetic from scratch ----------
# K = Q[z]/Phi_5. elements = 4-tuples in basis B0 = (1, z, z^2, z^3).
def kred(c5):  # reduce z^4 = -1 - z - z^2 - z^3
    c = list(c5[:4])
    for i in range(4): c[i] -= c5[4] if len(c5) > 4 else 0
    return tuple(c)
def kmul(a, b):
    c = [F(0)]*7
    for i in range(4):
        for j in range(4):
            c[i+j] += a[i]*b[j]
    # reduce degrees 6,5,4 using z^4 = -(1+z+z^2+z^3)
    for d in (6, 5, 4):
        co = c[d]
        if co:
            c[d] = F(0)
            for k in range(d-4, d):
                c[k] -= co
    return tuple(c[:4])
def sigma(a, s):  # z -> z^s
    out = [F(0)]*4
    for i in range(4):
        e = (i*s) % 5
        if e == 4:
            for k in range(4): out[k] -= a[i]
        else:
            out[e] += a[i]
    return tuple(out)
def ktr(a):
    return sum(sigma(a, s)[0]*1 for s in (1, 2, 3, 4)) if False else \
        4*a[0] - a[1] - a[2] - a[3]   # Tr(1)=4, Tr(z^i)=-1
def pair_tr(a, b):  # <a,b>_tr = (1/5) Tr(a sigma_4(b))
    return F(1, 5)*ktr(kmul(a, sigma(b, 4)))

def iota(v): return tuple(v)              # B0 coordinates ARE the K element
ok_bridge = True
for w4 in list(itertools.islice(
        (t for t in itertools.product((F(-2), F(-1), F(0), F(1), F(2)), repeat=4)
         if any(c != 0 for c in t)), 0, None, 1)):
    wK = iota(w4)
    if pair_tr(wK, wK) != m_of(w4): ok_bridge = False; break
    # MATRIX_B0(T_w) with T_w(x) = w <x,w>_tr : column j = <e_j, w>_tr * w
    Tw = tuple(tuple(pair_tr(tuple(F(1 if t == j else 0) for t in range(4)), wK)*wK[i]
               for j in range(4)) for i in range(4))
    if Tw != mmul(outer(w4, w4), G): ok_bridge = False; break
gate("A16-Rcyc-fields-equal-m-and-vvTG-on-624-sweep", ok_bridge)
gate("A17-witness-Rcyc-total-and-density",
     pair_tr(iota(xL), iota(xL)) == F(3, 4)
     and pair_tr(iota(xR), iota(xR)) == F(3, 4)
     and smul(F(1)/F(3, 4), mmul(outer(xL, xL), G)) == rL_stated
     and smul(F(1)/F(3, 4), mmul(outer(xR, xR), G)) == rR_stated)

print()
print("FINDINGS %d" % len(FIND))
if FIND:
    print("BROKEN: " + ", ".join(FIND)); sys.exit(2)
print("AUDIT VERDICT: the posted synthesis computations withstand the "
      "independent pass")
sys.exit(0)
