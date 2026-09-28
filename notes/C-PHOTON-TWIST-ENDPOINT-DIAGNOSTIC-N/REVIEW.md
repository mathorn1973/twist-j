# Pre-execution analytical and static review

**PUBLIC / NON-CANONICAL. Review of the prospective #1249 candidate.**

This is a separate review pass by an assistant agent in the same working
session, not independent confirmation by another human author. It reviews
PROOF.md, PREREG.md, sample.cpp, analyze.py and run_pilot.py before their
public execution pin. No sampler, audit, analysis or numerical fixture was
executed for this review. Compilation and Python syntax checks are not
scientific execution evidence.

## Mathematical review

The finite character expansion has the correct coefficient
2^{|P|-|supp n|} and link factor 5^{|E|}. Normalization gives the original
full ternary measure, without restricting occupied supports or signs.
The common seam residue and translation invariance identify the averaged
observable with the previously defined seam contrast in expectation.

The first derivative is i C_k on the surface side and -R_k E Y_k on the
link side. Hence C_k=i R_k E Y_k; its imaginary sign and the L^{-2}
normalization are correct. A single-face second derivative gives the
Q term with L^{-4}; the uniform-source second derivative gives G^2.
Eliminating the contact term yields

    R_k E Y_k^2 = R_k - E[(G^2+Q) cos(k theta A)].

At k=0, E(G^2+Q)<=1. Positivity of each endpoint partition sum, together
with the characteristic-function identity, gives 0<R_k<=1. These facts
imply Var(R_k Y_k)<=2. The positive two-endpoint measure has denominator
E I0=1/(1+R_k)>=1/2, signed ratio E T/E I0=-i C_k and E T^2<=1.
The two-mode Fourier identity has coefficient 5, as stated in the proof.
No lower bound on either signed contrast follows from these bounds.

## Static implementation and protocol review

- The oriented curl, six plaquettes incident to each link, seam support,
  cached flux updates and observable normalization agree with the proof.
  The heat-bath table uses evenness of W to reduce each incident factor to
  W(b_i+a). Its five conditional probabilities are the intended ones.
- Endpoint proposals are made with probability 1/2. Their score difference
  uses only the seam; the adjacent-replica exchange exponent has the
  correct sign. Exchanges move links, flux, endpoint and replica identity
  together. The exact ideal kernels preserve the stated product measure.
- Every production sweep is measured. Warmup is excluded, production
  roundtrip tracking is reset, and target endpoint changes include those
  caused by exchanges. Complete blocks and labelled roundtrips are retained.
- Sizes, modes, four initial states, seeds, temperatures, sweep counts,
  timeout limits and concurrency are fixed prospectively. The controller
  preserves process exits, stderr and raw-output hashes. Launch failures
  and timeouts are recorded; failed jobs are not resubmitted.
- The analyzer checks the execution manifest and audit result as well as
  the raw TSV records. A complete-looking TSV from a failed process cannot
  produce a usable result. It also checks frozen metadata, the exact
  temperature ladder, completion, block counts and counter totals.
- Ratio errors use the paired numerator-denominator residual. Coarsening
  stays within chains. Reported uncertainty includes the independent-chain
  residual error; agreement gates exclude that added error. All-zero
  empirical error is unresolved. The squared range is derived from signed
  intervals, and no thermodynamic or phase classifier is implemented.

The review found two pre-pin implementation gaps: the initially mandatory
endpoint proposal did not match the lazy protocol, and the initial analyzer
did not consume process-execution evidence. Both were corrected before
this review was finalized. Metadata and counter formats were reconciled
between sampler and analyzer before execution.

## Disposition and remaining review

No blocking mathematical or static protocol error remains in the reviewed
candidate. This permits freezing the prospective engineering attempt; it
does not certify finite-precision correctness, successful execution,
equilibration, independence of observations or coverage of the empirical
intervals. The written finite-volume results retain a candidate-T ceiling.
The numerical attempt has ZERO scientific evidential weight under its
preregistration and cannot close P1 or promote a Canon claim.

There is no post-run review in this file. The exact public pin, first
invocation, preserved outputs, failures and diagnostic disposition must be
recorded separately after execution. Those observations must not be used
to rewrite this preregistration or this pre-execution review.
