# SPDX-License-Identifier: Apache-2.0
"""Independent H3 relay measurement using the previously published exact kernel."""

import kernel as k


HEADER = (
    "mode rank source125 restore157 first_local read_tick inhibit_tick work_tick "
    "work_site work_tag work_offtag escrow_tick retained_read_tick retained_work_tick "
    "paid_effect_tick paid_work_tick"
).split()
LEDGER = ((-9, 2, -2, -3), (19, 7, 5, 19), (463, 0, 152, 152), 774)
SOURCE, MEMORY = 7, 31
T = k.from_j(1, 1, 1, 1)
W = k.from_j(1, 0, 1, 1)
T_WORD = T, k.scale(-1, T)
W_WORD = W, k.scale(-1, W)


def require(ok, context):
    if not ok:
        raise AssertionError(context)


def native(field, tick, ledger, context):
    bit = tick % 2
    post_c = k.transport(field, k.HEIGHT, bit)
    post_b, tags = k.scatter_field(post_c)
    recovered_c, inverse_tags = k.scatter_field(post_b)
    require(recovered_c == post_c, (context, tick, "inverse B"))
    require(inverse_tags == tuple((3 - tag) if tag else 0 for tag in tags),
            (context, tick, "inverse tags"))
    require(k.transport(recovered_c, k.HEIGHT, bit, -1) == field,
            (context, tick, "inverse C"))
    require(k.account(post_c) == ledger, (context, tick, "C account"))
    require(k.account(post_b) == ledger, (context, tick, "B account"))
    return post_c, post_b, tags


def replace(field, site, cell):
    return (*field[:site], cell, *field[site + 1:])


def triple(pre, cut, site):
    post_c, post_b, tags = cut
    return {
        "pre_C": [k.reported(word) for word in pre[site]],
        "post_C": [k.reported(word) for word in post_c[site]],
        "post_B": [k.reported(word) for word in post_b[site]],
        "tag": tags[site],
    }


def read_projection(pre, live_cut, worker):
    live_c, live_b, live_tag = live_cut
    forced_matter = tuple(
        k.contact(pre[worker][lane], T_WORD[lane])[0] for lane in range(2)
    )
    forced_c = (*forced_matter, *live_c[worker][2:])
    forced_b, forced_tag = k.scatter(forced_c)
    live_moves = live_c[worker][:2] != pre[worker][:2]
    forced_moves = forced_matter != pre[worker][:2]
    if live_c[worker][:2] == forced_matter or not (live_moves or forced_moves):
        return None
    work = (
        live_tag[worker] in (1, 2)
        and live_b[worker][:2] != live_c[worker][:2]
        and live_b[worker][:2] != forced_b[:2]
        and live_tag[worker] != forced_tag
    )
    return live_moves, not live_moves and forced_moves, work, forced_c, forced_b, forced_tag


def matches_off(pre, off_pre, live_cut, off_cut, worker, forced_c, forced_b, forced_tag):
    if off_pre[MEMORY][:2] != T_WORD or pre[worker] != off_pre[worker]:
        return False
    live_c = live_cut[0]
    off_c, off_b, off_tags = off_cut
    return (
        live_c[worker][2:] == off_c[worker][2:]
        and forced_c[:2] == off_c[worker][:2]
        and forced_b[:2] == off_b[worker][:2]
        and forced_tag == off_tags[worker]
    )


def escrow(pre, tick, worker, expected, ledger, context):
    for payer, cell in enumerate(pre[:28]):
        if cell[:2] == T_WORD:
            compensated = replace(pre, MEMORY, (*T_WORD, *pre[MEMORY][2:]))
            compensated = replace(compensated, payer, (*W_WORD, *cell[2:]))
            require(k.account(compensated) == ledger, (context, tick, "escrow account"))
            post_c, post_b, tags = native(compensated, tick, ledger, (*context, "escrow"))
            require((post_c[worker], post_b[worker], tags[worker]) == expected,
                    (context, tick, "escrow projection", payer, worker))
            return payer
    return None


