# Mathematical review of P-NATIVE-RECEIVER-CARRY-MIRROR-1

Status: NON-CANONICAL / L1. This is a review record, not a Canon fold.

Target: PR #1884 at head c9bd0bc5ac97ad034be399e6619695c7fc2c4a61. The
reviewed text is PROOF.md at pin aaf3ec7e925c2c0261604179ee4166d542233e14,
SHA-256 13998852f685c474e0ec775ac2e4cd41f102c2c93412ee2ef0a77beeece28fd5.
The authority used for comparison is Public Canon v108, `canon/CANON.md`,
SHA-256 c2c4a1ef4ad8859b4b9e9e92022bdd3528c641a3e426df66dc4ade640a5b862a.

**Exposure.** The results were known before this review. The reviewer had
read the target verifier and compiled audit before writing this text; see
PREREG.md. The derivations below were done by hand from PROOF.md and the
Canon, and none of them relies on output from the target code. A separate
code-independent checker (review.py, see RESULT.md) re-derives the same
facts from scratch.

## Verdict

No mathematical error was found. Every algebraic statement in sections 1
to 7 is correct as stated, within its declared domain and port. The
finite-realization statements in section 8 follow once the compiled word is
audited, and PROOF.md says so explicitly.

Recommended disposition, for each declared v109 scope:

| Scope | Content | Verdict |
| --- | --- | --- |
| 1 | First-tick receiver transfer and its unique affine port | Accept |
| 2 | Marked integral carry pairing and the reversible four-register circuit | Accept with editorial corrections E1 and E2 |
| 3 | Fixed-input multiplier discrimination at the next carry precision | Accept, with clarification E3 recommended |
| 4 | Finite 62-cell, 500-input compiled realization | Accept as finite evidence (candidate-C), with notes E4 and E5 |

None of the corrections changes a conclusion. They make dependencies and
conventions explicit, and a Canon text built from this probe should
include them.

Items E6 to E9 were added after the independent execution; see the
Addendum at the end. The verdicts above are unchanged by them. For
scope 3, E8 is a required wording restriction, not an optional
clarification.

## Section-by-section check

### 1. Native law, admitted family and first-tick rows

**The generators match the Canon.** PROOF.md writes x=(A,B,C,D,q,r), while
the Canon (lines 610-614) writes x=(p1,p4,p1p,p4p,q,r). The identification
A=p1, B=p4, C=p1p, D=p4p carries all five generators a..e over exactly. The
selector g_(z+2 theta_n) with theta_n=s_2(n) mod 2 is the Canon definition
in section 2.

**The first-tick rows are correct.** At counter 0, theta=0. On the ready
state (A,B,C,D,0,1), z=kappa+1=s, so g_s fires. Substituting q=0, r=1:

- a gives (q,r)=(0,1);
- b gives (-0,-1)=(0,4);
- c gives (1-q,-r)=(1,4);
- d gives (1-q,1-r)=(1,0);
- e gives (2-q,1-r)=(2,0).

The five pairs are distinct. h=q+r+2 returns 3,1,2,3,4 for s=0..4, so h=s
holds exactly on s!=0.

**The affine port is unique.** The three admitted rows (0,4), (1,4) and
(1,0) are affinely independent: their difference vectors (1,0) and (0,-4)
form a basis of F5^2. So at most one affine map takes them to 1,2,3, and the
derivation in PROOF.md finds alpha=1, beta=1, gamma=2. The fourth row,
(2,0), gives 4 as required.

**The q-reader is correct.** q=0 occurs only for s=1, q=2 only for s=4, and
q=1 for both s=2 and s=3. chi(2)=chi(3)=-1 and chi(1)=chi(4)=1, so q alone
determines chi(s) on the admitted family. R_q is that function. It is well
defined and is the stated contract.

The count of 125 per sheet is correct. On the s=0 control sheet the native
state stays at (0,1), and the port sends it to 3.

### 2. Cyclotomic digits

**The unit identities are correct.** (1+j^2)(-j-j^2) = -(j+j^2+j^3+j^4) = 1.
Expanding with j=1-l (l=lambda) gives J=2-2l+l^2 and J^-1=-2+3l-l^2.
The minimal polynomial of lambda is l^4-5l^3+10l^2-10l+5, so N(lambda)=5
and lambda is totally ramified. 5 = prod_(k=1..4)(1-j^k) with each factor
equal to lambda times a unit, so 5 is in (l^4) and 5/l is in (l^3).

