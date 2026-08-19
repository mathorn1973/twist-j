#!/usr/bin/env python3
"""Exact finite audit for P-DQRC-INTRINSIC-SELECTION-1, target R3.

The universal word identities and uniqueness statements are proved in
PREREG.md.  This program audits frozen finite windows with two independent
integer implementations of floor(n/sqrt(2)) and a substitution branch that is
independent of the DQRC comparator branch.  It uses no floating point, RNG,
external input, network service, or third-party package.
"""

from math import isqrt
import platform
import sys


WORD_LENGTH = 20_000
MAX_SHIFT = 32
ABSOLUTE_PREFIX_LIMIT = 4_000
AGREEMENT_PREFIX = 40
COMPARATOR_MAX = WORD_LENGTH + MAX_SHIFT
TAU_ZERO = (1,)
TAU_ONE = (1, 1, 0)

ACTIVE_GATE = "startup"


class IntegrityFailure(Exception):
    """The accepted execution or verifier contract was not met."""


class ScientificFailure(Exception):
    """A frozen exact audit condition failed."""


def require_integrity(condition: bool, detail: str) -> None:
    if not condition:
        raise IntegrityFailure(detail)


def require_science(condition: bool, detail: str) -> None:
    if not condition:
        raise ScientificFailure(detail)


