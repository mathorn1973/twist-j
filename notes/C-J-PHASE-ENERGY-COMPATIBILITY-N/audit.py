#!/usr/bin/env python3
"""Frozen-intent notes audit; run only after a public source pin (PREREG.md).

Author: A. M. Thorn. SPDX-License-Identifier: Apache-2.0.
Exact finite audit of part A; part B has a written analytic proof only.
"""
from itertools import product


def energy(s):
    return sum(t * t for t in s[:4]) + s[4]


def gate(s, axis, epsilon):
    q, p, u, v, b, sigma, eta, c = s
    h = epsilon * sigma
    if axis == "Q":
        trial = (q + h, p, u, v)
    else:
        trial = (q, p + h, u + h * q, v + h * q)
    delta = sum(t * t for t in trial) - sum(t * t for t in s[:4])
    if b >= delta:
        return trial + (b - delta, sigma, eta, c)
    return (q, p, u, v, b, -sigma, eta, c)


def request(eta, c):
    return (("Q", 1), ("P", eta), ("Q", -1), ("P", -eta))[c]


def forward(s):
    out = gate(s, *request(s[6], s[7]))
    return out[:7] + ((s[7] + 1) % 4,)


def backward(s):
    old = s[:7] + ((s[7] - 1) % 4,)
    axis, epsilon = request(old[6], old[7])
    return gate(old, axis, -epsilon)


def area(s, t):
    return s[0] * (t[1] - s[1])


def orbit(seed, inventory):
    seen, path, s = set(), [], seed
    while s not in seen:
        if s not in inventory:
            return path, False
        seen.add(s)
        path.append(s)
        s = forward(s)
    return path, s == seed


def cycle_data(path):
    return (len(path), energy(path[0]),
            sum(area(s, forward(s)) for s in path))


def allowed(cycles):
    return [(k, b) for k, b in product(range(5), repeat=2)
            if all((a - n * (k * e + b)) % 5 == 0 for n, e, a in cycles)]


def main():
    inventory = []
    for coords in product(range(-2, 3), repeat=4):
        h = sum(t * t for t in coords)
        for b in range(7 - h):
            for sigma, eta, c in product((-1, 1), (-1, 1), range(4)):
                inventory.append(coords + (b, sigma, eta, c))
    states = set(inventory)
    flags = {name: True for name in
             ("energy", "inverse", "coboundary", "cycles", "zero_cycle_sum")}
    for s in inventory:
        t = forward(s)
        flags["energy"] &= energy(t) == energy(s) and t in states
        flags["inverse"] &= backward(t) == s and forward(backward(s)) == s
        flags["coboundary"] &= area(s, t) == t[2] - s[2] == t[3] - s[3]
    visited, cycles = set(), []
    for s in inventory:
        if s in visited:
            continue
        path, closes = orbit(s, states)
        flags["cycles"] &= closes and not (set(path) & visited)
        visited.update(path)
        if path:
            datum = cycle_data(path)
            cycles.append(datum)
            flags["zero_cycle_sum"] &= datum[2] == 0
    flags["cycles"] &= visited == states
    print("NON-CANONICAL L1 exact finite audit; E<=6")
    print("states", len(inventory), "cycles", len(cycles))
    pairs = allowed(cycles)
    print("whole_inventory_allowed", pairs)
    flags["whole_inventory_pairs"] = pairs == [(0, 0)]
    witnesses = (
        ("zero", (0, 0, 0, 0, 0, 1, 1, 0)),
        ("one", (0, 0, 1, 0, 0, 1, 1, 0)),
        ("cold_B0", (0, 0, 1, -1, 0, 1, 1, 0)),
        ("cold_B4", (0, 0, 1, -1, 4, 1, 1, 0)),
    )
    cold = []
    for label, seed in witnesses:
        path, closes = orbit(seed, states)
        flags["witness_" + label] = closes and bool(path)
        if path:
            datum = cycle_data(path)
            print(label, "period_energy_area", datum)
            if label.startswith("cold"):
                cold.append(datum)
    cold_pairs = allowed(cold)
    print("cold_orbits_allowed", cold_pairs)
    flags["cold_pairs"] = len(cold) == 2 and cold_pairs == [(0, 0)]
    for label, ok in flags.items():
        print(label, "PASS" if ok else "FAIL")
    print("AUDIT", "PASS" if all(flags.values()) else "FAIL")


if __name__ == "__main__":
    main()
