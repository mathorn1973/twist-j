# Result: `C-C40-RECIPROCAL-RAMIFIED-SEAM-N`

```text
RESULT:          PASS
GRADE:           candidate-T / L1
AUTHORITY:       NONE (NON-CANONICAL incubation)
FORMAL PROBE:    NONE
EVIDENCE CREDIT: NONE
```

Both frozen programs exited `0`, their outputs match the captured transcripts,
and no decisive falsifier fired.

## Accepted candidate delta

At candidate grade only:

1. \(\Phi_{40}(x)=x^{16}-x^{12}+x^8-x^4+1\).
2. \(\Phi_{40}\bmod2=\Phi_5^4\) and
   \(\Phi_{40}\bmod5=\Phi_8^4=(x^2-2)^4(x^2-3)^4\).
3. The ramified profiles are `(4,4,1)` at `2` and `(4,2,2)` at `5`.
4. The complete unramified atlas has factor types `1^16`, `2^8`, and `4^4`
   on respectively `1`, `7`, and `8` reduced residue classes modulo `40`,
   with Dirichlet densities `1/16`, `7/16`, and `1/2`.
5. \((\mathbf Z/40\mathbf Z)^\times\cong C_4\times C_2\times C_2\) has
   exponent `4`; hence no unramified rational prime is inert, and the two
   ramified identities complete the proof that `Phi_40 mod p` is reducible
   for every rational prime `p`.

## Required local distinction

Modular reducibility does not imply local-field reducibility here.
`Phi_40 mod 2` is the repeated polynomial `Phi_5^4`, but `Phi_40` is
irreducible over `Q_2` because `(e,f,g)=(4,4,1)` gives one completion of
degree `16`. At `5`, two residue factors of degree `2` and multiplicity `4`
lift to two `Q_5` factors of degree `8`. Both ramified residue algebras are
nonreduced; neither is an etale field product. The ramified value `g=1` at `2`
is not inertness.

## Dependency and claim boundary

The compositum/intersection theorem and the registered quartic local
ingredients are imports from the four Canon rows named in `README.md` and
`PREREG.md`. They are audited but not reclaimed. The result does not merge
the fields, assert a `2`-to-`5` symmetry, select a component, promote
`I-BILOCATED`, establish a physical or causal bridge, or imply RH.

No Canon, Registry, Frontier, gate, or program status is changed by this
result. Promotion is not performed; it would require a later, distinct public
fold under the then-current `POLICY.md`.

