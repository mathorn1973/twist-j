# MODEL-SPACE LIFT OF THE LOCAL PRIME FACTOR

```text
STATUS: NON-CANONICAL incubation note
ISSUE:  #357
PUBLIC STATUS CHANGES: none
RH STATUS CHANGE: none
```

## 1. One prime as two one-dimensional model spaces

Let

```text
r=p^(-1/2),
b_r(z)=(z-r)/(1-rz).
```

The Hardy model space

```text
K_(b_r)=H^2(D) minus b_r H^2(D)
```

is one-dimensional. Its normalized reproducing kernel is

```text
k_r(z)=sqrt(1-r^2)/(1-rz).
```

For the coordinate inner function `z`,

```text
K_z = span{1},
k_0(z)=1.
```

On the unit circle,

```text
|k_r(e^(i theta))|^2
  =(1-r^2)/|1-r e^(i theta)|^2
  =P_r(theta),
```

where `P_r` is the Poisson kernel. Since the complete local Weil symbol was
already shown to be

```text
w_p(theta)=(log p)[1-P_r(theta)],
```

one has exactly

```text
w_p(theta)
  =(log p)[|k_0(e^(i theta))|^2-|k_r(e^(i theta))|^2].
```

Thus the finite-place Weil contribution is the difference of the boundary
kernel densities of the two rank-one model spaces associated to the inner
functions `z` and `b_r`.

**Status:** candidate-T.

## 2. Exact inertia of the model-space pair

Choose an orthonormal basis of the two-dimensional span so that

```text
k_r = sqrt(1-r^2) e_0 + r e_1,
e_0 = 1.
```

Let `P_0` and `P_r` be the rank-one orthogonal projections onto `K_z` and
`K_(b_r)`. Then

```text
trace(P_0-P_r)=0,
det(P_0-P_r)=-r^2,
spectrum(P_0-P_r)={+r,-r}.
```

Hence there is an exact rank-two model-space analogue of the local prime
obstruction: it is the relative position of two distinct one-dimensional
Hardy model spaces, and their projection difference is indefinite.

With `r=p^(-1/2)`, the exact local inertia scale is

```text
{+p^(-1/2), -p^(-1/2)}.
```

The diagonal density identity alone does not provide a congruence or unitary
map from the delayed Euler tower to `P_0-P_r`. Without that carrier map, this is
an independent model-space analogue, not a refinement or new proof of the
earlier Sylvester no-go.

**Status:** candidate-T.

## 3. Finite-prime inner-pair lift

For a finite prime set `F`, introduce one independent disk coordinate `z_p`
per prime and define on the polydisk

```text
Z_F(z)=product_(p in F) z_p,
B_F(z)=product_(p in F) b_(p^(-1/2))(z_p).
```

Both are inner functions on the product Hardy space. Restrict to the critical
scaling orbit

```text
z_p(xi)=p^(i xi).
```

Then exactly

```text
product_(p in F) rho_p(1/2+i xi)
  = Z_F(z(xi))/B_F(z(xi)).
```

The directional phase derivative along this orbit is

```text
d/dxi arg[Z_F/B_F]
 = sum_(p in F) (log p)[1-P_(p^(-1/2))(xi log p)],
```

which is the complete finite-place Weil symbol for the full Euler towers of
the primes in `F`.

Thus the finite-place signed **symbol** can be lifted one level up to a
quotient of two genuine inner channels. This is a finite-prime Hardy/Bohr
repackaging of the Euler-normalized balanced stabilization; no novelty over
the classical local-factor theory is claimed. It is not a lift of the frozen
strict-cutoff `q_A` or corrected `R_+,R_-` carrier, and no linear map from the
delayed tower is supplied.

**Status:** candidate-T for the exact algebraic lift.

## 4. Relation to the Connes disk

`CONNES-LOCAL-IDENTIFICATION.md` proves that, after unfolding the prime cylinder
through the conformal/exponential coordinate, the Connes--Consani Blaschke
product is exactly the lifted `b_r` up to the constant phase `-1`.

Therefore the rank-one model space above is the cylinder-level fundamental
cell of the same Hardy inner factor whose full pole orbit appears in their
global disk.

## 5. Strong sufficient gate, not an equivalence

For inner functions, a typed inclusion/divisibility relation can order the
corresponding model kernels. A future use must freeze which model space is
included in which, the projection orientation, and the quotient or transfer
map. With the orientation giving a positive projection difference, an exact
completed inclusion would be a sufficient route to a contractive compression.

This would be a **strong sufficient mechanism**, not an established equivalent
form of RH. The local prime pair itself fails the inclusion because the two
one-dimensional spaces are distinct, reproducing the local no-go.

The scientifically relevant question is whether the archimedean/prolate defect
can enlarge the positive side so that the completed semilocal graph becomes an
orthogonal compression of an isometric model-space transfer.

No such inclusion is claimed here. Under the frozen #357 breaker order, G6 is
blocked while G3 is undecided. This model-space comparison may be tested early
only under a separate lock as an independent carrier/no-go study.
