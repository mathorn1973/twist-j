# Fixed nonlinear native receiver from origin zero

PUBLIC / NON-CANONICAL / L1. Prospective analytical candidate-T, not an
independently accepted theorem. A. M. Thorn. Original work Apache-2.0.
This proof and its exact candidate were exposed before the new audit.
The audit cannot change the equations below after its public pin.

## 1. Exact question and admitted mathematical class

Use the unchanged native U on N0 x F5^6 with theta_n=popcount(n) mod2,
selector j=(sum(x)+2 theta_n) mod5, and the five original generators in the
current Canon, Native conventions. Coordinates are x=(a,b,c,d,q,r).
The constructor chooses one global bijection Phi:F5^6 -> F5^2 x F5^4,
one fixed total semantic reader on F5^2 and a source preparation at n=0.
The receiver is the FIRST TWO current Phi coordinates at every tick.
No time or previous-state argument, decoder feedback, added register, or
new transition is allowed. Both message labels are chosen initially.

All coordinate functions and their inverse may be polynomial over F5.
On a finite field every map is polynomial as a function, so this broad
class does not by itself provide physical admissibility or locality.
Its nonempty existence question is distinct from uniqueness and from a
physically justified class. The affine subfamily has the prior no-go in
#1519/#1520; no older claim or source is altered here.

Write A=a+c, B=b+d, C=a-c-2, D=b-d-1 and z=A+B+q+r.
The affine coordinate chart alpha=(z,A,B,C,D,q) has inverse

    a=3(A+C+2), c=3(A-C-2),
    b=3(B+D+1), d=3(B-D-1), r=z-A-B-q.

All arithmetic is in F5. The factor 3 is the inverse of 2.
The generator trace actions are z,-z,2-z,2-z,3-z respectively.
An involutive generator does not imply global injectivity of U.

## 2. Total nonlinear coordinate change, with no singularity

Set tau(z,A)=z A^3+1-A^4. For z in {1,4}, it is nonzero: if A=0 it
is one, and if A!=0 then A^4=1 and tau=z A^-1. Define

    z=0:    Phi(x)=(z,C,A,B,D,q),
    z=2:    Phi(x)=(z,q,A,B,C,D),
    z=1,4:  Phi(x)=(z,tau D,A,B,C,q),
    z=3:    Phi(x)=(z,D,A,B,C,q).

From y=(z,t,s0,s1,s2,s3) recover A=s0, B=s1 and

    z=0:   C=t,  D=s2,              q=s3,
    z=2:   C=s2, D=s3,              q=t,
    z=1,4: C=s2, D=t*tau(z,A)^3,    q=s3,
    z=3:   C=s2, D=t,               q=s3.

Then apply alpha^-1. Since tau^3 is its reciprocal on the two relevant
sheets, substitution proves BOTH inverse compositions on all F5^6,
including A=0. In particular every receiver value has exactly 5^4=625
full-state preimages. No desired-output lookup table is used in this inverse.

Let e_j(z)=1-(z-j)^4. It equals one on z=j and zero on the other four
sheets. The receiver R=(z,T) has the single fixed polynomial expression

    T=e_0 C+e_2 q+(e_1+e_4)(z A^3+1-A^4)D+e_3 D.

It has total degree at most nine in the affine coordinates (and hence in
raw coordinates), not a claimed minimum degree. The remaining chart and
inverse coordinates also have polynomial expressions by the same selectors.
State-dependent case notation describes one fixed global map, not a change
of reader between ticks. This algebraic re-coordination is not a new
physical actuator or a proof that the original raw port can compute it.

## 3. Product preparation and exact origin-zero prefix

For every lambda,mu in F5 prepare once

    E(lambda,mu)=(3(lambda+3),3(mu+1),3(-lambda-1),3(-mu-1),0,1).

Directly alpha(E)=(2,1,0,lambda,mu,0) and
Phi(E)=(2,0,1,0,lambda,mu). Thus the ENTIRE two-coordinate receiver
is common, (2,0), while the complement has independent entries lambda,mu.
Also the raw first piston pair (a,c) depends only on lambda, the second
(b,d) only on mu, and (q,r)=(0,1) is common. No source-sum answer or
future output history is precomputed into the ready receiver.

The actual origin-zero driver prefix is 0,1,1. Using the trace table:

| n | selected next generator | z | A | B | C | D | q |
|---|---|---|---|---|---|---|---|
| 0 | g2 | 2 | 1 | 0 | lambda | mu | 0 |
| 1 | g2 | 0 | 3 | 2 | lambda | mu+2 | 1 |
| 2 | g4 | 2 | 1 | 0 | lambda | mu | 0 |
| 3 | tail | 1 | -1 | 0 | -lambda | -mu | 2 |

Since g2^2=id, x2=x0 as COMPLETE checkpoints. Nevertheless (2,x2) is
not (0,x0), and theta_2 differs from theta_0. The new third transition
therefore does not assert an autonomous reset of the whole Omega state.
Both x1 and x2 are actual descendants of the specified n=0 preparation;
no stipulated predecessor-free late launch is used.

