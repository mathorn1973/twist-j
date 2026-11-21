# First-order Hodge / trace-kernel bridge

**NON-CANONICAL, candidate-T argument at L1; exact locally audited only.** All symbols and hypotheses in this file are fixed to the marked A4 construction of the public `A4-RAMIFIED-HODGE-TRACEKERNEL` and `J-HODGE-HERM2-LOXODROME` mathematical claims. This text is not a formal pre-registered proof and not a Canon theorem.

## 1. Carrier and the exact first-order identity

Take the marked integral A4 root module `V` with basis `(e_i - e_0)_(i=1..4)`, Gram `H=I_4+11^T` and determinant 5. Let `B=Lambda^2 V` with ordered basis `(01,02,03,12,13,23)`. Denote the **unimodular**, orientation-dependent symmetric wedge pairing on `B` by `beta`, and the positive induced Gram by `G_2`. In these bases `beta^2=I_6`, and the scaled Hodge operator

```
K = beta G_2      satisfies     K^2 = 5 I_6.
```

Let `s=sqrt(5)` and `F=Q(s)`. The two rank-three Hodge eigenspaces are the images of `(K+eta*s I)` for `eta=+1,-1`. Expanding and using `K^T beta=beta K=G_2`, `K^T beta K=5 beta` gives the exact **six-by-six** identity

```
(K+eta*s I)^T beta (K+eta*s I)
    = eta*2*s*(G_2 + eta*s*beta).
```

Hence the normalized bilinear form on a chosen generator set of the eta eigenspace is

```
(1/s)*(K+eta*s I)^T beta (K+eta*s I)
    = eta*2*G_2 + 2*s*beta.
```

This must be read over the real quadratic field F and its ramified prime `(s)`. It is not division by a uniformizer of the full cyclotomic extension `Q(zeta_5)`; there `(s)` has valuation two at the prime over 5.

## 2. The marked three-space and the exact scalar

Reducing `K` modulo 5 gives `Kbar^2=0`, rank 3 and `im Kbar=ker Kbar=ell wedge Vbar`, with `ell=(1,1,1,1)`. The marked root Gram induces an isometry

```
Vbar/<ell>  --> W_5 = ker(sum:F_5^4 -> F_5),
```

where the Gram of `g_5` in the difference basis `b1=(1,-1,0,0)`, `b2=(0,1,-1,0)`, `b3=(0,0,1,-1)` is

```
B_5 = [[2,4,0], [4,2,4], [0,4,2]],  det(B_5)=4  in F_5.
```

Choose three source basis columns whose `Kbar`-images are independent. Map them through `ell wedge Vbar` and the preceding marked quotient isometry, using no fitted coordinate transform. This gives the exact reduction of the first-order forms

```
h_plus  =  3 g_5,                h_minus  = -3 g_5.          (F_5)
```

In the frozen marking the coefficient is `3 = 2 det(B_5) = 8 (mod 5)`. Two is a consequence of the projector identity `(K+sI)=2s P_+`; the determinant four comes from the marked metric-volume geometry already specified in the trace-kernel bridge. The independently reconstructed matrices in `verify.py` check the entire identity rather than inserting the output as an assumption.

This is a **similarity** for uniformizer `s`, not an `F_5`-isometry: `det(g_5)=4` is a square, while `det(3g_5)=3` is a nonsquare. Since `-1=2^2` in F_5, the `+` and `-` residual forms are mutually isometric. Reversing the marked 4D orientation exchanges the eigenspaces and wedge sign; the induced normalized scalar stays in the same marked class. Changing the wedge pairing itself to `beta/2` destroys unimodularity over Z and changes the square class: the statement is not rescaling-independent.

## 3. Uniformizer units and definite-real-place parity

The full unit group of `O_F=Z[phi]` is `+/- phi^Z` with `phi=(1+s)/2`, `phi^2=phi+1` and `N(phi)=-1`. Each generator of the ramified real-field prime has form

```
pi = u*s,    u=epsilon*phi^n,    epsilon in {+1,-1}, n in Z.
```

Its residual scalar relative to `g_5` is

```
s(pi) = 3*(s/pi) mod s
      = 3*(u mod s)^(-1)
      = epsilon*3^(1-n) (mod 5).
```

Here `phi mod s=1/2=3` in F_5. Conjugation acts trivially on the residue field, so for any unit `u`, with the second real embedding denoted by a prime,

```
u' = u (mod s),          (u mod s)^2 = N(u) (mod 5).
```

Since `N(u)=(-1)^n`, the permitted residues are `u mod s in {+/-1}` for even n and `{+/-2}` for odd n. Therefore `s(pi)` is a nonsquare iff n is even. For odd n it is a square, and an A5-equivariant isometry can be achieved by scaling the fixed comparison by the corresponding field scalar.

The normalized `beta/s` form on the marked plus Hodge lattice is **positive definite at each of the two real embeddings** (its conjugate plus lattice is the minus Hodge lattice, with the wedge sign also reversed). Under `beta/(u*s)`, each real-embedded form is still **definite**, and its sign is the sign of the corresponding embedding of `u` (or its reciprocal). The signs at the two real places agree iff `N(u)=+1` iff n is even, while an isometric residual normalization is possible iff `N(u)=-1` iff n is odd.

Thus the fixed unit group gives a genuine tradeoff between **residual isometry** and **same-sign real definiteness**. A different use of the word “indefinite” at one place is false.

## 4. A5-equivariance and negative controls

In the selected finite-field representation, the simultaneous centralizer of the marked five-cycle and three-cycle generators of `A5` is exactly

```
End_A5(W_5) = F_5 I_3.
```

Any A5-equivariant comparison differs by a scalar, changing its Gram by a square. This makes the nonsquare square-class result under fixed `beta` and uniformizer `s` invariant under allowed identification changes.

The marked exterior-square `L=Lambda^2 M_J` acts on the reduced common three-space. Its induced action `D` is **twice** the quotient action of `M_J` on `Vbar/<ell>` because `M_J ell = 2 ell (mod 5)`. Dropping this factor changes the operator. Direct exact linear-constraint elimination finds a one-dimensional family of A5-fixed symmetric forms and **zero** nonzero forms fixed by both A5 and `D`. This excludes the fixed-metric equivariant shortcut within the marked class; it does not settle the complete L2 spatial-commutator admissibility problem.

Independently, for every odd prime p,

```
Phi_p(1+p*t) = sum_(k=0)^(p-1) (1+p*t)^k = p (mod p^2).
```

So the characteristic polynomial `Phi_p(X-1)` has no root lifting `X=2` modulo `p^2`. A rank-one free invariant summand or quotient of the corresponding integral cyclotomic step would require such a root. This obstruction is a general ramification statement, **not** a new fifth-prime selector. The check for p=3,5,7,11,13 in the script is illustrative; the binomial argument proves the all-odd-prime identity.

## 5. Exact boundaries

The original supplied reviewer also reported that the Lorentz restriction on a suitably saturated `E_J` lattice reduces with rank 2 and rotation-plane radical, and that the full group generated by the marked `A5` and `D` has 744000 elements. Those additional scopes are not newly fully checked by this note's accepted `verify.py`; no promotion is claimed for them. They are retained as reported context in `REVIEW.md`.

The original native `U`, physical spacetime, physical time, spatial curvature forcing, decoder completeness, probability and L1-to-L2 lift remain open and are not assumed. `TRACEKERNEL-CURVATURE-FORCING [O]` is unchanged.
