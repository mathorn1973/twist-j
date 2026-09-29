# Independent-agent static mathematical review

PUBLIC / NON-CANONICAL. No authority. Action layer: L1.

Review scope: the mathematical argument in PR #1282, as present on public
`main` at `789399eebba3ea17a2e59af237bb3280173fbff2`.
Review context: follow-up lock #1283.

Disposition: no falsifier of the decoder or the stated modulo-5 obstruction
was found. One capacity-scope defect was found in a literal native-label
reading of section 7 and must be explicitly corrected before the successor
proof is pinned; see section 5 below. The written results remain candidate-T;
reported finite counts and executions remain candidate-C. This review does
not promote any claim or close a Canon owner.

## 1. Inputs and separation of activities

The reviewer read:

- `notes/C-J-TWO-TRACE-RESIDUE-DECODER-N/PROOF.md`;
- that note's `PREREG.md` and `RESULT.md`;
- `probes/P-U-COUNTER-AMPLITUDE-CLASS-1/PROOF.md`, especially sections 3-4;
- the `U-COUNTER-REACHABLE-AMPLITUDE-CLASS` row in `canon/REGISTRY.tsv`.

During this assigned review the reviewer did not separately open
`decoder.py`, `verify.py`, or `break.py`, did not execute scientific code, and
did not independently enumerate the strip or reproduce a reported digest.
However, the reviewer inherited the full parent conversation, including
excerpts of those predecessor implementations. The reviewer was therefore
not implementation-blinded. The review checks deductions and scope, not
implementation correspondence or finite-run evidence. This is an
independent-agent static mathematical review with that disclosed context
exposure. It is not blind code confirmation, a second-architecture
computation, or a claim that the reported census has already been
independently reproduced. Any separately blinded breaker must establish
its own isolation and provenance; this report does not supply that status.

Repository authority, pins, hashes, ancestry, and execution provenance are
separate checks performed by the owning session. This report does not
substitute for them.

## 2. Two traces and uniform injectivity [candidate-T]

The real-quadratic coordinate reconstruction is valid. Multiplication by
`J*bar(J)=2-phi` maps `(u,v)` to `(2u-v,v-u)`, giving

    S0=2u+v, S1=3u-v,
    u=(S0+S1)/5, v=(3S0-2S1)/5.

The one congruence `S0+S1=0 mod 5` makes both reconstructed coordinates
integral, but does not assert representability as `alpha*bar(alpha)`. The
proof correctly retains a later representability check.

The norm identity and second-order recurrence follow from this invertible
integer update. In particular the recurrence is valid in both time
directions for pure J steps. It establishes that additional pure-step
traces cannot supply new information once the initial pair is given.

The uniform separation argument is sound. Equality of the ordered trace
pairs implies equality of both positive squared embedding magnitudes.
If distinct scalars have the same residue modulo `mO`, their difference
is `m*eta` for a nonzero algebraic integer eta. Its positive absolute norm
is at least `m^4`. The two embedding triangle inequalities give an upper
bound `16*N(alpha)`. Thus `m^4>16X` excludes all such collisions, including
ones arbitrarily far along a J orbit. No finiteness of the original domain
is used here.

## 3. Total termination and recognition [candidate-T]

The normalization argument also works for surviving input pairs that have
not yet been shown to come from a scalar. This point should be stated
explicitly in the formal successor.

After the prescribed preliminary checks, `u,v` are integers and the real
numbers

    A=u+v*phi, B=u+v-v*phi

have positive product N and positive sum S0. Therefore both are positive,
independently of scalar representability. Set `r=A/B>0`. The two failure
conditions are exactly `r<1` and `r>=phi^4`. They cannot hold simultaneously.

For `r<1`, an inverse J step multiplies r by `phi^4`; while the loop continues
it increases r, and its first entry into `[1,infinity)` is strictly below
`phi^4`. For `r>=phi^4`, a forward J step divides r by `phi^4`; while the loop
continues it decreases r, and its first value below `phi^4` is at least 1.
The Archimedean property gives finite termination in either direction.
There is no oscillation between the two branches. Evaluating a logarithm
is unnecessary.

The half-open convention gives uniqueness, including both endpoint cases.
The sign of the recorded exponent is consistent: an inverse J step on the
working state increases k in `alpha=J^k beta`, and a forward step decreases
it. Multiplication by J is an automorphism of the integral carrier and of
every residue quotient used here.

Centering the four final residues modulo 25, checking the coefficient box,
and recomputing the exact two traces gives a sound recognizer. A successful
check constructs an integral beta with exactly the normalized input data.
Reversing the recorded transformations constructs alpha with exactly the
original input data. Conversely, every scalar in the declared domain must
pass. Thus representability is verified rather than silently presumed.

This establishes mathematical termination for every well-typed input in
the stated interface. It is not a resource bound uniform over arbitrarily
large input integers, nor a statement about implementation handling of
inputs outside that interface.

## 4. Finite coefficient coverage [candidate-T]

The strip implies `1<=sqrt(A/B)<phi^2`, and therefore
`S(beta)<3*sqrt(N(beta))`. The strict upper strip endpoint is correctly used.
At `N<=941`, integrality then gives `S<=92`.

On the four-coordinate integral basis the trace form is

    2S=c^T(5I-11^T)c,
    (5I-11^T)^(-1)=(I+11^T)/5.

It is positive definite. Coordinate Cauchy-Schwarz gives
`c_i^2<=4S/5<=368/5<81`, hence each integral coordinate lies in `[-8,8]`.
The box therefore covers the entire normalized norm-bounded domain, not
merely representatives encountered in an experiment. Its width is less
than 25, giving unique recovery by centered residues.

