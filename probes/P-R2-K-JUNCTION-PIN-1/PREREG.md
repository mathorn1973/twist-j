# P-R2-K-JUNCTION-PIN-1 preregistration

Status: PREREGISTERED CANDIDATE; FIRST FORMAL RUN FORBIDDEN UNTIL REMOTE PIN

This document freezes one rigorous enclosure probe. It contains no formal
gate output and earns no scientific status. Formal execution of `verify.py`
is forbidden until this exact document and verifier are committed, pushed,
and read back as one immutable public pin on issue 95.

## Public identity and scope

```text
program:          TWIST-J
probe:            P-R2-K-JUNCTION-PIN-1
public lock:      issue 95
session:          R2-K junction enclosure session
owner:            A. M. Thorn
branch:           probe/P-R2-K-JUNCTION-PIN-1
path:             probes/P-R2-K-JUNCTION-PIN-1/
layer:            L6, completed-zeta first-rung arithmetic only
maximum result:   C, rigorous finite enclosure of lambda_1^K
parent status:    R2 and RH remain O regardless of the numerical outcome
```

Authority is Public Canon v11, public activation commit
`3d8c6307f20d01ad50fc90ae1c5777926b884881`, content commit
`3dc0d4255ae47f0512e5dd656d92ceb308ab026a`, Canon SHA-256
`d20b064c8564af4e4a22ec3d0a84a9847a3705af84fd6fee2faa6b2710d7c7e8`.
The public Canon is authoritative for this public cleanup. The exact
identities imported below retain their Canon labels. This probe can add only
a computed enclosure and convention audit. It cannot promote the R2 carrier,
the Li ladder, or RH.

## Frozen five fields

### 1. Equation

Let `K = Q(zeta_5)`, with degree four, signature `(r1,r2) = (0,2)`,
discriminant `D_K = 125`, and Dirichlet characters on `(Z/5Z)^*` generated
by `omega(2) = i`. The primitive factorization convention is

```text
zeta_K(s) = zeta(s) L(s,omega) L(s,omega^2) L(s,conj(omega)).
```

The registered first completed-zeta rung is

```text
lambda_1^K = 1 + (3/2) log 5 - 2 log(2 pi) - gamma
             + sum_{chi in {omega,omega^2,conj(omega)}} L'/L(1,chi).
```

Here is the frozen derivation, independent of the numerical enclosure. With
`Gamma_C(s) = 2(2 pi)^(-s) Gamma(s)`, complete the Dedekind zeta by

```text
xi_K(s) = constant * s(s-1) D_K^(s/2) Gamma_C(s)^2 zeta_K(s).
```

At `s=1`, logarithmic differentiation contributes:

```text
d log s                         = 1,
d log D_K^(s/2)                = (1/2)log 125 = (3/2)log 5,
d log Gamma_C(s)^2             = -2log(2pi) - 2gamma,
d log((s-1)zeta(s))            = +gamma,
d log product(nonprincipal L)  = sum L'/L(1,chi).
```

Thus `lambda_1^K = xi_K'/xi_K(1)` is exactly the registered expression.
The code separately checks the rational coefficient bookkeeping
`(+gamma)-2gamma = -gamma` and `(1/2)log(5^3) = (3/2)log 5`.

For the Laurent convention

```text
zeta(s,q) = 1/(s-1) + gamma_0(q) - gamma_1(q)(s-1) + ...,
```

put

```text
A_chi = sum_{a=1}^4 chi(a) gamma_0(a/5),
B_chi = sum_{a=1}^4 chi(a) gamma_1(a/5).
```

Since `sum_a chi(a) = 0`, the Hurwitz decomposition
`L(s,chi) = 5^(-s) sum_a chi(a) zeta(s,a/5)` gives exactly

```text
L'/L(1,chi) = -log 5 - B_chi/A_chi.
```

The minus sign before `B_chi/A_chi` is load-bearing. Writing

```text
A_2 = g01-g02-g03+g04,       B_2 = g11-g12-g13+g14,
x   = g01-g04, y = g02-g03, u = g11-g14, v = g12-g13,
```

where `gra = gamma_r(a/5)`, the full nonprincipal sum reduces to

```text
-3 log 5 - B_2/A_2 - 2(ux+vy)/(x^2+y^2).
```

The verifier does not assume this reduction as its primary path. It first
constructs `A_chi`, `B_chi`, and `-log 5-B_chi/A_chi` independently for all
three characters in complex rational interval arithmetic. It then requires
the imaginary sum to enclose zero narrowly and the real sum to overlap the
displayed reduction. No expected centre or sign of `lambda_1^K` is
preregistered.

### 2. Code version

