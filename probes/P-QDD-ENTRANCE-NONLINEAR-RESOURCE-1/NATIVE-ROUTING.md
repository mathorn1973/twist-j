# Exact entrance from affine routing and two actual native ticks

**PUBLIC; NON-CANONICAL; proof-first, result-exposed mathematical
construction. No physical realization or scientific execution is asserted
by this derivation.** The admitted comparison operations are arbitrary
invertible affine maps of the existing six-dimensional checkpoint over
`F5`, together with actual native selector steps at their indicated counter
values. There is no added register, inverse of the global native map,
source measurement, postselection, or supplied nonlinear `f` gate.

This mathematical operation family is specified independently as the whole
affine group, but the particular routing below was synthesized for the
desired entrance target. Its physical availability is not derived from
`U`. In particular, the affine routing maps are genuine additional
interventions and are not words in the native generators. They do not
satisfy the unchanged read-only architecture merely because the endpoint
agrees with an admitted target.

## 1. Objects and actual timing

All point coordinates and coefficients in this note are in `F5`, ordered
as `x=(a,b,c,d,q,r)`. Define `s=a+b+c+d`, `z=s+q+r` and

```text
Y_h=(h,0,0,0,1-h,0),                 h=1,2,3,4,
f(1)=1,                             f(2)=f(3)=f(4)=2,
C_3 Y_h=(h,0,0,0,1-h-f(h),f(h)).
```

The ascending order here is solely a convenient table order. It denotes
the same four endpoint basis vectors as the public order `(1,2,4,3)`.
LOW is `h=1`. HIGH is the span of the other three basis vectors.

Write `F_t(x)=g_(z(x)+2t mod 5)(x)` for one native checkpoint step,
where `t` is the actual driver bit, not the step duration. The generator
index order is `(a,b,c,d,e)`; these names do not denote coordinate values.
The actual Thue--Morse bits at counters three and four are

```text
theta_3=0,                         theta_4=1.
```

On the stable sheet `z=1`, `F_0` selects generator `b` and moves to
`z=4`; there `F_1` also selects `b`. Since `b^2=I`, the free two-tick
map satisfies

```text
N_(3,2) Y_h=Y_h,
N_(3,2) C_3 Y_h=C_3 Y_h.                                  (N1)
```

The second identity is valid because the entrance shift preserves `z`.
The elapsed-time comparison is therefore exactly `N_(3,2) C_3`, not an
entrance whose two native ticks were omitted from the clock account.

## 2. Two affine permutations

Define the entrance routing `A` by

```text
A(a,b,c,d,q,r)=(a,b,c,d,q+a+b+c+d+2,r).                    (N2)
```

Its inverse subtracts `a+b+c+d+2` from `q`. Define the inter-tick routing
`B` by

```text
B(a,b,c,d,q,r)=(
  a+b+3c+r+3,
  3a+3c+3r,
  4a+2r+3,
  4a+2c+d+r,
  q+4c,
  3a+3c+4r+3
).                                                        (N3)
```

For an output tuple `(A0,B0,C0,D0,Q0,R0)`, the following sequential
formulas give its unique preimage:

```text
r = R0-B0-3,
a = 4(C0-3-2r),
c = 2B0-a-r,
b = A0-3-a-3c-r,
d = D0-4a-2c-r,
q = Q0-4c.                                                (N4)
```

For example, the difference between the sixth and second outputs in
(N3) is `r+3`; the third output then determines `a`, since `4^-1=4`,
and the second determines `c`, since `3^-1=2`. The remaining three
formulas recover `b,d,q`. Thus both maps are globally invertible affine
maps of the original checkpoint space.

Their availability is an added comparison premise. In a fixed native
generator word, the new `r` depends only on the old `r`, and the new
`q` only on the old `q`. Map `A` violates the latter property, and map
`B`, whose sixth component contains `3a+3c`, violates the former. Neither
map is a fixed native generator word.

## 3. Complete four-point construction

The protocol is, chronologically,

```text
counter 3:       apply A;
native tick 3:   apply actual F_0;
counter 4:       apply B;
native tick 4:   apply actual F_1;
completion:     counter 5.
```

