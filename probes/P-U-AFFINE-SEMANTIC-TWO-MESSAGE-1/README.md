# Affine two-message reading from origin zero

PUBLIC / NON-CANONICAL / L1. Author A. M. Thorn, Apache-2.0.
Owner Codex-20261016-affine-semantic-two-message; issue #1542.

Changing the preparation, while retaining the weaker common-semantic-blank
contract, admits a fixed affine pair on unchanged native U from n=0.
The preparation is itself affine:

    r=3(1+mu-lambda), E=(3mu,3,3mu,2,2-mu-r,r).
    X=a+b+c-d-1, H=2a+b+d+q+r-2.
    decode(X,H)=BLANK if H=0, else PRESENT(H^2 X).

All arithmetic is in F5. The actual prefix is c,c,e, with raw values
(mu,0),(-lambda,3),(mu,0),(-mu,3). PROOF.md proves permanent second
readback, including mu=0, by the preserved invariant2ACz. REVIEW.md supplies
a separate agent's formula-exposed analytic review and exact150-point support.
The second message is already visible in the raw initial pair while the
decoder calls it BLANK. This is NOT a common raw-ready receiver contract.

The six preregistered falsifiers are checked by two newly authored exact
implementations: direct generator tuples and parameterized tails versus
affine matrices and a full native-state scan. Freeze/public readback precedes
the first run. Both implementations know the formula; this is not blind.

    python3 probes/P-U-AFFINE-SEMANTIC-TWO-MESSAGE-1/verify.py

The earlier550-state family's affine impossibility and sharp degree2 result
in #1536/#1541 remain unchanged. Here the minimum degree is1 and minimum
number of F5 coordinates is2. No enumeration of all row spaces is needed
for this affirmative witness. No physical detector, access selection,
disjoint-sector transfer, fresh information, source clearing or Canon change.

The user's reported third audit of #1541 remains unavailable in this session
and is not treated as checked evidence. No old audit is imported or rerun.
