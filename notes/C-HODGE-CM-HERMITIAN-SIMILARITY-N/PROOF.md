# Exact CM Hermitian similarity of the marked predictive carrier

**PUBLIC / NON-CANONICAL / candidate-T analytical note. L1 only.**
Owner: A. M. Thorn / hodge-cm-hermitian-similarity-20260927, issue #1228.
No Canon authority or public status promotion.

## 1. Inherited premises and notation

All source references in this note are read at public main
5daf8df697dc480227d7db5fe2c678f48c14040d, with Public Canon v92 unchanged.
The premises are the marked construction and the claims
J-HODGE-PREDICTIVE-CLOSURE [T] and J-HODGE-HERM2-LOXODROME [T] in
[canon/CANON.md](../../canon/CANON.md), together with the exact Gram
certificate of the original
[P-J-HODGE-HERM2-LOXODROME-1 preregistration](../../probes/P-J-HODGE-HERM2-LOXODROME-1/PREREG.md)
and its accepted
[exact audit](../../probes/P-J-HODGE-HERM2-LOXODROME-1/verify.py).
That audit is a cited existing source; it is not executed by this note.

Let V=A4 tensor Q, with its marked root basis, Gram H=I+11^t, orientation
and coordinate five-cycle C. Put

    W=Lambda^2 V,    L=Lambda^2(I+C^2),    Q_W=Lambda^2 C.

The wedge pairing on W is beta. Write K_H for the source Hodge operator
called K in the Canon, reserving K below for a number field. Over
F=Q(sqrt(5)), let

    P_+=(I+K_H/sqrt(5))/2,    P_-=(I-K_H/sqrt(5))/2,
    E=E_+=im(P_+) + im(P_- L P_+),
    g=beta|E,                A=L|E.

The inherited statements give dimension four, A-invariance,
nondegeneracy and preservation of g, and

\[
\operatorname{char}_A(X)
=(X^2-3X+1)(X^2-\varphi X+1),
\qquad \varphi=(1+\sqrt5)/2.
\tag{1}
\]

The audited F-basis has Gram matrix

\[
\frac{\sqrt5}{10}
\begin{pmatrix}3&1&1\\1&3&1\\1&1&3\end{pmatrix}
\ \oplus\ \left[-\frac{2+\sqrt5}{8}\right].
\tag{2}
\]

The 3-by-3 block and the orthogonal fourth entry in (2) are asserted
exactly in the cited audit, not inferred from approximate eigenvalues.

Set j=exp(2*pi*i/5), K=Q(j), lambda=-j^3 and J=1+j^2. Then

\[
K=F(\lambda),\quad \lambda+\bar\lambda=\varphi,\quad
\lambda\bar\lambda=1,\quad \lambda^5=-1,\quad
-J^{-2}=\varphi^2\lambda.
\tag{3}
\]

The bar is CM conjugation, fixing F. In particular, lambda has polynomial
X^2-phi X+1, irreducible over F: its discriminant phi-3 is negative
in the chosen real embedding.

## 2. The three source blocks and the five-cycle

Equation (1), with its pairwise coprime factors, gives

\[
E=H_+\oplus H_-\oplus P,\qquad
H_\pm=\ker(A-\varphi^{\pm2}I),\quad
P=\ker(A^2-\varphi A+I),
\tag{4}
\]

of dimensions 1,1,2 over F. Here P denotes the compact primary plane,
not either Hodge projector P_+ or P_-.

The five-cycle C preserves H and the marked orientation. Thus Q_W
preserves beta, commutes with K_H and L, and preserves E. Let Q=Q_W|E.
Its block actions are

\[
Q|H_+=Q|H_-=I,\qquad Q|P=-A|P.
\tag{5}
\]

Here is a direct derivation of (5). Over K the eigenvalues of C on V
are j^a, a=1,2,3,4. On an exterior eigenpair (a,b), Q_W acts by
j^(a+b) and L acts by (1+j^(2a))(1+j^(2b)). For b=-a the Q_W
eigenvalue is one, and the two L values are phi^2 and phi^-2.
For distinct a,b with b!=-a, the residue b/a is 2 or 3. The five
exponents

    0, 2a, 2b, 2(a+b), a+b

then run through all residues modulo five. Their fifth-root sum vanishes,
so the L value is -j^(a+b). This proves L=-Q_W on the other four
exterior factors and hence (5) on P. No new spectral census is used.

Choose h_+!=0 in H_+, h_-!=0 in H_- and write b=g(h_+,h_-).
A-invariance of g and the distinct reciprocal spectral factors imply

