# ADDENDUM 1 to PREREG: C-NATIVE-FIBRE-PENTIT-WIGNER-N

**NON-CANONICAL. Candidate with no authority. Action layer L1 only.**
Frozen 2026-10-02, before the first execution of the addendum verifier.

## 0. Why an addendum and not an edit

The base preregistration
(sha256 `cbda8c9f0fbc7da3b5baeed685d9e8592ecffaa6b70617633a271056ca94757c`)
was pinned at 2026-10-02T16:59:20Z and its verifier was executed before the
owner's addition reached this session. A pinned preregistration is not
amended. Nothing in the base document, its verifier, its stdout or its result
is changed here. This addendum adds claims B7, B8 and C2 with their own
verifier and their own pin. Authority and currency are those of the base
document: Public Canon v97, tag `canon-v97`, main
`738e0421bd15aaea5bb6ef2a56f1cab752d44de5`, re-read before this freeze and
unchanged.

Origin. Owner direction of 2026-10-02: state the boundary of the measuring
reader, add the control example of the Fourier line state against the LOW
direction, and freeze explicitly the admissible readers and the change of
state after a reading. Counting holds for line preparations together with
line readings; a nonnegative input alone is not enough.

Unchanged by this addendum: `C-OCCURRENCE-CYCLE-COUNT-N` stays
`STOP_APPLICABILITY / H_NOT_TESTED`.

## 1. Frozen class of the point model

Carrier: the 25 points `u = (q,r)` of `F_5^2`. Conventions of the base
document, section 1.

**Preparations admitted.** The uniform count on one of the 30 lines.

**Readers.**
1. Deterministic point reader: a map from points to outcomes. On a
   preparation `mu` the outcome `x` has weight `mu(o^(-1)(x))`.
2. Line reader of direction `delta`: the deterministic point reader whose
   outcome is the line of direction `delta` through the point. Five outcomes.
3. Stochastic point reader: response functions with values in `[0,1]`
   summing to 1 over outcomes. Admitted only so that the exclusion in B7 is
   stated for the wider class as well.

**State change U1.** After a line reading of direction `delta` the point moves
to `u + t delta`, where `t in F_5` is one fresh coordinate, counted uniformly
and uncorrelated with the system point. One such coordinate is consumed per
reading. It is a supplied resource of this model.

**Control update U0.** The reading leaves the point where it is.

Counts in B8 are counts over microstates `(u, t1, t2)`: an ensemble count. They
are not frequencies along one trajectory.

## 2. Target exposure for the addendum, complete

Seen before this freeze:

1. Owner's addition: `|<l,f>|^2 = 1/4` for the Fourier vector `f` and the LOW
   direction; a deterministic reader on five points gives only multiples of
   `1/5`.
2. This author, by hand before the freeze: the dual inversion formula of B7.1;
   the LOW response as five times the Wigner values of B4; LOW probabilities
   `4/5`, `1/20`, `0`, `1/4` on the basis and Fourier line states; the
   prediction that exactly two of the 30 values are multiples of `1/5` and
   that the other twenty lie among `(3+-sqrt5)/10`, `(7+-sqrt5)/40`,
   `(17+-sqrt5)/40`; the acceptance response; the value `-1` of the HIGH
   response at the origin; the rule U1, its expected agreement, the expected
   failure of U0, and the necessity argument of B8.4.
3. Everything listed in section 2 of the base document and the full base
   stdout (sha256 `3b2bdc432e1bfebcd453b83a6766a2863b6a1d54243180cbc20e0b1ce4ea39ad`).

Not seen before this freeze, recorded as found: the multiplicities of the
twenty remaining LOW probabilities; the multiset of the HIGH response.

## 3. Claims

### B7. Reader boundary

**B7.1, dual uniqueness.** For every operator `E` the function

$$
\xi_E(u)=\operatorname{Tr}(E\,A_u)
$$

is the unique function on the 25 points with

$$
\frac15\sum_{u\in L}\xi_E(u)=\operatorname{Tr}(\Pi_L E)\qquad\text{for all 30 lines } L .
$$

