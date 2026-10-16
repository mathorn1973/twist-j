# K: complete comparison and lift contract

**NON-CANONICAL / conditional candidate-T / L1.** Sources and authority are
frozen in README.md. Every equality is literal, and every hidden register
used by a proposed inverse belongs to its complete carrier.

## 1. Fixed interfaces

Let C be T1's 23-state context set: three startup states I0,I1,I2 and
the ready set Cready={+1,-1} x {1,4} x F5. At transition n to n+1 the
observer receives beta=theta_n. Its total update is exactly h_beta from
T1, with the three startup transitions and, on ready contexts,

    h_beta(sigma,z,nu)=(-sigma,4+2beta,nu+[beta=t(z)]),
    t(4)=0, t(1)=1.

All arithmetic in z,nu is modulo five. Its readout is T1's fixed
d_C(tau,q,r), with BLANK at startup and the five-point restored-pair
table afterward. Driver access, its timing and one-time I0 preparation
are admitted resources. No minimum-size or reversible-implementation
claim is imported.

Let X be T2's complete two-cell field carrier, including occupied stocks,
link eta and pointer p. Let k in {0,1,2} label S01,S02,S12, respectively,
and F_k=S_k T in that exact order. Two occupied integer registers a,b
have the fixed bijection

    B(X,a,b)=(F_k X,3a+k,floor(b/3)), k=b mod3.

The integer registers have unbounded capacity. They are not fresh zero
bits, a finite-capacity device or a physical work reservoir. Choices for
a prescribed finite word are preloaded into b; a finite b does not
supply an arbitrary infinite choice stream.

## 2. Exact deterministic composition

For one supplied bit beta, define the complete Cartesian comparison map

    Phi_beta(tau,X,a,b)=(h_beta(tau), B(X,a,b)).

The first factor does not read or modify X,a,b. The second does not read
or modify tau. This precisely fixes the order and absence of coupling.
Both are total on all declared states, including occupied helpers and
refused contacts. No commutation with an unlisted source interaction or
with a stock swap is assumed.

For the native comparison, take an unchanged native trajectory launched
from every P in F5^4 at common receiver (q,r)=(0,1), origin zero; supply
its actual theta_n to Phi and expose its actual current receiver (q_n,r_n)
to d_C. The context starts once at I0, while X0,a0,b0 are arbitrary.
The native cell is not identified with either field cell or integer register.

The two fixed readers have separately typed input ports:

    native reader: (tau_j,q_j,r_j),
    field archive reader: (X_j,a_j,b_j,j).

The native payload decoder uses only its three declared inputs. At j>=3 it
returns PRESENT(kappa(P)). The archive reader receives the known horizon j
to specify the requested archive length. If these ports are combined and
one field step is synchronized with every native tick, j equals the native
counter: the combined interface DOES expose it. No absence-of-counter claim
is made for that combined interface. The finite driven-reader claim remains
about the restricted native reader. At j>=1, k_j=a_j mod3 and T2's last-gain
reader returns

    g_(k_j)(X_j)=r_R(S_(k_j)X_j)-eta(X_j).

For a full archive it applies T2's inverse j times and reverses the resulting
gain list. The initial integer a0 may be occupied. No assertion associates
the recovered kappa with the field gain or with contact choice k_j.

## 3. Frozen complete-product T3 class

The candidate reversible lift class admits any nonempty helper set M,
finite or infinite, and a purported bijection L_beta on Cready x M.
The projection pi is onto Cready and must satisfy on EVERY input

    pi L_beta(tau,m)=h_beta(tau), tau in Cready, m in M.

M may include the complete field state, both integer registers, other
occupied work registers and arbitrary interactions. A complete inverse
must be two-sided on the entire product. A helper preparation restriction
or a changed projected off-preparation transition changes this class.

Decision T3: this entire fixed-bit class has no member. The same negative
decision holds with all 23 contexts and their literal startup transition.
This is a complete-product factor obstruction, not a universal no-go for
reversible measurement, finite-horizon computation or every observer.

## 4. Required successor changes

A positive reversible successor must name at least one changed premise:

1. Specify off-preparation behavior different from literal h_beta and prove
   a complete bijection plus its reader on the intended prepared states.
2. Specify a proper invariant carrier or reachable graph, prove its closure
   in both directions, and expose the actual clock and lost information.
3. Use a different context/observed port and prove its readout and complete
   resource account anew.

Replacing all driver/context machinery by a finite autonomous
source-independent controller still falls under T1's all-finite no-go.
A full ordered archive for arbitrary omitted contact words still has T2's
unbounded-capacity requirement. Neither obligation disappears by renaming
registers or retaining only the last contact label.

No positive native/field bridge is assumed. Such a bridge needs its own
source carrier, preparation map, dynamics relation, contact selection,
accessible observations, helper energy and exact domain. Missing premises
are recorded as missing, not filled by the intended output.

## 5. Falsification and status

An error in the factor-surjectivity argument, the fixed-bit image, or the
two imported readout/occupied-inverse proofs blocks the corresponding claim.
A claimed counterexample must satisfy the entire frozen class, especially
the projection identity for every helper state. A changed domain is a
new contract rather than a counterexample to this one.

This is proof-only analytical work. No scientific program, finite audit,
computational PASS or public gate is claimed. All physical and canonical
obligations retain their existing status.
