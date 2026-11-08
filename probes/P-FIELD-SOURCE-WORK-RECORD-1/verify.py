#!/usr/bin/env python3
"""Exact finite audit of the explicitly added local source-work gate.

PUBLIC / NON-CANONICAL / L1. A. M. Thorn, Apache-2.0.
No native-U or physical-admission claim. Run only after the public pin.
"""

from functools import lru_cache
from itertools import product


Z4 = (0, 0, 0, 0)
ZERO3 = (Z4, Z4, Z4)
R = ((1, -2, 1, 0), Z4, Z4)
AM = ((1, 0, 0, 0), (0, -1, 0, 0), (0, -1, 1, 0))
ZM = ZERO3
OTHER = (Z4, (1, -2, 1, 0), Z4)
CHARGED = ((1, 0, 0, 0), (0, -1, 0, 0), (1, 1, 0, 0))
V1 = (2, -1, 0, 0)
V2 = (2, -1, -5, 5)
Y1 = (0, 0, -2, 1)


class Falsifier(Exception):
    pass


def need(condition, message):
    if not condition:
        raise Falsifier(message)


def Q(v):
    a, b, c, d = v
    return (6 * (a*a + b*b + c*c + d*d)
            + 4 * (a*b + a*d + b*c + c*d) - 2 * (a*c + b*d))


def H(y):
    a, b, c, d = y
    return 2*a*a - 2*a*b + 3*b*b + c*c + d*d + 2*a*c - a*d - b*c + 3*b*d


def Hraw(z):
    e0, e1, e2, e3, m0, m1 = z
    return (e0*e0 + e1*e1 + e2*e2 + e3*e3 + m0*m0 + m1*m1
            + e0*(m0-m1) - e1*m0 + (e2+e3)*m1)


def join(y, static=(0, 0)):
    a, b, c, d = y
    u, v = static
    return (a-b+u, -a+u, b+v, b+u-v, c, d)


