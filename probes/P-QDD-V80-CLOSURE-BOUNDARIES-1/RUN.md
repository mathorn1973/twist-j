# Run record: P-QDD-V80-CLOSURE-BOUNDARIES-1

```text
pin_commit: 9a0b42fe75b91181b8806ac618f7c54ff5b4cb85
verifier_sha256: e7bfb9c7e1c0042884bed692eb8cd2d8f5715d3eadc6d621298a2294a5f86919
command: python3 probes/P-QDD-V80-CLOSURE-BOUNDARIES-1/verify.py
platform: Ubuntu 24.04.3 LTS
architecture: x86_64
python: CPython 3.12.3
exit_code: 0
stdout_sha256: 29f7b55cca982ac4203c199fe6322d7e5a14915ecb26df0c6e25b8924adc6862
stdout_bytes: 1313
stdout_lines: 22
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
environment: LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1
```

## Public custody and prospective review

Public issue: #871. Started UTC: 2026-09-06T16:55:28.022855+00:00.
The complete pin was pushed to GitHub and its public head read back before
this execution. A fresh clone from that GitHub branch checked out exactly
the pin. Native Linux Git confirmed a clean worktree before and after the
scientific command. The pin has one parent, the verified public v79 main.
All eight pinned files matched their fetched Git blobs before execution and
remained byte-identical afterward. The wrapper used a 600-second ceiling
and captured stdout and stderr separately as bytes. Only after exit zero,
empty stderr and unchanged custody checks was actual stdout saved verbatim
as EXPECTED.txt. No earlier output or private run was substituted.

| Pinned file | Bytes | SHA-256 |
| --- | ---: | --- |
| MIXED-PROOF.md | 10118 | 93e08d44c30e670257779ce57c102d719d6449a0e861554c2f53d1efcf1e3a8d |
| NATIVE-PROOF.md | 8833 | 97c592f2b00ca2e03b8c0fc74abd658c4a804d6b6f20bc7722af881b9a76a295 |
| OCCURRENCE-PROOF.md | 16885 | 4fa925dbe8de9841c787033567f07f00782be2affe002bdc92d75edbe878633c |
| PREREG.md | 11188 | 61b1fb07bb7508d84ba4b8211ef64b1a9b7875272dbe87d75a45f75143dacea8 |
| mixed_audit.py | 7978 | 2d379748470c75c21a5a090fb63f53a368d60bd4e156a24a3a8f1d0ba40c767b |
| native_audit.py | 7176 | 46a0120c11d55df3e7cac12cf1e2a891de15d0e0b601bb2ee15bab6d729f0bb3 |
| onset_audit.py | 10900 | ce3196940e535af5e5534ed8b60f5bbc6e499fe1d3a410e670193fe591e5628d |
| verify.py | 2289 | e7bfb9c7e1c0042884bed692eb8cd2d8f5715d3eadc6d621298a2294a5f86919 |

Separate same-session reviewers checked the mathematical proofs and exact
code statically before the pin. A review precision about equal projectors
at consecutive phases was resolved before pinning. None imported or ran
the accepted modules before the pin. Syntax parsing alone was performed.
The universal claims are carried by proofs; the finite audit is not a
physical experiment or a proof of physical apparatus completeness.

This local x86_64 result is one architecture. The required GitHub x86_64
and aarch64 jobs must replay this unchanged bundle against this one exact
EXPECTED.txt. Their results are independently visible on the pull request.
