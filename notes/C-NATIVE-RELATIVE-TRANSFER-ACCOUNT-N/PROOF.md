# Native one-shot transfer with a whole-prefix relative account

Status: **NON-CANONICAL analytical result, L1**. No Canon promotion.
Contract/source pin: d5aa5c84da6c7115ca3c5be3c48b4da7faa96c8f.
Source attribution and exact commits: [SOURCES.md](SOURCES.md).

The actual original native step already writes into a receiver. This is
the canonical U-NATIVE-SOURCE-RECEIVER-RECORD, not a new chosen contact.
We give its explicit raw occupied-input specialization and a conserved
relative account on a larger, precisely declared pair carrier. The
account is not selected physical energy and does not implement the paid
working machine of #1612/#1615. Section 8 shows why merely adding
independent native copies cannot repair #1617's frozen timing.

All state arithmetic is in F5 unless a balanced integer lift, real cost
or counter is explicitly used. Every argument below is analytical; no
finite enumeration is needed.

## 1. Original dynamics and comparison carrier

Write x=(a,b,c,d,q,r), where the first four coordinates are respectively
(p1,p4,p1p,p4p), and z=a+b+c+d+q+r. To avoid collision with other
canonical quotients, call the controller triple Gamma(x)=(z,q,r).
The existing counter n gives theta_n=popcount(n) mod 2. The actual letter
is indexed by z+2 theta_n in the ordered alphabet (a,b,c,d,e).
In the following table lower-case row labels are letters, not coordinates:

| Letter | Literal checkpoint image | Gamma image |
| --- | --- | --- |
| a | (b,a,d,c,q,r) | (z,q,r) |
| b | (-c,-d,-a,-b,-q,-r) | (-z,-q,-r) |
| c | (2-c,1-d+r,2-a,1-b-r,1-q,-r) | (2-z,1-q,-r) |
| d | (2-a,1-b,3-c,4-d,1-q,1-r) | (2-z,1-q,1-r) |
| e | (2-a,1-b,3-c,4-d,2-q,1-r) | (3-z,2-q,1-r) |

Take two independently evolving original checkpoints x and rho and one
common original counter. This explicitly declared comparison product has
no interaction between its copies. Its full state retains both checkpoints
and the counter. Define

\[
\mathcal C=\{(n,x,\rho):\Gamma(x)=\Gamma(\rho)\}.
\]

This is an added reference resource, not an assertion that one original
six-coordinate cell contains two cells. At each n there are
5^3 choices of Gamma and 5^3 choices of each piston vector in its fiber,
hence 5^9=1,953,125 pairs. Equal Gamma selects the same actual letter;
the last column proves that it remains equal. Thus C is forward invariant.
The reference is a present state evolved by U, not a simulation of a
target working history extracted from n.

Let delta=(a-a_rho,b-b_rho,c-c_rho,d-d_rho). Its sum is zero and the
q,r differences are zero. Subtracting the literal formulas gives

| Letter | delta image |
| --- | --- |
| a | (delta_b,delta_a,delta_d,delta_c) |
| b,c | (-delta_c,-delta_d,-delta_a,-delta_b) |
| d,e | -delta |

In particular the r-dependent shear in c cancels. This is the
single-letter proof of the signed-permutation corollary of #1430,
section 8.3, equation (25). It applies before synchronization as well as
after it, and to every pair in C, not only the preparation used below.

## 2. Whole-prefix relative conservation and exact block balance

Use the original coordinate split S=(a,c), M=(b,d), R=(b,d,q,r).
R is the actual receiver inside x. Choose one common even function
f:F5 -> R_{>=0} with f(0)=0 and define

\[
E_S^f=f(\delta_a)+f(\delta_c),\qquad
E_M^f=f(\delta_b)+f(\delta_d),\qquad
E_{\rm rel}^f=E_S^f+E_M^f.
\]

These are fixed readings of present coordinates of both copies. They do
not read n. The difference table proves on all of C that

\[
a:(E_S^f,E_M^f)\longmapsto(E_M^f,E_S^f),\qquad
b,c,d,e:(E_S^f,E_M^f)\longmapsto(E_S^f,E_M^f).
\tag{1}
\]

