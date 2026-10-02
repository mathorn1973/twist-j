# Frozen-program reproduction

NON-CANONICAL.

Status: PASS.

Evidence: SUPPLEMENTARY_SAME_ARCHITECTURE.

Platform: Ubuntu 22.04.5 LTS.
Architecture: x86_64.
Python: CPython 3.10.12.
Basis: `738e0421bd15aaea5bb6ef2a56f1cab752d44de5`.

Environment: `LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC`.

| Program | Status | Exit | Stdout bytes | Stdout SHA-256 | Stderr bytes |
| --- | --- | --- | --- | --- | --- |
| base | PASS | 0 | 4476 | `3b2bdc432e1bfebcd453b83a6766a2863b6a1d54243180cbc20e0b1ce4ea39ad` | 0 |
| addendum1 | PASS | 0 | 2436 | `fc5432d288f340038d64edb5ceab9aeec71c3b400cc378c8556878089b549bed` | 0 |
| base_breaker | PASS | 0 | 2660 | `f1044cc3c1371342ca3bfc5b921460332fa7c07a17999874e556dc1891cf6f0f` | 0 |
| addendum1_breaker | PASS | 0 | 1403 | `6e3aa7f8eac8d2df31f6c60f4e2b5cfa78c11a4092501b4a5defa1a12a733bd6` | 0 |

Raw stdout and stderr are retained without newline conversion.
A differing byte, nonzero exit or any stderr stops the run.
No candidate status or occurrence disposition is promoted by this record.

Custody annotation, status RECORDED: this run record originally completed at
`2026-10-02T17:32:24Z`, as reported by its filesystem modification timestamp
before this annotation. Owner session: `CODEX-W1-ARCH-20261002`.

Runner SHA-256:
`33a38114852e6a70c173867959a103ca21e1e2f809c978ba92d41b37fded166c`.

Exact invocation expressed with portable path placeholders:

```sh
python3 W1/run_frozen.py \
  --package C-NATIVE-FIBRE-PENTIT-WIGNER-N_handoff_2026-10-02 \
  --repo /path/to/twist-j \
  --output W1/supplementary-x86_64 \
  --architecture x86_64 \
  --attest-native
```

The interpreter was local Ubuntu WSL `python3`. Paths at execution were
absolute. No shell pipeline or newline normalization was used.
