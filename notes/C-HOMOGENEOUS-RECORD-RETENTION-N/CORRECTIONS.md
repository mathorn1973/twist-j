# Corrections after review: `C-HOMOGENEOUS-RECORD-RETENTION-N`

**PUBLIC, NON-CANONICAL. Additive correction record.**

License: Apache-2.0.

Review: `CHANGES_REQUIRED` on head `93d16b22be1378d7955dbe53e853f967c13d4c0c`
(pin `24cc067983142017d3fd9a111acf80d6ab29db54`), items R1–R4, in the pull
request review
https://github.com/mathorn1973/twist-j/pull/1744#pullrequestreview-5639331800.
The review found no counterexample to the Theorem 6 bound for its declared
family; R1–R4 concern exported statements, typing and protocol classification.

## 0. What is preserved unchanged

These files keep the bytes of the pin or of the first run record. Corrections
never edit them:

| File | SHA-256 | Bytes |
|---|---|---|
| `notes/C-HOMOGENEOUS-RECORD-RETENTION-N/PROTOCOL.md` | `afd849bd4aa20a41588f29e2b5d22575a3754bb45a5583e7eea50bf6746a034f` | 10333 |
| `notes/C-HOMOGENEOUS-RECORD-RETENTION-N/SOURCES.tsv` | `3e55ad8d45179c8e0f6af34ed55387c970ba205f2bb2d18c18b581537d3c1c6b` | 3267 |
| `reproduce/C-HOMOGENEOUS-RECORD-RETENTION-N/verify.py` | `a349d3fc0711a59e6174a2534b47c62df766b1f6ab82e0e215ebcd8a596f26c7` | 33053 |
| `reproduce/C-HOMOGENEOUS-RECORD-RETENTION-N/EXPECTED.txt` | `dccec8381f051efede09b61cea2b15c6735a883a4286e2d13c131bc2ea0164d3` | 1162 |
| `reproduce/C-HOMOGENEOUS-RECORD-RETENTION-N/RUN.md` | `069c117630c735d5fb004ad7ff083598d847b6229ee248776a01381881a413dd` | 2315 |
| `reproduce/C-HOMOGENEOUS-RECORD-RETENTION-N/README.md` | `dfeda4dab4dbe7b7a2cd407e01bb37d82bdaad00eadfc31ce0b6344cee87f7ef` | 1853 |

The frozen parameters, the tolerance $1/100$, the first verdict
(`ACHIEVED`, $\varepsilon(10^6)\le7.475\times10^{-4}$), the disclosed pre-pin
floating-point evaluation, the toy-parameter exercises and the failed timing
wrapper invocation all remain part of the record.

The analytical documents are corrected forward in separate commits, one per
review item. Their reviewed versions remain at head `93d16b2`:

| File at `93d16b2` | SHA-256 | Bytes |
|---|---|---|
| `PROOF.md` | `d806d79ba7a647c1467c966c590c7b666de40e21bf60db6b99d60e20d5deb0b6` | 28645 |
| `INTERFACE.md` | `3e7657f899a83aede34823700170611f419f2e47e1e68b6082d68bbdec4b928f` | 3976 |
| `README.md` | `7d180df1d637e48814a82f8e696f7617c7141db722ba3527d8b4a8faa2aec1fb` | 3336 |
| `RESULT.md` | `9ec9ff500ac435d31c121507f2b3c6e6a5dd6b351059abf5ae3bda7c5577f826` | 5483 |

---

## R4. Protocol disposition (recorded before any further execution)

**Finding.** `PROTOCOL.md` says the package is not a `P-...` registration.
It nevertheless calls its execution, gates and falsifiers "formal",
introduces a new computed threshold result, and runs through a new
`reproduce/` directory. `POLICY.md` §3 and `AGENTS.md` §6 reserve formal
public work for the named probe route: public claim, `probe/P-NAME` branch,
`probes/P-NAME/` preregistration and verifier. A note's own declaration
creates no exemption.

**Disposition.**

1. **Classification.** The pinned package `24cc067` and its run are a
   **design-exposed NON-CANONICAL analytical construction with an exact
   reproduction**. The verifier audits the arithmetic of an analytical
   theorem whose constants were explored numerically before the pin. The run
   is a pinned audit execution. It is not a formal gate of a registered public
   probe, it satisfies no `P-...` obligation, and it is not a blind or
   independent confirmation.
2. **Reading of the frozen text.** In the unchanged `PROTOCOL.md`, `RUN.md` and
   `RESULT.md`, the words "formal execution", "formal gates" and "falsifiers"
   mean "pinned audit execution", "audit groups" and "preregistered audit
   failure conditions" of this non-formal construction. The pin, the
   tolerance and the first verdict keep their recorded values and dates.
