# SPDX-License-Identifier: Apache-2.0
"""Use the published H3 transport, collision and cyclotomic arithmetic verbatim."""

import hashlib
import importlib.util
from pathlib import Path
import sys

PATH = Path(__file__).resolve().parents[2] / "reproduce" / "h3-referenced-record" / "verify.py"
SOURCE_SHA256 = "4553945d3bf32574ffd55de917859497e9644394f506aaf01ff9492adb8eeedd"
if hashlib.sha256(PATH.read_bytes()).hexdigest() != SOURCE_SHA256:
    raise ValueError("public H3 source digest")

spec = importlib.util.spec_from_file_location("published_h3", PATH)
h3 = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = h3
spec.loader.exec_module(h3)


def empty():
    return [h3.ZERO] * (8 * 4 * 4)


def ix(x, y, rail):
    return h3.index(4, x, y, rail)


def put(field, x, y, words):
    start = ix(x, y, 0)
    field[start:start + 4] = words


def cell(field, x, y):
    start = ix(x, y, 0)
    return tuple(field[start:start + 4])


def ledger(field):
    matter = h3.ring_sum(word for i, word in enumerate(field) if i % 4 < 2)
    radiation = h3.ring_sum(word for i, word in enumerate(field) if i % 4 >= 2)
    hermitian = h3.ring_sum(h3.h(word) for word in field)
    return matter, radiation, hermitian, h3.scalar_account(hermitian)


def reverse(end, bit):
    post_c, _ = h3.collide(end, 4)
    return h3.transport(post_c, 4, bit, backward=True)


def step(field, bit):
    field = tuple(field)
    post_c = h3.transport(field, 4, bit)
    post_b, events = h3.collide(post_c, 4)
    recovered, _ = h3.collide(post_b, 4)
    h3.require(recovered == post_c and h3.transport(recovered, 4, bit, backward=True) == field,
               "complete native inverse")
    h3.require(ledger(field) == ledger(post_c) == ledger(post_b), "complete native accounts")
    return post_c, post_b, events
