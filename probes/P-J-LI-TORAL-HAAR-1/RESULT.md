# P-J-LI-TORAL-HAAR-1 result

Status: FORMAL PROBE RESULT; TWO-ARCHITECTURE REPRODUCIBILITY GATE PASS; PUBLIC CLAIM UNREGISTERED

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
formal evidence commit:376add6c14e6d2bc37dbcf4a7478b0d8af493982
EXPECTED.txt SHA-256:  8e17b45e07b977fbbfe74f31cb64e2a78bc950cd5bedb70b9b163bcd77fbefc8
RUN.md SHA-256:       5393587ec61c769f4bf1b328fe6ece651faccc1de655bcec8764c86c9e3284e3

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

`EXPECTED.txt` is the exact first formal stdout.

Two-architecture record:

```text
aarch64 leg    Ubuntu 24.04.4 LTS, CPython 3.12.3, neutral environment;
               first formal execution at the exact pin, followed by two
               byte-identical repetitions; verifier 3f309c32...219d;
               stdout 8e17b45e...efc8, 2717 bytes.
x86_64 leg     GitHub check on pull request 51, evidence head
               376add6c14e6d2bc37dbcf4a7478b0d8af493982; run
               29578010224, job 87876817139, conclusion success;
               Ubuntu 24.04.4, CPython 3.12.13; verifier and stdout hashes
               byte-identical to the aarch64 leg; log reports
               VERIFY PASS P-J-LI-TORAL-HAAR-1.
gate:          PASS. The aarch64 and GitHub x86_64 outputs are byte-identical.
```

The gate establishes reproducibility of the exact audit. The proposed
theorem grade comes from the frozen proof, not from multiplying machine
runs. No public claim is registered by this probe alone.
