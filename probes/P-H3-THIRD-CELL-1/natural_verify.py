# SPDX-License-Identifier: Apache-2.0
"""Independently replay selected native matched encounters in five coefficients."""

import argparse
from collections import defaultdict
from dataclasses import dataclass

import kernel as k
import measure as m


def cells(coefficients):
    if len(coefficients) % 16 != 0:
        raise ValueError("incomplete cell")
    words = tuple(k.from_j(*coefficients[i:i + 4])
                  for i in range(0, len(coefficients), 4))
    return tuple(words[i:i + 4] for i in range(0, len(words), 4))


@dataclass(frozen=True)
class Arm:
    carrier: str
    writer: int
    reader: int
    rank: int
    write_tick: int
    write_tag: int
    tick: int
    bit: int
    moved: int
    receiver_tag: int
    write_c: tuple
    write_b: tuple
    donor_pre: tuple
    donor_c: tuple
    donor_b: tuple
    pre: tuple
    c: tuple
    b: tuple

    def carried(self, cell):
        return cell[:2] if self.carrier == "matter" else cell[2:3]

    def material_work(self):
        return self.c[:2] != self.b[:2]

    def readiness(self):
        other = self.c[2:] if self.carrier == "matter" else (*self.c[:2], self.c[3])
        return self.writer, self.reader, self.bit, self.pre, other


def launch_rows(stream):
    rows = {}
    for line in stream:
        mode, rank, depth, *coefficients = map(int, line.split())
        m.require(mode == 2 and depth == 0 and rank not in rows,
                  (mode, rank, depth, "invalid launch ID"))
        row = cells(coefficients)
        m.require(len(row) == 32 and k.reported_account(row) == m.LEDGER,
                  (rank, "invalid launch"))
        rows[rank] = row
    m.require(set(rows) == set(range(85)), "incomplete launch ranks")
    return rows


def witness_rows(stream):
    grouped = defaultdict(list)
    first_writes = {}
    for line in stream:
        fields = line.split()
        if fields and fields[0] == "ARM":
            contrast, side, carrier, *numbers = fields[1:]
            fields = list(map(int, numbers))
            arm = Arm(carrier, *fields[:9], *cells(fields[9:]))
            grouped[(arm.writer, arm.reader, carrier, contrast)].append((int(side), arm))
        elif fields and fields[0] == "WRITES":
            rank, site, b1, b2, tick, tag, *coefficients = map(int, fields[1:])
            if rank == 43 and site in (29, 30) and b1 + b2:
                first_writes[site] = (tick, tag, *cells(coefficients))
    return grouped, first_writes


def check_pair(key, pair):
    m.require([side for side, _ in pair] == [1, 2], (key, "missing paired arm"))
    a, b = (arm for _, arm in pair)
    m.require(a.readiness() == b.readiness(), (key, "readiness"))
    m.require(a.carried(a.donor_pre) != b.carried(b.donor_pre), (key, "equal input"))
    contrast = key[-1]
    correct = {
        "distinct_input": True,
        "distinct_C": a.carried(a.c) != b.carried(b.c),
        "active_idle": a.material_work() != b.material_work(),
        "same_tag_distinct_material": (
            a.material_work() and b.material_work()
            and a.receiver_tag == b.receiver_tag and a.b[:2] != b.b[:2]
        ),
        "two_active_tags": a.material_work() and b.material_work()
                           and a.receiver_tag != b.receiver_tag,
    }
    m.require(correct[contrast], (key, "contrast"))


def replay(launch, rank, arms, first_writes):
    starts = defaultdict(list)
    reads = defaultdict(list)
    for arm in arms:
        m.require((arm.writer, arm.reader, arm.bit) in {(28, 29, 0), (28, 31, 1), (29, 30, 1)},
                  (rank, arm.tick, "native vertical edge"))
        m.require(arm.tick > arm.write_tick and arm.tick % 2 == arm.bit,
                  (rank, arm.tick, "matching and order"))
        starts[arm.write_tick].append(arm)
        reads[arm.tick].append(arm)

    ledger = k.account(launch)
    field = launch
    held = set()
    first_ticks = {sample[0] for sample in first_writes.values()}
    pending = set(first_writes)
    for tick in range(1, max((*reads, *first_ticks), default=0) + 1):
        pre = field
        if tick in starts or tick in reads or tick in first_ticks:
            contact, field, tags = m.native(pre, tick, ledger, ("native witness", rank))
        else:
            contact, field = k.native_step(pre, tick % 2)

        for site in tuple(pending):
            if contact[site][:2] == field[site][:2]:
                continue
            m.require((tick, k.scatter(contact[site])[1], contact[site], field[site])
                      == first_writes[site], (rank, site, tick, "first native material write"))
            pending.remove(site)

        for arm in reads.get(tick, ()):
            m.require(arm in held, (rank, tick, "missing writer provenance"))
            held.remove(arm)
            writer, reader = arm.writer, arm.reader
            m.require(
                (pre[writer], contact[writer], field[writer]) ==
                (arm.donor_pre, arm.donor_c, arm.donor_b) and
                (pre[reader], contact[reader], field[reader]) == (arm.pre, arm.c, arm.b) and
                tags[reader] == arm.receiver_tag and
                arm.moved == (arm.carried(arm.pre) != arm.carried(arm.c)),
                (rank, tick, "native encounter projection"),
            )
            m.require(arm.carried(pre[writer]) == arm.carried(arm.write_b),
                      (rank, tick, "native delivered carrier"))

        for arm in held:
            writer = arm.writer
            word = arm.carried(arm.write_b)
            m.require(all(arm.carried(cut[writer]) == word for cut in (pre, contact, field)),
                      (rank, tick, "interrupted carrier retention"))

        for arm in starts.get(tick, ()):
            writer = arm.writer
            m.require(
                (contact[writer], field[writer], tags[writer]) ==
                (arm.write_c, arm.write_b, arm.write_tag) and
                arm.write_c[:2] != arm.write_b[:2] and
                arm.carried(arm.write_c) != arm.carried(arm.write_b),
                (rank, tick, "authentic native writer output"),
            )
            held.add(arm)

    m.require(not held and not pending, (rank, "incomplete witness replay"))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("launches", type=argparse.FileType("r", encoding="ascii"))
    parser.add_argument("records", type=argparse.FileType("r", encoding="ascii"))
    args = parser.parse_args()
    launches = launch_rows(args.launches)
    witnesses, first_writes = witness_rows(args.records)
    by_rank = defaultdict(set)
    for key, pair in witnesses.items():
        check_pair(key, pair)
        for _, arm in pair:
            by_rank[arm.rank].add(arm)
    if first_writes:
        by_rank[43]
    for rank in sorted(by_rank):
        replay(launches[rank], rank, by_rank[rank], first_writes if rank == 43 else {})
    print(f"independent raw-43 first writes at sites 29 and 30: {len(first_writes)}")
    print(f"native matched witnesses: {len(witnesses)} pairs across {len(by_rank)} ranks")


if __name__ == "__main__":
    main()
