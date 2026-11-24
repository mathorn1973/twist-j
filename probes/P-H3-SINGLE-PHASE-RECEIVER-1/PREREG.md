# P-H3-SINGLE-PHASE-RECEIVER-1 preregistration

**Status: FORMAL PREREGISTRATION / PROSPECTIVE / L1**

Public claim: [issue #2001](https://github.com/mathorn1973/twist-j/issues/2001)
Owner: A. M. Thorn
Branch: `probe/P-H3-SINGLE-PHASE-RECEIVER-1`
Directory: `probes/P-H3-SINGLE-PHASE-RECEIVER-1/`

## Public authority and exposure

| Field | Value |
| --- | --- |
| State | ACTIVE |
| Canon | Public Canon v113 |
| Main at claim | c089e7ec7ecc82f4838c27663d94c040f5cc4ea3 |
| Tag | canon-v113 |
| Tag object | 3a91e2bee83a3045b17f3aa2895f69deef62d89c |
| Content commit | 50d0e94d81e4954b7351bff755ed1889290bb7b8 |
| Canon SHA-256 | 47114cb616069242cff36bb499e5fe9b11266a92c744ba3f15a9085c11956b34 |
| Canon bytes | 1555510 |

The bare clock, its ready cuts, the rank-44 and rank-4 inputs and the
five-copy worker results are prior exposed work. The earlier note proposes
this geometry and gives qualitative predictions. The outcomes of the new
augmented single-copy controlled trials and uninterrupted orbit are
prospective at this pin. The [antecedent note](https://github.com/mathorn1973/twist-j/blob/46f34d449a68aa65493cdb4d401f0a853d3c85f1/notes/C-H3-RECURRENT-PHASE-WORKER-N/RESEARCH.md#next-contact-experiment)
is a non-canonical draft source. The equations, preparations and gates
below and the accepted verifier define this experiment.

## Field 1. Equation and decision

Use the public native H3 law on the even torus of width 8 and height 4,
with zero-based coordinates \(x,y\). Each site carries \(R_0,R_2,\mathrm{CLK},
\mathrm{CORR}\) in \(O=\mathbb Z[j]\), with \(j=\zeta_5\),
\(\rho=j^2\), \(J=1+\rho\), and \(h(z)=z\bar z\). Every tick at next
matching bit \(b\) applies the transport \(C_b\) followed by the collision
\(B\), then toggles \(b\). Transport pairs vertical rows starting at
\(y\equiv b\pmod 2\) on the first three rails and horizontal columns
starting at \(x\equiv b\pmod 2\) on CORR, using increasing coordinates
modulo the torus sizes. On each ordered pair it applies
\[
C(u,v)=(m+\rho e,m-\rho e),\qquad m=(u+v)/2,\quad e=(u-v)/2
\]
if \(u-v\in2O\); otherwise the pair is unchanged.

For a collision set \(d=(R_0-R_2)/2\), \(f=(\mathrm{CLK}-\mathrm{CORR})/2\).
When both differences are integral, branch 1 takes
\((d,f)\mapsto(Jd,J^{-1}f)\) if \(d\ne0\) and \(h(f)=h(J)h(d)\);
branch 2 takes \((d,f)\mapsto(J^{-1}d,Jf)\) if \(f\ne0\) and
\(h(d)=h(J)h(f)\). Both midpoints are held fixed. Test branch 1 first
and use identity when neither branch applies. The read \(B_2\), transport
\(C_0\), and reset \(B_1\) must occur in that order. A passive transfer is
a change of either matter rail at the receiver from the pre-transport cut
to the post-transport substep. The post-collision cut must retain that matter
change.

## Field 2. Code and measurement

The accepted exact standard-library program is
`probes/P-H3-SINGLE-PHASE-RECEIVER-1/verify.py`. Its verifier
uses exact integer cyclotomic arithmetic with \(1+j+j^2+j^3+j^4=0\) and
labels all ticks by their ending full-cut index. It constructs its own
bare, controlled and recurrent preparations. It reads no data from the
draft note or a working checkout of its branch. Run from the repository root
with `python3 probes/P-H3-SINGLE-PHASE-RECEIVER-1/verify.py`.
The formal invocation follows the pushed, read-back preregistration pin.
The scientific checks inspect exact state, matching bit, branch choices and
post-transport as well as post-collision values.

## Field 3. Carrier and stock

The bare rank-zero ready preparation has next bit zero. Unless written
below all rails are zero. Put \(R_0=2J,\ R_2=-2J,\ \mathrm{CLK}=1\) at
\((0,y)\) for all rows. In rows 0 and 1 put CORR triple \((-3,-3,5)\)
at columns \(0,1,2\). At \((0,2)\) and \((0,3)\) put CORR
\(J-\rho^2-2\rho J(2+\rho+\rho^2)\). Define raw ready rank \(r\) by
applying the left \((0,1)\) pair contact followed by the right \((1,2)\)
pair contact \(r\) times to the starting triple, retaining the other
preparation entries. Use all \(r=0,\ldots,84\). Identify cuts by full bare
state and next matching bit. The bare orbit from raw rank 0 has period
622, with one occurrence of each ready state over that period. Rank 44 is
the cut at tick 74. Derive each ready predecessor in the bare evolution,
including rank zero's predecessor at the end of the bare period; each
predecessor has next bit 1.

Put the head at \((1,0)\) and the passive receiver at \((1,1)\).
Use \(F=1025\), \(A=-2-j^2-5j^3\). Keep all bare CORR values intact
when augmenting a preparation. Assign the head matter midpoint zero,
half-gap \(JF\), and CLK \(A+2F\). Assign the passive matter midpoint
4, half-gap \(F\), and CLK zero. Replace only those matter and CLK
entries when loading stock. No new stock or external reset enters during
a run. Every controlled trial begins with that stock at its own bare
predecessor. The separate uninterrupted run begins with that stock on
bare raw rank zero, at tick zero with next bit zero.

## Field 4. Systematics and controls

All 85 controlled runs advance exactly two ticks, in the order \(1,0\).
Check the same-residue raw-rank-4 control separately: its head CORR at
the incoming post-transport cut differs from \(A\) by a nonzero element
of \(2O\). Require integral input half-gaps, both norm equalities
to fail, and branch zero with unchanged collision output. Observe the actual branch and rail values rather than
inferring a read from the bare phase label.

For each monitored substep compare the complete augmented state against
the corresponding bare cut or bare post-transport state plus the exact
stock in the two specified sites. Outside the two sites all four rails
must match the bare reference; at the two sites check all four rails,
including the two exact field offsets \(+\rho F\) on CLK and
\(-\rho F\) on CORR while the head is written. The head's matter
half-gap is \(F\) while written and \(JF\) when restored. Outside that
interval the two CORR entries coincide with the bare projection. At a
work substep the bit-zero vertical matter contact changes the two midpoints
while preserving their respective half-gaps. Starting \(m_H=0,m_P=4\),
the complete midpoints after \(n\) work events are
\[
m_H=2-2\rho^n,\qquad m_P=2+2\rho^n.
\]
The passive stock must not be altered before the work substep or by a
collision. Compare the full augmented state and next bit at recurrence,
including the unmodified sites and all stock coordinates.

Check the exact matter sum, radiation sum, total Hermitian account
\(\mathcal H=\sum h(z)\) over all rails, and the positive scalar account
\(Q=\operatorname{Tr}_{\mathbb Q(j)/\mathbb Q}(\mathcal H)/2=18907703\).
In the ordered basis \(1,j,j^2,j^3\) the initial account tuples are
\[
Q_m=(8,0,0,0),\qquad Q_r=(2066,6,7,5),\qquad
\mathcal H=(10498377,0,2089051,2089051).
\]
Compare the complete ring-valued accounts with these values at
every transport and collision, for every controlled trial and the entire
recurrent trajectory. Check that applying the collision inverse recovers
the exact post-transport state with branches 1 and 2 exchanged, then
applying inverse transport (replace \(\rho\) by \(\rho^{-1}\) on admitted
pairs) recovers the exact incoming state and matching bit.

## Field 5. Failure thresholds

The controlled predicate passes exactly when the only passive matter
transfer over the 85 two-tick trials is at raw rank 44 on tick two.
At rank 44 the head must take branch 2 on tick one, the passive transfer
must occur at the following bit-zero transport with the head still
written, and the head must take branch 1 in the collision of tick two.
The passive change must survive that collision and the carrier disturbance
must clear. No other trial may write the head or change the passive matter
at either monitored substep. The rank-4 norm refusal and all full-state,
inverse and account checks are mandatory.

The uninterrupted predicate passes exactly when the native orbit from
its single prepared start has all its passive transfers at ending ticks
\(75+622k\), \(k=0,1,2,3,4\), across 3110 ticks. Require the corresponding
reads on the previous ticks, resets on the transfer ticks, no other
head writes or passive changes, the exact state/substep/account checks
above, no earlier full return, and return of the complete augmented
state and next bit at tick 3110. A successful controlled predicate does
not substitute for this uninterrupted predicate, and vice versa.

There is zero tolerance for missing, additional or mistimed events, a
wrong-phase write, a projection difference outside the specified head
defect, stock discrepancies, inverse failures or account discrepancies.
Report a deterministic JSON record with PASS or FALSIFIED for each gate
and complete normally on a well-formed scientific counterexample, with no
threshold adjustment, carrier substitution, or suppressed failure. A
program or fixture error that prevents a well-formed execution is an
operational failure. Keep scientific failures in the formal public result.

## Field 6. Action layer L1

This tests a finite phase predicate in the specified native H3 state
space with the declared initial stock. A passing result certifies one
controlled material write and its recurrence at the stated cuts within
this model. It provides no 85-label fixed-latency material register,
autonomous stock preparation, or physical interpretation.
