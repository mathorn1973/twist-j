#!/usr/bin/env python3
"""Deterministic failure-capture qualification for a two-child pipeline.

This module is deliberately synthetic.  It exercises process supervision,
bounded diagnostic capture, fail-fast cancellation, and child reaping without
opening any scientific input or producing a scientific observable.
"""

from __future__ import annotations

from concurrent.futures import Future, wait
from dataclasses import dataclass
import hashlib
import os
from pathlib import Path
import queue
import subprocess
import sys
import threading
import time
from typing import BinaryIO, Callable, Sequence


STDERR_PREFIX_CAP = 4096
PIPE_CAP = 4096
SUPERVISOR_TIMEOUT = 10.0
CLEANUP_SECONDS = 4.0
BATCH_SHUTDOWN_SECONDS = 8.0
POLL_SECONDS = 0.01
CANONICAL_ENVIRONMENT = {
    "LC_ALL": "C",
    "LANG": "C",
    "TZ": "UTC",
    "PYTHONDONTWRITEBYTECODE": "1",
    "PYTHONHASHSEED": "0",
}


class QualificationFailure(RuntimeError):
    """The synthetic supervisor did not satisfy its fixed contract."""


@dataclass(frozen=True)
class SyntheticSpec:
    name: str
    engine_mode: str
    reader_mode: str


@dataclass(frozen=True)
class StreamCapture:
    total_bytes: int
    full_sha256: str
    prefix: bytes
    truncated: bool

    @property
    def prefix_bytes(self) -> int:
        return len(self.prefix)

    @property
    def prefix_hex(self) -> str:
        return self.prefix.hex()


@dataclass(frozen=True)
class PipelineCapture:
    spec: str
    engine_pid: int
    reader_pid: int
    engine_returncode: int
    reader_returncode: int
    engine_stderr: StreamCapture
    reader_stderr: StreamCapture
    pipe_bytes: int
    pipe_sha256: str
    engine_reaped: bool
    reader_reaped: bool
    cancelled: bool
    surviving_pids: tuple[int, ...]


@dataclass(frozen=True)
class BatchCapture:
    failing_spec: str
    trigger: PipelineCapture
    sibling: PipelineCapture
    sibling_was_running: bool
    queued_cancelled: int
    queued_total: int
    queued_child_starts: int
    all_futures_done: bool
    surviving_pids: tuple[int, ...]


class BoundedDaemonFuturePool:
    """Minimal Future pool whose workers cannot hold interpreter shutdown."""

    def __init__(self, max_workers: int) -> None:
        if max_workers <= 0:
            raise QualificationFailure("future_pool_worker_count")
        self._items: queue.Queue[object] = queue.Queue()
        self._sentinel = object()
        self._closed = False
        self._lock = threading.Lock()
        self._futures: list[Future[object]] = []
        self._threads = tuple(
            threading.Thread(
                target=self._worker,
                name=f"bounded-future-worker-{index}",
                daemon=True,
            )
            for index in range(max_workers)
        )
        for thread in self._threads:
            thread.start()

    def _worker(self) -> None:
        while True:
            item = self._items.get()
            try:
                if item is self._sentinel:
                    return
                future, function, arguments, keywords = item  # type: ignore[misc]
                if not future.set_running_or_notify_cancel():
                    continue
                try:
                    result = function(*arguments, **keywords)
                except BaseException as error:
                    future.set_exception(error)
                else:
                    future.set_result(result)
            finally:
                self._items.task_done()

    def submit(
        self,
        function: Callable[..., object],
        *arguments: object,
        **keywords: object,
    ) -> Future[object]:
        with self._lock:
            if self._closed:
                raise QualificationFailure("future_pool_closed")
            future: Future[object] = Future()
            self._futures.append(future)
            self._items.put((future, function, arguments, keywords))
            return future

    def shutdown(self, deadline: float) -> None:
        with self._lock:
            if self._closed:
                return
            self._closed = True
            futures = tuple(self._futures)
        for future in futures:
            future.cancel()
        for _thread in self._threads:
            self._items.put(self._sentinel)
        for thread in self._threads:
            remaining = max(0.0, deadline - time.monotonic())
            thread.join(remaining)
        if any(thread.is_alive() for thread in self._threads):
            raise QualificationFailure("future_pool_shutdown_timeout")


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _validated_loader_path(environment: dict[str, str]) -> str | None:
    raw = environment.get("LD_LIBRARY_PATH")
    if not raw:
        return None
    if len(raw.split(os.pathsep)) != 1:
        raise QualificationFailure("python_loader_path_components")
    candidate = Path(raw)
    expected = Path(sys.base_prefix) / "lib"
    if not candidate.is_absolute() or candidate.resolve() != expected.resolve():
        raise QualificationFailure("python_loader_path_outside_runtime")
    return raw


