# Complete unit-flow reader and conditional energy calibration

PUBLIC, NON-CANONICAL. Physical interpretation: working hypothesis H.
Mathematical statements below: conditional candidate-T, action layer L1.
Owner: A. M. Thorn. Reservation [#1431](https://github.com/mathorn1973/twist-j/issues/1431).

## 1. Purpose and the new premise

This is one specified system that can be prepared, advanced, reversed and
challenged. Two independently prepared sources change the same occupied
receiver on consecutive actual steps. A finite pointer and retained contact
context read the changes. Transfer amount is specified before an energy
profile is selected.

**H-UNIT-READER:** three nonnegative stocks of the same kind admit the
complete unit-transfer interaction below, together with the stated finite
apparatus, preparation and observable interface. This is a proposed
physical law, not an implementation or derivation from native U or J.

The declared hypotheses are:

1. A unit can pass along an enabled contact in its stored direction.
   An empty donating stock reflects that direction without transfer.
2. The two contacts, five-position pointer and alternating phase obey one
   complete autonomous discrete update. An abstract tick is a supplied
   time step; its physical clock and duration are not derived.
3. The apparatus has the stated independent raw zero flags. The interaction
   reads actual stock availability, not a possibly faulty flag. Flags are
   updated reversibly and made accessible at the reading interface.
4. The supported independent initial stocks and correct flags/pointer can
   be prepared. The constructor below specifies a preparation, not a
   physical preparation mechanism.
5. When energy is discussed, all three stocks share one additive profile
   and the entire remaining energy belongs to the listed finite hardware.
   No stock-dependent interaction term or unlisted reservoir is admitted
   to that classification. Conservation on faulty states is an additional
   explicit premise of the strongest classification.

These premises can be tested separately. Positive physical interpretations
do not follow merely because an exact program reproduces their consequences.

## 2. Complete carrier and one autonomous step

The ordered state is

\[
s=(r_1,r_2,y,d_1,d_2,e_1,e_2,z,p,\tau,\chi_1,\chi_2).
\]

Here \(r_1,r_2,y\in\mathbb N_0\), \(d_i\in\{-1,+1\}\),
\(p\in\mathbb Z/5\), and \(e_1,e_2,z,\tau,\chi_1,\chi_2\in\{0,1\}\).
Every combination belongs to the carrier. In particular, raw flags are
independent bits, not a restriction to a graph of correct zero indicators.

The hardware projection is

\[
h(s)=(d_1,d_2,e_1,e_2,z,p,\tau,\chi_1,\chi_2).
\]

The initial phase selects \(i=1+\tau\). The switches \(\chi_i\) are conserved.
If \(\chi_i=0\), every coordinate except the phase stays unchanged.
The phase changes to \(1-\tau\) on every step.

If the contact is enabled, apply the following map to its source, the
receiver and its direction:

\[
B(r,y,d)=
\begin{cases}
(r-1,y+1,+1),&d=+1,\ r>0,\\
(0,y,-1),&d=+1,\ r=0,\\
(r+1,y-1,-1),&d=-1,\ y>0,\\
(r,0,+1),&d=-1,\ y=0.
\end{cases}
\]

Let \(\delta=y'-y\). The rest of the actual update is

\[
p'=p+\delta\pmod5,\qquad \tau'=1-\tau,
\]

\[
e_i'=e_i\oplus[r_i=0]\oplus[r_i'=0],
\qquad
z'=z\oplus[y=0]\oplus[y'=0].
\]

The other source, direction and flag stay unchanged. Square brackets denote
a zero-or-one indicator; \(\oplus\) is XOR. All disabled, empty and faulty
branches are included. Call this complete map \(T_R\).

The code uses zero-based active index \(i=\tau\), and consequently the last
active index of a poststate is \(i=1-\tau\).

## 3. Complete inverse and invariant accounts

The inverse local map is

\[
B^{-1}(r,y,d)=
\begin{cases}
(r+1,y-1,+1),&d=+1,\ y>0,\\
(r,0,-1),&d=+1,\ y=0,\\
(r-1,y+1,-1),&d=-1,\ r>0,\\
(0,y,+1),&d=-1,\ r=0.
\end{cases}
\]

