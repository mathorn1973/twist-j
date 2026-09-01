# PHOTON-Z5-EXACT-HEATBATH-KERNEL

**Status:** exact reference implementation / non-canonical infrastructure  
**Authority:** none  
**Public basis:** Public Canon v74 and the fixed `t=1` face weight  
**Parent experiment:** #742  
**Consumed predecessor:** the zero-evidence pilot merged by PR #746

This package removes the integrity failure found after the first photon pilot.
It does not repair that sealed pilot, reuse its identifier, or assign any phase
label. It supplies an exact transition kernel for its successor.

## 1. Fixed measure

On the periodic four-torus, for link field `A in C^1(K_L;Z5)` and plaquette
flux `F=dA`, the target unnormalised measure is

```text
pi(A)=product_p W(F_p),
W=(4,phi^2,phi^-2,phi^-2,phi^2)
  =(4,1+phi,2-phi,2-phi,1+phi),
phi^2=phi+1.
```

Every weight is a strictly positive algebraic integer in `Z[phi]`.

For one oriented link, write the six incident plaquette fluxes as

```text
F_i(a)=r_i+epsilon_i a mod 5,
epsilon=(+,+,+,-,-,-).
```

The exact five conditional masses are

```text
L_a=product_(i=1)^6 W(F_i(a)),
P(A_link=a | all other links)=L_a / sum_(b in Z5) L_b.
```

No decimal approximation is needed.

## 2. Why the old fixed 64-bit categorical allocation was not exact

For the all-zero residual environment the five masses are

```text
4096,
89+144 phi,
233-144 phi,
233-144 phi,
89+144 phi,
```

and their sum is exactly `4740`. The probability of retaining the zero link
value is therefore

```text
4096/4740 = 1024/1185.
```

Its reduced denominator is not a power of two. Consequently no allocation of
all `2^64` words to five categories can represent this conditional law
exactly. Increasing the fixed word width only makes the bias smaller; it never
makes this probability exact.

## 3. Exact progressive categorical decision

The accepted sampler consumes an unbiased bit stream progressively. After
`n` bits, let the sampled real be known only to lie in

```text
I_n=[m/2^n,(m+1)/2^n).
```

Let `C_j=sum_(a<j)L_a` and `S=sum_a L_a`. A category `j` is returned only when

```text
m S       >= 2^n C_j,
(m+1) S   <= 2^n C_(j+1).
```

Both comparisons are exact in `Z[phi]`. If the dyadic interval crosses a
threshold, another bit is read. The only nonterminating bit streams represent
one of finitely many exact thresholds, a measure-zero set. Thus the ideal
algorithm terminates almost surely and returns exactly the declared
categorical law. A concrete implementation must treat exhaustion of its
prospectively frozen bit budget as `STOP_INTEGRITY`, never as permission to
round.

The deterministic SHA-256 counter stream in `verify.py` is only a public
reproducibility source for the finite audit. Exactness here means that the
category decision is exact relative to the supplied bit stream; it does not
turn a deterministic generator into physical randomness.

## 4. Stationarity and finite-volume ergodicity

For fixed exterior links, write the exterior factor as `R`. If two
configurations differ only at the selected link, with values `a` and `b`, then

```text
pi(A_a) K(A_a,A_b)
 = R L_a L_b / S
 = pi(A_b) K(A_b,A_a).
```

The single-link heat-bath kernel therefore satisfies detailed balance with the
fixed `t=1` measure. Any declared composition of these link kernels preserves
that measure, even when a systematic sweep is not itself reversible.

Strict positivity gives every link value positive conditional probability.
Any complete link field can therefore reach any other one through a finite
sequence of single-link assignments with positive probability. Retaining the
current value also has positive probability. On every finite periodic lattice
the chain is consequently irreducible and aperiodic and has the displayed
measure as its unique stationary distribution.

This is an existence and integrity statement. It supplies no useful mixing-time
bound.

## 5. Flat holonomy-sheet move

For direction `mu` and `h in Z5`, add `h` to every `mu`-directed link whose
starting coordinate satisfies `x_mu=0`. This is a closed periodic one-cochain:
every plaquette receives two equal and opposite contributions, so

```text
delta F_p=0
```

for every plaquette. The move is accepted with probability one and changes the
corresponding noncontractible holonomy by `h`.

This move samples flat holonomy sectors efficiently. It does not change the
Polyakov radius and is not, by itself, a proof of radial hot/cold mixing.

## 6. Audit coverage

`verify.py` uses only the Python standard library and exact integer arithmetic.
It checks:

1. the `Z[phi]` multiplication and exact real-embedding sign comparison;
2. positivity and inversion symmetry of all five face weights;
3. all `5^6=15625` local residual environments;
4. all five candidate masses in every environment;
5. local translation covariance under a changed link origin;
6. an exact dyadic-interval containment certificate from a public counter bit
   stream for every environment;
7. the explicit non-dyadic probability `1024/1185`;
8. the flat holonomy identity on periodic four-tori of sizes 2 through 5.

Run from the repository root:

```text
python3 reproduce/PHOTON-Z5-EXACT-HEATBATH-KERNEL/verify.py
```

Standard output must match `EXPECTED.txt` byte for byte, standard error must be
empty, and the exit code must be zero on both required architectures.

## 7. Scientific boundary

A passing reproduction establishes only the mathematical and implementation
integrity of this local kernel and the flat holonomy move. It does not establish
fast mixing, a thermodynamic limit, a photon phase, a pole, polarization,
physical randomness, apparatus, or SI calibration.

The next consumed pilot identifier is new. It must freeze its sweep schedule,
bit-budget STOP rule, flat-sheet schedule, hot/cold starts, autocorrelation
method and terminal thresholds before execution. Its maximum positive result
is permission to freeze the production preregistration; its phase-evidence
weight remains zero.
