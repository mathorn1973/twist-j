# P-C8-BILINEAR-SHADOW-2 result

status: proof-first theorem candidate at T, L1 scope; formal aarch64 leg
`6/6 ALL PASS`; required GitHub x86_64 leg pending. No local falsifier fired.
No frozen file was amended after the public pin.

This is a transparent protocol repair with a known predecessor result, not a
blind discovery. `P-C8-BILINEAR-SHADOW-1` remains protocol-invalid audit
history and is not evidence for this candidate.

Candidate content at the frozen scope, conditional on the required GitHub
leg and review:

```text
AXES        <tau> = F_5^* union tau F_5^*. The even powers are exactly the
            nonzero base-field axis; the odd powers are its tau-multiple.
            The order-eight elements are exactly {+-tau,+-eta}.
GALOIS      Frobenius is conjugation a+b tau -> a-b tau. It fixes F_5,
            negates tau F_5, preserves norm under sign, and sends the two
            registered branches to one another.
SWAP        Frob(Y_n^+)=Y_n^- for every n. The branches are
            Galois-conjugate; no broader physical or gauge equivalence is
            claimed.
RECORD      For V^epsilon containing Theta always, Y_n^epsilon on even
            digit-sum classes, and Y_n^epsilon Y_m^epsilon on odd pairs,
            V^+=V^-=:V is F_5-valued. Mixed parity is off-axis and
            branch-dependent.
REFINE      The norm reads s2 mod 4. V reads the declared even and odd-pair
            classes mod 8, with witnesses 15/255 and (1,1)/(1,31); on even
            classes (Y_n^epsilon)^2=Theta_n^-1.
```

The all-n scope is carried by the frozen exact proof; the finite verifier is
its audit. The result selects no branch and provides no L2-L6, clock,
gravity, SI, force, uniqueness, or physical-gauge bridge.
`SQRT-PHI-TIME-GRAVITY [O]` remains open.

Proposed disposition, outside this probe: after the required x86_64 byte
match and manual review, retain this probe as the sole evidence candidate
for a later separately sealed `C8-BILINEAR-SHADOW [T]` fold. No Canon,
registry, frontier, dependency, or release file changes here.
