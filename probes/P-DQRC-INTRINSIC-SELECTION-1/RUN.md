# P-DQRC-INTRINSIC-SELECTION-1 formal run record

Status: `AUDIT-CONSISTENT / REPARAMETERIZATION-ONLY / ONE LOCAL FORMAL LEG / CANON UNCHANGED`

The public pin and both accepted files were read back before execution. The
single owner-authorized formal execution then used the sealed invocation from
`PREREG.md`. The machine-readable `command` field below uses the repository
checker spelling; the launcher normalization is disclosed immediately after
the record.

```text
pin_commit: 2897cd968b3271d1c928891d6fea06a948119a03
base_commit: 18f1180b6128c05705ebaa23733a10457aea3d3f
branch: probe/P-DQRC-INTRINSIC-SELECTION-1
public_lock: issue 440
public_pin_comment: 5345208242
prereg_sha256: 3e937835a35fecd5baf9089d256b667cd5acb2f6e02ddeb094738bab02c0beec
prereg_bytes: 15149
prereg_git_blob: 25e07a8ba9a7052ed547b5f84edcd29fa3e06307
verifier_sha256: 226824dbc053acd8f41517f5f5103697509172519ea483055e2fd49711e7062f
verifier_bytes: 8018
verifier_git_blob: 606959a117e432819cb53733fd338b881fb88f6b
command: python3 probes/P-DQRC-INTRINSIC-SELECTION-1/verify.py
sealed_invocation: python3 -B probes/P-DQRC-INTRINSIC-SELECTION-1/verify.py
platform: Ubuntu 24.04.3 LTS
architecture: x86_64
python: CPython 3.12.13
optimization: 0
arguments: none
locale: LC_ALL=C.UTF-8 LANG=C.UTF-8
timezone: Europe/London
formal_execution_count: 1
post_capture_repository_replays: 1
exit_code: 0
stdout_sha256: 67eeba11fccc240d7da681357f72620adc741e854165b4b2657b51059bf5342e
stdout_bytes: 596
stdout_lines: 11
stdout_lf: 11
stdout_cr_bytes: 0
stdout_nul_bytes: 0
stdout_final_byte: 0a
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
stderr_lf: 0
stderr_cr_bytes: 0
stderr_nul_bytes: 0
stderr_final_byte: EMPTY
run_integrity: AUDIT-CONSISTENT
coefficient_disposition: REPARAMETERIZATION-ONLY
architecture_gate: pending required GitHub x86_64 and aarch64 replays
```

## Launcher normalization

The sealed command actually executed was

```text
python3 -B probes/P-DQRC-INTRINSIC-SELECTION-1/verify.py
```

The machine-readable `command` field omits `-B` only because
`tools/check_verifier.py` requires exactly that repository spelling. The
required checker invokes the same pinned script as `[sys.executable, path]`
with `PYTHONDONTWRITEBYTECODE=1`. Thus both launchers suppress bytecode writes;
`-B` is an interpreter option, does not enter `sys.argv`, leaves the frozen
`len(sys.argv)==1` gate unchanged, and does not alter scientific stdout. This
is an explicit launcher normalization, not an edit to the pin or accepted
verifier.

## Exact local record

`EXPECTED.txt` is the exact raw stdout of the one formal execution, with LF
line endings and a final LF. The process exited zero, wrote no stderr, and
returned the frozen disposition `AUDIT-CONSISTENT`. The seven bounded gates
audit the formulas; the universal word and uniqueness statements remain
carried by the written proofs in `PREREG.md`.

After the transcript and run record were assembled, one local invocation of
`tools/check_verifier.py --base 18f1180b6128c05705ebaa23733a10457aea3d3f`
replayed the pinned script and reproduced `EXPECTED.txt` byte for byte. That
repository validation is a post-capture reproduction, not a second formal
capture and not independent scientific evidence.

The verifier has a deliberate hard interpreter guard
`sys.version_info[:2] == (3, 12)`. The repository workflow currently pins
Python 3.12 on both architectures. A future workflow change to another minor
version would produce an integrity `STOP`; this sealed probe cannot be repaired
in place and would require a fresh probe if replay were still needed.

The two GitHub architecture legs are not pre-recorded here. They must rerun
the pinned verifier and compare stdout byte for byte with `EXPECTED.txt` in
the pull-request workflow.
