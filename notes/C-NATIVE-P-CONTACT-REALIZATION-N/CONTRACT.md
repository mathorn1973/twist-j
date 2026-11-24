# Complete comparison contract and unresolved native fields

**PUBLIC / NON-CANONICAL / L1.**
A. M. Thorn. SPDX-License-Identifier: Apache-2.0.

This is the released #1628 target, specialized to one nonempty shell for
a prospective native implementation. Its mathematical reference identities
hold on the whole family below. A native implementation is not supplied.

## 1. Full comparison state and equality

Use ordinary integers for q,p,u,v and the bank. Use F5 for mu,alpha,beta,tau.
Equality is coordinatewise equality of the entire tuple, not a quotient
by phase, cost, clock, preparation or observed output.

```text
s = (mu,q,p,u,v,alpha,beta,tau)
ell(0,1,2,3,4) = (0,1,2,-2,-1)
epsilon(0,1,2,3,4) = (0,1,0,0,-1)
h = epsilon(mu)
H_P(s) = q^2+p^2+u^2+v^2 + 2 ell(mu)^2
y = (s,b,c,d), 0 <= b <= B, c in {0,1}, d in {+1,-1}
Y_(E,B) = {y : H_P(s)+b=E}
```

The nominated implementation target is the ENTIRE `Y_(8,3)`, including
all source symbols that satisfy the shell equation, every Weyl label,
occupied references, both vertices, both directions, and every refusal.
The reference proof also covers every integer E,B >= 0. This uniform
reference theorem is not a uniform native-realization claim.

Every other content/reference/archive of #1627 is a retained spectator
`sigma`, fixed arbitrarily before a run, with equality and the identity
transition. Its full original cost `C_sigma` is retained, so the total
account is `E+C_sigma`. No varying unbounded spectator belongs to the
claimed finite local shell. An optional varying spectator would require
an independently bounded factor and its account before a later pin.

## 2. One edge and its total controller

For k in {-1,0,1}, with mu unchanged, set

```text
P_k(s) = (mu,q,p+k,u+k*q,v+k*q,alpha+k,beta,tau)
Delta_k(s) = 2*k*(p+q*(u+v)) + k^2*(1+2*q^2)
```

Only alpha is reduced modulo five in this formula. Forward traversal
uses k=h; reverse traversal uses k=-h at its actual input, with the same
retained mu. No external sign is substituted.

The pairing H_e is defined on the complete shell:

| Input (c,d) | Proposal | Acceptance |
|---|---|---|
| (0,+1) | (P_h(s), b-Delta_h(s), 1,-1) | Both bank bounds hold |
| (1,-1) | (P_-h(s), b-Delta_-h(s), 0,+1) | Both bank bounds hold |
| (0,-1), (1,+1) | Input itself | Outward endpoint |

An out-of-range proposal fixes the entire input under H_e. Let
`D(s,b,c,d)=(s,b,c,-d)`; the full local tick is `F_P=D H_e`,
with inverse `H_e D`. Refusal leaves s,b,c unchanged and reverses d.
An accepted h=0 edge still advances c and retains d under F_P.
Endpoint reflection is part of the machine, not an external reset.

The local controller replaces only the comparison of this one edge. It
does not implement the other 24L-step source gates.

## 3. Weyl semantics and actual receiver record

Fix `X e_t=e_(t+1)`, `Z e_t=j^t e_t` and
`R(alpha,beta,tau)=j^tau Z^alpha X^beta`, with `ZX=jXZ`.
Operator equality includes the central phase. An accepted forward edge
left-multiplies by `Z^h`, the accepted backward edge by `Z^-h`.
A refused or outward endpoint edge supplies I. The integer and label
updates are inseparable parts of the same proposal.

The comparison present-record read is
`r_P(s)=sgn(u^2-v^2)`, with sgn(0)=0. It is defined on all occupied
states and refusals. This mathematical read is not an admitted native
detector or a statement that every occupied state decodes the source.

The exposed accepted witness uses E=8, B=3, b=3, c=0, d=+1, common
`(q,p,u,v)=(1,0,1,-1)`, common phase `(0,0,0)`, common sigma,
and mu=1 versus mu=4. Both have H_P=5 and Delta=3. The outputs are

