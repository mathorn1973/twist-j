# W2 proof audit

[NON-CANONICAL] Analytic support for the single owner session
`CODEX-W2-INDEPENDENT-20261002`, dated 2026-10-02. Action layer L1 only.
This document changes no frozen file and promotes no candidate or registered
row. `C-OCCURRENCE-CYCLE-COUNT-N` remains
`STOP_APPLICABILITY / H_NOT_TESTED`.

[EXPOSURE] The handoff, promotion proposal rev2, recorded results, base
preregistration and Addendum 1 were read. The generator formulas were read
from the local Canon text at lines 580 to 584. No original package Python
program was opened or used. No computation was executed for this analytic
support. The new derivations below are exposed to the stated conclusions;
they do not claim blindness, empirical confirmation or a separate claim.

## S3: a hand derivation from the shear

[PASS: ANALYTIC, NON-CANONICAL] The stated four multiplier families, their
dimensions and their ranks follow directly from the generator formulas.

Write the following linear coordinates on the piston block over `F_5`:

```text
K = p1 + p4 + p1p + p4p = kappa
A = p1 - p4 + p1p - p4p
B = p1 + p4 - p1p - p4p
C = p1 - p4 - p1p + p4p
Q = q
R = r
```

The piston change of basis has determinant of magnitude 16 and is invertible
over `F_5`. Capital letters below denote coordinates, while `dK`, for
example, denotes the associated covector. Removing affine constants gives:

| Linear map | K | A | B | C | Q | R |
| --- | --- | --- | --- | --- | --- | --- |
| `L_a` | K | -A | B | -C | Q | R |
| `L_b` | -K | -A | B | C | -Q | -R |
| `L_c` | -K | -A | B+2R | C-2R | -Q | -R |

All three maps are involutions. Thus a nonzero common multiplier form
satisfying `L_g^* omega = m_g omega` has `m_g` in `{1,-1}`.

Let `T = L_c L_b`. It fixes all coordinates except

```text
B -> B - 2R
C -> C + 2R.
```

It has order five. Its multiplier is `m_b m_c`; applying its fifth power
shows `(m_b m_c)^5 = 1`. Since the multiplier is a sign and the characteristic
is five, this forces `m_b = m_c`. Hence `omega` is invariant under `T`.
Conjugating by `L_a` also leaves `omega` invariant and changes the shear to

```text
B -> B - 2R
C -> C - 2R.
```

The two shear vectors `(-2,2)` and `(-2,-2)` in the `(B,C)` plane are
independent: their determinant is `8`, nonzero in `F_5`. The shears commute,
and their powers therefore generate both elementary shears
`x -> x + R(x)e_B` and `x -> x + R(x)e_C`.

For any such shear `S_w = I + w tensor dR`, with `dR(w)=0`, expansion gives

```text
S_w^* omega - omega = dR wedge i_w omega,
```

where `(i_w omega)(y)=omega(w,y)`. Invariance is equivalent to
`i_w omega` being a multiple of `dR`. Taking `w=e_B,e_C` shows that every
coefficient involving `dB` or `dC` vanishes except those of
`dB wedge dR` and `dC wedge dR`. Conversely this condition makes both
shears preserve the form.

Consequently the remaining space consists of the six alternating forms on
`span{dK,dA,dQ,dR}`, together with `dB wedge dR` and `dC wedge dR`.
The diagonal actions of `a` and `b` now give the complete answer:

| `(m_a,m_b,m_c)` | Space of forms | Dimension |
| --- | --- | --- |
| `(1,1,1)` | `wedge^2 span{dK,dQ,dR}` | 3 |
| `(-1,1,1)` | `dA wedge span{dK,dQ,dR}` | 3 |
| `(1,-1,-1)` | `span{dB wedge dR}` | 1 |
| `(-1,-1,-1)` | `span{dC wedge dR}` | 1 |

There are no other nonzero solutions. The first family is an alternating
form supported on three independent covectors, so a nonzero member has
rank two. The other three families consist of explicitly decomposable
nonzero two-forms and also have rank two. This gives radical dimension
four in every case. The number of distinct nonzero forms in the four
families is `2(5^3-1)+2(5-1)=256`.

