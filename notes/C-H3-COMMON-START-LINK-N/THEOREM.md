# Common-start material obstruction and conditional receiver

NON-CANONICAL / NO AUTHORITY. L1. Claim #2143.

Status: conditional candidate-T for the statements proved in this file.
No new scientific code has been executed for this proof. The conditional
local discrimination count is algebra, not a count of successful apparatus
trajectories. Original-work preservation, actual readiness, native transfer
and the 32-tick retention gates remain separate finite questions.

The frozen experiment is PREREG.md at
`7f5a4b26a5816d0372149f42dcb539e76aab79a5`. The unchanged native law is
`reproduce/h3-referenced-record/verify.py` at public main
`6f2e112aafc4f3aca4222bb4bf3dced1d79fe2ed`, SHA256
`4553945d3bf32574ffd55de917859497e9644394f506aaf01ff9492adb8eeedd`.
The supplied original preparation is the predecessor's model.py, SHA256
`7b2f12553efe075e97a3814e68b6402690d1f66c389e1a6c45694aeccd91365d`.

The earlier amplitude and prepared-module interfaces are in
`notes/C-H3-NATIVE-READOUT-LINK-N/` at
`f9d8d0f27dbe839f140bde3e13189febad6b04be`. Its A_RESULT.md reports a
finite waiting-probe witness; its THEOREM.md separates that witness from
the later paid receiver assembly. Those are NON-CANONICAL premises. Their
failed gates and recorded source-freeze protocol deviation remain unchanged.
The proofs here do not infer a new successful prefix from that old witness.

## 1. Native law and the relevant ideal

Let `O=Z[j]`, with `1+j+j^2+j^3+j^4=0`, in its fraction field. Set

```text
rho=j^2, eta=1-rho, J=1+rho, Jinv=-j-j^2,
h(z)=z*conjugate(z), gamma=h(J).
```

J and rho are units. Direct multiplication gives `J*Jinv=1`, and

```text
gamma=2+rho+rho^-1,
gamma^2-3*gamma+1=0,
gamma^-1=3-gamma,
gamma^-2=8-3*gamma,
h(eta)=4-gamma,
J^2=gamma*rho.
```

Gamma is positive in both real embeddings and irrational. In particular
`gamma!=1`, so `gamma^2!=1` as well.

An admitted C pair has `a-b in 2O` and is updated by

```text
a'=a-eta*(a-b)/2,
b'=b+eta*(a-b)/2.
```

An odd difference refuses and leaves both slots unchanged. The inverse
uses rho inverse in place of rho. Each admitted pair preserves its sum
and Hermitian account, because its integral half-difference is multiplied
by the unit-modulus rho. The admitted output difference is rho times the
input difference, so the same domain is admitted by the inverse.

A B cell has material `(a,b)` and radiation `(g,r)`. It is idle if either
difference is odd. Otherwise its half-differences and centers are

```text
d=(a-b)/2, f=(g-r)/2, mc=(a+b)/2, rc=(g+r)/2.
```

B1, for `d!=0` and `h(f)=gamma*h(d)`, replaces `(d,f)` by
`(J*d,Jinv*f)`. B2, for `f!=0` and `h(d)=gamma*h(f)`, replaces them
by `(Jinv*d,J*f)`. Both centers are retained. The nonzero branches
cannot both apply, since that would require `gamma^2=1`. They are inverse
branches. Thus B is an involution and preserves the two separate linear
sums and the combined Hermitian account. The complete inverse tick first
recovers the previous matching bit, then applies B, then inverse C.

The ideal `(eta)` is prime with residue field F5. Indeed rho becomes 1
modulo eta; `j^2=1` and `j^5=1` imply `j=1`, and the cyclotomic
relation gives 5=0. Evaluation at j=1 modulo5 supplies the converse map.
In particular 2 is invertible modulo eta. More generally,

```text
2*x in eta^s*O  implies  x in eta^s*O, for every integer s>=0.
```

