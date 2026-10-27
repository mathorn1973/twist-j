# Native realization boundary for the two-path contact

Status: NON-CANONICAL. Layer: L1. Conditional analytical candidate only;
no new public claim status or physical realization is asserted.
Reservation: [issue #1806](https://github.com/mathorn1973/twist-j/issues/1806).
Author: A. M. Thorn <thorn@twistj.com>. Original text: Apache-2.0.

Public basis: ACTIVE Canon v105, immutable main/tag target
`892a0b11089d34e241e1eb76d2c03247022d18e6`. Existing claim identifiers below
refer to that tree. No scientific executable or formal gate is run here.

## 1. The conditional coherent construction

Let `H_S = C^5` have counting-orthonormal basis `|j>`, `j in Z/5`, and
`Z|j> = |j+1>`. On an added two-path space define

\[
C=|0\rangle\langle0|\otimes I+|1\rangle\langle1|\otimes Z^2.
\]

This C is a permutation of ten basis points. With the separately supplied
ready vector `|+>=(|0>+|1>)/sqrt(2)` and coherent output reading in the
plus/minus basis, the two branch operators are exactly

\[
K_0=\langle+|C|+\rangle=(I+Z^2)/2,\qquad
K_1=\langle-|C|+\rangle=(I-Z^2)/2.
\]

They obey `K_0^dagger K_0 + K_1^dagger K_1 = I`. A computational-basis
ready bit and a computational-basis read do not supply these operators.
Equivalently, preparing and recombining with a Hadamard makes the displayed
contact on a computational ready slice, but then those two coherent
operations are explicit resources. Classical random selection between I
and Z^2 gives a mixture of channels and lacks the cross terms in
`K_0 rho K_0^dagger`.

Write `V=1^perp` and `Pi=I-11^T/5`. Z preserves this faithful subspace.
For `phi^2=phi+1`, `phi>1`, the effect

\[
E_0=K_0^\dagger K_0=(2I+Z^2+Z^{-2})/4
\]

has eigenvalues `phi^(-2)/4` on characters k=1,4 and `phi^2/4` on k=2,3.
On the omitted constant character k=0 its eigenvalue is 1. Thus restricting
to V is a substantive source/code condition. These are effect weights;
neither physical energies nor event probabilities follow without their
separate reading and occurrence premises.

## 2. A genuine native word is not an actual-U schedule

The public native generators act on `x=(p1,p4,p1p,p4p,q,r)` in F5^6.
Their complete affine definitions, with every component taken modulo five,
are

```text
c=(2,1,3,4,1,1),       v=(0,0,0,0,1,0),
d(x)=c-x,             e(x)=c+v-x.
```

They are the definitions in the immutable [native verifier source][defs],
which is read here as source and is not re-executed. Direct substitution
gives `(e o d)(x)=x+v`, hence `(e o d)^2(x)=x+2v` for every checkpoint.

Canon section 2 gives `[d,e]=T_(0,0,0,0,3,0)`, with composition right to
left. Consequently the reverse commutator gives the desired translation:

\[
W=[e,d]=e\circ d\circ e\circ d
       =T_{(0,0,0,0,2,0)}.
\]

Its chronological command word is `d,e,d,e`. Explicitly the q coordinate
passes through `q, 1-q, 1+q, -q, q+2`. The four piston coordinates and r
have identical involutive transformations under d and e, so four such
letters restore them. This proves the word on every checkpoint, not only
on a five-state orbit. A unit q translation is `[d,e]^2`, so W is its
square. No word-length minimum is claimed.

This is a construction in the freely commanded alphabet
`Gamma=<a,b,c,d,e>`. Actual native evolution is instead

\[
U(n,x)=(n+1,g_{z(x)+2\theta_n}(x)),\quad
\theta_n=\operatorname{popcount}(n)\bmod2,
\quad(g_0,g_1,g_2,g_3,g_4)=(a,b,c,d,e).
\]

The selector is part of the law. One cannot replace its selected letter
by a desired command without supplying that intervention. In particular,
q translations change z; a word in Gamma need not be a valid continuation
of the synchronized native sheets. A controlled use of W on one path and
an identity action on the other is an additional control obligation, even
though the abstract ten-point controlled shift is a permutation.

Sources: [native law, Canon line 462][native-law],
[commutators, line 501][commutators], and
`QDD-PORT-QUOTIENT-ORIGIN-BOUNDARY [T]` at [line 6780][port-boundary].
The last claim explicitly distinguishes a constant commanded word from
source-dependent control and actual native commandability.

### 2a. The literal four-reflection control fails the selector

As freely commanded words, d,d,d,d is the identity and d,e,d,e is W.
They differ only in the second and fourth commands, so one retained path
bit could select between d and e at those two times in a supplied
controller. In the affine notation above the reflection centers are
c/2 and (c+v)/2 in F5^6; c and c+v are their affine offsets.

The unchanged actual U cannot carry out these literal four-tick paths.
Write t=theta_n and z=z(x). Since sum(c)=2 and sum(v)=1 modulo five,
d sends z to 2-z and e sends z to 3-z. If the selector has chosen d,
then z=3-2t; if it has chosen e, then z=4-2t. In both cases,

    z(U(n,x))=4+2t mod5,
    sigma(U(n,x))=4+2(t+theta_(n+1)) mod5.

Thus the next command after either selected reflection is exactly:

| Current clock bit t | Next clock bit | Next selected command |
| --- | --- | --- |
| 0 | 0 | e |
| 0 | 1 | b |
| 1 | 0 | b |
| 1 | 1 | d |

In particular two native paths at the same counter, both firing d in
the first tick, have the same next selected command regardless of their
other checkpoint coordinates. They cannot split into d versus e at the
second tick. Adding a coherent superposition of such points does not
alter this pointwise restriction on the selected commands.

There are also separate obstructions to the proposed individual words.
The substring d,e,d would require the middle clock bit to be both zero
and one, so it is impossible even with an arbitrary binary driver. More
generally any three consecutive commands all in {d,e} require three
identical clock bits. The actual Thue-Morse driver has no such triple:
every three consecutive indices contain an even-odd pair (2m,2m+1),
and theta_(2m+1)=1-theta_(2m). Hence neither d,d,d,d nor d,e,d,e is a
literal four-tick trajectory of U, from any starting checkpoint or time.

This is an analytical obstruction to this proposed direct schedule, not
a prohibition on every native realization of the two-path instrument.
A successor would need intervening commands, a different independently
specified encoding and decoding, or an explicitly enlarged controller.
It must still meet the complete contract in section 5. The common
reflection pattern by itself neither selects the two centers under U
nor supplies the coherent ready state and output recombination.

### 2b. A literal q register cannot close after any positive native block

There is a stronger obstruction when the proposed carrier is the literal
q coordinate and all other checkpoint coordinates must be restored. The
sheet maps in [U-GALOIS-FIBER-CODE][coherent-code], with entries ordered
by the input trace z=0,1,2,3,4, are

    tau_0=(0,4,0,4,4),       tau_1=(2,1,1,3,1).

They follow by summing the native generator coordinates with the actual
selector. Consequently the image of one step has trace in

    S_0={0,4} when theta_n=0,
    S_1={1,2,3} when theta_n=1.

Fix any common initial counter n and any length N>=1. The image of its
last step, and therefore of the complete block U^N, has trace in
S_(theta_(n+N-1)). This statement permits every actual earlier letter,
including a, b and c, and does not depend on the initial preparations.

Now fix the five other output checkpoint coordinates. Let q run through
F5. The five requested output addresses then have all five trace values,
because z=q+constant. They cannot all lie in either S_0 or S_1. Therefore
no such positive native block realizes a permutation of the full literal
q register while returning all other coordinates to their fixed ready
values. This excludes q->q and q->q+2 separately, and hence excludes the
proposed controlled pair. The fixed ready values may differ between the
two paths; the contradiction already applies to either complete path.
It also holds if the common final ready values differ from the initial
ones, provided they are independent of the logical q mark.

This is an output-address obstruction, not a prohibition on a decoded
five-cycle. A code that compensates q in another coordinate, a changed
output encoding, an external intervention or a distributed coherent code
requires a different argument. Adding more native ticks alone cannot
repair this literal register and reset contract.

### 2c. A fixed-address controlled shift on one common fired sheet

A second obstruction permits nonliteral q encodings. Fix ten distinct
checkpoint addresses x_(p,j), with p=0,1 and j in F5, all on one sheet
X_s={x:z(x)=s} with the same s in {1,4}. They share one counter n and
the same block length N>=1. Use these same checkpoint addresses for input
and output encoding; the counter itself advances from n to n+N and is
not required to return.

On these sheets the actual transitions are

| Input trace | theta=0: letter, next trace | theta=1: letter, next trace |
| --- | --- | --- |
| 1 | b, 4 | d, 1 |
| 4 | e, 4 | b, 1 |

Thus {1,4} is invariant, and all points on one starting sheet follow the
same selected word in b,d,e. In fact their next trace is 4+2 theta_n.
Let P exchange the first and third piston coordinates and the second and
fourth, while leaving q and r fixed. The full six-coordinate linear parts
are L_b=-P and L_d=L_e=-I. They commute and square to I. The compiled
checkpoint map of any such common word is therefore affine,

    F(x)=Lx+a,       L in {I,-I,P,-P},       L^2=I.

This is also the linear-part property in
[FIRED-COMMUTATOR-NOGO][commutators]. Suppose the block implements the
fixed-address controlled shift

    F(x_(0,j))=x_(0,j),
    F(x_(1,j))=x_(1,j+2)                  for every j in F5.

Choose any fixed address x_0 from the first path. Then a=(I-L)x_0 and
F(x_0+y)=x_0+Ly, so F^2=I on the entire affine checkpoint space. The
second path instead requires F^2(x_(1,j))=x_(1,j+4), different from
x_(1,j). This contradiction excludes the specified controlled shift for
every block length, including words with arbitrarily many intervening
b commands. A single fixed address and one five-cycle already suffice.

Here F^2 is the algebraic square of the compiled affine map. The argument
does not assume that a second actual time block repeats the first block's
driver word. It uses only the stipulated action of F on the invariant
set of encoded addresses.

The common starting sheet and unchanged checkpoint encoding are essential
scope conditions. Distinct-sheet source transients, changing output
encodings, different clock phases, unreturned controller coordinates and
distributed coherent codes are outside this statement. In particular
[U-GALOIS-FIBER-CODE][coherent-code] uses specified coherent correlations
and a different output representation; neither this obstruction nor the
literal-register obstruction contradicts its declared code transport.
They supply no native coherent preparation or output recombination.

### 2d. A positive origin-zero witness with one fixed coherent orbit code

The unchanged native selector does admit a partial positive realization
once a distributed coherent encoding is supplied. The following code is
the same at input and output; no inverse evolution is put into an output
decoder. The statement concerns one actual eight-tick prefix, including
its advancing counter, and does not claim a complete prepared instrument.

Write the four piston slots as \(p_1,p_2,p_3,p_4\), so a checkpoint is
\(x=(p_1,p_2,p_3,p_4,q,r)\), with all arithmetic in \(\mathbb F_5\),
and \(X_1=\{x:\sum_i p_i+q+r=1\}\).
Starting at counter zero, the actual Thue-Morse bits are
\(0,1,1,0,1,0,0,1\). Every checkpoint in \(X_1\) therefore follows
the same selected history:

| Counter \(n\) | \(\theta_n\) | Trace before | Selected letter | Trace after |
| ---: | ---: | ---: | --- | ---: |
| 0 | 0 | 1 | b | 4 |
| 1 | 1 | 4 | b | 1 |
| 2 | 1 | 1 | d | 1 |
| 3 | 0 | 1 | b | 4 |
| 4 | 1 | 4 | b | 1 |
| 5 | 0 | 1 | b | 4 |
| 6 | 0 | 4 | e | 4 |
| 7 | 1 | 4 | b | 1 |

This table follows directly from the sheet transitions in section 2c and
the binary digit sums of the eight displayed counter values. It is an
analytical evaluation of a specified prefix, not a scientific enumeration.
Since \(b^2=I\), the chronological word \(b,b,d,b,b,b,e,b\) has full
checkpoint action

\[
F=b\circ e\circ b\circ d.
\tag{N-01}
\]

Let \(P(p_1,p_2,p_3,p_4,q,r)=(p_3,p_4,p_1,p_2,q,r)\), so the
generator \(b(x)=-Px\).
Using the offset \(c_0=(2,1,3,4,1,1)\) from section 2 and
\(v_q=(0,0,0,0,1,0)\), \(v_r=(0,0,0,0,0,1)\), direct composition gives

\[
F(x)=x-c_0-P(c_0+v_q)=x+2v_q-2v_r.
\tag{N-02}
\]

Indeed the four piston entries of \(c_0+Pc_0\) vanish modulo five;
the last two entries of \(c_0+P(c_0+v_q)\) are \(3,2\).
Thus the actual prefix restores all four pistons and sends
\((q,r)\) to \((q+2,r-2)\), preserving the trace. Its checkpoint map
has order five and no fixed checkpoint address.

Use the counting Hilbert representation of the declared checkpoints.
Let \(k\in\mathbb F_5\) label the logical five-state source, and let the
logical path space have basis \(|0\rangle,|1\rangle\). Define one encoder
\(E:\mathbb C^2\otimes\mathbb C^5\longrightarrow\ell^2(X_1)\) by

\[
\begin{aligned}
E|0,k\rangle
 &=\frac1{\sqrt5}\sum_{t\in\mathbb F_5}
       |k,0,0,0,t,1-k-t\rangle,\\
E|1,k\rangle
 &=|0,1,0,0,k,-k\rangle.
\end{aligned}
\tag{N-03}
\]

Every displayed address has trace one. Different \(k\) on path zero
have disjoint piston supports; its five summands have distinct \(q\).
The five path-one addresses are distinct, and their second piston is
one whereas every path-zero address has second piston zero. Consequently
all ten encoded vectors are orthonormal and \(E^*E=I_{10}\).
The whole code uses 30 distinct checkpoint addresses.

Put \(R|k\rangle=|k+2\rangle\) and \(D=\operatorname{diag}(I_5,R)\);
this \(D\) is the controlled shift called \(C\) in section 1.
Translation (N-02) permutes each uniform sum in the first line of
(N-03) by \(t\mapsto t+2\), leaving that encoded vector unchanged.
It sends the second line at \(k\) exactly to the second line at \(k+2\).
Thus the fixed checkpoint code intertwines the compiled native map and
the controlled shift on the entire ten-dimensional logical space.

The full counter must still be shown. Define
\(E_n=|n\rangle_{\rm counter}\otimes E\), and let \(N_8\) be the
deterministic linear extension of the actual \(U^8\), restricted to
the admitted initial sheet at counter zero. Then

\[
\boxed{N_8E_0=E_8D.}
\tag{N-04}
\]

Each prefix has a common selected word on \(X_1\). Each native letter in
that word is an affine bijection of the complete checkpoint space, so
its restriction and every composed prefix are injective on \(X_1\).
Their counting linear extensions are therefore isometries on this whole
initial sheet, not just on the ten code vectors. Norms, inner products
and all code coherences are preserved at every prefix; tensoring with
an arbitrary passive reference preserves the same statement. This does
not make the selected native map globally injective on other sheets.

There is also an exact encoded witness for the full rational two-port
matrix \(V\) in PROOF.md, equation (JI-06). To distinguish that operator
from the faithful source subspace \(V=1^\perp\) used in section 1 here,
denote it by \(\mathcal V\) in this paragraph. With

\[
H_2=\frac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix},
\quad B=H_2\otimes I_5,\quad
\mathcal V=BDB
=\frac12\begin{pmatrix}I+R&I-R\\I-R&I+R\end{pmatrix},
\]

