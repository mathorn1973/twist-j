# P-ENTROPY-LAW-REDUCTION-1

```text
STATUS: PUBLIC PREREGISTRATION, SCIENTIFIC STATUS UNEARNED
AUTHORITY: PROTOCOL PIN ONLY AFTER THIS FILE AND verify.py ARE COMMITTED
TARGET LINE: PUBLIC
OWNER: A. M. Thorn / mathorn1973 / GPT-5.6 Thinking owner session
AUTHOR IDENTITY FOR GIT: A. M. Thorn <thorn@twistj.com>
TARGET REPOSITORY: mathorn1973/twist-j
TARGET BRANCH: probe/P-ENTROPY-LAW-REDUCTION-1
TARGET PATH: probes/P-ENTROPY-LAW-REDUCTION-1/
ISSUE LOCK: https://github.com/mathorn1973/twist-j/issues/226
PUBLIC CANON: Public Canon v27
PUBLIC CONTENT COMMIT: 116b62edf505914d96fcd65318d97f3675c53f85
PUBLIC CANON SHA-256: c7c4c7e6d5a3116e356b060eaf696963285b0f2f465d5f2e1dcda5c094a309f6
BRANCH BASE MAIN: 501f7d9f3d1dc8a915ad7fcc1f33f0673b5b4b8a
ACCEPTED VERIFIER FORMAL EXECUTION BEFORE PIN: NONE
INTENDED STATUS IF PROOF SURVIVES: T
```

This probe targets one theorem internal to the already registered
`GATE-L2-L5-ENTROPY-BRIDGE`. It does not construct the bridge map and does not
close `ENTROPY-LAYER-BRIDGE [O]`.

## 0. Collision and provenance guard

Before this public pin, recheck public `main`, issues, branches,
`probes/`, `notes/entropy-selection-recon`, `canon/REGISTRY.tsv`,
`canon/EVIDENCE.tsv`, `canon/GATES.tsv`, and the v28 fold queue.

The issue-time and pin-time searches found no competing branch, probe, registry row, pull request, or prior issue named `P-ENTROPY-LAW-REDUCTION-1` or
`ENTROPY-LAW-REDUCTION`. The existing branch
`notes/entropy-selection-recon` owns construction and obstruction work for an
actual transfer family. This probe does not take that work. Its scope is the
universal reduction of the already frozen `Law_W` predicate, conditional on
exact equivariance.

Exploratory calculations and independent non-canonical audits preceded this preregistration. They are discovery only and are
not evidence. The accepted `verify.py` in this directory has not been formally
executed. Only syntax and static checks were permitted before this public pin. Issue #219 remains a later record-audit constraint and changes no scientific gate here.

Any changed authority tuple, collision, changed `Law_W`, changed generator
presentation, or changed action-layer contract is a STOP requiring a new
review before pinning.

## 1. Equation

Use the exact Public Canon v27 Route A objects:

```text
mu = m_TM x h_lambda,
tau_src(kappa,y) = (S_K kappa, J y),
P : K_TM x O_(K,lambda) -> F_5^6,
P(tau_src x) = F_(theta(kappa))(P(x))  mu-almost everywhere,
theta(kappa) = kappa_0.
```

Let `u_R` be the probability on `F_5^6` assigning mass `1/6250` to
each state in the public recurrent set `R` and zero elsewhere.

The single target theorem is:

```text
For every measurable total P satisfying exact equivariance mu-almost
 everywhere,

    Law_W(P)  if and only if  P_* mu = u_R.

More precisely, exact equivariance forces

    z_6(P(kappa,y)) = 4 + 2 kappa_-1 mod 5

mu-almost everywhere. Therefore, for every integer n,

    i_(P,n) = 4 + 2 kappa_(n-1) + 2 kappa_n mod 5,

and the selector and pair-00 clauses of Law_W hold at each single time n.
Also tau_src preserves mu, so nu_(P,W) = P_* mu for every nonempty finite
window W, in particular W = {512,...,2047}.
```

Equivalent class description:

```text
A_A = {[P]_mu : P is measurable and total,
                  P o tau_src = F_theta o P mu-almost everywhere,
                  P_* mu = u_R}.
```

This is a reduction of the decision surface, not a decision of nonemptiness.

## 2. Code

Accepted verifier:

```text
probes/P-ENTROPY-LAW-REDUCTION-1/verify.py
```

It audits only exact finite premises:

