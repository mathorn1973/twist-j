# Deterministic permutation profile on a native common-ready orbit

**NON-CANONICAL / DEFINITION AND CONDITIONAL MODEL COMPOSITION.** This note
proposes a deterministic calendar using the three already separated inputs:
the common-ready source inverse, the fixed incidence word, and permutation
counts. It changes no pinned probe, existing claim scope, Canon file or
physical obligation. It records no scientific execution, empirical result,
new public T claim, adopted probability measure or physical realization.

**Preparation status: READY for nonnormative reconciliation.** Exact inputs
are [native common-ready inverse](../../probes/P-QDD-V80-CLOSURE-BOUNDARIES-1/NATIVE-PROOF.md),
sections 2--4; [incidence source, slots and record equality](../../probes/P-U-PREPARATION-EVENT-RECORD-1/INCIDENCE-PROOF.md),
sections 1--5; and [permutation counts](../../probes/P-QDD-V80-CLOSURE-BOUNDARIES-1/OCCURRENCE-PROOF.md),
section 4. The first and third are frozen in public pin
`9a0b42fe75b91181b8806ac618f7c54ff5b4cb85`. The incidence input is the
unchanged file at `canon-v79`, SHA-256
`5538718c55cabb07702a5d6d7daaecdcb4a8f5775f6863a5fc9ca39ba70910aa`,
also pinned as a source by that joint probe. This proposed composition does
not change any of those inputs.

## Inputs and fixed choices

Keep unchanged origin-zero U and one common ready `(q,r)=(0,1)`. Its source
is any `p in F_5^4`. At a query, the input is the complete current checkpoint
and actual native counter `(n,F_n(p,0,1))`. The common-ready inverse
recovers p at every n. Apply the existing balanced lift to obtain
`v in {-2,-1,0,1,2}^4` and its fixed word

```text
e_v:Z/M->{LOW,HIGH,SILENT}, M=1024,
s=sum_i v_i, Q=sum_i v_i^2,
A=s^2, B=5(4Q-s^2), D=A+B.
```

These are the already specified Cartesian incidence slots, not a new
coupling. D>0 exactly for v!=0. Source recovery uses full current-state
access; the apparatus-only `(q,r)` history does not acquire this capability.
The source remains the original p of one orbit throughout. The trial
labels below do not mean new physical preparations or resets of U.

Choose once, independently of p and its target ratio,

```text
n_*=2562, T=M^2=1048576, P=M!.
```

The anchor is at the existing wholly synchronized length-2560 native
history threshold. The actual counter is already an explicit input here;
the anchor does not derive a physical onset marker or initial alignment.
Before n_* this profile returns UNAVAILABLE and no trial record.

## Total order and calendar

Enumerate every permutation of `(0,...,M-1)` in lexicographic order, with
indices `0,...,P-1`. Define

```text
pi_b=unrank_lex(b mod P),
s_b=n_*+bT, E_b=s_b+T-1, b=0,1,2,... .
```

Unranking is total finite arithmetic: repeatedly divide the remaining
rank by `(M-1-j)!`, select that indexed member of the ascending unused
addresses, remove it, and retain the remainder. No measured output, source
coordinate, QDD ratio or target comparison enters this order constructor.

The b-th trial occupies integer cuts `s_b,...,E_b`. For pi_b=(r_0,...,r_(M-1))
define its address visits by

```text
tau_(b,0)=s_b+((r_0-s_b) mod M),
tau_(b,j)=tau_(b,j-1)+((r_j-r_(j-1)) mod M), 1<=j<M,
```

where mod M takes values `0,...,M-1`. The first visit is inclusive: if the
first requested address is the trial's initial phase, it is visited at s_b.
Every later requested residue differs from its predecessor, so every later
increment is in `1,...,M-1`. The visits are strictly increasing, have the
requested native residues, and satisfy

```text
s_b <= tau_(b,0),
tau_(b,M-1) <= s_b+(M-1)+(M-1)^2
             =s_b+M(M-1) < s_b+M^2.
```