set \(E_B=EB\) and \(E_{B,n}=|n\rangle_{\rm counter}\otimes E_B\).
Since \(B^2=I\), equation (N-04) gives

\[
\boxed{N_8E_{B,0}=E_{B,8}\mathcal V.}
\tag{N-05}
\]

Both occurrences of \(E_B\) are the same fixed checkpoint encoder.
For a logical ready input \(|0\rangle\otimes\psi\), the encoded output
is exactly \(E_{B,8}(|0\rangle K_0\psi+|1\rangle K_1\psi)\), with the
two \(K_i\) of section 1. This is a full-code amplitude identity; it
does not discard the second branch.

**What has been supplied.** The uniform orbit modes in (N-03), their
relative phases, the counting Hilbert representation and their initial
preparation are declared resources. Native deterministic evolution does
not prepare those sums from single addresses. Passing to \(E_B\) also
puts the ready-path coherence and output recombination into the fixed
encoder/readout convention. The native prefix transports that code; it
does not by itself prepare or physically read it. The formula is not a
target-times-inverse-evolution decoder: \(F\) was derived from the
actual selector, and both endpoints use the explicitly displayed same
orbit code. Its supplied nature remains part of the claim.

There is no contradiction with section 2b: the source \(q\) mark is
compensated by \(r\), which changes by \(-2\) and is not a common reset
register. There is no contradiction with section 2c: the identity path
uses fixed coherent uniform modes, not fixed checkpoint addresses.
The translation \(F\) has no fixed address, while its counting
representation has these fixed vectors.

