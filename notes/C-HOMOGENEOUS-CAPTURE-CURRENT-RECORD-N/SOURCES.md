# Immutable Sources, Custody Receipt, and License/Security Review

**PUBLIC, NON-CANONICAL. Source provenance and custody manifest (`SOURCES.md`) for `C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N`.**

Owner: A. M. Thorn. License: Apache-2.0.

---

## 1. Public Authority Basis

The active public authority is `mathorn1973/twist-j` `main` at commit `e6240e2689bb22aab5f02bad90b75d3692bb96d9` (`Public Canon v104`, annotated tag `canon-v104` object `b3eb6210f9c89abf0a4c5fa77294b548f78a23ed`, content commit `4a50e527d20018839f006ed312454b710e6486b4`).

| Authority File | Bytes | Git Blob SHA-1 | SHA-256 |
|---|---:|---|---|
| `canon/CANON.md` | 1262204 | `f24448eceeda3f56db504313dbda4c3f59ae89f6` | `c8d0cfadb44cf882af9f8ac303ba558b232663451d634d99467ce6d2c4a6814d` |
| `STATUS.md` | 2391 | `75227ff5535f7c7ae33c5fd265f1a79641e6015d` | `3704b1e222e3f4eee9c72624cbdad7ea8ea4b14b99194781e3d59e7c8fff6f5b` |
| `POLICY.md` | 17333 | `10b49a9551eb2f2a3e32d65b0d5b7206febe9de9` | `da5d2cf5a021f4d069c471725e02b6d2c201e3acadd5ecfd4213a361184b7a5d` |
| `AGENTS.md` | 21813 | `a449c8036ccbc40240060c885bb936630d4fc680` | `7363b83ca6d822ec35e8465fe64c1aa8cd0007bf8b99ae599c265cc49fcee6e1` |
| `canon/CORE.md` | 37109 | `924b6eb65a92a0cb47f89caee1a956540909c047` | `bce891d62b48aa95e2e124856e82bb16799ad930b422a8264542c84bfcb7fbf9` |
| `canon/FRONTIER.md` | 27382 | `acc208da19cf123cd50f538ee1f967530daadbc4` | `8574c3d4b0cc70278dec7d64e2a51022718cc54497c64025d9e6021775fcbaf0` |

Two canonical `[T]` entries in `canon/CANON.md` are used directly:
1. `CONTACT-W-BOUND-PAIR-RESPONSE [T]`: defines the free two-body coin/streaming walk, the contact operator $W(P)$, and its $3\times 3$ contact resolvent blocks $G_0, K$ at $P=0$.
2. `CONTACT-W-SPECTRAL-READING [T]`: proves that the full operator $W$ has two open spectral gaps of width at least $\arccos(7/25) - 2\pi/5 > 0$.

---

## 2. Frozen Public Predecessor Packages (`mathorn1973/twist-j`)

The following three frozen public note packages in `mathorn1973/twist-j` supply the analytical derivations of the native occupancy intertwiner, physical half-space cut current, open-channel causal history reduction, dark-state current counterexample, and infinite-carrier no-go theorems consolidated in `PROOF_CURRENT_RECORD_INTERFACE.md`. Their standalone note-local scripts (`verify.py`, `break_certificate.py`) were neither imported nor executed as reproductions in this package.

### 2.1 Spatial-Cut Current Package (`PR #1721`, commit `d221e10747e009cb1315295a258f1d48e8b75bce`)

