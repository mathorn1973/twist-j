# Direct Hodge memory under faithful native continuation

**NON-CANONICAL; L1; candidate-T conditional analytical obstruction.**
This note records a restriction on a proposed identification of retained ion
history with Hodge predictive memory. It is not a new ion result, a numerical
test, or a retrospectively preregistered falsification. The broader
identification remains a hypothesis, untested at this scope. Public Canon v97
and the physical HOLD are unchanged.

## 1. Exact claim and domain

Let X be a declared extended state set, D the original data state set
**including the counter**, and pi:X -> D the map forgetting the added state.
Let F:X -> X and U:D -> D be the proposed extended and source updates. The
identities below are required only on a declared domain Omega subset X.
Write K=Q(sqrt(5)) for the Hodge coefficient field, to distinguish it from
the update F. Let r:D -> K and m:X -> K be fixed readings.

Assume faithful continuation

$$
\pi(Fx)=U(\pi x)\qquad(x\in\Omega)
$$

and direct present reading

$$
y(x)=r(\pi x)\qquad(x\in\Omega\cup F(\Omega)).
$$

No linearity, injectivity, unitarity, reversibility or physical interaction
assumption is needed for the following scalar statement. All functions have
the same declared state semantics; pi is not silently switched between
forgetting classical configuration entries, a Hilbert-space projection and
a partial trace.

**Conditional proposition.** On Omega, the first axial Hodge equation

$$
y(Fx)=3y(x)-m(x)
$$

holds if and only if

$$
\boxed{m(x)=\bar m(\pi x),\qquad
\bar m(d)=3r(d)-r(Ud).}
$$

**Proof.** Substitute the direct reading and faithful continuation:

$$
m(x)=3y(x)-y(Fx)
     =3r(\pi x)-r(U(\pi x)).
$$

Conversely, that formula for m gives the required first equation by the same
substitution. The forced values of bar m concern pi(Omega); the displayed
formula is not a claim that the assumptions hold on every data state.

Consequently, no two x_3,x_4 in Omega can satisfy all of

$$
\pi x_3=\pi x_4,\qquad m(x_3)\ne m(x_4),\qquad
y\circ F=3y-m.
$$

This contradiction already follows from the first equation. It does not
require a second iterate or any further coordinates of the Hodge carrier.

## 2. What the ion collision supplies, and what it does not

