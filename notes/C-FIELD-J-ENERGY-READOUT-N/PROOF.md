# Active field, scalar readout and the unchanged neutral-work chain

**NON-CANONICAL. Prospective candidate-T at L1; finite audits and independent
review pending.** Basis and exposure are specified in PREREG.md; public freeze
is pending. This proof uses
the selected v96 chain as defined; it adds no law of motion. The historical
census targets are not premises in any universal argument below.

## 1. Explicit chart and the two different operators

Write coefficient vectors as a=(a,b,c,d), and active field vectors as y.
The selected matrices and energy are

```text
A_f = [[ 1, 0, 1, 0],       B_f = [[ 4,-2, 2,-1],
       [ 0, 1, 0, 1],              [-2, 6,-1, 3],
       [-2, 1,-1, 1],              [ 2,-1, 2, 0],
       [ 1,-3, 1,-2]],             [-1, 3, 0, 2]],
H(y)=y^T B_f y/2.

C_cyc = [[0, 1, 0, 0],     C_cyc^-1 = [[2,-2,1,-1],
         [0, 0, 1,-1],                   [1, 0,0, 0],
         [1,-1, 0,-1],                   [1,-1,0,-1],
         [0, 1,-2, 1]],                  [1,-2,0,-1]],

Z = [[0,0,0,-1],            M_J = [[1,0,-1,1],
     [1,0,0,-1],                   [0,1,-1,0],
     [0,1,0,-1],                   [1,0, 0,0],
     [0,0,1,-1]],                  [0,1,-1,1]].
```

Both products of C_cyc and its displayed inverse are I. Hence this is an
exact bijection Z^4 -> Z^4, not a rational-only chart. In
O=Z[j]/(1+j+j^2+j^3+j^4), Z is multiplication by j and M_J=I+Z^2 is
multiplication by J=1+j^2. Direct matrix multiplication gives

```text
A_f C_cyc=C_cyc Z,
(I+A_f^2) C_cyc=C_cyc M_J,
A_f^T B_f A_f=B_f.
```

The actual free field step is A_f, of order five. J_f=I+A_f^2 is a virtual
linear transform for the proposed observation. For example a=J=(1,0,1,0)
gives y=(0,1,1,-2), H(y)=1. Its J_f image corresponds to J^2=(0,-1,1,-1),
is (-1,2,2,-4), and has H=2. Thus J_f does not preserve H on all integral
states; identifying this virtual observation with the actual free update
would be false even on the small sector.

## 2. Universal coefficient identities

Complex conjugation sends j to j^4. Put phi=-j^2-j^3, so phi^2=phi+1.
Since j+j^4=phi-1 and j^2+j^3=-phi, direct multiplication gives, with no
restriction on the four integers,

```text
alpha bar(alpha)=u+v phi,
u=a^2+b^2+c^2+d^2-ab-bc-cd,
v=ab+bc+cd-ac-ad-bd.
```

The coefficient vector of the product is (u,0,-v,-v). This proves the
identity coefficient by coefficient in the free integral basis. The two
ordered real conjugates are A=u+v phi and B=u+v-v phi. Their sum is 2u+v;
the full degree-four trace counts each twice. Thus

```text
S(alpha)=Tr(alpha bar(alpha))/2=2u+v,
N(alpha)=AB=u^2+uv-v^2.
```

For nonzero alpha both A and B are positive and N is a positive integer.
For zero all these quantities vanish. Substitution of the chart into H,
and then substitution of M_J a, gives the following coefficient table.
An off-diagonal column denotes the coefficient of that monomial once,
not half of it.

| Form | a^2 | b^2 | c^2 | d^2 | ab | ac | ad | bc | bd | cd |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| u | 1 | 1 | 1 | 1 | -1 | 0 | 0 | -1 | 0 | -1 |
| v | 0 | 0 | 0 | 0 | 1 | -1 | -1 | 1 | -1 | 1 |
| H(C_cyc a) | 1 | 1 | 1 | 1 | 0 | -1 | -1 | 0 | -1 | 0 |
| H(C_cyc M_J a) | 1 | 1 | 1 | 1 | -1 | 0 | 0 | -1 | 0 | -1 |

Consequently e0=H(y)=u+v and e1=H(J_f y)=u. In particular this is the
weighted energy identity on every integral field, not a fit to sample
vectors. Also J bar(J)=2-phi, which sends (u,v) to (2u-v,v-u). It follows
that, identically,

```text
S(alpha)=e0+e1,
S(J alpha)=3u-v=4e1-e0,
N(alpha)=-e0^2+3e0 e1-e1^2.
```

