# C-U-NONLINEAR-TWO-MESSAGE-READOUT-N finite audit. NON-CANONICAL / L1.
# U transcribed from canon/CANON.md native conventions: x=(p1,p4,p1p,p4p,q,r)
# written here as (a,b,c,d,q,r); (g0..g4)=(a,b,c,d,e); selector g_(z+2*theta_n).
import itertools

M = 5

def ga(x):
    a, b, c, d, q, r = x
    return (b, a, d, c, q, r)

def gb(x):
    return tuple((-v) % M for v in (x[2], x[3], x[0], x[1], x[4], x[5]))

def gc(x):
    a, b, c, d, q, r = x
    return ((2 - c) % M, (1 - d + r) % M, (2 - a) % M,
            (1 - b - r) % M, (1 - q) % M, (-r) % M)

def gd(x):
    a, b, c, d, q, r = x
    return ((2 - a) % M, (1 - b) % M, (3 - c) % M,
            (4 - d) % M, (1 - q) % M, (1 - r) % M)

def ge(x):
    a, b, c, d, q, r = x
    return ((2 - a) % M, (1 - b) % M, (3 - c) % M,
            (4 - d) % M, (2 - q) % M, (1 - r) % M)

GENS = [ga, gb, gc, gd, ge]

def z(x):
    return sum(x) % M

def theta(n):
    return bin(n).count("1") % 2

def step(n, x):
    return GENS[(z(x) + 2 * theta(n)) % M](x)

def A(x):
    return (x[0] + x[2]) % M

def C(x):
    return (x[0] - x[2] - 2) % M

def D(x):
    return (x[1] - x[3] - 1) % M

def tau(zz, aa):
    return (zz * aa ** 3 + 1 - aa ** 4) % M

def T(x):
    zz = z(x)
    if zz == 0:
        return C(x)
    if zz == 2:
        return x[4]
    if zz in (1, 4):
        return tau(zz, A(x)) * D(x) % M
    return D(x)

def R(x):
    return (z(x), T(x))

def psi(x):
    return (C(x) * (1 - z(x) ** 2) + A(x) * z(x) * D(x)) % M

def prep(lam, mu):
    return (3 * (lam + 3) % M, 3 * (mu + 1) % M, 3 * (-lam - 1) % M,
            3 * (-mu - 1) % M, 0, 1)

def check(cond, msg):
    if not cond:
        raise AssertionError(msg)

ALL = list(itertools.product(range(M), repeat=6))
BLANK = -1

# 1. Transcription cross-check: Canon (z,q,r) quotient table for every
# generator, on every one of the 15625 states.
QUOT = [
    lambda zz, q, r: (zz, q, r),
    lambda zz, q, r: (-zz % M, -q % M, -r % M),
    lambda zz, q, r: ((2 - zz) % M, (1 - q) % M, -r % M),
    lambda zz, q, r: ((2 - zz) % M, (1 - q) % M, (1 - r) % M),
    lambda zz, q, r: ((3 - zz) % M, (2 - q) % M, (1 - r) % M),
]
for x in ALL:
    for gi, g in enumerate(GENS):
        y = g(x)
        check((z(y), y[4], y[5]) == QUOT[gi](z(x), x[4], x[5]),
              "quotient table mismatch")

# 2. Preparations: identities, affine parametrization, common word, reset.
P0 = prep(0, 0)
VL = tuple((prep(1, 0)[i] - P0[i]) % M for i in range(6))
VM = tuple((prep(0, 1)[i] - P0[i]) % M for i in range(6))
check(VL == (3, 0, 2, 0, 0, 0) and VM == (0, 3, 0, 2, 0, 0), "directions")
for lam in range(M):
    for mu in range(M):
        x = prep(lam, mu)
        check(x == tuple((P0[i] + lam * VL[i] + mu * VM[i]) % M
                          for i in range(6)), "prep not affine in messages")
        check(A(x) == 1 and C(x) == lam and D(x) == mu and z(x) == 2,
              "prep identities")
        xs = [x]
        for n in range(3):
            xs.append(step(n, xs[-1]))
        check(xs[1] == (3 * lam % M, 3 * mu % M, (2 * lam + 3) % M,
                        (2 * mu + 2) % M, 1, 4), "x1 formula")
        check(xs[2] == xs[0], "full checkpoint reset x2=x0")
        check(xs[3] == ge(xs[0]) == ((2 * lam + 3) % M, (2 * mu + 3) % M,
              (3 * lam + 1) % M, (3 * mu + 2) % M, 2, 0), "x3 formula")
        check([z(v) for v in xs] == [2, 0, 2, 1], "z sequence")
        check(A(xs[3]) == 4 and D(xs[3]) == 4 * mu % M, "x3 A,D")
        check(R(xs[0]) == (2, 0) and R(xs[1]) == (0, lam)
              and R(xs[2]) == (2, 0) and R(xs[3]) == (1, mu), "R table")

