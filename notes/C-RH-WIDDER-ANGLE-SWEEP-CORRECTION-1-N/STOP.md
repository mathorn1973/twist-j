# Integrity stop

```text
DECISION:         STOP
STATUS:           NON-CANONICAL / NO SCIENTIFIC RESULT EARNED
PUBLIC BASIS:     Public Canon v57
ISSUE:            #477
BRANCH:           notes/c-rh-widder-angle-sweep-correction-1-n
FORMAL VERIFIER:  NOT RUN
CANON MOVEMENT:   none
```

## Sequence preserved

```text
1. Issue #477 opened on current Public Canon v57.
2. Branch created from main e6845b96fc19a47c473761ad49d4f8a7812c2f58.
3. PREREG.md committed and remotely read back.
4. break.py committed and remotely read back.
5. The breaker executed exactly once:
     exit 0,
     stderr empty,
     stdout 652 bytes,
     stdout SHA-256
       a0e838a691ac3e9f946d226df0f8ef6b3eb99e0a8882a13c7f02be22330cd9f0,
     BREAKER FINDINGS 0/10.
6. PROOF.md and the accepted verifier were written.
7. The verifier remote readback did not match the locally frozen accepted
   verifier hash.
8. The verifier was not executed.
```

## Mismatch

The accepted verifier was frozen locally before the write as:

```text
bytes:          9397
SHA-256:        adbf8ca21c5360a3237edfc0260b8a1b7e09107a8cb1448ea956b849bf2cecb1
Git blob SHA-1: 98b64b9b1477e7c5ba7c7bf185fd0d240b24063c
```

Remote readback returned:

```text
Git blob SHA-1: 98973ce7a5895e7b63a8f1ecd9c45c561ca525fc
pin commit:     24e2d845fa4b1e7ace22327fad219f109014c367
```

The mismatch triggers the repository stop condition. Its cause is not inferred.
The remote verifier is not interpreted as the accepted verifier merely because
its visible text resembles the intended source.

## Consequences

```text
EXPECTED.txt: absent
RUN.md:       absent
RESULT.md:    absent
PROMO.md:     absent
candidate-T:  not earned by this lane
candidate-C:  not earned by this lane
RH:           unchanged and open
```

The exact mathematical correction remains exposed preparation:

- the arbitrary-level endpoint criterion in the handoff audit has a concrete
  rational counterexample;
- exact resonance requires `floor(pi/(2 theta))+1`, not an unconditional use
  of `ceil`;
- the owner depths 2 and 32 are unaffected;
- the finite-prefix family is a written proposed theorem.

None of these is promoted or graded by this stopped lane. The original handoff
audit remains unchanged as an independent record. A future retry requires a
fresh issue, identifier, branch, preregistration, breaker pin, accepted
verifier pin, and remote byte readback. This branch is retained only as the
audit surface of the stopped attempt.
