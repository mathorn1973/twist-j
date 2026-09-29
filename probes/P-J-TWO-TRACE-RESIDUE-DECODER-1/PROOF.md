# Two traces and a residue determine a bounded-norm scalar

Status: candidate-T. PUBLIC formal probe; NON-CANONICAL until a separate fold.
Author: A. M. Thorn. Action layer: L1. Issue: #1283.

Fresh reviewed successor to the immutable note in PR #1282. The decoder and
its thresholds are unchanged. Section 7 corrects an overbroad literal claim
about the number of native labels: arithmetic capacity K_m is capped by
3125 when counting usable native labels. REVIEW.md preserves that finding.

This is arithmetic, not a construction of a physical detector. All statements
refer to exact integers; finite verification audits, rather than replaces,
the proofs. No numerical embedding or logarithm is used by the inverse.

## 1. Carrier and observables

Let O=Z[zeta], 1+zeta+zeta^2+zeta^3+zeta^4=0, J=1+zeta^2 and
phi=-zeta^2-zeta^3. The two complex embeddings send zeta to zeta and zeta^2.
For nonzero alpha in O write

$$
\alpha\overline\alpha=u+v\varphi,\quad
A=|\sigma_1\alpha|^2=u+v\varphi,\quad
B=|\sigma_2\alpha|^2=u+v-v\varphi.
$$

Both A and B are positive, and N(alpha)=AB=u^2+uv-v^2 is a positive integer.
Define S(alpha)=A+B=Tr(alpha*bar(alpha))/2 and
S0=S(alpha), S1=S(J alpha). This is a stipulated pure J step, not an
arbitrary pair of consecutive source-driven states.

For alpha=a+b*zeta+c*zeta^2+d*zeta^3, direct multiplication gives

$$
 u=a^2-ab+b^2-bc+c^2-cd+d^2,\qquad
 v=ab-ac-ad+bc-bd+cd.
$$

Multiplication and its inverse in this coefficient basis are

$$
 J(a,b,c,d)=(a-c+d,b-c,a,b-c+d),
$$
$$
 J^{-1}(a,b,c,d)=(c,-a+c+d,-a-b+c+d,-b+d).
$$

These formulas follow from the cyclotomic relation and J^{-1}=-zeta-zeta^2.

## 2. Two-trace reconstruction and its exact recurrence

Since J*bar(J)=2-phi, multiplication of u+v*phi by 2-phi sends
(u,v) to (2u-v,v-u). Therefore

$$
 \boxed{S_0=2u+v,\quad S_1=3u-v,\quad
 u=\frac{S_0+S_1}{5},\quad v=\frac{3S_0-2S_1}{5}.}
$$

The integer matrix [[2,1],[3,-1]] has determinant -5. Its image in Z^2 is
exactly {S0+S1=0 mod5}: this congruence makes both displayed inverse
coordinates integral. It does NOT by itself imply that the pair is realized
as alpha*bar(alpha).

Solving instead for A and B gives

$$
 A=\frac{\varphi^2S_0-S_1}{\sqrt5},\qquad
 B=\frac{S_1-\varphi^{-2}S_0}{\sqrt5}.
$$

In particular the two-trace pair determines the ordered magnitudes, not just
their unordered set. The norm is

$$
 \boxed{N(\alpha)=\frac{3S_0S_1-S_0^2-S_1^2}{5}.}
$$

For S_n=S(J^n alpha), valid also at negative integer n,

$$
 \boxed{S_{n+2}=3S_{n+1}-S_n.}
$$

Indeed its two exponential roots are phi^{-2} and phi^2, whose sum is 3
and product is 1. Equivalently substitution of the preceding integer
(u,v) update proves the same identity. The forward pair map is
(S0,S1)->(S1,3S1-S0), and the inverse is (S0,S1)->(3S0-S1,S0).
Thus further pure-step traces contain no information beyond the first two.

## 3. A uniform trace-residue injectivity criterion

For integers X>=1, m>=1, define

$$
 D_m(\alpha)=(S(\alpha),S(J\alpha),\alpha\bmod mO),\qquad
 0<N(\alpha)\le X.
