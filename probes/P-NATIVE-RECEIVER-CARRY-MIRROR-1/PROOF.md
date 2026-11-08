# Native first-tick receiver and a declared carry-mirror circuit

**NON-CANONICAL / L1.** This is a proposed exact proof for
P-NATIVE-RECEIVER-CARRY-MIRROR-1. The algebraic statements are candidate-T;
the separately frozen finite executions are candidate-C until the required
evidence and review are obtained. No execution or independent acceptance of
this new probe is asserted here. The supplied predecessor results were
exposed before this authoring session.

The native reference is Public Canon v108 at activation
`17de90b58f814238e151aac77badde6654b52627`, content
`f8afa5ceec6cbaa60f1f81593a3a09bdc2a28c4d`. Its definitions of U and its
native receiver quotient are retained exactly. The subsequent register
interconnection is supplied separately; it is not identified with U.

All F5 equations below are modulo five. Words of executed operations are
listed in chronological order. Function compositions use the ordinary
right-first convention, stated explicitly where needed.

## 1. Native law and the admitted input family

The native state is `(n,x)` in `N_0 x F5^6`, not the six-coordinate
checkpoint alone. For `x=(A,B,C,D,q,r)`, put

    z(x)=A+B+C+D+q+r,
    theta_n=popcount(n) mod 2,
    U(n,x)=(n+1,g_(z(x)+2 theta_n)(x)).

In generator order `(g_0,g_1,g_2,g_3,g_4)=(a,b,c,d,e)`, the canonical maps
are

    a(x)=(B,A,D,C,q,r),
    b(x)=(-C,-D,-A,-B,-q,-r),
    c(x)=(2-C,1-D+r,2-A,1-B-r,1-q,-r),
    d(x)=(2-A,1-B,3-C,4-D,1-q,1-r),
    e(x)=(2-A,1-B,3-C,4-D,2-q,1-r).

Every first execution here starts at native counter zero, hence theta_0=0.
Prepare `(0;A,B,C,D,0,1)` with arbitrary four pistons in F5^4. Distinguish
the piston sum and complete initial trace:

    kappa=A+B+C+D,          s=kappa+1.

The admitted family is `s!=0`. It has 500 preparations, 125 for each
nonzero s: after fixing three pistons, the fourth is uniquely determined
by their sum. The other 125 preparations have `s=0`, equivalently
`kappa=4`. They are controls. In particular the zero piston tuple belongs
to the admitted sheet s=1, not to the excluded sheet.

At the first tick the chosen generator is g_s. Direct substitution gives

| s | First generator | Current receiver (q1,r1) | q1+r1+2 |
| ---: | :---: | :---: | ---: |
| 0 | a | (0,1) | 3 |
| 1 | b | (0,4) | 1 |
| 2 | c | (1,4) | 2 |
| 3 | d | (1,0) | 3 |
| 4 | e | (2,0) | 4 |

Thus the fixed transfer `h(q,r)=q+r+2` obtains the original full trace
s from the two actual occupied receiver cells for every admitted input.
It is not fed the original pistons or an independently computed s.
The five receiver pairs themselves are distinct. Failure of h on s=0 is
therefore only failure of this chosen transfer on its attempted extension;
it is not an impossibility of reading all five sheets by another reader.

The transfer is unique among affine scalar maps
`alpha*q+beta*r+gamma` that equal s on the four admitted rows. Subtracting
the s=1 row from s=2 gives alpha=1. Subtracting s=2 from s=3 gives beta=1,
since the r difference is -4=1. The first row then gives gamma=2.
The fourth row satisfies these values. No uniqueness outside the affine
class is claimed.

Let chi be the quadratic character of F5, with values
`chi(0)=0, chi(1)=chi(4)=1, chi(2)=chi(3)=-1`. On these four rows the
receiver reader `R_q(1)=-1`, `R_q(0)=R_q(2)=1` equals chi(s).
Its values at other q are irrelevant to the stated contract. The rule
does not give chi(0) on the excluded row.

## 2. Cyclotomic digits and exact multipliers

Let `O=Z[j]`, where j is a primitive fifth root of unity, and set

    lambda=1-j,             J=1+j^2,             J^-1=-j-j^2.

