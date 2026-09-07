# From incidence to occurrence: exact finite selection boundaries

**PROOF-FIRST / RESULT-EXPOSED / L1 MATHEMATICAL MODEL.**
Public lock: [#887](https://github.com/mathorn1973/twist-j/issues/887).
Basis: Public Canon v80 and `P-BINARY-RECORD-QUADRATIC-SELECTION-1`.
The arguments and witnesses below precede the public execution pin. They
are elementary proofs, not claims of historical mathematical priority.

The previous probe classified pair valuations. Here an incidence carrier
and its branch labels are already given. This asks what additional laws
turn those cardinalities into occurrences. A mathematical probability vector
below is an explicit conditional parameter, not a physical measure.

## 1. What relabeling symmetry can select

Let a finite group G act on finite sets R of ready states and E of possible
fine outcomes; assume E is nonempty. All equalities are literal. A selector
F:R->E is equivariant when F(gr)=gF(r) for every g and r. Write

    G_r = {g in G: gr=r},       E^(G_r) = {e: ge=e for all g in G_r}.

**Theorem 1 (complete selector criterion).** On each G-orbit of R, choose
one representative r. An equivariant selector exists if and only if every
E^(G_r) is nonempty. Its complete class is obtained by choosing one element
e_r of E^(G_r) per representative and setting F(gr)=g e_r. In particular,
the number of selectors is the product of |E^(G_r)| over the ready orbits.
For empty R this is the single empty map, with empty product one.

**Proof.** If h fixes r, equivariance gives hF(r)=F(r), proving necessity.
Conversely, g r=g' r implies g'^{-1}g is in G_r. It fixes the chosen e_r,
so g e_r=g' e_r. The formula is well-defined and equivariant. Every such
map is determined by its values on the representatives. This proves both
completeness and the product formula.

If E is transitive and |E|>1, it has no point fixed by all of G. Hence no
fully symmetric ready state (G_r=G) admits a deterministic equivariant
selection of a single outcome. Enriching the ready carrier can supply the
missing asymmetry: R=E with F the identity, or R the linear orders on E
with F the first member. These are different, explicitly structured carriers.

This is also a dynamical statement. If T:R->R is deterministic and
equivariant, G_r is contained in G_(T(r)); iteration preserves that
inclusion. If T is bijective and equivariant, its inverse is equivariant,
and the two stabilizers are equal. A symmetric initial state cannot lose
its symmetry through such a closed update. The same holds with an allowed
fixed NO_EVENT symbol: a fully symmetric ready can remain silent, but it
cannot select one member of a nontrivial transitive E. New inputs, an
asymmetric initial state, a different group, or a multivalued rule change
the premises. This is not a no-go theorem for asymmetric native U states.

**Theorem 2 (conditional ensemble law).** The invariant probability laws
on any finite G-set R are exactly the laws constant within each orbit:

    mu(r) = alpha_O / |O|,      alpha_O>=0, sum_O alpha_O=1.

There is no probability law on empty R. If F is equivariant and mu is
invariant, its pushforward is invariant on E. If E is transitive, that
pushforward is uniform. For a declared coarse partition E=disjoint-union
E_j this gives P(j)=|E_j|/|E|. The partition need not be preserved by G;
the symmetry assumption concerns the fine outcome law before coarse reading.

**Proof.** Invariance makes the mass at r equal to the mass at every gr,
so it is constant on an orbit. Conversely these constants define invariant
laws. Equivariance bijects the inverse images of e and ge, preserving their
mu masses. Transitivity then makes all |E| output masses equal; normalization
fixes them to 1/|E|. Summation over each coarse fibre proves the last formula.

Invariance of the input law is sufficient, not necessary, for a uniform
output when F has larger fibres. It is not selected by covariance of F or T.
When the action on E has several orbits, symmetry alone leaves their total
masses free. Changing the physical symmetry to make it transitive would be
a substantive new premise. None of these assertions supplies a realized
event, a law on ready states, or independence between repeated selections.

## 2. Exact replacement for an unspecified mixing assumption

Let Omega be a nonempty finite set, T a permutation of Omega, and
e:Omega->{1,...,r} disjoint-union {SILENT}, r>=1. Observe e(T^t x) at
consecutive t=0,1,..., including the initial state. There is no reset,
new input, external time-dependent rule, or hidden changing context.
All memory and any finite clock belong to Omega. For each cycle C write

    l_C=|C|, m_(C,j)=|{x in C:e(x)=j}|, d_C=sum_j m_(C,j).

**Theorem 3 (every-start occurrence classification).** A start on C with
d_C=0 gives NO_EVENT forever. On any other cycle the accepted event stream
is periodic with a period of d_C labels. Its limiting accepted frequency is

    q_(C,j)=m_(C,j)/d_C.

For n>=1 accepted events, its prefix count K_j(n) satisfies

    |K_j(n) - n q_(C,j)| < d_C.

For a fixed normalized vector q, every start in Omega has events with
limiting frequencies q if and only if

    d_C>0 and m_(C,j)=q_j d_C for every cycle C and every j.    (CB)

**Proof.** Each cycle repeats its l_C tick labels. Removing SILENT repeats
its d_C accepted labels; a different start merely rotates that word.
Writing n=a d_C+b, 0<=b<d_C, leaves a exact periods and a remainder of
b labels. Both the remainder count and b q_(C,j) lie in [0,b], so their
difference has absolute value at most b<d_C. This proves convergence and
the bound. Necessity and sufficiency of (CB) follow cycle by cycle. For
tick counts the identical argument gives limiting m_(C,j)/l_C and a
prefix error less than l_C, including silent cycles.

The possible individual-run limiting vectors are exactly the q_C of the
non-silent cycles. Taking an arbitrary initial ensemble does not make one
trajectory switch cycles. An allowed-ready subset would simply restrict
(CB) to the cycles meeting that subset; that restriction must be declared.

**Theorem 4 (stationarity is a different condition).** Every stationary
probability law for T has the unique form

    mu(x)=gamma_C/l_C for x in C,   gamma_C>=0, sum_C gamma_C=1.

If the chance of an accepted tick is positive, the stationary single-tick
law conditioned on acceptance is

    P(j | accepted tick)
      = [sum_C gamma_C m_(C,j)/l_C] / [sum_C gamma_C d_C/l_C].  (S)

Equivalently it is a mixture of q_C with weights proportional to
gamma_C d_C/l_C. Every mixture of the non-silent q_C is obtainable by a
stationary law: for desired mixture weights beta_C, take gamma_C
proportional to beta_C l_C/d_C on those cycles and zero on silent ones.
If all cycles are silent the conditional law is undefined, with NO_EVENT.

**Proof.** T-invariance is precisely mu(Tx)=mu(x), so masses are constant
on cycles. Normalization gives gamma and its converse. Sum the masses
over each event fibre and divide by the total accepted mass to obtain (S).
The stated substitution gives the converse mixture construction.

Uniform mu on Omega is always stationary and gives the global counting
ratio |e^{-1}(j)|/sum_i |e^{-1}(i)| at an accepted tick. This does not imply
(CB), nor does it turn a conditioned random tick into a chronological first
hit. The v80 predecessor-gap theorem already separates those protocols.

## 3. Exact countermodels and a positive conditional route

For any d>=2, take Omega=E={0,...,d-1}, T=id and e(x)=x. All permutations
of E act simultaneously on states and outputs. The dynamics is reversible
and fully equivariant, and the uniform initial law is invariant and
stationary. Every single-time ensemble marginal is uniform, but each realized
stream is x,x,x,... . No individual start has the uniform fine frequencies.
Under that ensemble, for t!=s,

    P(e_t=e_s)=1, whereas independent uniform draws give 1/d.

This refutes the structural implications

    reversible + relabeling covariant + uniform stationary ensemble
      => every-start counting frequencies
      => independent trials

where the second implication is separately refuted by the next model.
An arbitrary prepared delta law on this same model is also a direct witness
that dynamics and covariance alone do not select the ensemble marginal.

For a positive frequency construction, cycle once through any given finite
nonempty incidence carrier E, recording its already supplied branch labels.
The single cycle meets (CB) for q_j=|E_j|/|E| from every start. This uses no
random initial phase for the frequency conclusion. It does adopt a cyclic
order/update on E, and does not derive that order from U. For already
declared complete pair fibres |E_j|=d_j^2, it conditionally yields the
quadratic ratios d_j^2/sum_i d_i^2; it does not select the pair fibres.

A sharper independence counterexample is the four-state cycle with coarse
word 0011. Every start has frequency 1/2. Under uniform initial phase the
four adjacent pairs 00,01,11,10 each have probability 1/4, just as two fair
independent bits do. Nevertheless 000 never occurs, whereas three such
bits give it probability 1/8. Correct one- and two-record laws do not imply
all-order independence. This example strengthens the diagnostic, not the
existing v80 result about its particular LOW^A HIGH^B word.

## 4. The exact finite cost of a requested independent horizon

Let a closed deterministic autonomous model have N finite possible initial
states and one binary output at each step. The update need not be reversible
for the following lower bounds. All memory and clocks are included; there
is no externally supplied fresh input. An arbitrary law on initial states
is allowed as a conditional mathematical parameter.

**Theorem 5 (finite horizon capacity, with a sharp reversible witness).**

(a) If its first k>=1 outputs have exactly the independent Bernoulli(p)
law with 0<p<1, then N>=2^k. More precisely the support of the initial law
has at least 2^k states. Consequently no fixed finite closed deterministic
model has that law for all finite horizons.

(b) If the initial law is uniform on N states and p=a/b in lowest terms,
0<a<b, then b^k divides N. In particular N>=b^k.

(c) For each such a,b and k, there exists a reversible single-cycle model
on exactly b^k states whose first k outputs, under uniform initial phase,
have that exact law, and whose every-start long-run frequency is a/b.
It cannot have the independent law through k+1 at the same initial ensemble.

**Proof of (a).** A deterministic initial state determines just one k-word.
Every one of the 2^k binary words has positive Bernoulli probability.
All must have nonempty, disjoint preimages in the supported initial states.
The bound follows. Choose k with 2^k>N for the all-order impossibility.

**Proof of (b).** The all-LOW word has probability a^k/b^k. It also has
probability n/N for an integer n counting its initial states. Since
gcd(a^k,b^k)=1, equality forces b^k to divide N.

**Proof of (c).** Use the alphabet A={0,...,b-1}. Construct the directed
graph with vertices the (k-1)-words on A and one edge for each k-word,
from its prefix to its suffix of length k-1. At k=1 it is one vertex with
b labeled loops. Every vertex has b incoming and b outgoing edges, and
appending the letters of any target vertex gives a directed path to it.
Thus the graph is balanced and strongly connected. An Euler circuit exists:
follow unused edges until closing a trail (balance forbids getting stuck
elsewhere), and splice in further such closed trails until no edges remain;
connectivity ensures any unused edges can be reached from a used vertex.

Read the appended edge letters cyclically along this circuit. Each cyclic
k-window is one edge's k-word, exactly once, giving a cyclic word of length
b^k. This is the usual defining property of a de Bruijn cycle, proved here
by the graph construction. Use phase x modulo b^k as the autonomous state,
T(x)=x+1, and output LOW when that phase's letter belongs to {0,...,a-1}.
T is a permutation consisting of one cycle. Uniform phase gives every exact
k-letter word probability 1/b^k. A prescribed coarse binary word with h
LOWs has a^h(b-a)^(k-h) preimages, exactly its Bernoulli(a/b) probability.
Shorter marginals follow by summing extensions. There are a b^(k-1) LOW
phases, so (CB) gives frequency a/b from every start. Part (b) rules out
independence through k+1 since b^(k+1) cannot divide b^k.

The construction makes (b) sharp even with reversibility and every-start
frequency balance. It adopts an order and a uniform initial phase; it does
not physically generate that phase law. At k=2,b=2 it includes the 0011
example up to rotation. The finite word repetition is an exact observable
correlation. A deterministic writer can copy the emitted symbol into a
fresh addressed cell using the previous probe's reversible transposition;
such an archive requires its own extra cells and does not create entropy.

For the already adopted v80 source (1,0,0,0), A=1,B=15 and p=1/16. Twenty
exact independent outputs under a uniform finite ready ensemble therefore
require N divisible by 16^20=2^80. With arbitrary nonuniform initial masses,
only the general 2^20 support lower bound above is asserted. These are
conditional counts of distinguishable initial states, not a physical memory
estimate or an empirical requirement on any existing apparatus.

## 5. Scientific disposition and the next concrete obligation

The structural sufficiency claims are false in the displayed mathematical
classes. Positive conditional routes survive: invariant fine ensemble plus
transitivity for a marginal, cycle balance for every-start frequencies, and
an explicitly prepared finite resource for a finite independent horizon.
These are three different statements with different premises.

The new contributions to this program are the complete ready-stabilizer
criterion, the all-cycle occurrence criterion with silent-state handling,
and the sharp denominator/resource construction. They do not rerun the
v80 classification of chronological onset laws, native history readers,
or the earlier pair-valuation census. No universal new physics theorem or
historical novelty of finite group/dynamical combinatorics is claimed.

Any proposed physical bridge must now specify its incidence carrier, actual
ready selection, symmetry action, complete autonomous update, accepted-event
map and protocol. It must prove the needed occurrence law on that supplied
class, instead of replacing it by ensemble invariance or reversibility.
Independence is an additional hypothesis only if the proposed experiment
requires it; this probe does not add it to the physical owner's contract.

In particular, native U has an unbounded n counter. Its finite checkpoint
alone is not a complete autonomous state. The finite N obstruction cannot
be applied to U, an open apparatus supplied with fresh environmental input,
or a reader of an unbounded history by ignoring those resources. This probe
neither supplies nor excludes a physical Born mechanism. The physical
apparatus, class-completeness and terminal-event obligations remain O/STOP.
All results here are L1 mathematics; no L4/L5 or L5/L6 gate is executed.