**The digit representation is unique.** O/(l^2) has 25 elements and
characteristic 5. The representation lo+hi*l with lo,hi in F5 is a bijection
onto it. The argument in PROOF.md is complete because (l) intersected with
Z is 5Z.

**The quotient maps are correct.** Modulo l^2, J acts as 2-2l, so
J(lo+hi l) = 2lo + (2hi-2lo)l, which is F(lo,hi)=(2lo,3lo+2hi).
Likewise J^-1 acts as -2+3l, which gives I(lo,hi)=(3lo,3lo+3hi). Composing
them in either order gives (lo, 15lo+6hi) = (lo,hi).

### 3. The four-register circuit

Direct substitution gives L(q,r,h,k)=(q,r,b+3k,3b+2h) with b=q+r+2.
Applying L twice: the high register becomes b+3(3b+2h)=10b+6h=h, and the
archive becomes 3b+2(b+3k)=5b+6k=k. So L^2=id on all 625 states, and no
blank auxiliaries are needed. With h=k=0 the intermediates are as stated,
and I(2b,3b)=(6b,15b)=(b,0) is the full-word control.

**E1 (editorial). State the order of the conjugation.** PROOF.md says that
"L is the conjugate of the h/k swap by the composition of the shear and F".
Put M=F∘S, so the shear is applied first. Then L = M^-1 ∘ SWAP ∘ M, which
is the true statement. The other reading, M ∘ SWAP ∘ M^-1, gives the
different map (q,r,4q+2k,3q+3h). PROOF.md promises to state the
composition convention wherever it matters, and here it matters. The
involution itself is proved independently by substitution, so nothing else
is affected.

### 4. Integral carries and marked pairing

All claims hold, and for a more general reason than the text uses. Let
epsilon be any unit with l-expansion e0+e1 l+e2 l^2+e3 l^3. Let b be any
integer and a any integer with a = e0 b (mod 5). Then e0 b - a = 5m, and

    C = (epsilon b - a)/l = 5m/l + e1 b + e2 b l + e3 b l^2,

so C is in O and C = e1 b + e2 b l (mod l^2), because 5m/l is in (l^3).
Applying the inverse unit to the actual output a gives

    C_mirror = (epsilon^-1 a - b)/l = -epsilon^-1 C.

This is exact and does not depend on the section. The residue of
-epsilon^-1 is -1/e0. For J, e0=2, e1=-2 and e2=1, which gives
v=res C=-2b=3b and w=res C_mirror=(-1/2)(3b)=b. These are the values in
PROOF.md, and they agree with the register values of section 3.

The same-input control is the expansion above with epsilon=J^-1
(e0=-2, e1=3). Its first residue is 3b, equal to the forward residue. This
is the collision that section 6 then resolves.

The omitted offset sends the mark to s-2 on every admitted sheet. Comparing
signs only, chi(s-2)=chi(s) holds only for s=1 (chi(4)=chi(1)). That is
125 preparations.

**E2a (dependency to state). The sign reversal rests on (2/5)=-1.**
Since chi(-1)=1 in F5,

    chi(res C_mirror) = chi(-1/e0) * chi(res C) = chi(e0) * chi(res C).

So the paired carry characters are opposite if and only if J mod lambda=2
is a quadratic non-residue. The opposite character is a property of this
particular unit, not of marked inverse pairing in general: a unit whose
residue is a square would give equal paired characters. The second native
observation in section 5 gives chi(2b)=-chi(b), which is the same fact.
Sections 4 and 5 are therefore not two independent sign confirmations;
both are the single Legendre-symbol fact (2/5)=-1. The proof's direct
computations are correct; this dependency should be named.

**E2b (convention). Separate the convention-free content from the reader
convention.** The carry-sign reader -chi(res C) carries a fixed global minus
sign. The q-reader R_q is defined on three values so that it equals chi(s).
The word "opposite" is invariant under the global sign. But "agrees with
the native receiver sign" in section 4, and "this second forward native
observation agrees with the paired carry sign" in section 5, hold only
because of the chosen convention. The results were exposed before the
formalization (PROVENANCE.md), so under the reading-family discipline of
POLICY.md these agreements should be recorded as definitional. The
convention-free content is:

    chi(v) = -chi(b),   chi(w) = chi(b),   chi(a) = -chi(b),   for b != 0.