$$

If m^4>16X, this reader is injective. To prove this, suppose D_m(alpha)
=D_m(beta). Section 2 gives the same A and B for alpha and beta. For
nonzero gamma=alpha-beta, the triangle inequality gives

$$
 |\sigma_1\gamma|\le2\sqrt A,\quad
 |\sigma_2\gamma|\le2\sqrt B,\quad N(\gamma)\le16AB\le16X.
$$

But the equal residues give gamma=m*eta for a nonzero eta in O. Hence
N(gamma)=m^4*N(eta)>=m^4, a contradiction. The integrality used here can
also be read as the determinant of multiplication by eta on the free
Z-module O. No probabilistic separation hypothesis is used.

For X=941, m=25 the exact comparison is

$$
 16\cdot941=15056<390625=25^4.
$$

This proves sufficiency, NOT minimality of the modulus. The complete map
is not a finite-state encoding: its first two entries are unbounded integers.

## 4. Integer strip normalization

The public J-unit strip is 1<=A/B<phi^4. In (u,v) coordinates it is
v>=0 and u-v>0, equivalently

$$
 \boxed{2S_0<3S_1,\qquad 2S_1\le3S_0.}
$$

Let alpha=J^k beta with beta in this half-open strip. An exact algorithm starts
with k=0 and the observed residue r. If v<0, replace the pair by
(3S0-S1,S0), r by J^{-1}r, and k by k+1. If u-v<=0, replace the pair by
(S1,3S1-S0), r by Jr, and k by k-1. Stop when both strip inequalities hold.

For any surviving input pair, even before scalar representability is known,
A and B are positive: their sum S0 and product N are positive. Thus the ratio
r=A/B is positive. The two failure cases are respectively r<1 and r>=phi^4;
they cannot hold simultaneously. Repeated multiplication in the first case
first crosses 1 at a value below phi^4; repeated division in the second case
first falls below phi^4 at a value at least 1. Hence there is no oscillation.
Each step
moves A/B by exactly phi^4 or phi^{-4}, respectively. The half-open intervals
[phi^{4j},phi^{4j+4}) partition the positive line, so the algorithm terminates
at unique normalized data. For representable data those are the data of the
unique strip representative beta; for other inputs beta need not exist and
the image check in section 6 must still reject them. The algorithm is
integer-only; its termination proof does not require evaluating a logarithm.
For representable data the returned k satisfies alpha=J^k beta.

The boundary A/B=1 is included; A/B=phi^4 is excluded and is moved by one J
step. These distinct inequalities must not be made symmetric.

## 5. A small coefficient box at norm 941

For beta in the strip put x=sqrt(A/B), so 1<=x<phi^2. Then

$$
 S(\beta)=\sqrt{N(\beta)}(x+x^{-1})<3\sqrt{N(\beta)}.
$$

Here x+x^{-1} is increasing for x>=1 and phi^2+phi^{-2}=3. Thus N<=941
implies S<93, since 9*941<93^2, and the integer S satisfies S<=92.
For beta=sum_i c_i*zeta^i, i=0,...,3, let G=5I-11^T. The trace identity is

$$
 2S(\beta)=c^TGc=5\sum_i c_i^2-\left(\sum_i c_i\right)^2,
 \qquad G^{-1}=\frac{I+11^T}{5}.
$$

Cauchy-Schwarz in this positive definite form gives

$$
 c_i^2\le (G^{-1})_{ii}\,c^TGc=\frac45S(\beta)
 \le\frac{368}{5}<81.
$$

Consequently every normalized coefficient is in [-8,8]. Coefficientwise
reduction modulo 25 is therefore injective on this box. These are four
coordinates over Z/25Z, not four elements of a field with 25 elements.

## 6. Direct inverse and total image recognition

The inverse takes two integers S0,S1 and four canonical residues in 0,...,24.
Reject nonpositive S0 or S1, nonintegral inverse (u,v), and N outside [1,941].
For the surviving pairs A and B are positive: their sum is S0>0 and their
product is N>0. Perform section 4 on the pair and residue. Center each final
residue in [-12,12], reject any coefficient outside [-8,8], and call the
result beta. Finally require that its recomputed two traces equal the
normalized pair. If they do, return alpha=J^k beta; otherwise reject.