Finally, (N-04)-(N-05) concern counters 0 and 8. The checkpoint identity
\(F^5=I\) does not reset that counter or prove that every later eight-tick
native interval repeats \(F\); the future Thue-Morse words remain part
of the unchanged law. No repeated-use budget, retained physical record,
occupied-memory behavior, energy/work account or occurrence rule is
provided by this partial witness. These remain obligations of section 5.

## 3. Exact point-preparation obstruction

Freeze the literal point encoding: a logical ready basis state is one
native basis point, and deterministic native evolution is represented by
`N_f|x>=|f(x)>`. Enlarged deterministic history labels are allowed, but no
coherent preparation is silently introduced in the encoder or decoder.

The actual global U is not a permutation. At counter zero, the points
x=(0,0,0,0,1,0) and x'=(2,1,3,4,3,1) have traces one and four.
The selector chooses b and e respectively; both images are
(0,0,0,0,4,0), at counter one. The forward counter also has no predecessor
at zero. The known-sheet bijections used above must not be promoted to a
global bijection or an arbitrary-state unitary law.

The support bound does not require injectivity. For a finite-support
vector and any deterministic map f,

    (N_f psi)_y=sum_(x:f(x)=y) psi_x,
    supp(N_f psi) subseteq f(supp psi),
    |supp(N_f psi)| <= |supp psi|.

