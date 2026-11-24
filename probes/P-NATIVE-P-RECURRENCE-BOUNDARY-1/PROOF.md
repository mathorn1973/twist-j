# Recurrent contact: exact obstruction and a selected correction

PUBLIC / NON-CANONICAL / L1 / candidate-T pending review and fold.
A. M. Thorn. SPDX-License-Identifier: Apache-2.0.

This proof concerns the frozen PREREG.md. The complete reference contact
is taken from #1629 at 217cfc13befc3ab4b14444aed49e3fce7f50a7b7.
Neither that source's STOP nor its completed review is reopened.

## 1. The reference really is a permutation with a local acquisition test

The reference retains s=(mu,q,p,u,v,alpha,beta,tau), bank b, vertex c,
direction d, and fixed spectators. Its account is
H=q^2+p^2+u^2+v^2+2 ell(mu)^2, H+b=8, 0<=b<=3.
The controlled translation P_h and its price are

```text
h=epsilon(mu), epsilon=(0,1,0,0,-1)
P_h: (p,u,v,alpha) -> (p+h,u+h*q,v+h*q,alpha+h mod 5)
Delta_h=2h[p+q(u+v)]+h^2(1+2q^2).
```

H_e pairs an allowed (c,d)=(0,+1) input with its funded P_h output at
(1,-1). The inverse proposal uses P_-h and returns exactly the original
bank. Both bounds are symmetric on that paired edge. Refused inputs and
outward endpoints are fixed. Hence H_e is an involution on the entire
shell, including h=0. D flips d and is also an involution. F_P=D H_e is
therefore a permutation, with inverse H_e D. It need not be an involution.

The witness pair has mu=1 or 4, (q,p,u,v,b,c,d)=(1,0,1,-1,3,0,+1),
and common Weyl labels/spectators. Both have H=5 and Delta=3. The two
outputs have (p,u,v)=(1,2,0) or (-1,0,-2), b=0, c=1, d=+1;
alpha changes by +1 or -1 and the remaining labels are unchanged.
The receiver records sgn(u^2-v^2) are +1 and -1. These exposed exact
reference substitutions do not demonstrate native execution.

## 2. Exact native difference transport

The coordinate order and the five literal raw maps are fixed in PREREG.
Let B exchange coordinates 0 with 2 and 1 with 3, fixing 4 and 5.
On the synchronized sheet at time n,

```text
z_n=4+2 theta(n-1) mod 5.
```

Only b,d,e fire. Direct substitution gives the complete table:

| theta(n-1) | theta(n) | letter | raw linear part |
|---|---|---|---|
| 0 | 0 | e | -I |
| 0 | 1 | b | -B |
| 1 | 0 | b | -B |
| 1 | 1 | d | -I |

Thus b does carry differences between disjoint raw coordinates. There is
no blanket no-write claim here. For two same-time synchronized states,
however, the sequence of letters is identical and affine offsets cancel.
Since B^2=I, their k-step difference obeys

```text
Delta x_(n+k)=(-1)^k B^(theta(n-1) XOR theta(n+k-1)) Delta x_n.
```

The parity telescopes because b occurs precisely at a clock-bit change.
The same formula holds independently in each of any m common-clock cells.

For every k>0 and any requested lower bound N, choose j so large that
2^j>k, n=2^j-k+1>=N, and j=1+theta(k-1) mod 2. The j-bit binary
expansion of 2^j-k is the complement of that of k-1. Consequently

```text
theta(n-1)=j-theta(k-1) mod 2=1,
theta(n+k-1)=theta(2^j)=1.
```

At this explicit arbitrarily late n, the complete raw difference map is
(-1)^k I. No coordinate acquires a difference that it lacked at the start.
This all-k proof is independent of the finite clock audit.

## 3. No realization in the complete literal-product class

Fix any finite m>=1 and k>=1. The clock-preserving encoding required by
the source contract is explicitly Enc(n,y)=(n,e_n(y)); native clock shifts
depending on y are not admitted. This spells out the original #1629
clock condition and the preregistered single common clock, not an added
restriction on the checkpoint encoding. Each e_n may be arbitrary,
nonlinear and different at different n. No polynomial, coordinatewise,
affine, dimension-minimal or fixed-chart assumption is made.

Suppose faithful full-state decoding and the frozen repeated equation
hold for all n>=3 and all y in Y_(8,3). Put a=ceil(9/k). For every
n>=3+a*k and every y, bijectivity of F_P gives

```text
Enc(n,y)=V_m^(a*k) Enc(n-a*k,F_P^(-a)y).
```

