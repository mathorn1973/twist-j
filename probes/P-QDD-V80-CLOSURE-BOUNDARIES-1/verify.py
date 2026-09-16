#!/usr/bin/env python3
"""Exact proof-certificate audit; execute only after the public pin."""

from hashlib import sha256
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SOURCES = {
    "probes/P-QDD-U-NATIVE-READBACK-1/PROOF.md":
        "2df18b2118d0a2e483c8089976eda8485127951efa9e2f3364d38ac2aab0d76c",
    "probes/P-U-PREPARATION-EVENT-RECORD-1/NATIVE-PROOF.md":
        "45c93ea7a031ca0a5690ed7240d0648417d526659238cfffe52d5409925c0856",
    "probes/P-U-PREPARATION-EVENT-RECORD-1/INCIDENCE-PROOF.md":
        "5538718c55cabb07702a5d6d7daaecdcb4a8f5775f6863a5fc9ca39ba70910aa",
    "probes/P-QDD-COMMUTATOR-SATURATION-CLOSURE-1/PREREG.md":
        "f0d428cec1c6f0552e239be522a0f2a64decd20e538992c26f0efc18d4e25f96",
}
LOCAL = {
    'NATIVE-PROOF.md': '97c592f2b00ca2e03b8c0fc74abd658c4a804d6b6f20bc7722af881b9a76a295',
    'OCCURRENCE-PROOF.md': '4fa925dbe8de9841c787033567f07f00782be2affe002bdc92d75edbe878633c',
    'MIXED-PROOF.md': '93e08d44c30e670257779ce57c102d719d6449a0e861554c2f53d1efcf1e3a8d',
    'native_audit.py': '46a0120c11d55df3e7cac12cf1e2a891de15d0e0b601bb2ee15bab6d729f0bb3',
    'onset_audit.py': 'ce3196940e535af5e5534ed8b60f5bbc6e499fe1d3a410e670193fe591e5628d',
    'mixed_audit.py': '2d379748470c75c21a5a090fb63f53a368d60bd4e156a24a3a8f1d0ba40c767b',
}


def main():
    assert len(LOCAL) == 6, "incomplete prospective custody inventory"
    for name, digest in sorted(SOURCES.items()):
        assert sha256((ROOT / name).read_bytes()).hexdigest() == digest, name
    for name, digest in sorted(LOCAL.items()):
        assert sha256((HERE / name).read_bytes()).hexdigest() == digest, name

    from native_audit import audit as native_audit
    from onset_audit import audit as onset_audit
    from mixed_audit import audit as mixed_audit

    lines = ["P-QDD-V80-CLOSURE-BOUNDARIES-1", "PUBLIC_INPUT_CUSTODY PASS 4"]
    for audit in (native_audit, onset_audit, mixed_audit):
        result = audit()
        assert isinstance(result, tuple) and result
        assert all(isinstance(line, str) and "\n" not in line for line in result)
        lines.extend(result)
    lines.append("EXACT_AUDIT PASS; PHYSICAL_APPARATUS_AND_OCCURRENCE NOT_CLOSED")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