This content is what should be canonized.

### 5. The second native device

With fixed pistons (-1,0,0,0) (equivalently (4,0,0,0)) and receiver (0,1),
the SUM of a gives trace (a-1)+0+0+0+0+1=a, so g_a fires. The resulting q
is 0,1,1,2 for a=1,2,3,4, so R_q gives chi(a). On the admitted domain a=2b
is nonzero and chi(a)=-chi(b), which is E2a again. The remark that F applied
twice gives 4b=-b is correct. The scope disclaimers are accurate: the
section supplies an extra receiver, a write and an origin, and it is not a
native inverse.

### 6. Fixed-input discrimination

Using the general expansion from section 4:

- J has v=e1 b=3b and u=e2 b=b, so the slope is 2;
- J^-1 has v=3b and u=-b, so the slope is -1/3=3.

These match the table. The integer part 5m/l lies in (l^3), so neither the
choice of section nor the lift of v affects u. The latter holds for any lift,
not only the two specified ones, because two lifts differ by 5n and 5n/l is
in (l^3). For b=0 both carries are 0. The minimality claim is correctly
restricted to ideal-power precisions of this observation: modulo l the
residues coincide (both e1=3), and modulo l^2 the slopes 2 and 3 are
disjoint whenever v!=0.

**E3 (clarification, recommended).** The slope u/v equals e2/e1, a property
of the first two nonconstant l-coefficients of the multiplier. Any two
multipliers with e1 != 0 (mod 5) and different e2/e1 are separated by this
reader. The reader identifies multiplier labels; it does not recognize
inversion as such. The fact that the slopes of J and J^-1 differ is a
computed property of this pair. PROOF.md does not claim more, and the Canon
wording should keep that precision. "Observing u requires the product modulo
l^3 or the integral carry" is correct, since C mod l^2 needs epsilon*b
mod l^3.

### 7. Rank obstruction at the trace port

Summing the components gives these traces:

| Generator | Sum of components | Trace |
| --- | --- | --- |
| a | permutes the coordinates | z |
| b | -z | -z |
| c | 7-z | 2-z |
| d | 12-z | 2-z |
| e | 13-z | 3-z |

The trace after any tick is therefore a function of the trace before it,
for all 5^6 states and not only the ready family. This closure is the step
that makes "a common continuation applies a function to the trace"
legitimate.

The clock maps are tau_0=(0,4,0,4,4) and tau_1=(2,1,1,3,1). Each has
image size 2 on {1,2,3,4}, and later function applications cannot enlarge
an image. So no nonempty common binary word realizes the four-valued map
s -> 2s at that port. The scope limitation is accurate: the full receiver
distinguishes all five sheets, as section 1 shows.

### 8. Finite compiled realization

These statements are conditional on the exhaustive audit of the actual
expanded word, which PROOF.md requires and does not presume. Given that
audit, the composition argument is sound. The integrated schedule
interleaves only secondary-machine operations and a read of the low cell
between the four-register steps. Those operations touch none of cells
0..50 or the primary machine. So the four-register endpoint of section 3
and the secondary endpoint of section 5 compose with no extra assumption.
The swap gadget (k+=h; h-=k; k+=h; h*=-1) exchanges arbitrary values. The
count 80705 = 2*40348 + 9 matches the nine routing primitives: two for the
shear, one SUM, four for the swap and two for the inverse shear.

**E4 (note for the Canon wording). The inverse is the literal reverse of the
forward word.** The compiled "inverse multiplier" is the forward word
reversed, with each primitive inverted. It is not a separately compiled
J^-1 circuit. Since F^-1=I and the work cells are clean, the reversed word
computes I on all 25 inputs. The executed mirror is therefore literally:
compute, move the carry into the archive, uncompute with a blank high
digit. That is L = M^-1 ∘ SWAP ∘ M from E1. This is correct and is
disclosed in section 8, but a Canon statement should say it plainly, so
that "inverse multiplier" is not read as an independent device.