| Source | (q,p,u,v) | Bank | (c,d) | Phase | u^2-v^2 |
|---|---|---|---|---|---|
| mu=1 | (1,1,2,0) | 0 | (1,+1) | (1,0,0) | 4 |
| mu=4 | (1,-1,0,-2) | 0 | (1,+1) | (4,0,0) | -4 |

These are exact analytical substitutions supplied by the assignment, not
blind predictions or observed execution outputs.

## 4. Clock and prospective implementation equality

For a future common fixed positive integer k, use the nonempty
forward-closed start set `N={3,4,5,...}` and target

```text
Fhat_P(n,y,sigma) = (n+k,F_P(y),sigma).
```

Its inverse exists on the image n>=3+k and uses F_P^-1; it is not globally
surjective on the forward carrier. A native slice may depend on n, but
must be an explicitly admitted slice.

A realization must supply X,V,Enc,Dec and prove, for every n in N and
every y in Y_(8,3),

```text
Dec Enc(n,y,sigma) = (n,y,sigma)
V^k Enc(n,y,sigma) = Enc(n+k,F_P(y),sigma).
```

It must also prove the corresponding inverse on the actual image, code
image invariance and faithful preservation of every auxiliary residue.
If auxiliaries change, their complete state and transition must enlarge
the comparison BEFORE a computational pin. A variable-duration proposal
needs a separate first-return contract.

The fixed encoding grammar may use its admitted native chart at n.
It may not evaluate target iterates to preload future answers, supply
a state-by-time table, or select a cycle relabeling after inspecting F_P.
An arbitrary global conjugacy is not an admission certificate.

## 5. Required native receiver separation

A future implementation must fix disjoint coordinate sets S_N,R_N and
their projections, with all prepared coordinates outside S_N identical
for the paired witness, including all of R_N, auxiliaries and controller.
Disjoint coordinates need not be independent dynamical subsystems.

The only permitted external common context here is the common present
clock n and fixed parameters E,B,sigma. No source-dependent context,
loader, program bit, archive or future answer
is permitted as unaccounted external/common context. Declared internal
resources require their own accounted dynamics and access rules.
Any additional context or memory that changes with received data belongs
to R_N and the complete resource account.

One present function rho of the clock, R_N projection and this common
context must agree with r_P throughout the complete encoded domain.
At the two witness outputs it must give +1 and -1. Decoding the record
from the complete global state, which already contains mu, is insufficient.

No concrete native S_N,R_N, Enc or rho is certified here. The comparison
ports `{mu}` and `{u,v}` are not native-coordinate assignments.

## 6. Resource inventory and missing-field register

| Resource | Comparison inventory | Native admission |
|---|---|---|
| Source | One retained F5 symbol mu, price 2 ell(mu)^2 | Actual source chart exists; its coupling to this target is missing |
| Geometry and references | Four integers q,p,u,v, all occupied values on the shell | No supplied faithful native realization of this full tuple and transition |
| Weyl record | Three F5 labels, 125 states, zero varying price | Algebraic representation; native update mechanism missing |
| Bank | Four values 0,1,2,3 at B=3 | Encoding, exact arithmetic, guard and inverse implementation missing |
| Local controller | Four (c,d) values, zero varying price | Comparison rule supplied; native calendar/actuation missing |
| Clock | One unbounded original n, zero varying price | Original clock exists; common k and full intertwining not supplied |
| Spectators | Fixed arbitrary sigma, cost C_sigma | Native preservation must be proved with the encoding |
| Auxiliary storage | None added to the comparison | A future implementation must declare any requirement and transition |
| Preparation | Entire shell as admissible comparison starts; named pair has equal nonsource resources | Full-shell native preparation and the source-local common-ready witness not supplied |
| Read/cost | r_P and H_P+b+C_sigma | Native port, present rho, complete native cost and relation missing |

The four integers are bounded on a fixed shell. All other local factors
are finite, hence Y_(8,3) is finite and nonempty. This does not price their
physical preparation or establish a sufficient number of native cells.
No native cell count m, complete coupled alphabet, common k, encoding
grammar, full native account or local native receiver can presently be
certified from the inspected inputs.

Those fields are explicitly UNSUPPLIED, not implicitly chosen to fit the
target. The missing independently admitted common carrier/contact interface
triggers STOP_ADMISSION_UNSUPPLIED before search. The exact remaining
proof obligations are preserved rather than filled with guessed gates.
