# C-J A/U5 coincidence-channel owner freeze (NON-CANONICAL)

```text
STATUS:                  OWNER-ADOPTED PHYSICAL-ROUTE RULING /
                         PRE-HYPOTHESIS FREEZE
AUTHORITY:               NOT CANON
SCOPE:                   PROPOSAL-LOCAL / ROUTING ONLY /
                         NO FREQUENCY-LAW ADOPTION
OWNER DECISION:          SPLIT A/U5
COUNT CHANNEL:           A, integral
NORMALIZED PROFILE:      U5=A/sqrt(5)
POSITIVE POLAR CHANNEL:  B, separate and open
RAW J RECORD INPUT:      FORBIDDEN BY THIS FREEZE
COINCIDENCE-RECORD-FREQUENCY:
                         CANDIDATE-H / UNTESTED / STOP
QDD-INSTRUMENT-APPARATUS: O / STOP, unchanged
FORMAL RUN:              NONE
CANON CHANGE:            NONE
REGISTRY CHANGE:         NONE
DEPENDENCY CHANGE:       NONE
GATE CHANGE:             NONE
PUBLIC BASE:             Public Canon v75
PUBLIC CANON TAG:        canon-v75
ACTIVATION COMMIT:       c4f00e1d9c89f503d913224dc3c09dc760dcec9d
CONTENT COMMIT:          e32e85ed7297d4320df5b345e4488d78323d550c
CANON SHA-256:           44130160a3ce29bfcdc757e255d2d1c25a010b22911edfe66cf6b132be081fbe
CANON BYTES:             399513
PUBLIC MAIN BASE:        a7ef8ba676a7a26ebac4b0d5a0b31c47bc41cc9c
OWNER RULING DATE:       2026-09-04
```

This note records the owner's answer to the fork left open by
`C-J-PLENUM-BORN-CHAIN-1-N`, refined by
`C-J-RESIDUAL-INTEGER-UNIT-1-N` and
`P-J-COINCIDENCE-RECORD-BOUNDARY-1`.

It resolves only the still-open routing choice in section 8 of the Born-chain
note. Every other authority boundary, mathematical caveat, and STOP in that
note remains in force. For this coincidence-count port it supersedes the
earlier candidate-H design preference for raw-`J` branch (a). It does not
declare raw `J` unphysical or alter its algebraic role outside this port.

The adopted route is:

```text
integral multiplicity evolution       A,
normalized coordinate-square profile  U5=A/sqrt(5),
positive polar evolution               B, in a separate open channel.
```

The raw map `J` is not admitted as the input of the coincidence-count port.
This is a physical routing choice. It is not an algebraic theorem, it does
not replace the algebraic identity for `J`, and it does not establish the
candidate frequency law.

## 0. Freeze firewall first

A continuation returns `FREEZE-BREACH / STOP` if, without a new explicit
owner ruling, it does any of the following:

1. feeds `Jd`, `J^n d`, `Bd`, or `B^n d` directly into the frozen
   coincidence-count port;
2. treats `U5 d` as a literal population of integer units;
3. calls `B` a scalar scale, a universal yield, or an invisible factor;
4. turns the commuting operators `U5` and `B` into tensor factors of the
   state space;
5. identifies a residual ordinal token across two read cuts;
6. derives complete Cartesian incidence from equal marginals or from the
   Cayley copy alone;
7. reports `COINCIDENCE-RECORD-FREQUENCY` as tested, confirmed, adopted, or
   Canon;
8. supplies a probability, stochastic seed, collapse, temporal ensemble,
   modal branch measure, or single-run random law;
9. assigns gravity, time, matter, detector, observer, or SI semantics to the
   open `B` channel;
10. changes Canon, Registry, Frontier, dependencies, gates, or `STATUS.md` by
    inference from this note.

An exact failure of an algebraic identity displayed below makes this route
internally inconsistent and returns `ROUTE-INCONSISTENT / STOP`. It is not a
Canon `F` result.

## 1. Inherited algebraic boundary

Let

```text
E_Z = Z^5,
V_Z = {d in E_Z : sum_k d_k=0},
q(d)=sum_k d_k^2,
A=1+g^2-g^3-g^4,
U5=A/sqrt(5).
```

On the real augmentation sector `V_R`, the confirmed identities are

```text
A^T A=5I-N,
q(Ad)=5q(d),
U5^T U5=I,
A^n d=5^(n/2) U5^n d,
q(A^n d)=5^n q(d).
```

The last two identities are real identities. Their left side is integral
when `d` is integral; the generally irrational vector `U5^n d` is not
thereby turned into an integer population.

For every supported nonzero `d in V_Z`, every `n>=0`, and every cell `k`,

```text
(A^n d)_k^2 / q(A^n d)
  =(U5^n d)_k^2 / q(U5^n d).
```

Thus `A` and `U5` carry the same normalized coordinate-square profile. Only
`A` carries the frozen literal integer multiplicities.

## 2. Adopted count channel

At an admitted integer read cut `n`, define

