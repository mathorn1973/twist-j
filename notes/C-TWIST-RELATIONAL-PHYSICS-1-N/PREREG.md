# C-TWIST-RELATIONAL-PHYSICS-1-N: fixed candidate contract

**NON-CANONICAL.** One finite conditional mathematical construction and an
explicit effective physical interpretation. This is a note candidate, not a
public Canon promotion, a formal `probes/` result, or an empirical confirmation.
Author: A. M. Thorn. License: Apache-2.0.

The analytical predictions below were derived before this contract was
written. The arithmetic checks have not yet been executed. Their purpose is
verification of a known proposed identity, not a blind search or discovery of
an unexpected fit. Publish this contract, `verify.py`, and `break_check.py` in
one immutable commit and read them back before their first execution. Never
amend that pin or tune the contract to its outputs.

## 1. Equation

Fix `K=560`, `d=561`, `L=140`, and `E_ctl>0`. The complete inherited apparatus
has spectral projectors `P_s`, `s=0,...,K`, and energies
`E_s=E_ctl*(2*s+1)/d`. Its full data dimension is `657072000`. Its program
cursor has dimension `d`; it is distinct from the new reference clock.

Define

```text
H_C = (2 E_ctl/d) sum_q q |q><q|, q=0,...,K
E_star = (2K+1) E_ctl/d
V = sum_s |K-s> tensor P_s
rho_0 = |0><0|_program tensor rho_data,reference
R = (V tensor I_reference) rho_0 (V* tensor I_reference)
H_total = H_C tensor I + I tensor H_A
|t_j> = d^(-1/2) sum_q exp(-2pi i qj/d)|q>, j=0,...,K
tau_j = pi hbar j/E_ctl
```

The target is `V*V=I`, `(H_total-E_star)V=0`, uniform clock probabilities
`p(j)=1/d`, and conditional apparatus state
`exp(-i H_A tau_j/hbar) rho_0 exp(+i H_A tau_j/hbar)`, with every passive
reference retained. A passive reference has zero Hamiltonian in this energy
account. Its size need not be finite.

The full energy shell is `Q_star=VV*`. For pointer projectors `Pi_y`, `y=0,1`,
the global physical-sector effects are
`E_jy=Q_star (|t_j><t_j| tensor Pi_y) Q_star`, completed on the full carrier
by `E_out=I-Q_star`. They are positive, sum to `I` with `E_out`, and commute
with `H_total`. They give the same probabilities as the uncompressed local
effects on ideal `R`. They are generally not projectors or local operations.
The local-clock conditional state is not asserted to be the post-state of
an instrument implementing these compressed effects.

Fix the clock window `J={187,...,374}`. Write

```text
Delta = 65536(48533-10985 sqrt(5)) / [5^9(39521+154 sqrt(5))]
p_j = sin^2(pi j/561)
B_j = sum_(m=140)^560 binom(560,m) p_j^m (1-p_j)^(560-m)
epsilon = (3/16)^140
delta_joint = (Delta/561) sum_(j in J) B_j
```

The candidate predicts `Delta>1/50`, `1-B_j<epsilon<2^(-280)` on `J`,
and `delta_joint>47/14025`. The joint event includes the window and pointer
one; its probability is per prepared trial, with all other outcomes retained.

## 2. Accepted code and independent roles

`verify.py` is the builder's exact arithmetic check. `break_check.py` is an
independently written countercheck from this contract and the pinned source
contracts, without reading the builder's implementation or execution output.
Both use Python standard-library integers and rational arithmetic. No floating
point threshold, fitted interval, random seed, empirical input, or parameter
optimization is admitted. Source hashes and static inspection may be checked
before the pin; scientific assertions may not be executed before readback.

The general projector identities, arbitrary mixed/reference scope, binomial
cursor law, and measurement-effect argument are analytical proofs. The code
checks their finite arithmetic certificates and explicit counterexamples. It
does not enumerate a dense matrix of dimension `561^2 * 657072000`, prove the
inherited source circuit afresh, or supply a physical apparatus.

## 3. Carrier, inputs, and source authority

The sole canonical input is public `mathorn1973/twist-j`, main commit
`a193e389fb1ddb0bdc89165b015c95a17eb1e425`, Public Canon v106, with
`canon/CANON.md` SHA-256
`52302c640033dd15d4a7a075cad16fa48b1473b7396d1f7413536a9ec45422e7`.
The input claims are `ACTIVE-ISOSPECTRAL-RECORD [T]` and
`COMPACT-ACTIVE-RECORD-APPARATUS [T]`, at their stated conditional L1 scopes.

Complete inherited gates are specified by these files at that same commit:

- `notes/C-COMPACT-ENERGY-RECORD-N/COMPACT_MODEL.md`, Git blob
  `381f32303b8233203bec0a64521cc29e389a0776`.
