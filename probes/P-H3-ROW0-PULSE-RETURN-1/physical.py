"""Exact two-row H3 packet preparation, evolution, and port projection."""

from functools import lru_cache
from hashlib import sha256
from importlib.util import module_from_spec, spec_from_file_location
import json
from math import gcd
from pathlib import Path
import sys


KERNEL_SHA256 = "4553945d3bf32574ffd55de917859497e9644394f506aaf01ff9492adb8eeedd"
WIDTH, ORIGIN, FUND = 288, 112, 8192
RECEIVERS = (12, 13)
REFERENCE = 23
END = 256
NATIVE_TICKS = tuple(range(12, END + 1, 2))
PROJECTED_TICKS = tuple(range(98, END + 1, 2))
LATE_START = NATIVE_TICKS.index(PROJECTED_TICKS[0])
ARMS = ("FULL", "SWAP", "HEAD", "TAIL")
ZERO = (0, 0, 0, 0)
STATION = (
    ((4651, -14000, -30149, -21499), (1, 0, 1, 1), (-14000, -15050, -1750, 7550)),
    ((-3300, -11500, -13300, -6150), ZERO, (-14000, -15050, -1750, 7550)),
)


def key(case):
    return tuple(case[name] for name in ("arm", "k", "l", "eta", "m"))


def roster(gains):
    gains = tuple(gains)
    if any(type(gain) is not int or gain <= 0 for gain in gains) or len(set(gains)) != len(gains):
        raise ValueError("expected distinct positive integer gains")
    cases = []
    for rank in range(10):
        for gain in gains:
            for k in range(5):
                for l in range(5):
                    if k != l:
                        for arm in ARMS:
                            cases.append(dict(k=k, l=l, eta=-gain if rank < 5 else gain,
                                              m=rank % 5, arm=arm))
        cases.append(dict(k=0, l=1, eta=0, m=0, arm="Q"))
    return cases


