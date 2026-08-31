# P-O5-FIRST-MISSING-SHELL-1 result

Status: **CANDIDATE-T / PROOF-FIRST / LOCAL FORMAL LEG PASS / PUBLIC TWO-ARCHITECTURE REPLAY PENDING / CANON UNCHANGED**

## Verdict

The frozen written proof survives the accepted exact audit.

For every face `J` of the split-prime product-threshold complex, let `r_J` be the least split prime not in `J`, let `M_J=floor(N/product(J))`, and let `L_J` be the support link. Define the terminal family

```text
C_J(N)={F in L_J : r_J notin F and r_J*product(F)>M_J}.
```

The proof gives an augmented acyclic cone subcomplex whose quotient has exactly the terminal faces as a basis and zero differential. Hence

```text
H~_d(L_J;Z) ~= Z^(#{F in C_J(N): |F|=d+1}).
```

In particular, every link has torsion-free integral reduced homology with an explicit terminal-shell basis.

A separate exact sign-reversing involution on ordered support partitions cancels every nonterminal pair. For squarefree split-supported `n`, with

```text
r(n)=least split prime not dividing n,
t(n)=#{p|n:p>r(n)},
```

the surviving fibres have cardinality `2^t(n)`, yielding

```text
S_5^sum(N)
  = sum_(n<=N, n squarefree split, n*r(n)>N)
      (-1)^omega(n) 2^t(n).
```

Grouping by `r(n)=q_k` gives the frozen primorial terminal-shell identity of `PREREG.md`.

## Accepted exact audit

```text
pin_commit:       b9ac3f52c28d06293d27dcd2fb1ca7338ad68b0e
verifier_sha256:  3fd20a130eb38d093815116bfd8c5a5b771b9dcd2298ece6492752a9d7beb256
stdout_sha256:    bd89fd430dfdee0f5d508cfa51e1b92ecef32a70611d1da9909acd3ea03cbd96
stdout_bytes:     348
stdout_lines:     9
exit_code:        0
stderr_bytes:     0
readout:          VERIFY RESULT 8/8 ALL PASS
```

Frozen breakers all fired at the preregistered witnesses: `B1=B2=B3=B4=B5=11` with the exact face/support refinements recorded in `PREREG.md`.

## Scientific boundary

The link homology theorem and the first-missing/primorial terminal-shell identities are `candidate-T`. The finite verifier audits the universal written proof and does not define its scope.

No summatory estimate is obtained. No RH or GRH statement, analytic continuation, zero-location theorem, Hecke/automorphic object, selected split orientation, physical dictionary, probability statement, SI statement, or L1-L6 lift is claimed. The transform is not claimed to be contractive, and absolute-value estimates remain subject to the already established large-prime obstruction.

Public Canon v67, Registry, Frontier, dependencies, gates, evidence, Notes, and all existing public rows remain unchanged.
