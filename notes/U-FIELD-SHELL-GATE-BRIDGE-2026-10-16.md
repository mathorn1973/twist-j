# Native U piston invariance and magnetic seed generation at the L Z^4 field gate

**NON-CANONICAL / L1 mathematical note.** This note records an exact algebraic
bridge between the piston block of the native kernel `U` on `F_5^6` and the
`L Z^4` shell-conversion gate of the conservative integer field cell in
`DEF-FIELD-WORK-RECORD-CHAIN` (`FIELD-CONSERVATIVE-CHAIN-LAW`). It creates no
canonical claim, status change, gate closure, probability law, or permission
for a formal probe run. It does not derive the declared field chain from `U`
or `J`, and the existing live `H` and `O` owners remain unchanged.

## 1. Setup and the a-swapped piston frame

Write the autonomous native state on `X = F_5^6` in the order
`x = (p1, p4, p1p, p4p, q, r)` with piston block `p = (p1, p4, p1p, p4p)` in
`F_5^4`, phase `z(x) = p1 + p4 + p1p + p4p + q + r mod 5`, balanced lift
`ell(0, 1, 2, 3, 4) = (0, 1, 2, -2, -1)`, and generators `(a, b, c, d, e)` as
in Canon section 2:

```text
a(x) = (p4, p1, p4p, p1p, q, r),
b(x) = (-p1p, -p4p, -p1, -p4, -q, -r),
c(x) = (2 - p1p, 1 - p4p + r, 2 - p1, 1 - p4 - r, 1 - q, -r),
d(x) = (2 - p1, 1 - p4, 3 - p1p, 4 - p4p, 1 - q, 1 - r),
e(x) = (2 - p1, 1 - p4, 3 - p1p, 4 - p4p, 2 - q, 1 - r).
```

Define the `a`-swapped piston reading and its balanced integer lift:

```text
tilde_p(x) = a_piston(p) = (p4, p1, p4p, p1p) in F_5^4,
tilde_y(x) = ell(tilde_p(x)) in {-2, -1, 0, 1, 2}^4 subset Z^4.
```

In `DEF-FIELD-WORK-RECORD-CHAIN`, the divergence-free wave embedding
`P: Z^4 -> Z^4 x Z^2`, the symplectic shear restriction `A_f`, the wave
quadratic `H(w) = w^T B_f w / 2`, and the shell conversion matrices are:

```text
A_f  = [[ 1,  0,  1,  0], [ 0,  1,  0,  1], [-2,  1, -1,  1], [ 1, -3,  1, -2]],
B_f  = [[ 4, -2,  2, -1], [-2,  6, -1,  3], [ 2, -1,  2,  0], [-1,  3,  0,  2]],
L    = [[ 1, -3, -1, -2], [-3,  4, -2,  1], [ 0,  5,  1,  2], [ 5, -5,  2, -1]],
Vinv = [[ 1,  2,  1,  2], [ 2, -1,  2, -1], [ 0, -5,  1, -3], [-5,  5, -3,  4]],
```

with `L = (I - A_f)(I - A_f^2)`, `Vinv = 5 L^-1`, `det(L) = 25`, and
`H(L x) = 5 H(x)`. By Shared proof 2 of `FIELD-CONSERVATIVE-CHAIN-LAW`, an
integer wave vector `y = (a, b, c, d)` in `Z^4` lies in the image lattice
`L Z^4` if and only if

```text
a + 2 b = 0 (mod 5)    and    c + 2 d = 0 (mod 5).
```

Define the corresponding 25-element subspace of `F_5^4`:

```text
G_L = { u = (u0, u1, u2, u3) in F_5^4 : u0 + 2 u1 = 0 and u2 + 2 u3 = 0 mod 5 }.
```

## 2. Exact statements

### Proposition 1 (Cyclotomic shear identity and balanced gate census)

