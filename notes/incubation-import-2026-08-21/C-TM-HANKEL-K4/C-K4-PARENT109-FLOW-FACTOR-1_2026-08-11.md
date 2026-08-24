# C-K4-PARENT109-FLOW-FACTOR-1: T-A unfired, T-B FIRED, 2026-08-11

```text
STATUS:  incubation candidate, NO AUTHORITY. G2 fired, so the candidate
         is dead under this id per its own Field 5; the T-A gate is
         recorded as UNFIRED at the declared scope, which is NOT a
         confirmation and is not evidence for T-A.
PREREG   revision 1, sha256
         42b3bb4a38b6cc5d8e578c6502959fb7a400061b226a13bc1f201abb9b355b41
         (revision 0, d3ff23ce..., superseded before any computation)
VERIFIER verify_k4_parent109_flow_factor_1.py
         sha256 f487114a240fdc3cb2c39ae2a4590e8ab9b6ccf3cf04ae2002f329a0809c8dea
         41264 B, assembled from the pinned third cut 2bf4bf01...
STDOUT   sha256 469322f7259373b1034606a8ba79327eb6c0f7ecd2a7a8992230778800ee7657
         1753 B, exit 1 (fired), empty stderr
LEG 1    x86_64, accepted run, well inside the 3600 s budget
LEG 2    aarch64, Debian 13, same verifier hash confirmed before
         execution, stdout sha256 469322f7... byte-identical to leg 1,
         empty stderr, exit 1
SEALED   2026-08-11. Both legs complete, two-architecture evidence
         closed, candidate administratively dead under this id. No
         successor may reuse the id, and no later run may reopen it.
```

## E', as frozen

```text
D 19448 tables, D union B2 29534, with T3 78599 tables
flow +1: 58534, flow -1: 20065
two-profile bit values common to both LCG blocks: 0
block index intervals [0,3999] and [4000,7999] asserted disjoint
```

## G1, T-A: UNFIRED at the declared scope

```text
A1  400 bases, 47934 weight-2 orbit-preserving moves, 0 fiber pairs
A2  40 bases, 251843 weight-4 moves, 0 fiber pairs
A3  mask {21,41,37,61}, COMPUTED orbit size 6, stabilizer order 4;
    79352 eligible applications, 191 F_109 preserved, 0 profile flips
```

The owner's insistence that the orbit be computed rather than declared
was immediately vindicated: the assumed 24 images are in fact 6, the
stabilizer has order 4, and a frozen "24" would have been a false
statement inside a gate.

No opposite-flow pair shares an F_109 value anywhere in the three arms.
T-A is UNFIRED at this scope. Per the frozen asymmetry this is not a
proof, not evidence, and may not be quoted as either: 2^65 rules out
enumeration, and only a structural proof could ever confirm T-A.

## G2, T-B: FIRED on E'

```text
F_14 = eight orbit sums (indices 0..7) + full gram211, dim 14
buckets on E': 2321
counterexample: 0x121e73f85d7c190 flow +1 versus 0x121ef3e85d5c1d0 flow -1
```

The best surviving compression of the previous cut dies on the enlarged
abstract domain, exactly as the fragility pattern predicted: every
low-dimensional decider found so far has been a domain artifact. The
candidate is dead under this id by its own zero-tolerance threshold.

## G3, regression and readback set

Zero F_14 opposite-flow hits and zero F_109 fiber hits across E' union
the seventeen reals. No independent evidence is claimed from this set;
it can only expose implementation error or contradiction, and it exposed
neither.

## G4, diagnostics, gating nothing

```text
sums10 COLLIDES, gram31 COLLIDES, gram22 COLLIDES, gram211 COLLIDES
full109 separates
d_min on E' at least 9 (search bounded at cost 8 by the freeze)
```

Every proper layer of the parent map now collides on E', including
gram31, which survived every earlier domain. The full 109 map is the
only thing left standing. The lane has therefore been reduced to exactly
the question the owner named: is the parent map itself enough.

## Reading

The two outcomes are consistent and sharpen the program. Compression
below the full map keeps dying as domains grow (four layers and F_14 all
gone), while the full map has never failed on any domain tried:
78599 abstract tables here, plus the reals, with zero fiber violations,
and 191 genuine fiber pairs from the mechanism family that all preserved
flow. T-A is the right question and it is still open.

## Next, owner's call

```text
1  successor id repeating T-A on a domain built to HURT it: many
   mechanism families rather than one, deeper flips, and fiber pairs
   generated directly rather than found by luck
2  the structural route: characterize the fiber relation of F_109 on
   the two-profile locus, which is the only path that can ever confirm
   T-A rather than fail to kill it
3  nothing further on compression: F_14 is dead, and rebuilding another
   low-dimensional decider on a new domain would repeat a known error
```
