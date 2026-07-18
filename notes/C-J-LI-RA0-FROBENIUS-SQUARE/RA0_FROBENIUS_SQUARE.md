# C-J-LI-RA0-FROBENIUS-SQUARE: first route-RA parent and its exact kill

```text
STATUS:       RECON, FIRED. NON-CANONICAL.
AUTHORITY:    none.
PUBLIC CLAIM: none; no registry row, Canon edit, issue, or probe.
BASIS:        Public Canon v8 at d94d4a94976a9b5d27db3a1c586e4886697daabb;
              notes/j-li-q-moment-n2 at
              4845f4af44b01eecee423864feff55f627db11c4.
READ-ONLY:    public main bbe751090ef1b832c7674746b140d0a7a8d83570 was
              checked; its STATUS declares Public Canon v9. It is not a
              scientific basis, no v9 content is imported, and no status is
              lifted here.
MACHINE:      NOT RUN. PRE_FREEZE only; no PIN/EXPECTED/RUN record exists.
SCOPE:        the minimal Frobenius/Euler positive-square route RA0 only.
RH:           open. A fired construction is not evidence against RH.
```

## 1. Result first

The first explicit route-RA proposal does not survive.  It is useful because
it separates three objects that had previously been compressed into the word
"relative":

1. an analytic Euler determinant family in the trivial `C4` sector;
2. a Hurwitz-number-operator relative block for the Gamma factor;
3. a fixed positive trace-class operator in the `w` chart.

The first two repackage the known completion but do not produce the third.
The most economical positive extraction from the Euler channel is

```text
A_RA0 = diag_p(p^-2).
```

Strictly, its prime-mode carrier fails `G0/G7`: the current project has no
theorem-grade primitive-output bridge that constructs the rational-prime
index set from an all-ideal `J` object.  The existing phrase "primes are
outputs of the step" is diagnostic, not a closed construction theorem.

Even if that missing bridge is granted provisionally, RA0 is killed exactly
by the first moment gate.  For

```text
B_RA0 = A_RA0 (I + A_RA0/4)^(-1)
```

the single atom `p=2` gives

```text
Tr(B_RA0) >= b_2 = 4/17
                    > 3/125
                    > 23095708972138893 / 10^18
                    = upper(lambda_1).
```

Thus `K1` fires without a prime table, a zero list, a floating-point
evaluation, or an infinite sum.  Adding positive pole or archimedean blocks
by direct sum can only increase the trace and cannot repair the miss.

The construction is therefore frozen as `RA0-FROBENIUS-SQUARE [FIRED]`, not
as a candidate `A_J`.

## 2. Frozen dependency audit

The intended graph was

```text
J
 -> Z[J] = Z[zeta_5]
 -> monoid of finite-index J-invariant sublattices
 -> nonzero ideals of Z[zeta_5]
 -> primitive ideal atoms and C4/Frobenius orbits       [MISSING BRIDGE]
 -> rational trivial-sector atoms p
 -> H_tr and K_J = diag_p(p^-1)
 -> A_RA0 = K_J* K_J.
```

The invariant-sublattice/ideal identity exists at candidate grade in
`C-WEIL-REALIZATION-1`.  It does not by itself construct the primitive
projector, its Hilbert completion, or the rational trivial-sector
multiplicity.  Defining `H_tr` literally as `l2(primes)` would put primes in
the carrier definition and violates the current `G7` rule.  Using
`P_0/f_5=zeta` and then reading its Euler product does not fix this: it is an
alias of the target arithmetic factor, not a new `J`-native lift.

Consequently the strict gate order is

```text
G0  FIRED: primitive-output bridge absent.
G1  conditional definition below, not an independently closed gate.
G2  PASS if the missing G0 bridge is provisionally granted.
G3  HOLD: the Euler and Gamma families do not supply a fixed positive A_J.
G7  FIRED: the rational-prime carrier is target arithmetic unless the same
    missing primitive-output bridge is supplied from the J-only carrier.
K1  FIRED exactly for the conditional positive square.
```

