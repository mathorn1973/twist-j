# Result: exact inversion and the modulo-five capacity obstruction

PUBLIC / NON-CANONICAL. No authority. Action layer: L1 only.
Author: A. M. Thorn. Issue: #1281.
Status: candidate-T written derivations; candidate-C finite census and audit.
Disposition: PASS at the frozen scope. Mathematical falsifiers fired: none.

The prospective pin is 821090bc4daa55bb9974e3ec5a8e6af4d391a07a.
Both scripts were frozen and publicly read back before their first execution.
Neither script nor the proof/preregistration was changed after execution.

## 1. A working exact inverse [candidate-T]

For every nonzero alpha in Z[zeta_5] with N(alpha)<=941, the reader

$$
 D_{25}(\alpha)=\bigl(S(\alpha),S(J\alpha),\alpha\bmod25O\bigr),
 \qquad S(\alpha)=\tfrac12\operatorname{Tr}(\alpha\overline\alpha),
$$

has the direct integer inverse in decoder.py. It also rejects data outside
its exact image. The proof covers the complete infinite norm-bounded domain,
not just the finite tested shifts. It uses the unique J strip and the
proved normalized coefficient bound [-8,8]^4. The two traces are unbounded
integers and refer to a stipulated pure J step.

The sufficient general separation criterion is m^4>16X. At this scope,
25^4=390625>15056=16*941. This is not a smallest-modulus theorem.

## 2. Complete observed-orbit census [candidate-C]

Both methods returned the same entire 3150-element strip, bound by one digest,
and the same census line byte for byte:

| Quantity at norm at most 941 | Exact count |
|---|---:|
| Complete oriented J-strip B_941 | 3150 |
| B_940, public control | 3110 |
| Distinct two-trace pairs | 145 |
| Distinct two-trace plus mod5 keys | 2603 |
| Distinct two-trace plus mod25 keys | 3150 |
| Mod5 collision classes | 493 |
| Largest mod5 collision class | 10 |
| Shortfall against 3125 labels at mod5 | 522 |

The universal observed-orbit capacity proof is in PROOF.md section 7:
K_m(X)=|D_m(B_X)| is exactly the largest number of labels that the observed
reader can distinguish globally across all sheets n>=3. Changing the J
representative assigned to a label cannot repair a collision, because the
corresponding half-orbits meet at sufficiently large times in observed data.

Thus, at this fixed norm bound and in this fixed reader class, NO choice of
codebook makes mod5 suffice for 3125 labels. Mod25 does suffice. Among the
family of full residues modulo 5^r, the least successful depth is r=2.
This last endpoint conclusion consumes the finite census and remains
candidate-C until its own formal evidence and independent review are complete.
It says nothing about other readers, partial residue refinements, a different
norm budget or a physical selection of a codebook.

## 3. First collision and an explicit arithmetic witness

The complete census first collides at norm 55 [candidate-C minimality]:

$$
 \alpha=\zeta+\zeta^2-2\zeta^3,\qquad
 \beta=\zeta+\zeta^2+3\zeta^3.
$$

Direct multiplication supplies the witness independently of the census
[candidate-T identity]:

$$
 \alpha\overline\alpha=\beta\overline\beta=7+\varphi,\quad
 N(\alpha)=N(\beta)=55,\quad (S_0,S_1)=(15,20),
$$
$$
 \beta-\alpha=5\zeta^3,\qquad
 \alpha\equiv\beta\pmod{5O},\qquad
 \alpha\not\equiv\beta\pmod{25O}.
$$

The code reconstructs respectively (0,1,1,-2) and (0,1,1,3) from their mod25
readings. Further pure J traces cannot distinguish their magnitudes: the
entire trace stream follows S(n+2)=3S(n+1)-S(n) from the same initial pair.
The older norm-625 witness (5,5*zeta) is also preserved.

## 4. Execution and limits [candidate-C]

The primary audit examined all 83521 coefficient vectors in [-8,8]^4 and
completed 103950 exact inverse round trips (every strip element and k=-16
through 16), plus 40 stress cases at k in {-1024,-257,257,1024}. Twelve
invalid readings were rejected, both half-open boundaries were checked, and
one affine-step control was rejected. A valid-to-valid corruption control
explicitly prevents claiming general error correction.

The second implementation examined all 130321 coefficient vectors in
[-9,9]^4, used cyclic polynomial multiplication instead of decoder.py,
completed 15750 independent-code lookup round trips, and checked 645
mod5-collision pair differences. It returned the identical complete strip
and observed-key census. The largest observed coefficient was 7; the written
uniform bound 8 is deliberately NOT retuned to the census.

Both executions used one x86_64 architecture and one author. They are
method-separated verification, not blind two-agent confirmation or a formal
two-architecture scientific gate. RUN.md, VERIFY.txt and BREAK.txt retain
exact commands, bytes and hashes. Repository CI does not execute notes
scripts as registered scientific probes.

No existing Canon status, scope or open owner is changed. No physical
apparatus, Born occurrence, preparation, native-source completeness, SI
scale, photon/P1 or RH result is claimed.
