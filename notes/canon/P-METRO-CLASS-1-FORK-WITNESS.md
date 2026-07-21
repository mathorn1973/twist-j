# P-METRO-CLASS-1: compositional fork witness and completeness recommendation (NON-CANONICAL)

Status: `DRAFT / GOVERNANCE-INPUT / DEFINITION-UNRESOLVED`

This note answers the two open decisions of
`notes/canon/P-METRO-CLASS-1-SCOPE-MAP.md`: the section 5 compositional
fork (factorwise versus joint spectral) and the section 7 completeness
choice (finite surface versus all-parameter theorem). It is not `PREREG.md`,
a public definition, theorem, verifier, run, Canon change, or status
proposal. It changes no Canon object. `METRO-ADMISSIBILITY` stays `[O]`.

## Authority pin

```text
Canon:              Public Canon v14
state:              ACTIVE
tag:                canon-v14
activation commit:  f278855cada75691142c02ebad1a75ecc2730db3
content commit:     ab4ea07d15ab1cfa0c403d3c2a74164011ffa0e7
Canon SHA-256:      f9f06af42a9b0b63f806603ddc671ebe6a9e5014b50d230da04a28722ed1a6a2
Canon bytes:        87061
owner row:          METRO-ADMISSIBILITY [O]
gate:               GATE-L5-L6-METRO-NORMALIZATION
child candidate:    METRO-COMMUTING-DIGIT-AUTOMATIC-CHILD-1
scheduler:          DECODER_CORE / ROOT / READY / FORMAL
```

## 1. The fork is decidable by witness, not by taste

A minimal exact witness inside the proposed child class settles section 5.
Take the smallest nontrivial parameters: `q = 2`, `a = 2`, `r = 2`,
`|S| = 2`, the frozen column-function convention.

```text
state carrier   S = {0, 1}
coordinate 1    delta_(1,0) = delta_(1,1) = swap    T_1 = swap matrix
coordinate 2    delta_(2,0) = id, delta_(2,1) = swap  T_2 = averaging idempotent
readout         W5(s) = e_s in Q_(>=0)^2

verified exactly:
  all digit actions commute (all pairs, all states);
  T_1^2 = I with peripheral eigenvalue -1: the factorwise limit
    P_1 = lim T_1^m DOES NOT EXIST (the gap ||T_1^(m+1) - T_1^m|| is
    exactly 1 at every m);
  T_2^2 = T_2 and T_1 T_2 = T_2 T_1 = T_2: coordinate 2 kills the
    peripheral mode of coordinate 1 in every joint box;
  the direct anchored value Raw_(m1,m2) = (1/2, 1/2) EXACTLY for every
    start, every m1 >= 0 and m2 >= 1; Normalize gives PROBABILITY(1/2, 1/2),
    start independent and order independent.
```

The factorwise/iterated decision and the direct decision therefore
genuinely disagree at the smallest nontrivial size, by exactly the
mechanism the note names (a periodic peripheral mode of one coordinate,
killed jointly). Two architectures byte identical (x86_64 and aarch64):

```text
witness stdout sha256 014ce19c0dcd54724d02e8ead031b01eee9f251ff31d6757ed4c52f23c793606
```

Incubation-lane candidate evidence (candidate-C), not authority.

## 2. Recommendation on section 5

```text
Choose B, JOINT SPECTRAL, and type the compositional map as a CERTIFICATE
of the direct property; disagreement is STOP integrity, not a scientific
negative. Register the witness above as a computed control that kills
factorwise-as-independent-law, so it cannot be reintroduced later; keep
FACTORWISE NEGATIVE only as the name of that sealed non-equivalence.
```

Grounds. The sealed one-dimensional precedent already types the spectral
side as a characterization, not a second science channel:
`METRO-DFAO-SPECTRAL-IFF` is an iff between the uniform direct mean and the
spectral condition. Extending faithfully to the `N^a` class keeps the
scientific object as the direct translated-box property, with the joint
spectral decomposition, on the reachable submodule only and with exact
certificates for peripheral phases and Jordan structure as the note already
requires, as its decidable form. Option A would enshrine a provably
inequivalent definition as a permanent co-equal decision and generate
disagreement that is not physics.

## 3. Recommendation on section 7 (completeness)

```text
Two-tier freeze:
1  ALL-PARAMETER THEOREM for the ANCHORED q-adic criterion: an exact
   terminating decision by simultaneous primary/peripheral decomposition
   of the commuting rational matrices on the reachable submodule. This
   mirrors the sealed 1-D shape (METRO-ADMISSIBILITY-FINITE-STATE is a
   decision theorem, not a bounded enumeration).
2  The TRANSLATED-BOX uniformity (the boundary decomposition and effective
   modulus that section 4 itself flags as still required) stays a named
   obligation with its own gate; it is not silently folded into the
   anchored freeze.
FINITE SURFACE remains the honest fallback only if the owner insists on a
single frozen criterion equal to the full translated-box property, since
that theorem is not in hand for arbitrary (q, a, r, |S|).
```

This keeps the class from claiming a bounded exhaustive probe and an
unbounded theorem at once, the trap the note names.

## 4. What stays open

The governance routing of section 1, the exact digit and padding
convention, the L5/L6 transport adoption, the effective translated-box
theorem, minimization and blocking proofs, and the layer-gate endpoints all
remain owner decisions. This note selects a fork and a completeness shape
and supplies the deciding witness; it adopts nothing.
`METRO-ADMISSIBILITY` stays `[O]`, `METRO-EDGE-SCALE` stays `[O]`,
`OBSERVER-WRITE-PORT` stays blocked, and no Canon frontier count changes.
