# Native controlled occupied writer: analytic proof draft

**NON-CANONICAL. Analytical candidate only.** Prepared on 2026-10-29 against
mathorn1973/twist-j main a193e389fb1ddb0bdc89165b015c95a17eb1e425,
Public Canon v106. This draft does not change any public status. No new
scientific verifier has been executed in preparing this proof.

The claim is a finite, one-shot, controlled routing theorem for the
unchanged native update. It does not assert a physical apparatus,
quantum gate, universal computation, reusable writing, a new clock,
an energy law, or a solution of the problem of time.

## 1. Native law and admitted resources

All coordinates and arithmetic below are in \(\mathbf F_5\). Write

\[
x=(p_1,p_4,p'_1,p'_4,q,r),\qquad
z(x)=p_1+p_4+p'_1+p'_4+q+r.
\]

The native generators, in selector-index order, are

\[
\begin{aligned}
a(x)&=(p_4,p_1,p'_4,p'_1,q,r),\\
b(x)&=(-p'_1,-p'_4,-p_1,-p_4,-q,-r),\\
c(x)&=(2-p'_1,1-p'_4+r,2-p_1,1-p_4-r,1-q,-r),\\
d(x)&=(2-p_1,1-p_4,3-p'_1,4-p'_4,1-q,1-r),\\
e(x)&=(2-p_1,1-p_4,3-p'_1,4-p'_4,2-q,1-r).
\end{aligned}
\]

To distinguish the generator \(c\) from the logical control, the latter
is denoted \(\chi\in\{0,1\}\) in this proof. Put

\[
\theta_n=s_2(n)\bmod2,\qquad
F_t(x)=g_{z(x)+2t\bmod5}(x),\qquad
U(n,x)=(n+1,F_{\theta_n}(x)).
\]

The three input blocks are the fixed original coordinates

\[
S=(p_1,p'_1),\qquad M=(p_4,p'_4),\qquad C_{\rm ref}=(q,r).
\]

For independent \(\lambda,\mu\in\mathbf F_5\) and
\(\chi\in\{0,1\}\), prepare at the common native counter zero

\[
\boxed{
x_{\lambda,\mu,\chi}(0)
 =(\lambda,\mu,4-\lambda,1-\mu,\chi,0).
}
\tag{1}
\]

This is a 50-point product preparation:
\(S=(\lambda,4-\lambda)\) depends only on the new source label;
\(M=(\mu,1-\mu)\) depends only on the independently variable old memory
label; and \(C_{\rm ref}=(\chi,0)\) depends only on the control.
The receiver \((M,C_{\rm ref})\) contains no initial \(\lambda\).
The old memory is occupied, including the legitimate label zero.

The resources are one native head, its six \(\mathbf F_5\) coordinates,
the existing counter, the specified initial preparation, and the two
fixed readout functions defined below. Both readouts use the shared
native \(q,r\) coordinates, but neither uses the other piston pair.
There is no added state register, intervention during the evolution,
selected later stopping time, saved input, historical buffer, clock
value supplied to either reader, or new native interaction.
Producing the preparation or physically implementing a readout is not
derived here.

### Why the preparation uses the offsets four and one

Consider first the chosen product-code class

\[
(\lambda,\mu,s-\lambda,-s-\mu,\chi,0),
\qquad s\in\mathbf F_5.
\tag{1a}
\]

Its source and memory sums are \(s,-s\), so their total is zero and
the raw \(q=\chi\) is exactly the initial selector trace. The actual
write prefix gives source and memory sums \(1-s,s+3\). If we impose
the additional design criterion that these two output sums be equal,
then

\[
1-s=s+3\quad\Longleftrightarrow\quad s=4.
\]

This selects the offsets \(4,1\) within (1a). It makes the write-tail
trace reconstructible as either \(2A+q+r\) or \(2B+q+r\), and the
resulting nonzero squared sums distinguish the write and hold tails.
Equality of those output sums is a chosen simplicity criterion.
Neither this criterion nor this preparation class is a physical
uniqueness principle derived from the native law.

## 2. Actual selector prefixes

The initial piston sum is \(4+1=0\), so the initial trace is exactly
\(\chi\). The native driver starts with \(011\).

For \(\chi=0\), the actual generator word is \(a,c,e\):

