# Original passive records and native current-state memory

**PROOF-FIRST / RESULT-EXPOSED / L1 ONLY.** This proof accompanies the fresh
public probe P-QDD-PASSIVE-NATIVE-MEMORY-1. Prior exploratory calculations
revealed the witnesses and finite values before preregistration. The chosen
passive family is inherited from Public Canon v87, not selected by this proof.
The new verifier is an exact audit and finite inventory evaluation; this
document is not a report of its execution or an earned Canon status.

## 1. Fixed native source and inherited theorem

All native coordinates lie in F_5. Write x=(p1,p4,p1p,p4p,q,r),
z(x)=sum(x) and theta_n=popcount(n) mod 2. The unchanged law is

    U(n,x)=(n+1,G_(z(x)+2 theta_n)(x)), G=(a,b,c,d,e),

with generator index reduced modulo five and

    a(x)=(p4,p1,p4p,p1p,q,r),
    b(x)=(-p1p,-p4p,-p1,-p4,-q,-r),
    c(x)=(-p1p+2,-p4p+1+r,-p1+2,-p4+1-r,1-q,-r),
    d(x)=(2-p1,1-p4,3-p1p,4-p4p,1-q,1-r),
    e(x)=(2-p1,1-p4,3-p1p,4-p4p,2-q,1-r).

Let F_n(x) be the checkpoint after n ticks starting from (0,x). The source
remains K_QDD={kappa_x=(U^n(0,x))_(n>=0):x in F_5^6}, with equality of
complete pointed sequences retaining the distinguished origin. Its balanced
head map is beta_QDD(kappa_x)=(ell(p1),ell(p4),ell(p1p),ell(p4p)),
where ell(0,1,2,3,4)=(0,1,2,-2,-1).

The public theorem `U-NATIVE-CHART-AND-QDD-READBACK`, proved in
[P-QDD-U-NATIVE-READBACK-1](../P-QDD-U-NATIVE-READBACK-1/PROOF.md), supplies:

1. F_3 maps all 15625 heads onto X_3={y:sum(y)=1}; each of the 3125 fibers
   has exactly five heads, one from each initial phase z=0,1,2,3,4.
2. For n>=3 the reachable sheet is
   X_n={y:sum(y)=4-3 theta_(n-1)}. Actual native evolution between successive
   reachable sheets is bijective. The explicit conserved chart in that
   theorem recovers F_3(x) from the current indexed checkpoint (n,F_n(x)).
3. Consequently every F_n fiber for n>=3 is exactly an F_3 fiber, transported
   by a bijection. No later merger changes original-record recoverability.

These are inherited exact premises, not a new synchronization claim. The
public record theorem does not need to be re-proved to apply its general
fiber criterion to the newly selected passive records. The present verifier
independently checks the needed finite three-tick structure with coordinate
and affine native kernels.

## 2. The five complete records and their exact equality

The selected definitions and algebraic proof are
[P-QDD-PASSIVE-READING-FAMILY-1](../P-QDD-PASSIVE-READING-FAMILY-1/PROOF.md).
For v=beta_QDD(kappa_x), set

    t(v)=(v1+v2+v3+v4)^2/20,
    l(v)=(v1-v2-v3+v4)^2/4,
    r(v)=((v1-v4)^2+(v2-v3)^2)/2,
    m(v)=t(v)+l(v)+r(v)=sum(v_i^2)-(sum v_i)^2/5.

The fixed IDs and block orders are

    PI-ALL:   ((t,l,r))
    PI-TRACE: ((t),(l,r))
    PI-LEG:   ((t,r),(l))
    PI-PAIR:  ((t,l),(r))
    PI-ATOMS: ((t),(l),(r)).

Write rho_pi(x)=R_pi(kappa_x). Its five fields, in order, are exactly

    partition_id, support_state, total_weight,
    block_weights, normalized_weight_state.

For v=0 the record is

    (pi,ZERO_SUPPORT,0,(0,...,0),ZERO_DENOMINATOR).

For v!=0 it is

    (pi,SUPPORTED,m,(w_B)_B,(NORMALIZED,(w_B/m)_B)).

