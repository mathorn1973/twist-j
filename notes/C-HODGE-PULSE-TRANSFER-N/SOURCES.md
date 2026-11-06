# Sources, authority and custody

**NON-CANONICAL.** Only PUBLIC Canon v104 is the normative scientific basis.
The attachment and the two open draft sources below are not authority.
This publication is covered by the repository's Apache-2.0 policy.

## Verified public basis

- Repository: `mathorn1973/twist-j`, public `main`.
- Main and peeled tag `canon-v104`: `e6240e2689bb22aab5f02bad90b75d3692bb96d9`.
- Content ancestor: `4a50e527d20018839f006ed312454b710e6486b4`.
- `canon/CANON.md`: 1262204 bytes; SHA-256
  `c8d0cfadb44cf882af9f8ac303ba558b232663451d634d99467ce6d2c4a6814d`.
- All five entries of `canon/SHA256SUMS` matched. The repository Canon checker
  passed with 576 registered claims. The declared release, tag, ancestry and
  successful x86_64/aarch64/aggregate checks were verified before publication.
- `STATUS.md`, `POLICY.md`, `AGENTS.md`, `canon/CORE.md`, `canon/FRONTIER.md`
  and the relevant registry, evidence, dependency and gate entries were read.

## Exact mathematical inputs

1. [J-Hodge loxodrome preregistration](https://github.com/mathorn1973/twist-j/blob/e6240e2689bb22aab5f02bad90b75d3692bb96d9/probes/P-J-HODGE-HERM2-LOXODROME-1/PREREG.md)
   supplies the marked E_J, preserved wedge form and two characteristic factors.
   SHA-256 `fb12b0848286f9e4de6b54d4f8bcc1fc91f82e7d39aaa86dc988d7a850a9736c`.
   Its public claim is T at its registered L1 scope, not a physical identification.
2. [Trace-kernel exterior-closure preregistration](https://github.com/mathorn1973/twist-j/blob/e6240e2689bb22aab5f02bad90b75d3692bb96d9/probes/P-TRACEKERNEL-EXTERIOR-CLOSURE-1/PREREG.md),
   sections 5, 6 and 8, supplies the explicit g5, h/e/f chart, Phi and Killing=2g5.
   SHA-256 `0f295d9401c497931af591e00ccc51afecc90c819929b9ffb95ad0c6d6930952`.
   Its closure premise and all scope exclusions remain unchanged.
3. [First-order candidate in draft PR #1711](https://github.com/mathorn1973/twist-j/blob/434f8738cebb2a47dfd7ddceb8299a6e32ced858/notes/C-J-HODGE-FIRSTORDER-BRIDGE-1/CLAIM.md):
   `mathorn1973/twist-j@434f8738cebb2a47dfd7ddceb8299a6e32ced858`;
   path `notes/C-J-HODGE-FIRSTORDER-BRIDGE-1/CLAIM.md`;
   Git blob `d1d5801a1a2a12966fb808ead817353cc0bea5e1`; 6933 bytes;
   SHA-256 `0ceaa356437aadfa14125052b9e728078a721225d8fa5ef7898bb8d18da452d8`.
   This supplies candidate h_plus=3g5 with its fixed normalization, not a T input.
4. [Homogeneous capture source in handoff draft PR #33](https://github.com/mathorn1973/twistj-handoff/blob/0b9bf39b3a5866fdb34c6f37711462dc8dd08ab8/homogeneous-capture-2026-10-22/proofs/homogeneous_source.md):
   `mathorn1973/twistj-handoff@0b9bf39b3a5866fdb34c6f37711462dc8dd08ab8`;
   path `homogeneous-capture-2026-10-22/proofs/homogeneous_source.md`;
   Git blob `2405eb6674482e3cb4ec5498833537255d21ce6c`; 37570 bytes;
   SHA-256 `3e8832f435caeddcbbca34ace5e63c366ea86fa5210007c10cfd77f5859b6e30`.
   Equation (3) supplies Q and E(k); equation (9) supplies the new capture
   rotation. Its receiver and energy qualifications are not altered here.
   This note consumes the displayed mathematical definitions, not a purported
   canonical or independently certified capture theorem.

Both draft heads were re-read and unchanged during intake. No scripts or
private infrastructure data were copied from the handoff repository.

## Incoming local comparison

Input: `C-HODGE-PULSE-TRANSFER-N.zip`, 10689 bytes, SHA-256
`f08a16bed821ce9d5e1526227b2fbd61c8fb8af92283cadf61cd30665a31f38e`.

The archive was treated as untrusted data: entries were checked against absolute
paths, path traversal, symlinks and oversized members; extraction used a fresh
directory. All eight source manifest entries matched. Both programs were read
in full before being run with an isolated working directory. They make no
network call, subprocess call or file mutation. SymPy is an explicit dependency
of the transfer audit, not vendored code or a hidden formal-probe dependency.

The four code/output files are copied byte-for-byte from that archive. Source
`CONTRACT.md` and its later `TRACE-ADDENDUM.md` disclosed result exposure; their
historical local-only/no-write boundary was superseded only for publication by
the user's explicit note request. They were not public preregistrations.
The present README reformulates the comparison, specifies the alternative
signed regrouping, and explicitly separates Hermitian congruence from the
residual adjoint action. No frozen formal gate is altered.

## Collision and public-safety review

All 277 remote heads were enumerated with `git ls-remote --heads origin`.
Exact candidate/branch searches and the current registry/tree showed no
collision. Broader pulse/transfer/Hodge matches #832, #898, #1033, #1421 and
#1628 were read and have distinct carrier or apparatus scopes. The publication
is reserved by #1712 and does not claim either source branch.

Only the named new note files are staged. No credentials, private addresses,
private machine names, external code payloads, binary archive, generated
bytecode, historical failed-run logs or files over the policy size limit are
included. The original result-exposed provenance is retained without claiming
blind independence, formal preregistration or Canon promotion.