The conditional calculation is still worth retaining: any later bridge that
lands on this same prime square is dead before expensive work begins.

The bounded checks `R01` and `R02` in the companion machine file are only
regressions of encoded normalization identities.  They do not close the
missing `G0/G7` bridge or prove the analytic continuation used below.

## 3. Conditional `C4` Euler parent

Let `K=Q(zeta_5)` and `G=Gal(K/Q)=C4`.  If a primitive-output bridge is
granted, put

```text
H_full = direct_sum_(p != 5) C[G]  direct_sum  C e_5.
```

Right translation gives the `C4` action.  On the `p` block, left
multiplication by `g_p = p mod 5` gives Frobenius; the ramified place `p=5`
has its separately named one-dimensional inertia-invariant line.  With

```text
P_tr = (1/4) sum_(g in G) U_g,
```

the trivial sector is one-dimensional in every unramified regular block.
For `Re(s)>1`,

```text
T_full(s) = direct_sum_(p != 5) p^-s F_p  direct_sum  5^-s,
T_tr(s)   = P_tr T_full(s) P_tr = diag_p(p^-s).
```

The local determinant of a regular `C4` block is

```text
det(I - x F_p) = (1 - x^d)^(4/d),
d = ord_C4(g_p),
```

whereas its trivial-sector determinant is `1-x`.  Therefore, conditionally,

```text
det_1(I - T_tr(s))^-1 = product_p (1-p^-s)^-1.
```

On `Re(s)>1` the public root-filter normalization identifies the last
product with `Z_J=P_0/f_5=zeta`.

Two local statements must not be conflated:

- the inertia-invariant line supplies the multiplicative local factor
  `(1-5^-s)^-1`;
- independently, `+f_5'/f_5` cancels the counterfeit additive `5^m` tower
  in `-P_0'/P_0`.

They occupy the same place in the bookkeeping but are not the same local
identity.

## 4. The archimedean pair is relative but not positive

On `H_inf=l2(N_0)`, let `N e_n=n e_n`.  The pair

```text
(N+1, N+s/2),       common domain Dom(N),
```

has trace-class resolvent difference away from its poles, since its diagonal
terms are `O(n^-2)`.  Its zeta-regularized quotient gives the standard
Hurwitz identity

```text
det_zeta(N+1) / det_zeta(N+s/2) = Gamma(s/2).
```

Together with the scalar factors `pi^(-s/2)` and `s(s-1)/2`, this packages
the standard completion.  It does not produce a self-adjoint positive
trace-class `A_J`: on `s=1/2+it`, `T_tr(s)` is not even Hilbert-Schmidt,
because its squared singular values sum to `sum_p 1/p`, and `N+s/2` is not
self-adjoint.  Scalar analytic continuation does not create positivity.

This is the precise type mismatch that the old route label concealed.

## 5. Minimal positive square and exact kill

The pole anchor selects the boundary operator

```text
K_RA0 = T_tr(1) = diag_p(p^-1).
```

Conditionally on the carrier bridge, classical Euler estimates give, as a
proof-first import rather than a machine result,

```text
K_RA0 in S2 but not S1.
```

Among positive integer powers of `abs(K_RA0)`, the square is the unique
minimal choice with the frozen boundary:

```text
A_RA0 = K_RA0* K_RA0 = diag_p(p^-2) in S1,
sqrt(A_RA0) not in S1.
```

The ordinary trace-class Schur parent is

```text
L_0(t)=I,
L_1(t)=I-t^2 A_RA0,
det_rel(L_1,L_0)=det_1(I-t^2 A_RA0).
```

It is a valid determinant, but not the completed `Xi_J` determinant.  More
decisively, transport to the frozen `w` chart gives

```text
b_p = (p^-2)/(1+p^-2/4) = 4/(4p^2+1).
```

The `p=2` atom alone yields the exact `K1` contradiction in section 1.  No
constant rescaling is allowed by `K0`; in any event a scale cannot repair the
counting law.  By the prime number theorem,