The reported observed maximum coefficient 7 is not needed and must not
replace this prospective bound. A finite enumeration of the complete box
can supply exact strip and collision counts if its implementation and
execution are independently verified.

## 5. Observed-orbit capacity [candidate-T conditional framework]

The upper bound requires every retained label to occur at every sufficiently
late sheet. That premise is available, and is stronger than a bare formula
for the reader:

- `probes/P-U-COUNTER-AMPLITUDE-CLASS-1/PROOF.md`, section 3, explicitly proves
  `Lambda_n:X_n -> F5^5` is a bijection for every `n>=3` and sets
  `ell_n=Lambda_n` there;
- section 4 proves the complete parametrization
  `R(n,x)=L^n G(ell_n(x))`;
- the canonical Registry row `U-COUNTER-REACHABLE-AMPLITUDE-CLASS` records the
  conserved onto labels and this parametrization on the origin-zero
  reachable domain.

With `L(alpha)=J*alpha`, all retained labels are consequently available at
every `n>=3`. The proof is not assuming the existence of an otherwise
unproved infinite family of reachable states.

For clarity, the new formal proof can state the exact capacity argument as
follows. Normalize each nonzero generator as
`G(label)=J^(a_label)*beta_label`, with `beta_label in B_X`. Define
`K_m(X)=|D_m(B_X)|`. Equality of normalized keys is preserved under every
common integral J shift: the trace-pair map is invertible and J is a unit
modulo m.

If two labels have the same normalized key, choose an integer
`t>=max(a_label,a_other)+3`. Their respective reachable sheets
`n1=t-a_label` and `n2=t-a_other` are both at least 3, and the complete observed
readings agree there. A globally injective reader therefore requires
different normalized keys for different labels, giving the bound K_m(X).

For attainment, choose one strip representative per distinct key. Strip
normalization of an observed reading recovers its unique exponent n and its
normalized key. Thus equality of readings implies both the same n and the
same selected label. The bound is attained for the abstract retained-label
reader. The native label supply is at most 3125, so the maximum number of
native labels actually usable is `min(3125,K_m(X))`.

This last distinction is a required scope correction. The original
phrase "maximum number of labels ... exactly K_m(X)" refers to the arithmetic
codebook capacity if given an abstract-label interpretation. As written
under the native reader classification, its literal interpretation as the
number of distinct native labels is false when K_m(X)>3125: it must be capped
at 3125. In particular K_25=3150 is the number of
available arithmetic keys, not the number of retained native labels. The
3125-label impossibility for mod5 and feasibility for mod25 are unaffected.
Preserve this finding in the successor record; do not silently revise the
historically frozen proof.

## 6. Necessary scope statement about time

The observed datum in the capacity theorem is `D_m(alpha)` alone. Global
injectivity compares readings from different reachable sheets as well as
from different labels. The sheet index n is not an additional supplied
observable. The formal successor should freeze this point explicitly.

If n were additionally supplied, generators `G(label)=J^(a_label)` with
distinct integer offsets would allow the observer to subtract the known n
from the reconstructed total exponent. The norm remains 1. Thus the
K_m(X) obstruction cannot be asserted for the different reader
`(n,D_m(alpha))`, or for a requirement comparing labels only at one fixed
known time. This is outside the frozen observation class, not a falsifier
of the stated global observation theorem.

## 7. Minimal collision and reported finite evidence

The norm-55 witness is consistent with the displayed exact quadratic forms:
both `(0,1,1,-2)` and `(0,1,1,3)` yield `(u,v)=(7,1)`, and hence the same
`(S0,S1)=(15,20)` and norm 55. Their difference is `5*zeta^3`, which is zero
modulo 5O and nonzero modulo 25O. Both satisfy the strip inequalities.
This explicit identity is a candidate-T arithmetic witness.

The reduction from arbitrary collisions to strip collisions is valid:
equal trace pairs imply the same normalization path and exponent, the norm
is unchanged, and multiplication by a power of J preserves congruence.
Therefore an exhaustive, correctly verified strip census can prove
minimality over the entire infinite norm-bounded domain. A verified witness
at 55 together with verified absence below 55 also identifies the globally
first positive collision norm; no search above 941 would be needed for that
limited minimality conclusion.

This static review has not independently established the absence below 55,
the counts 3150/3110/145/2603, the reported class sizes, the number of round
trips, or the digests. Those remain candidate-C evidence pending the new
formal execution and its required controls. The modulo-5 shortfall and the
least successful full 5-power depth consume that census and must retain its
evidence status.

## 8. Disposition and requested clarifications

The decoder proof supports progression to a new formally pinned probe at
the declared L1 scope. The native capacity statement requires the explicit
scope correction identified above before that pin. The correction preserves
the mathematical substance of the 3125-label comparison. Before freezing
the prospective proof, address these three points:

1. Apply the termination argument to every surviving positive pair, even
   before representability has been established.
2. Cite the all-sheet bijectivity in the inherited native chart proof and
   distinguish arithmetic key capacity K_m from native usable capacity
   `min(3125,K_m)`.
3. State that n is not an extra supplied observation and that injectivity
   is required across different reachable sheets.

These comprise one scope correction and two proof clarifications. They do
not change the decoder, thresholds, norm budget, strip convention, or census
questions.
They do not license modifying the frozen historical note. Implementation
verification, fresh scientific execution, and repository promotion remain
separate obligations.
