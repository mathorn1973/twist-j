# First formal local run

pin_commit: 1293b52ba13dee35fff1c40ed02fe21523b61b57
prereg_sha256: 6fc94eb99e75f4b178ed47ebc7f68e9b762dd999cf20f622b2c69ef77dc02609
verifier_sha256: 96a5b86448ed10333de9e1e126c55f5365d09e917b65367652c9baa4aecf40e3
command: python3 probes/P-J-C5-HODGE-CONIC-ATLAS-1/verify.py
platform: Debian GNU/Linux 13
architecture: x86_64
python: 3.13.5
exit_code: 0
stdout_sha256: d11c3e1a88ef8ad87d0859d50752d9a23954876fe4055af686eb2b985c90ac9b
stdout_bytes: 302
stdout_lines: 8
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0

The pinned verifier was reconstructed from the public GitHub blob and its Git
blob SHA and SHA-256 both matched before execution. This is one x86_64 lane
only; clean GitHub x86_64 and aarch64 jobs must replay the unchanged verifier
against the same EXPECTED.txt before computation-grade acceptance.