For s>0, reduction modulo eta first gives `x=eta*y`. Cancel eta in
the domain O and apply the same argument successively. No claim that 2
is a unit of O itself is needed. Write `nu_eta(a)=s` to mean
`a in eta^s*O` but `a not in eta^(s+1)*O`.

## 2. Antisymmetric material columns and an all-time obstruction

Fix a column untouched by every external material boundary. Material C
contacts are vertical, with exactly the same matching on r0 and r2;
they do not transport material between columns. Radiation is unrestricted.

**Antisymmetry lemma, conditional candidate-T.** If each row starts with
`r2=-r0`, this relation holds at every later full and post-C cut.

For a material C pair `(a,b)` on r0 the r2 pair is `(-a,-b)`.
Its parity decision is the same, and its output is the negative of the
r0 output, whether admitted or refused. At B the material center is
zero and remains zero. Its r0 value is either unchanged, multiplied by
J, or multiplied by Jinv. This closes the induction. The argument does
not assume that different rows have the same value.

**Leading-residue lemma, conditional candidate-T.** Suppose the column
is antisymmetric and all r0 values lie in `eta^s*O` for one s>=0.
Then each row's zero or nonzero residue after division by eta^s, modulo
eta, is invariant under all future native ticks. C preserves that residue
literally; B may multiply it by a nonzero residue.

For an admitted C pair both values lie in `eta^s*O`. The preceding
divisibility fact shows that `(a-b)/2` also lies in that ideal.
Each C increment therefore lies in `eta^(s+1)*O`. A refusal has no
increment. At B the material value is multiplied by a unit or unchanged.
Modulo eta, J is 2 and Jinv is 3, both nonzero. Thus membership in
`eta^s*O` persists, and a nonzero leading residue cannot become zero.
Induction applies to every contact and both cut types. Arbitrary changes
to the radiation do not invalidate this material argument.

In particular, if every initial r0 has valuation exactly s, every one
retains that valuation forever. Their initial values and leading residues
may all differ. The result does not assert preservation of each higher
valuation when only a lower common bound is known; neighboring lower-order
material can change higher coefficients while respecting the stated lemma.

### Application to original column6

In the supplied original preparation, every row of column6 has

```text
r0=d0=Jinv*eta=(-1,-2,-2,0),
r2=-d0.
```

Here `nu_eta(d0)=1`, since Jinv is a unit. Initial radiation replacement
does not change this material. The only later authorized source exchange
touches column0, not column6. Hence, for every radiation preparation and
every native duration satisfying that boundary contract, every material
slot of column6 retains valuation1 at full and post-C cuts.

The former prepared module supplied

```text
dR=-J*eta^2*v
```

as r0, with opposite r2, for nonzero integral v. This has valuation at
least2. Even a single original worker r0 slot cannot attain that value
under the stated contract. The literal former twelve-slot receiver is
therefore unreachable. Allowing native adaptation after relative89 or an
arbitrarily long delay does not help. Neither extra radiation nor its
retained stock changes this obstruction. A material boundary in column6
would change the premise and would be a different protocol.

This excludes the old material prescription, not all original-start
receivers. In particular the natural-worker construction below keeps
valuation1 before and after its proposed write.

### Empty material columns do not supply an alternative for free

If an entire column starts with both material rails zero, C keeps them
zero. B1 is excluded by d=0, and B2 would require `0=gamma*h(f)` with
f nonzero, which is impossible. Such a column stays zero unless a material
boundary changes it. In the present original preparation this applies to
columns1,2,3. A radiation-only initial replacement cannot make them into
a nonzero material receiver under this H3 law.

## 3. The waiting probe's two outgoing words

Use the two fixed amplitudes

```text
fB=(-3,-5,-4,0),
dstar=J*fB=(1,-1,-3,-1),
fA=J^2*fB=(3,2,1,1).
```

