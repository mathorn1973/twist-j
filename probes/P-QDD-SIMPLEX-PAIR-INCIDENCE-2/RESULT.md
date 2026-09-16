# Result: P-QDD-SIMPLEX-PAIR-INCIDENCE-2

Status: T
Scope: L4 regular-simplex support and scalar reading.
Public lock: #879.
Immutable scientific pin: `2acf78ea5fbffaa93811b89f2ec44be14b907fb9`.
Predecessor: `P-QDD-SIMPLEX-PAIR-INCIDENCE-1`, ABANDONED, not reused.

## Theorem result

The written proof establishes, for every integer `N>=2`, every regular-simplex
setting k, every bijection beta onto the remaining vertices, and every integer
source z:

```text
U = N(N-1)
A = (sum z_i)^2
B = N * sum_(i<j) (z_i-z_j)^2
D = A+B
```

with `U` the least positive universal integer lift that makes both the prepared
simplex relation x and its LOW projection integral. The primitive integral LOW
ray generator is `a_k=N e_k-1`, with `q(a_k)=U`.

The exact branch identities are

```text
q(P_k x) = A/U
q(Q_k x) = B/U
q(x)     = D/U
```

and, for the integral lift `X=U x`,

```text
q(P_k X) = U A
q(Q_k X) = U B
q(X)     = U D.
```

The same source has literal ordered Cartesian-pair cardinalities A in the LOW
sum-amplitude fibre and B in N labeled copies of all source-difference fibres.
Therefore the chosen second-order pair census and the quadratic P/Q scalar
reading are mathematically identical on this family.

The lift retains the complete prepared source:

```text
z_i = (X_(beta(i)) - X_k) / U.
```

The ordered branch pair reconstructs X by `P_k X + Q_k X = X`.

For nonzero source, the normalized values are exactly A/D and B/D. Zero has no
normalized ratio; zero sum kills LOW; HIGH vanishes exactly on all-equal source
coordinates.

## TWIST-J specialization

At `N=p=5`,

```text
U = 20 = 5*4 = q(5 u_k)
A = s^2
B = 5(4 S2-s^2)
D = 4(5 S2-s^2)
q(P_k x) = A/20
q(Q_k x) = B/20
q(x) = D/20.
```

For public `k=2,beta=(0,1,3,4)`, A, B and D are the already-public incidence
cardinalities and P/Q are the already-public stabilizer projectors. Their p=5
scalar equality is prior public mathematics and is not claimed anew here.

The new result is the uniform regular-simplex theorem, the forced minimal
integral scale `N(N-1)`, the primitive-ray interpretation of 20 and exact source
recovery. In particular the factor 20 is not introduced to normalize the known
QDD ratio after the fact.

## Scientific interpretation

Provisional future registry name if folded:

```text
QDD-SIMPLEX-PAIR-READING-EQUIVALENCE [T]
```

The theorem supplies a structural reason for the existing quadratic decoder
choice: it is exactly a second-order Cartesian-pair reading of the integer
relation, expressed in regular-simplex norm coordinates.

This is **not** a uniqueness theorem. It is compatible with the merged public
result that other positive additive mathematical frame readings exist. The
program may choose the quadratic branch without claiming that arithmetic
forbids every other question.

## Audit

The completed local formal run produced:

```text
104768 exact assertions
2560 contexts
exit 0
stderr 0 bytes
stdout 340 bytes
stdout SHA-256 6ca17fe44c2aeb9824f193a3b206d2b554450f59f4449c1323942b21b0e34f6f
```

The finite audit includes the complete 625-source public box in the canonical
context, all 120 p=5 setting/beta contexts on frozen witnesses, regular-simplex
witnesses through N=8, primitive scales through N=32, direct pair-set counts,
and an out-of-slot source control. Universal scope comes from PROOF.md, not
finite enumeration.

GitHub x86_64 and aarch64 byte-identity checks are required on the pull request
before merge.

## Hard boundary

No physical QDD owner moves. This theorem supplies no physical effect,
apparatus, ready state, coupling, pointer, reduction, exclusive event,
occurrence or sampling law, post-state selection, reset, L5 stream or L6
measure. It does not derive source capture from native `Omega,U`.

Accordingly `QDD-INSTRUMENT-APPARATUS`,
`QDD-INSTRUMENT-CLASS-COMPLETENESS` and
`QDD-TERMINAL-EVENT-SEMANTICS` remain open at their existing scopes.
