# RECON-K4-W2-OVERLAP-TRACE, 2026-08-11

NON-CANONICAL, two cheap questions, no freeze. Script
recon_k4_w2_overlap_trace.py in the fleet handoff repo.

## Q1, the overlap, and the answer is the awkward one

```text
closed by the Delta K inertia gate   18
cheap by free bits (at most 9)      114
BOTH                                  0
NEITHER                             120
```

The two sets are DISJOINT. Every pattern the algebra closes is expensive,
and every cheap pattern is still open. So the computational fallback
loses nothing to the algebra gate and gains nothing from it: the arm
still has to decide all 114 cheap patterns, and 120 patterns are both
expensive and open.

That is worth knowing before any successor is frozen, and it is the
opposite of what one would hope. It also carries a hint: the patterns
whose perturbation is spectrally small (rank 2, inertia (1,14,1)) are
exactly the ones the fiber equations pin weakly, leaving 19 free bits.
Weak spectral action and weak linear pinning coincide, and so do their
opposites.

## Q2, a new exact constraint linking the fiber condition to the spectrum

The parent map does not carry the 55 trivial-sector quadratics as
coordinates, which was the owner's correction and stands. But it carries
the ten orbit sums, so every product of orbit sums is a FUNCTION of the
map. Together with the 78 + 15 + 6 Gram coordinates that is
55 + 78 + 15 + 6 = 154, the whole space of S_4-invariant quadratics.

```text
F_109(x) = F_109(y)  =>  every S_4-invariant polynomial of degree at
                         most 2 in the signs agrees on x and y
```

Tr K is linear in the signs and S_4 invariant. Tr K^2 is quadratic and
S_4 invariant. Both therefore agree on every fiber pair:

```text
Tr K(x) = Tr K(y)        and        Tr K(x)^2 = Tr K(y)^2
```

Checked exactly on 41 fiber pairs, all constructed from the equations and
one from the known equal-F_109 pair: both agree in every case. Control on
40 non-fiber neighbours of one table: Tr K differs on 19 of them and
Tr K^2 on all 40, so the agreement is not a triviality of the operator.

Consequence for the no-go route: on any fiber pair the first two power
sums of the spectrum coincide, so the two eigenvalue multisets lie on one
exact hyperplane and one exact sphere. The transition (7,0,9) to (9,0,7)
must move two eigenvalues across zero while keeping sum and sum of
squares fixed. That is a genuine constraint and the first bridge between
the fiber condition and the spectrum, and it is exactly what the Schur
route was missing. It is NOT yet a proof: two power sums do not by
themselves forbid a sign change of two.

The natural next question, cheap to ask and not asked here: does the
fiber condition also fix higher power sums, and if not, what is the
smallest p with Tr K^p free? Degree p invariants beyond 2 are not
determined by the map, so p = 3 is the first candidate, and the answer
decides whether this bridge is one constraint or a whole tower.
