# P-C8-PHASE-SELECTION-1 result

Status: **SCIENTIFIC RESULT; TWO-ARCHITECTURE COMPUTATION GATE PASS; PUBLIC CLAIM UNREGISTERED**

## Decision

```text
verdict: ALL FROZEN GATES PASS
exit:    0
stderr:  empty
stdout:  byte-identical to EXPECTED.txt
```

The probe earns two narrow L1 conclusions and one explicit non-conclusion:

1. the four phase representations form a free transitive Klein-four torsor under source Frobenius branch flip and target complex conjugation;
2. in the frozen Frobenius-natural selector class, the source sign branch `tau` versus `-tau` has no canonical selector;
3. the same Frobenius argument does **not** eliminate the distinct `J_lambda -> S` versus `S^-1` orientation choice.

No Canon, Registry, Frontier, dictionary, issue #716 disposition, or physical claim changes here.

## Independent exact proof

### G1 — root pair

In `F25=F5[tau]/(tau^2-2)`, the equation `r^2=2` has the two roots `+-tau`. They are distinct and a quadratic has at most two roots. Moreover

```text
tau^2 = 2,
tau^4 = 4 = -1,
tau^8 = 1,
```

with `tau^4 != 1`, so both roots have exact order eight.

Frobenius fixes `F5` pointwise. Since

```text
tau^5 = tau tau^4 = -tau,
```

it swaps the two roots while fixing `J_lambda=2`. Thus the intrinsic datum

```text
D=(F25/F5,J_lambda,{tau,-tau})
```

is Frobenius-stable but neither root is Frobenius-fixed.

### G2 — representation torsor

An isomorphism `C8 -> mu_8` sends a generator to a generator. The generator exponents modulo eight are exactly

```text
E={1,3,5,7}.
```

Precomposing `rho_k` with source Frobenius `tau -> tau^5` gives

```text
B(k)=5k mod 8=k+4 mod 8.
```

Postcomposing with target complex conjugation gives

```text
O(k)=-k mod 8.
```

Both are involutions and commute. Their product acts by `3k mod 8`. The four maps

```text
id, B, O, BO
```

are exactly multiplication by the four units modulo eight. Acting on any odd `k` they produce all four odd residues, and none of the three nonidentity maps fixes an odd residue. Hence `E` is a free transitive torsor for `C2 x C2`.

This classifies two binary choices. It does not choose either one.

### G3 — Frobenius sign-branch no-go

A Frobenius-natural selector on the frozen datum would have to assign

```text
s(D) in {tau,-tau}
```

and satisfy equivariance under every automorphism of `D`. Frobenius fixes the datum `D`, so equivariance requires

```text
s(D)=sigma(s(D)).
```

But Frobenius swaps the two roots and has no fixed point in the root pair. Contradiction.

Therefore **no Frobenius-natural root selector exists in the frozen class**. Equivalently, after one target C4 orientation has been fixed, Frobenius-invariant source data cannot distinguish `rho_k` from `rho_(k+4)`.

This is a relative naturality no-go, not an impossibility theorem for every larger theory.

### G4 — C4 orientation firewall

The preceding no-go cannot be reused to kill the second binary choice. The **abstract `C8` power automorphisms** with exponents `3` and `7` would exchange the two C4 orientations, but they are not automorphisms of the marked field extension over `F5`. Indeed

```text
(tau^3)^2=(tau^7)^2=tau^6=3=2^-1,
```

so they send `J_lambda=2` to `J_lambda^-1=3` and therefore do not preserve the marked source datum.

Correspondingly, the actual source Frobenius action `B` preserves the two representation pairs

```text
{1,5}: J_lambda -> S,
{3,7}: J_lambda -> S^-1,
```

while target conjugation `O` exchanges them.

Thus this probe proves **no source-side no-go** for `S` versus `S^-1`. This boundary is load-bearing. The existing `RAMIFIED-TM-LIFT [T]` already distinguishes source multiplier `2` in its fixed `M_J/Tr_4` channel; what is still missing is an independently justified comparison rule that maps that source orientation to one target phase orientation.

### G5 — full-k boundary

If neither the source root branch nor target phase orientation is chosen, the declared Klein-four symmetry acts freely on all four representations and has no fixed `k`. Hence a symmetry-natural unique `k` cannot exist in that frozen class.

A future unique `k` must add independently justified symmetry-breaking data, justify a narrower selector class before target comparison, or prove the final claimed readout invariant under the unresolved choice.

## Immutable pin and local exact leg

```text
public lock:          issue 721
base commit:          d6e8e466c1d5b1c447acf12fc653059ae8aa65e7
preregistration pin: 8c561f6f0708443d3eb1622319dc0d5e3349ff20
PREREG.md SHA-256:    20c58eb092352df5ef8b9d4d07cd53528bf5070eb221d910bf78bfeab1ad7661
verify.py SHA-256:    4de6bfeb43dd8f3c1a4a38388de22000d003efcf262c3bfeccee3ce82603213b
platform:             Debian GNU/Linux 13 (trixie)
architecture:         x86_64
Python:               CPython 3.13.5
exit/stderr:          0 / 0 bytes
stdout SHA-256:       482b050912678b69fe858aea7ae282ef2fecaab1bc1e3059cd6c0b92ba177c25
stdout bytes/lines:   490 / 6
result:               ALL FROZEN GATES PASS
```

`EXPECTED.txt` is the exact stdout of this execution. The frozen `PREREG.md` and `verify.py` remain byte-identical to the public pin.

## Required two-architecture workflow

```text
pull request:          722
formal evidence head: a8ec828ca537a2969b7b79cb4252fabaea9b30b5
workflow run:          33376963569
x86_64 job:            99440516542  success
aarch64 job:           99440516949  success
aggregate check job:   99440581493  success
verifier SHA-256:      4de6bfeb43dd8f3c1a4a38388de22000d003efcf262c3bfeccee3ce82603213b
stdout SHA-256:        482b050912678b69fe858aea7ae282ef2fecaab1bc1e3059cd6c0b92ba177c25
stdout bytes/lines:   490 / 6
byte identity:         PASS against committed EXPECTED.txt
gate:                  PASS
```

Both architecture jobs passed repository policy, unit tests, Canon checks, ledger checks, gate-contract checks, and `Reproduce changed public probes`. The aggregate job reported the two-architecture check as successful. `RUN.md` remains the neutral local execution record; this close-gate commit changes only `RESULT.md`.

## Scope firewall

The result is exact L1 algebra and selector classification only. It does not derive a physical qubit, T gate, Born rule, measurement, apparatus, Hamiltonian, quantum speedup, universality, time, gravity, SI quantity, decoder completion, or any L2-L6 lift. It does not identify target complex conjugation as a physical gauge. It does not claim that no possible extension can select a branch or orientation. It does not register #717 and does not close #716.
