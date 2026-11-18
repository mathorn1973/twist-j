# SPDX-License-Identifier: Apache-2.0
"""Use the published integer H3 contacts on rectangular even tori."""

import hashlib
import importlib.util
from pathlib import Path
import sys

SOURCE = Path(__file__).resolve().parents[2] / "reproduce/h3-referenced-record/verify.py"
DIGEST = "4553945d3bf32574ffd55de917859497e9644394f506aaf01ff9492adb8eeedd"
if hashlib.sha256(SOURCE.read_bytes()).hexdigest() != DIGEST:
    raise ValueError("public native source digest")
spec = importlib.util.spec_from_file_location("public_h3", SOURCE)
h3 = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = h3
spec.loader.exec_module(h3)


def put(field, ny, x, y, words):
    offset = h3.index(ny, x, y, 0)
    field[offset:offset + 4] = words


def cell(field, ny, x, y):
    offset = h3.index(ny, x, y, 0)
    return tuple(field[offset:offset + 4])


def ledger(field):
    m = h3.ring_sum(a for i, a in enumerate(field) if i % 4 < 2)
    u = h3.ring_sum(a for i, a in enumerate(field) if i % 4 >= 2)
    h = h3.ring_sum(h3.h(a) for a in field)
    return m, u, h, h3.scalar_account(h)


def transport(field, ny, bit, backward=False):
    nx, remainder = divmod(len(field), 4 * ny)
    h3.require(not remainder and nx >= 2 and ny >= 2 and not (nx % 2 or ny % 2),
               "complete rectangular even torus")
    # NX is the public reproduction's geometry parameter. Restore it after each call.
    original = h3.NX
    try:
        h3.NX = nx
        return h3.transport(field, ny, bit, backward)
    finally:
        h3.NX = original


def reverse(field, ny, old_bit):
    pre_b, _ = h3.collide(tuple(field), ny)
    return transport(pre_b, ny, old_bit, backward=True)


def step(field, ny, bit):
    field = tuple(field)
    c = transport(field, ny, bit)
    b, tags = h3.collide(c, ny)
    before_b, _ = h3.collide(b, ny)
    h3.require(before_b == c and reverse(b, ny, bit) == field, "whole native inverse")
    h3.require(ledger(field) == ledger(c) == ledger(b), "complete M/U/H/Q")
    return c, b, tags
