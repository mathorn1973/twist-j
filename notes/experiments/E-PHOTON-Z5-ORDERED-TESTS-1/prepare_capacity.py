"""Source preparation only. Never creates or samples a scientific state."""
from pathlib import Path
import hashlib

ROOT = Path(__file__).resolve().parent
PIN = "c089e7ec7ecc82f4838c27663d94c040f5cc4ea3"
HASHES = {
    "photon_z5.cpp": "68232b2f44bca6fd71514547e2f5aa0ad8aa85b9d298dde5d9a4109ac2151e14",
    "photon_z5_part1.inc": "263b631d6322526296cef5b32104f9bbc34184a8506f30fc15962687fcd6727a",
    "photon_z5_part2.inc": "7d1183e0f8368310be259fb88fac54aaba9e8661c64112e2577e9929e8ea379d",
    "photon_z5_part3.inc": "c6f5776e5c401618bd8478cf98bf99ad9020f50b0dc4495e53e2eea4a971686a",
    "photon_z5_part4.inc": "442f79534fc7849fa4801d46908c24abf2d22e0b31a5fdec2e4b068bfd66db4b",
}
REPLACE = {
    "photon_z5_part1.inc": (
        b'if (options.L < 2 || options.L > 16) throw std::runtime_error("L must be in [2,16]");',
        b'if (options.L < 2 || options.L > 64) throw std::runtime_error("L must be in [2,64]");',
    ),
    "photon_z5_part2.inc": (
        b"std::array<LineFace, 6 * 16> entries{};",
        b"std::array<LineFace, 6 * 64> entries{};",
    ),
}
OLD_COLLISION = b'''                for (std::size_t i = 0; i < affected.count; ++i) {
                    for (std::size_t j = i + 1; j < affected.count; ++j) {
                        if (affected.entries[i].id == affected.entries[j].id)
                            throw StopIntegrity("STOP_INTEGRITY duplicate_noncontractible_line_face");
                    }
                }'''
NEW_COLLISION = b'''                std::array<std::size_t, 6 * 64> sorted_ids{};
                for (std::size_t i = 0; i < affected.count; ++i)
                    sorted_ids[i] = affected.entries[i].id;
                const auto end = sorted_ids.begin() + affected.count;
                std::sort(sorted_ids.begin(), end);
                if (std::adjacent_find(sorted_ids.begin(), end) != end)
                    throw StopIntegrity("STOP_INTEGRITY duplicate_noncontractible_line_face");'''

def prepare():
    source = ROOT / "upstream"
    if {p.name for p in source.iterdir()} != set(HASHES):
        raise ValueError("upstream inventory mismatch")
    outputs = {}
    previous = {}
    for name, expected in HASHES.items():
        data = (source / name).read_bytes()
        if hashlib.sha256(data).hexdigest() != expected:
            raise ValueError("upstream source hash mismatch: " + name)
        if name in REPLACE:
            old, new = REPLACE[name]
            if data.count(old) != 1:
                raise ValueError("capacity source guard mismatch: " + name)
            data = data.replace(old, new)
        previous[name] = data
        if name == "photon_z5_part2.inc":
            if data.count(OLD_COLLISION) != 1:
                raise ValueError("collision-validation source guard mismatch")
            data = data.replace(OLD_COLLISION, NEW_COLLISION)
        outputs[name] = data
    target = ROOT / "kernel64"
    if target.exists():
        if {p.name for p in target.iterdir()} != set(outputs):
            raise ValueError("derived inventory mismatch")
        for name, data in outputs.items():
            existing = (target / name).read_bytes()
            if existing not in (data, previous[name]):
                raise ValueError("refusing altered derived file: " + name)
        for name, data in outputs.items():
            if (target / name).read_bytes() != data:
                (target / name).write_bytes(data)
    else:
        target.mkdir()
        for name, data in outputs.items():
            (target / name).write_bytes(data)
    return outputs

if __name__ == "__main__":
    for name, data in sorted(prepare().items()):
        print(name, len(data), hashlib.sha256(data).hexdigest())