| Path in `mathorn1973/twist-j@d221e10747e009cb1315295a258f1d48e8b75bce` | Bytes | SHA-256 | Role in This Package |
|---|---:|---|---|
| `notes/C-HODGE-SPATIAL-CUT-N/PROOF_CURRENT.md` | 17448 | `b6b36f8b940fdad68c00f6272ee0ec13f466eef80cad283fb4aa59c7f8595d12` | Analytical source: physical cut $\ell$, active charge weights $(2,2,4,2)$, $J_\ell = C^* D_c^*(j_{S,\ell}+j_{E,\ell})D_c C$ |
| `notes/C-HODGE-SPATIAL-CUT-N/PROOF_NATIVE.md` | 17897 | `b9141d218beec2ce0fc85a8e53d407174d940d1c8b8958394736ccdd75e25d1a` | Analytical source: $\mathcal{I} = \mathsf{Emb}\,\Gamma^{-1}D_2^*$, occupied-helper pullback |
| `notes/C-HODGE-SPATIAL-CUT-N/PROOF_RELATION.md` | 18296 | `498f73c5e99292c34223a904b86b5719d47992818e21648add6ccec480ad6206` | Analytical source: relation to boundary-port predecessors and scope limits |
| `notes/C-HODGE-SPATIAL-CUT-N/PREREG.md` | 9041 | `43ff5c46539b5506d2778383dc801603991e236febeaa3e1aa46974a9061e7dd` | Predecessor protocol and declarations |
| `notes/C-HODGE-SPATIAL-CUT-N/README.md` | 11359 | `12a1e7d07911c03dfc0f8994d8ec36fcae669bb0901b4fd6273ddf2a362f18d3` | Predecessor overview and scope |
| `notes/C-HODGE-SPATIAL-CUT-N/RESULT.md` | 5496 | `cf7edd3e182f2adfde0dfd6ac56c74e2cb73405a0a5a7f7863c40421bbde8ba3` | Predecessor result record |
| `notes/C-HODGE-SPATIAL-CUT-N/RUN.md` | 4230 | `f2caa19924bacd9560d2288d7485d06ba4ad40fd379f659b4b76348fa2768a14` | Predecessor custody record |
| `notes/C-HODGE-SPATIAL-CUT-N/SOURCES.md` | 9945 | `cead240de6b231d0f80c3696258cb5d317f31d0d3e5a525b47d46a5fed67cf58` | Predecessor source manifest |

### 2.2 Open-Channel Reduction Package (`PR #1723`, commit `b4696efa4fcb56cef8883fb593d2ab571bdcd047`)

| Path in `mathorn1973/twist-j@b4696efa4fcb56cef8883fb593d2ab571bdcd047` | Bytes | SHA-256 | Role in This Package |
|---|---:|---|---|
| `notes/C-HODGE-OPEN-CHANNEL-N/PROOF_REDUCTION.md` | 8295 | `f170abec693e645eaecc2d04888b3514e36c42b1d07b0655c736b8a22b872ffb` | Analytical source: exact block reduction, causal history reconstruction $L_m$, return amplitudes $g_k$ |
| `notes/C-HODGE-OPEN-CHANNEL-N/PROOF_PORT.md` | 18535 | `9f7428ebca237586012c4c04bd06b1b02451214db0fa0631fe4f6ea0354485db` | Analytical source: open-channel port transfer $s(z)=(4-F(z))/(4+F(z))$ |
| `notes/C-HODGE-OPEN-CHANNEL-N/PROOF_CURRENT.md` | 18741 | `fd9ef380f700ba03295c158db8d9bff37dab1fa87204b7fac49af20471db03d3` | Analytical source: history charge/current kernels, dark-state counterexample $\psi_\pm$ |
| `notes/C-HODGE-OPEN-CHANNEL-N/PREREG.md` | 10793 | `66916a78143ef49e0511fd4a53467dac6e48b8f5e3735ba46e78bec66e2b3fa1` | Predecessor protocol and declarations |
| `notes/C-HODGE-OPEN-CHANNEL-N/README.md` | 8810 | `5d5dbc05cd7c768264f0b0126372337fbf789ba3c84c8f318ff2bb8d1f21404e` | Predecessor overview and scope |
| `notes/C-HODGE-OPEN-CHANNEL-N/RESULT.md` | 6077 | `7f8752e2dddd412ec28ea150fbbdb14d21fc26f25f6c4b1d7f104ae96aee4669` | Predecessor result record |
| `notes/C-HODGE-OPEN-CHANNEL-N/RUN.md` | 4103 | `89b6cb4f604b96acd200ddc4533f007bf140911453b81a8ca357276e8cee7d81` | Predecessor custody record |
| `notes/C-HODGE-OPEN-CHANNEL-N/SOURCES.md` | 6480 | `63837957ecd1c149e6a7cb0904dba9e5073fe0f978f3f8d2078e2f4d8a37997e` | Predecessor source manifest |

