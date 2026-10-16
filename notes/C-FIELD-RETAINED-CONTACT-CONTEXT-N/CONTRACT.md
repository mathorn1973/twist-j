# Complete context contract

**NON-CANONICAL / conditional candidate-T / L1.** Analytical preparation;
no scientific execution. The source bindings in README.md are part of this
contract. All state equalities below are literal coordinate equalities.

## 1. Old carrier and fixed laws

A cell is c=(m,b,E,M,r), with m,b in (Z^4)^3, E in Z^4, M in Z^2 and
r in N_0. The complete old carrier is

    X = Cell_source x Cell_receiver x N_0_eta x (Z/5)_p.

Every occupied stock, link and pointer is admitted. There is no hidden Gauss,
matter, integral-split, funding or zero-memory restriction. Use exactly the
canonical matrices C,D,K, the complete G with every refused branch fixed,
the complete F and the actual receiver event e defined in the bound sources.
Write

    h(c) = sum_i m_i^t K m_i + sum_i b_i^t K b_i
           + Hraw(E,M) + r,
    Hraw(E,M) = E.E + M.M + E.(C M),
    Htot(X) = h(source) + h(receiver) + eta + 1.

The pointer has the canonical constant energy 1 for every p. E_R(X)=h(receiver)
is the fixed receiver-energy observable; it includes receiver stock.

T has the exact forward chronology Ghat; A; B; F:

* Ghat applies G to both cells and adds the receiver's input event e to p
  modulo 5;
* A swaps the entire source stock and eta;
* B swaps the entire eta and receiver stock;
* F acts on both cells.

Thus T=F B A Ghat and T^-1=Ghat^-1 A B F^-1. All are complete bijections;
G and F preserve each cell's h, and the swaps exchange actual occupied
stocks. No contact is moved across either stock swap in this note.

Fix Kctx={0,1,2}, corresponding in order to (01,02,12). To avoid confusing
this context alphabet with the quadratic-form matrix K, subscripts k always
refer to Kctx. Let S_k act only on the receiver by the already completed
static contact. The fixed whole class contains exactly

    F_k = S_k T,             F_k^-1 = T^-1 S_k.

There is one contact after T, never a contact before it. S_k is an involution
and preserves h and every spectator, including eta and p.

For a receiver c, its proposal swaps b_i,b_j and changes E to E+n v_ij,
with the following exact data:

| k | ij | 5n | v_ij |
|---|---|---|---|
| 0 | 01 | chi(b0)-chi(b1) | (-2,-2,-1,-1) |
| 1 | 02 | chi(b2)-chi(b0) | (1,1,3,-2) |
| 2 | 12 | chi(b2)-chi(b1) | (-1,-1,2,-3) |

Here chi is the coordinate sum. If 5 does not divide the numerator the
contact refuses. Otherwise its raw price is

    kappa_ij(c)=n^2 ||v_ij||^2 + 2n E.v_ij.

The proposal sets r'=r-kappa, and is committed exactly when r'>=0 and
a_G(proposal)=a_G(c), where a_G is the actual complete reaction-acceptance
bit. Refusal fixes every register. Define the *effective* price

    lambda_k(c)=r(c)-r(S_k c).

It equals the raw kappa on a committed proposal and zero on a refusal.
A committed zero-price event also has lambda=0. Its nonstock action need
not be identity. Using an unfunded raw price in place of lambda is forbidden.

## 2. History domain and readings

For one step the joint history domain is all (Y,k) in X x Kctx, interpreted
as X_k=F_k^-1 Y followed by F_k. The entire old final state Y is visible;
the contact label is omitted unless explicitly added. Initial old states
may differ between histories. The target is the integer

    g_k(Y)=E_R(Y)-E_R(F_k^-1 Y).

A supplementary code c(Y,k) into a common alphabet M is adequate for this
target exactly when g factors through (Y,c). No claim requires recovery of
k when two labels have equal target values. A code that must recover the
entire labelled history is a stronger contract.

For horizon n>=0, a word w=(k1,...,kn) specifies X_j=F_kj X_(j-1).
The target archive is the ordered integer tuple

    A=(E_R(X1)-E_R(X0),...,E_R(Xn)-E_R(X_(n-1))).

The horizon is known to the reader. The final interface omits the entire
word. The joint domain contains every Y and every word in Kctx^n, with its
unique inverse initial state. The fixed-initial-state lower bound in PROOF
is stronger than this unrestricted history-domain requirement.

## 3. Claims and exact failure conditions

C1. On every old state Y,

    g_k(Y)=r_R(S_k Y)-eta(Y)=r_R(Y)-eta(Y)-lambda_k(Y).

C2. The gain fibre is partitioned exactly by equal effective prices.
Its local minimum code cardinality is q1(Y)=|{lambda_0,lambda_1,lambda_2}|.
The five partitions in PROOF exhaust every case. Globally three values
are necessary and sufficient, including when restricted to the Gauss
states of the explicit sharp witness. This is last-gain capacity, not a
global uniqueness theorem for contacts or their physical readings.

C3. For each n, the archive set and its exact fibre partition obey the
recursion in PROOF. Its local minimum code cardinality is qn(Y), the number
of distinct archive tuples. A fixed known word needs no supplementary
word code; the final state and n determine its inverse trajectory.

C4. There is one fixed energy shell, one old state Y* and an integer L>=1
such that q_(mL)(Y*)>=3^m for every m>=1, even restricting to histories
starting at Y*. Consequently no fixed finite supplementary alphabet can
recover every full archive at arbitrary horizons. L is an existence value,
not a computed recurrence time or an efficient bound.

C5. On the entire extended carrier X x N_0 x N_0, with arbitrary occupied
a,b, the autonomous update

    k=b mod3,
    Bctx(X,a,b)=(F_k X, 3a+k, floor(b/3))

is a bijection. Its inverse reads k=a' mod3 and returns

    (F_k^-1 Y, floor(a'/3), 3b'+k).

After n steps the last n ternary digits of a_n recover the contact word
regardless of a_0. This supplies exact last-gain and archive reading, and
complete occupied-context inversion. It uses unbounded integer capacity;
an arbitrary n-step word must be supplied in the low n digits of b_0.
A finite b_0 eventually supplies only label 0. An arbitrary infinite
choice stream needs a different, explicitly infinite carrier.

One mathematical counterexample to C1-C5 on the frozen domain refutes the
corresponding claim. No tolerance or finite-to-infinite inference is used.
No EXPECTED, RUN or achieved computational status exists before execution.

## 4. Composition obligations

The retained constant-label map (X,k)->(F_k X,k) is also a complete
bijection. Repeating it uses the same label every time. It must not be
described as accepting arbitrary new unrecorded choices at each step.

The integer-context Bctx instead specifies its own selection dynamics.
It does not commute automatically with another controller, context writer,
stock exchange, or proposed K/T3 step. A later composition must bind its
exact order, show both inverse identities on the whole extended carrier,
identify any restrictions and their invariance, and demonstrate the
accessible reader. If a controller modifies a or b, the inverse must account
for that actual modification. A projection that discards either register
does not inherit the full-state bijection or archive guarantee.

The theorem fixes no nonconstant controller energy that Bctx conserves.
Assigning an arbitrary constant bookkeeping energy is possible abstractly
but supplies no physical preparation, storage cost or work reservoir.
The source-bridge and old-alphabet limitations in the bound source remain.