The inverse identity follows from
`(1+j^2)(-j-j^2)=-(j+j^2+j^3+j^4)=1`. Substituting j=1-lambda gives
the exact integral expressions

    J=2-2 lambda+lambda^2,
    J^-1=-2+3 lambda-lambda^2.

Evaluation at j=1 identifies `O/(lambda)` with F5. Also
`product_(k=1..4)(1-j^k)=5`, and each factor is divisible by lambda.
Consequently `5 in (lambda^4)`, and `5/lambda in (lambda^3)`.

Every element of `O/(lambda^2)` has a unique representation
`lo+hi*lambda`, with lo,hi in F5. Existence follows by substituting
j=1-lambda and using `5 in (lambda^2)`. For uniqueness, equality first
forces the low coefficients equal modulo five by reduction modulo lambda;
after removing that coefficient, dividing by lambda forces equality of
the high coefficients. Changing an integer digit lift by a multiple of
five does not alter these two coefficients.

Reduction of the two exact multipliers therefore gives

    F(lo,hi)=(2lo,3lo+2hi),
    I(lo,hi)=(3lo,3lo+3hi).

Their compositions in either order are identity on all 25 digit pairs.
These are exact finite quotient maps, not approximations to the integral
ring. They are separately supplied register operations, not native U.

## 3. Four occupied registers and their complete inverse

Use four current registers `(q,r,h,k)` in F5^4, where q,r are the native
post-tick receiver, h is the multiplier high digit and k is an archive.
Only the admitted preparations set h=k=0. Define the following operations
on arbitrary values of all four registers:

1. Set q to q+r+2 by a reversible SUM and SHIFT, preserving r.
2. Apply F to `(q,h)`.
3. Swap the complete h and k registers.
4. Apply I to `(q,h)`.
5. Subtract r+2 from q.

Write `b=q+r+2` for the value after the first operation. The complete map
is, by direct substitution,

    L(q,r,h,k)=(q,r,b+3k,3b+2h).

Applying it again gives high `b+3(3b+2h)=h` and archive
`3b+2(b+3k)=k`, while q,r remain fixed. Thus `L^2=id` on all 625
four-register states, including occupied high and archive registers.
Equivalently L is the conjugate of the h/k swap by the composition of
the shear and F. This proves its complete inverse without assuming blank
auxiliary registers.

For h=k=0, the actual intermediate values are

    loaded b=q+r+2,
    forward output (a,v)=(2b,3b),
    after the swap: low a, high 0, archive v,
    inverse output (b,w)=(b,b),
    final receiver (q,r), high w=b, archive v=3b.

The inverse multiplier receives the actual forward low a. Neither a nor b
is loaded as a separate externally supplied mark. The final two carries
are simultaneous records at different addresses. This record-producing
trajectory is not the direct inverse of the entire forward two-digit
word: applying I to `(a,v)` instead returns `(b,0)` and removes its high
digit. Applying the complete L again also removes the two records.

The restored receiver is the native post-tick receiver, not a reversal
of the original native step. Primary pistons are untouched by L, so the
complete six-register post-tick checkpoint is restored. No global inverse
of the unrestricted native U follows from this argument.

## 4. Integral carries and marked edge pairing

Fix either integer digit section, counting `{0,1,2,3,4}` or balanced
`{-2,-1,0,1,2}`. In each case there is one integer representative for each
residue and zero is represented by zero. For an input representative b,
let a be the representative of `2b mod5` in the same section and define
the integral forward carry

    C=(Jb-a)/lambda.

The numerator has residue zero modulo lambda, so C lies in O. If the
inverse multiplier receives this actual output representative a, its
output representative is exactly b, since `3*2=1` modulo five and the
section is fixed. Its integral carry satisfies, without truncation,

    C_mirror=(J^-1 a-b)/lambda=-J^-1 C.

As `-J^-1` has residue 2 modulo lambda, the carry residues obey

    v=res(C)=3b,            w=res(C_mirror)=2v=b.

