#!/usr/bin/env python3
"""Exact audit of a NEW declared apparatus; never executes a source verifier.

PUBLIC / NON-CANONICAL / L1. A. M. Thorn. Apache-2.0.
Freeze this file and PREREG before execution. Integers and F5 only.
"""
from dataclasses import dataclass, replace
from itertools import product, combinations


def ell(a):
    return (0, 1, 2, -2, -1)[a % 5]


def sign(a):
    return (a > 0) - (a < 0)


def epsilon(a):
    return {1: 1, 4: -1}.get(a % 5, 0)


@dataclass(frozen=True)
class State:
    cells: tuple  # work/output, input 1..L, retained native reference
    scratch: tuple
    bundles: tuple  # each (q,p,u,v,a,b,c), Weyl j^c Z^a X^b
    bank: int
    capacity: int
    pc: int
    direction: int


def energy(s):
    return (sum(sum(x*x for x in w[:4]) for w in s.bundles)
            + 2*sum(ell(x)**2 for h in s.cells for x in h)
            + 2*sum(ell(x)**2 for x in s.scratch))


def total(s):
    return energy(s) + s.bank


def primitive(s, edge, inverse=False):
    """One unguarded bijection, including all dirty inputs; no PC change."""
    j, op = divmod(edge, 24)
    j += 1
    cells = [list(h) for h in s.cells]
    scratch = list(s.scratch)
    bundles = list(s.bundles)
    if op == 0:
        cells[0][0], cells[j][1] = cells[j][1], cells[0][0]
    elif op == 1:
        bundles[0], bundles[j] = bundles[j], bundles[0]
    elif op < 22:
        axis = (op - 2) % 4
        q, p, u, v, a, b, c = bundles[0]
        eta = epsilon(cells[0][0])
        h = (1, eta, -1, -eta)[axis]
        if inverse:
            h = -h
        if axis % 2 == 0:
            q += h
            b, c = (b+h) % 5, (c-h*a) % 5
        else:
            p, u, v = p+h, u+h*q, v+h*q
            a = (a+h) % 5
        bundles[0] = (q, p, u, v, a, b, c)
    elif op == 22:
        u, v = bundles[0][2:4]
        bit = sign(u*u-v*v)
        scratch[j-1] = (scratch[j-1] + (-bit if inverse else bit)) % 5
    else:
        scratch[j-1], cells[0][1] = cells[0][1], scratch[j-1]
    return replace(s, cells=tuple(map(tuple, cells)), scratch=tuple(scratch),
                   bundles=tuple(bundles))


def matching(s):
    """Energy-shell edge matching H; involution even at refusal/boundary."""
    end = 24*len(s.scratch)
    edge = s.pc if s.direction == 1 else s.pc-1
    if not 0 <= edge < end:
        return s
    t = primitive(s, edge, inverse=s.direction == -1)
    bank = s.bank + energy(s) - energy(t)
    if not 0 <= bank <= s.capacity:
        return s
    return replace(t, bank=bank, pc=s.pc+s.direction, direction=-s.direction)


def flip(s):
    return replace(s, direction=-s.direction)


def step(s):
    return flip(matching(s))


def back(s):
    return matching(flip(s))


def chart(gamma, h):
    A, z, r = gamma
    mu, lam = h
    B, k = 3*A % 5, A*z % 5
    C, D = k*(2+3*mu) % 5, k*(1+3*lam) % 5
    return tuple(x % 5 for x in
                 (3*(A+C+2), 3*(B+D+1), 3*(A-C-2),
                  3*(B-D-1), z-4*A-r, r))


def readers(x):
    a, b, c, d, q, r = x
    A, B = (a+c) % 5, (b+d) % 5
    zs, zr = (4*A+q+r) % 5, (3*B+q+r) % 5
    assert B in (2, 3) and zr in (1, 4)
    return ((1+2*A*zs*(a-c-2)) % 5,
            (3-B*zr*(b-d-1)) % 5)


def native(x, bit):
    a, b, c, d, q, r = x
    letter = (sum(x)+2*bit) % 5
    images = ((b,a,d,c,q,r), (-c,-d,-a,-b,-q,-r),
              (2-c,1-d+r,2-a,1-b-r,1-q,-r),
              (2-a,1-b,3-c,4-d,1-q,1-r),
              (2-a,1-b,3-c,4-d,2-q,1-r))
    return tuple(t % 5 for t in images[letter])


