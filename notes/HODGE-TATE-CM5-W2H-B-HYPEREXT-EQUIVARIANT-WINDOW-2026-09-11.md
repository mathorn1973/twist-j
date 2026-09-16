# Hodge-Tate CM5: W2H-B hyper-Ext obstruction and equivariant window

**STATUS: NON-CANONICAL RESEARCH NOTE.**

**Basis:** Public Canon v84 and the companion Hodge-Tate / Markman / Perry CM5 notes through
`HODGE-TATE-CM5-W2H-NONDECOMPOSABLE-POSTNIKOV-OUTER-2026-09-11.md`.

**Date:** 2026-09-11.

This note continues **Gate W2H-B**. W2H constructed a genuinely non-external Postnikov representative

\[
R:=P_{\mu,\nu}=\operatorname{Fib}\bigl(P^{\oplus 2}\xrightarrow{(\mu,\nu)}P[2]\bigr),
\qquad
P=G_1\boxtimes G_1^\vee,
\]

with exactly the same `K_0` class, Chern character, normalized Markman class, and nonzero Hodge-Weil projection as the original decomposable outer object.

The present note computes a representation-independent lower bound for

\[
\operatorname{Ext}^2(R,R)
\]

from the hyper-Ext spectral sequence. The result is negative for **ordinary semiregularity**, and in fact for every minimal two-cell same-`K`-class Postnikov construction `Fib(P^2 -> P[2k])` on this source. The same calculation then reveals a real equivariant window at order 80: the previous dimension obstruction disappears after taking an `H x H` invariant part, provided the invariant source deformation dimension is at most 30.

This is not an algebraicity theorem. It does not yet construct the required `H`-equivariant source sheaf, nor prove equivariant semiregularity. It isolates the next exact gate.

No `canon/` or registry file is changed.

---

## 1. Source Ext dimensions

Let

\[
r:=\dim \operatorname{Ext}^1_X(G_1,G_1).
\]

W2E-B proved

\[
\boxed{r\ge 399.}
\]

For the scale-one source class,

\[
\chi(G_1,G_1)=800.
\]

Because `G_1` is simple on the abelian fourfold `X`, Serre duality gives

\[
e_0=e_4=1,
\qquad
e_3=e_1=r.
\]

Writing

\[
e_2=s,
\]

Riemann-Roch gives

\[
2-2r+s=800,
\]

hence

\[
\boxed{s=798+2r.}
\]

Thus the source self-Ext dimension vector is

\[
\boxed{(1,r,798+2r,r,1).}
\]

---

## 2. Ext dimensions of the product cell P

Put

\[
A^i:=\operatorname{Ext}^i_Z(P,P),
\qquad
a_i:=\dim A^i,
\qquad Z=X\times X.
\]

Kunneth gives the convolution of the source Ext vector with itself. In the low degrees needed below,

\[
\boxed{a_0=1,}
\]

\[
\boxed{a_1=2r,}
\]

\[
\boxed{a_2=r^2+2s=r^2+4r+1596,}
\]

and

\[
\boxed{
 a_3=2r+2rs=2r(1+s)=2r(799+2r).
}
\]

Since `Z` is an abelian eightfold,

\[
a_{8-i}=a_i.
\]

In particular

\[
a_6=a_2,
\qquad a_8=a_0=1.
\]

At the minimal allowed value `r=399`,

\[
\boxed{a_1=798,}
\]

\[
\boxed{a_2=162393,}
\]

\[
\boxed{a_3=1274406.}
\]

---

## 3. Hyper-Ext spectral sequence for the W2H object

For

\[
R=P_{\mu,\nu},
\]

W2H proved

\[
\mathcal H^{-1}(R)=P,
\qquad
\mathcal H^0(R)=P^{\oplus2}.
\]

Use the standard hyper-Ext spectral sequence

\[
E_2^{p,q}
=
\bigoplus_i
\operatorname{Ext}^p(\mathcal H^i(R),\mathcal H^{i+q}(R))
\Longrightarrow
\operatorname{Ext}^{p+q}(R,R),
\]

with

\[
d_m:E_m^{p,q}\to E_m^{p+m,q-m+1}.
\]

There are only three rows, `q=-1,0,1`.

The lower-row total-degree-two term is

\[
E_2^{3,-1}
=\operatorname{Ext}^3(P^{\oplus2},P)
\cong (A^3)^{\oplus2},
\]

of dimension

\[
2a_3.
\]

Only two differentials can hit it:

1. `d_2` from
   \[
   E_2^{1,0}
   =A^1\oplus M_2(A^1),
   \]
   whose dimension is `5a_1`;
2. `d_3` from
   \[
   E_3^{0,1}\subset E_2^{0,1}
   =\operatorname{Hom}(P,P^2),
   \]
   whose dimension is at most `2a_0=2`.

There are no further incoming or outgoing differentials for this lower-row position. Therefore, independently of the multiplication table of `RHom(P,P)` and independently of the choice of `mu,nu`,

