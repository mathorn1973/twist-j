# P-PHOTON-Z5-DUAL-WORM-CROSSCHECK-1 preregistration

Status: FORMAL ENGINEERING PREREGISTRATION / INDEPENDENT DUAL IMPLEMENTATION / ZERO EVIDENTIAL WEIGHT

Owner: A. M. Thorn  
Public reservation: issue #756  
Parent experiment: issue #742  
Production-freeze dependency: issue #757  
Public base: `a91ec3c2a38c64a9c0b1be4db55947ce0c97e937`  
Canon: Public Canon v74

This lane freezes an implementation that is deliberately independent of the
primal exact heat-bath sampler. It does not reuse the primal transition code,
Philox stream, cached plaquette implementation, or in-memory observables. Its
purpose is to supply the independent dual surface-ensemble check required by
the photon measurement contract.

No phase label may be emitted from this package. A later cross-check execution
may validate or invalidate numerical Ward identities, but it remains
`ZERO_ENGINEERING_ONLY` until a separately preregistered evidential experiment
consumes it.

## 1. Exact dual target

The dual state is a plaquette 2-chain

```text
n in {-1,0,+1}^P,
partial n = 0 mod 5,
```

on the periodic cubical four-torus `K_L=(Z/LZ)^4`. Residues are stored as
`0,1,4` in `F_5`. The exact target is

```text
pi_L(n) = Z_dual(L)^(-1) 2^(-|supp n|).
```

This is the character-expansion ensemble of the fixed primal face weight

```text
W(f)=2+2 cos(2 pi f/5),
F_5 W = 5(2,1,0,0,1).
```

The declared integer defect current for later checks is

```text
j = partial n / 5
```

using principal integer representatives `{-1,0,+1}` before the integer
boundary is divided by five. The Markov constraint is only `partial n=0 mod 5`;
integer `j` need not vanish.

## 2. Orientation and cycle generators

Coordinates are ordered `0<1<2<3`. Plaquettes carry orientation `(mu,nu)`
with `mu<nu`. Three-cells carry `(mu,nu,rho)` with `mu<nu<rho`. The cubical
boundary convention is the standard alternating upper-minus-lower convention.

The proposal generator set is the disjoint union

```text
B = { boundaries of all oriented 3-cells },
H = { six positive coordinate 2-tori H_(mu,nu), mu<nu }.
```

For `H_(mu,nu)` the two transverse coordinates are fixed to zero and all
`L^2` positively oriented `(mu,nu)` plaquettes are included.

Over `F_5`, the periodic four-torus has

```text
b_2 = 6,
dim Z_2 = 3 L^4 + 3,
dim B_2 = 3 L^4 - 3.
```

The cube boundaries span `B_2`; the six coordinate tori represent a basis of
`H_2(T^4;F_5)`. Therefore `B union H` spans the complete cycle space `Z_2`.
The verifier audits this rank statement at `L=2,3`; the general statement is
the cellular-homology proof, not an extrapolation from those finite checks.

## 3. Independent symmetric random-word proposal

A proposal increment `z in Z_2` is generated without reference to the primal
sampler.

1. Draw a word length `N>=0` from

```text
P(N=m)=2^(-(m+1)).
```

This is the number of zero fair bits before the first one.

2. For each letter independently:
   - one fair bit chooses boundary class `B` or homology class `H`;
   - choose the generator index exactly uniformly by rejection, never by
     biased modulo reduction;
   - choose sign `+1` or `-1` by one fair bit;
   - add that signed generator in `F_5`.

The source implementation uses a SHA-256 counter bitstream with a public seed
and domain separator. This is deliberately a different deterministic stream
from the primal Philox implementation. It is a reproducibility device, not a
claim of physical randomness.

For every random word yielding `z`, changing every sign yields `-z` with the
same probability. Hence

```text
Q(z)=Q(-z).
```

The proposal on states is `n' = n+z mod 5`.

## 4. Zero-support firewall and exact acceptance

If any coordinate of `n'` is residue `2` or `3`, the Fourier coefficient is
zero and the proposal is rejected exactly.

Otherwise `n'` is again in `{-1,0,+1}^P`. Since `z` is a cycle, closure is
preserved. Put

```text
d = |supp n'|-|supp n|.
```

The exact Metropolis rule is

```text
if d <= 0: accept,
if d > 0:  accept with probability 2^(-d).
```

For positive `d` this is implemented by reading exactly `d` fair bits and
accepting iff all are zero. No floating-point number, logarithm, exponential,
or rounded threshold appears in the decision path.

