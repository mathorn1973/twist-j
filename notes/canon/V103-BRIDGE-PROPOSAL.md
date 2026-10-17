# Proposed residue-bridge addition

**PUBLIC / NON-CANONICAL / L1.** This file is a proposed Canon passage,
not Public Canon v103 and not a change of authority. All proposed results
remain candidate scope. A separate reviewed fold must assign any public
claim IDs, statuses, evidence and dependencies. Current Public Canon v102
continues to govern.

This passage is designed to follow the existing integer field-shell and
native protected-invariant material. It uses their literal matrices,
native generators and counter convention. Full provenance, excluded
source assertions and the detailed derivations are in
`../C-V103-BRIDGE-SYNTHESIS-N/ACCEPTANCE.md`, `CLAIMS.tsv` and
`SYNTHESIS.md`. The optional bounded-cell section is separable.

## 1. Native zero gate and integer shell residues

Fix the canonical native checkpoint `x=(a,b,c,d,q,r)` in `F5^6`,
`z=a+b+c+d+q+r`, and

```text
h(x)=(b+2a,d+2c),
pi_P(x)=(a,b,c,d),        W(a,b,c,d)=(b,a,d,c),
K={(a,3a,c,3c):a,c in F5},
G_L={(3s,s,3t,t):s,t in F5}.
```

**Proposed candidate theorem.** `W(K)=G_L`, and for every checkpoint
`h(x)=0` if and only if `W pi_P(x) in G_L`. By the canonical integer
image criterion, this is also equivalent to **every** integer representative
of `W pi_P(x)` belonging to `LZ^4`. Here `K` and `G_L` are different
marked subspaces of `F5^4`, each with 25 elements; the checkpoint gate
`G0=pi_P^(-1)(K)` has 625 elements.

Proof: the two shell congruences evaluated at `W pi_P(x)` are precisely
the two components of `h`. Shell membership depends only on the residue.
This identifies a predicate and does not choose a lift or decode a message.

Let `J2` exchange the two gate coordinates. For canonical generators
`g0,...,g4`, direct substitution gives

```text
h(g0 x)=2h(x)+2(a,c),
h(g1 x)=-J2 h(x),
h(g2 x)=-J2 h(x)+(r,-r),
h(g3 x)=h(g4 x)=-h(x).
```

The `g0` action has no closed `h`-only law: the pair
`(h(p),h(g0 p))` determines the full piston, because each two-coordinate
block has determinant 3 in `F5`. On `X14={z=1 or z=4}`, selection uses
only `g1,g3,g4`, so zero-gate membership and its complement persist under
every future driver word. This permanence is a corollary of the inherited
protected-sign invariant. It is not pointwise fixation or global selected-map
bijectivity: `T_t(G0 intersect X14)=G0 intersect X_(4+2t mod 5)`, a
two-to-one map from 250 gated checkpoints onto 125.

## 2. Unit-seed residue classification

Use the existing literal field marking

```text
A_f = [[1,0,1,0],[0,1,0,1],[-2,1,-1,1],[1,-3,1,-2]],
B_f = [[4,-2,2,-1],[-2,6,-1,3],[2,-1,2,0],[-1,3,0,2]],
L   = [[1,-3,-1,-2],[-3,4,-2,1],[0,5,1,2],[5,-5,2,-1]],
H(a,b,c,d)=2a^2-2ab+3b^2+c^2+d^2+2ac-ad-bc+3bd.
```

The canonical identities `L=(I-A_f)(I-A_f^2)`, `det L=25`,
`L^2=5A_f^3`, `V_inv=A_f^2 L=5L^-1`, `H(Lu)=5H(u)`,
`H(A_f u)=H(u)` and `sum_(j=0)^4 A_f^j=0` retain their existing status.
Call `u` a unit seed precisely when `H(u)=1`.

**Proposed candidate theorem.** For `pi_L(u)=Lu mod 5`,

```text
pi_L: {u in Z^4:H(u)=1} -> G_L minus G_L^(A_f)
```

is a bijection. The five residues with no unit preimage are exactly

```text
G_L^(A_f)={(3s,s,0,0):s in F5}
 ={(0,0,0,0),(1,2,0,0),(2,4,0,0),(3,1,0,0),(4,3,0,0)}.
```

Proof. A complete unit count follows from

```text
4H=Q+(2c+2a-b)^2+(2d-a+3b)^2,
Q=3a^2+2ab+2b^2,
2Q=5a^2+(a+2b)^2,       3Q=5b^2+(3a+b)^2.
```

