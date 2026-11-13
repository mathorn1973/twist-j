# Reference proof and restricted native boundaries

**PUBLIC / NON-CANONICAL / L1. Authored candidate-T pending review.**
A. M. Thorn. SPDX-License-Identifier: Apache-2.0.

These are analytical arguments. No scientific executable or enumeration
was used. The reference matching argument is inherited from #1627 and
specialized to #1628; it is not claimed as a new autonomous native mechanism.

## 1. Full occupied P inverse and account

Let A=p+q(u+v) and C=1+2q^2. Since P_k fixes q and mu, applying P_-k
after P_k restores all four integers and all three phase labels.
The source cost 2 ell(mu)^2 is retained and cancels from the difference.

Expanding the three changed squares gives

```text
(p+k)^2-p^2 + (u+kq)^2-u^2 + (v+kq)^2-v^2
  = 2k[p+q(u+v)] + k^2(1+2q^2)
  = Delta_k(s).
```

After P_k, A'=A+kC, hence

```text
Delta_-k(P_k(s)) = -2k(A+kC)+k^2 C = -Delta_k(s).
```

The identities hold for arbitrary occupied u,v and all mu, including
the zero-control symbols. No source value, reference or old phase
label is erased.

## 2. Pairing, both bank bounds and all inverse branches

An accepted H_e edge maps bank b to b'=b-Delta_k(s).
At its opposite vertex/direction the prescribed inverse gate has bank

```text
b' - Delta_-k(P_k(s)) = b.
```

The original b lies in [0,B], so the return is accepted. Thus accepted
points occur in exact two-point pairs (even if the DATA gate is identity,
the vertices differ). Refused points and outward endpoints are fixed.
An accepted point cannot land at a refused point, because its return
bank is admissible. Therefore H_e^2=I on the ENTIRE domain.

D^2=I immediately. Consequently F_P=D H_e is bijective with inverse
H_e D. H_e preserves H_P+b by the difference formula and D changes only
a zero-priced direction. Spectators are unchanged with their costs intact.
Both-bank admissibility is essential; it is not enough to test b'>=0.

For h=0, Delta=0 and an inward edge always accepts. Its data stay fixed,
but the controller follows

```text
(0,+1) -> (1,+1) -> (1,-1) -> (0,-1) -> (0,+1).
```

In general accepted F_P steps retain direction and change vertex.
Refusals and outward endpoints reverse direction without any data,
phase, bank or vertex change. These statements describe complete states,
not just their observed account.

## 3. Entire finite shells and the advancing clock

For fixed E,B>=0, every integer coordinate of Y_(E,B) has square at
most E. The bank, source, Weyl labels and local controller have finite
ranges. Hence the shell is finite, and section 2 makes F_P a permutation
of the entire shell. This proof does not require enumerating it.

Fixed arbitrary spectators add C_sigma, not an omitted cost.
An unbounded varying spectator or the original advancing n would destroy
the asserted finiteness. For fixed positive k, Fhat_P is injective on
n>=3 with inverse (n,y,sigma) -> (n-k,F_P^-1(y),sigma) only for n>=3+k.
It is not surjective onto the starting-time carrier. Finiteness or
recurrence of the core implies neither for the complete clock state.

## 4. Occupied Weyl labels

For any alpha,beta,tau in F5,

```text
R(P_k(s)) = j^tau Z^(alpha+k) X^beta = Z^k R(s).
```

No extra central phase appears in this left-ordered convention.
The reverse edge supplies Z^-h. A refusal or endpoint changes no label
and supplies I. All phases, including tau, remain in full-state equality.

The label reading is faithful: the output basis index determines beta;
the ratio of phases on successive input indices determines alpha; then
tau is determined. Equality of labels is not equality only up to phase.

## 5. Exact nontrivial shell witnesses

On Y_(8,3), take the pair in CONTRACT section 3. Its initial geometric
cost is 3 and retained source cost is 2, so H_P=5 and b=3.
For h=+1 or -1, A=0,C=3 and Delta_h=3. Both transitions accept.
The references become (2,0) or (0,-2), giving squared differences
4 or -4. The bank becomes zero and the reverse accepted proposal
returns it to 3. Mu and all spectators remain unchanged.

