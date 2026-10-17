# P-FIELD-CHAIN-UNIT-SEED-1

Status: ABANDONED

The frozen preregistration pin is
066ef45911f6215f7574daba80fd53616ee1c66d (PREREG.md SHA-256
7b83fad72421105a3a965679b4283bbe5a6f7206672e1af3f039913049a8d0cb,
verify.py SHA-256
abd037a045b1a8216bd9864e94ddccb70f707a608074c3677deabfe9a1c29489),
read back byte for byte before execution. The formal gate was started
once, on Ubuntu 22.04.5 LTS x86_64, Python 3.10.12, from the repository
root, and never completed: exit code 1, empty stdout, stderr reporting
`AssertionError: SOS identity fails` at the sum-of-squares coefficient
comparison.

Root cause is a verifier fixture defect, not a mathematical result.
The sum-of-squares expansion accumulates a (c*d) coefficient whose two
contributions cancel to an explicit dictionary entry 0, and the frozen
code compares dictionaries without removing zero coefficients, so the
identity check raises although every coefficient of the identity in
fact agrees. No enumeration ran and no scientific conclusion of any
kind is produced by this probe. No EXPECTED.txt and no RUN.md exist,
because no completed run produced either.

The identifier P-FIELD-CHAIN-UNIT-SEED-1 is consumed and must not be
reused, renamed or resumed. The unchanged scientific content is
retargeted under the successor identifier P-FIELD-CHAIN-UNIT-SEED-2,
which names this abandoned predecessor in its own preregistration
before its own pin.
