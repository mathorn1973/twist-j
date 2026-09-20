#!/usr/bin/env python3
"""Exact finite audit of the declared conditional delayed-record protocol.

Python standard library only. No randomness, files, network or floating point.
The all-word/all-duration conclusions belong to PROOF.md, not a finite run.
All point arithmetic is F5; amplitude arithmetic is Q[j]/Phi_5(j).
A. M. Thorn; original text Apache-2.0.
"""

from fractions import Fraction
from itertools import product


MOD = 5
MARKS = (1, 2, 4, 3)
COARSE = (0, 1, 2, 2, 2)


def check(value, message):
    if not value:
        raise AssertionError(message)


def point(p, z, r):
    return tuple(p) + ((z - sum(p) - r) % MOD, r % MOD)


def trace(x):
    return sum(x) % MOD


def generator(index, x):
    a, b, c, d, q, r = x
    if index == 0:
        y = (b, a, d, c, q, r)
    elif index == 1:
        y = (-c, -d, -a, -b, -q, -r)
    elif index == 2:
        y = (2-c, 1-d+r, 2-a, 1-b-r, 1-q, -r)
    elif index == 3:
        y = (2-a, 1-b, 3-c, 4-d, 1-q, 1-r)
    elif index == 4:
        y = (2-a, 1-b, 3-c, 4-d, 2-q, 1-r)
    else:
        raise AssertionError("invalid generator")
    return tuple(v % MOD for v in y)


def step(x, bit):
    return generator((trace(x) + 2*bit) % MOD, x)


def evolve(x, word):
    for bit in word:
        x = step(x, bit)
    return x


def translate(x, delta):
    return x[:4] + ((x[4]-delta) % MOD, (x[5]+delta) % MOD)


def parity(n):
    return 1 if n % 2 == 0 else -1


def mark(x, n):
    return (parity(n-3)*sum(x[:4])) % MOD


def write(x, n):
    return translate(x, COARSE[mark(x, n)])


def exchange(x, m, reference, sign):
    return (point(x[:4], trace(x), reference+sign*m),
            (sign*(x[5]-reference)) % MOD)


def protocol(x, m, n, word, reference):
    """Execute both added maps and the actual selected steps between them."""
    ready = point(x[:4], trace(x), reference)
    final_reference = evolve(ready, word)[5]
    return exchange(evolve(write(x, n), word), m,
                    final_reference, parity(len(word)))


def words(maximum):
    return tuple(w for length in range(maximum+1)
                 for w in product((0, 1), repeat=length))


def native_audit():
    count = 0
    selected = {(1, 0): (1, 4), (1, 1): (3, 1),
                (4, 0): (4, 4), (4, 1): (1, 1)}
    for p in product(range(5), repeat=4):
        for z, r, bit, delta in product((1, 4), range(5), (0, 1), range(5)):
            x = point(p, z, r)
            free = step(x, bit)
            moved = step(translate(x, delta), bit)
            index, next_z = selected[z, bit]
            check((z+2*bit) % MOD == index, "selector index")
            check(trace(free) == next_z, "stable sheet")
            check(moved == translate(free, -delta), "one-step conjugacy")
            check(moved[:4] == free[:4] and trace(moved) == trace(free),
                  "source and selector preservation")
            check(sum(free[:4]) % MOD == (-sum(p)) % MOD,
                  "transported source sum")
            # Local mark transport for each counter parity is the same law.
            for n in (3, 4):
                check(mark(free, n+1) == mark(x, n), "transported mark")
            count += 1
    check(count == 62500, "stable audit count")
    return count


def write_audit():
    count = 0
    for n in (3, 4):
        image = set()
        for x in product(range(5), repeat=6):
            y = write(x, n)
            check(y[:4] == x[:4] and trace(y) == trace(x), "write invariant")
            check(translate(y, -COARSE[mark(y, n)]) == x, "write inverse")
            image.add(y)
            count += 1
        check(len(image) == 15625, "global write permutation")
    check(count == 31250, "write audit count")
    return count


def exchange_audit():
    count = 0
    for reference, r, m, sign in product(range(5), range(5), range(5), (1, -1)):
        # p and z are arbitrary spectators; the exhaustive port law is scalar.
        x = point((2, 1, 4, 3), 4, r)
        y, out = exchange(x, m, reference, sign)
        check(y[:4] == x[:4] and trace(y) == trace(x), "exchange spectator")
        check((y[5]-reference) % MOD == sign*m % MOD, "exchange port")
        check(out == sign*(r-reference) % MOD, "exchange archive")
        check(exchange(y, out, reference, sign) == (x, m), "exchange involution")
        count += 1
    check(count == 250, "exchange audit count")
    return count