| Counter | Complete checkpoint | Trace | Next actual generator |
| --- | --- | ---: | --- |
| \(0\) | \((\lambda,\mu,4-\lambda,1-\mu,0,0)\) | \(0\) | \(a\) |
| \(1\) | \((\mu,\lambda,1-\mu,4-\lambda,0,0)\) | \(0\) | \(c\) |
| \(2\) | \((1+\mu,2+\lambda,2-\mu,1-\lambda,1,0)\) | \(2\) | \(e\) |
| \(3\) | \((1-\mu,4-\lambda,1+\mu,3+\lambda,1,1)\) | \(1\) | \(b\) |

For \(\chi=1\), the actual generator word is \(b,b,d\):

| Counter | Complete checkpoint | Trace | Next actual generator |
| --- | --- | ---: | --- |
| \(0\) | \((\lambda,\mu,4-\lambda,1-\mu,1,0)\) | \(1\) | \(b\) |
| \(1\) | \((1+\lambda,\mu-1,-\lambda,-\mu,4,0)\) | \(4\) | \(b\) |
| \(2\) | \((\lambda,\mu,4-\lambda,1-\mu,1,0)\) | \(1\) | \(d\) |
| \(3\) | \((2-\lambda,1-\mu,4+\lambda,3+\mu,0,1)\) | \(1\) | \(b\) |

Every row follows by substituting the preceding checkpoint into its
actual selected generator. Neither word depends on \(\lambda,\mu\).
The equality of checkpoints at counters zero and two in the hold
branch is not a reset of the autonomous state, whose counter advances.

The source-dependent raw difference is literally routed by the first
native \(a\) in the write branch. In the hold branch the first \(b\)
acts separately inside the source and memory pairs.

## 3. Stable-tail identities

Introduce

\[
A=p_1+p'_1,\quad B=p_4+p'_4,\quad
C=p_1-p'_1-2,\quad D=p_4-p'_4-1.
\tag{2}
\]

Here \(C\) is a scalar chart coordinate, distinct from the reference pair
\(C_{\rm ref}\). On the stable union \(z\in\{1,4\}\), the selector table is

| Trace | Driver bit | Selected generator | Next trace |
| --- | --- | --- | --- |
| \(1\) | \(0\) | \(b\) | \(4\) |
| \(1\) | \(1\) | \(d\) | \(1\) |
| \(4\) | \(0\) | \(e\) | \(4\) |
| \(4\) | \(1\) | \(b\) | \(1\) |

In these cases,

\[
\begin{array}{c|ccccc}
&A'&B'&C'&D'&z'\\ \hline
b&-A&-B&C&D&-z\\
d\text{ or }e&-A&-B&-C&-D&z .
\end{array}
\tag{3}
\]

Consequently

\[
A^2,\quad B^2,\quad I_S=AzC,\quad I_M=BzD
\tag{4}
\]

are invariant under every subsequent selected step. The ratio \(A/B\)
is also invariant when \(B\ne0\). The following conclusions therefore
hold for every future binary word after the displayed prefix; no
control over that future word is assumed or supplied.

At counter three the write and hold branches have

| Branch | \(A\) | \(B\) | \(I_S\) | \(I_M\) |
| --- | ---: | ---: | --- | --- |
| \(\chi=0\), write | \(2\) | \(2\) | \(\mu+1\) | \(\lambda\) |
| \(\chi=1\), hold | \(1\) | \(4\) | \(1-2\lambda\) | \(3+2\mu\) |

Thus the write tail has \(A=B\) and \(A^2=B^2=4\), whereas the hold
tail has \(A=-B\) and \(A^2=B^2=1\). These two branches are disjoint.

## 4. Fixed local readers and their complete chronology

The semantic outputs are BLANK and PRESENT(\(k\)), \(k\in\mathbf F_5\).
BLANK is distinct from PRESENT(0). BLANK below is a pending/unavailable
readout label; it does not mean that the raw memory is empty.

### Receiver reader

