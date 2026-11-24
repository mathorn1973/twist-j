# Two-cut defects, harmonic overlap, and the scalar energy

**NON-CANONICAL. Authority none. Action layer NOT_APPLICABLE.**
The finite identities, examples and readout costs are **candidate-D**.
The positive whole-window bound is **O**. Paper scope [round 2](SCOPE.md).

Use the fixed ambient signed cube, parity \(\Gamma\), odd symmetric
operator \(A=\sum_i c_i\gamma_i\), and \(s=\sum_i c_i^2>0\)
of [the boundary note](../BOUNDARY.md). All cutoffs in a comparison
use the same ambient prime list, weights and signs. Extend compressed
operators by zero. Write \(P_x\) for a coordinate cutoff,
\(D_x=P_xAP_x\), \(B_x=P_xA(1-P_x)AP_x\), and
\(I_x=\operatorname{tr}(\Gamma P_x)\). In particular,
\(D_x^2=sP_x-B_x\) and \(\operatorname{str}B_x^j=s^jI_x\)
for positive integers \(j\).

## 1. Mixed defects and the four-step terms

If \(P_x\le P_y\), put \(W_{x,y}=P_xA(P_y-P_x)AP_x\). Then
\[
 P_xB_yP_x=B_x-W_{x,y},\qquad
 \operatorname{str}(B_xB_y)=s^2 I_x-\operatorname{str}(B_x W_{x,y}).
 \tag{1}
\]
The first identity partitions the outside of \(P_x\). The second
uses the zero extension of \(B_x\) and its single-cut second moment.
Both \(W_{x,y}\) and \(P_xB_yP_x\) are positive semidefinite.
Their order comparison gives no order for their graded traces.

For vertices \(u,v\) of \(P_x\), put
\(b_z(u)=\sum_{i:\,u\triangle i\notin P_z}c_i^2\), for \(z=x,y\).
The diagonal contribution of \(u\) to the mixed graded trace is
\(\Gamma_{u,u}b_x(u)b_y(u)\). An off-diagonal term requires
that \(u,v\) differ in exactly two coordinates \(i,j\). Label their
two possible intermediate vertices \(w_1,w_2\). The two path signs
are opposite. For the product of entries to survive, one
intermediate must be outside \(P_y\) and the other inside \(P_x\).
Indeed each cutoff must exclude exactly one intermediate, and the
outside sets are nested. The surviving product is \(c_i^2c_j^2\)
with the same sign on each of the two individual entries before
multiplication. The unordered pair therefore contributes
\(2\Gamma_{u,u}c_i^2c_j^2\), since both endpoints have equal grade.
These diagonal and off-diagonal terms exhaust the four-step
closed walks. The ordinary trace sums nonnegative contributions,
while the graded trace keeps the parity signs.

For the divisor cutoff \(d\le N\le M\), the off-diagonal pairs are
exactly \(dp,dq\le N\) with \(p<q\), \(p,q\nmid d\) and \(dpq>M\).
Their contribution is \(-2\mu(d)c_p^2c_q^2\) per squarefree \(d\).
The coefficient of \(c_p^4\) in the full mixed graded trace is
\[
 \sum_{\substack{d\le N,\ p\nmid d\\pd>M}}\mu(d).
 \tag{2}
\]
For a pair \(p<q\), the coefficient of \(c_p^2c_q^2\) is supported
on the four-vertex faces \(d,dp,dq,dpq\) with \(p,q\nmid d\).
Let \(r,t\) be the number of these vertices retained at \(N,M\),
respectively. Ordered by product, the retained vertices are
initial segments of the indicated order. The only nonzero
contributions to this coefficient, divided by \(\mu(d)\), are
\[
\begin{array}{c|ccc}
 (r,t)&(1,1)&(1,2)&(3,3)\\ \hline
 [c_p^2c_q^2]&2&1&-2 .
\end{array}
\tag{3}
\]
To see this, set \(a=c_p^2,b=c_q^2\) and retain only these
directions. With one vertex the defect there is \(a+b\).
With the first two vertices the defect is \(bI\), and their
grades cancel when both cutoffs have two vertices. With three
vertices the base has defect zero. The other two vertices have
diagonal entries \(b,a\) and an off-diagonal entry of magnitude
\(|c_pc_q|\), hence a rank-one block with eigenvalue \(a+b\)
and negative grade relative to the base. At \((2,3)\) only the
second vertex contributes, giving \(-b^2\) with no mixed
coefficient. Four vertices give zero defect. These cases prove
(3), and a one-coordinate face gives (2). Every four-step
closed walk uses one coordinate four times or two coordinates
twice each. Thus restriction to these one- and two-coordinate
faces extracts all polynomial coefficients with no other
coordinate interactions.
Equivalently the three cases of (3) sum over the following ranges,
always restricted to squarefree \(d\) with \(p,q\nmid d\):
\[
 \left(\frac Mp,N\right],\qquad
 \left(\max\!\left(\frac Np,\frac Mq\right),
                   \min\!\left(N,\frac Mp\right)\right],\qquad
 \left(\frac M{pq},\frac Nq\right].
\]
Empty intervals contribute zero.

