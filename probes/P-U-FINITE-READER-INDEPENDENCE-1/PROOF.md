# P-U-FINITE-READER-INDEPENDENCE-1: native event language and finite horizons

**NON-CANONICAL; proof-first, result-exposed L1 mathematics.**
Public lock: [#890](https://github.com/mathorn1973/twist-j/issues/890).
This file is a candidate proof, not a run record or physical certificate.

## 1. The actual source and the admitted reader

Use the unchanged public autonomous update

```
Omega = N_0 x F_5^6,
theta_n = popcount(n) mod 2,
U(n,x) = (n+1,g_((sum(x)+2 theta_n) mod 5)(x)).
```

The source class here is every origin-zero head `(0,x_0)`, with all 15,625
choices of `x_0`. The counter is unbounded. The assertion is about each full
actual trajectory, not a periodic replacement of its checkpoint projection.
Other initial counter values are not needed or silently included.

Write `d_n=(x_n,theta_n)`. Fix a positive finite integer `L` and one function

```
f : legal length-L decorated windows -> {0,1,*}.
e_n = f(d_(n-L+1),...,d_n),               n >= L+2.
```

Here 0 and 1 are ordered mathematical event symbols, and `*` is SILENT.
The first admitted window is wholly in the synchronized region `n>=3`.
Delete SILENT outputs in chronological order to obtain the accepted word
`a_0 a_1 ...`, when there are infinitely many accepted outputs. The same
`f` is used at every tick. Its fixed context, if any, is not changed with
time or chosen after comparison with a target. No absolute counter, growing
window, separate persistent memory, additional source input, intervention,
feedback, fresh independent trial supply, or physical occurrence is inferred.

This is the mathematical finite-window class in
`P-U-FINITE-HISTORY-EVENT-1/MEMORY-PROOF.md`, sections 1-3, with an explicit
SILENT-deletion operation. Taking the union over all finite `L` is different
from letting the length of a single reader grow during its run.

## 2. Inherited full-trajectory coding

The registered `U-NATIVE-CHART-AND-QDD-READBACK` gives 3,125 constant chart
labels `ell=(alpha,beta,gamma,delta,epsilon)` for synchronized origin-zero
trajectories. The source files are

* `P-QDD-U-NATIVE-READBACK-1/PROOF.md`, sections 1-3;
* `P-U-NATIVE-MEMORY-EVENT-1/CLOCK-PROOF.md`, sections 1-2 and 5;
* `P-U-FINITE-HISTORY-EVENT-1/MEMORY-PROOF.md`, sections 2-3.

Their exact coding uses

```
S(0)=0, S(m)=m-S(floor(m/2)),
c_m=(m mod 5,S(m) mod 5,theta_m,theta_(m+1)),
C=F_5^2 x {0,1}^2,                        |C|=100,
T0(r,s,u,v)=(2r,2r-s,u,1-u),
T1(r,s,u,v)=(2r+1,2r+1-s,1-u,v),
sigma(c)=T0(c) T1(c),                     c_0=(0,0,0,1).
```

Only the first two coordinates are modulo five. The word `c_0 c_1 ...` is
the length-two substitution fixed word. Every aligned length-`2^j` block is
`sigma^j(c_m)`. The exact primitive certificate is that `sigma^77(c)`
contains every letter of `C` for every `c`.

For every chart label there is a length-two morphism `psi_ell` such that

```
psi_ell(c_m)=((x_(2m+1),theta_(2m+1)),(x_(2m+2),theta_(2m+2))).
```

It agrees with the actual native trajectory for `m>=1`. The first formal
pair merely extends the chart and is not the unsynchronized actual head.
All arguments below either concern the formal word or its fully synchronized
tail; inherited recurrence makes their legal finite languages equal.

## 3. A direct linear bound on native word complexity

For a word `w`, let `p_w(t)` be the number of distinct contiguous length-`t`
factors in its synchronized tail. Fix a chart label and `t>=1`. Choose a
superblock length `B=2^(j+1)` with `j>=0`, `B>=t`, and `B<=2t`.
Each superblock is `psi_ell(sigma^j(c))`. A length-`t` factor lies in two
adjacent superblocks and is specified by their ordered two-letter ancestor
and one of `B` starting offsets. Counting all pairs in `C^2` is a harmless
upper bound, whether or not each pair is legal. Therefore

```
p_d(t) <= |C|^2 B <= 20,000 t.                         (1)
```

No imported entropy formula is needed. Across all chart labels the union
language has cardinality at most `62,500,000 t`. Possible coincident chart
languages reduce this bound and do not invalidate it.

## 4. Nonempty acceptance has a bounded gap

Suppose that the reader accepts one legal length-`L` word `W` on this chart.
Choose `j>=0` such that the finite prefix `psi_ell(sigma^j(c_0))` contains
`W`. Such a `j` exists because `W` occurs in the actual trajectory. The
primitive certificate gives

```
sigma^(j+77)(c) contains sigma^j(c_0)  for every c in C.
```

Thus every aligned decorated superblock of length `B=2^(j+78)` contains
`W`. Every interval of `2B` consecutive native letters contains a whole
aligned `B`-block. Its contained occurrence of `W` has an accepted endpoint
in that interval. Consequently every `G=2^(j+79)` consecutive admitted
output ticks contains an accepted endpoint. In particular acceptance is
infinite and consecutive accepted endpoints differ by at most `G`.

The constant is sufficient, not minimal. This argument uses word
containment along the actual fixed-origin trajectory, not stationarity,
random onset, or an assumed limiting acceptance density. If the reader
accepts no legal window, its disposition is NO_EVENT and there is no accepted
ratio. There is no third case with finitely many synchronized accepted events.

## 5. Accepted-event complexity and the independence obstruction

Fix the reader and chart, with nonempty acceptance, and any valid gap bound
`G` from section 4. A block of `k>=1` accepted symbols starting at endpoint
`n` is completely determined by the native decorated factor beginning at
`n-L+1` of length

```
t_k = L+G(k-1).
```

Indeed, its first output is accepted; the `k`th accepted endpoint occurs
no later than `n+G(k-1)`. Apply `f` to the successive windows inside that
factor and retain its first `k` accepted outputs. Equation (1) therefore gives

```
p_accepted(k) <= 20,000 [L+G(k-1)].                    (2)
```

The right side grows linearly. Choose any `k` such that `2^k` is larger.
At least one binary length-`k` word never occurs in the synchronized accepted
tail. For every `0<p<1`, the nondegenerate Bernoulli product assigns that
word the strictly positive value `p^(#0) (1-p)^(#1)`.

Hence the actual accepted stream cannot have those product block
frequencies at all orders. This statement does not presume that its other
block-frequency limits exist. An absent block already has frequency zero.
Adding finitely many unsynchronized outputs preserves this block-frequency
obstruction: any newly introduced occurrences have limiting frequency zero.
Separately, any block law supported on the synchronized legal accepted
language, whatever its onset weights, cannot be the full Bernoulli law at
the excluded length. This latter support statement does not include onsets
inside an arbitrarily prepended preparation prefix.

For one fixed global `f` on all heads, discard the charts with NO_EVENT and
take the maximum `G` over the finite remaining chart set. A common missing
word exists once

```
2^k > 62,500,000 [L+G(k-1)].                           (3)
```

This excludes attempts to recover the full product law merely by mixing the
finitely many head classes and arbitrary accepted onsets within this fixed
reader. It does not quantify over infinitely many changing contexts/readers.

This is stronger than a finite periodic-checkpoint obstruction: the native
counter remains unbounded throughout. It is also different from the already
registered driver-only `TM-ENTROPY-ZERO`: the proved object is the full
decorated native trajectory after an arbitrary fixed finite history reading
and deletion of its SILENT symbols.

## 6. No uniform finite failure horizon across all window lengths

The preceding conclusion cannot be strengthened to one fixed finite horizon
that defeats every reader in the union over all finite `L`.

Fix any integer `h>=1`. The binary de Bruijn directed graph has vertices
the `(h-1)`-bit words and one edge for each `h`-bit word, from its prefix to
its suffix. Each vertex has indegree and outdegree two. Appending the letters
of a target vertex gives a path to it, so the graph is strongly connected.
Splicing closed trails exhausts all edges and gives an Euler cycle. Reading
the final bit of each traversed edge yields a cyclic word `D_h` of length
`2^h` containing every binary length-`h` word exactly once. This is the same
finite combinatorial resource used in `P-RECORD-OCCURRENCE-SYMMETRY-1`.

For every `1<=j<=h`, each binary `j`-word has `2^(h-j)` extensions, so
its cyclic count is `2^(h-j)` and its all-prefix frequency is `2^-j`.
At length `h+1` there are at most `2^h` cyclic blocks instead of `2^(h+1)`;
the full fair product block law fails.

The registered `U-FINITE-HISTORY-CLOCK-PHASE` proves that a legal past-and-
current Thue-Morse word of fixed length `L_h=5*2^(h-1)` determines its
endpoint phase modulo `2^h`. A decorated checkpoint window contains these
same driver bits. Compose that phase reader with `D_h`. On every origin-zero
native trajectory, after full synchronized warm-up, this single fixed
finite-window reader emits `D_h[n mod 2^h]` and has no SILENT outputs.
Its all-prefix time block frequencies agree exactly with the fair product
values through the prechosen horizon `h`; it fails at `h+1`. These are
deterministic time frequencies, not an independently realized stochastic
trial law.

This mathematical construction supplies neither an actual random trial law
nor a physical apparatus. The phase and cycle are deliberate reader resources.
The no-go in section 5 is asymptotic in the order for each fixed reader;
it cannot by itself reject an experiment of a specified finite horizon, give
a minimal required window, or establish an approximate-independence bound.

## 7. Complete-state and physical boundary

If arbitrary explicit counter dependence is admitted, any prescribed binary
sequence `b_n` has the mathematical reader `F(n,x)=b_n`; if the sequence is
computable, this is a computable reading algorithm. Thus a theorem about all
readers of the complete carrier cannot be inferred from a complexity bound
on its decorated finite-alphabet projection. The present no-go explicitly
requires fixed finite-window dependence and does not constrain every decoder.

The theorem narrows a proposed occurrence mechanism: if it lives in this
class, its actual accepted language has the stated bound. It does not decide
whether physical experiments demand exact all-order independence, nor does
it falsify Born's marginal rule. A native physical occurrence mechanism still
requires an independently typed event map and apparatus resources, actual
preparation, persistence/reset, accepted-trial semantics, and the relevant
comparison horizon. None is selected by this proof. The existing physical
QDD owners and every L4/L5 or L5/L6 gate retain their status.
