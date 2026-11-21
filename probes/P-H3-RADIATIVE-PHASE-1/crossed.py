# SPDX-License-Identifier: Apache-2.0
"""Cross the source and resident signs in a counted native H3 preparation."""


def run(native):
    h3 = native.h3
    zero, one, rho, j_unit = h3.ZERO, h3.ONE, h3.RHO, h3.J
    four = h3.scale(4, one)
    unit = h3.add(h3.J_POWERS[1], h3.J_POWERS[4])
    unit_inv = h3.inverse(unit)
    # Use the integral representative throughout the native law.
    inverse_word = h3.mul(h3.J_POWERS[1], h3.J_INV)
    h3.require(unit_inv == inverse_word, "inverse source stock")
    link = h3.sub(one, rho)
    test_gaps = {"+": link, "-": h3.mul(unit, link)}
    stock = zero, zero, h3.scale(650, one), 1300
    target, reference = (2, 1), (2, 3)

    def antipodal(gap, clk=zero, corr=zero):
        return gap, h3.scale(-1, gap), clk, corr

    def site_q(field):
        return tuple(
            h3.scalar_account(h3.ring_sum(h3.h(word) for word in field[i : i + 4]))
            for i in range(0, len(field), 4)
        )

    def require_antipodal(field):
        h3.require(
            all(field[i] == h3.scale(-1, field[i + 1]) for i in range(0, len(field), 4)),
            "matter species edge currents cancel by equal guards and opposite rails",
        )

    results = {}
    for distant in (False, True):
        common_q = None
        records = []
        for source_sign, source_unit, other_unit, field_unit, source_tag in (
            ("-", unit, inverse_word, j_unit, 2),
            ("+", inverse_word, unit, h3.J_INV, 1),
        ):
            for test_sign, other_sign in (("+", "-"), ("-", "+")):
                gap, anchor = test_gaps[test_sign], test_gaps[other_sign]
                field = native.empty()
                tiles = (4, 6) if distant else (0, 4)
                for start, word in zip(tiles, (source_unit, other_unit)):
                    fill = antipodal(h3.mul(four, word), four, h3.scale(-1, four))
                    for x in (start, start + 1):
                        for y in (0, 1):
                            native.put(field, x, y, fill)
                native.put(field, *target, antipodal(gap))
                native.put(field, *reference, antipodal(anchor))
                start = tuple(field)
                h3.require(native.ledger(start) == stock, "common complete launch stock")
                test_quadratic = h3.scale(2, h3.h(gap))
                source_quadratic = h3.scale(2, h3.h(h3.mul(four, source_unit)))
                h3.require(-test_quadratic[2] == (2 if test_sign == "+" else -2),
                           "test sign is the coefficient of phi in material H")
                h3.require(-source_quadratic[2] == (-32 if source_sign == "-" else 32),
                           "source sign is the coefficient of phi in material H")
                initial_q = site_q(start)
                if common_q is None:
                    common_q = initial_q
                h3.require(initial_q == common_q, "source and test signs preserve every launch Q")

                c1, b1, tags1 = native.step(start, 0)
                h3.require(c1 == start, "first matching leaves all launch coordinates fixed")
                h3.require(native.cell(b1, *target) == antipodal(gap)
                           and native.cell(b1, *reference) == antipodal(anchor),
                           "test and anchor unchanged after first tick")
                h3.require((tiles[0] + 1, 1, source_tag) in tags1, "first source branch")
                c2, b2, tags2 = native.step(b1, 1)
                incoming = zero if distant else h3.scale(-2, h3.mul(link, field_unit))
                h3.require(native.cell(c2, *target) == antipodal(gap, zero, incoming),
                           "only the predicted CORR reaches the unchanged gap")
                expected_tag = 0 if distant or test_sign == "-" else (1 if source_sign == "-" else 2)
                actual_tag = next((tag for x, y, tag in tags2 if (x, y) == target), 0)
                h3.require(actual_tag == expected_tag, "crossed reader decision")
                factor = field_unit if expected_tag else one
                for cut in (start, c1, b1, c2, b2):
                    require_antipodal(cut)
                    h3.require(native.ledger(cut) == stock, "complete stock throughout")
                    h3.require(native.cell(cut, 2, 0)[:2] == (zero, zero)
                               and native.cell(cut, 2, 2)[:2] == (zero, zero),
                               "no material enters either empty target-column neighbor")
                    h3.require(native.cell(cut, *reference) == antipodal(anchor),
                               "anchor stays fixed through second step")
                resident = native.cell(b2, *target)[0]
                h3.require(resident == h3.mul(factor, gap), "exact target half-gap")
                ratio = h3.mul(resident, h3.inverse(anchor))
                initial_ratio = h3.mul(gap, h3.inverse(anchor))
                h3.require(ratio == h3.mul(factor, initial_ratio), "normalized target/anchor ratio")
                h3.require(native.reverse(b2, 1) == b1
                           and native.reverse(native.reverse(b2, 1), 0) == start,
                           "rewind to the complete original launch")
                records.append({
                    "source_nu": -source_quadratic[2],
                    "test_nu": -test_quadratic[2],
                    "incoming_CORR": incoming,
                    "reader_tag": actual_tag,
                    "normalized_ratio": factor,
                })
        results["distant" if distant else "near"] = records
    return {"Q": stock[3], "launches": 8, **results}
