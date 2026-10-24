# Formal separation principle and bridge contract

**Status:** PUBLIC-source, NON-CANONICAL. New abstract deductions are
candidate-T pending independent review. Action layer L1 only.

No new computation is used here.

## 1. Read sufficiency is a factorization property

Let (X) be a declared complete state set. Let

[
R:X	o Y
]

be one read, and let (mathcal F={F_alpha:X	o Z_alpha}) be a declared
family of admitted responses, future reads or context changes.

### Definition 1: sufficiency relative to a family

The read (R) is **sufficient for (mathcal F)** when for every
(alpha) there exists a map

[
ar F_alpha:R(X)	o Z_alpha
]

such that

[
F_alpha=ar F_alphacirc R.
]

This is a relative definition. Enlarging (mathcal F) can destroy
sufficiency without changing (R).

### Proposition 1: factorization criterion

The following are equivalent:

1. (R) is sufficient for (mathcal F).
2. For every (x,yin X),

   [
   R(x)=R(y)
   quadLongrightarrowquad
   F_alpha(x)=F_alpha(y)
   quad	ext{for every }alpha.
   ]

#### Proof

If (F_alpha=ar F_alphacirc R), equal (R)-values give equal
(F_alpha)-values.

Conversely, assume condition 2. For (rin R(X)), choose any (x) with
(R(x)=r) and define

[
ar F_alpha(r):=F_alpha(x).
]

Condition 2 makes this independent of the chosen representative. Hence
(F_alpha=ar F_alphacirc R). (square)

### Corollary 1

One witness

[
R(x)=R(y),
qquad
F_alpha(x)
e F_alpha(y)
]

is enough to prove that (R) is not a complete predictive state for the
family containing (F_alpha).

This says nothing about whether (R) remains sufficient for a narrower
family.

## 2. Hodge instance: same-source context change

