# Pre-execution wording correction

Before any execution, correct the phrase `dark cell0 count at n1` in field5
of PREREG.md to `cell 1 count equal to 0 at n=1`. Field3 and the already
pinned verifier both specify cell1, with counts[1]==0. This is a wording
correction only. No input, code, threshold or interpretation changes.
The original PREREG and PIN.json remain intact; this addendum is separately
hashed in RUN-PIN.json before the first execution.
