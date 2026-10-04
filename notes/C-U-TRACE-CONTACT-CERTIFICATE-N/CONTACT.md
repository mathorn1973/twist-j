# Trace contact: energy criterion and realization boundary

NON-CANONICAL L1 proof note, 4 October 2026. Prospective reservation:
[C-U-TRACE-CONTACT-CERTIFICATE-N, #1356](https://github.com/mathorn1973/twist-j/issues/1356).
The deductions below are symbolic; no new scientific program was executed.
They do not supply a physical realization certificate or close #1349.

## 1. The exact contact and its endpoint energy

Write the receiver as \(\psi=(P,q,r)\in\mathbb F_5^6\), with four piston
coordinates \(P\), \(\kappa=\sum P\), and \(z=\kappa+q+r\). The admitted contact is

\[
C(s,(P,q,r))=(z,(P,s-\kappa-r,r)).
\]

State arithmetic is in \(\mathbb F_5\). Energies below are ordinary real
numbers. This map fixes \(P,r\) and exchanges \(s,z\); it is an involution
on the entire product \(\mathbb F_5\times\mathbb F_5^6\).

Suppose independently specified disconnected endpoint energies have the form
\(H(s,\psi)=e(s)+E_R(P,q,r)\), with no additional participant taking energy
between those endpoints. Then \(C\) conserves \(H\) on its entire domain if
and only if

\[
\boxed{E_R(P,q,r)=e(\kappa+q+r)+K(P,r)}
\]

for some real function \(K\).

**Proof.** In the invertible chart \((P,z,r)\), conservation reads
\[
e(s)+\widetilde E_R(P,z,r)
=e(z)+\widetilde E_R(P,s,r)
\]
for every \(s,z,P,r\). Thus \(\widetilde E_R(P,z,r)-e(z)\) is independent
of \(z\), which is exactly the displayed form. Conversely substitution
proves conservation. This uses every state of the stated product domain;
agreement only on prepared contacts is a different, weaker condition.

The theorem tests a previously justified energy. Defining that energy from
the boxed formula would produce a compatible mathematical account, without
establishing its physical meaning. The theorem also does not account for
interaction energy or switching work during a pulse. Those require a full
dynamical model even when the endpoint test passes.

## 2. A sharper boundary for a separate q spectrum

Suppose the receiver endpoint energy separates its raw \(q\) coordinate:
\[
E_R(P,q,r)=G(P,r)+f(q).
\]
The function \(G\) may couple its five spectator coordinates arbitrarily.
Then full-domain conservation of \(C\) holds **if and only if both \(e\)
and \(f\) are constant**. In particular, the result applies to a sum of
seven separate coordinate energies; energies of \(P,r\) remain unrestricted.

**Proof.** Set \(h=\kappa+r\). For every fixed \(P,r\), conservation gives
\[
e(s)+f(q)=e(q+h)+f(s-h)
\]
for all \(s,q\). Hence \(f(q)-e(q+h)=K_h\), independent of \(q\).
Every \(h\in\mathbb F_5\) occurs. Summing over the five values of \(q\)
gives \(5K_h=\sum_q f(q)-\sum_q e(q)\), so \(K_h\) does not depend on
\(h\). Comparing two shifts forces \(e\) constant; the same identity then
forces \(f\) constant. The converse follows because \(C\) fixes \(P,r\).

This is an obstruction in a precise endpoint-energy class, not a prohibition
of all realizations. A nonseparable receiver energy, an explicit work store,
another encoding, or a restricted preparation domain changes the hypotheses.

For a concrete test, take independently fixed equal-gap spectra
\(e(s)=\Delta\operatorname{rep}(s)\), \(f(q)=\Delta\operatorname{rep}(q)\),
where \(\Delta>0\) and \(\operatorname{rep}\) takes values \(0,1,2,3,4\).
The actual second ready receiver in #1355 is
\((2,1,3,4,0,4)\). Thus \(\kappa=0\), \(z=4\), and the contact sends
\((s,q)\) to \((4,s+1)\). Its endpoint energy change is
\[
\frac{\Delta_C}{\Delta}
=4+\operatorname{rep}(s+1)-\operatorname{rep}(s)
=\begin{cases}5,&s=0,1,2,3,\\0,&s=4.\end{cases}
\]
This failure therefore occurs even on the five actually admitted second
contact inputs. The first ready receiver \((0,0,0,0,1,0)\) has
\(\kappa+r=0\); that contact is an equal-spectrum \(s,q\) exchange and
has zero endpoint cost. No physical spectrum is selected by this example.

## 3. A conditional implementation using pair operations

Let \(F\) fix \(s,P,r\) and replace \(q\) by \(q+\kappa+r\). Then, with
rightmost operation first,
\[
\boxed{C=F^{-1}\operatorname{SWAP}_{s,q}F.}
\]
Indeed the successive \((s,q)\) pairs are
\((s,z)\), \((z,s)\), and \((z,s-\kappa-r)\).

The map \(F\) is five pair additions into \(q\), one from each coordinate
of \(P\) and one from \(r\). Its inverse is five pair subtractions. A swap
can be implemented chronologically by
\[
q\mathrel{+}=s;\quad s\mathrel{-}=q;\quad
q\mathrel{+}=s;\quad s\leftarrow-s,
\]
always using current values. Consequently the full contact has an exact
all-state circuit with **13 signed pair additions and one local negation**,
without another data register. This is a sufficient count, not a minimum.
Here a signed pair addition means SUM or its inverse as one admitted logical
operation. If only positive SUM is available, each inverse requires four
applications over \(\mathbb F_5\): this particular sequence then uses
31 positive SUM applications and one local negation.
The required pair connectivity is a star centered on \(q\), with edges to
\(s,r\) and the four piston coordinates. No trace-reading primitive is
needed in this circuit description.

There is a pre-existing conditional library in
[QDD-AFFINE-CONTROL-REALIZATION](https://github.com/mathorn1973/twist-j/blob/5e872c22a18043c8126945a982efad55472cea82/canon/CANON.md#L6681).
For five-level registers with \(N|j\rangle=j|j\rangle\), it admits local
Fourier controls and pair Hamiltonians
\(H_{ij}=-\hbar gN_iN_j\), \(g>0\). A positive pulse of duration
\(2\pi k/(5g)\), conjugated by the stated target Fourier transforms,
implements \(|x,y\rangle\mapsto|x,y+kx\rangle\) exactly for
\(k=1,2,3,4\), including subtraction at \(k=4\).

Using this library for the circuit above requires admitting it on seven
distinguishable registers and the six stated edges. The earlier theorem
does not independently supply that hardware. Its
[explicit limitation](https://github.com/mathorn1973/twist-j/blob/5e872c22a18043c8126945a982efad55472cea82/canon/CANON.md#L6732)
leaves local pulse durations, switching, control fields and work sources as
additional resources, and supplies neither native material energy nor
compatibility with native tick slots. Its assumptions also require known
drift and phases to be compensated. The present compilation inherits these
debts. Logical pair support is not a proof of spatial locality; a logical
signed addition is not one physical pulse or one native tick.

## 4. A conditional battery account

The existing
[INTEGER-ENERGY-FUNDED-INVOLUTION](https://github.com/mathorn1973/twist-j/blob/5e872c22a18043c8126945a982efad55472cea82/canon/CANON.md#L7237)
applies directly after an endpoint energy \(H_0\) and a unit
\(\varepsilon>0\) are independently fixed. Assume
\(d(x)=(H_0(Cx)-H_0(x))/\varepsilon\) is integer on the declared domain.
For a stored resource \(b\in\mathbb N_0\), define
\[
\widehat C(x,b)=
\begin{cases}(Cx,b-d(x)),&b-d(x)\ge0,\\
(x,b),&b-d(x)<0.
\end{cases}
\]
Since \(d(Cx)=-d(x)\), every accepted transition reverses, and rejected
states are fixed. Thus \(\widehat C\) is an involution preserving
\(H_0(x)+\varepsilon b\). On the finite contact domain, a fixed initial
\(b_0\ge\max_x\max(0,d(x))\) accepts every first contact. The battery's
actual, generally input-dependent final state remains part of the output.

This construction assumes the contact and the work store; it does not
derive either. It inherits locality only if \(C\), \(d\), and the battery
access already have the claimed local support. A budget for one contact
does not prove a budget for a whole native trajectory or for the
intermediate gates of a pulse implementation. Those steps need their own
energy and domain accounting. Adding a battery changes the complete carrier
of #1355 and must be stated as a further extension.

## 5. What a complete realization certificate must contain

The next candidate must specify the following before treating agreement
with \(C\) as physical realization.

1. **Carrier and preparation.** Actual distinguishable states, the encoding
   of all seven coordinates, the physical positions and allowed interaction
   graph, and source-independent preparation of receivers and auxiliaries.
   A coordinate change does not establish an accessible trace port.
2. **Independent energy.** Bare and interaction energies, energy unit,
   spectral or classical-state meaning, and a reason for those choices
   independent of the target transition. Include all work stores and
   switching contributions, with admissibility on the full claimed domain.
3. **Available interactions.** The precise elementary laws and their
   domains, addressed supports, pulse durations, drift and phase treatment,
   and a derivation of \(C\) using only those laws. Algebraic invertibility
   does not itself make an inverse pulse available.
4. **Clock and controller.** The physical controller, program, address and
   phase states; their preparations and complete outputs; and the relation
   between physical time and native counter checkpoints. A nonzero-duration
   circuit cannot simply be inserted before a native tick while assuming
   that \(U\) or its counter waits. A pause, compensation, or simultaneous
   evolution must be explicitly modeled and proved compatible with the
   desired enlarged transition and its subsequent \(011\) write window.
5. **Complete outputs and archive.** Retain the exported old trace in the
   source port and every changed battery, controller, helper and environment
   state. Prove that later operations preserve earlier fixed readings
   \(W_i=(p_{1,i}+p'_{1,i})^2\). The receiver coordinates need not stand
   still; the protected obligation is their reading. Address isolation must
   follow from the physical interaction law as well as the logical schedule.
6. **The native continuation.** Justify the physical implementation or
   effective reduction used for the subsequent native steps. #1355 exhibits
   complete-state collisions for its declared mathematical machine. If a
   proposed larger physical dynamics is reversible, the missing distinction
   must survive in its included environment; then those larger complete
   states do not collide. A dissipative implementation likewise needs its
   environmental energy and information account. Reversibility of \(C\)
   alone establishes neither conclusion about the entire apparatus.

Return of helpers or of a controller to their initial state is an additional
claim requiring proof. Source consumption remains admitted here. None of
these conditions silently substitutes the source-preserving SUM contract
of #1349 for the contact being studied.

## 6. Existing ownership and current conclusion

The construction examined is #1355 at
`2bd0b048d5e01d7d5bf260dbada338e4089b04b8`; its full-trace contact, complete
state and physical limitations are explicit in its contract. The Canon
references above are pinned to baseline
`5e872c22a18043c8126945a982efad55472cea82`, Public Canon v97.

- [#993 completed result](https://github.com/mathorn1973/twist-j/issues/993#issuecomment-5655461040)
  owns the synchronized-factor preparation boundary; it supplies no physical
  preparation or reset mechanism.
- [#994 completed result](https://github.com/mathorn1973/twist-j/issues/994#issuecomment-5655607857)
  derives piston-slot exchange within one native checkpoint. It neither
  supplies spatial carriers nor implements the external scalar/trace contact.
- [#996](https://github.com/mathorn1973/twist-j/issues/996) already studies
  added exchange, arming and read ports, with their physical justification
  and spatial meaning explicitly unprovided. Its historical computational
  status is unchanged and no old program is used here.
- [#998 completed result](https://github.com/mathorn1973/twist-j/issues/998#issuecomment-5662316457)
  distinguishes transported readers from actuators and proves its own scoped
  native exclusion. It is not a universal prohibition of the present \(C\).
- [#1349 native contract](https://github.com/mathorn1973/twist-j/blob/5e872c22a18043c8126945a982efad55472cea82/notes/C-OMEGA24-PAIR-CONTACT-N/NATIVE-CONTRACT.md)
  retains the independent carrier, energy, interaction, control and timing
  obligations for its different source-preserving task.

The inspected sources supply no completed physical certificate for this
contact. The present result is the exact endpoint-energy criterion, its
separate-q-spectrum obstruction, a concrete second-contact work witness,
and a conditional pair-operation route. Missing carrier, energy, control or
timing evidence leaves realization **NOT PROVIDED**; it does not prove a
universal impossibility. No reset, indefinite renewal, physical energy
selection, Canon promotion or closure of #1349 is claimed.