def primitive(word):
    divisor = gcd(*word)
    return tuple(value // divisor for value in word) if divisor else ZERO


def projected(trace):
    if len(trace) != len(NATIVE_TICKS):
        raise ValueError("expected the complete even-tick native trace")
    return tuple(tuple(primitive(row) for row in tick) for tick in trace[LATE_START:])


def load_kernel(path):
    path = Path(path)
    if path.is_dir():
        path /= "reproduce/h3-referenced-record/verify.py"
    data = path.read_bytes()
    if sha256(data).hexdigest() != KERNEL_SHA256:
        raise ValueError("H3 kernel SHA-256 mismatch")
    name = "_h3_late_port_kernel"
    spec = spec_from_file_location(name, path)
    module = module_from_spec(spec)
    # The kernel defines dataclasses. Register the module during class creation.
    previous = sys.modules.get(name)
    sys.modules[name] = module
    try:
        exec(compile(data, path, "exec"), module.__dict__)
    finally:
        if previous is None:
            del sys.modules[name]
        else:
            sys.modules[name] = previous
    return module


def store(row, site, word):
    if word == ZERO:
        row.pop(site, None)
    else:
        row[site] = word


def capture(radiation, matter):
    return tuple(tuple(sorted(row.items())) for row in radiation), tuple(matter)


def exchange(left, right):
    """Keep the recipient matter and leading radiation, exchanging x <= 0."""
    def mix(recipient, donor):
        local, matter = recipient
        return tuple(
            tuple((x, w) for x, w in remote if x <= ORIGIN)
            + tuple((x, w) for x, w in row if x > ORIGIN)
            for row, remote in zip(local, donor[0], strict=True)
        ), matter

    return mix(left, right), mix(right, left)


class Physical:
    def __init__(self, kernel_path):
        self.kernel = kernel = load_kernel(kernel_path)
        self.D = kernel.sub(kernel.ONE, kernel.RHO)
        self.DI = kernel.mul(self.D, kernel.J_INV)
        self.d = kernel.ONE
        for _ in range(12):
            self.d = kernel.mul(self.d, self.D)
        stock = kernel.scale(2, self.d)
        self.first_stock = (stock, ZERO, stock)
        self.reference_word = kernel.scale(FUND, self.DI)
        self.phase = tuple(kernel.J_POWERS[(2 * m) % 5] for m in range(5))
        self.pair = lru_cache(maxsize=100000)(kernel.transport_pair)
        self.scatter = lru_cache(maxsize=80000)(kernel.collision)
        self.seed = lru_cache(maxsize=1000)(self.seed)
        self.propagate = lru_cache(maxsize=6000)(self.propagate)
        self.first_history = lru_cache(maxsize=128)(self.first_history)

    def first_history(self, tick, k, l, quiet):
        kernel = self.kernel
        word = ZERO
        if tick == 11:
            word = kernel.scale(4, kernel.mul(kernel.J_INV, self.d))
        elif tick == 12:
            roots = ZERO if quiet else kernel.add(self.phase[k], self.phase[l])
            word = kernel.scale(2, kernel.mul(self.d, kernel.add(kernel.ONE, roots)))
        return (*self.first_stock, word)

    def seed(self, k, l, eta, phase, quiet):
        kernel = self.kernel
        row = {ORIGIN + REFERENCE: self.reference_word}
        if not quiet:
            u, w, v = self.phase[k], self.phase[l], kernel.scale(eta, self.phase[phase])
            for offset, coefficient in enumerate((1, 2, -3, -2), start=-4):
                row[ORIGIN + offset] = kernel.scale(FUND * coefficient, u)
            store(row, ORIGIN, kernel.scale(FUND, kernel.add(u, v)))
            store(row, ORIGIN + 1, kernel.scale(FUND, kernel.mul(self.DI, kernel.sub(w, v))))
        radiation = [row, row.copy()]
        matter = [self.first_stock, self.first_stock, *STATION]
        self.step(radiation, matter, 1, k, l, quiet)
        return capture(radiation, matter)

    def step(self, radiation, matter, tick, k, l, quiet):
        # A matches horizontal radiation and vertical matter. B scatters both
        # rows at each receiver and returns their radiation to the field.
        bit = (tick - 1) % 2
        pair, scatter = self.pair, self.scatter
        for row in radiation:
            anchors = {site if site % 2 == bit else (site - 1) % WIDTH for site in row}
            for left in anchors:
                right = (left + 1) % WIDTH
                a, b = row.get(left, ZERO), row.get(right, ZERO)
                if a != b:
                    x, y = pair(a, b, False)
                    if x != a:
                        store(row, left, x)
                        store(row, right, y)

        for index, location in enumerate(RECEIVERS):
            site = ORIGIN + location
            low, high = 2 * index + bit, 2 * index + 1 - bit
            if matter[low] != matter[high]:
                rails = tuple(pair(a, b, False) for a, b in zip(matter[low], matter[high]))
                matter[low], matter[high] = map(tuple, zip(*rails))
            for row_index, row in enumerate(radiation):
                slot = 2 * index + row_index
                incoming = (*matter[slot], row.get(site, ZERO))
                if index == 0 and tick <= 12 and incoming != self.first_history(tick, k, l, quiet):
                    raise ArithmeticError("first receiver history differs")
                outgoing, _ = scatter(incoming)
                matter[slot] = outgoing[:3]
                store(row, site, outgoing[3])

    def propagate(self, after, k, l, quiet):
        frozen_radiation, frozen_matter = after
        radiation, matter = [dict(row) for row in frozen_radiation], list(frozen_matter)
        source = ORIGIN + RECEIVERS[1]
        destination = source + 1
        subtract = self.kernel.sub
        trace, material = [], []
        for tick in range(2, END + 1):
            observe = tick >= NATIVE_TICKS[0] and tick % 2 == 0
            if observe:
                old = tuple(row.get(destination, ZERO) for row in radiation)
            self.step(radiation, matter, tick, k, l, quiet)
            if observe:
                trace.append(tuple(subtract(row.get(destination, ZERO), before)
                                   for row, before in zip(radiation, old, strict=True)))
            if 13 <= tick <= 96:
                material.append((matter[2][1], matter[3][1]))
        digest = sha256(json.dumps(material, separators=(",", ":")).encode("ascii")).hexdigest()
        return tuple(trace), digest

    def run(self, case):
        """Return the 123 raw two-row transfer samples and material digest."""
        arm, k, l, eta, phase = key(case)
        if arm == "Q":
            if (k, l, eta, phase) != (0, 1, 0, 0):
                raise ValueError("unexpected quiet control")
            return self.propagate(self.seed(0, 1, 0, 0, True), 0, 1, True)
        if (arm not in ARMS or any(type(value) is not int for value in (k, l, eta, phase))
                or not (0 <= k < 5 and 0 <= l < 5 and 0 <= phase < 5) or k == l):
            raise ValueError("invalid active packet")
        full = self.seed(k, l, eta, phase, False)
        low, high = sorted((k, l))
        if arm == "FULL":
            return self.propagate(full, low, high, False)
        if arm == "SWAP":
            donor = self.seed(l, k, eta, phase, False)
            swapped, twin = exchange(full, donor)
            if swapped != donor or twin != full:
                raise ArithmeticError("reversal changed the leading cut")
            return self.propagate(swapped, low, high, False)
        quiet = self.seed(0, 1, 0, 0, True)
        head, tail = exchange(full, quiet)
        if arm == "HEAD":
            return self.propagate(head, low, high, False)
        return self.propagate(tail, 0, 1, True)