- `notes/C-ORIGINAL-PORT-SOURCE-PREPARATION-N/SOURCE_CIRCUIT.md`, Git blob
  `fea890cd90c5f1d6c14e477c51509e08da2e8ffa`.

The complete carrier has two 561-level clock registers and eleven data
registers of dimensions `15,15,15,4,3,26,26,3,2,2,2`. Old memory and passive
reference correlations are retained. Fresh-write recognition restricts old
memory to `span(d_1,...,d_25)`. All helpers, setting, source, and zero pointer
are the inherited ready inputs. The 140th gate first changes the pointer.
The remaining 420 padded gates are identities.

No open PR, private snapshot, native six-pentit carrier, infinite spectral
logarithm, or other battery/source construction is an additional premise.

## 4. Systematics and predeclared error budget

Keep source setting, contact phase, controlled scalar phases, read projector,
window, sign convention, dimensions, and energy/time calibration fixed.
Finite-coordinate agreement is only for the inherited admitted source prefix.
Register locality is not locality in simulated particle coordinates.

The construction is a single joint read model. Repeated measurements,
first-passage detection, resets, indefinite records, Lorentz invariance,
proper-time comparison between paths, and gravity are outside this contract.
The original native counter `n` is not identified with `j` or with proper time.

For a separate possible implementation, let trace distances of the actual
joint preparations from `R_+` and `R_-` be at most `epsilon_+` and
`epsilon_-`. Let the implemented joint-event effect differ from the ideal
compressed event effect by operator norm at most `eta`. Then the contrast
loss is at most `epsilon_+ + epsilon_- + 2 eta`. All events, including
`E_out`, remain counted. The sufficient fixed budget
`epsilon_+=epsilon_-=eta=1/10000` therefore implies implemented probability contrast
`>47/14025-1/2500>1/400`. These are requirements, not achieved tolerances.
The inherited compact-device error budget does not certify this new stationary
preparation, the reference-clock readout, or the global measurement instrument.

## 5. Exact acceptance and failure thresholds

The following gates are frozen. A failed identity or inequality is a failure
of this candidate check; it must be reported without revising this pin.

1. All `561` energy pairs `q=560-s` sum to `1121 E_ctl/561`; energies and
   multiplicities have the stated finite positive bounds.
2. The discrete Fourier orthogonality certificate covers all residue
   differences, including non-coprime differences for composite `561`.
   Geometric cancellation, not an assumption of prime dimension, is required.
3. The phase exponent identity for all `561^2` pairs `(j,s)` agrees with the
   specified **forward** apparatus evolution, allowing one common phase.
4. The window contains exactly `188` clock values, its complement `373`,
   and its angle interval is exactly `[pi/3,2pi/3]`. The analytical sine
   bound gives `p_j>=3/4` throughout that interval.
5. Exact binomial weights sum to one, and their moments give
   `<H_A>=E_ctl`, `Var(H_A)=560 E_ctl^2/561^2`,
   `<H_C>=560 E_ctl/561`, and zero total-energy variance.
6. Exact ordered-field arithmetic or certified rational isolation proves
   `Delta>1/50`, with a positive denominator.
7. Exact integers/rationals prove
   `epsilon<2^(-280)<1/2` and
   `(188/561)(1-epsilon)Delta>47/14025`.
8. The data and two-clock dimensions match the declared factorization. The
   dimension is not called a number of sites or qubits.
9. Negative controls detect incorrect pairing `q=s`, the wrong Fourier
   sign when called forward evolution, and destruction of an off-diagonal
   coherent input when clock-apparatus energy correlations are dephased.
10. The physical-sector effect identity, positivity and completeness are
    checked as orthogonal-block algebra, with `E_out` retained. No false
    projector or post-measurement-state claim is accepted.
11. The fixed robustness budget proves the exact rational lower margin
    `47/14025-1/2500>1/400`.

Structural proofs are required alongside passing arithmetic. A code PASS
cannot discharge a missing physical premise or an inherited source assumption.
No laboratory data are used by these gates. An eventual experiment requires
its own hardware, independently characterized preparation and effects,
calibration, trial count, uncertainty model, and predeclared rejection rule.

## 6. Action layer and disposition

The new mathematical construction is conditional **L1**. The carrier,
stationary preparation, complete readout and calibration are expressly
proposed **physical postulates**, not proved lifts to L2-L6 and not changes
to the public registry. Born probabilities and outcome occurrence are adopted
as an effective interpretation. A pass means only that this specified finite
construction survived its stated exact checks and analytical review.

The scalar source contrast is inherited. The general stationary-clock method
is prior Page-Wootters/history-state mathematics. The proposed contribution
is its exact composition with this whole TWIST-J source/contact/occupied-memory
apparatus, its complete joint-event bound, and a typed physical contract.

This candidate does not derive the whole model from native `U`, select an
electron or photon, derive SI scales, supply a general-relativistic metric,
or establish a fundamental theory of nature. Such claims require new named
constructions and their own tests.
