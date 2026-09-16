# Sharp threshold law and fourth-moment repair

Status: COMPLETED / PASS / CONDITIONAL L1; independent proof with an exact
computational audit. This result proposes theorem-grade content for a later
reviewed Canon fold; it does not itself change any public registry status.

Owner: A. M. Thorn. Reservation: [#1024](https://github.com/mathorn1973/twist-j/issues/1024).

## Evidence and completed gates

The public preregistration pin is
`31b446a79db8747230d611f16e4d7a5b2318f30c`, a direct child of the declared
v87 baseline. The three frozen files were pushed, publicly read back byte
for byte and fetched before the first formal execution. Their hashes and
the Linux execution metadata are recorded in [RUN.md](RUN.md).

All six preregistered groups completed and passed. The verifier exited zero,
wrote no stderr and produced exactly the 286 bytes in [EXPECTED.txt](EXPECTED.txt),
SHA-256 `e9089180e6a025f911d34fc1f51924be2f759fed8ad4e3cf10791afc980444b0`.
No scientific falsifier fired. No frozen source, threshold, carrier or
equivalence relation changed after the pin. Public x86_64 and aarch64 jobs
must independently reproduce these same bytes; their status belongs to the
exact PR head and is not inferred from this local run.

## Scientific conclusion

For the explicitly fixed passive fiber, raw second-moment matrix, cold
source geometry, origin port and threshold, all admitted rational ensemble
laws have exactly the count-law family

    Pr(C=0,1,5) = (3a, 1-4a, a), rational 0 <= a <= 1/4.

Every parameter in that interval is attained by the explicit endpoint
mixtures in [PROOF.md](PROOF.md); allowing real ensemble weights gives the
corresponding real interval. Consequently the sharp ranges are
`Pr(C>0) in [1/4,1]` and `E[C] in [1,5/4]`. The identical complete passive
record and identical raw second moment do not determine this count law.
The endpoint means differ; symmetric sign mixtures also establish the
same obstruction with zero means and equal centered covariance.

Exactly one additional scalar expectation suffices and is necessary for
this context: `M4=E[z0^4]`, with `1<=M4<=4`, determines
`a=(M4-1)/12`. It is equivalently a calibrated expectation of the squared
origin deposit. This is a context-specific repair, not a universal
finite-moment reconstruction theorem.

The proof establishes the universal range, attainment and minimality;
the verifier independently audits the finite carrier, endpoint moments,
field-to-port equation, support/zero typing and reconstruction identities.
The prior exploratory exposure is explicitly disclosed in [PREREG.md](PREREG.md).

## Boundary and disposition

The ensemble law is supplied as mathematical input. No occurrence law,
empirical frequency, apparatus realization, post-state instrument or
cross-layer lift is derived. The physical QDD open obligations remain open.
The probe is complete and must not be resumed or have its identifier reused.
Its result is eligible for review as a separate L1 theorem after the
required public checks; Public Canon v87 remains the active authority.
