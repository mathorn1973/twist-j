# The fixed receiver excludes every full four-coordinate linear subquotient

**C-HODGE-BOUNDARY-CURRENT-N. NON-CANONICAL. L1.**

**Supplemental pre-execution analytical strengthening.** This argument was
written before either scientific program was run. It supplements the fixed
source factorization proved in PROOF_CURRENT.md; it does not change the bytes
or claims of that proof or of PROOF_METRIC.md. No computation is reported here.
The originally declared acceptance fixtures are unchanged.

The result concerns one fixed receiver-label involution and products retaining
that same factorization. It strengthens the directional-marginal conclusion
to arbitrary linear invariant subquotients of the complete joint Hermitian
carrier. It is not a no-go theorem for the full capture law, for arbitrary
label operations, or for all multichannel boundary readings.

## 1. Source, fixed class, and statement

The source is

<https://github.com/mathorn1973/twistj-handoff/blob/0b9bf39b3a5866fdb34c6f37711462dc8dd08ab8/homogeneous-capture-2026-10-22/proofs/homogeneous_source.md>.

Its equations (3) and (6) give the pulse step with its unchanged identity
factor on all 26 pulse labels. Equations (43)--(46) give the same involutive
exchange of every pair of encoded pulse and receiver labels. Sections 9--10
give zero free receiver energy, the occupied-code scope, and preservation of
the old memory label in the outgoing pulse. The accompanying static review is

<https://github.com/mathorn1973/twistj-handoff/blob/0b9bf39b3a5866fdb34c6f37711462dc8dd08ab8/homogeneous-capture-2026-10-22/proofs/native_completion_static_review.md>.

In PROOF_CURRENT.md, equations (15), (17), and (21) derive the actual spatial
transfer of the full pulse and its one receiver:

~~~
A(lambda)^dagger Sigma A(lambda) = Sigma,
Sigma = diag(1,-1),
T_receiver = A(lambda) tensor J,
J^dagger = J,       J^2 = I.
~~~

Here J exchanges the complete 26-by-26 encoded label factor; it is not an
eigenlabel preparation or a projection onto empty memory.

We prove a statement for the following explicitly fixed larger class. Let L
be a finite-dimensional label Hilbert space, let J be one fixed unitary
involution on L, and let

~~~
T = A tensor J^n,
A in U(1,1) = {A : A^dagger Sigma A = Sigma},
n an integer.
~~~

Any finite product of factors A_j tensor J^(n_j), with each A_j in U(1,1),
has this form: its directional factor is the ordered product of the A_j and
its label exponent is the sum of the n_j. This includes repeated passages
through the same declared receiver and scalar directional words. A finite
spectator identity factor can be included by replacing J with J tensor I.

On the complete real vector space

~~~
W = Herm(C^2 tensor L),
R_T(X) = T X T^dagger,
~~~

consider any invariant real subspaces W0 contained in W1 contained in W.
The induced action on W1/W0 cannot be isomorphic to the full marked Hodge
action L_J with characteristic polynomial

~~~
chi_LJ(z) = (z^2-3z+1)(z^2-phi*z+1),
phi = (1+sqrt(5))/2.
~~~

Equivalently, for no invariant W1 is there a surjective real-linear reading
r: W1 -> E_J satisfying r R_T = L_J r. This includes readings of arbitrary
joint directional and label coherences, not just the directional marginal.

## 2. Complexification includes the entire joint carrier

The complexification of Herm(V), regarded as a real vector space, is End(V).
Under this identification the complexified congruence still sends

~~~
X -> T X T^dagger.
~~~

Column vectorization gives the matrix bar(T) tensor T. Permuting the tensor
factors therefore gives a similar matrix

~~~
(bar(A) tensor A) tensor (bar(J^n) tensor J^n).
~~~

This acts on the complete complexified matrix space. It does not restrict X
to product matrices or to uncorrelated states. In real terms, Herm(C^2)
tensor_R Herm(L) spans the complete Herm(C^2 tensor L).

Because J is a unitary involution, it is diagonalizable with eigenvalues
contained in {1,-1}. The eigenvalues of its congruence factor are consequently
contained in {1,-1}, for every integer n. If n is even only +1 occurs.
If n is odd, the actual multiplicities depend on the two eigenspace
dimensions of J; no claim that both signs must occur is needed.

## 3. Directional spectral dichotomy, including repeated roots