\[
g(h_+,h_+)=g(h_-,h_-)=0,\qquad
H_\pm\perp_g P,\qquad b\ne0.
\tag{6}
\]

For example, a cross functional g(h_+,.) on P would be a left
eigenvector of A|P with eigenvalue phi^-2, which is not a root of its
irreducible quadratic. It therefore vanishes. Nondegeneracy then forces
b!=0 and nondegeneracy on P. The hyperbolic block in (6) has signature
(1,1) at either real place.

## 3. The compact plane as a scaled CM norm

Give P its K-module structure by letting lambda act as A|P. Since the
quadratic in (1) is irreducible, every nonzero p in P is a K-basis.
Fix such a p, and define

\[
c_p=g(p,p).
\]

At the chosen real place (2) has signature (3,1), so (6) makes P
positive definite. Consequently c_p!=0 for every such p.

Preservation of g says that the g-adjoint of A|P is its inverse.
It follows by F-linearity that multiplication by x in K has adjoint
multiplication by bar(x). Also A+A^-1=phi I on P, so

\[
2g(p,Ap)=\varphi c_p.
\]

Writing an arbitrary element of K as a+b lambda proves
g(p,zp)=c_p Tr_(K/F)(z)/2. Therefore

\[
\boxed{g(xp,yp)=c_p\frac{x\bar y+\bar x y}{2}},\qquad
\boxed{g(xp,xp)=c_pN_{K/F}(x)}.
\tag{7}
\]

Combining (6) and (7), every w=uh_++vh_-+xp satisfies

\[
g(w,w)=2buv+c_pN_{K/F}(x).
\tag{8}
\]

Changing the auxiliary K-basis to p'=eta p changes c_p to
c_p N_(K/F)(eta). Thus the coset

\[
[c_p]\in F^*/N_{K/F}(K^*)
\tag{9}
\]

is independent of p. The choices h_+,h_- do not enter this coset.

## 4. Fixed Hermitian target and a constructive map

Let mathcal H=Herm_2(K/F), an F-vector space of dimension four. Write

\[
X=\begin{pmatrix}u&z\\\bar z&v\end{pmatrix},\qquad
q(X)=-\det X=N_{K/F}(z)-uv.
\]

The bilinear form associated with q is its polarization over F.
No new orientation or time orientation is selected.

Put a_H=-J^-2=phi^2 lambda and define the two F-linear target actions

\[
R_A(X)=\varphi^{-2}GXG^\dagger,\quad G=\operatorname{diag}(a_H,1),
\qquad
R_Q(X)=DXD^\dagger,\quad D=\operatorname{diag}(-\lambda,1).
\tag{10}
\]

Since N(a_H)=phi^4, they preserve q. More explicitly,

\[
R_A:(u,v,z)\mapsto(\varphi^2u,\varphi^{-2}v,\lambda z),
\qquad
R_Q:(u,v,z)\mapsto(u,v,-\lambda z).
\tag{11}
\]

In particular R_Q has order five. Its phase is -lambda, not lambda;
this is the sign required by the inherited action (5).

Define

\[
\boxed{
M_p(uh_++vh_-+xp)=
\begin{pmatrix}u&x\\\bar x&-2bv/c_p\end{pmatrix}.}
\tag{12}
\]

It is an F-linear bijection. Equations (8) and (11) give, by direct
substitution,

\[
\boxed{g(w,w)=c_p q(M_pw)},\qquad
\boxed{M_pA=R_AM_p,\qquad M_pQ=R_QM_p.}
\tag{13}
\]

Polarization proves the corresponding bilinear identity. Thus (12)
constructs an exact similarity intertwining the full fixed actions,
rather than merely matching their characteristic factors.

## 5. Complete map and scale classification

Fix c in F^*. Consider every F-linear bijection M:E->mathcal H with
M A=R_A M, M Q=R_Q M and g(w,w)=c q(Mw).

The distinct primary factors force an A-intertwiner to map H_+,H_-
to the corresponding diagonal target lines and P to the offdiagonal
plane. On the last block it must be K-linear. Consequently every
bijective A-intertwiner has precisely the form

\[
M(uh_++vh_-+xp)=
\begin{pmatrix}
\alpha u&\xi x\\\bar\xi\bar x&\beta v
\end{pmatrix},\qquad
\alpha,\beta\in F^*,\quad\xi\in K^*.
\tag{14}
\]

Conversely every map in (14) intertwines A and, by (5) and (11), Q.
Although x->bar(x) is F-linear, it conjugates lambda to bar(lambda).
Since lambda!=bar(lambda), it does not intertwine the fixed target
action. Hence there is no omitted conjugate-linear compact branch.

