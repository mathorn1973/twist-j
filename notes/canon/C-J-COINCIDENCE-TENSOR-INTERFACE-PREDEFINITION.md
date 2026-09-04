# C-J coincidence tensor-interface predefinition (NON-CANONICAL)

```text
STATUS:                  OWNER-ROUTED PREDEFINITION /
                         TENSOR-INTERFACE BOUNDARY
AUTHORITY:               NOT CANON
SCOPE:                   PROPOSAL-LOCAL / L1 TYPING /
                         PHYSICAL REALIZATION OPEN
DEPENDS ON:              C-J A/U5 coincidence-channel owner freeze /
                         C-J plenum Born-chain proposal
COUNT INPUT:             a_n=A^n d in V_Z
ALGEBRAIC COPY:          full marked cell register before compression
FINITE PAIR CARRIER:     separately defined Cartesian incidence
POSITIVE POLAR CHANNEL:  separate / not tensorized
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
PUBLIC MAIN BASE:        a7ef8ba676a7a26ebac4b0d5a0b31c47bc41cc9c
```

This note fixes the smallest tensor interface compatible with the owner's
`A/U5` route. It separates three objects that have the same square list but
do not have the same type:

1. a diagonal joint coefficient in a tensor product;
2. a diagonal Gram contraction;
3. a finite complete incidence relation.

Only the third object has `d_k^2` elements. Identifying any two of these
objects without the displayed seam is forbidden.

## 0. Type firewall first

A continuation returns `TYPE-BREACH / STOP` if it does any of the following:

1. copies after passing to the nonorthogonal four-dimensional simplex
   quotient;
2. says the linear Cayley copy manufactures `a_(n,k)^2` coefficient units;
3. interprets a Gram entry as a realized record without the candidate-H row;
4. derives complete incidence from the two marginal fibres;
5. treats the two tensor factors as already populated physical registers;
6. makes the `B` channel a third tensor factor merely because `B` commutes
   with `U5`;
7. feeds raw `J` into the coincidence-count input;
8. applies literal finite-fibre language to generally nonintegral `U5^n d`;
9. traces residual ordinal tokens across updates;
10. fills any apparatus, pointer, event, observation, self-location, or
    frequency field by algebraic inference.

## 1. Carrier and order of operations

Freeze two tagged copies of the full orthogonal marked-cell carrier:

```text
E_sys,Z = direct-sum_(k=0)^4 Z e_k^sys,
E_rec,Z = direct-sum_(k=0)^4 Z e_k^rec.
```

Their real extensions have the standard marked orthonormal bases. The
augmentation-zero count carrier is

```text
V_Z={d in E_sys,Z : sum_k d_k=0}.
```

For a supported nonzero preparation `d in V_Z` and an admitted integer read
cut `n>=0`, the owner-routed count input is

```text
a_n=A^n d in V_Z.
```

The order is load-bearing:

```text
integral preparation
  -> integral A evolution on the marked full register
  -> full-cell tensor copy
  -> Gram contraction and separately defined finite incidence
  -> only then any allowed compression or higher-layer read.
```

The confirmed simplex boundary forbids replacing this order by
`compression -> copy`. The five compressed simplex vertices have one source
relation but their tensor squares are linearly independent, so no linear map
on the four-dimensional quotient copies all five labels.

## 2. Algebraic tensor port

Define the full-cell Cayley copy

```text
K:E_sys,Z -> E_sys,Z tensor_Z E_rec,Z,
K e_k^sys=e_k^sys tensor e_k^rec.
```

It is the ready-column restriction of the reversible controlled addition on
the full `5 x 5` marked register. At read cut `n`,

```text
Psi_n(d)=K a_n
        =sum_k a_(n,k) e_k^sys tensor e_k^rec.
```

In the ordered cell bases its coefficient matrix is

```text
M_n=diag(a_(n,0),...,a_(n,4)).
```

Therefore the two algebraic contractions agree:

```text
M_n M_n^T=M_n^T M_n
           =diag(a_(n,0)^2,...,a_(n,4)^2),
Tr(M_n M_n^T)=q(a_n)=5^n q(d).
```

This is the exact tensor-to-square seam. The diagonal coefficient
`a_(n,k)` has only `|a_(n,k)|` reduced signed ordinal units. The linear map
`K` does not square that number.

The labels `sys` and `rec` distinguish the two algebraic factors. They do
not assert that a physical system and a physical apparatus have been built.

## 3. Finite incidence port

At the same frozen cut, independently form two tagged copies of the fresh
residual fibre:

```text
U_k^S(a_n), U_k^R(a_n),
|U_k^S(a_n)|=|U_k^R(a_n)|=|a_(n,k)|.
```

The complete mathematical incidence relation is

```text
C_k^x(a_n)=U_k^S(a_n) x U_k^R(a_n),
C^x(a_n)=disjoint-union_k C_k^x(a_n).
```

Finite-set multiplication gives

```text
|C_k^x(a_n)|=a_(n,k)^2,
|C^x(a_n)|=q(a_n).
```

Consequently,

```text
cardinality-vector(C^x(a_n))
  =diag(M_n M_n^T)
  =diag(M_n^T M_n).
```

That equality is the whole earned bridge. The two equal marginals also admit
the empty relation, the ordinal diagonal, and every intermediate
cardinality. Hence the tensor coefficient and its Gram diagonal do not
select complete physical incidence.

## 4. Three-port interface after the owner split

For bookkeeping, define the typed interface tuple

```text
R_n(d)=(Count_n(d), Profile_n(d), Polar_n(d)),

Count_n(d)   =a_n=A^n d,
Profile_n(d) =(a_(n,k)^2/q(a_n))_(k=0)^4
             =((U5^n d)_k^2/q(U5^n d))_(k=0)^4,
Polar_n(d)   =(phi^(-n)P_+d, phi^n P_-d).
```

| Port | Carrier | Exact content | Physical status |
|---|---|---|---|
| Count | `V_Z` | Integral coefficients, fresh residual fibres, available pair cardinalities | Realization open |
| Profile | Marked square simplex | Scale-free profile shared by `A^n d` and `U5^n d` | Frequency identification open |
| Polar | `P_+V_R direct-sum P_-V_R` | Unequal positive sector gains making `B^n d` | Carrier and read law open |

This tuple is a typed Cartesian record of outputs. It is not a physical
tensor product. The count and profile entries are deliberately redundant:
their exact agreement is the calibration identity of the split route.

The polar entry uses the canonical direct-sum sector decomposition already
defined on `V_R`. No tensor decomposition of `V_R` follows. In particular,

```text
[U5,B]=0
```

does not imply a carrier factorization. It only permits the operator identity
`J^n=U5^n B^n` on `V_R`.

## 5. What a later apparatus must add

The present interface does not fill `QDD-INSTRUMENT-APPARATUS [O]`. A later
physical package must explicitly supply at least:

```text
an apparatus carrier and ready condition,
a typed joint evolution or coupling,
five marked pointer cells or an exact replacement,
a rule selecting the realized incidence relation,
a calibrated read cut and resolution,
an event or record persistence law,
the relation, if any, between the separate polar channel and the apparatus,
a no-feedback or explicit-feedback rule,
an L5 stream and an L5-to-L6 frequency reading.
```

Reversible full-cell controlled addition is an algebraic witness for the
copy column; by itself it does not provide the remaining apparatus package.
Likewise, the complete finite relation is a mathematical option; by itself
it is not a realized event population.

## 6. Physical row held at the seam

The only proposed physical move remains exactly:

```text
COINCIDENCE-RECORD-FREQUENCY [candidate-H / future L5-L6 / STOP]

At a frozen calibrated read cut, the realized records are exactly the
elements of C^x(a_n), every within-cell ordered pair occurs once, no other
record occurs, and observed cell frequency is

f_(n,k)=|C_k^x(a_n)|/|C^x(a_n)|.
```

If that row is supplied, the tensor interface yields

```text
f_(n,k)
  =diag(M_n M_n^T)_k/Tr(M_n M_n^T)
  =(A^n d)_k^2/q(A^n d)
  =(U5^n d)_k^2/q(U5^n d).
```

Without that row, the display is only an equality among a conditional
frequency symbol, a finite ratio, a normalized Gram diagonal, and an
algebraic square profile.

No one-run randomness is introduced. If every pair is later declared
realized, observer indexicality remains an additional self-location
question, not a result of the tensor contraction.

## 7. Scope

This predefinition fixes types, ports, and operation order only. It creates
no `[T]`, `[D]`, `[C]`, `[H]`, `[O]`, or `[F]` row. It does not make `B`
unphysical; it quarantines `B` in a separate unresolved channel. It does not
change the algebraic role of raw `J`; it excludes raw `J` from this one
counting port by the owner's ruling.

Public Canon, Registry, Frontier, gates, dependencies, dictionaries,
`QDD-INSTRUMENT-APPARATUS [O]`, and `STATUS.md` remain unchanged.