def _require_runtime() -> None:
    for name, expected in CANONICAL_ENVIRONMENT.items():
        if os.environ.get(name) != expected:
            raise QualificationFailure(f"canonical_environment:{name}")
    canonical_python = {"PYTHONDONTWRITEBYTECODE", "PYTHONHASHSEED"}
    for name in os.environ:
        upper = name.upper()
        if upper.startswith("PYTHON") and upper not in canonical_python:
            raise QualificationFailure(f"python_ambient:{name}")
        if (
            (upper.startswith("LD_") and upper != "LD_LIBRARY_PATH")
            or upper.startswith("DYLD_")
        ):
            raise QualificationFailure(f"loader_ambient:{name}")
    _validated_loader_path(os.environ)
    expected_flags = {
        "optimize": 0,
        "dont_write_bytecode": 1,
        "no_user_site": 1,
        "no_site": 1,
        "ignore_environment": 0,
        "hash_randomization": 0,
        "isolated": 0,
        "safe_path": False,
        "warn_default_encoding": 0,
    }
    for name, expected in expected_flags.items():
        if hasattr(sys.flags, name) and getattr(sys.flags, name) != expected:
            raise QualificationFailure(f"python_flag:{name}")
    if sys.warnoptions or sys._xoptions:
        raise QualificationFailure("python_runtime_options")


def _child_environment() -> dict[str, str]:
    environment = os.environ.copy()
    for name in tuple(environment):
        upper = name.upper()
        if upper.startswith("PYTHON"):
            environment.pop(name)
            continue
        if (
            (upper.startswith("LD_") and upper != "LD_LIBRARY_PATH")
            or upper.startswith("DYLD_")
        ):
            environment.pop(name)
    loader = _validated_loader_path(os.environ)
    if loader is None:
        environment.pop("LD_LIBRARY_PATH", None)
    else:
        environment["LD_LIBRARY_PATH"] = loader
    environment.update(CANONICAL_ENVIRONMENT)
    return environment


def _child_command(role: str, mode: str) -> tuple[str, ...]:
    return (
        sys.executable,
        "-S",
        "-s",
        "-B",
        str(Path(__file__).resolve()),
        "--child",
        role,
        mode,
    )


def _spawn(command: Sequence[str], *, stdin: int | BinaryIO) -> subprocess.Popen[bytes]:
    try:
        return subprocess.Popen(
            tuple(command),
            stdin=stdin,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            env=_child_environment(),
        )
    except OSError as error:
        raise QualificationFailure(f"child_start:{Path(command[0]).name}") from error


def _kill(process: subprocess.Popen[bytes]) -> None:
    if process.poll() is not None:
        return
    try:
        process.kill()
    except (OSError, ProcessLookupError):
        pass


def _wait_reaped(process: subprocess.Popen[bytes], deadline: float) -> int:
    observed = process.poll()
    if observed is not None:
        return observed
    _kill(process)
    remaining = deadline - time.monotonic()
    if remaining <= 0:
        raise QualificationFailure("child_reap_deadline")
    try:
        return process.wait(timeout=remaining)
    except subprocess.TimeoutExpired as error:
        raise QualificationFailure("child_reap_timeout") from error


