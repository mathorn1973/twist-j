# Terminal record: C-RH-RAY-FINITE-WINDOW-CERTIFICATE-2-N

Status: `ABANDONED`.

NON-CANONICAL. This is a v63 accounting record, not a scientific result.

```text
identifier       C-RH-RAY-FINITE-WINDOW-CERTIFICATE-2-N
issue lock       #468
source branch    notes/c-rh-ray-finite-window-certificate-2-n
branch head      22affa65c129275d1e6411f21ba2d78c9002df1a
prereg path      notes/C-RH-RAY-FINITE-WINDOW-CERTIFICATE-2-N/PREREG.md
prereg blob      eb6375d2de08eda6152579e8aa49b9bf951a8b2a
prereg sha256    fa08c3ee1b6559fc4038c35a225948b746a0a7adea2ebe3f3aee4588d86ded62
formal gate      executed, never completed
scientific result none
recorded         2026-08-24, Public Canon v62
```

## Why the gate never completed

The pinned wrapper failed during import before the audit engine ran because
the dynamically loaded module had not been inserted into `sys.modules`. The
wrapper was not repaired. A run that dies before the engine produces no exact
scientific stdout to pin, no completed run record and no scientific result.

This history is recorded by the fresh successor on branch
`notes/c-rh-ray-finite-window-certificate-3-n`, path
`notes/C-RH-RAY-FINITE-WINDOW-CERTIFICATE-3-N/RESULT.md`, section 5, at
commit `ce3c7b5cb41f79d0686a600f40534ec411764f6f`. That successor is cited,
not folded into v63.

## The identifier is consumed

`C-RH-RAY-FINITE-WINDOW-CERTIFICATE-2-N` is spent. It must not be reused,
renamed, repaired, rerun or resumed. The successor is a fresh lane and
repairs nothing in this one.

The source branch remains the exact audit surface. Its proof, breaker,
engine and wrapper are cited, not folded, promoted or regraded by this
record.

## Canon effect

None. RH remains open. No Canon, Registry, Frontier, evidence, gate,
dependency or claim status changes. The live `H` and `O` count remains 30.