The inherited TM-SHEET-SYNCHRONIZING-GRAPH theorem says that every actual
nine-tick block sends all initial sheet labels to the synchronized graph.
Therefore EVERY encoded checkpoint in every cell at such an n is
synchronized. This is true even if early encoded slices were not
origin-reachable or were deliberately outside the usual prepared chart.

Choose the explicit n in section 2 with N=3+a*k. At this n, encode the
two reference witness inputs. By the frozen source-local preparation
criterion they agree at every raw coordinate outside the fixed source
set S_N. By section 2 their outputs still agree at every coordinate
outside S_N. In particular their disjoint receiver projections R_N
coincide. Their current clock and every permitted external context also
coincide. A single present receiver function must therefore give equal
outputs. Full simulation and reference readback require +1 and -1.
This is a contradiction.

Hence NO_REALIZATION_IN_FROZEN_CLASS, for all finite m and positive k.
Adding finitely many auxiliary original cells cannot evade the theorem.
A family with a finite cell count depending on E is obstructed already
at its Y_(8,3) member if it obeys the same contract.

This is not the earlier fixed-checkpoint permanent-write theorem, nor
the finite-reader T obstruction. It permits nonlinear time-dependent
encoding/readout and requires only one nontrivial local record. The
all-n and common fixed-k requirements, fixed disjoint raw ports and
literal componentwise U are load-bearing. Sparse or variable-duration
calendars, independent cell clocks, CSUM or other coupling, coordinate
interventions, changing ports and different native extensions are not
classified. Original one-shot transfers at a selected preparation/time
are compatible with this negative result.

## 4. A complete target-independent correction class

Raw tau=e composed with d translates q by one and fixes the other five
coordinates. Choose a nonempty subset D of F5 and two fixed residues
delta_t, independently of P. On the entire union X_D of full sheets set
C_t=tau^delta_t f_t. Each literal g is a bijective affine map between
its full input and output sheets. Therefore C_t permutes X_D exactly
when z -> T_t(z)+delta_t is a permutation of D.

The image of T0 has size two, so |D|<=2. For a singleton {z}, the unique
choice is delta_t=z-T_t(z), giving five schemes. At size two D must be
a translate of {0,4}. Among the five cyclic adjacent pairs, {3,4} fails
T0 injectivity. Of the four survivors, {1,2} fails T1 injectivity and
{2,3} has T1 image {1,3}, whose difference cannot translate to an
adjacent pair. The two remaining schemes are exactly

| D | delta0 | delta1 | size of X_D |
|---|---|---|---|
| {0,4} | 0 | 3 | 6250 |
| {0,1} | 1 | 4 | 6250 |

Together with the five singletons this exhausts the whole frozen class.
Only the first maximal scheme leaves the theta=0 update unchanged.
No claim of minimal correction word length or complete physical
minimality is implied by this classification.

## 5. The retained two-sheet control

Select X=X0 union X4 and C_t=tau^(-2t) f_t. Its four branches are

| t | z | branch | resulting z |
|---|---|---|---|
| 0 | 0 | a | 0 |
| 0 | 4 | e | 4 |
| 1 | 0 | tau^-2 c | 0 |
| 1 | 4 | tau^-2 b | 4 |

The first two branches are involutions. Both b and c reverse q, so
g tau^r g=tau^-r for g=b,c. Consequently (tau^-2 g)^2=I.
Each C_t is an involution on all 6250 states, including every occupied
piston and fibre coordinate. Each sheet, hence its binary distinction,
is retained under arbitrary sequences of the two C_t, not just under
Thue-Morse. The map (n,x)->(n+1,C_theta(n)x) is injective and has the
inverse (n,x)->(n-1,C_theta(n-1)x) for n>=1. It is not surjective onto
the forward time-zero layer.

This is state-dependent branching, not an arbitrary target-cycle
matching. The raw equations define it before any P encoding exists.
It restores access to a and c by keeping the control outside the
synchronized {1,4} graph. The correction itself is an additional law.

## 6. Complete five-microtick carrier and inverse

To avoid treating four commands as instantaneous or external, introduce
one explicit alternative selection law using the existing n. At each
step put r0=n mod 5, m=n-r0 and t=theta(m). At r0=0 execute the literal
selector f_t; at phases 1,2,3,4 execute temporal dddd if t=0, eded if
t=1. Increment n after EVERY command. The phase is derived from n and
no additional dynamic register is omitted.

Define the entire legal slice using the following sets D_(t,r0):