The first equality follows either from the exact polynomial for J or
from `5/lambda in (lambda^3)`, which removes the integer rounding term
from the residue. With the same fixed carry-sign reader `-chi(res C)`,
the forward and paired inverse signs are respectively chi(b) and
`-chi(b)` whenever b is nonzero. This agrees with the digit-register
values v,w in section 3 for either integer section.

Two different controls must remain distinct. If J^-1 receives the same
unchanged b with blank carry, its first-carry residue is again 3b, so
its sign agrees with the forward sign. If it receives the entire forward
two-digit output `(a,v)`, it removes the high digit. Neither control is
the marked-letter mirror that archives v and supplies high zero at a.

Omitting the transfer offset gives `q+r=s-2`, a wrong marked digit on
every admitted sheet. Sign agreement alone does not repair that failure:
for s=1 the characters of s and s-2 happen to agree, whereas the other
three admitted sheets do not. Thus 125 of the 500 native preparations
would pass that weaker sign-only comparison despite the wrong mark.

## 5. A second native sign observation is a separate initialized device

Prepare another native receiver at its own counter zero, with fixed
pistons `(-1,0,0,0)` and receiver `(0,1)`. A reversible SUM adds the
live forward low a into its first piston while preserving a. Its complete
trace is now `(-1+a)+1=a`. One genuine first tick of this second U
therefore gives a receiver whose identical q-reader is chi(a).

On the admitted domain a=2b is nonzero and `chi(a)=-chi(b)`. Thus this
second forward native observation agrees with the paired carry sign.
The reference is source independent; its subsequent change is caused by
the declared SUM from an existing wire, not by another external mark.

This construction nevertheless supplies an extra receiver, a write, and
an independently enabled first-step origin. It is not native time
reversal, nor does the unchanged original U choose that write or start
the second device. Repeating the forward digit multiplier twice would
give `4b=-b`, not the marked return b obtained with J^-1.

## 6. Fixed-input discrimination at the next carry precision

This is a separate comparison, with the same nonzero integer b supplied
to J and J^-1, zero initial carry and the same tick convention. Let their
own output representatives in the chosen common section be a_+ and a_-.
The exact expansions give

    C_+=(2b-a_+)/lambda-2b+b lambda,
    C_-=(-2b-a_-)/lambda+3b-b lambda.

Both numerators in the first terms are integer multiples of five.
Those terms belong to `(lambda^3)` and vanish modulo lambda^2.
Writing the first carry as `v+u lambda mod lambda^2` yields

| Multiplier | Output residue | v | u | u/v for b nonzero |
| --- | --- | --- | --- | --- |
| J | 2b | 3b | b | 2 |
| J^-1 | 3b | 3b | -b | 3 |

For an actual integral carry, v is its residue. To obtain u, subtract
any integer lift of v, divide by lambda and reduce again. Two integer
lifts differ by a multiple of five, and their quotient by lambda
vanishes modulo lambda; hence this reading is independent of the choice
between the two specified lifts.

At precision `O/(lambda)` the two operations collide for each fixed b.
No function of that residue and their common tick can distinguish them.
At precision `O/(lambda^2)`, nonzero b implies v!=0, and the two possible
slopes 2 and 3 are disjoint. One fixed reader, without b, output letter,
multiplier flag or clock direction as arguments, distinguishes the two
operations. This proves minimality only among ideal-power precisions of
this first-carry observation on the stated input family. If original and
output letters are available, their quotient distinguishes the multiplier
already in F5; that is a different reading contract.

The main two-digit product circuit stores the output letter and v. It
does not also supply u. Observing u requires the product modulo lambda^3
or access to the integral carry. For b=0, both exact carries are zero,
so no precision of this carry distinguishes the operations and u/v is
undefined. There is no extension to arbitrary non-integer source words
or arbitrary nonzero initial carry in this statement.

## 7. Rank obstruction for the native trace port only

Summing the canonical generators gives trace maps
`z,-z,2-z,2-z,3-z`, respectively. For a supplied common clock symbol
t in `{0,1}`, the native selected map is `T_t(x)=g_(z+2t)(x)`.
The resulting closed trace maps, in input order 0,1,2,3,4, are

    tau_0=(0,4,0,4,4),
    tau_1=(2,1,1,3,1).

