# The actual positive energy left by omitting either factor square

C-RH-ARITHMETIC-KERNEL-N, issue [#2087](https://github.com/mathorn1973/twist-j/issues/2087), draft [#2089](https://github.com/mathorn1973/twist-j/pull/2089), round 9. **NON-CANONICAL. No authority. Candidate-D paper deductions.** Action layer NOT_APPLICABLE. The complete signed estimate remains **O**. This tests the same arithmetic coefficients as round eight, under [PREREG.md](PREREG.md).

## 1. Retain the signs before taking a positive part

Keep the original taper \(w\) on dyadic \(X\), with \(w=1\) at all integers in \([X,2X)\) and support in \([7X/8,17X/8]\). Let \(T(y)=\sum_{m\le y}t(m)\) with the usual integer floor and value zero below one. The actual local values are \(t(p^j)=-1\) at split primes, \((-1)^j\) at inert primes, and \(0\) at positive powers of five. Thus \(|t(m)|=1\) for \(5\nmid m\) and \(t(m)=0\) for \(5\mid m\).

Write \(f=t^{-1}=\mathbf1*u\) for the Dirichlet inverse of \(t\), \(U\) for the coefficient series of \(u\), and \(F(y)=\sum_{k\le y}f(k)\). The local inverse coefficients are \(2^{j-1}\) at a positive split-prime power \(p^j\), one at an inert prime and zero at higher inert powers, and zero at positive powers of five. In particular \(f(k)\ge0\). Round-eight COUPLED-CUTS, equation (9), gives
\[
 F(y)=U(1)y+O(y^{5/12}),\qquad U(1)>0,                          \tag{1}
\]
after absorbing its displayed cubic term into the error.

For a strict integer cutoff \(A\), put \(t_{\le A}(m)=t(m)\mathbf1_{m\le A}\), \(t_{>A}=t-t_{\le A}\), \(h_A=\sum_{m\le A}t(m)/m\), and \(D_A(m)=T(m)-T(A)\) for \(m\ge A\). The exact Dirichlet identity is
\[
 t=2t_{\le A}-f*t_{\le A}*t_{\le A}+f*t_{>A}*t_{>A}.
\]
The short rectangle has linear term \(nU(1)h_A^2\). Its error from (1) is \(O(X^{5/12}A^{7/6})\), by \(\sum_{m\le A}m^{-5/12}\ll A^{7/12}\) and \(|t(m)|\le1\). This applies when \(A^2\le7X/8\), so all arguments of \(F\) are at least one. The long rectangle is split at \(r_k=\lfloor\sqrt{n/k}\rfloor\) in each oriented term, subtracting its overlap. Consequently, on the full taper,
\[
 \begin{split}
 T(n)&=\mathcal L_A(n)-nU(1)h_A^2-\mathcal S_A(n)
                  +O\big(A+X^{5/12}A^{7/6}\big),\\
 \mathcal S_A(n)&=
       \sum_{1\le k\le n/(A+1)^2}f(k)D_A(r_k)^2,\\
 \mathcal L_A(n)&=
       2\sum_{1\le k\le n/(A+1)^2} f(k)
          \sum_{A<a\le r_k}t(a)D_A\big(\lfloor n/(ka)\rfloor\big).
 \end{split}                                                    \tag{2}
\]
Every pair with \(a,b>A\) and \(kab\le n\) has a coordinate at most \(r_k\). The intersection of the two orientations is exactly \(A<a,b\le r_k\). Thus (2) retains the integer boundary and the signs of both squares. The displayed \(\mathcal L_A\) equals the regrouped divisor form of round eight by \(j=ka\), including the arguments beyond \(\sqrt n\). At \(A=\lfloor X^{1/14}\rfloor\) the error in (2) is \(O(\sqrt X)\), as in the frozen earlier formula.

## 2. A uniform lower bound for the actual overlap penalty

Fix \(0<\alpha<1/6\) and let \(A\asymp X^\alpha\) on the block, with constants independent of \(X\). In \([A+1,2A]\), at least \(4A/5-O(1)\) distinct integer edges \(m-1\to m\) have \(|D_A(m)-D_A(m-1)|=1\), because \(5\nmid m\). Each such edge has a nonzero endpoint, and each endpoint accounts for at most two edges. Since \(D_A(A)=0\) and all these values are integers, there are \(\gg A\) indices \(m\in[A+1,2A]\) with \(D_A(m)^2\ge1\).

For each such \(m\), the condition \(r_k=m\) is exactly
\[
             n/(m+1)^2<k\le n/m^2 .
\]
Both endpoints are retained with these inequalities even when integral. Since \(m\ge A+1\), all its \(k\) belong to the sum in (2). By (1), for \(n\) on the full taper its \(f\)-mass is
\[
 \begin{split}
 F(n/m^2)-F(n/(m+1)^2)
  &= U(1)n\left(\frac1{m^2}-\frac1{(m+1)^2}\right)
                    +O\big((X/A^2)^{5/12}\big)\\
  &\gg X/A^3 .
 \end{split}                                                     \tag{3}
\]
The main term has order \(X/A^3\) uniformly in \(m\), and the error divided by that order is \(O(X^{-7/12}A^{13/6})=o(1)\) in the full stated range of \(\alpha\). Because \(f\ge0\), using only these bins gives the unconditional actual-coefficient bound
\[
                  \mathcal S_A(n)\gg_\alpha X/A^2               \tag{4}
\]
uniformly on the taper. The error in (2) is \(o(X/A^2)\): the term \(A\) has that property for \(\alpha<1/3\), and \(X^{5/12}A^{7/6}\) has it for \(\alpha<7/38\). In particular both hold in the range used here.

## 3. Actual positive times of \(T\)

There are arbitrarily large integers with \(T(n)>0\). This uses the inherited signed power-window lemma, only with a weaker half-plane than its round-three application. On \(\Re s>1\) the Mellin transform of \(T\) is
\[
          \mathcal T(s)=\int_1^\infty T(y)y^{-s-1}dy
                       =\frac{1}{s\zeta(s)U(s)}.
\]
The round-six formal factorization provides the continuation
\[
    U(s)=L(2s,\chi_5)\zeta(3s)L(3s,\chi_5)W_4(s)
\]
with \(W_4\) absolutely convergent on \(\Re s>\log2/\log11\). In particular \(U\) is holomorphic on \(\Re s>1/3\). For real \(s>1/3\) the fixed character values \(L(2s,\chi_5)\) and \(L(3s,\chi_5)\) are positive: grouping the defining real \(L\)-series by residue periods gives positive blocks, since \(v^{-q}-(v+1)^{-q}\) decreases strictly in \(v>0\) for \(q>0\). Also \(\zeta(3s)>0\), and the local \(W_4\) factors are positive with absolutely summable deviations. This gives \(U(s)>0\) throughout that real interval. The Riemann zeta function has no real zero for \(s>1/3\): its Euler product is nonzero for real \(s>1\), and for \(0<s<1\) the paired alternating series \((1-2^{1-s})\zeta(s)\) is positive. At \(s=1\), \(\mathcal T\) has a zero from the zeta pole. Thus \(\mathcal T\) is meromorphic on \(\Re s>1/3\) and has no real pole there.

Hardy's theorem supplies nonreal zeros of \(\zeta\) on \(\Re s=1/2\). At any such zero \(U\) is holomorphic, so a zero of \(U\) there could only increase the pole order of \(\mathcal T\). There is no cancellation by a pole of \(U\). Apply the inherited FOUNDATION §1 lemma with \(f(v)=T(e^v)\) in its notation, \(\theta=2/5\), and any fixed window ratio greater than one. The exponential size premise follows from \(|T(y)|\le y\), and the preceding argument verifies the actual nonreal pole and real-axis regularity. This gives arbitrarily large \(y\) with \(T(y)>0\). Flooring yields arbitrarily large such integers. Only the existence of this unbounded sequence of positive times is used here.

## 4. Lower bounds when one square is omitted

Take a dyadic block \(X\le n_0<2X\) with \(T(n_0)>0\). There are infinitely many such blocks by §3. Write \(B_X=X/A^2=o(X)\). By (4), fix a constant \(c_1>0\) such that \(\mathcal S_A(n)\ge c_1B_X\) on the taper at all sufficiently late blocks. At least one side of \(n_0\) in the central integer interval permits \(\lfloor c_1 B_X/4\rfloor\) steps, since that number is \(o(X)\). At every such \(n\), the unit increment bound on \(T\) gives \(T(n)\ge-c_1B_X/4\). Equation (2) has error \(o(B_X)\); therefore
\[
 \mathcal L_A(n)-nU(1)h_A^2\ge \tfrac12c_1 B_X
\]
at \(\gg_\alpha B_X\) distinct integers of weight one on each of these late blocks. In particular
\[
 \big\|\big(\mathcal L_A-nU(1)h_A^2\big)_+\big\|_w^2
       \gg_\alpha X^{3-6\alpha}
 \quad\hbox{on infinitely many dyadic }X.                       \tag{5}
\]
The same lower bound holds for \(\|(\mathcal L_A)_+\|_w^2\). At the exact round-eight cutoff \(A=\lfloor X^{1/14}\rfloor\), (5) has exponent \(18/7\). This rules out the round-eight sufficient approach that bounds the positive part of \(\mathcal L_A\) alone. It also rules out dropping just the overlap penalty while keeping the full affine penalty, even on that unchanged cutoff. These conclusions are for the actual \(t\), not substituted prefix data.

There is also a strict cutoff for which **each penalty is necessary separately**. Fix the same \(\alpha\) and \(A_0=\lfloor X^\alpha\rfloor\). Let \(m\) be the first integer greater than \(A_0\) with \(5\nmid m\), so \(m\le A_0+2\). Choose \(A\in\{m-1,m\}\) maximizing \(|h_A|\), breaking a tie with the smaller cutoff. Because \(|h_m-h_{m-1}|=1/m\), \(|h_A|\ge1/(2m)\), hence \(nU(1)h_A^2\gg X/A^2\) uniformly on the taper. This choice depends on the actual coefficients through that cutoff, is fixed on the entire slab, and changes the original integer choice by at most two. Equation (4) gives the same lower scale for the overlap penalty on this slab. Repeating the positive-time interval argument with the smaller of the two lower constants establishes
\[
 \big\|\big(\mathcal L_A-\mathcal S_A\big)_+\big\|_w^2
      \gg_\alpha X^{3-6\alpha},
 \qquad
 \big\|\big(\mathcal L_A-nU(1)h_A^2\big)_+\big\|_w^2
      \gg_\alpha X^{3-6\alpha}
\]
on the same infinitely many blocks. At \(\alpha=1/14\) this neighboring-cutoff family still has the round-eight \(O(\sqrt X)\) reconstruction error. The affine-square obstruction here concerns this specified cutoff choice. The overlap-square obstruction (5) needs no adjustment of the original cutoff. All statements concern the separate positive energies obtained after one deletion. The lower bounds do not apply to the true profile with both penalties.

## Scope and sources

**Candidate-D.** The large lower bounds use fixed dyadic cutoffs, actual \(t\), nonnegative actual \(f\), explicit floor bins, and a proof of arbitrarily late positive \(T\) times. **O.** The norm of the complete jointly signed profile, with both squares and all original upper prefix arguments retained, remains open.

- [Arithmetic-kernel baseline 6a91ef48f6454743797614503aa5863dde54befb](https://github.com/mathorn1973/twist-j/tree/6a91ef48f6454743797614503aa5863dde54befb/notes/C-RH-ARITHMETIC-KERNEL-N). Read FOUNDATION §§1–2, round 6 BALANCED-UNIT-TAIL §1, and round 8 COUPLED-CUTS §4. The existing signed-window lemma, factorization of \(U\), and weaker mean estimate (1) are used as stated. Formula (2) records the inherited sign and upper-argument structure with its dependence on \(A\).
- [G. H. Hardy, Sur les zéros de la fonction ζ(s) de Riemann, C. R. Acad. Sci. Paris 158 (1914), 1012–1014](https://fr.wikisource.org/wiki/Page:Comptes_rendus_hebdomadaires_des_s%C3%A9ances_de_l%E2%80%99Acad%C3%A9mie_des_sciences,_tome_158,_1914.djvu/1014). The original article gives existence of critical-line zeros. No zero table, verification of RH, or inference about zeros of \(L(s,\chi_5)\) on the critical line is used.
- Read the neighboring [full coupled-energy and review notes at ceb77e3632ec4617c54d8e1fd504d3b1c99dd106](https://github.com/mathorn1973/twist-j/tree/ceb77e3632ec4617c54d8e1fd504d3b1c99dd106/notes/C-RH-THREE-INTERFACE-SYNTHESIS-N) and the [Huang arithmetic-bridge report and prime-scale note at fd6232aa10da26a374e421d6d46538b36b41aafb](https://github.com/mathorn1973/twist-j/tree/fd6232aa10da26a374e421d6d46538b36b41aafb/notes/C-HUANG-ARITHMETIC-BRIDGE-N). Their models and actual prime-boundary identities have distinct carriers. Neither supplies an arithmetic lower bound for this overlap penalty.

Paper algebra only. No numerical or symbolic scientific execution, formal runner or repository modification in this lane. The authority and scope readbacks preceded the work and were completed by the same session owner.