Every positive diagonal input likewise remains diagonal under
N_f rho N_f^*. With collisions this last operation is not generally
trace preserving on arbitrary coherent inputs; it is not silently
declared a global quantum channel. On the admitted isometric codes the
norm statements have their separate proofs.

Then a single ready point remains one point after every finite protocol.
It cannot become the sum of two distinct encoded path points. This remains
true if f has collisions: one occupied input basis point still has one
image. Monomial phases change only its phase. Independent classical
mixtures of point preparations and monomial operations remain diagonal
and likewise do not create the missing off-diagonal path coherence.

This is a precise impossibility for that point encoding and gate class.
It is not an impossibility theorem for arbitrary coherent encodings,
pre-existing coherent auxiliaries, or non-diagonal coherent output maps.
Nor does an odd cycle alone exclude a two-valued reading: the native
alphabet has involutions, and the complete U has an unbounded counter.
The two classes in `QUBIT-FROM-F5 [T]` are a sign quotient, not an admitted
preparation of a coherent `|+>` state.

In a closed model allowing only these maps on its literal global point
basis, future off-diagonal coherence must therefore come from initial
global coherence. This does not select a particular initial plenum and
does not prohibit dynamical preparation of a subsystem using a coherent
environment already included in that global state. A swap of a prepared
coherent auxiliary into a subsystem is a simple permutation example.
Likewise logical mixing in a supplied distributed code is not excluded;
the no-go concerns its preparation from a single literal global point.

