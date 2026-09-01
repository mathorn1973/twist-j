# P-PHOTON-Z5-DUAL-WARD-CROSSCHECK-1

Formal zero-evidence `L=6,8` Ward/covariance execution for issue #756 and
production-firewall clause F3.

The package pairs a deterministic replay of already public primal pilot-2
chains with four independently seeded closed-surface dual chains at each L.
It can emit no phase label.  Its public terminals are

```text
DUAL_CROSSCHECK_PASS
STOP_DUAL_MIXING
STOP_DUAL_INTEGRITY
BREAK_DUAL_DICTIONARY
```

Before the public immutable pin, development is restricted to compilation and
the frozen `L<=4` fixture:

```sh
export LC_ALL=C LANG=C TZ=UTC PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0
python3 dual_chain.py dev --L 2 --seed 0x7560201 \
  --thermal 8 --samples 2 --between 2 --start surface
```

No `decision` command with `L=6` or `L=8`, no analyzer on decision logs and no
`run_crosscheck.py` invocation is allowed before the pin is pushed and every
pinned byte is publicly read back.

After that readback, the one and only formal local command is

```sh
export LC_ALL=C LANG=C TZ=UTC PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0
python3 run_crosscheck.py
```

The driver compiles the inherited exact primal kernel, checks the small
fixture, validates the public input hashes, runs the frozen primal replays and
dual chains, writes custody records, analyzes them, and invokes `verify.py`
exactly once.  Its captured verifier stdout becomes `EXPECTED.txt`; stderr
must be empty and the terminal must be complete.

CI later runs only the deterministic verifier over the committed record.  It
does not regenerate the expensive chains.

Only a merged, publicly read-back `DUAL_CROSSCHECK_PASS` satisfies F3.  The
production experiment #742 remains forbidden while this package is in flight.