1. the displayed integer inverse of `M_J` and `det M_J = 1`;
2. the five public generators and their trace laws on all `5^6` states;
3. the two branch trace maps;
4. the exact length-nine Thue-Morse language certificate;
5. the sharp length-nine trace synchronization;
6. the public stationary pair law and the forced selector law;
7. frozen-window arithmetic.

The universal measurable theorem is carried by the proof below. The verifier
is an audit, not the theorem's source.

Python standard library only. Exact `int` and `Fraction` arithmetic. No float.
The formal command after the public pin is:

```text
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
python3 probes/P-ENTROPY-LAW-REDUCTION-1/verify.py
```

## 3. Carrier and data

No external data.

Exact carriers:

```text
F_5^6,
K_TM with substitution sigma(0)=01 and sigma(1)=10,
O_(K,lambda), K=Q(zeta_5), lambda=1-zeta_5,
W={512,...,2047}.
```

Frozen finite certificate data:

```text
branch trace maps
T_0 = (0,4,0,4,4),
T_1 = (2,1,1,3,1),

all four legal two-letter factors 00,01,10,11,

the 24 length-nine factors listed in Section 7,

stationary pair law
(00,01,10,11) = (1/6,1/3,1/3,1/6).
```

The recurrent set `R` is used only as the fixed support appearing in the
public definition of `Law_W`. The proof does not use the computed statement
that recurrent states lie on sheets `{1,4}`.

## 4. Systematics

The proof must survive all of the following.

```text
S1  Direction and index audit: the backward word is
    kappa_-9 ... kappa_-1, and the output depends on kappa_-1.

S2  Almost-everywhere audit: iteration uses one finite intersection of nine
    translated conull sets, justified by tau_src invariance.

S3  Language-completeness audit: every length-nine factor lies in sigma^4(ab)
    for a legal pair ab, and every listed factor occurs.

S4  Trace audit: the reset is derived from the complete public generator trace
    table, not from the recurrent census.

S5  Measure audit: normalized Haar is preserved because multiplication by J is
    a compact-group automorphism, not because of an empirical window.

S6  Pair-law audit: selector masses use the registered stationary Thue-Morse
    pair law and no physical interpretation of 1/6.

S7  Layer audit: this is internal simplification of the existing L2-to-L5 gate.
    It adds no L5-to-L6 measure, entropy rate, physical probability, SI unit,
    regularity, canonicity, or existence claim.

S8  Sharpness audit: length eight is not enough. The allowed factor 10100101
    maps input sheets to (2,1,1,1,1).
```

## 5. Failure threshold

The theorem fails if any one of the following exact events occurs:

```text
F1  a public generator trace law or the branch trace table is wrong;
F2  the frozen list omits or adds a length-nine Thue-Morse factor;
F3  one allowed length-nine factor is not synchronizing;
F4  one synchronized output is not 4+2 times the final bit modulo 5;
F5  tau_src does not preserve mu under the frozen source definition;
F6  the public stationary pair law does not give the selector vector
    (0,2/3,0,1/6,1/6);
F7  a measurable exactly equivariant P satisfies one side of the claimed
    equivalence and not the other;
F8  the argument imports CENSUS-Z5-SHEET, a finite-window limit, or an
    unregistered layer lift.
```

Any change of threshold after the public preregistration pin is forbidden.

## 6. Action layer

```text
Declared layer: MULTI, internal to GATE-L2-L5-ENTROPY-BRIDGE.
From layer: L2 source manifold with its frozen invariant probability.
To layer: L5 finite readout already declared by the owner gate.
New lift: none.
L6 physical measure: excluded.
```

The pushforward probability in `Law_W` is part of the already registered
gate predicate. This theorem only removes redundant clauses under exact
equivariance. It does not create a new physical measure reading.

## 7. Proof

### Lemma 1. Complete branch trace maps

The public generator trace laws are

```text
z_6(a psi)=z,
z_6(b psi)=-z,
z_6(c psi)=2-z,
z_6(d psi)=2-z,
z_6(e psi)=3-z.
```

Since `F_eps(psi)=g_(z_6(psi)+2 eps)(psi)`, direct substitution gives

```text
T_0 = (0,4,0,4,4),
T_1 = (2,1,1,3,1).
```

These are maps from the five input sheets to the output sheet.

### Lemma 2. Exact length-nine language

