# P-PHOTON-Z5-DUAL-WARD-ENGINE-QUALIFICATION-2

Deterministic zero-evidence qualification of the exact arbitrary-width dyadic
orbit sampler and fail-closed two-child supervisor reserved on issue #756.
It is the fresh, dependency-closed successor to the immutable unmerged
QUALIFICATION-1 public-replay failure recorded at
`https://github.com/mathorn1973/twist-j/issues/756#issuecomment-5499581652`.

The orbit fixture reproduces the old `shift >= 63` guard on the exact
high-level two-plane envelopes `(0,-72,-36)` at `L=6` and `(0,-128,-64)` at
`L=8`, then verifies a repository-owned standard-C++17 `ExactUInt` sampler.
It separately reproduces the old sum-overflow and 64-bit bounded-draw-width
guards.  Whenever the inherited `uint64_t` path is defined, including its
`bit_length(total-1)<=63` condition, selected indices and random-bit
consumption remain byte-identical.  The independent supervisor fixture
preserves bounded stderr custody and both return codes, cancels queued work,
kills running siblings and reaps every child.

Accepted execution is Linux/POSIX-only.  A reproducible local replay uses a
base system CPython and an empty environment:

```sh
env -i PATH=/usr/bin:/bin LC_ALL=C LANG=C TZ=UTC \
  PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 \
  python3 probes/P-PHOTON-Z5-DUAL-WARD-ENGINE-QUALIFICATION-2/verify.py
```

The structured `RUN.md` command field remains exactly
`python3 probes/P-PHOTON-Z5-DUAL-WARD-ENGINE-QUALIFICATION-2/verify.py`; its
environment is recorded separately.  A direct Windows or non-Linux run fails
closed because the outer process-group cleanup qualified here is POSIX.

It compiles and runs only synthetic fixtures, requires empty stderr and exact
LF stdout, verifies `SOURCE_SHA256SUMS`, and byte-compares the combined fixture
with `FIXTURE_EXPECTED.txt`.  The exact integer implementation uses no Boost,
third-party header, package-manager installation or host intrinsic.  Bare
`git` and `g++` run with `PATH=/usr/bin:/bin`; compiler, Git, loader and Python
ambient variables are scrubbed or rejected, and supervisor interpreters use
`-S -s -B`.  The already selected base Python/OS loader and system Git,
compiler and standard libraries are the explicit host trust boundary, not a
sandbox claim.  The verifier needs no network and opens no abandoned seed,
log, partial stream or Ward value.

The only successful terminal is

```text
WARD_ENGINE_QUALIFICATION_PASS
```

Every outcome has maximum status `ZERO_ENGINEERING_ONLY`.  A pass does not
satisfy issue #757/F3, does not authorize production issue #742, and does not
reserve CROSSCHECK-3.  Canon remains Public Canon v74 and no physical or
cosmological claim changes.
