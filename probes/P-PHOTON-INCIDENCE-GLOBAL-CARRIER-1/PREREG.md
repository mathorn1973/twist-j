# P-PHOTON-INCIDENCE-GLOBAL-CARRIER-1 preregistration

**Status: FORMAL PREREGISTRATION / RESULT-EXPOSED / PROOF-FIRST**

Public claim: [issue #1992](https://github.com/mathorn1973/twist-j/issues/1992)
Owner: A. M. Thorn, coordinating the exact proof and audit
Branch: `probe/P-PHOTON-INCIDENCE-GLOBAL-CARRIER-1`
Directory: `probes/P-PHOTON-INCIDENCE-GLOBAL-CARRIER-1/`

The author adopts the L4 scalar incidence class and the literal character-preserving map below. The task is the global quadratic-support comparison for the selected lattice and incidence action. The operational characteristic, written argument and exploratory arithmetic had been exposed before the immutable pin. The first formal verifier invocation takes place only after public readback of the pin.

### Public authority

```text
STATE: ACTIVE
CANON: Public Canon v112
MAIN AT CLAIM: bdfe935fc973aa385986c08b989c1f66713661c9
TAG: canon-v112
TAG OBJECT: 6ff28f3d717532e2bf4a0d13f0e3fe529ce1cf3b
CONTENT_COMMIT: c5afa4bad34456efaf2c5a9eac0cc91886e3e689
CANON_SHA256: 246c76843fca21da8a4e7e16c3324d674690cd12c38b26d7fcd96cf094217534
CANON_BYTES: 1554930
```

## Field 1: equation and decision

The source action gives the quadratic form on its unit-character incidence graph. The proposed equality for the whole declared class is
\[
\det(\lambda I-T(k))=-\lambda Q_{B,R}(\omega,k),\qquad
\lambda=e^{-i\omega},\qquad
\iota(K_{B,R})=K_{\rm op}.
\]
The witness uses six spatial sign lines and one temporal sign line. The universal part of the statement is justified by the written operator identity, with the finite verifier auditing exact identities and controls.

### Six-component membership

Let \(B\) consist of the six pairs of squared length two. It is invariant under the signed-coordinate group and generates \(D_3\). Select the ordered basis \(b_1=(1,1,0),\,b_2=(1,0,1),\,b_3=(0,1,1)\) inside \(B\). Let \(T_v f(x)=f(x+v)\). The spatial endpoint difference is \(D_v=T_v-1\).

For rows in \(B\) use the identity block. For each remaining pair representative \(v=\sum_i n_i b_i\), set the row on the selected basis edges using

\[
D_v=\sum_{i=1}^3 P_{vi}D_{b_i},\qquad
P_{vi}=\left(\prod_{j<i}T_{b_j}^{n_j}\right)
       \frac{T_{b_i}^{n_i}-1}{T_{b_i}-1}.
\]

The quotient denotes a Laurent polynomial. For \(n>0\) it is \(\sum_{r=0}^{n-1}T^r\). For \(n<0\) it is \(-\sum_{r=n}^{-1}T^r\), and for \(n=0\) it vanishes. Multiplication of each divided difference by \(T_{b_i}-1\) makes the sum telescope. Thus \(R D_B=D_S\) holds on every finite-support scalar field. Conjugation by a signed coordinate permutation preserves the identity, including orientation-reversing changes of anchor.

Each centered symbol row therefore obeys
\[
\widetilde R_g(k)a_B(k)=a_S(k)
\]
at every \(k\). Multiplying a row by \(e^{i\langle k,v\rangle/2}\) leaves its squared norm unchanged. This expresses the metric directly by the displayed Laurent factors in the nearest-edge coordinates. Uniform positive definiteness follows from the identity contributions, which give \(h\ge (6/81)I\). Literal point-group action and all bundle transition laws hold before any null-set comparison.

An alternative equivariant presentation uses the average over all shortest paths of nearest steps from \(0\) to \(v\). The endpoint difference telescopes along every path, so their average is also an admissible rational \(R\). A signed coordinate permutation maps the path set bijectively to the corresponding path set. The action therefore supplies a second presentation of the same scalar reading. Both presentations preserve the complete scalar-gradient sector. Their rank-six graph concerns this sector of the rank-thirty edge model.

### Exact null-set comparison

For finite-support fields,
\[
D_v^*D_v=2-T_v-T_{-v}.
\]
Summing weighted antipodal pairs yields
\[
\sum_{v\in S^+}\frac{w_v}{324}D_v^*D_v
=\frac1{324}\sum_{v\in S} w_v(1-T_v).
\]
This also proves real-space equality of the spatial operator obtained from the source action and the spatial operator in the selected transfer. Varying the source action gives
\[
f_{m+1}-2f_m+f_{m-1}
+\frac1{324}\sum_{v\in S}w_v(1-T_v)f_m=0.
\]
The finite-support variational calculation produces a local finite-range operator. Its formula extends to arbitrary field sequences. At the middle index \(m\) the extended equation is the registered forward two-slice equation. Every unrestricted forward initial pair has a unique bilateral continuation since the coefficient of the earlier slice is one. The continuation generally lies outside the finite-support action domain.

Evaluate the finite Laurent operators on the unit character \(\lambda^m e^{i\langle k,x\rangle}\), with \(\lambda=e^{-i\omega}\). The character is a symbol evaluation outside the finite-support action domain. Its spatial symbol, denoted here by \(s\), follows from the pair identity. Its signed quadratic value is
\[
Q_{B,R}(\omega,k)
=2-\lambda-\lambda^{-1}
-\sum_{v\in S^+}\frac{w_v}{324}
        |e^{i\langle k,v\rangle}-1|^2
=4\sin^2(\omega/2)-s(k).
\]
This holds for every admissible \(B,R\) by the source incidence equality. On the operational side the already registered two-slice matrix is
\[
T(k)=
\begin{pmatrix}2-s(k)&-1\\1&0\end{pmatrix}.
\]
Its determinant comparison is the exact identity
\[
\det(\lambda I-T(k))=-\lambda\,Q_{B,R}(\omega,k).
\]
Since \(\lambda\) is a unit complex phase, this proves the equivalence of the two zero conditions at every base point. The comparison projection is total and preserves each character. It gives \(\iota(K_{B,R})=K_{\mathrm{op}}\), including both frequency branches and the common apex. [Selected transfer and characteristic](https://github.com/mathorn1973/twist-j/blob/bdfe935fc973aa385986c08b989c1f66713661c9/canon/REGISTRY.tsv#L406-L407)



## Field 2: accepted code

```text
file: probes/P-PHOTON-INCIDENCE-GLOBAL-CARRIER-1/verify.py
sha256: d2e8f78bf9c3ff62e6fd5dfa27cf1990c7d60cab4320721c7037c8bbd918258e
bytes: 16032
command: python3 probes/P-PHOTON-INCIDENCE-GLOBAL-CARRIER-1/verify.py
dependencies: Python standard library
arithmetic: exact integers and Laurent polynomials
input: fixed constants in verify.py and the definitions in this preregistration
timeout_seconds: 600
```

## Field 3: carrier and data

### Source and real-space action

Take the five squared lengths \(2,4,8,10,16\) of the registered L2 shell problem in \(\mathbb Z^3\). Use all displacements of those lengths. The subgroup they generate is \(D_3\). Indeed they have even coordinate sum and the nearest shell contains \((1,1,0),(1,0,1),(0,1,1)\), a basis of determinant of absolute value two. Use the connected component of the vertex \(0\). Its signed-coordinate group is \(G\), the group of all 48 signed permutations. [L2 shell and moment theorem](https://github.com/mathorn1973/twist-j/blob/bdfe935fc973aa385986c08b989c1f66713661c9/canon/REGISTRY.tsv#L398)

Use the positive integral weights of least total weight making the shell quartic moment isotropic. The registered source theorem gives \(W_*=(6,1,15,1,1)\) and directed second moment \(648|k|^2\). Choose one representative \(v\) of each spatial pair \(\{v,-v\}\) by taking the first nonzero coordinate positive. The pair coefficient is \(c_v=w_v/324\). This makes the spatial Dirichlet form have unit tangent coefficient because the paired second moment is \(324|k|^2\).

The source domain is finite-support scalar functions \(f:\mathbb Z\times D_3\to\mathbb C\), with literal function equality. The complexification permits character evaluation. Spatial edge cochains change sign under reversal of the same oriented edge, and use the same unshifted lattice upon orientation transport. Use the trivial flat connection. The source time lattice is the primitive integer translation line, with edges \(m\to m+1\). It is an auxiliary domain for the incidence calculation.

Choose a hyperbolic quadratic action built solely from the primitive time difference and the weighted spatial edge differences. Normalize the small-frequency time coefficient to the same unit as the small-momentum spatial coefficient. Because the time edge is primitive, the coefficient on its squared difference is one. The resulting action on the source domain is

\[
\mathcal A[f]=\sum_{m\in\mathbb Z,\,x\in D_3}
 \left(\left|f(m+1,x)-f(m,x)\right|^2
 -\sum_{v\in S^+} c_v\left|f(m,x+v)-f(m,x)\right|^2\right).
\]

Primitive time range, signature, flat connection, the connected component and unit tangent convention are adopted dictionary data. The quartic weight minimizer and the displayed second moment are inherited results. The use of the time line defines a translation character and a variational domain.

### Admissible carriers

Let \(P=\widehat{\mathbb Z\times D_3}=S^1\times T_{D_3}\), with literal equality of the character values on the two marked translation groups. For spatial charts use \(T_{D_3}=\mathbb R^3/\Gamma_{D_3}\), where \(\Gamma_{D_3}\) is the \(2\pi\)-dual of \(D_3\). A centered spatial edge of direction \(v\) has deck sign \(\chi_v(\gamma)=(-1)^{\langle\gamma,v\rangle/(2\pi)}\). A centered temporal edge has sign \(-1\) for a \(2\pi\) time shift. These conventions come from translating from an edge endpoint to its midpoint in the symbol. The midpoint labels an edge of the integer cochain.

The complete admitted class is specified by the following parameters. Write \(S^+\) for the 30 spatial pair representatives. Let \(B\) range over all signed-coordinate invariant sets of pairs in \(S^+\) that generate \(D_3\), and let \(D_B\) and \(D_S\) denote their endpoint-anchored real-space difference operators. For each such \(B\) admit every finite-range, spatial-translation-equivariant spatial cochain operator \(R\) from the \(B\) edges to the \(S^+\) edges with rational shift coefficients, subject to the following two conditions.

1. In the rows belonging to \(B\), \(R\) is the identity on those edge coordinates.
2. \(R D_B f=D_S f\) for every finitely supported scalar field. This is an equality of operator rows in the group ring \(\mathbb Q[D_3]\).

Spatial signed permutations act on oriented cochains, including their change of anchor when an orientation is reversed. Use all conjugates \(R_g=g R g^{-1}\) with equal weight \(1/48\). In centered Fourier charts write \(\widetilde R_g(k)\) for the symbol of \(R_g\). Equivalently one can obtain this symbol by multiplying each input column \(b\) by \(e^{i\langle k,b\rangle/2}\) and each output row \(v\) by \(e^{-i\langle k,v\rangle/2}\) relative to endpoint symbols. The spatial real sign bundle \(E_B\) consists of one line per pair in \(B\) with the deck signs specified above. Equip it with the quadratic form

\[
 h_{B,R;k}(u,u)=\frac{1}{48}\sum_{g\in G}
 \sum_{v\in S^+}\frac{w_v}{81}
       \left|(\widetilde R_g(k)u)_v\right|^2 .
\]

It is a smooth real metric. The diagonal contribution from the identity rows is positive definite. Every coefficient in a centered symbol changes by the product of the input and output signs, so the quadratic form descends. The average makes the metric invariant under all signed permutations. The normalization of spatial coordinates uses division of the centered complex difference symbol by \(2i\), so its real value is \(a_b(k)=\sin(\langle k,b\rangle/2)\). This accounts for the factor four between \(w_v/81\) and the real-space coefficient.

The L4 support carrier \(X_{B,R}\) is the graph over all of \(P\) of the marked unit-character incidence section of the time line plus \(E_B\). The character is normalized to \(f(0,0)=1\) before taking differences. In the time convention \(f(m,x)=e^{-im\omega+i\langle k,x\rangle}\), the temporal component is \(\tau(\omega)=2\sin(\omega/2)\). In the spatial coordinates above it is \(a_B(k)\). This graph is determined by source incidence at every character, including the identity character where both components vanish. The null subset \(K_{B,R}\) consists of the zeros of the restriction of the fibre quadratic form \(Q=\tau^2-h_{B,R}\) to this graph.

Literal equality in \(X_{B,R}\) is equality of the base characters and of the transported fibre entries under the specified sign transitions. A change of representatives is a signed change of frame. Two presentation changes carry the same reading if their graph identification preserves the marked base character and the scalar value of \(Q\) at every graph point. Independent edge cochains are a different domain from the marked incidence graph.

This enumeration by \(B,R\) gives the full class for this declared incidence reading, including both a full-shell presentation and twisted bundles with fewer edge types. Its scope is the scalar-gradient sector of the displayed local action. Admitting other L4 sources, temporal actions or physical readings requires specifying their own data.

### Admissible comparison map

The codomain is the character space of the same marked temporal translation and spatial lattice. Require the map to carry both character evaluations literally at every graph point. This selects the total projection \(([ \omega],[k],\tau,a_B)\mapsto([\omega],[k])\) uniquely. It is a homeomorphism with inverse given by the globally defined section graph. The condition uses only the marked translation groups and their equality. A proof of agreement must compare the complete projected null subset with the operational null set.

The temporal centered frame uses \(\tau=i e^{i\omega/2}(e^{-i\omega}-1)=2\sin(\omega/2)\). Each individual \(R\) has finite support. The class does not specify one common support radius for all \(R\). Every centered coefficient has the product of the corresponding input and output deck signs. The scalar graph is the support carrier, with literal equality of the marked base and transported fibre entries. Presentation equivalence preserves the marked base and quadratic value. The full-shell choice \(B=S^+,R=I\) also belongs to the class.

## Field 4: systematics

The source action and membership test use the registered L2 shell and moment theorem and the adopted real-space input dictionary. The L5 selected transfer enters at the comparison, after construction of the support and map. Phase anchoring, signed representatives and coefficient normalization are fixed throughout. The check distinguishes the primitive time signature and range, and the scalar-gradient sector of the incidence graph, from arbitrary fibre states.

The added time control \(+\eta|D_t^2 f|^2\) preserves the unit quadratic germ and the discrete time symmetries. Its global mismatch checks sensitivity to the choice of time range. The earlier Hermitian tangent germ and separated single-chart obstruction keep their registered scopes. The admitted sign-bundle route concerns the chosen incidence action only. The comparison supplies no physical occurrence, photon, polarization, propagator, thermodynamic phase or SI calibration.

## Field 5: failure thresholds and controls

The mathematical decision requires each equality exactly. Any exact counterexample to a listed statement fires its falsifier.

- F01. Shell counts, nearest-shell basis, normalized second moment, quartic isotropy or weighted symmetry fails.
- F02. The six-line factorization fails an identity row or an operator row of \(R D_B=D_S\).
- F03. Signed coordinate transport, reversal of the edge anchor, or the centered deck sign law fails.
- F04. The source metric has an incorrect coefficient, fails to descend or violates its \(6/81\) identity-block lower bound for the witness.
- F05. A declared admissible representation violates the universal source-energy equality on its incidence graph.
- F06. The paired quadratic operator differs from the directed operator or the Euler equation differs from the declared recurrence.
- F07. The Laurent-polynomial determinant equality fails.
- F08. The exact two-torsion census or the total and unique character-preserving graph projection and its exact global null-set equality fails.

Required negative controls corrupt one Laurent factorization row, change the spatial coefficient or shell census, omit orientation anchor transport, twist the fixed trivial connection, change the primitive time coefficient, add the positive second-difference time term, and use the full fibrewise null cone in place of the incidence graph. Rejection of an intentionally altered control is an expected part of PASS.

For the temporal controls take \(k=\pi(1,1,1)/2\) and \(\lambda=(5+i\sqrt{11})/6\). At this operational null point \(s=1/3\). Coefficient \(c\ne1\) yields \((c-1)/3\) and the added term with \(\eta>0\) yields \(\eta/9\). For the full fibre control, the zero vector lies over \(\lambda=-1,k=0\), where the operational characteristic is nonzero.

PASS requires the proof's universal statements, the exact finite audit, rejection of each control, the same verifier hash, zero exit, empty stderr and byte-identical stdout in the required architecture jobs. A completed exact falsifier yields BREAK and is retained. A pin mismatch, runtime error, incomplete execution or transcript integrity failure without a checked mathematical counterexample is STOP.

## Field 6: action layers

The proposed incidence-support dictionary is L2 → L4. The admitted class and literal comparison map determine the scoped existential witness for `GATE-L4-L5-PHOTON-GLOBAL-CARRIER`. A passing probe supports AGREE and a separate reviewed Canon D fold for `PHOTON-CONE-CONVERGENCE`. The probe changes one probe directory.

## Execution and custody

Commit and push this file and verify.py. Fetch and read back the commit and both file hashes before the formal command. Run the pinned verifier from the repository root on Linux. Record the exact stdout in EXPECTED.txt and the exit code, environment and hashes in RUN.md. RESULT.md records the scientific outcome. The hosted x86_64 and aarch64 jobs replay the same verifier and match the same expected bytes.
