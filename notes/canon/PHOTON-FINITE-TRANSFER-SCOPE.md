# Proposed Canon disposition of the finite photon transfer

**PUBLIC; NON-CANONICAL.** Proposed fold scope, not a release or earned status.
Prepared against public main `11b66d4755a697031157f0e10dc1898a7d5b6379`,
Public Canon v91, with active release and required checks verified. The
mathematical source is [TRANSFER.md](../C-PHOTON-POLE-S1-S7-N/TRANSFER.md);
the original note and frozen audit are retained as evidence of the proposal.

## 1. What can move

The finite S2 work can justify a substantive, narrow addition to section
**9. The photon and the electron**: a complete family of finite positive
transfer operators, their exact support and electric observable algebra,
and an exact boundary on the microscopic Gauss interpretation. The existing
proof is a candidate for theorem status after review. It does not earn any
new canonical status merely by being present in a note.

This is more than another target formula. The same fixed five weights now
produce the transfer whose actual spectrum can be studied. The spatial
weights remain in its support and in its explicit matrix. The result does
not identify that spectrum with the already canonical D3 characteristic.

The useful small fold has one mathematical definition and three theorem
rows. There is no need to split every identity into a separate registered
claim or to register a new falsified photon proposition.

## 2. Proposed definition and claim rows

All identifiers below are **proposals**. A fresh public issue/ref/registry
collision scan and the relevant owner reservation must precede formal work.
All three proposed rows belong to section 9 and have prospective semantic
type `THEOREM`, status `T`, layer `L4`. Their present status remains
`candidate-T` in non-canonical prose, which is not a public registry status.

### DEF-PHOTON-FINITE-Z5-ACTION

Add one `DEFINITION` item to `NORMATIVE.tsv`, with no claim status and no
`REGISTRY.tsv` row. Define the labelled periodic spatial cubical complex
`(Z/NZ)^3`, `N>=2`, the counting Hilbert space, all oriented links and
plaquettes, `F5` link fields, incoming-minus-outgoing boundary, the exact
`W` and `G`, counting sums, the gauge average, spatial multiplication `M`,
the rectangular `N^3 x m` full-link partition function, and the transfer
and electric/magnetic insertion prescriptions. Preserve the distinction
between labelled links when `N=2`.

The primary spacetime volume prescription is the diagonal periodic sequence
with even `N=m` tending through **all** even integers. The finite theorem
also permits arbitrary `N,m>=2`; this does not replace the primary limit.

This definition fixes a mathematical comparison model. It does not assert
that the model is forced by `J`, equals native `U`, is a physical occurrence
law, or supplies the D3 carrier. It can be adopted as a well-defined object
for conditional mathematics without registering a physical dictionary at
`D`. A later physical adoption requires its own complete typed reading and
gate; calling the definition a physical selection now would overstate the
source.

### PHOTON-FINITE-Z5-TRANSFER

Proposed scope:

> At L4, conditional on DEF-PHOTON-FINITE-Z5-ACTION, for every integer
> N>=2 the finite transfer `mathbbT=M K P_g M` is positive semidefinite,
> with exact range `M S`, where `S` is the span of the characters labelled
> by `r in {-1,0,1}^{E_N}` with `partial r=0 mod 5`. Its largest eigenvalue
> `Lambda_N` is simple and positive. On `H_+=M S`, `T=mathbbT/Lambda_N`
> has spectrum in `(0,1]`, so `H_N=-log T` is well-defined and
> nonnegative. For the full-link counting convention,
> `Z_(N,m)=(5^(N^3) Lambda_N)^m tr(T^m)` for every `m>=2`. The common
> polar unitary gives the explicit transfer matrix
> `sqrt(ell(r')ell(r)) b(r'-r)/Lambda_N`, with `b` the finite character
> sum of the same spatial plaquette weights. No locality of the logarithm,
> uniform gap estimate, native time or thermodynamic/continuum limit follows.

The Fourier support `S` is not itself the transfer range. Zero eigenvalues
outside `H_+` are not assigned finite energy. Strict positivity of the
original kernel entries is distinct from positive definiteness on `H_+`
and from positivity of every entry of its ternary representation.

Falsifier: an admitted `N` and exact violation of positivity, the claimed
range, Perron simplicity, normalization, or the displayed finite matrix.
An audit, publication or runtime defect without such a mathematical
counterexample is an integrity `STOP`, not a scientific refutation.