## 3a. A uniform sheet, its code projection and a point record

Suppose the initial checkpoint state is the coherent uniform vector on
the trace-one sheet. This is an additional initial-state hypothesis.
There are \(5^5=3125\) points in \(X_1\). The translation \(F\) in
(N-02) has 625 disjoint orbits of length five, indexed by the four piston
coordinates \(p\in\mathbb F_5^4\). Define their normalized uniform modes
and the uniform sheet vector by

\[
u_p=\frac1{\sqrt5}\sum_{q\in\mathbb F_5}
 |p_1,p_2,p_3,p_4,q,1-\sum_i p_i-q\rangle,
\qquad
\Omega=\frac1{\sqrt{3125}}\sum_{x\in X_1}|x\rangle
       =\frac1{25}\sum_p u_p.
\tag{N-06}
\]

These 625 modes are orthonormal. Translation by two permutes the five
terms of each \(u_p\), so its counting extension fixes every \(u_p\)
and \(\Omega\). The actual prefix therefore sends
\(|0\rangle_{\rm counter}\otimes\Omega\) to
\(|8\rangle_{\rm counter}\otimes\Omega\); it does not localize it.

Let \(f_0=5^{-1/2}\sum_k|k\rangle\) be the logical constant source
mode, and let \(P_E=EE^*\) project onto the ten-dimensional code (N-03).
The overlap of \(\Omega\) with each path-zero orbit mode is \(1/25\);
with each path-one point it is \(1/(25\sqrt5)\). Hence exactly

