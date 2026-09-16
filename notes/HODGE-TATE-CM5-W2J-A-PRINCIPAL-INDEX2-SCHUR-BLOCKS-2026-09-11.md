# Hodge-Tate CM5: W2J-A principal index-two Schur blocks

**STATUS: NON-CANONICAL RESEARCH NOTE.**

**Basis:** Public Canon v84 and the companion Hodge-Tate / Markman / Perry CM5 notes through
`HODGE-TATE-CM5-W2I-B-TWISTED-PERFECT-CORRECTION-2026-09-11.md`.

**Date:** 2026-09-11.

This note starts **Gate W2J**. W2I-B produced an exact weight-one perfect source class on the mixed order-80 quotient, but the witness was deliberately decomposable. The remaining problem is categorical: obtain a Schur/simple representative and control

\[
r_H=\dim\operatorname{Ext}^1(\mathscr G,\mathscr G).
\]

The first step is to replace the nine-term correction certificate by a much smaller derived model built from principal nondegenerate divisor classes of index two. The result is exact:

\[
\boxed{\bar Q=S_1S_2S_3+S_4S_5S_6,}
\]

where all six `S_i` are integral quotient divisor classes with

\[
\boxed{\chi(\mathcal O(S_i))=1,\qquad \operatorname{index}(S_i)=2.}
\]

Each factor therefore determines a canonical two-cell Schur object which is Fourier-Mukai equivalent, up to line-bundle twist and shift, to the ideal sheaf of one point. This does not yet prove the two triple tensor blocks are Schur, but it replaces arbitrary virtual divisor algebra by six explicit small Schur building blocks and makes the next dg gluing problem finite.

No `canon/` or registry file is changed. No semiregularity theorem is claimed.

---

## 1. An LLL-reduced quotient Neron-Severi basis

Let

\[
R_0,\ldots,R_7\in\operatorname{NS}(\bar X)
\]

be the quotient divisor classes whose pullbacks are expressed in the original CM5 Hermitian NS basis `N_0,...,N_7` by the columns of

\[
\boxed{
L_{\rm red}=
\begin{pmatrix}
2&0&2&-2&0&2&0&0\\
0&0&0&-2&2&-2&2&0\\
2&2&-2&2&0&0&0&0\\
0&-4&-2&0&2&2&2&0\\
-2&0&-2&-2&0&0&0&-2\\
0&0&0&0&0&0&4&-8\\
0&0&0&0&2&2&4&2\\
0&0&0&0&2&2&-4&-2
\end{pmatrix}.
}
\]

The companion verifier reconstructs every transformed alternating form and checks that all eight classes are integral on the mixed order-80 quotient lattice.

The basis is chosen for short coordinates only; no positivity property of the `R_i` is assumed.

---

## 2. Six principal index-two divisor classes

Define

\[
\begin{aligned}
S_1&=R_1-R_4,\\
S_2&=R_0-R_1-R_2-R_4,\\
S_3&=R_0+R_1-R_3-R_4-R_5,\\
S_4&=R_1+R_4,\\
S_5&=R_0-R_1-R_3-R_4,\\
S_6&=R_0-R_2-R_5.
\end{aligned}
\]

Their pullbacks to the original CM5 product have the following coefficients in the Hermitian NS basis:

\[
\begin{array}{c|rrrrrrrr}
 &N_0&N_1&N_2&N_3&N_4&N_5&N_6&N_7\\ \hline
S_1&0&-2&2&-6&0&0&-2&-2\\
S_2&0&-2&2&4&0&0&-2&-2\\
S_3&2&2&2&-8&0&0&-4&-4\\
S_4&0&2&2&-2&0&0&2&2\\
S_5&4&0&-2&2&0&0&-2&-2\\
S_6&-2&2&4&0&0&0&-2&-2
\end{array}
\]

Exact Pfaffian calculation on the quotient gives

\[
\boxed{\operatorname{Pf}(S_i)=1\quad (1\le i\le6).}
\]

Hence each line bundle `O(S_i)` is nondegenerate with Euler characteristic `1`.

To determine its index without floating point, evaluate the associated two-by-two Hermitian determinant and trace at the two real embeddings of `F=Q(sqrt(5))`. In `x+y phi` coordinates the exact trace/determinant pairs are

\[
\begin{array}{c|c|c}
 &\operatorname{tr}&\det\\ \hline
S_1&2-8\varphi&8+4\varphi\\
S_2&2+2\varphi&-12-16\varphi\\
S_3&4-6\varphi&-28-44\varphi\\
S_4&2&-8-4\varphi\\
S_5&2+2\varphi&-12+4\varphi\\
S_6&2+2\varphi&-12+4\varphi
\end{array}
\]

