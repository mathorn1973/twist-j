#!/usr/bin/env python3
"""Audit the prospectively pinned receiver construction from hash-checked sources."""

from hashlib import sha256
from pathlib import Path
import sys
from types import ModuleType


ROOT = Path(__file__).resolve().parents[2]
NOTE = "notes/C-FIELD-RECEIVER-BOUNDED-RECORD-N/"
SOURCE_SHA256 = {
    'notes/C-FIELD-RECEIVER-BOUNDED-RECORD-N/PREREG.md': '51e9d854f94f7486dbd5034e548fecb5f9d52fc96a2b710e4fca3d83b48489c6',
    'notes/C-FIELD-RECEIVER-BOUNDED-RECORD-N/PROOF.md': 'e410d85a0bba2980dd266a540f75ca436255141a9e038e5f4e42f35413c6e7e9',
    'notes/C-FIELD-RECEIVER-BOUNDED-RECORD-N/audit.py': 'e18149ae8f5cfba1786511a6c44af458a792a1cbbfa06b28ce33cccba779ef67',
    'notes/C-FIELD-RECEIVER-BOUNDED-RECORD-N/audit_challenger.py': '557e306b68114f159f189cbfc5f5ebb6293e10c0e6cc17640e6eb34b04bdd92a',
    'notes/C-FIELD-THREE-CELL-DELAYED-TRANSFER-N/PREREG.md': '9b9f0c6ceab706474ac74ed0229df30fafced164ad128400770315a18796aa7d',
    'notes/C-FIELD-THREE-CELL-DELAYED-TRANSFER-N/PROOF.md': 'd439f642b3447aec34efa3951ac70575182686b3168f44d89a53039ad90948b7',
    'notes/C-FIELD-THREE-CELL-DELAYED-TRANSFER-N/verify.py': '42ec10cd001028ec126045647eea89347ec12bbf3612c40e1aa204ab77913a59',
    'notes/C-FIELD-THREE-CELL-DELAYED-TRANSFER-N/break.py': 'fc435a7efffea8edd4bd8e11aa12e16c2d1489a39c74997ae0b204837b7445b1',
    'notes/C-FIELD-FINITE-CHAIN-FIRST-DELIVERY-N/SCOPE.md': '89697d86015f3686875456e5bdbf4432b5dd21d2ac32d8ffc7b11b8766e19380',
    'notes/C-FIELD-FINITE-CHAIN-FIRST-DELIVERY-N/PROOF.md': '03913a77dfcc0e266668ebdd66594a287c3fa077ed1292596f91b775dc2d0df7',
}


def load_checked(name, relative, sources):
    module = ModuleType(name)
    path = ROOT / relative
    module.__file__ = str(path)
    exec(compile(sources[relative], str(path), "exec"), module.__dict__)
    return module


def main():
    if not __debug__:
        raise RuntimeError("the exact audit requires enabled assertions")
    sources = {}
    for relative, expected in SOURCE_SHA256.items():
        data = (ROOT / relative).read_bytes()
        if sha256(data).hexdigest() != expected:
            raise RuntimeError("public source hash mismatch: " + relative)
        sources[relative] = data

    # Fixed ASCII/LF output transport on each platform.
    sys.stdout.reconfigure(encoding="ascii", newline="\n")
    sentinel = object()
    previous = sys.modules.get("audit_challenger", sentinel)
    try:
        sys.modules["audit_challenger"] = load_checked(
            "audit_challenger", NOTE + "audit_challenger.py", sources)
        audit = load_checked("receiver_record_pinned_audit", NOTE + "audit.py", sources)
        audit.main()
    finally:
        if previous is sentinel:
            sys.modules.pop("audit_challenger", None)
        else:
            sys.modules["audit_challenger"] = previous


if __name__ == "__main__":
    main()
