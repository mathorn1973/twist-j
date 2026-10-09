#!/usr/bin/env python3
"""Exact finite audit of a selected five-state string-endpoint automaton.
NON-CANONICAL; no external inputs, floating point, or third-party packages.
"""
from itertools import product
import json

B = tuple(range(-2, 3))
OFFSETS = ((1, 0, 0), (0, 1, 0), (0, 0, 1),
           (-1, 1, 0), (-1, 0, 1), (0, -1, 1))


def charge(f, edges, nv):
    n = [0] * nv
    for w, (a, b) in zip(f, edges):
        n[a] -= w
        n[b] += w
    return n


def energy(n):
    return sum(x * x for x in n)


def gate(f, e, edges, nv):
    """Direct route: reconstruct every charge from the complete links."""
    n = charge(f, edges, nv)
    a, b = edges[e]
    d = n[a] - n[b]
    delta = d if -2 <= f[e] + d <= 2 else 0
    out = list(f)
    out[e] += delta
    return out, delta


def sweep(f, edges, nv, layers, reverse=False, incremental=False):
    """Two routes written by one author, not independent-agent evidence."""
    out = list(f)
    order = list(reversed(layers)) if reverse else layers
    n = charge(out, edges, nv)
    current = [0] * len(edges)
    for layer in order:
        for e in layer:
            a, b = edges[e]
            if incremental:
                d = n[a] - n[b]
                delta = d if -2 <= out[e] + d <= 2 else 0
                out[e] += delta
                n[a] -= delta
                n[b] += delta
            else:
                out, delta = gate(out, e, edges, nv)
            current[e] -= delta
    if incremental:
        assert n == charge(out, edges, nv)
    dn = charge(current, edges, nv)
    before, after = charge(f, edges, nv), charge(out, edges, nv)
    assert all(y - x == -z for x, y, z in zip(before, after, dn))
    assert sorted(before) == sorted(after)
    assert energy(before) == energy(after)
    assert all(x in B for x in out)
    return out


def boundary_cases():
    accepted = rejected = changed = count = 0
    for f, left, right in product(B, range(-22, 23), range(-22, 23)):
        a, b = left - f, right + f
        d = a - b
        proposal = f + d
        out = proposal if proposal in B else f
        delta = out - f
        aa, bb = a - delta, b + delta
        assert aa * aa + bb * bb == a * a + b * b
        assert sorted((aa, bb)) == sorted((a, b))
        inv_proposal = out + aa - bb
        inv = inv_proposal if inv_proposal in B else out
        assert inv == f
        solutions = {t for t in B
                     if (left - t)**2 + (right + t)**2 == a*a + b*b}
        allowed = {f} | ({proposal} if proposal in B else set())
        assert solutions == allowed
        accepted += proposal in B
        rejected += proposal not in B
        changed += delta != 0
        count += 1
    assert count == 10125
    return dict(cases=count, admitted=accepted, rejected=rejected,
                nonidentity=changed)


def complete_rows():
    result = []
    for size in (4, 6):
        edges = [(i, (i + 1) % size) for i in range(size)]
        layers = [list(range(p, size, 2)) for p in (0, 1)]
        images = set()
        nonidentity = 0
        for f0 in product(B, repeat=size):
            f = list(f0)
            out = sweep(f, edges, size, layers)
            assert out == sweep(f, edges, size, layers, incremental=True)
            assert sweep(out, edges, size, layers, reverse=True) == f
            back = sweep(f, edges, size, layers, reverse=True)
            assert sweep(back, edges, size, layers) == f
            images.add(tuple(out))
            nonidentity += out != f
        assert len(images) == 5**size
        result.append(dict(length=size, states=5**size,
                           distinct_images=len(images), changed=nonidentity))
    return result


def d3(shape):
    vertices = list(product(*(range(d) for d in shape)))
    index = {v: i for i, v in enumerate(vertices)}
    edges, keys, edge_index = [], [], {}
    for x in vertices:
        for typ, off in enumerate(OFFSETS):
            y = tuple((x[t] + off[t]) % shape[t] for t in range(3))
            assert y != x
            edge_index[x, typ] = len(edges)
            edges.append((index[x], index[y]))
            keys.append((x, typ))
    layers = [[i for i, (x, typ) in enumerate(keys)
               if typ == 0 and x[0] % 2 == parity] for parity in (0, 1)]
    for layer in layers:
        ends = [v for e in layer for v in edges[e]]
        assert len(ends) == len(set(ends)) == len(vertices)
    return vertices, index, edges, keys, edge_index, layers


def translate(f, amount, shape, keys, edge_index):
    out = [0] * len(f)
    for w, (x, typ) in zip(f, keys):
        y = ((x[0] + amount) % shape[0], x[1], x[2])
        out[edge_index[y, typ]] = w
    return out


def string(shape, length, start, ne, edge_index):
    f = [0] * ne
    for k in range(length):
        f[edge_index[((start + k) % shape[0], 0, 0), 0]] = 1
    return f


