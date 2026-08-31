# P-O5-WALSH-LINK-HOMOLOGY-1 preregistration

Status: **FORMAL PUBLIC PROBE PREREGISTRATION / PROOF-FIRST / UNRUN / CANON UNCHANGED**

Date: 2026-08-27.

## Public identity

```text
probe:             P-O5-WALSH-LINK-HOMOLOGY-1
public claim lock: issue #601
owner:             A. M. Thorn / delegated session 2026-08-27
branch:            probe/P-O5-WALSH-LINK-HOMOLOGY-1
path:              probes/P-O5-WALSH-LINK-HOMOLOGY-1/
basis main:        d14a8fa3b4e5dd15d1294c4b2022e8dc6c649a11
canon:             Public Canon v67, tag canon-v67
CONTENT_COMMIT:    f58df589519d04820d0d819afcb732e2c2ec0429
CANON_SHA256:      b20b62ee730c2b5ac2e2845cb99f40a1cf72618eb71dae3c1279056943d43a98
CANON_BYTES:       351502
action layer:      NOT_APPLICABLE, finite simplicial homology / exact character algebra
layer lift:        none
authority:         none until a later sealed Canon fold
```

This is the fresh successor of abandoned
`P-O5-ORIENTATION-CHARACTER-HOMOLOGY-1`, issue #599, pin
`66999aa757850d0761136b69e79076753c7f1d34`, terminal abandonment merged by
PR #600 as `d14a8fa3b4e5dd15d1294c4b2022e8dc6c649a11`. That pin earned no
scientific result because its one formal invocation did not complete inside
the local runtime limit.

The theorem, carrier, finite N audit surfaces, falsifiers and breaker witnesses
are unchanged. The successor changes only `support_faces(N)` to exact
product-pruned recursion: after a partial prime product exceeds `N`, no
larger-prime extension is enumerated. No scientific threshold moves.

Adjacent lanes remain separate: merged #598 supplies the incidence-triangle
no-go only; squarefree-core and divisor-read probes are not evidence inputs;
draft Notes PR #595 is NON-CANONICAL; `TRIVIAL-RAPIDITY-EVALUATION-BRIDGE [O]`
is untouched.

## Proposed row

```text
O5-WALSH-LINK-HOMOLOGY [candidate-T]
```

For `N>=1`, let `Delta_5(N)` have as vertices the rational primes `p<=N`
with `chi_5(p)=1`, and faces the finite sets `S` with
`prod_(p in S)p<=N`, including the empty face. Let `K_5(N)` be its
octahedralization: over each support prime are two formal vertices `(p,+)` and
`(p,-)`, and an oriented face chooses at most one of them. Order simplices by
increasing rational prime. Work with augmented chains over `Q`.

For faces `J subseteq S`, define the unnormalised Walsh vector

```text
E_(S,J)
  = sum_(epsilon:S->{+-1})
    prod_(j in J)epsilon(j) [S,epsilon].
```

### Theorem A: Walsh basis

For fixed `S`,
`sum_epsilon chi_J(epsilon)chi_J'(epsilon)=2^|S|` when `J=J'` and zero
otherwise. Hence the `2^|S|` vectors `E_(S,J)` form a `Q`-basis of the
oriented-face space over `S`. Grouping equal `J` gives a direct sum of chain
groups. Invertibility of `2` is load-bearing; no characteristic-two theorem is
claimed.

### Theorem B: character boundary

If `S={p_0<...<p_q}`, then

```text
d E_(S,J)
  = 2 sum_(p in S\J) (-1)^pos_S(p) E_(S\{p},J).
```

Proof: if the deleted `p` lies in `J`, the two extensions of a lower
orientation have opposite Walsh weights and cancel. If `p notin J`, they have
equal Walsh weight and add, giving the factor `2`. Thus every fixed `J`
defines a chain subcomplex `C_*^(J)`.

### Theorem C: link chain isomorphism

For `J in Delta`, let

```text
L_J = link_Delta(J),
nu_J(T)=#{(j,t) in J x T:j<t},
Psi_J([T])=2^(-|T|)(-1)^nu_J(T) E_(J union T,J).
```