\[
E^*\Omega=\frac{\sqrt5|0\rangle+|1\rangle}{25}\otimes f_0,
\qquad
\|P_E\Omega\|^2=\frac6{625}.
\tag{N-07}
\]

If this code projection is selected and normalized, its decoded state
and its state in the Hadamard encoder \(E_B\) are respectively

\[
\chi=\frac{\sqrt5|0\rangle+|1\rangle}{\sqrt6}\otimes f_0,
\qquad
E_B^*\frac{P_E\Omega}{\|P_E\Omega\|}
=\frac{(\sqrt5+1)|0\rangle+(\sqrt5-1)|1\rangle}{\sqrt{12}}
 \otimes f_0.
\tag{N-08}
\]

Both have only the constant source mode: their projection into
\(\mathbb C^2\otimes f_0^\perp\) is zero. In particular every ready
code vector \(E_B(|0\rangle\otimes\psi)\) with \(\psi\perp f_0\)
is orthogonal to \(\Omega\). Since \(Rf_0=f_0\), the contact has
\(K_0f_0=f_0\), \(K_1f_0=0\). The displayed path populations belong
to the projected initial state; they are not clicks generated from a
fresh path-zero input.

This conclusion uses the actual uniform coefficients, not invariance
alone. Indeed \(\operatorname{Fix}(D)=(|0\rangle\otimes\mathbb C^5)
\oplus\operatorname{span}\{|1\rangle\otimes f_0\}\). Arbitrary data
on the identity path can be invariant. The uniform sheet gives equal
overlaps with its five selected orbit modes and therefore gives \(f_0\).

A uniform point distribution does not specify this coherent state.
For comparison put \(\rho_{\rm mix}=I_{X_1}/3125\). Both states give
probability \(1/3125\) at every point, but their code projections differ:

| Initial state | Code probability \(\operatorname{Tr}(P_E\rho)\) | Normalized decoded code state |
| --- | ---: | --- |
| \(|\Omega\rangle\langle\Omega|\) | \(6/625\) | \(|\chi\rangle\langle\chi|\) |
| \(\rho_{\rm mix}\) | \(2/625\) | \(I_{10}/10\) |