Completeness: every domain element reaches its unique beta in [-8,8]^4,
whose four coefficients are exactly the centered residues. It passes every
check and reconstructs exactly.
Soundness: every accepted beta is integral, has the checked positive norm
and traces, and the prescribed residue. Applying J^k preserves the norm and
reverses both transformations of the data. Hence the output realizes exactly
the input reading. Uniqueness follows from section 3.
This is a terminating recognizer of the exact image, not merely an inverse
promised to work when an unverified input happens to be valid.

There is no general corruption-detection theorem. For example replacing the
residue of 1 by that of zeta while retaining (S0,S1)=(2,3) changes one valid
reading into another valid reading. Both must be accepted.

## 7. What modulo five can and cannot do

The distinct scalars 5 and 5*zeta both have N=625 and (S0,S1)=(50,75), and
both reduce to zero in O/5O. Thus D_5 is not injective on the full N<=941
domain. The recurrence implies that supplying MORE pure J traces cannot
repair this collision. It is separated by D_25.

That single collision does not decide whether a carefully chosen 3125-label
codebook could still use D_5 at bound 941. For this let B_X be the COMPLETE
oriented strip of norm at most X and define

$$
 K_m(X)=|\{D_m(\beta):\beta\in B_X\}|.
$$

Under the public reader classification R(n,x)=J^n G(ell_n(x)), arbitrary
nonzero integral G with 1<=N(G(label))<=X and global injectivity across all
reachable sheets n>=3,
the arithmetic codebook capacity is K_m(X). The usable subset of the native
3125-label alphabet has maximum size min(3125,K_m(X)); all native labels can
be distinguished exactly when K_m(X)>=3125.

The native premise is explicit: P-U-COUNTER-AMPLITUDE-CLASS-1/PROOF.md
section 3 proves ell_n=Lambda_n:X_n->F5^5 bijective for EVERY n>=3,
and section 4 proves the displayed reader classification. Every label is
therefore available at every sheet used in the collision argument.

The observed datum is D_m(alpha) alone. The sheet number n is not separately
supplied. Equality compares different sheets as well as different labels.
The different interface (n,D_m(alpha)) and fixed-time injectivity are outside
this assertion. With n supplied, distinct unit offsets G(label)=J^a_label
can be separated at norm one, so the omitted-time condition is essential.

For attainment, choose one beta per distinct key and put each selected G in
the strip. If two data readings agree, their trace normalization gives the
same exponent n and the same strip key, hence the same label.
For the upper bound, normalize any proposed G(label)=J^{a_label} beta_label.
If two labels have the same strip key, choose t>=max(a_label,a_other)+3 and take
n1=t-a_label, n2=t-a_other, both at least 3. Their complete D_m readings then
agree. These sheets exist by the all-sheet bijectivity just cited.
A label sent to zero cannot belong
to the nonzero globally injective reader class.

Therefore the full finite census of B_941 answers the codebook question for
this observed-reader class, even if unnormalized generators are admitted.
It also locates the first D_5 collision within N<=941: equal data normalize
by the SAME number of J steps and preserve congruence because J is a unit.
This reduction is independent of the census answers. The predecessor census
answers are disclosed before this new formal pin and are audit targets, not
new blind discoveries.

For m=25, the theorem already gives K_25(941)=|B_941|=3150, so a 3125-label
codebook is possible, but its physical selection is not supplied.

## 8. Scope limits

The two traces must be available as exact data. Their physical realization,
noise tolerance, conservation during measurement and measurement resources
are not established. The pure-step recurrence is not valid unmodified after
alpha->J alpha+d. Nor does a finite-state residue reader itself store the
unbounded step count. A codebook is an explicit mathematical choice, not a
preferred physical dictionary or a reconstruction of lost native head data.
No original open Canon owner is closed by this note. In particular it proves
no Born occurrence law, apparatus completion, native source-language
completeness, SI scale, physical time, entropy transport, photon or RH result.