For `H=1`, both `a,b` lie in `{-1,0,1}`. The fibers at `(0,0)`,
`(0,+/-1)`, `(+/-1,0)` and `+/-(1,-1)` have respectively 4, 8, 4
and 4 solutions, while `+/-(1,1)` has none. The parity of the two
displayed squares makes these finite fibers exhaustive. There are 20
units; the bare count is inherited, while the residue classification is
the proposed increment.

The exact integer kernel is `ker(pi_L)=LZ^4`: from `Lu=5v` follows
`u=V_inv v=L A_f^2 v`, and the converse follows from `L^2=5A_f^3`.
Two units of equal image residue differ by a kernel vector whose energy
is a multiple of five and, by Cauchy-Schwarz, at most four. They are
therefore equal. On `G_L`, the action of `A_f` is the shear
`(s,t)->(s+t,t)`. A unit mapping to its fixed subgroup would have
`A_f u-u` in the kernel with energy at most four, hence `A_f u=u`.
The canonical five-term sum then gives `5u=0`, a contradiction.
Twenty distinct unit residues exhaust the twenty remaining classes.

Every missing unit residue still has integer shell representatives.
This theorem states no uniform higher-shell minimum for the five exceptions.

## 3. One exact native minimum and its next-step boundary

Under the origin-zero native counter and `theta_n=popcount(n) mod 2`,
the zero orbit has

```text
x0=x1=(0,0,0,0,0,0),
x2=(2,1,2,1,1,0),
x3=(0,0,1,3,1,1).
```

These prefixes and the gate permanence on `X14` give `h(x_n)=0` at
every `n>=0`. In particular `r3=1`.

**Proposed candidate theorem.** The infinite coset
`{y in LZ^4:y mod 5=W pi_P(x3)=(0,0,3,1)}` has minimum energy 5,
attained uniquely at `y*=(0,0,-2,1)` with preimage
`u*=(0,-1,-1,2)`.

Proof. Literal substitution gives `Lu*=y*` and
`H(u*)=3+1+4-1-6=1`. Every other admissible `y=Lu` has `u!=0`, so
`H(y)=5H(u)>=5`. Equality forces a unit preimage of the same residue,
which is unique by section 2. The proof applies to the entire infinite
coset, not only a finite search domain.

**Proposed candidate corollary.** No sequence of unit seeds represents
this fixed native orbit at every boundary `n>=3` through the fixed map
`u -> Lu mod 5=W pi_P(x_n)`.

Proof. At boundary 3, `theta3=0` and `z3=1`; the next step uses
`g1(x)=(-c,-d,-a,-b,-q,-r)`. Hence
`x4=(4,2,0,0,4,4)` and `W pi_P(x4)=(2,4,0,0)`, one of the five
residues without a unit preimage. The required unit at boundary 4 does
not exist, even with unrestricted pointwise choices.

This does not exclude higher-energy integer lifts or an eventual unit lift
after some later cutoff, and it states no boundary-4 minimum. The unique
boundary-3 minimum is a mathematical compatibility result, not native
production, energy funding or physical selection of a source.

## 4. Preparation and contact scope

Set `A=a+c`, `B=b+d`, `C=a-c-2`, `D=b-d-1`. The exact gate identities
are `h1+h2=2A+B`, `h1-h2=2C+D`; thus `h=0` iff `B=3A` and `D=3C`.

**Proposed candidate interface consequences**, using the unchanged native
preparations and inherited complete supports:

| Family | Gate classification | Essential qualification |
|---|---|---|
| Original `E(lambda,mu)` with initial chart `(A,B,C,D,q,r)=(1,0,lambda,mu,0,1)` | 0 of its 550 support checkpoints | Its full piston can still distinguish all 25 pairs at each fixed common time; gate passage is not semantic readback. |
| Alternative `E_alt(lambda,mu)`, `t=3(1+mu-lambda)`, initial chart `(mu,0,3,0,2-mu-t,t)` | One of 150: `(2,1,2,1,1,3)`, at boundary 1 for `(lambda,mu)=(2,0)` | It leaves the gate next step; the initial `(q,r)` already encodes both labels. |
| Occupied one-shot `x_lambda(0)=(lambda,0,-lambda,0,0,0)` | Gate iff `lambda=0` for all actual times; 20 zero-payload points in the 100-state ready graph | Graph cardinality does not assert full orbit visitation; occupied zero passes before readiness. |
| One-shot absence `x_empty(0)=(0,0,1,0,0,0)` | Never passes | BLANK is distinct from PRESENT(0); its port history differs from occupied inputs before boundary 3. |

