#!/usr/bin/env python3
"""Exact finite audit of the direct, independently reviewed device law."""
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path
import sys

sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location(
    "unit_reader_model", Path(__file__).with_name("model.py"))
model = importlib.util.module_from_spec(spec)
spec.loader.exec_module(model)


def all_states():
    for total in range(9):
        for a in range(total+1):
            for b in range(total-a+1):
                y = total-a-b
                for directions in itertools.product((-1, 1), repeat=2):
                    for flags in itertools.product((0, 1), repeat=3):
                        for pointer in range(5):
                            for phase in range(2):
                                for enabled in itertools.product((0, 1), repeat=2):
                                    yield ((a, b, y) + directions + flags
                                           + (pointer, phase) + enabled)


def stock_coefficients(state):
    return (sum(v-v % 2 for v in state[:3]),
            sum(v % 2 for v in state[:3]))


def main():
    digest = hashlib.sha256()
    count = calibrated = 0
    for state in all_states():
        out = model.step(state)
        before = model.inverse(state)
        model.validate(out)
        model.validate(before)
        assert model.inverse(out) == state
        assert model.step(before) == state
        assert sum(out[:3]) == sum(state[:3])
        assert (out[8]-out[2]) % 5 == (state[8]-state[2]) % 5
        assert model.errors(out) == model.errors(state)
        assert out[10:] == state[10:]
        inactive = 1-state[9]
        assert out[inactive] == state[inactive]
        assert out[3+inactive] == state[3+inactive]
        assert out[5+inactive] == state[5+inactive]
        assert out[9] == 1-state[9]
        delta = out[2]-state[2]
        assert delta in (-1, 0, 1)
        if not state[10+state[9]]:
            assert out[:9] == state[:9]
            assert delta == 0
        if model.errors(state) == (0, 0, 0):
            calibrated += 1
            assert model.read_current(out) == delta
        digest.update((" ".join(map(str, state+out))+"\n").encode("ascii"))
        count += 1
    assert count == 211200
    assert calibrated == 26400

    preparations = 0
    for a, b, t in itertools.product(range(2), range(2), range(3)):
        state = model.prepare(a, b, t)
        one = model.step(state)
        two = model.step(one)
        assert one[2] == t+a and two[2] == t+a+b
        assert one[8] == one[2] and two[8] == two[2]
        assert two[:2] == (0, 0)
        assert two[3:5] == (1 if a else -1, 1 if b else -1)
        assert model.read_current(one) == a
        assert model.read_current(two) == b
        preparations += 1
    assert preparations == 12

    ends = []
    lasts = []
    for a, b in ((1, 0), (0, 1)):
        one = model.step(model.prepare(a, b, 1))
        two = model.step(one)
        ends.append(two)
        lasts.append(two[2]-one[2])
    assert ends[0][:3] == ends[1][:3] == (0, 0, 2)
    assert ends[0][5:] == ends[1][5:]
    assert [s[3:5] for s in ends] == [(1, -1), (-1, 1)]
    assert lasts == [0, 1]
    context = {"stocks": list(ends[0][:3]), "pointer": ends[0][8],
               "last": lasts, "directions": [list(s[3:5]) for s in ends]}

    faulty = (0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1)
    fault_out = model.step(faulty)
    fault = {"actual": fault_out[2]-faulty[2],
             "read": model.read_current(fault_out),
             "errors": list(model.errors(fault_out))}
    assert fault == {"actual": 0, "read": -1, "errors": [1, 0, 0]}

    energy_inputs = [model.prepare(3, 2, 1), model.prepare(2, 3, 1)]
    energy_outputs = [model.step(s) for s in energy_inputs]
    assert energy_inputs[0][3:] == energy_inputs[1][3:]
    assert energy_outputs[0][3:] == energy_outputs[1][3:]
    assert stock_coefficients(energy_inputs[0]) == (4, 2)
    assert stock_coefficients(energy_inputs[1]) == (4, 2)
    assert [sum(s[:3]) for s in energy_inputs+energy_outputs] == [6]*4
    defects = []
    for before, after in zip(energy_inputs, energy_outputs):
        x, y = stock_coefficients(before), stock_coefficients(after)
        defects.append([y[0]-x[0], y[1]-x[1]])
    assert defects == [[2, -2], [0, 0]]

    states = [model.prepare(2, 1, 1)]
    currents = []
    for _ in range(12):
        after = model.step(states[-1])
        currents.append(after[2]-states[-1][2])
        assert model.read_current(after) == currents[-1]
        states.append(after)
    assert states[12] == states[0]
    assert len(set(states[:-1])) == 12
    assert currents == [1, 1, 1, 0, 0, -1, -1, -1, -1, 0, 0, 1]
    cycle = {"states": [list(s) for s in states],
             "currents": currents, "period": 12}

    pairs = observations = 0
    projection = (2, 4, 6, 7, 8, 9, 10, 11)
    for b, t in itertools.product(range(2), range(3)):
        left = model.prepare(0, b, t, enabled=(0, 1))
        right = model.prepare(3, b, t, enabled=(0, 1))
        for n in range(13):
            assert tuple(left[i] for i in projection) == tuple(
                right[i] for i in projection)
            if n and 1-left[9] == 0:
                assert model.read_current(left) == model.read_current(right) == 0
            observations += 1
            if n < 12:
                left, right = model.step(left), model.step(right)
        pairs += 1
    assert (pairs, observations) == (6, 78)

    report = {"probe": "P-HYPOTHETICAL-UNIT-READER-1", "cutoff": 8,
              "states": count, "calibrated_states": calibrated,
              "transition_sha256": digest.hexdigest(),
              "two_write_preparations": preparations, "context": context,
              "fault": fault, "energy_defects": defects, "cycle": cycle,
              "disconnected_pairs": pairs,
              "disconnected_observations": observations}
    print(json.dumps(report, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
