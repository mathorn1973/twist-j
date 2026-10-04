# Two structural boundaries for the original native update

NON-CANONICAL L1. **A: candidate-T. B: candidate-T**, by complete symbolic
proofs within `CONTRACT.md`. No new scientific program or census was run.
The proposed conclusions and earlier #1351 proof were exposed before this
work. Existing claims and their files are not rewritten.

## Native identities used in both proofs

Let a checkpoint be psi=(P,F), P=(p1,p4,p1p,p4p), F=(q,r), with
kappa=sum(P), z=kappa+q+r. Summing the four piston coordinates in the
public native generator definitions gives the following exact table:

| Generator | kappa' | F' | z' |
| --- | --- | --- | --- |
| a | kappa | (q,r) | z |
| b | -kappa | (-q,-r) | -z |
| c | 1-kappa | (1-q,-r) | 2-z |
| d | -kappa | (1-q,1-r) | 2-z |
| e | -kappa | (2-q,1-r) | 3-z |

For c the constants in the piston block sum to 6=1 in F5 and the two
r terms cancel; for d,e they sum to 10=0. Since the actual selector is
z+2 theta_n, the projection (n,P,F)->(n,kappa,F) commutes with U.
In particular two preparations with the same kappa, F and counter have
identical future fibre histories, irrespective of their other piston
coordinates. This is the registered native apparatus-history factor.

The induced total-trace maps for driver bits zero and one are, in input
order z=0,1,2,3,4,

    T0=(0,4,0,4,4),    T1=(2,1,1,3,1).

At common launch zero the first three driver bits are 0,1,1. Thus the
complete trace image is {0,4} at time one, {1,2} at time two, and {1}
at time three. Thereafter it remains a singleton, because the trace
update is a function of the trace and common counter alone. More
specifically T0 sends both 1 and 4 to 4, while T1 sends both to 1. Hence
for every origin-zero state and n>=3,

    z_n=4+2 theta_(n-1).

The selected generator on each such common reached sheet is b, d or e:
it is e for consecutive clock bits 00, d for 11, and b for unequal bits.
Every such fibre map is -F+d_n, where the common translation d_n is
(0,0), (1,1) or (2,1). These are inherited synchronization and common-fibre
continuation identities, already owned by the registered source claims
and the corresponding #1342/#1351 arguments. They are restated only to
make the two deductions auditable; no duplicate claim is proposed.

## A. No affine same-reader SUM at any common finite time

**Theorem A.** Use exactly #1351's independent affine product preparations
and the same fixed affine block readers:

    E(x,y)=(P0+v x,F0+w y), v!=0, w!=0,
    X(P)=A.P+a, A.v=1, a=-A.P0,
    Y(F)=B.F+b, B.w=1, b=-B.F0.

For no common finite t>=1 does the actual U^t from counter zero satisfy
X(P_t)=x and Y(F_t)=x+y on all 25 pairs. The first-three-time result
remains #1351's result; this is its all-finite-time corollary.

**Proof.** For each initial total trace z and fibre u, denote the resulting
fibre at time t by F_t(z,u). It is well-defined by the closed native
projection above. The actual selected words for initial z=0,1,2,3,4
are respectively ace, bbd, cce, dbd, ebd in temporal order. They are
consequences of the actual selector, not external controls. Their first
one, two and three steps have the affine fibre form

    F_t(z,u)=epsilon_t(z) u+k_t(z),

with the following sign profiles, already derived in #1351:

| t | epsilon_t(0),...,epsilon_t(4) |
| --- | --- |
| 1 | (+1,-1,-1,-1,-1) |
| 2 | (-1,+1,+1,+1,+1) |
| 3 | (+1,-1,-1,-1,-1) |

Every later step is the same fibre reflection for all reached initial
states at that time. Therefore, for every t>=3,

    F_t(z,u)=eta_t F_3(z,u)+c_t,
    eta_t=(-1)^(t-3), eta_3=1, c_3=0.

Indeed eta_(n+1)=-eta_n and c_(n+1)=d_n-c_n under the common map
F->-F+d_n. The translation c_t and sign eta_t depend on the common
native clock, not on x,y,z or u. In particular
epsilon_t(z)=eta_t epsilon_3(z) is nonconstant in z for every t>=3.
The displayed first two profiles are also nonconstant.

Put s=sum(v), rho=w_q+w_r, and z0=sum(P0)+q0+r0. The initial trace is

    z=z0+s x+rho y.

If s=0, the initial closed port at fixed y is independent of x, so every
future receiver-only reading is independent of x. It cannot equal x+y
for all x.

