# Exact local formal execution

```text
pin_commit: 5d122f0cab1fb20b368302cee4b4989d13ff16d2
verifier_sha256: 5e57a4d9e9c1129fd68c453baf9679d25104b45664742608ccc8ba94b1c9d5fe
command: python3 probes/P-U-TWO-TRACE-PORT-CONTACTS-1/verify.py
platform: Windows 11
architecture: x86_64
python: 3.12.10
exit_code: 0
stdout_sha256: cc8109a7b389fc77db7f25366d143b198aaf7d3d1b1ff5c781713e3b57ad82fc
stdout_bytes: 2636
stdout_lines: 1
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

Started UTC: 2026-10-04T00:41:01.820418+00:00. Completed UTC: 2026-10-04T00:41:02.325146+00:00.

This is the first scientific execution of the public pin, after exact remote
commit/tree/ref readback. The wrapper ran the primary and separately frozen
independent programs. Both passed; stderr was empty. EXPECTED.txt is the
actual stdout, preserved verbatim. LOCAL-BEFORE.json binds every pre-run
input. LOCAL-RUN.json preserves the neutral receipt. Complete evidence
resides under evidence/primary and evidence/independent. Architecture
reproduction and analytical all-time proof remain separate evidence.
