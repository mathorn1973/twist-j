#!/usr/bin/env python3
"""Production supervisor for P-PHOTON-AXIS-POS-PRIMAL-1.

Formal use, once, after the public pin and its readback:

    python3 run_axis.py formal --pin <full pin commit> --boost-deb <path> \
        --state-root <empty directory on a local disk> --attempt <n>

The supervisor refuses to start if any decision artifact exists, if a pinned
byte differs from SHA256SUMS, if HEAD is not the pin, if the probe directory
is dirty, or if the public branch head is not the pin.  It extracts the
frozen Boost headers, compiles the engine, reproduces the frozen pilot-2 and
AXIS fixtures, then runs the twenty chains concurrently.  Each chain is one
engine process.  At every candidate endpoint the four chains of one L stop;
the supervisor applies the automated #757 section 5 rule from axis_core and
answers MEASURE or CONTINUE on standard input.  No human decision enters.

Engine stdout plus the inserted RUNNER_COMMAND lines form the full transcript
of a chain; it stays with the link states under the state root.  The compact
records committed to the probe are its exact byte prefix up to MEASURE_BEGIN
and the exact reduction of its AXIS_S lines.  The supervisor then runs the
independent state reader, the analysis and verify.py, in that order.

An interrupted attempt is never resumed.  A later attempt reruns every chain
from macrocycle zero with the same pin, seeds and command; the sampler is a
pure function of its seeds, so every partial transcript of an earlier attempt
must be a byte prefix of the new one, which the supervisor checks.

``dev`` runs the same pipeline with the DEVELOPMENT configuration and its own
seed family, into a directory outside the repository.  It never touches the
formal seeds.
"""

from __future__ import annotations

import argparse
from collections import deque
import hashlib
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import threading
from typing import Sequence

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import axis_core as core  # noqa: E402

PINNED_FILES = (
    "PREREG.md",
    "AXIS_PIN.md",
    "README.md",
    "axis_engine.cpp",
    "axis_core.py",
    "axis_reader.py",
    "run_axis.py",
    "verify.py",
    "FIXTURE_EXPECTED.txt",
)
DECISION_ARTIFACTS = (
    "records", "CHAINS.tsv", "READER.txt", "STATE_MANIFEST.tsv", "ANALYSIS.txt",
    "EXPECTED.txt", "RUN.md", "RESULT.md",
)
BRANCH = "refs/heads/probe/P-PHOTON-AXIS-POS-PRIMAL-1"
BOOST_DEB_SHA256 = "1f11fc6fb2ffe9378a0f0ebc8f2fd9223fb958b4a40bb9381c67a8857d947ca3"
COMPILE_FLAGS = ("-std=c++20", "-O3", "-DNDEBUG", "-Wall", "-Wextra", "-Wpedantic")
FIXTURE_SIZES = (3, 4, 6)
MODELED_STOP_EXPECTED = (
    b"KERNEL_STATUS STOP_INTEGRITY\n"
    b"INTEGRITY_REASON value=STOP_INTEGRITY_modeled_cap_fixture\n"
    b"EVIDENTIAL_STATUS ZERO_PILOT_ONLY\n"
)
MIN_FREE_BYTES = 60 * 1024**3


class SupervisorError(RuntimeError):
    pass


def say(message: str) -> None:
    print(message, flush=True)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


# ---------------------------------------------------------------------------
# Preflight
# ---------------------------------------------------------------------------


