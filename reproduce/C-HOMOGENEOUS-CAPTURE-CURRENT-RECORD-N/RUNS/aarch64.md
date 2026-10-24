# Exact source reproduction record (non-canonical)

candidate_commit: 44a2d76e9888d42a5eec5082752e4439b9f0f354
run_base_commit: 44a2d76e9888d42a5eec5082752e4439b9f0f354
reproduction: C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N
verifier_sha256: d1f82078039f09e69010048d31a4f49cbfdbc6cfa9ac126d30beb8e2df2691b6
expected_sha256: 46a5221d8fea9d0c8855c5d18d2823381053c7f1e64d538452bb3afa48d09441
command: python3 reproduce/C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N/verify.py
platform: Debian 12
architecture: aarch64
python: 3.11.2
exit_code: 0
stdout_sha256: 46a5221d8fea9d0c8855c5d18d2823381053c7f1e64d538452bb3afa48d09441
stdout_bytes: 708
stdout_lines: 8
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
result: PASS

The exact source commit was checked out detached in a clean isolated checkout.
HEAD and tracked source bytes remained unchanged; the checkout was clean after
the run. The standard deterministic environment was LC_ALL=C, LANG=C,
PYTHONDONTWRITEBYTECODE=1, PYTHONHASHSEED=0 and TZ=UTC.

Started UTC: 2026-10-23T23:35:05.528319+00:00
Finished UTC: 2026-10-23T23:35:07.297140+00:00
