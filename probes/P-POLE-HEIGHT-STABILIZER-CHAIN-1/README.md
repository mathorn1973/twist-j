# A zero-first stabilizer construction for the common loader

NON-CANONICAL / L1. Public reservation: issue #1903.

The fixed preparation is I_t=(tB,-tB,u,u,X,2), with
j^5=1, Phi_5(j)=0, p=j^2, u=1-j, B=1-p and X=1+j-2j^3.
The required complete endpoint is G_t=(u+tB,u-tB,0,0,X,2)
for every t in {-2,-1,0,1,2}, using one chronological word.

This probe starts from the publicly verified W38 and its 64-direction
returning-loop bank, freezes a new zero-first construction, and emits
explicit small stock-obstruction certificates. Read PREREG.md for the
exact algorithm, limits and outcome rules; PROOF.md for the coset and
Schreier arguments; PROVENANCE.md for pre-exposed review evidence.

BANK.json contains only the public MACRO and EXTENSION_ROOTS records
from the sealed predecessor, with unchanged record values. No predecessor
program is imported or resumed. All new source files and the fixture
are pinned before the first execution.

A found word is audited on all five inputs with complete helper return
and an exact inverse. A partial search cannot prove impossibility. A
complete subgroup obstruction does not exclude the full odd stabilizer.
No shortest common-five word, autonomous controller, funded execution,
physical clock, action normalization or electromagnetic coupling follows.

The exact run command, from the repository root, is:

```text
python3 probes/P-POLE-HEIGHT-STABILIZER-CHAIN-1/verify.py
```

Only EXPECTED.txt, RUN.md and RESULT.md are appended after execution.
Sources remain frozen. Standard x86_64 and aarch64 CI compare the same
scientific stdout bytes; status remains NON-CANONICAL pending independent
review and any separately authorized promotion.