def _collect_stream(
    stream: BinaryIO,
    prefix_cap: int,
    target: dict[str, StreamCapture],
    key: str,
    failures: list[str],
    lock: threading.Lock,
) -> None:
    digest = hashlib.sha256()
    prefix = bytearray()
    total = 0
    try:
        while True:
            chunk = stream.read(4096)
            if not chunk:
                break
            total += len(chunk)
            digest.update(chunk)
            if len(prefix) < prefix_cap:
                prefix.extend(chunk[: prefix_cap - len(prefix)])
        target[key] = StreamCapture(
            total_bytes=total,
            full_sha256=digest.hexdigest(),
            prefix=bytes(prefix),
            truncated=total > prefix_cap,
        )
    except OSError as error:
        with lock:
            failures.append(f"collect:{key}:{error.__class__.__name__}")


def supervise_pipeline(
    spec: SyntheticSpec,
    *,
    cancel_event: threading.Event | None = None,
    running_event: threading.Event | None = None,
    timeout: float = SUPERVISOR_TIMEOUT,
) -> PipelineCapture:
    """Run one synthetic engine/reader pair and retain both failure legs.

    The stderr digests and byte counts cover the complete streams while only
    ``STDERR_PREFIX_CAP`` bytes per stream remain resident in the returned
    record.  A cancellation or timeout kills both direct children and waits
    for both, so this function never returns with an unreaped child.
    """

    if timeout <= 0:
        raise QualificationFailure("invalid_supervisor_bound")
    if cancel_event is None:
        cancel_event = threading.Event()

    engine: subprocess.Popen[bytes] | None = None
    reader: subprocess.Popen[bytes] | None = None
    threads: tuple[threading.Thread, ...] = ()
    started_threads: list[threading.Thread] = []
    cleanup_failures: list[str] = []
    try:
        engine = _spawn(
            _child_command("engine", spec.engine_mode),
            stdin=subprocess.DEVNULL,
        )
        if engine.stdout is None or engine.stderr is None:
            raise QualificationFailure("engine_capture_pipe_missing")
        reader = _spawn(
            _child_command("reader", spec.reader_mode),
            stdin=subprocess.PIPE,
        )
        if reader.stdin is None or reader.stdout is None or reader.stderr is None:
            raise QualificationFailure("reader_capture_pipe_missing")

        captures: dict[str, StreamCapture] = {}
        pipe_capture: dict[str, int | str] = {}
        failures: list[str] = []
        lock = threading.Lock()

        def pump() -> None:
            total = 0
            digest = hashlib.sha256()
            try:
                while True:
                    chunk = engine.stdout.read(4096)
                    if not chunk:
                        break
                    total += len(chunk)
                    if total > PIPE_CAP:
                        raise QualificationFailure(
                            f"engine_pipe_cap:{spec.name}"
                        )
                    digest.update(chunk)
                    reader.stdin.write(chunk)
                reader.stdin.flush()
            except (BrokenPipeError, OSError, QualificationFailure) as error:
                if not cancel_event.is_set():
                    with lock:
                        failures.append(f"pump:{error}")
                    _kill(engine)
                    _kill(reader)
            finally:
                try:
                    reader.stdin.close()
                except OSError:
                    pass
                pipe_capture["bytes"] = total
                pipe_capture["sha256"] = digest.hexdigest()

        threads = (
            threading.Thread(
                target=pump,
                name=f"pump-{spec.name}",
                daemon=True,
            ),
            threading.Thread(
                target=_collect_stream,
                args=(
                    engine.stderr,
                    STDERR_PREFIX_CAP,
                    captures,
                    "engine",
                    failures,
                    lock,
                ),
                name=f"stderr-engine-{spec.name}",
                daemon=True,
            ),
            threading.Thread(
                target=_collect_stream,
                args=(
                    reader.stderr,
                    STDERR_PREFIX_CAP,
                    captures,
                    "reader",
                    failures,
                    lock,
                ),
                name=f"stderr-reader-{spec.name}",
                daemon=True,
            ),
        )
        for thread in threads:
            thread.start()
            started_threads.append(thread)
        if running_event is not None:
            running_event.set()

        deadline = time.monotonic() + timeout
        cancelled = False
        timed_out = False
        while engine.poll() is None or reader.poll() is None:
            if cancel_event.is_set() or time.monotonic() >= deadline:
                cancelled = cancel_event.is_set()
                timed_out = not cancelled
                _kill(engine)
                _kill(reader)
                break
            time.sleep(POLL_SECONDS)

        reap_deadline = time.monotonic() + CLEANUP_SECONDS
        engine_rc = _wait_reaped(engine, reap_deadline)
        reader_rc = _wait_reaped(reader, reap_deadline)
        for thread in started_threads:
            remaining = max(0.0, reap_deadline - time.monotonic())
            thread.join(remaining)
        if any(thread.is_alive() for thread in started_threads):
            raise QualificationFailure(f"pipeline_thread_reap:{spec.name}")
        if timed_out:
            raise QualificationFailure(f"pipeline_timeout:{spec.name}")
        if failures:
            raise QualificationFailure(
                f"pipeline_stream:{spec.name}:{','.join(failures)}"
            )
        if set(captures) != {"engine", "reader"}:
            raise QualificationFailure(f"stderr_incomplete:{spec.name}")
        if set(pipe_capture) != {"bytes", "sha256"}:
            raise QualificationFailure(f"pipe_capture_incomplete:{spec.name}")

        # The reader's fixed report is independently cross-checked against the
        # streaming count and digest made by the supervisor pump.
        reader_stdout = reader.stdout.read(PIPE_CAP + 1)
        if len(reader_stdout) > PIPE_CAP:
            raise QualificationFailure(f"reader_stdout_cap:{spec.name}")
        try:
            fields = reader_stdout.decode("ascii").strip().split(" ")
            if len(fields) == 3 and fields[0] == "PIPE":
                reader_pipe_bytes = int(fields[1])
                reader_pipe_sha256 = fields[2]
                if (
                    reader_pipe_bytes != pipe_capture["bytes"]
                    or reader_pipe_sha256 != pipe_capture["sha256"]
                ):
                    raise ValueError("pipe_custody")
            elif not cancelled:
                raise ValueError("shape")
        except (UnicodeDecodeError, ValueError) as error:
            raise QualificationFailure(
                f"reader_stdout_shape:{spec.name}"
            ) from error

        surviving_pids = tuple(
            process.pid
            for process in (engine, reader)
            if process.poll() is None
        )
        return PipelineCapture(
            spec=spec.name,
            engine_pid=engine.pid,
            reader_pid=reader.pid,
            engine_returncode=engine_rc,
            reader_returncode=reader_rc,
            engine_stderr=captures["engine"],
            reader_stderr=captures["reader"],
            pipe_bytes=int(pipe_capture["bytes"]),
            pipe_sha256=str(pipe_capture["sha256"]),
            engine_reaped=engine.poll() is not None,
            reader_reaped=reader.poll() is not None,
            cancelled=cancelled,
            surviving_pids=surviving_pids,
        )
    finally:
        # This is the single exit for every post-spawn path, including reader
        # spawn failure, thread-start failure, parsing failure and cancellation.
        cleanup_deadline = time.monotonic() + CLEANUP_SECONDS
        for process in (engine, reader):
            if process is not None:
                _kill(process)
        for label, process in (("engine", engine), ("reader", reader)):
            if process is not None:
                try:
                    _wait_reaped(process, cleanup_deadline)
                except QualificationFailure as error:
                    cleanup_failures.append(f"{label}:{error}")
        for thread in started_threads:
            remaining = max(0.0, cleanup_deadline - time.monotonic())
            thread.join(remaining)
        if any(thread.is_alive() for thread in started_threads):
            cleanup_failures.append("threads_alive")
        else:
            streams = (
                None if engine is None else engine.stdin,
                None if engine is None else engine.stdout,
                None if engine is None else engine.stderr,
                None if reader is None else reader.stdin,
                None if reader is None else reader.stdout,
                None if reader is None else reader.stderr,
            )
            for stream in streams:
                if stream is not None:
                    try:
                        stream.close()
                    except OSError as error:
                        cleanup_failures.append(
                            f"stream_close:{error.__class__.__name__}"
                        )
        if cleanup_failures:
            raise QualificationFailure(
                f"pipeline_cleanup:{spec.name}:{','.join(cleanup_failures)}"
            )