Hence an effect acts on line preparations as a point reader exactly when
`0 <= xi_E <= 1`, and as a deterministic one exactly when `xi_E` takes only
the values 0 and 1. Falsifier: an audited effect whose inversion from the 30
line sums differs from `Tr(E A_u)`.

**B7.2.** The LOW projector has response `1` once, `3/4` four times, `-1/4`
four times, `(1+sqrt5)/8` eight times, `(1-sqrt5)/8` eight times. Twelve values
are negative. LOW is therefore no point reader on line preparations,
deterministic or stochastic. Falsifier: any other multiset.

**B7.3, control example.** `f = (1,zeta,zeta^2,zeta^3,zeta^4)/sqrt5` is the line
state of one line of direction `(1,0)`, and

$$
|\langle \ell,f\rangle|^2=\frac14 ,
$$

while every deterministic point reader returns a multiple of `1/5` on a line
state. Falsifier: a different value, or `f` not a line state.

**B7.4.** On the 30 line states the LOW probability is `4/5` and four times
`1/20` on the basis states, `0` and four times `1/4` on the Fourier states;
exactly two of the 30 values are multiples of `1/5`. The remaining twenty are
recorded as found. Falsifier: any of the ten stated values wrong, or a count
other than two.

**B7.5.** The acceptance effect `I - |+><+|`, the projector on the sum-zero
sector, is a deterministic point reader: response 1 off the line `r=0`, 0 on
it. The boundary therefore runs between acceptance and the LOW and HIGH
split, not at acceptance. Falsifier: any other response.

**B7.6.** HIGH, acceptance minus LOW, has response values outside `[0,1]` and
is no point reader either. The multiset is recorded as found. Falsifier: all
values inside `[0,1]`.

Scope of B7. The declared QDD reading leaves line counting through its
measurement as well as through its preparations (B3). Nothing is said about
larger carriers, contextual apparatus or other readings. For any future
classification of an apparatus class, preparations and readers both have to
be classified; a nonnegative preparation alone decides nothing.

### B8. State change

**B8.1.** For all lines `L, M`:

$$
\Pi_M\,\Pi_L\,\Pi_M=\frac{|L\cap M|}{5}\,\Pi_M .
$$

After a line reading with outcome `M` the state is the line state of `M`.
Falsifier: one pair where the identity fails.

**B8.2.** With U1, for every line preparation `L` and every ordered pair of
directions, counting the 125 microstates `(u,t1,t2)` returns exactly

$$
P(M_1,M_2)=\operatorname{Tr}(\Pi_L\Pi_{M_1})\,\operatorname{Tr}(\Pi_{M_1}\Pi_{M_2}),
$$

the two-round law of the line readings, including the repeated context
`delta_2 = delta_1` and the changed context. Exhaustive over
`30 x 6 x 6 = 1080` scenarios. Falsifier: one history whose count differs.

**B8.3.** With U1, given any two-round history the final point is uniform on
the last outcome line. Falsifier: one history with a different final law.

**B8.4, necessity of the fresh coordinate.** Let an update reproduce the next
line reading in every direction. By B2 the law of the point after outcome `M`
must then be the uniform count on `M`. A preparation transversal to the
reading has exactly one point on `M`. So one microstate needs five
continuations: no function of the point alone can serve, and each reading
consumes at least one uniformly counted five-valued coordinate. Falsifier: a
transversal pair of lines meeting in other than one point.

**B8.5, control.** With U0 the three-round history `delta_1, delta_2, delta_1`
with `delta_1 != delta_2` returns the first outcome with count 1, while the
line-reading law gives `1/5`. This holds in all `30 x 30 = 900` scenarios;
U1 gives `1/5` in all of them. Falsifier: a scenario where U0 agrees or U1
disagrees.

### C2. Applicability, no computation

