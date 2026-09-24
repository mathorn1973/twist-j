# ADDENDUM 2 to PREREG-C-PHOTON-CONTRAST-DRIFT-N: host substitution

Status: NON-CANONICAL. Written 2026-09-22 about 23:21 CEST, before any
analysis of the drift chains on any host. It changes no equation, code, data,
gate, rule, terminal or reading.

## What happened

The primary x86_64 host rebooted at about 23:12 CEST. Its temporary working
directory was cleared. The 20 x86_64 chains, started at 22:16, were lost
before completion, and so were the raw logs of parts A2 and A3 of
C-PHOTON-PHASE-ORIENTATION-N kept there. The analysis outputs and hashes of
A2, A3 and B3 are in the project. The engine is deterministic and bitwise
reproducible across the two architectures used, so those logs can be
regenerated exactly from the pinned code and seeds.

The aarch64 leg was not affected. Its working directory was moved by rename,
on the same file system, to a persistent location while the chains were
running. The B3 logs on that host still match the B3 manifest (sha256
ca004f0c...).

## Substitution

The x86_64 leg was restarted at 23:18 CEST on a different x86_64 Linux host:

- the same five source files, re-hashed on the host and matching
  PIN-DRIFT.sha256;
- gcc 14.2 with the same flags (-O2 -ffp-contract=off), Python 3.13.5;
- the same job list and seeds, into a persistent directory.

Build check before any drift data: the B3 chain TW_L8_cold1 was regenerated on
this host. Its log is byte-identical to the B3 manifest entry (sha256
c5af4c846cb9c9db9cf958bc8a89f371ce5db1f6b28d859ffe67055869c6fdc4).

The reproduction clause is unchanged. The END hashes of the x86_64 leg on the
substitute host are compared chain by chain with the aarch64 leg. If the
aarch64 leg finishes first, its analysis is reported as provisional until the
x86_64 leg is compared.