def check_pin_manifest() -> None:
    raw = (HERE / "SHA256SUMS").read_bytes()
    if b"\r" in raw or not raw.endswith(b"\n"):
        raise SupervisorError("SHA256SUMS not LF with final LF")
    names = []
    for line in raw.decode("ascii").splitlines():
        digest, sep, name = line.partition("  ")
        if not sep or len(digest) != 64:
            raise SupervisorError("SHA256SUMS malformed")
        if sha256_bytes((HERE / name).read_bytes()) != digest:
            raise SupervisorError(f"pinned hash mismatch: {name}")
        names.append(name)
    if tuple(names) != PINNED_FILES:
        raise SupervisorError("SHA256SUMS inventory or order mismatch")
    present = {p.name for p in HERE.iterdir()}
    if present != set(PINNED_FILES) | {"SHA256SUMS"}:
        raise SupervisorError("probe directory inventory differs from the pin: "
                              + ",".join(sorted(present ^ (set(PINNED_FILES) | {"SHA256SUMS"}))))


def git(*args: str) -> str:
    done = subprocess.run(("git", *args), cwd=HERE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                          check=False)
    if done.returncode != 0:
        raise SupervisorError("git " + " ".join(args) + " failed")
    return done.stdout.decode("ascii").strip()


def check_git(pin: str) -> None:
    if git("rev-parse", "HEAD") != pin:
        raise SupervisorError("HEAD is not the pin commit")
    if git("status", "--porcelain", "--untracked-files=all", "--", ".") != "":
        raise SupervisorError("probe directory differs from the pin commit")
    remote = git("ls-remote", "origin", BRANCH).split()
    if not remote or remote[0] != pin:
        raise SupervisorError("public branch head is not the pin commit")


def build_engine(boost_deb: Path, workdir: Path) -> Path:
    if sha256_bytes(boost_deb.read_bytes()) != BOOST_DEB_SHA256:
        raise SupervisorError("Boost package hash mismatch")
    root = workdir / "boost"
    done = subprocess.run(("dpkg-deb", "-x", str(boost_deb), str(root)), stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE, check=False)
    if done.returncode != 0:
        raise SupervisorError("Boost extraction failed")
    binary = workdir / "axis_engine"
    command = ("g++", *COMPILE_FLAGS, "-isystem", str(root / "usr" / "include"),
               str(HERE / "axis_engine.cpp"), "-o", str(binary))
    built = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
    if built.returncode != 0 or built.stdout or built.stderr:
        sys.stderr.buffer.write(built.stderr)
        raise SupervisorError("engine compile failed or produced output")
    return binary