def _exception_cleanup_qualification() -> None:
    """Inject both one-child and two-child failures and require full reap."""

    global _spawn
    original_spawn = _spawn

    reader_spawned: list[subprocess.Popen[bytes]] = []
    spawn_calls = 0

    def fail_reader_spawn(
        command: Sequence[str],
        *,
        stdin: int | BinaryIO,
    ) -> subprocess.Popen[bytes]:
        nonlocal spawn_calls
        spawn_calls += 1
        if spawn_calls == 2:
            raise QualificationFailure("injected_reader_spawn")
        process = original_spawn(command, stdin=stdin)
        reader_spawned.append(process)
        return process

    _spawn = fail_reader_spawn
    reader_error = ""
    try:
        supervise_pipeline(SyntheticSpec("reader_spawn_fault", "block", "block"))
    except QualificationFailure as error:
        reader_error = str(error)
    finally:
        _spawn = original_spawn
    reader_survivors = tuple(
        process for process in reader_spawned if process.poll() is None
    )
    for process in reader_survivors:
        _kill(process)
        _wait_reaped(process, time.monotonic() + CLEANUP_SECONDS)
    if reader_error != "injected_reader_spawn":
        raise QualificationFailure("reader_spawn_fault_not_preserved")
    if len(reader_spawned) != 1 or reader_survivors:
        raise QualificationFailure("reader_spawn_fault_not_reaped")

    both_spawned: list[subprocess.Popen[bytes]] = []

    def record_spawn(
        command: Sequence[str],
        *,
        stdin: int | BinaryIO,
    ) -> subprocess.Popen[bytes]:
        process = original_spawn(command, stdin=stdin)
        both_spawned.append(process)
        return process

    original_thread_start = threading.Thread.start
    start_calls = 0

    def fail_thread_start(thread: threading.Thread) -> None:
        nonlocal start_calls
        start_calls += 1
        if start_calls == 2:
            raise QualificationFailure("injected_thread_start")
        original_thread_start(thread)

    _spawn = record_spawn
    threading.Thread.start = fail_thread_start
    thread_error = ""
    try:
        supervise_pipeline(SyntheticSpec("thread_start_fault", "block", "block"))
    except QualificationFailure as error:
        thread_error = str(error)
    finally:
        threading.Thread.start = original_thread_start
        _spawn = original_spawn
    thread_survivors = tuple(
        process for process in both_spawned if process.poll() is None
    )
    for process in thread_survivors:
        _kill(process)
        _wait_reaped(process, time.monotonic() + CLEANUP_SECONDS)
    if thread_error != "injected_thread_start":
        raise QualificationFailure("thread_start_fault_not_preserved")
    if len(both_spawned) != 2 or thread_survivors:
        raise QualificationFailure("thread_start_fault_not_reaped")


