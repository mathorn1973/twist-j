# Observer/boost public reproduction

This witness fixes the exact algebraic boundary of the Public Canon v1
observer/boost layer. It uses only the Python standard library and exact
arithmetic in `Q(sqrt(5))`.

The theorem-level statement is the boost reading split. Put

```text
phi = (1 + sqrt(5))/2,  psi = (1 - sqrt(5))/2 = -phi^-1,
C_n = phi^n + phi^-n,  S_n = phi^n - phi^-n.
```

The Binet identities give

```text
L_n       = phi^n + psi^n,
sqrt(5)F_n = phi^n - psi^n.
```

Since `phi^-n = (-1)^n psi^n`, substitution proves for every nonnegative
integer `n`

```text
(C_n, S_n) = (L_n, sqrt(5)F_n)  when n is even,
(C_n, S_n) = (sqrt(5)F_n, L_n)  when n is odd.
```

This is an identity, not a finite-range inference. The finite loops in the
verifier guard the implementation and the committed output. They also check
the exact addition law for `beta_n = S_n/C_n`, the constant unit gap
`C_n^2 - S_n^2 = 4`, and the equivalent Lucas--Fibonacci identity.

The remaining three public claims are dictionary statements. The witness
checks their algebraic support without promoting the readings themselves:

- integer boost exponents add;
- the observer partition of `mu_4` has sizes `1+3`, while multiplication by
  the alternator `-1` has two fixed-point-free orbits of sizes `2+2`;
- `A = diag(1,-1)` commutes with `B_J = diag(phi,phi^-1)`, has two exact axis
  projectors, and supplies the alternator tick in `STEP = B_J A`.

No density theorem, continuum limit, experimental velocity claim, or claim
that the dictionary is forced is made here.

Run:

```bash
python3 reproduce/observer-boost/verify.py
```

Success means exit code `0`, empty stderr, and stdout byte-identical to
`EXPECTED.txt`.