These identities follow by direct multiplication in O. At a target with
positive material half-difference dstar, radiation `(fA,-fA)` triggers
B1 and emits `(dstar,-dstar)`. At the supplied negative material pair,
whose difference is odd, it is idle and emits `(fA,-fA)`. Applying these
facts at relative108 requires the actual post-C material and radiation;
the identity of the amplitudes alone does not establish their arrival.

For any nonzero integral v put

```text
w=eta^2*v,
b=-dstar-8*v.
```

The negative CORR word satisfies

```text
(-fA)-b=dstar-fA+8*v=(-2,-3,-4,-2)+8*v = j mod2.
```

It therefore refuses a C contact with b. The positive word is -dstar,
whose difference from b is exactly8v. If the buffer and receiver have the
required common CORR b and no intervening B alters the buffer, the two
successive horizontal contacts give

```text
buffer:   b for negative, b+4*eta*v for positive,
receiver: b for negative, b+2*eta^2*v for positive.
```

For the frozen schedule these are contacts(4,5) at109 and(5,6) at110.
Their application requires the actual common ready values, matching bits,
and buffer inactivity. TAIL and RING do not establish those later
conditions merely by supplying the initial constants.

## 4. Receiver matched to the original material

Assume, at the actual post-C receive cut, common material `(d0,-d0)`
and common CLK g, with the incoming CORR values from Section3. For
receiver tag1 take K=J; for receiver tag2 take K=Jinv. Define

```text
ft=K*d0,
g=b+2*w+2*ft.
```

The positive radiation half-difference is ft and the negative one is
`fminus=ft+w`. All are integral. The positive cell takes the chosen
branch and outputs material `(K*d0,-K*d0)`. Its outgoing radiation
half-difference is d0 for either branch. More explicitly, with
`cplus=b+2*w+ft`, its outgoing radiation is

```text
(cplus+d0,cplus-d0).
```

The negative cell is idle exactly when

```text
h(ft+w) != gamma*h(d0)
and
h(d0) != gamma*h(ft+w).
```

These exclusions also cover fminus=0 correctly: then both branches are
idle, since d0 is nonzero. The positive material output differs from d0
because J and Jinv differ from1. Both possible outputs still have
valuation1, in agreement with Section2.

This is a strict local discriminator conditional on actual readiness. It
does not assert that r0 at the receiver stayed d0 during the preceding
worker process, that its CLK stayed g, that the two arriving CORR values
were delivered, or that the received pair subsequently remains stationary.
The rest of column6 may still carry old or background information.

## 5. Complete nominal local classification for the frozen scales

Let `v=m*j^k`, with positive integer m and k in0..4. Set

```text
x=h(eta)=4-gamma,
c_k=eta*j^k+conjugate(eta*j^k).
```

The exact five values and their shifted coefficients are

| k | c_k | gamma^-1*c_(k+2 mod5) |
|---|---|---|
|0|4-gamma|-7+3*gamma|
|1|3-2*gamma|-11+4*gamma|
|2|2*gamma-3|0|
|3|gamma-4|11-4*gamma|
|4|0|7-3*gamma|

For example `j+j^-1=1-gamma` and `j^2+j^-2=gamma-2` give
the middle column directly. Multiplication by `gamma^-1=3-gamma`
and the quadratic equation give the last column.

For tag1, `ft=eta`. Thus

```text
h(fminus)=h(eta)*N1,
N1=1+m*c_k+m^2*x.
```

The negative cell takes B1 exactly when N1=1, and B2 exactly when
`N1=gamma^-2`. For tag2, `ft=Jinv^2*eta`. Since
`Jinv^2=gamma^-1*rho^-1`,

```text
h(fminus)=h(eta)*N2,
N2=gamma^-2+m*gamma^-1*c_(k+2)+m^2*x.
```

Here negative B1 means N2=1 and negative B2 means `N2=gamma^-2`.

These equalities can be solved over integers without a trajectory or a
numerical embedding. If `c=A+B*gamma`, N1=1 requires
`A+4*m=0` and `B-m=0`. Only k=3,m=1 satisfies both.
N1=`gamma^-2=8-3*gamma` requires

