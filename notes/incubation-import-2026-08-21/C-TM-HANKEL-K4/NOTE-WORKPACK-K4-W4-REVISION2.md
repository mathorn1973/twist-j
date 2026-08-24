# Note: workpack K4-W4-FIBER-CENSUS, revision 2

The workpack itself is NOT duplicated into this project. Its authority is
the git copy, and this note exists so the project carries the pin and the
reason for the revision without a second byte stream that could drift.

```text
authority   mathorn1973/twistj-handoff, WORKPACK-K4-W4-FIBER-CENSUS.md
revision 2  d641785723b8ba76bb74099f6588f83b9c196bcbe72264fd4f118f68b5c744c1
            9222 bytes, verified by an independent fresh-clone readback
revision 1  0d3482fa6d27717c0a11074d2effd8cd9b048906fb1eaf87df297ea10bf4b8a3
            7674 bytes, superseded, kept in git history, never sealed against
```

## Why revision 2 exists

The owner's readback found a real mathematical gap, not a wording defect.
A weight-4 mask is two disjoint swaps, and the relative sign between the
two swaps splits the class in two:

```text
rho = +1   (+,-) and (+,-)
rho = -1   (+,-) and (-,+)
```

Negating the mask globally exchanges the two endpoints of one pair, so it
identifies (+,-),(+,-) with (-,+),(-,+) and (+,-),(-,+) with (-,+),(+,-).
It does NOT connect rho = +1 to rho = -1, and the two are not
S_4-equivalent in general. Revision 1 enumerated only rho = +1 and
presented it as the whole weight-4 class, which was half the truth. The
full class is 29478 pairs of swaps times 2 relative classes, 58956 mask
classes.

## What the measurement of the second branch showed

```text
rho = +1   free bits 1:8972 2:2916 3:216 5:15304 6:172 9:252 19:1646
           leaves 863 639 144
rho = -1   free bits 1:8848 2:2772 3:216 5:15200 6:260 9:456 19:1678
           33:48
           leaves 413 197 382 704
```

The branches are not mirror images. The rho = -1 branch carries 48
patterns with 33 free bits, 2^33 solutions each, and those 48 alone hold
99.8 percent of the census. They are not exhaustible on any machine in
this fleet, so the achievable deliverable is a complete census of 58908
mask classes plus 48 explicitly named exceptions. Revision 2 says exactly
that, rather than promising a total.

The regression witness, mask cells 21, 41, 37, 61 with tables
0x4d21ed2f85b5c190 and 0x6d21ef0f8595c190, lies in the rho = +1 branch,
so reproducing it certifies that branch only. Revision 2 labels it so.

## The process lesson, recorded

A pin must point at bytes in git, never at bytes in a session container.
Revision 1 was pinned from a container copy and the delivery path altered
the bytes on the way to the owner, which he caught by hashing what he
received. Revision 2 was authored directly in the repository clone,
committed, and then read back from a fresh clone before its hash was
quoted anywhere. That readback, not my word, is what makes the pin usable
for a seal.
