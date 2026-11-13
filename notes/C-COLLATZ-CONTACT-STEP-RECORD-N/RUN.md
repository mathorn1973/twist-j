# Author run record

NON-CANONICAL / L1. One scientific execution on x86_64.

Source pin: `5aef722e8f1c3d5cd3c9c25b164b5ed91f660aa2`.
Public source and contract were read back byte for byte before execution.
Preregistration SHA-256: `e03e59bc29aa6b159321805cb5a869ecba45cecc7e0b8eeec80458a79fb711fa`.
Verifier SHA-256: `0b1523cd92814fb19461c3c917a51c54fcd31fcb75081f571305884895f9e224`.

The design and arithmetic rule were known before execution. This is an exact
pre-execution-pinned finite implementation test, not a blind discovery of the
Collatz rule. The separate breaker had not read this code or output.

Command from the task workspace (the verifier reads no local data):

```sh
env LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC python3 -u contact_collatz/verify.py
```

Public repository replay:

```sh
env LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC python3 notes/C-COLLATZ-CONTACT-STEP-RECORD-N/verify.py
```

Platform: Linux-6.18.57-x86_64-with-glibc2.39. Architecture: x86_64. Python: 3.12.14.
Exit code: 0. Empty stderr: True.
Scientific stdout: 757 bytes, SHA-256 `4a234a7878fa307167be727a75cf6b6b2d4568972d7b896697468a240ee345e7`.

The 4096 skip cases use the abstract token circuit, justified by the separately
replayed six-row primitive controlled-swap contract. They are not 4096 full
primitive-word replays. The eight complete trajectories and 80 occupied
continuations, and their inverses, replay the actual primitive word.

Ordinary repository integrity CI does not scientifically execute notes/.
This single-machine result does not satisfy a public two-architecture
computation gate or independently close any Canon owner.
