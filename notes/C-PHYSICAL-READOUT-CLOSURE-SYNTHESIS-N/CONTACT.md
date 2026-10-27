# Conditional charge contacts and energy-profile selection

**NON-CANONICAL. Conditional candidate-T at L1.** This is a self-contained
exact proof on a selected integer cell. It proposes new contact rules; it
does not promote them to the Canon, derive them from native `U` or `J`, or
identify a physical energy, apparatus, unit, or measured response. No
scientific program, formal gate, or reproduction is claimed here.

The starting carrier, quadratic forms, split, and reaction `G` are the
mathematical definitions used by FIELD-CONSERVATIVE-CHAIN-LAW and
FIELD-LOCAL-WORK-RECORD in [Public Canon v100](../../canon/CANON.md).
They are restated so that the new contact results can be checked without
executing a verifier. All equality below means literal equality of the
complete ordered state.

## 1. Complete cell and the selected positive energy

A cell is

```text
s=(m,b,E,M,r),
m=(m0,m1,m2), b=(b0,b1,b2), mj,bj in Z^4,
E in Z^4, M in Z^2, r in N_0.
```

All three reacting registers `mj` reside at electric vertex 0. Register
`bj` resides at vertex `j`. The four ordered edges are
`(0->1,0->1,0->2,2->1)`; the first two are distinct. Put

```text
C=[[1,-1],[-1,0],[0,1],[0,1]],
D=[[1,1,1,0],[-1,-1,0,-1],[0,0,-1,1]],
K=[[6,2,-1,2],[2,6,2,-1],[-1,2,6,2],[2,-1,2,6]],
Q(v)=v^t K v, chi(v)=sum_i v_i,
Hraw(E,M)=E^t E+M^t M+E^t C M,
H1(s)=sum_j Q(mj)+sum_j Q(bj)+Hraw(E,M)+r,
rho(s)=(chi(b0)+sum_j chi(mj),chi(b1),chi(b2)),
delta(s)=DE-rho(s).
```

Thus `DC=0`. The eigenvalues of `K` are `9,1,7,7`, so
`Q(v)>=||v||^2`. Direct expansion gives

```text
4Hraw(E,M)=||2E+CM||^2+M0^2+(M0+M1)^2.
```

Consequently `Q` and `Hraw` are positive definite integer forms on their
integer carriers. The Gauss subset is `delta=0`; the complete carrier also
retains every non-Gauss state and every raw field outside the split below.

For a real profile parameter `c`, define

```text
pi(r)=r mod2 in {0,1},
f_c(r)=r+(c-1)pi(r),
Hc(s)=H1(s)+(c-1)pi(r).
```

Here `f_c(2k)=2k` and `f_c(2k+1)=2k+c`. Nonnegativity on the full
stock domain is equivalent to `c>=0`; the resource has zero cost only at
zero iff `c>0`. An integer-valued profile additionally requires integer
`c`. This is a declared family, not the class of all possible invariant
energies. If one assumes `f(0)=0` and `f(r+2)-f(r)=2` for every
`r>=0`, this is exactly the resulting one-parameter resource family.

Additional cells and neutral integer stocks can be retained unchanged.
Their chosen costs are added to the total account; none is an erased
reservoir or an electric charge current in the results below.

## 2. Exact split, image admission, and reaction

For `y=(a,b,c,d)` and `sigma=(u,w)`, let

```text
P(a,b,c,d)=(a-b,-a,b,b,c,d),
S(u,w)=(u,u,w,u-w,0,0),
Bf=[[4,-2,2,-1],[-2,6,-1,3],[2,-1,2,0],[-1,3,0,2]],
H(y)=y^t Bf y/2
    =2a^2-2ab+3b^2+c^2+d^2+2ac-ad-bc+3bd,
L=[[1,-3,-1,-2],[-3,4,-2,1],[0,5,1,2],[5,-5,2,-1]],
Vinv=[[1,2,1,2],[2,-1,2,-1],[0,-5,1,-3],[-5,5,-3,4]].
```

