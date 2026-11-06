#!/usr/bin/env python3
"""Prospective absolute capture enclosure, one bounded deterministic audit.

Author: A. M. Thorn. SPDX-License-Identifier: Apache-2.0.
NON-CANONICAL / L1. No scientific execution before public pin/readback.
All arithmetic in the scientific path is outward fixed-point interval arithmetic.
"""

from dataclasses import dataclass
import heapq

from interval_core import I, Q, S, CI, Uncertain, init_constants
from model import CaptureModel


GEOMETRY_BUDGET = 4096
F1_PANEL_BUDGET = 1024
F2_PANEL_BUDGET = 4096
INITIAL_PANELS = 64
ROOT_NEWTON_STEPS = 16
ROOT_EXPANSIONS = 9
ROOT_MIN_RAW = S // (1 << 40)
TARGET_FACTOR = 10


def positive(x):
    return x.lo > 0


def negative(x):
    return x.hi < 0


def separated(x):
    return positive(x) or negative(x)


def sign(x):
    return 1 if positive(x) else (-1 if negative(x) else 0)


def overlap(a, b):
    return max(a.lo, b.lo) <= min(a.hi, b.hi)


def hull(a, b):
    return I(min(a.lo, b.lo), max(a.hi, b.hi))


def intersection(a, b):
    lo, hi = max(a.lo, b.lo), min(a.hi, b.hi)
    if lo > hi:
        raise ValueError("contradictory certified interval intersection")
    return I(lo, hi)


def raw_point(x):
    return I(x, x)


def abs_upper(x):
    return max(abs(x.lo), abs(x.hi))