def lower_isqrt(n: int) -> int:
    """Return floor(n/sqrt(2)) through the standard integer square root."""
    require_integrity(n >= 0, "negative-comparator-input")
    return isqrt((n * n) // 2)


def lower_bisection(n: int) -> int:
    """Independent monotone search for max m with 2*m^2 <= n^2."""
    require_integrity(n >= 0, "negative-bisection-input")
    lo = 0
    hi = n + 1
    square = n * n
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if 2 * mid * mid <= square:
            lo = mid
        else:
            hi = mid
    return lo


def increment(shift: int, k: int) -> int:
    require_integrity(shift >= 0 and k >= 0, "negative-word-index")
    return lower_isqrt(k + shift + 1) - lower_isqrt(k + shift)


def shifted_count(shift: int, prefix: int) -> int:
    require_integrity(shift >= 0 and prefix >= 0, "negative-prefix-index")
    return lower_isqrt(prefix + shift) - lower_isqrt(shift)


def substitute(word: tuple[int, ...]) -> tuple[int, ...]:
    out: list[int] = []
    for symbol in word:
        if symbol == 0:
            out.extend(TAU_ZERO)
        elif symbol == 1:
            out.extend(TAU_ONE)
        else:
            raise IntegrityFailure("nonbinary-substitution-input")
    return tuple(out)


def silver_word(length: int) -> tuple[int, ...]:
    require_integrity(length >= 0, "negative-silver-length")
    word = (1,)
    while len(word) < length:
        word = substitute(word)
    return word[:length]


def dqrc_word(shift: int, length: int) -> tuple[int, ...]:
    require_integrity(length >= 0, "negative-dqrc-length")
    return tuple(increment(shift, k) for k in range(length))


def audit() -> None:
    global ACTIVE_GATE

    ACTIVE_GATE = "I1/environment"
    require_integrity(platform.python_implementation() == "CPython",
                      "implementation-not-CPython")
    require_integrity(sys.version_info[:2] == (3, 12),
                      "python-version-not-3.12")
    require_integrity(sys.flags.optimize == 0, "optimization-not-zero")
    require_integrity(len(sys.argv) == 1, "arguments-not-empty")
    require_integrity(
        (WORD_LENGTH, MAX_SHIFT, ABSOLUTE_PREFIX_LIMIT,
         AGREEMENT_PREFIX, COMPARATOR_MAX)
        == (20_000, 32, 4_000, 40, 20_032),
        "frozen-constants-mismatch",
    )
    require_integrity(TAU_ZERO == (1,) and TAU_ONE == (1, 1, 0),
                      "substitution-mismatch")

    print("P-DQRC-INTRINSIC-SELECTION-1 R3 exact audit")
    print("ENV implementation=CPython version=3.12 optimization=0")
    print("BOX N=20000 J=0..32 K=0..3999 comparator=0..20032")

    ACTIVE_GATE = "G1/comparator"
    comparator_checks = 0
    for n in range(COMPARATOR_MAX + 1):
        left = lower_isqrt(n)
        right = lower_bisection(n)
        require_science(left == right, f"comparator-disagreement-n={n}")
        require_science(2 * left * left <= n * n,
                        f"comparator-lower-bound-n={n}")
        require_science(n * n < 2 * (left + 1) * (left + 1),
                        f"comparator-upper-bound-n={n}")
        comparator_checks += 1
    print(f"G1 COMPARATOR checks={comparator_checks} PASS")

    ACTIVE_GATE = "G2/substitution"
    incidence = (
        (TAU_ONE.count(1), TAU_ZERO.count(1)),
        (TAU_ONE.count(0), TAU_ZERO.count(0)),
    )
    require_science(incidence == ((2, 1), (1, 0)),
                    "incidence-matrix-mismatch")
    w = silver_word(WORD_LENGTH + 1)
    tau_w = substitute(w)
    require_science(tau_w[:WORD_LENGTH] == w[:WORD_LENGTH],
                    "substitution-prefix-not-fixed")
    print("G2 SUBSTITUTION incidence=2,1;1,0 fixed-prefix=20000 PASS")

    ACTIVE_GATE = "G3/all-prefix-identities"
    u0 = dqrc_word(0, WORD_LENGTH + 1)
    u1 = dqrc_word(1, WORD_LENGTH)
    require_science(u0 == (0,) + w[:WORD_LENGTH], "u0-not-0w")
    require_science(u1 == w[:WORD_LENGTH], "u1-not-w")

    prefix0 = 0
    prefix1 = 0
    prefix_checks = 0
    for k in range(WORD_LENGTH + 1):
        if k:
            prefix0 += u0[k - 1]
            prefix1 += u1[k - 1]
        require_science(prefix0 == lower_isqrt(k),
                        f"u0-prefix-sum-k={k}")
        require_science(prefix1 == lower_isqrt(k + 1),
                        f"u1-prefix-sum-k={k}")
        prefix_checks += 2
    print(
        "G3 WORD_PREFIXES u0=0w u1=w checked-length=20000 "
        f"prefix-sums={prefix_checks} PASS"
    )

    ACTIVE_GATE = "G4/fixed-shift-box"
    fixed: list[int] = []
    for shift in range(MAX_SHIFT + 1):
        candidate = dqrc_word(shift, WORD_LENGTH)
        if candidate == w[:WORD_LENGTH]:
            fixed.append(shift)
    require_science(fixed == [1], f"fixed-shifts={fixed}")
    print("G4 FIXED_SHIFT_IN_BOX shifts=0..32 survivor=1 PASS")

    ACTIVE_GATE = "G5/absolute-count-box"
    absolute: list[int] = []
    telescope_checks = 0
    for shift in range(MAX_SHIFT + 1):
        running = 0
        survives = True
        for prefix in range(ABSOLUTE_PREFIX_LIMIT):
            if prefix:
                running += increment(shift, prefix - 1)
            require_science(running == shifted_count(shift, prefix),
                            f"telescope-shift={shift}-k={prefix}")
            telescope_checks += 1
            if running != lower_bisection(prefix):
                survives = False
        if survives:
            absolute.append(shift)
    require_science(absolute == [0], f"absolute-shifts={absolute}")
    print(
        "G5 ABSOLUTE_COUNT_SHIFT_IN_BOX shifts=0..32 survivor=0 "
        f"telescope-checks={telescope_checks} PASS"
    )

    ACTIVE_GATE = "G6/agreement-pin"
    agreements = sum(
        w[k] == u0[k]
        for k in range(AGREEMENT_PREFIX)
    )
    mismatches = AGREEMENT_PREFIX - agreements
    require_science(agreements == 16, f"agreements={agreements}")
    require_science(mismatches == 24, f"mismatches={mismatches}")
    print("G6 AGREEMENT_W_U0_40 agreements=16 mismatches=24 PASS")

    ACTIVE_GATE = "G7/index-pair-box"
    absolute_index = absolute[0]
    fixed_index = fixed[0]
    require_science((absolute_index, fixed_index) == (0, 1),
                    "survivor-index-pair-mismatch")
    print("G7 INDEX_PAIR_IN_BOX absolute=0 fixed=1 PASS")
    print("VERIFY PASS gates=7/7 disposition=AUDIT-CONSISTENT")


def entrypoint() -> int:
    try:
        audit()
    except ScientificFailure as exc:
        print(f"SCIENCE FAIL gate={ACTIVE_GATE} detail={exc}")
        return 2
    except IntegrityFailure as exc:
        print(f"INTEGRITY FAIL gate={ACTIVE_GATE} detail={exc}")
        return 1
    except Exception as exc:  # no traceback or stderr in the formal contract
        print(
            "INTEGRITY FAIL "
            f"gate={ACTIVE_GATE} unexpected={type(exc).__name__}"
        )
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(entrypoint())