The second row follows from \(E^*\rho_{\rm mix}E=I_{10}/3125\).
Also distinguish the code projector from the diagonal projector onto
the set \(S\) of its 30 used addresses. The latter has probability
\(30/3125=6/625\) on both inputs. For \(\Omega\) its output equals
\(P_E\Omega\), because \(S\) consists of six complete \(F\)-orbits.
For the mixed input the normalized output is instead \(I_S/30\), of
rank 30; it is not a state supported wholly in the rank-ten code.

A specified point can arise as a conditional result of an additionally
declared point measurement. With \(P_x=|x\rangle\langle x|\), its
selected and nonselected operations on the uniform pure input are

\[
\Pr(x)=\frac1{3125},\qquad
\rho_{\mid x}=|x\rangle\langle x|,\qquad
\sum_x P_x|\Omega\rangle\langle\Omega|P_x
 =\frac{I_{X_1}}{3125}.
\tag{N-09}
\]

The last state is a mixture, not one selected point. A coherent record
coupling with orthonormal record states gives yet another complete state:

\[
|x\rangle|{\rm ready}\rangle\longmapsto|x\rangle|x\rangle_{\rm rec},
\qquad
\Omega|{\rm ready}\rangle\longmapsto
 \frac1{\sqrt{3125}}\sum_x|x\rangle|x\rangle_{\rm rec}.
\tag{N-10}
\]

This joint state remains pure and is entangled. Tracing the record gives
the mixture in (N-09); conditioning on one record gives its corresponding
point under the declared instrument rule. Neither the record coupling,
its preparation and reading, nor an occurrence rule follows from \(F\)
or from the orbit decomposition. Likewise a selected code projection
must retain its complementary failure branch in a complete instrument.

Thus a coherent uniform-plenum hypothesis supplies pre-existing orbit
coherence, but does not by itself prepare the complete ready code with
a balanced logical source. A classical uniform distribution likewise
does not supply the declared orbit coherence or a pure ready source.
These are analytical conditional statements about the fixed code and
proposed initial states, not a new native preparation theorem.

## 4. Complete classical-endpoint obstruction for this unsharp effect

Take five distinct point preparations at one common clock phase and any
finite deterministic native protocol with complete endpoints f(j). Use
the free counting representation on C^5, source subspace V, and a final
classical endpoint effect `0<=D<=I` diagonal in the endpoint basis.
This is the class of `U-POINT-SOURCE-SHARP-READOUT-NOGO [T]`, but the
following argument addresses the present unsharp E_0 directly.

If `f(j)=f(k)` for j!=k, then `v=|j>-|k>` belongs to V, has norm squared
2, and satisfies `N_f v=0`. Thus the complete code norm is not preserved.
Every subsequent linear endpoint branch also kills v; the pulled-back
effect has zero weight on it. In contrast K_0 is invertible even on C^5:
`1+zeta^(2k)` is nonzero for every fifth root zeta^k, since -1 is not a
fifth root. Therefore `v^dagger E_0 v>0`, excluding equality in this case.

If f is injective, its five output points are orthonormal and N_f is an
isometry. The complete endpoint-effect class on V is then

\[
F(w)=\Pi\operatorname{diag}(w_0,\ldots,w_4)\Pi\big|_V,
\qquad 0\le w_j\le1.
\]

Every w is possible by assigning those responses to the distinct endpoint
points. This includes classical randomized processing and arbitrary
deterministically supplied endpoint histories.

Suppose `F(w)=E_0|_V`. Since Pi commutes with Z and E_0 is a polynomial
in Z, average the equality over conjugation by Z^m, m=0,...,4. Cyclic
averaging makes every diagonal entry equal to `w_bar=(sum_j w_j)/5`:

\[
E_0|_V=\frac15\sum_{m=0}^4 Z^mF(w)Z^{-m}
      =\bar w I_V.
\]

This contradicts the two distinct golden eigenvalues in section 1.
Hence neither injective nor noninjective f realizes E_0 in this complete
point/free-representation/classical-endpoint class. The proof is not a
claim that E_0 is sharp, and does not misuse the earlier sharp-projector
conclusion. Changing the encoding or allowing a coherent endpoint read
changes the hypotheses. No complete physical apparatus class is excluded.

