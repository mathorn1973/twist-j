"""Acquire an anonymous fresh batch and audit it after the blind commitment."""

import argparse
from hashlib import sha256
import json
from pathlib import Path

from physical import Physical, projected, roster


HERE = Path(__file__).resolve().parent
PANELS = ((961, 962, 963, 964), (1024, 1088, 1152, 1216))
PANEL_SIZE = 3210
SEED_SHA256 = "02209a9316a4533061b727261cee98885584aa0574a9e4a709dc1475aa3360fb"


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode("ascii")


def digest(data):
    return sha256(data).hexdigest()


def order(seed, size):
    """Map anonymous positions to zero-based positions in the canonical roster."""
    if len(seed) != 32:
        raise ValueError("expected a 32-byte binary seed")
    return sorted(range(size), key=lambda index: sha256(seed + index.to_bytes(4, "big")).digest())


def default_root():
    relative = Path("reproduce/h3-referenced-record/verify.py")
    for candidate in HERE.parents:
        if (candidate / relative).is_file():
            return candidate
    raise ValueError("H3 kernel checkout unavailable; pass --root")


def load_seed(path):
    seed = Path(path).read_bytes()
    if len(seed) != 32 or digest(seed) != SEED_SHA256:
        raise ValueError("binary seed does not match the frozen SHA-256 commitment")
    return seed


def packets(root):
    physics = Physical(root)
    records = []
    for gains in PANELS:
        cases = roster(gains)
        if len(cases) != PANEL_SIZE:
            raise ValueError("fresh panel size mismatch")
        records.extend(canonical(projected(physics.run(case)[0])).rstrip(b"\n") for case in cases)
    return records


def batch_bytes(records, permutation):
    return b"[" + b",".join(records[index] for index in permutation) + b"]\n"


def acquire(seed, root, anonymous):
    records = packets(root)
    data = batch_bytes(records, order(seed, len(records)))
    with anonymous.open("xb") as stream:
        stream.write(data)
    return {"anonymous_sha256": digest(data), "records": len(records)}


def audit(seed, root, anonymous, calls):
    from reader import load_reader

    records = packets(root)
    permutation = order(seed, len(records))
    data = anonymous.read_bytes()
    if data != batch_bytes(records, permutation):
        raise ValueError("anonymous batch differs from regenerated shuffled records")
    call_data = calls.read_bytes()
    observed = json.loads(call_data)
    if type(observed) is not list or len(observed) != len(records) or call_data != canonical(observed):
        raise ValueError("blind calls must be a canonical list matching the anonymous batch size")

    read = load_reader(root)
    cached = {}
    canonical_calls = [None] * len(records)
    for index, supplied in zip(permutation, observed, strict=True):
        record = records[index]
        if record not in cached:
            cached[record] = read(json.loads(record))
        expected = cached[record]
        if canonical(supplied) != canonical(expected):
            raise ValueError(f"public reader disagrees at canonical index {index}")
        canonical_calls[index] = expected
    return {"anonymous_sha256": digest(data), "anonymous_calls_sha256": digest(call_data),
            "canonical_calls_sha256": digest(canonical(canonical_calls)), "records": len(records)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, help="checkout containing the pinned H3 kernel")
    commands = parser.add_subparsers(dest="command", required=True)
    for name in ("acquire", "audit"):
        command = commands.add_parser(name)
        command.add_argument("seed", type=Path, help="file of 32 raw bytes")
        command.add_argument("anonymous", type=Path)
        if name == "audit":
            command.add_argument("calls", type=Path)
    args = parser.parse_args()
    seed = load_seed(args.seed)
    root = args.root if args.root is not None else default_root()
    if args.command == "acquire":
        result = acquire(seed, root, args.anonymous)
    else:
        result = audit(seed, root, args.anonymous, args.calls)
    print(canonical(result).decode("ascii"), end="")


if __name__ == "__main__":
    main()
