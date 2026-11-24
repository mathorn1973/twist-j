# Handoff: C-J-AURIFEUILIAN-INTERNAL-SEPARATION-N

**NON-CANONICAL. NO AUTHORITY. L1.** Promotion is not requested or performed.
Owner: A. M. Thorn. Original session:
ChatGPT-Astra-Sol-20261124-Internal-Separation.
Continuation: ChatGPT-Astra-20261124-Internal-Separation-R2.
Claim #2090, draft PR #2092, same branch and scientific directory.
PUBLIC basis: main 6f2e112aafc4f3aca4222bb4bf3dced1d79fe2ed,
verified Public Canon v117.

## Current result

**candidate-D:** all previous paper deductions retain their scope. Round
two adds a complete finite menu for every four-unit separation in the
power-of-five tower, an exact reflected menu of (h^2-1)/2 entries, and a
factor-independent integer bound on the entire proper gcd at every fixed
unit weight, even with unrestricted exponents and adaptive menus.

**candidate-C:** the prospective complete menu at m=125 returned only gcd
1 or the whole input on both individual sides. Each had 781246 unit gcds
and four whole-input gcds, among 781250 tests. Both separate source
implementations agree on all 1562500 comparisons. The completeness proof
therefore excludes every internal four-unit split at this index, including
arbitrary exponents, phases and all prime-power multiplicities.

Separate exposed product and Bezout certificates establish coprime proper
factors on both sides, so each really has at least two distinct prime
divisors. No primality assertion is needed. Thus the old minimum-four
example at m=25 does not extend to m=125: internal separation there needs
at least five units. Attainment at five is not established.

[Round-two overview](round2/README.md),
[completeness](round2/FOUR_UNIT_COMPLETENESS.md),
[unrestricted-exponent theorem](round2/GROWING_WEIGHT.md),
[opposition](round2/OPPOSITION.md), [execution](round2/RUN.md).

## Custody and review

The original index-25 pin remains
dab860c8c51ecc76da24a6960051340ad2e5d2cb. Its PREREG.md, verify.py,
break.py, EXPECTED.txt, BREAK_EXPECTED.txt and RUN.md are unchanged.
Its 31250-test and minimality audit remains candidate-C on x86_64.

The new index-125 source pin is
7b50c67e16e712d5653d9f594d506eacff2d0ba7. Its three source files were
read back before execution and remain unchanged. The two outputs have
1032 bytes each and SHA-256
e90991f9b8c2f98b03170e5270ed85894871f1cbf69242898e49d60550f88ea3.
This is one aarch64 execution lane. The earlier x86_64 run tested a
different index and is not its second-architecture counterpart.

The separate exposed factor-certificate source pin is
28d870698e0e3e30a2bbeb19a25ae71dd7e0b4a4. Both files were read back
before execution. The resulting 604-byte JSON has SHA-256
65fd5a200ac9ea083938ed1920e1727827ff6222c37a74ea152b61247faa3638.
It checks four published integer factors and outputs exact Bezout
coefficients. This is not blind factor discovery or a primality test.

Both mathematical drafts received root review and separate same-session
paper opposition. This is internal review, not external peer review. The
two main executable sources were authored independently from the frozen
specification and only cross-read after both source hashes were fixed.

Repository checks test delivery and repository contracts. Ordinary CI does
not execute these notes-only scientific programs. Their passing jobs do
not promote any result to computation-grade T.

## Remaining questions

1. Does a new prescribed five-unit family separate distinct primes within
   either individual index-125 side? The lower bound five is proved only
   as a consequence of the exact negative four-unit audit and its paper
   completeness theorem; no five-unit success is claimed.
2. Is there one universal constant weight for every same-side pair at all
   power-of-five indices? Four is excluded. The general question remains O.
3. Are there infinitely many sides with two sufficiently large distinct
   prime factors to activate the growing-weight lower bound? No such
   infinitude is assumed or proved.

The number and cost of tests remain distinct from their unit weight.
The universal proper-output bound does not bound a product of many
separately extracted small factors. No efficient general factoring method,
physical decoder, RH conclusion, Canon change, merge or promotion follows.

Any further finite search needs a new prospective specification; neither
completed source pin may be extended or silently reinterpreted.