1. The divergence-free shear matrix `A_f` satisfies
   `I + A_f + A_f^2 + A_f^3 + A_f^4 = 0` and `A_f^5 = I` over `Z`. The integer
   matrix `J_f = I + A_f^2` satisfies `det(J_f) = 1`, `tr(J_f) = 3`, and has
   characteristic polynomial `X^4 - 3 X^3 + 4 X^2 - 2 X + 1 = Phi_5(X - 1)`.
2. A balanced vector `y = ell(u)` in `{-2, -1, 0, 1, 2}^4` lies in `L Z^4` if
   and only if `u` lies in `G_L`. Exactly 25 of the 625 balanced vectors lie
   in `L Z^4`.
3. On those 25 vectors, the exact integer preimage `x = Vinv y / 5` takes wave
   energies `h = H(x)` in `{0, 1, 2, 3, 4, 5, 7}` with multiplicities
   `(1, 8, 4, 4, 2, 4, 2)`:
   - `h = 0` (1 state): `y = (0, 0, 0, 0)`, `x = (0, 0, 0, 0)`.
   - `h = 1` (8 states):
     - four pure magnetic unit basis preimages `x = (0, 0, -1, 0)`,
       `(0, 0, 0, -1)`, `(0, 0, 0, 1)`, `(0, 0, 1, 0)` with balanced images
       `y = (1, 2, -1, -2)`, `(2, -1, -2, 1)`, `(-2, 1, 2, -1)`,
       `(-1, -2, 1, 2)` and mod-5 coordinates `(1, 2, 4, 3)`, `(2, 4, 3, 1)`,
       `(3, 1, 2, 4)`, `(4, 3, 1, 2)`;
     - four one-sided balanced vectors `y = (0, 0, 1, 2)`, `(0, 0, 2, -1)`,
       `(0, 0, -2, 1)`, `(0, 0, -1, -2)` with preimages `x = (1, 0, -1, 1)`,
       `(0, 1, 1, -2)`, `(0, -1, -1, 2)`, `(-1, 0, 1, -1)`.

### Proposition 2 (Invariance of G_L in the a-frame and defect role of r)

In the `a`-swapped piston coordinates `tilde_p = (p4, p1, p4p, p1p) = (u0, u1, u2, u3)`:

1. The native translation vectors `S_VEC = (2, 1, 2, 1)` and
   `C_D[:4] = (2, 1, 3, 4)` map to
   `a(S_VEC) = (1, 2, 1, 2)` in `G_L` and
   `a(C_D[:4]) = (1, 2, 4, 3)` in `G_L`, whose balanced lift is
   `(1, 2, -1, -2) = L (0, 0, -1, 0)^T`.
2. For every `x` with `tilde_p(x)` in `G_L` and every `(q, r)` in `F_5^2`:
   - `tilde_p(b(x)) = (-u2, -u3, -u0, -u1)` lies in `G_L`;
   - `tilde_p(d(x)) = tilde_p(e(x)) = (1 - u0, 2 - u1, 4 - u2, 3 - u3)` lies
     in `G_L`;
   - `tilde_p(c(x)) = (1 - u2 + r, 2 - u3, 1 - u0 - r, 2 - u1)` has gate
     residuals
     `((1 - u2 + r) + 2 (2 - u3), (1 - u0 - r) + 2 (2 - u1)) = (r, -r) mod 5`,
     and therefore lies in `G_L` if and only if `r = 0 mod 5`.

### Proposition 3 (All-zero native trajectory and t = 3 unit seed)

Let `x(t) = U^t(0, (0, 0, 0, 0, 0, 0))` be the origin-zero trajectory from the
all-zero state. Then `tilde_y(x(t))` lies in `L Z^4` for every `t >= 0`:

1. For `t = 0` and `t = 1`, `tilde_y(x(t)) = (0, 0, 0, 0)` with `h = 0`.
2. At `t = 2` (after `c` fires at `t = 1` with `r(1) = 0`),
   `tilde_y(x(2)) = (1, 2, 1, 2) = L (2, 0, -3, 2)^T` with `h = 5`.