and the companion verifier checks the signs exactly at both embeddings. In every case the total number of negative Hermitian eigenvalues is two. Thus

\[
\boxed{\operatorname{index}(S_i)=2.}
\]

By the index theorem for nondegenerate line bundles on abelian varieties, for every `alpha in Pic^0(bar X)`

\[
H^k(\bar X,\mathcal O(S_i)\otimes\alpha)=0\quad(k\ne2),
\]

and

\[
\boxed{h^2(\bar X,\mathcal O(S_i)\otimes\alpha)=1.}
\]

The inverse line bundle also has index `4-2=2` and the same one-dimensional middle cohomology.

---

## 3. Two-term divisor-triple identity for bar Q

Exact exterior algebra gives

\[
\boxed{
\bar Q=S_1S_2S_3+S_4S_5S_6.
}
\]

Both summands couple equally to the support polarization:

\[
\boxed{
\int_{\bar X}\bar L\,S_1S_2S_3=5,
\qquad
\int_{\bar X}\bar L\,S_4S_5S_6=5.
}
\]

Thus the two correction blocks are balanced relative to the divisor-supported source. In particular neither is Euler-orthogonal to that source.

This is a stronger categorical starting point than the first compact two-term identity found during the search, where one summand had zero `bar L` pairing.

---

## 4. Canonical two-cell Schur object for each S_i

Let

\[
L_i:=\mathcal O_{\bar X}(S_i).
\]

Since `L_i` has index two and Euler characteristic one,

\[
\operatorname{Ext}^2(L_i^{-1},\mathcal O_{\bar X})
=H^2(\bar X,L_i)
\simeq\mathbf C.
\]

Choose its unique nonzero class up to scalar,

\[
\epsilon_i:L_i^{-1}\longrightarrow\mathcal O_{\bar X}[2],
\]

and define

\[
\boxed{
C_i:=\operatorname{Cone}(\epsilon_i).
}
\]

Then

\[
\boxed{[C_i]=[\mathcal O]-[L_i^{-1}]\in K_0(\bar X).}
\]

This is the derived replacement for the ordinary divisor Koszul factor `1-O(-S_i)`. It uses no effectivity or arbitrary section choice.

---

## 5. Fourier-Mukai identification with an ideal-point sheaf

Let

\[
\Phi_{\mathcal P}:D^b(\bar X)\to D^b(\widehat{\bar X})
\]

be the Poincare Fourier-Mukai equivalence.

The nondegenerate index theorem gives

\[
\Phi_{\mathcal P}(L_i^{-1})
\simeq\widehat L_i[-2]
\]

for a line bundle `widehat L_i` on the dual, because the transform has rank `|chi(L_i)|=1`. With the standard normalization

\[
\Phi_{\mathcal P}(\mathcal O_{\bar X})
\simeq k(0)[-4],
\]

so

\[
\Phi_{\mathcal P}(\mathcal O[2])
\simeq k(0)[-2].
\]

The nonzero class `epsilon_i` therefore becomes the unique nonzero morphism

\[
\widehat L_i\longrightarrow k(0),
\]

which is surjective. Its cone is the ideal sheaf of the origin twisted by `widehat L_i`, up to the common shift. Hence

\[
\boxed{
\Phi_{\mathcal P}(C_i)
\simeq
I_0\otimes\widehat L_i[-1]
}
\]

up to the harmless global convention for the Fourier-Mukai shift.

Consequently every `C_i` is Schur:

\[
\boxed{\operatorname{End}(C_i)=\mathbf C.}
\]

Moreover the rank-one torsion-free sheaves `I_x\otimes P_alpha` form the smooth local family `bar X x Pic^0(bar X)` of dimension eight. Thus

\[
\dim\operatorname{Ext}^1(C_i,C_i)=8.
\]

The self Euler characteristic is

\[
\chi(C_i,C_i)
=\int(1-e^{S_i})(1-e^{-S_i})
=-\frac1{12}\int S_i^4
=-2,
\]

because `chi(L_i)=S_i^4/4!=1`. Serre duality on the abelian fourfold therefore gives

\[
\boxed{
\dim\operatorname{Ext}^{0,1,2,3,4}(C_i,C_i)
=(1,8,12,8,1).
}
\]

So each divisor factor is an explicit small Schur derived object, not merely a virtual K-class.

---

## 6. Two actual perfect correction blocks

Define

\[
K_A:=C_1\otimes^LC_2\otimes^LC_3,
\qquad
K_B:=C_4\otimes^LC_5\otimes^LC_6.
\]

