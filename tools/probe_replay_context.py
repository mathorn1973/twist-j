"""Replay explicitly registered context-bound probes against their frozen inputs.

The reviewed manifest is data, not a command or an override supplied by RUN.md.
Only the listed Markdown inputs are admitted. The current verifier, prereg,
run record and expected stdout remain subject to the ordinary replay checks.
Historical input bytes are obtained from one immutable ancestor commit, never
from a replacement copy of current Canon. This is reproduction of historical
evidence, not certification of a new Canon by the old authority check.
"""

from __future__ import annotations

from collections.abc import Iterator
from contextlib import contextmanager
import hashlib
import json
from pathlib import Path
import re
import subprocess
import tempfile


MANIFEST = "tools/probe_replay_contexts.json"
REPLAY_CONTROL_PATHS = frozenset({
    MANIFEST, "tools/probe_replay_context.py", "tools/check_verifier.py",
})
CONTEXT_PATHS = frozenset({
    "canon/CANON.md", "STATUS.md",
    "notes/canon/C-FRW-INHOM-TYPED-ADM-PREDEFINITION-N.md",
})
MAX_BYTES = 5 * 1024 * 1024


class ReplayContextError(RuntimeError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise ReplayContextError(message)


def exact_keys(value: object, keys: set[str], label: str) -> None:
    require(isinstance(value, dict) and set(value) == keys,
            f"{label} has invalid fields")


def digest(value: object, length: int) -> bool:
    return isinstance(value, str) and re.fullmatch(f"[0-9a-f]{{{length}}}", value) is not None


def validate_blob(spec: object, label: str) -> None:
    exact_keys(spec, {"git_blob", "sha256", "bytes"}, label)
    require(digest(spec["git_blob"], 40) and digest(spec["sha256"], 64),
            f"{label} has invalid hashes")
    require(type(spec["bytes"]) is int and 0 <= spec["bytes"] <= MAX_BYTES,
            f"{label} has invalid byte count")


def unique_object(pairs: list[tuple[str, object]]) -> dict:
    result = {}
    for key, value in pairs:
        require(key not in result, f"replay manifest repeats {key}")
        result[key] = value
    return result


def registrations(root: Path) -> dict:
    try:
        data = json.loads(current_regular(root, MANIFEST).decode("utf-8"),
                          object_pairs_hook=unique_object)
    except (OSError, ValueError) as error:
        raise ReplayContextError(f"cannot read replay manifest: {error}") from error
    exact_keys(data, {"schema", "probes"}, "replay manifest")
    require(type(data["schema"]) is int and data["schema"] == 1,
            "unsupported replay manifest schema")
    require(isinstance(data["probes"], dict), "replay probes must be an object")
    for name, entry in data["probes"].items():
        require(re.fullmatch(r"P-[A-Z0-9]+(?:-[A-Z0-9]+)*", name) is not None,
                "replay manifest has an invalid probe name")
        exact_keys(entry, {"pin_commit", "verifier", "prereg", "context_files"}, name)
        require(digest(entry["pin_commit"], 40), f"{name} has invalid pin")
        validate_blob(entry["verifier"], f"{name} verifier")
        validate_blob(entry["prereg"], f"{name} prereg")
        files = entry["context_files"]
        require(isinstance(files, dict) and set(files) == CONTEXT_PATHS,
                f"{name} must list exactly the permitted context paths")
        for path, spec in files.items():
            validate_blob(spec, f"{name} {path}")
    return data["probes"]


def git_bytes(root: Path, *args: str) -> bytes:
    result = subprocess.run(["git", *args], cwd=root, capture_output=True, timeout=30)
    require(result.returncode == 0, f"historical replay git {args[0]} failed")
    return result.stdout


def verify_bytes(data: bytes, spec: dict, label: str) -> None:
    require(len(data) == spec["bytes"], f"{label} byte count differs")
    require(hashlib.sha256(data).hexdigest() == spec["sha256"],
            f"{label} SHA-256 differs")
    git_header = b"blob " + str(len(data)).encode("ascii") + b"\0"
    require(hashlib.sha1(git_header + data).hexdigest() == spec["git_blob"],
            f"{label} Git blob differs")


def pinned_blob(root: Path, pin: str, path: str, spec: dict) -> bytes:
    # The manifest permits only exact fixed paths; no pathspec or filesystem
    # traversal is accepted. Reject links and submodules before reading bytes.
    tree = git_bytes(root, "ls-tree", "-z", pin, "--", path)
    expected = f"100644 blob {spec['git_blob']}\t{path}\0".encode("ascii")
    require(tree == expected, f"{path} is not the registered regular Git blob")
    size = git_bytes(root, "cat-file", "-s", spec["git_blob"])
    require(size.strip() == str(spec["bytes"]).encode("ascii"),
            f"{path} Git byte count differs")
    data = git_bytes(root, "cat-file", "blob", spec["git_blob"])
    verify_bytes(data, spec, path)
    return data


def current_regular(root: Path, relative: str) -> bytes:
    path = root / relative
    require(path.resolve() == root.resolve() / relative and path.is_file(),
            f"{relative} must be a regular current file without symlink traversal")
    return path.read_bytes()


@contextmanager
def execution_root(root: Path, name: str, pin: str, verifier_bytes: bytes) -> Iterator[Path]:
    """Yield current root normally, or a completely validated frozen context."""
    entry = registrations(root).get(name)
    if entry is None:
        yield root
        return
    require(pin == entry["pin_commit"], f"{name} RUN pin differs from replay registration")
    require(git_bytes(root, "cat-file", "-t", pin).strip() == b"commit",
            f"{name} replay pin is not a commit")
    git_bytes(root, "merge-base", "--is-ancestor", pin, "HEAD")

    verifier_path = f"probes/{name}/verify.py"
    prereg_path = f"probes/{name}/PREREG.md"
    frozen_verifier = pinned_blob(root, pin, verifier_path, entry["verifier"])
    require(current_regular(root, verifier_path) == verifier_bytes == frozen_verifier,
            f"{name} current verifier differs from registered pin")
    frozen_prereg = pinned_blob(root, pin, prereg_path, entry["prereg"])
    require(current_regular(root, prereg_path) == frozen_prereg,
            f"{name} current prereg differs from registered pin")
    payload = {verifier_path: frozen_verifier}
    for path, spec in entry["context_files"].items():
        payload[path] = pinned_blob(root, pin, path, spec)

    # Only regular files are materialized. There are no shell commands or
    # executable path fields; ambient directories and modules are not copied.
    with tempfile.TemporaryDirectory(prefix="twistj-probe-replay-") as directory:
        isolated = Path(directory)
        for relative, data in payload.items():
            target = isolated / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
        print(f"VERIFY HISTORICAL CONTEXT {name} {pin} {len(entry['context_files'])} inputs")
        yield isolated