### 2.3 Infinite-Carrier Obstruction Package (`PR #1726`, commit `bebdd534cf1ec57596b83be7faf2b724f00b8f24`)

| Path in `mathorn1973/twist-j@bebdd534cf1ec57596b83be7faf2b724f00b8f24` | Bytes | SHA-256 | Role in This Package |
|---|---:|---|---|
| `notes/C-HODGE-INFINITE-CARRIER-N/PROOF.md` | 18486 | `0a58d9f07e0fb9d3a614cb4fc69d7d0bb65aa523e3098c14cbd730ea35d1adb7` | Analytical source: lattice recurrence, Theorems 1–3 (extreme coordinate, nonrational $F,s$ without P24, infinite $\pm 2$ current index) |
| `notes/C-HODGE-INFINITE-CARRIER-N/README.md` | 2694 | `bc47979b3a78a4427533d430d3abbeec9ac259e792c1bc1cbd15858561e2ad94` | Predecessor overview and scope |
| `notes/C-HODGE-INFINITE-CARRIER-N/REVIEW.md` | 4622 | `8f915ddfe3e1a577e09eb48a9911e3ec40b4223b37442ea3dce3f09b3a5c9654` | Author-session analytical review |
| `notes/C-HODGE-INFINITE-CARRIER-N/SOURCES.md` | 4630 | `bf325cefe97234978c2fe64cd386d5664eafe7be72e9f06cbc9350046222ca45` | Predecessor source manifest |

---

## 3. Primary Homogeneous Capture Source and Review Basis

The primary homogeneous capture, branch-gap, finite-strip, and receiver-completion derivations consolidated in full in `PROOF_CAPTURE_SCATTERING.md`, `PROOF_PACKET_CERTIFICATE.md`, and `PROOF_CURRENT_RECORD_INTERFACE.md` originate from `mathorn1973/twistj-handoff` commit `0b9bf39b3a5866fdb34c6f37711462dc8dd08ab8` (`homogeneous-capture-2026-10-22/`, prospective pre-execution source pin `df4d70c951c4d0829a22882e4382acdc5ea12d1d`; inherited branch-gap source `91e10f808200a7b2727598ceba34464375781fac`), together with the three component reviews (`4182f3d65e8c5a453b5108a3c0e5b13eaad8fa92`, `53d45d6df03c912193b347b93a7cbaf13f600cf3`, `ea7b179f9da74bc674ecc2f48f27fe784cbb7582`) and interface synthesis (`bd6ea7d3b9da7eadc49f97eafe66def9336ff4f4`, integrated head `3ede9389797540f8d3766af1fec020ad8ead951a`). Because all mathematical definitions, proofs, and standard-library certificates are reproduced in full within this public package, no access to `twistj-handoff` is required to audit any claim.

