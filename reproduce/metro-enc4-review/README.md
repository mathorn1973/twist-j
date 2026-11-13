# Supplemental ENC4 review fixtures

Run `python3 reproduce/metro-enc4-review/verify.py` from the repository
root with Python optimization disabled. The exact standard-library
program imports the existing probe's generator and checker for the
values under test. Expected aligned limits, transport maps and stream
values are constructed separately on the declared fixture surfaces.

The reproduction compares the complete set G in 192 binary permutation
cases and one active two-axis product. It checks 22 reduction fixture
transports through indices 0..15 per coordinate and compares their
certificates. The six forms are relabeling, reachable restriction,
Nerode quotient, coordinate permutation, common blocking under Pre_blk,
and initialized MSD blocking. It also checks an MSD transient positive
tail against an exact zero family, normalization after box averaging,
and two quotient/spectral cases with directly derived expectations.

These are finite supplemental checks of the proposal. The public
probe and its prospective run records remain unchanged. The exact
expected output is in EXPECTED.txt.
