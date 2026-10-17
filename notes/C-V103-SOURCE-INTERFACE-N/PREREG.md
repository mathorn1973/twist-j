# Preregistration: C-V103-SOURCE-INTERFACE-N

**Status:** NON-CANONICAL / L1 analytical candidate  
**Program:** [#1548](https://github.com/mathorn1973/twist-j/issues/1548) (Lane D)  
**Child issue:** [#1551](https://github.com/mathorn1973/twist-j/issues/1551)  
**Public session:** `Antigravity-20261016-v103-source-interface`  
**Author:** A. M. Thorn  
**License:** Apache-2.0

## Six Preregistration Fields (`POLICY.md` Section 3)

1. **Equation:**
   Exact parametric and inductive comparison across the inherited v102 native preparation families $E(\lambda,\mu)$ (550-point support), $E_{\mathrm{alt}}(\lambda,\mu)$ (150-point support), and $x_\lambda(0) = (\lambda,0,-\lambda,0,0,0)$ with $x_{\mathrm{empty}}(0) = (0,0,1,0,0,0)$ (100-state ready carrier), evaluating:
   - the piston comparison map $W(p_1,p_4,p_1',p_4') = (p_4,p_1,p_4',p_1')$ and shell-gate residue $h(x) = (p_4+2p_1, p_4'+2p_1') \in \mathbb{F}_5^2$ relative to $L\mathbb{Z}^4 = \{y \in \mathbb{Z}^4 : y_0+2y_1 \equiv y_2+2y_3 \equiv 0 \pmod 5\}$;
   - the six-stage domain/map/equality chain from $\mathbb{F}_5^6$ checkpoints through $W$, balanced lift $\ell$, integer split $P y + S_{\mathrm{st}} \sigma$, funded rational contact $a(q,r) = S\eta(q,r)$ under $H_B$, and declared receiver readouts;
   - the common-time $(q_n, r_n)$ factor and composed $H_B$ trajectory invariance for $E(\lambda,\mu)$ on an initially common complete receiver under any source-independent schedule;
   - the quadratic-form difference $H(W y) - H(y)$ for $H(y) = \frac{1}{2} y^T B_f y$ vs coordinate relabeling $W^T B_f W$.
   Questions Q1–Q4 of `CONTRACT.md` define the complete mathematical scope.

2. **Code:**
   `NONE / NOT_RUN`. This assignment authorizes analytical work only and forbids new numerical searches or exploratory scripts. All results rest on complete symbolic/parametric derivations and explicit algebraic witnesses in `PROOF.md`. Repository policy/Canon validators are administrative checks only.

3. **Carrier or data:**
   - Native checkpoint carrier $\mathbb{F}_5^6$ with affine chart $(z,A,B,C,D,q)$, piston residue carrier $\mathbb{F}_5^4$, and gate residue carrier $\mathbb{F}_5^2$.
   - Integer active-field carrier $\mathbb{Z}^4$, shell sublattice $L\mathbb{Z}^4$ of index $25$, raw split lattice $P\mathbb{Z}^4 \oplus S_{\mathrm{st}}\mathbb{Z}^2 \subset \mathbb{Z}^6$ of index $5$, and finite chain carrier $X_N$ / $\widehat{X}_N = X_N \times C_5$ (`FIELD-CONSERVATIVE-CHAIN-LAW`, `FIELD-LOCAL-WORK-RECORD`).
   - Rational wave/tape/contact carrier $\mathbb{Q}^D \times \mathbb{Q}^D \times (\mathbb{Q}^4)^4 \times (\mathbb{Z}/2\mathbb{Z}) \times ([0,B]\cap\mathbb{Q}) \times \mathbb{Q} \times \{+1,-1\}$ on the 705-site Dirichlet domain $D = Y + B_\star + B_\star \subset D_3$ (`SIGNED-PORT-OCCUPIED-REVERSIBILITY`, `FUNDED-CONTACT-INVOLUTION`).
   - All admitted canonical input files are bound by exact byte count, Git blob SHA, and SHA-256 in `SOURCES.tsv` and `INPUTS.sha256` at `a632c6a162dc87e60104d7a478e7650a6d5c4a1b`.

4. **Systematics:**
   - Strictly separate common raw reset $R(x_2) = R(x_0) = r_\star$ across preparations from common semantic `BLANK` decoding $\delta(R(x)) = \mathrm{BLANK}$ with message-dependent raw blank values.
   - Strictly separate occupied zero message `PRESENT(0)` ($\lambda=0$ or $\mu=0$) from an explicitly declared sixth absence preparation $x_{\mathrm{empty}}(0) = (0,0,1,0,0,0)$.
   - Strictly separate coordinate relabeling by $W$ (which conjugates operators and transforms $B_f \mapsto W^T B_f W$) from applying $W$ as a map on states in the fixed canonical quadratic form $H(y) = \frac{1}{2} y^T B_f y$.
   - Strictly separate residue gate membership $h(x) = (0,0) \in \mathbb{F}_5^2$, balanced integer lifting $\ell$, and the full 31-coordinate source preparation $(R, 0, P L w, 0)$ with $H(w)=1$ in `FIELD-CHAIN-FIRST-WORK`.
   - Preserve the exposure barrier for independent reviewer lane RD (`C-V103-SOURCE-INTERFACE-REVIEW-N`): commit and push `README.md`, `CONTRACT.md`, `PREREG.md`, `SOURCES.tsv`, and `INPUTS.sha256` first, read back the immutable specification commit, and publish the metadata receipt before committing `PROOF.md` and `RESULT.md`.

5. **Failure threshold:**
   Zero algebraic tolerance. Every parametric identity, set cardinality, prefix table, inductive invariant on $X_{14}$, gate-overlap classification, and composition invariance statement must hold identically over $\mathbb{F}_5$, $\mathbb{Z}$, or $\mathbb{Q}$ as typed. Any counterexample to a universal clause refutes that clause at its exact scope and is retained without altering `CONTRACT.md` or `PREREG.md`.

6. **Action layer:**
   `L1` throughout. All checkpoints, charts, lifts, field shears, and funded contacts are mathematical constructions at `L1`. No `L2`–`L6` lift, physical energy calibration, autonomous native compilation of $W$ or $\eta$, or Canon promotion is claimed.