The last equality is a quartic polynomial identity in a,b,c,d. Since the
chart is onto the integral field lattice, these coefficient identities
cover every y in Z^4. Conversely the energy pair is recovered from the
trace pair by e1=(S0+S1)/5 and e0=(4S0-S1)/5. The scalar-residue information
is therefore the same as the inherited two-trace data on this domain.
Nothing here says a physical device can obtain either virtual energy.

## 3. The independently bounded H<=5 sector

Let K= C_cyc^T B_f C_cyc. From the table,

```text
K = [[2, 0,-1,-1],       5 K^-1 = [[6,2,3,4],
     [0, 2, 0,-1],                   [2,4,1,3],
     [-1,0, 2, 0],                   [3,1,4,2],
     [-1,-1,0, 2]],                  [4,3,2,6]].
```

Ordering the coordinates (c,a,d,b) turns K into the A4 Cartan tridiagonal
matrix with 2 on the diagonal and -1 on the adjacent off-diagonals. Its
leading principal minors are 2,3,4,5, proving positivity, and the displayed
inverse can also be checked by multiplication. Cauchy-Schwarz for the K
inner product gives a_i^2 <= (K^-1)_ii a^T K a. Since a^T K a=2H,

```text
a^2,d^2 <= 12H/5,      b^2,c^2 <= 8H/5.
```

For H<=5 these imply |a|,|d|<=3 and |b|,|c|<=2, before any enumeration.
The whole sector is therefore in a box of 7*5*5*7=1225 integer tuples.
Positivity makes its unique energy-zero member the zero vector.

For any nonzero point of the sector the norm identity gives

```text
1<=N=5 e0^2/4-(e1-3e0/2)^2<=125/4,
```

so the integer N<=31. The same inequality N>0, with 1<=e0<=5, places e1
strictly between ((3-sqrt(5))/2)e0 and ((3+sqrt(5))/2)e0, hence 1<=e1<=13.
These are containing bounds, not claims that every such pair is realizable.
The finite shell census and the attainability of norm 31 are exactly the
pending audits registered in PREREG.md; the upper bound needs no census.

## 4. Injectivity, total inverse and image recognition

Define E5(alpha)=(e0,e1,alpha mod 5O) on the preceding chart sector. Equal
data give equal u,v and therefore equal positive A,B. For two distinct
nonzero alpha,beta with equal data, gamma=alpha-beta=5 eta for nonzero
eta in O. The embedding triangle inequalities give

```text
N(gamma)<=16 A B<=16*31=496,
N(gamma)=5^4 N(eta)>=625,
```

a contradiction. Norm integrality is also the determinant of integral
multiplication on O, and the field embeddings make the nonzero norm positive.
Zero cannot collide with a nonzero element because e0 then differs. Thus
E5 is injective. This is the inherited general criterion specialized using
a newly proved energy bound, not a claim that modulo five suffices at norm
941 or for all 3125 normalized labels.

Here is the entire inverse, including inputs not known to be in the image.
On Python input use exactly the syntax contract in PREREG.md; malformed
inputs reject before arithmetic. For well-typed (e0,e1,r):

1. Reject unless 0<=e0<=5. If e0=0, accept only e1=0 and r=(0,0,0,0),
   returning alpha=y=0; otherwise reject.
2. For e0>0 reject e1<=0 or N=-e0^2+3e0 e1-e1^2 outside [1,31].
3. For each coordinate list every integer in its proved box interval that
   equals the supplied canonical residue modulo five. Form the finite
   Cartesian product. There are at most four candidates, since b,c each
   have one choice and a,d each have at most two.
4. Recompute H(C_cyc a) and H(C_cyc M_J a) for each candidate. Accept iff
   exactly one has the supplied values, returning (a,C_cyc a); otherwise
   reject. Never accept only from the preliminary norm condition.

The procedure terminates on every input: it uses fixed finite loops and
integer arithmetic, even when e1 is arbitrarily large. Completeness follows
from the containing box and recomputation; the original scalar is among the
candidates and passes. Soundness follows because any accepted scalar has the
prescribed energy bound, both prescribed readings and exactly the supplied
residue. Uniqueness follows from the preceding norm argument. Thus this is
an exact image recognizer as well as an inverse. It must accept a corrupted
datum that happens to be another valid datum: for instance the residues of
1 and j with the common e0=e1=1 both specify valid, different fields.

## 5. The equal-energy source pair and its fixed-context comparison

The canonical field reaction uses

```text
L=(I-A_f)(I-A_f^2),
P(a,b,c,d)=(a-b,-a,b,b,c,d),
L=[[ 1,-3,-1,-2],[-3,4,-2,1],[0,5,1,2],[5,-5,2,-1]],
H(Lw)=5H(w),       A_f L=L A_f.
```

