# SPDX-License-Identifier: Apache-2.0
"""Independent exact witness checks in the inherited five-coefficient kernel."""

from collections import defaultdict

import kernel as k
import measure as m


REPLAY_LIMIT = 4096
FIRST_WRITE = 159
ANCHOR_RANKS = {0, 22, 43}
WORKER = 28
CELLS = ("writer_c", "writer_b", "donor_pre", "reader_pre", "reader_c", "reader_b")


def vertical_mate(site, bit):
    x, y = divmod(site, k.HEIGHT)
    first = y % 2 == bit
    return x * k.HEIGHT + (y + (1 if first else -1)) % k.HEIGHT, int(not first)


def receiver_transport(receiver, donor, orientation):
    if orientation == 0:
        return tuple(k.contact(a, b)[0] for a, b in zip(receiver[:3], donor[:3]))
    return tuple(k.contact(b, a)[1] for a, b in zip(receiver[:3], donor[:3]))


def local(event, ranks):
    at = event["rank"], event["writer"], event["read"]
    rank, writer, read = at
    reader, bit, write = (event[key] for key in ("reader", "bit", "write"))
    m.require(0 <= rank < ranks and 0 <= writer < 8 * k.HEIGHT
              and 0 <= reader < 8 * k.HEIGHT and bit in (0, 1)
              and 0 < write < read and read % 2 == bit, (at, "event identity"))
    m.require(vertical_mate(reader, bit)[0] == writer, (at, "vertical read edge"))
    m.require(0 <= event["prior"] < write
              and (not event["prior"] or event["writer_tag"] == 2),
              (at, "repeat event identity"))
    m.require(event["anchor"] in (False, True)
              and (not event["anchor"] or (rank in ANCHOR_RANKS
                   and writer == WORKER and write > FIRST_WRITE and write % 2 == 1
                   and event["writer_tag"] == 2)), (at, "anchor event identity"))
    cells = {}
    for name in CELLS:
        cell = event[name]
        m.require(len(cell) == 4 and all(len(word) == 4 for word in cell),
                  (at, name, "four rails in the j basis"))
        cells[name] = tuple(k.from_j(*word) for word in cell)
    m.require(cells["writer_b"][:2] == cells["donor_pre"][:2],
              (at, "the same ordered word arrives at pre-C"))
    # Matter and CLK use the same vertical matching. CORR enters on a
    # horizontal bond and is an observed common input at the local-only horizon.
    _, orientation = vertical_mate(reader, bit)
    projected = receiver_transport(cells["reader_pre"], cells["donor_pre"], orientation)
    m.require(projected == cells["reader_c"][:3], (at, "ordered local C"))
    for role in ("writer", "reader"):
        source, target = cells[f"{role}_c"], cells[f"{role}_b"]
        tag = event[f"{role}_tag"]
        m.require(tag in (1, 2) and source[:2] != target[:2]
                  and k.scatter(source) == (target, tag)
                  and k.scatter(target) == (source, 3 - tag),
                  (at, role, "material write and inverse"))
    return cells


def episode(pre, c, b, tags, site, tick):
    bit = tick % 2
    donor, _ = vertical_mate(site, bit)
    m.require(tags[site] == 2 and pre[site][:2] != c[site][:2]
              and pre[donor][:2] != c[donor][:2] and c[site][:2] != b[site][:2],
              (site, tick, "B2 with native matter contact on both ends"))
    return (site, bit, pre[site], pre[donor][:2], c[site][2:], b[site][:2])


def check_predecessor(launch, rank):
    row, _details = m.trial(launch, 2, rank)
    values = dict(zip(m.HEADER, row))
    m.require(all(values[key] == 1 for key in ("source125", "restore157", "first_local"))
              and (values["work_tick"], values["paid_work_tick"], values["work_site"],
                   values["work_tag"], values["work_offtag"])
              == (FIRST_WRITE, FIRST_WRITE, WORKER, 2, 0),
              (rank, "original #2026 paid first write"))


def check_anchor(pre, c, b, tags, tick, ledger, rank, renewed):
    at = rank, tick, "renewed #2026 anchor"
    m.require(renewed and pre[m.MEMORY][:2] == m.W_WORD and tags[WORKER] == 2
              and pre[WORKER][:2] != c[WORKER][:2] != b[WORKER][:2],
              (at, "native renewal and active read"))
    reference = m.read_projection(pre, (c, b, tags), WORKER)
    m.require(reference is not None, (at, "distinct old-word projection"))
    direct, _inhibit, work, forced_c, forced_b, forced_tag = reference
    m.require(direct and work and forced_c[:2] == pre[WORKER][:2]
              and forced_tag == 0 and forced_b == forced_c,
              (at, "old word would remain idle"))
    # Reuse the published exact account check on a separate witness copy.
    # Neither that copy nor its outcome enters the forward trajectory.
    m.require(m.escrow(pre, tick, WORKER, (forced_c, forced_b, forced_tag),
                       ledger, at) is not None, (at, "funded old-word control"))