For the strict family, contraction against all three forms
`dK wedge dQ`, `dK wedge dR`, `dQ wedge dR` vanishes exactly when
`K=Q=R=0`. Its common radical has dimension three. Since `d,e` have linear
part `-I`, they preserve every alternating form and add no restriction.
Thus the S3 exclusion holds for the stated invariant affine realization.
It makes no assertion about another realization or enlarged carrier.

## Base section 7: proof audit

[PASS: ANALYTIC, NON-CANONICAL] A3's involution, Hermiticity, trace,
orthogonality, reflection-conjugation and sum calculations are consistent
with the declared phase convention. In the conjugation calculation the
exponent is
`2b(4a-2q-2j)+2r(q-2a+j) = 2(2b-r)(2a-q-j)`, as printed.
The Weyl-conjugation identities stated in A3 also follow by substituting
the specified `D_(q,r)`; the scalar Weyl phase cancels under conjugation.

[PASS: ANALYTIC, NON-CANONICAL] A4's multiplier lemma is valid. The hand
derivation above supplies the remaining classification without reliance
on a finite linear-algebra census.

[PASS: CONDITIONAL ON REGISTERED INPUT] A5(iv) substitutes the registered
synchronization formula correctly: `z_n=4+2 theta_(n-1)` gives selectors
`4,1,1,3` for clock pairs `00,01,10,11`, respectively. This review does not
re-prove the registered synchronization theorem. The deduction remains a
statement about its origin-zero synchronized regime.

[PASS: ANALYTIC, NON-CANONICAL] The B1 trace formula follows from
orthogonality of the phase-point operators. The line projectors have a
direct additional proof: a vertical line `q=q0` gives `|q0><q0|`; a line
`r=mq+b` gives

```text
<k|Pi_L|j> = (1/5) zeta^((m/2)(k^2-j^2)+b(k-j)),
```

where `1/2` means the inverse of two in `F_5`. This is the outer product of
the normalized vector with entries
`zeta^((m/2)j^2+bj)/sqrt(5)`. Hence every line operator is a rank-one
projector directly, without needing to extrapolate a numerical audit.

[PASS: ANALYTIC, NON-CANONICAL] B2's line-inversion argument is valid for
real signed functions as well as nonnegative ones. Every point distinct
from `u` occurs on exactly one of the six lines through `u`, which gives
the printed inverse and proves uniqueness on the fixed 25-point carrier.

[PASS: ANALYTIC, NON-CANONICAL] B3's proof is valid for every odd integer
`d>=3`, including composite dimensions. Multiplication by two permutes
`Z/dZ`, so summing `c(2q)` is legitimate. The Fourier transform on this
cyclic group is invertible even when `d` is composite. Nonzero Fourier
amplitudes cannot all acquire zero squares in the complex field. With real
amplitudes the convolution is real, and its nonzero, zero-sum row has
negative mass. Parseval and Cauchy-Schwarz yield the displayed lower bound.
The final use of the inequality between the one-norm and the two-norm is
valid, though it need not be sharp. Dimension one has no nonzero sum-zero
state and should be excluded when displaying the bound's denominator.
Complex amplitudes would invalidate the real-convolution step; they are
explicitly outside this claim.

[PASS: ANALYTIC, NON-CANONICAL] B5 follows from
`<l,v_tilde>=-s/sqrt(20)` and `||v_tilde||^2=Q-s^2/5`.
For a nonzero real four-vector this denominator is positive: projecting
`(0,v)` to the constant-vector complement can vanish only when all five
entries were equal, which forces `v=0`. The overlap identity with Wigner
functions follows from the orthogonal operator basis. The QDD
interpretation still requires the declared reading premise.

## Addendum section 4: proof audit

[PASS: ANALYTIC, NON-CANONICAL] B7.1 correctly reconstructs the total
`T=sum xi` from any complete parallel class, then obtains
`xi(u)=(sum_(L through u) s(L)-T)/5`. The algebra also works for complex
operator-valued data reduced by trace. For an effect, Hermiticity makes
the response real; a binary stochastic reader exists precisely when this
unique response and its complement lie in `[0,1]`.