Every w_B is nonnegative, the displayed blocks sum to m, and m>0 precisely
when v!=0. Zero-weight individual blocks remain in their ordered positions.
Equality means equality of every field, ID, tag, tuple length, order and
rational value. No density field is introduced, and no total field is
dropped. At a fixed pi, the raw ordered block tuple uniquely determines
the other fields. Thus equality of those tuples is equivalent to complete
record equality, including the zero branch.

All records remain functions of the original head. Computing beta on a
later native checkpoint as if it were a new origin is not the question here.
The comparison input (n,F_n(x)) omits that original head; it is a distinct
proposed readback carrier. No change to K_QDD or to the selected R_pi occurs.

## 3. Factor criterion and minimal additional memory

For a preparation subset A of F_5^6 and fixed n>=3, a function d_n satisfying

    d_n(F_n(x))=rho_pi(x), x in A,

exists if and only if rho_pi is constant on every F_3 fiber intersected
with A. Necessity follows because equal current inputs require equal
outputs. For sufficiency recover the F_3 image using the inherited chart,
then assign the common value on its admitted fiber. Empty fibers require
no value on the reachable input domain. This proof also applies to the
joint tuple of all five records.

Three supported initial heads are

| x | m(beta_QDD(kappa_x)) | (t,l,r) |
| --- | --- | --- |
| (4,4,4,0,4,4) | 6/5 | (9/20,1/4,1/2) |
| (2,1,3,3,2,1) | 64/5 | (1/20,1/4,25/2) |
| (0,4,0,0,3,2) | 4/5 | (1/20,1/4,1/2) |

Substitution in U gives F_3(x)=(0,0,0,1,0,0) for all three. Their original
total-weight fields differ, so their complete records differ under every
one of the five partitions, including PI-ALL. Every n>=3 has the same
three-way conflict. An auxiliary register whose alphabet has fewer than
three states at read time cannot distinguish the three required outputs.
The bound also allows an evolving register: its final alphabet still must
distinguish them. This is a cardinality lower bound, not a claim of three
bits, a physical entropy, or a native extra coordinate.

For sufficiency, initialize a static tag from the original phase:

    c(x)=0 for z(x)=0,
         1 for z(x) in {1,2},
         2 for z(x) in {3,4},
    U'(n,x,c)=(U(n,x),c).

The first-three-tick maps on phases 0,1,2,3,4 are eca,d,e,dbd,dbe;
involutivity gives the inverse heads over y in X_3 as

    ace(y), d(y), e(y), dbd(y), ebd(y),

in initial-phase order, with composition read right to left. The second
and third have the same four pistons, and so do the fourth and fifth.
The tag therefore identifies the required piston tuple from F_3(x).
For n>=3 the chart recovers that F_3 image, giving every rho_pi exactly.

For n=0,1,2, consider all initial heads compatible with the current
checkpoint and saved tag. If two required records differed, deterministic
continuation would carry them into the same F_3 checkpoint with the same
tag, contradicting the preceding result. Thus the compatible records are
equal at these times too, defining a readback function on every correctly
initialized reachable input.

Three additional states are therefore necessary and sufficient for a
universal all-time reader, and separately at every fixed n>=3, for each
partition and for the full family. This does not assert that three states
are needed at n=0 alone. It is an initialized extension, not a register
already present in unchanged U, and no global injectivity of U' on arbitrary
incorrectly initialized inputs is claimed.

## 4. Finite record and preparation inventories

There is a compact independent finite specification of every count. Write
y=(a,b,c,d,q,r) in X_3, take (a,b,c,d,r) freely in F_5^5, and set
q=1-a-b-c-d-r. The three inverse piston classes are

    A=(d+3-r,c+4,b+4+r,a), multiplicity 1,
    B=(2-a,1-b,3-c,4-d), multiplicity 2,
    C=(-c,-d,-a,-b), multiplicity 2,

all modulo five. These follow by substituting in the five inverse heads.
For a piston tuple p, put v_i=ell(p_i) and define integer atom keys

    T=(v1+v2+v3+v4)^2,
    L=5(v1-v2-v3+v4)^2,
    R=10((v1-v4)^2+(v2-v3)^2).

