#!/usr/bin/env python3
"""Frozen exact incubation audit; not a repository formal probe."""
import hashlib
import json

Z = (0, 0, 0, 0)
ONE = (1, 0, 0, 0)
RHO = (0, 0, 1, 0)
U = (1, 0, -1, 0)
W = (1, 0, 1, 0)
DOMAIN = (1, 3, 5, 7, 9, 11, 13, 15, 17, 23)
INITIAL = tuple(range(1, 16, 2))
X = tuple((2*i, 2*i+1) for i in range(6))
Y = tuple((12+2*i, 13+2*i) for i in range(6))
ARCH = (tuple((24+2*i, 25+2*i) for i in range(3)),
        tuple((30+2*i, 31+2*i) for i in range(3)))
SCRATCH = tuple(range(36, 45))
SEL = (45, 46, 47)
HELP = 48
CACHE = {}
APPLICATIONS = 0


def add(a, b):
    return tuple(x+y for x, y in zip(a, b))


def jmul(a):
    return (-a[3], a[0]-a[3], a[1]-a[3], a[2]-a[3])


def rho_mul(a):
    return jmul(jmul(a))


def account(a):
    return (5*sum(x*x for x in a)-sum(a)**2)//2


def primitive(a, b):
    key = (a, b)
    if key in CACHE:
        return CACHE[key]
    difference = tuple(x-y for x, y in zip(a, b))
    if any(x % 2 for x in difference):
        result = (a, b)
    else:
        center = tuple((x+y)//2 for x, y in zip(a, b))
        twist = rho_mul(tuple(x//2 for x in difference))
        result = (add(center, twist), tuple(x-y for x, y in zip(center, twist)))
    c, d = result
    assert add(a, b) == add(c, d)
    assert account(a)+account(b) == account(c)+account(d)
    assert sum(a) % 5 == sum(c) % 5
    assert sum(b) % 5 == sum(d) % 5
    CACHE[key] = result
    return result


def primitive_word(state, word, inverse=False):
    global APPLICATIONS
    state = list(state)
    edges = reversed(word) if inverse else word
    repeats = 4 if inverse else 1
    for a, b in edges:
        for _ in range(repeats):
            state[a], state[b] = primitive(state[a], state[b])
            APPLICATIONS += 1
    return tuple(state)


def dword(h, a, b):
    return [(h, a)]*3 + [(h, b)]*3 + [(h, a), (h, b), (h, a)]


def vword(g, a, b):
    d = dword(HELP, a, b)
    return [(g, HELP)] + d + [(g, HELP)]*4 + d


def table(n):
    x = 3*n+1
    v = 0
    while x % 2 == 0:
        x //= 2
        v += 1
    return x, v


def rails(register, value):
    return [pair[(value >> i) & 1] for i, pair in enumerate(register)]


def compile_circuit():
    # Macro is (control, token_target_a, token_target_b). All helpers restore.
    macros = []

    def controlled(controls, targets):
        assert 1 <= len(controls) <= 10
        borrowing = []
        conjunction = controls[0]
        for position, source in enumerate(controls[1:]):
            gate = (conjunction, source, SCRATCH[position])
            borrowing.append(gate)
            conjunction = SCRATCH[position]
        macros.extend(borrowing)
        macros.extend((conjunction, a, b) for a, b in targets)
        macros.extend(reversed(borrowing))

    for bank, selector in zip(ARCH, SEL[:2]):
        for n in DOMAIN:
            m, v = table(n)
            targets = [Y[i] for i in range(6) if (m >> i) & 1]
            targets += [bank[i] for i in range(3) if (v >> i) & 1]
            controlled([selector]+rails(X, n), targets)
        for n in DOMAIN:
            m, v = table(n)
            targets = [X[i] for i in range(6) if (n >> i) & 1]
            controlled([selector]+rails(Y, m)+rails(bank, v), targets)
        for i in range(6):
            controlled([selector, Y[i][1]], [X[i]])
            controlled([selector, X[i][1]], [Y[i]])

    word = []
    for control, a, b in macros:
        word.extend(vword(control, a, b))
    word.extend(dword(HELP, SEL[1], SEL[2]))
    word.extend(dword(HELP, SEL[0], SEL[1]))
    return tuple(macros), tuple(word)


def put(state, register, value):
    for i, (a, b) in enumerate(register):
        state[a], state[b] = (Z, U) if (value >> i) & 1 else (U, Z)


def read(state, register):
    value = 0
    for i, (a, b) in enumerate(register):
        pair = (state[a], state[b])
        assert pair in ((U, Z), (Z, U))
        value |= (pair == (Z, U)) << i
    return value


def preparation(n, a=0, b=0, selector=0):
    state = [Z]*49
    for reg, value in ((X, n), (Y, 0), (ARCH[0], a), (ARCH[1], b)):
        put(state, reg, value)
    state[SEL[selector]] = U
    state[HELP] = W
    return tuple(state)


def boundary(state, n, a, b, selector):
    assert read(state, X) == n
    assert read(state, Y) == 0
    assert read(state, ARCH[0]) == a
    assert read(state, ARCH[1]) == b
    assert all(state[i] == Z for i in SCRATCH)
    assert state[HELP] == W
    assert tuple(state[i] for i in SEL) == tuple(U if i == selector else Z for i in range(3))
    assert sum(account(z) for z in state) == 98
    assert tuple(sum(z[i] for z in state) for i in range(4)) == (20, 0, -18, 0)


def abstract_step(state, macros):
    state = list(state)
    for g, a, b in macros:
        assert state[g] in (Z, U)
        assert (state[a], state[b]) in ((Z, Z), (U, Z), (Z, U))
        if state[g] == U:
            state[a], state[b] = state[b], state[a]
    for a, b in ((SEL[1], SEL[2]), (SEL[0], SEL[1])):
        assert (state[a], state[b]) in ((Z, Z), (U, Z), (Z, U))
        state[a], state[b] = state[b], state[a]
    return tuple(state)


def main():
    assert account(U) == 5 and account(W) == 3
    macros, word = compile_circuit()
    word_hash = hashlib.sha256(''.join(f'{a},{b}\n' for a, b in word).encode()).hexdigest()
    # Six complete token-swap rows, including dirty zero-target rows.
    for control in (Z, U):
        for pair in ((Z, Z), (U, Z), (Z, U)):
            state = [Z]*49
            state[0], state[1], state[2], state[HELP] = control, *pair, W
            state = tuple(state)
            expected = list(state)
            if control == U:
                expected[1], expected[2] = expected[2], expected[1]
            output = primitive_word(state, vword(0, 1, 2))
            assert output == tuple(expected)
            assert primitive_word(output, vword(0, 1, 2), inverse=True) == state
    print('PASS six literal controlled-swap rows and inverses')

    all_boundaries = []
    final_pairs = []
    for n in INITIAL:
        initial = preparation(n)
        boundary(initial, n, 0, 0, 0)
        first_m, first_v = table(n)
        assert first_m in DOMAIN
        second_m, second_v = table(first_m)
        s1 = primitive_word(initial, word)
        boundary(s1, first_m, first_v, 0, 1)
        s2 = primitive_word(s1, word)
        boundary(s2, second_m, first_v, second_v, 2)
        s3 = primitive_word(s2, word)
        boundary(s3, second_m, first_v, second_v, 0)
        assert tuple(s2[i] for i in range(45)) == tuple(s3[i] for i in range(45))
        restored = s3
        for _ in range(3):
            restored = primitive_word(restored, word, inverse=True)
        assert restored == initial
        recovered = ((1 << second_v)*second_m-1)//3
        assert recovered == first_m
        recovered = ((1 << first_v)*recovered-1)//3
        assert recovered == n
        all_boundaries.append([n, [s1, s2, s3]])
        final_pairs.append((n, first_m, first_v, second_m, second_v))
    print('PASS eight two-transition-plus-skip trajectories and full primitive inverses')

    for n in DOMAIN:
        m, depth = table(n)
        for old in range(8):
            initial = preparation(n, a=old, selector=1)
            output = primitive_word(initial, word)
            boundary(output, m, old, depth, 2)
            assert primitive_word(output, word, inverse=True) == initial
    print('PASS 80 literal occupied-A continuations and full inverses')

    # Preregistered abstract skip audit; not 4096 primitive-word replays.
    for n in range(64):
        for a in range(8):
            for b in range(8):
                state = preparation(n, a, b, selector=2)
                output = abstract_step(state, macros)
                boundary(output, n, a, b, 0)
    print('PASS 4096 abstract-token skip cases, using the six-row literal contract')

    # Independent identity check on every discovered primitive input pair.
    keys = list(CACHE)
    for a, b in keys:
        pair = (a, b)
        for _ in range(5):
            pair = primitive(*pair)
        assert pair == (a, b)
    assert table(1) == (1, 2) and table(5) == (1, 4)
    fingerprint = hashlib.sha256(json.dumps(all_boundaries, separators=(',', ':')).encode()).hexdigest()
    print(f'WORD contacts={len(word)} macros={len(macros)} sha256={word_hash}')
    print(f'BOUNDARY sha256={fingerprint}')
    print(f'RESOURCE slots=49 account=98 source_bits=6 depth_bits_per_bank=3')
    print('FINAL '+json.dumps(final_pairs, separators=(',', ':')))
    print(f'COUNTS primitive_applications={APPLICATIONS} distinct_pair_inputs={len(CACHE)}')
    print('PASS C-COLLATZ-CONTACT-STEP-RECORD-N; finite supplied-rule compiler only')


if __name__ == '__main__':
    main()
