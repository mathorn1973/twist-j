# PREREG: P-CENSUS-REPLAY-1

**FORMAL PREREGISTRATION PIN CANDIDATE.** Public claim: issue #72. No formal
execution of this probe verifier occurred before this preregistration commit.

```text
ISSUE:         #72 https://github.com/mathorn1973/twist-j/issues/72
BASE_COMMIT:   72a04e1e2dae8df66f170b169328611b75a8a1af
LAYER:         L1 state only; no lift to L2-L6 is claimed
TARGET:        fresh two-architecture replay evidence for CENSUS-313,
               CENSUS-Z5-SHEET, CENSUS-PAIRING, and CENSUS-HOSTING [all C]
STATUS_ACTION: none in this probe; all four rows remain C
```

## Frozen fields

```text
EQUATION     Replay the eleven exact gates of the public kernel-census
             witness without changing a threshold:

             G01  a^2=b^2=c^2=d^2=e^2=id and (bc)^5=id on all states;
             G02  exactly 313 attractor signatures;
             G03  312 signatures of size 20 and one of size 10, with
                  disjoint recurrent support of size 6250;
             G04  312 basins of size 50 and one of size 25, covering all
                  15625 seeds;
             G05  313=13^2+12^2;
             G06  every recurrent state has z_6 in {1,4};
             G07  only b,d,e fire on the recurrent sheet;
             G08  the piston pairing is an involution with 144
                  transpositions and 25 fixed attractors, giving 169
                  classes;
             G09  |<d,beb>|=10, d(beb)=T_0=(0,0,0,0,3,2), and the
                  two-coset hosting formula holds on all 313 attractors;
             G10  every signature is closed under both one-step drive-bit
                  transitions;
             G11  the independent second 300-tick window reproduces every
                  signature exactly.

CODE         verify.py is an exact byte-for-byte copy of
             reproduce/census/verify.py at BASE_COMMIT.
             Frozen verifier SHA-256:
             1df13ba2218acaa9cf48dab2480e6472b107691aac868618dc7f91d511718a5c
             Frozen verifier bytes: 8127. Python standard library only;
             exact integer arithmetic; deterministic; no files written.

CARRIER      X=(Z/5Z)^6, 15625 encoded states, with coordinates
             (p1,p4,p1p,p4p,q,t), the five public involutions a,b,c,d,e,
             z_6(x)=sum_i x_i mod 5, Thue-Morse drive
             theta_n=popcount(n) mod 2, and selector
             i_n=(z_6+2 theta_n) mod 5. Every seed receives warmup 400,
             collection window 300, then a disjoint stability window 300.
             Attractor signatures are sets of states in the first window.

SYSTEMATICS  This is an architecture replay, not an independent algorithm.
             It strengthens auditability only; it does not prove that the
             400/300/300 protocol is independent of its finite windows or
             that it captures a broader all-orbit notion. Historical
             aarch64/x86_64 genesis executions are informational because
             they lack one immutable public formal pin and neutral run
             records. The formal owner leg must be Linux aarch64 and the
             GitHub leg x86_64, both at the same pinned verifier hash.
             The public reference output is already frozen at
             reproduce/census/EXPECTED.txt, SHA-256
             f0022dc0c19314c88efae2974139b659d0748b3d039c9f9368de1be891a8bbb0,
             1125 bytes. It fixes the threshold but is not substituted for
             the fresh post-pin owner stdout.

THRESHOLD    PASS only if the post-pin Linux aarch64 command exits 0,
             writes empty stderr, prints RESULT 11/11 ALL PASS, and its
             stdout is byte-identical to the frozen public reference; the
             GitHub x86_64 check must reproduce the same verifier hash and
             stdout bytes. FAIL-STOP on any hash, byte, gate, exit-code, or
             stderr mismatch. Preserve a failed formal result; do not move
             thresholds or silently rerun under a changed pin. A gate
             failure contradicts the corresponding claim at its frozen
             finite-protocol scope. An architecture-only mismatch blocks
             the evidence upgrade and requires a separately reviewed cause.
```

## Formal command and environment

From a clean checkout of the full immutable pin:

```text
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
python3 probes/P-CENSUS-REPLAY-1/verify.py
```

The owner record must use neutral public fields (`platform`, `architecture`,
Python version, hashes, byte counts, exit code, and elapsed time). It must not
contain a machine nickname or private path.

## Scope firewall

- No Canon, registry, evidence, dependency, history, gate, or status file is
  changed in this probe.
- No claim is promoted. A later sealed Canon fold may decide whether the
  fresh evidence changes only `architecture_requirement` while retaining C.
- This replay does not discharge census protocol-independence and does not
  convert any downstream `BOUNDED_BY` relation into `REQUIRES`.
- No geometry, support, stream, measure, continuum, or physical-reading lift
  is asserted.

## Pin checklist

1. Create and record the public issue claim for `P-CENSUS-REPLAY-1`.
2. Replace the draft marker and `ISSUE` placeholder with the exact issue.
3. Confirm `verify.py` is byte-identical to `reproduce/census/verify.py` and
   has the frozen SHA-256 and byte count above.
4. Commit and push only this `PREREG.md` and `verify.py` as the immutable pin.
5. Do not amend, rebase, squash, or force-push the pin.
6. Only then execute the owner aarch64 gate and add `EXPECTED.txt`, `RUN.md`,
   and `RESULT.md` in a later commit on the same branch.
