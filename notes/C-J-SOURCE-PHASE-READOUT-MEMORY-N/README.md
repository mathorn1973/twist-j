# TWIST-J source, phase readout, and memory

**Working item:** C-J-SOURCE-PHASE-READOUT-MEMORY-N  
**Author:** A. M. Thorn  
**Date:** 29 September 2026  
**Scope:** PUBLIC, NON-CANONICAL; notes-only; no authority  
**Scientific ceiling:** candidate-T for Theorems A and C; candidate-C for the exact one-architecture finite certificates reported below; one explicit O remains open. No Canon, Registry, Frontier, GATES, release, activation, or formal probe file is changed.

## 0. Purpose and authority boundary

This note isolates a small exact apparatus built on the public TWIST-J arithmetic:

- a chosen two-coordinate source symbol;
- an affine carrier step in `O = Z[zeta_5]`;
- an exact phase readout of the residue class modulo 5;
- a reversible two-step record cycle with pointer reset;
- an archive that distinguishes histories which the final carrier can no longer distinguish;
- an exponential upper bound on the number of distinct exact carrier endpoints.

At authorship time `STATUS.md` declares Public Canon v92 active. This note does not depend on unpublished v93 content and does not promote any statement into the Canon.

The construction makes explicit choices. In particular, the source port, the 25-symbol alphabet, the two-step read timing, and any quadratic probability rule are not derived here from native `U`. The note proves consequences **conditional on those choices**.

A one-architecture external review supplied after the first draft independently recomputed the self-contained arithmetic with Python 3 on Linux x86_64: 49 checks passed, 0 failed, and one inherited `q`-transport check was skipped because its definition was outside the reviewed document. The review was not a formal public pin and did not provide a second-architecture run. Its corrections are incorporated below; section 11 records the evidence boundary.

## 1. Arithmetic and explicit source choice

Write

\[
K=\mathbb Q(\zeta),\qquad O=\mathbb Z[\zeta],\qquad
1+\zeta+\zeta^2+\zeta^3+\zeta^4=0,
\]

and

\[
J=1+\zeta^2,\qquad J^{-1}=-\zeta-\zeta^2.
\]

The public v92 basis supplies the two complex sizes

\[
|\sigma_1J|=\varphi^{-1},\qquad |\sigma_2J|=\varphi,
\qquad h=2\log\varphi.
\]

The equality of this `h` with toral entropy is an inherited public input. The endpoint-count theorem in section 8 has its own direct proof, but the numerical exponent is produced by the **same expanding/contracting mechanism**, not by an independent occurrence of the same number.

Choose a source symbol

\[
s_n=(u_n,v_n)\in\{-2,-1,0,1,2\}^2,
\qquad b(s_n)=u_n+v_n\zeta.
\]

The carrier obeys

\[
\boxed{\alpha_{n+1}=J\alpha_n+b(s_n).}
\]

The 25 inputs are a chosen interface, not a derived cardinality of a native physical port. For fixed `s`, the map is bijective with inverse

\[
\alpha_n=J^{-1}(\alpha_{n+1}-b(s_n)).
\]

Hence its linear extension on the basis `|alpha>` is unitary. A coherent source can be retained as a control register; the source label is not erased by the carrier update.

In the power basis `1,zeta,zeta^2,zeta^3`, for `alpha=(x,y,z,t)`,

\[
M_J=
\begin{pmatrix}
1&0&-1&1\\
0&1&-1&0\\
1&0&0&0\\
0&1&-1&1
\end{pmatrix},
\]

with an integral inverse. The verifier uses only exact integer/cyclotomic arithmetic.

## 2. Theorem A: two source symbols are exactly recoverable from one two-step residue change

After two steps,

\[
\beta=J^2\alpha+J(u_0+v_0\zeta)+(u_1+v_1\zeta).
\]

Let

\[
d=\beta-J^2\alpha=(d_0,d_1,d_2,d_3).
\]

Since `J=1+zeta^2` and `J zeta=zeta+zeta^3`,

\[
\boxed{d=(u_0+u_1,\ v_0+v_1,\ u_0,\ v_0).}
\]