The unique rational split `(E,M)=Py+S sigma` is

```text
a=(2E0-3E1+E2+E3)/5,
b=(-E0-E1+2E2+2E3)/5,
c=M0, d=M1,
u=(2E0+2E1+E2+E3)/5,
w=(E0+E1+3E2-2E3)/5.
```

Writing `g(E)=2E0-3E1+E2+E3`, the four electric numerators are
`g,2g,g,3g` modulo five. The split is therefore integral iff `g=0 mod5`.
The following identities follow by multiplication or substitution:

```text
DP_E=0, C^t S_E=0,
DS_E(u,w)=(2u+w,-3u+w,u-2w),
Hraw(Py+S sigma)=H(y)+Hstatic(sigma),
Hstatic(u,w)=3u^2-2uw+2w^2,
Vinv L=L Vinv=5I, det L=25, L^t Bf L=5Bf.
```

`H` is positive definite because `P` is injective and `H(y)=Hraw(Py)`.
It is integer-valued. In particular `H(Lx)=5H(x)`. Moreover

```text
y=(a,b,c,d) in L Z^4
iff a+2b=0 mod5 and c+2d=0 mod5,
x=Vinv y/5 on that image.
```

For completeness, the four entries of `Vinv y` modulo five are
`p+q,2(p+q),q,2q`, where `p=a+2b` and `q=c+2d`.
Thus the displayed congruences are equivalent to integrality of `x`;
`L Vinv=5I` supplies sufficiency.

The literal ordered matter endpoints are

```text
R=((1,-2,1,0),0,0),
AM=((1,0,0,0),(0,-1,0,0),(0,-1,1,0)).
```

Their energies are `18` and `20`. Their complete vector sums coincide,
and both total charges are zero. A permutation of these registers is a
different state unless it literally equals the displayed endpoint.

Define `G` on every complete input as follows. Matter other than literal
`R` or `AM`, a nonintegral split, or a failed stated admission or funding
test gives identity on the entire input. On `R`, require `y in L Z^4`,
set `x=Vinv y/5`, and require `r+4H(x)-2>=0`. On `AM`, set `x=y`
and require `r+2-4H(x)>=0`. The accepted rules are

```text
G(R,b,PLx+S sigma,r)=(AM,b,Px+S sigma,r+4H(x)-2),
G(AM,b,Px+S sigma,r)=(R,b,PLx+S sigma,r+2-4H(x)).
```

These are disjoint transpositions. Each accepted output has the funded
inverse, and rejected inputs cannot be accepted outputs. Hence `G^2=I`
on the complete carrier. The identity

```text
18+5H(x)+Hstatic(sigma)+r
 =20+H(x)+Hstatic(sigma)+r+4H(x)-2
```

with all unchanged register costs added proves conservation of `H1`.
The stock change is even, so `G` preserves every `Hc`. It also separately
preserves `rho`, `DE`, and `delta`. These statements include occupied
stocks and rejected or non-Gauss states.

## 3. Gauss admission and the limitation on unit transport

There is an exact identity

```text
g(E)=(DE)_0-(DE)_1-5E1.
```

On the Gauss subset, an integral split therefore requires
`rho0-rho1=0 mod5`. A transfer of charge `q` from vertex 0 to vertex 1
changes this difference by `-2q`. Both endpoints can remain in the split
lattice only if `q=0 mod5`. In particular a unit transfer cannot have
both endpoints there. This restriction concerns the selected split
lattice; it does not exclude unit transfer on the complete raw carrier.

On a Gauss state with matter `R` or `AM`, put

```text
nu=chi(b0)-chi(b1).
```

Since the reacting matter has total charge zero and `DP_E=0`, the
integral static coordinate satisfies

```text
nu=rho0-rho1=5u.
```

These contacts move multiples of five in this admitted sector. They do
not establish elementary unit-charge motion within it.

## 4. Fixed paths, complete funded raw contacts, and parity

