# P-J-FUNDED-PAIR-NETWORK-1

PUBLIC / NON-CANONICAL / L1. Owner: A. M. Thorn, funded-network session.
Reservation: https://github.com/mathorn1973/twist-j/issues/1969.
Basis: ACTIVE Public Canon v110, main 629a9d4058501f938dc91a690c3eb59a914493d1,
content c8197bcc807de1f62248463aec77f7ac7ab46f85.

## Question and authority boundary

Can the supplied partner-funded four-slot J involution be composed into an
uninterrupted conservative network with actual transport and fixed receiver
reading? Distinguish a recurring readable signal from a permanent archive,
and transport of relative account from transport of source phase.

Issue #1968 owns the primitive. Its definition is restated self-contained;
only the network, exact code factor, no-export boundary and re-pairing
continuation are claimed here. No imports or runtime dependence on that
unmerged probe. The earlier C-J-FUNDED-PAIR-EXCHANGE-N attachment is a
noncanonical reference. No Canon, registry, gate, workflow or old probe edits.

## Frozen laws, carriers and preparations

O=Z[j], 1+j+j^2+j^3+j^4=0, rho=j^2, J=1+j^2, Jinv=-j-j^2,
h(z)=z conjugate(z), g=h(J)=2-phi. The full account is H=sum h(z_i),
E=Tr(H)/2, S=sum z_i. All raw cell coordinates are integers.

For four ordered cells (x,y,p,r), reject identically unless x-y,p-r are in
2O. Otherwise put c=(x+y)/2,d=(p+r)/2,u=(x-y)/2,v=(p-r)/2.
Fix c,d. On u!=0 and h(v)=g h(u), send (u,v) to (Ju,Jinv v).
On v!=0 and h(u)=g h(v), send (u,v) to (Jinv u,Jv). Else use identity.
Call the complete gate B. The two nonzero branches must be disjoint.

Fixed-site network: m even, m>=4, 2m raw cells, site i=(z_(2i),z_(2i+1)).
K0 simultaneously applies B to site pairs (0,1),(2,3),...; K1 to
(1,2),(3,4),...,(m-1,0). One complete tick is T=K1 K0. The state is the
raw array alone. Geometry, permanent site pairing and two-layer order are
supplied. There is no counter, driver word, output feedback or post-start
reset. Full inverse T^-1=K0 K1 is predicted.

Binary code: arbitrary fixed integral centers c_i, common nonzero integer a,
fixed epsilon_i in {-1,+1}, r_i mod5, occupation eta_i in {0,1};
site i=(c_i+u_i,c_i-u_i), u_i=a epsilon_i rho^r_i J^eta_i.
Predicted gate action swaps occupations, not the local phase labels.
At full ticks eta_i(t)=eta_(i-2t)(0) for even i and eta_(i+2t)(0) for odd i.
Indices are modulo m. Hence T^(m/2)=I on this code.

Remote two-message family: m=4d, d>=1, centers0, a=1, all phase labels1.
The sole high occupation is at site0 for message+1, site1 for message-1.
Only source sites0,1 depend on the message. All other sites are the same
occupied background (1,-1). The fixed reader is
R=(E_site(2d)-E_site(2d+1))/2: tag NO_EXCESS if R=0, otherwise VALUE(R).
Equality is exact rational/tag equality. It predicts VALUE(message) exactly
at t=d modulo 2d, otherwise NO_EXCESS. E=16d+2. Reading is after a COMPLETE
two-layer tick; it is not claimed stable during the intermediate layer.
This is deliberately a different encoding from an unknown sign at one site.

Re-pairing control: four raw cells, B0=B_(01|23), B1=B_(12|30), T4=B1 B0.
W=Jrho; A_a=(2a,0,W,-W), a in {-1,+1}; the payer is common to both inputs.
Predicted exact cycles are
A_+ -> (2,-W,W,0) -> (1+J,1-J,rho,-rho) -> A_+,
A_- -> (-1-J,J-1,rho,-rho) -> A_-.
H=8-2phi, E=14. The receiver is raw cell1, literally zero initially.
Its total reader is BLANK at zero, otherwise VALUE(sign(Tr(cell1))).
A nonzero zero-trace cell is VALUE(0), not BLANK. On both cycles every
nonblank reading must equal a, including the intermediate layers. The
positive record has two consecutive readable full boundaries, the negative
one; later erasure and recurrence are mandatory, not discarded outcomes.