For A in U(1,1), its determinant has modulus one. Choose a scalar eta of
modulus one with eta^2=det(A), and set A0=eta^-1 A. Congruence is unchanged,
and A0 is in SU(1,1). Comparing its determinant-one inverse with
Sigma A0^dagger Sigma gives

~~~
A0 = [[alpha, gamma],
      [bar(gamma), bar(alpha)]].
~~~

Hence t=tr(A0) is real, and the eigenvalues of A0 are r,r^-1, the roots of
z^2-t*z+1. Its characteristic polynomial is real, so bar(A0) has the same
multiset of eigenvalues. Triangularizing the two factors over C shows that
bar(A0) tensor A0 has eigenvalues, with algebraic multiplicities,

~~~
1, 1, r^2, r^-2.
~~~

Triangularization does not require diagonalizability. This argument therefore
includes all repeated-root and parabolic cases.

There are only the following possibilities:

1. If t^2>4, both roots r,r^-1 are real and nonzero. All four congruence
   eigenvalues are positive real numbers.
2. If t^2<4, the roots are complex conjugates with product one, so |r|=1.
   All four congruence eigenvalues have modulus one.
3. If t^2=4, both roots are +1 or both are -1. Every congruence eigenvalue is
   +1, although Jordan blocks may be present.

Multiplication by the label congruence eigenvalues in {1,-1} proves the
needed dichotomy for the full joint action:

~~~
spec(R_T complexified) is entirely real,
or spec(R_T complexified) is entirely of modulus one.
~~~

The alternatives can overlap. No assertion about diagonalizability of R_T
is part of this statement.

## 4. Invariant subquotients cannot acquire the missing factor

The marked target has the four distinct eigenvalues

~~~
phi^2, phi^-2, zeta_10, zeta_10^-1.
~~~

The first pair is positive real with modulus different from one. The second
pair is nonreal and has modulus one. Its spectrum is therefore neither
entirely real nor entirely of modulus one.

For an invariant chain W0 contained in W1 contained in W, choose a complex
basis adapted to its complexification. The matrix of R_T is block triangular,
with the matrix induced on W1/W0 as one diagonal block. Its characteristic
polynomial is a product of the diagonal-block characteristic polynomials.
Thus every eigenvalue of the induced subquotient is an eigenvalue of the
ambient action. This remains true in the presence of Jordan blocks.

The spectral dichotomy of section 3 consequently excludes L_J on every
four-dimensional invariant subquotient. For a surjective intertwining reading
r: W1 -> E_J, its kernel is invariant and W1/ker(r) is isomorphic to E_J;
the same conclusion follows. The argument does not require the reading to
be a marginal, a tensor product, positive, or an isometry.

A non-surjective reading could retain only part of the target carrier, such
as its boost plane. The conclusion concerns a reading onto the full
four-dimensional target and does not rule out every nonzero intertwiner.

## 5. Physical meaning and precise boundary

The unchanged receiver exchange supplies only a sign to joint label
coherences. It cannot supply the independent tenth-root rotation while the
same directional transfer supplies the nontrivial boost. Selecting a more
general linear reading of the occupied memory does not repair that missing
spectral factor.

The calculation includes all encoded label states, arbitrary superpositions,
and entanglement with the direction or finite identity spectators. It does
not require initially empty memory, discard the old label, or project onto
an eigenlabel. An invariant preparation subspace is already included in W1.

The following extensions are outside this lemma:

1. Products of distinct receiver involutions J_i need not reduce to powers
   of one fixed J. Their product can have label phases other than signs.
   Arbitrary retained label unitaries are likewise outside the stated class.
2. An interferometric network whose internal elimination sums paths with
   different label histories need not factor as A tensor J^n. A product-word
   argument alone does not establish that factorization for such a network.
3. The full capture contact introduces object, token, and pulse arrangement
   channels. The lemma does not classify its complete scattering transfer or
   exclude a suitable reading of those additional coherent channels.
4. Different input and output context identifications are not an invariant
   subquotient of one fixed endomorphism. The covariant-current analysis in
   PROOF_CURRENT.md remains the appropriate separate test.
5. Nonlinear, state-dependent, or postselected readings are not the linear
   surjective intertwining maps classified here.

This is a strict strengthening for the fixed-source A tensor J^n class.
The general higher-channel allowance in PROOF_CURRENT.md remains valid:
additional independently derived coherent phases can change the spectrum.
No source derivation of those phases, no metric or lattice identification,
and no original-U realization follows from this supplementary obstruction.
