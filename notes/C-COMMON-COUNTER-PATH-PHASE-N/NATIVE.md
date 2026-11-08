<!-- SPDX-License-Identifier: Apache-2.0 -->

# Native U at a common counter

**NON-CANONICAL / L1.** A corollary of registered theorems with an exhaustive
exact audit. No new native theorem is claimed. Reservation:
[#1922](https://github.com/mathorn1973/twist-j/issues/1922).

## Registered inputs

All coordinates are in F5. The unchanged native update of Public Canon v109 is

```text
x=(p1,p4,p1p,p4p,q,r),   z(x)=p1+p4+p1p+p4p+q+r,   theta_n=s2(n) mod 2,
U(n,x)=(n+1,g_(z(x)+2 theta_n mod 5)(x)),   (g0,g1,g2,g3,g4)=(a,b,c,d,e),
```

with the counter started at zero. Three registered rows are used.

1. **U-NATIVE-APPARATUS-HISTORY-FACTOR [T].** The quotient `(z,q,r)` is closed
   and the selector depends only on `(z,theta_n)`:

   | Generator | New `(z,q,r)` |
   | --- | --- |
   | a | `(z,q,r)` |
   | b | `(-z,-q,-r)` |
   | c | `(2-z,1-q,-r)` |
   | d | `(2-z,1-q,1-r)` |
   | e | `(3-z,2-q,1-r)` |

2. **U-NATIVE-CHART-AND-QDD-READBACK [T].** For every `n>=3` the reachable
   sheet is `X_n={x:z(x)=4-3 theta_(n-1)}`. With

   ```text
   S(0)=0,  S(m)=m-S(floor(m/2)),
   t_n=(-1)^(n-3),  h_n=(-1)^(n+theta_(n-1)),  N_n=S(floor((n-1)/2))-1,
   ```

   the five labels

   ```text
   alpha=t_n(p1+p1p),    beta=t_n(p4+p4p),
   gamma=h_n(p1-p1p-2),  delta=h_n(p4-p4p-1),
   epsilon=t_n r-N_n
   ```

   form a bijection `X_n -> F5^5` and are constant along each synchronized
   native trajectory.

3. **U-NATIVE-WHOLE-SHEET-RETURN-WINDOWS [T]**, (WR-3) to (WR-5). On an
   uninterrupted origin-zero trajectory started in `X_1 union X_4` the
   occupied sheet has trace `4+2 theta_(n-1)` for every `n>=1`. With `h=0`
   on trace 1 and `h=1` on trace 4 the tick acts by
   `h'=1-theta_n`, `v'=-v`, `r'=-r+(h xor theta_n)`.

The integer lift of the fibre is the lift of
[#1915](https://github.com/mathorn1973/twist-j/pull/1915), extended to the
letters `a` and `c`: `rt_0=r_0` in `{0,...,4}` and `rt_(n+1)=eps*rt_n+kappa`
with `(eps,kappa)=(1,0)` for `a`, `(-1,0)` for `b` and `c`, `(-1,1)` for `d`
and `e`. It is a supplied arithmetic record of the registered fibre rule.

## Corollary

Let `x_n` and `x'_n` be two origin-zero trajectories and `3<=n0<n1`.

**(C1) The fibre is a conserved label plus a function of the counter.**
`r_n=t_n(epsilon+N_n)`. Hence

```text
r_n1-(-1)^(n1-n0) r_n0 = t_n1 (N_n1-N_n0)   in F5,
```

the same value for every trajectory.

**(C2) Two trajectories keep their fibre difference up to sign.**
`r_n-r'_n=t_n(epsilon-epsilon')`.

**(C3) The lifted shift over a window is one integer for all trajectories.**
For every tick `n>=3` the lifted rule is `rt_(n+1)=-rt_n+kappa_n` with one
integer for all trajectories,

```text
kappa_n = t_(n+1) (N_(n+1)-N_n):   kappa_n=0 for odd n,
                                   kappa_(2k)=S(k)-S(k-1)=e_k,   e_k=[v_2(k) even].
```

Hence over every window, of either parity,

```text
rt_n1-(-1)^(n1-n0) rt_n0 = t_n1 (N_n1-N_n0)   in the integers.
```

For even length `n1=n0+2m` this is

```text
+(S(k0+m-1)-S(k0-1))   for odd  n0=2k0-1,
-(S(k0+m-1)-S(k0-1))   for even n0=2k0.
```

On trajectories started in `X_1 union X_4` the same holds from `n>=1`.

**(C4) There is one piston course per piston cut.** The four pistons at
`n+1` are a bijective function of the four pistons at `n` and of the counter.
Two trajectories with equal pistons at one cut `n>=3` have equal pistons at
every cut `n>=3`.

**(C5) The only branching is in ticks 0, 1, 2, by the initial trace.** The
letter words are `ace`, `bbd`, `cce`, `dbd`, `ebd` for `z_0=0,1,2,3,4`, with
`r_3=r_0+1`, `1-r_0`, `1-r_0`, `2-r_0`, `2-r_0`. Every state of `X_3` has
exactly five origin preimages, one on each trace sheet. This is the
registered first-three-tick fibre.

**Proof.** (C1) and (C2) restate the conservation of `epsilon`.

(C3) On `X_n` the selector index `z+2 theta_n` is a function of the counter,
and on the traces 1 and 4 it selects `b,d` and `e,b`. So one letter of
`{b,d,e}` acts on the whole sheet, and the lifted rule is `rt'=-rt+kappa_n`
with one `kappa_n` in `{0,1}` for all trajectories. Reducing modulo 5 and
comparing with (C1) at `n` and `n+1` gives
`kappa_n=t_(n+1)(N_(n+1)-N_n)` in F5. The right side is an integer in
`{0,1}`: for odd `n` it vanishes because `N_(n+1)=N_n`, and for `n=2k` it is
`S(k)-S(k-1)`, which equals 1 for odd `k` and `1-(S(k/2)-S(k/2-1))` for even
`k`. That is the recursion of `e_k`. Two integers in `{0,1}` that agree
modulo 5 are equal. The window formula follows by summation, because
`t_n1 t_(i+1)=(-1)^(n1-1-i)`. On `X_1 union X_4` the ticks 1 and 2 use the
same letters by (WR-3) and (WR-4), with kicks 0 and 1, and
`N_1=N_2=-1`, `N_3=0` give the same formula.

Read pair by pair, this is the pair law of #1915: `+e_k` on the pair from
`2k-1` and `-e_k` on the pair from `2k`. It is stated there for trajectories
started in `X_1 union X_4`; from counter 3 it holds for every origin-zero
trajectory.

(C4) is the conservation of `alpha,beta,gamma,delta`, which involve only the
pistons and the counter. (C5) follows by evaluating the registered quotient
table on the driver bits `0,1,1`: the traces move by `0,4,0,4,4`, then
`0->2` and `4->1`, then `2->1` and `1->1`.

## Reading of the two windows of #1915

The matched ten-tick windows `1->11`, `11->21`, `21->31` have lifted shifts

```text
S(5)-S(0)=4,   S(10)-S(5)=2,   S(15)-S(10)=4.
```

#1915 states them as successive windows, and that is what they are: three
counter windows of one trajectory. The finite marks
`(n mod 5, theta_(n-1), theta_n)` agree at their cuts, but the shift is a
function of the full counter: among the odd starts `n0<4096` carrying the
marks `(1,0,1)`, the ten-tick shift takes the values 2, 3, 4 on 24, 102 and
104 starts. The lifted shift therefore reads counter bits that the finite
marks do not show. It is a further hand of the same clock.

At a common counter the two windows coincide. By (C3) any two trajectories
then have the same lifted shift, and by (C4) trajectories with a common final
piston state have had the same pistons throughout. A comparison of two paths
with a common end and a common counter has nothing to compare on this
carrier. Its null outcome is fixed by the registered chart, and it is not
evidence about carriers with state-dependent branching.

This agrees with the scope stated in #1915 itself: the character `j^r`, its
lift and the balance are L1 arithmetic readings, and an independently
realized path-work transfer is listed there as open.

## Exact audit

`recon_native_u_2026-11-06.py` enumerates all 15625 origin-zero heads through
counter 64. No falsifier fired.

| Clause | Audit |
| --- | --- |
| U1 | letter, new trace and fibre kick depend on `(z,theta_n)` only, all states and both bits |
| U2 | image sizes 6250, 6250, 3125 after ticks 1, 2, 3; full sheet and bijection for `3<=n<=64` |
| U3 | one letter per tick; one affine map with linear part `-P` (for `b`) or `-I` (for `d`, `e`); one lifted shift on all 15625 trajectories for each of 1891 windows |
| U4 | pistons at `n+1` are a bijective function of pistons at `n` |
| U5 | five origin preimages per state of `X_3`, one per trace sheet; the five words and fibre maps |
| U6 | closed form on every even window with `n1<=64`: all states for `n0>=3`, `X_1 union X_4` for `n0>=1` (992 windows); the values `+4,+2,+4,+10,-10` of #1915 |
| U7 | census of ten-tick shifts over odd starts below 4096 |

The breaker (`break_recon_parts_u_k_2026-11-06.py`, part B-U) composes the
five generators as affine maps without enumerating states. It extends the
one-letter and fibre-row statements to every counter below 4096, and the
closed form to every even window from counter 3 in that range, hence to
every even window with an odd start.

`check_tick_law_2026-11-06.py` was written while this note was prepared. It
follows fifty heads, ten on each initial trace sheet, to counter 4096 and
checks the tick law of (C3) as an integer identity at every tick, and the
window formula for both parities on all windows with `n1<=300`.

## Limits

Unchanged origin-zero U only. Nothing is said about an added carrier, a
contact, a controller, or an admission that supplies sheets after the origin.
No physical phase, time or action reading is attached to the fibre.
