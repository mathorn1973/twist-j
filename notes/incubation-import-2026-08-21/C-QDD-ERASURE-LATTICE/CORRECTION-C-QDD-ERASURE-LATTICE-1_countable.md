# CORRECTION. C-QDD-ERASURE-LATTICE-1, one word

```text
STATUS:  INTERNAL, NON-CANONICAL. Addendum. Nothing frozen is edited.
RAISED:  by the owner, 2026-08-21, on reading the result.
GRADE:   accepted. The finding is against my own prose, not against any
         gate, verifier output, or earned statement.
```

## The error

`RESULT-C-QDD-ERASURE-LATTICE-1_2026-08-21.md` line 112 and
`PREREG-C-QDD-ERASURE-LATTICE-1.md` lines 44 and 133 say the architecture
residual `H_k` "leaves a continuum" of physical classes.

That word is wrong. The frozen class admits rational laws only:

```text
T = e R + r C + s J,   e, r, s in Q,   e^2 = 1,   r^2 + s^2 = 1.
```

The solution set is the rational points of the unit circle, parametrized
by `t in Q` through `r = (1-t^2)/(1+t^2)`, `s = 2t/(1+t^2)`. That set is
countably infinite and dense in the real circle, and it is not a
continuum. The verifier already printed the parametrization and its
injectivity identity `s/(1+r) = t`, so the programs were right and only
the prose was loose.

## The corrected wording

```text
was:  the architecture residual alone leaves a continuum
is:   the architecture residual alone leaves a countably infinite family,
      the rational points of the unit circle
```

Nothing else changes. `NONSELECTION` is unaffected: countably infinite is
still infinitely many physical classes, so the H rung selects nothing.
The public registry text of QDD-INSTRUMENT-NONSELECTION says "infinitely
many physical post-state classes" and never said continuum, so no public
row inherits the error.

## Why it is not edited in place

`PREREG-C-QDD-ERASURE-LATTICE-1.md` is pinned at
`6ba0d1e947e310e1c8952e83bdb59bdac8642eff72b28a1d9504aa402adbb921` in
`FREEZE-C-QDD-ERASURE-LATTICE-1.txt` and is frozen. `RESULT` is published
at `171dc9a2...` in `mathorn1973/twistj-handoff`, branch
`handoff/qdd-erasure-lattice-20260821`, and its hash is recorded in
`INDEX.md`. Both are therefore corrected by this addendum and not by
rewriting, in the way POLICY treats a sealed object.

## Second item, an improvement rather than an error

`E4` was earned by a 16-dimensional exact nullspace computation. It has a
one-line proof that is stronger than what was run:

```text
D satisfies Phi_5, and {I, D, D^2, D^3} are independent, so the minimal
polynomial of D is exactly Phi_5. Phi_5 is irreducible over Q, so
comm(D) = Q[D] = Q[x]/(Phi_5) = Q(zeta_5), a FIELD. A field has no zero
divisors. Hence A P_k = 0 with A in comm(D) forces A = 0 whenever
P_k != 0.
```

Consequences. First, the emptiness does not depend on the record anchor
being the stabilizer projector: it holds for ANY nonzero anchor, checked
exactly on 199 further anchors, all empty. `E4` is therefore stronger
than stated. Second, the emptiness is arithmetic in origin. It holds
because `Phi_5` is irreducible, that is, because 5 is prime. The motor
resists reading for the same reason the field is a field.
