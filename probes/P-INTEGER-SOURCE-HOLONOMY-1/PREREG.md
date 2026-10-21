# P-INTEGER-SOURCE-HOLONOMY-1

Status: PREREGISTERED proposal; NON-CANONICAL.

Owner: A. M. Thorn, session `integer-gravity-2026-10-18`.
Public ownership: https://github.com/mathorn1973/twist-j/issues/1632
Branch: `probe/P-INTEGER-SOURCE-HOLONOMY-1`.
Base: `dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d`, Public Canon v103.

## 1. Equation and claims

This probe asks whether a selected, complete integer apparatus can couple a
stored source to nontrivial Hermitian transport, record its effect in an
occupied receiver, and account for every accepted and rejected microstep.
It also tests a precise obstruction to reading the existing K1 history with
fixed denominator. It does not assert that the apparatus is general relativity.

Let O=Z[j]=Z[X]/(1+X+X^2+X^3+X^4), K=Q(j), conjugation bar(j)=j^-1,
phi=-j^2-j^3, J=1+j^2, and O+=Z[phi]. Define

```text
A = diag(J,phi),           A^-1 = diag(-j-j^2,phi-1),
B(q) = [[1,q],[0,1]],      B(q)^-1 = B(-q),
L(q) = [[1,0],[q,1]],
v = J/phi-1 = -2+j-j^2,   w = v bar(v) = 9-5phi.
rho(M)H = M H M^dagger,   det H = a d - c bar(c),
H = [[a,c],[bar(c),d]],    a,d in O+, c in O.
```

The complete state is X=(s,q,H,R,Z,p,b,epsilon): s,q are arbitrary integers;
H,R,Z are arbitrary Herm2(O); p is in Z/6; b is a nonnegative integer;
epsilon is +1 or -1. No positive-semidefinite constraint applies to the
detector Z. The bare bijection T increments p after exactly one operation:

| Input phase p | Operation; all unmentioned registers are retained |
| --- | --- |
| 0 | (s,q) <- (s-q,s) |
| 1 | H <- rho(B(-q))H |
| 2 | H <- rho(A^-1)H |
| 3 | H <- rho(B(q))H |
| 4 | H <- rho(A)H |
| 5 | Z <- Z+H-R |

