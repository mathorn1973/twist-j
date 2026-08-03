"""Verify the local checkerboard identity on a large window: lay the
pattern over every site of a box, compute the boundary, and check the
central edges get exactly 5*j while central transverse edges get 0.
Then, if the base recipe fails, search the small sign-choice space:
    n_01 = s1 * alpha tau
    n_02 = s2 * alpha tau        n_12 = s3 * alpha tau
    n_03 = s4 * alpha tau g(x3)  n_13 = s5 * alpha tau g(x3)
with s* in {-1,+1} and g in the two phases, against
    j(e_0) = alpha tau, j(e_1) = -alpha tau.
"""
from itertools import product
from kappa_lib import chain_d

R = 5   # box radius


def alpha_tau(v):
    a = -1 if (v[0] + v[1]) % 2 else 1
    t = -1 if (v[2] + v[3]) % 2 else 1
    return a * t


def try_recipe(s1, s2, s3, s4, s5, gph):
    n = {}
    for v in product(range(-R, R + 1), repeat=4):
        at = alpha_tau(v)
        g = (v[3] + gph) % 2
        n[(v, 0, 1)] = s1 * at
        n[(v, 0, 2)] = s2 * at
        n[(v, 1, 2)] = s3 * at
        if g:
            n[(v, 0, 3)] = s4 * at
            n[(v, 1, 3)] = s5 * at
    dn = chain_d(n)
    ok = True
    for v in product(range(-1, 2), repeat=4):
        at = alpha_tau(v)
        want = {0: 5 * at, 1: -5 * at, 2: 0, 3: 0}
        for d in range(4):
            if dn.get((v, d), 0) != want[d]:
                ok = False
    return ok


def main():
    hits = []
    for s in product((1, -1), repeat=5):
        for gph in (0, 1):
            if try_recipe(*s, gph):
                hits.append((s, gph))
    print("working recipes:", hits if hits else "NONE")


if __name__ == "__main__":
    main()