Their K-classes are exactly the two divisor-Koszul products in Section 3. Therefore their degree-six Chern characters are respectively

\[
Q_A=S_1S_2S_3,
\qquad
Q_B=S_4S_5S_6,
\]

with

\[
Q_A+Q_B=\bar Q.
\]

The exact degree-eight contributions are

\[
\boxed{
\operatorname{ch}(K_A)=Q_A+4[\mathrm{pt}],
}
\]

and

\[
\boxed{
\operatorname{ch}(K_B)=Q_B-6[\mathrm{pt}].
}
\]

Hence

\[
\operatorname{ch}(K_A\oplus K_B)
=\bar Q-2[\mathrm{pt}].
\]

Add three shifted point sheaves:

\[
K_{\rm blk}:=
K_A\oplus K_B\oplus\mathcal O_p[1]^{\oplus3}.
\]

Then

\[
\boxed{
\operatorname{ch}(K_{\rm blk})
=\bar Q-5[\mathrm{pt}].
}
\]

On the square-root gerbe, tensor with the tautological weight-one line `mathscr M`. Since

\[
\frac12\int\bar L\bar Q=5,
\]

the top term cancels and

\[
\boxed{
\mathscr T_{\rm blk}
:=\mathscr M\otimes p^*K_{\rm blk},
\qquad
\operatorname{ch}(\mathscr T_{\rm blk})=\bar Q.
}
\]

This is a six-Schur-block replacement for the nine-term correction witness of W2I-B.

---

## 7. Both correction blocks couple to the divisor source

Let

\[
\mathscr F_0=i_*(\mathscr M|_{\bar Y}),
\qquad [\bar Y]=\bar L.
\]

Its Chern character is

\[
\operatorname{ch}(\mathscr F_0)
=\bar L+\frac1{24}\bar L^3.
\]

Because `Q_A,Q_B` have codimension three, Riemann-Roch immediately gives

\[
\boxed{
\chi(\mathscr F_0,\mathscr M\otimes K_A)
=-\int\bar LQ_A=-5,
}
\]

and

\[
\boxed{
\chi(\mathscr F_0,\mathscr M\otimes K_B)
=-\int\bar LQ_B=-5.
}
\]

Point corrections have zero Euler pairing with the rank-zero divisor source.

Thus neither large correction block is categorically decoupled from `mathscr F_0` at Euler level. This is necessary for a non-split Schurization, although it does not by itself locate the required even-degree gluing morphisms.

---

## 8. What is and is not closed

The new exact state is:

```text
scale-one twisted perfect source class       DONE
nine-term arbitrary divisor witness          superseded for Schur search
bar Q two triple-product decomposition       DONE
all six divisors principal nondegenerate     DONE
all six line-bundle indices                  2 exactly
six canonical two-cell factors C_i           DONE
C_i Schur / FM ideal-point model             DONE
Ext(C_i,C_i)                                  (1,8,12,8,1)
two actual correction blocks K_A,K_B         DONE
balanced Euler coupling to divisor source    -5, -5
Schur property of K_A,K_B                     OPEN
non-split Schur source with ch=bar delta      OPEN
exact r_H                                     OPEN
r_H <= 30                                    OPEN
```

The next useful calculation is no longer a lattice search. It is the dg endomorphism/cross-Ext calculation for

\[
\mathscr F_0,
\quad
\mathscr M\otimes K_A,
\quad
\mathscr M\otimes K_B,
\quad
\mathscr M\otimes\mathcal O_p[1].
\]

A successful connected twisted complex built from these cells would have exactly the required Chern character `bar delta`. Its Schur property and `Ext^1` dimension can then be checked by finite linear algebra.

---

## 9. Reproduction

The companion verifier

```text
notes/HODGE-TATE-CM5-W2J-A-SCHUR-BLOCKS-VERIFY.py
```

reconstructs the quotient NS lattice, checks the six `S_i`, and reproduces exactly:

```text
Pf(S_i)                              1 for all six
index(S_i)                           2 for all six
bar Q = S1 S2 S3 + S4 S5 S6         PASS
Lbar.Q_A                             5
Lbar.Q_B                             5
Koszul top(Q_A)                      +4
Koszul top(Q_B)                      -6
base block top after 3 shifted pts   -5
root-gerbe top correction            +5
final ch(T_blk)                      bar Q
```

All lattice, sign, and intersection calculations are exact.

---

## 10. Verdict

W2J-A does not yet close semiregularity, but it removes most of the arbitrariness from the source correction. The scale-one correction is now built from six canonical Schur cells, each Fourier-Mukai equivalent to an ideal point, grouped into only two balanced correction blocks.

The next gate is the finite dg gluing calculation for these blocks.