Thus every actual native step preserves E_rel, and the exact relative
transfer into memory is

\[
W_f:=E_M^{f\prime}-E_M^f=-\big(E_S^{f\prime}-E_S^f\big).
\tag{2}
\]

At a, W_f=E_S^f-E_M^f; otherwise W_f=0. This is a bookkeeping identity
with a declared readout, not an identification of W_f as physical work.
The common q,r motion and common part of the piston motion disappear in
the difference. No value for their physical cost has been supplied.

For an explicit nonnegative integer account choose the balanced lift
ell(0,1,2,3,4)=(0,1,2,-2,-1) and f_2(t)=ell(t)^2. Oddness of ell under
negation makes (1) exact, without approximate arithmetic. E_rel then
vanishes precisely when the two full checkpoints agree. It is positive
on their nonzero contrast, not positive definite on the full apparatus
state: the entire diagonal x=rho has zero account.

## 3. An independently occupied raw receiver

For every independent lambda,mu in F5 prepare

\[
x_{\lambda,\mu}(0)=(\lambda,\mu,-\lambda,-\mu,0,0),
\qquad \rho(0)=0.
\tag{3}
\]

For fixed mu only the source depends on the new message lambda.
The same evolving reference works for all 25 preparations. Actual bits
011 select a,c,e, as is checked by the trace at each input:

| n | x_(lambda,mu)(n) | Gamma | next actual letter |
| --- | --- | --- | --- |
| 0 | (lambda,mu,-lambda,-mu,0,0) | (0,0,0) | a |
| 1 | (mu,lambda,-mu,-lambda,0,0) | (0,0,0) | c |
| 2 | (2+mu,1+lambda,2-mu,1-lambda,1,0) | (2,1,0) | e |
| 3 | (-mu,-lambda,1+mu,3+lambda,1,1) | (1,1,1) | b |

The reference is the same table with lambda=mu=0; it is not held fixed
at zero after the first step. The actual first a swaps both raw piston
blocks. It sends the old memory mu back into the source and the new
source lambda into memory. At mu=0 the source is exactly zero at n=1;
later it agrees with the reference source and need not itself be zero.

The set X14={z in {1,4}} is invariant under either bit. At z=1 the
selected letters are b,d; at z=4 they are e,b. A selected b negates z;
a selected d/e preserves it. No a or c is selected in this tail.
The difference blocks (t,-t) are fixed by the negative swap of b and
negated by d/e. Consequently for every n>=1 a common sign epsilon_n
satisfies

\[
\delta_S(n)=\epsilon_n\mu(1,-1),\qquad
\delta_M(n)=\epsilon_n\lambda(1,-1),
\]

with epsilon_1=epsilon_2=1 and epsilon_3=-1. Therefore

\[
(E_S^f(0),E_M^f(0))=(2f(\lambda),2f(\mu)),
\qquad
(E_S^f(n),E_M^f(n))=(2f(\mu),2f(\lambda))\quad(n\ge1).
\tag{4}
\]

The net first-step transfer is 2(f(lambda)-f(mu)), including negative
and zero values for occupied input. It is not always an emission.

This is a raw occupied-input family. Its initial completion reader is
BLANK for every mu. It is not a reset of a previously completed
PRESENT(mu) record. Independently occupied native writing already appears
in #1430; (3) supplies an explicit specialization on this literal
coordinate split together with (4), not a first occupied-writer claim.

## 4. Two fixed present-state readers retain both labels

Use exactly the canonical receiver reader, for R=(b,d,q,r):

\[
B=b+d,\quad D=b-d-1,\quad \widehat z=3B+q+r,
\]

\[
\operatorname{ready}(R)\iff B\in\{2,3\},\ \widehat z\in\{1,4\},
\qquad
\operatorname{read}_R(R)=
\begin{cases}
\mathrm{BLANK},&\text{not ready},\\
\mathrm{PRESENT}(3-B\widehat zD),&\text{ready}.
\end{cases}
\tag{5}
\]