def split(z):
    e0, e1, e2, e3, c, d = z
    numerators = (2*e0-3*e1+e2+e3, -e0-e1+2*e2+2*e3,
                  2*e0+2*e1+e2+e3, e0+e1+3*e2-2*e3)
    if any(t % 5 for t in numerators):
        return None
    a, b, u, v = (t // 5 for t in numerators)
    return (a, b, c, d), (u, v)


def Af(y):
    a, b, c, d = y
    return (a+c, b+d, -2*a+b-c+d, a-3*b+c-2*d)


def L(y):
    a, b, c, d = y
    return (a-3*b-c-2*d, -3*a+4*b-2*c+d,
            5*b+c+2*d, 5*a-5*b+2*c-d)


def L_inverse(y):
    a, b, c, d = y
    if (a+2*b) % 5 or (c+2*d) % 5:
        return None
    n = (a+2*b+c+2*d, 2*a-b+2*c-d, -5*b+c-3*d, -5*a+5*b-3*c+4*d)
    return tuple(t // 5 for t in n)


def signed_B(y):
    a, b, c, d = y
    return (-c, -d, -a, -b)


def price_B(y):
    a, b, c, d = y
    return (c-d)**2 + d*d - (a-b)**2 - b*b


def raw_F(z):
    e0, e1, e2, e3, m0, m1 = z
    a0, a1, a2, a3 = e0+m0-m1, e1-m0, e2+m1, e3+m1
    return (a0, a1, a2, a3, m0-a0+a1, m1+a0-a2-a3)


def raw_F_inverse(z):
    e0, e1, e2, e3, n0, n1 = z
    m0, m1 = n0+e0-e1, n1-e0+e2+e3
    return (e0-m0+m1, e1+m0, e2-m1, e3-m1, m0, m1)


def cell(matter=ZM, y=Z4, resource=0, static=(0, 0), spectators=ZERO3):
    return matter, spectators, join(y, static), resource


@lru_cache(maxsize=None)
def vector_group_energy(vectors):
    return sum(Q(v) for v in vectors)


def cell_energy(c):
    m, b, z, r = c
    return vector_group_energy(m) + vector_group_energy(b) + Hraw(z) + r


def cell_residue(c):
    m, b, z, r = c
    return (tuple(tuple(t % 5 for t in v) for v in m),
            tuple(tuple(t % 5 for t in v) for v in b),
            tuple(t % 5 for t in z), r % 5)


def divergence(c):
    e0, e1, e2, e3 = c[2][:4]
    return (e0+e1+e2, -e0-e1-e3, -e2+e3)


def charge(c):
    m, b = c[:2]
    return (sum(b[0]) + sum(sum(v) for v in m), sum(b[1]), sum(b[2]))


def matter_sum(c):
    return tuple(sum(v[k] for v in c[0]) for k in range(4))


def local_observables(c):
    div, rho = divergence(c), charge(c)
    return (rho, div, tuple(a-b for a, b in zip(div, rho)), matter_sum(c), c[1])


def G(c):
    m, b, z, r = c
    if m != R and m != AM:
        return c
    parts = split(z)
    if parts is None:
        return c
    y, static = parts
    if m == R:
        x = L_inverse(y)
        if x is None:
            return c
        new_r = r + 4*H(x) - 2
        if new_r < 0:
            return c
        return AM, b, join(x, static), new_r
    new_r = r + 2 - 4*H(y)
    if new_r < 0:
        return c
    return R, b, join(L(y), static), new_r


def event(c):
    return int(c[0] == R and G(c)[0] == AM)


def Ghat(c, pointer, inverse=False):
    out = G(c)
    if inverse:
        return out, (pointer-event(out)) % 5
    return out, (pointer+int(c[0] == R and out[0] == AM)) % 5


def K_B(c):
    """New declared gate; all nonsplit and unaffordable inputs are fixed."""
    m, b, z, r = c
    parts = split(z)
    if parts is None:
        return c
    y, static = parts
    delta = H(signed_B(y)) - H(y)
    if r < delta:
        return c
    return m, b, join(signed_B(y), static), r-delta


def field_step(c, inverse=False):
    m, b, z, r = c
    return m, b, (raw_F_inverse(z) if inverse else raw_F(z)), r


def chain_energy(s):
    cells, channels, pointer = s
    return sum(cell_energy(c) for c in cells) + sum(channels) + 1


def chain_observables(s):
    return tuple(local_observables(c) for c in s[0])


def replace_resource(c, resource):
    return c[0], c[1], c[2], resource


def chain_step(s, cut=None, enabled=True, inverse=False):
    cells, channels, pointer = list(s[0]), list(s[1]), s[2]
    n = len(cells)

    def contact_A():
        for j in range(n-1):
            if j != cut:
                old = cells[j][3]
                cells[j] = replace_resource(cells[j], channels[j])
                channels[j] = old

    def contact_B():
        for j in range(n-1):
            if j != cut:
                old = cells[j+1][3]
                cells[j+1] = replace_resource(cells[j+1], channels[j])
                channels[j] = old

    if inverse:
        cells = [field_step(c, inverse=True) for c in cells]
        contact_B()
        contact_A()
        cells[-1], pointer = Ghat(cells[-1], pointer, inverse=True)
        cells[:-1] = [G(c) for c in cells[:-1]]
        if enabled:
            cells[0] = K_B(cells[0])
    else:
        if enabled:
            cells[0] = K_B(cells[0])
        cells[:-1] = [G(c) for c in cells[:-1]]
        cells[-1], pointer = Ghat(cells[-1], pointer)
        contact_A()
        contact_B()
        cells = [field_step(c) for c in cells]
    return tuple(cells), tuple(channels), pointer


def check_local(c, op, inverse):
    out = op(c)
    need(inverse(out) == c and op(inverse(c)) == c, 'local two-sided inverse')
    need(cell_energy(out) == cell_energy(c), 'local energy')
    need(out[3] >= 0 and local_observables(out) == local_observables(c),
         'local resources/charge/divergence/defect/spectators/matter sum')
    return out


def check_chain(s, cut=None, enabled=True):
    out = chain_step(s, cut, enabled)
    prev = chain_step(s, cut, enabled, inverse=True)
    need(chain_step(out, cut, enabled, inverse=True) == s, 'chain backward-forward')
    need(chain_step(prev, cut, enabled) == s, 'chain forward-backward')
    need(chain_energy(out) == chain_energy(prev) == chain_energy(s), 'chain energy')
    need(chain_observables(out) == chain_observables(prev) == chain_observables(s),
         'chain charge/divergence/defect/matter sums/spectators')
    need(all(c[3] >= 0 for c in out[0]+prev[0])
         and all(q >= 0 for q in out[1]+prev[1]), 'chain nonnegative resources')
    if cut is not None:
        need(out[1][cut] == prev[1][cut] == s[1][cut], 'cut channel overwritten')
    return out


def local_audit():
    n_full = n_context = refused = offsplit = n_raw = 0
    ys = tuple(product(range(-2, 3), repeat=4))
    statics = tuple(product(range(-1, 2), repeat=2))
    for y in ys:
        need(H(signed_B(y))-H(y) == price_B(y), 'signed-swap price polynomial')
        need(signed_B(signed_B(y)) == y, 'signed-swap inverse')
        need(H(Af(y)) == H(y) and H(L(y)) == 5*H(y), 'field energy identities')
        need(L_inverse(L(y)) == y, 'field-image inverse')
        for static in statics:
            z = join(y, static)
            u, v = static
            need(split(z) == (y, static), 'integral split/join')
            need(Hraw(z) == H(y)+3*u*u-2*u*v+2*v*v, 'static energy account')
            need(raw_F(z) == join(Af(y), static), 'raw/active free intertwining')
            for resource in range(5):
                c = cell(ZM, y, resource, static, CHARGED)
                out = check_local(c, K_B, K_B)
                if resource < price_B(y):
                    need(out == c, 'declined gate changed full cell')
                    refused += 1
                else:
                    need(split(out[2]) == (signed_B(y), static)
                         and out[3] == resource-price_B(y), 'accepted gate incomplete')
                n_full += 1
        # Gate contexts factor because K_B fixes matter and spectators exactly.
        for matter in (R, AM, ZM, OTHER):
            for resource in range(5):
                c = cell(matter, y, resource, (1, -1), CHARGED)
                check_local(c, K_B, K_B)
                check_local(c, G, G)
                if matter in (ZM, OTHER):
                    need(G(c) == c, 'reaction accepted a nonliteral matter endpoint')
                for pointer in (0, 4):
                    out, p = Ghat(c, pointer)
                    need(Ghat(out, p, inverse=True) == (c, pointer), 'Ghat forward inverse')
                    old, pold = Ghat(c, pointer, inverse=True)
                    need(Ghat(old, pold) == (c, pointer), 'Ghat backward inverse')
                n_context += 1
    for z in product(range(-1, 2), repeat=6):
        for resource in (0, 1, 4):
            c = R, CHARGED, z, resource
            check_local(c, K_B, K_B)
            check_local(c, G, G)
            check_local(c, field_step, lambda w: field_step(w, inverse=True))
            if split(z) is None:
                need(K_B(c) == G(c) == c, 'nonsplit raw input was changed by gate/reaction')
                offsplit += 1
            n_raw += 1
    need((n_full, n_context, n_raw, refused, offsplit)
         == (28125, 12500, 2187, 9252, 1728), 'local inventory')
    need(G(cell(R, Z4, 0)) == cell(R, Z4, 0)
         and G(cell(R, Z4, 1)) == cell(R, Z4, 1), 'unfunded forward reaction guard')
    need(G(cell(R, (1, 0, 0, 0), 4)) == cell(R, (1, 0, 0, 0), 4),
         'field image guard')
    need(G(cell(AM, Y1, 4)) == cell(AM, Y1, 4), 'unfunded reverse reaction guard')
    need(G(cell(R, Z4, 2)) == cell(AM)
         and G(cell(AM)) == cell(R, Z4, 2), 'funded zero-field reaction endpoints')
    print('LOCAL PASS split_K={} context_K_G={} raw={} refused={} nonsplit={}'.format(
        n_full, n_context, n_raw, refused, offsplit))


def occupied_audit():
    fixtures = (
        cell(ZM), cell(R), cell(AM), cell(OTHER, V1, 4, (1, -1), CHARGED),
        cell(R, Y1, 0, (-1, 1), CHARGED), cell(AM, Z4, 3, (1, 1), ZERO3),
        cell(ZM, V1, 0, (0, 0), CHARGED),
        (R, CHARGED, (1, 0, 0, 0, 1, -1), 4),
    )
    count = 0
    for a, b in product(fixtures, repeat=2):
        for q, pointer, cut, enabled in product((0, 1, 4), range(5), (None, 0), (False, True)):
            check_chain(((a, b), (q,), pointer), cut, enabled)
            count += 1
    need(count == 3840, 'occupied-chain inventory')
    print('OCCUPIED PASS complete_two_cell_cases={} both_directions cuts both_laws'.format(count))


def preparation(n, source, pointer=0):
    cells = [cell(ZM, source)] + [cell(ZM) for _ in range(n-2)] + [cell(R)]
    return tuple(cells), (0,) * (n-1), pointer


def phase_witness():
    need(Af(V1) == V2 and H(V1) == H(V2) == 15, 'source equal-energy phase pair')
    need(tuple(v % 5 for v in V1) == tuple(v % 5 for v in V2), 'source active residue')
    need(tuple(v % 5 for v in join(V1)) == tuple(v % 5 for v in join(V2)), 'source raw residue')
    need(join(V1)[:4] == join(V2)[:4], 'source electric fields differ')
    orbit = (V1, V2, (-3, 4, 5, -10), (2, -6, -5, 10), (-3, 4, 5, -5))
    need(tuple(price_B(y) for y in orbit) == (-10, 115, 260, 225, 60), 'phase prices')
    need(all(Af(orbit[i]) == orbit[(i+1) % 5] for i in range(5)), 'five-phase orbit')
    out = K_B(cell(ZM, V1))
    need(split(out[2]) == (Y1, (0, 0)) and out[3] == 10 and Hraw(out[2]) == 5,
         'source-funded ten-unit conversion')
    need(K_B(cell(ZM, V2)) == cell(ZM, V2), 'second phase must first refuse')
    early, late = cell(ZM, V1), cell(ZM, V2)
    need(cell_residue(early) == cell_residue(late), 'full-cell initial checkpoint mismatch')
    need(cell_residue(K_B(early)) != cell_residue(K_B(late)),
         'claimed checkpoint projection obstruction absent')
    need(K_B(cell()) == cell(), 'zero-source gate')
    print('PHASE PASS common_H=15 common_r=0 common_mod5 delta=(-10,115,260,225,60)')


def trajectory(n, source, pointer=0, cut=None, enabled=True):
    s = preparation(n, source, pointer)
    history = [s]
    writes = [0]
    for unused in range(n+12):
        e = event(s[0][-1])
        out = check_chain(s, cut, enabled)
        need(out[2] == (s[2]+e) % 5, 'pointer did not record actual accepted reaction')
        writes.append(writes[-1]+e)
        history.append(out)
        s = out
    return history, writes


def source_to_record_audit():
    trajectories = steps = cut_runs = shifted_runs = 0
    for n in range(2, 9):
        bases = []
        for source, expected_arrival, expected_write in ((V1, n-1, n), (V2, n+3, n+4)):
            history, writes = trajectory(n, source)
            trajectories += 1
            steps += n+12
            need(chain_energy(history[0]) == 34, 'initial complete source energy')
            arrival = next((t for t, s in enumerate(history) if s[0][-1][3] > 0), None)
            first_write = next((t for t, w in enumerate(writes) if w), None)
            need(arrival == expected_arrival and first_write == expected_write,
                 'source phase arrival/first-write delay')
            need(all(history[t][2] != 0 for t in range(expected_write, expected_write+8)),
                 'eight-boundary ready-pointer retention after first write')
            need(history[arrival][0][-1][3] == 10, 'first arrival is not ten units')
            receiver = history[arrival][0][-1]
            reacted = G(receiver)
            need(receiver[0] == R and reacted[0] == AM
                 and receiver[3]-reacted[3] == 2
                 and vector_group_energy(reacted[0])-vector_group_energy(receiver[0]) == 2
                 and reacted[3] == 8, 'ten-unit source versus two-unit receiver account')
            bases.append((history, writes))
            for p in range(1, 5):
                shifted, shifted_writes = trajectory(n, source, p)
                trajectories += 1
                shifted_runs += 1
                steps += n+12
                need(shifted_writes == writes, 'initial pointer changes event history')
                for base, moved in zip(history, shifted):
                    need(base[:2] == moved[:2] and moved[2] == (base[2]+p) % 5,
                         'occupied pointer covariance')
            for cut in range(n-1):
                blocked, blocked_writes = trajectory(n, source, cut=cut)
                trajectories += 1
                cut_runs += 1
                steps += n+12
                need(not any(blocked_writes) and all(s[2] == 0 for s in blocked),
                     'cut control wrote a record')
                for s in blocked:
                    need(s[0][cut+1:] == blocked[0][0][cut+1:]
                         and s[1][cut:] == (0,) * (n-1-cut),
                         'cut control changed a full downstream state')
            off, off_writes = trajectory(n, source, enabled=False)
            trajectories += 1
            steps += n+12
            need(not any(off_writes) and all(s[2] == 0 for s in off), 'omitted-gate control')
            expected = off[0]
            for s in off:
                need(s == expected, 'omitted-gate control differs from complete free trajectory')
                expected = (tuple(field_step(c) for c in expected[0]), expected[1], expected[2])
        positive, negative = bases[0][0], bases[1][0]
        need(negative[4] == positive[0], 'late preparation does not reach early full state')
        need(all(negative[t+4] == positive[t] for t in range(len(negative)-4)),
             'whole-state four-tick history delay')
        need(all(bases[1][1][t+4] == bases[0][1][t] for t in range(len(negative)-4)),
             'actual writes do not share four-tick delay')
        for t in range(n, n+4):
            need(positive[t][2] != 0 and negative[t][2] == 0, 'four-boundary HIT/BLANK reading')
        empty, empty_writes = trajectory(n, Z4)
        trajectories += 1
        steps += n+12
        need(not any(empty_writes) and all(s[2] == 0 for s in empty), 'zero-source control')
        need(all(s == empty[0] for s in empty), 'zero-source full state is not fixed')
        if n == 2:
            state = positive[2]
            need(state[0][-1][0] == AM and state[0][-1][3] == 0
                 and state[1] == (8,) and state[2] == 1, 'two-cell boundary-two witness')
            state = positive[3]
            need(state[0][-1] == cell(R) and state[0][0][3] == 8
                 and state[1] == (2,) and state[2] == 1, 'receiver return with retained pointer')
        print('CHAIN PASS N={} arrival=({},{}) first_write=({},{}) distinguish={}..{}'.format(
            n, n-1, n+3, n, n+4, n, n+3))
    need((trajectories, steps, cut_runs, shifted_runs) == (147, 2555, 56, 56), 'trajectory inventory')
    print('RECORD PASS trajectories={} steps={} cut_runs={} nonblank_pointer_runs={}'.format(
        trajectories, steps, cut_runs, shifted_runs))


def main():
    try:
        local_audit()
        occupied_audit()
        phase_witness()
        source_to_record_audit()
    except Falsifier as exc:
        print('FALSIFIER: {}'.format(exc))
        print('AUDIT FAIL')
        return 0
    print('BOUNDARY added local integer gate; original U admission and physical reading UNSUPPLIED')
    print('AUDIT PASS')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
