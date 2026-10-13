# Native-classical contact census formal run

```text
pin_commit: 498f658f2de0ecfcd71694cd2bc026f280f2fa3b
base_commit: 5f54015ed8361e3a64cb10894397020ddfadd104
public_issue: https://github.com/mathorn1973/twist-j/issues/1491
public_readback_comment: https://github.com/mathorn1973/twist-j/issues/1491#issuecomment-6157186517
public_readback_utc: 2026-10-13T23:13:21.218827+00:00
public_readback: PASS before formal execution
command: python3 probes/P-NATIVE-CLASSICAL-CONTACT-CENSUS-1/verify.py
executed_command: python3 -B probes/P-NATIVE-CLASSICAL-CONTACT-CENSUS-1/verify.py
platform: Ubuntu 22.04.5 LTS
architecture: x86_64
python: 3.10.12
start_utc: 2026-10-13T23:14:29.283983+00:00
finish_utc: 2026-10-13T23:14:46.463780+00:00
formal_execution_count: 1
exit_code: 0
stdout_sha256: 4e1cb9c563d5fe96bf1058b8c81e66fb955e1414bcc77e55a6c84af12aeb50b5
stdout_bytes: 107
stdout_lines: 1
stdout_line_endings: LF-only, final LF present
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
verifier_sha256: e629d525616b07b112d19cfe98553ea0bc93a9ce5c57f7241af4238231c32acb
verifier_bytes: 19975
verifier_blob: 4e52cad5fd5d648114fc2f78432e91327fc740ea
prereg_sha256: 40295a7a6897dc88a9e92b33601b242a7aaae1315bcc2e21fc56dc74549d1e8d
prereg_bytes: 10757
prereg_blob: b80c4c55ccf73079c5cf9a3659532a814272a250
all_pinned_sources_pre_post_match: yes
execution_checkout_clean_before_after: yes
```

The first formal run used a clean detached Linux checkout of the exact public
pin. The verifier ran from its repository root with LC_ALL=C, LANG=C, TZ=UTC,
PYTHONHASHSEED=0, PYTHONDONTWRITEBYTECODE=1 and PYTHONNOUSERSITE=1.
The command field uses the repository gate's required replay spelling;
executed_command records the actual initial invocation. Its additional -B
duplicates the recorded PYTHONDONTWRITEBYTECODE=1 setting.
EXPECTED.txt is the captured subprocess stdout, unchanged byte for byte.
The pinned verifier and preregistration were checked before and after execution.
Results were written outside the execution checkout after successful completion.

The earlier Windows preparation replays and guard-removal development check
were disclosed before this pin. They remain prior knowledge, not this formal
run, blind prediction or independent architecture evidence. GitHub architecture
replay is recorded separately when its required jobs finish.