def trial(field, mode, rank, details=False):
    """Return the integer ABI row and optional exact local witnesses for one launch."""
    context = mode, rank
    field = tuple(tuple(cell) for cell in field)
    require(k.reported_account(field) == LEDGER, (context, "launch account"))
    ledger = k.account(field)
    row = dict.fromkeys(HEADER, 0)
    row.update(mode=mode, rank=rank)
    report = {}
    live, off = field, None
    first_difference = None
    uninterrupted = False
    retained_through = None

    for tick in range(1, 165):
        live_pre, off_pre = live, off
        live_cut = native(live_pre, tick, ledger, (*context, "live"))
        live_c, live, live_tags = live_cut
        if tick == 125 and live_tags[SOURCE] == 2:
            row["source125"] = 1
            pulled, inverse_tag = k.scatter(live[SOURCE])
            require((pulled, inverse_tag) == (live_c[SOURCE], 1),
                    (context, tick, "source undo"))
            off = replace(live, SOURCE, pulled)
            require(k.account(off) == ledger, (context, tick, "source undo account"))
            if details:
                report["source"] = {
                    "tick": tick, "bit": tick % 2, "site": SOURCE,
                    "live": triple(live_pre, live_cut, SOURCE),
                    "source_off_post_B": [k.reported(word) for word in off[SOURCE]],
                    "inverse_tag": inverse_tag,
                }
        if off_pre is None:
            continue

        off_cut = native(off_pre, tick, ledger, (*context, "source_off"))
        off_c, off, off_tags = off_cut
        if first_difference is None:
            if live_c[MEMORY] != off_c[MEMORY]:
                first_difference = tick, "C"
            elif live[MEMORY] != off[MEMORY]:
                first_difference = tick, "B"

        if tick == 157:
            restored = (
                live_c[MEMORY][:2] == T_WORD
                and live[MEMORY][:2] == W_WORD
                and live_tags[MEMORY] == 1
                and live_c[MEMORY][:3] == off_c[MEMORY][:3]
                and live_c[MEMORY][3] != off_c[MEMORY][3]
                and off_tags[MEMORY] == 0
                and off[MEMORY][:2] == T_WORD
            )
            row["restore157"] = int(restored)
            row["first_local"] = int(restored and first_difference == (157, "C"))
            uninterrupted = restored
            if details:
                report["restore"] = {
                    "tick": tick, "bit": tick % 2, "site": MEMORY,
                    "live": triple(live_pre, live_cut, MEMORY),
                    "source_off": triple(off_pre, off_cut, MEMORY),
                    "first_local_difference": first_difference,
                }
                retained_through = (157, "B") if restored else None
            continue
        if tick < 158 or not uninterrupted:
            continue

        require(live_pre[MEMORY][:2] == W_WORD, (context, tick, "live hold pre-C"))
        worker = 28 if tick % 2 else 30
        result = read_projection(live_pre, live_cut, worker)
        if result is not None:
            direct, inhibit, work, forced_c, forced_b, forced_tag = result
            strict = matches_off(live_pre, off_pre, live_cut, off_cut, worker,
                                 forced_c, forced_b, forced_tag)
            payer = escrow(live_pre, tick, worker, (forced_c, forced_b, forced_tag),
                           ledger, context)
            paid = payer is not None
            conditions = (
                ("read_tick", strict and direct),
                ("inhibit_tick", strict and inhibit),
                ("work_tick", strict and work),
                ("escrow_tick", strict and paid),
                ("retained_read_tick", strict and tick >= 159),
                ("retained_work_tick", strict and work and tick >= 159),
                ("paid_effect_tick", paid),
                ("paid_work_tick", paid and work),
            )
            first = [key for key, scored in conditions if scored and not row[key]]
            for key in first:
                row[key] = tick
            if "work_tick" in first:
                row.update(work_site=worker, work_tag=live_tags[worker], work_offtag=off_tags[worker])
            if details and first:
                witness = {
                    "tick": tick, "bit": tick % 2,
                    "source": SOURCE, "memory": MEMORY, "worker": worker,
                    "live_memory": triple(live_pre, live_cut, MEMORY),
                    "source_off_memory": triple(off_pre, off_cut, MEMORY),
                    "live_worker": triple(live_pre, live_cut, worker),
                    "source_off_worker": triple(off_pre, off_cut, worker),
                    "hybrid_worker_post_C": [k.reported(word) for word in forced_c],
                    "hybrid_worker_post_B": [k.reported(word) for word in forced_b],
                    "hybrid_worker_tag": forced_tag,
                    "escrow_site": payer,
                    "actual_moves_at_C": direct,
                    "hybrid_moves_at_C": forced_c[:2] != live_pre[worker][:2],
                    "strict_source_off_match": strict,
                }
                for key in first:
                    report[key] = witness

        if live_c[MEMORY][:2] != W_WORD:
            uninterrupted = False
        else:
            if details:
                retained_through = tick, "C"
            if live[MEMORY][:2] != W_WORD:
                uninterrupted = False
            elif details:
                retained_through = tick, "B"

    if details:
        report["live_retained_through"] = retained_through
    return [row[key] for key in HEADER], report