```text
-7+A*m+4*m^2=0,
3+B*m-m^2=0.
```

Using the table, k=1 permits m=1 and satisfies both equations. The
other positive integer root supplied by the second equation is k=2,m=3,
which fails the first; the other three phases have no positive integer
root of the second equation.

For N2 write the last table column as `A+B*gamma`. Equality to
gamma inverse squared would require `A+4*m=0,B-m=0`; neither of
the positive possibilities m=3,k=0 or m=4,k=1 satisfies both.
Equality N2=1 requires

```text
7+A*m+4*m^2=0,
-3+B*m-m^2=0.
```

Only k=1 gives positive integer possibilities m=1,3; m=1 satisfies
the first equation and m=3 does not. Irrationality of gamma justifies
equating the two rational coefficients in every case. Thus the complete
exception table for all positive integer m is

| Intended positive tag | m | k | Actual negative tag |
|---|---:|---:|---|
|1|1|1|2|
|1|1|3|1|
|2|1|1|1|

All other pairs are negative-idle and positive-active under the exact
local readiness assumptions. For m=1..8 there are therefore77 of80
nominal eligible choices. Duplicating them over TAIL and RING gives154
of160 labels passing this conditional algebraic criterion. It gives no
number of successful initial preparations, preserved prefixes, delivered
signals or retained receivers. Those counts can be zero without
contradicting this theorem.

The large-m exclusions also have direct exact bounds. In the principal
embedding `gamma=(3-sqrt(5))/2` lies in(0,1), and every c_k is at least
`-x`. For tag1 and m>=2,
`N1>=1+x*m*(m-1)>=1+2*x`; the last bound exceeds gamma inverse
squared by `1+gamma` and exceeds1. For tag2 and m>=3,
`N2-gamma^-2>=m*x*(m-gamma^-1)>0`, since
`gamma^-1=3-gamma<3`; gamma inverse squared itself exceeds1.
At m=2 the lowest phase, k=1, gives `N2=2+gamma`, strictly between
1 and gamma inverse squared. All other phases give at least `10-gamma`,
exceeding gamma inverse squared by `2+2*gamma`. The m=1 exceptions are
the exact table above. These inequalities use no decimal approximation.

## 6. What the two initial supports actually establish

The waiting stock is `CLK(4,3)=CLK(4,4)=fA` and
`CORR(3,3)=CORR(4,3)=-fA`. Both supports add `CLK(6,3)=g`.
TAIL adds CORR b in columns5,6 at row3. RING adds it in columns
0,1,2,5,6,7 at that row. No material is replaced.

The original odd-row CORR values are the common even element
`E0=2*eta*J*(2-rho)`. Modulo2,

```text
b=g=(1,1,1,1)=j^4,
-fA=(1,0,1,1),
(-fA)-b=j,
E0=0.
```

At original full0 every horizontal contact on row3 is consequently
either an equal pair or a pair with odd difference, in either support.
C alone fixes that entire row, under either matching. TAIL's edges
against the untouched even CORR refuse; RING replaces those outside
values by the common b and retains the odd interfaces against -fA.

The original worker CLK is the common element
`G0=eta*(6,-2,12,1)` in the coefficient basis. Its parity is
`1+j^3=(1,0,0,1)`, different from g. Thus the new CLK(6,3) refuses
its initial vertical contacts with the original neighboring CLK values.
The other worker CLK pairs are equal. Similarly, the original column4
CLK is `(31,18,27,14)`, whose parity differs from fA, so the pair of
waiting CLK values is initially isolated by refusals at its boundary.

These statements concern the supplied initial field and C-only
continuation. A native B at a port or neighboring cell can change a
participating radiation value or its parity. Native material evolution
can change whether a later B occurs. The facts above therefore do not
prove waiting until222, worker readiness at221..224, buffer idleness,
or preservation of the original source and old archive. Every such
full-field condition remains an actual frozen comparison. The RING
support in particular changes source and archive radiation, so its larger
initial common CORR region is not automatically an admissible guard for
the original material work.

