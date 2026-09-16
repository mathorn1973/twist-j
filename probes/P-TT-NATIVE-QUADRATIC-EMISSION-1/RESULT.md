# P-TT-NATIVE-QUADRATIC-EMISSION-1 result

Status: two-architecture computation gate PASS; candidate-T by written exact
proof, pending independent scientific review. Public Canon unchanged.

Owner: ChatGPT-TT-SOURCE-20260910-B. Lock: #931.
Basis: Public Canon v83, main 51dee9705628e0c9f7bfc7082df46af46ed314b3.
Pin: a8e35e95d8adb891a28233779f2547a2441d70f1.

## Decision

The accepted local formal execution of the exact public pinned verifier
completed with exit code 0, empty captured stderr and exact stdout matching
`EXPECTED.txt`. None of the frozen scientific falsifiers F1 through F9 fired
on the audited surfaces. The written proof in `PROOF.md` supplies the universal
derivations.

The required public pull-request workflow then replayed the unchanged pinned
verifier from clean GitHub checkouts on both required architectures. Run
`34449802081` completed with:

```text
architecture-x86_64   success   job 102782713610
architecture-aarch64  success   job 102782713864
aggregate check       success   job 102782797989
```

Both architecture jobs separately passed policy, unit tests, Canon, ledger,
gate contract and `Reproduce changed public probes`. The x86_64 log records

    VERIFY PASS P-TT-NATIVE-QUADRATIC-EMISSION-1
      3e05906a2113305ae21de00c5eb306a139e913d0d6f7d6a12369feb5fbaab692
      e66a90283d718825c0aa3190cf4c7f955b1cab709dd602cac20c4f89b40e18ac

and the aarch64 job reached the same successful probe-replay step. The
aggregate `check` emitted `TWO-ARCHITECTURE CHECK PASS`. This satisfies the
repository computation gate for the pinned exact verifier. It does not replace
independent review of the written theorem argument.

An earlier attempted local execution is explicitly excluded from evidence
because its local draft differed by eight unused bytes from the public pin.
`RUN.md` records the complete custody correction. The pinned verifier itself
was never changed. A later one-character typo in the recorded SHA-256 of empty
stderr was also corrected only in `RUN.md`; the accepted run, pin and output
were unchanged.

## Scientific result at current evidence grade

[candidate-T] Native source dependency. The complete length-four factor
language of the public Thue-Morse driver is exactly the ten-word K1 alphabet.
Its stationary masses are 1/6 on `0110` and `1001`, and 1/12 on each other
word, exactly the optional K1 input law. The K1 coordinates are

    u0=w2-w0,
    u1=w3-w1.

The public L5 orientation-source formula `omega(a,b,c)=c-a` evaluates to the
same two expressions on the overlapping triples. That equality is retained as
a cross-check only. This L1 probe does not consume the L5 source object as an
input, infer an L5-to-L1 physical map, or claim an unnamed cross-layer lift.
The actual L1 source dependency rests on the public K1 packet and the native
Thue-Morse word theorem above. No physical occurrence law is supplied.

[candidate-T] Quadratic source-map classification. In the frozen class of
local homogeneous quadratic O(2)-equivariant maps from two ordered spin-one
source slices to a spin-two output, with reflection covariance and slice
antisymmetry, the complete class is

    Q_kappa(x,y)=kappa(y^2-x^2).

Matching the emitted zero-start quadratic energy to the inherited K1 kinetic
radiative channel forces `kappa^2=1` on every nonstatic source packet. Forward
source order fixes the displayed representative

    Phi=b1^2-b0^2=H1-H0.

No new dimensionless source coefficient is introduced. The classification is
conditional on the frozen local quadratic class. TT-SOURCE does not require a
global uniqueness theorem, and none is claimed here.

[candidate-T] Regular emission. With the outgoing TT field independent of the
source doublet,

    h0=h1=0,
    R_L h1=Phi,
    R_L hm=0 for m>=2,

has one total prefix-compatible rational history and gives h2=Phi. The map is
zero on the four static K1 packets and nonzero on all six active packets. Its
spatial mean is zero. This construction contains no action pullback through a
square and therefore does not inherit the singular zero-amplitude branch of
the PR #930 mechanism.

