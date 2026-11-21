# SPDX-License-Identifier: Apache-2.0
"""Two native ticks from an exact fixed preparation with two launch encodings."""

from collections import defaultdict

import kernel as k
import measure as m


CLOCK_SITES = (0, 1, 4, 5, 8, 9)
BANK_SITE = 6
BANK = ((-5, 1, -1, -3), (-4, 1, -1, 0), (-1, 0, -2, 5), (-1, 0, -3, 5))
WRITER = ((-1, 0, 0, 0), (1, 0, 0, 0), (2, 1, 2, 0), (0, 1, 0, 0))
READER = ((-1, -1, 0, 1), (1, 1, 0, -1), (1, 0, 0, -1), (0, -1, 0, 0))
INPUT = ((3, 0, 2, 2), (-3, 0, -2, -2), (0, 0, 0, 0), (0, 0, 0, 0))
OUTPUT = ((0, 1, 0, 1), (-1, -1, 0, -1))


def words(cell):
    return tuple(k.from_j(*word) for word in cell)


def reported(cell):
    return tuple(k.reported(word) for word in cell)


def launch(bare, writer, reader, sign):
    prepared = list(bare)
    prepared[BANK_SITE] = words(BANK)
    prepared[writer] = words(WRITER)
    prepared[reader] = words(READER)
    encoded = words(INPUT)
    if sign == "-":
        encoded = (encoded[1], encoded[0], *encoded[2:])
    prepared[writer + 3] = encoded
    return tuple(prepared)


def step_path(initial, ledger, label):
    first = m.native(initial, 1, ledger, label)
    second = m.native(first[1], 2, ledger, label)
    m.require(k.inverse_step(k.inverse_step(second[1], 0), 1) == initial,
              (label, "complete two-tick native inverse"))
    return first, second


def swap(field, writer, a, b):
    current = field[writer][:2]
    m.require(a != b and current in (a, b), "unmatched writer swap")
    return m.replace(field, writer, (*(b if current == a else a), *field[writer][2:]))


def outcome(pre, stages, reader):
    contact, complete, tags = stages
    return {
        "pre_C": reported(pre[reader]),
        "post_C": reported(contact[reader]),
        "post_B": reported(complete[reader]),
        "tag": tags[reader],
        "material_write": contact[reader][:2] != complete[reader][:2],
    }


