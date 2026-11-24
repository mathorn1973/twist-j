# Round 18. Closed chains in the actual period Gram expansion

**NON-CANONICAL. No authority. No Canon status change.** The mathematical source is [RH commit 40e56bab026552e089d7afcfeff08d2defb9c005][pin]. The deductions are **candidate-D** under the stated hypotheses. The required estimate on the actual period family remains **O**.

## 1. Operator expansion

Retain the concrete `SConc` realization, its fixed `SIso`, and the actual full Poincaré maps $P_u:E_u\to F$, normalized by $A_u=P_u/\sqrt{c_0(u)}$ with positive $c_0(u)$. Use the two-prime integral split frame, `ColReps`, `LevelSubgroupCharacter`, `LevelSubgroupNormalized` and the ordered-pair conclusions `KExpansion`, `AbsConvT` and `OOIntAll` under their hypotheses. Here $F$ is the full row space before the good-row cut and $E_u$ is the full column space before the ramified cut. [Geometric realization][sconc] · [Normalization][kform] · [Unfolding proof][kexp-proof] · [Integrability and convergence suppliers][ooint-all].

Write $G_{uv}=A_u^*A_v$ and $\widehat G_{uv}={\rm sharp}_uG_{uv}{\rm sharp}_v^{-1}$ in the finite class-coordinate spaces $C_u=\bigoplus_{\rho\in {\rm Cl}_u}V_{\pi,u}$. The class-coordinate identifications are antiunitary. The flipped inner product in `KExpansion` gives precisely $\widehat G_{uv}$. An ordered cycle trace in $C_u$ is the complex conjugate of its trace in $E_u$. Each $(\rho,\rho')$ block of $\widehat G_{uv}$ is the source's sum of `blk` over geometric terms. The proof of `summable_blk_of_abs` bounds the sum of their operator norms by the `AbsConvT` majorant. [Flipped inner product][sharp] · [Block definition][blocks] · [Exact operator expansion][kexp] · [Absolute block summability][summable].

## 2. Exact finite and archimedean formulas

**Candidate-D.** Fix a cycle $u_1,\ldots,u_\ell$, $u_{\ell+1}=u_1$, allowing repeats. Choose a column class $\rho_i$ at each vertex and write $x_i=h_{\rho_i}x_{u_i}$. For each leg choose a geometric term $t_i$ for $(u_i,u_{i+1})$. Write $\gamma_i$ for the rational unitary underlying `t_i.pt` and $\lambda_{u_i}(\rho_i)$ for the lattice of the column class. A term can contribute only if

$$
 \lambda_{u_i}(\rho_i)=t_i.{\rm lam},\qquad
 \lambda_{u_{i+1}}(\rho_{i+1})=t_i.{\rm lam}',\qquad
 k_i=x_i^{-1}\gamma_{i,f}x_{i+1}\in K_2 .
$$

Each $\gamma_i$ sends the lattice at vertex $i+1$ onto the one at vertex $i$. Set $\gamma_\circ=\gamma_1\cdots\gamma_\ell$ and $k_\circ=k_1\cdots k_\ell$. Telescoping the finite parts and using the level character law give

$$
 k_\circ=x_1^{-1}\gamma_{\circ,f}x_1\in K_2,\qquad
 \prod_i\chi_2(k_i)=\chi_2(k_\circ),\qquad
 \gamma_\circ\lambda_{u_1}(\rho_1)=\lambda_{u_1}(\rho_1).       \tag{18.S1}
$$

These equalities use the chosen representatives `GTerm.rep`. Classification by a representative-independent rational closing element would require a separate check of the equivalence relation. [Rational matrix and lattice matching][rat] · [Finite block support and phase][blocks] · [Level character][level-character].

**Candidate-D.** In the actual two-prime integral split level, $\gamma_\circ$ is rational special unitary. Since $k_\circ$ preserves the finite integral lattice and $\det\gamma_\circ=\det k_\circ$ at the finite places, $\det\gamma_\circ$ is an integral norm-one unit. All its complex absolute values equal one, so it is a root of unity. The level congruence gives determinant one modulo a place over each of the two distinct rational primes. A root of unity reducing to one in residue characteristic $p$ has $p$-power order. For its prime-to-$p$ part $z$ of order $n$, the factor $1+z+\cdots+z^{n-1}$ is a unit when $z\equiv1$, so $z^n=1$ implies $z=1$. The two residue characteristics force order one. The additive level character still appears in (18.S1). The rational identity closing element has phase one. [Two-prime determinant congruence][r17-det] · [Additive level formula][level-form].

Put $O_i={\rm OOt}(t_i)$ and $b_i={\rm scl}(F_{N,u_i},F_{N,u_{i+1}})\operatorname{vol}(K_2)$. A supported tuple contributes

$$
 \left(\prod_i b_i\right)\chi_2(k_\circ)
      \operatorname{tr}_{V_{\pi,u_1}}(O_1\cdots O_\ell).          \tag{18.S2}
$$

Summing (18.S2) over the supported terms and column indices gives $\operatorname{tr}_{C_{u_1}}(\widehat G_{u_1u_2}\cdots\widehat G_{u_\ell u_1})$. Block multiplication enforces matching intermediate columns. There are finitely many column tuples. For each tuple the product of the absolute edge majorants and $|\operatorname{tr}(O_1\cdots O_\ell)|\le\dim V_{\pi,u_1}\prod_i\|O_i\|$ justify the expansion with the factors $b_i$. [Block composition][blocks] · [Absolute block summability][summable].

For $z_i\in{\rm FundOf}(t_i)$ put $v_i=W_{u_i}(z_i)$ and $w_i=W_{u_{i+1}}(\gamma_{i,\infty}^{-1}z_i)$. The source defines $O_i$ as the Bochner integral of $\xi\mapsto\langle w_i,\xi\rangle v_i$, with inner product linear in its second entry. The rank-one product has trace

$$
 \operatorname{tr}(O_1\cdots O_\ell)
 =\int_{\prod_i {\rm FundOf}(t_i)}
       \prod_{i=1}^{\ell}\langle w_i,v_{i+1}\rangle\,\prod_i d\mu_\infty(z_i),
 \qquad v_{\ell+1}=v_1.                                         \tag{18.S3}
$$

The integrand is bounded by $\prod_i\|w_i\|\|v_i\|$. Each factor is integrable by `OOIntAll` and the rank-one operator norm formula, which proves Fubini for each fixed tuple. The stronger `OOLintSum` supplier also makes the sum of the absolute integrals over all term tuples finite by multiplying its edge majorants. With `AbsConvT` and `OOIntAll` the sum of separately formed integrals already converges absolutely. [Rank-one integral and domain][oo] · [Norm and integrability proof][oo-norm] · [Stronger absolute-integral supplier][oo-sum].

**Candidate-D.** The determinant multipliers of round 17 have equal source phases at the two ends of each supported leg. Averaging their phases leaves every term in (18.S2). The additive level character permits a different formal test. It has finite image of order $h$, since its kernel contains the principal congruence subgroup of finite index in $K_2$. In the same array replace each $\chi_2(k_i)$ by $\chi_2(k_i)^j$ for $j\bmod h$. The absolute majorant is unchanged. Character orthogonality selects exactly the summands with $\chi_2(k_\circ)=1$ in the average. Fourier weights select any specified phase. The residue $j=1$ gives the actual source array. Identifying another one with automorphic period maps would require a geometric realization at the changed level character. [Determinant intertwiners][r17-phase] · [Triviality on the principal level][level-character].

## 3. A sufficient estimate on the multiplicity spaces

**Candidate-D.** Write $D=\dim F>0$, $n_u=\dim E_u$, $R=\sum_u n_u>0$, $S=\sum_u A_uA_u^*$ and $Q=(D/R)S$. Under the sharper diagonal bound $\|A_u^*A_u-I\|_{\rm HS}^2\le e_F n_u$, the centered frame comparison gives

$$
 \epsilon(P)\le\sqrt{e_F}+D^{-1}\operatorname{tr}((Q-I)_+).         \tag{18.S4}
$$

For $L_u=A_u^{-1}W$ and the orthogonal projector $\Pi_W$, the trace of $A_u^*\Pi_W A_u$ is at least the trace of $A_u^*A_u$ on $L_u$. The latter differs from $\dim L_u$ by at most $n_u\sqrt{e_F}$ by Hilbert–Schmidt Cauchy–Schwarz. Sum, divide by $R$, subtract $\dim W/D$ and bound by the positive-part trace. Also $|\operatorname{tr}(Q-I)|\le D\sqrt{e_F}$. At a scale $\tau$ with $\sqrt{e_F}=O(\tau)$, either of these estimates would suffice.

- $D^{-1}\operatorname{tr}((I-Q)_+)=O(\tau)$. A stronger sufficient condition is a lower spectral bound $1-O(\tau)$ outside a spectral subspace of relative dimension $O(\tau)$, using $Q\ge0$.
- $D^{-1}\operatorname{tr}((Q-I)^{2a})=O(\tau^{2a})$ for a fixed integer $a\ge1$. Hölder bounds the normalized trace norm without a factor growing in $D$.

The centered frame comparison belongs to the separately owned [issue 2065](https://github.com/mathorn1973/twist-j/issues/2065) and [PR 2067](https://github.com/mathorn1973/twist-j/pull/2067). The new formula gives the ordered traces entering its moments. Cyclic permutation in the trace expresses $\operatorname{tr}_F(S^\ell)$ as the sum of $\operatorname{tr}_{E_{u_1}}(G_{u_1u_2}\cdots G_{u_\ell u_1})$ over ordered word tuples. Centering requires the signed combinations of these moment sums and the identity term. The diagonal words contribute $(D/R)(1+O(\sqrt{e_F}+e_F))$ to $D^{-1}\operatorname{tr}(Q^2)$. An exponentially small centered variance requires compensating this term up to the trace normalization error. The off-diagonal upper bound $(1+\eta_0)n_un_v/D_*$ for $\|G_{uv}\|_{\rm HS}^2$ supplies no such deficit. [Sharp diagonal bound][diag] · [Source trace and square-trace estimates][pair-moment].

For the common algebra of round 17 let $z_\beta$ project to the simple type $\mathbb C^{s_\beta}\otimes M_\beta$, and let $z_{\beta,u}$ denote its source action. Write $a_{u,\beta}$ for the normalized multiplicity maps, $S_\beta=\sum_u a_{u,\beta}a_{u,\beta}^*$ and $Q_\beta=(D/R)S_\beta$. The exact intertwiner and trace identity give

$$
 \begin{aligned}
 s_\beta\operatorname{tr}_{M_\beta}(S_\beta^\ell)
   &=\operatorname{tr}_F(z_\beta S^\ell)\\
   &=\sum_{u_1,\dots,u_\ell}\operatorname{tr}_{E_{u_1}}
      (z_{\beta,u_1}G_{u_1u_2}\cdots G_{u_\ell u_1}),\\
 \operatorname{tr}_F((Q-I)_+)
   &=\sum_\beta s_\beta\operatorname{tr}_{M_\beta}((Q_\beta-I)_+) .
 \end{aligned}                                                   \tag{18.S5}
$$

The factors $D/R$ and $s_\beta$ use the full-space normalization. The class-coordinate insertion is $\mathrm{sharp}_{u_1}z_{\beta,u_1}\mathrm{sharp}_{u_1}^{-1}$. If it mixes column classes, its entries need a separate phase analysis. The finite telescoping applies directly to traces with no insertion or with a column-diagonal insertion. The general product with an insertion still has an absolutely convergent operator expansion. [Common algebra and multiplicity decomposition][r17-mult].

**O.** The audited source computes a Hilbert–Schmidt square using `RP` and `pvR`. These pair two terms for one ordered word pair with common lattice-pair and Levi label through `rowOf`. Formula (18.S2) joins successive terms through each intermediate column, with the overlaps (18.S3) and one closing phase. An additional estimate would have to control signed sums of these overlaps at the centered moment precision, or give the lower spectral estimate above. The round 9 comparison has exactly centered normalized $2a$-th moment $(1-\rho)\sigma^a$ for $\sigma=D/R$, since its eigenvalues are $1$ and $1\pm\sqrt{\sigma}$ with the stated proportions. Its defect remains $(1-\rho)\sqrt{\sigma}/2$. Thus a bound at the $\sigma^a$ scale can leave the square-root obstruction for every fixed $a$. The spectral criteria here are sufficient conditions. [Pair packet][pairs] · [Levi kernel][pair-label] · [Scalar norm transfer][normtie] · [Round 9 model][r9].

The cited definitions and proofs were read at the mathematical pin. No numerical instance, scientific computation, Lean run, or source update was used.

[pin]: https://github.com/leanprover-community/riemann-hypothesis/tree/40e56bab026552e089d7afcfeff08d2defb9c005
[sconc]: https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/ParametersTermRelations.lean#L286-L323
[kform]: https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/LocalToGlobal/SiegelLatticeTheory/HaarTransversals/PoincareInHH.lean#L252-L263
[kexp-proof]: https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedLocalOrbits/GaugeLatticeShifts/DoubleCosetSingleUnfolding.lean#L466-L496
[ooint-all]: https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedLocalOrbits/GaugeLatticeShifts/DoubleCosetSingleUnfolding.lean#L435-L447
[sharp]: https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/ParametersTermRelations.lean#L25-L75
[blocks]: https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedLocalOrbits/TermOp.lean#L194-L263
[kexp]: https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedLocalOrbits/TermOpStmt.lean#L21-L31
[summable]: https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedLocalOrbits/GaugeLatticeShifts/KExpCut.lean#L406-L441
[rat]: https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedLocalOrbits/TermOp.lean#L60-L104
[level-character]: https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/LocalToGlobal/SiegelLatticeTheory/HaarTransversals/HidaSetting.lean#L346-L365
[level-form]: https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/LocalToGlobal/SiegelLatticeTheory/HaarTransversals/HidaSetting.lean#L117-L128
[oo]: https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedLocalOrbits/TermOp.lean#L140-L151
[oo-norm]: https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedLocalOrbits/GaugeLatticeShifts/KExpCut.lean#L337-L359
[oo-sum]: https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedLocalOrbits/GaugeLatticeShifts/DoubleCosetSingleUnfolding.lean#L373-L396
[diag]: https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/SharpRestriction/CuspSpanNormBounds/StandingHypothesesHoldFamily.lean#L119-L184
[pair-moment]: https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/SharpRestriction/CuspSpanNormBounds/AdmissibleBoundsFromSource.lean#L212-L259
[pairs]: https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/ParametersTermRelations.lean#L170-L236
[pair-label]: https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedLocalOrbits/TermOp.lean#L322-L360
[normtie]: https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/ParametersTermRelations.lean#L338-L389
[r17-det]: ../round17/OPPOSITION.md#joint-determinant-twists-with-one-global-unit-loss
[r17-phase]: ../round17/REPORT.md#3-exact-common-action-and-support
[r17-mult]: ../round17/REPORT.md#7-the-exact-remaining-obligation
[r9]: ../round9/PROOF.md#32-exact-defect-over-every-complex-subspace
