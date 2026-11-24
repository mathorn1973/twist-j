#!/usr/bin/env python3
"""A proposed reversible unit-flow reader; physical hypothesis, not native U.

State order:
r1, r2, y, d1, d2, e1, e2, z, p, tau, chi1, chi2.
Stocks are nonnegative integers, directions +/-1, pointer modulo five.
All flag and switch bits are independent members of the complete carrier.
"""
import argparse
import json

FIELDS = ("r1", "r2", "y", "d1", "d2", "e1", "e2", "z",
          "p", "tau", "chi1", "chi2")


def validate(state):
    if len(state) != 12 or any(type(v) is not int for v in state):
        raise ValueError("state must contain exactly twelve integers")
    if any(v < 0 for v in state[:3]):
        raise ValueError("stocks must be nonnegative")
    if any(v not in (-1, 1) for v in state[3:5]):
        raise ValueError("directions must be -1 or 1")
    if any(state[i] not in (0, 1) for i in (5, 6, 7, 9, 10, 11)):
        raise ValueError("flags, phase and switches must be bits")
    if state[8] not in range(5):
        raise ValueError("pointer must be in 0..4")


def errors(state):
    return tuple(state[5+i] ^ int(state[i] == 0) for i in range(3))


def prepare(a, b, receiver, pointer=None, enabled=(1, 1)):
    stocks = (a, b, receiver)
    p = receiver % 5 if pointer is None else pointer
    state = stocks + (1, 1) + tuple(int(v == 0) for v in stocks)
    state += (p, 0) + tuple(enabled)
    validate(state)
    return state


def step(state):
    """One complete autonomous step, including disabled and faulty states."""
    out = list(state)
    i = state[9]
    if state[10+i]:
        r, y, direction = state[i], state[2], state[3+i]
        if direction == 1:
            if r:
                out[i], out[2] = r-1, y+1
            else:
                out[3+i] = -1
        elif y:
            out[i], out[2] = r+1, y-1
        else:
            out[3+i] = 1
        delta = out[2] - y
        out[8] = (state[8] + delta) % 5
        out[5+i] ^= int(r == 0) ^ int(out[i] == 0)
        out[7] ^= int(y == 0) ^ int(out[2] == 0)
    out[9] = 1 - state[9]
    return tuple(out)


def inverse(state):
    """Inverse of step on the same complete carrier."""
    out = list(state)
    i = 1 - state[9]
    if state[10+i]:
        r, y, direction = state[i], state[2], state[3+i]
        if direction == 1:
            if y:
                out[i], out[2] = r+1, y-1
            else:
                out[3+i] = -1
        elif r:
            out[i], out[2] = r-1, y+1
        else:
            out[3+i] = 1
        reverse_delta = out[2] - y
        out[8] = (state[8] + reverse_delta) % 5
        out[5+i] ^= int(r == 0) ^ int(out[i] == 0)
        out[7] ^= int(y == 0) ^ int(out[2] == 0)
    out[9] = 1 - state[9]
    return tuple(out)


def read_current(state):
    """Read the preceding forward transfer; requires calibrated flags."""
    i = 1 - state[9]
    if not state[10+i]:
        return 0
    if state[3+i] == 1 and state[7] == 0:
        return 1
    if state[3+i] == -1 and state[5+i] == 0:
        return -1
    return 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sources", nargs=2, type=int, default=(2, 1))
    parser.add_argument("--receiver", type=int, default=1)
    parser.add_argument("--pointer", type=int,
                        help="default: receiver modulo five")
    parser.add_argument("--enabled", nargs=2, type=int, choices=(0, 1),
                        default=(1, 1))
    parser.add_argument("--state", nargs=12, type=int, metavar="INTEGER",
                        help="complete raw state, including faulty flags")
    parser.add_argument("--steps", type=int, default=12)
    parser.add_argument("--backward", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    if args.steps < 0:
        parser.error("--steps must be nonnegative")
    try:
        state = (tuple(args.state) if args.state is not None else
                 prepare(*args.sources, args.receiver, args.pointer,
                         args.enabled))
        validate(state)
    except ValueError as exc:
        parser.error(str(exc))
    operation = inverse if args.backward else step
    rows = []
    for n in range(args.steps+1):
        rows.append({"n": -n if args.backward else n,
                     "state": list(state),
                     "flag_errors": list(errors(state)),
                     "pointer_offset": (state[8]-state[2]) % 5,
                     "last_forward_current": read_current(state) if n else None})
        if n < args.steps:
            state = operation(state)
    if args.json:
        print(json.dumps({"fields": FIELDS, "rows": rows},
                         sort_keys=True, indent=2))
        return
    print("WORKING HYPOTHESIS; one abstract tick, no physical time calibration")
    print("n r1 r2 y d1 d2 e1 e2 z p tau chi1 chi2 last_forward_current flag_errors")
    for row in rows:
        values = [row["n"]] + row["state"]
        current = row["last_forward_current"]
        print(" ".join(str(v) for v in values),
              "-" if current is None else current,
              "".join(str(v) for v in row["flag_errors"]))
    print("Pointer is modulo 5. Current is exact only with flag_errors=000.")
    print("For backward traces the reader labels the preceding FORWARD event.")


if __name__ == "__main__":
    main()