def one(bare, x, rank):
    writer = x * 4
    reader = writer + 1
    m.require(k.reported_account(bare) == k.BARE_ACCOUNTS, (rank, "bare account"))
    failures = []
    initial = [launch(bare, writer, reader, sign) for sign in ("+", "-")]
    altered = [tuple(i for i, (old, new) in enumerate(zip(bare, field)) if old != new)
               for field in initial]
    clocks = all(field[site][3] == bare[site][3]
                 for field in initial for site in CLOCK_SITES)
    if not clocks:
        failures.append("original_clock_CORR_changed")
    initial_accounts = [k.reported_account(field) for field in initial]
    if any(account != m.LEDGER for account in initial_accounts):
        failures.append("launch_account")
        return failures, {}, {
            "rank": rank, "altered_sites": altered, "original_clock_CORR": clocks,
            "launch_accounts": initial_accounts,
        }

    ledger = k.account(initial[0])
    paths = [step_path(state, ledger, (x, rank, sign))
             for state, sign in zip(initial, ("+", "-"))]
    first = [a for a, _ in paths]
    second = [b for _, b in paths]
    first_fields = [a[1] for a in first]
    pairs = [f[writer][:2] for f in first_fields]
    first_b2 = all(a[2][writer] == 2 and a[0][writer][:2] != a[1][writer][:2] for a in first)
    expected = [k.from_j(*v) for v in OUTPUT]
    first_words = tuple(pairs) == tuple((v, k.scale(-1, v)) for v in expected)
    identical_pre = first_fields[0][reader] == first_fields[1][reader]
    identical_rad = second[0][0][reader][2:] == second[1][0][reader][2:]
    receiver_taken = all(a[0][reader][:2] != a[1][reader][:2] for a in second)
    distinct_material = second[0][1][reader][:2] != second[1][1][reader][:2]
    tags = tuple(a[2][reader] for a in second)
    checks = {
        "first_writer_B2_both": first_b2,
        "first_writer_expected_words": first_words,
        "same_reader_pre_C": identical_pre,
        "same_reader_post_C_radiation": identical_rad,
        "reader_material_work_both": receiver_taken,
        "distinct_reader_material_outputs": distinct_material,
        "reader_tags_B1_and_B2": set(tags) == {1, 2},
        "writer_only_swaps_preserve_accounts": False,
        "writer_only_swaps_switch_reader": False,
    }
    swapped_details = []
    if pairs[0] != pairs[1]:
        swapped_starts = [swap(field, writer, *pairs) for field in first_fields]
        funded = all(k.account(field) == ledger for field in swapped_starts)
        checks["writer_only_swaps_preserve_accounts"] = funded
        if funded:
            switches = []
            for arm, swap_start in enumerate(swapped_starts):
                opposite = 1 - arm
                cut = m.native(swap_start, 2, ledger, (x, rank, arm, "writer-only swap"))
                m.require(swap(swap_start, writer, *pairs) == first_fields[arm],
                          (x, rank, arm, "swap involution"))
                restored_cut = k.inverse_step(cut[1], 0)
                restore_first = swap(restored_cut, writer, *pairs)
                m.require(k.inverse_step(restore_first, 1) == initial[arm],
                          (x, rank, arm, "complete swapped inverse"))
                native = second[opposite]
                same_opposite = (swap_start[reader] == first_fields[opposite][reader]
                                 and cut[0][reader] == native[0][reader]
                                 and cut[1][reader] == native[1][reader]
                                 and cut[2][reader] == native[2][reader])
                switches.append(same_opposite and cut[2][reader] != second[arm][2][reader])
                swapped_details.append(outcome(swap_start, cut, reader))
            checks["writer_only_swaps_switch_reader"] = all(switches)
    failures.extend(name for name, ok in checks.items() if not ok)
    detail = {
        "rank": rank,
        "altered_sites": altered,
        "original_clock_CORR": clocks,
        "launch_accounts": initial_accounts,
        "reader_tags_plus_minus": tags,
        "native_writer_tick_1": [outcome(state, stages, writer)
                                 for state, stages in zip(initial, first)],
        "native_reader_tick_2": [outcome(state, stages, reader)
                                 for state, stages in zip(first_fields, second)],
        "writer_only_swap_reader_tick_2": swapped_details,
    }
    return failures, checks, detail


def run(bare_fields):
    m.require(len(bare_fields) == 85, "expected exactly 85 inherited launch fields")
    result = {
        "initial_bit": 1,
        "bit_encoding_order": ["+", "-"],
        "original_clock_CORR_sites": CLOCK_SITES,
        "prepared_data": {
            "bank_site": BANK_SITE, "bank": BANK,
            "writer_y0": WRITER, "reader_y1": READER,
            "input_y3_plus": INPUT, "input_y3_minus": (INPUT[1], INPUT[0], *INPUT[2:]),
        },
        "expected_writer_outputs_first_rail": OUTPUT,
        "layouts": {},
    }
    for x in (5, 7):
        failed = defaultdict(list)
        passed = []
        tag_counts = defaultdict(int)
        examples = {}
        for rank, raw_field in enumerate(bare_fields):
            bare = tuple(map(tuple, raw_field))
            failures, checks, detail = one(bare, x, rank)
            for name in failures:
                failed[name].append(rank)
            if not failures:
                passed.append(rank)
            tags = detail.get("reader_tags_plus_minus")
            if tags is not None:
                tag_counts["/".join(map(str, tags))] += 1
            if rank == 43:
                examples["rank43"] = {**detail, "checks": checks}
            if not failures and "first_pass" not in examples:
                examples["first_pass"] = {**detail, "checks": checks}
            if failures and "first_fail" not in examples:
                examples["first_fail"] = {**detail, "checks": checks}
        result["layouts"][str(x)] = {
            "writer": 4 * x,
            "reader": 4 * x + 1,
            "input": 4 * x + 3,
            "raw_count": len(bare_fields),
            "all_checks_pass_ranks": passed,
            "failure_ranks": dict(sorted(failed.items())),
            "reader_tag_pair_counts": dict(sorted(tag_counts.items())),
            "examples": examples,
        }
    return result