3. **What the existing evidence is.** It consists of an exact single-program
   run on x86_64 and the same-program byte-identical replay in CI run
   `40117289016` (x86_64 and aarch64, Python 3.12.15). That workflow's
   `VERIFY NOT APPLICABLE` line confirms that no public probe was certified.
   `reproduce/` is used only as the repository's mechanism for exact byte
   replay of this audit. It carries no claim status, registry row or evidence
   row.
4. **Further runs in this package.** The correction audit for R1 and R2 checks
   exact identities that are already proved analytically. It introduces no new
   threshold, parameter or quantitative result. It runs in the same non-formal
   regime: its contract `CORRECTION_PROTOCOL.md` and its code
   `reproduce/C-HOMOGENEOUS-RECORD-RETENTION-BALANCE-N/verify.py` are
   committed, pushed and read back before its first execution. It lives in a
   separate directory, so the bytes of the first run are not touched.
5. **Formal successor (not created here).** A formal public test of any part of
   this work would need a new identifier and a collision check. It would also
   need a public claim reservation, a `probe/P-NAME` branch and
   `probes/P-NAME/` with `PREREG.md` and an accepted verifier pinned under
   `POLICY.md` §3, and then its own execution. It could not be obtained by
   renaming this executed pin. Its design exposure, through the disclosed
   floating-point evaluation and this run, would have to be declared in that
   preregistration. Canon promotion would require a separate sealed fold. This
   correction requests neither.

---

## R2. False commutator, contradictory location sentence, label typing

**Findings.** (a) `PROOF.md` Theorem 4, proof of item 3, said that
$U_0 = W\otimes\widetilde V$ commutes with $I\otimes\mathbf 1_{x<z}$. That is
false: the pulse hops across the cut. For example, a bank-1 pulse at $x = z-1$
acquires a bank-2 component at $x = z$ after one free step. (b) Theorem 1
item 4 ended with "The object, the helpers and nothing else carry it". That
sentence contradicted the preceding placement of the old information in the
carrier label or the memory. (c) `INTERFACE.md` §4 attached a second label
$e_k$ to $U^n\Omega_+\varphi$ although $\varphi$ already contains $p_1$, and
`PROOF.md` Corollary 1.2 and Corollary 6.1 had the same double-label typing.
(d) The dark-token example could be read as a classification of eternal
records. (e) The witness wording "held exactly for three steps" did not state
the elapsed times.

**Corrections (`PROOF.md`, `INTERFACE.md`, `README.md`).**

- Theorem 4 item 3 now uses only the commutation of $U_0$ with the velocity
  spectral projection $I\otimes\Pi_{v>0}$, together with the commutation of the
  partial inner products $\langle e_i|\otimes I$ with $I\otimes\Pi_{v>0}$ and
  $I\otimes\mathbf 1_{x<z}$. It says explicitly that $U_0$ does not commute
  with $I\otimes\mathbf 1_{x<z}$. The conclusion $\delta_n>0$ is unchanged.
- Theorem 1 item 4 is replaced by the exact conditional location read off
  equation (1). On $\mathbf 1_\ge\chi_n$ the old state is
  $\sum_ke_k\otimes\phi_k$, in the carrier label. On $\mathbf 1_<\chi_n$ it is
  $\sum_kd_k\otimes\phi_k$, in the memory. The spatial factor is independent of
  $k$, and reference–position correlation arises only through the kept
  left/right split.
- A label-stripping convention is added to `PROOF.md` §0:
  $\varphi = \varphi_{\rm sp}\otimes p_1$, $\Psi_{\rm loc} =
  \psi_{\rm loc}\otimes t_1$, and $U^n\Omega_+\varphi = \eta_n\otimes e_1$ with
  $\eta_n\in\mathcal H_{\rm sp}$. Corollary 1.2 now uses $\psi_{\rm loc}$, and
  Corollary 6.1 and `INTERFACE.md` §4 write the ideal record as
  $\sum_k\eta_n\otimes e_k\otimes d_1\otimes\phi_k$.
- Proposition 5 is stated as an existence example, not a classification. The
  permanence of a captured record remains open.
- The finite witness is described as zero wrong-memory weight at $n = 0,1,2$
  and nonzero weight at $n = 3$.

The R1/R2 correction audit
(`reproduce/C-HOMOGENEOUS-RECORD-RETENTION-BALANCE-N/`) also checks the
counterexample to the removed commutator exactly.
