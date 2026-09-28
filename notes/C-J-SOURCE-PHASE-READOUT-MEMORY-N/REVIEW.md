# Review intake: source, phase readout, and memory

**Date incorporated:** 29 September 2026  
**Status:** review evidence for a NON-CANONICAL note; not a public pin

A supplied independent reading and independently written verifier reviewed the first apparatus draft on one architecture: Linux x86_64, Python 3.

Reported result:

```text
49 checks, 0 failures, 1 skipped
script sha256 68b5a7fce187f7bf2adc5e30e7a40510ef499b3175b46e3c1686c023b7bd4b30
stdout sha256 712cf53d4db7ea10fa569a12c0462cce665166590a50a11d9377f98d5cdb4211
```

The skipped item was inherited `q` transport whose definition was not present in the reviewed document. The reviewer also did not have the earlier source notes or `verify_twist_relational.py`, so those inherited claims were outside the independent replay.

The review confirmed the self-contained arithmetic for `J`, its integer matrix and inverse, Theorem A, reduction modulo 5, exact order 20, the phase-reader kernel, the complete 390,625 two-step residue/source cases, reversibility of the record cycle, endpoint cancellation, endpoint census, the finite form of Theorem C, and the digital-error locality statement.

The review required four corrections or status changes, all incorporated into `README.md`:

1. The archive stores the decoded source block, not the carrier residue. Residue-sector dephasing belongs to tracing the freshly populated residue pointer/reference record, whereas tracing the archive dephases a coherent source in the source-block basis. The old wording conflated those registers.
2. The three-step cancellation is elementary: `J + J^-1 = 1-zeta`, so the displayed cancellation follows because `zeta-1` lies in the chosen alphabet. The useful content is the existence of history collision in the chosen interface, not depth of the identity itself. There are 13 length-three zero-return words including the silent word.
3. The exponent `h=2 log phi` in Theorem C comes from the same expanding embedding that underlies the toral entropy. The endpoint proof is separate; the mechanism producing the number is not.
4. Equality of the endpoint-growth exponent with `h` remains open. The note now carries an explicit `O-J-ENDPOINT-GROWTH-LOWER-BOUND` rather than treating the length-10 census as a theorem.

The independent census reported exact endpoint counts through length 10:

```text
n=5   111289
n=6   390609
n=7   1241777
n=8   3723281
n=9   10693249
n=10  29816617
```

These values are evidence for the open lower-bound problem only.