Let `sigma(0)=01`, `sigma(1)=10`. The word
`sigma^3(0)=01101001` contains all four legal pairs
`00,01,10,11`.

Every length-nine factor of the two-sided Thue-Morse subshift lies in
`sigma^4(ab)` for one legal pair `ab`. Indeed, a level-four supertile has
length `16`; an interval of length `9` meets at most two adjacent level-four
supertiles. Conversely, every factor of `sigma^4(ab)` occurs because every
legal pair `ab` occurs in the subshift.

The resulting exact language has 24 words. Direct composition of `T_0,T_1`
gives:

```text
constant 4, words ending in 0:
001011010 010010110 010110100 011010010
100101100 100110010 100110100 101001100
101100110 110010110 110011010 110100110

constant 1, words ending in 1:
001011001 001100101 001101001 010011001
010110011 011001011 011001101 011010011
100101101 101001011 101101001 110100101
```

Therefore for every allowed word `w=w_0...w_8` and every input sheet `z`,

```text
T_(w_8) ... T_(w_0)(z) = 4 + 2 w_8 mod 5.
```

The reset length is sharp. The allowed length-eight word `10100101` maps the
five input sheets to `(2,1,1,1,1)`.

### Lemma 3. Forced sheet law for every equivariant map

Let `E` be the conull set on which one-step equivariance holds. Multiplication
by `J` is an automorphism of the compact additive group
`O_(K,lambda)` because `J` is a unit. It preserves normalized Haar measure.
The two-sided shift preserves `m_TM`. Hence `tau_src` is invertible and
preserves `mu`.

The set

```text
E_9 = intersection_(r=1)^9 tau_src^r(E)
```

is conull. For `x=(kappa,y)` in `E_9`, iterate equivariance from
`tau_src^-9 x` to `x`:

```text
P(x) = F_(kappa_-1) ... F_(kappa_-9)(P(tau_src^-9 x)).
```

The word `kappa_-9...kappa_-1` is an allowed length-nine factor. Lemma 2
therefore gives

```text
z_6(P(kappa,y)) = 4 + 2 kappa_-1 mod 5
```

on a conull set.

Applying the same statement to `tau_src^n x` gives, for each fixed integer
`n`,

```text
z_6(psi_(P,n)(kappa,y)) = 4 + 2 kappa_(n-1) mod 5.
```

Taking the countable intersection of the translated conull sets gives one
`tau_src`-invariant conull set on which this identity holds for every integer
`n` simultaneously.

### Lemma 4. The selector and pair clauses are automatic

By definition,

```text
i_(P,n) = z_6(psi_(P,n)) + 2 kappa_n mod 5
          = 4 + 2 kappa_(n-1) + 2 kappa_n mod 5.
```

Thus the four pairs map as

```text
00 -> 4,
01 -> 1,
10 -> 1,
11 -> 3.
```

The public stationary Thue-Morse pair law is

```text
P(00,01,10,11) = (1/6,1/3,1/3,1/6).
```

Hence, at every single `n`,

```text
P(i_(P,n)=j) = (0,2/3,0,1/6,1/6)_j,
P(kappa_n=kappa_(n+1)=0) = 1/6.
```

Averaging these time-independent values over the frozen window changes
nothing.

### Lemma 5. The state window is a single pushforward

For every measurable total `P` and every integer `n`, invariance of `mu` gives

```text
(P o tau_src^n)_* mu = P_* mu.
```

Therefore

```text
nu_(P,W) = P_* mu
```

for every nonempty finite window `W`, including the frozen window of 1536
terms.

### Conclusion

For an exactly equivariant measurable total `P`, the selector clause and the
pair-00 clause of `Law_W` are automatic by Lemma 4, and the state clause is
exactly `P_*mu=u_R` by Lemma 5. This proves the displayed equivalence.

## 8. Decision and status discipline

```text
PROOF-SURVIVES:
  written proof remains valid, finite audit passes, no falsifier fires;
  intended result status T because the theorem is proof-first.

PROOF-FAILS:
  one named exact falsifier fires.

STOP:
  stale authority, collision, changed scope, changed Law_W, formal execution
  before the public pin, unregistered layer lift, or inability to preserve the
  exact preregistration files and hashes.
```

Even `PROOF-SURVIVES` does not close `ENTROPY-LAYER-BRIDGE [O]`. It leaves one
precise remaining positive obligation:

```text
construct one measurable total exactly equivariant P with P_*mu=u_R.
```
