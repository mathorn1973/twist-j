# P-J-LI-TORAL-HAAR-1 result

Status: FORMAL AARCH64 RESULT; GITHUB X86_64 GATE PENDING; PUBLIC CLAIM UNREGISTERED

## Scientific decision at the recorded leg

```text
TH1 through TH9 theorem-skeleton gates    9/9 PASS
X1 finite exploratory witness             PASS, not a theorem gate
exit                                      0
stderr                                    empty
```

No preregistered falsifier fired on the first formal aarch64 execution. The
same fresh-clone execution was repeated twice and all three stdout files were
byte-identical.

The exact audit confirms the Cayley and half-angle dictionaries, the forced
symmetrized-measure identities on the declared synthetic fixture, the public
`M_J` characteristic data, the two algebraic modulus alternatives,
cyclotomic exclusion, exterior-square non-escape, and both directed interval
certificates. The finite X1 loops agree with the declared carrier, but they
do not prove the all-dimensional theorem.

## Proof-first conclusion and boundary

The proposed theorem-grade conclusion rests on the proof frozen in
`PREREG.md`:

```text
exact Haar-Koopman realization
  => lambda_n >= 0 for all n
  => RH by Li's criterion
  => the symmetrized vector measure equals the forced atomic sigma_xi
  => contradiction with the root-of-unity-free toral character spectrum.
```

The contradiction is unconditional as a no-go for the assumed realization;
it neither assumes nor proves RH. The general statement applies to
`A in GL_d(Z)` with no root-of-unity eigenvalue. TH4 through TH7 independently
place the named `M_J` specialization in that carrier. The all-dimensional
step follows from the carrier hypothesis and the character-orbit proof, not
from X1 or from extrapolation of the `M_J` computation.

Only the symmetrized vector measure is forced. No uniqueness of the
unsymmetrized measure is claimed. The accumulation law remains a proof-first
consequence of the declared Riemann-von Mangoldt and Stieltjes imports; TH9
audits its exact leading-term interval machinery at one frozen epsilon and is
not a finite-epsilon proof of the asymptotic.

## Scope and non-conclusions

- This is an L6 measure/spectral no-go with one named `M_J`/Pillar-A toral
  specialization and no further layer lift.
- It excludes only the declared finite-dimensional Haar-Koopman carrier
  class. It does not exclude non-Haar, non-Koopman, boundary, scattering,
  enlarged, or infinite-dimensional carriers.
- It constructs no replacement realization and closes no moment bridge or
  Weil-positivity route.
- RH remains open; no numerical test or proof of RH is claimed.
- No registry, frontier, Canon, fold, release, or tag file changes here.
- `J-LI-TORAL-HAAR-NOGO`, `J-LI-BY-STANDARD-TORAL-HAAR`, and
  `J-LI-SPECTRAL-TARGET` remain unregistered pending the public gate and a
  separate reviewed fold.

## Formal evidence

```text
initial base:          7fe66e7ee8d02068c9717314988500c6022e73d6
public lock:           issue 50
preregistration pin:   47b738ac90c7e76063696b62ef88685ca507d973
PREREG.md SHA-256:     91efae35540d16f0714bf199d69f31d44f4ca1fef6863cc253e36680315c4383
verify.py SHA-256:     3f309c3244a5ca8c911d9d2da0dfe7f48ade08f09c5ba8ada2cc379235fd219d

platform:              Ubuntu 24.04.4 LTS
architecture:          aarch64
Python:                3.12.3
exit code:             0
stderr:                0 bytes
stdout SHA-256:        8e17b45e07b977fbbfe74f31cb64e2a78bc950cd5bedb70b9b163bcd77fbefc8
stdout bytes:          2717
stdout lines:          16
determinism:           three executions byte-identical
```

`EXPECTED.txt` is the exact first formal stdout. The required GitHub x86_64
rerun and byte comparison are pending. Until that check passes, this file
records only the formal aarch64 leg and no two-architecture gate result.
