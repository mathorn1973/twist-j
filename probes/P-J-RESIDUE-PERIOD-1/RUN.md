# P-J-RESIDUE-PERIOD-1 formal run record

Date: 2026-08-25

Status: local formal record. The public two-architecture gate will be complete
only after the repository pull-request workflow reruns the pinned verifier on
x86_64 and aarch64 under Python 3.12 and compares stdout byte for byte against
`EXPECTED.txt`.

The flat fields below are the machine-readable record required by
`tools/check_verifier.py`.

```text
pin_commit: 04512fc7b5efff94f13ac8f988f248abf16409bb
verifier_sha256: b59360415624a2c03826215c2937f27ef06fff5e6548a41b82594d3e32dfb6ec
command: python3 probes/P-J-RESIDUE-PERIOD-1/verify.py
platform: macOS 26.5
architecture: aarch64
python: CPython 3.9.6
exit_code: 0
stdout_sha256: 559d73794323e0abd2e7ef86cd241afbdc2099239664e7967c326a3ac6d81a8c
stdout_bytes: 723
stdout_lines: 13
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

The local `uname` reports `arm64`, the same instruction set recorded above as
`aarch64`.

## Pin audit

```text
parent_commit: 505f4096453a52bacb8c8de26583b38874ea408b
prereg_sha256: b786ecdf70e51bb6255d20b5af2c737641740a4097a95d911aaad51754eaae64
prereg_bytes: 12296
prereg_lines: 211
prereg_blob: 842e065cd4215b1210a992225ceef84a248e2969
verify_bytes: 8401
verify_lines: 277
verify_blob: d946fcbd581627319d968f7b4394446b187b9296
public_claim_lock: issue 567
public_pin_comment: 5416660039
```

`PREREG.md` and `verify.py` were committed together and pushed before the
formal execution, and the pin commit touches no other path. They were then
fetched from the public remote into a second clean checkout at the exact full
pin. In that checkout the head commit, the worktree cleanliness, the two paths,
and the SHA-256 of both pinned files were read back and matched the values
recorded at the pin and in the public pin comment.

Result exposure, disclosed in `PREREG.md` before the pin and repeated here: the
accepted verifier was smoke-executed twice before the pin, outside this
repository, once on x86_64 under CPython 3.11.15 and once on aarch64 under
CPython 3.9.6. Both runs produced the digest recorded below. The probe is
preregistered proof-first: the universal statements rest on the written proofs
in `PREREG.md`, every comparison in the verifier is exact integer equality, and
no declared threshold can move as a consequence of that exposure. No pinned
byte changed after publication.

## Formal execution

The accepted verifier was executed exactly once, from the repository root of
the clean public readback checkout.

```text
start_utc: 2026-08-25T20:55:54.1000150Z
end_utc: 2026-08-25T20:55:56.5237300Z
elapsed_ms: 2424
```

`elapsed_ms` is the monotonic process-wrapper stopwatch; the UTC values are the
independently sampled wall-clock envelope and need not differ by exactly that
integer after timestamp and scheduler rounding. The run is well inside the
120 second budget declared in `PREREG.md`.

The interpreter was started from an emptied environment carrying only:

```text
PATH=/usr/bin:/bin
LC_ALL=C
LANG=C
PYTHONDONTWRITEBYTECODE=1
PYTHONHASHSEED=0
TZ=UTC
```

Standard output and standard error were captured separately outside the
repository. `EXPECTED.txt` is the complete raw standard output, 723 bytes,
thirteen LF-terminated lines, with no CR and a final LF. Standard error was
empty. The verifier was not rerun and the pinned checkout remained clean.

The local interpreter is a compatibility witness. The required pull-request
jobs independently run the same pin under Python 3.12 on x86_64 and aarch64;
their byte identity against this one committed `EXPECTED.txt` is the public
two-architecture computation gate. Only those workflow jobs and their aggregate
`check` constitute the acceptance gate; the local Python 3.9 record does not.

No external data exist in this probe.

## Accepted run

```text
guards:     4/4 PASS
A, B:       999 rational moduli 2..1000, ord_zeta firings 0, period law firings 0
census:     6 moduli, orbit lcm against period, firings 0
C:          134 split primes below 4000, 536 prime ideals,
            ratio 1 in 438, ratio 5 in 98, any other ratio 0
witness:    p = 11 with zeta_5 -> 3: ord(phi) = 10, ord(J) = 2, lcm = 10, ratio 5
lattice:    sup norms of J^n . 1 for n = 1..12, no finite orbit
decision:   J-RESIDUE-PERIOD-CONFIRMED
scope:      L1 exact residue arithmetic only
digest:     a1142052bde0cfd86f20b4085690f317097dd89c08488b016a5adbc804fb166b
```

The universal statements (A), (B) and (C) rest on the written proofs in
`PREREG.md`. The finite carriers are an exact audit, not their quantifier.
