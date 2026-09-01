# Preregistration: `C-C40-RECIPROCAL-RAMIFIED-SEAM-N`

Status: **NON-CANONICAL incubation**  
Owner: `session-c40-seam-2026-09-01`  
Lock: [issue #750](https://github.com/mathorn1973/twist-j/issues/750)  
Maximum output: `candidate-T / L1`

This note preregisters one exact arithmetic audit. It is not a formal public
probe, carries no evidence credit, and does not alter Canon, Registry,
Frontier, any gate, or program status. A later, separate public fold would be
required for any promotion.

## Frozen object

Let

\[
K_{40}=\mathbf Q(\zeta_{40}),\qquad
\Phi_{40}(x)=x^{16}-x^{12}+x^8-x^4+1.
\]

The word *seam* denotes only the exact complementary ramified reductions at
the rational primes `2` and `5`. It does not denote a merger of fields, a
physical bridge, a causal mechanism, a selector, or an RH consequence.

## Registered dependency and novelty boundary

Public Canon v74 row `DQRC-MAXIMAL-SECTOR-FIELD-BOUNDARY [T]` already records
\(\mathbf Q(\zeta_5)\cap\mathbf Q(\zeta_8)=\mathbf Q\), their compositum
\(\mathbf Q(\zeta_{40})\), and degree `16`. Those facts are imported registered
theorems, not new candidate output. Three further registered dependencies are
kept behind the same firewall: `QUARTIC-CYCLOTOMIC-TOTAL-RAMIFICATION-CENSUS
[T]` already owns `e=4` at `(K_8,2)` and `(K_5,5)`;
`J-BINARY-NORM-INDEX [T]` already uses the inert `p=2` residue field `F_16` in
`K_5`; and `BORN-RESIDUAL-SPLIT [T]` already owns the two-quadratic
factorization of `Phi_8 mod 5` and its conjugation swap. These facts are
nevertheless checked again below as self-contained dependency audits. The
genuinely new candidate scope is limited to the `K_40` synthesis: `Phi_40`,
the repeated ramified reductions and resulting local profiles, the complete
unramified modulo-`40` atlas and densities, and the exponent/no-unramified-
inert conclusion.

## Frozen claims to test

1. **Compositum and generators.**
   \[
   \mathbf Q(\zeta_5)\mathbf Q(\zeta_8)=\mathbf Q(\zeta_{40}),
   \quad \zeta_5=\zeta_{40}^{8},
   \quad \zeta_8=\zeta_{40}^{5},
   \quad \zeta_{40}=\zeta_5^2\zeta_8^{-3}.
   \]
   The degree check is `4 * 4 = 16`; coprime conductors `5` and `8` give
   trivial intersection. More explicitly, `8*2 + 5*(-3) = 1` puts
   `zeta_40` in the compositum, while the degree formula
   `[KL:Q][K intersection L:Q]=[K:Q][L:Q]` then gives intersection degree one.

2. **Cyclotomic polynomial.**
   \[
   \Phi_{40}(x)=x^{16}-x^{12}+x^8-x^4+1.
   \]

3. **Ramified reductions and local profiles.**
   \[
   \Phi_{40}(x)\bmod 2=\Phi_5(x)^4
   =(x^4+x^3+x^2+x+1)^4,
   \]
   where `Phi_5` is irreducible over `F_2`, and
   \[
   \Phi_{40}(x)\bmod 5=\Phi_8(x)^4
   =(x^4+1)^4=(x^2-2)^4(x^2-3)^4,
   \]
   where both quadratics are irreducible over `F_5`. The corresponding
   `(e,f,g)` profiles are `(4,4,1)` at `2` (one prime) and `(4,2,2)` at `5`
   (two primes). These reductions have repeated factors and are not etale
   products of fields. In each reduction the `p`-primary cyclotomic part
   supplies multiplicity four while the prime-to-`p` part controls the
   separable factors. Thus `Phi_40` remains irreducible over `Q_2`: its one
   completion has degree `ef=16`, even though its reduction modulo `2` is the
   repeated polynomial `Phi_5^4`. Over `Q_5`, by contrast, `Phi_40` has two
   irreducible factors of degree `ef=8`; modulo `5` they become the two
   degree-`2` factors, each with multiplicity `4`. Residue-factor degrees must
   not be confused with degrees of the `p`-adic factors. The value `g=1` at
   the ramified prime `2` means one prime above `2`; it is not an inertness
   statement.

4. **Complete unramified atlas.** For every rational prime `p` not dividing
   `40`, put `f=ord_40(p)` and `g=16/f`. The exact unit-class partition is:

   | `p mod 40` | `f` | factorization type of `Phi_40 mod p` | Dirichlet density |
   |---|---:|---:|---:|
   | `1` | 1 | `1^16` | `1/16` |
   | `9,11,19,21,29,31,39` | 2 | `2^8` | `7/16` |
   | `3,7,13,17,23,27,33,37` | 4 | `4^4` | `8/16 = 1/2` |

5. **Group and inertness.**
   \[
   \operatorname{Gal}(K_{40}/\mathbf Q)
   \cong (\mathbf Z/40\mathbf Z)^\times
   \cong C_4\times C_2\times C_2.
   \]
   Its exponent is `4`; therefore no unramified rational prime is inert in
   `K_40`. Together with the two ramified identities, `Phi_40 mod p` is
   reducible for every rational prime `p`.

In the atlas notation `f^g`, `f` is the common irreducible-factor degree and
`g` is the number of distinct factors; it is not exponentiation of degrees.

## Frozen acceptance rule

The incubation may end at `candidate-T / L1` only if both frozen Python
programs terminate successfully and independently confirm every item above.
The principal verifier must derive cyclotomic polynomials over `Z`, check both
ramified polynomial identities and irreducibilities, enumerate all units
modulo `40`, recover the exact class/order/type/density table, and perform a
finite prime scan as an audit. The breaker must be independently authored from
this preregistration and must attempt the decisive falsifiers below without
reading the principal verifier.

The finite prime scan is **audit evidence only**. The proof of the universal
unramified statement is the exact exponent/order argument, not enumeration.
Likewise, *reciprocal* describes complementary `2`- and `5`-primary reduction
roles, not a symmetry exchanging the primes: `(4,4,1)` and `(4,2,2)` are
different local profiles.

## Decisive falsifiers

The result is `STOP` if either frozen program finds any of the following:

- failure of a compositum exponent, degree, cyclotomic, or reduction identity;
- a wrong irreducible-factor multiplicity at `2` or `5`;
- a mismatch between a unit class modulo `40`, its order, its factorization
  type, or the stated density;
- an element of order `16` in `(Z/40Z)^*`, or an unramified inert prime;
- a field-merger interpretation of reduction at a ramified prime;
- a collision with an existing canonical row at stronger scope.

No conclusion may merge the two fields, create a selector, or promote
`I-BILOCATED` or any other registered row.

## Frozen execution and custody

`PREREG.md`, `verify.py`, and the independently authored `break.py` must be
committed together on branch
`notes/c-c40-reciprocal-ramified-seam-n`, read back from GitHub, and pinned by
full commit SHA plus SHA-256 file hashes in issue #750 before either program is
executed. After that pin these three files are immutable. Exact stdout is then
preserved in `EXPECTED.txt` and `BREAKER_EXPECTED.txt`; the terminal record is
reported in `RESULT.md` and the non-authoritative handoff in
`PROMO-C-C40-RECIPROCAL-RAMIFIED-SEAM-N.md`.
