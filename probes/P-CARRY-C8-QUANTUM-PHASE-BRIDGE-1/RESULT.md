# P-CARRY-C8-QUANTUM-PHASE-BRIDGE-1 result

Status: **SCIENTIFIC RESULT; TWO-ARCHITECTURE COMPUTATION GATE PASS; PUBLIC CLAIM UNREGISTERED**

## Recorded decision

```text
verdict: ALL FROZEN GATES PASS
exit:    0
stderr:  empty
stdout:  byte-identical to EXPECTED.txt
```

No preregistered falsifier fired. The required public workflow reproduced the probe successfully on both x86_64 and aarch64 and its aggregate `check` passed. This is an L1 algebra/operator result only. It changes no Canon, Registry, Frontier, dependency, dictionary, physical claim, or status row.

## Independent exact proof

The result does not rest on finite computation.

### G1

For bits `a,b`, ordinary integer addition obeys

`a+b = (a XOR b) + 2(a AND b)`.

Exponentiating a generator `g` of `C4` gives

`g^a g^b = g^(a XOR b) (g^2)^(a AND b)`.

Under `g -> S=diag(1,i)` and `g^2 -> Z=S^2`, this is exactly

`S^a S^b = S^(a XOR b) Z^(a AND b)`.

### G1b

The sign image of the carry is a `U(1)` coboundary:

`(-1)^(a AND b) = i^(2(a AND b)) = i^(a+b-(a XOR b))`

and therefore

`(-1)^(a AND b) = i^a i^b / i^(a XOR b)`.

Accordingly this probe does **not** transport the nonzero `H^2(C2,C2)` extension class into a nonzero `U(1)` class.

### G2

For `q(x)=sum_(i<j) x_i x_j mod 2`, each `CZ_ij` contributes the basis phase `(-1)^(x_i x_j)`. Multiplying all six pair gates gives

`product_(i<j) (-1)^(x_i x_j) = (-1)^q(x)`.

Hence

`U_q = product_(i<j) CZ_ij`

on every computational basis vector. Direct evaluation by Hamming weight gives `q=0` exactly at weights `0,1 mod 4`; in width four the nonzero zero-locus is therefore the four weight-one vectors together with `1111`, exactly the carried five-element set.

### G3

Every automorphism of `C8` is multiplication by a unit modulo eight, so the possible generator images are exactly exponents

`k in {1,3,5,7}`.

With `T=diag(1,zeta_8)`, `S=T^2`, `Z=T^4`, the exact pentit relations `tau^2=J_lambda` and `tau^4=-1` give

`tau -> T^k`,
`J_lambda -> T^(2k)=S^k in {S,S^-1}`,
`-1 -> T^(4k)=Z`.

Since `-tau=tau^5`, its image is `T^(5k)=T^k Z`; the sign branch is therefore preserved as a real algebraic choice and is not selected by this bridge.

For `P_k=diag(1,zeta_8^k)`, conjugation of Pauli `X` has off-diagonal ratio `zeta_8^(2k)`. Up to scalar an off-diagonal Pauli is `X` or `Y`, whose ratios are `+1` or `-1`. Thus `P_k` normalizes the Pauli group exactly when `2k=0 or 4 mod 8`, equivalently when `k` is even. Every `C8` generator image is therefore non-Clifford, while `S^±1` and `Z` are Clifford.

This is only an exact classification in the standard operator algebra. It is not a universality theorem and not a physical realization claim.

## Immutable pin and local formal leg

```text
public lock:          issue 716
base commit:          de5210f4a1bfe801d994137132a3dca4e72ff7ef
preregistration pin: cc0c08c77caa2c50fa5dbbdd114aa69b61dec366
PREREG.md SHA-256:    1e434eeb4b90020dd521d49533e92b26102539a02e2cff9426dda360afc58ad5
verify.py SHA-256:    9d4f025257c60878225880bcf656381dd2dcdaad75c4017862a8c159d7c55fcc

platform:             Debian GNU/Linux 13 (trixie)
architecture:         x86_64
Python:               CPython 3.13.5
exit/stderr:          0 / 0 bytes
stdout SHA-256:       3b2676d3840765918771680d25998afcf95c91861c24fb1da5a18d183ef528dc
stdout bytes/lines:   478 / 7
result:               ALL FROZEN GATES PASS
```

`EXPECTED.txt` is the exact stdout of this execution. The frozen `PREREG.md` and `verify.py` remain byte-identical to the public pin.

## Required two-architecture workflow

```text
pull request:          717
formal evidence head: 9380e9767c1c62183efecd85f2048f7922098784
workflow run:          33374960000
x86_64 job:            99434265658  success
aarch64 job:           99434266171  success
aggregate check job:   99434329352  success
verifier SHA-256:      9d4f025257c60878225880bcf656381dd2dcdaad75c4017862a8c159d7c55fcc
stdout SHA-256:        3b2676d3840765918771680d25998afcf95c91861c24fb1da5a18d183ef528dc
stdout bytes/lines:   478 / 7
byte identity:         PASS against committed EXPECTED.txt
gate:                  PASS
```

Both architecture jobs passed repository policy, unit tests, Canon checks, ledger checks, gate-contract checks, and `Reproduce changed public probes`. The aggregate job reported the two-architecture check as successful. `RUN.md` remains the neutral local execution record; this close-gate commit changes only `RESULT.md`.

## Auxiliary breaker

The negative-control audit passes six guards: removal of the AND carry breaks G1; the explicit `U(1)` coboundary is present; even exponents fail to generate `C8`; odd generator images lie outside the `C4` phase subgroup; `tau` and `-tau` remain distinct branches related by `Z`; and the quadratic carry phase is not reducible to linear parity.

The breaker is auxiliary. The scientific proof is the exact derivation above.

## Earned scope and fences

The result earns only the following mathematical statement pending repository review and fold: the carried binary carry algebra and pentit order-eight subgroup admit the displayed exact phase-operator representation, the carried quadratic form is exactly the complete-pair `CZ` phase polynomial, and the `C8` generator layer lies beyond the diagonal Clifford phase subgroup by the Pauli-normalizer test.

It does **not** claim that TWIST/J derives quantum mechanics; that any TWIST/J carrier is a physical qubit, quantum state, gate, phase, or apparatus; that the Born rule, measurement, preparation, decoherence, a Hamiltonian, or a physical occurrence law has been derived; that the `C4`/quadratic layer gives quantum advantage; that this bridge proves universal quantum computation; that any generator orientation is selected; or that any L2-L6 lift exists.
