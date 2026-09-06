# Fixed-reader frequency classification

Status: NON-CANONICAL incubation, candidate-T, L1 only. Issue #861.
This is a mathematical classification of the preregistered reader class,
not an adopted physical occurrence law. The finite certificate is audited
by the separately pinned `verify.py` and reported in `EXPECTED.txt`.

## 1. Whole atoms, not divisible probabilities

Fix one synchronized chart label and its native orbit. CLOCK-PROOF.md
establishes the limiting frequencies of every present-state atom, along
all prefix lengths. Let the distinct atoms have positive rational weights
`w_1,...,w_k`, summing to one. A time-independent reader assigns each atom
one symbol. Conversely every assignment on this finite support extends to
a reader on the entire preregistered domain by assigning arbitrary values
off the support. Thus, for any finite output alphabet, the complete set
of output frequency vectors consists exactly of the sums over partitions
of these atoms. This classifies all functions, with no linearity assumption.

For a binary checkpoint reader the attainable LOW densities are exactly
the subset sums of checkpoint weights. For a decorated reader allocate
each whole atom to LOW, HIGH or SILENT. If their masses are `a,b,1-a-b`,
the accepted LOW frequency is `a/(a+b)` when `a+b>0`. When `a=b=0`, the
accepted frequency is UNDEFINED. This normalization follows from convergence
of the two count sequences and positive limiting acceptance density.
No fractional allocation of an individual atom is permitted.

The finite verifier independently uses the following exact recursions.
Choose a common denominator `D` and let `d_i=D*w_i` be positive integers:

    S_0 = {0}
    S_(i+1) = S_i union {s+d_(i+1): s in S_i}
    B_0 = {(0,0)}
    B_(i+1) = B_i union {(a+d_(i+1),b): (a,b) in B_i}
                       union {(a,b+d_(i+1)): (a,b) in B_i}.

Induction on the number of atoms proves necessity and sufficiency of
both recursions. The three terms in the second recurrence are respectively
SILENT, LOW and HIGH. This is finite exhaustion of the complete class,
not a selection of a favorable reader.

## 2. Closed form of the finite spectra

Write `w=(alpha,beta,gamma,delta)` for the first four chart labels.
The fifth label translates a residue coordinate and does not change the
weight multisets. CLOCK-PROOF.md supplies the following complete list:

| Domain and normalization | `w != 0` | `w = 0` |
| --- | --- | --- |
| Checkpoint atoms | 20 copies of 1/20 | 10 copies of 1/10 |
| Decorated atoms, all ticks | 10 copies each of 1/60, 2/60, 3/60 | 10 copies each of 1/30, 2/30 |
| Decorated atoms conditional on either fixed driver bit | 5 copies each of 1/30, 2/30, 3/30 | 5 copies each of 1/15, 2/15 |

Each driver bit has total density 1/2 before conditioning. The preregistration
uses the aliases Snap-only and Flow-only without fixing which names denote
bit zero and bit one. Here both bit restrictions are classified explicitly;
their attainable sets are equal, so this naming ambiguity changes no result.
No additional clock window or parity reader is introduced.

For completeness, the integer weights in every nonuniform row can be
allocated to any three nonnegative integer bin loads with the same total.
For `m` copies each of 1, 2 and 3, with `m>=2`, start with loads totaling
`6m`. Assign the `m` coins of value 3 greedily to any bin with capacity at
least 3. Before the final such assignment, the total remaining capacity is
at least `3m+3>6`, whereas three bins all smaller than 3 could hold at most
6. Therefore this stage cannot stall. Next distribute all `m` coins of
value 2. Before the final such assignment remaining capacity is at least
`m+2>3`, whereas bins all smaller than 2 hold at most 3. Finally fill the
remaining capacities with the `m` ones. All capacities and steps are integer.
For `m` copies each of 1 and 2, start at the second stage with total `3m`;
the same argument applies. This proves the complete triangular two-bin
spectrum. It applies here with `m=10` and `m=5`.

Consequently:

| Reader class | `w != 0` | `w = 0` |
| --- | --- | --- |
| Binary checkpoint LOW density | `{k/20: 0<=k<=20}` | `{k/10: 0<=k<=10}` |
| Decorated LOW density, all ticks | `{k/60: 0<=k<=60}` | `{k/30: 0<=k<=30}` |
| LOW density conditional on bit 0, or conditional on bit 1 | `{k/30: 0<=k<=30}` | `{k/15: 0<=k<=15}` |
| LOW fraction among accepted events | `F_60` | `F_30` |
| LOW fraction among accepted events with either bit restriction | `F_30` | `F_15` |

Here `F_D={a/b: 0<=a<=b<=D}`, interpreted as a set of rational numbers;
equivalently its reduced denominators are at most `D`. Indeed any pair of
integer loads `a,c>=0`, `1<=a+c<=D`, yields `a/(a+c)`. Conversely every
`a/b` with `b<=D` is realized by loads `(a,b-a,D-b)`.
Empty acceptance is additional tagged undefined data, not a member of `F_D`.

These are per-orbit attainable sets. They do not assert that one global
reader realizes independently specified target values on every chart label
at once: different oriented labels can share atoms and constrain each other.
For excluding a target on a particular orbit, the complete per-orbit set
already suffices. No ensemble averaging over preparations is included.

## 3. Comparison with inherited QDD targets

The classification above uses only native dynamics and the frozen reader
class. Only after constructing these sets does the verifier enumerate the
inherited supported QDD head weights. For balanced pistons
`v=(ell(p1),ell(p4),ell(p1p),ell(p4p))`, `ell=(0,1,2,-2,-1)`, put
`s=sum(v)` and `q=sum(v_i^2)`. On the supported domain `5q-s^2>0`, the
normalized LOW weight is exactly

    s^2 / (4*(5q-s^2)).

All 624 nonzero piston tuples are enumerated, with no division at zero.
The full membership comparison, including any failed target, is retained
in the exact stdout. No comparison selects or adopts a reader.

In particular `1/256` lies outside even the largest accepted-event spectrum
`F_60`: its reduced denominator is 256, and it is smaller than its least
positive member 1/60. This supported QDD value therefore cannot be supplied
by any reader in this frozen class on any synchronized orbit. Allowing
SILENT and either driver bit does not repair that obstruction. The value
`9/14` belongs to the accepted-event spectra (14<=15), but its attainability
does not supply a target-independent physical choice of the corresponding
atom partition. Both statements concern exact infinite-prefix limits.

Thus this complete restricted class cannot reproduce the entire supported
QDD target law. This is a negative disposition of the present fixed-reader
route, not a proof that general physical sampling is impossible. Readers
with clock windows, changing contexts, extra memory, interventions or
different dynamics remain outside the frozen class and are not silently
added to it. Original-head information lost in native mergers also remains
unrecoverable, independently of the frequency obstruction.
