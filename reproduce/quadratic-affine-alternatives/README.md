# Quadratic L5 affine-alternative count

Evidence for `QUADRATIC-L5-AFFINE-ALTERNATIVE-COUNT` at L1.
[Canon statement and proof](../../canon/CANON.md#quadratic-l5-affine-alternative-count-t)

The exact arithmetic checks cover Gram counts, the finite ingredients of the
five-alternative lower bound and the explicit upper bounds. In the class of
K plus its two-dimensional radical, the output-isometry selector satisfies
the ready Gram identity with data fibres of size at most two. The verifier
checks the continuation flow and the explicit permutation on the
nondegenerate coordinates with one ignored bit and the identity on the
radical. The permutation uses six linear alternatives on the ready layer
and fifteen on reachable occupied states. The structural fallback acts on
unreachable occupied states. The selection and bit tables are target-derived.

Run `python3 reproduce/quadratic-affine-alternatives/verify.py` from
the repository root. The verifier uses the Python standard library and
integer arithmetic. A successful run exits 0 with empty stderr and prints
all 47 passing checks in [EXPECTED.txt](EXPECTED.txt).

The verifier and expected stdout preserve the bytes of the reviewed source
note, including the verifier's description of the original note's status.
[Source #2068 at 0ff48f747195a38e08c57ee5bf94a33315e4f112](https://github.com/mathorn1973/twist-j/blob/0ff48f747195a38e08c57ee5bf94a33315e4f112/notes/C-QUADRATIC-MEMORY-AFFINE-BRANCH-COUNT-N/README.md)
