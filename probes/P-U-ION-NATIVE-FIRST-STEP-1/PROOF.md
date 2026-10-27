# A finite retained-history realization of the first native step

**NON-CANONICAL conditional ideal-model construction.** Reservation
[#1368](https://github.com/mathorn1973/twist-j/issues/1368). This proof
specifies a finite word in the elementary controls of [MODEL.md](MODEL.md).
It supplies no execution result, practical fidelity, complete finite work
source or preparation-to-boundary-nine realization. Public authority
remains Canon v97.

The target is the actual first post-contact native family, with the fixed
dictionary of [#1363](https://github.com/mathorn1973/twist-j/blob/8847b657c648b5c2b231eca13d9adfbef451cc60/notes/C-U-ION-OFFSET-GLOBAL-AUDIT-N/README.md).
The preceding local exchange is the separate result
[#1365](https://github.com/mathorn1973/twist-j/blob/8cbdf106f6626698aabcc84c8d028bd12ff643c1/probes/P-U-ION-LS-LOCAL-EXCHANGE-1/RESULT.md).
Neither a general SWAP nor a state-selected branch gate is assumed here.
The known native collision motivates retaining the selector in counted
memory; it is not claimed as a new discovery.

## 1. Registers, target and elementary controls

The seventeen five-level ion factors have the fixed index order

```text
0:S1, 1:S2,
2:R1.p1, 3:R1.p4, 4:R1.p1p, 5:R1.p4p, 6:R1.q, 7:R1.r,
8:R2.p1, 9:R2.p4, 10:R2.p1p, 11:R2.p4p, 12:R2.y, 13:R2.r,
14:M1, 15:M2, 16:N.
```

The dictionary of R2 remains `y=q2-1 mod5`; all other displayed labels
are direct labels. N is an explicitly counted physical five-state factor
with this task's input 0 and output 1, not an unbounded clock. The input
sector consists of the twenty-five orthogonal vectors

```text
I(s,t): S1=1, S2=t, R1=(0,0,0,0,s,0), R2=(0,0,0,0,0,0),
        M1=0, M2=0, N=0,                     s,t in F5.
```

The required complete output is

```text
O(s,t): S1=1, S2=t, R1=f(s), R2=(0,0,0,0,3,0),
        M1=s, M2=1, N=1,
```

where the original generators and actual selectors give

| s | selected R1 generator | f(s) in the six original R1 coordinates |
| ---: | --- | --- |
| 0 | a | (0,0,0,0,0,0) |
| 1 | b | (0,0,0,0,4,0) |
| 2 | c | (2,1,2,1,4,0) |
| 3 | d | (2,1,3,4,3,1) |
| 4 | e | (2,1,3,4,3,1) |

Indeed theta_0=0 and the R1 selector equals s. R2's conjugated selector
equals 1 on its all-zero physical input, so its conjugated b produces
y=3. Thus M1 and M2 store the actual two selected indices. The identical
data rows f(3)=f(4) have different M1 outputs.

The carrier controls are individually addressed star rotations only:

```text
R_(i;0,k)(theta,phi)
  = exp[-i theta (exp(-i phi)|0><k|+exp(i phi)|k><0|)_i/2],
                                      k=1,2,3,4.
```

Define `Ry_(i;0,k)(theta)=R_(i;0,k)(theta,pi/2)`. A negative angle is
implemented as the positive angle with phase increased by pi. True
adjoints below use that rule and reverse the chronological pulse order.
The only entangling primitive is the declared global closed LS loop;
there is no physically pair-selected LS beam in the construction.

## 2. One global closed force loop

Let `D0=diag(d0,...,d4)` be the one fixed real nonscalar response profile.
The fixed complex spatial factors c_i do not include eta. In the declared
single-mode interaction frame, put

```text
A = sum_(i=0)^16 c_i D0_i,
H(t) = i hbar eta lambda/2
       [A a^dagger exp(-i delta t)-A^dagger a exp(i delta t)],
tau = 2 pi/delta,       delta>0,
K = pi eta^2/(2 delta^2).
```

A is normal because its terms are commuting diagonal operators. The
Magnus series terminates after its second term: the first is a
displacement with coefficient
`eta lambda(1-exp(-i delta t))/(2i delta)`, and the second is

```text
-i eta^2 lambda^2 (delta t-sin(delta t))/(4 delta^2) A A^dagger.
```

All higher nested commutators vanish. Consequently the completed loop is

```text
L(lambda) = exp[-i K lambda^2 A A^dagger] tensor I_motion.
```

This is an operator identity in the declared harmonic-mode model; it
does not replace the oscillator by a fresh vacuum or a finite numerical
cutoff. Residual stationary one-ion phases admitted by MODEL.md are
written as an additional `exp[-i sum_i L_(i,e)]`, where L_(i,e) is the
dimensionless integrated diagonal phase for one loop at the chosen
intensity lambda_e. These profiles are fixed across one echo. Bare-frame
phases already included elsewhere in MODEL.md are not counted twice.

## 3. Five hundred loops isolate equality on one chosen pair

Write

```text
S = sum_j d_j,    Q = sum_j d_j^2,
B = 5Q-S^2 = sum_(j<k)(d_j-d_k)^2 > 0,
g_(i,j) = Re(c_i conjugate(c_j)).
```

The needed unordered pair set is exactly
`E_star={{14,k}:k=2,...,7}`. Require `g_e != 0` on those six edges and
the independently admitted positive intensities

```text
lambda_e = delta / [eta sqrt(50 B |g_e|)].
```

These are conditions on the model, not fitted values from the twenty-five
logical outputs. For a selected edge e, assign both active ions the
direction `(1,0,0)` in F5^3. Form the lexicographically sorted list of all
nonzero vectors in F5^3 whose first nonzero coordinate is 1. It has
`25+5+1=31` members. Remove `(1,0,0)` and assign the first fifteen
remaining vectors to spectator ions in ascending ion-index order.

For each `(a,u)` in lexicographic order, with `a=1,...,4` and
`u in {0,...,4}^3`, apply the seventeen independently addressed
monomial permutations with underlying label maps

```text
p_i(x) = a x+v_i dot u mod5,
```

then one complete global LS loop at lambda_e, then their true adjoints.
There are exactly 500 such framed loops. Their complete internal
endpoints are diagonal and therefore commute. Their product is the
exponential of the exact sum of their diagonal phases; no Trotter limit
or average-Hamiltonian truncation is used.

Here are the required sums, valid for every joint internal basis label.
For one ion, each affine permutation occurs 25 times, so

```text
sum_(a,u) d_(p_i(x))^2 = 100Q,
sum_(a,u) L_(i,e)(p_i(x)) = 100 Tr L_(i,e).
```

For distinct directions, the two linear forms of u have rank two.
Each pair of offsets occurs five times for each a. Hence any pair other
than e contributes

```text
sum_(a,u) d_(p_i(x)) d_(p_j(y)) = 20 S^2,
```

independently of x and y. The active pair shares its direction. If x=y
its sum is 100Q. If x differs from y, the twenty affine maps send (x,y)
bijectively through all ordered unequal label pairs, with multiplicity
25 from u, and its sum is `25(S^2-Q)`. The difference is 25B.

Let `E_e=sum_x |x,x><x,x|` on the active pair, tensored with the identity
on the other ions. Expanding `A A^dagger` therefore gives the full
seventeen-ion identity

```text
sum_(a,u) (A A^dagger)_(p(a,u)) = C_e I+50 B g_e E_e,

C_e = 100Q sum_i |c_i|^2
      +40 S^2 sum_(i<j) g_(i,j) -10 B g_e.
```

All spectator dependence and all residual local profiles become scalars.
In particular no unrecorded spectator unitary remains. The completed
500-loop word has the exact form

```text
G_e = gamma_e exp[-i sign(g_e) pi E_e/2] tensor I_motion,

gamma_e = exp[-i K lambda_e^2 C_e-i100 sum_i Tr L_(i,e)].
```

Gamma_e is independent of every internal input label. It may depend on
the declared physical edge and calibrated stationary phase profiles.
Squaring the normalized word removes the sign of g_e:

```text
Z_e = gamma_e^(-2) G_e^2 = I-2E_e.
```

Every occurrence of Z below denotes two actual G words. Normalization
only records their common scalar; it is not an extra physical gate.

## 4. Explicit star compilation and its finite count

Use `T_j=R_(0,j)(pi,0)` on the named individual ion. It is a monomial
star transposition with its actual phases retained. For any label
permutation, decompose it into forward cycles, start every cycle at its
smallest member and order the cycles by those members. Chronological
star lists are

```text
(0,a1,...,aL):      a1,...,aL,
(a1,...,aL), 0 absent and cycle length>=2: a1,...,aL,a1.
```

Singletons are skipped. This implements the specified underlying
permutation with at most six star pi pulses on five labels. Its true
inverse is the reversed list with carrier phase pi. Monomial phases
cancel in the conjugation of the diagonal force and local profiles.
They are not silently replaced by a phase-free SWAP matrix.

For the twenty affine maps `x->a x+b`, the canonical star lengths sum
to 72. This also follows without enumeration: the four nonidentity
translations contribute 16; the five reflections a=4 contribute
`6+4*4=22`; each of a=2 and a=3 contributes `5+4*3=17`. The identity
contributes zero. Each affine map appears 25 times per ion in G_e.
Forward and inverse frames therefore require exactly

```text
17 * 25 * 2 * 72 = 61200
```

individually addressed star pi pulses per G_e. The loops are chronological
in the order already fixed. Within each frame, act on ions in ascending
index order; undo them in reverse order using the individual adjoints.
No parallel-pulse assumption is needed for this count or the time bound.

## 5. One-value controlled rotations from three pair masks

Fix a physical control ion, a target ion, and a target pair of levels
`(0,k)`, with k nonzero. For a sorted two-element control mask A, define
the label permutation P_A that maps its two sorted labels to `(0,k)`
and maps the remaining control labels, in ascending order, to the
remaining target labels in ascending order. Compile P_A by section 4.

The following chronological word uses the same physical edge throughout:

```text
P_A on control;
Z_e; Ry_target(-beta); Z_e; Ry_target(+beta);
P_A^dagger on control.
```

After removing its known scalar gamma_e^4, this is exactly Ry(2 beta)
on the target when the control label belongs to A, and identity when it
does not. To check the complete operator, condition first on the control
basis label. If it is 0 or k in the permuted frame, Z acts on the target
two-level subspace as either sign of its Pauli Z, so
`Z Ry(-beta) Z=Ry(+beta)`. For any other control label, Z commutes with
the rotation. Outside the target pair, the rotations are identity and
the two Z factors cancel. Thus this proof covers all twenty-five columns,
including target labels outside the rotated pair.

For a one-value condition j, choose b and c to be the two smallest labels
other than j. Apply in this order the masks

```text
{j,b}, beta=+pi/4;
{j,c}, beta=+pi/4;
{b,c}, beta=-pi/4.
```

The rotations have the same target axis and add their angles. Their
control projectors obey
`(P_j+P_b)+(P_j+P_c)-(P_b+P_c)=2P_j`. Consequently the product is

```text
CROT_(control=j; target,0,k) = controlled Ry_(0,k)(pi),
```

with identity for every false control label and outside the target pair.
The actual word has the common scalar gamma_e^12, from twelve G words.
All three masks are executed for every input. This construction supplies
the controlled operation; it is not presumed as an elementary control.

## 6. The complete native word on its actual input sector

First transfer the value of ion 6, R1.q, into the counted ready ion M1.
For k=1,2,3,4 in ascending order, execute

```text
CROT_(ion6=k;  ion14,0,k),
CROT_(ion14=k; ion6,0,k).
```

There are eight controlled rotations. Since
`Ry(pi)|0>=|k>` and `Ry(pi)|k>=-|0>`, the pair of active operations at
k=s gives

```text
|s,0>_(ion6,ion14) -> -|0,s>        if s!=0,
|0,0>_(ion6,ion14) ->  |0,0>        if s=0,
```

apart from their already recorded common LS scalars. Earlier and later
k blocks are inactive on that input. R1 is now all zero and M1=s.
This is a newly specified eight-block transfer on the actual ready
sector, not an assumed full SWAP or a new abstract copying primitive.

Next loop over s=1,2,3,4 in that fixed order, and within each row over
the six R1 coordinates in index order 2,...,7. Whenever that fixed row
of f(s) has a nonzero entry k, execute

```text
CROT_(ion14=s; target coordinate,0,k).
```

The fixed table has respectively 1,5,6,6 nonzero entries, so there are
eighteen such blocks. The loop bounds and omissions are compiled from
the declared table before input preparation; the runtime program does not
inspect s to select a pulse list. For any actual input, only its row
acts. Each addressed target is still in level 0 when its active block
occurs and therefore acquires level k with positive amplitude. M1 is
unchanged and R1 becomes exactly f(s).

Apply to M1 the four pulses `R_(14;0,j)(2pi,0)`, j=1,2,3,4 in order.
Their product is the single-ion diagonal operator

```text
D0 = diag(+1,-1,-1,-1,-1).
```

The level-0 sign occurs four times, whereas each nonzero level occurs
once. D0 cancels the transfer sign for every s. Finally execute the three
fixed positive-amplitude preparations

```text
Ry_(12;0,3)(pi), Ry_(15;0,1)(pi), Ry_(16;0,1)(pi).
```

Their inputs are still level 0. They set R2.y, M2 and N to 3,1,1 and
give no relative sign. All other declared coordinates have their target
values, including S1=1 and the unchanged arbitrary S2=t.

Thus the full word W has

```text
W |I(s,t)> = Gamma |O(s,t)>,        for every s,t in F5,
Gamma = product_over_all_26_CROT gamma_(its_edge)^12.
```

Gamma is common to all twenty-five inputs. The claimed normalized
amplitudes are exactly +1; the physical common scalar has not been
discarded from the account. Linearity establishes the same identity on
the entire twenty-five-dimensional input span, including superpositions
entangled with a reference. No test outcome is postselected. This is a
specialized native-step realization on that span, not a realization of
the general state-selected map on all six-pentit inputs.

## 7. Primitive resources, common time and incident optical energy

There are 26 controlled rotations, hence 312 G words and exactly

```text
156000 complete global LS loops.
```

Besides the 61200 star pi pulses per G, each controlled rotation has six
control-permutation frames of at most six star pi pulses each, and six
target rotations of absolute angle pi/4. There are four final 2pi pulses
and three final pi pulses. Conservative complete bounds are therefore

```text
N_carrier <= 312*61200 + 26*36 + 26*6 + 7 = 19095499,

A_carrier/pi <= 312*61200 + 26*36 + 26*6/4 + 4*2 + 3
             = 19095386.
```

These are finite bounds for the specified compiler, not minimum or
practical pulse counts. In particular the large count does not imply an
acceptable accumulated physical error.

Let Omega_min>0 be an independently admitted lower bound on the usable
addressed Rabi rates for this finite programme. With serial pulses,

```text
T_active <= 156000*(2pi/delta) + 19095386*pi/Omega_min.
```

A uniform switching-interval bound t_switch adds at most
`19251500*t_switch`, including both ends, because the displayed pulse
count is at most `19095499+156000`. Additional preparation, measurement
or declared idle intervals require their own account. This schedule and
its duration are independent of s and t.

The G-word counts per physical edge are

```text
n_G({14,6})=144,
n_G({14,k})=36 for k=2,3,4,5,
n_G({14,7})=24.
```

They sum to 312. Let P_LS,e be the total incident power of the two LS
beams during a loop at lambda_e. Let P_(i,j) and Omega_(i,j) be the
corresponding carrier power and positive Rabi rate for an individually
addressed star transition. One conservative incident-energy bound is

```text
E_incident <= 500*(2pi/delta)*sum_e n_G(e) P_LS,e
              +19095386*pi*max_(i,j)[P_(i,j)/Omega_(i,j)],
```

plus separately counted illumination during switching or idle intervals.
If both LS beams use the model's common intensity scale,
`P_LS,e=lambda_e*(P_LS,1^0+P_LS,2^0)` may be substituted. These statements
require the chosen lambda_e, powers and rates actually to belong to the
admitted parameter domain. No numerical values are inferred from the
logical table. Incident optical energy is not total apparatus work or a
proof of a finite quantum battery trajectory.

## 8. Remainder inheritance and the exact boundary of the construction

Every LS loop closes before the next carrier frame. The 500-loop identity
removes spectator dependence as an operator, not only as a mean-energy
statement or a test on basis spectators. Consequently the complete word
has the proved internal action tensored with identity on the included
interaction-frame harmonic mode and with the model's declared uncoupled
remainder evolution. It does not require fresh motion. This remains true
for arbitrary correlations with references and other included remainder
factors. M1, M2 and N are counted internal factors and are deliberately
changed; they are not part of a purported reset remainder.

The initial blank memory sector and the post-contact data family are
inputs to this first-step task. Their actual preparation and the resources
inherited at the second contact have not been constructed here. The
output M1=s cannot subsequently be treated as a common blank register.
Laboratory-frame phases, other motional modes, finite carrier and force
errors, scattering, decay, addressing errors and the physical states of
finite control and work sources remain subject to MODEL.md's explicit
limits. Returning the effective harmonic mode does not return those
other resources automatically.

The positive statement is a finite, completely prescribed control word
for this one native input family within the admitted effective model.
It evades the data-only collision obstruction by transferring the
distinction to M1. It does not establish a practical seventeen-ion
implementation, an independently calibrated error bound, later native
steps, the full two-contact history, or derivation of these physical
resources from J. Failure of this particular candidate would likewise
not prove a prohibition on the entire enlarged control class.
