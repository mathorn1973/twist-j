# `C-C40-RECIPROCAL-RAMIFIED-SEAM-N`

Status: **NON-CANONICAL incubation**  
Terminal grade: `candidate-T / L1`  
Lock and custody: [issue #750](https://github.com/mathorn1973/twist-j/issues/750)  
Frozen preregistration pin: [`aa44cfe32bf461c217d6046ff3c835d3bd12eca7`](https://github.com/mathorn1973/twist-j/commit/aa44cfe32bf461c217d6046ff3c835d3bd12eca7)

This packet records an exact arithmetic synthesis for
\(K_{40}=\mathbf Q(\zeta_{40})\). It is a public note, not a formal public
probe. It creates no evidence credit and changes no Canon, Registry, Frontier,
gate, or program status.

## Result in one line

The `2`-primary and `5`-primary parts of conductor `40` leave complementary,
nonreduced residue factorizations,

\[
\Phi_{40}\bmod2=\Phi_5^4,
\qquad
\Phi_{40}\bmod5=\Phi_8^4,
\]

while every unramified factor degree is an order in
\((\mathbf Z/40\mathbf Z)^\times\), whose exponent is `4`. Consequently
\(\Phi_{40}\) is reducible modulo every rational prime, but there is no
unramified inert rational prime in \(K_{40}\).

That modular statement must not be confused with local-field reducibility:
\(\Phi_{40}\) is irreducible over \(\mathbf Q_2\).

## Exact derivation

### Imported compositum boundary

Public Canon v74 already owns the compositum and intersection through
`DQRC-MAXIMAL-SECTOR-FIELD-BOUNDARY [T]`. The self-contained check here is:

\[
\zeta_5=\zeta_{40}^8,qquad
\zeta_8=\zeta_{40}^5,qquad
8\cdot2+5\cdot(-3)=1,
\]

so \(\zeta_{40}=\zeta_5^2\zeta_8^{-3}\). Hence the compositum is
\(\mathbf Q(\zeta_{40})\). Since its degree is
\(\varphi(40)=16=\varphi(5)\varphi(8)\), the degree formula gives trivial
intersection.

This is a dependency audit, not new candidate content.

### Polynomial and ramified reductions

Exact cyclotomic division gives

\[
\Phi_{40}(x)=x^{16}-x^{12}+x^8-x^4+1.
\]

In characteristic `2`, Frobenius to the fourth power gives

\[
(x^4+x^3+x^2+x+1)^4=x^{16}+x^{12}+x^8+x^4+1
=\Phi_{40}(x)\bmod2.
\]

The base polynomial is irreducible over \(\mathbf F_2\), because
\(\operatorname{ord}_5(2)=4\). In characteristic `5`, the binomial
coefficients give

\[
(x^4+1)^4=x^{16}-x^{12}+x^8-x^4+1,
\]

and

\[
x^4+1=(x^2-2)(x^2-3)\pmod5,
\]

with both quadratics irreducible over \(\mathbf F_5\).

For `n=p^a m` with `(p,m)=1`, cyclotomic local theory gives

\[
e=\varphi(p^a),\qquad f=\operatorname{ord}_m(p),\qquad
g=\frac{\varphi(n)}{ef}.
\]

Therefore:

| prime | repeated residue factorization | `(e,f,g)` | factorization over the local field |
|---:|---|---:|---|
| `2` | one degree-`4` factor, multiplicity `4` | `(4,4,1)` | one degree-`16` factor over `Q_2` |
| `5` | two degree-`2` factors, each multiplicity `4` | `(4,2,2)` | two degree-`8` factors over `Q_5` |

Both residue algebras are nonreduced. They are not etale products of fields.
The value `g=1` at ramified `2` means one prime above `2`, not inertness.

### Complete unramified atlas

For `p` not dividing `40`, every irreducible factor of `Phi_40 mod p` has
degree \(f=\operatorname{ord}_{40}(p)\), and the number of factors is
\(g=16/f\).

| `p mod 40` | `f` | number `g` | factorization type | density |
|---|---:|---:|---:|---:|
| `1` | 1 | 16 | `1^16` | `1/16` |
| `9,11,19,21,29,31,39` | 2 | 8 | `2^8` | `7/16` |
| `3,7,13,17,23,27,33,37` | 4 | 4 | `4^4` | `1/2` |

The density statement uses Dirichlet's theorem: the sixteen reduced residue
classes modulo `40` each have density `1/16`. Abelianity alone is not being
used as a substitute for that input.

Chinese remaindering gives

\[
(\mathbf Z/40\mathbf Z)^\times
\cong(\mathbf Z/8\mathbf Z)^\times\times(\mathbf Z/5\mathbf Z)^\times
\cong C_2\times C_2\times C_4.
\]

Its exponent is `4`, so an unramified Frobenius can never be a `16`-cycle.
This exact group argument proves the absence of unramified inert rational
primes. The finite scans in the two scripts are audits only.

## Canon dependency firewall

The packet imports, without promoting or reclaiming:

- `DQRC-MAXIMAL-SECTOR-FIELD-BOUNDARY [T]`;
- `QUARTIC-CYCLOTOMIC-TOTAL-RAMIFICATION-CENSUS [T]`;
- `J-BINARY-NORM-INDEX [T]`;
- `BORN-RESIDUAL-SPLIT [T]`.

The candidate delta is only the `K_40` synthesis above. In particular, this
note does not merge fields, choose a component or orientation, promote
`I-BILOCATED`, create a physical or causal seam, or imply RH.

## Reproduction map

- `PREREG.md` — immutable scope, falsifiers, and custody rule;
- `verify.py` / `EXPECTED.txt` — principal exact verifier and captured stdout;
- `break.py` / `BREAKER_EXPECTED.txt` — blind independent breaker and stdout;
- `RUN.md` — pin, environment, commands, and execution record;
- `RESULT.md` — terminal assessment;
- `PROMO-C-C40-RECIPROCAL-RAMIFIED-SEAM-N.md` — later-fold handoff only;
- `SHA256SUMS` — content hashes for the packet.

