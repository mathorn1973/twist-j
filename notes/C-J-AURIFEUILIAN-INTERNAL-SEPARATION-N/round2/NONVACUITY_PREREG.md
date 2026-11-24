# Exposed factor certificate for the index-125 obstruction

**NON-CANONICAL. NO AUTHORITY. L1. Separate exact certificate audit.**

Owner: A. M. Thorn / ChatGPT-Astra-20261124-Internal-Separation-R2,
claim #2090, draft #2092. This certificate follows the already completed
R2-M125 menu at source pin 7b50c67e16e712d5653d9f594d506eacff2d0ba7.
It neither changes nor extends that frozen search.

The table *Fibonacci and Lucas Factorizations*, mersennus.net, consulted
2026-11-24, supplies the following four exposed numerical inputs:

    minus: 2775001,
           6362780164662187387605023763432934660589177501
    plus:  13181501253515178490001,
           1339507616024322442312867213751

Sources: https://mersennus.net/fibonacci/l1000.txt at L(625),
https://mersennus.net/fibonacci/lucas.txt at L625A and L625B, and
https://mersennus.net/fibonacci/format.html for the sign convention.
This is an exposed certificate check, not blind factor discovery. Only
numerical facts are used; no table archive, prose or third-party code is
copied. No table assertion of primality is used.

Before execution, commit and read back this file and check_nonvacuity.py.
The program independently derives F_125 using the integer recurrence and
checks for each sign that the two displayed integers exceed one, their
product is exactly A_sigma(125), and their gcd is one. It additionally
outputs exact Bezout coefficients x,y and asserts x*a+y*b=1. No search
bound, factorization procedure or primality assertion is included.

Scientific stdout is one sorted, indented JSON object with a cases list,
one row per sign in the order -1,+1. Each row has sigma, A, left, right,
bezout_left and bezout_right; all fields except sigma are decimal strings.
The program has a 60-second timeout and uses only the Python standard
library. Exit zero, empty stderr and successful arithmetic assertions are
required. Any failed equality is retained as a failed certificate.

The execution is an exact audit, not independent blind code confirmation.
The displayed products and Bezout identities are standalone finite integer
certificates. Together with the complete four-unit menu result, they prove
that its inability to split either side is nonvacuous: both sides contain
at least two distinct prime divisors. They do not prove five-unit attainment
or any assertion about infinitely many composite sides.
