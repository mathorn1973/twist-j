#!/usr/bin/env python3
"""PUBLIC / NON-CANONICAL independent exact challenge; action layer L1.

Written from the frozen PREREG.md and public definitions, without reading
verify.py, PROOF.md, builder calculations, or scientific stdout. Targets were
exposed in the assignment. This is implementation independence, not discovery
independence. No scientific execution preceded the joint public source pin.

Only the standard library is used. Finite controls audit identities and
explicit obstructions; they are not a substitute for the all-C proof.

The universal argument being challenged is short: completing the square makes
H positive definite precisely when C^t C < 4I. A bounded integral orbit is
finite; the finitely many standard-basis orbits then give a common period for
T. On a singular two-plane, T has characteristic polynomial
u^2-(2-lambda)u+1. At lambda=4 its nontrivial Jordan block is unbounded;
above 4 an eigenvalue has modulus greater than one. If all integer basis
orbits were bounded, every real orbit would be bounded, contradicting either
block. Kernels are fixed, including empty and rank-deficient cases. This
uses a real decomposition only, never an integral direct-sum assumption.
"""

from fractions import Fraction
from itertools import combinations, product
from math import gcd


def require(condition, label):
    if not condition:
        raise AssertionError(label)


def identity(n):
    return tuple(tuple(int(i == j) for j in range(n)) for i in range(n))


def zero(m, n):
    return tuple(tuple(0 for _ in range(n)) for _ in range(m))


def transpose(a):
    return tuple(zip(*a))


def plus(a, b):
    return tuple(tuple(x + y for x, y in zip(r, s)) for r, s in zip(a, b))


def times(k, a):
    return tuple(tuple(k * x for x in r) for r in a)


def minus(a, b):
    return plus(a, times(-1, b))


def multiply(a, b):
    return tuple(tuple(sum(x * y for x, y in zip(r, s))
                       for s in transpose(b)) for r in a)


def apply(a, x):
    return tuple(sum(p * q for p, q in zip(r, x)) for r in a)


def dot(x, y):
    return sum(p * q for p, q in zip(x, y))


def unit(n, i):
    return tuple(int(j == i) for j in range(n))


def columns(vectors, rows):
    return tuple(tuple(v[i] for v in vectors) for i in range(rows))


def operator_from_step(fn, n):
    return columns([fn(unit(n, i)) for i in range(n)], n)


def power(a, n):
    answer = identity(len(a))
    for _ in range(n):
        answer = multiply(answer, a)
    return answer


def polynomial(a, coefficients):
    """Coefficients are listed in ascending powers."""
    result = zero(len(a), len(a))
    for k, coefficient in enumerate(coefficients):
        result = plus(result, times(coefficient, power(a, k)))
    return result


