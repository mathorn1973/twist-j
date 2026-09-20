# First formal local run

pin_commit: cb8258a481a1cbf1bfe3e815c9d5cebbeaf41065
prereg_sha256: b6187ff3b6031a42294ff20e49db977f9d4e8b4f88c92fdc6fd970ef17473064
verifier_sha256: 8ee55c2d03e6871ee60a8427895abb29e8f2ce74892a3e0674c3743db12b91ae
breaker_sha256: 62b73abac792adb21a32d0e7becf33a83bd74542156f93802a65611022b5b11e
breaker_prereg_sha256: 39daee009ac2d057db2ca7f90e0479ce09dcc20cf2c26d522ee00c103c6f4b1e
proof_sha256: 84f339e9dd1970256bbfc159936425186f3765b9d73e9705423ec46c79e9b481
command: python3 probes/P-U-GALOIS-CHANNEL-OPTIMUM-1/verify.py
platform: Ubuntu 22.04.5 LTS
architecture: x86_64
python: 3.10.12
started_utc: 2026-09-19T16:02:27.692141+00:00
exit_code: 0
stdout_sha256: 9732399d5eee7a839ec55a65f7cdac982741f581dd9c19cb53769c747df52ed1
stdout_bytes: 11565
stdout_lines: 2
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0

The immutable public pin and all six source files were read back before
this first execution. The author verifier and independently authored
breaker ran in one process under the frozen 600-second bound. Only
the local x86_64 leg is recorded here. The required GitHub x86_64
and aarch64 jobs must match this same EXPECTED.txt before acceptance.
A repeated execution or different architecture alone is reproduction,
not independent code construction or a new universal proof.
