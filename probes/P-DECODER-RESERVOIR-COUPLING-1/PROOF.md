# Reservoir coupling and record accounting: conditional proof

**NON-CANONICAL / PROOF-FIRST / CHOICE-EXPLICIT / L1 ONLY.**

This is the uniform argument for `DECODER-RESERVOIR-RECORD-ACCOUNTING`,
reserved by `P-DECODER-RESERVOIR-COUPLING-1` in
[#824](https://github.com/mathorn1973/twist-j/issues/824). It assigns no
public status and records no scientific execution. Its public basis is
`a353b7e2aaec3e13f458f52e68c6464b9d718e67`, ACTIVE Public Canon v76.
All statements below concern the fixed mathematical choices, not a physical
apparatus realization. Finite tests audit these formulas rather than replace
their quantifiers over finite supports, contexts and finite histories.

## 1. Inherited wave and exact context

The wave carrier is `V=C_c(D3,Q)`, where
`D3={x in Z^3:sum_i x_i is even}`. A pair is `(u,v)=(previous,current)`.
The selected flat operator is

```text
(Lv)_x=sum_(z in N) c_z(v_x-v_(x+z)),
N = complete shells of squared norms 2,4,8,10,16,
c_z=w_|z|^2/324,       (w_2,w_4,w_8,w_10,w_16)=(6,1,15,1,1).
```

Thus `N=-N`, `c_z=c_-z>0`, and `sum_z c_z=8/9`. Put `B={0} union N`.
For neighbouring `y=x+z`, write `c_xy=c_z`. A directed edge sum includes
both orientations. Define

```text
E(u,v)=||v-u||^2/2+<u,Lv>/2,
e_x(u,v)=5(v_x-u_x)^2/18
         +sum_y c_xy[(v_y-u_x)^2+(u_y-v_x)^2]/8.
```

The inherited result proves `sum_x e_x=E`, `e_x>=0`, and `E=0 iff u=v=0`
on this finite-support carrier. These are not assertions on every function
in `Map(D3,C)` or on a substituted periodic box.

For an arbitrary forced step `w=2v-u-Lv+f`, it also proves

```text
E(v,w)-E(u,v)=<w-u,f>/2,
e_x(v,w)-e_x(u,v)+sum_y J_xy(u,v,w)=(w_x-u_x)f_x/2,           (1)
J_yx=-J_xy.
```

For clarity, the same fixed representative of the current is

```text
D_xy(u,v)=c_xy[(v_y-u_y)^2-(v_x-u_x)^2]/8,
J_xy=c_xy(v_x-v_y)[(w_x-u_x)+(w_y-u_y)]/4
     -D_xy(v,w)+D_xy(u,v).
```

These are the formulas of the preceding transport probe, not a new density
or current selection. The implementation consumes the existing file

```text
path: probes/P-DECODER-RETARDED-ENERGY-TRANSPORT-1/transport.py
pin:  30ab237b4dcb339115517f67b883ca4cc3e00c32
SHA256: 983d22690e061128d287f23ef4672fbd72954faa28f1a3fde9ce38b0d6660a60
bytes: 11353
```

through its immutable dependency contract. It does not copy or edit that
module or reinterpret its completed result.

A reservoir context is a finite map `Gamma:R->Q_(>0)` and one common
threshold `q in Q_(>0)`. Extend `gamma_x=Gamma(x)` by zero outside `R`.
The empty map is admitted. Zero-weight entries are excluded from its
canonical representation; they would not be active channels. Sites,
coefficients and threshold have literal equality, with the distinct sites
ordered lexicographically. The context is fixed for a history and is not
selected from future outputs. Incoming and outgoing port amplitudes are
complete rational vectors on `R`, including zero entries, with energy

```text
K_Gamma(a)=sum_(x in R) gamma_x a_x^2.
```

The source, damping coefficients, threshold and cold-port convention are
explicit choices. No uniqueness or physical admissibility theorem is assumed.

## 2. Reversible local coupling with arbitrary incoming ports

Given `(u,v)` and incoming amplitudes `a`, define, at active sites,

```text
p_x=(w_x-u_x)/2,
f_x=gamma_x(2a_x-p_x),
b_x=a_x-p_x.
```

Outside `R`, put `f_x=0` and introduce no port. Substitution into the forced
wave equation gives the explicit successor

```text
(1+gamma_x/2)w_x
 =2v_x-(Lv)_x-(1-gamma_x/2)u_x+2gamma_x a_x,                 (2)
```

where the last term is zero outside `R`. Every denominator is at least one,
so all finite-support rational pairs and rational port vectors have a unique
successor. Its support is contained in
`supp(u) union (supp(v)+B) union supp(a)`. The last support is within `R`.
No inverse spatial operator or boundary condition is needed: each denominator
in (2) is scalar and local. The value at `x` uses the old pair on `x+B` and
the context and incoming amplitude at `x` only.

The map `(u,v,a)->(v,w,b)` is bijective. Given its output, solve

```text
(1+gamma_x/2)u_x
 =2v_x-(Lv)_x-(1-gamma_x/2)w_x+2gamma_x b_x,                 (3)
a_x=b_x+(w_x-u_x)/2                    for x in R.
```

Outside `R`, (3) is the ordinary inverse wave step. To verify (3), use
`a=b+p` in the force: `f=gamma(2b+p)`, and collect the coefficient of `u`.
Substitution recovers both original equations. The inverse has the same
finite-range and rational character. In particular `gamma=2` is admitted
and causes no singularity in the full port coupling.

The port relation gives, pointwise,

```text
gamma_x(b_x^2-a_x^2)=gamma_x(p_x^2-2a_xp_x)=-p_x f_x.
```

Together with (1), this proves exact conservation

```text
E(v,w)+K_Gamma(b)=E(u,v)+K_Gamma(a),                         (4)
e_x(v,w)-e_x(u,v)+sum_y J_xy
 =gamma_x(a_x^2-b_x^2)                                    (5)
```

at active sites; the right side of (5) is zero elsewhere. Thus the full map
is a bijective, quadratic-energy preserving rational coupling. Incoming
port energy is explicitly included; it is never a hidden source of energy.
This algebraic statement is not a physical unitarity or reservoir theorem.

## 3. Cold ports, actual wave update and stored outgoing tape

The chosen dissipative history supplies a fresh zero incoming port vector
at every numbered step: `a=0`. Then (2) becomes

```text
w_x=[2v_x-(Lv)_x-(1-gamma_x/2)u_x]/(1+gamma_x/2),
b_x=-(w_x-u_x)/2,
h_x=gamma_x b_x^2=gamma_x(w_x-u_x)^2/4 >=0.                 (6)
```

The actual next wave is `(v,w)`, rather than the free successor accompanied
by an unrelated counter increment. Formula (1) implies

```text
E(v,w)-E(u,v)=-sum_x h_x,
e_x(v,w)-e_x(u,v)+sum_y J_xy=-h_x.                          (7)
```

For a history of `n` steps, retain the complete signed outgoing tape
`(b^0,...,b^(n-1))`. Define its site heat summary

```text
M_x^n=sum_(j=0)^(n-1) gamma_x (b_x^j)^2,       M_x^0=0.
```

Induction in (7) gives

```text
E(P_n)+sum_x M_x^n=E(P_0),
M_x^(n+1)=M_x^n+h_x^n >= M_x^n.                            (8)
```

The signed tape and `M` are two representations of the same stored energy.
Their energies are not added together. If both are stored, the summary must
equal the displayed sum of weighted squares. No additional energy is assigned
to a record merely because it appears in more than one view.

For any finite spatial set `A`, summing the local law yields

```text
E_A(P_(n+1))-E_A(P_n)
 +sum_(x in A,y outside A) J_xy +sum_(x in A intersect R) h_x^n=0.
```

Equivalently, `e_x(P_n)+M_x^n`, with memory zero outside `R`, satisfies the
same conservative local law with current `J`. Interior edges cancel. The
deposit at `x` uses the old pair on `x+B`; reading pair energy on `A` uses
the completed pair on `A+B`. Evaluating a transition current uses its completed
triple at the edge endpoints. Computing those successor values from an older
pair additionally uses their stencils. The reservoir rule does not remove
the inherited energy-density halo.

Each finite history can be represented by finitely many initially zero port
slots. Apply the bijection of section 2 to the wave and one unused slot at
each step, keeping every earlier outgoing slot. The total wave-plus-slot
energy is conserved. Reversing the used slots in reverse order reconstructs
the earlier waves and, on a generated cold history, the zero incoming slots.
There is no erasure or reset of an occupied slot.

In this rational real scalar model the signs of the outgoing amplitudes
retain real amplitude/phase information that their squares discard. Inverse
reconstruction uses the signed slot, not its heat alone. Any loss of
reversibility in the reduced wave/heat description comes from fixing fresh
cold inputs and discarding that information in the summary; it is not fundamental
irreversibility of the full coupling. No physical photon phase is thereby
identified or measured.

## 4. Source preparation and its energy budget

Keep the preceding probe's preparation exactly. For `alpha in Q^4`, put
`s=sum_i alpha_i` and inject coefficients

```text
(alpha_0-s/5,alpha_1-s/5,alpha_2-s/5,alpha_3-s/5,-s/5)
```

at the five distinct sites `(000),(110),(101),(011),(200)`. Call this field
`S_source(alpha)`. Its squared norm is

```text
m(alpha)=sum_i alpha_i^2-s^2/5.
```

The initial post-kick pair is `P_0=(0,S_source(alpha))`. The source kick is
performed before enabling the reservoir coupling; its preceding ready pair
is `(0,0)`. Initialize the outgoing tape and all heat summaries as empty/zero.
Then

```text
E(P_0)=m(alpha)/2,
2[E(P_n)+sum_x M_x^n]=m(alpha)              for every n>=0.   (9)
```

Simultaneously damping the source kick would instead produce a different
initial wave and source-work budget. That alternative is not substituted.
The exposed source isometry and its rational extension are inherited choices;
on the balanced QDD subset, `m` is the existing total QDD weight. No physical
target independence or LOW/HIGH interpretation follows from (9).

## 5. Complete threshold records without double counting

For the fixed positive common threshold `q`, define at each active channel

```text
N_x^n=floor(M_x^n/q),
r_x^n=M_x^n-q N_x^n,              0<=r_x^n<q.
```

Rational division and integer floor make these total exact operations.
Because heat is nondecreasing, the threshold batch at step `n` consists of
every channel/ordinal pair

```text
(x,k) with x in R and N_x^n < k <= N_x^(n+1).                (10)
```

Order channels lexicographically and ordinals increasingly, or represent
each complete ordinal interval by its endpoints. Both presentations denote
the same finite batch. No channel or crossing is randomly selected; multiple
crossings in one step are all retained. An empty batch is an explicit
completed-step record and does not halt the wave.

At a fixed channel the consecutive intervals in (10) are disjoint and their
union through step `n-1` is exactly `1,...,N_x^n`. Thus there are no skipped
or repeated threshold ordinals. Moreover

```text
E(P_n)+sum_x(q N_x^n+r_x^n)=E(P_0),
sum_x N_x^n <= floor(E(P_0)/q).                              (11)
```

The last inequality follows from `q sum_x N_x^n<=sum_x M_x^n<=E(P_0)`.
Threshold energy and remainders partition heat; they are not another energy
reservoir in addition to it. On the chosen source family, the bound is
`floor(m(alpha)/(2q))`. For an arbitrary initial finite-support pair, the
same proof uses its own initial energy and zero tape.

Every finite-step batch is computable, but a particular threshold need not
ever be reached. Its first crossing time, if one is defined, lies in
`N union {infinity}`. There is no assertion that a finite-prefix computation
can certify every infinite non-crossing case. These records are a chosen
thresholded view of accumulated mathematical energy, not physical clicks,
Born frequencies or a guarantee of finite detector completion.

## 6. Zero, nonabsorption and complete-absorption controls

An empty context has no ports, deposits or threshold crossings and gives
the free wave update. A zero pair with cold inputs remains zero for every
context. The chosen prepared pair is zero exactly when `alpha=0`; a later
zero wave does not conversely imply a zero initial source.
A zero deposit or empty threshold batch does not conversely imply a zero
wave, zero local energy, or failed preparation.

Two exact examples delimit the general finite-support pair carrier:

* Take `R={0}`, any `gamma_0>0`, `u=0`, and
  `v=delta_p-delta_-p` for `p=(1,1,0)`. The wave operator commutes with
  inversion. Odd previous/current slices have value zero at the origin, as
  does their free successor. The midpoint velocity at the origin, the force
  and the deposit are therefore zero. Oddness is preserved inductively,
  so heat is zero forever,
  while global initial energy is `1`. The initial passive density at the
  origin is nevertheless `e_0=2(6/324)/8=1/216>0`. Passive aperture energy
  and actual midpoint-friction deposit are different quantities.
* Take `R={0}`, `gamma_0=2`, `u=a delta_0`, `v=0`. Formula (6) gives
  `w=0` everywhere, outgoing amplitude `b_0=a/2`, and deposit `a^2/2`,
  equal to the entire initial wave energy. Thus one-step complete absorption
  is possible on this carrier. Changing `a` to `-a` leaves the heat unchanged
  but reverses the signed slot; the inverse recovers this distinction.

These examples are on the general pair carrier and need not be images of
the selected source preparation. Together they forbid both a universal
perfect-absorption assertion and an assertion that complete absorption is
impossible. No reflection-free boundary, impedance matching or eventual
absorption theorem is adopted. In particular `gamma=2` is not excluded:
only the reduced wave map can lose information there, while the full port
coupling remains bijective.

## 7. Uniform finite-prefix and history statement

For every fixed finite context, every finite-support rational initial pair
and every finite rational incoming-port prefix, equations (2)-(3) define
unique finite-support rational updates and inverses. For cold histories,
each update determines one signed outgoing vector, its nonnegative deposit,
the next heat summary, all threshold intervals and the next wave pair.
All denominators are positive and every threshold interval is finite.

Starting at the declared initial pair and empty tape, induction therefore
constructs a unique record prefix of any finite length. No formula uses the
requested final horizon or a future incoming vector. Extending the horizon
leaves all earlier wave states, signed slots, heat values and threshold
batches unchanged. Append stores exactly the next cut and its complete
record; prior records remain immutable. Passive rereading creates no new
deposit or event. No reset discards the tape, rewinds the heat or reissues an
old ordinal. These laws concern generated compatible histories, not arbitrary
forged combinations of records and summaries.

## 8. Scope boundary

This is a concrete mathematical interaction and post-state rule extending
the earlier passive reader. Its fixed context, cold port supply, signed
memory and threshold law are disclosed model choices. They act only on the
candidate scalar wave and its apparatus state. No port or record is an
additional input to autonomous U.

The result supplies neither a physical source/photon/detector certificate
nor a complete physical apparatus family. The #539 definition/profile and
class obligations remain STOP. Physical pointer/reduction, calibration,
absorption, realized occurrence, Born selection, Bell accounting and L6
measure remain open. Retained real signs do not certify photon polarization
or physical phase. The #744 pole/residue chain and #756 F3 requirement are
unchanged; production under #742 remains forbidden. No public Canon claim
is promoted by choosing or exactly implementing this model.

The inherited input is the
[retarded transport proof at its immutable pin](https://github.com/mathorn1973/twist-j/blob/30ab237b4dcb339115517f67b883ca4cc3e00c32/probes/P-DECODER-RETARDED-ENERGY-TRANSPORT-1/PROOF.md).
Its completed scope is recorded in
[the public result](https://github.com/mathorn1973/twist-j/blob/a353b7e2aaec3e13f458f52e68c6464b9d718e67/probes/P-DECODER-RETARDED-ENERGY-TRANSPORT-1/RESULT.md).
Neither source is amended by this separately named construction.