3. At synchronization tick `t = 3` (entering the stable union `z in {1, 4}`),
   `x(3) = (0, 0, 1, 3, 1, 1)` gives
   `tilde_y(x(3)) = (0, 0, -2, 1) = L (0, -1, -1, 2)^T`, whose preimage
   `w_3 = (0, -1, -1, 2)` has exact unit wave energy `h = H(w_3) = 1` and raw
   field energy `H_raw(P tilde_y(x(3))) = 5`. Preparing cell 0 of
   `DEF-FIELD-WORK-RECORD-CHAIN` with `(R, 0, P tilde_y(x(3)), 0)` satisfies
   all hypotheses of `FIELD-CHAIN-FIRST-WORK` and `FIELD-LOCAL-WORK-RECORD`.
4. For all `t >= 3`, `tilde_y(x(t))` remains in the four-element dihedral
   orbit `{(0, 0, -2, 1), (2, -1, 0, 0), (-1, -2, -1, -2), (1, 2, 1, 2)}` in
   `L Z^4`, with preimage wave energies `h(t)` in `{1, 3, 5}` and positive
   reaction resource deltas `4 h(t) - 2` in `{+2, +10, +18}`.

### Proposition 4 (Five-payload origin-zero family in G_L)

A piston vector `p = (p1, p4, p1p, p4p)` in `G_L` satisfies `p1 = -2 p4 mod 5`
and `p1p = -2 p4p mod 5`, so its coordinate sum is
`p1 + p4 + p1p + p4p = -p4 - p4p mod 5`. The intersection of `G_L` with the
origin-zero condition `z(x) = 0` at `q = r = 0` is therefore the five-element
family

```text
x_lambda(0) = (-2 lambda, lambda, 2 lambda, -lambda, 0, 0) mod 5,   lambda in F_5.
```

Under unchanged `U`:

1. All five trajectories share identical `(z(t), q(t), r(t))` for all `t >= 0`,
   with `(z(1), q(1), r(1)) = (0, 0, 0)`, `(z(2), q(2), r(2)) = (2, 1, 0)`, and
   `(z(3), q(3), r(3)) = (1, 1, 1)`.
2. Because `a` fires at `t = 0`, `tilde_p(x_lambda(1)) = p_lambda(0)` lies in
   `G_L`; because `c` fires at `t = 1` with `r(1) = 0` and only `b, d, e` fire
   for `t >= 2`, `tilde_y(x_lambda(t))` lies in `L Z^4` for every `lambda` in
   `F_5` and every `t >= 1`.
3. At `t = 1`, `lambda = 0` gives `x_pre = (0, 0, 0, 0)` with `h = 0`
   (`4 h - 2 = -2 < 0`, rejected by gate `G` at `r_0 = 0`), while the four
   nonzero payloads `lambda = 1, 2, 3, 4` biject onto the four unit magnetic
   basis seeds `x_pre = (0, 0, 0, 1)`, `(0, 0, -1, 0)`, `(0, 0, 1, 0)`,
   `(0, 0, 0, -1)`, each with `h = 1` (`4 h - 2 = +2`).
4. Across `(t = 2, t = 3)`, the five payloads `lambda = 0, 1, 2, 3, 4` yield
   five pairwise distinct wave-energy pairs `(h(2), h(3))`:
   `(5, 1)`, `(2, 3)`, `(3, 5)`, `(1, 2)`, and `(3, 3)`.

## 3. Scope boundary

These identities are exact finite and integer algebra connecting the declared
constants of `U` and `DEF-FIELD-WORK-RECORD-CHAIN`. They do not prove that the
spatial chain graph, the matrices `C, D, K`, or the `G; A; B; F` schedule are
uniquely forced by `U` or `J`, and they supply no physical apparatus,
occurrence law, or layer lift.
