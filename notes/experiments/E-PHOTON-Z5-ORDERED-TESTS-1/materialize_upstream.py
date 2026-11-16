"""Materialize the exact original sample-kernel sources from the declared Git pin."""
from pathlib import Path
import hashlib
import subprocess

from prepare_capacity import HASHES, PIN, prepare


def main():
    source = Path(__file__).resolve().parent / "upstream"
    prefix = "probes/P-PHOTON-Z5-EXACT-HEATBATH-MIXING-PILOT-2/"
    files = {}
    for name, expected in HASHES.items():
        data = subprocess.check_output(["git", "-C", str(source.parent), "cat-file", "blob",
                                        f"{PIN}:{prefix}{name}"])
        if hashlib.sha256(data).hexdigest() != expected:
            raise ValueError("Pinned content mismatch: " + name)
        files[name] = data
    source.mkdir(exist_ok=True)
    for name, data in files.items():
        target = source / name
        if target.exists():
            if target.read_bytes() != data:
                raise ValueError("Refusing divergent local source: " + name)
        else:
            with target.open("xb") as output:
                output.write(data)
    prepare()


if __name__ == "__main__":
    main()
