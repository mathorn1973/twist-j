#!/usr/bin/env python3
"""NON-CANONICAL exact audit of the new funded contact, not the old census.

Original work A. M. Thorn, Apache-2.0, 2026-10-14.
Read CONTRACT.md. No source/response-table imports and no native U replay.
"""

from dataclasses import dataclass, replace
from fractions import Fraction as Q
from itertools import product
import json


def require(ok, message):
    if not ok:
        raise AssertionError(message)


ELL = (0, 1, 2, -2, -1)
READY = ((0, 4), (1, 4), (1, 0), (2, 0), (0, 1))
Y = ((0, 0, 0), (1, 1, 0), (1, 0, 1), (0, 1, 1), (2, 0, 0))
SITES = Y + ((0, 0, 2), (4, 0, 0))
SHELLS = {2: 6, 4: 1, 8: 15, 10: 1, 16: 1}
DIM = len(SITES)
ZERO = (Q(0),) * DIM


def add(a, b, scale=Q(1)):
    return tuple(x + scale * y for x, y in zip(a, b))


def scale(a, s):
    return tuple(s * x for x in a)


def dot(a, b):
    return sum((x * y for x, y in zip(a, b)), Q(0))


def unit(i):
    return tuple(Q(int(j == i)) for j in range(DIM))


def kick(receiver):
    q, r = receiver
    z0, z1 = Q(ELL[q], 2), Q(ELL[r] + 1, 2)
    mean = (z0 + z1) / 5
    return (z0 - mean, z1 - mean, -mean, -mean, -mean, Q(0), Q(0))


def laplacian():
    stencil = {}
    for d in product(range(-4, 5), repeat=3):
        norm = sum(t * t for t in d)
        if norm in SHELLS and sum(d) % 2 == 0:
            stencil[d] = Q(SHELLS[norm], 324)
    diagonal = sum(stencil.values(), Q(0))
    # Both extra sites lie in Y + one stencil step, hence in inherited D.
    require(all(y in stencil for y in SITES[5:]), "outside-D fixture")
    matrix = []
    for i, x in enumerate(SITES):
        row = []
        for j, y in enumerate(SITES):
            delta = tuple(x[k] - y[k] for k in range(3))
            row.append(diagonal if i == j else -stencil.get(delta, Q(0)))
        matrix.append(tuple(row))
    require(all(matrix[i][j] == matrix[j][i]
                for i in range(DIM) for j in range(DIM)), "L symmetry")
    return tuple(matrix)


def matvec(matrix, vector):
    return tuple(dot(row, vector) for row in matrix)


def energy(u, v, matrix):
    difference = add(v, u, Q(-1))
    return (dot(difference, difference) + dot(u, matvec(matrix, v))) / 2


def delta_energy(u, v, a, sign, matrix):
    # Separate formula from direct energy evaluation used by the tests.
    centered = add(add(v, u, Q(-1)), matvec(matrix, u), Q(1, 2))
    return sign * dot(centered, a) + dot(a, a) / 2


@dataclass(frozen=True)
class State:
    native: tuple
    u: tuple
    v: tuple
    work: Q
    battery: Q
    sign: int
    incoming: tuple
    outgoing: tuple
    pointer: int
    other: tuple


def make_state(receiver, u, v, battery, sign=1, work=Q(7, 11)):
    return State(
        native=(7, 1, 4, 2, 3, *receiver), u=u, v=v,
        work=work, battery=battery, sign=sign,
        incoming=((Q(1, 3), Q(-2), Q(0), Q(1)),
                  (Q(-1, 2), Q(0), Q(3), Q(2))),
        outgoing=((Q(3, 7), Q(1), Q(-1), Q(2)),
                  (Q(1), Q(2), Q(3), Q(4))),
        pointer=1, other=("retained-program", 4, 19),
    )


def full_energy(state, matrix):
    tape_energy = sum((2 * dot(slot, slot)
                       for slot in state.incoming + state.outgoing), Q(0))
    return energy(state.u, state.v, matrix) + tape_energy


def funded(state, capacity, matrix):
    require(0 <= state.battery <= capacity, "input battery domain")
    require(state.sign in (-1, 1), "input direction domain")
    a = kick(state.native[-2:])
    delta = delta_energy(state.u, state.v, a, state.sign, matrix)
    offered = state.battery - delta
    if not 0 <= offered <= capacity:
        return state
    return replace(state, v=add(state.v, a, Q(state.sign)),
                   battery=offered, work=state.work + delta, sign=-state.sign)


def naive_without_direction(state, capacity, matrix):
    a = kick(state.native[-2:])
    delta = energy(state.u, add(state.v, a), matrix) - energy(state.u, state.v, matrix)
    if not 0 <= state.battery - delta <= capacity:
        return state
    return replace(state, v=add(state.v, a), battery=state.battery - delta,
                   work=state.work + delta)


def rank(rows):
    a = [list(row) for row in rows]
    pivot = 0
    for col in range(DIM):
        candidate = next((i for i in range(pivot, len(a)) if a[i][col]), None)
        if candidate is None:
            continue
        a[pivot], a[candidate] = a[candidate], a[pivot]
        denominator = a[pivot][col]
        a[pivot] = [v / denominator for v in a[pivot]]
        for i in range(len(a)):
            if i != pivot and a[i][col]:
                coefficient = a[i][col]
                a[i] = [x - coefficient * y for x, y in zip(a[i], a[pivot])]
        pivot += 1
        if pivot == len(a):
            break
    return pivot