| r0 | t=0 sheet set | t=1 sheet set |
|---|---|---|
| 0 | {0,4} | {0,4} |
| 1 | {0,4} | {1,2} |
| 2 | {2,3} | {1,2} |
| 3 | {0,4} | {0,1} |
| 4 | {2,3} | {2,3} |

The full carrier consists of all (n,x), n>=0, z(x) in D_(theta(m),r0).
Every legal slice contains 6250 checkpoints; it includes arbitrary
occupied coordinates, not only paths from the displayed witness.
These sets are direct images of whole sheets under at most four frozen
raw commands. They are not future P outputs or a target orbit table.

At r0=0 the selector is a bijection of its declared two-sheet source
onto the phase-1 set. Every later command is an affine involution on
the entire raw space. Thus each legal slice maps bijectively to the next.
After phase 4 the image is {0,4} independently of the old and new t,
which handles a bit change at the next block boundary.

For the inverse at n>=1 put ell=n-1, rprev=ell mod 5, mprev=ell-rprev,
tprev=theta(mprev). If rprev>=1, apply the same previous raw involution.
If rprev=0 and tprev=0, use a when the current z is 0, otherwise e
(current z=4). If rprev=0 and tprev=1, use c when current z=2 and b
when current z=1. Decrement n. This is a complete two-sided inverse
between the actual slices, including block starts. No branch, original
content or intermediate residue is erased.

Four d commands compose to I. Temporal eded is
(d composed with e)^2=tau^-2. Hence for every block start n=0 mod 5,

```text
V^5(n,x)=(n+5,C_theta(n)x).
```

There are exactly five microticks on both control branches, all counted.
This blocked n+5 law and the section-5 n+1 compound law have different
calendars. No equality theta(5n)=theta(n), change of native clock units,
or simulation of the whole compound sequence by clock rescaling is used.

## 7. Actual acquisition by an occupied local receiver

Take xplus=(1,1,0,0,3,0) on X0 and xminus=(1,1,0,0,2,0) on X4.
The sole differing coordinate is source q, index 4. The receiver is the
fixed raw projection (p4,p4p), indices 1 and 3. Its initial value (1,0)
is identical and occupied. Every other coordinate is also identical.

| t | full C_t(xplus) | full C_t(xminus) |
|---|---|---|
| 0 | (1,1,0,0,3,0) | (1,0,3,4,0,1) |
| 1 | (2,1,1,0,1,0) | (0,0,4,4,1,0) |

For either t the present receiver is (1,0) versus (0,4). With the
balanced residue representatives ell=(0,1,2,-2,-1), the same fixed read
rho=sgn(ell(p4)^2-ell(p4p)^2) gives +1 versus -1. It reads no source,
counter, history or prepared table. The five-microtick implementation
has exactly these outputs at its endpoints. The inverse restores all
original contents, including the old occupied receiver.

This two-input acquisition witness is available at every block start;
it does not say that a running receiver is autonomously renewed to the
same ready preparation after each use, that a late independent source
is loaded, or that the sign stays permanently readable. In particular
it is not the reference P witness: no bank, Weyl update or integer-shell
data has been encoded. The conserved distinction is the full-state
sheet z, not an assertion that the original source q value stays fixed.

## 8. Resource and scientific disposition

| Resource | Actual status in this construction |
|---|---|
| Six raw F5 coordinates and unbounded n | Original native carriers |
| Literal a,b,c,d,e and selector on the first microtick | Original native formulas |
| Commanded raw-word algebra | Admitted conditional algebra at its canonical scope |
| Choosing the two sheets and ready pair | Explicit new preparation restriction |
| q correction after the selector | NEW_DECLARED actuation |
| n mod 5 calendar and prior block-bit evaluation | NEW_DECLARED selection/control rule |
| Complete memory and inverse | All six coordinates and n retained; no hidden reset |
| Present receiver read | Explicit mathematical function on two current coordinates |
| Conserved physical energy / price of commands | Not supplied or inferred |
| Full Y_(8,3), bank/refusals and Weyl realization | Not supplied |

The negative result is NO_REALIZATION_IN_FROZEN_CLASS for the exact
literal class in section 3. The positive construction is
DECLARED_EXTENSION_ONLY, with the additional law isolated explicitly.
The predecessor's broader native admission and physical owners stay open.
No experiment, frequency sign, J/phi dynamical reading or L2-L6 claim
follows. The useful next target is the actual internal actuation and
complete resource account of this fixed correction, before using it to
compile P. Its exact formula can now be attacked instead of assuming an
unspecified general controlled gate.
