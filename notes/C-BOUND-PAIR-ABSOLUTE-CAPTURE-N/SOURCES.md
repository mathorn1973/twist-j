# Sources and authority for the absolute capture calculation

**NON-CANONICAL / L1. Prospective source custody.**

Author: A. M. Thorn <thorn@twistj.com>.
SPDX-License-Identifier: Apache-2.0.
Reservation: [#1814](https://github.com/mathorn1973/twist-j/issues/1814).
Owner: the single continuing session recorded in that reservation.

This source inventory and the three executable digests in `PREREG.md`
are finalized for the prospective public pin. Nothing in this file records
a completed scientific execution.

## 1. Public authority

The source authority is ACTIVE Public Canon v106 on
`mathorn1973/twist-j`, with this fixed tuple:

```text
main / peeled canon-v106: a193e389fb1ddb0bdc89165b015c95a17eb1e425
content commit:           9242db4f040d67d9417eacd06612230b74248cff
main Git tree:            bd7a34b48355dab457ecd7f0884edc089c3eebea
canon/CANON.md bytes:     1370107
canon/CANON.md SHA-256:   52302c640033dd15d4a7a075cad16fa48b1473b7396d1f7413536a9ec45422e7
```

`STATUS.md`, `POLICY.md`, `AGENTS.md`, `canon/CORE.md` and
`canon/FRONTIER.md` determine authority and scope. The controlling policy
blobs are `10b49a9551eb2f2a3e32d65b0d5b7206febe9de9` for `POLICY.md`
and `a449c8036ccbc40240060c885bb936630d4fc680` for `AGENTS.md`.

The root session owns the current authority, normative-hash and collision
readbacks. The readbacks already inspected for this unchanged tuple include
successful main x86_64/aarch64/check run `40556926452` and successful full
tag activation readback `40557096572`. Those checks concern the inherited
authority, not this new calculation. They are not independent acceptance
of the new scalar reductions or interval certificate. No completed GitHub
Release asset readback is asserted here.

## 2. Inherited canonical model and proof sources

All paths in this table refer to the fixed v106 commit above. Byte counts
and SHA-256 values were checked against the actual local source copies.
The current-record interface proof and package README, initially absent
locally, were fetched as exact base64 file contents at the fixed commit,
decoded and hashed. These checks agree with the custody entries carried
in the pinned PR1813 `SOURCES.md`. Source custody is not independent
scientific confirmation.

| Path | Bytes | SHA-256 | Role |
|---|---:|---|---|
| `canon/CORE.md` | 42836 | `a16583a85e3bece4117df6cfed13c1717fe79ffe56935f10ca9f371243371834` | Orientation and exact registered scope |
| `canon/REGISTRY.tsv` | 572480 | `705423faa1c7b8676d90362d6c5c5cb56f0b58ab21db65155c0054239a965e68` | Status and claim scope |
| `canon/FRONTIER.md` | 27382 | `8574c3d4b0cc70278dec7d64e2a51022718cc54497c64025d9e6021775fcbaf0` | Unchanged live obligations |
| `notes/C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N/PROOF_CAPTURE_SCATTERING.md` | 41783 | `62b6e848de6de50534c1edfbec086551f67576708bc8b117f7dee2928fd2d997` | Full law, arrangements, complete port functions and scattering normalization |
| `notes/C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N/PROOF_PACKET_CERTIFICATE.md` | 18606 | `80573da4664db680c0e03a7f9b6ac2348c6743666a7703ea9ebe92b0ddd6ba46` | Original normalized source, selected output root, windows and positive lower bound |
| `notes/C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N/PROOF_CURRENT_RECORD_INTERFACE.md` | 30031 | `705bc93a6293bc1a7b84c913d86c48cd294d4ca7c8c466e20aa873c980e0621c` | Joint record event and retained memory/reference scope |
| `notes/C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N/README.md` | 23159 | `ff4406dde2ab8d4c614b1ef14aa1ef139000f99e4b9741bbda3856e635a89056` | Source-package contract and boundaries |

Canonical premises are used only at the scopes of
`CONTACT-W-BOUND-PAIR-RESPONSE` and
`HOMOGENEOUS-CAPTURE-CURRENT-RECORD`. A historical NON-CANONICAL heading
on a retained source package is not a new promotion of every statement in
that package. The Canon and registry identify the adopted premises.

## 3. Pinned conditional predecessor

The sole profile predecessor is [PR1813](https://github.com/mathorn1973/twist-j/pull/1813)
at **`8298af04f7385ec24f61a1b7c84d861cae017529`**. It is an open,
unmerged NON-CANONICAL L1 proposal. Its relative-profile reproduction and
same-session checks do not make its new analytical statements canonical.

| Predecessor path | Bytes | SHA-256 | Use |
|---|---:|---|---|
| `notes/C-BOUND-PAIR-CAPTURE-MOMENTUM-N/PROOF_CAPTURE_PROFILE.md` | 12556 | `855c20e2878ceeb5df87abe468f6925ef0302645fc11b44eb2f9db48bfbb45f5` | CP-9, CP-11--14 and CP-24: density, normalized source, full probability and finite input width |
| `notes/C-BOUND-PAIR-CAPTURE-MOMENTUM-N/ABSOLUTE_BOUND.md` | 4650 | `141d438f2e59d9bacb1d50e35cb988eff30b4789261376276b1224fed19a21d8` | Complete-denominator identity and conservative full-event upper bound |
| `notes/C-BOUND-PAIR-CAPTURE-MOMENTUM-N/SOURCES.md` | 3679 | `852772da8d4fef61ed2a902080d80adfaf5b1d2e39ad2ce162ad41acd96e4b06` | Predecessor custody and inherited scope |

These byte counts and SHA-256 values were also checked against the local
copies of the exact pinned predecessor files.

The post-run absolute-bound addendum is used as a separately labeled
conditional analytical premise. It was not part of the predecessor's
prospective relative-profile finite audit. The predecessor's `verify.py`
is not imported or executed and its 86 checks are not counted as new
absolute-probability evidence.

## 4. New package custody

Only the following reserved areas belong to this continuation:

```text
notes/C-BOUND-PAIR-ABSOLUTE-CAPTURE-N/
probes/P-BOUND-PAIR-ABSOLUTE-CAPTURE-1/
branch: probe/P-BOUND-PAIR-ABSOLUTE-CAPTURE-1
```

The complete executable inventory consists of exactly these three files.
Their final digests are recorded in the input table in `PREREG.md` and
checked in the public pin readback.

| New executable input | Final repository path |
|---|---|
| Sole scientific entry point | `probes/P-BOUND-PAIR-ABSOLUTE-CAPTURE-1/verify.py` |
| Outward fixed-point arithmetic and derivatives | `probes/P-BOUND-PAIR-ABSOLUTE-CAPTURE-1/interval_core.py` |
| Complete scalar boundary model | `probes/P-BOUND-PAIR-ABSOLUTE-CAPTURE-1/model.py` |

Runtime fixtures: **NONE**. External constant tables: **NONE**.
There are no unlisted runtime helpers, ambient workspace inputs, network
fetches, downloaded predecessor code or writable external caches.

The sole final analytical note is
`notes/C-BOUND-PAIR-ABSOLUTE-CAPTURE-N/PROOF.md`. It contains the scalar
reductions, physical-sheet convention, complete boundary accounting and
the range-enclosure argument used by the executable. The broader
analytical discussion does not introduce additional executable branches:
this probe uses one uniform external K,E box, with no outer partition
or excision.

That proof, this `SOURCES.md` and
`probes/P-BOUND-PAIR-ABSOLUTE-CAPTURE-1/PREREG.md` belong to the same public
pin as the three executable files. The root records their exact byte
counts and SHA-256 values in the public pin readback and subsequent
custody manifest. No document contains its own hash, and no circular
self-referential hash requirement is imposed.

## 5. Interpretation and independence

This work asks for a certified absolute interval for the original
asymptotic joint event, on its original normalized incoming state. It
does not change the source, condition the token on the outgoing momentum
window, replace the complete denominator by selected channels, or change
the bound/pulse/record projector. It is not an absolute rate, a plane-wave
cross section, a finite-time detector result or a particle identification.

The new derivations and the verifier receive component-separated static
crosschecks inside one continuing assistant session. These are authoring
checks, not external independent theorem acceptance or a blind test.
Later byte-identical x86_64/aarch64 replay would establish the repository's
computational reproducibility condition only. No Canon, registry,
frontier, gate, workflow, predecessor probe or physical occurrence claim
is changed by this package.

All newly authored text and code use Apache-2.0. No third-party numerical
implementation, fitted target, private infrastructure detail, credential
or external experimental dataset is introduced.