Let `e0=(1,0,0,0)` and `gamma=(0,0,1,1)`. Solving `Dt=0` over the
integers gives `t3=t2`, `t0=-t1-t2`, and
`t=C(-t1,t2)`. Thus

```text
ker_Z D=C Z^2,
Dh=De0 iff h=e0+Cz=(1+z0-z1,-z0,z1,z1).
```

For one fixed such path, the raw proposal swaps the complete occupied
registers `b0,b1`, sets `E'=E-nu h`, leaves `M` and all `mj` unchanged,
and adjusts the stock by

```text
kappa_h=Hraw(E-nu h,M)-Hraw(E,M)
       =nu^2||h||^2-nu(2E.h+h^t C M),
r'=r-kappa_h.
```

Commit every proposed change iff `r'>=0`; otherwise retain the entire
input. This defines a complete raw contact `V_h^raw`. The swap gives
`nu'=-nu` and the field formula gives `kappa_h'=-kappa_h`. Every
committed output consequently has its funded inverse; blocked states are
fixed and cannot be committed outputs. Therefore `(V_h^raw)^2=I`.
The sum of the two matter costs is unchanged, so this gate preserves
`H1`. The charge change is `(-nu,nu,0)` and equals `D(E'-E)`; hence
it preserves the exact Gauss defect, including outside the Gauss subset.

The two paths of interest give

```text
kappa_e0=nu^2-nu(2E0+M0-M1),
kappa_gamma=2nu(nu-E2-E3-M1).
```

The latter is always even. The former is odd exactly when `nu` is odd
and `M0+M1` is even. More generally, a fixed path has an even price for
every integer `nu,E,M` iff

```text
h=gamma mod2,
equivalently z0=0 mod2 and z1=1 mod2,
equivalently h=gamma+2Cw for some w in Z^2.
```

Indeed, modulo two the price is
`nu(||h||^2+h^t CM)`. Universality requires an even squared norm and
both entries of `h^t C` even. Substituting the displayed path gives

```text
||h||^2=1+z1 mod2,
h^t C=(1+z1,1+z0+z1) mod2,
```

which proves both directions. If the preparation is restricted to
`M=0`, only odd `z1` is required; the stronger classification must not
be asserted on that smaller context.

The classification concerns fixed updates `-nu h` with `M` unchanged.
General Gauss-compatible flux changes can add arbitrary `Ck`, including
ones not divisible by `nu`, or can change `M`. They are outside this
fixed-path class.

The stock adjustment here is explicitly defined using the selected field
price. Conservation of `H1` is consequently a construction theorem,
not an independent physical derivation of that price or funding law.

## 5. Stability of the accepted Gauss-R sector

Let `A_R` consist exactly of the Gauss inputs with literal matter `R`
whose split, image, and funding tests for `G` all pass. Write their active
field as `y=Lx`, set `epsilon=H(x)`, and retain `sigma=(u,w)`.

For a proposed fixed-path contact on this sector, `nu=5u`. The exact
split changes are

```text
sigma'=(-u,w-u),
Delta y=u(-2-5z0,1-5z1,0,0).
```

The change of `a+2b` is `-5u(z0+2z1)` and that of `c+2d` is zero.
Thus the image congruences survive. Also
`Hstatic(-u,w-u)=Hstatic(u,w)`. In particular

```text
direct e0: Delta y=u(-2,1,0,0), Delta x=u(0,-1,-1,3),
alternative gamma: Delta y=u(-2,-4,0,0),
                   Delta x=u(-2,0,4,-2).
```

The stock update and static identity imply

```text
kappa_h=5[H(x')-H(x)],
r'+5H(x')=r+5H(x).
```

On `r>=0`, `epsilon in N_0`, the R funding test is equivalent to
`r+5epsilon>=2`: if `epsilon=0` both require `r>=2`; if
`epsilon>=1` both hold. Thus every funded contact output remains in
`A_R`. Every blocked input remains there unchanged. This proves
invariance of the entire accepted sector, not just one successful state.
Every positive field price on it is at least five. Section 8 attains five.