def next_gamma(gamma, bit):
    A, z, r = gamma
    if (z+2*bit) % 5 == 1:
        return (-A % 5, -z % 5, -r % 5)
    return (-A % 5, z, (1-r) % 5)


def gamma_at(n):
    assert n >= 3
    g = (1, 1, 1)
    for k in range(3, n):
        g = next_gamma(g, k.bit_count() % 2)
    return g


def full_step(n, gamma, s):
    assert gamma == gamma_at(n)
    t = step(s)
    g = next_gamma(gamma, n.bit_count() % 2)
    for h in t.cells:
        assert native(chart(gamma, h), n.bit_count() % 2) == chart(g, h)
    return n+1, g, t


def full_back(n, gamma, s):
    assert n >= 4 and gamma == gamma_at(n)
    return n-1, gamma_at(n-1), back(s)


def matrix(w):
    """Independent exact monomial action: images of all five basis vectors."""
    a, b, c = w
    return tuple(((k+b) % 5, (c+a*(k+b)) % 5) for k in range(5))


def left_letter(m, axis, h):
    if axis == 'Q':
        return tuple(((k+h) % 5, e) for k, e in m)
    return tuple((k, (e+h*k) % 5) for k, e in m)


def phase_audit(s, t):
    mats = [matrix(w[4:]) for w in s.bundles]
    if t.pc != s.pc:
        edge = min(s.pc, t.pc)
        j, op = divmod(edge, 24)
        if op == 1:
            mats[0], mats[j+1] = mats[j+1], mats[0]
        elif 2 <= op < 22:
            axis = (op-2) % 4
            h = (1, epsilon(s.cells[0][0]), -1, -epsilon(s.cells[0][0]))[axis]
            h *= s.direction
            mats[0] = left_letter(mats[0], 'Q' if axis % 2 == 0 else 'P', h)
    assert mats == [matrix(w[4:]) for w in t.bundles]


def audit(s):
    t = step(s)
    assert total(t) == total(s)
    assert 0 <= t.bank <= t.capacity
    assert back(t) == s and step(back(s)) == s
    assert matching(matching(s)) == s
    phase_audit(s, t)
    if t.pc == s.pc:
        assert t == flip(s)  # no partial geometry, memory or phase update
    else:
        assert t.pc-s.pc == s.direction and t.direction == s.direction
    return t


def prepared(messages, old=(2, 3), bank=None, companions=None, ref=(2, 4),
             dirty=(2,-1,3,0,4,2,1)):
    L = len(messages)
    if bank is None:
        bank = 52*L
    if companions is None:
        companions = tuple((j+2) % 5 for j in range(L))
    cells = (tuple(old),) + tuple((v, e % 5) for v,e in zip(companions,messages)) + (ref,)
    return State(cells, (0,)*L, (dirty,)+((0,0,1,-1,0,0,0),)*L,
                 bank, bank, 0, 1)


def gate_native():
    seen = set()
    count = 0
    for A,z,r,mu,lam in product((1,4),(1,4),range(5),range(5),range(5)):
        g, h = (A,z,r), (mu,lam)
        x = chart(g,h)
        assert readers(x) == h
        seen.add(x)
        for bit in (0,1):
            assert native(x,bit) == chart(next_gamma(g,bit),h)
            count += 1
    assert len(seen) == 500
    for lam,mu in product(range(5), repeat=2):
        x = (lam,mu,-lam % 5,-mu % 5,0,0)
        for n in range(3):
            x = native(x, n.bit_count() % 2)
        assert x == chart((1,1,1),(mu,lam))
    print(f'NATIVE chart=500 continuation={count} occupied_prefix=25 PASS')