def determinant(a):
    n = len(a)
    work = [[Fraction(x) for x in row] for row in a]
    result = Fraction(1)
    for j in range(n):
        pivot = next((i for i in range(j, n) if work[i][j]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != j:
            work[j], work[pivot] = work[pivot], work[j]
            result = -result
        value = work[j][j]
        result *= value
        for i in range(j + 1, n):
            ratio = work[i][j] / value
            for k in range(j, n):
                work[i][k] -= ratio * work[j][k]
    return result


def inverse(a):
    n = len(a)
    work = [[Fraction(x) for x in a[i] + identity(n)[i]] for i in range(n)]
    for j in range(n):
        pivot = next((i for i in range(j, n) if work[i][j]), None)
        require(pivot is not None, "inverse requires full rank")
        work[j], work[pivot] = work[pivot], work[j]
        value = work[j][j]
        work[j] = [x / value for x in work[j]]
        for i in range(n):
            if i != j:
                ratio = work[i][j]
                work[i] = [x - ratio * y for x, y in zip(work[i], work[j])]
    return tuple(tuple(row[n:]) for row in work)


def reduced_rows(a, modulus=None):
    work = [[Fraction(x) if modulus is None else int(x) % modulus
             for x in row] for row in a]
    row_index = 0
    pivots = []
    for j in range(len(work[0]) if work else 0):
        pivot = next((i for i in range(row_index, len(work)) if work[i][j]), None)
        if pivot is None:
            continue
        work[row_index], work[pivot] = work[pivot], work[row_index]
        value = work[row_index][j]
        multiplier = 1 / value if modulus is None else pow(value, -1, modulus)
        work[row_index] = [x * multiplier for x in work[row_index]]
        if modulus is not None:
            work[row_index] = [x % modulus for x in work[row_index]]
        for i in range(len(work)):
            if i != row_index:
                ratio = work[i][j]
                work[i] = [x - ratio * y for x, y in zip(work[i], work[row_index])]
                if modulus is not None:
                    work[i] = [x % modulus for x in work[i]]
        pivots.append(j)
        row_index += 1
        if row_index == len(work):
            break
    return tuple(tuple(row) for row in work[:row_index]), tuple(pivots)


def rank(a):
    return len(reduced_rows(a)[1])


def integral(a):
    return all(Fraction(x).denominator == 1 for row in a for x in row)


def characteristic(a):
    """Newton identities, output in descending powers."""
    n = len(a)
    traces = [None] + [sum(power(a, k)[i][i] for i in range(n))
                       for k in range(1, n + 1)]
    coefficients = [Fraction(1)]
    for k in range(1, n + 1):
        coefficients.append(-sum(coefficients[k - j] * traces[j]
                                 for j in range(1, k + 1)) / k)
    return tuple(coefficients)


def determinantal_divisors(a):
    values = [1]
    for size in range(1, len(a) + 1):
        common = 0
        for rr in combinations(range(len(a)), size):
            for cc in combinations(range(len(a)), size):
                minor = tuple(tuple(a[i][j] for j in cc) for i in rr)
                value = determinant(minor)
                require(value.denominator == 1, "integer minor")
                common = gcd(common, abs(value.numerator))
        values.append(common)
    return tuple(values)


def column_hermite(a):
    """Return H,V with A V=H; only unimodular column operations are used."""
    n = len(a)
    h = [list(row) for row in a]
    v = [list(row) for row in identity(n)]

    def swap(i, j):
        for matrix in (h, v):
            for row in matrix:
                row[i], row[j] = row[j], row[i]

    def subtract(j, i, q):
        for matrix in (h, v):
            for row in matrix:
                row[j] -= q * row[i]

    for i in reversed(range(n)):
        if not h[i][i]:
            pivot = next((j for j in range(i) if h[i][j]), None)
            require(pivot is not None, "Hermite full-rank pivot")
            swap(i, pivot)
        for j in range(i):
            while h[i][j]:
                q = h[i][j] // h[i][i]
                subtract(j, i, q)
                if h[i][j]:
                    swap(i, j)
        if h[i][i] < 0:
            for matrix in (h, v):
                for row in matrix:
                    row[i] = -row[i]
        for j in range(i + 1, n):
            subtract(j, i, h[i][j] // h[i][i])
    return tuple(tuple(row) for row in h), tuple(tuple(row) for row in v)


def forward(c, f, state):
    e = len(c)
    electric, magnetic = state[:e], state[e:]
    updated_e = tuple(electric[i] + sum(c[i][j] * magnetic[j] for j in range(f))
                      for i in range(e))
    updated_m = tuple(magnetic[j] - sum(c[i][j] * updated_e[i] for i in range(e))
                      for j in range(f))
    return updated_e + updated_m


def backward(c, f, state):
    e = len(c)
    electric, magnetic = state[:e], state[e:]
    old_m = tuple(magnetic[j] + sum(c[i][j] * electric[i] for i in range(e))
                  for j in range(f))
    old_e = tuple(electric[i] - sum(c[i][j] * old_m[j] for j in range(f))
                  for i in range(e))
    return old_e + old_m


def reversal(c, f, state):
    e = len(c)
    electric, magnetic = state[:e], state[e:]
    return (tuple(electric[i] + sum(c[i][j] * magnetic[j] for j in range(f))
                  for i in range(e)) + tuple(-x for x in magnetic))


def energy(c, f, state):
    e = len(c)
    electric, magnetic = state[:e], state[e:]
    return (dot(electric, electric) + dot(magnetic, magnetic)
            + sum(electric[i] * c[i][j] * magnetic[j]
                  for i in range(e) for j in range(f)))


def polarization(fn, n):
    return tuple(tuple(2 * fn(unit(n, i)) if i == j else
                       fn(tuple(x + y for x, y in zip(unit(n, i), unit(n, j))))
                       - fn(unit(n, i)) - fn(unit(n, j))
                       for j in range(n)) for i in range(n))


def show(label, value):
    def spelling(x):
        if isinstance(x, (tuple, list)):
            return "[" + ",".join(spelling(y) for y in x) + "]"
        return str(x)
    print(label + "=" + spelling(value))


def raw_audit(c, f, label, order=None):
    n = len(c) + f
    t = operator_from_step(lambda x: forward(c, f, x), n)
    ti = operator_from_step(lambda x: backward(c, f, x), n)
    r = operator_from_step(lambda x: reversal(c, f, x), n)
    b = polarization(lambda x: energy(c, f, x), n)
    require(multiply(t, ti) == identity(n) == multiply(ti, t), label + " inverse")
    require(multiply(transpose(t), multiply(b, t)) == b, label + " energy")
    require(power(r, 2) == identity(n), label + " R involution")
    require(multiply(r, multiply(t, r)) == ti, label + " RTR")
    require(multiply(transpose(r), multiply(b, r)) == b, label + " R energy")
    if order is not None:
        require(power(t, order) == identity(n), label + " finite order")
        require(all(power(t, k) != identity(n) for k in range(1, order)),
                label + " exact order")
    show("control." + label, "passed")
    return t, ti, b


def critical_control():
    c = ((1, 1), (1, 0), (1, 0), (0, 1), (0, 1))
    t, _, _ = raw_audit(c, 2, "Ccrit")
    v = (1, 1)
    cv = apply(c, v)
    require(apply(transpose(c), cv) == (4, 4), "critical eigenvector")
    state = (0, 0, 0, 0, 0, 1, 1)
    for n in range(13):
        predicted = (tuple((-1) ** (n + 1) * n * z for z in cv)
                     + tuple((-1) ** n * (2 * n + 1) * z for z in v))
        require(state == predicted, "critical formula n=" + str(n))
        require(energy(c, 2, state) == 2, "critical H=2 n=" + str(n))
        if n < 12:
            state = apply(t, state)
    show("critical.formula_n_0_to_12", "passed; all-n proof uses C^t C v=4v")
    for sign in (-1, 1):
        gram = ((3, sign), (sign, 3))
        require(characteristic(gram) == (1, -6, 8), "adjacent signed triangles")
    show("adjacent_ordinary_signed_triangles", "Gram roots 2,4; outside strict window")


def main():
    print("C-FIELD-CYCLOTOMIC-WINDOW-N independent challenge; NON-CANONICAL L1")
    print("Source: frozen preregistration/public definitions only; targets exposed")
    raw_audit(((0, 0, 0), (0, 0, 0)), 3, "zero_2_by_3", 1)
    raw_audit(((1,), (0,)), 1, "rectangular_2_by_1", 6)
    raw_audit(((1, 0), (0, 0)), 2, "rank_deficient", 6)
    raw_audit((), 0, "empty_0_by_0", 1)
    raw_audit((), 3, "empty_0_by_3", 1)
    raw_audit(((), ()), 0, "empty_2_by_0", 1)
    critical, _, _ = raw_audit(((2, 0), (0, 0)), 2, "critical_diag_2_0")
    jordan = minus(power(critical, 2), identity(4))
    require(jordan != zero(4, 4) and power(jordan, 2) == zero(4, 4),
            "critical nonzero nilpotent Jordan obstruction")
    unstable, _, _ = raw_audit(((3, 0), (0, 0)), 2, "unstable_diag_3_0")
    require(apply(unstable, (0, 1, 0, 0)) == (0, 1, 0, 0),
            "nonzero bounded special orbit in unstable system")
    block = tuple(tuple(unstable[i][j] for j in (0, 2)) for i in (0, 2))
    require(characteristic(block) == (1, 7, 1), "unstable real reciprocal roots")
    show("unstable.special_orbit", "nonzero fixed E1; universal boundedness is essential")
    critical_control()

    # Construct the chosen incidence independently from the declared graph.
    edges = ((0, 1), (0, 1), (0, 2), (2, 1))
    d = tuple(tuple(int(tail == vertex) - int(head == vertex)
                    for tail, head in edges) for vertex in range(3))
    c = columns(((1, -1, 0, 0), (-1, 0, 1, 1)), 4)
    g = multiply(transpose(c), c)
    require(g == ((2, -1), (-1, 3)), "G5 incidence")
    require(multiply(d, c) == zero(3, 2), "actual graph boundary DC5=0")
    require(determinant(g) == 5 and determinant(minus(times(4, identity(2)), g)) == 1,
            "strict positive singular window certificates")
    require(4 - g[0][0] > 0, "4I-G Sylvester first minor")
    t, ti, raw_b = raw_audit(c, 2, "C5", 5)
    show("raw.T", t)
    show("raw.inverse", ti)
    show("graph.D", d)

    embedding = columns(tuple(tuple(c[i][j] for i in range(4)) + (0, 0)
                              for j in range(2))
                        + ((0, 0, 0, 0, 1, 0), (0, 0, 0, 0, 0, 1)), 6)
    extraction = ((0, -1, 0, 0, 0, 0), (0, 0, 1, 0, 0, 0),
                  (0, 0, 0, 0, 1, 0), (0, 0, 0, 0, 0, 1))
    require(multiply(extraction, embedding) == identity(4), "integer saturation extraction")
    phi_raw = polynomial(t, (1, 1, 1, 1, 1))
    require(multiply(phi_raw, embedding) == zero(6, 4) and rank(phi_raw) == 2,
            "active rational kernel exactly equals saturated embedding")
    unsaturated_coordinates = ((2, 0, 0, 0), (0, 1, 0, 0),
                               (0, 0, 1, 0), (0, 0, 0, 1))
    false_basis = multiply(embedding, unsaturated_coordinates)
    require(rank(false_basis) == 4 and multiply(phi_raw, false_basis) == zero(6, 4),
            "unsaturated fake basis has the same rational kernel")
    require(determinant(unsaturated_coordinates) == 2
            and apply(inverse(unsaturated_coordinates), (1, 0, 0, 0))
            == (Fraction(1, 2), 0, 0, 0),
            "unsaturated fake basis misses an explicit integer active vector")
    show("active.unsaturated_basis_control", "same rational kernel, index2, rejected")
    act = multiply(extraction, multiply(t, embedding))
    require(multiply(t, embedding) == multiply(embedding, act), "active intertwiner")
    b = polarization(lambda x: energy(c, 2, apply(embedding, x)), 4)
    require(b == multiply(transpose(embedding), multiply(raw_b, embedding)),
            "active Gram independently polarized")
    require(polynomial(act, (1, 1, 1, 1, 1)) == zero(4, 4), "active Phi5")
    require(power(act, 5) == identity(4) and act != identity(4), "active exact prime order")
    require(characteristic(act) == (1, 1, 1, 1, 1), "active characteristic")
    show("active.embedding", embedding)
    show("active.extraction", extraction)
    show("active.T", act)
    show("active.B", b)

    seed = (0, 0, 1, 0)
    module = columns([apply(power(act, n), seed) for n in range(4)], 4)
    module_inverse = inverse(module)
    require(abs(determinant(module)) == 1 and integral(module_inverse),
            "chosen cyclic seed is a full integral module basis")
    companion = ((0, 0, 0, -1), (1, 0, 0, -1), (0, 1, 0, -1), (0, 0, 1, -1))
    require(multiply(act, module) == multiply(module, companion), "t is declared zeta5")
    show("module.map", module)
    show("module.inverse", module_inverse)

    static = columns(((1, 1, 0, 1, 0, 0), (0, 0, 1, -1, 0, 0)), 6)
    require(multiply(minus(t, identity(6)), static) == zero(6, 2), "static basis")
    require(rank(minus(t, identity(6))) == 4, "static dimension")
    static_extract = ((1, 0, 0, 0, 0, 0), (0, 0, 1, 0, 0, 0))
    require(multiply(static_extract, static) == identity(2), "static saturation")
    gluing = tuple(embedding[i] + static[i] for i in range(6))
    require(abs(determinant(gluing)) == 5, "integral gluing index five")
    q = ((2, -3, 1, 1, 0, 0),)
    require(all(x % 5 == 0 for x in multiply(q, gluing)[0]), "gluing kernel congruence")
    require(gcd(gcd(2, 3), 5) == 1, "gluing character surjective")
    # A surjective Z/5 character and this index-five sublattice have equal kernels.
    charge = tuple(row + (0, 0) for row in d)
    charge_character = multiply(((2, 0, 1),), charge)
    require(all((x - y) % 5 == 0 for x, y in zip(q[0], charge_character[0])),
            "gluing obstruction is actual charge 2rho0+rho2 mod5")
    require(multiply(charge, embedding) == zero(3, 4), "active actual Gauss kernel")
    require(rank(charge) == 2, "active equals rational Gauss kernel")
    require(multiply(charge, t) == charge, "raw T retains actual charges")
    static_charges = multiply(charge, static)
    show("static.basis", static)
    show("static.charges", static_charges)
    show("gluing.index", 5)
    show("gluing.admission", "2E0-3E1+E2+E3=0 mod5 iff 2rho0+rho2=0 mod5")
    show("gluing.inverse", inverse(gluing))

    j = plus(identity(4), power(act, 2))
    require(characteristic(j) == (1, -3, 4, -2, 1), "J characteristic")
    require(sum(j[i][i] for i in range(4)) == 3 and determinant(j) == 1, "J unit")
    require(integral(inverse(j)), "J inverse integral")
    require(multiply(transpose(j), multiply(b, j)) != b, "false J energy isometry rejected")
    j_witness = (1, 0, 0, 0)
    before = energy(c, 2, apply(embedding, j_witness))
    after = energy(c, 2, apply(embedding, apply(j, j_witness)))
    require(before != after, "explicit J energy counterexample")
    show("J.energy_counterexample", (j_witness, before, after))

    ell = multiply(minus(identity(4), act), minus(identity(4), power(act, 2)))
    numerator = multiply(power(act, 2), ell)
    require(multiply(ell, act) == multiply(act, ell), "L commutation")
    require(power(ell, 2) == times(5, power(act, 3)), "L squared")
    require(determinant(ell) == 25, "L determinant")
    require(multiply(numerator, ell) == times(5, identity(4)), "inverse numerator left")
    require(multiply(ell, numerator) == times(5, identity(4)), "inverse numerator right")
    adjoint = multiply(inverse(b), multiply(transpose(ell), b))
    require(multiply(adjoint, ell) == times(5, identity(4)), "actual energy adjoint")
    require(multiply(transpose(ell), multiply(b, ell)) == times(5, b), "energy multiplier five")
    require(multiply(transpose(ell), ell) != times(5, identity(4)),
            "Euclidean-adjoint substitution rejected")
    divisors = determinantal_divisors(ell)
    require(divisors == (1, 1, 1, 5, 25), "Smith determinantal-divisor certificate")
    smith = tuple(divisors[i + 1] // divisors[i] for i in range(4))
    h, hv = column_hermite(ell)
    require(multiply(ell, hv) == h and abs(determinant(hv)) == 1, "Hermite certificate")
    require(all(h[i][i] > 0 for i in range(4)), "Hermite positive diagonal")
    require(all(h[i][j] == 0 for i in range(4) for j in range(i)), "Hermite triangular")
    require(all(0 <= h[i][j] < h[i][i] for i in range(4) for j in range(i + 1, 4)),
            "Hermite reduced upper entries")

    def admission(y):
        return all(value % 5 == 0 for value in apply(numerator, y))

    def partial_inverse(y):
        integers = apply(numerator, y)
        if any(value % 5 != 0 for value in integers):
            raise ValueError("outside L5 image; division forbidden")
        return tuple(value // 5 for value in integers)

    # This is exactly the preregistered residue audit, not a shell search.
    image_residues = {tuple(value % 5 for value in apply(ell, x))
                      for x in product(range(5), repeat=4)}
    accepted, rejected = 0, 0
    for y in product(range(5), repeat=4):
        admitted = admission(y)
        require(admitted == (y in image_residues), "complete residue image equivalence")
        if admitted:
            accepted += 1
            require(apply(ell, partial_inverse(y)) == y, "accepted exact inverse")
        else:
            rejected += 1
            try:
                partial_inverse(y)
            except ValueError:
                pass
            else:
                raise AssertionError("hidden division accepted nonmember")
    require((accepted, rejected, len(image_residues)) == (25, 600, 25),
            "all 625 residues and image index25")
    congruences, _ = reduced_rows(numerator, 5)
    require(len(congruences) == 2, "two independent mod5 image conditions")
    # Chosen algebraically before execution: H(0,0,1,-2)=1+4=5.
    shell_witness = (0, 0, 1, -2)
    require(energy(c, 2, apply(embedding, shell_witness)) == 5, "shell witness H5")
    require(not admission(shell_witness), "whole-shell surjectivity counterexample")
    require(energy(c, 2, apply(embedding, seed)) == 1, "nonempty input H1 shell")
    show("L5.matrix", ell)
    show("L5.energy_adjoint", adjoint)
    show("L5.inverse_numerator", numerator)
    show("L5.Smith_determinantal_divisors", divisors)
    show("L5.Smith", smith)
    show("L5.Hermite", h)
    show("L5.Hermite_right_unimodular", hv)
    show("L5.image_congruence_rows_mod5", congruences)
    show("L5.residue_audit_accepted_rejected_total", (accepted, rejected, 625))
    show("L5.H5_nonimage_witness", (shell_witness, apply(numerator, shell_witness)))

    full_ell = multiply(minus(identity(6), t), minus(identity(6), power(t, 2)))
    p_static = times(Fraction(1, 5), phi_raw)
    require(power(p_static, 2) == p_static, "rational static projector")
    require(multiply(p_static, embedding) == zero(6, 4), "projector kills active")
    require(multiply(p_static, static) == static, "projector fixes static")
    require(multiply(full_ell, static) == zero(6, 2), "full L static contamination")
    require(multiply(full_ell, embedding) == multiply(embedding, ell), "full L active restriction")
    require(multiply(charge, full_ell) == zero(3, 6), "full L erases actual divergence")
    require(multiply(transpose(full_ell), multiply(raw_b, full_ell)) != times(5, raw_b),
            "full-carrier similitude overclaim rejected")
    extension = plus(full_ell, p_static)
    require(multiply(charge, extension) == charge, "rational extension preserves actual D")
    require(multiply(extension, static) == static, "extension fixes static")
    require(multiply(extension, embedding) == multiply(embedding, ell), "extension active action")
    raw_witness = (1, 0, 0, 0, 0, 0)
    extension_image = apply(extension, raw_witness)
    require(any(Fraction(x).denominator != 1 for x in extension_image),
            "rational extension does not preserve raw integer lattice")
    require(apply(charge, extension_image) == apply(charge, raw_witness),
            "nonintegral witness still preserves rational actual charge")
    static_witness = (1, 1, 0, 1, 0, 0)
    require(energy(c, 2, static_witness) == 3 and apply(full_ell, static_witness) == (0,) * 6,
            "static positive-energy annihilation witness")
    require(apply(charge, static_witness) == (2, -3, 1), "static actual charge witness")
    show("full_L.static_witness_energy_and_charge", (static_witness, 3, (2, -3, 1)))
    show("rational_extension.raw_integer_counterexample", (raw_witness, extension_image))
    show("rational_extension.projector", p_static)
    print("DISPOSITION: active identities pass; total injection and partial inverse distinguished")
    print("REJECTED OVERCLAIMS: integral direct sum, J isometry, Euclidean adjoint,")
    print("whole H1-to-H5 shell surjectivity, full L similitude/charge retention,")
    print("and whole raw-lattice integrality of the charge-preserving rational extension")
    print("INTERFACE: Z^4 active raw embedding; L5 image admission has two mod5 residues;")
    print("energy h->5h; active D charge zero; inverse rejects before dividing by five;")
    print("phase/branch/coupling and a 4h release reservoir remain additional data")
    print("Finite exact audit only; no shell enumeration, physical claim, or earned public status")


if __name__ == "__main__":
    main()
