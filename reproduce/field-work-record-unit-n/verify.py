#!/usr/bin/env python3
"""Hash-checked public audit of the known event-record unit."""
from hashlib import sha256
from pathlib import Path
import sys
from types import ModuleType

ROOT = Path(__file__).resolve().parents[2]
NOTE = "notes/C-FIELD-WORK-RECORD-UNIT-N/"
SOURCE_SHA256 = {
    'notes/C-FIELD-WORK-RECORD-UNIT-N/PREREG.md': '3b50502c27330588bc71bd176f1217a68855dde78c559ff01d0e8d2574cd5731',
    'notes/C-FIELD-WORK-RECORD-UNIT-N/PROOF.md': '91675857b1b99862772858bef50dd6ba9e56c2f001bcc1ea42f25dd6f192c511',
    'notes/C-FIELD-WORK-RECORD-UNIT-N/primary.py': '11009d50a61a6e158aeffd9f1fde5bd867ccfb286b38029f985774d9155eb705',
    'notes/C-FIELD-WORK-RECORD-UNIT-N/challenger.py': '5067aa1f50b433d6c1ddd50c00f40151164982226b665e51728a211e184c072c',
    'notes/C-FIELD-WORK-RECORD-UNIT-N/audit.py': '2293c9354f3109351dc6ea652d68230b48714b69ce829a2ef27b3e727a1bc0b6',
    'notes/C-FIELD-THREE-CELL-DELAYED-TRANSFER-N/PROOF.md': 'd439f642b3447aec34efa3951ac70575182686b3168f44d89a53039ad90948b7',
    'notes/C-FIELD-THREE-CELL-DELAYED-TRANSFER-N/verify.py': '42ec10cd001028ec126045647eea89347ec12bbf3612c40e1aa204ab77913a59',
    'notes/C-FIELD-THREE-CELL-DELAYED-TRANSFER-N/break.py': 'fc435a7efffea8edd4bd8e11aa12e16c2d1489a39c74997ae0b204837b7445b1',
    'notes/C-FIELD-FINITE-CHAIN-FIRST-DELIVERY-N/PROOF.md': '03913a77dfcc0e266668ebdd66594a287c3fa077ed1292596f91b775dc2d0df7',
    'notes/C-FIELD-FINITE-CHAIN-FIRST-DELIVERY-N/SCOPE.md': '89697d86015f3686875456e5bdbf4432b5dd21d2ac32d8ffc7b11b8766e19380',
    'notes/C-FIELD-FINITE-CHAIN-FIRST-DELIVERY-N/audit_challenger.py': 'eaf429421c7e57c16dd1be97a469cbb63313b48597e44a4efd65a87f9087a267',
}


def main():
    if not __debug__:
        raise RuntimeError("exact audit requires enabled assertions")
    sources = {}
    for relative, digest in SOURCE_SHA256.items():
        data = (ROOT/relative).read_bytes()
        if sha256(data).hexdigest() != digest:
            raise RuntimeError("public source hash mismatch: "+relative)
        sources[relative] = data
    sys.stdout.reconfigure(encoding="ascii", newline="\n")
    missing = object()
    saved = {name: sys.modules.get(name, missing) for name in ("primary", "challenger")}
    try:
        for name in ("primary", "challenger", "audit"):
            relative = NOTE+name+".py"
            module = ModuleType("work_record_"+name)
            module.__file__ = str(ROOT/relative)
            exec(compile(sources[relative], module.__file__, "exec"), module.__dict__)
            if name != "audit":
                sys.modules[name] = module
            else:
                module.main()
    finally:
        for name, previous in saved.items():
            if previous is missing:
                sys.modules.pop(name, None)
            else:
                sys.modules[name] = previous


if __name__ == "__main__":
    main()
