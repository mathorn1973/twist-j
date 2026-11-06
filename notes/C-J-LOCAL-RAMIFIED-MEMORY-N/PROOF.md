# Exact local circuits and their limits

**NON-CANONICAL / candidate-T / L1 / proof-first / result-exposed.**
Author: A. M. Thorn <thorn@twistj.com>. Owner #1294.

## 1. Algebra and the literal digit obstruction

Put O=Z[j], j^4+j^3+j^2+j+1=0, J=1+j^2 and beta=varpi=1-j.
The coefficient basis is always (1,j,j^2,j^3), except in the explicitly
labelled beta-basis table below. One has

```
J^-1 = -j-j^2,
beta = 1-(J-1)^3,
beta^4 = 5 J^2,
O/beta O = F5,   [a+bj+cj^2+dj^3]_beta = a+b+c+d mod5.
```

The last quotient follows by setting j=1 in Phi_5. Thus its five affine
cosets are disjoint. They are not vector subspaces of O. The displayed
beta^4 identity is an element identity; beta^4=5 would be false. J is an
algebraic unit, not thereby a unitary operator on a chosen inner product.

**Proposition 1 (every nonredundant beta digit system has a missing value).**
Let D be any complete set of five representatives for O/beta O, with 0 in D.
It is impossible that every x in O has a finite expansion with digits in D.

Proof. Choose nonzero d in D and put x=d/j, which lies in O because j is a
unit. Then x=beta x+d and x mod beta=d mod beta. The forced digit is d and
the forced quotient (x-d)/beta is x again. A finite expansion must terminate
at zero after its successive forced divisions. This nonzero fixed point
does not. Redundant digits or a nonzero terminal state change the premise.

**Proposition 2 (the usual finite words are not J-stable).**
For D={0,1,2,3,4}, 1 has a finite beta expansion but J does not.

Proof. In the beta basis, Phi_5(1-beta)=0 gives

```
beta^4 - 5 beta^3 + 10 beta^2 - 10 beta + 5 = 0.
```

For x=a0+a1 beta+a2 beta^2+a3 beta^3, let d be a0 mod5 in D and
k=(a0-d)/5. Forced division has the exact coefficient rule

```
T(a0,a1,a2,a3) = (a1+10k, a2-10k, a3+5k, -k).
```

Since J=2-2 beta+beta^2, its successive coefficients are:

| Step | Coefficients in the beta basis | Emitted digit |
| --- | --- | --- |
| 0 | (2,-2,1,0) | 2 |
| 1 | (-2,1,0,0) | 3 |
| 2 | (-9,10,-5,1) | 1 |
| 3 | (-10,15,-9,2) | 0 |
| 4 | (-5,11,-8,2) | 0 |
| 5 | (1,2,-3,1) | 1 |
| 6 | (2,-3,1,0) | 2 |
| 7 | (-3,1,0,0) | 2 |
| 8 | (-9,10,-5,1), the step-2 state | 1 |

Each row follows by substitution into T. The six distinct nonzero states
from steps 2 through 7 form a cycle. Therefore no finite such word denotes J.
This is a closure obstruction, not merely a slow-carry claim. No numerical
search or finite-sweep evidence is needed for the displayed witness.

## 2. A common finite alphabet for all integer states

Write D_b={-2,-1,0,1,2} and let bal(z) be the representative of z mod5 in D_b.
Every integer z has a unique finite-support expansion

```
z = sum_(i>=0) z_i 5^i,     z_i in D_b.
```

Indeed the quotient (z-bal(z))/5 has smaller absolute value for |z|>=3,
and the values -2,...,2 terminate immediately. Uniqueness follows by taking
the first different digit modulo five and dividing. Zero padding denotes
the same infinite, eventually-zero sequence, not different algebraic data.

Encode each element of O by four such tracks. A cell alphabet D_b^4 is
finite and represents every O value with finitely many nonzero cells. This
is a coefficient code in base five, not a claim that the literal beta
digits were repaired without changing their class.

For two registers E,X, put the four digits of E at sites i>=0 and those of X
at sites -1-i. The contact is the edge (-1,0). A finite implementation uses
sites -N,...,N-1, with fixed, retained endpoint marks and finite auxiliary
tracks. Sites and the schedule are additional structure. The four-track
alphabet and the gate types do not grow with N.

At width N, each coefficient has the exact centered range

```
-(5^N-1)/2 <= z <= (5^N-1)/2.
```