Therefore

\[
\boxed{(u_0,v_0,u_1,v_1)
=(d_2,d_3,d_0-d_2,d_1-d_3).}
\]

The change-of-basis matrix

\[
L=\begin{pmatrix}
1&0&1&0\\
0&1&0&1\\
1&0&0&0\\
0&1&0&0
\end{pmatrix}
\]

has determinant 1. Thus the decoding is integral and remains bijective modulo every integer modulus.

For modulus 5 and every known initial residue `m = alpha mod 5`, the 625 ordered pairs of source symbols map bijectively to the 625 possible final residues. The integer lifts are then unique because the source alphabet was fixed in advance to `[-2,2]^2`.

This reconstructs the **chosen two source coordinates per step**, not the full native six-coordinate checkpoint.

## 3. The finite readout ring is ramified, not a field

The apparatus reads

\[
A_5=O/5O\cong\mathbb F_5[\epsilon]/(\epsilon^4),
\qquad \epsilon=\zeta-1.
\]

This is a 625-element ring with nilpotents, not `F_625`. Since

\[
\Phi_5(X)=(X-1)^4\pmod5,
\]

one gets

\[
J=2+2\epsilon+\epsilon^2,\qquad
J^5=2,\qquad J^{10}=-1,\qquad J^{20}=1\pmod5,
\]

and the exact order of `J` modulo 5 is 20.

This finite orbit is not the positive-entropy toral system and not the order-10 action on the exterior-power periodic lattice. No complex embedding, norm ratio, or toral entropy is transferred to `A_5` merely by reduction modulo 5.

## 4. Exact coherent phase readout of the four residue coordinates

Let

\[
\delta=\frac{\zeta^2-\zeta}{5},\qquad
\chi_\alpha(x)=\exp(2\pi i\,\operatorname{Tr}(\delta\alpha x)).
\]

The trace-pairing matrix and its inverse are

\[
Q=\begin{pmatrix}
0&0&0&1\\
0&0&1&-1\\
0&1&-1&0\\
1&-1&0&0
\end{pmatrix},
\qquad
Q^{-1}=\begin{pmatrix}
1&1&1&1\\
1&1&1&0\\
1&1&0&0\\
1&0&0&0
\end{pmatrix}.
\]

Its columns determine `v_j` satisfying

\[
\operatorname{Tr}(\delta\zeta^i v_j)=\delta_{ij}.
\]

For `y_j=v_j/5` and `alpha=sum a_j zeta^j`, translation gives

\[
T_{y_j}|\alpha\rangle=\zeta^{a_j}|\alpha\rangle.
\]

With the five-point Fourier transform

\[
F_5|r\rangle=\frac1{\sqrt5}\sum_{t=0}^4\zeta^{rt}|t\rangle
\]

and the controlled translation `C_j`, define

\[
R_j=(F_5^\dagger\otimes I)C_j(F_5\otimes I).
\]

Then exactly

\[
\boxed{R_j(|r\rangle|\alpha\rangle)
=|r+a_j\bmod5\rangle|\alpha\rangle.}
\]

The kernel is the finite cyclotomic sum

\[
\frac15\sum_{t=0}^4\zeta^{t(r+a_j-k)},
\]

which is 1 for `k=r+a_j mod 5` and 0 otherwise. Four readers therefore coherently write `alpha mod 5` into four five-level pointer registers while preserving the full carrier basis state.

For a superposition this produces entanglement,

\[
\sum_\alpha c_\alpha|\alpha\rangle|0\rangle_P
\mapsto
\sum_\alpha c_\alpha|\alpha\rangle|\bar\alpha\rangle_P,
\]

not a clone of the unknown state.

## 5. Reversible record cycle and ready-state reset

At the start of a two-step block, let

- `alpha` be the carrier;
- `m = alpha mod 5` be a synchronized reference register;
- `p=0` be the fresh pointer;
- `e=0` be a fresh archive cell.

After two source steps the carrier is `beta`. The finite registers then undergo six invertible operations:

