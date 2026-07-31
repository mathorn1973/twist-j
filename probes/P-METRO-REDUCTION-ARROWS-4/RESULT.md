# RESULT P-METRO-REDUCTION-ARROWS-4

## Local result

```text
local_status: PASS
gates: 17 of 17 OK
fired_falsifiers: none
reproduction_status: PASS
```

The single prospective-pinned local execution passed every frozen gate with
exit code 0, empty stderr, and exact stdout SHA-256
`c0e4b5685b86799937e905b4cd6c55513c8c368c083587d6af7ddfb5bd3ac2d7`.

## Frozen-scope conclusion

At the declared L5 scope, the result supports:

1. state relabeling with transported starts, digit maps, and output;
2. restriction to the digit-map closure of allowed starts;
3. the multi-action Nerode quotient exactly when its finite congruence
   precondition holds;
4. coordinate permutation exactly when the ordered input basis is transported;
5. pointwise transported L5-stream invariance for every admitted arrow with
   `tau_R=identity`.

The exact proofs are stated in `PREREG.md`; the verifier audits their frozen
finite families and witnesses. The two- and three-state exhaustion found
exactly 1024/0 and 4251528/0 protocols/counterexamples, respectively. The
four-state witness therefore establishes the frozen minimality statement for
`q=2`, `a=2`, `r=1`, and binary output.

## Firewall

This probe supplies no evidence for obligation B (forbidden transformations),
obligation D (common `q^k` blocking), or obligation E (completeness of
`approx_red`). It owns no L5-to-L6 normalization, scientific-decision,
terminal-value, physical, SI, or other cross-layer gate.

No Canon, registry, frontier, changelog, hash, release, or status change is
proposed. `METRO-REDUCTION-CALCULUS` remains `[O]` and remains STOP. Final
reproduction status is PASS: the required GitHub x86_64 check reproduced the
pinned verifier and exact stdout SHA-256. Review remains pending.