The all-time classifications have elementary parametric proofs. For the
original family, put `k=lambda+3mu`. Prefix gate values are
`(1+k,1-k)`, `(k,3-k)`, `(1+k,1-k)`, `(-1-k,-1+k)`.
On the tail, `s=A in {1,-1}`, `z in {1,-1}`, `B=0`,
`C=sz lambda`, `D=sz mu`, so `h=s(1+zk,1-zk)` has nonzero sum.
For the alternative, the four prefix values are
`(mu+3,mu-3)`, `(-mu+3+t,-mu-3-t)`, `(mu+3,mu-3)`,
`(-mu+2,-mu-2)`. Only the specified boundary-1 pair passes. Its tail
has `C in {2,3}` and `h=C(2z mu+1,2z mu-1)`, never zero.

For occupied one-shot states the proof must be piecewise: coefficients
of `(lambda,-lambda)` are 2 at boundary 0, 1 at boundaries 1 and 2,
and `-2Bz in {1,-1}` only on the ready tail at `n>=3`. The tail chart
has `B in {2,3}`, `z in {1,4}`, `D,r in F5` and payload
`lambda=3-BzD`, giving twenty zero-payload points. The absence invariant
has `h=s(1-z,1+z)`, with nonzero sum. The tail parametrization must
not be applied to the occupied prefix.

**Proposed candidate source-blindness theorem.** Let the rational source
remain `a_contact(q,r)=S(ell(q)/2,(ell(r)+1)/2,0,0)`, with the canonical
balanced section and injective `S`. For the original preparation family,
a common complete receiver and a common source-independent protocol have
identical receiver histories for all message pairs. The same holds among
the five occupied one-shot payloads.

Proof. The quotient `(z,q,r)` evolves by the five restrictions
`(z,q,r)`, `(-z,-q,-r)`, `(2-z,1-q,-r)`, `(2-z,1-q,1-r)`,
`(3-z,2-q,1-r)`. Selection uses only `z` and the common bit, so a common
initial quotient gives identical control histories. Both named families
have that property within their occupied preparations. Equal source and
equal complete receiver state give equal deterministic wave, tape and
contact updates, including resource guards, refusals and ledger changes.
Induction proves the claim. The complete receiver includes its wave vectors,
four tape slots, pointer, store, ledger, direction and protocol state.
Adaptation using only its common history preserves the argument; an extra
message-dependent input changes the premise.

The alternative family has `q0=3lambda+mu+4`,
`r0=2lambda+3mu+3`, with determinant 2, so its controls are already
pair-sensitive. This does not establish funded receiver separation or
native source loading. The absence history differs from occupied inputs
at boundary 2 and may have made a persistent receiver record; later
quotient equality does not prove complete-history equality.

The native piston-to-shell comparison and the `(q,r)`-to-rational-source
route are separate maps. A shell-admitted four-vector does not specify the
full integer source, resources, static field, channels or chronology, and
no full-state map to the rational contact carrier is provided. With the
fixed form, `H(Wy)-H(y)=a^2-b^2+ac-bd`, so `W` is not an energy
isometry. A passive change of coordinates must also transform the metric
and operators.

The remaining positive-interface obligation is to freeze a permitted
message-sensitive source-access map on a complete preparation family,
with complete receiver, initial common-state conditions, equality/readout,
funding, timing and a falsifier. Any integer-chain leg additionally requires
a shell-admitted complete preparation and a typed full-carrier relation.
This is a proposed open obligation, not an executed experiment or an
adopted registry/gate row. Gate arrival alone is not funded transmission.

## 5. Optional finite cell comparison

Under the declared unweighted electric-first shear,
`A_G=[[I,I],[-G,I-G]]` and
`H_G(z,M)=z^t Gz+M^t M+z^t GM`. The five selected Grams
`(2)`, `(3)`, `[[2,1],[1,2]]`, `[[2,1],[1,3]]` and
`[[3,1],[1,3]]` have exact matrix orders 4, 3, 6, 5 and infinite.
The first four energy forms are positive definite; the last is positive
semidefinite with nullity one. Its Jordan chain
`v=(1,1,-2,-2)`, `w=(0,0,1,1)` satisfies
`(A_G+I)v=0`, `(A_G+I)w=v`, hence
`A_G^n w=(-1)^n(w-nv)` for every integer `n`.

Digons here use distinct parallel edges, and reorientations act on whole
edges or faces. The mixed-cell face reorientation gives the canonical
`A_f`. Matrix order is not the period of every state. The raw/static
decomposition is rational, not a direct integral splitting. General
conservation, triangle order three, canonical order five and the zero-mode
boundary are inherited. This bounded comparison proves neither unique
physical selection of order five nor universal cell minimality.