def full_torus(shape):
    vertices, vi, edges, keys, ei, layers = d3(shape)
    nv, ne = len(vertices), len(edges)
    contacts = steps = translated = 0
    for seed in range(8):
        f = [((i*i + seed*(i+3) + 7*seed) % 5) - 2 for i in range(ne)]
        n = charge(f, edges, nv)
        for e, (a, b) in enumerate(edges):
            out, delta = gate(f, e, edges, nv)
            nn = charge(out, edges, nv)
            assert sorted(nn) == sorted(n)
            assert energy(nn) == energy(n)
            assert nn[a] - n[a] == -delta and nn[b] - n[b] == delta
            assert nn[a]**2 - n[a]**2 == -(nn[b]**2 - n[b]**2)
            assert gate(out, e, edges, nv)[0] == f
            contacts += 1
        # Reversing within disjoint matchings changes no map.
        reverse_inside = [list(reversed(layer)) for layer in layers]
        assert sweep(f, edges, nv, layers) == sweep(f, edges, nv, reverse_inside)
        # One-cell translation exchanges the two layers, not T with itself.
        shifted = translate(f, 1, shape, keys, ei)
        assert sweep(shifted, edges, nv, layers) == translate(
            sweep(f, edges, nv, layers, reverse=True), 1, shape, keys, ei)
        for _ in range(12):
            out = sweep(f, edges, nv, layers)
            assert out == sweep(f, edges, nv, layers, incremental=True)
            assert sweep(out, edges, nv, layers, reverse=True) == f
            f = out
            steps += 1
    for length in (2, 4):
        if length >= shape[0]:
            continue
        for start in (0, 1):
            initial = string(shape, length, start, ne, ei)
            n = charge(initial, edges, nv)
            assert sorted(x for x in n if x) == [-1, 1]
            assert energy(n) == 2
            speed = 2 if start % 2 == 0 else -2
            for backwards in (False, True):
                f = initial
                direction = -1 if backwards else 1
                for tick in range(1, 17):
                    f = sweep(f, edges, nv, layers, reverse=backwards)
                    expected = translate(initial, direction*speed*tick,
                                         shape, keys, ei)
                    assert f == expected
                    assert energy(charge(f, edges, nv)) == 2
                    translated += 1
    # A triangle is a literal signed 1-cycle, even with quotient labels.
    a, b, c, p = (0,0,0), (1,0,0), (0,1,0), (shape[0]-1,0,0)
    e = ei[a, 0]
    loop = [0] * ne
    loop[ei[a, 0]] = 2
    loop[ei[b, 3]] = 2
    loop[ei[a, 1]] = -2
    assert charge(loop, edges, nv) == [0] * nv
    assert sweep(loop, edges, nv, layers) == loop
    baseline = [0] * ne
    baseline[ei[p, 0]] = 1
    blocked = [x+y for x, y in zip(baseline, loop)]
    assert all(w in B for w in blocked)
    assert charge(baseline, edges, nv) == charge(blocked, edges, nv)
    allowed_out, da = gate(baseline, e, edges, nv)
    blocked_out, db = gate(blocked, e, edges, nv)
    assert da == 1 and db == 0 and blocked_out == blocked
    assert charge(allowed_out, edges, nv)[vi[b]] == 1
    assert charge(blocked_out, edges, nv)[vi[a]] == 1
    assert energy(charge(baseline, edges, nv)) == 2
    # The added old wave energy changes although H_def does not.
    wave_delta = sum(w*w for w in allowed_out) - sum(w*w for w in baseline)
    assert wave_delta == 1
    lengths = []
    for length in range(1, shape[0]):
        f = string(shape, length, 0, ne, ei)
        assert energy(charge(f, edges, nv)) == 2
        assert sum(w*w for w in f) == length
        lengths.append([length, 2, length])
    return dict(shape=list(shape), vertices=nv, labelled_edges=ne,
                full_edge_contact_checks=contacts, trajectory_steps=steps,
                exact_forward_backward_translate_checks=translated,
                same_charge_loop_blocks=True, neutral_loop_is_fixed=True,
                endpoint_extension_old_wave_energy_error=wave_delta,
                string_length_defect_energy_wave_energy=lengths)


def main():
    output = {
        "status": "PASS; NON-CANONICAL finite audit, not an elementary particle",
        "boundary_contact_class": boundary_cases(),
        "complete_periodic_rows": complete_rows(),
        "d3_tori": [full_torus(sh) for sh in ((4,2,2),(6,2,2),(8,3,2))],
        "infinite_time_translation": "written proof, not inferred from samples",
        "isolated_endpoint": "written proof with half-infinite field tail",
        "neutral_photon_sector": "absent: this hop law fixes every neutral state",
        "old_photon_energy_bridge": "fails for the frozen endpoint extension",
    }
    print(json.dumps(output, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