\[
\boxed{
\dim\operatorname{Ext}^2(R,R)
\ge 2a_3-5a_1-2.
}
\]

Substituting the formulas above,

\[
\boxed{
\dim\operatorname{Ext}^2(R,R)
\ge
8r^2+3186r-2.
}
\]

At `r=399`,

\[
\boxed{
\dim\operatorname{Ext}^2(R,R)
\ge 2544820.
}
\]

The ordinary degree-two semiregularity target on an abelian eightfold has dimension

\[
\dim HH_{-2}=8008.
\]

Hence

\[
\boxed{
R\text{ cannot be ordinarily semiregular.}
}
\]

This is a dimension obstruction for the new non-external object. It is different from W2G-B: it does not use a factorwise class `xi box id`.

---

## 4. The whole minimal two-cell same-K-class lane is ordinarily impossible

The previous construction is the first member of the natural family

\[
R_k
:=
\operatorname{Fib}\bigl(P^{\oplus2}\to P[2k]\bigr),
\qquad k=1,2,3,4.
\]

Because the shift is even,

\[
[R_k]=2[P]-[P[2k]]=[P].
\]

Put

\[
d:=2k-1.
\]

Then

\[
\mathcal H^{-d}(R_k)=P,
\qquad
\mathcal H^0(R_k)=P^2.
\]

The hyper-Ext spectral sequence has rows `q=-d,0,d`.

### k=1, d=1

This is W2H. Section 3 gives

\[
\dim\operatorname{Ext}^2(R_1,R_1)
\ge2544820.
\]

### k=2, d=3

The central total-degree-two term has dimension

\[
5a_2.
\]

Its only possible outgoing differential to the lower row is

\[
d_4:E_4^{2,0}\to E_4^{6,-3},
\]

whose target has dimension at most

\[
2a_6=2a_2.
\]

There is no incoming differential to the central term. Thus

\[
\boxed{
\dim\operatorname{Ext}^2(R_2,R_2)
\ge3a_2
\ge487179.
}
\]

### k=3, d=5

The only possible outgoing differential from the central term is

\[
d_6:E_6^{2,0}\to E_6^{8,-5},
\]

with target dimension

\[
2a_8=2.
\]

Hence

\[
\boxed{
\dim\operatorname{Ext}^2(R_3,R_3)
\ge5a_2-2
\ge811963.
}
\]

### k=4, d=7

The corresponding target would require `A^10`, which vanishes on the eightfold. Therefore the central term survives entirely:

\[
\boxed{
\dim\operatorname{Ext}^2(R_4,R_4)
\ge5a_2
\ge811965.
}
\]

Moreover `Ext^8(P,P)` is one-dimensional, so this last shift does not even supply two independent `k`-invariants of the type used to prove indecomposability in W2H.

Thus

\[
\boxed{
\text{every minimal two-cell same-K-class Postnikov construction }
P^2\to P[2k]
\text{ is ordinarily non-semiregular.}
}
\]

This closes the ordinary two-cell lane.

---

## 5. Why the equivariant lane is different

The previous bounds use the full Ext algebra. Perry's weak/equivariant theory asks instead for an equivariant lift and the invariant obstruction space.

W2E-A found many order-80 theta subgroups compatible with the correction class `Q`. For such an `H`, if an honest `H`-equivariant scale-one source object is realized, put

\[
r_H:=\dim\operatorname{Ext}^1(G_1,G_1)^H.
\]

W2E-A gives the exact lower bound

\[
\boxed{r_H\ge12}
\]

at `|H|=80`.

The invariant self-Euler characteristic is

\[
\chi(G_1,G_1)^H=\frac{800}{80}=10.
\]

For a simple equivariant source object, Serre duality gives

\[
(e_0^H,e_1^H,e_2^H,e_3^H,e_4^H)
=(1,r_H,8+2r_H,r_H,1).
\]

Now take the factorwise outer group

\[
\Gamma:=H\times H.
\]

For the product cell `P`, invariants factor:

\[
\operatorname{Ext}^n(P,P)^\Gamma
=
\bigoplus_{i+j=n}
\operatorname{Ext}^i(G_1,G_1)^H
\otimes
\operatorname{Ext}^j(G_1^\vee,G_1^\vee)^H.
\]

Writing `a_i^Gamma` for their dimensions,

\[
\boxed{a_1^\Gamma=2r_H,}
\]

\[
\boxed{a_2^\Gamma=r_H^2+16+4r_H,}
\]

and

\[
\boxed{
 a_3^\Gamma
 =2r_H(9+2r_H).
}
\]

If the mixed Postnikov plane

\[
\langle\mu,\nu\rangle
\subset
\operatorname{Ext}^1(G_1,G_1)^H
\otimes
\operatorname{Ext}^1(G_1^\vee,G_1^\vee)^H
\]

is chosen `Gamma`-invariant, the same spectral-sequence estimate applies inside the invariant category:

\[
\boxed{
\dim\operatorname{Ext}^2(R,R)^\Gamma
\ge
8r_H^2+26r_H-2.
}
\]

