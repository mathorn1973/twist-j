# PROMO-C-U-NONLINEAR-TWO-MESSAGE-READOUT-N

Status: NON-CANONICAL, candidate-T proofs / candidate-C audit, L1.
No request for immediate Canon inclusion. Independent review pending.

## Source identity and first execution

Public main basis: b79143fb00839b870686f6cea34e174959060df1.
Public Canon v101, tag canon-v101, content
421a4ec1daf07c04d19022c1ee219607e83c09a8; canon/CANON.md verified this
session at 992352 bytes with the STATUS-declared SHA-256.
SOURCES.sha256 pins the consumed public files.

Input pin: d085d7ad63401619911bd26a2da09df06be5a047. The five inputs
were publicly read back byte for byte before the first lane execution
and remain unchanged. First stdout and environment are in EXPECTED.txt
and RUN.md, including the disclosed Windows CRLF versus repository LF
framing note. Conversational throwaway runs preceding the lane are
disclosed in PREREG.md and are not counted. No blind-prediction or
external-independent claim is made.

## Candidate statements and their failure conditions

1. ORIGIN-ZERO-NONLINEAR-READOUT: PROOF sections 1-3. Fails on any
   admitted pair, prefix formula, reset equality, sector identity,
   tail invariant, reader value, or completion inverse mismatch.
2. AFFINE-DIMENSION-THREE: section 4. Fails if the direction facts
   (linear part of `c` fixes both message directions; linear part of
   `e` is `-I`) are wrong, the rank argument has a gap at dimension 2,
   or the displayed `F5^3` map collides two labels on the required set.
3. QUADRATIC-CODE-BOUNDARY: section 5. Fails if the exact F5 systems at
   degree 2 are in fact consistent in either named code. Makes no
   claim about a general quadratic pair with arbitrary decoder.
4. ACCESS-CLASSIFICATION: section 6. Fails if the 550-point set is not
   exactly the visited set of the actual orbits, or any subset verdict
   is wrong; the receiver-block witness pair at `n=1` is checkable by
   hand from the displayed formulas.

## Independent-review contract

A distinct owner should independently derive the formulas and author a
breaker from the frozen definitions in PROOF.md and PREREG.md before
reading verify.py, freeze that breaker's preregistration and code in
Git before its first run, record first stdout and negative results,
and only then compare with this primary implementation. Re-running
verify.py is reproduction only; a Linux replay additionally retires the
CRLF/LF note in RUN.md. Prior exposure to the claimed outcomes must be
disclosed. The review should in particular attack: the distinction
between receiver-value reset and receiver-state reset (the #1520
contract), the pre-loaded character of both messages, the arbitrary
table decoder used at affine dimension 3, and whether the required set
really exhausts the actual Thue-Morse orbits.

## Explicit exclusions and preservation

No second-message insertion, source depletion, funded contact, energy
accounting, physical instrument, probability, or layer lift is claimed.
Nearby #1520/#1524, the canonical one-shot transfer theorem,
#1527/#1528, and the #1506 funded-device program are credited and
unchanged. Any formal audit probe or later Canon fold is a separately
named task following POLICY.md and AGENTS.md, with no reused pin or
moved threshold.
