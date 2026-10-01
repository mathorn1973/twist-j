# Finite-chain first delivery: analytical follow-up scope

NON-CANONICAL / candidate-T by conditional proof / L1. Authority: none.
Public authority remains Public Canon v95.

This is a separate local analytical follow-up to PR #1310 at
`dd354e3e01ad7f7bb535f33e012c5ef1b46a87d2`. The user supplied the induction,
contact formula, times N-1 and N, energy41 and all-cut argument before this
work. They are known candidate mathematics, not blind predictions. Review
seeks a counterexample or an omitted full-state/edge condition. The law and
the predecessor's frozen files are unchanged. This note does not expand the
earned scope of #1310 retroactively.

## Exact question

For every fixed finite integer N>=2 and every w in Z^4 with H(w)=1, use
exactly #1310's G; A; B; F schedule. Initially the source is (R,0,PLw,0),
every intermediate cell is (ZM,0,0,0), the target is (R,0,0,0), and all
channels are zero. Decide the first boundary delivery and first target
reaction, give every stored coordinate through boundary N, and account for
energy41 and 32N-1 coordinates. For every cut j=0..N-2, replace BOTH
contacts A_j,B_j by identity, retaining q_j, and decide whether the complete
downstream prepared component stays fixed for all time.

The proof covers all N and w. The finite audit below checks the exposed
formula against actual full-state evolution; it is neither an all-N
exhaustion nor a substitute for induction. A single mismatch fails the audit.
No fitted tolerance, random search, experiment, period search, persistent
record, charge transport, infinite network or physical speed is included.

## Bounded local validation plan (fixed before execution)

`audit.py` uses generic-N simultaneous layers over nested cell tuples, with
the predecessor's hash-guarded `verify.py` local gates. Separately authored
`audit_challenger.py` uses flat 32N-1 coordinates and the predecessor's
hash-guarded `break.py` scalar local gates. Both predecessors are exposed;
these adapters do not claim new clean-room implementation independence.
The predecessor main routines and its 6120-state run are not invoked.

1. Check inherited exact field certificates. Enumerate every integer H(w)=1
   seed in a proved finite containing box and compare both energy formulas.
   With w=(a,b,c,d), positivity gives

   4H(w)=||C(2a+c,2b+d)||^2+c^2+(c+d)^2.

   Hence |c|<=2, |c+d|<=2, |d|<=4, |2a+c|<=2 and |2b+d|<=2,
   so |a|<=2 and |b|<=3. Enumerate the full box
   [-2,2] x [-3,3] x [-2,2] x [-4,4], retaining exactly H=1.
   The number of retained seeds is not assumed. The theorem itself does not
   rely on their enumeration.
2. For N in {2,...,16,31,32,33,64}, run each retained seed from k=0 to N.
   Compare every literal coordinate with the closed formula, both adapters
   with each other, every layer's full energy, node charges, Gauss defects,
   spectator registers and reacting-vector sums, and both inverse identities.
   Derive first times from the actual target state, then compare to N-1,N.
3. For w=(0,0,1,0), N in {2,...,16,32}, every single cut j, and k=0..N+2,
   check both implementations, retained cut content, inverse identities and
   the full fixed downstream component at each layer. This bounded run
   audits the invariant proof; all-time invariance follows from the proof.
4. For every N=2..64, use distinct symbolic resource labels to check the
   contact permutation and its inverse, and occupied nonnegative integer
   resources to check both actual implementations, with every single cut.
   Check cut-channel retention. This catches overwriting and parsing of
   multi-digit cell indices. It checks a general linear coordinate map at
   each audited N, not just a travelling two-unit preparation.

This is local validation of an analytical notes candidate, not a formal
public probe or a public computation gate. No new public preregistration,
issue, push, PR, architecture receipt or promotion is claimed. A later formal
public lane must use its own public reservation, immutable source pin and
required checks before formal execution. The local report records actual
source hashes, command, environment, counts and outcome without borrowing
the predecessor's x86_64/aarch64 results.

## Source custody

The starting checkout is the exact #1310 head above. Fresh public main is
`b8ba1a07ad776cdd8d878fe0a407e07312c0e263`; canon-v95 peels to that commit,
and declared content `5a1dd8ba6c339640940b5a013d3c412025a1f8fc` is its
ancestor. Local Canon bytes match STATUS: 848893 bytes, SHA-256
`b4ebf2ffc7393b703d65ce62cf3e0ee382e7309a563d99ec866ee3fa82f9ba7f`.
The actual public main architecture jobs and aggregate at run36766242516
are successful. Public STATUS was also read through the GitHub connector.
Remote heads and related open issues were checked before creating the local
branch. This records authority context, not a new public claim reservation.

The required pinned local arithmetic files have SHA-256:

- `../C-FIELD-THREE-CELL-DELAYED-TRANSFER-N/verify.py`:
  `42ec10cd001028ec126045647eea89347ec12bbf3612c40e1aa204ab77913a59`.
- `../C-FIELD-THREE-CELL-DELAYED-TRANSFER-N/break.py`:
  `fc435a7efffea8edd4bd8e11aa12e16c2d1489a39c74997ae0b204837b7445b1`.

No Canon, registry, workflow, predecessor evidence or local reaction rule is
edited by this follow-up. Changing N changes the finite architecture's stored
dimension even though the local law, per-step depth and preparation energy
remain the same.