```text
N_B(epsilon)
  = pi(sqrt(epsilon^-1 - 1/4))
  ~ 2 epsilon^-1/2 / log(1/epsilon),
```

while the forced Riemann-von Mangoldt target is

```text
(1/(4 pi)) epsilon^-1/2 log(1/epsilon)
```

at leading order.  The mismatch is of order `log(1/epsilon)^2` (`K4`).

## 6. Two structural lemmas retained

### 6.1 Positive trace-class quotient collapse

Let `A_0,A_1>=0` be trace class and suppose

```text
F(z)=det_1(I-z A_1)/det_1(I-z A_0)
```

extends to an entire function.  At every positive eigenvalue `lambda`,
entireness forces the multiplicity in `A_1` to dominate that in `A_0`.
Cancel the common spectral multiset.  The residual multiset is trace class,
and absolute genus-zero products give

```text
F(z)=det_1(I-z A_R)
```

for a positive trace-class residual `A_R`.  Thus an `A`-level quotient of
positive trace-class parents does not create positivity; after cancellation
it is the ordinary positive Fredholm problem again.  This lemma does not
apply to unbounded parents having only trace-class resolvent difference.

### 6.2 Coupled-block normal form

For a genuine coupling `K:H_a -> H_inf` with `K in S2` but `K not in S1`,
put `A=K K*`.  Then

```text
A in S1,       sqrt(A) not in S1,
```

and, with the positive-frequency multiplicity fixed,

```text
det_2( [ I    t K* ] ) = det_1(I-t^2 K K*).
       [ t K  I    ]
```

The full off-diagonal perturbation is `S2`, not `S1`; the trace-class object
is its Schur complement.  In the exact finite model, if `C(t)` denotes the
off-diagonal perturbation, then `Tr(C(t))=0`; hence
`det_2(I+C(t))=det(I+C(t)) exp(-Tr(C(t)))=det(I+C(t))`, and the ordinary
Schur-complement identity gives the displayed polynomial.  This is the
correct coupled architecture for the frozen Schatten boundary.  The machine
file only encodes that finite algebra.  It is not an infinite construction,
and its infinite operator-ideal statement remains proof-first.

## 7. Scoped no-go map

The following routes are now separated cleanly:

```text
positive S1 / positive S1 quotient
    -> collapses to an ordinary residual A; no shortcut.

unitary/Cayley ordinary relative det_1
    -> wrong ideal: the Li defect is S2 but not S1.

finite-periodic direct occupation on levels log n
    -> counting is exponential or O(T), never T log T.

prime Frobenius square RA0
    -> strict G0/G7 gap; conditionally K1 and K4 fire.

unbounded parents with trace-class resolvent difference
    -> not killed; this is the surviving route-RA class.
```

The modular Lax-Phillips construction is a useful blueprint for the last
line, but it imports the modular surface, cusp, Eisenstein series, and a
non-self-adjoint resonance generator.  Its determinants are superzeta-
regularized, not the required ordinary positive Fredholm determinant.  It is
therefore not a `J`-native construction.

## 8. Next constructive target

The next proposal must define, before any comparison with `lambda_1`, an
explicit `C4`-intertwining kernel

```text
K_J : H_arithmetic -> H_infinity,
```

directly from an all-ideal or all-sublattice `J` carrier, with

```text
K_J in S2 but not S1,       A_J=K_J K_J*.
```

The arithmetic and archimedean channels must be coupled before the positive
square.  A prime projector, Gamma factor, spectral shift, or inverse
scattering datum may not be inserted as target data.  The first cheap gates
are:

```text
C0  primitive arithmetic is an output of the all-ideal carrier;
C1  common domains, C4 intertwining, and the kernel are explicit;
C2  S2\S1 is proved from the kernel itself;
C3  q_w,0 is derived and meets the frozen lambda_1 interval.
```

Until such a kernel exists, route RA remains open at the unbounded coupled
parent level and closed for RA0 only.
