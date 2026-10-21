# First local formal run

pin_commit: edfedd7e75c515d6d318032f526f381f66317da3
command: python3 probes/P-INTEGER-AUTONOMOUS-JOINT-ENERGY-1/verify.py
verifier_sha256: e06f99beda7e7b9cc4c86df49e4ae18d497ff5faed5d9548eb2550e74338c016
platform: Linux-6.18.55-x86_64-with-glibc2.39
architecture: x86_64
python: 3.12.14
exit_code: 0
stdout_sha256: ab1a15571a69961896471aa2212771fdf379afbc9a06837b1d4c3aa30ddad42e
stdout_bytes: 808
stdout_lines: 29
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0

started_utc: 2026-10-19T15:33:19.377707+00:00
completed_utc: 2026-10-19T15:33:25.510406+00:00
prereg_sha256: ad0393b79582111668fde21cbcbe0cc0724aea1b89f1fa9facc3849b3cb09331
proof_sha256: 7ecbdb61f1718b9ec0bf363088a212deadb8b8d10e4a16ea372cb0a1e605dd06
source_sha256: 8885266f0921770c580bca57f438fc7042103ea3f71832f3a8f6d73975003f14
breaker_sha256: 92ce0a55605f6715b475492560259ad905bbcf515905ded28e977bce581af092
frozen_manifest_sha256: 44fd6cfe32a3521799096b07ba072f7a649536686fc780659d9bc3867089729b

## Execution custody

This was the first scientific execution of either pinned implementation.
All six prospective files were published and read back from GitHub at
edfedd7e75c515d6d318032f526f381f66317da3 before execution. Each fetched
byte string matched its local original. The local index and commit tree
both equalled 64163b38553dba2b1fd2382966b8db8ddbe2f78b, all six Git
blob comparisons matched, and the owned checkout was clean at the pin.

The public prospective pin receipt was posted at 2026-10-19T15:32:50Z
and read back before the run began:
https://github.com/mathorn1973/twist-j/issues/1649#issuecomment-6270996681.
No new scientific source was imported or executed during authoring or
static review. No expected output or computed history digest existed
before the pin. The parent is Public Canon v103 main
dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d.

The connector's previously disclosed account privacy email appears in
the author and committer metadata, both read back as A. M. Thorn.
The pin was preserved without history rewriting.

Environment: LC_ALL=C, LANG=C, PYTHONDONTWRITEBYTECODE=1,
PYTHONHASHSEED=0, TZ=UTC. The primary command used the Python executable
reported above by version and architecture. It launched breaker.py with
the same executable and -I in a separate process. The successful primary
return requires child exit zero, empty stderr, and exact raw identity
of all 768 bytes of the shared 27-line certificate, including final LF.
The certificate SHA-256 is
4a87f32901b0e472f4b402eb8bf8daf1d1dd573fde52a20f72655dc3a160e4a1.
The primary then appended its two terminal success lines to produce
the 808-byte, 29-line stdout.

The first stdout and stderr were captured as bytes before any result
file was written. EXPECTED.txt is the unmodified first stdout; its hash
was checked against that capture before and after copying. No stripping,
newline normalization, manual certificate editing or output replacement
was used. The first run completed with PASS and no preregistered falsifier.
No frozen file changed after the pin.

## Required architecture gate

This file records the observed first local run only. The draft PR's
unchanged Python 3.12 workflow must replay this same verifier and child
on x86_64 and aarch64 against the same EXPECTED.txt. Actual workflow and
job receipts will be recorded in the PR and public completion comments
after observation. This local x86_64 result alone does not assert that
the two-architecture gate has passed.