From the final phase, the preceding contact is \(i=2-\tau'\).
Undo that contact if enabled, subtract the recovered forward \(\delta\)
from \(p'\), apply the same XOR zero-indicator differences, and flip phase.
If it was disabled, only flip phase. These disjoint inverse branches cover
every output, proving

\[
T_R^{-1}T_R=T_RT_R^{-1}=\mathrm{id}
\]

on the complete infinite carrier.

An independent description avoids the branch formulas. At fixed pair total
\(n=r+y\), put

\[
u=\begin{cases}y,&d=+1,\\2n+1-y,&d=-1.\end{cases}
\quad\in\mathbb Z/[2(n+1)].
\]

Then \(B\) is precisely \(u\mapsto u+1\), and its inverse is \(u\mapsto u-1\).
This is the algorithm of the separately authored independent verifier.

The following quantities are invariant:

\[
N=r_1+r_2+y,\qquad a=p-y\pmod5,\qquad \chi_1,\chi_2,
\]

\[
\eta_1=e_1\oplus[r_1=0],\quad
\eta_2=e_2\oplus[r_2=0],\quad
\eta_y=z\oplus[y=0].
\]

For example, the two copies of \([r_i'=0]\) cancel when computing
\(e_i'\oplus[r_i'=0]\). Thus errors are preserved, not erased or repaired.

The complete fixed-\(N\) shell has

\[
1280\binom{N+2}{2}
\]

states: four direction choices, eight raw-flag choices, five pointer values,
two phases and four switch settings for each stock triple. Every orbit is
therefore periodic. This is a count for the new carrier, not a capacity
statement about native U or the earlier T12 system.

## 4. A fixed present-state reading interface

The interface exposes \(h(s)\). Its context includes the actual retained
directions, the phase, both switches and the zero flags; it takes no source
label, external clock or earlier state as an additional argument.

On a poststate, select \(i=2-\tau\). Define the last-transfer reader

\[
j(h)=
\begin{cases}
0,&\chi_i=0,\\
+1,&\chi_i=1,\ d_i=+1,\ z=0,\\
-1,&\chi_i=1,\ d_i=-1,\ e_i=0,\\
0,&\text{otherwise}.
\end{cases}
\]

For every state with calibrated flags
\(\eta_1=\eta_2=\eta_y=0\),

\[
\boxed{j(h(T_Rs))=y(T_Rs)-y(s).}
\]

Proof: a completed positive transfer ends with direction positive and
\(y'>0\); a completed negative transfer ends with direction negative and
\(r_i'>0\). A failed positive transfer ends with direction negative and
\(r_i'=0\); a failed negative transfer ends with direction positive and
\(y'=0\). The disabled case has zero change. These are exactly the branches
in the fixed reader. The calibrated sector is invariant, so this holds
after every actual step. Event interpretation begins after an executed step;
an arbitrary prepared boundary is not evidence that its formal predecessor
was physically realized.

The equality/codomain contract is ordinary exact equality in
\(\{-1,0,1\}\). For the stock pointer, equality is in \(\mathbb Z/5\).
The pointer itself does not determine \(j\). The complete raw observation
family is this one explicit \(h\), with these fixed maps and no output-based
selection between alternative readers.

Absolute pointer calibration requires the separate condition \(a=0\).
Then \(p=y\bmod5\). If the prepared conserved total satisfies \(N\le4\),
the representative \(p\in\{0,1,2,3,4\}\) equals the integer \(y\) for
the entire history. For larger \(N\), a single pointer value in general
gives only a residue. Enlarging the pointer or composing digits would be
another device specification; it is not silently assumed here.

A false zero flag need not spoil transfer but can spoil the reading.
For the complete initial state

\[
(0,0,1,+1,+1,0,1,0,1,0,1,1),
\]

the first enabled contact reflects. The true \(\delta\) is zero, while the
fixed reader of the output reports \(-1\). Its preserved error vector is
\((1,0,0)\). This is a declared counterexample to uncalibrated exact reading.

## 5. Two consecutive writes on the actual first output

For independently selected \(a,b\in\{0,1\}\) and \(t\in\{0,1,2\}\), prepare

\[
(r_1,r_2,y)=(a,b,t),\quad(d_1,d_2)=(+1,+1),\quad
p=t,\quad\tau=0,\quad(\chi_1,\chi_2)=(1,1)
\]

with correct flags. The receiver stocks along the first two actual steps are

\[
\boxed{t\longrightarrow t+a\longrightarrow t+a+b.}
\]

Both sources are then zero. Their final directions are positive precisely
when the corresponding input bit was one. The original input information
is retained in the complete state, rather than erased at the empty source.
No receiver reset or new receiver preparation occurs between the writes.

All these preparations have \(N\le4\), so the pointer equals the receiver
stock throughout the subsequent orbit, including its reverse transfers.

### A context collision

With \(t=1\), compare \((a,b)=(1,0)\) and \((0,1)\).
After two steps, both have

\[
(r_1,r_2,y)=(0,0,2),\quad(e_1,e_2,z)=(1,1,0),
\quad p=2,\quad\tau=0,\quad(\chi_1,\chi_2)=(1,1).
\]

Their last receiver increments are respectively \(0\) and \(1\).
Their directions are respectively \((+1,-1)\) and \((-1,+1)\).
Thus the complete stock triple, pointer and phase do not determine the
last transfer if directions are hidden. The admitted interface retains
the distinguishing contact context and its fixed reader returns both
correct answers. This does not evade the earlier overlap criterion; it
supplies one explicit context that satisfies it for this chosen law.

### Disconnection is a causal intervention

When \(\chi_1=0,\chi_2=1\), the coordinates

\[
(r_2,y,d_2,e_2,z,p,\tau,\chi_1,\chi_2)
\]

have a closed update independent of \(r_1,d_1,e_1\).
At phase zero only the phase changes; at phase one the listed active
source, receiver and apparatus evolve without source one.
Thus paired preparations differing only in the disconnected source have
identical displayed histories of
\((y,d_2,e_2,z,p,\tau,\chi_1,\chi_2)\).
This proves all-time independence, without asserting that the display
alone predicts its future when \(r_2\) is hidden.

The source-one zero flag can differ between those preparations; no identity
of that disconnected source datum is asserted.

## 6. Energy selection with the apparatus included

Fix the admitted energy family before inspecting an output:

\[
\mathcal E_{f,A}(s)=f(r_1)+f(r_2)+f(y)+A(h(s)),\qquad f(0)=0.
\]

Here \(f:\mathbb N_0\to\mathbb R\) is the same function for all three stocks,
and \(A\) is an arbitrary real function of the listed finite hardware.
The question is which \(f\) admit at least one \(A\) making every complete
transition conservative. An arbitrary prescribed \(A\) need not work.

### 6.1 Two equal-shell witnesses select the old parity parameter

For the earlier declared family

\[
f_c(n)=2\lfloor n/2\rfloor+c(n\bmod2),\qquad c\ge0,
\]

take two correctly flagged preparations with common directions \(++\),
phase zero, pointer one and both contacts enabled:

| Quantity | First preparation | Second preparation |
|---|---|---|
| Initial stocks | \((3,2,1)\) | \((2,3,1)\) |
| After contact one | \((2,2,2)\) | \((1,3,2)\) |
| Conserved unit total | \(6\) | \(6\) |
| Initial stock energy | \(4+2c\) | \(4+2c\) |
| Final stock energy | \(6\) | \(4+2c\) |
| Stock energy change | \(2-2c\) | \(0\) |

All stocks before and after are positive. Thus both histories have
identical initial hardware and identical final hardware, including all
flags and the pointer increment. Let their common hardware-energy
change be \(\Delta A\). Conservation requires

\[
2-2c+\Delta A=0,\qquad \Delta A=0,
\]

so \(c=1\). Conversely \(c=1\) admits a constant \(A\), because \(N\) is
conserved. These witnesses already work on the calibrated sector.

The initial complete energies are also equal, whatever the common \(A\).
No assumption that the pointer or controller has zero energy was needed.

### 6.2 Complete stock-profile criterion on the full raw carrier

**Theorem.** On the complete carrier,

\[
\mathcal E_{f,A}\circ T_R=\mathcal E_{f,A}
\]

if and only if

\[
f(n)=\varepsilon n
\]

for some real \(\varepsilon\), and \(A(h(T_Rs))=A(h(s))\) for every state.
The last equality is on the complete state: the hardware alone need not
have an autonomous update.

**Proof.** Restrict to directions \(++\) and switches \(11\), retaining
arbitrary raw flags, pointer and phase. Write \(Lh\) for the interior
hardware change \(p\mapsto p+1,\tau\mapsto1-\tau\), with flags unchanged.

For each such \(h\), choose active stocks \((r_i,y)=(m+1,m)\), \(m\ge1\).
The new stocks are \((m,m+1)\), so their \(f\)-sum is identical for any \(f\).
Conservation forces \(A(Lh)=A(h)\) for every such raw \(h\).

An arbitrary other interior transfer with \(r_i\ge2,y\ge1\) has exactly the
same hardware change. Hence

\[
f(r_i)-f(r_i-1)=f(y+1)-f(y).
\]

All differences with index at least two are the same \(\varepsilon\).
Therefore \(f(n)=\varepsilon n+b[n>0]\), where \(b=f(1)-\varepsilon\).

Now take \(r_i=1,y\ge1\). Only the source zero flag toggles; the stock
energy change is \(-b\). If \(F_i\) toggles raw bit \(e_i\), conservation
and the already proved identity at \(F_i h\) give

\[
A(F_i h)-A(h)=b.
\]

Both raw values of this flag are admitted for the same physical stocks.
Applying the same equation to \(F_i h\) gives the opposite left-hand side
equal to \(b\). Thus \(2b=0\), so \(b=0\).
For linear \(f\), the stock energy is \(\varepsilon N\), and conservation
is equivalent to invariance of the remaining \(A\). This also proves
sufficiency. No enumeration on a finite cutoff proves this infinite-domain
claim; the argument above does.

The proof does not need a five-position pointer specifically. Its force
comes from matched apparatus transitions and the full raw-flag carrier.

When both contacts are enabled, every invariant hardware-only \(A\) is
constant. To see this, interior swaps in the \(++\) direction sector
generate \((p,\tau)\mapsto(p+1,1-\tau)\), a single ten-cycle. Reflections
connect that sector to each mixed direction sector, and interior moves
connect the other phase there; a further reflection reaches \(--\).
Consequently directions, \(p\) and phase cannot change \(A\) at fixed raw
flags. A transfer from \(r_i=1,y\ge1\) toggles only \(e_i\), and one from
\(r_i\ge2,y=0\) toggles only \(z\). All three raw flags therefore drop out.
Thus on the enabled device the admitted conserved energy has the form

\[
\boxed{\mathcal E=\varepsilon(r_1+r_2+y)+C.}
\]

Nonnegative stock energy would require \(\varepsilon\ge0\).
A nonzero positive unit requires the additional \(\varepsilon>0\).
Its numerical value in joules is not selected.

### 6.3 What changes if faulty states are excluded

If conservation is required only on correctly flagged states, the
occupancy ambiguity remains:

\[
f(n)=\varepsilon n+b[n>0],\qquad
A(h)=b(e_1+e_2+z).
\]

Their complete energy on that sector is \(\varepsilon N+3b\).
Interior matched transitions still force all differences of index at least
two to agree, so these and only these stock profiles admit some \(A\) on
the calibrated sector. Full linearity requires the stronger raw-state
premise. The parity family nevertheless has \(c=1\) already from section 6.1.

General stock-dependent interactions would also reopen the classification.
For example, arbitrary functions of the conserved flag errors or
\(p-y\bmod5\) are complete invariants outside the separated \(f+A\) class.
No uniqueness among all functions of the complete state is claimed.

## 7. Investigable predictions and exact return

The default preparation in model.py is

\[
(r_1,r_2,y)=(2,1,1),\quad d_1=d_2=+1,\quad p=1,\quad\tau=0,
\quad\chi_1=\chi_2=1
\]

with correct flags. Its twelve receiver changes are

\[
(+1,+1,+1,0,0,-1,-1,-1,-1,0,0,+1).
\]

The entire twelve-coordinate state first returns after twelve steps.
The registered audit will record all thirteen boundaries, including the
repeated last boundary. This particular period is a stated finite witness,
not a formula for all two-contact orbits.

For an isolated local pair of total \(n\), the cyclic-coordinate proof
gives a complete local period \(2(n+1)\). Repeated positive transfer,
reflection, reverse transfer and reflection are direct predictions of
the law. The two-contact device has different possible periods.

First discriminating tests are: two writes on the actual first output;
source disconnection; a zero donor; reversal of the complete state;
last-event ambiguity after context is hidden; a deliberately faulty flag;
and the equal-shell energy pair. Merely obtaining a chosen final sum is
insufficient. The predicted directions, flags, pointer and return must
also agree.

A finite recurrent apparatus is not a permanent irreversible archive.
Resetting its complete state by running the inverse is a permitted
mathematical operation; discarding an external observer or inserting
fresh independent sources is not part of this closed device.

## 8. Prior constructions and the physical receiving boundary

The complete packet and finite-record construction already exists in
[C-FIELD-J-CONTENT-TRANSPORT-N](https://github.com/mathorn1973/twist-j/blob/c164b79ce134152ac7cd600421791df74113f29f/notes/C-FIELD-J-CONTENT-TRANSPORT-N/RESULT.md).
The separately selected coherent instrument and internal controller are
likewise earlier work; see
[C-FIELD-J-INTERNAL-CONTROL-N](https://github.com/mathorn1973/twist-j/blob/c164b79ce134152ac7cd600421791df74113f29f/notes/C-FIELD-J-INTERNAL-CONTROL-N/RESULT.md).
This probe does not claim the first autonomous apparatus in the repository.

The parity-price and context obstructions are received from
[PR #1424](https://github.com/mathorn1973/twist-j/pull/1424), specifically
[READOUT.md](https://github.com/mathorn1973/twist-j/blob/c404723bbda3a65dd39c86ae4fc1152b587977c3/notes/C-PHYSICAL-READOUT-CLOSURE-SYNTHESIS-N/READOUT.md)
and
[SOURCE_SELECTION.md](https://github.com/mathorn1973/twist-j/blob/c404723bbda3a65dd39c86ae4fc1152b587977c3/notes/C-PHYSICAL-READOUT-CLOSURE-SYNTHESIS-N/SOURCE_SELECTION.md).
The present contact selects transfer amount directly, instead of funding a
chosen field change from a previously selected stock price. The conditional
price selection consequently is a consequence of this new contact. The
physical selection of the contact itself remains H.

[PR #1430](https://github.com/mathorn1973/twist-j/pull/1430) supplies actual
native one-shot fixed-read transfers and precise repeated-write obstructions:
[PROOF.md](https://github.com/mathorn1973/twist-j/blob/67fde06d2aec8cead7a0bf1bad3988e65c486cdb/probes/P-U-NATIVE-FIXED-READ-1/PROOF.md).
Its native coordinates are in \(\mathbb F_5\); these stocks are in
\(\mathbb N_0\). Equal notation or a five-position display is no bridge
between them. A native realization would have to implement this complete
contact on successive actual output states, including reflection, pointer
updates, phase and fault states.

This probe supplies no extension to every earlier Gauss-shell cell state,
commutation with its reaction G, field propagation, spatial metric,
Hilbert coherence, photon phase, Born occurrence or SI clock/energy.
The concrete next physical question is now a fixed local operation:
can a specified carrier realize B together with its pointer and flag update
under an independently justified energy account? Replacing that question
with a post hoc decoder is outside the hypothesis.