## Proof obligations and negative controls

Prove the complete gate inverse and conservation, full-network inverse,
finite-shell recurrence, binary factor and complete message continuation.
For fixed site pairing, prove independent local sign covariance, fixed
centers and relative J-orbits, and the permutation of relative Hermitian
accounts. This implies no source-sign export to other sites and no excitation
of an equal-cell site. It is not a theorem for changing constituent pairs.
For parity-admitted fixed sites, prove the full orbit bound m! divided by
multiplicities of repeated initial relative accounts. These are analytical
claims, not deductions from the size of a tested sample.

The four-cell re-pairing example must both defeat that broader, unclaimed
no-export extension at its first payer read and retain the exact small cycles.
Neither example may be called indefinite fresh renewal, stored history,
positive entropy, a native-U realization, radiation, gravity or Born occurrence.

## Exact finite audit inventory

The accepted verifier specifies all loop orders and hashes compact JSON
rows with ASCII encoding and one LF. It prints one sorted-key compact JSON
report and one LF, no file output, randomness, network or subprocesses.
All counts refer to executed cases and may have overlaps.

1. All 9^4=6561 ordered raw four-cell inputs from
   [0,1,-1,j,-j,J,-J,Jinv,-Jinv]. Compare two arithmetic encodings,
   involution, pair sums, full H/E, and sign covariance of both sites.
2. All 7^4=2401 four-site arrays from the ordered six pairs
   (c+u,c-u), c in [0,1], u in [0,1,J], followed by (0,1).
   Test both arithmetic updates, full inverse, accounts, marked pair sums,
   four separate sign flips and every equal-cell-site control.
3. Every binary word for m=4,6,8,10, followed for m/2 ticks, including
   complete return. 1360 starts, 6368 updates. Compare actual raw arrays
   to the direct shift formula and both arithmetic implementations.
4. Every binary word for m=8 and a in [-3,-1,1,3], with centers c_i=i mod3-1,
   epsilon_i=(-1)^i, r_i=i mod5, followed for four ticks. 1024 starts,
   4096 updates. Check local labels stay at their original addresses.
5. Both remote messages for every d=1..8, t=0..4d inclusive: 304 complete
   boundaries and 288 backward steps. Check every raw coordinate, reader,
   constant account and complete return at 2d and 4d.
6. The ORIGINAL unknown-sign family (2a,0,W,-W,0^12), a=+/-1, in the
   fixed-site network for t=0..32: 66 boundaries. All nonsource coordinates
   must be identical between signs; all sites beyond the first payer remain
   literally zero. This negative control is not replaced by the code family.
7. Both four-cell re-pairing inputs for t=0..12: 26 full boundaries and
   24 backward steps, exact cycle states and receiver tags. Compare both
   arithmetic updates and all intermediate-layer sign readings.

The two coefficient-arithmetic implementations are written by ONE author.
They share gate logic; their agreement is not blind independent confirmation.
The separate closed-form shift and cycle comparisons audit that shared logic.

## Freeze, execution, failures and status

PREREG.md, PROOF.md and verify.py are the complete scientific source set.
Publish and read back the source pin and hashes BEFORE any import or scientific
execution. Static parsing and source review are permitted beforehand.
No scientific dry run has occurred. Do not modify frozen scientific sources.
Run with assertions enabled under the unchanged repository policy and verifier
runner. Record the first exact stdout, empty stderr requirement, full source
hashes and neutral platform metadata in EXPECTED.txt and RUN.md.

Tolerance is zero. Any missing case, state, inverse, invariant, factor, reader,
cycle or arithmetic-encoding mismatch defeats its claim. Do not remove cases,
move a threshold or silently change a carrier. Nonzero exit, stderr or timeout
is not a pass; follow the repository's unchanged disposition procedure.
Record actual architecture receipts only after they exist. No current source
has been independently authored or reviewed by another agent in this session.
Construction candidate-D, conditional analytic statements candidate-T,
finite audit candidate-C; all remain NON-CANONICAL pending a separate fold.
