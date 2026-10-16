"""Independent native-head implementation for the frozen lane V audit.

NON-CANONICAL / conditional L1 audit. Original work Apache-2.0,
A. M. Thorn, 2026. Definitions: the frozen A2 CONTRACT section 2 and
PROOF sections 3 and 7. This module contains no imported prior verifier.

The native selector need not be a permutation. ``decode_head`` recognizes
only the five-tick image of (p, 0, 1), with initial counter zero. Its receiver
test alone is insufficient: the recovered original piston sum must agree
with the receiver-selected inverse word.

Paired factorization, independently of enumeration: at any fixed actual
counter n, the two-head tick is (x, y) -> (f_n(x), f_n(y)), because neither
coordinate rule reads the other head. Induction over the same five counters
therefore gives (E(p), E(q)). The one-head left inverse below proves E
injective on every prepared p. Its product is consequently a left inverse
on all ordered pairs, and the exact paired image is image(E) x image(E).
Every sum class has 5**3 choices (the fourth piston is fixed by the first
three and the sum), so each ordered sum pair has 5**6 preparations. These
are product consequences, not 625**2 independently executed experiments.
No full-product selector inverse or physical source admission follows.
"""

from fractions import Fraction
from itertools import product


P = 5
ZERO = Fraction(0)

# Declared source targets, used only as comparison/inverse data. Forward
# states and selectors are always obtained from the formulas below.
WORDS = ((1, 1, 3), (2, 2, 4), (3, 1, 3), (4, 1, 3), (0, 2, 4))
C1 = ((0, 4), (1, 4), (1, 0), (2, 0), (0, 1))
C2 = ((0, 1), (0, 1), (4, 0), (3, 0), (1, 4))
C3 = ((1, 0), (2, 0), (2, 1), (3, 1), (1, 2))


def _residues(values, length):
    """Accept canonical residues only, without silently changing a carrier."""
    values = tuple(values)
    if len(values) != length or any(type(a) is not int or not 0 <= a < P
                                    for a in values):
        raise ValueError("expected canonical F5 coordinates")
    return values


def generator(j, x):
    """Apply the stated generator directly on the complete six coordinates."""
    if type(j) is not int or not 0 <= j < P:
        raise ValueError("generator index must be in range(5)")
    a, b, c, d, q, r = _residues(x, 6)
    if j == 0:
        raw = (b, a, d, c, q, r)
    elif j == 1:
        raw = (-c, -d, -a, -b, -q, -r)
    elif j == 2:
        raw = (2-c, 1+r-d, 2-a, 1-r-b, 1-q, -r)
    elif j == 3:
        raw = (2-a, 1-b, 3-c, 4-d, 1-q, 1-r)
    else:
        raw = (2-a, 1-b, 3-c, 4-d, 2-q, 1-r)
    return tuple(a % P for a in raw)


def tick(n, x):
    """Return (new head, actual generator index), using retained counter n."""
    if type(n) is not int or n < 0:
        raise ValueError("native counter must be a nonnegative integer")
    x = _residues(x, 6)
    j = (sum(x) + 2 * (n.bit_count() % 2)) % P
    return generator(j, x), j


def prepare(p):
    """Make the one prescribed common-ready receiver, preserving all pistons."""
    return _residues(p, 4) + (0, 1)


def eta(receiver):
    """Apply the declared signed lift; no source class or response table."""
    q, r = _residues(receiver, 2)
    # Centered representative in {-2, -1, 0, 1, 2}, derived from the residue.
    q_lift = q if q <= 2 else q - P
    r_lift = r if r <= 2 else r - P
    return (Fraction(q_lift, 2), Fraction(r_lift + 1, 2), ZERO, ZERO)


def decode_head(x5):
    """Return the original four pistons iff x5 belongs to the ready image.

    The distinct C3 receivers select one inverse word. Involution reverses
    that word on all six coordinates; common-ready receiver AND original
    piston sum then establish that the selectors really followed that word.
    For such a preparation the last two ticks cancel, giving x5=x3. This is
    an initialized-image inverse, never a global inverse of the selector.
    """
    try:
        x5 = _residues(x5, 6)
        h = C3.index(x5[-2:])
    except (ValueError, TypeError):
        return None
    recovered = x5
    for j in reversed(WORDS[h]):
        recovered = generator(j, recovered)
    if recovered[-2:] != (0, 1):
        return None
    p = recovered[:4]
    if sum(p) % P != h:
        return None
    return p


