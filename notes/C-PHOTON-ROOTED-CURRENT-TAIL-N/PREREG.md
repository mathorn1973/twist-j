# Preregistration: rooted-current certificate and conditional tail constants

**PUBLIC, NON-CANONICAL. No authority or earned claim.**
**Candidate:** C-PHOTON-ROOTED-CURRENT-TAIL-N.
**Owner:** A. M. Thorn / photon_scope; issue
[#1324](https://github.com/mathorn1973/twist-j/issues/1324).
**Date:** 2026-10-01. **Action layer:** L6 finite-measure mathematics.

## 1. Frozen scope and prior exposure

This is a proof-first, known-target review of a written lower bound for the
full rooted current moment, its consequence for one specified infrared
certificate, and conditional tail-to-moment constants. It is not an upper
tail theorem. The author has already derived the proposed statements in
CONTRACT.md; this preregistration does not retroactively make that derivation
blind or prospective. No scientific computation has been executed for this
candidate, and no numerical sampling result is an input.

The coordinator has exposedly checked the lower-bound reasoning against the
Canon source. That is preparatory review, not independent proof or independent
implementation. A fresh review must follow REVIEW_SPEC.md.

The scientific base is public main
`44423153eee6259c7277eec5f5adbed9679f9146`, Public Canon v96; declared
content commit `d63de7e7345cf5fa5ab344654aafb7238d6d8bca`. Canon is 873495
bytes with SHA-256
`eb2a7bc1c7e38e130544b9fef4c0f05443df01484bdb55a52fc10b427fcee0a2`.

The candidate pin is the first immutable public commit containing this file,
REVIEW_SPEC.md and the unchanged author draft CONTRACT.md. The coordinator
records its full SHA and these file hashes in issue #1324 after public
readback. That record, not a self-referential placeholder here, identifies
the frozen candidate. No review or gate is represented as completed here.

## 2. Allowed scientific inputs

Use exactly these source snapshots at the base commit. Their statuses are
not promoted by use. All other historical diagnostics are excluded as
evidence for these targets.

| Source | Admitted content | SHA-256 |
|---|---|---|
| `canon/CANON.md` | PHOTON-CONDITIONAL-VARIANCE-FLOOR only: finite model, linear-observable variance lemma, 21-face defect and ordered-profile floor | `eb2a7bc1c7e38e130544b9fef4c0f05443df01484bdb55a52fc10b427fcee0a2` |
| `notes/C-PHOTON-BCHI-DIRECT-BOUND-N/CONNECTED-CURRENT.md` | Exact paired augmentation and its normalization, component currents and conditional signs; NON-CANONICAL | `7ce7bdf7501e0e4b56de806a59b47ea53efc333cb141753c9d253576c211f0fe` |
| `notes/C-PHOTON-WHOLE-CURRENT-MOMENT-N/PROOF.md` | Definitions of ell, Xi and R3; deterministic whole-current reduction chi<=Xi<=R3/16; NON-CANONICAL | `82029583a8f27acfeec0461edf1c10d01613a2966aecc772a1264770b3a5054b` |

REVIEW_SPEC.md supplies the complete candidate carrier and targets without
the author's new derivation. CONTRACT.md is the author construction and is
withheld from the fresh reviewer until the independent written derivation is
frozen. Its unchanged SHA-256 is
`72250ffaefe50e075994ba9b4ba1fe7eb88e45afc714c3171f93900424b5748d`
and its byte count is 18442. No verifier, expected stdout, prior simulation,
historical diagnostic or builder implementation belongs to the initial
review input set. Repository policy and authority files remain required
procedural inputs.

## 3. Carrier, normalization, equality and systematics

The carrier is the complete ternary plaquette measure on every even periodic
four-torus L>=4, with V=L^4, 6V canonical plaquettes, 4V canonical positive
edges, constraint partial n=0 modulo five and weight
mu_L(n)=Z_L^-1 2^(-|supp n|). All current, exterior and winding sectors remain
included. Signed fields have literal coordinate equality.

Conditional on the whole n, every neutral degree-2r edge independently draws
one of its r! positive-to-negative incidence matchings uniformly. At each
degree-five charged edge all five occupied faces join. K is the resulting
paired face component, M_K its complete number of charged edges, and K(e)
the owner of charged edge e. Uncharged rooted contributions are zero. The
unsigned measure has literal labeled-support-and-pairing equality and weight

```
P_aug(S,M) = Z_L^-1 1_consistent 2^(k(S,M)-|S|)
                         product_(e:d_e even) 1/(d_e/2)!.
```

The signed and unsigned descriptions must have exactly the same Z_L.
Arbitrary neutral joins, edge-capacity restrictions, nonunique cycle
decompositions and compensating winding cycles may not be removed. There
is no statistical error model, fit, floating-point tolerance, selected
sector, finite-volume extrapolation or tunable post-result cutoff.

## 4. Frozen equations and conclusions to review

Write N=4V, p_(L,e)=P_mu(j_e!=0), j=partial n/5,
T_(L,e)(r)=P_aug(e charged,M_K(e)>=r), and

```
R3(L) = (4V)^-1 sum_e E_aug[1_(e charged) M_K(e)^3],
rho = 1/(36*2^41).
```

**G1. Charged-root lower bound.** For every L and canonical edge e,

```
p_(L,e) >= 2^-41.
```

The new proof must justify sign symmetry and the linear-observable
conditional-variance application on the complete exterior distribution.

**G2. Component support and moment lower bound.** Every nonzero component
current has M_K in {4,6,...,N}, and

```
R3(L) >= 2^-35.
```

**G3. Specified certificate limitation.** If a future theorem supplies
R3(L)<=C on all admitted volumes, using the inherited chi_upper=C/16 and
exactly the published b_lower=25rho gives

```
C>=2^-35,   C/16>=144rho,
b_lower-25chi_upper = -D(C),
D(C)=25(C/16-rho)>=3575rho>0.
```

This is not a statement that the actual b-25chi is nonpositive. A transverse
lower certificate used with C/16 must exceed 25C/16 to prove a strict margin.

**G4. Exact finite tail identity and exponential constant.** With
d_r=3r^2-3r+1,

```
R3(L)=(4V)^-1 sum_e sum_(r=1)^N d_r T_(L,e)(r).
```

If T_(L,e)(r)<=Aq^(r-1) uniformly, with A>=0 and 0<q<1, then R3<=A F_N(q),
where F_N=sum_(r=1)^N d_r q^(r-1), and

```
F_infinity(q)=(1+4q+q^2)/(1-q)^3,
F_infinity-F_N=q^N[(3N^2+3N+1)/(1-q)
                  +(6N+3)q/(1-q)^2+3q(1+q)/(1-q)^3].
```

For the alternative convention Aq^r the bound is multiplied by q.

**G5. Polynomial constant.** If T_(L,e)(r)<=C0 r^(-3-epsilon) uniformly,
with C0>=0 and epsilon>0, then the exact finite majorant is

```
C0[3H_N(1+epsilon)-3H_N(2+epsilon)+H_N(3+epsilon)],
H_N(s)=sum_(r=1)^N r^(-s).
```

The infinite majorant replaces H by zeta, is at most C0(1+3/epsilon), and
its positive tail beyond N is at most 3C0 N^(-epsilon)/epsilon.

**G6. Conditional even-size contraction implication.** Suppose, as an
additional unproved premise, one theta in [0,1) satisfies

```
T_(L,e)(6+2k)<=theta T_(L,e)(4+2k),  all L,e,k>=0.       (H)
```

If p_(L,e)<=p_* uniformly, including the unconditional choice p_*=1, put
Kmax=2V-2 and a_k=24k^2+72k+56. Then

```
R3(L)<=p_* G_Kmax(theta),
G_K(theta)=64+sum_(k=1)^K a_k theta^k,
G_infinity(theta)=(64-40theta+32theta^2-8theta^3)/(1-theta)^3,
G_infinity-G_K=theta^(K+1)[a_(K+1)/(1-theta)
                         +(48(K+1)+72)theta/(1-theta)^2
                         +24theta(1+theta)/(1-theta)^3].
```

The underlying conditional probability interpretation applies only when the
denominator event has positive probability; the undivided inequality covers
zero denominators without division. Neither (H) nor any full-measure upper
tail constants are asserted as results.

## 5. Code, review procedure and failure rules

No computational verifier is included or required: the targets are written
elementary finite-measure and series identities. No scientific execution is
authorized by this preregistration. Static file checks and custody hashes
are procedural checks, not scientific evidence. An optional finite audit
would require its own prospective frozen scope and procedure before running.

The fresh reviewer receives this preregistration, REVIEW_SPEC.md and the
three allowed source snapshots, with their immutable pins. The reviewer
must disclose prior exposure and freeze an independently authored written
derivation before opening CONTRACT.md or its detailed diff. No independent
implementation or result-blindness is claimed merely because the target
constants are known. The subsequent comparison must identify the exact
claim accepted, rejected or left blocked.

An exact admitted counterexample to G1-G6 rejects the corresponding claim.
For G4-G6 a counterexample must obey its displayed antecedent; failure of
the actual measure to obey an unproved antecedent does not refute the
conditional implication. An unsupported proof step is a proof gap and
blocks acceptance until disposition; it is not automatically a counterexample.
Frozen targets, domains and constants are not weakened after rejection.
Corrections requiring changed frozen content follow the repository's
successor/disposition rules. Passing finite examples cannot replace any
all-L, all-root or real-parameter proof.

Success means a complete written proof at precisely this scope and an
independent review of the frozen candidate. The prospective ceiling is
candidate-T for those scoped analytical statements, never Canon authority.
No finite-audit or two-architecture claim is requested.

## 6. Limit and repository boundary

The retained finite floors are
c_L=2^-41 floor(L/3)^2/(4L^2),
rho-2^-41/(6L)<=c_L<=rho, and
S_n,02,02^L(t e_1)>=25rho-25*2^-41/(6L)-10rho t^2.
Any use of b or chi is conditional on the originally specified nonempty
joint ordered-profile family: thermodynamic limit first at fixed nonzero
limiting t, then infrared limit. Profile existence, Fourier identification
from local convergence and limit interchange are not targets.

Only `notes/C-PHOTON-ROOTED-CURRENT-TAIL-N/` is this candidate's authoring
scope. The original CONTRACT.md is retained unchanged as known-target
author exposition. Uniform R3 boundedness remains unresolved. The exact
whole-moment reduction remains NON-CANONICAL; the broader #1122/#1143
owners, P1, PHOTON-MASSLESS-PHASE and the physical photon bridge retain their
existing status. No Canon, registry, gate, policy, workflow or release edit
is authorized by this note.
