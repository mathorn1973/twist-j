# Exact dilation correlations and the scope of finite local data

C-RH-ARITHMETIC-KERNEL-N, round 4, #2087 / #2089. NON-CANONICAL, no authority. Candidate-D paper proof under [PREREG-LOCAL](PREREG-LOCAL.md). No scientific computation.

Let \(t=(s*\chi_5)\). Its local values at positive prime powers are \(-1\) for split primes, \((-1)^k\) at the \(k\)-th power of an inert prime, and zero at powers of 5. For coprime positive \(a,b\), let \(P_{a,b}\) be the product of the distinct split primes dividing \(ab\). Then for every positive integer multiplier \(g\),
\[
 t(ga)t(gb)
   =\mathbf1_{5\nmid g}\,t(a)t(b)
       \prod_{\substack{p\mid P_{a,b}\\p\mid g}}(-1).           \tag{1}
\]
For inert primes the two added exponents have even total, so their contribution is unchanged. A split prime outside \(ab\) produces two equal local signs, with product one. A split prime dividing \(ab\) belongs to exactly one side. Inserting it into \(g\) makes the local sign on both sides \(-1\), changing the product from \(-1\) to \(+1\). A factor of 5 kills the relevant product. These exhaust the cases.

Expand each local factor in (1) as \(1-2\mathbf1_{p\mid g}\). Then for real \(Y\ge0\),
\[
 \sum_{g\le Y}t(ga)t(gb)=t(a)t(b)
       \sum_{d\mid P_{a,b}}(-2)^{\omega(d)}
       \left(\left\lfloor\frac{Y}{d}\right\rfloor
               -\left\lfloor\frac{Y}{5d}\right\rfloor\right).    \tag{2}
\]
The sequence in \(g\) is periodic with period dividing \(5P_{a,b}\). Its complete mean is
\[
 \frac45\,t(a)t(b)\prod_{p\mid P_{a,b}}(1-2/p),                 \tag{3}
\]
and the deviation of (2) from \(Y\) times this mean is at most \(3^{\omega(P_{a,b})}\). The difference of the two floor errors has absolute value at most one, and the absolute divisor weights sum to the displayed power of three. Equations (2)–(3) also give the interval readout by subtracting endpoints, or a weighted version by finite summation by parts. For example, the reduced ratios \(1:2\) and \(1:4\) have means \(-4/5\) and \(+4/5\). At \(1:11\) the mean is \(-\tfrac45(1-2/11)\). Thus individual reduced ratios have persistent signed correlation. Their periodic multiplier information does not give an upper bound for the joint sum over varying ratios and moving kernels in TRIANGULAR-SMOOTHING.md.

Here is a paper limit on any argument that consumes just a finite set of local factors. Fix any finite set of primes \({\cal F}\). Define a multiplicative coefficient \(f_{\cal F}\) by taking the exact \(t(p^k)\) at every positive prime power with \(p\in{\cal F}\) and the value \(1\) at all other prime powers. Then \(|f_{\cal F}|\le1\), and
\[
 \sum_{n\le X}f_{\cal F}(n)\sim C_{\cal F}X,\qquad
 C_{\cal F}=
   \prod_{\substack{p\in{\cal F}\\p\ {\rm split}}}(1-2/p)
   \prod_{\substack{p\in{\cal F}\\p\ {\rm inert}}}\frac{p-1}{p+1}
   \begin{cases}4/5,&5\in{\cal F},\\1,&5\notin{\cal F}.\end{cases}
\]
Every factor is strictly positive. To prove this let \(h=\mu*f_{\cal F}\), supported on integers with all prime factors in \({\cal F}\) with \(|h(p^k)|=|f_{\cal F}(p^k)-f_{\cal F}(p^{k-1})|\le2\). Its absolute series at one converges because \({\cal F}\) is finite. Now
\[
 X^{-1}\sum_{n\le X}f_{\cal F}(n)=
   \sum_{d\le X}h(d)X^{-1}\lfloor X/d\rfloor
       \longrightarrow \sum_d h(d)/d
\]
by dominated convergence. Multiplying the finite local series evaluates the limit as \(C_{\cal F}\).

Thus bounded multiplicativity and any finite selection of the prescribed prime-power factors do not force cancellation at the desired all-scale rate. This is a witness for finite input only. The full collection of prescribed prime-power factors determines \(t\), and no impossibility for using the full arithmetic is claimed.
