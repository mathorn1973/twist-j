# Relative phase codes and the zero layer

**NON-CANONICAL / candidate-T / L1 arithmetic / no authority.**
Author: A. M. Thorn <thorn@twistj.com>.
Prepared by session codex-zero-root-20261125 with same-session Astra and Sol
helpers. This is not an independent external review or a Canon promotion.
Reservation: #2097. Prospective scope: [PREREG.md](PREREG.md).

## 1. What zero means here

Let O=Z[j], Phi_5(j)=0, ell=1-j, rho=j^2, J=1+rho,
Delta=J-conjugate(J)=j^2-j^3=rho*ell, and
s=-1-2j^2-2j^3, so s^2=5. Put R_m=O/(ell^m).
The public ramification theorem gives (5)=(ell)^4 as ideals. Thus

    R_4 = O/(5) = F_5[ell]/(ell^4).

This is not the equation 5=ell^4 in O. The domain O has no nonzero
square-zero element. R_4 has exactly 25 square-zero elements:

    N = {x in R_4 : x^2=0} = ell^2 R_4.

More generally, in the local quotient R_m, x^2=0 iff
v_ell(x)>=ceil(m/2), so there are 5^floor(m/2) such elements.
Indeed x=ell^v u with u a unit for any nonzero class, and the square
vanishes exactly when 2v>=m. Conjugation preserves this valuation, so
x*bar(x)=0 has the same solution set. These are quotient statements,
not an assertion that a nonzero algebraic integer has zero size or energy.

The elements s and s*Delta have valuations 2 and 3. Their distinct leading
terms prove that

    x=s(a+b*Delta),  a,b in F_5,

parametrizes N bijectively. Multiplication by 1 preserves every state in
every unital ring; it is not a special consequence of nilpotence.

## 2. The exact integral reader is a coefficient contrast

Write x=sum_(i=0)^4 n_i rho^i with integral n_i. Such five-coefficient
representatives differ exactly by adding one common integer. Put S=sum n_i.
The trace of a fifth root is 4 at exponent zero and -1 at other exponents.
Consequently, for k in Z/5Z,

    D_k=2 Tr(rho^k*x)=10*n_(-k)-2*S,
    L_k=(D_k-D_0)/5=2*(n_(-k)-n_0).                 (1)

This proves divisibility without a numerical scan. It also proves the
integral reconstruction, since sum rho^(-k)=0:

    sum_(k=0)^4 D_k*rho^(-k)=10*x,
    sum_(k=1)^4 L_k*rho^(-k)=2*x.                  (2)

Both equations hold in O, before any reduction. No fractional state is
introduced by the last division: the displayed sum is exactly twice x.

Define r_k=L_k mod5. Adding 5y to x changes L_k by 5L_k(y), so r is a
well-defined map of R_4. Equation (2) and invertibility of 2 in F_5 prove

    R_4 -> F_5^4,  x -> (r_1,r_2,r_3,r_4)

is injective, hence bijective. Four five-valued symbols are the minimum
possible complete label for 625 states.

For the standard four-coordinate representative
x=A0+A1*j+A2*j^2+A3*j^3, the reader is particularly simple:

    r=(0, 2(A3-A0), 2(A1-A0), -2A0, 2(A2-A0)) mod5.   (3)

Conversely A0=-3r3, A1=3(r2-r3), A2=3(r4-r3),
A3=3(r1-r3), all in F_5. Thus a coefficient-access implementation does
not need absolute trace evaluation or a modulo-25 account. Whether the
specified dynamics supplies that access and an archive is a separate claim.

## 3. Raw quotients, representative offsets and the quadratic code

For x in ell O, D_k is divisible by 5: setting j=1 gives
Tr(x)=-x(1) modulo5. On N define F_k=D_k/5 mod5 using an integral lift.
It is important that F is not itself a map from N with no lift choice.
Replacing x by x+5y changes

    F_k -> F_k + D_k(y) = F_k - 2*y(1) mod5,       (4)