def composition_audit():
    # EXACT REDUCTION, not sampled source points: C and S depend on p only
    # through s(p). A01 exhausts all 625 p and proves the selected common-z
    # source map is port independent and carries s to -s. Each of the five
    # sums has 125 preimages. Thus the following 7,500 scalar cases represent
    # all 937,500 p-expanded cases for waits (), (0), (1). Induction in
    # PROOF.md supplies arbitrary words, not this finite enumeration.
    count = 0
    for s, z, reference, e, m, n in product(range(5), (1, 4), range(5),
                                           range(5), range(5), (3, 4)):
        p = (s, 0, 0, 0)
        x = point(p, z, reference+e)
        f = COARSE[mark(x, n)]
        for word in ((), (0,), (1,)):
            sign = parity(len(word))
            free_ready = evolve(point(p, z, reference), word)
            expected = (point(free_ready[:4], trace(free_ready),
                              free_ready[5]+sign*m), (e+f) % MOD)
            direct = protocol(x, m, n, word, reference)
            early_x, early_m = exchange(write(x, n), m, reference, 1)
            transported_early = (evolve(early_x, word), early_m)
            check(direct == expected == transported_early,
                  "complete delayed composition and covariance")
            count += 1
    check(count == 7500, "composition audit count")
    return count


def endpoint(h):
    return point((h, 0, 0, 0), 1, 0)


def holding_check(x, n, word, reference):
    f = COARSE[mark(x, n)]
    free, moved = x, write(x, n)
    check((moved[5]-reference) % MOD == f, "initial held mark")
    for j, bit in enumerate(word, start=1):
        free, moved = step(free, bit), step(moved, bit)
        check(moved[:4] == free[:4] and trace(moved) == trace(free),
              "intermediate free source and trace")
        check(moved == translate(free, parity(j)*f), "intermediate conjugacy")
        check(parity(j)*(moved[5]-free[5]) % MOD == f, "held mark")
        check(mark(moved, n+j) == mark(x, n), "held source label")
    check(protocol(x, 0, n, word, reference) == (free, f),
          "restored full checkpoint")


def word_audit():
    count = 0
    for word in words(6):
        images = set()
        for h in MARKS:
            x = endpoint(h)
            holding_check(x, 3, word, 0)
            images.add(evolve(x, word))
            count += 1
        check(len(images) == 4, "word code injectivity")
    check(count == 508, "word audit count")
    return count


def actual_audit():
    code = {3: tuple(endpoint(h) for h in MARKS)}
    for n in range(3, 51):
        code[n+1] = tuple(step(x, n.bit_count() % 2) for x in code[n])
    count = 0
    for n in range(3, 36):
        reference = code[n][0][5]
        check(len({(trace(x), x[5]) for x in code[n]}) == 1,
              "actual common reference port")
        for k in range(17):
            word = tuple(j.bit_count() % 2 for j in range(n, n+k))
            for index, h in enumerate(MARKS):
                x = code[n][index]
                check(mark(x, n) == h, "actual current label")
                holding_check(x, n, word, reference)
                check(evolve(x, word) == code[n+k][index], "actual free prefix")
                count += 1
    check(count == 2244, "actual audit count")
    return count


# Exact cyclotomic arithmetic. Coefficients use the basis 1,j,j^2,j^3,
# with j^4=-1-j-j^2-j^3 and complex conjugation j -> j^4.
ZERO = (Fraction(0),)*4
ONE = (Fraction(1), Fraction(0), Fraction(0), Fraction(0))


def scalar(value):
    return (Fraction(value), Fraction(0), Fraction(0), Fraction(0))


def add(a, b):
    return tuple(x+y for x, y in zip(a, b))


def scale(a, value):
    return tuple(x*value for x in a)


def mul(a, b):
    c = [Fraction(0) for _ in range(7)]
    for i in range(4):
        for j in range(4):
            c[i+j] += a[i]*b[j]
    for degree in range(6, 3, -1):
        for shift in range(1, 5):
            c[degree-shift] -= c[degree]
        c[degree] = Fraction(0)
    return tuple(c[:4])


def root_power(exponent):
    exponent %= 5
    if exponent == 4:
        return (Fraction(-1),)*4
    return tuple(Fraction(int(i == exponent)) for i in range(4))


def conjugate(a):
    out = ZERO
    for i, coefficient in enumerate(a):
        out = add(out, scale(root_power(-i), coefficient))
    return out


def matrix(rows, cols):
    return [[ZERO for _ in range(cols)] for _ in range(rows)]


def identity(size):
    return [[ONE if i == j else ZERO for j in range(size)] for i in range(size)]


