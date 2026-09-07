# Pair statistics and recovery: an exact renewal boundary

NON-CANONICAL. L1 rational coefficient calculus and finite weighted event
trees. No physical occurrence law, native U lift or experimental result.
The external probabilistic interpretation below is explicitly conditional.

## 1. Three different sequences

Start with a registration at integer step zero. At age k since the most recent
registration, let h_k in [0,1] be a rational hazard. A registration resets age;
a nonregistration increments it. The transition depends only on age and the
fixed h, with no hidden state or history dependence. Successive waiting times
then have the same independent law. These are the renewal premises, not
consequences of having a recorded sequence.

For a finite prefix through N, define

```
S_0 = 1,
w_k = h_k S_(k-1),       S_k = S_(k-1)(1-h_k),
u_0 = 1,
u_n = sum_(j=1)^n w_j u_(n-j).
```

Here S_k is the weight of no registration in steps 1..k, w_k is the weight of
the FIRST subsequent registration at k, and u_k is the weight of ANY
registration at lag k from the initial registration. The last quantity sums
histories with zero, one or several intervening registrations. It is the
anchored all-pairs quantity, not the first-gap distribution or the hazard.

These assertions can be read without a physical probability postulate:
each binary word of length N has weight equal to the product of the h_age
or (1-h_age) factors along its age-reset path. Splitting a prefix into its two
extensions preserves total weight. Summing words by first occupied position
gives w; summing by occupancy at n gives u. Partition by the first registration
j and restart the identical tree to obtain the displayed renewal recurrence.

An absolutely calibrated stationary renewal experiment, conditioned on a
registration at its origin, has this u. A raw histogram requires an additional
observation map, exposure/edge correction, timing and registration semantics.
No such map from a physical file is supplied by the coefficient recurrence.

## 2. Exact inverse and finite-prefix admissibility

Given rational u_1..u_N and u_0=1, there is exactly one candidate gap prefix:

```
w_n = u_n - sum_(j=1)^(n-1) w_j u_(n-j).
```

It is a possible renewal prefix if and only if

```
w_n >= 0 for every n,       sum_(n=1)^N w_n <= 1.
```

Necessity follows because first-gap alternatives are disjoint. For sufficiency,
put the residual mass S_N at gap N+1. This gives a proper finite-support gap
law with the required prefix; reapplying the forward recurrence recovers u
by induction. A stopping/defective extension is another possible interpretation,
but is not required for this existence proof.

For each age with S_(n-1)>0, the only compatible hazard is

```
h_n = w_n / S_(n-1).
```

If S_(n-1)=0, admissibility forces w_n=0 and that age is UNREACHABLE.
Its hazard is not inferred to be zero. Any chosen value there is only a
representation of dynamics on a state that the process never visits.
This is a boundary on uniqueness of hazards, not of the reconstructed w.

Finite prefixes do not identify the eventual intensity. When S_N>0, placing
it at N+1 or N+7 gives equal observed prefixes and different means
`sum_(j=1)^N j w_j + S_N L`. The stationary intensity of a proper renewal
extension with finite mean is the reciprocal of its mean gap: with mean mu, stationary age k
has weight S_(k-1)/mu, and its total registration weight is
`sum_k w_k/mu=1/mu`. An all-zero finite prefix can
therefore be followed by a registration; it is not a permanently silent law.

This inverse needs the complete, absolutely scaled prefix u_1..u_n. Discarding
early lags, normalizing by an arbitrary reference bin, or supplying only a
shape does not satisfy its input contract. Even memoryless hazards h_k=a have
u_k=a and stationary intensity a: their normalized pair shapes are all one,
although the hazards differ for different a.

## 3. A hard-dead-time detector has non-step pair statistics

Take d dead steps, followed by the constant hazard a:

```
h_k = 0 for 1 <= k <= d;       h_k = a for k >= d+1.
```

For 0<a<=1 the gap is d plus a geometric waiting time on {1,2,...}:

```
w_n = 0 (n<=d),
w_n = a(1-a)^(n-d-1) (n>=d+1),
mean gap = d + 1/a,
lambda = a/(1+d a).
```

One can also derive lambda from stationary state balance: each registration
occupies d dead steps, while a fraction 1-d lambda of steps are ready and
register with hazard a. Thus lambda=a(1-d lambda). This does not assert a
pointwise long-lag limit in periodic cases.

For n>=1, the j-th subsequent registration is at n with weight

```
binom(n-jd-1,j-1) a^j (1-a)^(n-j(d+1)),
1 <= j <= floor(n/(d+1)).
```

Distribute n-j(d+1) failures among j geometric gaps; the number of weak
compositions is the displayed binomial coefficient. Summing these disjoint
registration-order alternatives gives u_n. The formula includes a=1, with
0^0=1. At a=0 there are no later registrations and lambda=0; division by
either a or lambda is undefined, not a normalized zero response.

The specific counterexample d=1, a=1/2 has

```
w_1=0,       w_n=2^(1-n) for n>=2,
lambda=1/3,
u_2=1/2,     u_3=1/4,     u_4=3/8,
u_2/lambda=3/2, u_3/lambda=3/4, u_4/lambda=9/8.
```