BLANK differs from PRESENT(0). On the four cuts in the table,
(B,zhat)=(0,0),(0,0),(2,2),(3,1). At n=3, D=1-2lambda, so (5)
returns lambda. Let A=a+c. At this cut A=1=2B. Selected b,d,e negate
both A and B, preserving A=2B and therefore z=zhat. Their remaining
actions are

| Selected branch | B image | D image | z image |
| --- | --- | --- | --- |
| b | -B | D | -z |
| d at z=1, e at z=4 | -B | -D | z |

Thus BzD is invariant and readiness persists. For every lambda,mu,

\[
\operatorname{read}_R(x_{\lambda,\mu}(n))=
\begin{cases}
\mathrm{BLANK},&0\le n<3,\\
\mathrm{PRESENT}(\lambda),&n\ge3.
\end{cases}
\tag{6}
\]

The actual receiver reader uses no reference cell, source, counter,
history or invocation time. The proof even holds for every future binary
word after the actual prefix, which does not add a control port to U.
Three is the latency of this completion mark, not minimum transfer time.

The old mu also has a fixed present-state reader on the declared tail:

\[
C=a-c-2,\quad z_S=4A+q+r,\qquad
\operatorname{read}_S(a,c,q,r)=1+2Az_SC.
\tag{7}
\]

At n=3, A=z_S=1 and C=2-2mu, so (7) equals mu. Since B=3A persists,
z_S=z. Under b, A and z negate while C is fixed; under selected d/e,
A and C negate while z is fixed. Hence AzC is invariant. Equation (7)
returns mu at every n>=3. Its correctness is asserted only on this
prepared tail, although the formula is a total finite function.
It uses the source pistons and shared q,r, not the receiver pistons.
Together (5) and (7) recover both labels after the exchange. No old
content has been erased.

## 5. Exact inverse scope, not a global reversal of selected U

Each displayed letter is an involution on the full checkpoint. With its
input Gamma and bit fixed, the selected letter maps that whole input
fiber bijectively onto its output fiber. Applying that same letter to
both output copies recovers the input pair.

More explicitly, fix an initial triple Gamma_0 and let Gamma_n be its
actual deterministic triple history. At every n the slice

\[
\mathcal C_n(\Gamma_0)=
\{(n,x,\rho):\Gamma(x)=\Gamma(\rho)=\Gamma_n\}
\]

has 125^2=15,625 pairs. The original product step is a bijection from
this slice onto the next. Its inverse uses the letter selected on the
known preceding slice. This covers the prefix and every occupied
continuation in (3), not only a first blank emission.

This is not a global inverse on the union of controller slices. The
selected trace maps can merge different input traces. Nor does applying
an inverse letter constitute its allowed forward re-selection at a later
time. In particular repeating a at n=3 would replace the actually
selected b. The tail never returns to the z=0 input family. No reset,
fresh independent input, reusable ready receiver or growing archive has
been constructed. The canonical continuation boundary is unchanged.

## 6. Conservation does not select physical energy

In the declared common-even one-coordinate family, f is determined by
two nonnegative numbers f(+-1) and f(+-2). After f(1)=1 there remains
an unconstrained relative weight. This is a classification of this
declared family only, not of all conserved observables.

For the same preparations, reference, native transitions and readers,
compare f_2(t)=ell(t)^2 with f_4(t)=ell(t)^4. For mu=0 their transferred
accounts are

| lambda | 0 | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- | --- |
| 2 f_2(lambda) | 0 | 2 | 8 | 8 | 2 |
| 2 f_4(lambda) | 0 | 2 | 32 | 32 | 2 |

They have the same unit calibration and both satisfy the whole-prefix
conservation, occupied exchange, slice inverse and fixed record. They
are inequivalent on this same family. No choice is justified by matching
a target mass, energy or output. The second account is a sum of fourth
powers of individual coordinates, not the square of a block energy.

At lambda=mu=0 the two complete copies agree at every cut: every E_f
is zero. Yet (6) changes from BLANK to PRESENT(0). This supplies an
exact counterexample to interpreting E_rel as a strictly positive cost
of every completed record. It does not rule out a zero-cost reversible
operation; it shows that this account assigns no positive cost to that
completion mark. The common apparatus motion is removed
by subtraction. Accounting for a transported contrast is different from
pricing reference preparation, readiness, the counter or the apparatus.