Restricted to the four nonzero initial traces, either first symbol has
image cardinality two. A deterministic continuation common to all inputs
cannot increase the image cardinality: applying a function to two values
produces at most two values. Hence no nonempty fixed binary clock word
can make the actual current trace equal the four-valued permutation
`s -> 2s` on all four admitted sheets. The actual origin-zero native
clock is one included common word.

This excludes only that current trace port and fixed common-word
protocol. It does not concern the entire receiver or checkpoint, which
retains additional information, nor a history-dependent reader or the
separately supplied transfer. Indeed the first receiver rows of section 1
already distinguish all five initial traces. No rank obstruction to
arbitrary decoding, augmented registers or arbitrary physical realization
is inferred.

## 8. Finite compiled realization and its evidence boundary

The declared source compiler is
`probes/P-J-LAMBDA-CARRY-ARITHMETIC-1/arithmetic_compiler.py` at public
commit `227ef4cd42834a67f175ff1141e52b19ef8a49c4`, SHA-256
`0e3668a7e664f572e6c6c34c49bf454e8d931e6dd05b8f2ebaf3c1b0cd761027`.
Its two-digit layout has data addresses 0,1 and 48 working cells, for
50 compiler cells. The frozen finite implementation requires an actual
expanded forward word of 40348 primitive basis-register operations and
its literal reversed/inverted word, each acting on the same data cells.
The source inventory is

    EQ 30368; MUL 5840; REFLECT 1168; SCALE 2; SHIFT 112; SUM 2858.

These counts describe the declared compiler witness. They are not a
minimal circuit result or a physical gate count established by the
algebra above. The new finite audit must independently execute and check
the expanded word, its count, all 25 two-digit inputs in both directions,
and complete workspace recovery. It must not replace a compiled word
by the closed formulas F and I used as its comparison target.

The integrated addressed carrier has 62 F5 registers:

    data low/high:            0,1;
    compiler work:            the other 48 addresses below 50;
    forward carry archive:    50;
    primary native machine:  (51,52,53,54,0,55);
    secondary native machine:(56,57,58,59,60,61).

The primary q register is literally the compiler low register 0 from
initialization onward. The primary receiver r is 55. The program executes
the primary origin tick, the receiver SUM and SHIFT, the full compiled
forward word, a SUM from live low 0 to secondary first piston 56, the
secondary origin tick, the high/archive swap, the full compiled inverse
word, and the inverse receiver shear. The swap is implemented by
`SUM high->archive`, `SUM -archive->high`, `SUM high->archive`, then
`SCALE high by -1`; direct substitution exchanges arbitrary values.

The finite evidence obligation is all 500 admitted primary preparations
in this same mutable addressed carrier, with source-independent ready
values outside the four primary pistons. Every multiplier must restore
all 48 work cells. The final primary six-coordinate checkpoint must equal
its actual post-tick checkpoint, archive 50 must contain 3s, high 1 must
contain s, and the secondary receiver must give the opposite sign.
Four distinct boundary classes have multiplicity 125; these are not
500 independent carry predictions.

Once the complete compiled interfaces and their untouched complements
are verified, sections 1 through 5 prove the composed endpoint without
an additional algebraic assumption. The present proof does not assert
that those new runs have already passed. It also does not assert a
global reversible inverse of the 62-register computation containing
two native steps; the reversible four-register subcircuit has the exact
inverse proved separately in section 3. The secondary native output is
retained in the declared integrated forward computation.

The number 62 counts F5 basis registers. The two native origin counters,
the finite interconnection schedule and its control are explicitly
supplied; 62 is not a complete resource count for a derived autonomous
controller. There is no assertion that the second carry coefficient
of section 6 is present in this two-digit realization.

## 9. Scope

The positive statements concern exact native first-tick readout followed
by a specified finite reversible register interconnection, marked integral
carry pairing, and a separately typed higher-precision carry reader.
The negative statements retain their declared ports, domains and equality
rules. Nothing here asserts an in-machine implementation of the added
wiring by unchanged U, endogenous choice of multiplier or schedule,
native time reversal, an indefinitely reusable record store, or a
contact-bank renewal result. No L1-to-L4 physical bridge, observed time
direction, thermodynamic interpretation or Canon promotion is supplied.
