# Same-cut phase information and a single-copy contact test

**NON-CANONICAL, result-exposed exploration.** Time indices below refer to
complete native cuts. Tick zero is the phase-zero preparation with matching
bit zero.

## The middle radiation coordinate

An exact inspection of one lap of the four-row carrier gives 11, 85 and 45
distinct CORR values on the 85 ready cuts at source columns 0, 1 and 2,
respectively. The same counts hold after transport on the first outgoing
tick, before collision. Thus the middle CORR already gives an injective
radiation label at a fixed site and cut.

In the translated worker, the clean port-0 source middle CORR equals the
bare carrier's middle CORR at each ready cut. At the two ordinary alias
cuts, raw ranks 15 and 19, port 1 and port 4 respectively already have a
written head. Their CORR is the bare value minus \(F\rho\). The actual
dressed middle CORR of each of these ports remains injective in the checked
lap. On the bare recurrent snapshot set, the middle values occupy 15
residue classes modulo \(2O\), with 21 ready values in the largest
class. This limits a parity-only snapshot observer of that coordinate.
A trajectory initialized with reset stock requires its own check.

The local matter output from a collision with phase-independent incoming
matter has at most three values. The matter center is fixed, and the
half-difference \(d\) becomes \(d,\ Jd,\) or \(J^{-1}d\). Distinct incoming
radiation values that give the same branch produce identical matter
outputs. This rules out a one-site, one-collision conversion of all 85
labels with blank matter, even at an injective radiation coordinate.

## A prepared spatial upper bound

In the translated recurrent worker, the source at \((1,5)\) has matter
half-difference \(F\) at exactly one matching-bit-zero cut in each carrier
lap, at \(t=212\bmod622\). The other bit-zero cuts have half-difference
\(JF\) there. The marker is the ordinary port-1 head write and clears
without passive work. Replay over all 3110 ticks also found that columns 5
and 6 stay zero on every rail and row, including after transport.

For \(m=0,\ldots,310\), seed tile \(m\) with the translated worker's
complete state at tick \(2m\). Put the tiles side by side in a single
torus of width 2488 and height 20, ordering each tile's original columns
as \(6,7,0,1,2,3,4,5\). This even shift preserves the alternating
matching. Only CORR travels horizontally. The sole replaced edge per tile
is the \(5\)-to-\(6\) seam, whose zero endpoints make the native composite
update equal the separate tile updates by induction.

At a common complete bit-zero cut \(t\), exactly one tile has sensor
half-difference \(F\). Its index satisfies \(t+2m=212\bmod622\).
The other 310 sensors have half-difference \(JF\). Thus the same-cut
matter word distinguishes all 311 bit-zero cuts of the primary tile
within a carrier lap, including the 85 ready cuts. The tile ordering
uses uniform offsets, and the code measures no elapsed time. The total
scalar account is \(311\cdot188996320=58777855520\). This is a finite
implication of the marker and seam checks. The preparation supplies the
relative offsets. A coupled, single-copy encoder, an autonomous source
of the offsets and a single cell holding the integer phase are open.

## Next contact experiment

On a bare ready cut, an exact comparison at the middle site can use
\(d=JF\) and \({\rm CLK}=A+2F\). With admitted input \(a\), the field
half-difference is \(F+(A-a)/2\). If \(F\) exceeds the trace of
\(h((A-a)/2)\) on the admitted finite set, the branch-2 norm test forces
\(a=A\). Choose \(F\) large enough to exclude branch 1 in the real
embedding with \(h(J)>5/2\). An isolated contact can test equality
between exact values in the same residue class.

The obvious outgoing-read geometry fails a stronger requirement. At
all 85 ready starts, after the first bit-zero transport the middle
source CORR has the same residue as the third CORR. The following
bit-one right contact therefore admits in the bare carrier. If a
middle head writes \(-F\rho\) into CORR with odd \(F\), that right
contact wrongly refuses. With even nonzero \(F\), the contact admits
and transfers a nonzero part of the perturbation into column 2.
Restoring the head at column 1 cannot erase that change by itself.

For a candidate with clearance on the next horizontal edge, arm the
head on the incoming bit-one matching and place its passive partner on
the bit-zero vertical matching. Raw rank 44 is one candidate. Its
ready cut is tick 74, and the incoming middle value \(A\) has
coordinates \((-2,0,-1,-5)\) in \(1,j,j^2,j^3\). The bare post-transport
middle equals \(A\) only on the two steps ending at ticks 74 and 75.
The bit-zero left contact leading to tick 75 refuses before and after
a subtraction of \(F\rho\) for odd \(F\). Raw rank 4 gives a distinct
ready middle value in the same residue class.

In the four-row carrier, put one reader at column 1, row 0 and one
passive pair at column 1, row 1, leaving all CORR values unchanged
in the preparation. Use \(F=1025\) and the same auxiliary stock on every trial.
The bare carrier's Hermitian account bounds both \(A\) and \(a\) by
19 in either complex embedding, so the trace of \(h((A-a)/2)\) is
less than 722 where the half-difference is admitted.
Give the reader matter center zero, half-difference \(JF\) and CLK
\(A+2F\). Give the passive pair center 4, half-difference \(F\)
and CLK zero. For the 85 controlled trials apply these stocks at the
bare predecessor of each ready cut. Test for a passive write at a
common latency of two ticks from that predecessor, only for rank 44.
A separate recurrent run from one initialization would test whether
the transfer also occurs at the intended ready neighborhood without
a supplied start.

For the target, the head must write during the incoming bit-one step,
then admit the passive contact on the next bit-zero transport and
restore in the following collision. The same-residue control and
all other inputs must leave the passive matter unchanged at the
specified latency. Verify the complete carrier projection, exact
accounts and inverse, and trace any writes outside the tested ready
neighborhood. A missing target write, a wrong-phase passive change,
or an uncancelled carrier disturbance falsifies this geometry. The
geometry and test criteria are proposals. The augmented circuit has
yet to be run.

This first experiment tests extraction of one phase predicate from
one carrier. The full single-copy register would require a fixed
output region with 85 distinct matter values at a common native
latency, and a local release condition if it is to mark readiness
autonomously. Distinctness of an internal radiation coordinate alone
does not imply either result. The finite computations address the
specified H3 lattice dynamics. They supply no empirical test of a
material device or of a physical phase observable outside this
model.
