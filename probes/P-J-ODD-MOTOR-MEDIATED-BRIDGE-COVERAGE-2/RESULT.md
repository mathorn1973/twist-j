# P-J-ODD-MOTOR-MEDIATED-BRIDGE-COVERAGE-2 result

Status: **candidate-T evidence maintenance / L1 / COVERAGE-CERTIFIED / PUBLIC CANON STATUS AND SCOPE UNCHANGED.**
Mode: **RESULT-EXPOSED. Not independent confirmation.**

The first admissible execution of the immutable successor verifier exited zero, wrote
empty process stderr and matched the committed `EXPECTED.txt` bytes.

## Exact coverage result

```text
G1 native two-sector discriminant / CRT hardening          PASS
G2-G3 five-token block graph, bridge, 5/4 and 1/5          5/5 PASS
G4 D,D^2,D^3,D^4,D+D^-1 controls                           PASS
G5 explicit five-token Schur elimination                   5/5 PASS
G6 token-2 determinant                                      PASS
G7 Sym^2=1+epsilon+2V, End dimension 6, Hom vanishings      PASS
G8 q_plus/q_minus covariance and trilinear census           PASS
DECISION                                                    COVERAGE-CERTIFIED
```

The corrected native calculation supplies the exact discriminants

```text
(-5-sqrt(5))/2,
(-5+sqrt(5))/2,
```

negative in both real embeddings, with complementary CRT ranks `2,2`. The explicit
Schur calculation supplies

```text
S_PR = -(t^2/z) P A C A R,
S_PR^sharp S_PR = (5/4)(t^4/z^2) R,
S_PR S_PR^sharp = (5/4)(t^4/z^2) P.
```

Together with the original exact G2-G8 implementation, this covers every clause of the
current Public Canon v61 `J-ODD-MOTOR-MEDIATED-BRIDGE [T]` row.

## Excluded later result

The hardening source also computes the later 624-channel-box classification, but this
coverage verifier does not consume its truth value, survivor list, box count or final
hardening decision. Therefore no finite-box uniqueness clause is earned or folded by
this probe.

## Scientific routing

Maximum later public use is one evidence-maintenance operation:

```text
J-ODD-MOTOR-MEDIATED-BRIDGE
  status       T -> T
  scope        unchanged
  falsifier    unchanged
  dependencies unchanged
  evidence     EVIDENCE_CHANGE -> this complete coverage bundle
```

No new Registry claim, gate, dictionary, physical selector, material/resonance reading,
Born/probability statement, decoder/apparatus claim, SI statement or L2-L6 lift follows.
The stopped predecessor #542 supplies no evidence.
