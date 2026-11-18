# SPDX-License-Identifier: Apache-2.0
"""Exact native axis emission from a single prepared H3 material site."""

from native import cell, h3, ledger, put, reverse, step


SIZE, HORIZON = 24, 10
ZERO = h3.ZERO
CENTER = h3.add(h3.ONE, h3.scale(2, h3.add(h3.RHO, h3.mul(h3.RHO, h3.RHO))))
OUTGOING = h3.sub(h3.ONE, h3.RHO)


def launch(gap):
    field = [ZERO] * (4 * SIZE * SIZE)
    put(field, SIZE, 0, 0, (h3.ONE, h3.scale(-1, h3.ONE),
                            h3.add(CENTER, gap), h3.sub(CENTER, gap)))
    return tuple(field)


def support(field):
    result = [[], [], [], []]
    for i, word in enumerate(field):
        if word != ZERO:
            x, y = divmod(i // 4, SIZE)
            result[i % 4].append((x, y))
    return result


def case(tag, gap):
    initial = launch(gap)
    full = initial
    stock = ledger(initial)
    first = {}
    cuts = []
    for tick in range(1, HORIZON + 1):
        bit = (tick - 1) % 2
        c, b, tags = step(full, SIZE, bit)
        h3.require(reverse(b, SIZE, bit) == full and ledger(b) == stock,
                   "native axis inverse and complete accounts")
        if tick == 1:
            source = cell(b, SIZE, 0, 0)
            first = {"c_idle": c == initial, "tags": tags, "post_b_source": source,
                     "branch_match": tags == ((0, 0, tag),) and source == (
                         gap, h3.scale(-1, gap), h3.add(CENTER, h3.ONE),
                         h3.sub(CENTER, h3.ONE))}
        if tick == 2:
            clk = cell(c, SIZE, 0, SIZE - 1)[2]
            corr = cell(c, SIZE, SIZE - 1, 0)[3]
            first["emission_neighbors"] = [[0, -1], [-1, 0]]
            first["post_c_neighbor_words"] = [clk, corr]
            first["post_c_neighbor_h"] = [h3.h(clk), h3.h(corr)]
            expected = [h3.mul(OUTGOING, h3.half(word))
                        for word in (h3.add(CENTER, h3.ONE), h3.sub(CENTER, h3.ONE))]
            first["equal_nonzero_neighbor_h"] = h3.h(clk) == h3.h(corr) != ZERO
            first["expected_neighbor_words"] = [clk, corr] == expected
        for stage, state in (("C", c), ("B", b)):
            r0, r2, clk, corr = support(state)
            cuts.append({
                "tick": tick, "stage": stage,
                "material_source_only": r0 == r2 == [(0, 0)],
                "clk_off_axis": [(x, y) for x, y in clk if x != 0],
                "corr_off_axis": [(x, y) for x, y in corr if y != 0],
                "radiation_axis_sizes": [len(clk), len(corr)],
                "off_source_active_b": ([(x, y, mode) for x, y, mode in tags
                                         if (x, y) != (0, 0)] if stage == "B" else []),
            })
        full = b
    return {
        "branch": tag, "initial_rail_residues_nonzero": [
            not h3.even(word) for word in cell(initial, SIZE, 0, 0)
        ],
        "first_two_ticks": first, "cuts": cuts,
        "passed": first["c_idle"] and first["branch_match"]
                  and first["equal_nonzero_neighbor_h"] and first["expected_neighbor_words"]
                  and all(row["material_source_only"] and not row["clk_off_axis"]
                          and not row["corr_off_axis"] and not row["off_source_active_b"]
                          for row in cuts),
    }


def run():
    rows = [case(1, h3.J), case(2, h3.J_INV)]
    anti_real = h3.conj(CENTER) == h3.scale(-1, CENTER)
    center_is_one_mod_two = h3.even(h3.sub(CENTER, h3.ONE))
    return {"passed": anti_real and center_is_one_mod_two and all(
                row["passed"] and all(row["initial_rail_residues_nonzero"]) for row in rows),
            "geometry": [SIZE, SIZE], "initial_bit": 0, "horizon": HORIZON,
            "center": CENTER, "center_anti_real": anti_real,
            "center_is_one_mod_two": center_is_one_mod_two, "cases": rows}
