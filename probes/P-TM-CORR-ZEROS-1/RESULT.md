# P-TM-CORR-ZEROS-1 result record

Status: `PROOF-SURVIVES / TWO-ARCHITECTURE REPLAY PENDING / CANON UNCHANGED`.

## Decision

```text
P-TM-CORR-ZEROS-1 PROOF-SURVIVES
```

The self-contained proof in `PREREG.md` proves the four frozen theorem
clauses and the universal parity lemma. After the immutable public pin and
byte-for-byte readback, the accepted verifier returned exit code zero,
empty stderr, `SCIENTIFIC DECISION PROOF-SURVIVES`, and `SUMMARY 7/7 PASS`.
Its exact stdout is `EXPECTED.txt`.

This result record does not by itself complete the repository gate. The
single-probe pull request must replay the pinned verifier on GitHub-hosted
x86_64 and aarch64, and both jobs must reproduce `EXPECTED.txt` byte for byte.
Any architecture, hash, stdout, stderr, exit, or policy failure has STOP
precedence and remains public; it is not repaired in place.

## Frozen theorem scope

For the balanced one-sided Thue--Morse sequence

```text
u_n = (-1)^s_2(n),
S_k(N) = sum_(0 <= n < N) u_n u_(n+k),
c(k) = lim_(N -> infinity) S_k(N)/N,
```

the written proof establishes exactly:

1. both finite dyadic identities for every `m,N>=0`;
2. existence and uniqueness of every `c(k)`, the frozen recurrence, and
   `3c(k) in Z[1/2]`;
3. `c(k)=0` exactly when the positive lag has odd part `5` or `7`;
4. `c(m)=c(m+1)` exactly at `m=1`;
5. the scaled-pair integrality and odd-sum/odd-difference parity lemma for
   every `m>=4`.

The finite verifier ranges audit the proof carrier; they are not the source
of the universal quantifiers.

## Scope and priority firewall

The result is L5 abstract drive-word mathematics only. It provides no L1
realization, L6 measure, spectral statement, apparatus, decoder, physical
prime, `J`, `zeta_5`, or `F_5^6` lift. The excluded general discrepancy bound
remains excluded. The prior literature and all earlier exposed candidate
outputs are disclosed in `PREREG.md`; no novelty or priority claim is made
for any theorem clause or proof step.

No Canon, Registry, NORMATIVE, GATES, dependency, evidence, or scientific
status change occurs in this probe. A later separately reviewed fold may
propose only the theorem at this exact L5 scope after the required
two-architecture gate succeeds.

## Formal record

```text
public lock:          issue #694
base commit:          7f4c102e27e7b2ebdf5ca9215db5c5ab846ebbe2
pin commit:           f594c8ddd39e63432ac58026dd402b756f4893ad
PREREG SHA-256:       fc92c07cb17670872cde748d52ddf8b3b11b8e0f35ea0f20a84ffd45b8740d9b
verifier SHA-256:     a4f95475eb4b859c83b0e38256d3b9d5bc92772d6e06a57ad620ef50220a7861
EXPECTED SHA-256:     355eb61bb6fac32e3346fd4e0e76bbf6034eb9d15b372f27d1cbef91050845be
local architecture:  x86_64
local Python:        3.12.13
local exit/stderr:   0 / 0 bytes
local decision:      PROOF-SURVIVES / 7 OF 7 PASS
GitHub x86_64:       PENDING
GitHub aarch64:      PENDING
```