w1=(0,0,1,0)=C_cyc(1,0,0,0), w2=A_f w1=(1,0,-1,1)=C_cyc(0,1,0,0)
have H=1. Their prepared active fields Lw1 and Lw2 therefore correspond to

```text
ell=(1-j)(1-j^2)=(1,-1,-1,1),
j ell=(-1,0,-2,-2).
```

Both have alpha bar(alpha)=5, so e0=e1=5, S0=10, S1=15, full trace 20
and N=25. The complete prepared chains have the same energies 41 without
the pointer, 42 with it; every non-source preparation coordinate agrees.

For the stipulated B0 context use G=I-11^T/5 and E_LOW=11^T/4. The
registered algebraic normalized LOW weight is

```text
q_LOW(a)=(a^T G E_LOW a)/(a^T G a)
        =(sum a_i)^2/[4(5 sum a_i^2-(sum a_i)^2)]
        =(sum a_i)^2/[4 Tr(alpha bar(alpha))].
```

The denominator is positive for every nonzero coefficient vector, and zero
has the registered ZERO_DENOMINATOR state, not a ratio. Our two coefficient
vectors are both in [-2,2]^4, so they are valid balanced piston coordinates
under the added chart identification. Their sums are 0 and -5, their sums
of squares are 4 and 9, and their trace denominators are both 20. Hence the
two ratios are exactly 0 and 25/80=5/16. This follows directly from the
fixed context, not from choosing a context after the comparison.

Multiplication by j in a single complex embedding has unit modulus, but
the QDD comparison uses the four rational B0 coordinates and their trace
pairing. Its matrix is Z, not a scalar multiple of I. In particular these
two coefficient vectors are not proportional even over C: their first
coordinates would force the multiplier -1 while their second coordinates
disagree with it. Thus this is not discrimination of two global complex
phases of one four-dimensional ray. It is two distinct rational source
vectors in one chosen comparison context. The comparison supplies neither
physical probabilities nor a coherent instrument or its post-states.

## 6. Complete unchanged chain law needed for the induction

To make the scope self-contained, cell i stores (m_i,b_i,z_i,r_i): ordered
matter triple m_i in (Z^4)^3, ordered spectator triple b_i in (Z^4)^3,
z_i=(E_i,M_i) in Z^4 x Z^2 and r_i>=0. Between cells are q_j>=0. Receiver
t=N-1 alone stores p in Z/5Z. All equality is literal, with every old
channel content retained. Write

```text
R=((1,-2,1,0),0,0),
AM=((1,0,0,0),(0,-1,0,0),(0,-1,1,0)),
ZM=(0,0,0),   S(u,v)=(u,u,v,u-v,0,0).
```

The unique rational split z=Py+S(u,v), for y=(a,b,c,d), is

```text
5a=2E0-3E1+E2+E3,        5b=-E0-E1+2E2+2E3,
c=M0, d=M1,
5u=2E0+2E1+E2+E3,       5v=E0+E1+3E2-2E3.
```

G first rejects and retains the full input unless m is literal R or AM and
the split is integral. On R it also requires a+2b=c+2d=0 modulo five;
otherwise it rejects in full. The exact admitted preimage is x=Vinv y/5,
where

```text
Vinv=[[1,2,1,2],[2,-1,2,-1],[0,-5,1,-3],[-5,5,-3,4]],
Vinv L=L Vinv=5I.
```

For that R input let h=H(x), require r+4h-2>=0, and set
(R,b,PLx+S sigma,r) -> (AM,b,Px+S sigma,r+4h-2).
For AM let x=y, h=H(x), require r+2-4h>=0, and set
(AM,b,Px+S sigma,r) -> (R,b,PLx+S sigma,r+2-4h).
A failed guard retains every coordinate. Only an actually accepted receiver
R-to-AM transition adds one to p modulo five; every other branch fixes p.

Layer A swaps r_j and q_j for every j; layer B swaps q_j and r_(j+1).
These are complete swaps even when both entries are occupied. The field
layer F fixes all other coordinates and acts by

```text
C=[[1,-1],[-1,0],[0,1],[0,1]],
E'=E+C M,       M'=M-C^T E',
F(Py+S sigma)=P A_f y+S sigma.
```

The fixed chronology is Ghat then A then B then F. The inherited conservation
law concerns the selected matter form
K_m=[[6,2,-1,2],[2,6,2,-1],[-1,2,6,2],[2,-1,2,6]], Q(v)=v^T K_m v,
raw energy ||E||^2+||M||^2+E^T C M, all r_i, all q_j and constant pointer
energy one. No energy channel here transports a copy of y.

## 7. All-time receiver blindness, including return and rejection branches

