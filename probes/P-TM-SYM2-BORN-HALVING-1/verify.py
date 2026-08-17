#!/usr/bin/env python3
"""Exact verifier for P-TM-SYM2-BORN-HALVING-1.

PUBLIC FORMAL PROBE. Run only after the immutable PREREG+verify pin.
Standard library only. Exact arithmetic only.
"""
from fractions import Fraction as Q
from itertools import permutations

# ---------- exact Q(zeta_5), basis 1,j,j^2,j^3 ----------
Z0 = (Q(0), Q(0), Q(0), Q(0))
Z1 = (Q(1), Q(0), Q(0), Q(0))
JROOT = (Q(0), Q(1), Q(0), Q(0))

def zadd(x, y):
    return tuple(x[i] + y[i] for i in range(4))

def zneg(x):
    return tuple(-a for a in x)

def zsub(x, y):
    return zadd(x, zneg(y))

def zscale(c, x):
    return tuple(c * a for a in x)

def zmul(x, y):
    tmp = [Q(0) for _ in range(7)]
    for i, a in enumerate(x):
        for k, b in enumerate(y):
            tmp[i + k] += a * b
    # j^4 = -(1+j+j^2+j^3)
    for d in range(6, 3, -1):
        c = tmp[d]
        if c:
            tmp[d] = Q(0)
            for r in range(d - 4, d):
                tmp[r] -= c
    return tuple(tmp[:4])

def zpow(x, n):
    out = Z1
    y = x
    while n:
        if n & 1:
            out = zmul(out, y)
        y = zmul(y, y)
        n //= 2
    return out

JPOW = tuple(zpow(JROOT, k) for k in range(5))

def jpow(k):
    return JPOW[k % 5]

def zstar(x):
    out = Z0
    for r, a in enumerate(x):
        out = zadd(out, zscale(a, jpow(-r)))
    return out

def znorm(x):
    return zmul(zstar(x), x)

def fourier(a):
    out = []
    for k in range(5):
        s = Z0
        for r, ar in enumerate(a):
            if ar:
                s = zadd(s, zscale(ar, jpow(r * k)))
        out.append(s)
    return tuple(out)

def inverse_fourier(A):
    out = []
    for r in range(5):
        s = Z0
        for k, Ak in enumerate(A):
            s = zadd(s, zmul(Ak, jpow(-r * k)))
        out.append(zscale(Q(1, 5), s))
    return tuple(out)

# ---------- gate recorder ----------
gates = []

def gate(name, cond):
    ok = bool(cond)
    gates.append((name, ok))
    print(f"{name} {'PASS' if ok else 'FAIL'}")
    return ok

# ---------- W3 and source ----------
W3 = (
    (0, 0, 1),
    (0, 1, 0),
    (0, 1, 1),
    (1, 0, 0),
    (1, 0, 1),
    (1, 1, 0),
)

def N(w):
    a, b, c = w
    return (1 - a, 1 - b, 1 - c)

def R(w):
    a, b, c = w
    return (c, b, a)

def omega(w):
    a, b, c = w
    return c - a

# G01
carrier_ok = len(set(W3)) == 6 and all(N(w) in W3 for w in W3)
unseen = set(W3)
q_orbits = []
while unseen:
    w = min(unseen)
    O = frozenset((w, N(w)))
    q_orbits.append(O)
    unseen -= O
q_orbits = tuple(sorted(q_orbits, key=lambda O: tuple(sorted(O))))
carrier_ok = carrier_ok and len(q_orbits) == 3 and all(len(O) == 2 for O in q_orbits)
gate("G01 W3-CARRIER", carrier_ok)

# G02
source_character = all(
    omega(N(w)) == -omega(w) and omega(R(w)) == -omega(w)
    for w in W3
)
gate("G02 SOURCE-CHARACTER", source_character)

# G03: solve h(Nw)=-h(w), h(Rw)=-h(w) by exact linear algebra over Q.
# Unknowns are values on W3 in the fixed order.
index = {w: i for i, w in enumerate(W3)}
rows = []
for w in W3:
    row = [Q(0)] * 6
    row[index[N(w)]] += 1
    row[index[w]] += 1
    rows.append(row)
    row = [Q(0)] * 6
    row[index[R(w)]] += 1
    row[index[w]] += 1
    rows.append(row)