At the minimum `r_H=12`,

\[
\boxed{
\dim\operatorname{Ext}^2(R,R)^\Gamma
\ge1462,
}
\]

which is **below** the eightfold target dimension `8008`.

The lower bound remains at most `8008` exactly for

\[
\boxed{12\le r_H\le30.}
\]

At `r_H=31` it becomes `8492`.

This is the first lane in the CM5 programme where all previously known necessary dimension tests can overlap.

Furthermore the invariant mixed space has dimension

\[
\boxed{r_H^2\ge144,}
\]

so there is no shortage of two independent invariant mixed classes `mu,nu` once the equivariant source object exists.

---

## 6. A product-compatible order-80 census

The W2E verifier found 85 two-primary maximal isotropic subgroups for which `Q` descends integrally. The two-primary vector space splits according to the two abelian-surface factors,

\[
\mathbf F_2^8=V_A\oplus V_B,
\qquad \dim V_A=\dim V_B=4.
\]

Call a passing four-plane **factorized** if

\[
H_2=(H_{2,A}\subset V_A)\oplus(H_{2,B}\subset V_B),
\]

with both factors two-dimensional.

Exact enumeration gives

\[
\boxed{
25\text{ of the }85
\text{ passing two-primary Lagrangians are factorized.}
}
\]

The five-primary kernel likewise splits into two two-dimensional factors. A one-dimensional five-primary line lying wholly in one factor has

\[
\frac{5^2-1}{5-1}=6
\]

possibilities. It may lie in either factor, giving `12` factor-supported lines.

Therefore there are

\[
\boxed{
25\cdot12=300
}
\]

explicit cohomologically admissible order-80 theta subgroups with product form

\[
\boxed{H=H_A\times H_B,}
\]

of orders

\[
(|H_A|,|H_B|)=(20,4)
\quad\text{or}\quad(4,20).
\]

These are particularly useful because the quotient remains a product of two abelian surfaces and the factorwise outer group `Gamma=H x H` is explicit.

This census is finite and exact. The companion verifier reproduces the number `25` and hence `300` from the accepted W2E audit.

---

## 7. What is proved and what is still missing

The present gate gives two firm conclusions.

First,

\[
\boxed{
\text{ordinary semiregularity of the W2H Postnikov object is impossible.}
}
\]

This remains true for every minimal two-cell same-`K`-class shift `P^2 -> P[2k]`.

Second, the equivariant route is **not** killed by the same dimension argument. For an order-80 source symmetry,

\[
12\le r_H\le30
\]

is a genuine open window, and the invariant mixed space is automatically large enough to choose a non-external Postnikov plane.

What is not yet proved is equally important. The W2E descent audit established integral cohomological descent of `Q` for the 300 factorized candidates, but did not construct a specific scale-one coherent/perfect source representative carrying the required honest `H`-equivariant structure. Nor has it computed the exact value of `r_H`.

Therefore the next gate is:

### W2I: factorized order-80 equivariant source realization

For one explicit factorized subgroup `H=H_A x H_B` from the 300 candidates:

1. construct an honest `H`-equivariant scale-one source perfect/coherent object with Chern character `delta`;
2. descend it to `X/H` and compute
   \[
   r_H=\dim\operatorname{Ext}^1(G_1,G_1)^H;
   \]
3. require
   \[
   r_H\le30;
   \]
4. choose two independent invariant mixed classes
   \[
   \mu,\nu\in(E_1^H\otimes E_1^{\vee,H});
   \]
5. compute the invariant hyper-Ext differential and the equivariant semiregularity map of the resulting non-external Postnikov object.

This is now a concrete quotient-geometric problem, not another unrestricted search over secant classes or derived objects.

---

## 8. Reproduction

The companion verifier

```text
notes/HODGE-TATE-CM5-W2H-B-HYPEREXT-VERIFY.py
```

reuses the exact W2E theta audit and reproduces:

```text
passing 2-primary Lagrangians      85
factorized passing Lagrangians     25
factor-supported 5-lines           12
factorized order-80 candidates    300
ordinary k=1 lower bound      2544820
ordinary k=2 lower bound       487179
ordinary k=3 lower bound       811963
ordinary k=4 lower bound       811965
equivariant r_H=12 lower bound    1462
equivariant r_H=30 lower bound    7978
equivariant r_H=31 lower bound    8492
```

All calculations are exact integer arithmetic.

---

## 9. Verdict

W2H-B splits cleanly:

```text
non-external same-K-class representative       DONE (W2H)
ordinary semiregularity of that representative FAIL
ordinary minimal two-cell Postnikov lane       FAIL
order-80 factorized theta candidates           300 exact
invariant mixed Postnikov data                  dimensionally available
equivariant semiregularity dimension window    OPEN for 12 <= r_H <= 30
honest H-equivariant source representative      OPEN
exact r_H                                      OPEN
```

The useful next move is W2I on one explicit factorized order-80 quotient.