Compare two arbitrary unit seeds w,w' with H=1 in the exact positive
preparation of PREREG.md. Let k count completed F layers in the proof only;
it is not a stored clock. At every intermediate layer boundary the following
invariant holds:

* Every stored coordinate except source raw field is identical between the
  two chains. All non-source fields and all spectators remain zero.
* Source matter is R or AM. If it is R, its active field is L A_f^k w
  (respectively L A_f^k w'); if it is AM it is A_f^k w (respectively
  A_f^k w'). Its static field is zero.
* Intermediate matter is ZM, and receiver matter is R or AM.

Initially k=0 and every clause holds. We prove preservation by each actual
layer, rather than assuming a first-pass resource pattern forever.

At a source G opportunity, the R case always has integral split, admitted
L image and preimage A_f^k w of energy one. Its guard is r+2>=0 and is
always accepted, replacing R by AM, removing L and adding two resources in
both chains. In the AM case the preimage is the same energy-one vector.
Its guard is r-2>=0; the two chains have the same r, so either both reject
and retain everything or both accept, insert L, become R and remove two
resources. This explicitly handles arbitrarily late source reversals and
failed funding after resource returns. The phase k is unchanged by G.

Intermediates remain literal ZM and always reject. At the zero-field receiver
the R branch has h=0 and succeeds exactly when the common r>=2, while the
AM branch has h=0 and always succeeds, releasing two units. Both zero field
and zero static part stay zero under either branch. Thus matter and resource
updates agree, all rejections agree, and the actual accepted R-to-AM event
predicate agrees. The pointers therefore receive the same increment modulo
five, including after any number of wraps.

Layer A and layer B act only on resources and channels that already agree.
They preserve equality even when resources return from the receiver or
channels are occupied; no zero-content assumption is needed at later times.
They leave the source field and k alone. Finally F fixes every zero
non-source field and maps the source to A_f times its active field. Since
A_f L=L A_f and H(A_f^k w)=1, the source form persists with k replaced by
k+1. All remaining coordinates agree. This proves the induction at all four
layer boundaries for every forward macrostep, every finite N>=2 and every
pair of integral unit seeds.

The receiver's complete 31-tuple and its pointer are among the equal
coordinates, proving all-time receiver blindness for this family. Any fixed
function of that receiver state or its complete history has the same output
for the two seeds. Even a common externally supplied time or common receiver
context cannot distinguish identical histories. Access to the source,
seed-dependent preparation/control, or a different law changes the premise.

The ell/j ell pair in section 5 therefore has distinct fixed-context scalar
readings at preparation but identical receiver histories forever in this
unchanged chain. The source retains the distinguishing information; no
information erasure theorem is asserted. This exact counterexample rules
out using this preparation/receiver port as a faithful transport of that
reading. It says nothing universal about other transport architectures.

## 8. Interface, inherited status and remaining work

The exact prospective interface is y in Z^4 <-> a=C_cyc^-1 y in O. For y
in K5, E5 has the complete inverse above; the virtual energy pair produces
the inherited scalar traces, and a fixes the declared B0 context reading.
This is a mathematical data contract, not a funded measurement protocol.

| Item | Source and present disposition |
| --- | --- |
| Full chain bijection, accounts and literal rejected branches | Inherited FIELD-CONSERVATIVE-CHAIN-LAW [T], unchanged |
| First arrival/work/old-receiver return and local pointer retention | Inherited FIELD-CHAIN-FIRST-WORK and FIELD-LOCAL-WORK-RECORD [T], unchanged |
| Two-trace general inverse and norm-941 capacity | Inherited J-TWO-TRACE-RESIDUE-INVERSE and J-OBSERVED-SCALAR-CODE-CAPACITY [T], unchanged, modulo-25 boundary retained |
| Chosen normalized native readback and arbitrary target reader class | Inherited U-NORMALIZED-SCALAR-READBACK and U-COUNTER-REACHABLE-AMPLITUDE-CLASS [T], unchanged; target and codebook still choices |
| Registered trace/LOW identity | Inherited QDD-GALOIS-SUM-RATIO [T], unchanged |
| Chart energy identities, K5 exact inverse, fixed source comparison, all-time blindness | New prospective candidate-T statements in this proof, awaiting independent review |
| 291-shell census and maximum norm attainment | Exposed historical targets; candidate finite audit pending, not an executed finding here |

QDD-INSTRUMENT-APPARATUS, QDD-TERMINAL-EVENT-SEMANTICS,
QDD-INSTRUMENT-CLASS-COMPLETENESS and every other physical owner retain their
statuses. New state transport, complete post-states, terminal records, an
occurrence mechanism and a physical dictionary remain separate tasks. No
native-U realization, coherent QDD instrument, Born law, physical phase
measurement, SI energy or cross-layer closure follows from these L1 results.