Digits of negative coefficients also have finite support. No infinite sign
extension, infinite-precision cell, or unbounded carry alphabet is used.

## 3. The elementary clean local adder

We give gates, not an appeal to general computational universality. For two
distinct coefficient tracks x,y, implement y <- y+x modulo 5^N. Carry
registers c1,...,cN have alphabet C3 represented by {-1,0,1}; c0=0 is a
constant. The arithmetic promise is that all carry registers start at zero.

In increasing order i=0,...,N-1 perform:

```
kappa = (x_i+y_i+c_i-bal(x_i+y_i+c_i))/5,
c_(i+1) <- c_(i+1)+kappa mod3,
y_i     <- bal(y_i+x_i+c_i).
```

On the ready slice the newly computed carry is kappa in {-1,0,1}. Each line
is a controlled permutation of its target register, with all controls
unchanged. This remains a permutation on arbitrary dirty carry inputs.
Place c_i at the digit site i, including the end carry at the neighbouring
boundary site. A gate then uses at most two neighbouring sites; the boundary
may be a retained extra cell. On the negative half-line reverse the spatial
direction. A fixed finite enlargement of the boundary alphabet suffices.

After the forward sweep, clean in decreasing order i=N-1,...,0. Using the
updated y_i and the still present c_i, compute as a control function

```
old_y = bal(y_i-x_i-c_i),
kappa = (x_i+old_y+c_i-y_i)/5,
c_(i+1) <- c_(i+1)-kappa mod3.
```

These are again finite controlled permutations. Here old_y is a finite
lookup expression, not an allocated uncleared copy. It reconstructs the
actual old digit, so it removes exactly the forward carry. High-to-low order
keeps c_i available until it has served as a control. All carries end at zero.

Telescoping the digit equations proves the modular sum. If the exact integer
sum is inside the centered N-digit range, uniqueness of that representative
proves exact integer addition. A sufficient reserve makes this true; no
overflow is discarded and then described as an exact integer result.

The reverse gate word is the inverse on the entire finite carrier, including
dirty workspace. For prepared states it implements subtraction, with clean
workspace. Negation is the digitwise permutation z_i -> -z_i. Track swaps
are also local permutations. Therefore any fixed word in integer shears,
negations and track swaps has an explicit local reversible implementation.
It uses O(N) sites and O(N) sequential layers, with constants fixed by the
word. No tests mirroring these identities are needed to establish them.

**Reserve rule.** For a fixed integer gate word, choose a constant C bounding
the infinity norm of every partial linear map in that word. If all starting
coefficients have absolute value <=B, require (5^N-1)/2 >= C B. For the
single multiply-by-five digit transfer below also reserve a zero top digit
on its receiving coefficient, and bound post-transfer coefficients by
5 C B+2 before applying the remaining fixed charts. These finite linear
bounds select N=L+O(1) for L-digit inputs. The reserve is a declared resource,
not a local algorithm claimed to discover its own required endpoint.

More explicitly, let C_pre,C_post bound every partial pre/post chart and
let R_N=(5^N-1)/2. It suffices to require
R_(N-1)>=C_pre B and
R_N>=max(C_pre B,C_post(5 C_pre B+2)). For the inverse digit transfer use
the same zero-top-digit reserve on its receiving coefficient, with register
roles exchanged. For a fixed finite sequence of operations, apply the
corresponding finite bounds successively before selecting the common width.

## 4. J hold and its inverse on this same code

Direct reduction in O gives

```
J(a,b,c,d) = (a-c+d, b-c, a, b-c+d).
```

It is exactly the following five shears, in order:

```
b <- b-c
a <- a-c
c <- c+a
a <- a+d
d <- d+b.
```

All right-hand sides use the current registers. For example the third line
sets c to the original a. Reversing the order and all addition signs gives
J^-1. Section 3 implements both words with nearest-neighbour gates and clean
carry tracks, at depth O(N). The integer identity also proves determinant
one without imposing any positive-definite norm preservation.

## 5. Ramified writing as one digit transfer

Use centered rho(X)=bal(sum of the four coefficients of X). Define on all
of O squared

```
B(E,X) = (beta E+rho(X), (X-rho(X))/beta).
```

This is an exact bijection. Given E',X', recover

```
d = rho(E'),
E = (E'-d)/beta,
X = beta X'+d.
```

