# P-U-FINITE-READER-INDEPENDENCE-1 result

**Status: PROOF-SURVIVES; LOCAL EXACT AUDIT PASS; CANON UNCHANGED.**
Public lock: [#890](https://github.com/mathorn1973/twist-j/issues/890).
This is proof-first, result-exposed L1 mathematics. It supplies no physical
occurrence law.

A fixed finite-window reader of the actual native trajectory cannot produce
nondegenerate Bernoulli block frequencies at every order, even after its
SILENT outputs are deleted. The native counter remains unbounded in this
argument. Conversely, every prechosen finite horizon can be matched by a
deliberately constructed fixed finite-window reader. The full arguments are
in [PROOF.md](PROOF.md).

## Exact scope and conclusions

The source class contains all 15,625 origin-zero heads under unchanged U.
The input is a fixed length-L window of decorated checkpoints `(x_n,theta_n)`,
read at every consecutive tick with `n>=L+2`. The reader is fixed, has output
alphabet `{0,1,SILENT}`, and has no additional counter input, growing window,
separate persistent memory, changing context, intervention or feedback.

| Question | Proven answer |
| --- | --- |
| How many native length-t words can one synchronized trajectory contain? | At most `20,000 t`, from the inherited 100-letter constant-length substitution and the exact native chart. |
| Can acceptance be nonempty but occur only finitely often after synchronization? | No. One accepted legal window recurs with a finite bounded gap G. If no legal window is accepted, the disposition is NO_EVENT and there is no accepted ratio. |
| How many accepted k-words can the reader produce? | At most `20,000[L+G(k-1)]`. Once `2^k` exceeds this number, at least one binary k-word is absent. |
| Can mixing heads and accepted onsets recover every Bernoulli block law? | Not for one fixed global reader. The finite union over its active chart classes is bounded by `62,500,000[L+G(k-1)]`, using their maximum gap. |
| Is there one finite horizon that defeats every finite-window reader? | No. For each h, phase recovery from `5*2^(h-1)` driver bits followed by a binary de Bruijn cycle gives exact fair time block frequencies through h and fails at h+1. |

The bounds are sufficient and not claimed sharp. The absence of a word
already excludes its positive Bernoulli frequency; no existence theorem for
the reader's other frequency limits is assumed. Finite unsynchronized
prefixes cannot change this frequency obstruction. The separate support-law
statement concerns the synchronized accepted language, not arbitrary onsets
inside a prepended preparation prefix.

The positive construction gives deterministic all-prefix time frequencies.
It adopts the reader, phase reconstruction and cycle; it supplies no actual
stochastic preparation or independent realized-trial law. Its window is fixed
throughout a run but may depend on the horizon chosen before that run. No
minimal window requirement, finite-horizon physical impossibility, approximate
independence bound or measured-memory estimate follows.

## Exact audit and disposition

The first formal Linux run completed with no mathematical mismatches:

```text
native chart and actual paths: 281251 checks
clock identities and pairs:     12688 checks
complete finite languages:         29 checks
finite event readers:           80454 checks
finite-horizon controls:        10296 checks
total:                        384718 checks
stdout SHA-256: dab3f3faea009d9535452be96acaabebb974dfdd824fa49e96b7bd476b3db94d
```

The bounded native audit visits every origin-zero head through tick 11. The
clock audit certifies the 100-letter substitution's 77-step reachability and
its complete 150-pair language using constructive occurrence witnesses.
Literal prefixes are consistency checks, not evidence of language completeness.

The finite reader census covers all 90 ternary tables on one-bit or two-bit
Thue-Morse windows: two accept nothing, and the other 88 have a certified
sufficient gap of 16 and an absent 12-bit accepted word. Complete raw-language
extraction and independent direct-output extraction agree at accepted orders
1, 2, 3, 4, 8 and 12. This finite scalar subclass is not presented as an
exhaustive enumeration of arbitrary decorated-checkpoint readers. Positive
phase/de Bruijn controls pass for h=1..8; the written proof covers every h.

No frozen mathematical mismatch was found. The all-order sufficiency of the
declared finite-window class is the refuted implication. Required GitHub
x86_64 and aarch64 checks supply separate reviewed-head evidence recorded
on the pull request; local execution is not a substitute. Public pin and first-run custody are in
[RUN.md](RUN.md), and the raw accepted output is [EXPECTED.txt](EXPECTED.txt).
No Registry T/F status is created automatically by this result.

## Physical boundary and next test

This advances beyond a finite-cycle model without turning the finite
checkpoint into the whole autonomous state. It applies the inherited exact
coding to each actual unbounded-counter U trajectory. It also advances beyond
the registered driver-only entropy statement by covering complete decorated
finite histories and their accepted event words.

It does not cover every reading of complete U. Arbitrary counter dependence
permits `F(n,x)=b_n` for any prescribed sequence; computable sequences give
computable such readers. Additional memory, growing histories, changed
acquisition schedules and independently defined physical apparatuses require
their own complete analysis.

The physical next step remains to specify one independently motivated event
reader, its full resources, preparation and accepted-trial semantics, then
test the actual ordered law at the required horizon. The present result does
not presume that every quantum experiment requires exact all-order
independence and does not falsify Born's marginal rule.
`QDD-INSTRUMENT-APPARATUS`, `QDD-INSTRUMENT-CLASS-COMPLETENESS` and
`QDD-TERMINAL-EVENT-SEMANTICS` remain O/STOP. No physical carrier, occurrence
law, reset or persistence certificate, L4/L5 or L5/L6 gate, Canon fold,
version, tag or release is supplied.