The normalized hazard h_n/a is already one at all three lags. Therefore even
inside the renewal class a perfectly sharp recovery step does not produce a
step-shaped normalized all-pairs curve. For this example, the formal series
`W(z)=z^2/(2-z)` and `1+sum_(n>=1)u_n z^n=1/(1-W(z))` give
`u_n=1/3+(2/3)(-1/2)^n`. The oscillation is an intervening-registration effect;
no extra detector state or source fluctuation is needed.

This refutes the universal EXACT substitution of normalized all-pairs counts
for normalized recovery. It does not refute an independently justified
approximation or an external experiment's fitted detector model.

## 4. A quantitative dilute-input boundary

Suppose explicitly that h_j=a eta_j, where 0<=eta_j<=1 and 0<a<=1. A physical
interpretation is independent Bernoulli opportunities of rate a, with an
age-dependent success efficiency eta; missed opportunities must not change
the state. The coefficient result itself only uses 0<=h_j<=a.

For each finite lag k,

```
|u_k-h_k| <= a(1-S_(k-1))
          <= a[1-(1-a)^(k-1)]
          <= a^2(k-1).
```

To prove the first bound, split histories according to whether any registration
occurred in steps 1..k-1. On the no-registration part, the hazard at k is h_k.
On the remaining weight 1-S_(k-1), both the actual age's hazard and h_k are
in [0,a], so their difference is at most a. The second bound uses
S_(k-1)=product_(j<k)(1-h_j)>=(1-a)^(k-1); the last follows by the elementary
union/product bound. No monotonicity of eta is required.

Thus `|u_k/a-eta_k| <= a(k-1)`, uniformly at most a(K-1) for k<=K.
The last coefficient is attained at k=2 with eta_1=1, eta_2=0, since
h_2=0 and u_2=a^2. This sharpness control is not a monotone recovery model.
At a=0 the unnormalized inequality still holds with u=h=0; normalized
expressions are undefined.

This is a bound in units of the admitted opportunity rate a. It does NOT
justify substituting the stationary registration intensity lambda for a or
normalizing at a selected finite lag. It is finite-horizon and supplies no
uniform all-time approximation. Applying it to a continuous-time instrument
would need a justified binning and physical opportunity model, neither of
which is part of this probe.

## 5. Registration data do not separate source rate and efficiency

For a given finite nonzero hazard prefix, let m=max h_j. In the preceding
product model, every a in [m,1], with eta_j=h_j/a, gives exactly the same h
and hence the same registration tree. Conversely eta_j<=1 requires a>=m.
Thus incoming opportunity rate and detection efficiency are not separately
identified by registrations alone. Independent source information is needed.

If m=0, every positive a with eta=0 on the prefix works; a=0 also works with
arbitrary eta. Dividing by zero is not an inverse. For infinite profiles,
the analogous condition uses sup h_j, but no convergence or calibration is
inferred from a finite prefix.

The example prefix `(0,1/4,1/2,1/4)` admits a=1/2, 3/4 and 1 with different
efficiencies. These are equivalent stipulated models, not alternative
calibrations of the cited apparatus. Correlated illumination, missed-arrival
heating, afterpulsing and additional detector state can invalidate the product
and renewal premises themselves.

## 6. Even complete pair data need a renewal premise

Consider two periodic binary registration patterns of period 12:

```
A={0,1,4,6},       B={0,1,3,7}.
```

Choose a uniformly random phase on the 12 positions to define each stationary
process. Both have intensity 4/12=1/3. Conditional on a registration at zero,
its position in the pattern is uniformly chosen among the four occupied
positions. Hence the pair quantity at residue r is

```
u_r = |{x in A: x+r mod12 in A}|/4,
```

and similarly for B. For both patterns the numerator is 4 at r=0, 2 at r=6,
and 1 at every other residue. They therefore have exactly the same pair
statistics at EVERY integer lag, with the same absolute scale and intensity.

But their cyclic next-registration gaps are respectively

```
A: (1,3,2,6),       B: (1,2,4,5),
```

with each starting registration weighted 1/4. At age 3, conditional on no
earlier new registration, A's first-gap hazard is 1/2 and B's is zero.
Full all-pairs information therefore does not identify even the next-gap law
in the larger class of stationary processes. These are correlated periodic
gap processes, not iid renewals, so they do not contradict section 2.

As a separate finite control, fair independent bits at steps 1,2,3 and the
uniform even-parity words {000,011,101,110}, both with a registration fixed
at zero, have equal first and second occupancy moments. Their triple-111
weights and their true first-gap weight at 3 differ. Pair agreement is not
a certificate of renewal or higher-order independence.

## 7. What the verifier audits and what remains physical

The verifier compares recurrence calculations with independent weighted-word
enumeration, tests inverse admissibility and unreachable ages, checks the
hard-dead-time closed forms, the dilute inequalities, source ambiguity and
the two nonrenewal witnesses. All coefficients and comparisons are exact
rationals; the finite censuses audit the preceding all-length proofs.

No external histogram, detector model fit or measurement source is an input.
The primary paper and archive metadata motivate the distinction of observables;
they are not evidence of a new experimental failure. Before physical inverse
use one needs a calibrated observation map, absolute scale and the full
relevant prefix, an independently justified renewal/state model and source
information sufficient for any efficiency claim. A physical state or record
realization from native U remains open.