The finite extension `DYNAMICS.md` can be included here as a corollary:
for every `N>=2`, the ternary carrier splits into 125 nonempty global `F5`
winding sectors, each preserved by transfer and its logarithm, and the
unique finite Perron ground state belongs to the zero-winding sector.
This proof has been checked in the present review. Distinct oriented edge
labels let one or two parallel signed loops in each direction realize all
five values independently, including at `N=2`. Sector conservation is
modulo five; it is not a continuum superselection theorem or evidence of a
photon. No irreducibility within a winding sector or completeness of the
conserved-operator algebra is claimed.

### PHOTON-FINITE-ELECTRIC-INSERTIONS

Proposed scope:

> At L4 in the same finite model, the temporal `WG` insertion `D_l` is
> skew-adjoint and satisfies `D_l=Pi D_l Pi`, with `Pi` projecting onto
> `H_+`; its support is contained in, and strictly smaller than, the
> transfer support. With `kappa=tan(pi/5)` and
> `E_l=-i T_+^(-1/2) D_l T_+^(-1/2)`, one common unitary sends every
> `X_l=kappa E_l` to multiplication by `-r_l` on `S`. Thus the `X_l`
> commute, satisfy `X_l^3=X_l`, have exact spectrum `{-1,0,1}`, and obey
> `||E_l||=1/kappa` for every `N>=2`. The joint spectrum is the
> constrained set of signed modulo-five closed ternary edge fields.
> The compressed spatial score has norm at most `2+sqrt(5)`; products of
> separately compressed magnetic operators are not asserted to equal the
> prescribed same-slice product insertion.

Include the magnetic bound as a supporting corollary, not a fourth claim.
The electric bound is sharp; sharpness of the magnetic compression bound is
not claimed. The unitary may be nonlocal. Three electric values do not count
physical polarizations, and these observables do not supply canonical
commutation relations or a photon-number operator.

Falsifier: an exact admitted counterexample to support containment, the
common conjugacy, trivalence, commutativity, spectrum, or stated norm bounds.
The identity of insertion support with transfer support is expressly not a
claim; the inverse image of the zero character under
`Lambda_N^(-1/2)L^(1/2)M:H_+ -> S` supplies an extra null direction.

### PHOTON-FINITE-REAL-GAUSS-BOUNDARY

Proposed core scope:

> At L4 in the same finite model,
> `exp(2 pi i (partial X)(x)/5)=I` for every vertex. For every `N>=3`,
> the explicit 13-link flow made from five edge-disjoint paths between
> two neighbouring vertices is admitted and has integer divergences
> `-5,+5,0` at those two vertices and elsewhere. Consequently the full
> finite support is not a real divergence-free electric sector.

The finite extension `DYNAMICS.md` strengthens this same row, rather than
creating another one: for every `N>=3`, the real-divergence-free subspace is
not invariant under `T` or `H_N`. In the unique normalized finite ground
state, each vertex satisfies `<(partial X)(x)>=0` but
`<(partial X)(x)^2> > 0`. The four-plaquette surface joins the zero field to
the 13-link junction with a strictly positive transfer coefficient; the
ground state has a positive zero-label coefficient and, by nonnegative
transfer and Perron simplicity, a positive junction coefficient. Charge
conjugation makes the first moment zero. These arguments have been checked
in the present review. The junction is already in the trivial global
winding sector. Strict positivity at each finite size is not a positive
volume-independent lower bound or an infrared result.

This is a **T boundary theorem**, not an `F` verdict on
`PHOTON-MASSLESS-PHASE`, on emergent real transversality, or on a physical
photon. It precludes obtaining a different model by silently restricting
the transfer to real-Gauss fields. An infrared real-Gauss sector still needs
its own quantitative decoupling or scaling theorem.

Falsifier: an exact failure of the congruence, explicit witness, finite
noninvariance, zero first moment or strictly positive local second moment.

## 3. Dependencies and ledger changes

Recommended edges, with `REQUIRES` meaning the displayed theorem actually
consumes the mathematical input:

