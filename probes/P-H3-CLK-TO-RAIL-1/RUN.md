# Execution records

## Primary verifier

The public [preregistration readback](https://github.com/mathorn1973/twist-j/issues/2009#issuecomment-6960621714) verified all three input files before decorated execution. In a clean worktree at the pin, Linux independently checked the byte lengths and SHA-256 values and then invoked the Python verifier. Its exact standard output is in EXPECTED.txt.

```text
pin_commit: 1805d185a73e8c79de46e0c6872cafcb30e07fcb
command: python3 probes/P-H3-CLK-TO-RAIL-1/verify.py
working_directory: clean repository root at pin_commit
platform: Ubuntu 22.04.5 LTS (WSL2)
architecture: x86_64
python: 3.10.12
prereg_sha256: 0f6d1944cda458dd0b2674d3d24c2375a2f049fbe1a353170747326cfdead979
prereg_bytes: 9586
verifier_sha256: a6bc0f14917dda0ba60fb05bee87cd944717506eb53a204bde9f1bf9839f1c91
verifier_bytes: 23444
started_utc: 2026-11-17T20:50:44.976571+00:00
ended_utc: 2026-11-17T20:50:46.530535+00:00
exit_code: 0
stdout_bytes: 18372
stdout_lines: 1
stdout_sha256: 6b8329831ce0e9a7b8176c209d53aa0ccdbd1457d962aab01ad486a4a8fb1c34
stderr_bytes: 0
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

## Supplemental intrinsic-period engine

The pinned period.cpp is 17251 bytes with SHA-256 dc3696fbfc80d58a7a55c407079bdfcc345f6c33d9e74a50a1c27e33bd5da92d. Each run compiled with `-std=c++20 -O3`. From the probe directory:

```sh
g++ -std=c++20 -O3 period.cpp -o period
./period active 100000000
./period control 100000000
./period antenna 100000000
```

Ubuntu x86_64 (GCC 11.4.0) and Darwin arm64 (Apple Clang 21.0.0) returned byte-identical LF outputs. All six invocations exited successfully with empty stderr. A separate Windows x86_64 run (GCC 15.2.0) gave identical lines with CRLF endings. The Python transcript above and these long runs use separate arithmetic implementations. The following are the complete Linux outputs.

### active

920 bytes, SHA-256 af3c8743cf0b6269943bd6154be034ec65339a1a2db35c70bf9bf921cc18cd6e.

```text
preparation=active horizon=100000000 Q=717 matter=(-12,0,-4,-4) radiation=(20,6,8,17) hermitian=(434,0,151,151)
ticks=100000000 first_full_return=none_within_bound audit_count=24415 transport_writes=253651 collision_writes=154
raw=44 projected_predecessors=1 B1_reads=1 following_observations=1 changed_words=1 first_observation=75
observed_class distinct=1 (-3,2,-5,1)@75
written_class distinct=1 (-3,2,-5,1)@75
raw=4 projected_predecessors=1 B1_reads=1 following_observations=1 changed_words=1 first_observation=191
observed_class distinct=1 (2,4,1,3)@191
written_class distinct=1 (2,4,1,3)@191
observed_class_intersection distinct=0
written_class_intersection distinct=0
unscheduled_substep_changes count=253802 first_tick=192 first_stage=B before=(2,4,1,3) after=(3,4,3,5)
hold_mismatches count=199999587 first_tick=192 first_stage=B before=(2,4,1,3) after=(3,4,3,5)
qualifying_contacts_without_final_change count=0
```

### control

1139 bytes, SHA-256 9a63a7c15b666563b704d3a38c0c208f7b9cd2adb840587de750d9e777e77f1b.

```text
preparation=control horizon=100000000 Q=717 matter=(-12,0,-4,-4) radiation=(23,7,8,8) hermitian=(434,0,151,151)
ticks=3110 first_full_return=3110 audit_count=1 transport_writes=10 collision_writes=0
raw=44 projected_predecessors=5 B1_reads=5 following_observations=5 changed_words=5 first_observation=75
observed_class distinct=5 (-9,0,-3,-3)@1319 (-5,-2,-1,-7)@2563 (-3,2,-5,1)@75 (-1,-4,1,-1)@697 (3,4,3,5)@1941
written_class distinct=5 (-9,0,-3,-3)@1319 (-5,-2,-1,-7)@2563 (-3,2,-5,1)@75 (-1,-4,1,-1)@697 (3,4,3,5)@1941
raw=4 projected_predecessors=5 B1_reads=5 following_observations=5 changed_words=5 first_observation=191
observed_class distinct=5 (-9,0,-3,-3)@2679 (-5,-2,-1,-7)@813 (-3,2,-5,1)@1435 (-1,-4,1,-1)@2057 (3,4,3,5)@191
written_class distinct=5 (-9,0,-3,-3)@2679 (-5,-2,-1,-7)@813 (-3,2,-5,1)@1435 (-1,-4,1,-1)@2057 (3,4,3,5)@191
observed_class_intersection distinct=5 first_word=(-3,2,-5,1) raw44_tick=75 raw4_tick=1435
written_class_intersection distinct=5 first_word=(-3,2,-5,1) raw44_tick=75 raw4_tick=1435
unscheduled_substep_changes count=0
hold_mismatches count=0
qualifying_contacts_without_final_change count=0
```

### antenna

922 bytes, SHA-256 991100923fd7d0a1a82ead5da2068bfcfc3b6d2acab5fad877c316437eb78e92.

```text
preparation=antenna horizon=100000000 Q=794 matter=(-12,0,-4,-4) radiation=(26,5,11,18) hermitian=(487,0,180,180)
ticks=100000000 first_full_return=none_within_bound audit_count=24415 transport_writes=214525 collision_writes=134
raw=44 projected_predecessors=1 B1_reads=1 following_observations=1 changed_words=1 first_observation=75
observed_class distinct=1 (-3,2,-5,1)@75
written_class distinct=1 (-3,2,-5,1)@75
raw=4 projected_predecessors=1 B1_reads=1 following_observations=1 changed_words=1 first_observation=191
observed_class distinct=1 (2,4,1,3)@191
written_class distinct=1 (2,4,1,3)@191
observed_class_intersection distinct=0
written_class_intersection distinct=0
unscheduled_substep_changes count=214656 first_tick=208 first_stage=B before=(2,4,1,3) after=(3,4,3,5)
hold_mismatches count=199999283 first_tick=208 first_stage=B before=(2,4,1,3) after=(3,4,3,5)
qualifying_contacts_without_final_change count=0
```
