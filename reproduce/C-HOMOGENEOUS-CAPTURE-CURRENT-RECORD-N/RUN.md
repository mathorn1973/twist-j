# Execution Record: `C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N`

**Status:** `NON-CANONICAL` (Research-Note & First-Principles Reproduction Execution Record)  
**Claim ID:** `C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N`  
**Base Commit (`main`):** `e6240e2689bb22aab5f02bad90b75d3692bb96d9`  
**Active Prospective Source Pin Commit (Pin 4):** `c49d4630e8faf3b6714e5bf6ed16199b398a8504`

---

## 1. Prospective Source Pin Discipline and Complete Pin/Run Chronology

In accordance with `notes/C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N/PREREG.md` (§5), every modification to the pre-execution specification, proof, claim-table, provenance, or verifier source files was committed and pushed to `origin/codex/c-homogeneous-capture-current-record-n` and read back via `git ls-remote origin refs/heads/codex/c-homogeneous-capture-current-record-n` prior to executing `reproduce/C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N/verify.py`:

| Sequence | Prospective Pin Commit | Post-Execution Run Commit | Reason for Pin & Outcome |
|---|---|---|---|
| **Pin 1 $\to$ Run 1** | `d4ceea4960b547df0ebc80ccb441bb2e9d5d0ba0` | `18352983eeb6c837bfca26c97ec75cca5ee3e0b6` | Initial prospective source pin and local execution (`141` checks passed). |
| **Pin 2 $\to$ Run 2** | `fd710dbc6ca5023dba89c26de7421a6bbd9c01b5` | `2df30460045c9b1872a17df64e67bd4483f54adf` | Added `sys.stdout.reconfigure(newline="\n")` and `sys.flags.optimize` guard in `verify.py` for cross-platform LF determinism and `-O` safety; passed two-architecture GitHub Actions run `39993503251` (`architecture-x86_64`, `architecture-aarch64`, and `check`). |
| **Pin 3 $\to$ Run 3** | `4c7287debe0f28930acb9a9da20a9ba79d41d7d2` | `1982bc0d6667fecdcf706635cd77e085da45ecf1` | Repaired review findings across `PROOF_*.md`, `README.md`, `PREREG.md`, `CLAIMS*`, `SOURCES.md`, and `verify.py`; passed two-architecture GitHub Actions run `40007976624` (`architecture-x86_64`, `architecture-aarch64`, and `check`). |
| **Pin 4 $\to$ Run 4 (Active)** | `c49d4630e8faf3b6714e5bf6ed16199b398a8504` | Recorded by this commit | Repaired re-review groups `G01–G06` across `PROOF_*.md`, `README.md`, `PREREG.md`, `CLAIMS*`, `reproduce/README.md`, and `verify.py` (fixing `M_NAT = D2^* M_SRC D2 = Q tensor Q` and testing the exact intertwining `M_NAT D2^* == D2^* M_SRC` and `(S M_NAT Gamma)(Gamma^-1 D2^*) == (Gamma^-1 D2^*)(Gamma S M_SRC)`, plus `pulse[1] == (1,1,0,0,0)` and reversed-coin negative control; `144` checks passed). |

None of the ten prospectively pinned specification, proof, claim-ledger, provenance, or verifier source files were modified after `c49d4630e8faf3b6714e5bf6ed16199b398a8504`.

---

## 2. Active Pinned Execution Metadata (Pin 4 $\to$ Run 4)

| Field | Value |
|---|---|
| Command | `python reproduce/C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N/verify.py` |
| Environment | `LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC` |
| Start timestamp (UTC) | `2026-10-23T19:49:06Z` |
| End timestamp (UTC) | `2026-10-23T19:49:07Z` |
| Wall-clock elapsed time | `0.6298 s` |
| Python runtime | `Python 3.12.10` |
| Exit code | `0` |
| Standard error (`stderr`) | `0` bytes |
| Standard output (`EXPECTED.txt`) | `708` bytes (`8` lines, LF line endings) |
| `EXPECTED.txt` SHA-256 | `46a5221d8fea9d0c8855c5d18d2823381053c7f1e64d538452bb3afa48d09441` |

