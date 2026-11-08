#!/usr/bin/env python3
"""Tick law of the lifted fibre on native U. NON-CANONICAL, L1, exact.

Written while the note was prepared, after the recon runs. Not preregistered.
Fifty origin-zero heads, ten on each initial trace sheet, are followed through the
actual native update to counter 4096. Checked:
 T1  from counter 3 on every tick uses a letter of {b,d,e} (from counter 1 on the
     traces 1 and 4);
 T2  the lifted kick is kappa_n = t_(n+1) (N_(n+1) - N_n) as integers;
 T3  kappa_n = 0 for odd n and kappa_(2k) = S(k) - S(k-1) = [v_2(k) even];
 T4  for every window of either parity with n1 <= 300,
     rt_n1 - (-1)^(n1-n0) rt_n0 = t_n1 (N_n1 - N_n0) as integers.
Standard library only, integers only.
"""
from functools import lru_cache

HORIZON = 4096
WINDOW_MAX = 300
FAILS = []


def chk(name, cond, detail=""):
    print(("PASS " if cond else "FAIL ") + name + ((" " + detail) if detail else ""))
    if not cond:
        FAILS.append(name)


def theta(n):
    return bin(n).count("1") % 2


@lru_cache(maxsize=None)
def S(m):
    return 0 if m == 0 else m - S(m // 2)


def t_sign(n):
    return 1 if (n - 3) % 2 == 0 else -1


def N(n):
    return S((n - 1) // 2) - 1


def gen(letter, x):
    x0, x1, x2, x3, q, r = x
    if letter == "a":
        return (x1, x0, x3, x2, q, r)
    if letter == "b":
        return (-x2 % 5, -x3 % 5, -x0 % 5, -x1 % 5, -q % 5, -r % 5)
    if letter == "c":
        return ((2 - x2) % 5, (1 - x3 + r) % 5, (2 - x0) % 5, (1 - x1 - r) % 5, (1 - q) % 5, -r % 5)
    if letter == "d":
        return ((2 - x0) % 5, (1 - x1) % 5, (3 - x2) % 5, (4 - x3) % 5, (1 - q) % 5, (1 - r) % 5)
    return ((2 - x0) % 5, (1 - x1) % 5, (3 - x2) % 5, (4 - x3) % 5, (2 - q) % 5, (1 - r) % 5)


EPS_KAPPA = {"a": (1, 0), "b": (-1, 0), "c": (-1, 0), "d": (-1, 1), "e": (-1, 1)}

heads = []
for z0 in range(5):
    for r0 in range(5):
        heads.append(((z0 - 10 - r0) % 5, 1, 2, 3, 4, r0))
        heads.append((0, 0, 0, 0, (z0 - r0) % 5, r0))
assert len(set(heads)) == 50 and sorted(sum(h) % 5 for h in heads) == sorted(list(range(5)) * 10)

ok_letters = ok_kick = ok_parity = ok_lift = True
lifts = []
for head in heads:
    first = 1 if sum(head) % 5 in (1, 4) else 3
    x, rt = head, head[5]
    row = [rt]
    for n in range(HORIZON):
        letter = "abcde"[(sum(x) + 2 * theta(n)) % 5]
        eps, kappa = EPS_KAPPA[letter]
        x, rt = gen(letter, x), eps * rt + kappa
        ok_lift &= rt % 5 == x[5]
        row.append(rt)
        if n >= first:
            ok_letters &= letter in "bde"
            ok_kick &= eps == -1 and kappa == t_sign(n + 1) * (N(n + 1) - N(n))
            if n % 2:
                ok_parity &= kappa == 0
            else:
                k = n // 2
                v2 = (k & -k).bit_length() - 1
                ok_parity &= kappa == S(k) - S(k - 1) == int(v2 % 2 == 0)
    lifts.append((first, row))
chk("T0 the integer lift reduces to the native fibre at every tick", ok_lift, "heads=%d ticks=%d" % (len(heads), HORIZON))
chk("T1 letters in {b,d,e} from counter 3 (from counter 1 on the traces 1 and 4)", ok_letters)
chk("T2 kick kappa_n = t_(n+1) (N_(n+1) - N_n) as integers", ok_kick)
chk("T3 kappa_n = 0 for odd n and kappa_(2k) = S(k) - S(k-1) = [v_2(k) even]", ok_parity)

ok = True
windows = early = 0
for first, row in lifts:
    for n0 in range(first, WINDOW_MAX):
        for n1 in range(n0 + 1, WINDOW_MAX + 1):
            sign = 1 if (n1 - n0) % 2 == 0 else -1
            ok &= row[n1] - sign * row[n0] == t_sign(n1) * (N(n1) - N(n0))
            windows += 1
            early += n0 < 3
chk("T4 window law for both parities, n1 <= %d" % WINDOW_MAX, ok, "window checks=%d of which from n0<3: %d" % (windows, early))
print("RESULT", "PASS" if not FAILS else "FAIL", "fails=%d" % len(FAILS))