def supervise_batch() -> BatchCapture:
    """Exercise one fail-fast batch with running and queued siblings.

    Two worker threads are occupied before four additional jobs are queued.
    The first worker owns a live blocking engine/reader pair.  The second owns
    the trigger pair, whose two nonzero returns become the batch failure.  On
    that failure the coordinator sets one shared cancellation event, cancels
    every Future still queued, releases any wrapper already dequeued without
    allowing it to spawn children, and waits for every Future and child.
    """

    shared_cancel = threading.Event()
    sibling_running = threading.Event()
    trigger_wrapper_running = threading.Event()
    trigger_release = threading.Event()
    coordinator_decision = threading.Event()
    queued_child_starts = 0
    queued_lock = threading.Lock()
    queued_total = 4
    pool = BoundedDaemonFuturePool(max_workers=2)
    all_futures: list[Future[object]] = []
    queued_futures: list[Future[object]] = []

    def trigger_job() -> PipelineCapture:
        trigger_wrapper_running.set()
        if not trigger_release.wait(timeout=2.0):
            raise QualificationFailure("batch_trigger_release_timeout")
        return supervise_pipeline(SyntheticSpec("dual_rc", "fail7", "fail11"))

    def queued_job(index: int) -> PipelineCapture | None:
        nonlocal queued_child_starts
        if not coordinator_decision.wait(timeout=5.0):
            raise QualificationFailure(f"batch_queue_decision_timeout:{index}")
        if shared_cancel.is_set():
            return None
        with queued_lock:
            queued_child_starts += 1
        return supervise_pipeline(
            SyntheticSpec(f"queued_{index}", "block", "block"),
            cancel_event=shared_cancel,
        )

    sibling_future: Future[object] | None = None
    trigger_future: Future[object] | None = None
    try:
        sibling_future = pool.submit(
            supervise_pipeline,
            SyntheticSpec("running_sibling", "block", "block"),
            cancel_event=shared_cancel,
            running_event=sibling_running,
        )
        all_futures.append(sibling_future)
        if not sibling_running.wait(timeout=2.0):
            raise QualificationFailure("batch_sibling_not_running")

        trigger_future = pool.submit(trigger_job)
        all_futures.append(trigger_future)
        if not trigger_wrapper_running.wait(timeout=2.0):
            raise QualificationFailure("batch_trigger_not_running")

        # Both workers are now occupied, so these are genuine queued Futures.
        for index in range(queued_total):
            future = pool.submit(queued_job, index)
            queued_futures.append(future)
            all_futures.append(future)
        trigger_release.set()

        trigger_result = trigger_future.result(timeout=SUPERVISOR_TIMEOUT)
        if not isinstance(trigger_result, PipelineCapture):
            raise QualificationFailure("batch_trigger_capture_missing")
        if (
            trigger_result.engine_returncode == 0
            and trigger_result.reader_returncode == 0
        ):
            raise QualificationFailure("batch_trigger_did_not_fail")

        # The failure decision precedes both queue release and sibling kill.
        shared_cancel.set()
        queued_cancelled = sum(future.cancel() for future in queued_futures)
        coordinator_decision.set()

        completed, incomplete = wait(all_futures, timeout=SUPERVISOR_TIMEOUT)
        if incomplete:
            raise QualificationFailure("batch_future_wait_timeout")
        if completed != set(all_futures):
            raise QualificationFailure("batch_future_set_mismatch")

        sibling_result = sibling_future.result(timeout=0)
        if not isinstance(sibling_result, PipelineCapture):
            raise QualificationFailure("batch_sibling_capture_missing")
        for future in queued_futures:
            if not future.cancelled():
                queued_result = future.result(timeout=0)
                if queued_result is not None:
                    raise QualificationFailure("batch_queued_child_created")

        surviving_pids = tuple(
            sorted(trigger_result.surviving_pids + sibling_result.surviving_pids)
        )
        return BatchCapture(
            failing_spec=trigger_result.spec,
            trigger=trigger_result,
            sibling=sibling_result,
            sibling_was_running=sibling_running.is_set(),
            queued_cancelled=queued_cancelled,
            queued_total=queued_total,
            queued_child_starts=queued_child_starts,
            all_futures_done=all(future.done() for future in all_futures),
            surviving_pids=surviving_pids,
        )
    finally:
        # This path is also bounded and fail-closed if a condition above
        # fires: no worker gate or child pair is left behind.
        shared_cancel.set()
        trigger_release.set()
        coordinator_decision.set()
        for future in queued_futures:
            future.cancel()
        cleanup_failures: list[str] = []
        if all_futures:
            _completed, incomplete = wait(
                all_futures,
                timeout=BATCH_SHUTDOWN_SECONDS,
            )
            if incomplete:
                cleanup_failures.append("futures_alive")
        try:
            pool.shutdown(
                deadline=time.monotonic() + BATCH_SHUTDOWN_SECONDS
            )
        except QualificationFailure as error:
            cleanup_failures.append(str(error))
        if cleanup_failures:
            raise QualificationFailure(
                "batch_cleanup:" + ",".join(cleanup_failures)
            )


