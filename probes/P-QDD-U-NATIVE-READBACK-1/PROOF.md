# P-QDD-U-NATIVE-READBACK-1: proof contract

**Prospective, proof-first, result-exposed, L1 only.** These formulas and predictions were obtained privately before this formal candidate. This document supplies proofs; it does not report a new formal run. Exact public source identity and dependencies are frozen in the companion PREREG.md and this same pin.

Public overlap is explicit. KERNEL-Z6-SYNCHRONIZATION [T], sealed P-KERNEL-Z6-SYNCHRONIZATION-1 (issue160), already establish origin-zero synchronization and the exact five-to-one sheet structure. TM-SHEET-SYNCHRONIZING-GRAPH [T] and TM-CHECKPOINT-HULL-STABLE-IMAGE [T] cover synchronizing words and universal hull stability. Those results are inherited, not new claims here. The new targets are an explicit five-label chart and jump formula, and QDD-specific exact readback, memory and preparation bounds. The five-state full-head bound is an immediate memory corollary of the inherited fibers.

## 1. Fixed objects and inherited sheet structure

All checkpoint arithmetic is in F5. Write x=(p1,p4,p1p,p4p,q,r), z=sum(x), theta_n=popcount(n) mod 2. On Omega=N0 x F5^6 the native law is

    U(n,x)=(n+1,G_(z+2theta_n)(x)),  G=(a,b,c,d,e),

where

    a(x)=(p4,p1,p4p,p1p,q,r),
    b(x)=(-p1p,-p4p,-p1,-p4,-q,-r),
    c(x)=(-p1p+2,-p4p+1+r,-p1+2,-p4+1-r,1-q,-r),
    d(x)=(2-p1,1-p4,3-p1p,4-p4p,1-q,1-r),
    e(x)=(2-p1,1-p4,3-p1p,4-p4p,2-q,1-r).

Each generator is an involution. Summation gives the native phase maps

    f0=(0,4,0,4,4),  f1=(2,1,1,3,1),

listed in input-phase order0,1,2,3,4. Let F_n(x0) be the checkpoint after n ticks from (0,x0). The initial bits011 give z3=1 for every head. Each initial phase sheet maps bijectively onto this sheet, so F3 has3125 fibers, each containing five heads, one per initial phase. These are inherited public facts; the table also verifies them directly.

For n>=3 the reachable sheet is

    X_n={x : z(x)=4-3theta_(n-1)}.

The selected generator is e on adjacent bits00, b on01 or10, and d on11. Each such transition is a bijection X_n -> X_(n+1). Hence no mergers occur after n=3.

## 2. Explicit conserved five-label chart

Define the integer function

    S(0)=0, S(M)=M-S(floor(M/2))
        =M-floor(M/2)+floor(M/4)-floor(M/8)+... .

The finite alternating sum counts switches theta_j!=theta_(j-1) for1<=j<=M. Indeed theta_(2j)=theta_j and theta_(2j+1)=1-theta_j; every odd-index adjacent pair switches, while a pair at2j switches exactly when the pair at j does not. This gives S(M)=M-S(floor(M/2)).

For n>=3 let

    t_n=(-1)^(n-3), h_n=(-1)^(n+theta_(n-1)),
    N_n=S(floor((n-1)/2))-1.

On X_n define L(n,x)=(alpha,beta,gamma,delta,epsilon) by

    alpha=t_n(p1+p1p), beta=t_n(p4+p4p),
    gamma=h_n(p1-p1p-2), delta=h_n(p4-p4p-1),
    epsilon=t_n*r-N_n.

All five labels are in F5. Their inverse, for any l in F5^5, is

    A=t_n*alpha, B=t_n*beta,
    C=2+h_n*gamma, D=1+h_n*delta,
    p1=3(A+C), p1p=3(A-C),
    p4=3(B+D), p4p=3(B-D),
    r=t_n*(epsilon+N_n),
    q=(4-3theta_(n-1))-A-B-r.

Here3 is the inverse of2 modulo five. Substitution proves both inverse identities, and the q formula gives exactly X_n.

To prove invariance, put A=p1+p1p, B=p4+p4p and V=(p1-p1p-2,p4-p4p-1). Each native tail generator sends A,B to -A,-B. Generator b fixes V, while d,e negate it. Set kappa_n=1 if theta_n=theta_(n-1), otherwise0. Then

    V_(n+1)=(-1)^kappa_n V_n,  r_(n+1)=-r_n+kappa_n.