| Primary Source Path (`0b9bf39b3a5866fdb34c6f37711462dc8dd08ab8`) | Bytes | SHA-256 | Public Self-Contained Counterpart |
|---|---:|---|---|
| `homogeneous-capture-2026-10-22/proofs/homogeneous_source.md` | 37570 | `3e8832f435caeddcbbca34ace5e63c366ea86fa5210007c10cfd77f5859b6e30` | `PROOF_CAPTURE_SCATTERING.md` §§1–3, 5.2–5.3; `PROOF_CURRENT_RECORD_INTERFACE.md` §§1–2 |
| `homogeneous-capture-2026-10-22/probability/PACKET_PROOF.md` | 14326 | `200a41ec4d9d58520c1fd68952d382015cc106593413132454faa5337edd3239` | `PROOF_PACKET_CERTIFICATE.md` §§1–4 |
| `homogeneous-capture-2026-10-22/inputs/pr29/inputs/BRANCH_GAP_PROOF.md` | 10177 | `14db9058e7478d197a8735838173b4c3778b5197c92d95b3cf0bb3ad89a99b66` | `PROOF_CAPTURE_SCATTERING.md` §4; `verify.py` Group 1 |
| `homogeneous-capture-2026-10-22/proofs/finite_strip_complete.md` | 21814 | `3c92e9e28e30010ed82d1e19ae9ae2af91cf7d8e5002eab6cfc18a4deba6df4b` | `PROOF_CAPTURE_SCATTERING.md` §5.1; `verify.py` Group 6 |
| `homogeneous-capture-2026-10-22/proofs/native_completion_static_review.md` | 9712 | `997a4689ed9694d3cb00d5db1fa3191124b98cd02d9f53146fa24a7ca10e3fe8` | `PROOF_CURRENT_RECORD_INTERFACE.md` §§1, 3; `verify.py` Group 3 |
| `homogeneous-capture-2026-10-22/inputs/original-rearrangement/original_note.tex` | 42642 | `d66327a68711889606ff3d789bcadc530ecb3ac0d1dfd9c996816bcc0dd3da23` | `PROOF_CURRENT_RECORD_INTERFACE.md` §3 (native gate order, SWAP routing, clock phases) |
| `homogeneous-capture-2026-10-22/inputs/original-energy/local_coherent_capture.md` | 23191 | `20642c753aa8f18771c55c37fb684d2a36fb145cdb1d34f05d4fa312bca767d1` | `PROOF_CURRENT_RECORD_INTERFACE.md` §3 (object subbank port convention) |
| `homogeneous-capture-2026-10-22/probability/packet_certificate.py` | 13063 | `a8230d83bb0d5a5af495b72b47e72e38d83582c7df6767688e97cdcf2b799f48` | Replaced by first-principles stdlib verifier `verify.py` Group 2 (`PROOF_PACKET_CERTIFICATE.md` §5) |
| `homogeneous-capture-2026-10-22/verification/check_native_completion.py` | 9211 | `53709a7567935473cbec5c9c2df50b67e70523797ac335ed798e8d284389d23d` | Incorporated into `verify.py` Group 3 |
| `homogeneous-capture-2026-10-22/proofs/check_finite_strip_exact.py` | 5278 | `0a7855b6b0abc77fe946078463e1025dcdea652caaecdc6343451393d5a432b3` | Incorporated into `verify.py` Group 6 |
| `homogeneous-capture-2026-10-22/FROZEN_INPUTS.json` | 14476 | `5e186439cca122e50c0e5df23dde8bf09834dec432463f11c3e5d6fab35b86df` | Custody manifest (59 file entries; see §4 below) |

---

## 4. Extraction/Custody Receipt, Manifest Reconciliation, and License/Security Review

1. **Manifest entry-count reconciliation (59 vs. 62):**
   The pre-execution manifest `homogeneous-capture-2026-10-22/FROZEN_INPUTS.json` (14,476 bytes, SHA-256 `5e186439cca122e50c0e5df23dde8bf09834dec432463f11c3e5d6fab35b86df`) contains **59** file entries. All 59 entries were machine-audited and matched byte-for-byte in `v105-reviews-2026-10-23/capture/SOURCE_AUDIT.json`, `v105-reviews-2026-10-23/current/SOURCES.tsv`, and `v105-synthesis-2026-10-23/SOURCE_RECONCILIATION.json`. The narrative prose of Capture Review A's `REVIEW.md` and `REPLAY.md` wrote "62" when referring to that manifest; this clerical prose discrepancy is noted here for custody completeness without altering the sealed review reports.
2. **No wholesale private archive import:**
   Only clean, self-contained English mathematical proofs, explicit source/claim tables, and a dependency-free Python 3 standard-library verifier are placed in `notes/C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N/` and `reproduce/C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N/`. No private operational diaries, run logs, vendored wheels, or non-English working notes are imported.
3. **License and security review:**
   - **License:** All files in `notes/C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N/` and `reproduce/C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N/` are original work by A. M. Thorn licensed under Apache-2.0 (`LICENSE`).
   - **Security and policy compliance:** All files are UTF-8 LF text under 5 MiB; no forbidden suffixes (`.bak`, `.bin`, `.dll`, `.dylib`, `.env`, `.exe`, `.jam`, `.jsonl`, `.key`, `.log`, `.pem`, `.pt`, `.pth`, `.pyc`, `.so`, `.token`), no credentials or tokens, no network calls, no subprocess invocations, and no filesystem writes occur in `verify.py`.
