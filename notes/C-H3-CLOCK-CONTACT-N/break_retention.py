#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Blind same-session audit of the separately preregistered E family.

NON-CANONICAL / NO AUTHORITY. Own frozen cyclic-five engine only.
No primary E implementation or output was read before this source freeze.
"""

from pathlib import Path
import hashlib
import importlib.util
from itertools import product
import json


HERE = Path(__file__).resolve().parent
ENGINE = HERE / "break.py"
assert hashlib.sha256(ENGINE.read_bytes()).hexdigest() == "a8a7ae5d1f08156ad6dbd766602e658cb2d5e5f6840097c07a2aa75c48d61b60"
assert hashlib.sha256((HERE / "PREREG-E.md").read_bytes()).hexdigest() == "948ab61c34d22f23099a19a1546db52c17194e1c594bb78435da66a3a2945878"
spec = importlib.util.spec_from_file_location("own_cyclic_five", ENGINE)
E = importlib.util.module_from_spec(spec)
spec.loader.exec_module(E)


def emit(label, value):
    print(label, json.dumps(value, sort_keys=True), flush=True)


def outside(a, b):
    return all(a[i] == b[i] for i in range(E.NX * E.NY) if i // E.NY != 4)


def sum0(field):
    return E.total(c[0] for c in E.column(field, 4))


def pair(field):
    return field[E.site(4, 0)][:2]


def bad_partition(fields, projection, label):
    representatives = {}
    values = {}
    for key, field in fields.items():
        lab = label(key)
        val = projection(field)
        if lab in representatives:
            oldkey, oldval = representatives[lab]
            if val != oldval:
                return ("within_class_split", key, oldkey)
        else:
            representatives[lab] = (key, val)
        if val in values and values[val][0] != lab:
            return ("between_class_collision", key, values[val][1])
        values[val] = (lab, key)
    return None


def incident(field, rail, bit):
    position, size = (4, E.NX) if rail == 3 else (0, E.NY)
    left = position if position % 2 == bit else (position - 1) % size
    right = (left + 1) % size
    if rail == 3:
        i, k = E.site(left, 0), E.site(right, 0)
    else:
        i, k = E.site(4, left), E.site(4, right)
    a, b = field[i][rail], field[k][rail]
    typ = "equal" if a == b else "admitted" if E.is_even(E.minus(a, b)) else "refused"
    return {"class": typ, "pair": (E.short(a), E.short(b))}


def run_case(m, first, second, wheels, records):
    E.DELTA = E.times(m, E.multiply(E.ETA, E.RHO))
    wu, wv = wheels
    rstars = {second[p, 1][1][89][E.site(4, 0)][3] for p in range(5)}
    assert len(rstars) == 1
    info, failure = E.alias_and_polynomials(wu, wv, 0, 0, 89, 0, 1, next(iter(rstars)), records)
    if failure is not None:
        return {"m": m, "alias_rejected": failure, "retention": False}
    assert info["refusal"]
    starts = [E.install(E.initial(p), wu, wv, 0, 0, info) for p in range(5)]
    first_new = [E.history(z, 114) for z in starts]
    assert len({E.accounts(z) for z in starts}) == 1
    for p, hist in enumerate(first_new):
        assert sum0(starts[p]) == E.times(-6 * info["a"], E.O)
        for t in range(1, 115):
            assert hist[2][t] == first[p][2][t]
            for stage in (0, 1):
                assert outside(hist[stage][t], first[p][stage][t])
                assert tuple(c[3] for c in hist[stage][t]) == tuple(c[3] for c in first[p][stage][t])
    loaded = {(p, q0): E.exchange(first_new[p][0][114], p, q0)
              for p, q0 in product(range(5), repeat=2)}
    assert len(set(loaded.values())) == 10
    second_new, reused = {}, {}
    for key, initial in loaded.items():
        if initial not in reused:
            reused[initial] = E.history(initial, 121)
        second_new[key] = reused[initial]
    for key, hist in second_new.items():
        for t in range(1, 90):
            bank = tuple(e for e in hist[2][t] if e[0] == 4)
            assert bank == (((4, 0, 1),) if key[1] == 1 and t == 89 else ())
            assert tuple(e for e in hist[2][t] if e[0] != 4) == second[key][2][t]
            for stage in (0, 1):
                assert outside(hist[stage][t], second[key][stage][t])
                if t != 89 or stage == 1:
                    assert tuple(c[3] for c in hist[stage][t]) == tuple(c[3] for c in second[key][stage][t])
        pre, post = (hist[stage][89][E.site(4, 0)] for stage in (1, 0))
        if key[1] == 1:
            assert E.minus(post[3], pre[3]) == E.DELTA
            assert E.minus(post[2], pre[2]) == E.times(-1, E.DELTA)
        expected = E.times(-6 * info["a"], E.O)
        if key[1] == 1:
            expected = E.plus(expected, E.DELTA)
        assert sum0(hist[0][89]) == expected
    target = {k: h[0][89] for k, h in second_new.items()}
    label_fresh = lambda k: k[1] == 1
    label_old = lambda k: k[0] == 1
    label_pair = lambda k: (k[0] == 1, k[1] == 1)
    both = lambda z: (E.material_record(z), sum0(z))
    assert bad_partition(target, sum0, label_fresh) is None
    assert bad_partition(target, E.material_record, label_old) is None
    assert bad_partition(target, both, label_pair) is None

    failures = {"bank_idle": None, "S0": None, "old_material": None,
                "combined_four": None, "accounts_inverse": None}
    first_bank, first_old, pair_lost = None, None, None
    for t in range(90, 122):
        for stage, stage_name in ((1, "post-C"), (0, "full")):
            fields = {k: h[stage][t] for k, h in second_new.items()}
            if stage == 0:
                for key, hist in second_new.items():
                    for event in hist[2][t]:
                        witness = (t, stage_name, key, event)
                        if event[0] == 4:
                            if first_bank is None:
                                first_bank = witness
                            if failures["bank_idle"] is None:
                                failures["bank_idle"] = witness
                        if event[0] in (5, 7) and first_old is None:
                            first_old = witness
            bad = next((k for k, z in fields.items() if sum0(z) != sum0(target[k])), None)
            if bad is not None and failures["S0"] is None:
                failures["S0"] = (t, stage_name, "literal_value", bad)
            partition = bad_partition(fields, sum0, label_fresh)
            if partition is not None and failures["S0"] is None:
                failures["S0"] = (t, stage_name, partition)
            partition = bad_partition(fields, E.material_record, label_old)
            if partition is not None and failures["old_material"] is None:
                failures["old_material"] = (t, stage_name, partition)
            partition = bad_partition(fields, both, label_pair)
            if partition is not None and failures["combined_four"] is None:
                failures["combined_four"] = (t, stage_name, partition)
            if pair_lost is None:
                bad = next((k for k, z in fields.items() if pair(z) != pair(target[k])), None)
                if bad is not None:
                    pair_lost = (t, stage_name, bad)
    # E.history asserts all accounts and the literal native inverse at each cut.
    assert failures["accounts_inverse"] is None
    pos = second_new[0, 1]
    before_write = pos[1][89][E.site(4, 0)]
    after_write = pos[0][89][E.site(4, 0)]
    after_c = pos[1][90][E.site(4, 0)]
    after_b = pos[0][90][E.site(4, 0)]
    incidents = [incident(pos[0][89], rail, 1) for rail in range(4)]
    unchanged = after_c == after_write
    inverse = after_b == before_write
    next_tag = next((tag for x, y, tag in pos[2][90] if (x, y) == (4, 0)), 0)
    if unchanged:
        assert inverse and next_tag == 2
    assert incidents[2]["class"] == ("refused" if m % 2 else "admitted")
    assert (after_c[2] == after_write[2]) == bool(m % 2)
    restore = {}
    for x, name in ((0, "source"), (6, "worker")):
        restore[name] = sum(E.column(h[0][114], x) == E.column(E.initial(key[1]), x)
                            for key, h in second_new.items())
    restore["both"] = sum(all(E.column(h[0][114], x) == E.column(E.initial(key[1]), x)
                              for x in (0, 6)) for key, h in second_new.items())
    budget, oldbudget = E.accounts(starts[0]), E.accounts(E.initial(0))
    return {"m": m, "retention": all(z is None for z in failures.values()),
            "scales": (info["a"], info["b"]), "translation": E.short(info["translation"]),
            "clock": E.short(info["g"]), "constraints": info["constraints"],
            "accounts": tuple(E.short(z) for z in budget[:3]), "Q": budget[3],
            "Q_increment": budget[3] - oldbudget[3],
            "account_increment": tuple(E.short(E.minus(a, b)) for a, b in zip(budget[:3], oldbudget[:3])),
            "S0_negative": E.short(sum0(target[0, 0])), "S0_positive": E.short(sum0(target[0, 1])),
            "failures": failures, "first_bank_B": first_bank, "first_old_B": first_old,
            "fixed_pair_lost": pair_lost,
            "fixed_pair_hold_ticks": pair_lost[0] - 90 if pair_lost else 32,
            "restore114": restore, "incidents_next_C": incidents,
            "whole_cell_unchanged": unchanged, "next_B_tag": next_tag,
            "next_B_exact_inverse": inverse,
            "cell_pre_write": tuple(E.short(z) for z in before_write),
            "cell_post_write": tuple(E.short(z) for z in after_write),
            "cell_next_post_C": tuple(E.short(z) for z in after_c),
            "cell_next_full": tuple(E.short(z) for z in after_b),
            "all25": len(second_new), "distinct_second": len(reused)}


def main():
    first, second = E.baseline()
    wheels = (E.wheel((1, -1, -3, 0, -3, 0), 236), E.wheel((1, -1, 3, 0, -3, 0), 236))
    records = E.log_event(first, second, 89, 0)
    selected = None
    for m in range(1, 9):
        result = run_case(m, first, second, wheels, records)
        emit("BREAK E", result)
        if result["retention"] and selected is None:
            selected = m
    emit("BREAK E SUMMARY", {"amplitudes": 8, "selected": selected, "PASS": True})


if __name__ == "__main__":
    main()