| Item | Dependency | Relation | Reason |
| --- | --- | --- | --- |
| DEF-PHOTON-FINITE-Z5-ACTION | PHOTON-WINDOW-COORDINATES | REQUIRES | Exact five weights and Fourier convention; they do not force the action choice. |
| DEF-PHOTON-FINITE-Z5-ACTION | DEF-ACTION-LAYERS | REQUIRES | Conditional L4 placement and physical-lift boundary. |
| PHOTON-FINITE-Z5-TRANSFER | DEF-PHOTON-FINITE-Z5-ACTION | REQUIRES | Finite carrier, weights, equality and normalizations. |
| PHOTON-FINITE-ELECTRIC-INSERTIONS | PHOTON-FINITE-Z5-TRANSFER | REQUIRES | Positive support, normalized transfer and polar unitary. |
| PHOTON-FINITE-REAL-GAUSS-BOUNDARY | PHOTON-FINITE-ELECTRIC-INSERTIONS | REQUIRES | Joint electric spectrum and boundary convention. |
| PHOTON-FINITE-REAL-GAUSS-BOUNDARY | PHOTON-FINITE-Z5-TRANSFER | REQUIRES | Actual transfer needed by the extension's noninvariance statement. |
| PHOTON-MASSLESS-PHASE | PHOTON-FINITE-Z5-TRANSFER | BOUNDED_BY | Finite construction supplies one candidate input, not its phase or a complete bridge class. |
| PHOTON-MASSLESS-PHASE | PHOTON-FINITE-REAL-GAUSS-BOUNDARY | BOUNDED_BY | Real transversality is not an exact microscopic consequence. |

No dependency on `PHOTON-TEMPORAL-CHARACTERISTIC` is needed to prove these
finite L4 theorems. Adding one would conceal the important fact that the
fixed cubic gauge model and the selected D3 scalar recurrence remain
different constructions. Neither is a derivation of the other.

The matrix family `exp(-it H_N)` is auxiliary finite operator mathematics,
not a registered L5 native stream; do not close a new temporal physical
gate merely by writing it. No cross-layer gate closes in this fold.

A later sealed fold must consistently update `CANON`, `REGISTRY`,
`NORMATIVE`, `DEPENDENCIES`, `EVIDENCE`, `HISTORY`, status counts, changelog,
derived views and hashes. `CORE_SELECTION` need not include all three
technical rows: one short orientation paragraph is sufficient. Theorem
rows do not belong in `FRONTIER`, which is restricted to live H/O items.
Do not assign the next release number until the actual release queue is
known.

## 4. Existing open roots and the missing pole gate

The v91 ledgers contain only these photon root gates:

| Current owner | Current gate | Disposition from the finite proof |
| --- | --- | --- |
| PHOTON-CONE-CONVERGENCE [O] | GATE-L4-L5-PHOTON-GLOBAL-CARRIER | Unchanged. This is a broader exact global-carrier comparison, not the infrared pole problem. |
| PHOTON-MASSLESS-PHASE [O] | GATE-L4-L6-PHOTON-MASSLESS-PHASE | Remains open. One explicit finite action/transfer is available; the full state limit and massless conclusion are missing. |

`PHOTON-KAPPA-LEMMA [F]` and `PHOTON-WINDOW-PROOF [F]` remain terminal.
`PHOTON-WILSON-VILLAIN-FINITE-COUPLING-NONMEMBERSHIP [T]` remains a
restricted equality obstruction. The finite construction does not repair
these routes or import an `N=5` massless theorem.

The proposed `GATE-L5-L6-PHOTON-POLE-IDENTIFICATION` in
`notes/canon/PHOTON-PROGRAM-CLOSURE-V74.md`, section 8, is **not present** in
the v91 normative ledgers. This is a concrete place to advance Canon even
before proving a pole: register the missing obligation accurately.

Proposed owner: **PHOTON-POLE-IDENTIFICATION [O]**, semantic type
`OBLIGATION`, layer `MULTI`, section 9, with the `OPEN_LIFT`
`GATE-L5-L6-PHOTON-POLE-IDENTIFICATION`. The direction means that the
selected L5 characteristic is to be identified with the actual L6 spectral
support/residue. It is not permission to infer a measure from a scalar
dispersion. `MULTI` is appropriate because the obligation explicitly compares
the already selected L5 endpoint and the reconstructed L6 endpoint.

Freeze the complete S1-S7 profile before giving this owner a runnable
decision. Its output is the actual positive-energy matrix spectral measure,
the actual shell residue on `E=|q|`, and whether
`R(q)=Z_* |q| Pi_gamma(q/|q|)` holds with `0<Z_*<infinity`, the declared
D3 tangent normalization and controlled errors. The target projector is
never substituted for the measured or proved residue. The outcome grammar
remains `AGREE / DIFFER / NONUNIQUE / STOP` at the frozen profile's scope.
Missing continuation or state selection is `STOP`.

