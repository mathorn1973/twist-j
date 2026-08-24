# RUN record: two-platform pin 2, the k = 3 closure bundle

DATE 2026-08-11 (UTC). Incubation-lane record, no authority. Completes the
evidence bundle of C-TM-HANKEL-XOR-DEFECT-1 per the closure order of
ADDENDUM-6 (N4). Legs as in RUN-TWO-PLATFORM-PIN_2026-08-10.md:
leg 1 Ubuntu 24.04 x86_64 Python 3.11.15; leg 2 Debian 13 aarch64
Python 3.13.5. Transfer by four SHA-verified chunks; every file hash
verified against its pin BEFORE execution:

```
verify_tm_hankel_xor_defect_4.py  b1178bf5d6a325cbae37a1080c15a8e53b9c47ba4a08fc5777ed42f895afd338  OK
verify_tm_hankel_xor_defect_5.py  c2781d1796ad3168fa3da3b3a03473e5a1821a97f69d132d0c1fef39d08cf3c5  OK
verify_tm_hankel_xor_defect_6.py  49fb97765f75c067f669866fd2ba00becd19c187c16042b5647d0a213c7339a8  OK
verify_tm_hankel_xor_defect_7.py  417c8f680c93539b94803ff8fff1de08e71dcd095c780a05dc3da2b80591db7e  OK
witness_d9_falsifier.py           e17e4334596fe9b821d95d27356612b71d64c23750e7c033cba80a243dfd1d01  OK
```

Results, leg 2, byte identity against leg 1:

```
verifier                          exit  ms(leg2)  stdout sha256 (BOTH legs)
verify_tm_hankel_xor_defect_4.py  1     11944     50a508399dea10643ddd7dcd1f4b923dc48a54e9889b9ecef9c1df0816bf75d5
verify_tm_hankel_xor_defect_5.py  1     14457     c65c268958ea71997c56de9c289396b8fe756813eef36ba8a38e563a7bfbaea3
verify_tm_hankel_xor_defect_6.py  0     24843     570bb07440f44e870860c1d050d0db39076140a8db71b9b755d15544701106b8
verify_tm_hankel_xor_defect_7.py  0     1243      996a3320b613a48042d5151d6b6756f7c8e32cf37c7e6f1c3e4b5b9b05e72143
witness_d9_falsifier.py           0     500       62c7e631bbf73b3b9af2a215c62c59d1a6b413d7dbe9a88bf4b7b32fe4680a06
```

Exit codes 1 on v4 and v5 are the SEALED hypothesis firings (D8/D9 at
k >= 3; L1 rigidity), reproduced bit for bit on the second architecture,
including the firing lines. Every stdout is byte-identical across legs.
With RUN-TWO-PLATFORM-PIN_2026-08-10.md this closes the two-architecture
evidence for all ten pinned verifiers and the witness script of the two
candidates. Labels unchanged; promotion still goes through the public
probe protocol.