**E5 (provenance). Two declared sources sit on unmerged PRs.** The
compiler and the carry comparison source are the heads of open PRs #1819
and #1821. A byte-identical copy of the compiler is vendored in the probe
directory and bound by its SHA-256. The finite counts (40348 primitives and
the six-primitive inventory) are properties of that exact revision. A Canon
fold should cite the hash-bound copy inside the probe directory, not those
PRs, and it should not be read as accepting #1819 or #1821.

### 9. Scope

The negative scope statements are accurate and complete. In particular:

- the interconnection, archive allocation, second origin and schedule are
  all supplied;
- there is no native inverse, physical time direction, Hermitian-time
  identification, pulse execution, archive regeneration or L1-to-L4 bridge;
- the result is separate from the contact-bank carrier of PR #1879.

The 500 executions form four boundary classes of 125. They are not 500
independent predictions, and PROOF.md says so.

## Status recommendation

Sections 1 to 7 are proofs by direct substitution and elementary
cyclotomic arithmetic. This review finds them correct and complete at their
stated scope, which supports the candidate-T label after the editorial
corrections E1 and E2. Section 8 is finite evidence and stays candidate-C.
It is backed by the target's two-architecture replay, see CI-AUDIT.md, and
by the independent execution in RESULT.md.

The final acceptance decision and any Canon or registry change belong to
the Canon owner and to a separate reviewed fold. This review does not raise
any status.

## Addendum after the independent execution

The checker writer worked in a separate context. It did not see this text,
the target verifier or any outputs. It reported the reading points below,
and this reviewer has checked each one against PROOF.md. None of them is a
mathematical error. Each is a precision that a Canon wording should adopt.
E8 was found by this reviewer while checking those points.

**E6 (section 4). Both ingredients are needed.** PROOF.md says
`v=res C=3b` follows "either from the exact polynomial for J or from
5/lambda in (lambda^3)". Neither fact suffices alone. The value 3b comes
from the l-coefficient e1=-2 of J. That the integer rounding term
(2b-a)/l vanishes modulo l needs 5/l in (l). The general expansion in
section 4 above uses both. Replace "either ... or" with "and".

**E7 (section 7). Name trace closure as the premise.** The sentence "a
deterministic continuation common to all inputs cannot increase the image
cardinality" holds because every native step is trace-closed: the next
trace is tau_t of the current trace, over all 5^6 states. It would fail for
a continuation that reads the full state, which section 7 itself excludes.
State the closure as the operative premise. The review checker confirms it
on all 5^6 states and both bits (31250 evaluations), not only on the ready
family that the target verifier enumerates.

**E8 (section 6). The depth-two result is for carry-only readers.** Fix b
and take a blank high digit. The two-digit device stores
`(a,v)=(2b,3b)` for J and `(3b,3b)` for J^-1. The reader `v/a` therefore
gives 4 for J and 1 for J^-1 for every nonzero b. That separates the
multipliers already at depth one, from the device's own stored digits,
without b.

PROOF.md excludes the output letter from the reader's arguments in
section 6, so its minimality statement is correct as written. But its
sentence that the two-digit circuit "does not also supply u" can be misread
as saying the device cannot distinguish the multipliers. A Canon statement
of scope 3 must therefore keep the restriction explicit: next-precision
discrimination is minimal among readers of the carry alone. Readers that
also see the output letter, or the input letter, discriminate in F5.

Relatedly, "observing u requires the product modulo l^3" is true under that
carry-only contract. The text argues sufficiency, and necessity holds only
within that contract.

**E9 (minor wording).**
- Section 1, "the first row then gives gamma=2": this means the first
  admitted row (s=1). The table's first row is s=0, which would give 4.
- Section 3, "Only the admitted preparations set h=k=0": in the
  integrated carrier every preparation, including the s=0 controls, starts
  with blank high and archive. The marked contract is stated only for the
  admitted family. The review checker ran the 125 controls as well. As the
  closed L predicts, they give mark 3, high 3 and archive 4, with the
  checkpoint restored.
- Section 8, "the secondary receiver must give the opposite sign": this
  means opposite to the primary native sign chi(s), and equal to the paired
  carry sign under the convention of E2b.
- Section 4, omitted offset: on the s=2 sheet q+r=0, so the reader
  returns no sign (chi=0) rather than a wrong sign. The count of 125
  sign-only agreements is unaffected.
