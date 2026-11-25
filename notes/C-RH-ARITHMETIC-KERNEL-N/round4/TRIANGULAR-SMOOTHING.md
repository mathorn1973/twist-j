# Finite rational smoothing and the surviving short correlations

C-RH-ARITHMETIC-KERNEL-N, round 4, #2087 / #2089. NON-CANONICAL, no authority. Candidate-D paper proof under [PREREG-LOCAL](PREREG-LOCAL.md). No scientific computation or claim of historical priority. This uses the arithmetic sequence \(t=(s*\chi_5)\), with the exact local factors of the pinned candidate.

Write \(T(0)=0\), \(T(n)=\sum_{m\le n}t(m)\). From the local factors, \(|t(m)|\le1\) and \(t(m)^2=\mathbf1_{5\nmid m}\). Let \(X\ge16\) and \(2\le H\le X/8\) be integers. Define the finite rational average and its error by
\[
 {\cal T}_H(n)=\frac1{H^2}\sum_{|j|<H}(H-|j|)T(n+j),\qquad
 D_H(n)=T(n)-{\cal T}_H(n)\quad (X\le n<2X).
\]
The weights sum to one. Summing the first differences in the positive and negative shifts gives the exact identity
\[
 D_H(n)=\sum_{h=1}^{H-1}c_h\,[t(n-h+1)-t(n+h)],\qquad
 c_h=\frac{(H-h)(H-h+1)}{2H^2}.                             \tag{1}
\]
Thus \(|D_H(n)|\le H\). For \(1\le h\le H-1\), set \(u_H(1-h)=c_h\) and \(u_H(h)=-c_h\), and put \(u_H(j)=0\) elsewhere. The support is contained in \([2-H,H-1]\) and \(\sum_j u_H(j)=0\).

## 1. The exact quadratic expression and a high-gcd bound

For positive integers \(m,k\) set
\[
 K_{X,H}(m,k)=\sum_{n=X}^{2X-1}u_H(m-n)u_H(k-n).
\]
This kernel includes the time endpoints exactly and vanishes unless \(m,k\in[X-H,2X+H]\) and \(|m-k|\le2H\). Expanding (1) gives
\[
 {\cal E}(X,H):=\sum_{n=X}^{2X-1}|D_H(n)|^2
      =\sum_{m,k\ge1}t(m)t(k)K_{X,H}(m,k).                    \tag{2}
\]
Each entry has absolute value \(O(H)\), from Cauchy–Schwarz in \(n\) and \(|u_H|\le1/2\). The diagonal in (2) equals
\[
 \sum_j u_H(j)^2 \sum_{n=X}^{2X-1}\mathbf1_{5\nmid n+j}
       =\bigl(\tfrac45 X+O(1)\bigr)\sum_j u_H(j)^2=O(XH).
\]
The \(O(1)\) is uniform over translates, so the equality holds with the summation over \(j\) absorbed as stated.

For real \(G\ge1\), the total absolute contribution of off-diagonal terms with \(\gcd(m,k)\ge G\) is \(O(XH^2/G)\). Indeed their common divisor \(g=\gcd(m,k)\) is at most \(|m-k|\le2H\). For each integer \(g\) in this range, sum over all pairs divisible by \(g\), a permissible overcount. There are \(O(X/g)\) possible multiples \(m\) in the support window and \(O(H/g)\) nonzero differences \(k-m\) divisible by \(g\). Their total count is \(O(XH/G)\) by summing \(g^{-2}\). Multiplication by the entry bound \(O(H)\) proves the claim.

In particular, for fixed \(0<\delta<1/2\), take \(H=\lfloor X^{1/2+\delta}\rfloor\) at sufficiently large \(X\), and \(G=\max(2,\lceil H^2/X\rceil)\). Define the signed low-gcd term
\[
 {\cal A}(X,H,G)
   =\sum_{\substack{m\ne k\\\gcd(m,k)<G}}t(m)t(k)K_{X,H}(m,k).
\]
The result is
\[
 {\cal E}(X,H)={\cal A}(X,H,G)+O(X^2).                        \tag{3}
\]
Consequently the rational smoothing has square error \(O_\epsilon(X^{2+\epsilon})\) on all large dyadic blocks for every \(\epsilon>0\) exactly when \(({\cal A}(X,H,G))_+\) has that bound on those blocks. This is a reduction for the smoothing error. It leaves the separate estimate for the smoothed sum itself.

## 2. A signed, translation-invariant form below the \(X^{2/3}\) boundary

