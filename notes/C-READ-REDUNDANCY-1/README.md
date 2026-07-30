# notes/C-READ-REDUNDANCY-1

NON-CANONICAL. Incubation-lane candidate bundle, 2026-07-29. Nothing here
is evidence for a public claim, and no file here closes, moves, or anchors
`MINIMAL-READ-DERIVATION [O]` or `COIN-MINIMAL-READ [H]`. No formal public
probe exists for this candidate: the bundle's runs predate any public
preregistration pin and were executed on one platform, so they cannot serve
a `probes/` directory. Read `MANIFEST.md` first.

```
MANIFEST.md                                 bundle identity, basis, files,
                                            reproduction, falsifier
PREREG-C-READ-REDUNDANCY-1.md               the six frozen prereg fields
                                            sha256 334cb3bf9ef6feaccaa7e48c809e0f2f880c6686c025eee96474fb31c743d0d2
verify_read_redundancy_1.py                 verifier, 13 checks, stdlib only,
                                            int and Fraction, no float
                                            sha256 3febde99b4f0c328452bf435406b689a24343c576959f58368b96107b6e5fdcf
verify_read_redundancy_1.stdout.txt         pinned stdout, exit 0, 13/13 PASS
                                            sha256 05d567dc19a3705e7de6fcae4a91cc85964c1b2207d7c2da4fead959d901f3ef
break_read_redundancy_1.py                  independent break path
                                            sha256 ac22ddb164d3d835d0f7bac32ea9e33f62f9b2bbc0ec49ce0aec49f347229482
break_read_redundancy_1.stdout.txt          pinned stdout, exit 0,
                                            NO FALSIFIER FIRED
                                            sha256 4e4aa7b5b1f7ac0fac1f8df754ec68774d4ac55176103cbd655e35dd54b3f2da
C-READ-REDUNDANCY-1_RESULT_2026-07-29.md    result, candidate labels only,
                                            break round and residuals
PLAN-DECODER-SECTOR-POST-V27_2026-07-29.md  the sector plan this candidate is
                                            workstream A of
SHA256SUMS.txt                              hashes of the bundle as shipped
```

## Verification

The bundle files are tracked byte for byte as shipped, so `SHA256SUMS.txt`
still verifies. It also lists `PROMO-C-READ-REDUNDANCY-1.md`, which is a
proposed Canon patch and therefore lives at
`notes/canon/PROMO-C-READ-REDUNDANCY-1.md` under POLICY section 5. Check the
bundle and the promotion proposal separately:

```sh
cd notes/C-READ-REDUNDANCY-1
sha256sum -c --ignore-missing SHA256SUMS.txt
grep PROMO SHA256SUMS.txt | sed 's#PROMO#../canon/PROMO#' | sha256sum -c -
```

Reruns use the declared environment, from this directory:

```sh
env LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
    python3 verify_read_redundancy_1.py
env LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
    python3 break_read_redundancy_1.py
```

A rerun that differs in any byte is a finding and must be preserved, not
repaired.

## Status of the result

The candidate answers route precondition 5 of
`notes/canon/ADOPT-COIN-MINIMAL-READ-2026-07-29.md` section 5 in split form:
absence of feedback alone bounds nothing, while anonymity plus totality bound
admissible multiplicity by the prime support of the constant ring. Every label
in `C-READ-REDUNDANCY-1_RESULT_2026-07-29.md` is a candidate label. A public
probe would have to preregister and pin first, then reproduce byte-identically
on two architectures; until then a computation-only row is at most `C`.

The fold proposal is `notes/canon/PROMO-C-READ-REDUNDANCY-1.md` and changes
nothing until a separate sealed public fold.
