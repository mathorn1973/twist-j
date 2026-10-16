# Supplied temporal window: total update and prescribed native readout

**NON-CANONICAL / candidate proof / L1 only / 2026-10-13.**
Original work Apache-2.0, A. M. Thorn. Lane P of
[reservation #1484](https://github.com/mathorn1973/twist-j/issues/1484).

This proves the temporal sidecar specified by the already public frozen
[CONTRACT.md at 4302c31f07823b2a843e3702ca14620c1917b853](https://github.com/mathorn1973/twist-j/blob/4302c31f07823b2a843e3702ca14620c1917b853/notes/C-CLASSICAL-SIGNED-PORT-CONTRACT-N/CONTRACT.md),
especially Sections 5 and 8. The coordinator completed public byte readback
before dispatch. The contract, README and source manifest are unchanged.
This text uses written finite tables and proofs; no script, verifier,
propagator, scientific import, measurement or hardware experiment was run.
It does not construct the external bit provider or a physical clock.

The inherited native action and its five-context theorem are fixed at
[376f52d28c7e7a699a0d66a177592289ab5c6bf8, PROOF.md](https://github.com/mathorn1973/twist-j/blob/376f52d28c7e7a699a0d66a177592289ab5c6bf8/notes/C-BETA-PENTAD-MINIMUM-CONTEXT-N/PROOF.md).
That proof binds the first-entry lift to
[59711070f75b56b2441b951dd9cd77bb1dfc5da2, NATIVE_PROOF.md](https://github.com/mathorn1973/twist-j/blob/59711070f75b56b2441b951dd9cd77bb1dfc5da2/probes/P-BETA-PENTAD-NATIVE-EXTENSION-1/NATIVE_PROOF.md).
The separate raw-receiver observer is
[T1 at c5c4555a1641cdf39f235642e0e9230274d75d5f](https://github.com/mathorn1973/twist-j/tree/c5c4555a1641cdf39f235642e0e9230274d75d5f/notes/C-U-RAW-RESIDUE-CONTEXT-UPDATE-N).
All remain noncanonical at their declared scopes. Public Canon v101 is
the authority stated in STATUS; this lane does not change its ledger.

## 1. Types, starting point and the external port

Let Bit={0,1}, Q_window=Bit^4, and

    theta_m=popcount(m) mod2, m in N_0,
    W_n=(theta_n,theta_(n+1),theta_(n+2),theta_(n+3)),
    beta_n=theta_(n+4).

Choose any declared starting n0>=0. Its choice and the provider's
initialization must be independent of the classical source z in Q^4 and
the native payload x in F5^6. At this start the provider supplies W_n0
once. At the j-th update it supplies exactly beta_(n0+j). Both source
objects are inaccessible to the provider. These statements declare the
provider's mathematical interface, not its acquisition mechanism.

The internal stored state is one word q_j in Q_window. The total updater
receives only (q_j,beta), with beta in Bit; it receives no n0, n, source,
payload, current receiver, source history or classical wave. The readout
receives only q_j. The checkpoint evaluator receives (C,x,label), where
the label is this readout's time-information input. It receives no hidden
counter or local step index. n0 and j in the proofs below are bookkeeping
indices, not arguments supplied to either function.

Timing is explicit. Initialize before evaluating the starting checkpoint.
At step j, read the current label for time n0+j. Supply beta_(n0+j)
before committing the shift to q_(j+1). The next readout is for time
n0+j+1. There is no additional mathematical evaluation delay once the
window is supplied. The initial window already contains three future
values; every update receives the next required future value. No claim
of causal acquisition from the current bit alone, zero physical latency,
or an SI duration is made. Readout does not consume or refresh the word.

## 2. Complete transition and readout tables

For q=(b0,b1,b2,b3), define

    S(q,beta)=(b1,b2,b3,beta).

Let K5={k0,k1,k2,k3,k4}, with the literal triples

    k0=(1,0,0), k1=(0,0,0), k2=(1,0,1),
    k3=(0,1,0), k4=(0,0,1).

INVALID is a diagnostic symbol distinct from those five native contexts
and from every checkpoint in F5^6. Define r:Q_window->K5 union {INVALID}
by the following table. The two transition columns give every one of the
32 possible state/bit pairs; no transition is inferred from a selected
trajectory.

| q | S(q,0) | S(q,1) | r(q) |
|---|---|---|---|
| 0000 | 0000 | 0001 | INVALID |
| 0001 | 0010 | 0011 | INVALID |
| 0010 | 0100 | 0101 | k3=(0,1,0) |
| 0011 | 0110 | 0111 | k3=(0,1,0) |
| 0100 | 1000 | 1001 | k3=(0,1,0) |
| 0101 | 1010 | 1011 | k0=(1,0,0) |
| 0110 | 1100 | 1101 | k0=(1,0,0) |
| 0111 | 1110 | 1111 | INVALID |
| 1000 | 0000 | 0001 | INVALID |
| 1001 | 0010 | 0011 | k2=(1,0,1) |
| 1010 | 0100 | 0101 | k2=(1,0,1) |
| 1011 | 0110 | 0111 | k4=(0,0,1) |
| 1100 | 1000 | 1001 | k1=(0,0,0) |
| 1101 | 1010 | 1011 | k1=(0,0,0) |
| 1110 | 1100 | 1101 | INVALID |
| 1111 | 1110 | 1111 | INVALID |

Both functions are total on their stated finite types, including invalid
windows. INVALID does not halt, reset, normalize or repair the updater:
the displayed shift remains its transition. A new initialization is a new
preparation, not an automatically granted recovery operation.

The ten legal words will be proved to be exactly the actual length-four
Thue-Morse factors. On a legal word, an equivalent formula for r(q) is

    e0=(b0 xor b1)*(b2 xor b3),
    e2=(1-e0)*(1-b0),
    e3=b0*(1-b1),
    r(q)=(e0,e2,e3).                                      (P1)

Products and subtraction here are ordinary bit arithmetic. On the six
illegal words the readout is INVALID, regardless of the formula's value.
No additional error-memory state is stored: INVALID is an output symbol.

## 3. Completeness of the legal language

The Thue-Morse recursion is theta_(2m)=theta_m and
theta_(2m+1)=1-theta_m. Equivalently theta is the fixed point of
mu(0)=01, mu(1)=10, so it is also the fixed point of mu^2, whose blocks
are mu^2(0)=0110 and mu^2(1)=1001.

Every length-four factor starts at an offset j in {0,1,2,3} inside a
four-symbol block, and is contained in that block and its successor.
All four adjacent pairs ab in {00,01,10,11} occur: the prefix 01101001,
obtained by three substitutions, witnesses 01,11,10 and 00. Since
theta=mu^2(theta), every mu^2(ab) occurs at the corresponding aligned
position. Therefore the exact length-four language is

    L4={mu^2(ab)[j:j+4] : ab in {00,01,10,11}, 0<=j<4}.    (P2)

The slice has four symbols. These are its complete candidates:

| ab | mu^2(ab) | offset 0 | offset 1 | offset 2 | offset 3 |
|---|---|---|---|---|---|
| 00 | 01100110 | 0110 | 1100 | 1001 | 0011 |
| 01 | 01101001 | 0110 | 1101 | 1010 | 0100 |
| 10 | 10010110 | 1001 | 0010 | 0101 | 1011 |
| 11 | 10011001 | 1001 | 0011 | 0110 | 1100 |

Removing repetitions gives precisely

    L4={0010,0011,0100,0101,0110,1001,1010,1011,1100,1101}.

The complement in Bit^4 is exactly

    {0000,0001,0111,1000,1110,1111}.

Thus all ten non-INVALID table words occur, and none of the six INVALID
words occurs. This is a complete substitution proof, not an inference
from searching a long prefix or running a census.

## 4. Readiness and source independence at every declared start

**Proposition.** Initialize q_0=W_n0 once and supply the admitted sequence
beta_(n0+j). Then for every j>=0,

    q_j=W_(n0+j),                                        (P3)

and its readout is never INVALID.

**Proof.** The assertion holds at j=0 by preparation. If it holds at j,
the transition retains theta_(n0+j+1), theta_(n0+j+2), theta_(n0+j+3)
and appends beta_(n0+j)=theta_(n0+j+4). These are exactly the four entries
of W_(n0+j+1). Induction proves (P3). Every such word belongs to L4 by
Section 3, so its readout is valid. Nothing in this argument resets the
state after initialization. It applies to every n0, not only origin zero.

For any two classical sources or native payloads at the same declared
start, the initialization and supplied bit sequence are the same. S and r
do not inspect either source. Induction therefore also proves equality of
their internal words and time labels at every j. This is the exact
source-independence claim, with a time-only provider explicitly admitted.
It does not grant that provider any physical sensor or driver realization.

For arbitrary input bits, S is still total but (P3) need not hold. INVALID
certifies an illegal window, not every incorrect supply. A wrong bit may
leave a legal window and even the same label. Window legality alone does
not authenticate the actual clock or its alignment. In the frozen physical
qualification scheme, a missing qualified clock/provider is NOT_READY,
not a physical falsification or a license to repair the preparation.

## 5. Exact five-context output without a hidden counter

No three consecutive theta values agree: any three positions contain a
complete even-aligned pair, which is complementary by the recursion.
For even n, both pairs (theta_n,theta_(n+1)) and
(theta_(n+2),theta_(n+3)) are complementary, so e0 in (P1) equals one.
For odd n=2m+1, the four bits are

    (1-theta_m,theta_(m+1),1-theta_(m+1),theta_(m+2)).

If both neighboring pairs were complementary, theta_m=theta_(m+1)
and theta_(m+1)=theta_(m+2). This would be three equal consecutive bits,
which is impossible. Thus e0=0 for odd n. Consequently (P1) gives

    e0=1-(n mod2),
    e2=(n mod2)*(1-theta_n),
    e3=theta_n*(1-theta_(n+1)).                           (P4)

These are exactly the context coordinates kappa(n) in the frozen
five-context proof, equation (11). Equations (P3)-(P4) prove

    r(q_j)=kappa(n0+j)                                   (P5)

for all admitted starts and updates. The proof mentions n to establish
correctness; the readout algorithm uses only four stored bits.

The table partitions L4 into five classes of sizes 2,2,2,3,1, in the
order k0,k1,k2,k3,k4. All five labels occur: representative absolute times
are 0,1,2,3,11, respectively, as also shown in the frozen proof. This
states the global output image over all admitted times, without asserting
a new context minimum on a different domain. The inherited minimum five
concerns one time-only evaluator label common to every x and C; it is not
a claim that this sixteen-state driven buffer is a minimal controller.

## 6. Compatibility with the prescribed native evaluator

All arithmetic in this section is over F5. Write a native checkpoint
x=(p1,p4,p1p,p4p,q,r), set s=sum(p), z_native=s+q+r, and unpack

    p=4s*1+w1(1,-1,0,0)+w2(0,1,-1,0)+w3(0,0,1,-1).

The scalar sheet z_native is not the classical source vector z in Q^4.
For clarity recall the pinned decoder's matrices and affine data:

    A=[[4,1,0],[0,1,0],[0,1,4]],
    P=[[0,4,1],[0,4,0],[1,4,0]],
    w_star=(1,4,3),
    o_r=(4,4-r,1-r),
    R_r(w)=Aw+(r+1,0,1-r).

For a valid k=(e0,e2,e3), its affine chart is

    J_(k,z_native,r)(w)=
        P(A^e0 w-o_r),          z_native=0;
        w-w_star,              z_native=1;
        R_r^e2(w)-w_star,       z_native=2;
        P(A^e3 w-w_star),       z_native=3;
        P(w-w_star),           z_native=4.               (P6)

A^2=P^2=I and R_r^2=Id, so the chart is invertible. For C in GL(3,F5),
compute w'=J^-1 C J(w), keep (s,q,r), and repack p using the same
difference basis. Denote the resulting checkpoint map by D_native(C,x,k).
Its inverse for the same k replaces C with C^-1; no original native U
inverse is being assumed.

The frozen five-context proof, Sections 3-5, proves for every n and x
that D_native(C,x,kappa(n))=F_(C,n)(x), the checkpoint component of the
prescribed first-entry lift. Its actual first-entry chart mathcalK is a
nonzero scalar multiple of (P6). For linear C that scalar cancels in
mathcalK^-1 C mathcalK. Combining this all-time identity with (P5) gives

    D_native(C,x,r(q_j))=F_(C,n0+j)(x)                    (P7)

for EVERY native checkpoint x, including all transient sheets, and every
linear invertible C. In particular it holds for the specified T and
SO(B,F5). This uses the exact written inherited identity, not finite
samples of n, x or C. The evaluator's time-information input is only k.

For a total diagnostic interface one may return INVALID whenever r(q_j)
is INVALID; this is an error output, not a native checkpoint or an admitted
contact. No correctness for an incorrect but legal window is promised.
This lane defines an evaluator of the existing action, not a new native
generator, physical gate or coupling to the classical source.

## 7. The driven resource cannot be silently removed

For each fixed beta, S loses b0 and has only eight output words. Thus this
updater alone is neither injective nor onto Q_window; no full-state
reversibility follows from totality. An old bit and the provider/driver
information need explicit retention if a reversible completion is proposed.

Even restricted to actual windows, the current word cannot determine its
successor without extra input. The recursion gives W_0=W_6=0110, but
W_1=1101 and W_7=1100 because beta_0=1 and beta_6=0. No function of the
sixteen stored words alone can implement both actual successors.

Nor can the five-label readout update autonomously: kappa(0)=kappa(10)=k0,
whereas kappa(1)=k1 and kappa(11)=k4. These exact counterexamples concern
the stated word/label state descriptions. No new minimum for all possible
driven controllers, auxiliary clocks or time encodings is asserted.
The contract admits the supplied port; it does not close its acquisition.

## 8. Classical cut clock and remaining bridge obligations

| Object | Actual inputs and state | Output or scope |
|---|---|---|
| Classical two-cut wave model | Rational wave/tapes, t=0,1, external stop H_run=2; cyclic pointer k in Z2 | Signed four-port response; no theta bit is required by its rational law |
| Native temporal provider | Declared start and actual forward TM values; no access to z or x | One initial four-bit window, then one supplied beta per shift |
| This P updater/readout | A word in Bit^4 and a supplied next bit | Sixteen possible internal words; five valid time labels plus INVALID |
| Prescribed native evaluator | C, x in F5^6 and one valid time label | Checkpoint component F_(C,n)(x); n is not a decoder argument |
| T1 raw-receiver observer | Its 23-state context, current theta_n at transition n->n+1, and separate raw (q,r) reader | Original-residue readout at its own preparation and readiness contract |

The classical pointer's wrap after two cuts is neither a new cold
preparation nor an autonomous SI clock. H_run=2 does not set the native
starting n or equate a classical cut with a native tick. This P proof
does not change the wave, source, tape carrier or its ledger.

T1's current-bit interface is not the future-window provider declared here.
Its three startup states and twenty ready contexts are not the five
evaluator labels. The contact/archive T2 has its separate ternary label
and occupied integer registers. No field gain or omitted contact history
is read by this sidecar. The T3 complete-product obstruction is not evaded
by discarding the old word bit or by calling a driven shift reversible.

No Enc_native:F5^6->Q^4, common equation between n and t, contact realizing
T, or physical provider is supplied. Seven-mode DP5 endpoints remain a
different carrier and clock. There is no source-independent physical
acquisition proof, energy for window/control storage, SI timing assignment,
reset realization, occurrence law or L2-L6 bridge in this lane. Including
the sidecar in an actual apparatus requires those entries in the full
clock/control/reference/sensor/memory boundary; the classical E_full alone
is not an energy account for an unspecified provider.

The earned conclusion is (P7) under the explicit supplied-window
preparation/input contract, with a total sixteen-state transition and
total diagnostic readout. It is a written candidate proof, not a new
executed gate, physical qualification or Canon disposition.