The always-even path classification remains exact on `A_R`. For
necessity one can take `u=1`, `sigma=(1,3)`, and
`b=(5v,0,-5v)` with `v=(1,0,0,0)`. Image congruences modulo five
do not restrict the two magnetic parities: appropriate integer `y=Lx`
realizes every pair. An arbitrarily large stock funds the selected
event and passes the R test. Thus each path outside the classified
parity class has a funded odd-price witness in `A_R`.

## 6. Complete R/AM pairing and preserved reaction record

Define `V_h^R` by applying the funded contact only on `A_R`, and by
identity on its entire complement. Section 5 makes this a complete
involution. Let `A_AM=G(A_R)`. It is exactly the accepted Gauss AM
sector, is disjoint from `A_R`, and is interchanged with it by `G`.
Now define

```text
W_h=V_h^R (G V_h^R G), with rightmost factor first.
```

The first factor is supported in `A_R`, the second in `A_AM`.
Their supports are disjoint, so they commute and

```text
W_h^2=I, G W_h G=W_h.
```

This is a full gate: it applies `V_h^R` on `A_R`, the conjugate rule on
`A_AM`, and identity on every remaining state, including all non-Gauss,
nonintegrally split, image-rejected R, funding-rejected, and other-matter
inputs. AM admission has no separate L-image requirement.
No rejected state or occupied content is omitted or reset. It preserves
`H1` and the exact Gauss defect. It changes actual node charges on its
charged branch; these are not invariants of the new law.

The two completed gates used below are `W_d=W_e0` and
`W_a=W_gamma`. Both commute with `G` on the entire carrier.

For the existing reaction event put

```text
e(s)=1 iff matter(s)=R and matter(Gs)=AM, otherwise 0,
Ghat(s,p)=(Gs,p+e(s) mod5), p in C5.
```

Its complete inverse is `(s',p')->(Gs',p'-e(Gs') mod5)`, including
occupied pointers and rejected branches.

`W_h` retains each matter endpoint and its acceptance status, so
`e(W_h s)=e(s)`. Extending `W_h` by identity on every old pointer
value yields `W_h Ghat=Ghat W_h`. The pointer's chosen constant energy
`1` and neutrality leave all accounts unchanged. This proves compatibility
with the specified reaction record; it does not turn that record into a
measurement of the contact work.

## 7. Why the uniform AM rule fails; conjugate-branch limits

The identical raw rule on both matter endpoints need not preserve AM
acceptance and does not generally commute with `G`. Here is an exact
counterexample. Let `v=(1,0,0,0)` and take

```text
matter AM, b=(5v,0,-5v),
E=S_E(1,3)=(1,1,3,-2), M=(0,0), r=15.
```

This is Gauss, has active `y=0`, `H(y)=0`, raw energy `15`, and total
matter energy `320`. Its `H1` is `350`, and `G` accepts with guard
`r+2=17`. The raw direct contact has `nu=5`, price `15`, and output

```text
E'=(-4,1,3,-2), M'=(0,0), r'=0,
y'=(-2,1,0,0), H(y')=15, Hraw'=30.
```

The total remains `350`, but the AM guard is now `2-60<0` and `G`
rejects. In `G V_e0^raw` the matter therefore remains AM, whereas in
`V_e0^raw G` it is R with resource `2`. This proves noncommutation.
The accepted-sector conjugate in Section 6 is a different AM rule.

On an input in `A_AM` whose mirror R contact is funded, the direct conjugate
changes the raw field by

```text
Delta(E,M)=u(-1,-2,-2,-2;-1,3).
```

For the alternative path its change is

```text
Delta(E,M)=u(-4,0,-1,-1;4,-2).
```

To verify these formulas, apply `G` to obtain active R field `Lx`, use
the two `Delta x` and `Delta sigma` in Section 5, then form
`P Delta x+S Delta sigma`. The AM raw price is
`H(x')-H(x)=kappa_R/5`, and its stock decreases by that amount.
These formulas describe the accepted, funded conjugate branches. A
blocked mirror contact or an input outside `A_AM` is fixed by `W_h`;
the linear formula is not a global update on rejecting inputs.

