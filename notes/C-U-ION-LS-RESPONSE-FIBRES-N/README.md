# Exact response fibres and nonlinear Hodge compatibility

**NON-CANONICAL; L1; candidate-T analytical classification.**
Date: 2026-10-05. This note decides the finite compatibility question for
arbitrary fixed functions of the six connected LS responses. It uses hand
algebra and a graph proof, not a new scientific execution. It constructs no
physically selected decoder, calibrated device, later native history or
physical time interpretation. Canon v97 and the physical HOLD are unchanged.

The result differs from the preceding affine obstruction: generically the
responses admit sixteen scalar degrees of freedom of nonlinear Hodge
readings. Other profiles, including profiles satisfying the earlier affine
nondegeneracy condition, force every such reading to zero. An exact graph
criterion covers any fixed profile once its response equalities are known.

## 1. Frozen observation and native domain

Use the six responses derived in [the connected-readout note](../C-U-ION-LS-CONNECTED-READOUT-N/README.md):

$$
z_k(X)=\frac{a_{M1}a_{R1,k}}{B},\qquad
a_j=d_j-d_0,\quad a_0=0,\quad
B=\sum_{i<j}(d_i-d_j)^2>0.
$$

The decoder receives only this six-vector. It receives no original level
labels, source label t, counter/time index, additional local populations,
history or other detector output. Equality of z does not assert equality
of the complete level-measurement records.