def audit_native():
    """Run the frozen exhaustive one-head tests and return measured counts.

    Scope: all 5**6 carrier states for each generator and both selector
    parities; all 5**4 ready inputs through five actual ticks; and every
    possible endpoint against the independently constructed forward image.
    The inverse-word targets are not used to construct that forward image.
    """
    counts = {
        "generator_involutions": 0,
        "generator_sum_actions": 0,
        "selector_sum_actions": 0,
        "native_preparations": 0,
        "native_ticks": 0,
        "prepared_inverse_recoveries": 0,
        "candidate_endpoints": 0,
        "accepted_endpoints": 0,
        "rejected_endpoints": 0,
        "receiver_plausible_false_endpoints": 0,
    }

    # Each generator is audited on its whole domain, including occupied
    # receivers. The sum targets are the separately expanded affine sums.
    for x in product(range(P), repeat=6):
        z = sum(x) % P
        sums = (z, -z, 2-z, 2-z, 3-z)
        for j in range(P):
            y = generator(j, x)
            assert generator(j, y) == x, ("generator involution", j, x)
            counts["generator_involutions"] += 1
            assert sum(y) % P == sums[j] % P, ("generator sum", j, x)
            counts["generator_sum_actions"] += 1
        # Every nonnegative counter enters only through its exact parity.
        # n=0 and n=1 realize both values; this is not a finite-time claim
        # about an unbounded sequence of prepared-image inversions.
        for n in (0, 1):
            y, j = tick(n, x)
            expected_j = (z + 2*n) % P
            assert j == expected_j, ("selector index", n, x)
            assert sum(y) % P == sums[expected_j] % P, ("selector sum", n, x)
            counts["selector_sum_actions"] += 1

    target_signals = (
        (ZERO, ZERO, ZERO, ZERO),
        (Fraction(1, 2), ZERO, ZERO, ZERO),
        (Fraction(1, 2), Fraction(1, 2), ZERO, ZERO),
        (Fraction(1), Fraction(1, 2), ZERO, ZERO),
        (ZERO, Fraction(1), ZERO, ZERO),
    )
    image = {}
    classes = [0] * P
    actual_signals = set()
    assert tuple(n.bit_count() % 2 for n in range(5)) == (0, 1, 1, 0, 1)
    for p in product(range(P), repeat=4):
        h = sum(p) % P
        classes[h] += 1
        states = [prepare(p)]
        selectors = []
        for n in range(5):
            y, j = tick(n, states[-1])
            states.append(y)
            selectors.append(j)
            counts["native_ticks"] += 1
        assert tuple(selectors[:3]) == WORDS[h], ("source word", p, selectors)
        assert tuple(s[-2:] for s in states[1:4]) == (C1[h], C2[h], C3[h]), (
            "source receivers", p, states)
        assert sum(states[3]) % P == 1, ("third sum", p)
        assert sum(states[4]) % P == 4, ("fourth sum", p)
        assert selectors[3:] == [1, 1], ("continuing selectors", p)
        assert states[5] == states[3], ("five-tick endpoint", p)
        signal = eta(states[1][-2:])
        assert signal == target_signals[h], ("declared signed signal", p, signal)
        actual_signals.add(signal)
        assert decode_head(states[5]) == p, ("prepared inverse", p)
        counts["prepared_inverse_recoveries"] += 1
        assert states[5] not in image, ("prepared image collision", p)
        image[states[5]] = p
        counts["native_preparations"] += 1

    assert classes == [125] * P, ("sum class populations", classes)
    assert len(actual_signals) == P, ("distinct signed signals", actual_signals)
    assert len(image) == P**4, ("prepared image size", len(image))
    for x in product(range(P), repeat=6):
        decoded = decode_head(x)
        expected = image.get(x)
        assert decoded == expected, ("exact image classification", x, decoded, expected)
        counts["candidate_endpoints"] += 1
        if decoded is None:
            counts["rejected_endpoints"] += 1
            if x[-2:] in C3:
                counts["receiver_plausible_false_endpoints"] += 1
        else:
            counts["accepted_endpoints"] += 1

    assert counts["generator_involutions"] == 5 * 5**6
    assert counts["generator_sum_actions"] == 5 * 5**6
    assert counts["selector_sum_actions"] == 2 * 5**6
    assert counts["native_preparations"] == counts["prepared_inverse_recoveries"] == 5**4
    assert counts["native_ticks"] == 5 * 5**4
    assert counts["candidate_endpoints"] == 5**6
    assert counts["accepted_endpoints"] == 5**4
    assert counts["rejected_endpoints"] == 5**6 - 5**4
    assert counts["receiver_plausible_false_endpoints"] == 5**5 - 5**4
    counts["sum_classes"] = len(classes)
    counts["preparations_per_sum_class"] = classes[0]
    counts["paired_preparations_by_factorization"] = len(image)**2
    counts["ordered_signal_pairs_by_factorization"] = len(actual_signals)**2
    counts["preparations_per_signal_pair_by_factorization"] = classes[0]**2
    return counts