The routing operations occupy ideal comparison boundaries in this
mathematical model. No physical duration, energy, clock synchronization or
mechanism for either routing is supplied. The native counter is not
altered by the routing maps and advances exactly twice.

The first map gives `A Y_h=(h,0,0,0,3,0)`, whose trace is `h+3`.
Direct substitution into the public native formulas gives every
intermediate point:

| h | First selected generator | `F_0 A Y_h` | `B F_0 A Y_h` | Second selected generator |
| --- | --- | --- | --- | --- |
| 1 | e | `(1,1,3,4,4,1)` | `(0,0,4,0,1,4)` | b |
| 2 | a | `(0,2,0,0,3,0)` | `(0,0,3,0,3,3)` | b |
| 3 | b | `(0,0,2,0,2,0)` | `(4,1,3,4,0,4)` | d |
| 4 | c | `(2,1,3,1,3,0)` | `(0,0,1,0,0,3)` | b |

The traces before the second step are respectively `4,4,1,4`.
The actual bit is one, so the selector indices are respectively
`1,1,3,1`. The second step therefore gives

| h | `F_1 B F_0 A Y_h` | Required `C_3 Y_h` |
| --- | --- | --- |
| 1 | `(1,0,0,0,4,1)` | `(1,0,0,0,4,1)` |
| 2 | `(2,0,0,0,2,2)` | `(2,0,0,0,2,2)` |
| 3 | `(3,0,0,0,1,2)` | `(3,0,0,0,1,2)` |
| 4 | `(4,0,0,0,0,2)` | `(4,0,0,0,0,2)` |

Consequently

```text
F_1 B F_0 A |_(K_3) = N_(3,2) C_3 |_(K_3),              (N5)
K_3=span{|Y_h>:h=1,2,3,4}.
```

Here equality on the complex code is the free linear extension of the
pointwise identity, with coefficient `+1` on every basis transition.
There are four distinct points after every listed prefix. Thus every
prefix is isometric on this four-dimensional code, retains all relative
phases, and maps each of its sixteen matrix units to the corresponding
matrix unit. In particular it does not resolve the three HIGH labels
into an unlisted environment. There are no auxiliary degrees in this
construction to discard or restore.

This is not a global unitarity assertion for either native step. Native
`U` is not being inverted or silently replaced by a globally normalized
quantum channel. The mathematical comparison is confined to the stated
code and its actual intermediate supports. A physical interpretation
must separately supply a complete evolution and its full-state coherent
correspondence on that domain.

The source is allowed to change during the entrance: the intermediate
piston tuples in the table generally differ from their free trajectories.
Equation (N5) proves the correct completed entrance target and permits the
previously proved native holding theorem to start after completion. It
does not prove undisturbed source motion during the entrance itself.

## 4. No zero-tick affine construction

The four prepared points `Y_h` lie on one affine line with its indicated
parameter `h`. Any composition of invertible affine checkpoint maps
maps that line to one affine line.

In the target, the three HIGH points `h=2,3,4` remain an equally spaced
triple with common final port value `r=2`, while LOW has `r=1` and lies
off their affine line. An affine scalar function of `h` constant at
three distinct field elements is constant everywhere, so no affine map
alone has these four outputs. Applying a common free stable native word
to the target does not alter this distinction, because that word is an
invertible affine map on the relevant stable code.

## 5. No one-tick affine construction

Consider the complete class

```text
P_post F_t P_pre,
```

where both `P_pre` and `P_post` are arbitrary invertible affine maps of
`F5^6`, `t` is either bit value, and no additional coordinate is admitted.
The class includes any finite affine composition before or after the
single native step. On the prepared input line write

```text
x(h)=v+h u,
z(x(h))=beta+alpha h.
```

If `alpha=0`, the selected generator is common to all four inputs.
The whole operation is then affine on the line, and Section 4 applies.
Suppose henceforth `alpha!=0`.

The target HIGH outputs satisfy

```text
target(2)-2 target(3)+target(4)=0.                         (N6)
```

Any invertible affine post-map preserves this equality and its failure.
Therefore the three corresponding outputs of `F_t` must already satisfy
(N6). In particular their trace values must do so. The complete native
trace tables, in input trace order `0,1,2,3,4`, are

