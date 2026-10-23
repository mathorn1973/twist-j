# Execution Record: `C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N`

**Status:** `NON-CANONICAL` (Research-Note & First-Principles Reproduction Execution Record)  
**Claim ID:** `C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N`  
**Base Commit (`main`):** `e6240e2689bb22aab5f02bad90b75d3692bb96d9`  
**Prospective Source Pin Commit:** `fd710dbc6ca5023dba89c26de7421a6bbd9c01b5`

---

## 1. Prospective Source Pin Discipline

In accordance with `notes/C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N/PREREG.md` (§5), all pre-execution specification, proof, claim-table, provenance, and verifier source files were committed and pushed to `origin/codex/c-homogeneous-capture-current-record-n` at commit `fd710dbc6ca5023dba89c26de7421a6bbd9c01b5` (`git ls-remote origin refs/heads/codex/c-homogeneous-capture-current-record-n`), and read back before executing the formal verification run that populated `reproduce/C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N/EXPECTED.txt`, this `RUN.md`, and `notes/C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N/RESULT.md`.

None of the prospectively pinned specification, proof, or verifier source files were modified after `fd710dbc6ca5023dba89c26de7421a6bbd9c01b5`.

---

## 2. Pinned Execution Metadata

| Field | Value |
|---|---|
| Command | `python reproduce/C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N/verify.py` |
| Environment | `LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC` |
| Start timestamp (UTC) | `2026-10-23T17:12:49Z` |
| End timestamp (UTC) | `2026-10-23T17:12:49Z` |
| Wall-clock elapsed time | `0.6277 s` |
| Python runtime | `Python 3.12.10` |
| Exit code | `0` |
| Standard error (`stderr`) | `0` bytes |
| Standard output (`EXPECTED.txt`) | `708` bytes (`8` lines, LF line endings) |
| `EXPECTED.txt` SHA-256 | `1c0d4c4459a4ae52a74adf6d1206ff4eb91a9042f200708c5a8d06aeb831a43b` |

---

## 3. Exact Frozen Output (`EXPECTED.txt`)

```text
PASS GROUP 1 BRANCH_GAP: 24 checks; gap>=13/165; L<=165/13
PASS GROUP 2 PACKET_CERTIFICATE: 44 checks; B_hom>=903570708e-33>8e-25; P_joint>=287615489e-36>2e-28
PASS GROUP 3 NATIVE_COMPLETION: 27 checks; 2704 contact states; 1352 receiver-edge states
PASS GROUP 4 CURRENT_INTERFACE: 12 checks; cut l=99; j_coh=1642/625
PASS GROUP 5 OPEN_CHANNEL_AND_CARRIER: 16 checks; nu_1=4/5; dark_diff=4*sqrt(2)/5
PASS GROUP 6 FINITE_STRIP: 18 checks (16 Laurent identity groups + 2 negative controls)
SCOPE: connected asymptotic capture, full current, and coherent record; p(Q_full)>=p(Q_win)>2/10^28; finite-time preparation and occurrence NOT DERIVED
VERIFY PASS C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N total_checks=141
```

---

## 4. File Inventory and SHA-256 Verification Against Prospective Pin

All prospectively pinned files retain their exact byte lengths and SHA-256 digests from commit `fd710dbc6ca5023dba89c26de7421a6bbd9c01b5`:

| Repository Path | Role | Bytes | SHA-256 | Matches Pin `fd710dbc` |
|---|---|---:|---|---|
| `notes/C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N/README.md` | Package overview & theorem statement | `16099` | `3a6b9b14f907a07d58cf1d18bc10b91f42013e5f3e906aef0ad824d409b4c672` | Yes |
| `notes/C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N/PREREG.md` | Frozen preregistered test plan | `14192` | `22e9ba131f53121782f46020525f27bc2d42b861b0ec98e40a75e07b9c7ba141` | Yes |
| `notes/C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N/PROOF_CAPTURE_SCATTERING.md` | Capture, scattering & finite-strip proofs | `22461` | `0ca5c53716136c7b48b15c415001ef49d75303fc52f01756deda50258a32a21c` | Yes |
| `notes/C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N/PROOF_PACKET_CERTIFICATE.md` | First-principles packet certificate & soundness | `17111` | `3e648bf351ba7f30fd091c4a91508fa5ff623292403ce52beee66a0f198e4f6a` | Yes |
| `notes/C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N/PROOF_CURRENT_RECORD_INTERFACE.md` | Native completion, current & effect pullback proofs | `19255` | `3936d9c836c2a157c8f783511021cca5daaa2c124b1a6187930a0bd2835cb73c` | Yes |
| `notes/C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N/CLAIMS_AND_DISPOSITIONS.md` | Claim matrix, dispositions & scope fences | `13942` | `feab9ba1126ea349eea162bd6ebff617ddf68451096de1563a359db4442a9cf3` | Yes |
| `notes/C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N/CLAIMS.tsv` | Machine-readable claim ledger | `5012` | `87a9285427b0d51487ac84db521d9422271b98119b422a969921f5c607297959` | Yes |
| `notes/C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N/SOURCES.md` | Self-contained provenance & audit receipt | `12132` | `2d47892da0c92c78557badf653a55783a63f1aeeac984769c97bfd6d5c6e7b08` | Yes |
| `reproduce/C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N/README.md` | Reproduction harness instructions | `5957` | `a56b6388e78d5807b9447dcd529a1d7734ccd1486bcc5f1f7120909bd27de6d9` | Yes |
| `reproduce/C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N/verify.py` | Standard-library first-principles verifier | `56167` | `4a5bb106f680527a77093c5596463e18a1becf6ff7cf8e58364c86e96141370c` | Yes |
| `reproduce/C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N/EXPECTED.txt` | Frozen post-execution standard output | `708` | `1c0d4c4459a4ae52a74adf6d1206ff4eb91a9042f200708c5a8d06aeb831a43b` | Populated from pinned run |