For a prepared one-digit source X=d in D_b, it sends (E,d) to
(beta E+d,0). On arbitrary X it retains the quotient; no dirty high part is
deleted. The source alphabet is a centered copy of F5, equivalent to the
five residue classes but different from the digit choice in Proposition 2.

Here is an explicit local implementation, including the division. Set

```
P(x0,x1,x2,x3) = (x0+x1+x2+x3, x1, x2, x3),
Q(e0,e1,e2,e3) = (e3, -e0+e1+e3, -e1+e2+e3, -e2+2e3).
```

Their integral inverses are

```
P^-1(v) = (v0-v1-v2-v3, v1, v2, v3),
Q^-1(u) = (4u0-u1-u2-u3, 3u0-u2-u3, 2u0-u3, u0).
```

The multiplication matrix M_beta obeys

```
M_beta e = (e0+e3, -e0+e1+e3, -e1+e2+e3, -e2+2e3),
P M_beta = diag(5,1,1,1) Q,
P(d,0,0,0) = (d,0,0,0).
```

Consequently B is the following composition:

1. Transform E by Q and X by P, obtaining u and v.
2. Replace only their first coefficients by
   `(u0,v0) -> (5u0+d,(v0-d)/5)`, where d=bal(v0).
3. Transform the E output by P^-1 and the X output by Q^-1.

The other three coefficients in step 2 stay unchanged. For Q an explicit
shear/negation word is: negate e0, add e1 and then e3 to it; negate e1, add
e2 and then e3 to it; negate e2 and add e3 twice; finally rotate the four
tracks from (a,b,c,d) to (d,a,b,c). P is three additions to track zero.
Their reversed words implement their inverses. Thus every chart is covered
by the actual local gates of section 3.

Step 2 is especially simple in the shared code. Join the first tracks as
the ordered line

```
v_(N-1), ..., v_1, v_0, u_0, u_1, ..., u_(N-1).
```

Right rotation by one position is a permutation of these 2N digits. It can
be performed using 2N-1 adjacent swaps: move the last entry leftwards across
every preceding entry. There is no long edge connecting the endpoints.
The resulting digits are

```
u'_0 = v_0,             u'_i = u_(i-1)       (1<=i<N),
v'_i = v_(i+1) (i<N-1), v'_(N-1) = u_(N-1).
```

When the declared receiving top digit u_(N-1) is zero, these are exactly
5u0+d and (v0-d)/5. Otherwise the overflow is retained as the top source
digit and the finite map remains reversible, but is not the stated integer
transfer. The reserve rule distinguishes these cases in advance.

On an unbounded double ray with finite support, the same scalar transfer is
the ordinary one-site right shift, with no endpoint wrap. This is a separate
boundary convention; it is not used to hide the endpoint of a finite device.
The finite adjacent-swap construction establishes the claimed O(N) circuit.

**Conclusion of sections 2-5.** For every finite bound on initial integer
coefficients there is one sufficiently wide common finite-alphabet carrier
and explicit local reversible circuits for B, B^-1, J and J^-1. Their
workspace returns to ready on the promised domain. Each complete gate word
is a permutation on its entire finite carrier; exact integer semantics are
claimed only with the declared reserve and ready workspace.

## 6. A fixed local latency is impossible in this code

Let L>=1 and A_L=2 sum_(i=0)^(L-1) 5^i=(5^L-1)/2. Compare

```
M=A_L,        M_tilde=A_L+j^3.
```

In the common coefficient code they differ only at the lowest digit of the
fourth coefficient. All workspace, boundary marks, schedule and any phase
register are initially identical. The first coefficients after multiplication
by J are A_L and A_L+1. Their balanced expansions are respectively

```
A_L:   digits 2 in positions 0,...,L-1; digit 0 in position L,
A_L+1: digits -2 in positions 0,...,L-1; digit 1 in position L.
```

The second identity follows from 5^L-2 sum_(i<L)5^i=(5^L+1)/2.
Thus one change at site zero changes the output at site L. Any sequence of
local layers of radius at most R has dependence radius at most R times the
number of layers, by induction on the layers. Therefore an exact multiplier
in this encoding requires at least ceil(L/R) layers on this pair (R>0).
No constant bound works for all L. The upper O(N) construction and the lower
linear bound have the same order for this representation.

This is not a no-go for redundant digits, other spatial placements or other
state encodings. Nor does it forbid a local microdynamics: it forbids calling
an arbitrarily large canonical arithmetic macrostep one bounded local tick.

## 7. Local finite-phase readers