The canonical endpoint classification is at [Canon line 3225][point-nogo].
`U-GALOIS-FIBER-CODE [T]` supplies an explicit compatible alternative:
actual U transports a separately prepared correlated coherent code
isometrically in the declared free representation. Its source correlations
are substantive inputs, not a derivation of their preparation. See
[Canon line 3108][coherent-code].

## 5. Minimal positive native-realization contract

A positive successor should freeze the following before testing the target.

1. **Carrier and independent code.** Give all native coordinates, path
   states, source states, controller, counter, records and resource slots.
   Declare C^5 or V, the norm, and fixed encoding/decoding rules. A code or
   ready state defined afterwards by the desired K_0 is not its derivation.
2. **Ready preparation.** Exhibit how the coherent path state is prepared,
   or declare it supplied. State all initial source/path correlations.
   For a common-ready claim, the entire auxiliary ready state is independent
   of the source, including hidden coordinates and retained history.
3. **Actual controlled program.** Exhibit actual selected native histories
   or a declared enlarged law implementing I versus Z^2 at a common final
   counter. List every actuator and control predicate. A free phase factor
   `Y(U omega)=Z Y(omega)` rotates both paths and does not itself supply
   their relative control. The full native counter never returns after
   five steps, even when a five-phase factor does.
4. **Whole-code equality.** Prove an intertwining with the declared contact
   on the entire admitted source/path code, with one common phase, all
   reachable auxiliary states and every required continuation. Verify each
   prefix's norm and coherence, or supply the full instrument if a prefix
   is nonunitary. Basis output labels alone are insufficient if phases,
   discarded coordinates or normalization are unspecified. Do not define
   the output code as the desired inverse applied after the calculation.
5. **Complete instrument and records.** Supply both branches, their actual
   post-states, orthogonal output records, persistence interval and occupied
   memory behavior. Distinguish coherent path recombination from forgetting
   a fine path record. A no-click branch is a selected branch of a complete
   instrument, not an absent accounting obligation.
6. **Renewal, funding and occurrence.** Identify fresh ready slots, resets,
   retained records and any paid control. A finite-horizon or repeatable
   device must state its horizon and capacity. A conserved account or
   Hamiltonian is separate from the Hilbert norm. Finally declare the
   event/occurrence rule separately from the amplitude identity.

`QDD-SELECTED-SOURCE [D]` and `QDD-SELECTED-BORN [D]` already distinguish
adopted coherent preparation/control from adopted Born occurrence; neither
is derived merely by the native code transport. See [line 18727][source]
and [line 18784][born]. The conditional two-path contact is constructive
once its coherent interfaces are supplied. Its realization by unchanged U
remains open under the complete contract above.

[native-law]: https://github.com/mathorn1973/twist-j/blob/892a0b11089d34e241e1eb76d2c03247022d18e6/canon/CANON.md#L462
[defs]: https://github.com/mathorn1973/twist-j/blob/892a0b11089d34e241e1eb76d2c03247022d18e6/probes/P-FIRED-COMMUTATOR-NOGO-1/verify.py#L28
[commutators]: https://github.com/mathorn1973/twist-j/blob/892a0b11089d34e241e1eb76d2c03247022d18e6/canon/CANON.md#L501
[port-boundary]: https://github.com/mathorn1973/twist-j/blob/892a0b11089d34e241e1eb76d2c03247022d18e6/canon/CANON.md#L6780
[point-nogo]: https://github.com/mathorn1973/twist-j/blob/892a0b11089d34e241e1eb76d2c03247022d18e6/canon/CANON.md#L3225
[coherent-code]: https://github.com/mathorn1973/twist-j/blob/892a0b11089d34e241e1eb76d2c03247022d18e6/canon/CANON.md#L3108
[source]: https://github.com/mathorn1973/twist-j/blob/892a0b11089d34e241e1eb76d2c03247022d18e6/canon/CANON.md#L18727
[born]: https://github.com/mathorn1973/twist-j/blob/892a0b11089d34e241e1eb76d2c03247022d18e6/canon/CANON.md#L18784
