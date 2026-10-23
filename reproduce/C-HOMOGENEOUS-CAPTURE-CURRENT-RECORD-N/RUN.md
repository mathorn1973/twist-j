# Execution Record: `C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N`

**Status:** `NON-CANONICAL` (Research-Note & First-Principles Reproduction Execution Record)  
**Claim ID:** `C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N`  
**Base Commit (`main`):** `e6240e2689bb22aab5f02bad90b75d3692bb96d9`  
**Active Prospective Source Pin Commit (Pin 3):** `4c7287debe0f28930acb9a9da20a9ba79d41d7d2`

---

## 1. Prospective Source Pin Discipline and Complete Pin/Run Chronology

In accordance with `notes/C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N/PREREG.md` (§5), every modification to the pre-execution specification, proof, claim-table, provenance, or verifier source files was committed and pushed to `origin/codex/c-homogeneous-capture-current-record-n` and read back via `git ls-remote origin refs/heads/codex/c-homogeneous-capture-current-record-n` prior to executing `reproduce/C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N/verify.py`:

| Sequence | Prospective Pin Commit | Post-Execution Run Commit | Reason for Pin & Outcome |
|---|---|---|---|
| **Pin 1 $\to$ Run 1** | `d4ceea4960b547df0ebc80ccb441bb2e9d5d0ba0` | `18352983eeb6c837bfca26c97ec75cca5ee3e0b6` | Initial prospective source pin and local execution (`141` checks passed). |
| **Pin 2 $\to$ Run 2** | `fd710dbc6ca5023dba89c26de7421a6bbd9c01b5` | `2df30460045c9b1872a17df64e67bd4483f54adf` | Added `sys.stdout.reconfigure(newline="\n")` and `sys.flags.optimize` guard in `verify.py` for cross-platform LF determinism and `-O` safety; passed two-architecture GitHub Actions run `39993503251` (`architecture-x86_64`, `architecture-aarch64`, and `check`). |
| **Pin 3 $\to$ Run 3 (Active)** | `4c7287debe0f28930acb9a9da20a9ba79d41d7d2` | Recorded by this commit | Repaired review findings across `PROOF_*.md`, `README.md`, `PREREG.md`, `CLAIMS*`, `SOURCES.md`, and `verify.py` (adding `proj_alpha(d_prime, 0) == Cyc() and proj_alpha(chi_prime, 0) != Cyc()` and accurate check label for identical nonzero pulse output histories of $\psi_\pm$). |

None of the ten prospectively pinned specification, proof, claim-ledger, provenance, or verifier source files were modified after `4c7287debe0f28930acb9a9da20a9ba79d41d7d2`.

---

## 2. Active Pinned Execution Metadata (Pin 3 $\to$ Run 3)

| Field | Value |
|---|---|
| Command | `python reproduce/C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N/verify.py` |
| Environment | `LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC` |
| Start timestamp (UTC) | `2026-10-23T18:48:44Z` |
| End timestamp (UTC) | `2026-10-23T18:48:45Z` |
| Wall-clock elapsed time | `0.6173 s` |
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

## 4. File Inventory and SHA-256 Verification Against Prospective Pin 3

All ten prospectively pinned pre-execution files retain their exact byte lengths and SHA-256 digests from commit `4c7287debe0f28930acb9a9da20a9ba79d41d7d2`:

| Repository Path | Role | Bytes | SHA-256 | Matches Pin `4c7287de` |
|---|---|---:|---|---|
| `notes/C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N/README.md` | Package overview & theorem statement | `22440` | `fc93b5cce50e9002dd581f5539025d964499ace2fbc5212f6705e12c1fc464cd` | Yes |
| `notes/C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N/PREREG.md` | Frozen preregistered test plan | `14548` | `27f4c51c4c1fe48039d9c41a8bf376e1bf843addf9174aa3dc7c3cd66ab8dbad` | Yes |
| `notes/C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N/PROOF_CAPTURE_SCATTERING.md` | Capture, scattering & finite-strip proofs | `30342` | `32c787803fd89c3fafeb2d863d1e50c96e46e327ccf4e4c6925e309cf506abf0` | Yes |
| `notes/C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N/PROOF_PACKET_CERTIFICATE.md` | First-principles packet certificate & soundness | `18606` | `80573da4664db680c0e03a7f9b6ac2348c6743666a7703ea9ebe92b0ddd6ba46` | Yes |
| `notes/C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N/PROOF_CURRENT_RECORD_INTERFACE.md` | Native completion, current & effect pullback proofs | `25188` | `97bf3e4f0ae82c9b41fe9b31e60759103b69ea546f9679881cf76ae88410e4ff` | Yes |
| `notes/C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N/CLAIMS_AND_DISPOSITIONS.md` | Claim matrix, dispositions & scope fences | `15173` | `e13e479ebec8db395a689460af4e810a67e92b20247ee6491fe2f5d604367747` | Yes |
| `notes/C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N/CLAIMS.tsv` | Machine-readable claim ledger | `5533` | `8f27dc27580d7bf9aea93ae23da1718d3a5fb203029fbd06742458e93b750e39` | Yes |
| `notes/C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N/SOURCES.md` | Self-contained provenance & audit receipt | `12133` | `1384d8e0363dc75f8dec73d7d416a6bcd215fdb60d18fd55cb13832a1def6cc7` | Yes |
| `reproduce/C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N/README.md` | Reproduction harness instructions | `6194` | `b9294cde46950b51315585b8d32a07cd9b092e9393ffa6a102d6ba45d6733c5a` | Yes |
| `reproduce/C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N/verify.py` | Standard-library first-principles verifier | `56261` | `589d0a34042ea88ea9f5246e84585d716d194deafb4a8d58613e5dbbd4eea470` | Yes |
| `reproduce/C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N/EXPECTED.txt` | Frozen post-execution standard output | `708` | `1c0d4c4459a4ae52a74adf6d1206ff4eb91a9042f200708c5a8d06aeb831a43b` | Populated from pinned run |
