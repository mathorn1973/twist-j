# A 64-block realization of the same retained-memory native step

**NON-CANONICAL, candidate-T conditional ideal-model construction; L1.**
Reservation: [#1370](https://github.com/mathorn1973/twist-j/issues/1370).
This is an analytical candidate disclosed before execution, not a run
result. The physical model is [MODEL.md](MODEL.md); the chronological
recipe is [PROGRAM.json](PROGRAM.json). Public authority remains Canon
v97. The physical HOLD and the scopes of the sealed predecessors remain
unchanged. The construction uses exactly the original 500-loop block,
without frame cancellation, frame reordering or further compression.

The sources are pinned in [SOURCES.md](SOURCES.md). The all-ion equality
phase is inherited from #1369, and the embedded exchange identity is
adapted algebraically from #1365. The two-ion physical isolation premise
of #1365 is not imported into this seventeen-ion model.

## 1. Fixed carrier, inputs and complete target

The seventeen five-level factors, in their physical index order, are

```text
0:S1, 1:S2,
2:R1.p1, 3:R1.p4, 4:R1.p1p, 5:R1.p4p, 6:R1.q, 7:R1.r,
8:R2.p1, 9:R2.p4, 10:R2.p1p, 11:R2.p4p, 12:R2.y, 13:R2.r,
14:M1, 15:M2, 16:N.
```

All displayed labels are direct except the retained preparation-time
dictionary `R2.y=R2.q+4 mod5`. The supplied input vectors are

```text
I(s,t): S1=1, S2=t, R1=(0,0,0,0,s,0), R2=(0,0,0,0,0,0),
        M1=0, M2=0, N=0,                         s,t in F5.
```

Memory and counter are counted factors prepared before the supplied
boundary, not resources introduced or reset during this step. The target
is the same complete internal output as #1369:

```text
O(s,t): S1=1, S2=t, R1=f(s), R2=(0,0,0,0,3,0),
        M1=s, M2=1, N=1.
```

| s | Actual R1 selector | f(s), ordered (p1,p4,p1p,p4p,q,r) |
| ---: | --- | --- |
| 0 | a | (0,0,0,0,0,0) |
| 1 | b | (0,0,0,0,4,0) |
| 2 | c | (2,1,2,1,4,0) |
| 3 | d | (2,1,3,4,3,1) |
| 4 | e | (2,1,3,4,3,1) |

The source law is [Canon v97](https://github.com/mathorn1973/twist-j/blob/82ecf0aac0ee79c947000968e71573d4c65d386d/canon/CANON.md),
sections 2 and 3, at the declared content commit. For
`x=(p1,p4,p1p,p4p,q,r)`, all checkpoint arithmetic is modulo five:

```text
theta_n=popcount(n) mod2,
selector(n,x)=p1+p4+p1p+p4p+q+r+2theta_n mod5,
U(n,x)=(n+1,g_selector(n,x)(x)),
(g_0,g_1,g_2,g_3,g_4)=(a,b,c,d,e),
a(x)=(p4,p1,p4p,p1p,q,r),
b(x)=(-p1p,-p4p,-p1,-p4,-q,-r),
c(x)=(2-p1p,1-p4p+r,2-p1,1-p4-r,1-q,-r),
d(x)=(2-p1,1-p4,3-p1p,4-p4p,1-q,1-r),
e(x)=(2-p1,1-p4,3-p1p,4-p4p,2-q,1-r).
```

At n=0, theta_0=0 and the R1 input selects precisely s. Substitution
of `(0,0,0,0,s,0)` into g_s gives every row of f(s) above. For R2 the
fixed dictionary K sends q to y=q+4; its physical generator is
`K g_j K^-1` and its selector is

```text
selector_R2(n,P,y,r)=sum(P)+y+r+1+2theta_n mod5.
```

Thus R2's zero physical input selects 1 and its conjugated b sends
`(P,y,r)` to `(-p1p,-p4p,-p1,-p4,3-y,-r)`, giving the required y=3.
The mathematical law's unbounded n is a logical source definition; this
physical probe supplies only the counted finite N transition 0 to 1.
M1 distinguishes the equal data rows 3 and 4. No input-dependent program
selection or postselection is admitted.

Write the allowed individual carrier as

```text
R_(i;0,k)(theta,phi)
 = exp[-i theta (exp(-i phi)|0><k|+exp(i phi)|k><0|)_i/2],
Ry_(i;0,k)(theta)=R_(i;0,k)(theta,pi/2),
Rx_(i;0,k)(theta)=R_(i;0,k)(theta,0),          k=1,2,3,4.
```

It is identity on all other levels and all other ions. A negative angle
uses positive duration and carrier phase increased by pi. Inverses of
words reverse their chronological order and use the true adjoints.

## 2. The unchanged 500-loop equality block

For the fixed real nonscalar profile `D=diag(d_0,...,d_4)`, put

```text
S=sum_j d_j, Q=sum_j d_j^2, B=5Q-S^2>0,
A=sum_(i=0)^16 c_i D_i,
g_(i,j)=Re(c_i conjugate(c_j)),
tau=2pi/delta, K=pi eta^2/(2 delta^2).
```

The independently admitted parameters satisfy `eta>0`, `delta>0` and,
on the six required edges `e={14,k}`, `k=2,...,7`,

```text
g_e != 0,
lambda_e=delta/[eta sqrt(50 B abs(g_e))] <= lambda_max.
```

At this intensity the completed global force loop is

```text
L_e=exp[-i K lambda_e^2 A A^dagger-i sum_i L_(i,e)]
    tensor I_motion.
```

Here the `L_(i,e)` are fixed integrated diagonal residual local profiles
for one loop. The motion identity follows directly from the harmonic
force displacement at `tau`, with no oscillator cutoff or fresh-motion
assumption. All seventeen ions are illuminated; e selects an intensity
and a refocusing schedule, not a pair-selective beam.

For each edge assign direction `(1,0,0)` in `F5^3` to both active ions.
List the 31 vectors whose first nonzero coordinate is 1 in lexicographic
order, remove `(1,0,0)`, and assign the first fifteen remaining vectors
to the spectators in ascending physical index order. For each of the
500 pairs `(a,u)`, lexicographically ordered with `a=1,2,3,4` and
`u in F5^3`, apply the seventeen monomial frames with permutations

```text
p_i(x)=a x+v_i dot u mod5,
```

then one completed `L_e`, then the true adjoint of the complete frame.
Within a frame apply ions in ascending order and undo the complete word
in reverse order. The compiler is fixed in section 3.

These conjugated endpoints are diagonal and commute. The finite sums
for every complete internal basis input are

```text
sum_(a,u) d_(p_i(x))^2 = 100Q,
sum_(a,u) L_(i,e)(p_i(x)) = 100 Tr L_(i,e),
sum_(a,u) d_(p_i(x)) d_(p_j(y)) = 20 S^2
                                      for distinct directions.
```

On the active pair the last sum is `100Q` for equal labels and
`25(S^2-Q)` for unequal labels. Distinct projective directions have rank
two as linear forms in u, giving the independent-offset identity; on the
active pair each affine map occurs 25 times and is sharply two-transitive.
Consequently, with `E_e=sum_x |xx><xx|` on the selected pair,

```text
sum_(a,u) (A A^dagger)_(p(a,u)) = C_e I+50 B g_e E_e,
C_e=100Q sum_i abs(c_i)^2
    +40S^2 sum_(i<j) g_(i,j)-10 B g_e.
```

The unchanged raw block is therefore exactly

```text
G_e=gamma_e Q_e tensor I_motion,
Q_e=exp[-i sigma_e pi E_e/2], sigma_e=sign(g_e),
gamma_e=exp[-i K lambda_e^2 C_e-i100 sum_i Tr L_(i,e)].
```

E_e is tensored with identity on all other internal factors. Every
spectator contribution is scalar, including on superposed or correlated
spectators. The normalized notation records that scalar; it does not
insert a physical scalar-correction gate. Define also

```text
Z_e=Q_e^2=I-2E_e.
```

Every Z below denotes two actual G blocks and carries raw scalar
`gamma_e^2`. Nothing changes the 500-loop framing or its order.

## 3. Frozen monomial compiler and phases

On a named ion use `T_j=Rx_(0,j)(pi)`. Its underlying permutation is
`(0,j)`, and its action on both exchanged basis labels includes `-i`.
Its true adjoint is `R_(0,j)(pi,pi)`, not another phase-zero pi pulse.
For a permutation, use disjoint forward cycles, beginning each cycle
at its smallest element and ordering cycles by that element. The
chronological star lists are

```text
(0,a1,...,aL)                  -> a1,...,aL;
(a1,...,aL), 0 absent, L>=2   -> a1,...,aL,a1;
singleton                     -> empty list.
```

Following each label gives the declared permutation. All accumulated
monomial phases remain in the actual operator. They cancel when that
operator and its true adjoint conjugate a diagonal profile; no phase-free
permutation is substituted for the physical word.

Any five-label permutation needs at most six star pi pulses under these
rules. If zero is fixed, cycles of length l cost l+1 and at most two
nontrivial cycles fit into the other four labels. If zero is in a cycle,
its cycle costs one fewer than its length and the remaining cycles do
not exceed the same bound. For the twenty affine maps the lengths sum to
72: nonidentity translations contribute 16, the five reflections 22,
and each multiplier 2 and 3 contributes 17. Each affine map occurs
25 times at each ion in a G block. Thus each unchanged G uses exactly

```text
17*25*2*72=61200 individual star pi pulses.
```

All additional rotations below are themselves star rotations. No direct
D-to-D rotation, arbitrary one-ion unitary or controlled gate is added
to the physical primitive set.

## 4. Twelve blocks transfer q into retained memory

Fix `j in {1,2,3,4}` on the active physical edge `{6,14}`. Write

```text
J_j=|0><0|+|j><j|,
X=|0><j|+|j><0|,
Y=-i|0><j|+i|j><0|,
Z=|0><0|-|j><j|,
E_out=sum_(k notin {0,j}) |kk><kk|.
```

The Pauli operators vanish off their two-level support. Use the same
rotation on the two active ions, implemented as separate addressed
pulses, with

```text
Vx=Ry_(0,j)(pi/2), Vy=Rx_(0,j)(pi/2).
```

Then the three conjugated equality projectors are

```text
E_z=(J_j tensor J_j+Z tensor Z)/2+E_out,
E_x=(J_j tensor J_j+X tensor X)/2+E_out,
E_y=(J_j tensor J_j+Y tensor Y)/2+E_out.
```

Vx sends Z to X; Vy sends Z to -Y and that sign disappears in the
two-ion product. These three E operators commute on the complete pair
space: XX, YY and ZZ commute on the pair square, all three coincide on
the outside-equal sector, and they vanish on the remaining sectors.
On the pair square their sum is `I+P_j`, where P_j exchanges its factors.
The symmetric and antisymmetric eigenvalues are respectively 2 and 0.
For either sign `sigma=sign(g_(6,14))`, the normalized triple therefore
has the following complete action:

| Pair-input sector | B_j=exp[-i sigma pi(E_z+E_x+E_y)/2] |
| --- | --- |
| Both labels in {0,j} | Minus the two-level exchange P_j |
| Exactly one label in {0,j} | Identity |
| Equal labels k,k outside {0,j} | Phase i sigma |
| Unequal labels both outside {0,j} | Identity |

The outside-equal phase is retained; B_j is not a full five-level SWAP.
The raw chronological recipe is

```text
G_(6,14);
Vx^dagger on 6, then on 14; G_(6,14); Vx on 6, then on 14;
Vy^dagger on 6, then on 14; G_(6,14); Vy on 6, then on 14.
```

Its raw operator is `gamma_(6,14)^3 B_j`. The chronological axis frames
always act on the first named ion and then the second, exactly as shown.
The algebraic adjoint of a complete expanded word reverses every
primitive globally. Each G finishes every LS loop before any axis change.
Each B_j needs eight additional
individual star pulses, all of absolute angle pi/2.

Execute these four raw triples in order `j=1,2,3,4`. On `|s,0>`, s nonzero,
all triples before j=s see exactly one label inside their pair. The j=s
triple gives `-|0,s>`, and the subsequent triples again see exactly one
inside label. No outside-equal phase is visited. On `|0,0>` all four
triples contribute minus one. Thus the transfer is exactly

```text
|s,0> -> -gamma_(6,14)^12 |0,s>, s!=0;
|0,0> ->  gamma_(6,14)^12 |0,0>.
```

R1 is now zero and M1=s. The cost is twelve G blocks and thirty-two
additional pi/2 carrier pulses. This proof applies by linearity to the
entire five-dimensional ready-memory input subspace and its correlations.

## 5. Pair-mask and singleton controls, with arbitrary beta

Let A be a sorted two-element set of control labels and let `(0,k)` be
the target star pair. Define the permutation P_A by mapping the two
sorted members of A to `(0,k)`, in that order, and the three remaining
control labels in ascending order to the three remaining target labels
in ascending order. Use section 3's actual monomial word and adjoint.
The chronological mask word is

```text
P_A on control;
G_e; G_e; Ry_target(-beta); G_e; G_e; Ry_target(+beta);
P_A^dagger on control.
```

Its raw scalar is `gamma_e^4`. After normalization it is

```text
C_A(Ry_(0,k)(2 beta)),
```

for every beta used here, including negative beta. To prove this as a
complete operator, condition on a control basis label after P_A. For
labels 0 and k the two Z factors restrict to either sign of Pauli Z on
the target pair, and `Z Ry(-beta) Z=Ry(+beta)`. For the other labels Z
commutes with the target rotation, so the two rotations cancel. Outside
the target pair the rotations are identity and the two Z factors cancel.
The monomial phases in P_A cancel because the intervening normalized
operator is diagonal in the control label. This establishes all 25
pair-input columns, including initially occupied other target levels.

For the singleton label a, take b and c to be the two smallest labels
different from a. Execute the three masks

```text
{a,b}, beta=+pi/4;
{a,c}, beta=+pi/4;
{b,c}, beta=-pi/4.
```

Their rotations share an axis and their control projectors satisfy
`(P_a+P_b)+(P_a+P_c)-(P_b+P_c)=2P_a`. The normalized result is therefore
the singleton-controlled `Ry_(0,k)(pi)`, with raw scalar `gamma_e^12`.
Each pair mask costs four G blocks and at most fourteen extra carrier
pulses: two frame words of at most six pulses and two target rotations.
Each singleton costs twelve G blocks and at most forty-two extra pulses.

## 6. The fixed 52-block output recipe

After section 4, execute these operations in the exact displayed order.
The two complement constructions explicitly perform their unconditional
rotation first, then the cancelling mask. All masks leave M1 unchanged.

| Physical target | Chronological normalized operations | G count |
| --- | --- | ---: |
| 2: R1.p1 | Ry_(0,2)(pi); mask {0,1}, beta=-pi/2 | 4 |
| 3: R1.p4 | Ry_(0,1)(pi); mask {0,1}, beta=-pi/2 | 4 |
| 4: R1.p1p | singleton 2 on (0,2); mask {3,4} on (0,3), beta=pi/2 | 16 |
| 5: R1.p4p | singleton 2 on (0,1); mask {3,4} on (0,4), beta=pi/2 | 16 |
| 6: R1.q | mask {1,2} on (0,4), beta=pi/2; mask {3,4} on (0,3), beta=pi/2 | 8 |
| 7: R1.r | mask {3,4} on (0,1), beta=pi/2 | 4 |

For the first two rows, control labels 0 or 1 cause `Ry(-pi)Ry(pi)=I`,
and other labels cause `Ry(pi)`. Thus their effective condition is the
three-element set `{2,3,4}`, without a new three-value control primitive.
For the two primed coordinates the two predicates are disjoint. The two
q predicates are also disjoint. Although rotations on different target
pairs need not commute in general, at each fixed memory label at most
one such rotation is active. Every active positive-angle write sees
target level zero and maps it to the declared label with amplitude +1.
These statements produce exactly the table f(s), with no relative signs.

There are seven top-level pair masks and two singleton controls, so
their total is `7*4+2*12=52` G blocks. This count does not call each of
the six masks internal to singleton synthesis another top-level mask.

Next apply `Rx_(14;0,j)(2pi)` for j=1,2,3,4. Their product is

```text
D0=diag(+1,-1,-1,-1,-1)
```

on M1. It cancels the transfer sign, while leaving its value s intact.
Finally perform, chronologically,

```text
Ry_(12;0,3)(pi), Ry_(15;0,1)(pi), Ry_(16;0,1)(pi).
```

These set R2.y, M2 and N from 0 to 3,1,1 with positive amplitudes. The
full raw word W consequently satisfies

```text
W |I(s,t)> = Gamma_new |O(s,t)>,                 all s,t in F5,
Gamma_new = gamma_(14,2)^4 gamma_(14,3)^4
            gamma_(14,4)^16 gamma_(14,5)^16
            gamma_(14,6)^20 gamma_(14,7)^4.
```

The exponent 20 on the q-memory edge includes twelve transfer blocks
and eight q-output blocks. The six exponents sum to 64 and the scalar
is independent of s and t. The identity extends to the complete input
span and to entanglement with a reference. The normalized map agrees
with #1369 on that span; its raw scalar and laboratory duration are new.

PROGRAM.json encodes exactly this chronology. Its carrier angle field
and mask beta field use units pi/4. An exchange entry is the triple in
section 4; a singleton entry gives the control label after its target
pair label and expands by section 5. Negative pulse areas are implemented
by the positive-duration phase convention of section 1.

## 7. Forward resource, time and incident-energy bounds

The exact structural counts are

```text
N_G=12+52=64,
N_LS=64*500=32000,
n_G({14,k}), k=2,3,4,5,6,7: 4,4,16,16,20,4.
```

All frame words around every original LS loop remain present. A
conservative upper bound, using six star pulses per control permutation,
is

```text
N_carrier <= 64*61200 +32 +7*14 +2*42 +2+4+3
          =3917023.
```

Here the successive additions are transfer axis rotations, top-level
masks, singleton controls, unconditional writes, memory correction and
fixed final preparations. This is a pre-execution analytical upper
bound; it is not represented as an exact compiler count.

The total absolute carrier angle has the sharper corresponding bound

```text
A_carrier/pi <=64*61200 +16 +7*(12+1)+2*(36+6/4)+2+8+3
             =3916995.
```

The seven top-level masks have `abs(beta)=pi/2`, while each singleton's
six target rotations have absolute angle pi/4. These are forward-word
resources; algebraic adjoints in the audit do not double this account.

With serial addressed pulses and independently admitted `Omega_min>0`,

```text
T_active <=32000*(2pi/delta)+3916995*pi/Omega_min,
T_total <=T_active+3949024*t_switch.
```

The switching bound counts both ends and all boundaries of at most
`3917023+32000` primitives. It assumes a separately calibrated uniform
switching/settling interval bound, with specified dynamics during those
intervals. The program and its actual duration are input independent.
The upper bound on duration is not a substitute for the actual duration
when evaluating laboratory phases.

If `P_LS,e` is the total incident LS power at the selected intensity and
`P_(i,j)/Omega_(i,j)` is the calibrated carrier energy per unit angle,
the bound at a declared reference plane is

```text
E_incident <=500*(2pi/delta)*sum_e n_G(e) P_LS,e
             +3916995*pi*max_(i,j)[P_(i,j)/Omega_(i,j)].
```

For fixed reference powers `P_1,P_2`, use
`P_LS,e=lambda_e*(P_1+P_2)`. Illumination during idle and switching
intervals adds its explicit integral. This is not a bound on total
apparatus work or a finite quantum battery construction. The LS-loop
ratio to #1369 is `156000/32000=39/8`; no optimality is claimed.

## 8. Omitted-LS control and the inverse audit's scope

The specified negative control replaces every actual LS loop by an
equal-duration LS-off wait, retaining every carrier frame, its true
adjoint, all axis rotations and the common schedule. In the adopted
compensated interaction frame the wait contributes identity. The
LS-induced residual profiles are absent with the LS fields. The known
free laboratory evolution is still accounted for by MODEL.md.

Each framed loop then collapses to identity. Each triple exchange
collapses to identity, and each mask collapses to
`P_A^dagger Ry(beta)Ry(-beta) P_A=I`. The singleton controls also collapse.
M1 therefore remains zero for all inputs. The two unconditional writes
still set p1=2 and p4=1. For s nonzero the complete target fails because
M1 is wrong; for s=0 it fails because those two data coordinates are
wrong. Thus none of the 25 complete targets is attained. This is a
control for this frozen program, not an impossibility claim for all
carrier-only inputs or protocols.

Every elementary ideal factor is unitary, so the formal adjoint obeys
`W^dagger W=I`. An exact algebraic adjoint audit checks retained
information and phase bookkeeping. It does not construct a physical
inverse schedule at the same duration or resource count. In particular
one may not replace an LS pulse by an unadmitted negative duration.
Since `Q_e^4=I`, the optional identity

```text
G_e^3=gamma_e^4 G_e^dagger
```

is algebraically valid, but this forward probe does not specify or
account for a full inverse implementation based on it.

## 9. Limits and inherited remainder

Every included LS loop closes before the next carrier. Ideal carriers
act trivially on the included motion, so the full forward word factors
from its arbitrary inherited COM state and its correlations. No memory
is erased, and no motion is refreshed. M1, M2 and N are counted internal
factors with intentionally changed endpoints, not a purportedly reset
remainder.

The proof concerns the supplied 25-dimensional native input span.
It is not a full five-level SWAP, an arbitrary-input native law, occupied
memory reuse, the complete history through n=9 or a calibration of the
seventeen-ion device. Model truncations, actual preparation, all-mode
closure, decay and accumulated pulse error, finite control and work
sources, and archive protection remain open. Neither the shorter count
nor a successful exact audit removes the physical HOLD.