# 3. Sector lemmas, exhaustive: closure of X14 under both selector bits,
# A -> -A, invariance of I = zD/A where A != 0. The sector alone does not
# give A != 0 (1250 counterexamples); the trajectories give it via A(x3)=4.
count_a0 = 0
for x in ALL:
    if z(x) not in (1, 4):
        continue
    if A(x) == 0:
        count_a0 += 1
    for t in (0, 1):
        y = GENS[(z(x) + 2 * t) % M](x)
        check(z(y) in (1, 4), "X14 not closed")
        check(A(y) == (-A(x)) % M, "A not negated on X14")
        if A(x) != 0:
            check((z(y) * D(y) * pow(A(y), -1, M)
                   - z(x) * D(x) * pow(A(x), -1, M)) % M == 0,
                  "I not invariant")
check(count_a0 == 1250, "A=0 sector count")
for zz in (1, 4):
    for aa in range(M):
        check(tau(zz, aa) != 0, "tau vanishes")
check(all(tau(zz, aa) == zz * pow(aa, -1, M) % M
          for zz in range(M) for aa in range(1, M)), "tau != z/A")
check(all(tau(zz, 0) == 1 for zz in range(M)), "tau(A=0)")

# 4. Exact required set: n=0,1,2 points plus the all-words sector closure
# from each x3. This set contains every actual orbit point (step 5 shows
# the actual Thue-Morse word also visits all of it, by n=32).
def sector_reach(x3):
    seen = {x3}
    frontier = [x3]
    while frontier:
        nxt = []
        for x in frontier:
            for t in (0, 1):
                y = GENS[(z(x) + 2 * t) % M](x)
                if y not in seen:
                    seen.add(y)
                    nxt.append(y)
        frontier = nxt
    return seen

REQ = {}
def require(pt, label):
    check(REQ.get(pt, label) == label, "full-state label conflict")
    REQ[pt] = label

SECTORS = {}
for lam in range(M):
    for mu in range(M):
        x = prep(lam, mu)
        pts = [x]
        for n in range(3):
            pts.append(step(n, pts[-1]))
        require(pts[0], BLANK)
        require(pts[1], lam)
        require(pts[2], BLANK)
        sec = sector_reach(pts[3])
        check(len(sec) == 20, "sector size")
        check(all(A(p) * A(p) % M == 1 for p in sec), "A^2 != 1 on sector")
        SECTORS[(lam, mu)] = sec
        for p in sec:
            require(p, mu)
check(len(REQ) == 550, "required set size")

# 5. Both readers realize every label on the required set, and the actual
# U word visits exactly the required points.
for p, lab in REQ.items():
    check((z(p) == 2) == (lab == BLANK), "blank marker z=2")
    if lab != BLANK:
        check(T(p) == lab, "piecewise T value")
        check(psi(p) == lab, "cubic psi value")
for lam in range(M):
    for mu in range(M):
        x = prep(lam, mu)
        visited = set()
        for n in range(2000):
            lab = BLANK if n in (0, 2) else (lam if n == 1 else mu)
            check(REQ.get(x) == lab, "actual orbit leaves required set")
            if n >= 3:
                visited.add(x)
            x = step(n, x)
        check(visited == SECTORS[(lam, mu)], "sector not fully visited")

# 6. (z,T) extends to a global bijective coordinate change of F5^6
# (auditor's explicit completion, piecewise in z like T itself).
def phi(x):
    zz = z(x)
    y5 = D(x) if zz == 0 else C(x)
    y6 = D(x) if zz == 2 else x[4]
    return (zz, T(x), A(x), (x[1] + x[3]) % M, y5, y6)

check(len({phi(x) for x in ALL}) == M ** 6, "completion not bijective")

# 7. Affine boundary facts. The written proof uses: linear part of c fixes
# both message directions; linear part of e is -I. An explicit affine map
# into F5^3 (rows below, ignores coordinate c) separates all six labels.
def linpart(g, v):
    gv = g(v)
    g0 = g((0,) * 6)
    return tuple((gv[i] - g0[i]) % M for i in range(6))