The four lowest coefficient digits determine M mod5 at the contact. Their
sum determines M mod beta. Hence the following readers have bounded spatial
input, after the corresponding arithmetic macrostep has completed.

**Single ramified write.** Let E be arbitrary, delta in D_b, and

```
M_0=beta E+delta,     M_t=J^t M_0.
```

Since J mod beta=2 in F5, the reader

```
delta = bal(2^(-c) [M_t]_beta),     c=t mod4,
```

recovers the digit for every t>=0, independently of the old archive E.
The fixed finite lookup can be applied reversibly into an initially zero
output latch by controlled addition modulo five, leaving M and c unchanged.
Undoing that read requires the same controls or retention of their values.

For readers whose only inputs are `(M_t mod beta,t mod h)`, with the full
five-symbol alphabet and all E,t, exact recovery is possible iff 4 divides h.
Necessity: for any delta, the histories at times h and zero with messages
delta and 2^h delta have identical observations. Exact decoding requires
2^h delta=delta for every delta, hence 2^h=1. Its order in F5 is four.
Sufficiency is the displayed reader.

**Full residue packet.** If M_0 mod5=p is a full 625-element source, then

```
p = J^(-c) [M_t]_5,     c=t mod20.
```

In O/5, beta^4=0, J=2-2 beta+beta^2, so J^5=2 and J^20=1. Also
J^4=1+beta+terms of degree at least two, so J^4!=1; the coefficient is
4*2^3*(-2)=1 mod5. Since J^5 has order four, J has order twenty.
The same time-zero/time-h comparison on all p proves that a reader of
`(M_t mod5,t mod h)` works for the full source iff 20 divides h.
This agrees with v94 J-RESIDUE-PERIOD and C20-TEICHMULLER-SPLIT.

A single beta write does not replace the whole residue modulo five: the old
beta E term still contributes there. For a complete packet one may instead
prepare M_0=beta^4 E+v, where v is a four-beta-digit representative; these
625 representatives are distinct modulo beta^4, and (beta^4)=(5).
No claim that arbitrary O values have finite beta expansions is used.

The phase in either reader is relative to that write. It must be prepared,
or computed from a retained write timestamp and the current phase. An
existing clock cannot be reset to zero by an irreversible assignment. A
phase increment is charged once per completed H macrostep, not once per
adder microgate. Repeated mixed write/hold histories also require their
instruction/phase record for full backward reconstruction; a bounded
current phase is not asserted to encode that unbounded history.

## 8. One explicit autonomous local controller

The circuit schedules can themselves be internalized. This gives a selected
autonomous mathematical realization, not a derivation of the native U.
Fix any finite macro word in B, B^-1, H, H^-1 and the reversible finite read
gates. The word is part of the chosen law. Its implementation uses a fixed
finite list of oriented passes, independent of the reserved width N.

Take the finite line of data and boundary-carry cells used above, with M
sites numbered 0,...,M-1 for this controller paragraph only. Retain static
left/right endpoint, contact and E/X-side marks. The side marks matter:
the controller is not given nonlocal access to an unmarked region name.
Exactly one site contains a head labelled by direction epsilon in {+,-}
and phase p in C_r. Here r>=1 is the number of program phases, not a function
of N; an empty program uses one idle phase. All other sites have no head. The complete carrier consists of
arbitrary data/ancilla states, these consistent fixed marks, and exactly
one such head.

The head-only transition T is

```
(i,+,p) -> (i+1,+,p)       if i<M-1,
(M-1,+,p) -> (M-1,-,p),
(i,-,p) -> (i-1,-,p)       if i>0,
(0,-,p) -> (0,+,p+1 mod r).
```

It is one cycle of length 2Mr: each phase makes one rightward and one
leftward traversal, with an in-place turn at each endpoint. Every displayed
state has one predecessor, including the phase decrement at the left turn.
The head label is finite at every site; its position is distributed on the
line, not stored as an unbounded integer inside a cell.

For clock state c=(i,epsilon,p), let G_c be the local gate of that pass at
the old head site, or identity when the direction/region does not match.
All G_c are the explicit finite permutations above, supported within one
edge of the head, and they leave head and static marks untouched. Define
the simultaneous microstep

```
V_N(c,x) = (T c, G_c x),
V_N^-1(c',x') = (T^-1 c', G_(T^-1 c')^-1 x').
```