def main():
    matrix = laplacian()
    receivers = tuple(product(range(5), repeat=2))
    ready_kicks = tuple(kick(r) for r in READY)
    all_kicks = tuple(kick(r) for r in receivers)
    require(len(set(ready_kicks)) == 5 and len(set(all_kicks)) == 25,
            "control cardinality")
    require(rank(ready_kicks) == rank(all_kicks) == 2, "translation rank")
    require(kick((0, 4)) != kick((0, 1)), "q-only witness")
    require(kick((1, 0)) != kick((2, 0)), "r-only witness")
    ready_max = max(energy(ZERO, a, matrix) for a in ready_kicks)
    all_max = max(energy(ZERO, a, matrix) for a in all_kicks)
    require(ready_max == Q(2, 5), "prepared minimum budget")
    require(all_max == Q(8, 5), "all-receiver minimum budget")
    require(energy(ZERO, kick((3, 2)), matrix) == all_max, "maximum witness")
    for receiver in READY:
        state = make_state(receiver, ZERO, ZERO, ready_max, work=Q(0))
        result = funded(state, ready_max, matrix)
        require(result.sign == -1 and result.v == kick(receiver), "ready admission")
    for receiver in receivers:
        state = make_state(receiver, ZERO, ZERO, all_max, work=Q(0))
        require(funded(state, all_max, matrix).sign == -1, "all-blank admission")

    us = (ZERO, unit(5), scale(add(unit(0), unit(6), Q(2)), Q(1, 3)),
          tuple(Q((-1) ** i, 2) for i in range(DIM)))
    fixed_vs = (ZERO, unit(0), scale(unit(1), Q(-1)), unit(5),
                tuple(Q(i - 3, 7) for i in range(DIM)))
    cases = accepted = underflow = overflow = 0
    for receiver, sign, capacity in product(receivers, (-1, 1), (ready_max, all_max)):
        a = kick(receiver)
        for u, v, battery in product(us, fixed_vs + (a,), (Q(0), capacity / 2, capacity)):
            state = make_state(receiver, u, v, battery, sign)
            delta_direct = energy(u, add(v, a, Q(sign)), matrix) - energy(u, v, matrix)
            require(delta_direct == delta_energy(u, v, a, sign, matrix), "work formula")
            result = funded(state, capacity, matrix)
            require(funded(result, capacity, matrix) == state, "full occupied involution")
            require(0 <= result.battery <= capacity, "battery range")
            before, after = full_energy(state, matrix), full_energy(result, matrix)
            require(before + state.battery == after + result.battery, "positive energy")
            require(before - state.work == after - result.work, "signed work ledger")
            require(state.battery + state.work == result.battery + result.work,
                    "battery-ledger relation")
            require((state.native, state.u, state.incoming, state.outgoing,
                     state.pointer, state.other) ==
                    (result.native, result.u, result.incoming, result.outgoing,
                     result.pointer, result.other), "retained full state")
            proposed_battery = state.battery - delta_direct
            if proposed_battery < 0:
                underflow += 1
                require(result == state, "underfunded identity")
            elif proposed_battery > capacity:
                overflow += 1
                require(result == state, "full-store identity")
            else:
                accepted += 1
                require(result.v == add(v, a, Q(sign)) and result.sign == -sign,
                        "funded exact translation")
                require(result.work == state.work + delta_direct, "exact old ledger")
            cases += 1
    require(cases == 7200 and accepted and underflow and overflow, "test coverage")

    receiver = (0, 1)
    a = kick(receiver)
    start = make_state(receiver, ZERO, ZERO, ready_max, work=Q(0))
    endpoint = make_state(receiver, ZERO, a, Q(0), work=ready_max)
    require(naive_without_direction(start, ready_max, matrix) == endpoint,
            "naive forward witness")
    require(naive_without_direction(endpoint, ready_max, matrix) == endpoint,
            "naive collision must be exposed")
    require(funded(start, ready_max, matrix) != endpoint, "direction must be retained")
    occupied_cost = energy(ZERO, scale(a, Q(2)), matrix) - energy(ZERO, a, matrix)
    require(occupied_cost == Q(6, 5) and occupied_cost > ready_max, "occupied cost")
    full_store = make_state(receiver, ZERO, scale(a, Q(-1)), ready_max)
    require(funded(full_store, ready_max, matrix) == full_store, "overflow witness")
    require(delta_energy(full_store.u, full_store.v, a, 1, matrix) == -ready_max,
            "overflow must release energy")
    outside_ready = make_state((3, 2), ZERO, ZERO, ready_max)
    require(funded(outside_ready, ready_max, matrix) == outside_ready,
            "full receiver domain must not be confused with prepared domain")

    direction = (Q(4, 5), Q(-1, 5), Q(-1, 5), Q(-1, 5), Q(-1, 5), Q(0), Q(0))
    for q0 in range(5):
        q, blind, carry = q0, ZERO, ZERO
        for _ in range(5):
            next_q = (q + 1) % 5
            blind = add(blind, direction, Q(1, 2))
            carry = add(carry, direction, Q(ELL[next_q] - ELL[q], 2))
            q = next_q
        require(q == q0 and carry == ZERO, "cycle-respecting lift")
        require(blind == scale(direction, Q(5, 2)) and blind != ZERO,
                "naive native relation violation")

    print(json.dumps({
        "status": "PASS", "scope": "NON-CANONICAL_L1_NEW_CONTACT_ONLY",
        "contact_cases": cases, "accepted": accepted,
        "rejected_underfunded": underflow, "rejected_full_store": overflow,
        "prepared_interface": 5, "full_interface": 25, "translation_rank": 2,
        "blank_budget_prepared": str(ready_max), "blank_budget_all": str(all_max),
        "negative_controls": 5, "native_cycle_start_values": 5,
        "native_admission": "OPEN", "physical_status": "NOT_READY",
    }, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
