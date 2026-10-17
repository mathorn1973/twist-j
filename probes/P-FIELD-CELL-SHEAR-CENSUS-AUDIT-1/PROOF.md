# Independent RC derivation

PUBLIC / NON-CANONICAL / L1. Prepared before exposure to the author's proof,
program, execution or result. This is a mathematical audit of precisely the
five cells in PREREG.md, not a claim about all cell complexes or a physical
selection of the canonical cell. Exposed numerical hypotheses are acknowledged.

## 1. Coordinate recurrence and characteristic polynomial

Let C have full column rank k, let G=C^t C, and use the ordered state (z,M)
with E=Cz. From the two successive shears,

    z' = z+M,       M' = M-Gz',

we get M=z'-z and the second-order recurrence

    z_(n+2) = (2I-G)z_(n+1)-z_n.

The change (z,M) -> (z,z+M) is integral unimodular. It conjugates A_G to the
block companion matrix [[0,I],[-I,2I-G]]. Therefore

    det(XI-A_G) = det(X^2 I+(G-2I)X+I).

For example, elimination for X nonzero proves the companion determinant
identity over Q(X); equality of polynomials extends it to X=0. This is an
identity, not an eigenvalue counting heuristic. It proves det(A_G)=1.
Directly recovering M=M'+Gz', then z=z'-M, gives the integer inverse

    A_G^-1 = [[I-G,-I],[G,I]].

Consequently A_G+A_G^-1=diag(2I-G,2I-G). The verifier constructs A_G from
basis images of the coordinate update and independently obtains its
characteristic polynomial by Newton identities from exact power traces.
It does not implement the author's advertised polynomial-determinant method.

For scalar g the factor is X^2+(g-2)X+1. For a two-by-two G with diagonal
entries a,b and offdiagonal s=+/-1 it is

    (X^2+(a-2)X+1)(X^2+(b-2)X+1)-X^2.

This yields the entire fixed family:

| G with positive offdiagonal | Characteristic polynomial | Exact order |
|---|---|---|
| (2) | X^2+1 | 4 |
| (3) | X^2+X+1 | 3 |
| [[2,1],[1,2]] | X^4+X^2+1=(X^2+X+1)(X^2-X+1) | 6 |
| [[2,1],[1,3]] | X^4+X^3+X^2+X+1 | 5 |
| [[3,1],[1,3]] | X^4+2X^3+2X^2+2X+1=(X^2+1)(X+1)^2 | infinite |

For the first four, the characteristic polynomial divides X^N-1 for the
listed N, so Cayley-Hamilton gives A_G^N=I. A characteristic root has exact
order N: respectively i, a nontrivial cube root, a root of X^2-X+1, and a
nontrivial fifth root. If A_G^d=I, that root must also satisfy lambda^d=1,
forcing N to divide d. Thus these are minimal orders over the whole real,
rational and integer carrier (matrix equality is detected on integer basis
vectors). This proves every time claim; testing d<N in code is only an audit.

## 2. Nontrivial parabolic block, not a failed return search

For the last G, in the order (z0,z1,M0,M1), set

    v=(1,1,-2,-2),       w=(0,0,1,1).

Then (A_G+I)v=0 and (A_G+I)w=v != 0. On their two-dimensional invariant span,
A_G=-I+N, N^2=0 and Nw=v. The binomial identity, including inverse powers,
gives for every integer n

    A_G^n w = (-1)^n (w-nv).

The independent integer vectors v,w force A_G^n w != w whenever n != 0.
This is an exact infinite-order certificate. It does not say every state is
aperiodic: v has period two. In fact H_G(v)=0 and H_G(w)=2; the latter orbit
contains infinitely many integer states on the same energy shell. A repeated
root alone would not give this conclusion, and it is explicitly not used as
such in this audit.

## 3. Energy, inverse and the raw complement

For any C the raw inverse first recovers M=M'+C^t E', then E=E'-CM.
Both triangular shears have determinant one and preserve integer states.
Put a=E+CM. Substitution gives

    Hraw(E,M)=|a|^2+|M|^2-a^t CM
             =Hraw(a,M-C^t a).

The completed square is

    4Hraw(E,M)=|2E+CM|^2+M^t(4I-G)M.

The G spectra in the five cases are respectively

    {2}, {3}, {1,3}, {(5-sqrt(5))/2,(5+sqrt(5))/2}, {2,4}.

