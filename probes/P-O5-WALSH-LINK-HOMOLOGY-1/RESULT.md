# P-O5-WALSH-LINK-HOMOLOGY-1 result

Status: **CANDIDATE-T / PROOF-FIRST / LOCAL FORMAL LEG PASS / PUBLIC TWO-ARCHITECTURE REPLAY PENDING / CANON UNCHANGED**

## Verdict

The frozen written proof survives the accepted exact audit.

For every `N>=1`, the oriented split threshold complex admits an exact Walsh
character decomposition over `Q`. For support faces `J subseteq S`,

```text
E_(S,J)
  = sum_epsilon prod_(j in J)epsilon(j)[S,epsilon]
```

is the support-level Walsh basis and the boundary satisfies

```text
d E_(S,J)
  = 2 sum_(p in S\J)(-1)^pos_S(p) E_(S\{p},J).
```

If `L_J=link_Delta(J)`, `nu_J(T)=#{(j,t):j<t}` and

```text
Psi_J([T])=2^(-|T|)(-1)^nu_J(T)E_(J union T,J),
```

then `Psi_J` is a shifted chain isomorphism onto the `J` character sector.
Consequently

```text
H~_q(K_5(N);Q)
 ~= direct_sum_(J in Delta_5(N)) H~_(q-|J|)(L_J;Q),

chi~(K_5(N))
 = sum_(J in Delta_5(N)) (-1)^|J| chi~(L_J).
```

This is an exact finite signed-boundary decomposition. It is not a cancellation
estimate for the squarefree split summatory function.

## Accepted audit

```text
pin_commit:       662a5b57fcc6d1e65466e7404b0e47287467bab9
verifier_sha256:  41a08bc9d0711ae9a91cda8975248c4e59626c121bc657e37222e7a1e892259e
stdout_sha256:    40e978e31dacd7b1491af4178f275d2aaef0d62b6f23c376ed70253bd1b0c001
stdout_bytes:     292
stdout_lines:     8
exit_code:        0
stderr_bytes:     0
readout:          VERIFY RESULT 7/7 ALL PASS
```

Frozen breakers fired at `11`, `11`, `11`, `(209;11,19)` and characteristic
`2`. The successor verifier used product-pruned support enumeration while
retaining exactly the predecessor's theorem, N surfaces and witnesses.

## Scientific status

The Walsh basis, character-boundary formula, explicit link chain isomorphism,
rational homology direct sum and reduced Euler decomposition are `candidate-T`.

No RH, GRH, continuation, zero-location, or summatory cancellation estimate is
claimed. No orientation is selected. Link homology is not claimed to be small,
concentrated, sign-definite or uniformly bounded. The next live mathematical
problem is a uniform signed reconstruction or spectral estimate across the link
sectors. Public Canon v67, Registry, Frontier, dependencies, gates, evidence,
Notes and existing rows remain unchanged.