1. `p <- p + beta mod 5`;
2. `p <- p - M_J^2 m`;
3. `p <- L^{-1} p`;
4. `e <- e + p`;
5. `p <- p - e`;
6. `m <- M_J^2 m + L e`.

On the ready subspace,

\[
\boxed{
|\alpha\rangle|m\rangle_R|0\rangle_P|0\rangle_E
\mapsto
|\beta\rangle|\bar\beta\rangle_R|0\rangle_P|s\rangle_E.}
\]

The pointer is ready again, the reference is synchronized to the new carrier residue, and the source block remains in the archive. Every gate has an explicit inverse, and the verifier checks the whole cycle beyond the ready subspace as well.

The archive therefore grows. Pointer reset is not the same operation as erasing the recorded history.

## 6. Corrected superposition statement: pointer/reference readout and archive record different variables

The first draft conflated two different partial traces. The correction is structural.

Let `P_m` be the orthogonal projector onto carrier modes with residue `alpha mod 5 = m`.

### 6.1 Tracing a freshly populated residue pointer

Immediately after the coherent residue readout of section 4,

\[
\sum_\alpha c_\alpha|\alpha\rangle|0\rangle_P
\mapsto
\sum_\alpha c_\alpha|\alpha\rangle|\bar\alpha\rangle_P.
\]

If the **pointer** is then traced out before it is uncomputed, the carrier density matrix becomes

\[
\boxed{\rho\mapsto\sum_{m\in A_5}P_m\rho P_m.}
\]

Coherences between different residue classes disappear; coherences within the same class, for example between `alpha` and `alpha+5 gamma`, remain.

A synchronized reference register already contains this residue label at the start of a ready cycle. If it is treated quantum mechanically and then omitted from the state description, the same residue-sector distinction is already present there. One must therefore specify which registers are included in the state before interpreting a reduced density matrix.

### 6.2 Tracing the archive

The archive cell after the complete cycle stores the decoded **source block** `s`, not the carrier residue `m`. For a coherent source superposition, tracing the fresh archive dephases between distinct recorded source-block labels. For a classical source label it introduces no additional carrier dephasing by itself.

Thus the archive measures/records the chosen source block, whereas the temporary residue pointer reads the carrier residue. These are different observables and must not be conflated.

No statement here derives an occurrence law for a single event. A quadratic rule may be adopted for the explicit apparatus, but it is an additional rule rather than a consequence of the reversible gates alone.

## 7. Exact three-step cancellation: useful example, not a deep theorem

The identity

\[
J+J^{-1}=1-\zeta
\]

is equivalent to

\[
\boxed{J^2+J(\zeta-1)+1=0.}
\]

Hence the source word

\[
(b_0,b_1,b_2)=(1,\zeta-1,1)
\]

lies in the chosen alphabet and has the same three-step carrier effect as the zero word, for every initial carrier.

This cancellation is algebraically elementary: after division by `J` it is the displayed identity. Its content for the apparatus is that the chosen alphabet already contains a nonzero history whose net carrier contribution vanishes. The middle symbol is

\[
\zeta-1=-(J+J^{-1}),
\]

and `1-zeta` is the prime above five with norm 5.

A complete length-three census from the zero carrier contains 13 zero-return words out of 15,625, including the zero word. Thus history loss in the final carrier begins at length three and is not a numerical-rounding phenomenon.

For two two-step record blocks, the nonzero example and the silent word can have the same exact final carrier while their archives differ. The archive therefore preserves information that the final carrier alone does not contain.

This is cancellation in the affine arithmetic update. It is not by itself interference of probability amplitudes.

## 8. Theorem C: endpoint growth is at most `C exp(n h)`

Let `alpha_0=0` and let `A_n` be the set of distinct exact integer carrier addresses reachable after exactly `n` source steps from the chosen 25-symbol alphabet. Then

\[
\boxed{|A_n|\le C\varphi^{2n}=C e^{nh},}
\]

where

\[
C=32\left(4\varphi^2+\frac12\right)^2
       \left(4\varphi+\frac12\right)^2
 =93890+41760\sqrt5.
\]

Consequently