The partition keys are respectively

    k_ALL=(T+L+R), k_TRACE=(T,L+R), k_LEG=(T+R,L),
    k_PAIR=(T+L,R), k_ATOMS=(T,L,R).

They are 20 times the ordered raw tuples. Hence they preserve full record
equality at their fixed IDs. The exact number of initial records is

    N_pi=|{k_pi(p):p in F_5^4}|.

For each of the 3125 free tuples (a,b,c,d,r), compare the three keys of
A,B,C. There are exactly four mutually exclusive patterns:

| Equality of class keys | Head multiplicities |
| --- | --- |
| all distinct | (2,2,1) |
| A=B!=C or A=C!=B | (3,2) |
| B=C!=A | (4,1) |
| A=B=C | (5) |

Thus the four column counts below are explicitly the finite sums of these
four indicator functions over F_5^5. This specification is independent of
native trajectory enumeration and states the complete domain and equality
for the finite calculation. The exact verifier evaluates all heads with U,
matches every fiber to these inverse formulas, and computes complete-record
classes including all five fields. The following exposed values are the
frozen finite targets; their public computational acceptance requires the
pinned audit and required architecture checks.

| Partition | N_pi | (2,2,1) | (3,2) | (4,1) | (5) | Maximum origins |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| PI-ALL | 19 | 2510 | 200 | 385 | 30 | 7310 |
| PI-TRACE | 35 | 2774 | 116 | 226 | 9 | 6845 |
| PI-LEG | 62 | 2922 | 58 | 142 | 3 | 6601 |
| PI-PAIR | 63 | 2924 | 56 | 143 | 2 | 6598 |
| PI-ATOMS | 65 | 2946 | 54 | 123 | 2 | 6556 |

The optimum follows from the factor criterion. In each fiber an admissible
preparation may select heads from at most one same-record class. Choosing
a largest class independently in every fiber is both permitted and optimal.
If the four pattern counts are n221,n32,n41,n5, the resulting maximum is

    M_pi=2 n221+3 n32+4 n41+5 n5.

This proves the optimization formula and supplies a witness construction.
The finite algorithm explicitly constructs these preparation sets and
checks distinctness and size. No physical preparation rule is selected by
the cardinality optimum. Because later synchronized evolution is bijective,
the same maxima apply to each fixed n>=3 and to simultaneous all-time
unaugmented readback on that selected preparation set.

## 5. Restricting to supported heads preserves every maximum

The full domain has 15625 heads; its 25 zero-piston heads are the only zero
records, leaving 15600 supported heads. At most one of A,B,C in a fiber
can be the zero piston tuple. Indeed B=0 forces (a,b,c,d)=(2,1,3,4), where
A has last coordinate 2 and C!=0. C=0 forces (a,b,c,d)=(0,0,0,0), where
A has second coordinate 4 and B!=0. These exclude every pair of zero
classes, including pairs involving A.

Consequently a zero record class has at most two heads. If such a class
exists, at least one of the two multiplicity-two classes is supported.
It already gives a same-record supported class of size at least two.
Removing zero heads therefore cannot lower the largest class size in any
fiber. A supported largest class can always be chosen. All five maximum
values in the table are consequently attained on supported heads only.
The supported lower-bound witness in section 3 proves that their memory
minimum also remains three.

## 6. Scientific boundary

The source and selected reading maps are unchanged. A head-retaining
decoder can always read its distinguished head directly. The negative
result concerns recovery after replacing its input by a later native
checkpoint and clock without unreported retained origin information.
The positive repair explicitly adds initialized information. Coarsening
does not lower the memory minimum because the chosen five-field schema
retains total_weight in every partition; changing that schema would change
the problem. In particular normalized PI-ALL alone would discard a field
essential to the stated lower bound.

Every claim here is L1 exact mathematics. No later-checkpoint reading
adapter, apparatus realization, post-state instrument, occurrence law,
sampling, event-frequency interpretation, physical memory cost, physical
preparation selection or L1-to-L4/L5/L6 lift is supplied. The three open
physical QDD obligations remain outside this theorem's scope.
