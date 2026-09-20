# QDD writing through uninterrupted native evolution

**NON-CANONICAL; candidate-T; L1 conditional mathematical construction.**
Notes claim [#1083](https://github.com/mathorn1973/twist-j/issues/1083).
Public basis: main `8e283767271f8ada6d14f0edb70a1606c23b6ed0`,
active Public Canon v90. A. M. Thorn; original text Apache-2.0.

A paired displacement of the native q/r port preserves the complete
source trajectory on the synchronized sheets. It changes sign at each
actual native tick. Consequently an admitted controlled write can be
followed by arbitrarily many genuine U ticks before an admitted signed
archive exchange restores the entire freely evolved checkpoint and exports
the correct coarse mark.

This proves the complete delayed protocol, not a native implementation of
its entrance and exit operations. It supplies neither a physical archive
nor a selected event, new source preparation, occurrence law or layer lift.

## 1. Exact carrier and unchanged native steps

All point coordinates are in F5. Write

    x=(a,b,c,d,q,r),  p=(a,b,c,d),  s(p)=a+b+c+d,
    z=s(p)+q+r.

Equivalently x=(p;z,r), with q=z-s(p)-r. The canonical generators are

    g_a(x)=(b,a,d,c,q,r),
    g_b(x)=(-c,-d,-a,-b,-q,-r),
    g_c(x)=(2-c,1-d+r,2-a,1-b-r,1-q,-r),
    g_d(x)=(2-a,1-b,3-c,4-d,1-q,1-r),
    g_e(x)=(2-a,1-b,3-c,4-d,2-q,1-r).

For a driver bit t, define F_t(x)=g_(z+2t)(x), with generator indices
(a,b,c,d,e)=(0,1,2,3,4). Actual U advances the counter and uses the native
Thue-Morse bit t=theta_n. Let N_(n,k) denote exactly k such checkpoint
steps beginning at counter n, including N_(n,0)=identity. This is a
time-local propagator, not the origin-zero prefix notation in older proofs.

The stable union X14={x:z in {1,4}} has selector table

| z | t | selected generator | next z |
| --- | --- | --- | --- |
| 1 | 0 | b | 4 |
| 1 | 1 | d | 1 |
| 4 | 0 | e | 4 |
| 4 | 1 | b | 1 |

Thus X14 is forward invariant for every bit word. On a fixed sheet each
step is one bijective affine generator. The step on the union of both
sheets need not be injective; no global inverse for N_(n,k) is assumed.

## 2. Paired displacement and all-duration transport

For delta in F5 define the global permutation

    T_delta(p;q,r)=(p;q-delta,r+delta).

It preserves p and z, and T_delta^-1=T_(-delta). Direct substitution in
the three relevant generators gives

    g T_delta = T_(-delta) g,   g in {g_b,g_d,g_e}.             (1)

Their source coordinates do not depend on q or r, and both port
coordinates have linear coefficient -1. Since T_delta preserves z,
it also preserves the selected generator. Therefore, pointwise on X14,

    F_t T_delta = T_(-delta) F_t.                             (2)

Induction proves, for every bit word of length k and hence the actual
native word at every n,

    N_(n,k) T_delta = T_((-1)^k delta) N_(n,k).                (3)

At every intermediate tick, the perturbed and free trajectories have
identical p and z. In particular their complete source paths and selected
generator paths agree, not only their final source values. Their q/r
coordinates differ by the transported paired displacement.

Every g in {g_b,g_d,g_e} also obeys s(p')=-s(p), since the translation
sum for d and e is 2+1+3+4=0 in F5. Put, for n>=3,

    h_n(p)=(-1)^(n-3) s(p).

Then h_(n+1)(p')=h_n(p) along every stable trajectory.

For the declared coarse function

    f(0)=0, f(1)=1, f(2)=f(3)=f(4)=2,

define the global source-controlled permutation

    C_n(x)=T_(f(h_n(p))) x.                                  (4)

Its inverse subtracts the same f(h_n(p)), because it fixes p. The
function f is the admitted LOW/HIGH target; this construction does not
derive it from native dynamics. Equation (3) gives

    N_(n,k) C_n(x)
      = T_(epsilon f(h_(n+k)(p_free))) N_(n,k)(x),
    epsilon=(-1)^k.                                          (5)

Here p_free is the source part of N_(n,k)(x). This source-dependent
statement follows pointwise from the invariant mark; it does not treat
delta as an independently drawn variable.

## 3. Delayed exchange and exact restoration

Choose a common initial stable sheet and a source-independent reference
port r_n^0. Propagate this reference using the same bit word. The selected
generator and the port update depend only on its common z and the bit, so
the reference r_j^0 is independent of p. In the canonical endpoint code
the reference is fixed by z_3=1, r_3^0=0 and the actual subsequent bits.

Add one explicitly admitted F5 archive cell m. During the waiting interval
it is passive: the joint free map is N_(n,k) x identity_m. For N=n+k and
epsilon=(-1)^k define

    S_N^epsilon(p;z,r;m)
       = (p;z,r_N^0+epsilon m; epsilon(r-r_N^0)).              (6)

The source p and trace z remain fixed, so q is reconstructed as
z-s(p)-r. In coordinates e=r-r_N^0 and m, (6) is

    (e,m) -> (epsilon m,epsilon e).

Thus it is a global involution for each fixed reference and epsilon.
It is a signed exchange, not erasure.

Let x=(p;z_n,r_n^0) be ready. From (5), immediately before (6) the
native point is T_(epsilon f(h_n(p))) N_(n,k)(x). Hence

    S_N^epsilon (N_(n,k) x I) (C_n x I) (x;0)
       = (N_(n,k)(x); f(h_n(p))).                            (7)

The final native point is exactly its freely evolved counterpart,
including p,q,r,z. The archive contains the initial coarse mark. Native
U ran for all k ticks between the two added operations.

For a nonblank incoming cell m, the final native port is instead

    r=r_N^0+epsilon m,

while the archive receives f(h_n(p)). The old cell content returns to
the port. Restoration to the reference therefore needs a blank cell
or another explicitly owned destination for that old content.

A stronger useful identity includes arbitrary incoming port displacement
and arbitrary m on the chosen common-z sheet. Set B_n=S_n^+ (C_n x I).
Since the free port obeys

    r_N-r_N^0=epsilon(r_n-r_n^0),

the two sides of

    S_N^epsilon (N_(n,k) x I) (C_n x I)
       = (N_(n,k) x I) B_n                                  (8)

have the same source/trace, final port r_N^0+epsilon m, and archive
r_n-r_n^0+f(h_n(p)). This is a pointwise identity on that sheet times
the full archive cell. It is not asserted across initial sheets sharing
an incompatible reference trajectory.

## 4. The canonical four-point code and coherence

The canonical Galois-code endpoints at time three are

    Y_h=(h,0,0,0,1-h,0),  h in (1,2,4,3).

Write Y_h(n)=N_(3,n-3)Y_h. Their source sums give
h_n(p_h(n))=h. Their ports (z_n,r_n^0) are common, and their points remain
distinct because every later common-sheet step is bijective.

Let W_3 be the canonical code's map from its shifted source coordinates
to these four endpoints, and W_n=N_(3,n-3) W_3. On the source,

    P_L=ones4/4,   P_H=I-P_L.

On the endpoint space D_L selects Y_1; the canonical identity is
D_L W_3=W_3 P_L, with the complementary HIGH identity. In particular
HIGH means zero coefficient at Y_1 after W_3, not zero sum of endpoint
amplitudes. These source and endpoint bases remain distinct.

Extend the declared point permutations linearly to amplitude vectors.
For every source vector v, n>=3 and k>=0, (7) on the four basis points
gives the exact identity

    S_(n+k)^epsilon (N_(n,k) x I) (C_n x I)(W_n v x |0>)
      = W_(n+k) P_L v x |1> + W_(n+k) P_H v x |2>.            (9)

The three HIGH endpoints share precisely the same archive basis vector.
There is no fine HIGH label in this cell, so their mutual coherence is
preserved in the displayed joint state. This is a coherent record
correlation, not a derivation of a selected LOW or HIGH event.

The same admitted protocol can be repeated at later native times using
new blank cells. With earlier cells passive and the native checkpoint
restored after each exchange, induction yields

    W_N P_L v x |1,...,1> + W_N P_H v x |2,...,2>.             (10)

This is repeated recording of the same transported observable. It is
not a sequence of independent preparations or independent trials.
A new source and its preparation mechanism are not supplied here.

## 5. Native holding interval, boundaries and negative witnesses

During the entire interval after C_n and before the archive exchange,

    (-1)^(j-n) (r_j-r_j^0)=f(h_n(p)),  j>=n.                  (11)

Thus the written mark has an explicit native port carrier for an
arbitrarily long holding interval, read relative to the reference and
the native counter. Its entrance write remains an added operation.
This is not a fixed checkpoint reader or an unbounded native archive.

The stable-sheet hypothesis is essential. For the other two generators,

    g_a T_delta = T_delta g_a,
    g_c T_delta = V_delta T_(-delta) g_c,
    V_delta(p;q,r)=(a,b+delta,c,d-delta;q,r).

For example, at x=(0,0,0,0,0,0), bit t=1 and delta=1, both compared
inputs have trace zero and select c. Their source outputs are
(2,2,2,0) and (2,1,2,1), respectively. A temporary r change can
therefore disturb the source outside X14. No global all-state
conjugacy with sign reversal is claimed.

If the waiting length is odd and the final sign is omitted, an intended
archive mark f becomes -f. For f=1 this is 4, not 1. If a previously
occupied cell is reused, its old value returns to the native port by
(6), rather than disappearing. These are exact algebraic controls,
not reported program runs.

## 6. What has and has not been settled

The new result is the composed controlled-write, uninterrupted-native-
evolution and delayed-restoration identity (7)-(9). The elementary
signed r transport was already present in
[#1002, result section 1](https://github.com/mathorn1973/twist-j/issues/1002#issuecomment-5667244164).
The canonical retained chart also already transports the initial port
label. Those existing results are inputs and are not claimed anew.

The canonical
[U-NATIVE-INVARIANT-AND-NOWRITE proof](../../probes/P-U-NATIVE-MEMORY-EVENT-1/MEMORY-PROOF.md)
and its
[actual-clock recurrence proof](../../probes/P-U-NATIVE-MEMORY-EVENT-1/CLOCK-PROOF.md)
exclude permanent BLANK-to-WRITTEN changes for fixed checkpoint readers
on unchanged synchronized U. There is no contradiction: here C_n is an
admitted intervention, the port reading uses the counter and reference,
and the final archive is an additional carrier.

The preparation and LOW/HIGH inputs are the public
[Galois-code proof](../../probes/P-U-GALOIS-FIBER-CODE-1/PROOF.md).
The physical owner remains QDD-INSTRUMENT-APPARATUS in
[the active frontier](../../canon/FRONTIER.md).

In particular, the result does not supply:

- a physical interaction that implements C_n or S_N^epsilon;
- the finite-duration interaction law of either entrance or exit;
- a material archive with an independently justified passive law;
- a physical choice of the source/port partition or of the target f;
- a realized single event, occurrence law, new source or preparation;
- a passed L1-to-L5 bridge or a probability/L6 lift.

It settles free native evolution *between* the admitted operations.
It must not be summarized as realizing the operations themselves.
Although the source path and selector path stay free throughout that
interval, the full q/r checkpoint differs until restoration. Consequently
this intervention protocol does not silently satisfy the feeds_U=false
read-only architecture required by [#539](https://github.com/mathorn1973/twist-j/issues/539).

The proof was derived algebraically and independently reviewed from the
native generator formulas. No scientific script was executed and no
finite run is presented as proof of the all-time statements. Any later
formal computational probe must receive a separate preregistration and
public immutable pin. This note changes no Canon row or gate.