\[
\boxed{\limsup_{n\to\infty}\frac{\log|A_n|}{n}\le h=2\log\varphi.}
\]

### Proof

For every source symbol, because `|u|,|v|<=2` and both embeddings of `zeta` have modulus one,

\[
|\sigma_i b|\le4.
\]

The contracting embedding satisfies

\[
|\sigma_1\alpha_n|
\le4\sum_{k=0}^{n-1}\varphi^{-k}
\le4\varphi^2=:A,
\]

while the expanding embedding satisfies

\[
|\sigma_2\alpha_n|
\le4\sum_{k=0}^{n-1}\varphi^k
=4\varphi(\varphi^n-1)=:B_n.
\]

For two distinct algebraic integers, their nonzero difference `gamma` has positive integral norm, hence

\[
|\sigma_1\gamma|^2|\sigma_2\gamma|^2=N(\gamma)\ge1.
\]

Therefore

\[
|\sigma_1\gamma|^2+|\sigma_2\gamma|^2\ge2,
\]

so distinct embedded lattice points in `C^2 ~= R^4` are at Euclidean distance at least `sqrt(2)`. Radius-1/2 four-balls around them are disjoint and lie in the product of complex discs of radii `A+1/2` and `B_n+1/2`.

The four-ball volume is `pi^2/32`; the product-disc volume is

\[
\pi^2(A+1/2)^2(B_n+1/2)^2.
\]

Thus

\[
|A_n|\le32(A+1/2)^2(B_n+1/2)^2.
\]

Since

\[
B_n+\frac12\le\left(4\varphi+\frac12\right)\varphi^n,
\]

the stated bound follows. For any other fixed initial carrier, the reachable set is a translate by `J^n alpha_0` and has the same cardinality. `□`

This proof is independent of Haar measure or random source assumptions. It nevertheless uses the same geometric expansion `|sigma_2 J|^2=phi^2` that produces the public toral exponent `h`; the number is not an unrelated second appearance.

### 8.1 Exact endpoint census

The local verifier included here checks the exact census through length 4:

| n | source words | distinct exact endpoints |
|---:|---:|---:|
| 1 | 25 | 25 |
| 2 | 625 | 625 |
| 3 | 15,625 | 5,449 |
| 4 | 390,625 | 27,233 |

The supplied independent one-architecture review extended the same exact census:

| n | distinct exact endpoints | ratio to previous | ratio / `phi^2` |
|---:|---:|---:|---:|
| 5 | 111,289 | 4.087 | 1.561 |
| 6 | 390,609 | 3.510 | 1.341 |
| 7 | 1,241,777 | 3.179 | 1.214 |
| 8 | 3,723,281 | 2.998 | 1.145 |
| 9 | 10,693,249 | 2.872 | 1.097 |
| 10 | 29,816,617 | 2.788 | 1.065 |

These finite values are consistent with, but do not prove, an asymptotic exponent equal to `h`.

### O-J-ENDPOINT-GROWTH-LOWER-BOUND

**[O]** Prove or refute a matching lower bound, for example

\[
\exists c>0,\ n_0\quad\forall n\ge n_0:\qquad
|A_n|\ge c\varphi^{2n}.
\]

Such a theorem would imply

\[
\lim_{n\to\infty}\frac{\log|A_n|}{n}=2\log\varphi=h.
\]

A natural route is a lattice-filling theorem for the reachable set in a strip whose `sigma_1` width stays bounded while its `sigma_2` radius grows like `phi^n`. The census is evidence only; it is not a substitute for this lower bound.

## 9. Information interpretation under an additional random-source model

Only if one **additionally** assumes independent uniform sampling of the 25 source symbols does the source word have Shannon entropy `n log 25`. Then

\[
H(\alpha_n)\le\log|A_n|\le nh+\log C,
\]

and since the final carrier is a deterministic function of the source word,

\[
\boxed{H(S^n\mid\alpha_n)
\ge n(\log25-h)-\log C.}
\]

This does not assign that source law to native `U`. It says only that, under the stated external random-source model, the final carrier cannot retain the full source history asymptotically. A growing archive can.

## 10. Error statements retained at candidate level

