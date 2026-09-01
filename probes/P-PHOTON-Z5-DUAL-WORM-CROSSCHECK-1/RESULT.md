# RESULT

Status: **PASS / independent dual implementation frozen / zero engineering evidence**

Probe: `P-PHOTON-Z5-DUAL-WORM-CROSSCHECK-1`  
Public issue: #756  
Formal source pin: `fe74bf9d9cc8666b569d4618efd2149215c19c3d`

The proof-first package establishes the correctness of the frozen independent
dual closed-surface Markov kernel at its declared algorithmic scope.

## Exact result

The dual target is

```text
n in {-1,0,+1}^P,
partial n = 0 mod 5,
pi_L(n) proportional 2^(-|supp n|).
```

The frozen proposal uses random finite words in the complete cycle generator
set consisting of all 3-cell boundaries plus the six coordinate homology
2-tori. The word distribution is sign symmetric, so the proposal increment law
satisfies `Q(z)=Q(-z)`.

Forbidden residues `2,3` are rejected exactly. For an allowed candidate with
support change `d`, the Metropolis acceptance is exact:

```text
d <= 0: accept,
d > 0:  accept iff d fair bits are all zero.
```

Thus detailed balance with `pi_L` is exact. Because the generator set spans the
full cycle space and the geometric word distribution assigns positive
probability to every finite word, every allowed state can reach every other
allowed state with positive probability. The zero-length word has probability
`1/2`, so the chain is aperiodic.

Hence the finite frozen chain is reversible, irreducible and aperiodic, with
unique stationary law `pi_L`.

## Finite audit

The deterministic verifier independently checks the cycle-space dimensions and
generator ranks:

```text
L=2: rank d2 = 45, dim Z2 = 51, generator rank = 51
L=3: rank d2 = 240, dim Z2 = 246, generator rank = 246
```

A 2,000-step deterministic `L=2` implementation fixture remains inside the
allowed closed state space after every step and terminates at

```text
state_sha256 = 580174dde4d285c6763bb69db5478bf2e90f56de9dfa08176e3e27a6ba2a2188
```

The local run exited zero, wrote empty stderr and matched the 683-byte
`EXPECTED.txt` exactly.

## What this does and does not unlock

This merge candidate satisfies the #757 prerequisite that the independent dual
cross-check have a **frozen implementation**. Issue #756 itself remains open:
the `L=6,8` Ward/covariance cross-check still requires its own public pin and
zero-evidence execution.

Production under #742 must preserve this firewall:

```text
PHOTON_EVIDENCE is unavailable until #756 returns DUAL_CROSSCHECK_PASS.
```

Issue #748 remains the independent saved-state reader for periodic wrapping and
connected covariance blocks.

No photon phase, thermodynamic limit, physical photon, pole identification,
polarization, mass, contraction/expansion, Canon status or Registry row is
changed by this result.

## Integrity

```text
verify.py sha256: 6c55ef8162c2c9f96088dbe084a32c0619660f87143c687907b34422dcbbc03a
stdout sha256:   a15a0aed27d6a6c5bd54d4707c9ae6a8ebd6874d470b04c3d53ab04b81eb0ec3
stderr sha256:   e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```
