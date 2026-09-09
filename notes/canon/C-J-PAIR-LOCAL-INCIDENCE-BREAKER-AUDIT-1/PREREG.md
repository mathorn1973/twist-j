# C-J-PAIR-LOCAL-INCIDENCE-BREAKER-AUDIT-1

Local incubation audit, not a public formal probe. This is a post-exposure
audit of the user's B1-B4 and of the previously unexecuted local candidate.
Known breaker witnesses and expected values are disclosed below; no blind
prediction or independently discovered result is claimed.

1. **Equation and claim.** Freeze A=1+g^2-g^3-g^4 on Z^5 with
   g e_k=e_(k+1). Distinguish signed coefficients a, raw incoming positive
   and negative totals p,m, reduced magnitude |p-m|, and raw magnitude p+m.
   Audit |A a| not descending through |a|, q(Aa)=5q(a) on augmentation,
   raw-arrival pair totals, det(A|A4)=25, and the actual reduced-input bank.
   The universal raw positive-pair no-go compares unit inputs (+),(-),(+,-):
   nonnegative separately additive pair response cannot simultaneously have
   counts1,1,0. It is a mathematical boundary, not a physical falsification.
2. **Code.** `verify_incubation.py` is the audit. Its second code path uses
   source-column convolution and Fraction Gaussian elimination, independently
   of the frozen candidate's row-shift implementation. Only after these
   calculations does it import the exact snapshot `source/candidate_model.py`
   for comparison. No network, subprocess, external data or randomness is
   used by the audit. Snapshot and code SHA-256 values are sealed in PIN.json
   before execution.
3. **Carrier and inputs.** Five-cell exact integers/Fractions. B1 inputs
   (-3,0,-1,1,3),(-3,0,1,-1,3), plus both multiplied by5 to lie in the
   specified centered plenum lattice. Orbit seed (4,-1,-1,-1,-1), n=0..4.
   Known B2 totals212,1300,5300 versus100,500,2500. Known B3 cell1 raw terms
   (-1,-1,1,1), unsigned count16, reduced count0. B4 uses basis e_i-e_4
   and target e_0-e_4 for nonintegral inverse. No finite sample establishes
   a universal theorem; the accompanying algebraic arguments do that.
4. **Systematics.** Exact standard-library arithmetic, fixed source-column
   and cell order, no floating point, LC_ALL=C, PYTHONHASHSEED=0, TZ=UTC.
   Native Windows Python3.12 is permitted; actual platform/version are
   recorded. No claim of Linux execution or cross-architecture validation.
   Record stdout and stderr as exact bytes. Source snapshots are immutable.
   Given B1 witnesses outside the supported lattice must be reported as such;
   scale5 witnesses audit the supported case. Raw arrival counts use a newly
   reduced state at each preceding step, not the complete unreduced path tree.
5. **Failure threshold and interpretation.** Any demanded exact equality
   failing aborts with nonzero exit and is investigated without changing this
   pin. Success requires exit0, empty stderr, all asserted relations and
   the actual bank's dark cell0 count at n1. A16 output on raw mixed arrivals
   refutes the raw-arrival extension. It does not refute a bank defined only
   after signed reduction unless that frozen bank itself outputs16. A
   nonunimodular A is distinguished from failure of injectivity and from the
   bank's fixed-input involution. No output can confirm physical interference,
   apparatus realization or self-location. The printed audit success is
   operational, not candidate-T registration.
6. **Action layer.** L1 arithmetic and finite-set/code consistency only.
   Physical occurrence, cancellation mechanism, L5 stream, L6 frequency and
   individual self-location remain UNTESTED/STOP. No Canon, registry, public
   branch, claim lock, status or gate changes. The user explicitly authorized
   local incubation after a six-field preregistration and hash, correcting
   the previous blanket public-lock prerequisite.

The base public main at audit preparation is
fbf33fa1116d9e3526ac4ae057356cf2d2bddb6e. PR803 is already MERGED at
a7ef8ba676a7a26ebac4b0d5a0b31c47bc41cc9c; no current remote head matched the
coincidence/plenum/incidence branch patterns checked. No matching public issue
title for this audit name was found. This local audit name reserves no public
claim and does not take over C-J-COINCIDENCE-RECORD-1 in another project.