Thus every trial's M address visits fit within its own interval, regardless
of its initial phase. In particular `n_* mod M=514` causes no exception.
The next trial starts at E_b+1; no visit is shared by two trials. The model
continues chronological native acquisition and uses these selected visits
only for slot inspection. It does not reorder or omit the acquired bits.
It changes the invocation schedule relative to the consecutive first-hit
class, so the common-onset obstruction remains intact.

## Individual outcomes and virtual records

All M visits are fixed independently of v. If v!=0, let j_b(v) be the least
j with `e_v(r_j)!=SILENT`, which exists because the permutation covers all
addresses. Its selected label is exactly `e_v(r_(j_b(v)))`. At completion
cut E_b, define one virtual trial record containing

```text
(trial=b, source=v, completion_cut=E_b,
 first_hit_index=j_b(v), first_hit_cut=tau_(b,j_b(v)),
 first_hit_address=r_(j_b(v)), label=e_v(r_(j_b(v))),
 fine_slot_and_sign=the existing incidence descriptor).
```

The word supplies one label at its first occupied scheduled visit; the
completion convention returns that record only at E_b, after every
scheduled visit. It introduces no physical cell. If v=0, the completion
record instead has disposition NO_EVENT and no accepted label, hit index,
hit address or sign. NO_EVENT is not counted as LOW, HIGH or an accepted
event; its accepted ratio is UNDEFINED.

Source equality is literal ordered four-integer equality; in particular v
and -v remain distinct sources. Record equality compares every displayed
field literally, including sign, index and absolute time. History equality
is literal ordered tuple equality, with no sign, phase, permutation or
time-shift quotient. Equal coarse LOW/HIGH labels do not identify records.

At any n>=n_*, the complete returned history consists of the records with
E_b<=n. Their number is exactly `floor((n-n_*+1)/T)`. Every field is a
deterministic function of recovered v, b and the fixed constructor, so the
history can be regenerated from current checkpoint and counter, without a
saved source or an earlier archive as another input. A query before a
trial's completion does not emit its eventual record, even if its first
hit has occurred. Literal histories preserve trial indices and absolute
times; these complete records are not identified under a period shift.

This specifies each individual result, not only a histogram. For the first
trial the lexicographic permutation is `(0,1,...,1023)`. Consequently every
supported source with s!=0 has first label LOW; supported sources with s=0
have HIGH. This deterministic first-trial prediction is not a Born law.

## Exact cycle counts and limits of the composition

Across P consecutive trials beginning at b=0, each permutation occurs once.
For any fixed nonzero source, each of its D occupied addresses is first
among those D addresses in exactly P/D permutations, by the existing
permutation bijection. Hence

```text
LOW trials = P*A/D, HIGH trials = P*B/D, accepted trials = P.
```

These are exact integers and counts. No uniform measure on orders has been
imported: every order is actually specified by the mathematical calendar.
The coarse label and within-trial waiting-offset sequences have period P,
because T is a multiple of M. Every prefix N=qP+t of completed trials has
LOW count `qPA/D+R_LOW(t)`, where R_LOW(t) is the exact count in the first
t listed permutations and `0<=R_LOW(t)<=t<P`. Its deterministic trial-count
ratio therefore tends to A/D. This is a conditional model count limit,
not an adopted physical frequency or probability. At zero, every trial is
NO_EVENT and there is no accepted ratio.

One full count period costs `M^2 M!` native cuts under this schedule and
has `M M!` scheduled address inspections. The M^2 bound controls address
waiting only; it assumes the prescribed order is available to the model
when needed. It is not a runtime bound for permutation unranking, source
decoding or archive regeneration. A direct implementation retains an
order and scan position; virtual recomputation trades that memory for
calculation. Printing a growing complete history also has growing output
cost. No finite-speed physical controller has been derived.

Thus explicit enumeration removes the need for an assumed uniform
permutation measure when the desired statement is the exact mathematical
whole-cycle trial profile. It does not give independent trials, a
single-trial probability law, physical readiness or full-state access,
incidence coupling, writable storage, reset, physical calendar control or
feedback into U. Those remain separate obligations. The result is a
specified deterministic model alternative, not full physical closure.