## 8. One common charged input, two nonzero work values

Use the same complete preparation for both gates:

```text
matter R, b=(5v,0,-5v), v=(1,0,0,0),
E=(2,2,1,-4), M=(0,0), r=81.
```

It has `rho=DE=(5,0,-5)`, `nu=5`,
`sigma=(1,3)`, `Hstatic=15`,
`y=(-1,-2,0,0)=L(-1,0,2,-1)`, `H(x)=2`, and raw energy `25`.
The reacting cost is `18`; the two nonzero charged registers cost
`150+150=300`. Thus

```text
H1=18+300+25+81=424, Hc=423+c.
```

Both completed gates act here by their R rule and swap the entire
charged registers. Their outcomes are

| Quantity | Direct `W_d` | Alternative `W_a` |
|---|---:|---:|
| New electric field | `(-3,2,1,-4)` | `(2,2,-4,-9)` |
| New magnetic field | `(0,0)` | `(0,0)` |
| Field work | `5` | `80` |
| Raw field energy | `30` | `105` |
| Resource | `76` | `1` |
| `H(x')` | `3` | `18` |
| R guard `r'+4H(x')-2` | `86` | `71` |
| New `Hc` | `424` | `423+c` |

The alternative active vector is
`x'=(-3,0,6,-3)=3(-1,0,2,-1)`, giving `H(x')=18`.
Both have `sigma'=(-1,2)`, static cost `15`, and unchanged invariant
`r'+5H(x')=91`. Their node charges are `(0,5,-5)` and both remain
Gauss. Each has nonzero field work exactly opposite to its resource
change. The direct price attains the minimum positive price five in
the admitted R sector.

The example concerns `H1` without the optional constant-energy pointer;
including it adds one to every total. Neither pointer value nor any old
stock is used to finance an omitted term.

## 9. Exact selection statement and remaining premises

On a funded raw contact, or on the R branch of its completion,

```text
Hc(output)-Hc(input)
 =(c-1)[pi(r-kappa_h)-pi(r)].
```

Even prices leave every profile invariant; each odd-price event forces
`c=1` if the chosen contact is required to conserve a member of this
family. The conjugate AM branch has the same defect on its mirrored
R input because `G` preserves every `Hc`. Consequently the completed
direct gate selects `c=1` within this family, whereas the completed
alternative gate preserves every `Hc`. Section 8 exhibits the defects
`1-c` and `0` from one common input, with positive work in both cases.

Canonical pre/post processing cannot alter this all-state conclusion.
If `P0,Q0` are bijections preserving a given `Hc`, then

```text
Hc(P0 V Q0 s)-Hc(s)=Hc(V Q0 s)-Hc(Q0 s).
```

Surjectivity of `Q0` makes all-state conservation of `P0 V Q0`
equivalent to that of `V`. On a restricted preparation family this
necessity need not hold. The statement requires those maps to preserve
the tested profile, not merely `H1`.

The complete positive-energy account, Gauss compatibility, reaction
commutation, occupied-state inverse, and reaction-record compatibility
therefore do not select the direct path over the alternative path.
Requiring the direct path selects `c=1` only after adding that contact
law. The matrices, path, funding, sector restriction, and physical
identifications remain declared inputs. Funding was defined from the
selected price; it cannot itself serve as independent evidence for that
price. No uniqueness among all invariant energies is asserted.

Both new gates move charged content within one selected cell. They do not
derive native `U` or `J`, transport charge through the existing neutral
intercell resource channel, or supply a physical current or work record.
The original `G` and field-chain primitives preserve every actual node
charge, so these charged motions require a new primitive rather than a
word of those original gates. Here the energy exchange is field versus
explicit resource; the unchanged sum of quadratic matter costs is not
an independently derived kinetic or phase energy. Relative quantum
phase, photons, SI calibration, and measured physical acceptance remain
outside this conditional L1 result.