[PASS: ANALYTIC, NON-CANONICAL] The B7.3 control follows directly from
`sum_(j=1)^4 zeta^j=-1`: `<l,f>=1/2`, with squared magnitude `1/4`.
The explicit line-vector formula above identifies `f` as the line
`r=1`. B7.5 is correct because the constant vector is the line state
`r=0`, whose response is the indicator of that line.

[PASS: ANALYTIC, NON-CANONICAL] B8.1 is the standard rank-one sandwich
identity. B8.2 and B8.3 follow because, conditionally on any incoming
point and observed line, adding an independent uniform `t delta`
makes the outgoing point uniform on that line. Independent coordinates
at successive readings multiply the conditional counts. Statements
about a conditional state or a history require that the conditioning
event have positive count; zero-probability histories have no conditional
state. This qualification does not change any joint probability.

[PASS: ANALYTIC, NON-CANONICAL] B8.5 is correct. With U0 the third reading
in the first direction sees the identical point and must repeat the first
outcome. With U1, two distinct directions make every overlap `1/5`, so
the probability of repeating the first outcome after the intervening
reading is `1/5`, including when the initial preparation is itself in
one of the measured directions.

## S8: continuation lower bound and its boundary

[PASS: ANALYTIC UNDER POINT-KERNEL HYPOTHESES] Fix a direction `delta`.
Let an update be a kernel `K_delta(u,v)` on the same 25 points, independent
of the preparation, earlier history and the choice of the next direction.
Suppose its conditional state after every positive first outcome gives
the line-state probabilities for every next line reading. B2 then forces
that conditional state to be uniform on the observed line `M`.

For any point `u` on `M`, choose an admitted preparation line transversal
to `M` and passing through `u`. Conditional on outcome `M`, the incoming
point is exactly `u`. Therefore the corresponding row of the update is
forced to be

```text
K_delta(u,v) = 1/5  if v lies on M,
K_delta(u,v) = 0    otherwise.
```

This argument applies to every `u` and every direction, so it allows no
exceptional cheaper point. If `u` has `k(u)` positive, equally counted
continuations, the number ending at each of the five points of `M` is
`k(u)/5`. Thus `k(u)` is a positive multiple of five, and `k(u)>=5` for
each point individually. Variable continuation counts cannot reduce
any average below five under these hypotheses. A representation with
five continuations realizes the bound. A larger equal-count
representation has a uniform five-valued output-coordinate marginal.

[SCOPE QUALIFICATION] The words "each reading consumes" need the
continuation-ready, preparation-independent point-kernel interpretation
just stated. They are not a lower bound on all descriptions that reproduce
only a terminal outcome history. In particular, omitting `t2` after the
second outcome leaves the two-round outcome law in B8.2 unchanged, while
generally failing the final-state requirement B8.3 and future readings.

[SCOPE QUALIFICATION] History-aware control also permits identity updates
on repeated contexts. If the incoming conditional distribution is already
uniform on a line in the measured direction, reading it and leaving the
point fixed retains the required distribution without fresh randomness.
An apparatus using the previous direction to choose between this operation
and U1 is outside a single fixed point-only kernel `K_delta`. Thus a
universal fresh-coordinate lower bound for history-aware or
preparation-aware apparatus is not established here. The frozen class
and the stated exclusions should be retained when quoting S8.

[NO FALSIFIER FOUND IN THE BOUNDED CLAIM] These observations do not
contradict U1, the counted two-round and three-round laws, or the
point-kernel lower bound. They identify assumptions required for the
resource wording. B8.4's printed falsifier about transversal intersection
only checks its geometric premise; it does not independently test every
possible generalization of the resource conclusion.

## Disposition

[PASS: ANALYTIC AUDIT, NON-CANONICAL] No error was found in the audited
algebraic proofs at their stated finite-carrier scope. S3 now has an
explicit hand derivation in this local work item. S8 has a direct proof
against variable equal-count continuations for a preparation-independent,
continuation-ready point kernel, with its boundary recorded above.

[NOT AUDITED HERE] This document does not run or independently certify the
finite LOW/HIGH tables, the census hashes, architecture identity, native
event renewal, or the unresolved sharp negativity bound. Those are
separate from this bounded proof review. No status promotion or public
landing follows from this document.