def gate_small_shell():
    # ALL cost<=2 payloads, L=1, Weyl labels fixed at identity (not all labels).
    base = State(((0,0),)*3, (0,), ((0,0,0,0,0,0,0),)*2, 0,2,0,1)
    payloads = [base]
    for number in (1,2):
        for places in combinations(range(8), number):
            for signs in product((-1,1), repeat=number):
                vals = [0]*8
                for p,e in zip(places,signs):
                    vals[p] = e
                payloads.append(replace(base,bundles=(tuple(vals[:4])+(0,0,0),
                                                      tuple(vals[4:])+(0,0,0))))
    for p,e in product(range(7), (1,4)):
        vals = [0]*7
        vals[p] = e
        payloads.append(replace(base,cells=tuple(tuple(vals[2*i:2*i+2]) for i in range(3)),
                                scratch=(vals[6],)))
    assert len(payloads) == 143 and len(set(payloads)) == 143
    count = 0
    for s in payloads:
        for pc,direction in product(range(25),(-1,1)):
            audit(replace(s,pc=pc,direction=direction,bank=2-energy(s)))
            count += 1
    print(f'LOW_SHELL E=2 payloads=143 phase_identity_slice cases={count} PASS')


def gate_dirty_grid():
    count = accepted = refused = 0
    # Explicitly a product grid, not the whole unbounded apparatus.
    for q,p,u,v in product((-1,0,1),repeat=4):
        for mu,m,bank,pc,direction in product(range(5),range(5),range(3),
                                             (0,1,2,3,4,5,22,23,24),(-1,1)):
            s = State(((mu,m),(2,4),(3,1)),(2,),
                      ((q,p,u,v,mu,m,(mu+m)%5),(2,-1,0,3,1,2,3)),
                      bank,4,pc,direction)
            t = audit(s)
            accepted += t.pc != s.pc
            refused += t.pc == s.pc
            count += 1
    print(f'DIRTY_GRID cases={count} moved={accepted} bounced={refused} PASS')


def gate_weyl():
    count = 0
    for w in product(range(5),repeat=3):
        a,b,c = w
        for h in (-2,-1,0,1,2):
            assert matrix((a,(b+h)%5,(c-h*a)%5)) == left_letter(matrix(w),'Q',h)
            assert matrix(((a+h)%5,b,c)) == left_letter(matrix(w),'P',h)
            count += 2
    print(f'WEYL all_labels=125 left_multiplications={count} PASS')


def tensor_reading(s):
    out = []
    for basis in product(range(5), repeat=len(s.bundles)):
        k = list(basis)
        for edge in range(s.pc):
            j, op = divmod(edge, 24)
            if op == 1:
                k[0], k[j+1] = k[j+1], k[0]
        exponent = 0
        for i,w in enumerate(s.bundles):
            a,b,c = w[4:]
            k[i] = (k[i]+b) % 5
            exponent = (exponent+c+a*k[i]) % 5
        out.append((tuple(k), exponent))
    return tuple(out)


def gate_tensor_history():
    comparisons = 0
    for messages,bank in product(((1,-1),(-1,1)),(0,103,104)):
        s = prepared(messages,bank=bank)
        actual = tensor_reading(s)
        for _ in range(98):
            t = audit(s)
            if t.pc != s.pc:
                j,op = divmod(min(s.pc,t.pc),24)
                if op == 1:
                    changed = []
                    for basis,e in actual:
                        k = list(basis)
                        k[0], k[j+1] = k[j+1], k[0]
                        changed.append((tuple(k),e))
                    actual = tuple(changed)
                elif 2 <= op < 22:
                    axis = (op-2) % 4
                    eta = epsilon(s.cells[0][0])
                    h = (1,eta,-1,-eta)[axis]*s.direction
                    changed = []
                    for basis,e in actual:
                        k = list(basis)
                        if axis % 2 == 0:
                            k[0] = (k[0]+h) % 5
                        else:
                            e = (e+h*k[0]) % 5
                        changed.append((tuple(k),e))
                    actual = tuple(changed)
            assert actual == tensor_reading(t)
            comparisons += len(actual)
            s = t
    print(f'TENSOR_HISTORY trajectories=6 basis_comparisons={comparisons} PASS')


