# Independent numerator/cascade breaker freeze

Status: NON-CANONICAL / L1. Candidate
C-CONTACT-AFFINE-NUMERATOR-CASCADE-N. No authority or Canon promotion.

Owner: independent child session `/root/synthesis_breaker`.

## Frozen sources and order

The implementation was written from PREREG.md alone. The breaker did not
read or import the author's new verify.py, stdout or current states. The
parent author must not open this implementation before the present freeze.

- PREREG.md SHA-256:
  `fc85714e88ad9940ff31cdc6165fa541104543f0841c83f5b2ce1a7491574419`.
- Frozen blindbreak.py SHA-256:
  `afee2a28b67f357c03ab9f23e38484d6fe52de6d59ed97a81c5f57e8d1b612e7`.

Only syntax compilation with `python -m py_compile blindbreak.py` occurred
before this freeze. No contact, word constructor, multiplication, reader,
test case, or source formula was executed. The frozen source and this scope
must have public byte-identical readback before the first scientific run.
No executable change is permitted to repair a failed attempt.

The intended command after public pin and authorization is

    python blindbreak.py --boundaries-out break-boundaries.json

## Independent arithmetic and reading

The implementation uses the integral basis `(1,rho,rho^2,rho^3)`.
General multiplication is a cyclic length-five convolution followed by
elimination of rho^4. Primitive rotation uses a separately written integer
matrix. The matrix and convolution agree on every encountered pair
difference. The account is evaluated through the Gram expression
`2*sum(ai^2)-sum(i<k,ai*ak)`, not by the author's j-basis closed formula.
Current-state conversion to canonical j coordinates is
`(a,b,c,d)->(a-c,d-c,b-c,-c)`.

The word is exactly the 15 edges `(0,1),(0,2),...,(0,15)`. Its ASCII edge
digest includes `i,j\n` for every edge and the final newline. The q=3
boundary digest is compact JSON `[[n,state],...]` with no final newline,
in increasing odd n order. Each state has all 16 slots, each in four
canonical j-basis integer coordinates.

The independent reader is passed only the active slot and the thirteen
current cascade slots. It cannot access n, q, old archives, or source and
reference leftovers. It finds the nonzero prefix, flags all-thirteen
saturation, normalizes by the explicitly frozen integer unit J inverse,
and verifies membership in the u-integer chart before returning the
constant coefficient and depth. This normalization is a reading operation,
not an additional contact or a physical source-reset operation.

## Exact frozen audit

The program checks the two synthesis stages separately, all final source
and cascade formulas, actual admission/refusal prefixes, complete sums and
accounts, the output-only reader, arithmetic recovery, and complete native
inverses for:

1. All 2048 odd q=3 inputs through 4095, including coverage of every depth
   1 through 12.
2. All 576 q=1..9 and odd n=1..127 cases, including the 256 depth-zero
   cases from the four even gains.
3. All 225 declared occupied-archive cases, preserving both labelled prior
   values and the entire extended state and account.
4. The one q=3,n=5461 saturation witness. It must return DEPTH_LIMIT, retain
   an even active value and thirteen nonzero stored values, preserve the
   full state accounts, and invert. It is not counted as a successful
   positive arithmetic readout.

Every distinct ordered primitive pair encountered in forward and inverse
replay is audited for pair sum, pair Q, both labelled residues, C^5=id,
and the exact four-contact inverse. Every full inverse explicitly uses
the reversed edge list with four contacts per edge. Exact primitive caching
does not skip word replay or current-state comparisons.

The symbolic strict-source-reload obstruction may be reviewed separately.
It is not an extra executable test or a change to this frozen audit.

Any exception, timeout, source-hash mismatch, changed archive, formula or
reader mismatch, positive depth overflow, missed saturation, or native
inverse failure is retained as a failed attempt under the original contract.
Both implementations on this host are one x86_64 architecture. Their
agreement is not the public two-architecture scientific gate, and ordinary
repository integrity CI does not replay notes-only science.

The declared coherent source, chosen gain, common reference and fresh finite
cascade are premises. No clean raw source, identical source/output chart,
reloaded source, renewed bank, indefinitely repeated arithmetic step,
native-U realization, measured energy/time or occurrence law is claimed.