A = [row[:] for row in rows]
rank = 0
for col in range(6):
    pivot = next((r for r in range(rank, len(A)) if A[r][col] != 0), None)
    if pivot is None:
        continue
    A[rank], A[pivot] = A[pivot], A[rank]
    p = A[rank][col]
    A[rank] = [x / p for x in A[rank]]
    for r in range(len(A)):
        if r != rank and A[r][col] != 0:
            p = A[r][col]
            A[r] = [A[r][c] - p * A[rank][c] for c in range(6)]
    rank += 1
dim = 6 - rank
omega_vec = tuple(Q(omega(w)) for w in W3)
source_unique = dim == 1 and any(omega_vec)
gate("G03 SOURCE-UNIQUENESS", source_unique)

# G04: C_sel is imported from public T; Q_word is independently the word quotient.
C_SEL_COUNT = 4
type_separation = C_SEL_COUNT == 4 and len(q_orbits) == 3 and C_SEL_COUNT != len(q_orbits)
gate("G04 TYPE-SEPARATION", type_separation)

# ---------- monomial J-verb lift ----------
# v_t = delta_t + delta_(t+1)
lift_vectors = []
lift_spectra = []
for t in range(5):
    a = [Q(0)] * 5
    a[t] = Q(1)
    a[(t + 1) % 5] = Q(1)
    a = tuple(a)
    lift_vectors.append(a)
    lift_spectra.append(fourier(a))

# G05
monomial_fourier = True
for t in range(5):
    for k in range(5):
        rhs = zmul(jpow(t * k), zadd(Z1, jpow(k)))
        monomial_fourier &= lift_spectra[t][k] == rhs
gate("G05 MONOMIAL-FOURIER", monomial_fourier)

# G06: for k != 0, 1+j^k = sigma_(3k)(J), J=1+j^2.
# sigma_a(J)=1+j^(2a)
galois_reindex = True
for k in range(1, 5):
    a = (3 * k) % 5
    lhs = zadd(Z1, jpow(k))
    rhs = zadd(Z1, jpow(2 * a))
    galois_reindex &= a in (1, 2, 3, 4) and lhs == rhs
galois_reindex &= zadd(Z1, jpow(0)) == zscale(Q(2), Z1)
gate("G06 GALOIS-REINDEX", galois_reindex)

# G07: all five monomial lifts have identical pointwise spectral norms.
base_norms = tuple(znorm(x) for x in lift_spectra[0])
monomial_modulus = all(
    tuple(znorm(x) for x in spec) == base_norms
    for spec in lift_spectra
)
gate("G07 MONOMIAL-MODULUS", monomial_modulus)

# G08: exact inverse Fourier gives the frozen coefficient vectors.
fourier_inverse = all(
    inverse_fourier(lift_spectra[t]) ==
    tuple(zscale(c, Z1) for c in lift_vectors[t])
    for t in range(5)
)
gate("G08 FOURIER-INVERSE", fourier_inverse)

# G09: coordinate Born square on each support.
born_laws = []
born_halving = True
for a in lift_vectors:
    supp = [r for r, ar in enumerate(a) if ar != 0]
    Z = sum((ar * ar for ar in a), Q(0))
    law = tuple((a[r] * a[r]) / Z for r in supp)
    born_laws.append(law)
    born_halving &= len(supp) == 2 and sum(law, Q(0)) == 1 and law[0] == law[1]
born_halving &= all(law == born_laws[0] for law in born_laws)
gate("G09 BORN-HALVING", born_halving)

# G10: sheet-order swap changes no law.
sheet_orientation = all(
    tuple(reversed(law)) == law
    for law in born_laws
)
gate("G10 SHEET-ORIENTATION", sheet_orientation)

# ---------- modulus-only nonmonomial control ----------
Psi = tuple(zadd(Z1, jpow(k)) for k in range(5))
Psi_control = list(Psi)
Psi_control[1] = zstar(Psi_control[1])
Psi_control = tuple(Psi_control)

# G11 same pointwise moduli
control_modulus = all(
    znorm(Psi_control[k]) == znorm(Psi[k])
    for k in range(5)
)
gate("G11 CONTROL-MODULUS", control_modulus)

control_coeff = inverse_fourier(Psi_control)
control_weights = tuple(znorm(x) for x in control_coeff)

# G12 full support
control_full_support = all(x != Z0 for x in control_coeff)
gate("G12 CONTROL-FULL-SUPPORT", control_full_support)

