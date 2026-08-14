# C-TM-SYM2-ORIENTATION-SOURCE-1-N result

```text
STATUS:       NON-CANONICAL
ISSUE LOCK:   #375
PUBLIC BASIS: Public Canon v46
RESULT:       candidate-T L5 source theorem
DECISION:     SOURCE
PUBLIC ROWS:  unchanged
```

## 1. Source character

On

```text
W3={001,010,011,100,101,110}
```

define

```text
omega(a,b,c)=c-a.
```

Then directly

```text
omega(R(a,b,c))
 = omega(c,b,a)
 = a-c
 = -omega(a,b,c),
```

and

```text
omega(N(a,b,c))
 = omega(1-a,1-b,1-c)
 = (1-c)-(1-a)
 = a-c
 = -omega(a,b,c).
```

Since N and R commute,

```text
omega(NRw)=omega(w).
```

Thus omega carries the joint character

```text
R -> -1,
N -> -1,
NR -> +1.
```

In the chronological window

```text
q(n)=(theta_(n-1),theta_n,theta_(n+1)),
```

the source is exactly

```text
boxed: omega_n=theta_(n+1)-theta_(n-1) in {-1,0,1}.
```

[NON-CANONICAL candidate-T]

## 2. Uniqueness of the character source

Let `f:W3->Q` satisfy

```text
f(Rw)=-f(w),
f(Nw)=-f(w).
```

The reversal-fixed words `010` and `101` force

```text
f(010)=f(101)=0.
```

Put `x=f(001)`. Then

```text
R(001)=100  -> f(100)=-x,
N(001)=110  -> f(110)=-x,
R(110)=011  -> f(011)=x.
```

Every value is now fixed:

```text
001   x
010   0
011   x
100  -x
101   0
110  -x.
```

Hence the joint `(-1,-1)` character space is one-dimensional. For `x=1` this table is exactly `c-a`.

Therefore

```text
boxed:
{f:W3->Q | f o R=-f, f o N=-f}=Q . omega.
```

[NON-CANONICAL candidate-T]

Scale and overall sign are not fixed by this theorem. No physical normalization is claimed.

## 3. Exact match to epsilon_read

The inherited public reversal classification gives

```text
t_N  =(0,1),
t_R  =(1,0),
t_NR =(1,1)
```

on the selector quotient. For

```text
epsilon_read=chi_Q chi_F,
```

a translation `(u,v)` multiplies the epsilon character by

```text
(-1)^(u+v).
```

Therefore

```text
N  -> -1,
R  -> -1,
NR -> +1.
```

This is exactly the character of omega.

[NON-CANONICAL candidate-T]

The match uses no selector representative and no field enlargement.

## 4. Representative-free quotient stream

Order the four public quotient classes as

```text
(++),(+-),(-+),(--)
```

and put

```text
v_epsilon=(1,-1,-1,1)^T.
```

Define

```text
boxed: J_n=omega_n v_epsilon in Q^4.
```

This vector is defined on the complete quotient, not on a chosen selector. Its lift to all 48 selectors assigns to every selector `s`

```text
J_n(s)=omega_n epsilon_read(s),
```

which is constant on each 12-member G orbit. Hence replacing a selector by any other representative of the same G class leaves the source unchanged.

Let `P_b` be the quotient-class permutation induced by precomposition with `b in {N,R,NR}` and let `chi_eps(b)` be its epsilon sign. Then

```text
P_b v_epsilon = chi_eps(b) v_epsilon,
omega(bw)      = chi_eps(b) omega(w).
```

Consequently

```text
P_b [ omega(bw) v_epsilon ]
 = chi_eps(b)^2 omega(w) v_epsilon
 = omega(w) v_epsilon.
```

Thus the source is coherent under the simultaneous drive/quotient action of all three frozen involutions.

[NON-CANONICAL candidate-T]

This is the key selector-free source property.

## 5. Nontriviality and stationary mathematics

The exact value table is

```text
word  omega
001     +1
010      0
011     +1
100     -1
101      0
110     -1
```

Under the inherited uniform stationary law on W3,

```text
P(omega=+1)=1/3,
P(omega= 0)=1/3,
P(omega=-1)=1/3,
E[omega]=0,
E[omega^2]=2/3.
```

These are mathematical source statistics only. In particular `2/3` is not identified with a Born weight, gyron density, physical probability, or normalization.

## 6. Exact child recursion

For the parent window `(a,b,c)`, define its two oriented edge differences

```text
ell=b-a,
r  =c-b.
```

Then

```text
omega=ell+r.
```

The frozen child maps give

```text
E_even(a,b,c)=(1-a,b,1-b),
E_odd (a,b,c)=(b,1-b,c).
```

Therefore

```text
boxed: omega(E_even q)=-ell,
boxed: omega(E_odd  q)= r.
```

The edge-pair map is injective on W3:

```text
001 -> ( 0, 1)
010 -> ( 1,-1)
011 -> ( 1, 0)
100 -> (-1, 0)
101 -> (-1, 1)
110 -> ( 0,-1).
```

Thus the finite parent state `(ell,r)` determines the complete W3 word and the next source value under either doubling child. The orientation source is a closed finite-state L5 stream driven by the existing Thue-Morse child branch. No selector enters its evolution.

[NON-CANONICAL candidate-T]

## 7. Breaker verdict

The independently frozen breaker gives:

```text
B1 PASS   all six W3 signs agree
B2 PASS   joint (-1,-1) function space has dimension one
B3 PASS   inherited epsilon translation has the same character
B4 PASS   class reordering changes coordinates, not the epsilon line
B5 PASS   simultaneous action is coherent because both factors carry the same sign
B6 PASS   R-fixed palindromes necessarily have omega=0
B7 PASS   child recursion closes on the six edge-pair states
B8 PASS   no L6 or Born inference is used
```

No breaker fired.

## 8. Decision

```text
S1 PASS
S2 PASS
S3 PASS
S4 PASS
S5 PASS
S6 PASS
S7 SOURCE
S8 PASS

DECISION: SOURCE
```

The missing object localized by #372 exists at L5:

```text
boxed:
future-minus-past Thue-Morse current
omega_n=theta_(n+1)-theta_(n-1)
```

is the unique rational source on W3 in the same `(-1,-1)` character as `epsilon_read`, and

```text
J_n=omega_n v_epsilon
```

is its complete selector-free quotient realization.

This is stronger than the H4 diagnostic because it supplies nonzero epsilon-mode data whenever the chronological window is non-palindromic. It is not obtained by transforming the previously selector-independent `1/6` output.

## 9. Exact scope of the advance

At the NON-CANONICAL candidate level, this supplies the previously missing **successor L5 orientation-carrying source schema** requested by the public TM-SYM2 physical-measure frontier.

It does not close that frontier row. Still missing are at least:

```text
physical Born carrier,
total typed L5-to-L6 map,
normalization/equality semantics,
complete dependency graph,
proof that the resulting L6 measure is coherent and physically admissible.
```

No selector is chosen, no postcomposition gauge is enlarged, and `epsilon_read` is retained rather than quotiented.

No Canon, Registry, frontier, Born, decoder, physical probability, or L6 status moves in this incubation.
