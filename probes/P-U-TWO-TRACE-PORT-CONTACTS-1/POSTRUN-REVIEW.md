# Post-run retained-artifact and custody review

PASS. This review compares retained evidence and Git blobs only. Neither native implementation nor the added exchange algorithm was rerun; no frozen source was edited. The public pin is `5d122f0cab1fb20b368302cee4b4989d13ff16d2`, tree `b405ba965d67ddca390d3070a2e1fa9d64fb1d81`.

## Pin and first-run custody

All 21 inputs in the retained BEFORE.json match the exact pin's Git blobs in byte length and SHA-256, and remain byte-identical in the public preparation worktree. All twenty entries of INPUTS.sha256 match their pinned files. Its own hash is `3d4bf5d1eda32320d629d033c6d7db7f838e2bb1e0bc23dc941dfc42bf51400a`. The accepted primary, independent program, wrapper, contracts and review freezes are unchanged.

PUBLIC-PIN.md records the coordinator's public commit/tree readback at 2026-10-04 00:40:37 UTC and subsequent matching branch readback. The recorded first run begins later, at 00:41:01.820418 UTC, and ends at 00:41:02.325146 UTC. It used CPython 3.12.10 on Windows 11, x86_64. The exact retained stdout is one UTF-8/LF JSON line, 2636 bytes, SHA-256 `cc8109a7b389fc77db7f25366d143b198aaf7d3d1b1ff5c781713e3b57ad82fc`; stderr is empty and the receipt records exit zero. Wrapper, primary and independent statuses are PASS. EXPECTED.txt is byte-identical to this actual stdout.

The temporal public-readback claim is supported by the coordinator's receipt; the present review independently verifies the pinned bytes and retained run artifacts. It does not pretend to be a second contemporaneous witness of the earlier upload or a fresh execution.

## Complete cross-implementation agreement

These arrays are byte-identical between the two independent implementations, not merely equal after parsing:

| Array | Rows | Bytes | SHA-256 |
| --- | ---: | ---: | --- |
| Full boundary histories | 250 | 9002 | `a482c71935bbab702c261262df02017e14839e3df4171b91efdb4a0bb9fe80b1` |
| Local pre/post exchange contacts | 50 | 1802 | `3e1cffba722600bf92554bcceb328f076e6cf30f4c037c460e645d84c904e978` |
| Actual selector pairs | 225 | 2702 | `5a449912228b3b2b09919f56f606c2566e3d3d0698f44db3a55c0e52b7a21998` |
| No-exchange control histories | 250 | 9002 | `8670e671558f12b319dbf5c2341863b1881ca336b0be5a5508d2f7d149c25c93` |

The ordering and row widths match preregistration exactly. The main history covers 3500 pentit values and 250 counters: all fourteen state coordinates at every one of ten boundaries for all 25 input pairs. The corresponding CSV and JSON representations agree. All fifty full-state exchange objects agree with the boundary histories and local contact arrays, including the untouched factors and unadvanced counter at the algebraic exchange stage.

All 450 retained native cell-transition records have pre-states equal to the corresponding retained boundary or post-contact state, post-states equal to the next complete boundary, and selected indices equal to the independent selector array. This checks consistency between independently emitted artifacts without calculating another native trajectory. All 250 control boundary states also agree across implementations and CSV/JSON formats.

The public evidence/SHA256SUMS has sixteen entries. Every copied artifact matches both its manifest and a retained first-run artifact byte for byte; all are below 5 MiB. The independent SUMMARY.json agrees with its wrapper report, and all eleven primary artifact hashes and lengths agree with the primary report.

## Outcome and limits

The saved endpoint records agree with the fixed reader applied to their saved piston coordinates. Their pair counts are `(0,0):16`, `(0,1):4`, `(1,0):4`, `(1,1):1`, exactly as both independent input ranges require. These are deterministic counts over 25 preparations, not a derived occurrence probability law. The NO-EXCHANGE control has nine failing input pairs containing at least one four; it is the declared negative control, not a failure of the extended interaction.

The common second receiver state at boundary 6 is `(2,1,3,4,0,4)` in every retained history. Source exports are 1 and 4, with the second source untouched through that boundary. Complete receiver trajectories satisfy the declared cross-source independence. The complete enlarged states for inputs (0,0) and (1,0) are distinct initially, equal at every retained boundary from 3 through 9, and agree with the explicit collision artifact. The positive result therefore preserves its disclosed source consumption and global many-to-one behavior.

Both programs report complete coverage of the 78125-state added primitive. The independent report records 12500 X14/control retention cases and 456483 assertions. Those counts describe the already executed audit and are not new computations by this review or counts of independent experiments. The all-time guarantee still comes from the reviewed X14/A-negation induction, not the bounded histories through n=9.

I also reviewed the draft public RESULT.md, SHA-256 `475fa67c63ef84e8a2f57855927d90076ecf92063581dbc0d0316b8ec4b04a43`. It accurately distinguishes the analytical candidate-T theorem, this exact finite audit, the separate future architecture gate and non-canonical status. It retains the two paid receivers, two preloaded source ports, admitted trace access/address schedule, no reset, source loss and the restricted A-preserving necessity boundary. It makes no physical availability, energy, full SUM, source-preservation, indefinite-renewal or #1349 closure claim. No scope correction is required.

Detailed evidence identities and comparison counts are retained in POSTRUN-CUSTODY.json, SHA-256 `c4f9582f0eebd6fc70c3b91ef892566f12b6a7f533cdfd0eb294a10ed984a42a`. Its review time is 2026-10-04T00:44:26.335322Z. Public architecture reproduction and final PR acceptance remain separate later gates.