T^-1 decrements phase and inverts that phase's operation. In particular the
source inverse is (s',q')->(q',q'-s'), and the detector inverse subtracts H-R.

For x=(s,q,H,R,Z,p), define the selected arithmetic account

```text
Q(s,q) = s^2-sq+q^2,
N(H) = Tr_(K/Q)(tr(H^2)),
E(x) = 1+Q(s,q)+N(H)+N(R)+N(Z).
y = T^epsilon(x),  c = b+E(x)-E(y).
F(x,b,epsilon) = (y,c,epsilon) if c>=0;
                 (x,b,-epsilon) otherwise.
```

The proposed inverse of F uses y=T^(-epsilon)(x) and the same funding test.
An unsuccessful microstep reflects the stored direction, not the whole
six-phase cycle. There is no external time-dependent instruction.

Claims A1-A5, each conditional on these selected definitions:

1. A1: T and F are total bijections of their declared carriers; F preserves
   E+b and nonnegative b, including occupied receivers and reflected states.
2. A2: N is a positive definite integer quadratic form. Every fixed E+b
   shell is finite, and every full F orbit on it is periodic.
3. A3: all four transport phases preserve det H in O+; their loop is
   C_q=A B(q) A^-1 B(-q)=[[1,q v],[0,1]]. For q!=0 its action is nontrivial.
   The source kick is reciprocal between s and q, at exactly this scope.
4. A4: the paired ready experiment below changes the same initially nonzero
   read coordinate into distinguishable values. Its predicted phase costs,
   sharp budgets, rejection state and exact reversal hold.
5. A5: for the ready experiment, 36 bare phases restore s,q,H,p but add
   [[10w,6s_initial v],[6s_initial bar(v),0]] to Z. The record has a cost;
   a finite bank cannot sustain this all-forward accumulation forever.

## 2. Code and independent method

`verify.py` is the accepted entry point. It uses only Python's standard
library and exact integers/Fraction. It implements the author computation
and invokes `breaker.py` as a separate process, comparing the complete
certificate defined below. Both files are frozen together before either is
executed, imported, or used to generate data. Compilation and static review
are allowed. `PROOF.md`, `SOURCE.md`, this file and both implementations
are covered by `FROZEN.sha256` at the public pin.

The author uses four polynomial coefficients and polynomial reduction for
O. The breaker is separately written from this preregistration, using
five cyclic coefficients modulo the all-ones relation and direct Hermitian
coordinate transforms. It must not read, import, copy or execute verify.py.
Both implementations independently encode the fixtures and K1 recurrence.
Their shared input is this specification, not shared executable arithmetic.

The implementers and analytical reviewers are agents in the same assisted
session. They have seen the predicted mathematical outcomes. Independence
means separate implementation/method with author-code exclusion, not
external review or result-blind experimentation.

Scientific mismatches produce a completed, explicit FAIL certificate and
exit 0; operational exceptions preventing a certificate are nonzero and
leave an abandoned pin under POLICY.md. A FAIL is not repaired under this
identifier. No scientific threshold or code is changed after pinning.

## 3. Carrier, data and finite audit

The canonical representation of an O element is its four integers in
(1,j,j^2,j^3). A Hermitian register has eight integers

```text
H8=(a0,a1,d0,d1,c0,c1,c2,c3),
a=a0+a1 phi, d=d0+d1 phi, c=c0+c1 j+c2 j^2+c3 j^3.
pack(X)=[s,q,p,b,epsilon,*H8,*R8,*Z8].
```

Lists, not tuples or strings, are used in certificates. A digest over rows
is SHA-256 of the concatenation, in the specified order, of
`json.dumps(row,separators=(",",":"))+"\n"`, UTF-8. No spaces, floats,
platform information or nondeterministic iteration occur in these rows.

### Algebra and transport audit

Visit H8 in lexicographic `itertools.product((-1,0,1),repeat=8)` order.
For each H, check the formula for N in PROOF.md and its lower bound
N(H)>=2*sum(H8_i^2). Check exact determinant preservation for the six gates
in this order: A,A^-1,B(1),B(-1),L(1),L(-1).
The digest row is `[list(H8),[list(rho(M)H8) for M in gate_order]]`.
There are 6561 rows and 39366 transport evaluations. This finite audit
supports, and does not replace, the general determinant/positivity proofs.

Separately check these four negative controls exactly: diag(J,1) has
absolute field norm of determinant one but changes det(I); j I is
nonidentity with identity Hermitian action; C_1 and I both have matrix trace
two despite different actions; pure frame differences telescope to I.
For the last control choose g0=I,g1=A,g2=B(1), edges M10=g1*g0^-1,
M21=g2*g1^-1,M02=g0*g2^-1, and form M02*M21*M10.
These controls block an invalid inference, not the selected apparatus.

### Complete-step audit

Let

```text
O8=(0,0,0,0,0,0,0,0)
D8=(0,0,1,0,0,0,0,0)
I8=(1,0,1,0,0,0,0,0)
J8=(1,0,1,0,0,1,0,0)
fixtures (H8,R8,Z8), in this order:
0: (D8,D8,J8)
1: (I8,D8,(0,1,1,-1,1,1,-1,0))
2: ((1,-1,-1,1,1,0,-1,1),I8,(-1,0,-1,0,0,-1,0,0))
3: (O8,O8,O8)
```

Nested loop order is s in (-1,0,1), q in (-1,0,1), p in range(6),
epsilon in (-1,1), bank in (0,1,12,32,116,346,715,716,771,772), then
fixture in the listed order. For all 4320 full states X, compute F(X) and
F^-1(X), check both inverse compositions, both energy identities,
nonnegative banks, Hermitian integrality, and unchanged R. The digest row
is `[pack(X),pack(F(X)),pack(F^-1(X))]`. The window is a test set, not an
invariant carrier or exhaustive proof about all integer states.

### Source, occupied readout and budget experiment

For a=-1 then +1 set s=a,q=0,H=R=D8,Z=J8,p=0,epsilon=+1.
The read coordinate coeff_j(Z01) initially equals 1. The fixed reader is
coeff_j(Z01)-1. Six successful forward microsteps yield

```text
H_out=[[w,a v],[a bar(v),1]],
Z_out=[[1+w,j+a v],[bar(j)+a bar(v),1]].
E prefixes, including the initial state:
a=-1: (26,26,38,58,142,372,742)
a=+1: (26,26,38,58,142,372,798)
sharp initial budgets: a=-1 ->716; a=+1 ->772.
```

For each a, audit six funded microsteps for each initial bank in
(715,716,771,772), in that order. The first five steps succeed. The last
step succeeds iff its corresponding sharp budget is met. Otherwise it
retains p=5,H=H_out,Z=J8 and the current bank, and flips epsilon. Check
exact reversal of each whole recorded six-step history with F^-1.
Hash every row `[a,initial_bank,[pack(X_0),...,pack(X_6)]]` into the
experiment digest (eight rows). Compare each bare T prefix cost to the
analytical sequence. Common bank 772 ends at 56 for a=-1 and 0 for a=+1;
the occupied read coordinate ends at 0 and 2, respectively.

Check 36 bare forward phases for both signs, with no claim that these
unfunded trajectories are physical F histories. Confirm restoration of
s,q,H,R,p and the exact detector increment in A5. Certificate increments
are H8 lists, ordered by a=-1,+1.

### K1 bridge precision

Use exactly the v103 `DEF-K1-LINEAR-METRIC` words in this order:
0010,0011,0100,0101,0110,1001,1010,1011,1100,1101. For each word set
u_t=w_(t+2)-w_t and h_t(r)=[delta_(r,u_t)+delta_(r,u_t+1)]/2 for t=0,1,
with r modulo five. Then for all n>=1,

```text
h_(n+1)=[460h_n(r)+29(h_n(r+1)+h_n(r-1))
         +65(h_n(r+2)+h_n(r-2))]/324-h_(n-1)(r).
```

Claim K1: if d_n is the least positive common denominator of the five
reduced rational entries, v_3(d_n)=4(n-1) for every word and n>=1.
The universal 3-adic proof is in PROOF.md. The finite audit visits every
word and n=0,...,24. It checks the recurrence, sum h_n=1 and the stated
valuation (v_3(d_0)=0 as well). Each digest row is
`[word,n,[[numerator,denominator] for h_n(r) in r=0,...,4]]`.
There are 250 rows. The author uses Fraction evolution; the breaker uses
integer scaled recurrence before reducing fractions for certification.
No stochastic weights or empirical data are used.

The fixed-frame square-class obstruction and the nonintegral principal
four-dimensional trace are analytical boundaries in PROOF.md; finite
numeric sampling is not evidence for those universal statements.

Analytical bridge corollary: on any one fixed finite-energy shell of F,
every fixed single-valued current-state reader with rational K1 outputs
has finite image and hence bounded denominators. No such reader can
reproduce the complete K1 history of even one admitted word. This includes
arbitrary nonlinear readers on that shell, not just polynomial readers.
An external unbounded counter/history or increasing total resources changes
this full-state contract and is outside the obstruction.

### Exact certificate interface

Both implementations return this dictionary (keys sorted on serialization):

```text
schema: "P-INTEGER-SOURCE-HOLONOMY-1/v1"
constants: {phi:[0,0,-1,-1],J:[1,0,1,0],v:[-2,1,-1,0],
            w:[9,0,5,5],trace_w:26,trace_w2:294}
transport_rows: 6561
transport_sha256: digest specified above
step_rows: 4320
step_sha256: digest specified above
experiment_rows: 8
experiment_sha256: digest specified above
prefix_costs: [[-1,[26,26,38,58,142,372,742]],
              [1,[26,26,38,58,142,372,798]]]
detector_increments_36: [[-1,list(delta_Z_minus8)],[1,list(delta_Z_plus8)]]
k1_rows: 250
k1_sha256: digest specified above
negative_controls: [true,true,true,true]
```

The constants and costs must be computed and checked against the displayed
predictions, not merely printed. `breaker.py` writes exactly one JSON
object plus newline. On a scientific failure it instead returns
`{"failure":"precise check label"}`. `verify.py` compares the complete
certificate, reports which gate failed, and prints deterministic summary
lines and the aggregate PASS or FAIL. Its exact successful stdout is
committed only after the first public-pinned run.

## 4. Systematics, custody and limits

All state, F, resource weights, phase order, controlled gates, preparation,
reference, comparison and reader are NEW_DECLARED. Neither the added shear
nor A^-1 is supplied here as a forward contact of the original U. The
source-link kick reads s,q, not a curvature tensor or H,R,Z. The latter
affect admission only through the account. The first kick does not deplete
the source. This is not a derived gravitational backreaction law.

Hermitian matrices here are vectors of a fixed determinant quadratic
space. H and its Lorentz transport are not themselves a four-dimensional
metric. The principal real interpretation needs an embedding choice.
Rank eight integrality in O is not a discrete rank four spacetime lattice.
Matrix trace alone cannot detect shear holonomy, central j phase is
invisible to rho, and commuting shear families do not establish generic
curvature. A physical local curvature interpretation additionally needs a
spacetime complex with specified 2-cells, a solder/frame relation and a
torsion/connection law. None is silently inferred here.

E is a coercive arithmetic cost over both complex embeddings, not native
or measured energy. Internal p is control storage, not an admitted
material clock. Bank reflection costs no separate positive toll by
definition; it preserves the declared account. Finite-shell recurrence
precludes a permanent monotone record or a derived arrow of time here.

The K1 obstruction rules out fixed denominator, including fixed polynomial
readings with bounded rational coefficient denominators. It does not rule
out a numerator/denominator pair whose denominator is part of the state,
variable precision, field extensions, or a different metric construction.
The finite horizon 24 is fixed before running and is not the proof horizon.

Public source custody is recorded in SOURCE.md. No private files, physical
datasets or third-party code are inputs. Existing native-source and
P-recurrence draft lanes remain separately owned and unpromoted.

## 5. Failure thresholds and stopping rule

Every equality is exact; the tolerated discrepancy is zero. Any violated
claimed inverse, resource identity, determinant identity, finite row count,
source readout, predicted budget or K1 valuation fires its named falsifier.
Any author/breaker certificate discrepancy blocks acceptance even when
both programs self-report success. No finite run promotes an all-state or
all-time claim without its proof. A failed negative control invalidates the
audit; a successful negative control rejects only its named shortcut.

Pin this complete content and both accepted code files publicly, record
their SHA-256 values, then run. Do not amend, rebase, squash, force-push,
replace code or move thresholds after pinning. A completed scientific
failure is retained as F at its exact scope; an operationally abandoned
pin consumes the identifier. No successor is silently substituted.

## 6. Action layer and promotion

Everything constructed and proved here is L1 mathematics on the declared
state. Definitions are candidate-D; universal claims are candidate-T pending
independent proof review; finite audit is evidence only for its actual
enumeration. The two-architecture computation gate is the unchanged public
PR workflow running this same verify.py and breaker.py on x86_64 and
aarch64 against one committed EXPECTED.txt.

No L1-to-L2/L3/L4/L5/L6 lift is claimed. Native admission, matter-clock
coupling, metric/connection identification, dynamical source law, Einstein
constraints, continuum behavior and physical predictions remain separately
named obligations. This probe changes neither Canon nor registered gates.
Any promotion or Canon fold is a separate reviewed action.
