# RUN: P-J-HODGE-COUNTER-CARRY-FACTOR-1

pin_commit: 78fe0ca9d2e904fed569db3e90487f27eeabc525
verifier_sha256: 58db6d7a9f86c287baf6569322acbe3bde413448805fa443bfde6182c5e87fe2
command: python3 probes/P-J-HODGE-COUNTER-CARRY-FACTOR-1/verify.py
platform: Debian GNU/Linux 13 (trixie)
architecture: x86_64
python: 3.13.5
exit_code: 0
stdout_sha256: da48ca7e9b01dcf3518e17d5645ba6e76de45ade3b417d7d6a78172bf99c7c58
stdout_bytes: 460
stdout_lines: 12
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0

prereg_sha256: 13b6d1dceadedb0178c49cb6cc27650e57de84902ffc21f23982cbce8b36e91c
proof_sha256: 4ec12b98f7f9d30fc3793387a8142c636a42038172d517407847ec21d5c3b335
prereg_git_blob: 7e35138a42784976d320bbf265b1dc7a3baf4130
proof_git_blob: d53670517cdfd13aade82378000a75ae2a7ed5bc
verifier_git_blob: bb3d8af342b360df0b2205ffa8b5adae0dff262d

The first scientific execution followed public readback of the atomic
PREREG/PROOF/verifier pin and exact verifier Git-blob identity. It used
TERM=dumb, LC_ALL=C, LANG=C, PYTHONDONTWRITEBYTECODE=1,
PYTHONHASHSEED=0 and TZ=UTC.

EXPECTED.txt is the actual stdout. This is one local x86_64 audit lane. The
all-n claims are carried by PROOF.md, not the finite audit. Required clean
GitHub x86_64/aarch64 replay and aggregate check remain the computation gate.
