# SPDX-License-Identifier: Apache-2.0
"""Local identities on the public P-H3-THIRD-CELL-1 rank-43 receiver cuts."""

import json
from pathlib import Path

from native import h3


SOURCE_COMMIT = "3d49695af98440bdb9d97b05a40cad2f0a8934a5"
SOURCE_EXPECTED_SHA256 = "5b7d773d9d80f636128911ad83b363a5e0d246944b5e37ee041a6fbf0724bcf2"
SOURCE_KEY = "28/31/matter/two_active_tags"
FIXTURE = Path(__file__).with_name("receiver_cuts.json")

# Collision work in Z[j], with s = j^2 + j^3. Both entries have scalar -2.
EXPECTED_WORK = {135: (0, 0, 2, 2), 671: (-2, 0, -2, -2)}


def ell(word):
    return word[3] - word[1]


def words(raw):
    return tuple(map(tuple, raw))


def squared(words_in_sector):
    return h3.ring_sum(h3.h(word) for word in words_in_sector)


def audit_cut(record):
    tick, bit, moved, tag = (record[key] for key in ("tick", "bit", "matter_moved", "tag"))
    pre = words(record["receiver_pre_C"])
    post_c = words(record["receiver_post_C"])
    post_b = words(record["receiver_post_B"])
    donor = words(record["donor_pre_C_matter"])
    h3.require(bit == 1, "both archived reads use the odd matching")
    h3.require(pre[2:] == post_c[2:], "archived receiver radiation stays fixed through C")

    # Receiver 31 is row 3 and donor 28 is row 0 of the same column.
    # Native C matches in order (31,28), so its forward orientation is
    # receiver-to-donor. Report the negatives as donor-to-receiver flow.
    into_receiver = []
    for left, right, observed in zip(pre[:2], donor, post_c[:2]):
        next_left, next_right = h3.transport_pair(left, right, False)
        h3.require(next_left == observed, "archived receiver matter C does not replay")
        h3.require(h3.transport_pair(next_left, next_right, True) == (left, right), "contact inverse")
        flow = h3.sub(next_left, left)
        h3.require(flow == h3.sub(right, next_right), "contact continuity")
        into_receiver.append(flow)
    h3.require(any(word != h3.ZERO for word in into_receiver) == bool(moved), "matter-move marker")
    net = h3.ring_sum(into_receiver)
    h3.require(net == h3.ZERO, "transported algebraic matter sum is zero")

    observed, observed_tag = h3.collision(post_c)
    h3.require(observed == post_b and observed_tag == tag, "archived receiver B does not replay")
    restored, inverse_tag = h3.collision(post_b)
    h3.require(restored == post_c and inverse_tag == 3 - tag, "reciprocal B branch inverse")

    d, f = (h3.half(h3.sub(post_c[i], post_c[i + 1])) for i in (0, 2))
    dn, fn = (h3.half(h3.sub(post_b[i], post_b[i + 1])) for i in (0, 2))
    exponent = 1 if tag == 1 else -1
    unit = h3.J if tag == 1 else h3.J_INV
    inverse_unit = h3.J_INV if tag == 1 else h3.J
    relative_multiplier = h3.mul(unit, unit)
    h3.require(d != h3.ZERO and f != h3.ZERO, "active matter and radiation gap")
    h3.require(dn == h3.mul(unit, d) and fn == h3.mul(inverse_unit, f), "reciprocal gap multipliers")
    h3.require(h3.mul(dn, f) == h3.mul(relative_multiplier, h3.mul(d, fn)), "relative phase multiplier")

    matter = h3.sub(squared(post_b[:2]), squared(post_c[:2]))
    radiation = h3.sub(squared(post_b[2:]), squared(post_c[2:]))
    delta_q = [h3.scalar_account(value) for value in (matter, radiation)]
    h3.require(matter == EXPECTED_WORK[tick] and radiation == h3.scale(-1, matter), "ring work")
    h3.require(delta_q == [-2, 2], "both work deposits have the same traced accounts")
    return {
        "tick": tick,
        "tag": tag,
        "matter_gap_J_exponent": exponent,
        "relative_gap_J_exponent": 2 * exponent,
        "relative_gap_multiplier_j_coordinates": relative_multiplier,
        "donor_to_receiver_ell_by_rail": list(map(ell, into_receiver)),
        "donor_to_receiver_ell_total": ell(net),
        "B_delta_H_matter": matter,
        "B_delta_H_radiation": radiation,
        "B_delta_Q_matter": delta_q[0],
        "B_delta_Q_radiation": delta_q[1],
        "B_delta_Q_total": sum(delta_q),
    }


def run():
    data = json.loads(FIXTURE.read_text(encoding="utf-8"))
    h3.require(
        (data["source_commit"], data["expected_sha256"], data["key"], data["rank"])
        == (SOURCE_COMMIT, SOURCE_EXPECTED_SHA256, SOURCE_KEY, 43),
        "public receiver fixture metadata",
    )
    cuts = data["cuts"]
    h3.require([(cut["tick"], cut["tag"]) for cut in cuts] == [(135, 1), (671, 2)], "public cut selection")
    h3.require(cuts[0]["receiver_pre_C"] == cuts[1]["receiver_pre_C"], "same prefunded receiver input")
    results = [audit_cut(cut) for cut in cuts]
    h3.require(results[0]["B_delta_H_matter"] != results[1]["B_delta_H_matter"], "distinct active ring work")
    return {"rank": 43, "receiver": 31, "donor": 28, "local_witnesses": results}
