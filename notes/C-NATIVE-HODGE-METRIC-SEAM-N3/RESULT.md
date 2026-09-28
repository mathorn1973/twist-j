# Result: typed Hodge-frame correction

Status: PUBLIC NON-CANONICAL.
Owner: #1255. Author: A. M. Thorn <thorn@twistj.com>.
Ceiling: candidate-T correction and boundary; candidate-C same-code audit.

## Correct result

N2 site coordinates are coefficients of the orthogonal Hodge frame s1,s2,s3. Their spatial Gram is

    diag(2sqrt5/5, 6sqrt5/5, 3sqrt5/2).

The three positive cover directions have exact squared Hodge lengths

    43sqrt5/90,
    67sqrt5/90,
    76sqrt5/90.

They are pairwise distinct. The tagged diagonal increment d=(1,1,1) has square

    31sqrt5/10.

Therefore the abstract regular-hexagon symmetry of the selected native cover is NOT an isometry symmetry of the actual N2 Hodge-frame target.

## Superseded predecessor statement

The rho=45/4 calculation from C-NATIVE-HODGE-METRIC-SEAM-N is exact only for a different hypothetical mapping that treats cube coefficients as the original first-three E+ coordinates. N2 does not use that mapping.

Accordingly, #1252 is superseded for the actual N2 pipeline. Its rho=45/4 selected-seam interpretation must not be cited as a native/Hodge result.

## Correct selected flat metric

In the coordinates actually used by N2 the inherited selected flat Lorentz metric is

    diag(2sqrt5/5,
         6sqrt5/5,
         3sqrt5/2,
        -(2+sqrt5)/8),

with signature (3,1). This is Hodge input, not a native derivation.

## Remaining metric debt

A genuine derivation must supply an independently justified metric-sensitive map from the regular native commutator cover into the anisotropic Hodge frame. Abstract cover symmetry cannot simply be imported as target isometry symmetry.

## Exact audit

The unchanged prospective pin d4847ca43c6b94e1095053cb2e4ad54505601e93 passed on arm64 and x86_64 with identical 497-byte stdout, SHA256 182b13e52821a1d913c4cec7cf85ef70c2a08b1ca8ef492299622b2d08c61288, exit 0 and empty stderr.

The N1 hypothetical rho=45/4 control was reproduced inside one Q5 implementation only to identify exactly where the coordinate mismatch arose.
