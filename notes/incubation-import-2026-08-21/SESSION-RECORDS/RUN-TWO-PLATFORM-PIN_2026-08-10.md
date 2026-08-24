# RUN record: two-platform pin of C-TM-WALSH-INERTIA-1 and C-TM-HANKEL-XOR-DEFECT-1

DATE 2026-08-10/11 (UTC night session). Incubation-lane record, no authority.
Fired on owner directive: "two-platform pin obou kandidatu bych odpalil."

## Platforms, neutral fields

```
leg 1   Ubuntu 24.04, x86_64, Python 3.11.15   (the session that wrote and
        first ran every verifier; two byte-identical runs each, recorded in
        the candidate docs)
leg 2   Debian GNU/Linux 13 (trixie), aarch64, Python 3.13.5, 4 cores
env     env -i PATH HOME LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1
        PYTHONHASHSEED=0 TZ=UTC python3 <verifier>
```

## File transfer integrity

The five pinned verifiers moved to leg 2 as one tar.gz in base64. A first
single-blob transfer corrupted (19220 of 19224 bytes) and was DISCARDED; the
bundle was then moved in four chunks, each chunk SHA-256 verified against
the local value before assembly, and every extracted file SHA-256 verified
against its pinned hash BEFORE any execution:

```
verify_tm_walsh_inertia_1.py       0b56ebd126c876f2de98b737820b22890074ab88f248f47a90f1b74fa1efd646  OK
verify_tm_walsh_inertia_2.py       7a8e4e14aec22ac10f200cffabd98dc354f9e948f5cc32c3cd1862ab6bd10929  OK
verify_tm_hankel_xor_defect_1.py   c72b5cd7e3da6e67654fb22be22f3f54fc6cf31d6cf080f77f595f48ad979462  OK
verify_tm_hankel_xor_defect_2.py   ae97ddb51aecd72580ff339f6512e8a978ecd80af7576b686ed51c7cb07bec79  OK
verify_tm_hankel_xor_defect_3.py   0cf742249a3c200342d8915a0c3c9d08740a10c7e8edba563529ebbe98c007c0  OK
```

## Results, leg 2, and byte identity

```
verifier                          exit  ms(leg2)  stdout sha256 (BOTH legs)                                        bytes  gates
verify_tm_walsh_inertia_1.py      0     1884      e918be46b17cb03fce9ea21a66a4167ab87fcfaba571f52951cf4abd4bfac40a 3257   47 PASS 0 FAIL
verify_tm_walsh_inertia_2.py      0     1855      537af5c7da7140bfc6b2d58a05b48d043bc9755533d82abe670abd7e89b98971 3516   47 PASS 0 FAIL
verify_tm_hankel_xor_defect_1.py  0     4421      421a1de10f27b2b006e4749e2d69709fd9323a0b6a5927f02f4c497f1d47bb15 3963   29 PASS 0 FAIL
verify_tm_hankel_xor_defect_2.py  0     1308      2967fa167a11e8b25a6cceb736cbfa6a179a9aa7acce16d6b04325b9bec86251 589    12 PASS 0 FAIL
verify_tm_hankel_xor_defect_3.py  0     1109      3ea63d8b88bc8166d319d997a1a179fcd2333497c189590c9537cda69e515b5a 695    8 PASS 0 FAIL
```

Every stdout is byte-identical across the two legs: different architecture,
different operating system, different Python minor version, identical bytes.
All runtimes far under the 120 s budget on both legs.

## What this record does and does not do

It satisfies, at incubation grade, the two-architecture byte-identity
requirement that the public protocol demands of computation-grade claims.
Labels do not move: proved rows stay candidate-T, computed rows stay
candidate-C. Promotion still requires the public probe protocol (repository
pin of PREREG and verifier, fresh runs, GitHub x86_64 check, sealed fold);
this record is the evidence a fold can cite, not the fold.