The sole formal verifier is the `verify.py` committed beside this document.
It uses Python standard library only: integers, `Fraction`, `itertools`,
`math.comb`, and `math.isqrt`. Every assertion is an exact rational
comparison. No binary float, external table, network datum, or numerical
package is allowed. Decimal output is an outward-rounded display witness
only and is suppressed if any gate fails.

### 3. Dataset and finite parameters

There is no empirical dataset. The complete frozen input is:

```text
characters, a = 1,2,3,4:
  omega:       1,  i, -i, -1
  omega^2:     1, -1, -1,  1
  conj(omega): 1, -i,  i, -1

Euler--Maclaurin cuts:       N = 64 and N = 128
Euler--Maclaurin order:      m = 12, through B_24
independent coarse cut:      N_check = 37
atanh-log terms:             64
Machin arctan terms:         48 for 1/5, 14 for 1/239
outward rational grid:       10^70
```

The Bernoulli values through `B_24` are frozen in the verifier and checked
against their exact recurrence before use.

### 4. Systematics and conventions

1. The principal factor is the primitive conductor-one `zeta(s)`. If one
   instead multiplies the four imprimitive modulus-five L-series literally,
   then

   ```text
   product_{chi mod 5} L(s,chi) = (1-5^(-s)) zeta_K(s).
   ```

   With `u=5^-1`, direct differentiation derives the inverse-factor
   coefficient `-u/(1-u)=-1/4` and the omitted-correction drift
   `+u/(1-u)=+1/4`, both in units of `log 5`. Omitting the correction moves
   the logarithmic derivative at `s=1` by `+log(5)/4`.

2. The generalized Stieltjes convention above fixes the sign in `L'/L`.
   Reversing the `gamma_1` convention is not an allowed alternate reading.

3. All interval endpoints are rational and outward. A displayed decimal is
   never used as an assertion input.

4. Euler--Maclaurin is checked at two cuts and against a genuinely
   independent sum-integral enclosure that uses no Bernoulli remainder.

5. The positive real branches are used for `sqrt(5)`, `phi`, `s_J`, `pi`,
   and all logarithms. The Canon identity `s_J^2 phi = sqrt(5)` then gives
   symbolically

   ```text
   6 log s_J + 3 log phi = (3/2) log 5.
   ```

6. The Q-case value

   ```text
   lambda_1^Q = 1 + gamma/2 - log(4 pi)/2
   ```

   is a guard only, not a new result.

### 5. Failure threshold

The package fails if any frozen gate `K00..K11` fails. In particular it
fails if any character denominator interval at either cut or at their
intersection contains zero, the independent enclosure does not contain the
Euler--Maclaurin interval, the two cuts do not overlap, the complex
character sum is not narrowly real, the classical L(1) controls do not
overlap, the Q guard leaves `(0.0230957,0.0230958)`, the final K enclosure
has width at least `10^-24`, or either architecture differs by one stdout
byte.

## Enclosure proof frozen before execution

For the frozen cuts, `q > 0` and `A = N+q >= 64+1/5`. Put `L = log A`,
`H_j = sum_{r=1}^j 1/r`, and `c_k = B_(2k)/(2k A^(2k))`.
Euler--Maclaurin gives

```text
G0 = sum_{n<N} 1/(n+q) - L + 1/(2A) + sum_{k=1}^12 c_k,

G1 = sum_{n<N} log(n+q)/(n+q) - L^2/2 + L/(2A)
     + sum_{k=1}^12 c_k (L-H_(2k-1)).
```

Define the periodic Bernoulli function without factorial normalization by
`B~_24(t) = B_24({t})`. The remainder is

```text
R(s) = -(s)_24/24! integral_0^infinity
       B~_24(t) (A+t)^(-s-24) dt.
```

The classical bound `sup |B~_24| <= |B_24|`, `A>1`, therefore yields

```text
|gamma_0(q)-G0| <= |B_24|/(24 A^24),

|gamma_1(q)-G1| <= |B_24| A^(-24)
  ((H_24 + log A)/24 + 1/24^2).
```

The independent check starts directly from the defining limits. At
`A = N_check+q`, set

```text
C = sum_{n<N_check} 1/(n+q) - log A,
D = sum_{n<N_check} log(n+q)/(n+q) - (log A)^2/2.
```

For a tail function `f`, define

```text
E_A(f) = sum_{k>=0} (f(A+k) - integral_[A+k,A+k+1] f(x) dx).
```

If `h=-f'` is positive and decreasing, each cell excess is
`integral_0^1 (1-u)h(A+k+u)du` and lies between
`h(A+k+1)/2` and `h(A+k)/2`. Applying this first to `f(x)=1/x`
and using trapezoidal convexity gives

