# Non-Promotion Memo: `C-FUNDED-TWO-USE-EXECUTABLE-N`

**NON-CANONICAL / L1 / PARTIAL — STOP / `DO NOT PROMOTE`.**
Original work Apache-2.0, A. M. Thorn, 2026-10-15.

```text
candidate_id:              C-FUNDED-TWO-USE-EXECUTABLE-N
lane_issue:                https://github.com/mathorn1973/twist-j/issues/1507
parent_program:            https://github.com/mathorn1973/twist-j/issues/1506
branch:                    incubation/C-FUNDED-TWO-USE-EXECUTABLE-N
preregistration_commit:    81a70caa8dbcc61b64276e7d3df5ba84e860d4f1
scientific_status:         PARTIAL / STOP (T01_geometry_stencil_and_operators FAILED: Expected |D| = 869, got 705)
comparison_digest_status:  NOT_RUN (blocked by carrier discrepancy 705 vs 869)
physical_status:           NOT_READY
recommendation:            DO NOT PROMOTE
```

---

## 1. Explicit Recommendation: `DO NOT PROMOTE`

`C-FUNDED-TWO-USE-EXECUTABLE-N` is a `NON-CANONICAL` Layer `L1` incubation package under `notes/C-FUNDED-TWO-USE-EXECUTABLE-N/` and **must not be merged or promoted to Public Canon v101**.

1. **Fired `T01` geometry gate and mandatory `STOP`:**
   On the first execution after public preregistration pin `81a70caa8dbcc61b64276e7d3df5ba84e860d4f1` (`#1507#issuecomment-6189582448`), `verify.py` halted in `T01_geometry_stencil_and_operators` (`apparatus.py`, line 153, `get_geometry()`) with `RuntimeError: Expected |D| = 869, got 705`. Constructing the Minkowski sum $D = Y + B_{\mathrm{zero}} + B_{\mathrm{zero}}$ from the frozen 5-site set $Y$ and 61-element stencil set $B_{\mathrm{zero}}$ yields $|D| = 705$, conflicting with the $869$-site assertion carried in `#1500`, `#1504`, and `#1506`.
2. **Unreached audit and comparison inventory:**
   Under the zero-tolerance `STOP` rule of `#1507` and `PREREG.md` (`81a70caa8dbcc61b64276e7d3df5ba84e860d4f1`), tests `T02`–`T18`, adversarial tests `X01`–`X10`, the 6 witness boundary trajectories (`--witnesses`), and the 1200-record comparison stream (`TWOUSE-COMPARE-v1`, `--compare`) are all `NOT_RUN`.
3. **Notes-only CI limitation:**
   Ordinary repository checks `python3 tools/check_verifier.py` and `python3 tools/check_reproduce.py` do not execute scientific code under `notes/` (`NOT APPLICABLE`). Green administrative checks on this Draft PR are not a scientific replay.
4. **Conditional L1 and physical boundaries:**
   Even apart from the `T01` carrier-size stop, the package is strictly `L1`: native compilation of $L_{\mathrm{buf}}, H_{B,A}, H_{B,B}$ into the unchanged autonomous kernel $U$ is `UNSUPPLIED`, and physical realization is `NOT_READY`.

---

## 2. Required Preconditions Before Any Successor Run

1. Explicitly reconcile the upstream specification of $D = Y + B_{\mathrm{zero}} + B_{\mathrm{zero}}$ ($|D| = 705$) versus the stated $|D| = 869$ in `#1500`, `#1504`, and `#1506`.
2. Do not rewrite, rebase, or silently modify the consumed identifier `C-FUNDED-TWO-USE-EXECUTABLE-N` or its immutable pin `81a70caa8dbcc61b64276e7d3df5ba84e860d4f1`. Any corrected executable audit and 1200-record cross-implementation comparison must use a newly authorized identifier and a fresh pre-execution pin.
