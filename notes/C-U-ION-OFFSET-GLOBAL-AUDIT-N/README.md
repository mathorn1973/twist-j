# Fixed unequal ion encoding through the two-contact history

**NON-CANONICAL analytical audit.** Reservation [#1362](https://github.com/mathorn1973/twist-j/issues/1362).
Public authority remains Canon v97. This note establishes consistency of one
fixed coordinate dictionary and derives its changed implementation obligations.
It does **not** establish physical realizability, earn a public scientific
status, or remove the physical HOLD in [#1359](https://github.com/mathorn1973/twist-j/pull/1359).

The result is conditional but concrete: the dictionary is consistent with
every original checkpoint if the **entire** update is conjugated. Both actual
contact slices then require a physical SWAP. The second receiver needs a
different physical preparation, selector and generator actions. The old
same-dictionary symmetry obstruction does not apply; availability of these
new physical operations remains unproved.

## 1. Inputs, method and scope

The logical input is the complete two-contact protocol in
[CONTRACT.md](../../probes/P-U-TWO-TRACE-PORT-CONTACTS-1/CONTRACT.md),
at public main `2973a432303e046aacb2cee3cea97254ea3ab8eb`:

```text
omega = (n, s1, s2, R1, R2),   Ri = (p1,p4,p1p,p4p,q,r),
si(0) = ai+1 mod5,             a1,a2 in F5,
R1(0) = R2(0) = rho = (0,0,0,0,1,0).
```

At counters 0 and 6 the addressed source exchanges with its receiver trace;
then both receivers take their actual selected native step and the shared
counter increments. The target horizon is preparation through boundary 9.
All pentit arithmetic below is modulo five. No original input label enters
the update, selector or reader outside the two prepared source registers.

The fixed unequal-dictionary identity for the second contact is already in
[#1361's PROOF.md](https://github.com/mathorn1973/twist-j/blob/9f3586dca75d0c74b021d992e4f81bf7b7f3e8de/probes/P-U-ION-LS-CONTACT-BOUNDARY-1/PROOF.md).
It is a prior scope control, not a new discovery of this note. That probe's
same-dictionary, isolated-contact exclusion remains unchanged. Its immutable
model and source manifest are [MODEL.md](https://github.com/mathorn1973/twist-j/blob/9f3586dca75d0c74b021d992e4f81bf7b7f3e8de/probes/P-U-ION-LS-CONTACT-BOUNDARY-1/MODEL.md)
and [SOURCES.md](https://github.com/mathorn1973/twist-j/blob/9f3586dca75d0c74b021d992e4f81bf7b7f3e8de/probes/P-U-ION-LS-CONTACT-BOUNDARY-1/SOURCES.md).

This is an exact algebraic derivation with static reading of previously
stored evidence, **not a new executable enumeration or formal run**. The
predecessor's [PROOF.md](../../probes/P-U-TWO-TRACE-PORT-CONTACTS-1/PROOF.md)
gives the pre-contact R2 path. Its stored
[HISTORY.csv](../../probes/P-U-TWO-TRACE-PORT-CONTACTS-1/evidence/primary/HISTORY.csv)
and [CONTACTS.csv](../../probes/P-U-TWO-TRACE-PORT-CONTACTS-1/evidence/primary/CONTACTS.csv)
are reused without rerunning or editing that probe. Their input identities are:

| Input at the main pin above | Bytes | SHA-256 |
| --- | ---: | --- |
| CONTRACT.md | 14128 | `9b9b294ff4a797212fdefedc1780bedd14161f4be5f41142a4d43939b1013891` |
| HISTORY.csv | 8586 | `0485f39381fb83c1cf30edbdf7114df2a107d0d6b7aa40e0725f83ae1d84f3d3` |
| CONTACTS.csv | 1849 | `4480ac45a70548bc01688b59d3c3516428af687a201ea04b94ecfd3fe198ddf7` |

The analytical proof covers all 25 histories and all ten boundaries; the
tables below are explicit consequences and attributed examples, not a claim
that a new program exhaustively verified 250 rows. No pulse optimizer,
experimental apparatus, calibrated error bound or new verifier is supplied.

## 2. One dictionary, fixed from preparation

Keep the fourteen data factors from #1361. Change **only** R2.q:

```text
K(n,s1,s2,R1,(P2,q2,r2)) = (n,s1,s2,R1,(P2,q2+4,r2)),
y = q2+4 = q2-1,           q2 = y+1.
```

For S2 use `iota_S(s)=|ell_s>`; for R2.q use
`iota_Q(q)=|ell_(q+4)>`. The other thirteen coordinate-to-level maps remain
the identity label map. Neither physical tensor factors nor their decoders
are exchanged after a contact. K is a fixed dictionary, not an added X^4
pulse at counter 6. The physical decoder of R2.q always returns `y+1`.

Use the same actual level set as [Hrmo et al., Fig. 1](https://www.nature.com/articles/s41467-023-37375-2/figures/1):

| Physical label j | Level ell_j in 40Ca+ | Logical q2 decoded from j |
| ---: | --- | ---: |
| 0 | 4^2 S_(1/2), m_J=-1/2 | 1 |
| 1 | 3^2 D_(5/2), m_J=-3/2 | 2 |
| 2 | 3^2 D_(5/2), m_J=-1/2 | 3 |
| 3 | 3^2 D_(5/2), m_J=-5/2 | 4 |
| 4 | 3^2 D_(5/2), m_J=+1/2 | 0 |

The label order is not energy order. The preparation becomes

```text
K omega0(a1,a2) = (0,a1+1,a2+1, (0,0,0,0,1,0), (0,0,0,0,0,0)).
```

Both receivers still decode to the same logical rho and their preparations
remain independent of a1,a2. Their physical prepared states differ: R1.q is
in ell_1 and R2.q is in ell_0. This is a paid, fixed architectural choice.
If an additional contract demanded identical physical preparations or
identical physical update programs for the two receivers, this candidate
would not meet that contract. The logical common-rho contract does not
impose either requirement.

## 3. The complete native law changes on R2

Let `P=(p1,p4,p1p,p4p)`, `kappa=sum(P)` and `zbar=kappa+y+r` in the
physical labels of R2. Its original trace is `z=zbar+1`. Therefore its
selector must be

```text
theta_n = popcount(n) mod2,
j2 = (kappa+y+r+1+2 theta_n) mod5.
```

Its generator is `gtilde_j = K2 g_j K2^-1`, with K2 acting on q only.
Direct substitution into the [Canon v97 generators](../../canon/CANON.md)
gives the full six-coordinate maps:

```text
atil(P,y,r) = (p4,p1,p4p,p1p, y, r)
btil(P,y,r) = (-p1p,-p4p,-p1,-p4, 3-y, -r)
ctil(P,y,r) = (2-p1p,1-p4p+r,2-p1,1-p4-r, 4-y, -r)
dtil(P,y,r) = (2-p1,1-p4,3-p1p,4-p4p, 4-y, 1-r)
etil(P,y,r) = (2-p1,1-p4,3-p1p,4-p4p, -y, 1-r).
```

R1 retains the original generators and selector. Both selectors evaluate
their actual post-contact states. The contact calendar and counter are
unchanged. Neither selector receives the original a1,a2 as a shortcut.

This distinction is observable immediately. At boundary 0, R2 has all
physical labels zero. The correct selector chooses btil and produces y=3.
Using the original raw-label selector would choose a and keep y=0, already
violating the boundary-1 requirement. Even keeping the correct selector but
using the old unshifted b would give the wrong q label. Relabeling only the
second contact while keeping the physical program unchanged fails.

## 4. Contacts and the actually inherited input

The original full contact is

```text
C(s,(P,q,r)) = (kappa+q+r, (P,s-kappa-r,r)).
```

K leaves the first contact unchanged. On its actual boundary-0 slice,
`kappa=r=0`, it is the physical SWAP `(s1,1) -> (1,s1)`.
Here SWAP denotes the required exchange of encoded basis labels. The
coherent SWAP unitary is one exact representative; the tuple evidence alone
does not fix coherent phases or the action on the remainder. A physical
gate contract must state whether that stronger coherent target is required.

The complete conjugated second contact is

```text
Ctil2(s,(P,y,r)) = (y+kappa+r+1, (P,s-kappa-r-1,r)).
```

This is an involution by conjugacy. It is a SWAP on the slice
`kappa+r=4`; it is not a SWAP for arbitrary spectator coordinates.

Before the second contact, the stored predecessor path maps to:

| n | Physical R2 tuple (P,y,r) | Original logical q2 |
| ---: | --- | ---: |
| 0 | (0,0,0,0,0,0) | 1 |
| 1 | (0,0,0,0,3,0) | 4 |
| 2 | (0,0,0,0,0,0) | 1 |
| 3 | (2,1,3,4,4,1) | 0 |
| 4 | (2,1,3,4,4,4) | 0 |
| 5 | (2,1,3,4,4,1) | 0 |
| 6 | (2,1,3,4,4,4) | 0 |

The selected generator indices before boundary 6 remain b,b,d,b,b,b;
R2 executes their conjugated maps. The table is independent of both
sources because R2 has not yet interacted with either. S2 is still a2+1.
At boundary 6, kappa=0 and r=4, so the physical task is exactly

```text
(s,y)=(a2+1,4) -> (4,a2+1).
```

For a2=4 it is `|0,4> -> |4,0>`. The swap-invariant `|0,0>` input of
#1361 is no longer the actual input. On the full fixed slice the target is
SWAP, which commutes with port swap, so the previous symmetry argument
does not exclude this target. It does not prove attainability either.

After this contact y=s. Since theta_6=0, the R2 native selector is
`j2=kappa+y+r+1=s`, exactly the original logical selection. The two actual
contacts therefore demand the same type of physical permutation on
different pairs, with different spectator and inherited-resource states.
This does not supply one pulse that works on both full apparatus states.

## 5. All checkpoints, the archive and the remainder

Write F for the original complete update: scheduled contact, both native
updates, source exports and counter increment. The maps just derived are
exactly

```text
Ftil = K F K^-1,       preparation_til = K preparation.
```

K is bijective and independent of time and history. Induction gives
`Ftil^n(K omega0)=K F^n(omega0)` for every original pair a1,a2 and every
boundary n=0,...,9. Thus the entire 25-history family, including boundaries
7 and 8, is transported by one law. No desired checkpoint is inserted at
6, and no decoder consults the original history label.

The readers `Ai=p_i1+p_i1p`, `Bi=p_i4+p_i4p`, `Wi=Ai^2` are unchanged
because K moves no piston. R1 is entirely outside K's support. The original
retention set `z in {1,4}` on R2 is now `zbar in {0,3}`; its conjugated
continuation preserves the same W. Reusing `{1,4}` for the new raw trace
would misidentify the protected set. The original W1 from boundary 3 and W2
from boundary 9 retain their original meanings.

For an explicit terminal check, the stored R2 endpoint classes become:

| a2 | Physical R2 at boundary 9 | W2 |
| --- | --- | ---: |
| 0,1 | (0,0,0,0,3,2) | 0 |
| 2,3 | (2,1,3,4,2,3) | 0 |
| 4 | (4,4,2,4,1,0) | 1 |

This proves a logical preservation property, not a bound on physical
archive disturbance during active fields. Addressing, spectator phases,
leakage, readout error and retention over a declared finite time still need
physical treatment.

K preserves equality of complete data states in both directions. Hence it
preserves every history fibre and in particular the fourfold merger of
`{0,1} x {0,1}` at boundary 9 established in the prior evidence. With
orthogonal input codewords, a common pure initial remainder, exact
reversible evolution and the same pure final data codeword, output
orthogonality again requires `dim H_remainder >= 4`. No sufficiency claim
for four states follows. For a coarse logical decoder, additional
distinctions may instead reside inside its physical fibres; they must
still be counted in the full state.

There is no specified physical remainder trajectory in the old logical
CSV. This note cannot invent one. A prospective apparatus must evolve one
full state `X_h(t)`, including motion, controller, work sources and history
storage, from preparation. At boundary 6 it must use its actual inherited
state, which can depend on h. K acts only on the data dictionary and
authorizes no reset, recooling, battery replacement or fresh common
ancilla there. Even if an abstract unitary dilation were conjugated by K
on its data factors, its transformed Hamiltonian would require a separate
availability proof in the chosen ion model.

## 6. Energy: the contact debt moves into the history

Let epsilon_S(j), epsilon_Q(j) be the independently determined physical
level energies of S2 and R2.q. The logical assignments are now
`E_S(s)=epsilon_S(s)` and `E_Q(q)=epsilon_Q(q+4)`. At detached endpoints
of the isolated second contact the two-port energy change is

```text
w_s^K = epsilon_S(4)+epsilon_Q(s)-epsilon_S(s)-epsilon_Q(4)
      = d_4-d_s,     d_j=epsilon_S(j)-epsilon_Q(j).
```

If d_j is constant (matched spectra up to an additive offset), all five
values vanish. The first actual SWAP has the same cancellation if its two
spectra are matched. Matching is an explicit physical condition, not a fit
to the carry table. Field gradients or differential endpoint shifts require
the unshortened expression. Zero endpoint change is not zero laser,
switching or controller work, nor proof of energy access at every time.

There is also an exact whole-history bookkeeping identity. Compare the
new and old label assignments in the **same fixed additive bare-data
Hamiltonian at detached checkpoint boundaries**, `H_data=sum_i H_i`;
all other data-coordinate contributions are unchanged. For the R2.q
spectrum define `f(q)=epsilon_Q(q+4)-epsilon_Q(q)`. Then

```text
E_data,K(h,n) - E_data,old(h,n) = f(q2(h,n)),
[Delta E_K - Delta E_old]_(n->m) = f(q2(h,m))-f(q2(h,n)).
```

These are comparisons of specified data states, not measurements of an
old or new realized device. Use epsilon_Q(0)=0 as an energy-zero convention:

| Boundary/interval | New minus old stored data energy or endpoint change |
| --- | --- |
| Prepared boundary 0 | -epsilon_Q(1) |
| Boundary 6 before contact | +epsilon_Q(4) |
| Change over 0 -> 6 | +epsilon_Q(1)+epsilon_Q(4) |
| Change over 0 -> 9, a2=0,1 | epsilon_Q(1)+epsilon_Q(3)-epsilon_Q(4) |
| Change over 0 -> 9, a2=2,3 | epsilon_Q(1)+epsilon_Q(2)-epsilon_Q(3) |
| Change over 0 -> 9, a2=4 | 2 epsilon_Q(1)-epsilon_Q(2) |

The second receiver starts with all labels in the S level; by boundary 6
its q factor is in D_(5/2),m=+1/2 and all six of its data factors are in
the selected D levels. The physical implementation of its contact-free
native evolution must actually supply those excitations before the second
contact. The preparation is lower in stored
energy than under the previous dictionary, but the 0 -> 6 rise is larger.

The start boundary matters. If accounting starts from the same physical
reference **before preparation**, the new preparation's endpoint saving
must also be included. The new-minus-old terminal data energy is then only
`f(q2(9))`: epsilon_Q(3)-epsilon_Q(4) for a2=0,1,
epsilon_Q(2)-epsilon_Q(3) for a2=2,3, and
epsilon_Q(1)-epsilon_Q(2) for a2=4. These compare D levels, not an extra
optical excitation. None of these endpoint identities is the total work
cost or a finite battery-admissibility proof. Time-dependent fields or
non-detached endpoints require their Hamiltonian contributions as well.

## 7. What remains to admit a physical candidate

[Hrmo et al.](https://www.nature.com/articles/s41467-023-37375-2)
provide the level set and a state-dependent light-shift interaction with
closed motional loops. In the effective class frozen in #1361 a completed
LS loop is diagonal on the data levels and by itself does not swap their
populations. Collective rotations can change this statement for a sequence;
no sequence realizing the required SWAP has been supplied here. Commuting
with swap is a necessary symmetry test, not a synthesis certificate.

| Obligation | Result of this audit |
| --- | --- |
| Fixed dictionary through all logical checkpoints | Exact conjugacy derived; no switch at 6 |
| Original archive meaning and source exports | Preserved by fixed pi_K, unchanged W and the conjugated law |
| Old same-dictionary contact obstruction | Does not apply to this changed target |
| Physical SWAP on both addressed pairs | Unproved in the declared compatible control model |
| Physical preparation and conjugated native updates | Explicit targets above; no implementation yet |
| Remainder, motion and work available at 6 | Inheritance required; trajectory not supplied |
| Common finite times and error bounds | Not supplied |
| Physical archive protection and finite retention | Not supplied |

Any next control problem must include the converted native law, or
explicitly remain a local contact study. A full apparatus must provide
common input-independent times t0,...,t9 with its fixed decoding
`pi_K X_h(t_n)=omega_n(h)`, a finite verification interval, and errors
defined before comparison. An isolated post-C endpoint is needed only if
it is part of that next contract; otherwise the complete enlarged step
must be compared, including both receivers and all resources.

This audit removes the **global dictionary inconsistency concern**, subject
to the stated changed preparation and law. It neither excludes this new
physical candidate nor proves it feasible. The next missing result is a
compatible physical realization or a restricted impossibility proof, not
another relabeling at the second contact. Canon v97 and the physical HOLD
are unchanged.