The SAME shell also contains the following analytical branch examples,
with any common phase label and inward controller (0,+1):

| Branch | mu | (q,p,u,v) | H_P | b | Delta_h | Proposed b |
|---|---|---|---|---|---|---|
| Lower-bank refusal | 1 | (0,2,1,0) | 7 | 1 | 5 | -4 |
| Upper-bank refusal | 1 | (0,-2,0,0) | 6 | 2 | -3 | 5 |
| Zero control | 2 or 3 | (0,0,0,0) | 8 | 0 | 0 | 0 |

Each rejected example retains its complete data and reverses direction.
These substitutions do not constitute an executed shell census.

For arbitrary occupied references the actual change in the record is

```text
(u+hq)^2-(v+hq)^2 = u^2-v^2 + 2hq(u-v).
```

The sign therefore need not equal the source on arbitrary occupied
inputs. The receiver obligation is to read the actual record throughout
the domain, and to distinguish the nominated pair. It is not a five-symbol
transmission claim or a claim that every occupied record reports mu.

## 6. Restricted inherited-chart no-acquisition boundary

Use the prepared chart of #1627 PROOF section 1. Its fixed receiver
port is (b_N,d_N,q_N,r), where, in F5,

```text
B_N=3A, kappa=Az, D_N=kappa(1+3 lambda),
b_N=3(B_N+D_N+1), d_N=3(B_N-D_N-1),
q_N=z-4A-r.
```

Here gamma=(A,z,r) is common. These receiver coordinates depend only on
lambda and gamma, never mu. Changing mu affects the other piston pair
(a_N,c_N). Original continuation preserves both contents (mu,lambda)
and updates the same gamma for both preparations.

Thus two such cells with common gamma,lambda and differing mu have
identical literal receiver ports at every common future native time.
Any present function of that port and common clock/context returns
identical outputs. It cannot produce the opposite P-record signs for
the nominated pair. Waiting longer in this literal chart/port subclass
cannot supply the missing contact.

This is an inherited specific boundary, not a universal no-go. It does
not cover arbitrary native-coordinate partitions, other preparations,
structural encodings, coupled alphabets or admitted extensions. In
particular #1617's centered-block transfer has different hypotheses.

A related product argument holds when every complete cell contributing
to the receiver has the same initial checkpoint in both preparations
and evolves independently with common clock/context. Induction preserves
those complete checkpoints' equality. Merely disjoint coordinate sets
within one cell do NOT imply this premise: the original selector depends
on the sum of all six coordinates and can communicate across such a split.

A fixed, injective storage map E(y) into conserved synchronized native
chart labels likewise cannot implement a changed F_P by waiting:
unchanged U preserves E(y), whereas the required equality would give
E(y)=E(F_P(y)), hence y=F_P(y). The paired witness changes y.
This rules out that static-label encoding only. Target-dependent clock
decoders, other encodings and added interactions require their own
admission analysis; no arbitrary-encoding exclusion follows.

## 7. Closed receiver read versus a contact input

Suppose two runs have identical initial z and the same deterministic
closed read law z_(t+1)=A_t(z_t), with the same permitted common context.
Induction gives equal z histories. Any common decoder of z_t or that
history returns equal outputs and cannot recover two distinct records.
A constant A_t=T and a common unbounded clock do not change the proof.

If z=g(n,R) is noninjective, equal z histories do NOT imply equal raw
receiver histories R, and do not exclude another richer present read
rho(n,R). An explicit contact input to the recurrence also violates the
closed-receiver premise. The lemma does not require T to be the isolated
receiver's step during the P contact and imposes no such extra requirement.

The canonical finite-reader and counter-amplitude results remain
inherited statements with different target operators and domains.
Neither is re-proved here as a positive deliverable.

## 8. Logical disposition

Sections 1-5 establish the complete conditional comparison target,
not its native implementation. Sections 6-7 delimit only their stated
subclasses. The adjacent conditional alphabets do not provide the
full missing interface listed in ADMISSION.md. A search on guessed
gates would violate the assignment's prospective admission rule.
The supported final disposition is STOP_ADMISSION_UNSUPPLIED, with
the full native P-realization question open.
