# RECON-K4-W2-DELTAK-INERTIA, 2026-08-11

NON-CANONICAL. Four questions, no freeze, no result status. No known
opposite-flow pair, no G6 pair and no real failure enters anything below.
Script recon_k4_w2_deltak_inertia.py in the fleet handoff repo.

## R1, the exact formula

K is linear in the signs: K(v) = K_0 + sum_j v_j M_j for fixed integer
symmetric M_j. Flipping the cells of a mask sends v_j to -v_j there, so
with m_j = v_j on the mask and 0 elsewhere,

```text
Delta K(v, m) = K(v xor m) - K(v) = -2 sum_j m_j M_j
```

and for a weight-2 pattern with m_a = +1, m_b = -1 this is
Delta K = -2 (M_a - M_b). Verified against the direct difference on every
probe table, exactly.

## R4, the dependency, and it is the good case

Delta K depends ONLY on the mask and the signs the mask carries. The base
table does not enter. Verified. So the weight-2 perturbations are 252
fixed integer matrices that can be classified once and for all, with no
reference to fiber solutions, to domains or to any table.

## R2 and R3, rank and inertia of all 252 perturbations

```text
rank      2:  18    4:  72    6:  42    8:  60   10:  12   12:  48
inertia  (1,14,1): 18   (2,12,2): 72   (3,10,3): 42
         (4, 8,4): 60   (5, 6,5): 12   (6, 4,6): 48
```

Every weight-2 perturbation is EXACTLY BALANCED: inertia (k, 16-2k, k)
with k from 1 to 6, never anything else. That is a structural fact worth
keeping on its own: the difference of two cell matrices inside one orbit
is always a neutral form on its image, carrying equally many positive and
negative directions.

## What this closes, and what it does not

The rank gate fails: the minimum rank is 2, never 1.

The inertia gate closes exactly 18 of the 252 patterns. Those are the
ones with n_+ = n_- = 1, so by the standard bound

```text
-n_+(Delta K) <= n_-(K + Delta K) - n_-(K) <= n_-(Delta K)
```

the negative count can move by at most one, while the transition
(7,0,9) to (9,0,7) needs exactly two. For those 18 patterns the opposite
transition is IMPOSSIBLE, for every table of the stratum, fiber or not,
with no search of any kind. The 18 sit in three orbits, six patterns
each: type (0,1,2,2) of size 12, and the two size-4 orbits (0,2,2,2) and
(1,2,2,2).

The remaining 234 patterns carry k >= 2, so the simple bound permits a
change of two and closes nothing. They need the Schur gate.

## What the Schur gate would have to deliver

Write Delta K = U C U^T with C nonsingular of size 2k, and use the
bordered-matrix identity

```text
inertia(K + U C U^T) = inertia(K) + inertia(-C^-1 - U^T K^-1 U)
                       - inertia(-C^-1)
```

Since C is hyperbolic here, inertia(-C^-1) = (k, 0, k), and the
transition needs n_-( -C^-1 - U^T K^-1 U ) = k + 2. So the whole
sixteen-dimensional question does collapse onto a 2k by 2k matrix, as
hoped, but that matrix carries U^T K^-1 U, which depends on the table
through K^-1. The v-independence won at R4 is lost exactly here. A no-go
at k >= 2 therefore needs a statement about K^-1 on the fiber solutions,
not about Delta K alone.

## Honest reading

The cheap structural win is real but partial: 18 of 252 patterns are
closed by pure algebra, permanently and without compute. The other 234
are not closed by rank, not by inertia, and the Schur reduction moves the
difficulty rather than removing it. The fiber equations, which pin v, are
the only remaining lever, and they enter through K^-1.

The owner's fallback is unchanged and now more clearly valuable: the 114
low-free-bit patterns remain an exact computational arm held in reserve.
Note that the two sets are not the same: the 18 closed by algebra are
selected by the inertia of Delta K, the 114 cheap ones by how strongly
the fiber equations pin the table. Their overlap is worth computing
before any successor is frozen, since patterns closed by algebra need no
compute at all.