For a phase-reader error model in which the `j`-th eigenphase has additive error `delta_j`, with all other operations ideal, the exact success probability of one coordinate is

\[
P_j=\left|
\frac15\sum_{k=0}^4e^{ik\delta_j}
\right|^2
=\left[
\frac{\sin(5\delta_j/2)}{5\sin(\delta_j/2)}
\right]^2.
\]

Using

\[
\sum_{k,l=0}^4(k-l)^2=100
\]

gives

\[
1-P_j\le2\delta_j^2,
\qquad
P_{\rm error}\le\min\left\{1,2\sum_{j=0}^3\delta_j^2\right\}
\]

for the four-coordinate pure-mode readout under that model.

For digital residue-read errors `e_k` at block boundaries, if

\[
\hat s_k=L^{-1}(\hat m_{k+1}-M_J^2\hat m_k),
\]

then exactly

\[
\boxed{\hat s_k-s_k=L^{-1}(e_{k+1}-M_J^2e_k).}
\]

An isolated read error therefore affects at most the current and adjacent decoded source blocks; a later correct read resynchronizes the reference. This does not repair already stored wrong records and is not a general analog-noise theorem.

## 11. Verification and review status

The included `verify.py` is self-contained with respect to the claims of this note and uses `model.py`; it does not import the earlier relational verifier. It checks:

- the exact integer carrier matrix and inverse;
- the ramified ring relation and exact order 20 of `J mod 5`;
- all 15,625 fixed-source/carrier transitions used in the finite ring check;
- the exact five-point cyclotomic phase-reader kernel;
- determinant-one two-step decoding;
- all 390,625 initial-residue / two-step-source blocks;
- arbitrary-register inverses of the record gates;
- the 13 exact length-three zero-return words;
- the endpoint census through length four;
- an archive witness with equal final carriers and different histories;
- modulo-five aliasing as a negative control;
- the finite phase-error coefficient and a digital-error locality witness;
- a mock native adapter only.

This is a local exact certificate, not a preregistered public probe. It contains no native `U` kernel and makes no claim of physical realization.

The supplied independent review reported:

```text
platform: Linux x86_64, Python 3, one architecture
checks:   49 passed, 0 failed, 1 skipped
scope:    self-contained arithmetic of the reviewed apparatus note
script sha256: 68b5a7fce187f7bf2adc5e30e7a40510ef499b3175b46e3c1686c023b7bd4b30
stdout sha256: 712cf53d4db7ea10fa569a12c0462cce665166590a50a11d9377f98d5cdb4211
```

The reviewer did not possess the earlier source notes or `verify_twist_relational.py`, so inherited `q` transport and toral-entropy inputs were explicitly outside that replay. This note therefore does not use the inherited `q` transport as one of its own verified claims.

## 12. Native-interface boundary

Given a separately validated native step

\[
U(n,\psi)=(n+1,V_n\psi),\qquad \psi\in\mathbb F_5^6,
\]

one may **choose** a port, for example the first two checkpoint coordinates, and define an extension

\[
\widehat U(n,\psi,\alpha)
=(n+1,V_n\psi,J\alpha+b(\ell(\psi))).
\]

Projection back to `(n,psi)` then reproduces the supplied native step by construction. This proves noninterference of the added carrier with that projection; it does **not** prove that the carrier, chosen port, phase reader, timing, archive, Born rule, or event law already exist in native `U`.

The included adapter is tested only against a deliberately named mock kernel.

## 13. Canon-promotion gate

The mathematical core has Canon potential, but promotion should not precede the missing separations of status. A minimal promotion path is:

1. retain Theorem A as a self-contained integral decoding theorem;
2. retain the coherent phase-reader construction and corrected register semantics;
3. retain Theorem C only as the proved upper bound;
4. keep `O-J-ENDPOINT-GROWTH-LOWER-BOUND` open until a matching lower bound is proved;
5. obtain an actual public pin and a second-architecture replay;
6. only then decide whether the result belongs as a Canon mathematical theorem or remains an apparatus construction under `notes/`.

No physical claim should be promoted merely because the exact finite apparatus is reversible.
