#!/usr/bin/env python3
"""Replay the exposed audit from hash-checked public sources; no new discovery."""

from hashlib import sha256
from pathlib import Path
import sys
from types import ModuleType


ROOT = Path(__file__).resolve().parents[2]
NOTE = "notes/C-FIELD-FINITE-CHAIN-FIRST-DELIVERY-N/"
OLD = "notes/C-FIELD-THREE-CELL-DELAYED-TRANSFER-N/"
SOURCE_SHA256 = {
    NOTE + "PREREG.md": "ca6a02fbd8d5942a2d7fb5e5e9017f8c94f1a1131a6524aea5f3e73a53d6cbcd",
    NOTE + "SCOPE.md": "89697d86015f3686875456e5bdbf4432b5dd21d2ac32d8ffc7b11b8766e19380",
    NOTE + "PROOF.md": "03913a77dfcc0e266668ebdd66594a287c3fa077ed1292596f91b775dc2d0df7",
    NOTE + "RESULT.md": "5450aaa06c07031b3151612adaa318e273cbdd9980ce609c7f40b711534c86eb",
    NOTE + "SHA256SUMS": "b79adf65680866b1cf333efd54e0806b62298081618e959a36519299183edda1",
    NOTE + "audit.py": "283a51e9e94ee70d5fd36106d64dec43e481ad6efde7594402d072b23e90f9a6",
    NOTE + "audit_challenger.py": "eaf429421c7e57c16dd1be97a469cbb63313b48597e44a4efd65a87f9087a267",
    OLD + "PREREG.md": "9b9f0c6ceab706474ac74ed0229df30fafced164ad128400770315a18796aa7d",
    OLD + "PROOF.md": "d439f642b3447aec34efa3951ac70575182686b3168f44d89a53039ad90948b7",
    OLD + "verify.py": "42ec10cd001028ec126045647eea89347ec12bbf3612c40e1aa204ab77913a59",
    OLD + "break.py": "fc435a7efffea8edd4bd8e11aa12e16c2d1489a39c74997ae0b204837b7445b1",
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

    # Normalize only stdout transport. Preserve the original scientific lines.
    sys.stdout.reconfigure(encoding="ascii", newline="\n")
    sentinel = object()
    previous = sys.modules.get("audit_challenger", sentinel)
    try:
        sys.modules["audit_challenger"] = load_checked(
            "audit_challenger", NOTE + "audit_challenger.py", sources)
        audit = load_checked("finite_chain_pinned_audit", NOTE + "audit.py", sources)
        audit.main()
    finally:
        if previous is sentinel:
            sys.modules.pop("audit_challenger", None)
        else:
            sys.modules["audit_challenger"] = previous


if __name__ == "__main__":
    main()
