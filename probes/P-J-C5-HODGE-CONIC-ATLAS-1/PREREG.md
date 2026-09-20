# PREREG: P-J-C5-HODGE-CONIC-ATLAS-1

**FORMAL PUBLIC PROBE PREREGISTRATION / NO CANON STATUS.**

Owner: A. M. Thorn / C5 Hodge conic atlas session 2026-09-19
Action layer: L1
Authority basis: Public Canon v89
Issue lock: #1053
Branch: `probe/P-J-C5-HODGE-CONIC-ATLAS-1`

## Equation / decision target

Let A5 act on the marked augmentation-root carrier V=A4 tensor Q and on
W=Lambda^2 V.  The marked orientation gives W=W_+ direct-sum W_-.

Enumerate the Sylow-5 subgroups P of A5.  The frozen target count is six.
For each P define

```text
T_P = Fix_(W_-)(P).
```

The targets are:

```text
dim T_P = 1 for every P,
the six T_P are distinct.
```

For every nonidentity c in P put

```text
L_c = Lambda^2(I+c^2).
```

The frozen cross-image identity is

```text
im(P_- L_c P_+) = T_P
```

for all 24 order-five elements.  Consequently E_P=W_+ direct-sum T_P is the
fixed-c predictive carrier.  The Hodge sign certificate makes every E_P a
four-dimensional quadratic space of signature (3,1).

With the positive metric -beta on W_-, the six lines are preregistered to
satisfy

```text
<T_P,T_Q>^2/(<T_P,T_P><T_Q,T_Q>) = 1/5,  P != Q,
sum_P Pi_(T_P) = 2 I_3.
```

Thus the real lines form one six-line equiangular tight frame.

At the ramified place, use the exact A4 quotient-to-W5 isometry and the public
residual Gram g_5.  Each same Sylow-5 subgroup is preregistered to have one
fixed projective line in W5.  The six finite fixed lines must be distinct and
must equal exactly

```text
{[x] in P(W5): g_5(x,x)=0}.
```

Finally, the normalizer of every Sylow-5 subgroup inside A5 must have order
ten; the six labels are the A5/D5 orbit.

## Code and carrier

`verify.py` is Python standard-library only.  It uses exact Fraction
arithmetic, an exact two-component implementation of Q(sqrt(5)), and exact
mod-five arithmetic.  The A5 group, all Sylow subgroups, all 31 projective
lines of P(W5), the Hodge carriers and the ramified quotient map are generated
inside the verifier.  No table of the six target lines is supplied as input.

## Systematics and controls

1. The marked A4 root orientation fixes the Hodge sign.
2. All 24 order-five elements are checked, not one generator per subgroup.
3. Real line comparisons are projective and use rank, so no arbitrary vector
   normalization can make the cross-image condition pass.
4. The angle test uses the metric-invariant squared ratio.
5. The tight-frame test sums metric orthogonal projectors, so rescaling any
   line representative is irrelevant.
6. The finite target is obtained independently by enumerating all projective
   lines and testing the public residual quadratic form.
7. The same Sylow subgroup object labels the real line and the finite line.
8. Normalizer size and transitivity are checked from the complete 60-element
   A5 enumeration.

## Failure threshold

There is no tolerance.  The probe fires on any exact failure of:

- six Sylow-5 subgroups;
- one-dimensionality or distinctness of the real or finite fixed lines;
- any of the 24 cross-image identities;
- the pairwise squared angle 1/5;
- the projector sum 2 I_3;
- normalizer order ten or transitivity;
- equality of the six finite fixed lines with the complete W5 isotropic conic.

Any changed preregistration or verifier bytes after the pin is STOP.

## Explicit nonclaims

The six E_P are mathematical Lorentzian predictive charts only.  The probe
does not select one as physical, identify its negative line with physical
time, derive an observer or physical spatial dimension, construct native-U
transport, select a decoder, or supply probability, measure, SI or L2-L6
content.