## 7. Paid preparation, active accounts and retained context

For material stock M and radiation stock R define

```text
A(M,R)=(sum M, sum R, sum h(z), sum q(z)),
q(z)=Tr(h(z))/2=(5*sum_i z_i^2-(sum_i z_i)^2)/2.
```

The sums in H and Q include both types. q is positive on nonzero O.
For either support let n be2 for TAIL and6 for RING. Its incoming
radiation stock has `4+n+1` ordered slots, hence seven or eleven, with

```text
Sm=0,
Sr=n*b+g,
H=4*h(fA)+n*h(b)+h(g),
Q=4*q(fA)+n*q(b)+q(g).
```

The four waiting entries alone have zero sum and Q=52. Each supplied
slot counts even if its value happens to equal the original value.
For each input, append the common stock and swap its entries with the
declared original radiation slots. Keep every outgoing value in the
corresponding ordered radiation reserve. This is a type-preserving
permutation, so all complete accounts and the exact inverse are retained.

Also supply the original six material source values
`(eta*j^q,-eta*j^q)` repeated three times. They have a common account
for every q, with zero sum and Q=30. At absolute114 swap them with the
specified source slots and retain the actual outgoing material. The
original source contract separately requires those outgoing values to
be the prescribed p stock; its equality is not inferred from Q.
All reserves are inert during subsequent native evolution.

Native account conservation follows directly from Section1. For example
B1 preserves the varying contribution because
`gamma*h(d)+gamma^-1*h(f)=h(d)+h(f)` under its balance condition.
Linear centers are preserved separately. Thus each whole field plus its
retained reserves has the complete conserved account. An account equality
does not identify fields, ready states, histories or ordered reserves.

There is also a useful necessary test for a proposed complete endpoint.
The original full0 radiation is common across p, and the original full
field accounts are common. A fixed common radiation replacement therefore
leaves common ACTIVE accounts across p. If the prescribed equal-account
source exchange passes its actual inventory test, those active accounts
stay common across all25 (p,q) histories. An exact endpoint family with
unequal active account tuples cannot arise by this protocol, even if a
late assembly could balance them using input-dependent outgoing reserves.
This is only an obstruction to that complete prescribed endpoint. A
partially specified ready interface can leave radiation outside the
interface free to retain the necessary account and information.

The50 donor forks are a separate causal diagnostic, with both donors and
all outgoing bank material retained. They are not50 original trajectories
with an unmentioned additional independent input. For fixed p,q and fixed
common hardware, deterministic native evolution has a single actual bank
state. The independent a choice is introduced only at the declared
diagnostic boundary. Equal field replay is allowed only with literal
field/phase equality and reserve independence; original input identities
and multiplicities remain part of the compound state.

## 8. Scope and exact falsifiers

The material obstruction is an all-time result under its antisymmetry,
initial ideal and boundary hypotheses. It does not require a finite
trajectory audit and is not weakened by allowing adaptation90..107.
Changing those hypotheses is a new construction, not a counterexample
to the stated induction.

The local receiver formula requires actual `(d0,-d0)`, g and the two
specified arriving CORR values at the read cut. Its three exceptional
nominal labels fail exactly the negative-idle clause. A passing nominal
label still fails the complete experiment if any original-work, source,
bank, archive, readiness, native-contact or causal-control clause fails.
Unexecuted gates are not successful gates. The positive local output is
not a proof of clean column sums, stationary local matter, whole-worker
reset or a closed two-state future.

Only the frozen full-field comparisons can decide the160 original-start
labels, the A_ONLY diagnostic and the finite retention conditions. Both
new implementations must be jointly pinned before any execution as the
preregistration requires. The previous ordering deviation is not repaired
by the new experiment or by these proofs. No physical occurrence, native-U
identity, general source loader, arbitrary renewal, unlimited history,
Canon promotion or layer lift is asserted.