Use dependencies on `PHOTON-SPATIAL-TEMPORAL-TRANSFER` and
`PHOTON-TEMPORAL-CHARACTERISTIC` for the L5 target, and explicit open
boundaries on `PHOTON-MASSLESS-PHASE` and the finite transfer/observable
theorems for its other inputs. The all-even diagonal state construction and
nonzero massless shell cannot be marked satisfied by these finite inputs.
Schedule the new owner under `PHOTON_CONTINUUM` as `FOLLOWUP / STOP / FORMAL`
until its complete profile has been reviewed and frozen.

Do not silently rewrite the existing massless root, which currently freezes
a primary-source theorem/comparison route, as a solved direct-construction
route. If that root is broadened to explicitly admit a self-contained direct
proof at the fixed action, record a prospective scope amendment with the
same required thermodynamic and massless conclusion, and preserve its prior
evidence/history. This is separate from accepting the finite theorem.

## 5. Minimal evidence and review route

1. Correct `RESULT.md`'s support-equality wording; preserve the original
   `TRANSFER.md` and `audit.py` bytes and record the correction publicly.
   Finish authorship-compliant branch custody and a reviewed notes PR.
   Merging notes does not create canonical claims.
2. Review the mathematical argument independently, including `M S`, gauge
   normalization, `Lambda_N^m`, the polar-unitary orientation and sign,
   `N=2` labelled edges, sharp norm witnesses, compression/contact rules,
   and the all-even/diagonal limit boundary. Review new finite extension
   statements separately before incorporating them in a claim's scope.
3. A theorem fold may use a **self-contained exact proof in Canon** and
   `INLINE_CANON` evidence with `registry-scope-sha256-v1`. A note URL is
   not an accepted `EVIDENCE.tsv` kind. The proof must be in the normative
   text if the evidence location is `inline`.
4. If the formal public-probe route is chosen, create a fresh named probe
   with a prospective committed/pushed preregistration and accepted exact
   verifier before its formal execution. The old Git-blob pin and local
   audit are disclosed development evidence, not a retroactive formal
   probe. Two required Linux architecture jobs must compare the same
   committed bytes. Preserve the written all-N proof: finite audit cases
   do not prove its universal quantifier.
5. The optional exact audit should target assumptions and concrete boundary
   witnesses. The TARGET-projector check is only a consistency check on the
   separately specified target. It supplies no evidence of the action's
   pole or rank-two residue. A second operating system on x86_64 is not a
   second architecture; matching text after CRLF conversion is not formal
   byte identity.
6. Use one separate sealed release fold only after the evidence and review
   are accepted. Run the required policy, Canon, ledger, gate, probe and
   reproduction checks and both CI architectures. A Canon change replays
   the full public scientific inventory. Follow the normal content/release
   commit and public readback process; no ad hoc activation or workflow
   exception is needed.

An independently theorem-grade proof can establish `T` under policy; two
architecture runs are not a substitute for its mathematical review. Until
that review is recorded, retain the candidate label even if every finite
audit passes.

## 6. Next mathematical work with the highest value

The first target should be **construction of the prescribed infinite-volume
state and its spectral measure**, not another proof of the target matrix.
The companion [INFINITE-VOLUME.md](../C-PHOTON-POLE-S1-S7-N/INFINITE-VOLUME.md)
distinguishes the cluster-state
compactness/DLR lemma from the conditional OS contraction and insertion
framework. The model-specific two-cut reflection/gauge argument remains
outstanding. Subsequence existence is useful but smaller than S1: it does
not prove that all even diagonal volumes have the same limit, or that the
local insertion family has the required continuation. A separately reviewed
cluster-state theorem may later earn its own narrow row; it is not included
in the recommended three-row finite fold or called full reconstruction.

After the state is fixed, prove the simultaneous spatial/time translation
representation and the energy-momentum matrix measure for the declared
insertions. Then determine its actual infrared shell and residue. Uniform
local operator norms bound total spectral weight at finite lattice scale;
they do not prove an atom, linear dispersion, nonzero scaling weight, or a
controlled dimension-two continuum normalization.

The finite Gauss extension sharpens the question: a real-Gauss projection
changes the actual dynamics, so real transverse photons, if present, must
arise through a proved infrared suppression/decoupling of the allowed
charge-five modes. Global modulo-five flux-sector conservation does not
remove that local obstruction. Neither finite noninvariance nor a positive
finite ground-state Gauss-square decides whether its long-distance scaled
contribution vanishes.

The useful near-term canonical advance is therefore: a concrete finite
operator theory, an exact microscopic boundary, and an explicit remaining
pole obligation. The existence, two polarizations, preparation, occurrence,
detector, native-time and SI identification of a physical photon remain
separate unfinished claims.

Original new text: Apache-2.0. No Canon or formal probe is changed by this proposal.
