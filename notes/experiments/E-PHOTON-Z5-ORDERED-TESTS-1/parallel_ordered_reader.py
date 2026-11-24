"""Run independent portions of the exact ordered reader in a shared spawn pool."""

from concurrent.futures import ProcessPoolExecutor
import multiprocessing
import os


MATH_ENV = {
    "OPENBLAS_NUM_THREADS": "1",
    "MKL_NUM_THREADS": "1",
    "NUMEXPR_NUM_THREADS": "1",
    "BLIS_NUM_THREADS": "1",
    "VECLIB_MAXIMUM_THREADS": "1",
}


def _init_worker(affinity):
    if affinity is not None:
        os.sched_setaffinity(0, affinity)
    os.environ.update(MATH_ENV)
    os.environ.update(OMP_NUM_THREADS="1", OMP_THREAD_LIMIT="1")


def _measure_orientation(data, sha256, requested_m, requested_R, secondary, orientation):
    from ordered_reader import measure_bytes

    return measure_bytes(data, sha256, requested_m, requested_R, secondary=secondary,
                         orientations=(orientation,))


class ParallelReader:
    """One reusable service for all chain threads, entered before they start."""

    def __init__(self, worker_count):
        if type(worker_count) is not int or not 1 <= worker_count <= 24:
            raise ValueError("reader worker count must be an integer from 1 to 24")
        self.worker_count = worker_count
        self._pool = None
        self._original_env = None

    def __enter__(self):
        if self._pool is not None:
            raise RuntimeError("reader service is already active")
        # Spawn imports the main module before the initializer, so pass the
        # library caps in the inherited environment as well.
        self._original_env = {name: os.environ.get(name) for name in MATH_ENV}
        os.environ.update(MATH_ENV)
        try:
            affinity = tuple(sorted(os.sched_getaffinity(0))) if hasattr(os, "sched_getaffinity") else None
            self._pool = ProcessPoolExecutor(max_workers=self.worker_count,
                                              mp_context=multiprocessing.get_context("spawn"),
                                              initializer=_init_worker, initargs=(affinity,))
        except BaseException:
            self._restore_environment()
            raise
        return self

    def _restore_environment(self):
        for name, value in self._original_env.items():
            if value is None:
                os.environ.pop(name, None)
            else:
                os.environ[name] = value
        self._original_env = None

    def __exit__(self, exc_type, exc, traceback):
        try:
            self._pool.shutdown(wait=True, cancel_futures=exc_type is not None)
        finally:
            self._pool = None
            self._restore_environment()

    def measure_bytes(self, data, sha256, requested_m=(), requested_R=(), *, secondary=False):
        from ordered_reader import ORIENTATIONS, PRIMARY, IntegrityError, measure_bytes

        pool = self._pool
        if pool is None:
            raise RuntimeError("reader service is inactive")
        requested_m = tuple(requested_m)
        requested_R = tuple(requested_R)
        orientations = [
            orientation for orientation in ORIENTATIONS
            if ((requested_m and orientation in ((0, 1), (0, 2)))
                or (requested_R and (secondary or orientation in PRIMARY)))
        ]
        if not orientations:
            return measure_bytes(data, sha256, requested_m, requested_R, secondary=secondary)

        futures = []
        try:
            for orientation in orientations:
                futures.append(pool.submit(_measure_orientation, data, sha256, requested_m,
                                           requested_R, secondary, orientation))
            metadata = None
            observables = {}
            for future in futures:
                partial = future.result()
                values = partial.pop("observables")
                if metadata is None:
                    metadata = partial
                if metadata != partial or observables.keys() & values.keys():
                    raise IntegrityError("inconsistent parallel orientation result")
                observables.update(values)
        except BaseException:
            for future in futures:
                future.cancel()
            raise
        return {**metadata, "observables": observables}
