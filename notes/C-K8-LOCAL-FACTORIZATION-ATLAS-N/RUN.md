# Execution record

> **NON-CANONICAL.** Audit record only; no formal-probe or evidence authority.

## Freeze-before-run chronology

1. Issue `#749` froze the owner, branch, path, scope, and decisive falsifiers.
2. `PREREG.md` and `verify.py` were drafted without execution.
3. A separate blind subagent read only the final `PREREG.md` and authored
   `break.py`; it did not inspect or execute `verify.py`.
4. The three files were pushed, publicly read back byte-for-byte, and pinned at
   commit `aea19ff5238c05bb47fd39a735a440525caf09a1`.
5. Their SHA-256 hashes and Git blob identifiers were recorded in issue `#749`
   as comment `5490536033`, explicitly before either executable ran.
6. Only after that public record existed were the two commands below executed.

## Frozen executable hashes

```text
94023c59094a20e46f644170a1d6601fec07314a74b9461d73738e44891c0f98  verify.py
0aa69d8280b02a081023d40eebf95808875c786db50894f971e79c0ed14b6b25  break.py
```

## Environment

```text
Python 3.12.13
Linux 6.18.35 x86_64
standard library only
```

## Accepted verifier

Command:

```bash
python3 notes/C-K8-LOCAL-FACTORIZATION-ATLAS-N/verify.py --limit 1000000
```

Exit status: `0`. Exact stdout is `EXPECTED.txt`.

The verifier checked 78,497 odd primes, all three exact quadratic-algebra
identities, shifted Eisenstein, the separate `p=2` reduction and `Q_2`
certificate, Legendre rows, modular route products, independent finite-field
factor degrees, `V_4` fixed fields, and the ordered `p=5` residual actions.

## Blind breaker

Command:

```bash
python3 notes/C-K8-LOCAL-FACTORIZATION-ATLAS-N/break.py \
  --expect-sha256 0aa69d8280b02a081023d40eebf95808875c786db50894f971e79c0ed14b6b25
```

Exit status: `0`. Exact stdout is `BREAKER_EXPECTED.txt`.

The breaker found no decisive falsifier. Its design is materially distinct: it
enumerates all possible monic quadratic divisors from coefficient equations,
brute-cross-checks small fields, constructs the cyclotomic action in an exact
rational basis, and builds the ordered `F_25 x F_25` CRT product explicitly.
Its self-hash matched the pre-run public pin.

The two finite scans are audits. They are not used to infer universality.