The domain is the same 25 preparations (s,t), with s,t in F5, at boundaries
n=1,2,3, passive archive M1=s, M2=1 and unchanged sources. Its only edges
are the fifty native transitions 1->2 and 2->3. No closing 3->1 edge is
added. The native branches and the first prepared family are [pinned in
#1371](https://github.com/mathorn1973/twist-j/blob/723fc7d8da6a3cb9b626da31bbea247d15666d41/probes/P-U-ION-NATIVE-COMPRESSION-1/PROOF.md#1-fixed-carrier-inputs-and-complete-target).
The additional two-step continuation is a partial mathematical target,
not a compiled ion program.

Write a=a1, b=a2, c=a3, d=a4 in the following table; d here is the fourth
centered scalar, not the whole profile. The table lists B*z, so the common
positive denominator does not affect equality of rows. It follows by direct
substitution into the native checkpoint tuples in the preceding note.

| s | n | B*z in the order (p1,p4,p1p,p4p,q,r) |
| --- | --- | --- |
| 0 | 1,2,3 | (0,0,0,0,0,0) |
| 1 | 1 | (0,0,0,0,ad,0) |
| 1 | 2 | (0,0,0,0,a^2,0) |
| 1 | 3 | (ab,a^2,ac,ad,0,a^2) |
| 2 | 1 | (b^2,ab,b^2,ab,bd,0) |
| 2 | 2 | (0,0,0,0,b^2,0) |
| 2 | 3 | (b^2,ab,bc,bd,0,ab) |
| 3 | 1 | (bc,ac,c^2,cd,c^2,ac) |
| 3 | 2 | (bc,ac,c^2,cd,bc,cd) |
| 3 | 3 | (0,0,0,0,cd,bc) |
| 4 | 1 | (bd,ad,cd,d^2,cd,ad) |
| 4 | 2 | (bd,ad,cd,d^2,bd,d^2) |
| 4 | 3 | (0,0,0,0,d^2,bd) |

The five t values repeat every row and edge. They do not provide extra
information to this decoder.

Let L be the fixed-direction four-dimensional Hodge restriction. In a
suitable basis it is

$$
L=\begin{pmatrix}
\phi&-1&0&0\\1&0&0&0\\0&0&3&-1\\0&0&1&0
\end{pmatrix},\qquad \phi=(1+\sqrt5)/2.
$$

Its eigenvalues are the two primitive tenth roots exp(+/-i*pi/5) and
lambda_+/-=(3+/-sqrt5)/2. In particular L is invertible, and L^q-I is
invertible for every nonzero integer q with |q|<=9. The source's
[fixed-direction Hodge scope](https://github.com/mathorn1973/twist-j/blob/82ecf0aac0ee79c947000968e71573d4c65d386d/canon/CANON.md#j-hodge-semilinear-memory-t)
is retained; no arbitrary-direction closure is asserted.

## 2. All nonlinear functions reduce to a finite graph

For the fixed profile, merge exactly equal response rows into vertices.
For every actual native transition X->FX, retain the edge [X]->[FX].
Parallel copies can be retained or deduplicated because their equations
are identical; self-loops and distinct outgoing edges must be retained.
There is no assumption of a single-valued induced update on these vertices.

Assign an unknown r_v in R^4 to each vertex. The entire condition for a
fixed function f of z is

$$
\boxed{r_v=Lr_u\quad\text{for every edge }u\longrightarrow v.}
$$

Necessity is immediate. Conversely, any solution defines f on the finite
response set, and that function can be extended to all of R^6. Thus this
test covers every fixed nonlinear decoder on the stated family. It supplies
no physical reason for choosing a particular solution.
All finite dimension counts below concern values on the observed response
set; functions on the whole R^6 have unrestricted extensions away from it.

## 3. Exact criterion for every fixed profile

Call a connected component of the underlying undirected graph
**height-consistent** if integers h_v can be assigned with

$$
h_v=h_u+1\quad\text{for every directed edge }u\to v.
$$

This terminology only describes the finite graph; h is not a physical
counter readout supplied to the decoder.

**Proposition.** If q is the number of height-consistent components, the
solution space of all vertex readings has dimension 4q. Every inconsistent
component has zero readings. The zero-response component is always
inconsistent. A nonzero axial reading exists exactly when q>0.

**Proof.** Choose a root and an undirected spanning tree in a component.
Invertibility of L gives along the tree

$$
r_v=L^{h_v}w,
$$

where tree heights increase or decrease according to the direction in
which an edge is traversed. Each remaining edge u->v imposes

$$
(L^{h_u+1-h_v}-I)w=0.
$$

If every exponent is zero, w is an arbitrary four-vector and all equations
hold. If an exponent is nonzero, its absolute value is at most the length
of the associated fundamental simple cycle. There are at most nine
distinct transition edges in this graph: one zero self-loop from s=0,
and at most eight edges from s=1,...,4. Hence this nonzero exponent has
absolute value at most nine. The spectral fact above forces w=0. This
also handles parallel edges, opposite edges and self-loops. In particular
the zero vertex has a length-one self-loop and kills its entire component.

For a consistent component, choosing w with nonzero axial part produces
nonzero axial values, since all powers of L are invertible. Different
components are independent. This proves the proposition.

The nine-edge bound is specific to this horizon and response family.
For a longer graph a signed cycle of length ten can preserve the periodic
plane while killing the axial pair, so the above dimension rule must not
be extrapolated unchanged.

A direct exact audit for a specified profile is consequently:

1. Evaluate the thirteen symbolic response rows and merge exact equals.
2. Insert all ten s-indexed transitions, keeping all distinct equations.
3. In each connected component propagate integer heights along a tree.
4. If any retained edge contradicts the height equation, set that whole
   component's readings to zero; otherwise retain one free four-vector.

This is a mathematical decision rule conditional on exact response
equalities. Uncertain measured values must not be merged by an arbitrary
floating-point tolerance and called an exact audit.

## 4. Generic compatibility and an explicit exact witness

As polynomials in a,b,c,d, the twelve nonzero-archive rows are nonzero and
pairwise different. Excluding the finitely many algebraic coincidence
sets therefore gives an open dense subset of R^4 with thirteen vertices:
the zero vertex and twelve distinct other vertices. This algebraic
genericity does not assert that a real apparatus can vary its four profile
differences independently.

The quotient graph in this class has the zero self-loop and four disjoint
two-edge paths. Consequently q=4 and the solution dimension is 16. Choose
arbitrary w_s in R^4 for s=1,...,4 and assign

$$
f(z(X_1^{(s)}))=w_s,\quad
f(z(X_2^{(s)}))=Lw_s,\quad
f(z(X_3^{(s)}))=L^2w_s,\quad f(0)=0.
$$

In particular one can choose distinct axial readings for s=3 and s=4,
or choose the four initial vectors to span R^4. This is finite algebraic
compatibility, not a selected Hodge measurement.

An exact profile-shape witness is a=(0,1,2,3,5), with B=74. Its twelve
nonzero response numerators are:

| s | n=1 | n=2 | n=3 |
| --- | --- | --- | --- |
| 1 | (0,0,0,0,5,0) | (0,0,0,0,1,0) | (2,1,3,5,0,1) |
| 2 | (4,2,4,2,10,0) | (0,0,0,0,4,0) | (4,2,6,10,0,2) |
| 3 | (6,3,9,15,9,3) | (6,3,9,15,6,15) | (0,0,0,0,15,6) |
| 4 | (10,5,15,25,15,5) | (10,5,15,25,10,25) | (0,0,0,0,25,10) |

Their distinctness is visible directly. This profile also satisfies
a1*a2*(a1-a2)!=0. Thus the previous affine no-go and the present nonlinear
compatibility hold on the same exact profile. The affine obstruction does
not extend to every fixed processing of the six responses.

For completeness, any assignment r_i at distinct response points p_i can
be realized by a polynomial, for example

$$
f(z)=\sum_i r_i\prod_{j\ne i}
\frac{\|z-p_j\|_2^2}{\|p_i-p_j\|_2^2}.
$$

This explicit interpolation is a methodological control. Its coefficients
encode the desired values. It is not proposed as the physical decoder.

## 5. Complete failure inside the same earlier nondegeneracy class

Take a=(0,1,-1,-1,1), with B=20. The earlier condition again holds:
a1*a2*(a1-a2)=-2. Now:

- The s=1 first and second responses coincide, at e_q/20. Their self-loop
  forces zero, and the last response is then zero as well.
- The s=2 middle response is the same e_q/20. Both its neighbors are
  forced zero, using invertibility of L for its incoming edge.
- The s=3 first and second responses coincide at
  (1,-1,1,-1,1,-1)/20. This self-loop kills its whole path.
- The s=4 first and second responses coincide at
  (-1,1,-1,1,-1,1)/20, again killing its whole path.
- The s=0 readings vanish by the zero self-loop.

Thus q=0 and every fixed f(z) satisfying the two-step law has zero values
on all seventy-five checkpoints. Unlike the positive example, this is an
obstruction in the response information itself on this horizon.

Neither rational profile is a claimed calibrated device or a prescription
for tuning optics. They prove that the earlier nondegeneracy condition
alone does not decide the nonlinear question. Geometry, admitted intensity
and an actual physical profile remain independent requirements.

## 6. The proposed two-step-return witness

The implication z(X3)=z(X1) => (L^2-I)f(z(X1))=0 is correct. Under the
earlier condition a1*a2*(a1-a2)!=0, however, the table shows no *nonzero*
same-history return of this kind:

- For s=1, the first coordinate is zero at n=1 and a1*a2/B!=0 at n=3.
- For s=2, the last coordinate is zero at n=1 and a1*a2/B!=0 at n=3.
- For s=3 or s=4, equality of the first coordinates forces respectively
  a3=0 or a4=0; its entire response history is then zero.

The always-zero s=0 history is already killed. The negative example in
section 5 uses one-step repeats, so absence of a nonzero two-step return
does not imply compatibility.

Outside that earlier condition, an exact literal example is
a=(0,0,1,1,0), B=6. For s=2 the first and third response are
(1,0,1,0,0,0)/6, while the middle response is e_q/6. The resulting two-cycle
forces zero because L^2-I is invertible. This is another algebraic witness,
not a physical calibration.

## 7. Normalization, continuity and the affine residual bound

The normalization identity

$$
B=5\sum_j(d_j-\bar d)^2,\qquad \bar d=\tfrac15\sum_jd_j
$$

and invariance of Z under d_j -> alpha*d_j+beta, alpha!=0, are exact.
They preserve this observation graph, not the entire force Hamiltonian,
motional excursion, local phases or apparatus intensity constraints.

The proposed continuity extension is valid **within the affine class**:
if d -> R_d(X) is continuous at a profile d_* with B(d_*)>0, all neighboring
admissible readings remain affine and satisfy the same exact two-step
intertwining equations, and admissible nondegenerate profiles approach d_*,
then R_(d_*)(X)=0
on each checkpoint. A symmetry-restricted family may supply no such
approaching profiles. Continuity of arbitrary nonlinear f_d alone does not
allow the affine theorem to be used.

For a fixed profile in the affine no-go class, let E map its 28 coefficients
to all 300 checkpoint components, and K map them to all 200 step residuals.
The theorem is ker(K) subset ker(E), so

$$
E=EK^+K,\qquad
\|K\theta\|_2\ge\eta\|E\theta\|_2,
\qquad \eta=\|EK^+\|_2^{-1}>0.
$$

Here E is not the zero map: a nonzero constant coefficient already has
nonzero checkpoint values. The bound is a relative residual bound for the
specified real embedding, coordinate basis, units and Euclidean stacking.
An absolute residual floor needs a separately fixed minimum output norm.
No numerical eta or universal experimental error floor is supplied.

For another parametrization, E=0 would make unit-signal normalization
infeasible, not justify division by zero. If ker(K) is not contained in
ker(E), exact nonzero signals exist and the corresponding residual infimum
is zero. The positive nonlinear example is therefore not governed by the
previous affine bound.

## 8. Interpretation and remaining task

The response-fibre audit separates two questions exactly. Some profiles
lose information required by the imposed finite dynamics; others retain
enough distinct response values for arbitrary nonlinear interpolation.
Neither case selects a physically justified decoder. In the generic class,
the next missing ingredient is a target-independent physical rule choosing
f, not another proof that a sufficiently flexible finite table can be fit.

The connection with invariant spaces of observables is consistent with
[Brunton et al., arXiv:1510.03007v2](https://arxiv.org/abs/1510.03007v2).
The present result is only a finite trajectory compatibility theorem. It
does not establish a Koopman-invariant subspace on an invariant physical
state domain or extend the two-step result to all times.

All conclusions above were obtained by symbolic table substitution and
graph reasoning. No verifier was executed, no new calibration or pulse word
was produced, and no GitHub or Canon status was changed. Independent static
review is recorded in [REVIEW.md](REVIEW.md).