## 7. The absence code is outside this relative account

The canonical sixth absence preparation x_empty=(0,0,1,0,0,0) starts
with Gamma=(1,0,0), while rho(0)=0 has Gamma=(0,0,0). It is not in C.
Its valid canonical permanent-BLANK statement is not an additional case
of the conservation theorem.

An explicit check of this boundary is possible without an enumeration.
The absence trajectory has checkpoints (0,0,1,0,0,0),
(4,0,0,0,0,0), (0,0,1,0,0,0) at cuts 0,1,2. The reference has zero
at cuts 0,1 and (2,1,2,1,1,0) at cut 2. The squared balanced piston
difference is respectively 1,1,7. Thus extending this same invariant
unchanged to the six-code present/absence family would be false.
Choosing a different reference for absence would define another context,
not establish conservation on the frozen comparison above.

## 8. Any number of uncoupled copies retains the old timing obstruction

For completeness the original trace maps for bits 0 and 1, in input
order z=0,1,2,3,4, are

\[
\tau_0=(0,4,0,4,4),\qquad \tau_1=(2,1,1,3,1).
\]

The actual prefix 011 sends every initial trace to 1, independently
of q,r and the pistons. At cuts 3 and 4 the actual bits are 0 and 1.
Starting at trace 1 they select b then b, because the intermediate
trace is 4. Since the full checkpoint letter b is an involution,

\[
\boxed{x_5=x_3\quad\text{for every original checkpoint started at }n=0.}
\tag{8}
\]

This is an elementary corollary of canonical synchronization. For every
finite number of independent copies, with arbitrary correlated initial
preparations but the same origin-zero counter, their full checkpoint
tuple satisfies Psi_5=Psi_3. Including any additional unchanged register
does not alter this equality. Every fixed counter-blind reading of that
tuple therefore gives the same output at these two cuts.

In particular no such product implements #1617's frozen requirement
of BLANK at native cut 3 and HIT at cut 5. More independent copies can
increase capacity without removing this timing obstruction. Equation
(8) is not equality of the complete autonomous state: its counter has
increased by two. It does not exclude counter-dependent readers,
other cuts, macrostep protocols, stored history with its own updates,
or genuinely coupled dynamics. None is supplied by simply taking a
product of original U copies.

The positive result (6) has already completed its record at cut 3 and
keeps it at cut 5, so it does not contradict (8). Its message changes
the receiver during the original unsynchronized transient, before the
frozen starting cut of #1617.

## 9. The precise remaining construction

The supplied native mechanism is now explicit: a two-piston source,
a four-coordinate receiver including its q,r reference, and the actual
first a exchange. A real second native copy allows the exact relative
account (1)--(4); the fixed readers retain both independent labels.
It introduces no arbitrary chosen contact letter, but it does declare
the comparison product, its preparation and the family of readings.

To retain #1617's timing, an enlarged memory update must actually break
the equality seen by the reader. For example, write Psi for the full
product checkpoint at cut 3 and B for simultaneous b. If an additional
memory m updates by h_3(Psi) at cut 3 and h_4(B Psi) at cut 4 while
the old checkpoints still execute b,b, then the necessary distinction is

\[
\operatorname{Read}(\Psi,
 h_4(B\Psi)(h_3(\Psi)(m_{\rm ready})))
\ne \operatorname{Read}(\Psi,m_{\rm ready}).
\tag{9}
\]

An idle register fails (9). The h maps, their admissibility, previous
memory contents, resource balance and inverse would need an actual
construction; (9) does not choose them. Coupling the original checkpoints
instead would require its own specified transition and audit.

To make the present positive construction close physics would additionally
require a selection/occurrence rule for the reference preparation and
the energy reading, a physical account for common apparatus motion,
and a native mechanism for new arrivals and repeated writing. No bridge
from (2) to the working payment 10, the Dirac-channel gap
2(sqrt(1+m^2)-m), phase energy or inertial mass is supplied.
Those quantities are not equated. The finite m/arctan(m) discrepancy
is neither erased nor explained by this note.
