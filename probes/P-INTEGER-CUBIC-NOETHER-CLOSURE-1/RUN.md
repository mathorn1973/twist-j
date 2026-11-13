# First local formal run

pin_commit: d978a878dd6044d7ba297d8402195a522e6fc8f8
command: python3 probes/P-INTEGER-CUBIC-NOETHER-CLOSURE-1/verify.py
verifier_sha256: 8d923cae191c3677c06c08aa18c1becc182c222e449002872425ff7991c4212f
platform: Linux 6.18.55
architecture: x86_64
python: 3.12.14
exit_code: 0
stdout_sha256: 004569700d67d2c1d1614c056be97ce00eee3df732c887d30f8316e51dc5e98c
stdout_bytes: 807
stdout_lines: 24
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0

started_utc: 2026-10-19T19:08:28.254567Z
completed_utc: 2026-10-19T19:08:58.071497Z
prereg_sha256: 601e11e228261c9ee2d4614039dcf44b31664d61586d43ddbdde6dc5bf5b17bb
proof_sha256: 8395143efd7d2b20d3c05a5ac729e5595396fd4a1efedf16bc49f5356d3d70e2
source_sha256: 4e3a3eb3cc7ccfc2b7140eeb56732a77fc1800a9c601f6ac8b844c8a920619f0
breaker_sha256: 9958cb1d47d6afd7bbad7869bf72416ae404d4311c2797ec26ff36318bc776ed
frozen_manifest_sha256: 2c01fdf7e239e339afdbe6aa2691cda92cac68d4edba8d6496c3ae2bb67fa9bd

## Prospective custody

This was the first scientific execution of either new implementation.
Before execution, all six prospective files were published and fetched
back individually from GitHub at the pin above. Each byte string matched
the local original. The local Git tree and public tree were both
2b77c6126c7d636bdff4fb02af91abd24b8e078a; all six Git blob comparisons
matched, and the owned checkout was clean at the pin.

The public prospective receipt was posted at 2026-10-19T19:08:10Z and
read back before the run began:
https://github.com/mathorn1973/twist-j/issues/1653#issuecomment-6275084858.

The parent is Public Canon v103 main
dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d. Before the pin, preparation
was analytical derivation, separately authored code, static cross-review,
AST parsing, text checks, and hashing. Neither scientific source was
imported or executed. No computed gradient or Noether payload digest
existed before the prospective pin.

## Exact process and bytes

The actual first command used Python 3.12.14 with -I. The environment was
LC_ALL=C, LANG=C, PYTHONDONTWRITEBYTECODE=1, PYTHONHASHSEED=0, TZ=UTC.
The primary launched breaker.py with the same Python executable and -I
in a separate process. It requires child exit zero, empty child stderr,
and raw byte identity of the complete 22-line shared certificate before
it can emit its terminal success lines.

The shared certificate has 767 bytes and 22 LF, with SHA-256
45e7a0c88fa195bc6471cb7c4b0121f75bfcd2f0ce223169eee18e01a3e1df8c.
The primary appended BREAKER_RAW_BYTES=IDENTICAL and RESULT=PASS to form
the observed 807-byte, 24-line stdout. The child was checked through this
primary subprocess contract; no separate standalone child run is claimed
as the first execution.

The stdout and stderr were captured as bytes before writing the result
records. EXPECTED.txt contains the unmodified first stdout and was checked
against the captured bytes. No stripping, newline normalization, manual
certificate editing, or replacement output was used. No preregistered
falsifier fired. No prospective file changed after the pin.

## Required architecture gate

This record describes the observed local run. The unchanged draft PR
workflow must replay this verifier and its isolated child under Python
3.12 on x86_64 and aarch64 against this same EXPECTED.txt. Actual run and
job receipts will be recorded in the PR and public completion comments
after observation. The local x86_64 result alone does not assert that the
two-architecture gate has passed.
