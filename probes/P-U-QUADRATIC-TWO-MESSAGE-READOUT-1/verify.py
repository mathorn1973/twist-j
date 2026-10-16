#!/usr/bin/env python3
"""Exact new-readout certificate. A. M. Thorn; Apache-2.0; NON-CANONICAL L1."""
from collections import Counter
from hashlib import sha256
from itertools import product
from pathlib import Path


def certify_inputs():
    root = Path(__file__).resolve().parent
    for line in (root / "INPUTS.sha256").read_text().splitlines():
        digest, name = line.split("  ")
        assert sha256((root / name).read_bytes()).hexdigest() == digest, name


def native(A, B, C, D, z, r):
    return tuple(v % 5 for v in
                 (3*(A+C+2), 3*(B+D+1), 3*(A-C-2),
                  3*(B-D-1), z-A-B-r, r))


def pair(x):
    a,b,c,d,q,r = x
    A, B, C, D, z = a+c, b+d, a-c-2, b-d-1, sum(x)
    return (A+2*z) % 5, ((1+2*B)*D+3*B*C) % 5


def decode(p, t):
    return -1 if p == 0 else (-p*p*t) % 5


def main():
    certify_inputs()
    points = {}
    strata = Counter()

    def add(x, label, stratum):
        assert x not in points, ("duplicate", x)
        points[x] = label
        strata[stratum] += 1

    for lam, mu in product(range(5), repeat=2):
        add(native(1,0,lam,mu,2,1), -1, "blank")
        add(native(3,2,lam,(mu+2)%5,0,4), lam, "first")
    for A,z in product((1,4), repeat=2):
        for C,D,r in product(range(5), repeat=3):
            add(native(A,0,C,D,z,r), A*z*D % 5, "tail")
    assert dict(strata) == {"blank":25,"first":25,"tail":500}

    rows, decoded, images = [], {}, {k:set() for k in range(-1,5)}
    counts = Counter()
    for x, label in sorted(points.items()):
        p,t = pair(x)
        assert decode(p,t) == label, ("semantic", x, label, p, t)
        assert decoded.setdefault((p,t),label) == label, ("collision", x)
        counts[p,t] += 1
        images[label].add((p,t))
        rows.append(x+(label,p,t))
    assert len(rows) == 550 and len(decoded) == 25
    assert [len(images[k]) for k in range(-1,5)] == [5,4,4,4,4,4]
    assert sorted(Counter(counts.values()).items()) == [(5,5),(25,15),(30,5)]

    # All cross-label pairs, not a prescribed single code for each label.
    separated = 0
    for i, left in enumerate(rows):
        for right in rows[i+1:]:
            if left[6] != right[6]:
                assert left[7:] != right[7:]
                separated += 1
    assert separated == 123375

    # Independently authored native-coordinate scan and expanded polynomials.
    from check_independent import run
    summary, independent_rows = run()
    independent = [state+(label,p,t) for state,label,p,t in independent_rows]
    assert rows == independent, "independent implementation disagreement"
    assert summary["cross_label_collisions"] == 0

    payload = "".join(",".join(map(str,row))+"\n" for row in rows).encode("ascii")
    print("DOMAIN blank=25 first=25 tail=500 total=550")
    print("LABEL_IMAGES blank=5 present=4,4,4,4,4 all_codes=25")
    print("FIBRES size5=5 size25=15 size30=5")
    print("SEPARATION cross_label_pairs=123375 conflicts=0")
    print("INDEPENDENT native_scan=15625 matching_rows=550")
    print("ROWS_SHA256 " + sha256(payload).hexdigest())
    print("DECODER p0=BLANK p1=-t p2=t p3=t p4=-t")
    print("RESULT PASS quadratic_exists=YES minimum_degree=2 affine_lower_bound=INHERITED")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as exc:
        print("RESULT FAIL " + str(exc))
