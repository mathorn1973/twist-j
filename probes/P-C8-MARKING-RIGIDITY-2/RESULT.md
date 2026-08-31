# P-C8-MARKING-RIGIDITY-2 result

Status: **SCIENTIFIC RESULT; TWO-ARCHITECTURE COMPUTATION GATE PASS; PUBLIC CLAIM UNREGISTERED.**

## Recorded decision

```text
verdict:      6/6 ALL PASS
exit:         0
stderr:       empty
stdout:       766 bytes, 7 lines
stdout sha256 906b2bdc60e70cc4d225606609449f81c34dbb471c75b0045ac59cd3c80fc7e6
```

No frozen scientific falsifier fired in the single formal local execution from the immutable pin. GitHub workflow run `33413792559` independently replayed the committed verifier from clean checkouts: `architecture-x86_64` SUCCESS, `architecture-aarch64` SUCCESS, aggregate `check` SUCCESS, `publication` correctly SKIPPED. Both architecture jobs reproduced the same committed `EXPECTED.txt` bytes.

## Integrity repair

This successor repairs the two evidence-integrity defects discovered after merge of `P-C8-MARKING-RIGIDITY-1`.

1. The finite G2 primality audit now uses `math.isqrt` and integer divisibility only. The newly authored verifier contains no floating-point operation or float literal in a decision path.
2. The run record uses neutral platform, architecture and Python metadata only. It contains no machine nickname, private hostname, private address or internal fleet label.

The predecessor remains immutable provenance and is not promotion evidence.

## Earned mathematical scope

**[candidate-T / proof-first] Prime rigidity under the marking.** If an odd residue prime admits `tau^2=2` with `ord(tau)=8`, then `ord_p(2)=4`, hence `p|15` and `p` does not divide `3`, so `p=5`. The scan below 20000 is an exact integer audit of the divisor proof, not its source.

**[candidate-T / proof-first] C8 delivery under a nonsquare marking.** Over `F_5`, each nonsquare marking has two roots and both have exact order eight; square markings have no order-eight root. The C8 layer follows once the nonsquare marking is supplied.

**[candidate-T / proof-first] Source orientation.** The two nonsquares are `2` and `3=2^-1`; orientation reversal sends the marked multiplier to its inverse, while the sign branch preserves the marking.

**[candidate-T / external standard-QM comparison] Relative target no-go.** The `k=1` and `k=7` two-use states are entrywise complex conjugates. The ten two-qubit Pauli products with rational matrix entries form a rational basis for Hermitian rational-entry matrices and none separates the states. `XY` and `YX` do separate them, carrying target orientation through `i`.

## Boundaries

The marking `J_lambda=2` remains an input at its existing dictionary scope. No derivation of quantum mechanics, physical qubit, gate, state, apparatus, Born rule, measurement law, Born-norm transport, quantum advantage, universality or speedup is claimed. No unique C8 orientation is selected, and no statement says an independently oriented object cannot pay the orientation debt.

The successful two-architecture workflow repairs the public evidence package only. It does not register or promote a Canon claim. Any fold is separate.
