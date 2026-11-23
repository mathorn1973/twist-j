# Quadratic L5 native-word count

Evidence for `QUADRATIC-L5-NATIVE-WORD-COUNT` at L1.
[Canon statement and proof](../../canon/CANON.md#quadratic-l5-native-word-count-t)

The exact arithmetic checks cover the native group and the finite counts
behind the lower bound of 25 alternatives on a full ready slice (one fixed
value of the radical coordinates). The same bound applies to a fixed
residual-alphabet word satisfying the Gram identity throughout the slice.
The verifier checks the 65-element Gram cover and the 74-element selector
that also has data fibres of size at most two. The selector is a
target-derived assignment. Native register writes and continuation
remain open.

Run `python3 reproduce/quadratic-native-word-count/verify.py` from
the repository root. The verifier uses the Python standard library and
integer arithmetic. A successful run exits 0 with empty stderr and prints
all 27 passing checks in [EXPECTED.txt](EXPECTED.txt).

The verifier and expected stdout preserve the bytes of the reviewed source
note, including the verifier's description of the original note's status.
[Source #2072 at 16bfe6eeda21622e3b309a076b9369b8e970fe2f](https://github.com/mathorn1973/twist-j/blob/16bfe6eeda21622e3b309a076b9369b8e970fe2f/notes/C-QUADRATIC-MEMORY-NATIVE-WORD-COUNT-N/README.md)