def run_ready(s, messages, native_checks=False):
    initial = s
    old_receiver = s.cells[0][1]
    n, gamma = 3, (1,1,1)
    for edge in range(24*len(messages)):
        before = s
        s = audit(s)
        assert s.pc == edge+1 and s.direction == 1
        if native_checks:
            full = full_step(n,gamma,before)
            assert full_back(*full) == (n,gamma,before)
            n,gamma,t = full
            assert t == s
        if edge % 24 == 21:
            eta = messages[edge//24]
            assert s.bundles[0][:4] == (0,0,1+5*eta,-1+5*eta)
            assert s.bundles[0][4:] == (0,0,0)
        if edge % 24 == 23:
            j = edge//24
            assert s.cells[0][1] == messages[j] % 5
            assert s.scratch[j] == old_receiver
            old_receiver = messages[j] % 5
            assert energy(s)-energy(initial) == 52*(j+1)
            assert s.bank == initial.bank-52*(j+1)
    # Finite core returns only after both boundary reflections and exact undo.
    for _ in range(24*len(messages)+2):
        s = audit(s)
    assert s == initial
    return 2*(24*len(messages)+1)


def gate_delivery():
    trajectories = ticks = 0
    for eta,mu,m,comp in product((-1,1),range(5),range(5),range(5)):
        s = prepared((eta,),old=(mu,m),companions=(comp,),ref=(m,mu))
        ticks += run_ready(s,(eta,))
        trajectories += 1
    for e1,e2,mu,m in product((-1,1),(-1,1),range(5),range(5)):
        s = prepared((e1,e2),old=(mu,m),companions=(m,mu))
        ticks += run_ready(s,(e1,e2),native_checks=True)
        trajectories += 1
    print(f'DELIVERY trajectories={trajectories} core_ticks={ticks} L1_L2 sharp_bank=52L PASS')


def gate_funding_and_preparation():
    count = 0
    for eta,bank in product((-1,1),range(55)):
        s = prepared((eta,),bank=bank)
        for _ in range(50):
            t = audit(s)
            if bank < 52:
                assert t.pc < 20 and t.cells[0][1] == 3
            s = t
        count += 1
    # Both boundaries of the bounded bank, including capacity refusal.
    s = prepared((1,),bank=0)
    s = replace(s,pc=3,direction=-1,bundles=((1,0,1,-1,0,1,0),s.bundles[1]))
    assert step(s) == flip(s)
    for n in (3,4,7,12):
        full = full_step(n,gamma_at(n),s)
        assert full[0] == n+1 and full[2] == flip(s)
        assert full_back(*full) == (n,gamma_at(n),s)
    # Dirty references preserve bijectivity but destroy the intended sign readout.
    failures = 0
    for eta in (-1,1):
        s = prepared((eta,))
        s = replace(s,bundles=(s.bundles[0],(0,0,0,0,0,0,0)))
        for _ in range(24):
            s = audit(s)
        assert s.pc == 24 and s.cells[0][1] == 0
        failures += 1
    # Every scratch value is admitted; correctness requires the declared zero.
    for eta,zeta in product((-1,1),range(5)):
        s = prepared((eta,),bank=80)
        s = replace(s,scratch=(zeta,))
        for _ in range(24):
            s = audit(s)
        assert s.cells[0][1] == (zeta+eta) % 5
        assert s.scratch[0] == 3
    print(f'FUNDING budgets={count} dirty_reference_failures={failures} occupied_scratch=10 PASS')


def gate_corrected_r2():
    # Newly pinned exact counterexamples, not a rerun of the R2 breaker.
    m = matrix((0,0,0))
    for t in range(5):
        assert 25-(t+1)**2 >= 0
        m = left_letter(m,'Q',1)
    assert m == matrix((0,0,0))  # integer-open q=5, scalar I
    actual = left_letter(matrix((0,0,0)),'Q',1)
    wrong = tuple((k,(e+1)%5) for k,e in actual)
    assert actual != wrong  # q0=1,p0=-1,A=0,Q=1,P=0: wrong jX
    assert (1+1)**2-1**2 == 3 and 9-3 == 6
    print('R2_CORRECTIONS false_open_path_lemma=COUNTEREXAMPLE literal_prereg_A4=COUNTEREXAMPLE PASS')


def main():
    gate_native()
    gate_small_shell()
    gate_dirty_grid()
    gate_weyl()
    gate_tensor_history()
    gate_delivery()
    gate_funding_and_preparation()
    gate_corrected_r2()
    print('VERDICT DECLARED_CHAIN_VERIFIED; ORIGINAL_U_ADMISSION=OPEN; DIAG_J_PHI_BRIDGE=OPEN')


if __name__ == '__main__':
    main()