the same arbitrary constant at all five phases. In contrast r is unchanged.
For an arbitrary state of R_4, D_k/5 need not be integral at all.

The five rho-coefficient vectors of s and s*Delta may be chosen as

    s:       (-1,-2,0,0,-2),
    s*Delta: ( 0,-1,-2,2,1).

Their D_0 values are zero. Substituting into (1) yields, for any lift,

    F_k=c+2*b*k+3*a*k^2,
    r_k=  2*b*k+3*a*k^2.                          (5)

Here c is the representative offset, not an additional physical state of N.
There are 25 states in N and 125 raw words when all c are admitted.
Each phase is a point of F_5, including phase zero.

Distinct quadratic polynomials agree at at most two field points. This
proves all of the following without extrapolating from finite tests:

* Every three distinct raw phase readings determine (a,b,c).
* The full raw word family has parameters [5,3,3].
* Two missing symbols can be recovered.
* One independently corrupted raw symbol can be uniquely corrected.

The last assertion follows because radius-one Hamming balls about words
of distance at least three are disjoint. Distance three is attained by
a nonzero polynomial with two distinct roots. These are Reed-Solomon
evaluation codes, the standard construction of Reed and Solomon,
"Polynomial Codes Over Certain Finite Fields", SIAM 8 (1960), 300-304,
doi:10.1137/0108018. The candidate result is the exact identification
of this trace family with that construction, not the invention of coding
theory or the existence of an autonomous error-repair mechanism.

Writing delta f(k)=f(k+1)-f(k), with cyclic arguments in F_5, gives

    delta F(k)=2b+3a(2k+1),
    delta^2 F(k)=a,  delta^3 F(k)=0.              (6)

The common offset disappears at the first difference; orientation remains
in b and the second difference retains a.

## 4. The full hierarchy and a direct phase intertwiner

Put q_k=r_(k+1)-r_k. Telescoping gives sum q_k=0. The map
Q:x->q is injective: q=0 implies r is constant, and r_0=0 then gives x=0.
Both R_4 and the zero-sum subspace of F_5^5 have dimension four, so Q is
an isomorphism onto that subspace.

Each function on F_5 has a unique polynomial representative of degree at
most four. The power sums are zero in degrees 0,1,2,3 and -1 in degree 4.
Thus the zero-sum functions are exactly the polynomials of degree at most
three. Moreover, equation (1), or the defining traces, gives

    Q(rho*x)=T Q(x),  (Tf)(k)=f(k+1),
    Q((rho-1)*x)=delta Q(x).                     (7)

The ideals (rho-1) and (ell) coincide because rho-1=-ell*(j+1)
and j+1 is a unit. On polynomials of positive degree d<=3, delta lowers
the degree by exactly one: its leading coefficient is multiplied by d,
which is nonzero in F_5. Therefore, for 0<=r<=3,

    Q(ell^r R_4) = {q: deg q<=3-r}.              (8)

The unique antiderivative with r_0=0 has degree at most 4-r, because
delta is an isomorphism from zero-constant polynomials of degree at most
4-r to polynomials of degree at most 3-r. For nonzero x of valuation r,
the degrees are exactly deg r=4-r and deg q=3-r. This proves the
proposed hierarchy and its sharpness.

| State layer | States | Max degree of r | Anchored four-symbol code | Adjacent five-symbol code |
| --- | ---: | ---: | --- | --- |
| R_4 | 625 | 4 | [4,4,1] | [5,4,2] |
| ell R_4 | 125 | 3 | [4,3,2] | [5,3,3] |
| ell^2 R_4 | 25 | 2 | [4,2,3] | [5,2,4] |
| ell^3 R_4 | 5 | 1 | [4,1,4] | [5,1,5] |
| {0} | 1 | zero polynomial | trivial | trivial |

