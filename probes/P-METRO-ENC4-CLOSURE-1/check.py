"""Validate a finite ENC4 proof object without calling its generator."""
import argparse
import sys


from auxiliary import verify_auxiliary
from common import (
    align_value, aligned, digest, direction, dump, encoded, fields,
    follows, integer, limit_tables, modulus, mul, nonzero_point, norm, power,
    rat, read, require, sequence, sub, system, transition, value,
)


def parse_axes(s, axes):
    matrices = []
    projections = []
    periods = []
    for digit_maps, item in zip(s.digits, sequence(axes, s.a)):
        fields(item, "h", "E", "K", "theta")
        h = integer(item["h"], 1)
        k = integer(item["K"], 1)
        require(k % h == 0, "decay step is not a period multiple")
        e = tuple(tuple(map(rat, sequence(row, s.n))) for row in sequence(item["E"], s.n))
        require(all(sum(row) == 1 and all(x >= 0 for x in row) for row in e),
                "projection is not stochastic")
        p = transition(digit_maps)
        require(mul(e, e) == e and mul(p, e) == mul(e, p) and mul(power(p, h), e) == e,
                "invalid projection identities")
        theta = rat(item["theta"])
        require(0 <= theta < 1 and norm(sub(power(p, k), e)) == theta, "invalid decay contraction")
        matrices.append(p)
        projections.append(e)
        periods.append(h)
    return limit_tables(matrices, projections, periods), periods


def witness(s, item, periods=None):
    if periods is None:
        fields(item, "start", "words")
    else:
        fields(item, "start", "words", "residues")
    start = integer(item["start"], 0, s.n - 1)
    require(start in s.starts, "witness start is disallowed")
    words = []
    zero = () if s.convention.endswith("E0") else (0,)
    for word in sequence(item["words"], s.a):
        word = tuple(integer(d, 0, s.q - 1) for d in sequence(word))
        positive = bool(word and word[0 if s.msd else -1])
        require(positive or (periods is None and word == zero), "noncanonical witness word")
        words.append(word)
    residues = None if periods is None else tuple(
        integer(k, 0, h - 1) for k, h in zip(sequence(item["residues"], s.a), periods)
    )
    return start, words, residues


def step(axis, states, count):
    for _ in range(count):
        states = frozenset(f[v] for f in axis for v in states)
    return states


def exact_zero(s, item, periods):
    start, words, residues = witness(s, item, periods)
    states = frozenset({start})
    for axis, word, residue, period in zip(s.digits, words, residues, periods):
        fixed = follows(axis, word)
        if s.msd:
            states = frozenset(fixed[v] for v in states)
        current = step(axis, states, residue)
        visited = set()
        reachable = set()
        while current not in visited:
            visited.add(current)
            reachable.update(current)
            current = step(axis, current, period)
        states = frozenset(reachable)
        if not s.msd:
            states = frozenset(fixed[v] for v in states)
    return all(not any(s.weights[v]) for v in states)


def canonical_maps(s, axis):
    # Read MSD from the first nonzero digit. Read LSD backwards from the
    # last nonzero digit, composing each new letter on the input side.
    seen = {axis[d]: (d,) for d in range(1, s.q)}
    queue = list(seen)
    for mapping in queue:
        word = seen[mapping]
        for d, letter in enumerate(axis):
            if s.msd:
                following = tuple(letter[v] for v in mapping)
                next_word = word + (d,)
            else:
                following = tuple(mapping[v] for v in letter)
                next_word = (d,) + word
            if following not in seen:
                seen[following] = next_word
                queue.append(following)
    return seen


def checked_rows(s, raw, lit, limits, periods):
    positive = tuple(canonical_maps(s, axis) for axis in s.digits)
    rows = {row for row, _ in aligned(s, limits, positive)}
    point = nonzero_point(s, positive)

    def split(claim, reason, tagged):
        fields(claim, "status", "reason", "aligned")
        require(claim["reason"] == reason, "incorrect split reason")
        actual = []
        for item in sequence(claim["aligned"], 2):
            start, words, residues = witness(s, item, periods)
            row = align_value(s, limits, start, words, residues)
            actual.append(direction(row) if tagged else row)
        require(actual[0] != actual[1] and None not in actual, "split does not separate two limits")

    require(type(raw) is dict and type(lit) is dict, "missing claims")
    if len(rows) == 1:
        require(raw == {"status": "RAW", "limit": encoded(next(iter(rows)))}, "incorrect RAW limit")
    else:
        require(raw.get("status") == "REJECT", "RAW must reject")
        split(raw, "raw-split", False)

    if point is None:
        require(lit == {"status": "ZERO"}, "incorrect ZERO decision")
    elif any(not any(row) for row in rows):
        fields(lit, "status", "reason", "point", "zero")
        require(lit["status"] == "REJECT" and lit["reason"] == "tag-split", "incorrect tag split")
        start, words, _ = witness(s, lit["point"])
        require(any(value(s, words, start)), "nonzero witness has zero mass")
        require(exact_zero(s, lit["zero"], periods), "claimed zero family contains positive mass")
    else:
        dirs = {direction(row) for row in rows}
        if len(dirs) == 1:
            expected = {"status": "PROB", "limit": encoded(next(iter(dirs))),
                        "min_mass": str(min(sum(row) for row in rows))}
            require(lit == expected, "incorrect PROB limit or mass")
        else:
            require(lit.get("status") == "REJECT", "LIT must reject")
            split(lit, "direction-split", True)


def validate(obj, cert):
    s = system(obj)
    fields(cert, "schema", "system_sha256", "axes", "raw", "lit", "auxiliary")
    require(cert["schema"] == "metro-enc4-v1" and cert["system_sha256"] == digest(obj),
            "incorrect schema or source binding")
    limits, periods = parse_axes(s, cert["axes"])
    checked_rows(s, cert["raw"], cert["lit"], limits, periods)

    verify_auxiliary(s, cert["auxiliary"])
    return s


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("system")
    parser.add_argument("certificate")
    parser.add_argument("--epsilon", type=rat)
    args = parser.parse_args()
    try:
        obj, cert = read(args.system), read(args.certificate)
        s = validate(obj, cert)
        result = {name: claim["status"] for name, claim in (("raw", cert["raw"]), ("lit", cert["lit"]))}
        if args.epsilon is not None:
            require(args.epsilon > 0, "epsilon must be positive")
            result["minimum_side"] = {
                name: modulus(s, cert["axes"], cert[name], args.epsilon)
                for name in ("raw", "lit") if result[name] != "REJECT"
            }
        print(dump(result))
    except (ValueError, OSError) as error:
        sys.exit(str(error))


if __name__ == "__main__":
    main()