def mm(a, b):
    check(len(a[0]) == len(b), "matrix dimensions")
    out = matrix(len(a), len(b[0]))
    for i in range(len(a)):
        for j in range(len(b[0])):
            value = ZERO
            for k in range(len(b)):
                value = add(value, mul(a[i][k], b[k][j]))
            out[i][j] = value
    return out


def adjoint(a):
    return [[conjugate(a[j][i]) for j in range(len(a))]
            for i in range(len(a[0]))]


def ma(a, b):
    return [[add(x, y) for x, y in zip(row_a, row_b)]
            for row_a, row_b in zip(a, b)]


def coherent_lift(a, labels):
    out = matrix(8, 8)
    for i in range(4):
        for j in range(4):
            out[2*i+labels[i]][2*j+labels[j]] = a[i][j]
    return out


def archive_trace(joint):
    return [[add(joint[2*i][2*j], joint[2*i+1][2*j+1])
             for j in range(4)] for i in range(4)]


def coarse_reduce(a):
    return [[a[i][j] if (i == 0) == (j == 0) else ZERO
             for j in range(4)] for i in range(4)]


def cyclotomic_audit():
    # Reconstruct the code from H and the four Galois automorphisms, rather
    # than importing a previously computed endpoint matrix.
    h = ((1, 1, 1, 1), (1, -1, 1, -1),
         (1, 1, -1, -1), (1, -1, -1, 1))
    g = add(ONE, scale(add(root_power(1), root_power(4)), 2))
    check(mul(g, g) == scalar(5) and conjugate(g) == g, "real square root")
    c = scale(g, Fraction(1, 10))
    w = matrix(4, 4)
    for k in range(4):
        for i in range(4):
            total = ZERO
            for a, automorphism in enumerate(MARKS):
                total = add(total, scale(root_power(automorphism*(i+1)), h[k][a]))
            w[k][i] = mul(c, total)
    gram = [[scalar(Fraction(int(i == j))-Fraction(1, 5))
             for j in range(4)] for i in range(4)]
    gram_inverse = [[scalar(int(i == j)+1) for j in range(4)] for i in range(4)]
    p_low = [[scalar(Fraction(1, 4)) for _ in range(4)] for _ in range(4)]
    p_high = [[scalar(Fraction(int(i == j))-Fraction(1, 4))
               for j in range(4)] for i in range(4)]
    d_low = [[scalar(int(i == j == 0)) for j in range(4)] for i in range(4)]
    d_high = [[scalar(int(i == j and i != 0)) for j in range(4)] for i in range(4)]
    w_adjoint = adjoint(w)
    w_inverse = mm(gram_inverse, w_adjoint)
    check(mm(w_adjoint, w) == gram, "W adjoint W equals Gram")
    check(mm(w_inverse, w) == identity(4) == mm(w, w_inverse), "W inverse")
    for projector, effect in ((p_low, d_low), (p_high, d_high)):
        check(mm(projector, projector) == projector, "source projector")
        check(mm(effect, w) == mm(w, projector), "D W equals W P")
        check(mm(mm(w_adjoint, effect), w) == mm(gram, projector), "effect form")
    count = 0
    high_off_diagonal = 0
    low_high = 0
    labels = (0, 1, 1, 1)  # archive bases |1>,|2>, indexed internally 0,1
    for i, j in product(range(4), repeat=2):
        unit = matrix(4, 4)
        unit[i][j] = ONE
        # The same sixteen units here are literal ENDPOINT matrix units.
        # Below, W transforms them when used as SOURCE matrix units.
        endpoint_reduced = archive_trace(coherent_lift(unit, labels))
        check(endpoint_reduced == coarse_reduce(unit), "endpoint matrix unit")
        if i != j and i != 0 and j != 0:
            check(endpoint_reduced == unit, "HIGH cross term retained")
            high_off_diagonal += 1
        if (i == 0) != (j == 0):
            check(endpoint_reduced == matrix(4, 4), "LOW/HIGH cross term removed")
            low_high += 1
        rho = mm(mm(w, unit), w_adjoint)
        joint = coherent_lift(rho, labels)
        expected = matrix(8, 8)
        for a, pa in enumerate((p_low, p_high)):
            for b, pb in enumerate((p_low, p_high)):
                block = mm(mm(mm(mm(w, pa), unit), adjoint(pb)), w_adjoint)
                for row, col in product(range(4), repeat=2):
                    expected[2*row+a][2*col+b] = block[row][col]
        check(joint == expected, "coherent record on every source matrix unit")
        check(archive_trace(joint) == coarse_reduce(rho), "partial archive trace")
        operator = mm(mm(w, unit), w_inverse)
        for projector, effect in ((p_low, d_low), (p_high, d_high)):
            check(mm(mm(effect, operator), effect)
                  == mm(mm(mm(mm(w, projector), unit), projector), w_inverse),
                  "source operator coarse intertwining")
        count += 1
    check(count == 16, "matrix unit count")
    check(high_off_diagonal == 6 and low_high == 6, "coherence sector counts")
    # Explicit pure state e_LOW+e_HIGH. Every basis checkpoint is restored,
    # while its reduced native state loses the LOW/HIGH off-diagonal entry.
    rho = matrix(4, 4)
    for i, j in product((0, 1), repeat=2):
        rho[i][j] = ONE
    joint = coherent_lift(rho, labels)
    reduced = archive_trace(joint)
    check(rho[0][1] == ONE and reduced[0][1] == ZERO and reduced != rho,
          "basis restoration is not uncorrelated state restoration")
    check(joint[0][3] == ONE, "joint LOW/HIGH coherence remains in archive")
    return count