The position difference between `t` in ordered `J union T` and in ordered `T`
is `#{j in J:j<t}`. Removing `t` changes `nu_J` by the same parity. The factor
`2` in Theorem B changes `2^(-|T|)` to `2^(-(|T|-1))`. Therefore

```text
d Psi_J([T]) = Psi_J(d[T]).
```

The map `T -> J union T` is a degreewise bijection from link faces to supports
in the `J` sector, and `dim(J union T)=dim(T)+|J|`. Hence `Psi_J` is a chain
isomorphism from the augmented chain complex of `L_J`, shifted upward by
`|J|`, onto `C_*^(J)`.

### Theorem D: homology and Euler decomposition

Taking homology of the finite direct sum gives, for every integer `q`,

```text
H~_q(K_5(N);Q)
 ~= direct_sum_(J in Delta_5(N))
    H~_(q-|J|)(L_J;Q).
```

The augmented degree `-1` is included. Since a degree shift by `|J|`
multiplies reduced Euler characteristic by `(-1)^|J|`,

```text
chi~(K_5(N))
 = sum_(J in Delta_5(N)) (-1)^|J| chi~(L_J).
```

These are exact finite identities, not estimates.

## Falsifier first

The candidate theorem is falsified by one exact defect: a support Walsh family
is dependent over `Q`; a `p in J` deletion survives or another deletion has a
wrong sign/factor; `nu_J` or `2^(-|T|)` fails the chain conjugation; a sector
has wrong dimension; one rational Betti number violates the shifted link sum;
the reduced Euler identity fails; or the construction selects one orientation,
admits inert/ramified support, or imports a target cancellation/RH/GRH claim.

A stale basis, changed pin, failed startup preflight, nonzero exit, nonempty
stderr, stdout mismatch, architecture disagreement, moved threshold or scope
widening is STOP, not a mathematical counterexample.

## Frozen fields and gates

```text
EQUATION:     Theorems A-D exactly as displayed.
CODE:         probes/P-O5-WALSH-LINK-HOMOLOGY-1/verify.py; stdlib only;
              exact integers/Fraction, deterministic finite chains.
CARRIER:      Delta_5(N), K_5(N), augmented Q-chains, Walsh sectors and links.
SYSTEMATICS:  unordered split orientation pair; increasing-prime simplex order.
THRESHOLD:    G01-G07 and B1-B5 exactly; LF EXPECTED, exit 0, empty stderr.
LAYER:        NOT_APPLICABLE; finite topology / exact character algebra.
```

`support_faces(N)` must use product-pruned recursion. This changes runtime only,
not the mathematical face set or the frozen N surfaces.

```text
G01 Walsh orthogonality through support size 5.
G02 boundary formula for N in {11,121,209,500}.
G03 Psi_J chain map on every link sector for the same N.
G04 rational Betti decomposition for N in {1,11,121,209,500}.
G05 reduced Euler decomposition for N in {1,11,121,209,500,1000}.
G06 B1-B5 at 11,11,11,(209;11,19),char2.
G07 exact-rational stdlib source firewall.
```

Breakers mutate the production constructors: erase Walsh signs; retain
`p in J` deletion; omit factor `2`; omit `nu_J`; reduce the 2x2 Walsh matrix
modulo `2`.

## Formal discipline and nonclaims

Before the pin the verifier may only be read and AST-parsed. The first pushed
probe commit contains only fresh `PREREG.md` and `verify.py`. After exact
readback, the startup preflight is

```text
env -i PATH=/usr/bin:/bin LC_ALL=C PYTHONHASHSEED=0 TZ=UTC \
  /usr/bin/python3 -c "print('PYTHON_STARTUP_CLEAN')"
```

and the single scientific command is

```text
env -i PATH=/usr/bin:/bin LC_ALL=C PYTHONHASHSEED=0 TZ=UTC \
  /usr/bin/python3 probes/P-O5-WALSH-LINK-HOMOLOGY-1/verify.py
```

No threshold, witness, carrier, equation or firewall may move after the pin.

No RH/GRH result, summatory estimate, analytic continuation, zero statement,
Hecke/automorphic object, selected orientation, physical interpretation,
probability statement or L1-L6 lift is claimed. No claim is made that link
homology is small, concentrated, sign-definite or uniformly bounded.