def _require(condition: bool, label: str) -> None:
    if not condition:
        raise QualificationFailure(label)


def qualification_lines() -> tuple[str, ...]:
    engine_payload = b"E" * STDERR_PREFIX_CAP + b"engine-tail\n"
    reader_payload = b"R" * STDERR_PREFIX_CAP + b"reader-tail\n"
    pipe_payload = b"synthetic-pipe-payload\n"
    batch = supervise_batch()
    _exception_cleanup_qualification()
    capture = batch.trigger
    _require(capture.spec == "dual_rc", "failing_spec_lost")
    _require(capture.engine_returncode == 7, "engine_returncode_lost")
    _require(capture.reader_returncode == 11, "reader_returncode_lost")
    _require(capture.engine_stderr.total_bytes == len(engine_payload), "engine_stderr_bytes")
    _require(
        capture.engine_stderr.full_sha256 == _sha256(engine_payload),
        "engine_stderr_sha",
    )
    _require(
        capture.engine_stderr.prefix == engine_payload[:STDERR_PREFIX_CAP],
        "engine_stderr_prefix",
    )
    _require(
        capture.engine_stderr.prefix_bytes == STDERR_PREFIX_CAP,
        "engine_stderr_prefix_bytes",
    )
    _require(capture.engine_stderr.truncated, "engine_stderr_truncation")
    _require(capture.reader_stderr.total_bytes == len(reader_payload), "reader_stderr_bytes")
    _require(
        capture.reader_stderr.full_sha256 == _sha256(reader_payload),
        "reader_stderr_sha",
    )
    _require(
        capture.reader_stderr.prefix == reader_payload[:STDERR_PREFIX_CAP],
        "reader_stderr_prefix",
    )
    _require(
        capture.reader_stderr.prefix_bytes == STDERR_PREFIX_CAP,
        "reader_stderr_prefix_bytes",
    )
    _require(capture.reader_stderr.truncated, "reader_stderr_truncation")
    _require(capture.pipe_bytes == len(pipe_payload), "pipe_bytes")
    _require(capture.pipe_sha256 == _sha256(pipe_payload), "pipe_sha")
    _require(capture.engine_reaped and capture.reader_reaped, "failed_pair_not_reaped")
    _require(not capture.surviving_pids, "failed_pair_surviving_pids")

    _require(batch.failing_spec == "dual_rc", "batch_failing_spec_lost")
    _require(batch.sibling_was_running, "batch_sibling_never_running")
    _require(batch.sibling.spec == "running_sibling", "batch_sibling_spec_lost")
    _require(batch.sibling.cancelled, "batch_sibling_not_cancelled")
    _require(
        batch.sibling.engine_reaped and batch.sibling.reader_reaped,
        "batch_sibling_not_reaped",
    )
    _require(batch.queued_cancelled >= 2, "batch_queued_cancel_count")
    _require(batch.queued_child_starts == 0, "batch_queued_child_started")
    _require(batch.all_futures_done, "batch_futures_not_done")
    _require(not batch.surviving_pids, "batch_surviving_pids")

    return (
        "SUPERVISOR_BATCH PASS",
        f"FAILING_SPEC {batch.failing_spec}",
        f"ENGINE_RC {capture.engine_returncode}",
        f"READER_RC {capture.reader_returncode}",
        (
            "ENGINE_STDERR "
            f"stderr_total_bytes={capture.engine_stderr.total_bytes} "
            f"stderr_full_sha256={capture.engine_stderr.full_sha256} "
            f"stderr_prefix_bytes={capture.engine_stderr.prefix_bytes} "
            f"stderr_prefix_hex={capture.engine_stderr.prefix_hex} "
            f"stderr_truncated={str(capture.engine_stderr.truncated).lower()}"
        ),
        (
            "READER_STDERR "
            f"stderr_total_bytes={capture.reader_stderr.total_bytes} "
            f"stderr_full_sha256={capture.reader_stderr.full_sha256} "
            f"stderr_prefix_bytes={capture.reader_stderr.prefix_bytes} "
            f"stderr_prefix_hex={capture.reader_stderr.prefix_hex} "
            f"stderr_truncated={str(capture.reader_stderr.truncated).lower()}"
        ),
        f"PIPE_CAPTURE bytes={capture.pipe_bytes} sha256={capture.pipe_sha256}",
        f"SIBLING_WAS_RUNNING {str(batch.sibling_was_running).lower()}",
        f"SIBLING_CANCELLED {str(batch.sibling.cancelled).lower()}",
        f"SIBLING_ENGINE_REAPED {str(batch.sibling.engine_reaped).lower()}",
        f"SIBLING_READER_REAPED {str(batch.sibling.reader_reaped).lower()}",
        (
            "QUEUED_FUTURES_CANCELLED_AT_LEAST_TWO "
            f"{str(batch.queued_cancelled >= 2).lower()}"
        ),
        f"QUEUED_CHILDREN_NEVER_STARTED {str(batch.queued_child_starts == 0).lower()}",
        f"ALL_FUTURES_DONE {str(batch.all_futures_done).lower()}",
        f"SURVIVING_PIDS {len(batch.surviving_pids)}",
        "SUPERVISOR_QUALIFICATION PASS",
    )