```text
tau_0=(0,4,0,4,4),
tau_1=(2,1,1,3,1).                                        (N7)
```

There are only twenty possible trace arrangements `(alpha,beta)` per
bit. Their exact classification needed here is

| t | alpha | beta | Generators on `h=2,3,4` | Remaining obstruction |
| --- | --- | --- | --- | --- |
| 0 | 2 | 0 | e,b,d | `r` second difference is 2 |
| 0 | 3 | 2 | d,b,e | `r` second difference is 2 |
| 1 | 2 | 3 | e,b,d | `r` second difference is 2 |
| 1 | 3 | 0 | d,b,e | `r` second difference is 2 |
| 1 | 2 | 4 | a,c,e | `ell` second difference is 4 |
| 1 | 3 | 1 | e,c,a | `ell` second difference is 4 |

These are exactly the arrangements for which the trace second
difference in (N6) vanishes. The classification follows directly from
(N7): for bit zero all three output traces must be equal, hence the
input traces are `{1,3,4}`, whose arithmetic-progression middle is `1`.
For bit one either all outputs equal `1`, requiring input traces
`{1,2,4}` with middle `4`, or the outputs are `1,2,3` in one of the two
orders. In the latter case the middle input trace is `0`, the trace
giving output `3` is `3`, and the opposite endpoint must be `2`.
No other repeated or distinct output triple from (N7) has zero second
difference in `F5`.

For the first four rows, all selected generators negate the affine
function `r(h)`. Their added constants are `(1,0,1)`, so

```text
r(F_t x(2))-2r(F_t x(3))+r(F_t x(4))=2 != 0.             (N8)
```

For the last two rows use the source functional

```text
ell(a,b,c,d,q,r)=-a+b-c+d.
```

The five public generator formulas give the single exact identity

```text
ell(g x)=-ell(x)+3*1_{g=c}.                              (N9)
```

The two occurrences of `r` in generator `c` cancel in this functional;
its constant is `-2+1-2+1=3`. The constants of `d,e` are zero.
Since `ell(x(h))` is affine and `c` occurs only at the middle HIGH
input, the second difference is

```text
3*(0-2+0) = 4 != 0.                                     (N10)
```

Every possible arrangement therefore contradicts (N6). This proves
the complete one-native-tick obstruction at the stated affine,
six-coordinate, no-auxiliary scope. It is independent of how the affine
pre-map distributes the input label among the six coordinates.

Combining Sections 3--5 gives an exact minimum of **two native ticks**
in this mathematical resource class: arbitrary invertible affine
interventions, the fixed four-point code, its prescribed coherent
entrance target, and no extra coordinate. The positive witness uses
the actual consecutive bits at counters three and four. The lower
bound covers either possible bit of a one-tick candidate.

## 6. Meaning and remaining physical obligation

The added maps (N2)--(N3) are affine over `F5`, while the native selector
is nonlinear on the whole checkpoint space. The construction proves that
this existing selector supplies enough nonlinear behavior for the
entrance once the stated affine routing operations are admitted. A
separately supplied nonlinear conditional-shift primitive is unnecessary
within this enlarged mathematical operation family.

This does not derive the affine interactions from the native architecture.
They mix source and port coordinates, move the trajectory through
nonstable traces during the entrance, and intervene in the checkpoint.
The underlying physical carrier, preparation, availability and time law of
these interactions, the physical meaning of the formal coherent code,
their controls and resources, and their complete environmental outputs
remain unprovided. The polynomial degree of a point map is not the degree
of a physical Hamiltonian or material response.

The construction is one launch-phase witness at `n=3`. No all-launch
physical control law is supplied. Routing between native ticks is an
explicit mathematical admission, not a proof that an actual device can
perform it instantaneously or with the required synchronized duration.
The archive, a realized exclusive event, ordered occurrence and repeated
preparation remain outside this entrance result.

The strongest justified consequence is therefore constructive and scoped:
**the missing entrance can be reduced to physical realization of specified
affine routing interactions plus the existing native steps.** It is not
necessary to posit the nonlinear entrance map itself as a primitive, but
the physical origin of those routing interactions is still a genuine
obligation.