```text
a_n(d)=A^n d in V_Z.
```

The residual-unit convention is reapplied at that cut. For each coefficient
`a_(n,k)`, it creates a fresh signed ordinal fibre of cardinality
`|a_(n,k)|`. It does not trace a unit through the preceding update.

Two disjoint tagged copies of the fibre make the available complete
within-cell relation

```text
C_k^x(a_n)=U_k^S(a_n) x U_k^R(a_n).
```

Its mathematical cardinalities are

```text
N_(n,k)=|C_k^x(a_n)|=(A^n d)_k^2,
N_n=sum_k N_(n,k)=q(A^n d)=5^n q(d),
N_(n,k)/N_n=(U5^n d)_k^2/q(U5^n d).
```

The factor five is therefore a state-independent multiplier of total
available pair cardinality per `A` step. The single-unit total
`sum_k |(A^n d)_k|` has no such state-independent multiplier and is not the
frequency carrier.

The words `available`, `fibre`, `relation`, and `cardinality` in this section
remain L1 finite-set language. Physical realization still requires the sole
candidate-H row in section 5.

## 3. Normalized profile channel

The profile channel carries

```text
u_n(d)=U5^n d in V_R
```

only through its scale-free square profile

```text
pi_(n,k)(d)=u_(n,k)^2/q(u_n).
```

Equivalently, it may be regarded as the real ray of `u_n` together with the
marked cell basis. It is not a finite token population. The equality

```text
pi_(n,k)(d)=N_(n,k)/N_n
```

is an exact compatibility theorem between the integral count channel and
the normalized profile channel. It does not say that a ratio is an observed
frequency.

## 4. The separate positive polar channel

On `V_R`, let

```text
P_+=(I+H)/2,
P_-=(I-H)/2,
B=phi^-1 P_+ + phi P_-,
J=U5 B=B U5.
```

The full-register correction remains

```text
U5 B=B U5=J-(2/5)N.
```

The `B` channel is not a scalar scale. Its exact sector action is

```text
B^n d=phi^(-n) P_+d + phi^n P_-d,
q(B^n d)=phi^(-2n)q(P_+d)+phi^(2n)q(P_-d).
```

It changes the relative weights of two orthogonal sectors and generally
changes the marked coordinate-square profile. This is precisely why it may
not be silently discarded, absorbed into one universal gain, or passed into
the count channel.

The owner route preserves `B` as separate exact algebraic data while leaving
all of the following open:

```text
physical carrier,
source and preparation,
read law,
relation to an apparatus,
relation to a read cut,
coupling or feedback with the A/U5 route,
higher-layer and SI meaning.
```

The split is not a claim that

```text
V_R = V_profile tensor V_B.
```

Both `U5` and `B` act on the same `V_R`. Their commutation supplies the polar
factorization of an operator, not a tensor factorization of its carrier.

## 5. The sole physical hypothesis is unchanged

This owner ruling selects the route on which the hypothesis may later be
tested. It does not adopt the hypothesis:

```text
COINCIDENCE-RECORD-FREQUENCY [candidate-H / future L5-L6 / STOP]

At a frozen calibrated read cut for a supported nonzero integral preparation,
the physically realized record population is exactly C^x(a_n), with every
within-cell ordered pair realized once and no other record. The ensemble is
this simultaneous finite plenum itself, not repetition in time and not a set
of modal branches. Observed cell frequency is finite self-location in this
record population:

f_(n,k)=|C_k^x(a_n)|/|C^x(a_n)|
       =(A^n d)_k^2/q(A^n d)
       =(U5^n d)_k^2/q(U5^n d).
```

The row still does three physical jobs: it selects complete incidence,
declares every selected pair realized, and identifies a finite cardinality
ratio with observed frequency. No algebraic result in the inherited probes
performs any of those jobs.

If the row is later adopted and realized, it supplies no randomness for one
run. Every admitted pair is realized; `which result do I see?` remains a
finite self-location question. This note establishes no self-location fact.

## 6. Falsifiers and open obligations

The model-level falsifiers of the candidate row remain:

1. a frozen apparatus whose realized cell counts differ from the diagonal of
   the joint Gram contraction at the admitted `A` read cut;
2. a missing or multiply counted within-cell Cartesian pair;
3. an off-cell record or a record without a system-record coincidence;
4. a nonzero realized record where `(A^n d)_k=0`.

Operational use still requires the typed apparatus, preparation, background,
gain, resolution, pointer, read cut, and event stream missing from
`QDD-INSTRUMENT-APPARATUS [O]`. The separate `B` channel adds its own carrier
and coupling obligations; those obligations may not be backfilled from the
count route.

## 7. Scope

This is an owner-adopted non-Canonical routing freeze. It closes only the
`raw J` versus `A/U5` fork for the coincidence-count proposal. It does not
change any confirmed L1 theorem, register a new claim, perform a formal run,
or move any physical row. Public Canon, Registry, Frontier, gates,
dependencies, dictionaries, and `STATUS.md` remain unchanged.
