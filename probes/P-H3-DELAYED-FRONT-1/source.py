# SPDX-License-Identifier: Apache-2.0
"""Native capture helpers from the registered route-length experiment."""
import kernel as k

WIDTH = 8
A = k.HEIGHT + 3
WINDOW = 128
MAX_LENGTH = 4
LOOKAHEAD = MAX_LENGTH + 1
LENGTHS = tuple(range(1, MAX_LENGTH + 1))
DIRECTIONS = {-1: "west", 1: "east"}

def check(predicate, *context):
    if not predicate:
        raise AssertionError(context)


def checked_step(field, bit, conserved, digest, label):
    events = k.Witnesses()
    result = k.transition(field, bit, conserved, events, label, digest)
    check(not events.counts, label, events.report())
    return result[:3]


def digest_cut(digest, cut, bit):
    digest.update(bytes((bit,)))
    k.trace_cut(digest, cut)


def local_contact_phase(before, after, donor, target, label):
    gap_before = k.subtract(before[donor][k.CORR], before[target][k.CORR])
    gap_after = k.subtract(after[donor][k.CORR], after[target][k.CORR])
    if gap_before == k.ZERO:
        check(gap_after == k.ZERO, "equal pair changed gap", label)
        return None
    if k.even(gap_before):
        check(gap_after == k.multiply(k.RHO, gap_before), "admitted phase", label)
        return 2
    check(gap_after == gap_before, "refused phase", label)
    return 0
