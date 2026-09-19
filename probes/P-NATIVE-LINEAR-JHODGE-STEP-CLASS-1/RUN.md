# RUN: P-NATIVE-LINEAR-JHODGE-STEP-CLASS-1

pin_commit: d4bc4657795046a3b3fe60f0b021d64cfb58e0e7
verifier_sha256: 0b7fcf1c720f2b33174c4f15dd920e6c78a1802e2e37afc47153d8dc27e00cc3
command: python3 probes/P-NATIVE-LINEAR-JHODGE-STEP-CLASS-1/verify.py
platform: Debian GNU/Linux 13 (trixie)
architecture: x86_64
python: 3.13.5
exit_code: 0
stdout_sha256: a9bb303dbb77fc46d09d54ada0f0d82f68cc2214eb741f22a0ebf8cc82ab42b6
stdout_bytes: 537
stdout_lines: 15
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0

prereg_sha256: 01f85525e371b52a83658fd3b12733046a5e56cc667f67775d8575eae1c487c0
prereg_git_blob: 909ad24b8b72c79ff1a7c9d27161ce216170742a
verifier_git_blob: fc242344eb92bd61182902f7fb2cd46de5ae83a1

The pinned verifier was reconstructed byte-for-byte from the public readback;
its Git blob matched before execution. The clean local leg used
TERM=dumb, LC_ALL=C, LANG=C, PYTHONDONTWRITEBYTECODE=1,
PYTHONHASHSEED=0 and TZ=UTC.

An earlier container attempt did not supply evidence: the first materialization
failed before Python because the isolated runtime had no DNS; a later wrapper
execution produced the same scientific stdout but the surrounding pseudo-TTY
cleanup emitted a TERM diagnostic outside the verifier's redirected stderr.
No source, threshold or expected scientific result changed. The recorded leg
above is the clean replay of the unchanged pinned bytes.

This is one local x86_64 lane. Required clean GitHub x86_64/aarch64 replay and
aggregate check remain the public computation gate.
