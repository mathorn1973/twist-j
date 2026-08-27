# P-O5-EULER-INCIDENCE-TRIANGLE-NOGO-1 result

Status: **CANDIDATE-T / PROOF-FIRST / LOCAL FORMAL LEG PASS / PUBLIC TWO-ARCHITECTURE REPLAY PENDING / CANON UNCHANGED**

## Verdict

The frozen written proof survives the accepted exact audit.

For every integer `N>=1`, the oriented split-prime threshold carrier `K_5(N)`
is a finite simplicial complex and

```text
S_5^sum(N) = - reduced_Euler_characteristic(K_5(N)).
```

Every split prime `p` satisfying `11p>N` supplies two isolated vertices. If

```text
I_5(N)=#{split p<=N:11p>N},
```

then any one-vertex-incidence matching leaves at least
`max(0,2I_5(N)-1)` unmatched faces when the empty face may be used and at
least `2I_5(N)` when it may not.

Therefore the route

```text
incidence matching
  -> cancel matched opposite-parity faces
  -> bound only by the number of unmatched faces
```

cannot prove the all-epsilon square-root bound. The final asymptotic route
statement imports only classical PNT in the residue classes 1 and 4 modulo 5,
which gives `I_5(N)` of order `N/log N`.

This is a narrow route no-go. It is not a lower bound for the signed sum and
not a negative closure of any complete transfer class.

## Accepted audit

```text
pin_commit:       0c216fad6cf1a758153e893799403730c24c0028
verifier_sha256:  70e1d3b4e44657ad218a93bb1b067bfc171b0078bc0ceda75c21c6e8839af5fd
stdout_sha256:    222a9bf7e84b819138b164adf7773fb2319dfe127bde1f0413950b68e7249992
stdout_bytes:     496
stdout_lines:     9
exit_code:        0
stderr_bytes:     0
readout:          VERIFY RESULT 8/8 ALL PASS
```

Frozen breakers fired exactly:

```text
B1 one orientation only:                    11
B2 both conjugate orientations in one face: 121
B3 inert 2 treated as split:                2
B4 closed isolation threshold:              (209,19)
B5 empty face removed:                      1
```

## Scientific status

The exact finite carrier, Euler identity, isolation theorem, and universal
matching floor are `candidate-T`. The asymptotic route verdict is
`candidate-T on [T-lit] PNT-AP`.

No RH, GRH, zero-location, continuation, or cancellation estimate is claimed.
Signed cancellation among unmatched cells, Morse boundaries, homology,
weighted or nonlocal pairings, growing modes, and spectral kernels remain
open. Public Canon v67, Registry, Frontier, dependencies, gates, evidence,
Notes, and all existing rows are unchanged.