[candidate-T] Conservation compatibility. The linear transverse stress is
frozen as

    rho=J_i=S_i3=0,
    S11=Phi_plus/(2 lambda),
    S22=-Phi_plus/(2 lambda),
    S12=S21=Phi_cross/(2 lambda).

It satisfies the registered linear planar source conservation laws identically.
Separately, the quadratic radiative work ledger obeys

    Delta e+B^T j=q R_L h/2,

and the frozen source radiative channel `e_src=Phi^2/2` cancels the field gain
pointwise at onset. After the impulse the source is off and the field conserves
locally. The v83 auxiliary construction then gives `B^T p=0` exactly.

The two statements live at different perturbative orders and are not
identified. `rho=0` is the linear Hamiltonian source density of the pure
transverse TT stress. `e_src=Phi^2/2` is the second-order radiative work channel
frozen from the K1 kinetic difference. The probe does not claim that
`e_src` is the complete physical source energy or that the linear `rho` must
equal it. A nonlinear stress-energy completion is outside this probe.

A remaining review question is deliberately visible: the disappearance of the
isolated `e_src` channel after the impulse is the frozen finite-source transfer
contract, not a separately derived microscopic source evolution. The owner
condition asks for a typed emission map, source dependency, propagation and
conservation compatibility; whether it additionally requires a closed
dynamical depletion law for the complete source object is a Canon-fold review
question and is not silently decided by this probe.

[candidate-T] Spin compatibility. The source doublet has weight one and its
quadratic image weight two, so the registered rule `c(s)=1-s^2` gives

    c(1)=0,   c(2)=-3.

This is only the frozen representation/propagation compatibility. The probe
does not rederive the curved Schwarzschild endpoint.

## Falsifier ledger

```text
F1  TM4 language or masses differ from K1 law ................ no fire
F2  K1 overlaps differ from omega ............................ no fire
F3  frozen quadratic source class not one-dimensional ........ no fire
F4  source-work normalization does not fix |kappa|=1 ......... no fire
F5  wrong zero mode, static/active split or recurrence ........ no fire
F6  transverse source violates planar conservation ........... no fire
F7  local work or v83 auxiliary co-closure fails ............. no fire
F8  spin coefficients differ from 0,-3 ....................... no fire
F9  a new dimensionless source coefficient is required ....... no fire
```

## Evidence and integrity

```text
PREREG sha256    e5e75500ab88cf0e2a9e877e3134d85b832411baf2bb546a25a062cd881a5eb3
verify sha256    3e05906a2113305ae21de00c5eb306a139e913d0d6f7d6a12369feb5fbaab692
verify bytes     17699
verify git blob  6f838218ad880cda5e98839da0d20f8f2f1398ac
stdout sha256    e66a90283d718825c0aa3190cf4c7f955b1cab709dd602cac20c4f89b40e18ac
stdout bytes     558
stderr bytes     0
exact assertions 2010
local arch       x86_64
CI run           34449802081
CI x86_64 job    102782713610 PASS
CI aarch64 job   102782713864 PASS
CI aggregate     102782797989 PASS
```

The accepted exact-pinned local execution used the public pinned blob bytes and
matched `EXPECTED.txt`. The local environment could not perform a network
clone, so no fresh-local-clone claim is made. The required clean GitHub-hosted
replays now supply the cross-architecture evidence.

## Scope boundary

This probe supplies no outgoing vector dynamics, fourth-moment state
normalization, scalar comparison, numerical `r_T(k)`, detector, apparatus,
physical occurrence law, SI scale, irreversible radiation flux,
overlapping-source law, nonlinear source stress-energy completion, full FRW
reaction, full inhomogeneous GR or Stage-B pullback. It neither closes nor
changes `TT-VECTOR-STATE-NORMALIZATION`.

`TT-SOURCE [O]` remains O until a separate reviewed Canon fold decides whether
the proven typed map and source dependency satisfy its registered positive
condition. This probe itself makes no Canon, Registry, Frontier, dependency or
gate change.