Define the autocorrelation with no time boundary by
\[
 \Gamma_H(h)=\sum_{j\in\mathbb Z}u_H(j)u_H(j+h).
\]
It is even, supported on \(|h|\le2H\), has \(\sum_h\Gamma_H(h)=0\), and satisfies \(\sum_h|\Gamma_H(h)|\ll H^2\). For \(m\) at least \(H\) from either edge of the block, \(K_{X,H}(m,k)=\Gamma_H(k-m)\), since all possible time indices in the kernel lie in the block. Replacing \(K_{X,H}(m,k)\) by \(\mathbf1_{X\le m<2X}\Gamma_H(k-m)\) therefore changes only \(O(H)\) boundary values of \(m\) and \(O(H)\) neighboring values of \(k\) per such \(m\). The entry bound and \(|t|\le1\) give
\[
 {\cal E}(X,H)=\sum_h\Gamma_H(h)\sum_{m=X}^{2X-1}t(m)t(m+h)+O(H^3).
                                                               \tag{4}
\]
All arguments \(m+h\) are positive in the stated range of \(H\). The diagonal norms \(\sum_{m=X}^{2X-1}t(m+h)^2\) are \(\tfrac45X+O(1)\) uniformly in \(h\), by periodicity modulo five. Expand the squares in
\[
 {\cal E}(X,H)
 =-\frac12\sum_h\Gamma_H(h)\sum_{m=X}^{2X-1}\bigl(t(m+h)-t(m)\bigr)^2
     +O(H^3).                                                 \tag{5}
\]
Equation (5) follows from (4), the vanishing sum of \(\Gamma_H\), and the \(O(H^2)\) cost of the bounded translate errors in the diagonal norms. In particular for \(H\le X^{2/3}\) the boundary is within \(O(X^2)\). For this kernel, extending the averaging width beyond the square-root scale in this range while retaining the stated dyadic square-error bound reduces to cancellation across a signed weighted sum of short translation correlations. The known periodic contribution of the diagonals can be removed before estimating that sum. The individual inner squares in (5) are nonnegative, while their outer weights have both signs.

## 3. Positive low-gcd entries exceed the requested error scale

The local shape of \(\Gamma_H\) suffices for a lower bound on the positive-entry majorant. For \(H\ge4\), the terms \(1\le h\le\lfloor H/2\rfloor\) satisfy \(c_h\ge1/8\); thus \(\Gamma_H(0)\ge H/96\). The total variation of \(u_H\), extended by zero, is \(4c_1\le2\). Indeed the positive side rises to \(c_1\), the middle jump falls to \(-c_1\), and the negative side rises to zero. Also any difference of its entries has absolute value at most one. Hence for integer \(h\),
\[
 \Gamma_H(0)-\Gamma_H(h)
 =\frac12\sum_j (u_H(j+h)-u_H(j))^2
 \le\frac12\sum_j |u_H(j+h)-u_H(j)|
 \le |h|.
\]
Thus \(\Gamma_H(h)\ge H/192\) whenever \(|h|\le H/192\).

The inert primes \(p\) in \((5X/4,7X/4]\) number \(\gg X/\log X\), by the ordinary fixed-modulus PNT for the two classes \(2,3\) modulo five. They are interior to the block for \(H\le X/8\). Divide this interval into \(O(X/H)\) bins of \(\lfloor H/192\rfloor+1\) consecutive integers. If \(P_i\) counts the inert primes in bin \(i\), Cauchy–Schwarz gives
\[
 \sum_i P_i(P_i-1)\ \ge\ \frac{(\sum_i P_i)^2}{\#\{\text{bins}\}}-\sum_iP_i
             \ \gg\ \frac{XH}{(\log X)^2}
\]
when \(H/\log X\to\infty\). All pairs here are ordered, distinct, coprime and have \(|p-q|\le H/192\). Their coefficient products are \(t(p)t(q)=1\). For each, \(K_{X,H}(p,q)=\Gamma_H(q-p)\ge H/192\). It follows that the positive-entry majorant already has
\[
 \sum_{\substack{m\ne k\\\gcd(m,k)=1}}
    \bigl(t(m)t(k)K_{X,H}(m,k)\bigr)_+
        \gg \frac{XH^2}{(\log X)^2}.                           \tag{6}
\]
The argument draws primes from a single macroscopic interval. It does not assume a distribution theorem in the individual bins. For \(H=\lfloor X^{1/2+\delta}\rfloor\), (6) grows as \(X^{2+2\delta}/(\log X)^2\) and obstructs any entrywise positive or absolute upper bound at the scale in (3) for \(\epsilon<2\delta\). It uses the actual arithmetic coefficients and no adaptive deletion. The signed \({\cal A}\) can have cancellation with other pairs, and (6) gives no lower bound for \({\cal E}\).

The remaining condition is an upper bound for the actual signed sum \({\cal A}\), or for the equivalent signed form (5) when \(H\le X^{2/3}\). Neither the gcd count nor the inert-prime count furnishes that bound.

- Primary prime-count input: [Bennett, Martin, O’Bryant and Rechnitzer, Explicit bounds for primes in arithmetic progressions, Theorem 1.2](https://arxiv.org/html/1802.00085v3).