If s!=0, the change of labels (x,y)->(z,y) is a bijection of F5^2.
Because B.w=1, the proposed receiver output expressed in these labels is

    B.F_t(z,F0+w y)+b
      =epsilon_t(z)y+epsilon_t(z)B.F0+B.k_t(z)+b.

The demanded value is

    x+y=s^-1(z-z0)+(1-rho/s)y.

For each fixed z, equality for y=0 and y=1 forces

    epsilon_t(z)=1-rho/s.

The right-hand side is independent of z, contradicting the nonconstant
sign profile for every t>=1. Thus the receiver equation alone fails for
every candidate and every common finite time. This excludes its
conjunction with source retention without changing that requirement. QED.

The reader may be chosen when choosing the candidate and target time;
the proof still quantifies over every such choice. It does not allow a
reader depending on the original input, a history, or an input-dependent
time. The post-synchronization step is used only on actually reached
origin-zero sheets, not arbitrary checkpoints assigned a late counter.

## B. No exact checkpoint closure of a faithful fixed product code

**Theorem B.** Let P:F5->F5^4 and F:F5->F5^2 be arbitrary injective maps,
without an affine restriction, and let E(x,y)=(P(x),F(y)). There is no
common finite t>=1 for which

    pr_checkpoint U^t(0,E(x,y))=E(x,x+y)

holds for every x,y in F5.

**Proof.** Let kappa(x)=sum(P(x)). Suppose the displayed equality holds.
If kappa(x1)=kappa(x2), then at any fixed y the two initial closed ports
(kappa(x1),F(y)) and (kappa(x2),F(y)) agree. The actual future fibres
therefore agree. By the proposed endpoint equation their values are
F(x1+y) and F(x2+y). Injectivity of F gives x1=x2.

Thus kappa:F5->F5 is injective, hence bijective. Fix any y0. The total
traces of the five checkpoints E(x,y0) are

    kappa(x)+q(y0)+r(y0), x in F5,

so they exhaust F5. The entire code set C=E(F5^2) consequently contains
all five trace values.

SUM(x,y)=(x,x+y) permutes the label set, with inverse (x,y)->(x,y-x).
The proposed exact checkpoint closure therefore implies

    {pr_checkpoint U^t(0,c): c in C}=C.

Yet every origin-zero native checkpoint at time t belongs to a set whose
trace image is {0,4} if t=1, {1,2} if t=2, and a singleton if t>=3.
Its trace image cannot contain all five values. This contradicts the
equality of code sets. QED.

**Faithfulness and the minimal hypothesis actually used.** Proper fixed
block decoders for the two independent symbols require P and F to be
injective; conversely injectivity permits decoders on their image sets.
The proof above needs receiver injectivity directly, while source
injectivity would already follow from its derived injective kappa.

In fact the same argument works if F is merely nonconstant. If two
distinct x1,x2 had equal kappa, the closed-port equality and the proposed
closure for all y would give F(z)=F(z+x2-x1) for every z in F5. A nonzero
translation generates the additive group of F5, so F would be constant.
Thus nonconstancy is the weaker hypothesis sufficient for this proof.
The main declared class retains the natural stronger requirement that
both independent symbols be faithfully readable.

Some receiver hypothesis is essential. If it were removed, take

    P(x)=(x,x,-x,-x),    F(y)=(0,0).

Every initial trace is zero, so the first actual generator is a. It fixes
P(x) and F(y), and hence gives the displayed checkpoint equation at t=1
only because E(x,y)=E(x,x+y): the receiver symbol is not encoded at all.
This is a counterexample to an unqualified non-faithful formulation,
not to the faithful code theorem.

## Counter, launch and claim boundaries

Both theorems launch every input at counter zero and use one common
finite elapsed time. The real final state in Omega has counter t.
Theorem B deliberately asks for equality only after the named checkpoint
projection. It does not erase or reset the counter. Requiring equality
of complete states to (0,E(x,x+y)) would fail trivially because t>0 and
would not be the substantive claim proved here. No changing code E_n,
input-dependent stopping time or extra register is admitted.

Theorem B excludes exact return to the same product code with permuted
labels; it does not exclude every nonlinear endpoint reader that decodes
SUM from states lying outside that code. Theorem A excludes the original
affine same-reader class without requiring exact code closure. These are
two different complete classes, not a blanket impossibility claim for
every native contact. Other common launch contracts are not classified
here. Nothing changes #1351, #1342 or the existing post-synchronization
owners, and no physical carrier, energy, inverse, renewal, apparatus,
occurrence or #1349 contact condition is supplied.