Comparing the two quadratic forms in (8) and (14) gives exactly

\[
-c\alpha\beta=2b,\qquad cN_{K/F}(\xi)=c_p.
\tag{15}
\]

These are necessary and sufficient conditions. It follows that

\[
\boxed{\{c\in F^*: \text{an admitted map exists}\}
=c_pN_{K/F}(K^*).}
\tag{16}
\]

Indeed, for an admissible c choose any xi with N(xi)=c_p/c, choose
any alpha in F^*, and set beta=-2b/(c alpha). Norms form a subgroup,
so using c_p/c or c/c_p gives the same coset condition.

Let K^1=ker(N_(K/F):K^*->F^*). The full group of g-isometries of E
commuting with A and Q is

\[
U_{t,\eta}:
h_+\mapsto th_+,\quad h_-\mapsto t^{-1}h_-,\quad
xp\mapsto\eta xp,
\qquad(t,\eta)\in F^*\times K^1.
\tag{17}
\]

Completeness follows from the same primary-block argument as (14);
metric preservation fixes the hyperbolic scale product and the compact
norm to one. For any fixed admissible c, precomposition by (17) acts
freely and transitively on its map family: for two sets of parameters
in (14), take t=alpha_2/alpha_1 and eta=xi_2/xi_1. Equation (15)
gives N(eta)=1 and the required relation for beta. Thus

\[
\boxed{\text{the fixed-scale map family is a torsor under }F^*\times K^1.}
\tag{18}
\]

The displayed equations do not select one map. This statement does not
classify selections that impose additional data from outside this frozen
class, and it does not identify different maps by a physical equivalence.

## 6. The scale has opposite signs at the two real places

Let sigma be the nontrivial automorphism of F. The 3-by-3 integer matrix
in (2) is 2I+11^t and is positive definite over R. At the chosen place,
(2) has signature (3,1). Under sigma its 3-by-3 block becomes negative
definite and its fourth entry becomes -(2-sqrt(5))/8>0. Thus the conjugate
signature is (1,3).

The hyperbolic block (6) remains nondegenerate with signature (1,1).
Therefore P is positive definite at the chosen place and negative
definite at its conjugate. In particular,

\[
c_p>0,\qquad\sigma(c_p)<0.
\tag{19}
\]

Every nonzero CM norm is positive at both real places: applying either
embedding to N(x)=x bar(x) gives the squared complex absolute value of
the corresponding embedding of x. Equations (16) and (19) therefore
show that every admissible c has signs (+,-). In particular,

\[
\boxed{c=1\text{ admits no map in the frozen class}.}
\tag{20}
\]

Equivalently, the unscaled target q=-det has signature (3,1) at both
real places, whereas the inherited g does not. This does not contradict
the constructive scaled map (12). The sign condition is necessary, not
a claim that every scalar with those signs belongs to the norm coset.

## 7. Galois covariance changes the chart and the target actions

Choose tau:K->K with tau(j)=j^2; its restriction to F is sigma and it
commutes with CM conjugation. The source matrices L, Q_W, beta and K_H
are rational, while sigma exchanges the two Hodge projectors. Therefore
the coefficientwise transport takes E_+ to

    E_-=im(P_-) + im(P_+ L P_-).

It transports g,A,Q to their restrictions on that conjugate chart.
On the target it conjugates the coefficients a_H, phi and lambda in
(10), giving R_A^tau and R_Q^tau. Applying tau to any map in (14)
and to its source and target coordinates, with w'=tau(w), gives

\[
\tau(Mw)=M^\tau(\tau w),\qquad
g^\tau(w',w')=\tau(c)q(M^\tau w'),
\]

\[
M^\tau A^\tau=R_A^\tau M^\tau,\qquad
M^\tau Q^\tau=R_Q^\tau M^\tau.
\tag{21}
\]

The norm commutes with tau, so the scale coset is transported to
tau(c_p) N_(K/F)(K^*). Equation (21) is covariance of the whole
construction, with the primitive-J embedding and target actions
conjugated. It is not invariance inside one fixed E_+ with its target
action held unchanged. This transport must also not be confused with
the excluded conjugate-linear block in section 5.

## 8. Scope

The result is a classification of F-linear similarities and fixed
algebraic actions at L1. It adds explicit maps, their scale coset and
their remaining freedom to the inherited factor comparison. It chooses
no canonical map, physical chart, integral lattice, physical scale or
time update, and supplies no native-U intertwiner, photon or cone
comparison, P1 bound, decoder, apparatus, or L2-L6 lift.