This is a bijection on the complete declared one-head carrier, including
dirty data and carry registers. The head move and turns depend only on its
finite label and adjacent static marks. Computing a local data output from
a gate near the head requires only a bounded neighbourhood. A conservative
radius bound of three covers both the forward and inverse rules, independent
of M and N. Thus this is one uniform finite-alphabet local rule for the
chosen macro word on all consistently marked interval lengths. No claim is
made about arbitrary inconsistent marks or multiple-head configurations.

For completeness the pass compilation is constructive:

- An adder uses one phase firing carry-then-digit gates in low-to-high
  order on its designated half, followed by a phase firing cleanup gates
  in high-to-low order. The unused traversal of either phase is identity.
  On the X half the corresponding spatial directions are reversed.
  An inverse adder first undoes cleanup in low-to-high order, then undoes
  the forward pass in high-to-low order, applying the digit inverse before
  the carry inverse at each site. Thus traversal directions as well as
  local gate order are reversed.
- A digitwise sign change or track permutation fires once at each
  designated digit site on one traversal.
- The right rotation in section 5 fires swaps between a head site and its
  left neighbour in right-to-left order over the digit interval, skipping
  the leftmost digit. Boundary-carry cells are marked and skipped. The
  inverse uses the reversed adjacent-swap sequence.
- A finite read or a clock increment fires once at the contact during its
  designated phase and direction. A separate C20 latch there can count
  completed H operations; it does not count every head move. This residue
  phase is distinct from the head's program phase p.

Concatenating these finitely many passes yields r independent of N. The
return traversals and boundary turns are explicit idle microsteps where
appropriate. Declare the entry section c_*=(0,+,0), with phase zero the
first compiled pass, and let W_N be the compiled data permutation. Then

```
V_N^(2Mr)(c_*,x) = (c_*, W_N x).
```

One program traversal takes 2Mr=O(N) microsteps. Only the head returns
to its starting state; the full data state need not be periodic with that
period. An arbitrary other starting head state generally induces a cyclically
shifted gate word, not W_N itself. Full-carrier bijectivity still holds there;
the promised integer and clean-workspace semantics apply at the declared
entry/return section with ready work tracks and the reserve conditions.
Any promised integer operation still requires the reserved width; the head
does not grow the interval or ensure that a later source is prepared.

This construction internalizes scheduling in an added finite-state head.
It neither selects the macro word nor derives endpoint/side marks, source
arrival, clock preparation, increasing capacity or spatial geometry from J.
Its reversibility and locality are mathematical properties of V_N, not a
new assertion about the declared native update U.

## 9. Occupancy, capacity and the remaining dynamical debt

The integer zero is a payload. It is not a physical empty-register tag.
For example B(0,0)=(0,0), so this arithmetic alone cannot tell whether a
zero-write event occurred. A packet protocol must retain occupancy and
length or delimiters. Algebraic recovery of delta in section 7 is conditional
on a declared occupied write, not an event detector.

A reversible tag transport is explicit if needed: let a be a source
occupancy bit at site zero and z_i a finite-support bit tape on Z. Swap a
with z_0, then shift z right. Thus a'=z_0, z'_1=a and z'_i=z_(i-1) for i!=1.
Its inverse is immediate. On a=1 and all nonpositive z_i=0 it vacates the
source and inserts a mark, including for payload zero. The finite version
rotates a declared interval and keeps its endpoint just as in section 5.
This tag tape is an additional resource, not information latent in E=0.
It records accepted writes only if the write schedule and preparation are
supplied; it does not cause such events to occur.

At any fixed N with finite controllers and all registers included, the
machine has finitely many states and every completed gate word is a
permutation. Its orbits under a fixed repeated schedule recur. Longer finite
chains increase capacity but do not provide indefinitely growing history.
The scalable circuit family admits a larger N for a larger finite task;
it does not produce new blank cells inside one finite closed system.

For the same reason, reserve exhaustion is not permission to discard a high
digit or replace the state by zero. Extending the carrier, retaining an
overflow register, or adopting the explicit infinite-tape boundary are
different added resources. Reuse of clean carry workspace does not increase
the information capacity of the output register.

The established result is a mathematical feasibility and latency boundary:
one finite alphabet, explicit local reversible circuits and the selected
one-head autonomous rule suffice for the declared finite integer tasks.
Native-U source coupling, fresh preparations, automatic capacity growth,
selection of the graph and its geometry, and physical event semantics are
not derived. The native U remains the declared map on N_0 x F5^6. No live
apparatus or spacetime obligation is closed by this chosen local machine.
