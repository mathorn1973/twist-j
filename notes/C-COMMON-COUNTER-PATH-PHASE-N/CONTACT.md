<!-- SPDX-License-Identifier: Apache-2.0 -->

# Contact words: count, half-trace and closed words

**NON-CANONICAL / L1.** Candidate-T for the two written proofs, candidate-C
for the finite audits on one architecture. Reservation:
[#1922](https://github.com/mathorn1973/twist-j/issues/1922).

The contact, the slot frame and the accounts are the supplied model data of
RELATIVE-CONTACT-INTEGRAL-LAW [T]. No native-U implementation and no physical
energy, action or phase identification is asserted.

## Setup

Use the registered ring and contact:

```text
O=Z[j],  K=Q(j),  F=Q(sqrt5),  phi=-j^2-j^3,  rho=j^2,  pi=1-j,
O/(pi)=F5 by j->1,   c(a) = residue of a = coefficient sum mod 5,
h(a)=a*conj(a) in Z[phi],   q(a)=Tr_(K/Q)(a*conj(a))/2=Tr_(F/Q) h(a).
```

In the marked basis `a=a0+a1 j+a2 j^2+a3 j^3`,

```text
h(a)=A+B phi,
A=a0^2+a1^2+a2^2+a3^2-(a0a1+a1a2+a2a3),
B=(a0a1+a1a2+a2a3)-(a0a2+a1a3+a0a3),      q(a)=2A+B.
```

The total contact on a pair is refused unless `x-y` lies in `2O`; otherwise
`s=(x+y)/2`, `t=(x-y)/2` and `(x,y) -> (s+rho t, s-rho t)`.

A word is a finite sequence of attempted contacts on labelled pairs of a
bank `O^N`. Applied to a start state, each attempt is refused, admitted with
`t=0` (diagonal, nothing changes) or admitted with `t!=0` (state changing).
For a word `gamma` and a start state put

```text
N(gamma)   number of state-changing contacts,
H(gamma)   sum of h(t_k) over the admitted contacts, an element of Z[phi],
Q(gamma)   sum of q(t_k) over the admitted contacts = Tr_(F/Q) H(gamma).
```

These are sums over the contacts of a word. They are not the conserved
state accounts `E(z)=sum q(z_i)` and `h(z)=sum z_i*conj(z_i)` of the
registered law, which every contact leaves unchanged.

A word is closed at `x` if it returns `x`. The literal inverse of a word
reverses its order and repeats every contact four times (`C^-1=C^4`).

*Why H is called an area.* In a complex embedding `sigma`, interpolate an
admitted contact by `t -> exp(i tau) t`. With the standard form
`(1/2) Im(conj(x) dx)` summed over the two slots, the arc sweeps
`tau*sigma(h(t))`. So `sigma(H)` is the swept area per unit angle. This
remark is motivation only; no statement below uses the interpolation.

## Proposition K: the half-trace of a contact is a residue potential difference

For `v` in `O` let `ct` in `{0,...,4}` be the integer lift of `c(v)` and
`v1(v)=c((v-ct)/pi)` the first `pi`-adic digit. For a state `z` put

```text
psi(z) = 2 * sum_i c(z_i) * v1(z_i)   in F5.
```

**Proposition K.** For every admitted contact,
`q(t) = psi(after) - psi(before)` modulo 5.

**Proof.** `rho-1=-pi(1+j)` and `1+j=2` modulo `pi`. Residues are fixed
(registered). Since `(x'-ct)/pi=(x-ct)/pi-(1+j)t`, the first digits move by
`v1(x')=v1(x)-2c(t)` and `v1(y')=v1(y)+2c(t)`, and `2c(t)=c(x)-c(y)`. Hence
`psi(after)-psi(before)=-2(c(x)-c(y))^2=3(c(x)-c(y))^2`. On the other side
the registered trace formula `q(a)=(5*sum a_k^2-(sum a_k)^2)/2` gives
`q(a)=2c(a)^2` modulo 5, as the Canon text of
RELATIVE-CONTACT-FOUR-SLOT-MINIMUM [T] already notes. Hence
`q(t)=2((c(x)-c(y))/2)^2=3(c(x)-c(y))^2`. QED

The identity was audited on the 1452 admitted contacts of the ten runs below,
on all 28561 admitted ordered pairs with coefficients in `[-2,2]`, on 143795
admitted seeded random contacts, and by an independent digit algorithm on
100000 further contacts and on all 48480 admitted edges of the complete
orbit of the preparation `I_1` defined below.

**Consequences.**

- (K1) `Q(gamma)` modulo 5 is a function of the two endpoints. For a closed
  word `Q(gamma)=0` modulo 5.
- (K2) `q(t)=3(c(x)-c(y))^2` modulo 5. A contact between two slots with equal
  residue has `q(t)=0` modulo 5; residue difference `+-1` gives 3 and `+-2`
  gives 2.
- (K3) With `N_ik` the number of admitted contacts on the pair `{i,k}`,
  `Q(gamma)=3*sum N_ik (c_i-c_k)^2` modulo 5, an endpoint function. In a
  bank whose unequal residues all differ by the same square, such as the
  bank of #1908, the admitted count on pairs of unequal residue is therefore
  an endpoint function modulo 5. The path-dependent part of the count then
  lives on pairs of equal residue, where the half-trace is a multiple of
  five.

## Theorem L: closed words

**Theorem L.** Let `gamma` be a closed word on any bank `O^N`.

- (L1) For every `g` in `Gal(K/Q)` other than complex conjugation, the sum of
  `t_k*g(t_k)` over the admitted contacts of `gamma` is zero in `O`.
- (L2) `H(gamma)` lies in `5 Z[phi]`.
- (L3) Two words with the same start and the same end have
  `H(gamma1)-H(gamma2)` in `5 Z[phi]`.

**Proof.** (L1) Put `T_g(z)=sum_i z_i*g(z_i)`. For an admitted contact

```text
(s+rho t)g(s+rho t)+(s-rho t)g(s-rho t) = 2 s g(s) + 2 rho g(rho) t g(t),
```

and the same expression with `rho` replaced by 1 holds before the contact.
So `T_g(after)-T_g(before)=2(rho g(rho)-1) t g(t)`. For `g: j->j^a` the
product `rho g(rho)=j^(2+2a)` equals 1 only for `a=4`. For `a=1,2,3` the
factor `rho g(rho)-1` is a nonzero element of the field `K`; `T_g` returns
on a closed word, so the sum vanishes. For `a=4` the factor is zero: `T_g`
is the conserved Hermitian norm and gives no information, which is why `H`
itself need not vanish.

(L2) Reduce modulo 5: `O/5O=F5[j]/(j-1)^4`. Put `u=1-j`, nilpotent of index
four, and `l=-(u+u^2/2+u^3/3)`, the truncated logarithm of `j`; 2 and 3 are
invertible. Then `1,l,l^2,l^3` is a basis over F5 and `sigma_a(l)=a*l`,
because `log((1-u)^a)=a*log(1-u)` holds modulo `u^4` with denominators prime
to 5. Write `t=t0+t1 l+t2 l^2+t3 l^3` with `t_m` in F5. The `l^k`
coefficient of `t*sigma_a(t)` is `sum_(m+n=k) t_m t_n a^n`, so

```text
t*conj(t)       = t0^2 + (2 t0 t2 - t1^2) l^2          (a=4),
t^2             = t0^2 + ... + (2 t0 t2 + t1^2) l^2 + ...   (a=1),
t*sigma_2(t)    = t0^2 + ... + 2 t1^2 l^2 + ...             (a=2).
```

Thus `t0^2`, `t1^2` and `t0 t2` are F5-linear combinations of coefficients of
`t^2` and `t*sigma_2(t)`. By (L1) their sums over a closed word vanish in F5,
so `H(gamma)=0` in `O/5O`. Since `O=Z[phi]+Z[phi] j` is a direct sum,
`5O` meets `Z[phi]` in `5 Z[phi]`.

(L3) `gamma1` followed by the literal inverse of `gamma2` is closed. The
inverse passes through the same states backwards; each admitted contact of
`gamma2` is undone by four admitted contacts with half-differences
`rho t, rho^2 t, rho^3 t, rho^4 t`, which contribute `4h(t)`. Hence
`H(gamma1)+4H(gamma2)` lies in `5 Z[phi]`. QED

**Remarks.**

- Over Q the twelve coefficient forms of `t^2`, `t*sigma_2(t)`,
  `t*sigma_3(t)` have rank 8 and the two Hermitian forms `A`, `B` are
  independent of them (rank 10 of 10 monomials). Closed words with nonzero
  `H` exist; examples are below. Over F5 the twelve forms have rank 6 and
  contain `A` and `B`.
- Read one admitted contact as a rotation by `k` fifths of a turn. Then the
  swept area of a closed word is `k` whole turns times an element of
  `Z[phi]`, while an open word carries fifths. This is a property of the
  supplied model. No action quantum or physical normalization is claimed.
- (L2) was found after the first run of the frozen recon showed no holonomy
  of `(A,B)` modulo 5. Its proof does not depend on that run.

## The count is a determinant, not an account

`N` is additive under concatenation, and the literal inverse contributes
`4N=-N` modulo 5. Let `M_gamma` be the product of the K-linear maps of the
admitted contacts of `gamma`, with the identity for refused attempts. One
admitted contact has eigenvalues 1 and `rho` on its pair plane, so
`det M_gamma=rho^(number of admitted contacts)`, and `M_gamma x=x` for a
word closed at `x`. So the admitted count modulo 5 is the exponent of the
determinant of a linear map that fixes the state. Multiplying the start
state by an odd integer `m` leaves every admission, `M_gamma` and both
counts unchanged, while `H` is multiplied by `m^2`. `N` omits the diagonal
contacts, which are admitted but change nothing.

## Finite results (candidate-C)

The frozen clauses are run by `recon_contact_phase_2026-11-06.py`. The
lattices and the closed word are in `posthoc_contact_area_2026-11-06.py`,
the witnesses in `explore_shortest_count_loop_2026-11-06.py` and
`witness_equal_area_pair_2026-11-06.py`, and independent code paths in
`break_recon_parts_u_k_2026-11-06.py`. `check_log_coordinate_2026-11-06.py`
checks the displayed identities in the proof of (L2).

### The fixed word of #1908 and its slot-exchanged image

`WORD.txt` is the 322-contact word of
[#1908](https://github.com/mathorn1973/twist-j/pull/1908), and `sigma` its
image under the exchange of slots 1 and 2. The six-slot preparations are
those of #1908, with `u=1-j` (the element `pi` above), `B=1-j^2` and
`X=1+j-2j^3`. A contact on the slots `i` and `k` is written `ik`. On
`I_t=(tB,-tB,u,u,X,2)` every run ends at the complete target
`G_t=(u+tB,u-tB,0,0,X,2)`. `N6` is the number of admitted contacts touching
slot 6.

| run | admitted | refused | N | diagonal | N6 | Q | H |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| w, t=-2 | 137 | 185 | 135 | 2 | 40 | 1330 | 530+270 phi |
| w, t=-1 | 177 | 145 | 170 | 7 | 65 | 655 | 275+105 phi |
| w, t=0 | 112 | 210 | 100 | 12 | 40 | 380 | 160+60 phi |
| w, t=+1 | 177 | 145 | 170 | 7 | 65 | 655 | 275+105 phi |
| w, t=+2 | 123 | 199 | 123 | 0 | 40 | 1155 | 460+235 phi |

The run of `sigma` at `t` equals the run of `w` at `-t`. The first four
count columns replay the public table of #1908.

**Two paths at a common counter.** On `I_-2` the words `w` and `sigma` share
the start, the complete end `G_-2` and the number 322 of attempted contacts.
They differ in their course:

```text
N: 135 against 123, difference 12 = 2 mod 5      (admitted 137 against 123)
Q: 1330 against 1155, difference 175 = 5*35
H: difference 70+35 phi = 5 (14+7 phi)
```

The closed word `w` followed by the literal inverse of `sigma` has 1610
attempts, `N=627`, 629 admitted contacts, `Q=5950`, `H=2370+1210 phi`:
count 2 modulo 5, both accounts 0 modulo 5.

**A blind consequence of Proposition K.** The residues of the bank are
`(0,0,0,0,0,2)` and slot 6 returns. By (K2) and (K1), `Q=2*N6` modulo 5 and
`Q=0` modulo 5 in every run, so `N6` must be a multiple of five and every
admitted contact inside slots 1 to 5 must have `q(t)=0` modulo 5. The columns
`N6`, `Q` and `H` had not been computed or read before the recon text was
frozen. All ten runs agree.

### Path-difference lattices on orbits

For a root state let `D` be the set of differences
`(N,A,B)(gamma1)-(N,A,B)(gamma2)` over pairs of words from the root with a
common end. `D` is a subgroup of `Z^3`; it is generated by the spanning-tree
defects of the orbit graph. All fifteen pair contacts of the six slots are
generators.

| root | states | basis of D, rows (N; A, B) | D |
| --- | ---: | --- | --- |
| `I_0` | 2060, complete | (5; 5, 0), (0; 5, 5) | rank two, N in 5Z |
| `I_1` | 20400, complete | (1; -30, -15), (0; 5, -5), (0; 5, -10) | Z x 5Z x 5Z |
| `I_-2` | first 200000, capped | (1; 10, 5), (0; 10, -15), (0; 5, -10) | Z x 5Z x 5Z on the explored part |

On the complete orbit of `I_1` every element of `Z x 5 Z[phi]` is the
difference of two actual words with common endpoints. In particular there
are two words from `I_1` with the same end and the same `H` whose counts
differ by one. The count and the Hermitian sum are independent there.

Further audits:

- all 343 three-slot banks with entries in `{0,1,2,u,-u,B0,-B0}`, `B0=1-j^2`:
  orbits of 1 to 13 states, `N` has no holonomy modulo 5 (the admitted count
  has, through diagonal contacts, in 145 of them);
- 400 seeded random three- and four-slot banks, orbits capped at 20000
  states (188 reach the cap): no pair of words violates (L3); 191 banks show
  count holonomy.

### Explicit witnesses

The shortest closed word at `I_1=(B,-B,u,u,X,2)` whose count is not a
multiple of five has 27 contacts, all state changing:

```text
P27 = 12 12 12 12 35 36 16 16 16 16 46 46 46 46 24 36 36 36 36 16 12 12 46 45 45 45 45
N=27=2 mod 5,   H=55+20 phi=5(11+4 phi),   Q=130
```

Its word matrix fixes `I_1` and has determinant `rho^27=rho^2`. Padding it
with eight refused attempts on the pair 13 and comparing with

```text
P35 = 12 (five times), then three times: 35, 36 (five times), 35 (four times)
```

gives two closed paths at `I_1` with the same 35 attempts, the same
`H=55+20 phi` and `Q=130`, and counts 27 and 35. `P35` is built from trivial
returns `C^5=I` only.

## The fired hypothesis

The frozen recon text declared the hypothesis H_AREA: on closed words the
count modulo 5 is a linear function of `(A,B)` modulo 5, with the falsifier
"a closed word with `(A,B)=(0,0)` and nonzero count modulo 5". It fired on
the closed word of `w` and `sigma` at `I_-2` and on the complete orbit of
`I_1`. By (L2) it must fire on every orbit with count holonomy.

## Not claimed

- Any realization of the contact, its schedule or its admission rule by the
  native update.
- That `q`, `H` or the swept area is a physical energy or action, or that
  the count is a physical phase. The sentence "the count is the phase of one
  quantum and `H` is the action of the amplitude" is a reading, with no
  registered dictionary behind it.
- Minimality beyond the stated breadth-first search for `P27`, completeness
  for the capped orbit, or any statement about other contact laws.
- A Planck normalization or a value of alpha.