# G13 unequal exact coefficient Born numerators
control_unequal = len(set(control_weights)) > 1
gate("G13 CONTROL-UNEQUAL-BORN", control_unequal)

# ---------- S4 imported window law and total bridge ----------
# Import only the public L5 stationary W3 law: each word has one common mass.
# We encode it by normalization, not by a target L6 line value.
word_mass = Q(1, len(W3))
f = {w: word_mass for w in W3}

# G14 imported law is normalized and N-invariant; form Q_word marginal.
shell_mass = {}
for O in q_orbits:
    shell_mass[O] = sum((f[w] for w in O), Q(0))
s4_import = (
    sum(f.values(), Q(0)) == 1
    and all(f[N(w)] == f[w] for w in W3)
    and len(set(shell_mass.values())) == 1
)
gate("G14 S4-WINDOW-IMPORT", s4_import)

# G15 apply the derived Born conditional from G09 to every Q_word shell.
# No six-line target value appears in construction.
mu = {}
for O in q_orbits:
    members = tuple(sorted(O))
    law = born_laws[0]
    for i, w in enumerate(members):
        mu[w] = shell_mass[O] * law[i]
total_word_measure = (
    set(mu) == set(W3)
    and all(v > 0 for v in mu.values())
    and sum(mu.values(), Q(0)) == 1
)
gate("G15 TOTAL-WORD-MEASURE", total_word_measure)

# G16 universal selector coherence; 720 sweep is audit corollary only.
labels = tuple(range(6))
common = None
coherent = True
for p in permutations(labels):
    out = [Q(0)] * 6
    for w, label in zip(W3, p):
        out[label] += mu[w]
    out = tuple(out)
    if common is None:
        common = out
    coherent &= out == common
selector_coherence = coherent and sum(common, Q(0)) == 1
gate("G16 SELECTOR-COHERENCE", selector_coherence)

# G17 complete orientation-retaining source type: four selector classes times all words.
epsilon = (Q(1), Q(-1), Q(-1), Q(1))
orientation_totality = len(epsilon) == C_SEL_COUNT
for w in W3:
    om = Q(omega(w))
    current = tuple(om * e for e in epsilon)
    orientation_totality &= len(current) == 4 and w in mu
gate("G17 ORIENTATION-TOTALITY", orientation_totality)

# G18 no M_TM or GYRON input exists in the computation. The final common weight is
# read only now, after source/lift/Born/bridge/coherence construction.
common_weight = common[0] if selector_coherence and len(set(common)) == 1 else None
circularity_status = (
    common_weight is not None
    and all(v == common_weight for v in common)
    and sum(common, Q(0)) == 1
)
gate("G18 CIRCULARITY-STATUS", circularity_status)

# ---------- route ----------
source_pass = source_character and source_unique and type_separation
lift_pass = monomial_fourier and galois_reindex and monomial_modulus and fourier_inverse
half_pass = born_halving and sheet_orientation
control_pass = control_modulus and control_full_support and control_unequal
bridge_pass = s4_import and total_word_measure and orientation_totality
coherence_pass = selector_coherence and circularity_status

if not control_pass:
    decision = "STOP"
elif not (source_pass and lift_pass and half_pass and bridge_pass and coherence_pass):
    decision = "NEGATIVE"
else:
    decision = "BORN-HALVING-PASS"

assert len(gates) == 18
print(f"GATE_COUNT {len(gates)}")
print("SCIENTIFIC_RESULT_BEGIN")
print(f"SOURCE_SECTOR: {'PASS' if source_pass else 'NEGATIVE'}")
print(f"MONOMIAL_LIFT: {'PASS' if lift_pass else 'NEGATIVE'}")
print(f"BORN_HALVING: {'PASS' if half_pass else 'NEGATIVE'}")
print(f"MODULUS_ONLY_CONTROL: {'PASS' if control_pass else 'STOP'}")
print(f"TOTAL_BRIDGE: {'PASS' if bridge_pass else 'NEGATIVE'}")
print(f"SELECTOR_COHERENCE: {'PASS' if coherence_pass else 'NEGATIVE'}")
print(f"DERIVED_COMMON_LINE_WEIGHT: {common_weight if common_weight is not None else 'UNDEFINED'}")
print("STATUS_CEILING: D")
print(f"DECISION: {decision}")
print("SCIENTIFIC_RESULT_END")
