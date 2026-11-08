# Exact local run records

NON-CANONICAL, L1. One architecture only. The execution environment was
Linux x86_64, Python 3.13.5, standard library only. Both commands were executed
with PYTHONHASHSEED=0, TZ=UTC and LC_ALL=C.UTF-8. Neither scientific program
was run on the separate repository publication host. Remote execution of
repository integrity checks is not a scientific architecture leg.

## First audit

pin_commit: 9c984ee82b8779ef2997355bc5985a00e261b35c
command: python verify.py
platform: Linux
architecture: x86_64
python: 3.13.5
prereg_sha256: 0b1079cea87f829a55cdcc875c5f1c5a3bcbc5df444451df90b18e5882988451
verifier_sha256: f69715021956ed33b74671dfb2a4fd391279af694187a8c9d0b02542001be29e
exit_code: 0
stdout_bytes: 909
stdout_sha256: 43a4e1cc9dca9d2d888b4f3e3c9b55ad7d2e536e25b8c37cdb078acf2b40e65b
stderr_bytes: 0
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855

The public GitHub readback and byte hash were checked before local execution.
The displayed analytical predictions were already known before preregistration.

## Second implementation

pin_commit: 749ef40745bbc794184aae519c8b89869131c288
command: python second_audit.py
platform: Linux
architecture: x86_64
python: 3.13.5
prereg_sha256: e7ed23a2f9996a570c184ef94773af6b8d641aa065b6c8bdcd8ef31e0f5b2789
verifier_sha256: 1d86b2bc493559c1a853b5593a642f7a3b0b219a0b8712074cdee1efe9cf4a27
exit_code: 0
stdout_bytes: 370
stdout_sha256: ca5fe4cd1a4f22a287a17577118d4dbeeb1489415c473b3e76f408db56501f08
stderr_bytes: 0
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855

This is a same-session, result-exposed second implementation, with no import
of verify.py. It is not a blind independent-agent check or a second architecture.
No failed scientific run occurred. Local network retrieval was unavailable;
code was transferred from the published/read-back text with exact frozen hash
verification, not executed from a different source version.

## Reproduction

From this directory, with Python 3.11 or later:

    python verify.py > actual-replay.txt
    cmp actual-replay.txt ACTUAL.txt
    python second_audit.py > second-replay.txt
    cmp second-replay.txt SECOND-ACTUAL.txt

Do not commit temporary replay files. The original programs and preregistrations
are unchanged from their pins. Ordinary repository CI does not execute these
notes-only scientific programs and cannot be cited as their two-architecture gate.

## Publication readback

During this session main advanced to 5f20429944b409d912202d141e158fdfec145c41
by the unrelated P-INTEGER-FIXED-DURATION-BOUNDARY-1 probe. The authority files,
entire canon directory and resultant-seam predecessor are byte-identical to
the frozen basis. Both architecture jobs and the aggregate check on the new
main pass. The scientific inputs therefore remain unchanged; no rebase,
rewriting of the pre-execution pins, or implicit new scientific premise occurs.