For anchored words, r(k)=k*g(k) on k=1,2,3,4, so coordinatewise division
by these nonzero k gives ordinary polynomial evaluation of degree at most
3-r. A nonzero word has at most 3-r zero coordinates and minimum weight
r+1. For adjacent words the ordinary length-five evaluation bound gives
minimum distance r+2. Products with the maximal allowed number of distinct
roots attain both bounds.

On N specifically,

    q_k=a*k+(3a+2b).                             (9)

Two independent adjacent readings determine a,b. With independently
observed q symbols this [5,2,4] code recovers three erasures, corrects one
error, or corrects one error together with one known erasure.

## 5. The observation error model cannot be omitted

Raw F, anchored r and adjacent q are different interfaces.
One raw error F_i->F_i+e becomes two adjacent errors:
q_(i-1)->q_(i-1)+e and q_i->q_i-e. A raw anchor error at i=0
changes all four nonzero r coordinates by -e. Consequently the standard
independent-symbol guarantee of the q code cannot be applied to errors
introduced upstream in F. A decoder using the structured propagated-error
model can still correct one raw error; differencing has not created a
stronger independent-raw-error guarantee.

For raw quadratic readings a simple one-error syndrome is

    S0=sum y_k,  S1=sum k*y_k.

Both sums vanish on any quadratic codeword. For one error e at position i,
S0=e and S1=i*e. Thus i=S1/S0 when S0!=0; subtract e at that position
and verify the quadratic word. The guarantee is for zero or one error.
Two or more arbitrary errors can imitate a different admissible situation.

## 6. Hermitian blindness is a parity statement

On R_m consider the two integral Hermitian readings

    H_1(x)=x+bar(x),
    H_J(x)=J*x+bar(J)*bar(x).

If both vanish, H_1=0 gives bar(x)=-x, and then H_J=Delta*x=0.
Since v_ell(Delta)=1, x lies in ell^(m-1)R_m. Conjugation acts on
this last one-dimensional layer as (-1)^(m-1), because
bar(ell)=-j^(-1)*ell and conjugation is trivial on the residue field.
It follows that

    ker(H_1,H_J) = ell^(m-1)R_m  when m is even,
    ker(H_1,H_J) = {0}          when m is odd.    (10)

The nontrivial kernel has exactly five elements, including zero.
It is not an odd-depth effect and not an ever-growing hidden subspace.
The same kernel is blind to every Hermitian linear reading
t*x+bar(t)*bar(x): for an even-depth kernel element this reduces to
(t-bar(t))*x, and t-bar(t) belongs to (ell). At odd depth the two
displayed readings already separate all states.

At m=4 the root layer N has 25 elements, whereas the Hermitian-blind
layer has only five: ell^3R_4. Those two layers must not be identified.
The exact integer witness x=ell*s satisfies

    Delta*(x-bar(x))=5.                          (11)

Indeed (j^2-j^3)(j^4-j)=s. The right side is zero in R_4 but nonzero
in R_5. Thus observing it at the deeper precision is not observing a
nonzero value in the original quotient.

### A separate all-depth precision refinement

The following symbolic refinement was derived during review; the finite
audit does not claim new all-depth computational coverage. Set
A(x)=Delta*(x-bar(x)) modulo ell^(m+1). This is well-defined for
x modulo ell^m, since any lift change acquires at least one additional
ell factor after multiplication by Delta. The pair

    (H_1(x) modulo ell^m, A(x) modulo ell^(m+1))

is injective for every m. The exact identity

    2*Delta*x = A(x)+Delta*H_1(x)

recovers x modulo ell^m by exact division. For even m this detects the
previous last-layer ambiguity with one more ell layer of precision;
same-depth Hermitian readings cannot do so. No physical mechanism for
that deeper observation is inferred.

## 7. What the native residue port discards

Canon v117 U-NATIVE-APPARATUS-HISTORY-FACTOR and
U-NATIVE-RAW-RESIDUE-READOUT prove that, for the unchanged U, common
ready receiver (q,r)=(0,1), and standard raw four-piston source,
the entire receiver history depends only on

    kappa(x)=x(1)=A0+A1+A2+A3 modulo5.