def replay(launch, rank, records):
    launch = tuple(tuple(cell) for cell in launch)
    writes, reads, priors = defaultdict(list), defaultdict(list), defaultdict(list)
    anchors = set()
    for index, (event, cells) in enumerate(records):
        writes[event["write"]].append((index, event, cells))
        reads[event["read"]].append((index, event, cells))
        if event["prior"]:
            priors[event["prior"]].append((index, event["writer"]))
        if event["anchor"]:
            anchors.add(event["write"])
    if anchors:
        check_predecessor(launch, rank)
    ledger = k.account(launch)
    m.require(k.reported_account(launch) == m.LEDGER, (rank, "original launch ledger"))
    held, signatures = {}, {}
    field, renewed = launch, False
    for tick in range(1, max(reads) + 1):
        pre = field
        if tick in writes or tick in reads or tick in priors:
            c, field, tags = m.native(pre, tick, ledger, ("renewed witness", rank))
        else:
            c = k.transport(pre, k.HEIGHT, tick % 2)
            field, tags = k.scatter_field(c)

        for index, site in priors.get(tick, ()):
            signatures[index] = episode(pre, c, field, tags, site, tick)
        if tick in anchors:
            check_anchor(pre, c, field, tags, tick, ledger, rank, renewed)

        for index, event, cells in reads.get(tick, ()):
            writer, reader = event["writer"], event["reader"]
            at = rank, tick, writer, reader
            m.require(held.pop(index, None) == (writer, cells["donor_pre"][:2]),
                      (at, "held native output reaches the read"))
            m.require(pre[writer] == cells["donor_pre"]
                      and (pre[reader], c[reader], field[reader], tags[reader])
                      == (cells["reader_pre"], cells["reader_c"], cells["reader_b"],
                          event["reader_tag"]), (at, "full-field read witness"))

        for site, word in held.values():
            m.require(all(cut[site][:2] == word for cut in (pre, c, field)),
                      (rank, site, tick, "interrupted holding of the emitted word"))

        for index, event, cells in writes.get(tick, ()):
            site = event["writer"]
            at = rank, site, tick
            m.require((c[site], field[site], tags[site])
                      == (cells["writer_c"], cells["writer_b"], event["writer_tag"]),
                      (at, "full-field native writer"))
            if event["prior"]:
                m.require(signatures.pop(index, None) == episode(pre, c, field, tags, site, tick),
                          (at, "earlier local episode signature"))
            held[index] = site, cells["writer_b"][:2]

        if anchors and tick > FIRST_WRITE:
            before, after_c, after_b = (cut[m.MEMORY][:2] for cut in (pre, c, field))
            renewed = after_b == m.W_WORD and (
                (renewed and after_c == m.W_WORD)
                or before != m.W_WORD or after_c != m.W_WORD)
    m.require(not held and not signatures, (rank, "unmatched timeline requests"))


def check(fields, pairs):
    """Return counts of distinct local and independently replayed event certificates."""
    unique, by_rank = {}, defaultdict(list)
    for first, second in pairs:
        converted = []
        for event in (first, second):
            identity = tuple(event[key] for key in ("rank", "writer", "reader", "write", "read"))
            if identity in unique:
                prior_event, cells = unique[identity]
                m.require(prior_event == event, (identity, "inconsistent duplicate witness"))
            else:
                cells = local(event, len(fields))
                unique[identity] = event, cells
                if event["read"] <= REPLAY_LIMIT:
                    by_rank[event["rank"]].append((event, cells))
            converted.append(cells)
        a, b = converted
        at = first["rank"], first["read"], second["read"]
        m.require(all(first[key] == second[key] for key in ("rank", "writer", "reader", "bit"))
                  and a["reader_pre"] == b["reader_pre"]
                  and a["reader_c"][2:] == b["reader_c"][2:], (at, "same readiness"))
        m.require({first["reader_tag"], second["reader_tag"]} == {1, 2}
                  and all(a[key][:2] != b[key][:2]
                          for key in ("writer_b", "reader_c", "reader_b")),
                  (at, "distinct emission, arrival and opposite active outcome"))

    for rank, records in sorted(by_rank.items()):
        replay(fields[rank], rank, records)
    return {"events": len(unique), "full_replayed": sum(map(len, by_rank.values()))}