def safe_text(x, digits=18):
    """Outward decimal printing, without a binary float conversion."""
    scale = 10 ** digits
    lo = (x.lo * scale) // S
    hi = -((-x.hi * scale) // S)

    def fmt(n):
        sg = "-" if n < 0 else ""
        n = abs(n)
        return sg + str(n // scale) + "." + str(n % scale).zfill(digits)

    return "[" + fmt(lo) + "," + fmt(hi) + "]"


def root_k0(pi, phi):
    """The unique negative solution of cos(k)=(7-5phi)/8."""
    target = (7 - 5 * phi) / 8
    lo, hi = -pi.hi, 0
    for _ in range(128):
        mid = (lo + hi) // 2
        if mid == lo or mid == hi:
            break
        c = raw_point(mid).cos()
        if c.hi < target.lo:
            lo = mid
        elif c.lo > target.hi:
            hi = mid
        else:
            # A derivative lower bound on the retained middle quadrant gives
            # a certified final bracket even when constant intervals overlap.
            j = I(lo, hi)
            deriv = -j.sin()
            if positive(deriv):
                n = raw_point(mid) - (c - target) / deriv
                j = intersection(j, n)
                lo, hi = j.lo, j.hi
            break
    ans = I(lo, hi)
    if ans.hi - ans.lo > S // (10 ** 20):
        raise Uncertain("k0 constant isolation insufficient")
    return ans


@dataclass
class Root:
    sigma: int
    cover: I             # Normalized coordinate u=k/pi, one root for every K,E.
    u: I                 # A refined enclosure of that same root family.
    k: I
    coeff: I             # h G / (2 H_k'), signed cotangent coefficient.
    selected: bool


class Census:
    def __init__(self, model, pi):
        self.model, self.pi = model, pi
        self.calls = 0
        self.roots = []
        self.reason = ""
        self.data_cache = {}
        self.free_cache = {}

    def data(self, u, sigma):
        key = (u.lo, u.hi, sigma)
        if key in self.data_cache:
            value = self.data_cache[key]
            if isinstance(value, str):
                raise Uncertain(value)
            return value
        if self.calls >= GEOMETRY_BUDGET:
            raise Uncertain("geometry budget exhausted")
        self.calls += 1
        try:
            value = self.model.pole_data(self.pi * u, sigma)
        except Uncertain as exc:
            self.data_cache[key] = str(exc)
            raise
        self.data_cache[key] = value
        return value

    def free(self, u, sigma):
        key = (u.lo, u.hi, sigma)
        if key in self.free_cache:
            return self.free_cache[key]
        if self.calls >= GEOMETRY_BUDGET:
            raise Uncertain("geometry budget exhausted")
        self.calls += 1
        value = self.model.no_pole(self.pi * u, sigma)
        self.free_cache[key] = value
        return value

    def certify_root(self, candidate, sigma):
        mid = (candidate.lo + candidate.hi) // 2
        half = max(1, (candidate.hi - candidate.lo + 1) // 2)
        for _ in range(ROOT_EXPANSIONS):
            box = I(max(-S, mid - half), min(S, mid + half))
            try:
                pd = self.data(box, sigma)
                if not separated(pd.H.d1):
                    return None
                left = self.data(raw_point(box.lo), sigma).H.v
                right = self.data(raw_point(box.hi), sigma).H.v
                if sign(left) * sign(right) == -1:
                    rootbox = box
                    for _ in range(ROOT_NEWTON_STEPS):
                        m = raw_point((rootbox.lo + rootbox.hi) // 2)
                        value = self.data(m, sigma).H.v
                        deriv = self.data(rootbox, sigma).H.d1 * self.pi
                        if not separated(deriv):
                            raise Uncertain("lost root derivative separation")
                        refined = intersection(rootbox, m - value / deriv)
                        if refined.hi - refined.lo >= rootbox.hi - rootbox.lo - 4:
                            rootbox = refined
                            break
                        rootbox = refined
                    rp = self.data(rootbox, sigma)
                    coeff = rp.B.v / (2 * rp.H.d1)
                    kval = self.pi * rootbox
                    pobj = self.model.K - kval
                    selected = (
                        sigma == 1
                        and pobj.lo >= -Q(1, 100).lo
                        and pobj.hi <= Q(1, 100).lo
                    )
                    return Root(sigma, box, rootbox, kval, coeff, selected)
            except Uncertain as exc:
                if "budget" in str(exc):
                    raise
            half *= 2
        return None

    def add_root(self, new):
        for old in self.roots:
            if old.sigma != new.sigma or not overlap(old.u, new.u):
                continue
            # Only identify overlapping enclosures after proving monotonicity
            # on their union. Proximity alone never merges different poles.
            common = hull(old.cover, new.cover)
            try:
                pd = self.data(common, new.sigma)
                if separated(pd.H.d1):
                    old.cover = common
                    old.u = intersection(old.u, new.u)
                    old.k = self.pi * old.u
                    rd = self.data(old.u, old.sigma)
                    old.coeff = rd.B.v / (2 * rd.H.d1)
                    pobj = self.model.K - old.k
                    old.selected = (
                        old.sigma == 1
                        and pobj.lo >= -Q(1, 100).lo
                        and pobj.hi <= Q(1, 100).lo
                    )
                    return
            except Uncertain as exc:
                if "budget" in str(exc):
                    raise
            raise Uncertain("root families not provably distinct")
        self.roots.append(new)

    def run(self):
        for sigma in (-1, 1):
            pending = [
                I(-S + (2 * S * j) // INITIAL_PANELS,
                  -S + (2 * S * (j + 1)) // INITIAL_PANELS)
                for j in reversed(range(INITIAL_PANELS))
            ]
            while pending:
                cell = pending.pop()
                if cell.lo == cell.hi:
                    continue
                handled = False
                for r in self.roots:
                    if r.sigma != sigma:
                        continue
                    c = r.cover
                    if cell.lo >= c.lo and cell.hi <= c.hi:
                        handled = True
                        break
                    if cell.lo < c.hi and cell.hi > c.lo:
                        if cell.hi > c.hi:
                            pending.append(I(c.hi, cell.hi))
                        if cell.lo < c.lo:
                            pending.append(I(cell.lo, c.lo))
                        handled = True
                        break
                if handled:
                    continue
                if self.free(cell, sigma):
                    continue
                try:
                    pd = self.data(cell, sigma)
                    if separated(pd.H.v):
                        continue
                    if separated(pd.H.d1):
                        root = self.certify_root(cell, sigma)
                        if root is not None:
                            self.add_root(root)
                            pending.append(cell)
                            continue
                except Uncertain as exc:
                    if "budget" in str(exc):
                        raise
                if cell.hi - cell.lo <= ROOT_MIN_RAW:
                    raise Uncertain("unresolved critical or threshold neighborhood")
                mid = (cell.lo + cell.hi) // 2
                pending.append(I(mid, cell.hi))
                pending.append(I(cell.lo, mid))
        self.roots.sort(key=lambda r: (r.sigma, r.u.lo))
        selected = [r for r in self.roots if r.selected]
        if len(selected) != 1:
            raise Uncertain("selected outgoing pole is not uniquely identified")
        if not positive(abs(selected[0].coeff)):
            raise Uncertain("selected residue has no positive lower bound")
        return self.roots, selected[0]


def cot(x):
    return x.cos() / x.sin()


def regularized(model, pi, roots, u):
    """Full boundary integrand after zero-PV periodic pole subtraction."""
    k = pi * u
    out = CI(Q(0), Q(0))
    for sigma in (-1, 1):
        rr = [r for r in roots if r.sigma == sigma]
        chosen = None
        chosen_distance = None
        for r in rr:
            line_u = hull(u, r.u)
            distance = abs_upper(k - r.k)
            if (line_u.lo >= r.cover.lo and line_u.hi <= r.cover.hi
                    and distance <= Q(1, 8).lo):
                # The complete segment must stay in the certified smooth,
                # monotone gap neighborhood. A fixed distance alone would
                # incorrectly apply the Taylor quotient across a threshold.
                if chosen is None or distance < chosen_distance:
                    chosen, chosen_distance = r, distance
        if chosen is None:
            val = model.boundary(k, sigma)
        else:
            r = chosen
            line = hull(k, r.k)
            pd = model.pole_data(line, sigma)
            rd = model.pole_data(r.k, sigma)
            if not separated(pd.H.d1) or not separated(rd.H.d1):
                raise Uncertain("local quotient derivative not separated")
            # H(k)=(k-r) Hhat; Hhat lies in H'(hull(k,r)).
            # Exact divided differences remove the implicit pole without
            # replacing its root by a numerical midpoint.
            numerator = rd.B.v * pd.H.d2 / 2 - rd.H.d1 * pd.B.d1
            regular = numerator / (rd.H.d1 * pd.H.d1)
            dist = abs_upper(k - r.k)
            correction = I(-dist, dist) / 5
            # |cot(d/2)-2/d| <= |d|/5 for |d|<=1, proved in the note.
            regular = regular + r.coeff * correction
            val = CI(Q(0), regular)
        for r in rr:
            if r is chosen:
                continue
            val = val + CI(Q(0), r.coeff * cot((k - r.k) / 2))
        out = out + val
    return out


@dataclass
class Panel:
    lo: int
    hi: int
    value: object
    serial: int


def integrate(fun, lo, hi, max_panels, tolerance, factor=None):
    """Certified range sums. A panel contributes its width times its range."""
    if factor is None:
        factor = Q(1)
    serial = 0
    calls = 0
    heap = []
    values = {}
    totals = [0, 0, 0, 0]
    unresolved = 0

    def evaluate(a, b):
        nonlocal serial, calls, unresolved
        calls += 1
        serial += 1
        try:
            val = fun(I(a, b)) * (raw_point(b - a) * factor)
            score = (val.re.hi - val.re.lo) + (val.im.hi - val.im.lo)
        except Uncertain:
            val = None
            score = 1 << 300
        panel = Panel(a, b, val, serial)
        values[serial] = panel
        if val is None:
            unresolved += 1
        else:
            for j, endpoint in enumerate((val.re.lo, val.re.hi, val.im.lo, val.im.hi)):
                totals[j] += endpoint
        heapq.heappush(heap, (-score, serial))

    for j in range(INITIAL_PANELS):
        a = lo + ((hi - lo) * j) // INITIAL_PANELS
        b = lo + ((hi - lo) * (j + 1)) // INITIAL_PANELS
        evaluate(a, b)

    def total():
        if unresolved:
            return None
        return CI(I(totals[0], totals[1]), I(totals[2], totals[3]))

    while len(values) < max_panels:
        ans = total()
        if ans is not None:
            width = max(ans.re.hi - ans.re.lo, ans.im.hi - ans.im.lo)
            if width <= tolerance.lo:
                return ans, len(values), calls, True
        _, token = heapq.heappop(heap)
        p = values.pop(token)
        if p.value is None:
            unresolved -= 1
        else:
            val = p.value
            for j, endpoint in enumerate((val.re.lo, val.re.hi, val.im.lo, val.im.hi)):
                totals[j] -= endpoint
        m = (p.lo + p.hi) // 2
        if m == p.lo or m == p.hi:
            raise Uncertain("integration grid exhausted")
        evaluate(p.lo, m)
        evaluate(m, p.hi)
    ans = total()
    if ans is None:
        raise Uncertain("integration panel budget leaves an unresolved range")
    return ans, len(values), calls, False


def main():
    constants = init_constants()
    pi = constants["pi"]
    phi = (1 + Q(5).sqrt()) / 2
    k0 = root_k0(pi, phi)
    g = 2 * pi / 5
    beta = 4 * pi / 5
    est = 8 * pi / 5
    half = Q(1, 1000)
    K = k0 + I(-half.hi, half.hi)
    E = est + I(-half.hi, half.hi)
    model = CaptureModel(g=g, beta=beta, K=K, E=E)

    print("P-BOUND-PAIR-ABSOLUTE-CAPTURE-1")
    print("arithmetic: outward fixed-point 2^96; full boundary resolvents")
    print("source: delta=h=delta_K=1/1000; selected |P_out|<=1/100")
    census = Census(model, pi)
    try:
        roots, selected = census.run()
        print("geometry: COMPLETE; evaluations=" + str(census.calls))
        for index, root in enumerate(roots):
            print("pole " + str(index) + " sigma=" + str(root.sigma)
                  + " k=" + safe_text(root.k)
                  + " residue=" + safe_text(abs(root.coeff))
                  + " selected=" + ("yes" if root.selected else "no"))
        f1, panels1, calls1, tol1 = integrate(
            lambda u: model.f1(pi * u), 0, S,
            F1_PANEL_BUDGET, Q(1, 100)
        )
        f2reg, panels2, calls2, tol2 = integrate(
            lambda u: regularized(model, pi, roots, u), -S, S,
            F2_PANEL_BUDGET, Q(1, 20), factor=Q(1, 2)
        )
        residues = sum((abs(r.coeff) for r in roots), Q(0))
        f2 = f2reg + CI(residues, Q(0))
        if not positive(f1.re) or not positive(f2.re):
            raise Uncertain("no positive complete density lower bound")
        numerator = model.incoming_density() * abs(selected.coeff) / (2 * pi)
        numerator = 64 * pi * pi * numerator
        denominator = (CI(Q(4), Q(0)) + f1 * f2).norm2()
        positivity = 16 * f1.re * f2.re
        denominator = I(max(denominator.lo, positivity.lo), denominator.hi)
        if not positive(denominator):
            raise Uncertain("complete denominator not positively enclosed")
        probability = (half / pi) * numerator / denominator
        inherited_upper = 8 / (5 * pi * 10 ** 6)
        probability = I(max(probability.lo, Q(2, 10 ** 28).lo),
                        min(probability.hi, inherited_upper.hi))
        print("F1 Re=" + safe_text(f1.re) + " Im=" + safe_text(f1.im))
        print("F2 Re=" + safe_text(f2.re) + " Im=" + safe_text(f2.im))
        print("quadrature panels=" + str(panels1) + "," + str(panels2)
              + " evaluations=" + str(calls1) + "," + str(calls2)
              + " target_width=" + str(int(tol1)) + "," + str(int(tol2)))
        print("P_win(0)=" + safe_text(probability, 32))
        print("P_win(0) raw=[" + str(probability.lo) + ","
              + str(probability.hi) + "]/2^96")
        if probability.lo > 0 and probability.hi <= TARGET_FACTOR * probability.lo:
            print("status: CERTIFIED; upper/lower<=10")
        else:
            print("status: INCONCLUSIVE; certified enclosure wider than factor10")
    except Uncertain as exc:
        print("geometry evaluations=" + str(census.calls))
        print("status: INCONCLUSIVE; " + str(exc))
        print("retained bound: 2/10^28 < P_win(0) < 8/(5*pi*10^6)")
        fallback = I(Q(2, 10 ** 28).lo, (8 / (5 * pi * 10 ** 6)).hi)
        print("retained outward interval=" + safe_text(fallback, 32))
        print("retained raw=[" + str(fallback.lo) + ","
              + str(fallback.hi) + "]/2^96")


if __name__ == "__main__":
    main()