The mixed trace depends on information absent from the individual
indices. Use a fixed cube with primes through \(7\) and \(c_7\ne0\).
Take \(N=1\) and compare \(M=5\) with \(M=7\).
The indices at \(5,7\) are both \(-2\), since the additional
squarefree integers \(6,7\) have signs \(+1,-1\). The mixed trace
is \(s c_7^2\) at \(5\) and zero at \(7\), because its only diagonal
entry uses the vertex \(1\). The product of the individual
graded defect traces is \(-2s^2\) in both comparisons.

Even compression to the common retained space need not give
commuting defects. Give the primes \(2,3,5\) unit weight and all
other ambient primes zero weight. For \(N=6,M=10\), work on the
odd span of \(e_2,e_3,e_5\). The outside vertices reachable from
this span at \(6\) in active directions are \(10,15\). Their
boundary rows have vectors \(v=-e_2+e_5\) and \(w=-e_3+e_5\) in
the coordinate order \(2,3,5\). Thus \(B_6=vv^\intercal+ww^\intercal\)
on this span, and \(P_6B_{10}P_6=ww^\intercal\) there. Since
\(v,w\) are independent and \(v^\intercal w=1\), their rank-one
operators have nonzero commutator.

## 2. Harmonic overlap can be computed at the level of ranks

For the single divisor cutoff, suppose the least prime \(p\) in
the fixed ambient list has \(c_p\ne0\). All other real weights may
vanish. Use the differential
\(\partial=\sum_i c_i\iota_i\) on the divisor-closed retained
space. There \(D_N=\partial+\partial^*\) and
\(D_N^2=\partial\partial^*+\partial^*\partial\). The kernel of
\(D_N\) is the space of cycles orthogonal to boundaries
because \(\langle D_N^2 u,u\rangle=\|\partial u\|^2+\|\partial^*u\|^2\).