The defining signs give t_(n+1)=-t_n and h_(n+1)=(-1)^kappa_n h_n. For odd n, kappa_n=0 and N_(n+1)-N_n=0. For n=2m, kappa_n is the switch indicator at m, t_n=-1, and the S recurrence gives N_(n+1)-N_n=kappa_n. Thus in all cases

    N_(n+1)-N_n=-t_n*kappa_n.

Every component of L is therefore invariant. The synchronized native law is conjugate to

    (n,l) -> (n+1,l).

This chart is a mathematical function of the current checkpoint and existing clock. It is not a statement that individual checkpoint coordinates are constant or that extra registers have appeared in U.

A synchronized jump to time m>=n is encode(m,L(n,x)). Computing theta and the finite S sum takes O(log m) integer arithmetic steps, with bit cost dependent on the sizes of those integers. An arbitrary start first uses the inherited finite synchronization result and then this chart. The formal finite audit here starts at the registered origin-zero heads; no new arbitrary-start bound is proposed and the chart does not speed up physical time.

## 3. Complete factor criterion for native readback

Let rho be an initial record on a preparation set A subset F5^6. For any n>=3 there is a function d_n of the native current checkpoint such that

    d_n(F_n(x0))=rho(x0) for all x0 in A

if and only if

    F3(x0)=F3(y0) implies rho(x0)=rho(y0), for x0,y0 in A.

Necessity follows because a deterministic evolution cannot separate merged inputs. For sufficiency, the chart recovers F3(x0) from (n,F_n(x0)); assign the common rho value to each admitted F3 fiber. This is a statement about the current native state. A registered decoder whose input is the entire head-retaining orbit may still read its original head directly.

## 4. Inherited registered QDD record and its equality

The public QDD-ALGEBRAIC-FACTORIZATION and QDD-DIRECT-RECORD-E-NONCONGRUENCE results supply the following record and sign-equality lemma; we restate their proof for the new readback application. The registered origin-zero QDD head map uses v=(ell(p1),ell(p4),ell(p1p),ell(p4p)), where ell=(0,1,2,-2,-1). Use its registered exact direct/factor equivalence; do not redefine the historical direct map. Let

    s=sum(v), G=I-11^T/5,
    m=v^T G v=sum(v_i^2)-s^2/5,
    wL=s^2/20, wH=sum(v_i^2)-s^2/4.

The five fields are support, m, the ordered pair(wL,wH), density vv^T G/m, and the normalized ordered pair(wL/m,wH/m). The exact zero encoding is ('ZERO_SUPPORT',0,(0,0),'ZERO_DENOMINATOR','ZERO_DENOMINATOR'); at support it is ('SUPPORTED',m,(wL,wH),('DENSITY',matrix),('NORMALIZED',(wL/m,wH/m))). All numeric entries are rational. These are the canonical direct-route string zero tags, not singleton Python tuple wrappers. Never divide by zero. G has eigenvalues1,1,1,1/5, so m=0 exactly when v=0.

**Full-record equality lemma.** Two five-field records agree exactly if and only if v'=v or v'=-v. The forward implication follows from equal positive m and equal density: multiply by G^(-1) to get vv^T=v'v'^T, which forces v'=+/-v. The zero case is unique. Conversely sign reversal preserves every field. Since ell is a bijection and ell(-a)=-ell(a), this is equivalently equality of the four field-valued pistons up to common sign. In particular there are(625+1)/2=313 possible complete records. This lemma is not true if one silently drops mass or density.

For a concrete native failure, take supported heads

    x=(4,1,0,0,0,0), x'=(2,1,1,2,1,0).

Their native selected generators are a and c, respectively, and both become(1,4,0,0,0,0) after one tick. Their balanced pistons are(-1,1,0,0) and(2,1,1,2). The respective(m,wL,wH) values are(2,0,2) and(14/5,9/5,1), so normalized LOW is0 versus9/14. By the factor criterion, no universal later-current-native-state reader returns even this original LOW weight on all supported heads. This does not invalidate the registered orbit-input decoder.

## 5. Exact three-state saved-class repair

With composition read right to left, the first-three-tick maps on initial phases0,1,2,3,4 are

    H0=eca, H1=d, H2=e, H3=dbd, H4=dbe.

These follow directly from the phase table and involutions. The inverse heads over y in X3 are therefore

    ace(y), d(y), e(y), dbd(y), ebd(y).

The second and third heads have identical four pistons because d,e differ only in q. The fourth and fifth also have identical pistons. Consequently save only

    c0=0 if z(x0)=0,
    c0=1 if z(x0) in{1,2},
    c0=2 if z(x0) in{3,4}.