Every G is positive definite. In the fourth case 0<sqrt(5)<3 proves both
positivity and largest eigenvalue below four without a numerical estimate.
Thus the first four raw forms are positive definite; the last is positive
semidefinite with nullity one. Necessity at the boundary follows by setting
E=-CM/2; sufficiency follows directly from the sum of squares. The active
embedding P=diag(C,I) is injective, gives T_C P=P A_G, and pulls twice the raw
energy matrix [[2I,C],[C^t,2I]] back to

    B_G=[[2G,G],[G,2I]].

Its last-case kernel is exactly the span of v above; all other active forms
are positive definite. The code obtains both energy matrices by polarization
of the scalar energy and audits the corresponding congruences and exact
Schur-complement inertias, rather than sampling state energies.

Since G is invertible, every real raw E decomposes uniquely as
E=C G^-1 C^t E+E_perp with C^t E_perp=0. The electric complement is pointwise
fixed and has dimension m-k, while the active component follows A_G.
The same decomposition exists over Q. Hence the raw characteristic
polynomial is (X-1)^(m-k) times the active polynomial, and raw and active
orders coincide. This does not assert an integral direct splitting of every
raw integer state; the canonical raw split has its own index-five boundary.

## 4. Incidence and orientation completeness within the frozen class

Use +tail/-head divergence D. The representatives, including distinct
parallel edges for digons, are exactly:

| Name | Ordered directed edges | Rows of C |
|---|---|---|
| digon | 01,01 | (1),(-1) |
| triangle | 01,12,20 | (1),(1),(1) |
| digon-digon | 01,01,01 | (1,1),(-1,0),(0,-1) |
| digon-triangle | 01,01,02,21 | (1,1),(-1,0),(0,-1),(0,-1) |
| triangle-triangle | 01,12,20,13,30 | (1,1),(1,0),(1,0),(0,1),(0,1) |

Each column is an actual closed oriented boundary walk: the digon traverses
one parallel edge forward and the other backward; the positive second face
in the mixed cell traverses 01 then the negatives of 21 and 02. The other
columns are the displayed triangle cycles or parallel-edge differences.
Thus DC=0, and column inner products give the five G. The raw shear preserves
DE since D(E+CM)=DE. These are finite unweighted CW cells; the digons are not
simple-graph triangles.

For arbitrary edge and face sign matrices R,S, set C'=RCS, D'=DR,
Qraw=diag(R,S), Qact=diag(S,S). Since R^2=S^2=I,

    D'C'=0,     G'=SGS,
    T_C'=Qraw T_C Qraw,    A_G'=Qact A_G Qact,
    P_C' Qact=Qraw P_C,
    Hraw_C'(Qraw y)=Hraw_C(y).

These are uniform symbolic identities for all states, so all orders, metric
inertias and characteristic polynomials persist. The finite orientation
regression covers every one of 2^(m+k) sign choices in each fixed
representative: 8+16+32+64+128=248. It does not assert that these five
representatives exhaust all two-face spaces. Flipping a single coefficient
while retaining D is not an admitted edge or whole-face reorientation; the
negative control detects the resulting nonzero DC.

## 5. Exact canonical marking

In the mixed cell take S=diag(1,-1), Q=diag(S,S). The canonical edges keep
exactly the order 01,01,02,21. Its faces are e0-e1 and -e0+e2+e3, giving

    C_can=C_positive S=[[1,-1],[-1,0],[0,1],[0,1]],
    A_f=Q A_positive Q,
    B_f=Q B_positive Q.

Canonical active coordinates (a,b,c,d) are (z0,z1,M0,M1), and its raw
embedding is P(a,b,c,d)=(a-b,-a,b,b,c,d). Therefore this is the exact
v102 field marking, not a changed field law or a coordinate permutation
applied while keeping an incompatible metric. The displayed canonical
matrices are checked entrywise by the independent verifier.

## 6. Attribution and limits

The general raw shear, energy boundary and inverse are already
FIELD-SHEAR-ENERGY-BOUNDARY in v102, including the two-triangle zero mode.
The triangle order-three law is already FIELD-EISENSTEIN-RESONANCE.
The selected canonical C, A_f, B_f and order-five certificate are already
Shared proofs 1 and 2 of FIELD-CONSERVATIVE-CHAIN-LAW. Those are inherited,
not new RC or author-C theorems. The bounded comparison table, its digon
cases, and the explicit Jordan/infinite-order certificate are the comparison
content to be evaluated. This is a bounded audit of admitted Canon sources,
not a claim of priority against every historical document.

No conclusion here chooses p=5, gives a native-U lift, supplies a physical
port or energy-selection mechanism, or classifies weighted complexes,
longer faces, additional shared edges or other field laws. Universal proof
and finite exact audits remain separate. Candidate evidence here changes
no Canon status; author comparison begins only after the pinned first run.
