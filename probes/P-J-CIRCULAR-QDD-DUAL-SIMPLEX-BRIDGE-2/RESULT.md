# P-J-CIRCULAR-QDD-DUAL-SIMPLEX-BRIDGE-2 result

Status: **candidate-T / L1 / TWO CLAIMS CONFIRMED / ARCHITECTURE GATE PENDING / PUBLIC CLAIMS UNREGISTERED / CANON UNCHANGED**

## Recorded decision

```text
J-CIRCULAR-QDD-DUAL-SIMPLEX-BRIDGE:                  CONFIRMED
J-CIRCULAR-QDD-SIGNED-AFFINE-PROJECTOR-INTERTWINER: CONFIRMED
gates:                                               15/15 PASS
exit/stderr:                                         0 / empty
stdout:                                              byte-identical to EXPECTED.txt
SCIENTIFIC-FIRED-A/B:                                NOT SELECTED
STOP:                                                NOT SELECTED
ABANDONED-PIN:                                       NOT SELECTED
ARCHITECTURE GATE:                                   PENDING
MANUAL SECURITY REVIEW:                              PENDING
```

The immutable successor verifier was executed exactly once after public pin
`2d33ad06044b78f5e204fe28d966e8f66e043953` and byte-for-byte remote
readback. Its 26-line stdout has SHA-256
`6d512d1efe4f93505f69fc3cfe21182f02b7fd40cb052a59a7eb5095013f7e5a`.
Every frozen gate passed and no scientific falsifier fired.

The predecessor `P-J-CIRCULAR-QDD-DUAL-SIMPLEX-BRIDGE-1` remains
permanently `ABANDONED` on `main`. Its failed evidence custody is not an
execution leg, blind confirmation, transcript source, or scientific input to
this result.

## Claim A: integral dual-simplex bridge

In the frozen quotient basis, the primitive simultaneous intertwiner is
unique up to sign. Applying the frozen positive-first-entry sign normalization
reconstructs

```text
A=5T,
det T=-1/5,
T^T G_L T=G_Q,
G_L T in GL_4(Z).
```

Consequently, the QDD lattice is isometric to the circular metric dual, not
to the circular root lattice itself:

```text
T(O_K)=L#,
T(lambda O_K)=L,
T(lambda^2 O_K)=C_Z,
C_Z=(I+P_L)L.
```

Both adjacent indices are five and the total inclusion has Smith invariants
`(1,1,5,5)`. The saturated alternating-form quotient is integral because
`H_Z` has Smith invariants `(1,1)`.

The metric lattice `(L,G_L)` is integrally the root lattice `A4`, is even,
and has determinant five. Its dual minimum squared norm is `4/5`, and the
complete bounded census gives exactly

```text
Min(L#)={+w_x,-w_x : x in F_5},
10 vectors,
5 antipodal classes.
```

The differences `w_i-w_0` generate `L`. No integral orthogonal basis of
`L` exists: a diagonal Gram in an integral basis would have four positive
even entries and determinant divisible by 16, contradicting determinant five.

## Claim B: signed affine and projector transport

The signs and the QDD motor are load-bearing:

```text
D=M_J-I,
T D=(-P_L)T,
T rho(3,0)=(-S_L)T.
```

Removing either displayed minus sign fails for the frozen `T`. All twenty
affine maps transport exactly to

```text
H_Q=<-P_L,-S_L> ~= AGL_1(F_5),
|H_Q|=20,
-I not in H_Q.
```

The full circular group is the split central sign extension

```text
G_C=<P_L,S_L>=H_Q disjoint-union (-H_Q)
             ~= C_2 x H_Q,
|G_C|=40,
projective projector image order=20,
kernel={+I,-I}.
```

The predecessor complement `<-P_L,S_L>` is different; its intersection with
`H_Q` has order ten. The two order-five seams are also different:

```text
L/C_Z:  (P_L,S_L)=(-1, 2),
L#/L:   (P_L,S_L)=(-1,-1).
```

The five independently derived stabilizer averages transport as

```text
Pi_k=T Q_k T^(-1)=(5/4) w_k w_k^T G_L,
sum_k Pi_k=(5/4)I,
tr(Pi_i Pi_j)=1/16 for i!=j.
```

They are rank-one, idempotent and `G_L`-self-adjoint, but fractional,
pairwise nonorthogonal, and not a PVM or integral endomorphism family.

## Pending public reproduction

The sole local x86_64 leg is complete. Independent GitHub-hosted x86_64 and
aarch64 replay, exact transcript comparison, aggregate `check`, and a named
manual security review remain pending. `RUN.md` permanently records this
historical point with `architecture_gate: PENDING`; only this result file may
later close those gates with immutable receipts.

## Earned scope and firewalls

This is exact L1 algebra only. The combined marked bridge is new; the abstract
`A4` lattice, QDD simplex, affine group, forty-element circular group, and
positive form separately are not reclaimed.

The positive common form is determined only up to scale and supplies no Born
normalization. The five algebraic projectors are a nonorthogonal tight frame,
not measurement effects or an occurrence law. Nothing here establishes a
Born rule, probability, state/effect semantics, preparation, PVM/POVM,
measurement, apparatus, physical qudit, Clifford class, universality,
amplitude recombination, physical interference, space, time, action quantum,
numerical value of `h`, anyon identification, topological protection, quantum
advantage, or any L2--L6 bridge.

Public Canon, Registry, Frontier, gates, dependencies, dictionaries, and
`STATUS.md` are unchanged. Both claims remain publicly unregistered
candidate-T/L1; registration would require a separate fold.