def repeated_audit():
    count = 0
    for first, second in product(words(3), repeat=2):
        for h in MARKS:
            x = endpoint(h)
            y, m1 = protocol(x, 0, 3, first, 0)
            z, m2 = protocol(y, 0, 3+len(first), second, y[5])
            check(z == evolve(x, first+second), "repeated restored path")
            check((m1, m2) == (COARSE[h], COARSE[h]), "same repeated outcome")
            count += 1
    check(count == 900, "repeated record count")
    return count


def negative_audit():
    # 1. Outside the stable sheets, c transmits the port displacement to p.
    x = (0, 0, 0, 0, 0, 0)
    moved, free = step(translate(x, 1), 1), step(x, 1)
    check(moved[:4] == (2, 2, 2, 0) and free[:4] == (2, 1, 2, 1),
          "off-sheet c witness")
    check(moved != translate(free, -1), "off-sheet claimed extension rejected")
    # 2. At actual tick 3, b is selected and the mark changes sign.
    x = endpoint(1)
    free, moved = step(x, 0), step(write(x, 3), 0)
    wrong, wrong_mark = exchange(moved, 0, free[5], 1)
    check(wrong == free and wrong_mark == 4, "omitted odd sign witness")
    # 3. Nonready e=1 contributes to the archived mark, although checkpoint
    # restoration relative to the declared reference still happens.
    nonready = translate(x, 1)
    restored, contaminated = protocol(nonready, 0, 3, (), 0)
    check(restored == x and contaminated == 2, "nonready contamination witness")
    # 4. Occupied memory m=3 returns to the port; it cannot be erased by swap.
    occupied, saved = protocol(x, 3, 3, (), 0)
    check(occupied == translate(x, 3) and occupied != x and saved == 1,
          "occupied archive witness")
    # 5. Coarse HIGH recording preserves its cross terms. A fine read followed
    # by forgetting kills them and therefore is not the declared operation.
    rho = matrix(4, 4)
    for i, j in product((1, 2), repeat=2):
        rho[i][j] = ONE
    coarse = archive_trace(coherent_lift(rho, (0, 1, 1, 1)))
    fine = [[rho[i][j] if i == j else ZERO for j in range(4)] for i in range(4)]
    check(coarse == rho and coarse[1][2] == ONE and fine[1][2] == ZERO,
          "fine HIGH read witness")
    return 5


def main():
    print("P-QDD-UNINTERRUPTED-RECORD-1")
    count = native_audit()
    print(f"PASS A01 stable one-step conjugacy/source/trace: {count} cases")
    count = write_audit()
    print(f"PASS A02 global controlled-write permutations: {count} points/parities")
    count = exchange_audit()
    print(f"PASS A03 signed-exchange involutions: {count} port cases")
    count = composition_audit()
    print(f"PASS A04 full-port composition: {count} reduced / {count*125} source cases")
    count = word_audit()
    print(f"PASS A05 all bit words through length 6: {count} code cases")
    count = actual_audit()
    print(f"PASS A06 actual starts 3..35, delays 0..16: {count} code cases")
    count = cyclotomic_audit()
    print(f"PASS A07 exact Q(j) Gram/projectors/coherence: {count} matrix units")
    count = repeated_audit()
    print(f"PASS A08 two records of the same transported outcome: {count} code cases")
    count = negative_audit()
    print(f"PASS A09 scope and readiness negative controls: {count} witnesses")
    print("PASS finite-premise audit: 9/9")
    print("SCOPE all-duration proof: PROOF.md; entrance/exit/archive are admitted")


if __name__ == "__main__":
    main()