```text
C + 1/(2A) <= gamma_0(q)
                 <= C + 1/(2A) + 1/(2A^2).
```

For `f(x)=log x/x`,
`h(x)=(log x-1)/x^2` is positive and decreasing once `log A>3/2`.
The same cell lemma and integral comparison give

```text
D + log(A+1)/(2(A+1)) <= gamma_1(q)

gamma_1(q) <= D + (1/2)((log A-1)/A^2 + log A/A).
```

This proof path contains no Bernoulli number.

For rational logarithms, scale `x = 2^e y`, `1 <= y < 2`, and put
`t = (y-1)/(y+1)`. The verifier uses

```text
log y = 2 sum_{j=0}^{63} t^(2j+1)/(2j+1) + tail,
0 <= tail <= 2 t^129/(129(1-t^2)).
```

Pi is enclosed independently by Machin's identity
`pi = 16 atan(1/5) - 4 atan(1/239)` and alternating rational series.

## Frozen gates

```text
K00  Field, completion, and character data: the power-basis trace Gram
     determinant is 125; degree 4 and signature (0,2); conductor product
     1*5*5*5 = 125; the completed-zeta rational coefficients are exact;
     the character rows form the cyclic group, sum to zero when
     nonprincipal, and the quartic rows are exact conjugates.

K01  Principal-factor bookkeeping: derive the inverse correction coefficient
     -1/4 and omitted drift +1/4 from u=1/5 and 1-u, not from stored target
     constants. The drift interval +log(5)/4 must exclude zero.

K02  Arithmetic machinery: the frozen Bernoulli table satisfies its exact
     recurrence; rational atanh bounds enclose log(2); Machin bounds enclose
     3.14159 and have width below 10^-60.

K03  For q in {1/5,2/5,3/5,4/5,1}, the N=64 and N=128 Euler--Maclaurin
     intervals overlap for both gamma_0 and gamma_1; every intersection has
     width below 10^-24.

K04  For the same five q values, each tight intersection is contained in
     the independent N_check=37 sum-integral enclosure, whose precondition
     log(N_check+q) > 3/2 is proved by rational endpoints.

K05  Character assembly: every A_chi denominator norm at N=64, N=128, and
     their tight intersection excludes zero. The reduced denominators A_2
     and x^2+y^2 at all three stages also exclude zero.

K06  Classical controls: A_2/5 overlaps 2 log(phi)/sqrt(5), and
     (x^2+y^2)/25 overlaps 2 pi^2/25, with all quantities independently
     enclosed.

K07  The Q guard computed from gamma_0(1) lies strictly inside
     (0.0230957,0.0230958).

K08  The two separately assembled N=64 and N=128 K intervals overlap; the
     final intersection has width below 10^-24. No location or sign is a
     preregistered pass condition.

K09  Independently assemble A_chi, B_chi, and -log(5)-B_chi/A_chi in
     complex intervals for omega, omega^2, and conj(omega). At both cuts the
     summed imaginary interval must contain zero with width below 10^-24,
     and the real interval must overlap the algebraic real reduction. The
     direct completed-zeta assembly must overlap its simplified form.

K10  Plenum junction: from the positive-branch identity
     s_J^2 phi = sqrt(5), exact rational coefficient arithmetic gives
     6 log s_J + 3 log phi = (3/2) log 5.

K11  Negative convention control: adding the independently derived literal
     modulus-five drift log(5)/4 gives an interval disjoint from the
     registered K interval. Output identifies this as a deliberately wrong
     convention, not an alternate result.
```

## Formal run and evidence rule

The first formal execution must occur only after immutable remote readback
of the pin. It must run on an `aarch64` Linux connector with

```text
LC_ALL=C
LANG=C
PYTHONDONTWRITEBYTECODE=1
PYTHONHASHSEED=0
TZ=UTC
```

and repeat byte-identically three times. The later GitHub Actions `x86_64`
leg must reproduce the same stdout bytes. The preregistration commit,
`PREREG.md` SHA-256, `verify.py` SHA-256, both machine records, stdout byte
count, and stdout SHA-256 are evidence. Any mismatch is a fired falsifier.
Pinned history must not be amended, rebased, or force-pushed.

## Scope after any pass

A pass establishes at most `R2-K-JUNCTION-PIN [C]`: one rigorous numerical
enclosure of the first completed-zeta rung for `Q(zeta_5)`, plus a convention
audit and Q guard. It does not construct a TWIST-J R2 carrier, does not prove
the remaining Li rungs, and does not bear on RH. `R2 [O]` and `RH [O]` remain
unchanged.