Because `Q` is symmetric,

```text
pi(n) Q(n'-n) a(n,n') = pi(n') Q(n-n') a(n',n)
```

holds exactly. Thus the kernel is reversible with respect to `pi_L`.

## 5. Ergodicity theorem for the frozen kernel

### Irreducibility

Take any two allowed states `n,n'`. Their difference

```text
z=n'-n mod 5
```

is a cycle. Since `B union H` spans `Z_2`, `z` has a finite expression as a
sum of signed frozen generators; coefficients `2,3,4` in `F_5` are represented
by repeated `+1` or `-1` letters. The geometric word distribution assigns
strictly positive probability to that finite word and every exact index/sign
choice. The endpoint `n'` is allowed, so the Metropolis acceptance probability
is also strictly positive. Therefore every allowed state reaches every other
allowed state with positive one-step probability.

### Aperiodicity

`N=0` has probability `1/2`, producing the zero increment. Every state has a
strict self-loop and hence period one.

Therefore the frozen chain is finite, irreducible, aperiodic and reversible:
it has the unique stationary law `pi_L`.

This theorem is about correctness and ergodicity, not useful mixing time.

## 6. Frozen implementation and development audit

Accepted source files at the formal pin are:

```text
PREREG.md
README.md
dual_cycle_kernel.py
verify.py
```

`dual_cycle_kernel.py` owns the independent cell indexing, SHA-256 bitstream,
exact bounded draws, cycle generators, proposal word, support firewall and
exact dyadic Metropolis decision.

`verify.py` is an audit, not the proof source. It must reproduce exactly:

- `partial boundary = 0` for every frozen generator at `L=2,3`;
- rank of the plaquette boundary map and full generator span at `L=2,3`;
- the exact Metropolis support-exponent identity;
- 2,000 deterministic `L=2` transitions, with closure/support checked after
  every accepted state;
- a stable final state SHA-256.

The verifier must be deterministic, use only the Python standard library,
write empty stderr and match `EXPECTED.txt` byte for byte on CI.

## 7. Later Ward cross-check execution contract

This source-freeze PR does not consume pilot statistics. After merge, issue
#756 remains open for a separately pinned zero-evidence execution against
primal states on `L=6,8`.

Before that execution opens any decision output, the following must be frozen:

```text
four independent dual chains per L (two seed families),
thermalisation and thinning schedule,
primal state/observable input hashes,
plaquette orientations and separation vectors,
blocking rule and autocorrelation estimator,
Ward comparison uncertainty rule,
terminal precedence.
```

The mandatory independent comparisons are:

1. the contact score/current identity in the orientation convention used by
   the existing exact note;
2. for distinct plaquettes and the preregistered separations,

```text
Cov_mu(G_p,G_q) = -kappa^(-2) Cov_nu(n_p,n_q),
```

within the prospectively frozen Monte-Carlo uncertainty budget;
3. the declared integer current `j=partial n/5` and the low-momentum screening
   statistic required downstream by the photon contract.

A failed cross-check cannot be called evidence against a photon phase until
implementation integrity and mixing have passed. The allowed engineering
terminals are

```text
DUAL_CROSSCHECK_PASS
STOP_DUAL_MIXING
STOP_DUAL_INTEGRITY
BREAK_DUAL_DICTIONARY
```

where `BREAK_DUAL_DICTIONARY` requires a reproducible mathematical or exact
finite counterexample to the declared primal/dual identity, not a statistical
mismatch from an unmixed chain.

## 8. Relation to production freeze #757

Merge of this source-freeze package satisfies only the explicit #757
precondition that the independent dual cross-check have a **frozen
implementation**. It does not mean the cross-check has passed.

The final production preregistration may therefore be drafted and frozen after
this implementation merge, but production under #742 must retain a hard
firewall:

```text
PHOTON_EVIDENCE is unavailable until the later #756 cross-check returns
DUAL_CROSSCHECK_PASS.
```

Issue #748, the independent saved-state observable reader, remains separate and
must own periodic wrapping and connected-block reconstruction before those
observables can contribute to a production phase label.

## 9. Status boundary

This package proves no photon, phase, thermodynamic limit, polarization,
continuum limit, pole identification, contraction/expansion, matter/light
split, or SI statement. It moves no Canon, Registry, Frontier or gate row.

Maximum status:

```text
INDEPENDENT_DUAL_IMPLEMENTATION_FROZEN
ZERO_ENGINEERING_ONLY
```