Given only \((u,v,q,r)=(p_4,p'_4,q,r)\), compute

\[
B=u+v,\qquad D=u-v-1.
\]

Define a total function on all \(5^4\) inputs:

1. If \(B^2=4\), set \(\widehat z=2B+q+r\). If
   \(\widehat z\in\{1,4\}\), return
   PRESENT(\(B\widehat zD\)); otherwise return BLANK.
2. If \(B^2=1\), set \(\widehat z=q+r\). If
   \(\widehat z\in\{1,4\}\), return
   PRESENT(\(1+3B\widehat zD\)); otherwise return BLANK.
3. In every other case return BLANK.

On the write tail \(A=B\), so \(\widehat z=2B+q+r=z\);
the value is \(I_M=\lambda\). On the hold tail \(A=-B\), so
\(\widehat z=q+r=z\), and
\(1+3I_M=1+3(3+2\mu)=\mu\).

### Source reader

Given only \((s,t,q,r)=(p_1,p'_1,q,r)\), compute

\[
A=s+t,\qquad C=s-t-2.
\]

Define a total function on all \(5^4\) inputs:

1. If \(A^2=4\), set \(\widehat z_S=2A+q+r\). If
   \(\widehat z_S\in\{1,4\}\), return
   PRESENT(\(A\widehat z_SC-1\)); otherwise return BLANK.
2. If \(A^2=1\), set \(\widehat z_S=q+r\). If
   \(\widehat z_S\in\{1,4\}\), return
   PRESENT(\(3+2A\widehat z_SC\)); otherwise return BLANK.
3. In every other case return BLANK.

On the write tail this gives \(I_S-1=\mu\). On the hold tail it gives
\(3+2I_S=3+2(1-2\lambda)=\lambda\).

### Earlier times

For the write branch, the pairs \((A,B)\) at counters \(0,1,2,3\)
are respectively

\[
(4,1),\quad(1,4),\quad(3,3),\quad(2,2).
\]

Both readers' reconstructed traces are respectively \(0,0,2,1\).
Thus both return BLANK through counter two and the claimed permanent
values from counter three onward.

The hold preparation already lies in the closed hold tail:
\(A=4=-B\), \(B=1\), and \(z=1\). Directly at counter zero,

\[
I_S=3\lambda+1,\qquad I_M=2\mu-2,
\]

so the source reader gives \(\lambda\) and the receiver reader gives
\(\mu\). Identity (3) preserves these values forever.

The complete proved chronology is therefore

| Control | Source reader | Receiver reader |
| --- | --- | --- |
| Write, \(0\le n<3\) | BLANK | BLANK |
| Write, \(n\ge3\) | PRESENT(\(\mu\)) | PRESENT(\(\lambda\)) |
| Hold, every \(n\ge0\) | PRESENT(\(\lambda\)) | PRESENT(\(\mu\)) |

Both readers are stationary functions of their named current ports.
Neither receives the counter, the preparation labels, the other piston
pair, or a selected time at which to report.

### Retained control

On a ready receiver, \(B^2=4\) marks write and \(B^2=1\) marks hold.
Equivalently the retained logical control is

\[
\chi=3(B^2+1).
\tag{5}
\]

The same formula with \(A^2\) holds at the source. This is a control
record after completion, not a claim that the initial control coordinate
\(q\) is unchanged. In fact at counter three \(q=1\) for write and
\(q=0\) for hold, and it subsequently evolves. A total completion-aware
controller reader returns PENDING when the receiver test above fails,
and otherwise the branch value in (5). It returns PENDING through the
write prefix, write from counter three onward, and hold at every time
in the hold branch.

After completion the original triple \((\lambda,\mu,\chi)\) is recovered
by reading both ports and \(\chi\), then undoing the declared logical
swap when \(\chi=0\).

## 5. Complete 1000-point closed tail

The retained carrier can be described without referring to a selected
trajectory. It is the union of

\[
\begin{aligned}
\mathcal T_0&=\{x:z\in\{1,4\},\ A=B,\ A^2=4\},\\
\mathcal T_1&=\{x:z\in\{1,4\},\ A=-B,\ A^2=1\}.
\end{aligned}
\tag{6}
\]

All other coordinates are unrestricted subject to these equalities.
There are 500 points in each branch, hence 1000 in the union. A more
explicit bijective parametrization uses the 50 input triples and 20
context values

\[
(\lambda,\mu,\chi;\varepsilon,z,r),\qquad
\varepsilon\in\{1,4\},\quad z\in\{1,4\},\quad r\in\mathbf F_5.
\]

For write, set

\[
A=B=2\varepsilon,\quad I_S=\mu+1,\quad I_M=\lambda.
\]

For hold, set

\[
A=\varepsilon,\quad B=-\varepsilon,\quad
I_S=1-2\lambda,\quad I_M=3+2\mu.
\]

In either case put

\[
\begin{aligned}
C&=I_S/(Az),&D&=I_M/(Bz),&q&=z-A-B-r,\\
p_1&=3(A+C+2),&p'_1&=3(A-C-2),\\
p_4&=3(B+D+1),&p'_4&=3(B-D-1).
\end{aligned}
\tag{7}
\]

All divisions are valid because \(A,B,z\) are nonzero.
The actual counter-three checkpoints are obtained with
\(\varepsilon=1,z=1,r=1\).

For injectivity, a checkpoint determines its branch by \(A^2\) or
\(B^2\), its two labels by the displayed readers, and its
\(\varepsilon,z,r\) by the chart. Conversely (7) reconstructs every
point of (6). This proves exactly 50 distinct logical outputs, with
20 current context states per output.

Closure follows directly from (3). Both branches retain their defining
relation and squares. The quantities \(I_S,I_M\) and all three logical
labels stay fixed, while

\[
\varepsilon'=-\varepsilon,\qquad
(z',r')=
\begin{cases}
(-z,-r),&b,\\
(z,1-r),&d\text{ or }e.
\end{cases}
\tag{8}
\]

This count is a complete closed-tail parametrization. The proof does
not require a new assertion that every context is visited by a given
actual trajectory. The existing native recurrent-sign-fibre theorem
could supply that separate visitation statement: here \(A\ne0\), so
each fixed logical triple has the corresponding 20-point sign fibre.
No new recurrence computation is claimed.

Closure on this union does not assert global bijectivity of the
state-selected native map. The 50 actually prepared states remain
distinct at every time: within a branch their selected generator word
is common and consists of invertible generators, and after completion
the fixed readers recover every triple. At counters zero, one and two,
the two branches have different traces, respectively \(0\) versus \(1\),
\(0\) versus \(4\), and \(2\) versus \(1\).

## 6. Exact counterfactual response at the raw ports

Define mathematical translations on the original piston pairs by

\[
\begin{aligned}
P_{S,\delta}(p_1,p_4,p'_1,p'_4,q,r)
 &=(p_1+\delta,p_4,p'_1-\delta,p'_4,q,r),\\
P_{M,\delta}(p_1,p_4,p'_1,p'_4,q,r)
 &=(p_1,p_4+\delta,p'_1,p'_4-\delta,q,r).
\end{aligned}
\tag{9}
\]

On the admitted initial preparations these simply vary
\(\lambda\mapsto\lambda+\delta\) or
\(\mu\mapsto\mu+\delta\). They preserve the trace and control and hence
the actual selector prefix. Let \(E_3\) denote three actual native
ticks from origin zero, with the counter omitted from its checkpoint
output. Subtracting the explicit counter-three formulas proves, for
every \(\lambda,\mu,\delta\in\mathbf F_5\),

\[
\begin{array}{c|cc}
&E_3P_{S,\delta}&E_3P_{M,\delta}\\ \hline
\chi=0&
P_{M,-\delta}E_3&
P_{S,-\delta}E_3\\
\chi=1&
P_{S,-\delta}E_3&
P_{M,-\delta}E_3 .
\end{array}
\tag{10}
\]

Thus the whole process routes a source-supported perturbation into
the other piston pair exactly on the write branch. It similarly
routes an independently varied old-memory perturbation into the
source pair. The hold branch keeps each perturbation in its original
pair. In all cases the output raw orientation is reversed.

These are exact identities for changes between admitted preparations,
with fixed coordinate support and a common counter. They do not
postulate that an experimentalist can apply either output translation
as a physical gate. In particular the right side of (10) describes
the observed difference between endpoints, not an extra operation
inserted after the native evolution.

The identities constrain all 50 product inputs and all five shifts,
rather than fitting a single trajectory with a time-dependent decoder.
Their physical interpretation still requires an identification of
the prepared coordinates and observed ports with an apparatus.

## 7. Native paired-port returns and the limit of composition

For the already canonical paired translation

\[
T_\delta(p;q,r)=(p;q-\delta,r+\delta),
\]

the piston coordinates and \(q+r\) are unchanged. Both fixed readers,
their readiness tests, and the retained control are therefore
unchanged by every \(T_\delta\), including on the closed tail.

The existing native whole-sheet return-window theorem supplies actual
four-tick windows equal to \(T_{+2}\) or \(T_{-2}\) on the occupied
sheet in its specified clock contexts. Composing such an actual
window with this completed writer preserves both retained labels
and the control while producing the canonical raw port displacement.
This is preservation of an already written record during a return
window. It is not a new record of the occurrence of that window,
an arbitrary launch/reset resource, or a controlled pulse into a
separate native head.

The one-shot routing is not reusable under the unchanged tail.
After the write, \(A/B=1\), while the initial and hold preparation has
\(A/B=4\). The stable native law preserves this ratio. It also never
fires \(a\) on the stable union. A second independently chosen write
would therefore require an additional preparation, reset, changed
context or coupling not supplied here.

## 8. Novelty boundary and canonical dependencies

The prior native occupied transfer is already present in
COMMON-HISTORY-FUNDED-AREA-RECEIVER: its raw preparation
\(({\rm new},{\rm old},-{\rm new},-{\rm old},0,0)\) follows the native
prefix into a checkpoint carrying both labels. U-NATIVE-SOURCE-
RECEIVER-RECORD also already establishes the special one-message,
common-ready transfer and permanent receiver-only reading.
An occupied old-memory variable in the write branch alone is
therefore not the new claim.

The publicly completed, non-canonical
[P-U-NATIVE-FIXED-READ-1, PR #1430](https://github.com/mathorn1973/twist-j/pull/1430),
at commit ec4995176d36005ba924e0b381c3cc72b97420fc, already proves more
than an occupied write branch. Its
[proof, sections 4--6](https://github.com/mathorn1973/twist-j/blob/ec4995176d36005ba924e0b381c3cc72b97420fc/probes/P-U-NATIVE-FIXED-READ-1/PROOF.md)
gives a 50-point source/occupied-receiver/binary-context preparation
family, permanent local readback, and a retained context \(T\), with
the endpoint law

\[
(X',M',T')
=\bigl(X,(3-T)M+(3+T)X,T\bigr).
\tag{11}
\]

It uses the same local source and receiver readings before and after
the operation. Its two contexts follow the common actual \(a,c,e\)
word; the context selects different prepared receiver lines. It also
contains a separate persistent occupied-receiver sum. Accordingly,
neither a 50-point contextual native operation, an occupied input,
retained context, permanent readback, nor native one-shot arithmetic
is claimed as first supplied here. Its same-reader input/output
property is stronger than the pending write-prefix readings of this
candidate.

The narrower candidate addition is the explicit separately prepared
raw \(q\) control selecting the two different actual native words
\(a,c,e\) and \(b,b,d\), with source and memory in the two fixed
piston pairs. Those words give swap versus hold on the entire
independent product family, with the exact raw source/memory
perturbation routing in (10). The two stationary local readers,
retained control and full closed carrier complete this particular
raw-coordinate witness. This is not a priority claim for native
controlled occupied operations in general.

The nonzero and different piston-sum classes supply the orientation
information needed by both branches.
For comparison, the unshifted proposal
\((\lambda,\mu,-\lambda,-\mu,\chi,0)\) has \(A=B=0\) on its hold tail;
the canonical recurrent-sign-fibre classification identifies
\((\lambda,\mu)\) with \((2-\lambda,1-\mu)\) for every stationary
full-checkpoint reader. Merely retaining distinct states at a known
time would not establish the fixed permanent readings proved here.

The related public
[C-NATIVE-OCCUPIED-EXCHANGE-ENERGY-BOUNDARY-N proof, section 3](https://github.com/mathorn1973/twist-j/blob/5baf51d3019b73b8d6cd7cd755c080fe317b2b73/notes/C-NATIVE-OCCUPIED-EXCHANGE-ENERGY-BOUNDARY-N/PROOF.md)
already defines a complete fixed-control exchange on a 500-point
ready carrier and proves that this added exchange is not produced by
the native continuation. The present initial transient does not
realize that ready-to-ready exchange or evade its composition
boundary. The
[native memory composition note](https://github.com/mathorn1973/twist-j/blob/9de1e43a7fafb8405901f467e76811ddb3c7e238/notes/C-NATIVE-MEMORY-COMPOSITION-N/PROOF.md)
also already distinguishes permanent one-shot storage, transient
memory-to-target response, and later transport of pre-existing
redundancy. None is silently promoted into a reusable writer here.

Public source: canon/CANON.md at the pinned main commit, specifically
the sections U-NATIVE-SOURCE-RECEIVER-RECORD,
U-NATIVE-RECORD-CONTINUATION-BOUNDARY,
U-NATIVE-INVARIANT-AND-NOWRITE,
U-STABLE-PAIRED-PORT-TRANSPORT,
COMMON-HISTORY-FUNDED-AREA-RECEIVER, and
U-NATIVE-WHOLE-SHEET-RETURN-WINDOWS.

The direct substitutions and invariant proof above are sufficient for
this finite candidate. A subsequent frozen independent implementation
may try to falsify it on the complete stated domains. Such a run,
its platform, its artifacts and its status must be reported separately.
Neither this draft nor same-author-session checks constitute the
project's required independent acceptance.
