# A: earlier fixed-branch restoration response

NON-CANONICAL / NO AUTHORITY. L1, candidate-C finite result.
This executes only section A of the frozen preregistration at
53bc0c11b51d671f85977117a2b8df74f2b0698c. No native restoration,
changed-branch obstruction or universal apparatus impossibility is claimed.

## Result

Both permitted impulses, after B at column4,row0,t89 and t90, have
the same exact terminal response v. In the ordered eight radiation slots
(source0 row0 CLK,CORR; source0 row1 CLK,CORR; worker6 row0 CLK,CORR;
worker6 row1 CLK,CORR), all entries vanish except:

| Slot | 32 v |
|---|---|
| worker row0 CLK | (0,-2,-1,-2) |
| worker row0 CORR | (20,-1,12,14) |
| worker row1 CLK | (-6,-2,-3,-4) |

The target has only worker row0 CORR nonzero, u=(6,3,0,6).
Each single system and the pair system has coefficient rank1 and
augmented rank2 over Q(j). Therefore no field amplitudes solve the
restoration equations. Nonzero amplitudes and eta-scaled integral
amplitudes are consequently excluded without a separate lattice search.

A compact exact certificate is the row functional with
lambda_CLK(6,0)=(-5,-5,1,-9), lambda_CORR(6,0)=1 and all other
coefficients zero. It satisfies lambda(v)=0 and lambda(target)=u!=0.
Equivalently, the nonzero CLK(6,0) component forces the sum of the two
amplitudes to vanish, which also annihilates the entire response and
cannot produce the target.

The positive incoming CORR at both events is (5,0,14,-4); all four
negative inputs have common incoming value (7,-2,12,-2). Thus the
failure is not absence of local input distinction. It is the inability
of these fixed-branch radiation responses to restore all required slots.
The opposite CLK impulse at the injection cell is included explicitly.
All actual C admission decisions and B tags belong to the unmodified
positive reference history. No parity test is applied to a rational
perturbation, and no altered native branch is simulated as this response.

## Verification and custody

The script reconstructs all five bare preparations and executes native
histories through114, checking complete linear and Hermitian accounts,
post-C and full cuts, and exact inverses. The common Q is2630.
The fixed radiative operator reproduces the actual positive radiation
history at all114 full cuts before it is used for perturbations.
Exact field row elimination produces and directly checks the certificate.

The response verifier was committed before execution at
4c859a0a86b51064081e808d2c62aa91da84ce11. The command from repository
root was:

```sh
python3 notes/C-H3-CLOCK-CONTACT-N/response.py
```

Initial informal run: Linux, x86_64, Python3.12.14; exit0, empty stderr.
This is one architecture, not independent external confirmation or a
formal public gate. No further computation was needed after the exact
inconsistency certificate.

| File | Bytes | SHA256 |
|---|---:|---|
| response.py | 12563 | 12c966ca69084d6bc7fa592519e15dca60059cb736a17560e92403b6344e6427 |
| RESPONSE.txt | 3130 | d5de448664deb0da0124731c2eaa7736221e27f4fd8e12e0dc46e1c6a29f4893 |

The native law SHA256 is
4553945d3bf32574ffd55de917859497e9644394f506aaf01ff9492adb8eeedd.
The bare preparation is reconstructed from base() in the predecessor
verifier at f96db81df668f138d7242ddfa2c7d946ea892833. No predecessor
census or new section B/C implementation is imported.

Earlier failed91..102 experiments retain their original scope. This
separately frozen result covers only89,90 with the stated fixed branch
word. Timed predicate capture in sections B/C has separate success
conditions and cannot change this result.