The [pinned #1371 proof, section 1](https://github.com/mathorn1973/twist-j/blob/723fc7d8da6a3cb9b626da31bbea247d15666d41/probes/P-U-ION-NATIVE-COMPRESSION-1/PROOF.md#1-fixed-carrier-inputs-and-complete-target)
defines the source selector from the present original coordinates and the
source counter, without M1. Its exact construction covers the prescribed
prepared family I(s,t), with M1=M2=N=0, and the first endpoint O(s,t), with
M1=s, M2=1 and N=1. In its fixed physical coordinate dictionary,

```text
O(s,t): S1=1, S2=t, R1=f(s), R2=(0,0,0,0,3,0),
        M1=s, M2=1, N=1;
f(3)=f(4)=(2,1,3,4,3,1).
```

For a fixed t, x_3=O(3,t) and x_4=O(4,t) therefore have the same original
data and counter and distinct M1 basis states. Here pi means forgetting the
added memory entries of these endpoint configurations while retaining all
original data and the counter. The same prepared dictionary is used on
both configurations. The physical N is finite; the proven transition 0 -> 1
does not realize the source's unbounded counter.

Applying section 1 to this pair as inputs to a *further* step requires two
additional premises:

- A continuation domain Omega containing both occupied-memory endpoints,
  with pi F=U pi on them. The globally defined ion unitary does not by itself
  prove this source-law identity outside the prepared input subspace.
- A declared Hodge-field reading m that distinguishes these two states.
  Orthogonal physical states M1=3 and M1=4 do not by themselves specify
  different numerical Hodge values m_3 and m_4.

With these premises and y=r pi, the direct identification is excluded by
section 1. Without either premise, this note does not conclude a contradiction
in #1371. In particular, it does not claim to have tested repeated application
of the 64-block program on occupied memory. The [pinned result](https://github.com/mathorn1973/twist-j/blob/723fc7d8da6a3cb9b626da31bbea247d15666d41/probes/P-U-ION-NATIVE-COMPRESSION-1/RESULT.md)
remains a conditional first-step construction on its supplied input span.

## 3. The full axial pair and its two-step requirement

A positive identification must require both equations at the same boundary:

$$
y(Fx)=3y(x)-m(x),\qquad m(Fx)=y(x).
$$

Set

$$
\Omega_2=\{x\in\Omega:F(x)\in\Omega\}.
$$

For x in Omega_2, the first equation and faithful continuation apply at x
and Fx, and the direct reading applies at x, Fx and F^2x. Applying the
forced formula for m at Fx and then the second equation at x gives

$$
3r(Ud)-r(U^2d)=m(Fx)=r(d),\qquad d=\pi x.
$$

Hence

$$
\boxed{r(U^2d)-3r(Ud)+r(d)=0\qquad(d\in\pi(\Omega_2)).}
$$

No recurrence outside this two-step domain is inferred. On a partial domain,
the recurrence alone need not ensure compatible memory values at the output
boundary. Even a valid full axial pair does not establish the update of the
other coordinates in the four-dimensional Hodge realization.

The source [J-HODGE-PREDICTIVE-CLOSURE and J-HODGE-SEMILINEAR-MEMORY, Canon v97](https://github.com/mathorn1973/twist-j/blob/82ecf0aac0ee79c947000968e71573d4c65d386d/canon/CANON.md#j-hodge-semilinear-memory-t)
concerns one fixed marked J: the present triple and one previous axial value
attain the four-dimensional K-linear predictive minimum, and the axial
recurrence is y_(n+2)=3y_(n+1)-y_n. This is not a physical time identification
or a result for arbitrary changing directions. The exact rational-source
triple already has a closed Q-linear, non-K-linear update if Galois
conjugation is allowed. The four-dimensional minimum must therefore retain
its K-linear qualification. The elementary scalar obstruction in section 1
does not assume linearity of r or m.

## 4. Distinct successor questions

If memory makes two states with the same pi-image acquire different next
original data, then pi F=U pi cannot hold on both for the same U. This changes
the declared continuation, for example by adding a separately declared
contact between source steps. Faithfulness must be stated at the resulting
boundaries, not attributed to the unchanged source step.

If preserving U is the requirement, a different question is to admit a
memory-dependent present triple,

$$
Y=\widetilde R(D,M,\ldots),
$$

in place of Y=R pi. Equal original data can then have different readings of
the present, so the direct-reading premise of this obstruction need not hold.
If the axial component still factors through pi, however, section 1 still
applies to that component. Merely allowing dependence on memory does not
construct a Hodge update.

Such a successor must fix its state domain, reading and equality convention
independently of the outcomes to be explained, give the full subsequent
update, and check every coordinate of the claimed Hodge realization. Its
existence and noncircularity remain unproved here. No additional ion test of
the excluded conjunction is needed to derive this algebraic obstruction.

Retained history and predictive memory have distinct roles: a history label
that is ineffective for faithful future original data cannot simultaneously
be a different scalar value fixing the next direct reading of those data
through the displayed Hodge equation. This restricts their direct
identification; it does not invalidate history retention.

## 5. Record boundary

This is a local analytical note, with no new scientific execution or public
preregistration. It changes no probe result, public claim status or Canon
file. The broad identification remains NON-CANONICAL and untested; only the
explicit conjunction in sections 1 and 2 has a conditional algebraic
obstruction.

The related [complete-state/readout synthesis at its pinned draft](https://github.com/mathorn1973/twist-j/blob/4a7a89e6aba0182c6dbc904fafa75194df606fd1/notes/C-COMPLETE-STATE-OBSERVATION-SEPARATION-N/PROOF.md)
states a general fibre-factorization criterion and separates retained state
from readout. The present note adds the specific forced formula
m=(3r-rU) pi and the occupied-memory continuation premise. It does not
replace that broader synthesis or assert that its physical bridge exists.