Define one fixed total G on all 25 receiver values:

    G(z,t)=BLANK if z in {2,3}; PRESENT(t) if z in {0,1,4}.

PRESENT(0) is different from BLANK. The exact receiver prefix is

    (2,0), (0,lambda), (2,0), (1,mu),

so G reads BLANK, PRESENT(lambda), BLANK, PRESENT(mu).
The table proves the entire receiver is restored at n=2, not merely its
semantic label. Both messages are already present in the initial complete
state. No later independent loading or source clearing is claimed.

## 4. Permanent retention from an invariant, not simulation length

On X14={z=1 or z=4}, the actual selected generators are g1 or g3 when
z=1, and g4 or g1 when z=4. Direct substitution gives

    g1:       (z,A,B,C,D) -> (-z,-A,-B,C,D),
    selected g3/g4:       -> (z,-A,-B,-C,-D).

Consequently A!=0 remains so, and both ratios

    I_C=z C/A, I_D=z D/A

are invariant for EITHER driver choice on every point of X14 with A!=0.
This is a 5000-state domain. No probabilistic or recurrence premise is
needed. At x3 these ratios are lambda and mu. On this domain T=I_D,
and z remains 1 or 4. Therefore G(R(x_n))=PRESENT(mu) for every n>=3.
I_C also preserves the first label, but reading it is a separate full-data
reading, not a second private receiver or an assertion that R still reads
both labels at once.

A more specific finite certificate contains, for each pair, the 20 states
parameterized by A in {1,4}, z in {1,4}, q in F5, with

    B=0, C=lambda A/z, D=mu A/z.

Apply alpha^-1. These sets are disjoint for the 25 message pairs, have
500 states in all, contain x3 and are closed under BOTH selected controls.
One-step closure plus induction proves all-time retention. A regression
through n=1024 is not the proof and implies no extra long-time statement.
This does not contradict the synchronized permanent-write obstruction:
the BLANK x2 has z=2, outside X14; the label is already present at its
first synchronized checkpoint x3 and never changes thereafter.

## 5. Exact comparison boundaries

### Nonlinear is essential for this contract

Take x=E(0,0), y=E(0,1). R(x)=R(y)=(2,0), but
R(g4 x)=(1,0) and R(g4 y)=(1,1). If R=Lx+h were affine, since
g4 x=-x+t4, these two latter receiver values would be equal. Thus R
is not affine. This is how it escapes the earlier all-affine bound;
nonlinearity of G alone would not suffice under that earlier bound.

### Coordinate minimum and non-autonomy

A single F5 coordinate has only five values, while the fixed semantic
alphabet contains BLANK and all five PRESENT labels. No fixed total
reader can return all six from it, independent of preparation or reader
nonlinearity. This construction attains two coordinates with a complete
bijective complement. The minimum is in the declared F5-coordinate class,
not a bit count, physical dimension, polynomial degree or acquisition cost.

There is no next-receiver map from R alone even with the common time known:
E(0,0) and E(1,0) have the same R at n=0, while their next R are (0,0)
and (0,1). The receiver interacts with its omitted coordinates. No claim
that R is an autonomous native factor is made.

### The raw (q,r) port never receives the messages in this preparation

The quotient (z,q,r) closes for every generator:

    g0: (z,q,r); g1: (-z,-q,-r); g2: (2-z,1-q,-r);
    g3: (2-z,1-q,1-r); g4: (3-z,2-q,1-r).

The selector depends only on z and the common driver. All preparations
start at quotient (2,0,1); hence (z,q,r) is message-independent forever.
The new R is a nonlinear mixed-coordinate subsystem, not a raw-port
source-to-(q,r) transfer. Its trace-controlled selection of C, q and a
normalized D must not be relabelled physically source-blind or local.

### Not physical forcing or unlimited renewal

This proves one candidate mathematical possibility on the original U,
not uniqueness or independent physical admission of Phi, R, G or E.
The source coordinates remain informative and the whole counter does not
return. No energy, rational wave F, bounded H_B, source depletion, new
message insertion, repeatable late reset, Born law or higher-layer claim
is involved. Showing a function has a low-degree formula does not prove
a native device can evaluate it. Further physical permission is a distinct
question, not a condition to erase this scoped existence result.

## 6. Self-review and exact falsification points

The proof checks A=0 separately instead of dividing by zero; specifies G
on the unused z=3 sheet; retains every complement coordinate; checks actual
selectors rather than applying a freely selected word; distinguishes full
checkpoint reset from counter reset; proves retention by invariant closure;
and identifies the changed access class explicitly. Failure at any displayed
identity, any chart inverse, any message including zero, or any tail edge
refutes that frozen claim. No post-pin revision may silently repair it.
The same author's matrix/formula audit is not independent authorship.
A separate source-blind-code reviewer remains required for acceptance.