def _reader_child(mode: str) -> int:
    if mode == "block":
        while True:
            time.sleep(60.0)
    payload = sys.stdin.buffer.read()
    digest = _sha256(payload)
    sys.stdout.buffer.write(f"PIPE {len(payload)} {digest}\n".encode("ascii"))
    sys.stdout.buffer.flush()
    if mode == "fail11":
        sys.stderr.buffer.write(b"R" * STDERR_PREFIX_CAP + b"reader-tail\n")
        sys.stderr.buffer.flush()
        return 11
    raise QualificationFailure("unknown_reader_mode")


def _engine_child(mode: str) -> int:
    if mode == "block":
        while True:
            time.sleep(60.0)
    if mode == "fail7":
        sys.stdout.buffer.write(b"synthetic-pipe-payload\n")
        sys.stdout.buffer.flush()
        sys.stderr.buffer.write(b"E" * STDERR_PREFIX_CAP + b"engine-tail\n")
        sys.stderr.buffer.flush()
        return 7
    raise QualificationFailure("unknown_engine_mode")


def _main(arguments: Sequence[str]) -> int:
    _require_runtime()
    if list(arguments) == ["--fixture"]:
        sys.stdout.buffer.write(
            ("\n".join(qualification_lines()) + "\n").encode("ascii")
        )
        sys.stdout.buffer.flush()
        return 0
    if len(arguments) == 3 and arguments[0] == "--child":
        role, mode = arguments[1:]
        if role == "engine":
            return _engine_child(mode)
        if role == "reader":
            return _reader_child(mode)
    raise QualificationFailure("usage")


if __name__ == "__main__":
    try:
        raise SystemExit(_main(sys.argv[1:]))
    except (OSError, QualificationFailure, subprocess.SubprocessError) as error:
        print(f"SUPERVISOR_QUALIFICATION_ERROR {error}", file=sys.stderr)
        raise SystemExit(2)