Let \(K_N^{\rm pair}\) be the span of pairs \(e_d,e_{pd}\)
with \(p\nmid d\) and \(pd\le N\). The space is preserved by
\(\partial\) and by exterior multiplication \(\varepsilon_p\)
in the \(p\) direction. The equality
\(\partial\varepsilon_p+\varepsilon_p\partial=c_p I\) makes
it contractible. Every remaining vertex \(e_d\) has \(p\nmid d\)
and \(N/p<d\le N\). Each one-factor deletion goes into
\(K_N^{\rm pair}\), since its factor is at least \(p\). These
vertices have explicit cycles
\[
 z_d=e_d-c_p^{-1}\varepsilon_p\partial e_d .
\]
The cycles project to the distinct unpaired vertices in the
quotient by \(K_N^{\rm pair}\). All boundaries lie in that
paired space, and every cycle in it is a boundary by the
contraction. Thus the \(z_d\) represent a homogeneous basis of
homology. In particular the graded dimensions of \(\ker D_N\)
are the corresponding counts of unpaired vertices. For the full
prime list and unit weights, the single-cut counts are those in
[Björner, Theorems 2.1 and 3.1](https://arxiv.org/pdf/1101.5704).
An exterior degree \(j\) has simplicial degree \(j-1\), including
the empty label in degree \(-1\), so the two Euler gradings
have opposite signs.

For \(N\le M\) the chain inclusion sends each \(z_d\) to the same
vector. Its homology class dies precisely when \(pd\le M\):
in that case \(z_d=c_p^{-1}\partial\varepsilon_p e_d\) in the
larger complex. Otherwise \(z_d\) is still a member of the
displayed basis there. Thus every \(p\)-free label \(d\) contributes
a homology interval \([d,pd)\) in exterior degree \(\omega(d)\)
over the fixed-list filtration. The class is present at \(d\) and
absent at \(pd\). Hence the harmonic inclusion, orthogonal
projection to \(\ker D_M\) restricted to \(\ker D_N\), has rank
in each grading equal to the number of unpaired labels of that
grade in \(M/p<d\le N\). To identify the map, a cycle differs
from its harmonic projection by a boundary, and inclusion sends
boundaries to boundaries. These are rank identities. The
singular values of the harmonic map need no such identification.
Even the full harmonic overlap vanishes if \(M\ge pN\), without
forcing a vanishing product of indices. For example \(p=2\),
\(N=1,M=3\) have indices \(1,-1\).

For \(p=2\), a list containing all primes through \(N\) gives
\(\dim\ker D_N\gg N\). Indeed the number of odd integers in
\((N/2,N]\) is \(N/4+O(1)\). The nonsquarefree odd integers among
these are covered by odd multiples of \(q^2\) for odd primes
\(q\le\sqrt N\), of which there are at most \(N/(4q^2)+1\) for
each \(q\). The elementary bound
\(\sum_{q\ge2}q^{-2}\le 1/4+\int_2^\infty t^{-2}\,dt=3/4\)
already leaves a positive fraction after the \(O(\sqrt N)\)
rounding error. Thus reducing to harmonic space does not remove
the dimension order of a generic trace estimate in this case.

## 3. The tensor reconstruction and its exact price

The scalar product in the arithmetic energy is
\[
 \frac{(\operatorname{str}B_x)(\operatorname{str}B_y)}{s^2}
 =\frac{1}{s^2}\operatorname{tr}
      \big((\Gamma_x\otimes\Gamma_y)(B_x\otimes B_y)\big),
 \tag{4}
\]
with \(\Gamma_z\) restricted to the range of \(P_z\).
It uses independent pairs of vertices. The mixed trace (1)
instead contracts over common vertices. On the full
grading-preserving matrix space of dimensions
\(d_x=\operatorname{rank}P_x\), \(d_y=\operatorname{rank}P_y\),
the linear trace functional on the right, before the factor
\(s^{-2}\), has Hilbert-Schmidt dual norm \(\sqrt{d_xd_y}\) and
operator-norm dual norm \(d_xd_y\). In both cases the grading
matrix itself gives equality after normalization. These are
norms of the unrestricted linear functional, rather than lower
bounds on the actual tensor of defects. For harmonic projections
\(H_z\) onto \(\ker D_z\) in the retained space,
\(\operatorname{str} B_z=s\operatorname{str}H_z\). Using (4)
with \(H_x,H_y\) removes the two powers of \(s\) and replaces
\(d_x,d_y\) by the harmonic dimensions. The same sharp costs
hold on those respective spaces. Section 2 shows why a bound on
harmonic overlap alone cannot be substituted for this readout.

The same path identities cover the actual two-copy cutoff with
fixed \(T\), including the lower and upper exits. As the upper
bound \(z\) varies, \(P_{T,z}\) increases. Each commutator
or path formula above requiring only nested cutoffs therefore
applies to \(P_{T,z}\). For an off-diagonal pair the outside
intermediate at the larger cutoff can violate a lower bound
\(a,b>T\) or the upper bound \(ab\le z\); the exact criterion is
still one intermediate outside the larger cutoff and the
other inside the smaller cutoff. If both are outside at a cut,
the opposing paths cancel. In the diagonal term the two kinds
of exit enter \(b_z(u)\) together, then receive the retained
vertex's grade. This includes all signs in the boundary model
of [equations (5)–(6)](../BOUNDARY.md).

For a fixed slab and a single time \(N\), let \(\pi(j)\) be the
mass of the forward shift and put
\[
 F_N=\sum_j\pi(j)\sum_{1\le k\le(N+j)/(T+1)^2} B_{T,(N+j)/k},
 \qquad \ell_N=L_X(N)h_T^2 .
\]
All terms act on one common two-copy cube. The untruncated
signed value is \(Z_X(N)=s^{-1}\operatorname{str} F_N-\ell_N\).
The scalar square is exactly
\[
 Z_X(N)^2=s^{-2}\operatorname{tr}
       ((\Gamma\otimes\Gamma)(F_N\otimes F_N))
       -2s^{-1}\ell_N\operatorname{str}F_N+\ell_N^2 .
 \tag{5}
\]
This accounts for both averaged time arguments, all pairs of
floor layers and the external affine square. To get the
positive-part square it must still be multiplied by
\(1_{\{Z_X(N)>0\}}\) before applying the weights
\(1/[N(N+1)]\) over the complete integer window. Alternatively
one can retain the original positive-part dual pairing.
The displayed identities do not estimate either expression.
They recover the exact joint signed observable and distinguish
the different information in mixed paths and harmonic overlap
from the independent graded scalar products. The required
same-window estimate for \(Z\), and hence for \(R_{1/36}\) via
[the pinned transfer](https://github.com/mathorn1973/twist-j/blob/ceb77e3632ec4617c54d8e1fd504d3b1c99dd106/notes/C-RH-THREE-INTERFACE-SYNTHESIS-N/FULL-COUPLED-ENERGY.md),
remains **O**.