Source:
[`C-HODGE-OBSERVATION-STABILITY-N/PROOF.md`](https://github.com/mathorn1973/twist-j/blob/1bf5b154a049f5b70ac199c3997aee8f0026ce52/notes/C-HODGE-OBSERVATION-STABILITY-N/PROOF.md).

On the declared full real source carrier (W_mathbb R), the source note
defines fixed-direction reads

[
pi_a(w)=P_+w+Pi_aP_-w.
]

For distinct directions (a,b), it constructs

[
d=t_b-Pi_a t_b
]

with

[
pi_a(d)=0,
qquad
pi_b(d)=rac45t_b
e0.
]

Apply Proposition 1 with

[
R=pi_a,
qquad
F_b=pi_b.
]

Then (pi_a) is not sufficient for the same-source operation family that
includes the (b)-context read on all of (W_mathbb R).

### Boundary

The source note explicitly keeps two distinctions.

First, on the exact rational or integral algebraic source class, (P_+) can be
injective, so the displayed full-real collision does not establish a setwise
no-go there.

Second, simultaneous symmetry transport

[
pi_{ga}(gw)=gpi_a(w)
]

transforms source and context together. It is not the same problem as
reconstructing (pi_b(w)) from (pi_a(w)) for one unchanged source.

## 3. Exact reconstruction and real stability are different claims

The same Hodge source proves exact semilinear reconstruction on its algebraic
class while also exhibiting an unbounded integral family with

[
P_+w_n	o0,
qquad
|P_+Lw_n|	oinfty.
]

Therefore set-theoretic exact recovery and continuous one-place real recovery
are separate properties.

This matters for any future physical bridge. A claim about exact symbols cannot
silently become a claim about finite-resolution observations. The bridge must
declare a topology or error metric and an admitted preparation domain.

No universal detector-noise lower bound follows from the unbounded family.

## 4. Reversible collision requires a counted destination

Source for the obstruction:
[`C-U-ION-NATIVE-HISTORY-AUDIT-N/PROOF.md`](https://github.com/mathorn1973/twist-j/blob/edf4b386d42971279a895f0f400742e6666ca013/notes/C-U-ION-NATIVE-HISTORY-AUDIT-N/PROOF.md).

Source for the constructive witness:
[`P-U-ION-NATIVE-COMPRESSION-1/RESULT.md`](https://github.com/mathorn1973/twist-j/blob/723fc7d8da6a3cb9b626da31bbea247d15666d41/probes/P-U-ION-NATIVE-COMPRESSION-1/RESULT.md).

Let (|xangle,|yangle) be orthogonal pure input codewords and let an exact
isometry (U) produce the same pure prescribed data codeword
(|etaangle_D) for both.

Because (U|xangle) and (U|yangle) are pure and have the same pure data
marginal, each output factors as

[
U|xangle=|etaangle_Dotimes|r_xangle_R,
qquad
U|yangle=|etaangle_Dotimes|r_yangle_R.
]

Isometry preserves the inner product, so

[
0
=
langle x|yangle
=
langle r_x|r_yangle.
]

### Proposition 2: retained distinction

If reversible evolution maps two orthogonal inputs to one exact pure prescribed
data output, their distinction must remain in an orthogonal counted output
outside those prescribed data.

In particular, the complete output cannot be identical.

### Approximate data-only boundary

For a unitary (V) acting only on the prescribed data and one common target
(|etaangle), define

[
p_x=|langleeta|V|xangle|^2,
qquad
p_y=|langleeta|V|yangle|^2.
]

Since the projector onto (operatorname{span}{|xangle,|yangle}) is
bounded by the identity,

[
p_x+p_yle1.
]

Thus at least one complete-data error is at least (1/2). This is the
restricted endpoint obstruction already recorded by the source audit.

## 5. Native-memory instance

For the actual first native collision, the source audit identifies two
orthogonal inputs with (s=3) and (s=4) that require the same prescribed
data output.

The exact compressed construction at PR #1371 instead returns distinct counted
memory labels

[
M_1=3,
qquad
M_1=4,
]

while all 25 declared complete input/output columns pass with normalized
amplitude (+1).

This instantiates Proposition 2. The information has left the prescribed data
and remains in the complete state.

The construction does not show that this memory ion is a spacetime coordinate,
a Hodge line, or a unique physical memory architecture.

## 6. Complete state, read and event are three typed objects

The two instances support the following discipline.

### Complete state

A complete state (X) contains every degree of freedom whose output may retain
information relevant to the declared future operation family. In a physical
apparatus claim this includes every counted memory, motion, controller, work
source or environment output that the claim does not explicitly quotient.

### Contextual read

A read

[
R_c:X	o Y_c
]

may be sufficient for one operation family and insufficient for another.
Its dimension is therefore not automatically the dimension of (X).

### Event geometry

A physical event geometry is a separate object. Its coordinates need not encode
all internal memory or all predictive state variables. Conversely, a
Lorentzian signature on a predictive carrier does not by itself define event
positions or a trajectory law.

Hence none of the implications

[
dim X=dim Y_c,
qquad
Y_c=mathcal E,
qquad
	ext{memory coordinate}=	ext{time coordinate}
]

is licensed without an additional bridge.

## 7. Bridge contract

The following is a **definition of required input for a future claim**, not a
claim that the input exists.

A proposed complete bridge is a typed tuple

[
mathcal B=
(X_{m phys},A,U,C,{R_c},mathcal E,E,
sim_X,sim_E,mathfrak I,mathfrak A).
]

It must declare at least:

1. **Physical state carrier (X_{m phys}).**
   All degrees of freedom counted at the claimed endpoints, plus the equality
   relation (sim_X).

2. **Preparation domain (Asubseteq X_{m phys}).**
   The actually admitted initial states, including bounds needed for any
   topology or error statement.

3. **Update/contact family (U).**
   Fixed input-independent rules or a completely accounted controlled family,
   including every retained output resource.

4. **Context family (C) and reads (R_c).**
   Domain, codomain, equality and physical availability of every context used
   by the claim.

5. **Event carrier (mathcal E), equality (sim_E), and event map (E).**
   The event object must be independently stated rather than identified with a
   convenient predictive carrier by notation.

6. **Influence relation (mathfrak I).**
   The rule connecting update/contact relations in (X_{m phys}) to event
   displacement, causal adjacency or causal order in (mathcal E).

7. **Accuracy structure (mathfrak A).**
   A topology, metric or exact equality convention sufficient to distinguish
   algebraic recoverability from finite-precision stability.

8. **Context overlap or transport law.**
   If two reads are called coordinate descriptions of one event geometry, the
   overlap relation must be stated on the actual common domain. A source
   transformation and a same-source context change must not be conflated.

9. **Information accounting.**
   Any distinction lost from one read but needed by an admitted later response
   must have an explicit counted destination.

10. **Layer typing.**
    This note is L1 only. Any future claim that moves from the mathematical
    state/read statements here to L2-L6 or to a physical realization requires
    the corresponding named public gate before promotion.

## 8. What would count as closure

This note does not require global uniqueness of all readings.

A future bridge can close positively with multiple coordinate systems if their
domains, equivalence and overlaps are explicit and the same declared physical
apparatus supplies them.

A future bridge can also show that additional internal state is physically
necessary while the event geometry remains four-dimensional. There is no
contradiction in that outcome.

What is not allowed is to infer event dimension from complete-state dimension,
or to infer complete-state sufficiency from one restricted read, without the
factorization and bridge obligations above.

## 9. Status

- Proposition 1: candidate-T, elementary set-theoretic proof above.
- Proposition 2: candidate-T, elementary isometry proof above.
- Hodge instantiation: no stronger than its NON-CANONICAL source status.
- Native instantiation: no stronger than the PASS NON-CANONICAL conditional
  ideal-model source.
- Bridge contract: definition only.
- Physical event geometry: OPEN, not constructed here.

No Canon promotion is requested.