check(linpart(gc, VL) == VL and linpart(gc, VM) == VM, "c moves direction")
for i in range(6):
    ei = tuple(1 if j == i else 0 for j in range(6))
    check(linpart(ge, ei) == tuple((-v) % M for v in ei), "e linear != -I")

MROWS = [(0, 2, 0, 1, 0, 0), (3, 0, 0, 0, 1, 0), (2, 3, 0, 0, 0, 1)]
def mmap(p):
    return tuple(sum(row[i] * p[i] for i in range(6)) % M for row in MROWS)

images = {}
for p, lab in REQ.items():
    v = mmap(p)
    check(images.get(v, lab) == lab, "affine F5^3 label collision")
    images[v] = lab
check(len(images) == 125, "affine image count")

# 8. Polynomial degree inside two named exact-message codes, by exact
# linear algebra over F5: no degree <=2 message polynomial in either code;
# degree 3 exists (also given in closed form by psi in step 5). A general
# quadratic pair with an arbitrary decoder is not decided here.
def monomials_le(nvars, deg):
    out = []
    for total in range(deg + 1):
        for ex in itertools.combinations_with_replacement(range(nvars), total):
            e = [0] * nvars
            for v in ex:
                e[v] += 1
            out.append(tuple(e))
    return out

def design(points, exps):
    rows = []
    for p in points:
        row = []
        for e in exps:
            val = 1
            for k, ee in enumerate(e):
                if ee:
                    val = val * pow(p[k], ee, M) % M
            row.append(val)
        rows.append(row)
    return rows

def consistent(rows, rhs):
    aug = [row[:] + [b % M] for row, b in zip(rows, rhs)]
    nvar = len(rows[0])
    r = 0
    for c in range(nvar):
        piv = None
        for i in range(r, len(aug)):
            if aug[i][c] % M:
                piv = i
                break
        if piv is None:
            continue
        aug[r], aug[piv] = aug[piv], aug[r]
        inv = pow(aug[r][c], -1, M)
        aug[r] = [v * inv % M for v in aug[r]]
        for i in range(len(aug)):
            if i != r and aug[i][c] % M:
                f = aug[i][c]
                aug[i] = [(aug[i][j] - f * aug[r][j]) % M
                          for j in range(nvar + 1)]
        r += 1
        if r >= len(aug):
            break
    return all(any(aug[i][c] % M for c in range(nvar))
               or aug[i][nvar] % M == 0 for i in range(len(aug)))

present_pts = [p for p, lab in REQ.items() if lab != BLANK]
present_lab = [lab for lab in REQ.values() if lab != BLANK]
all_pts = list(REQ.keys())
code_marker = [0 if lab == BLANK else 1 for lab in REQ.values()]
code_msg = [0 if lab == BLANK else lab for lab in REQ.values()]
for deg, exp_present, exp_marker, exp_msg in ((2, False, True, False),
                                              (3, True, True, True)):
    exps = monomials_le(6, deg)
    check(consistent(design(present_pts, exps), present_lab) == exp_present,
          f"degree {deg} (z,psi) code feasibility")
    dall = design(all_pts, exps)
    check(consistent(dall, code_marker) == exp_marker,
          f"degree {deg} marker feasibility")
    check(consistent(dall, code_msg) == exp_msg,
          f"degree {deg} pair-code message feasibility")

# 9. Coordinate-access classification on the exact required set, with the
# canonical receiver-block witness pair at actual time n=1.
def subset_consistent(idx):
    seen = {}
    for p, lab in REQ.items():
        key = tuple(p[i] for i in idx)
        if seen.get(key, lab) != lab:
            return False
        seen[key] = lab
    return True

good = [idx for r in range(7)
        for idx in itertools.combinations(range(6), r)
        if subset_consistent(idx)]
check(good == [(0, 1, 2, 4, 5), (0, 1, 3, 4, 5), (0, 2, 3, 4, 5),
               (1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)],
      "access classification")
w0 = step(0, prep(0, 0))
w1 = step(0, prep(1, 0))
check(tuple(w0[i] for i in (1, 3, 4, 5)) == tuple(w1[i] for i in (1, 3, 4, 5))
      == (0, 2, 1, 4), "receiver-block witness values")
check(REQ[w0] == 0 and REQ[w1] == 1, "receiver-block witness labels")

print("PASS C-U-NONLINEAR-TWO-MESSAGE-READOUT-N states=15625 pairs=25 "
      "required=550 sector_per_pair=20 affine_dim=3 cubic_degree=3 "
      "minimal_access=5")
