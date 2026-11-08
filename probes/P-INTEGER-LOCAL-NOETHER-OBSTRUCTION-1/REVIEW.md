# Review and custody

Scope: NON-CANONICAL, NEW_DECLARED L1.

The two programs were written by separate agents from the textual contract.
Neither author read the other implementation or previous probe programs.
The breaker uses different differentiation and linear-system algorithms.
This is implementation independence within one coordinated work session,
not a claim of blind external peer review.

A third agent wrote the proof, and another independently read the full
proof and contract. The coordinator read both finished programs and checked
their correspondence to the equations. Static review caught the preliminary
audit-count transcription error before the pin; the declared horizons and
indices were preserved, with corrected counts 22/1200/244/222. The correction
was publicly recorded on issue #1661 before execution. Endpoint quantifiers,
the finite definedness of delta2 and the free common tail constant were
made explicit before the pin as well.

Only source inspection, AST parsing and byte hashing preceded the public
pin. No scientific code was imported, run or fixture-evaluated. The pinned
proof retains two Markdown hard-break spaces on its status lines; a generic
whitespace check reports those as trailing spaces. They have no scientific
or executable effect and were preserved with the rest of the pin.

The six-file pin is `6c257b169054625aa608974c1c6a264fb56e5d02`.
Every file was fetched from that public commit and compared byte for byte,
by Git blob identifier and SHA-256, before the public receipt
https://github.com/mathorn1973/twist-j/issues/1661#issuecomment-6279453073.
The first formal run then completed with exact primary/breaker certificate
identity, exit zero and empty stderr. No frozen file changed afterward.

The local Git transport lacked write authentication. An isolated repository
on an available connected host received a Git bundle and pushed the exact
commit object through the repository's existing access. Both author and
committer remain A. M. Thorn <thorn@twistj.com>. No credential, private
address, hostname, machine nickname or remote execution log is included in
the probe. No existing remote checkout or concurrent branch was changed.

Security review: only the named probe directory changes; Python uses the
standard library; authority files are read only; no network, secret access,
dynamic code evaluation or downloaded code appears in either verifier.
The only subprocess executes the separately frozen breaker with isolation,
captured bytes and a fixed timeout. All files are text below the policy size
limit. The result contains no observational data or fitted parameter.

The required PR jobs must replay the unchanged verifier on x86_64 and
aarch64 at the exact result head. Their public job logs and aggregate check
are the architecture evidence; a local pass alone is not described as a
completed two-architecture gate. The analytical claim remains conditional
candidate-T pending repository review and does not change Canon status.