Add the static label by the explicitly conditional extension

    U'(n,x,c0)=(U(n,x),c0).

For n>=3 recover y=F3(x0) through the chart, then evaluate QDD on ace(y), d(y) or dbd(y) according to c0. This recovers all five original fields. For n=0,1,2 enumerate only initial phases compatible with the current phase and saved class and reverse their selected involutions. All compatible heads give the same record: otherwise they would remain a conflicting same-class pair at n=3, contradicting the construction just proved.

Three added distinguishable states are necessary, even on supported heads. The common y=(0,0,0,1,0,0) has predecessors

    (0,4,0,0,2,2): LOW=1/16,
    (2,1,3,3,1,1): LOW=1/256,
    (4,4,4,0,4,4): LOW=3/8.

They have three distinct required records over the same native checkpoint. An additional alphabet of size two cannot distinguish them. The saved-class construction attains size three and is therefore minimal. This lower bound allows a more general evolving ancillary register: at the read time its alphabet still has to distinguish the three cases.

The new label is initialized from the initial head; it is not a native coordinate discovered inside U. The native projection is unchanged. Three labels preserve the QDD record but do not preserve every original head or make the whole extended evolution injective.

For full-head recovery, save z(x0) itself and choose the corresponding inverse H_z. The inherited five-head fibers show that an additional alphabet smaller than five cannot suffice. This achieves exact recovery on correctly initialized reachable slices, which are mapped bijectively to successive slices. The unconstrained map on all Omega x F5 still has native collisions at arbitrary equal tags. Recovery of an already determined fixed-origin trajectory needs no growing archive, but says nothing about independently writable new inputs.

## 6. Analytic maximum of6500 unaugmented preparations

Write the synchronized head y=(a,b,c,d,q,r), with sum(y)=1. Its three inverse piston classes are

    A=(d+3-r,c+4,b+4+r,a),             multiplicity1,
    B=(2-a,1-b,3-c,4-d),              multiplicity2,
    C=(-c,-d,-a,-b),                  multiplicity2.

Their QDD equality is exactly equality up to sign by the lemma above. All equations below are modulo five.

A never equals+/-B or+/-C. One direct check uses the first and fourth coordinate equations versus the second and third:

| Supposed equality | Incompatible requirements |
| --- | --- |
| A=B | r=0 and r=2 |
| A=-B | r=4 and r=3 |
| A=C | r=4 and r=1 |
| A=-C | r=2 and r=1 |

Also B=-C would require a+c=2 and a+c=3. The only possible coincidence is

    B=C iff a-c=2 and b-d=1.

This imposes two independent linear constraints on the five free coordinates of X3. There are exactly5^3=125 such fibers; all other3125-125=3000 fibers have three distinct records. Thus the full-record multiplicities are(4,1) in125 fibers and(2,2,1) in3000 fibers.

A preparation subset admits an unaugmented exact reader precisely when it chooses heads from at most one same-record class per fiber. Its maximum possible size is therefore

    125*4+3000*2=6500.

The bound is attained by selecting a largest class independently in each fiber. It is a cardinality optimum, not a privileged physical preparation rule.

The same maximum holds if every admitted head must be supported. In a fourfold class B=C, its piston cannot be zero: C=0 would force(a,b,c,d)=0, for which B=(2,1,3,4) is nonzero. In every other fiber at least one of B,C is nonzero, since they cannot both be zero. Hence a supported maximizing class always exists. The original domain has15625 heads, of which25 have all four pistons zero and15600 are supported. Restricting to6500 preparations changes that full registered domain.

## 7. Layer and proof limits

Every conclusion here is L1: exact native dynamics, current-state factorization, registered algebraic QDD records, and explicitly initialized finite mathematical extensions. No event is selected, no occurrence measure is supplied, and no L1-to-L5 or L6 bridge is asserted. Native protected physical registers, interaction-based working readers, O1/O2a/O2b closure, and the remaining typed matter/geometry/clock obligations are outside this proposition.

The finite verifier should independently check the displayed formulas and exhaustive finite domains with exact arithmetic. Its all-clock sample set is a regression check of the proved identities, not their logical justification. An exact mathematical counterexample to an identity, witness or full-record fiber count falsifies its corresponding component. Source/hash drift, incomplete execution or implementation defects are integrity STOP conditions, not mathematical falsifiers; their disposition is fixed in PREREG.md. The known private results are disclosed; a future formal run cannot be described as blind.