The frozen class of section 1 is a complete spatial counting contract for
two-round and three-round histories of line states. It needs one supplied
resource: a fresh uniformly counted pentit per reading. No native source of
such a coordinate, and no renewal of it inside a registered resource account,
is exhibited here. The contract table of the base document, Part C, is
therefore unchanged, and so is its disposition:
`STOP_APPLICABILITY / H_NOT_TESTED`.

Remark, not a claim. The registered native law contains one five-to-one merge
on ticks 0 to 2 (base claim A5). A merge is not a source of a fresh
coordinate, and no identification is made.

## 4. Proofs

**B7.1.** Put `s(L) = sum_(u in L) xi(u)` and `T = sum_u xi(u)`, which is the sum
of `s` over any one parallel class. Six lines pass through `u` and every other
point lies on exactly one of them, so
`sum_(L through u) s(L) = 6 xi(u) + (T - xi(u))`, hence
`xi(u) = (sum_(L through u) s(L) - T)/5`. Existence:
`Tr(Pi_L E) = (1/5) sum_(u in L) Tr(A_u E)` by definition of `Pi_L`.

**B7.5.** `|+><+|` is the line operator of the line `r=0` (base A3, B1), so
`Tr((I - |+><+|) A_u) = 1 - [r = 0]`.

**B8.1.** `Pi_M` is a rank-one projector (base B1), so
`Pi_M X Pi_M = Tr(X Pi_M) Pi_M` for every `X`; with `X = Pi_L` and base B1.

**B8.2 and B8.3.** The first outcome is the `delta_1`-line through `u`, with
count `|L cap M_1|` out of 5. After U1 the point is uniform on `M_1`, whatever
`u` was. The second outcome then has count `|M_1 cap M_2|` out of 5, and after
U1 the point is uniform on `M_2`. The counts multiply because `t1` and `t2`
are counted independently of `u`.

**B8.5.** Under U0 the third reading reads the same point in the same
direction as the first. The line-reading law is
`sum Tr(Pi_L Pi_M1) Tr(Pi_M1 Pi_M2) Tr(Pi_M2 Pi_M1) = 1/5` for two different
directions.

## 5. Code, systematics, thresholds, labels, breaking

Code: `claude_verify_addendum1_c_native_fibre_pentit_wigner_n_2026-10-02.py`.
Standard library, exact arithmetic, no float, no repository file needed.
Static compilation only before the pin. The hashes of this addendum and of
its verifier are recorded in
`claude_PIN-ADDENDUM-1-C-NATIVE-FIBRE-PENTIT-WIGNER-N.sha256` before the
first run.

Systematics: all of section 5 of the base document. In addition: the class
of section 1 is part of the claim; U1 is one admissible update and its
uniqueness is not claimed; the effects are those of the declared reading
(LOW direction with the empty coordinate 0, acceptance as the sum-zero
projector, HIGH as their difference); one architecture is available.

Failure threshold: any `FAIL` falsifies the corresponding claim at its stated
scope; the run is archived as is; nonzero exit on any `FAIL`.

Labels on a clean run. `candidate-T`: B7.1, B7.3, B7.5, B8.1, B8.2, B8.3,
B8.4, B8.5 (inline proofs, exhaustive audits). `candidate-C`: B7.2, B7.4,
B7.6 (finite computations), eligible for computation-grade T after
byte-identical stdout on two architectures. C2 is a disposition.

Breaking, after the run: an independent implementation. Line states built as
explicit vectors (basis vectors and quadratic-phase vectors), not as sums of
phase-point operators; probabilities by inner products in the basis
`1,zeta,zeta^2,zeta^3`; the response by Weyl expectation values; the point
model re-implemented with explicit microstate lists. Counterexample search:
a deterministic update of the point alone, taken from the 50 native fibre
maps or from all translations indexed by the outcome, that reproduces the
two-round law.

## 6. Note on the proof of B3

The owner's route to B3 through the support and constant-modulus lemmas of
Gross is an alternative proof in prime dimension. The base document's own
proof uses only the row `r=0` and holds in every odd dimension. Both stand;
neither source was needed for the run.

The update U1 is the usual one of epistemically restricted point models of
line states. No source was read for it in this session and none is used in a
proof.
