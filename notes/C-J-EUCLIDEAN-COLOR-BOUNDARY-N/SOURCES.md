# Sources and authority

Status: NON-CANONICAL source manifest. No third-party proof or source code
is copied into this note. All proofs and Python audit code here are original
to this session and use only the standard library.

## Public TWIST-J basis

Repository: https://github.com/mathorn1973/twist-j
Branch snapshot: c164b79ce134152ac7cd600421791df74113f29f.
Release: Public Canon v100, tag canon-v100.
Content commit: a4cc9666662967527abe711441833ff600c00337.
Activation/tag target: 807dae3fe97dd6a872d5d1305a0133e8e8d856ea.

The live GitHub connector was used to read STATUS.md, POLICY.md, AGENTS.md,
CORE.md and FRONTIER.md. A fetched Git checkout then confirmed tag/content
ancestry, all five normative SHA-256 sums, and the repository policy, Canon,
ledger and gate checks. The public main workflow 37855930685 had successful
architecture-x86_64, architecture-aarch64 and aggregate check jobs. Those
checks concern the existing main, not the new mathematics in this note.

Normative SHA-256 values at that basis:

```text
5e4de2da8d57ff2f7e4b873e6236b0695677e20d173d894ee70562c1389648c4  canon/CANON.md
b36f0933095603aa07dd7d08e76271464ea49de02a2297f9a41daf10754d9697  canon/CORE.md
8574c3d4b0cc70278dec7d64e2a51022718cc54497c64025d9e6021775fcbaf0  canon/FRONTIER.md
8f79dab86e4d77b4505c2d1011f2f8702d4ede937250cd5953718e671e7b910b  canon/REGISTRY.tsv
d1bba0d273966e347e11b02983f4ea9e8a38bfc5bbb9d5d01d95970ea278fe1d  canon/CHANGELOG.md
```

No attached internal Canon or project snapshot is used as authority.

## External E6 statement

OpenAI, The Euclidean plane is not five-colorable, September 23, 2026.
Repository source snapshot: fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb.

Manuscript supplied by the author:
https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Euclidean-plane-is-not-five-colorable-September-23-2026/paper.pdf

Formalization scope:
https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/158.md

Actual solution module:
https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/Geometry/PlaneColoring/Five.lean
Git blob: 377372bb81c65d351df698936319b809ca2682be.
Declaration: OAI.EuclideanFiveColor.no_proper_five_coloring.

Comparator configuration:
https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/ComparatorChallenges/EuclideanFiveColor.json
Git blob: deeb7e0e6185d8e44bc8803774270ed1eca83958.
It identifies the solution module and the permitted axioms propext,
Quot.sound and Classical.choice. The challenge .lean file itself has a
placeholder, so it is not evidence of a completed proof build.

The consulted scope and theorem statement concern arbitrary five-colorings
of C with distinct colors at every pair of norm-distance one. This note
uses precisely that statement as hypothesis E6 for one corollary. It does
not claim a fresh Lean build, a complete audit of the external proof, or an
explicit six-chromatic finite graph extracted from the PDF. Source text
and formalization metadata were used; the PDF was not independently audited
in this session. No empirical inference depends on E6 here.