Equation (2) identifies this scalar exactly inside the relative code:

    kappa(x)=3*sum r_k=3*delta^4 r=3*delta^3 q.    (12)

Every x in ell R_4 has kappa=0. Thus all 25 square-zero states have
the same designated receiver history as zero. The state s itself has
r_1=3, so this receiver cannot recover the relative reader at the
unchanged standard source/port interface. This is an all-time exact
obstruction at that interface, not a theorem forbidding every native
preparation, piston tap or internal record.

Multiplying the same source by known ring elements, applying a known
ring automorphism, or adding a known offset still gives receiver labels
of the form kappa(m)*kappa(x)+kappa(c). Such operations do not expose
the lost ideal directions. Source-dependent coefficient wiring changes
the interface and must be stated as an additional preparation.

## 8. A sharp passive native observation on the root layer

For the canonical source x=s(a+b*Delta), its four pistons are

    P=(-a+2b, 4b, -2a+b, -2a+3b).

Their sum is zero. With common ready (q,r)=(0,1), the first two native
generators are b,b. Reading only the first piston at ticks one and two gives

    y1=2a-b,  y2=-a+2b,
    a=4y1+2y2,  b=2y1+4y2.                      (13)

Thus two post-start samples of one existing piston determine all 25
states and every r_k. One five-valued sample cannot distinguish them.
This uses two observations or an observer's two-sample memory. It does
not install a writer in the designated (q,r) receiver.

The stronger constructive answer, with two initially blank native
pistons and one correlated source preparation, is stated separately in
[NATIVE-PROOF.md](NATIVE-PROOF.md). Its preparation is not the common
standard source in this section; therefore it does not contradict (12).

The subsequent [reference-PROOF.md](reference-PROOF.md) proves a fixed
current-state reader on the same prepared trajectories. Put
A=p1+p1p, B=p4+p4p, C=p1-p1p-2 and D=p4-p4p-1. At cut3,
A=1 and C=2. Every selected tail generator preserves AB and CD.
Thus the two written residues are recovered at every later cut as

    r_1=3(AB+3CD+1), r_4=3(AB-3CD-1).

The existing sum z of all six native coordinates is 0,0,2 before the
write and stays in {1,4} thereafter. The reader therefore reports BLANK
before cut3 and PRESENT(r_1,r_4) thereafter without a counter input.
It reads four pistons and z; native evolution still includes its counter.
PRESENT(0,0) is a valid prepared record. The raw six-zero launch lies
outside the preparation and produces PRESENT(0,3), so the construction
is not a universal test for absence. The proof also exhibits equal
four-piston projection sets at cuts2 and8, forbidding this readiness
schedule from four pistons alone. No internal reader circuit is supplied.

## 9. Conditional J-time observation

Equation (7) also gives Q(J*x)=(I+T)Q(x). For declared multiplication
by J and a sensor q_0, put b_n=q_0(J^n*x). Then

    b_n=sum_(i=0)^n binom(n,i)*q_i(x).

The first four b_n invert by a unit-triangular binomial matrix to
q_0,...,q_3, and q_4 is fixed by their zero sum. On N, the first two
b_n determine the linear q polynomial. This is a complete conditional
observability statement for a specified J multiplier and sensor.
Canon U-J-POWER-CHECKPOINT-NOGO forbids identifying that multiplier
with a nonzero fixed checkpoint reading of unchanged native U.
No such identification is made here.

## 10. Scope of the result

The integer identities, exact code parameters, parity theorem and
specified observation constructions are candidate-T written results.
Finite execution is supplementary candidate-C evidence. The two new
arithmetic implementations are same-session cross-checks, not independent
external confirmation. No probability, autonomous repair, quantum event,
physical apparatus, RH consequence or Canon status follows from these
statements. The original audit's missing source remains missing;
[PROVENANCE.md](PROVENANCE.md) preserves that custody boundary.