def run_capture(args: Sequence[str]) -> bytes:
    done = subprocess.run(tuple(args), stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
    if done.returncode != 0 or done.stderr:
        raise SupervisorError(f"fixture command failed: {' '.join(args[1:])}")
    return done.stdout


def check_fixtures(binary: Path) -> None:
    pilot = core.PILOT_DIR
    if run_capture((str(binary), "--self-test")) != (pilot / "SELFTEST_EXPECTED.txt").read_bytes():
        raise SupervisorError("pilot-2 self-test differs")
    if run_capture((str(binary), "--stop-integrity-fixture")) != MODELED_STOP_EXPECTED:
        raise SupervisorError("pilot-2 modeled stop differs")
    if run_capture((str(binary), "--fixture")) != (pilot / "REFERENCE_EXPECTED.txt").read_bytes():
        raise SupervisorError("pilot-2 reference fixture differs")
    axis = b"".join(run_capture((str(binary), "--axis-fixture", str(L))) for L in FIXTURE_SIZES)
    if axis != (HERE / "FIXTURE_EXPECTED.txt").read_bytes():
        raise SupervisorError("AXIS fixture differs from FIXTURE_EXPECTED.txt")


# ---------------------------------------------------------------------------
# Chains and the endpoint rule
# ---------------------------------------------------------------------------


class Group:
    """The four chains of one L meet at every candidate endpoint."""

    def __init__(self, L: int, cfg: core.Config, log_path: Path):
        self.L = L
        self.cfg = cfg
        self.log_path = log_path
        self.cond = threading.Condition()
        self.reports: dict[int, dict[tuple[str, int], tuple[list[str], str]]] = {}
        self.decisions: dict[int, str] = {}
        self.aborted = False

    def report(self, key: tuple[str, int], endpoint: int, window: list[str], progress: str) -> str:
        with self.cond:
            self.reports.setdefault(endpoint, {})[key] = (window, progress)
            if len(self.reports[endpoint]) == 4 and not self.aborted:
                self.decisions[endpoint] = self.decide(endpoint)
                self.cond.notify_all()
            while endpoint not in self.decisions and not self.aborted:
                self.cond.wait()
            return self.decisions.get(endpoint, "ABORT")

    def abort(self) -> None:
        with self.cond:
            self.aborted = True
            self.cond.notify_all()

    def decide(self, endpoint: int) -> str:
        out: list[str] = []
        try:
            windows, moves = {}, {}
            for key in core.CHAIN_KEYS:
                window, progress = self.reports[endpoint][key]
                if len(window) != self.cfg.window:
                    raise core.IntegrityError("short thermal window")
                rows = [core.validate_sample(line, self.L, endpoint - self.cfg.window + 1 + i)
                        for i, line in enumerate(window)]
                windows[key] = rows
                moves[key] = core.validate_progress(progress, "ENDPOINT", self.L, endpoint,
                                                    rows[-1]["state_hash"])
            accepted = core.thermal_decision(self.L, endpoint, windows, moves, self.cfg, out)
            decision = "MEASURE" if accepted else "CONTINUE"
        except (ValueError, KeyError, IndexError) as error:
            out.append(f"THERMAL_INTEGRITY L={self.L} endpoint={endpoint} {error}")
            decision = "ABORT"
        with open(self.log_path, "a", encoding="ascii") as handle:
            handle.write("\n".join(out) + "\n")
        say(f"ENDPOINT_DECISION L={self.L} endpoint={endpoint} command={decision}")
        return decision


class Chain:
    def __init__(self, binary: Path, cfg: core.Config, name: str, L: int, start: str, replica: int,
                 attempt_root: Path, group: Group):
        self.name, self.L, self.start, self.replica = name, L, start, replica
        self.key = (start, replica)
        self.cfg = cfg
        self.group = group
        self.seed = cfg.seed(L, start, replica)
        self.state_dir = attempt_root / "states" / name
        self.state_dir.mkdir(parents=True)
        self.transcript = attempt_root / "transcripts" / f"{name}.txt"
        self.args = (
            str(binary), "--axis", "--L", str(L), "--seed", f"0x{self.seed:016x}", "--start", start,
            "--chain", name, "--endpoints", ",".join(str(e) for e in cfg.endpoints),
            "--window", str(cfg.window), "--samples", str(cfg.samples),
            "--spacing", str(cfg.spacing_for(L)), "--state-dir", str(self.state_dir),
        )
        self.stderr = b""
        self.returncode: int | None = None
        self.accepted = 0

    def start_process(self) -> None:
        self.proc = subprocess.Popen(self.args, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                     stderr=subprocess.PIPE)
        self.err_thread = threading.Thread(target=self._drain_stderr, daemon=True)
        self.err_thread.start()
        self.thread = threading.Thread(target=self._pump, daemon=True)
        self.thread.start()

    def _drain_stderr(self) -> None:
        self.stderr = self.proc.stderr.read()

    def _pump(self) -> None:
        window: deque[str] = deque(maxlen=self.cfg.window)
        measuring = False
        finished_thermal = False
        with open(self.transcript, "wb") as out:
            for raw in self.proc.stdout:
                out.write(raw)
                if measuring:
                    continue
                line = raw.decode("ascii", "replace").rstrip("\n")
                if line.startswith("SAMPLE "):
                    window.append(line)
                elif line.startswith("ENDPOINT "):
                    out.flush()
                    endpoint = int(core.parse_fields(line, "ENDPOINT").get("completed", "0"))
                    command = self.group.report(self.key, endpoint, list(window), line)
                    window.clear()
                    if command == "ABORT":
                        self.proc.stdin.close()
                        continue
                    out.write(f"RUNNER_COMMAND endpoint={endpoint} command={command}\n".encode("ascii"))
                    out.flush()
                    if command == "MEASURE":
                        self.accepted = endpoint
                    self.proc.stdin.write((command + "\n").encode("ascii"))
                    self.proc.stdin.flush()
                elif line.startswith("MEASURE_BEGIN"):
                    measuring = True
                elif line.startswith("THERMAL_EXHAUSTED"):
                    finished_thermal = True
        self.returncode = self.proc.wait()
        self.err_thread.join()
        if not measuring and not finished_thermal:
            self.group.abort()

    def join(self) -> None:
        self.thread.join()


# ---------------------------------------------------------------------------
# Compaction of a full transcript into the committed records
# ---------------------------------------------------------------------------


def compact(cfg: core.Config, name: str, L: int, transcript: Path, records: Path) -> tuple[bytes, bytes]:
    data = transcript.read_bytes()
    lines = core.text_lines(data, name + " transcript")
    try:
        cut = next(i for i, line in enumerate(lines) if line.startswith("MEASURE_BEGIN "))
    except StopIteration:
        thermal = data
        (records / f"{name}.thermal.txt").write_bytes(thermal)
        return thermal, b""
    thermal = ("\n".join(lines[:cut + 1]) + "\n").encode("ascii")
    if not data.startswith(thermal):
        raise SupervisorError(f"{name} thermal prefix is not a byte prefix")
    accepted = int(lines[cut].split("=", 1)[1])
    width = L // 2 + 1
    rtot = {(I, r): [[0, 0] for _ in range(width)] for I in core.ORIENT for r in range(4)}
    out = [f"AXIS_MEASURE_RECORD chain={name} L={L} thermal_endpoint={accepted} "
           f"spacing={cfg.spacing_for(L)} transcript_sha256={sha256_bytes(data)} "
           f"transcript_bytes={len(data)}"]
    cursor = cut + 1
    for s in range(cfg.samples):
        out.append(lines[cursor])
        if not lines[cursor].startswith(f"SAMPLE index={s} "):
            raise SupervisorError(f"{name} transcript sample order")
        cursor += 1
        S = {}
        for I in core.ORIENT:
            for r in range(4):
                fields = core.parse_fields(lines[cursor], "AXIS_S")
                core.require_keys(fields, ("index", "I", "r", "S"), "AXIS_S")
                if (fields["index"], fields["I"], fields["r"]) != (str(s), I, str(r)):
                    raise SupervisorError(f"{name} AXIS_S order")
                S[(I, r)] = core.parse_pairs(fields["S"], L, "AXIS_S")
                cursor += 1
        R, Q = core.reduce_sample(S, L)
        for r in range(4):
            out.append(f"AXIS_Q index={s} r={r} Q={core.format_pairs(Q[r])}")
        for key, row in R.items():
            acc = rtot[key]
            for k, (u, v) in enumerate(row):
                acc[k][0] += u
                acc[k][1] += v
    for I in core.ORIENT:
        for r in range(4):
            out.append(f"AXIS_RTOT I={I} r={r} R={core.format_pairs(rtot[(I, r)])}")
    tail = lines[cursor:]
    if len(tail) != 3 or not tail[0].startswith("AXIS_DIAGNOSTICS "):
        raise SupervisorError(f"{name} transcript footer")
    out.extend(tail)
    measure = ("\n".join(out) + "\n").encode("ascii")
    (records / f"{name}.thermal.txt").write_bytes(thermal)
    (records / f"{name}.measure.txt").write_bytes(measure)
    return thermal, measure


def compact_failed(name: str, transcript: Path, records: Path, reason: str) -> tuple[bytes, bytes]:
    data = transcript.read_bytes()
    cut = data.find(b"\nMEASURE_BEGIN ")
    thermal = data if cut < 0 else data[:data.index(b"\n", cut + 1) + 1]
    measure = (f"AXIS_MEASURE_RECORD_FAILED chain={name} transcript_sha256={sha256_bytes(data)} "
               f"reason={reason.replace(' ', '_')}\n").encode("ascii", "replace")
    (records / f"{name}.thermal.txt").write_bytes(thermal)
    (records / f"{name}.measure.txt").write_bytes(measure)
    say(f"COMPACTION_FAILED {name} {reason}")
    return thermal, measure


def check_previous_attempts(state_root: Path, attempt: int, cfg: core.Config) -> list[str]:
    notes = []
    for previous in range(1, attempt):
        folder = state_root / f"attempt-{previous}" / "transcripts"
        if not folder.is_dir():
            notes.append(f"PREVIOUS_ATTEMPT attempt={previous} transcripts=ABSENT")
            continue
        for name, *_ in cfg.chains():
            old = folder / f"{name}.txt"
            new = state_root / f"attempt-{attempt}" / "transcripts" / f"{name}.txt"
            if not old.exists():
                continue
            old_bytes = old.read_bytes()
            if not new.read_bytes().startswith(old_bytes):
                raise SupervisorError(f"attempt {previous} transcript of {name} is not a prefix")
            notes.append(f"PREVIOUS_ATTEMPT attempt={previous} chain={name} prefix_bytes={len(old_bytes)} "
                         f"prefix_sha256={sha256_bytes(old_bytes)} prefix=PASS")
    return notes


# ---------------------------------------------------------------------------
# Pipeline
# ---------------------------------------------------------------------------


def run_pipeline(cfg: core.Config, binary: Path, state_root: Path, attempt: int, out_dir: Path,
                 formal: bool) -> None:
    attempt_root = state_root / f"attempt-{attempt}"
    attempt_root.mkdir(parents=True)
    (attempt_root / "transcripts").mkdir()
    groups = {L: Group(L, cfg, attempt_root / f"thermal_L{L}.txt") for L in cfg.sizes}
    chains = [Chain(binary, cfg, name, L, start, replica, attempt_root, groups[L])
              for name, L, start, replica in cfg.chains()]
    for chain in chains:
        chain.start_process()
    say(f"CHAINS_STARTED count={len(chains)}")
    for chain in chains:
        chain.join()
        say(f"CHAIN_DONE {chain.name} exit={chain.returncode} stderr_bytes={len(chain.stderr)}")

    records = out_dir / "records"
    records.mkdir()
    rows = ["\t".join(core.CHAINS_HEADER)]
    for chain in chains:
        try:
            thermal, measure = compact(cfg, chain.name, chain.L, chain.transcript, records)
        except (SupervisorError, ValueError, KeyError, IndexError) as error:
            # An engine STOP_INTEGRITY or a malformed transcript is recorded,
            # never repaired: the analysis turns it into STOP_INTEGRITY.
            thermal, measure = compact_failed(chain.name, chain.transcript, records, str(error))
        data = chain.transcript.read_bytes()
        rows.append("\t".join((
            chain.name, str(chain.L), chain.start, str(chain.replica), f"0x{chain.seed:016x}",
            str(cfg.spacing_for(chain.L)), str(chain.accepted), str(len(data)), sha256_bytes(data),
            sha256_bytes(thermal), sha256_bytes(measure) if measure else "-",
            str(chain.returncode), str(len(chain.stderr)),
        )))
        if chain.stderr:
            (attempt_root / f"{chain.name}.stderr.txt").write_bytes(chain.stderr)
    (out_dir / "CHAINS.tsv").write_bytes(("\n".join(rows) + "\n").encode("ascii"))
    for note in check_previous_attempts(state_root, attempt, cfg):
        say(note)

    reader = subprocess.run(
        (sys.executable, str(HERE / "axis_reader.py"), "--config", cfg.name, "--out", str(out_dir),
         "--attempt-root", str(attempt_root), "--workers", str(max(1, (os.cpu_count() or 2) // 2))),
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
    if reader.returncode != 0 or reader.stderr:
        sys.stderr.buffer.write(reader.stderr)
        raise SupervisorError("independent reader failed to run")
    say(reader.stdout.decode("ascii").strip().splitlines()[-1])

    lines, terminal = core.analyze(out_dir, cfg)
    (out_dir / "ANALYSIS.txt").write_bytes(("\n".join(lines) + "\n").encode("ascii"))
    say(f"ANALYSIS_WRITTEN terminal_hidden_until_verify")
    if formal:
        repo_root = HERE.parent.parent
        env = {"LC_ALL": "C", "LANG": "C", "PYTHONDONTWRITEBYTECODE": "1", "PYTHONHASHSEED": "0",
               "TZ": "UTC", "PATH": os.environ.get("PATH", "/usr/bin:/bin")}
        formal_run = subprocess.run(
            ("python3", (HERE / "verify.py").relative_to(repo_root).as_posix()),
            cwd=repo_root, env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
        if formal_run.returncode != 0 or formal_run.stderr:
            sys.stderr.buffer.write(formal_run.stderr)
            (out_dir / "EXPECTED.failed.txt").write_bytes(formal_run.stdout)
            raise SupervisorError("formal verifier failed")
        (out_dir / "EXPECTED.txt").write_bytes(formal_run.stdout)
    say(f"DRIVER_RESULT COMPLETE terminal={terminal}")


def main(argv: Sequence[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="mode", required=True)
    formal = sub.add_parser("formal")
    formal.add_argument("--pin", required=True)
    formal.add_argument("--boost-deb", required=True, type=Path)
    formal.add_argument("--state-root", required=True, type=Path)
    formal.add_argument("--attempt", required=True, type=int)
    dev = sub.add_parser("dev")
    dev.add_argument("--boost-deb", required=True, type=Path)
    dev.add_argument("--out", required=True, type=Path)
    args = parser.parse_args(argv)
    try:
        if args.mode == "formal":
            if args.attempt < 1:
                raise SupervisorError("attempt numbers start at 1")
            existing = [name for name in DECISION_ARTIFACTS if (HERE / name).exists()]
            if existing:
                raise SupervisorError("decision artifacts already exist: " + ",".join(existing))
            check_pin_manifest()
            check_git(args.pin)
            state_root = args.state_root.resolve()
            if (state_root / f"attempt-{args.attempt}").exists():
                raise SupervisorError("attempt directory already exists")
            state_root.mkdir(parents=True, exist_ok=True)
            if shutil.disk_usage(state_root).free < MIN_FREE_BYTES:
                raise SupervisorError("insufficient free space for link states")
            with tempfile.TemporaryDirectory(prefix="axis-pos-build-") as tmp:
                binary = build_engine(args.boost_deb, Path(tmp))
                check_fixtures(binary)
                say("PREFLIGHT PASS pin=" + args.pin)
                run_pipeline(core.FORMAL, binary, state_root, args.attempt, HERE, True)
        else:
            out = args.out.resolve()
            if out.exists():
                raise SupervisorError("dev output directory already exists")
            if HERE.parent.parent in out.parents:
                raise SupervisorError("dev output must lie outside the repository")
            out.mkdir(parents=True)
            with tempfile.TemporaryDirectory(prefix="axis-pos-dev-") as tmp:
                binary = build_engine(args.boost_deb, Path(tmp))
                check_fixtures(binary)
                say("DEV_PREFLIGHT PASS")
                run_pipeline(core.DEVELOPMENT, binary, out / "states", 1, out, False)
        return 0
    except (OSError, SupervisorError, subprocess.SubprocessError, UnicodeError, ValueError) as error:
        print(f"DRIVER_ERROR {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