---

## 3. Exact Frozen Output (`EXPECTED.txt`)

```text
PASS GROUP 1 BRANCH_GAP: 24 checks; gap>=13/165; L<=165/13
PASS GROUP 2 PACKET_CERTIFICATE: 44 checks; B_hom>=903570708e-33>8e-25; P_joint>=287615489e-36>2e-28
PASS GROUP 3 NATIVE_COMPLETION: 28 checks; 2704 contact states; 1352 receiver-edge states
PASS GROUP 4 CURRENT_INTERFACE: 14 checks; cut l=99; j_coh=1642/625
PASS GROUP 5 OPEN_CHANNEL_AND_CARRIER: 16 checks; nu_1=4/5; dark_diff=4*sqrt(2)/5
PASS GROUP 6 FINITE_STRIP: 18 checks (16 Laurent identity groups + 2 negative controls)
SCOPE: connected asymptotic capture, full current, and coherent record; p(Q_full)>=p(Q_win)>2/10^28; finite-time preparation and occurrence NOT DERIVED
VERIFY PASS C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N total_checks=144
```

---

## 4. File Inventory and SHA-256 Verification Against Prospective Pin 4

All ten prospectively pinned pre-execution files retain their exact byte lengths and SHA-256 digests from commit `c49d4630e8faf3b6714e5bf6ed16199b398a8504`:

| Repository Path | Role | Bytes | SHA-256 | Matches Pin `c49d4630` |
|---|---|---:|---|---|
| `notes/C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N/README.md` | Package overview & theorem statement | `23159` | `ff4406dde2ab8d4c614b1ef14aa1ef139000f99e4b9741bbda3856e635a89056` | Yes |
| `notes/C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N/PREREG.md` | Frozen preregistered test plan | `15010` | `7079679c3f154cbd7093f40765c33fda351304a0c06bf1460fead2b249717bd6` | Yes |
| `notes/C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N/PROOF_CAPTURE_SCATTERING.md` | Capture, scattering & finite-strip proofs | `41664` | `7645997a510b499e64afc5266a1c87ae4d3151aa8fd30eee0cfcc8ff3d5a71d2` | Yes |
| `notes/C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N/PROOF_PACKET_CERTIFICATE.md` | First-principles packet certificate & soundness | `18606` | `80573da4664db680c0e03a7f9b6ac2348c6743666a7703ea9ebe92b0ddd6ba46` | Yes |
| `notes/C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N/PROOF_CURRENT_RECORD_INTERFACE.md` | Native completion, current & effect pullback proofs | `29753` | `cbe89baed499249df94978373a557e4008d54142131a3515be33aeb3d11a7192` | Yes |
| `notes/C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N/CLAIMS_AND_DISPOSITIONS.md` | Claim matrix, dispositions & scope fences | `15708` | `edc24ecc044f591ebdc5904a9af145087439b2bb0a792bd78f450df84d854a54` | Yes |
| `notes/C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N/CLAIMS.tsv` | Machine-readable claim ledger | `5720` | `6a03678c69f117798a8ab3e26f98ceac33225208abc78d8d3e7cdf8636730ba0` | Yes |
| `notes/C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N/SOURCES.md` | Self-contained provenance & audit receipt | `12133` | `1384d8e0363dc75f8dec73d7d416a6bcd215fdb60d18fd55cb13832a1def6cc7` | Yes |
| `reproduce/C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N/README.md` | Reproduction harness instructions | `6646` | `07291e9f06da294c85f6c69617e186c5f095882580865581eead22de07acd9c1` | Yes |
| `reproduce/C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N/verify.py` | Standard-library first-principles verifier | `58164` | `d1f82078039f09e69010048d31a4f49cbfdbc6cfa9ac126d30beb8e2df2691b6` | Yes |
| `reproduce/C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N/EXPECTED.txt` | Frozen post-execution standard output | `708` | `46a5221d8fea9d0c8855c5d18d2823381053c7f1e64d538452bb3afa48d09441` | Populated from pinned run |
