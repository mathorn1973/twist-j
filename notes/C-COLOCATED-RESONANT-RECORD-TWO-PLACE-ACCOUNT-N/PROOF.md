<!-- SPDX-License-Identifier: Apache-2.0 -->

# Co-located resonant fixed-quantum record and two-place Hermitian account bridge

**NON-CANONICAL / L1. Proof-first conditional candidate-T. Independent acceptance pending.**

Candidate: `C-COLOCATED-RESONANT-RECORD-TWO-PLACE-ACCOUNT-N`
Date: `2026-11-08`
Public authority: `Public Canon v109`, `main` `d4d363722f052141a4ce65e9da39f11a74b43b95`.

This note is an additive `notes/` package. It is not a formal public `P-` probe, a Canon change, a physical identification, or a derivation of `alpha`. At the prospective source pin, `verify.py` and `break.py` are unexecuted; execution outputs and hashes are recorded in a separate subsequent commit without altering the frozen proof or preregistration.

---

## 1. Exact cyclotomic domain and co-located Gauss carrier

Let $O = \mathbb{Z}[j]$ be the ring of integers of $K = \mathbb{Q}(j)$, where $j^5 = 1$ and $1 + j + j^2 + j^3 + j^4 = 0$. Every element $v \in O$ has a unique integer representation in the power basis $(1, j, j^2, j^3)$:
$$v = v_0 + v_1 j + v_2 j^2 + v_3 j^3, \qquad (v_0, v_1, v_2, v_3) \in \mathbb{Z}^4,$$
and a standard five-coefficient cyclic representation $(c_0, c_1, c_2, c_3, c_4) \in \mathbb{Z}^5$ modulo $(1,1,1,1,1)$ via $v_k = c_k - c_4$ ($k=0,1,2,3$). Complex conjugation $\bar{v}$ sends $j \mapsto j^4 = -1 - j - j^2 - j^3$.

Fix the inherited contact parameters:
$$\rho = j^2, \qquad \phi = -j^2 - j^3, \qquad J = 1 + \rho = 1 + j^2.$$
Because $1 + j + j^2 + j^3 + j^4 = 0$, we have:
$$j^2 + j^3 = -\phi, \qquad j + j^4 = -1 - (j^2 + j^3) = \phi - 1, \qquad \phi^2 = j^4 + 2 + j = (\phi - 1) + 2 = \phi + 1.$$
Thus $O^+ = \mathbb{Z}[\phi]$ is the ring of integers of the real quadratic subfield $K^+ = \mathbb{Q}(\phi) = \mathbb{Q}(\sqrt{5})$.

The mod-$5$ augmentation homomorphism $\epsilon: O \to \mathbb{F}_5$ sends $j \mapsto 1$, so for $v = (v_0, v_1, v_2, v_3)$:
$$\epsilon(v) \equiv v_0 + v_1 + v_2 + v_3 \pmod 5, \qquad \ker\epsilon = (1 - j)O.$$

### 1.1 Co-located loaded carrier (`#1954` / `#1956`)

Consider a two-vertex, single-oriented-edge carrier with one charged slot $x \in O$ at vertex $A$, active charged slots $v_1, \dots, v_M \in O$ at vertex $B$ with zero fixed uncharged references ($e_r = 0$), and marked edge field $F \in O$. The two primitive-cut Gauss invariants are:
$$G_A(x, F) := F + x = 0, \qquad G_B(v_1, \dots, v_M, F) := F - \sum_{r=1}^M v_r = 0. \tag{1.1}$$
Together, `(1.1)` is equivalent to $F = -x$ and total charge neutrality $x + \sum_{r=1}^M v_r = 0$.

On this carrier, the matched-edge ($a = z/(2c) = 1$) loaded contact $C(x, v_r)$ between the vertex-$A$ slot $x$ and a vertex-$B$ slot $v = v_r$ has trial displacement:
$$d = \frac{2v - x - e_r + F}{4} = \frac{2v - x + (-x)}{4} = \frac{v - x}{2}. \tag{1.2}$$
- **Refused branch:** If $v - x \notin 2O$ ($d \notin O$), the contact acts as the identity on all slots and on $F$, with current $i = 0$ and step area $h(0) = 0$.
- **Admitted branch:** If $v - x \in 2O$ ($d \in O$), the contact current is $i = (\rho - 1)d$ and the state updates by:
  $$x' = x - i = x + (1 - \rho)d, \qquad v' = v + i = v - (1 - \rho)d, \qquad F' = F + i = -x', \tag{1.3}$$
  while all other vertex-$B$ slots $v_s$ ($s \neq r$) are unchanged, and the primitive step area is $h(d) \in \mathbb{Z}[\phi]$.

Since $x' + v' = x + v$ and $F' + x' = (F + x) + (i - i) = 0$, both Gauss equations `(1.1)` are preserved at every primitive cut. Since $\epsilon(\rho - 1) = \epsilon(j^2 - 1) \equiv 0 \pmod 5$, $\epsilon(i) \equiv 0 \pmod 5$, so every slot residue $\epsilon(x), \epsilon(v_r)$ is individually invariant at every cut. The inverse of a single contact $C(x, v_r)$ is $C(x, v_r)^4$, and the inverse of any chronological contact word reverses the word and replaces each contact by its fourth power.

---

## 2. Theorem 1 (`A1`): Two-place Galois/Hermitian account and conjugate trace decomposition

For $v = v_0 + v_1 j + v_2 j^2 + v_3 j^3 \in O$, write the Hermitian square $h(v) := v\bar{v} \in \mathbb{Z}[\phi]$ as:
$$h(v) = A(v) + B(v)\phi, \qquad A(v), B(v) \in \mathbb{Z}. \tag{2.1}$$
Expanding $(v_0 + v_1 j + v_2 j^2 + v_3 j^3)(v_0 + v_1 j^4 + v_2 j^3 + v_3 j^2)$ using $j + j^4 = \phi - 1$ and $j^2 + j^3 = -\phi$ yields the explicit integer quadratic forms:
$$\begin{aligned}
S_0(v) &= v_0^2 + v_1^2 + v_2^2 + v_3^2, \\
S_1(v) &= v_0 v_1 + v_1 v_2 + v_2 v_3, \\
S_2(v) &= v_0 v_2 + v_1 v_3 + v_0 v_3, \\
A(v) &= S_0(v) - S_1(v), \\
B(v) &= S_1(v) - S_2(v).
\end{aligned} \tag{2.2}$$

The real quadratic ring $\mathbb{Z}[\phi]$ has two real Galois embeddings $\sigma_1, \sigma_2: \mathbb{Q}(\phi) \hookrightarrow \mathbb{R}$ defined by $\sigma_1(\phi) = \phi = \frac{1+\sqrt{5}}{2}$ and $\sigma_2(\phi) = 1 - \phi = \frac{1-\sqrt{5}}{2}$:
$$\sigma_1(A + B\phi) = A + B\phi, \qquad \sigma_2(A + B\phi) = A + B(1 - \phi) = (A + B) - B\phi. \tag{2.3}$$
Its field trace and field norm over $\mathbb{Q}$ are:
$$Q(v) := \operatorname{Tr}_{\mathbb{Q}(\phi)/\mathbb{Q}}(h(v)) = \sigma_1(h(v)) + \sigma_2(h(v)) = 2A(v) + B(v) = \frac{1}{2}\operatorname{Tr}_{\mathbb{Q}(j)/\mathbb{Q}}(v\bar{v}), \tag{2.4}$$
$$N_{\mathbb{Q}(\phi)/\mathbb{Q}}(h(v)) = \sigma_1(h(v))\,\sigma_2(h(v)) = A(v)^2 + A(v)B(v) - B(v)^2 = N_{\mathbb{Q}(j)/\mathbb{Q}}(v). \tag{2.5}$$

On the co-located Gauss carrier `(1.1)` with zero uncharged references ($e_r = 0$), the complete loaded energy account of `C-LOADED-CURRENT-WORK-PHASE-COMPATIBILITY-N` (`K + V + H`) is:
$$E_{\mathrm{full}} = Q(x) + \sum_{r=1}^M \big(Q(v_r) + Q(v_r - 0)\big) + Q(F) = 2\left(Q(x) + \sum_{r=1}^M Q(v_r)\right) = \operatorname{Tr}_{\mathbb{Q}(\phi)/\mathbb{Q}}(H_{\mathrm{full}}), \tag{2.6}$$
where the complete two-place Hermitian account
$$H_{\mathrm{full}} := 2\left(h(x) + \sum_{r=1}^M h(v_r)\right) \in \mathbb{Z}[\phi] \tag{2.7}$$
is conserved at every primitive cut because $h(x') + h(v') = h(s - \rho d) + h(s + \rho d) = 2h(s) + 2h(d) = h(x) + h(v)$.

**Theorem 1 (Galois-conjugate contact factors and trace decomposition).**
1. The fundamental cyclotomic factors satisfy:
   $$\begin{aligned}
   h(1 - \rho) = h(1 - j^2) &= 2 - (j^2 + j^3) = 2 + \phi, & Q(1 - j^2) &= 5, & N(2 + \phi) &= 5, \\
   h(1 - j^4) &= 2 - (j + j^4) = 3 - \phi = \sigma_2(2 + \phi), & Q(1 - j^4) &= 5, & N(3 - \phi) &= 5, \\
   h(J) = h(1 + j^2) &= 2 + (j^2 + j^3) = 2 - \phi, & Q(J) &= 3, & N(2 - \phi) &= 1, \\
   h(3 + \rho) = h(3 + j^2) &= 10 + 3(j^2 + j^3) = 10 - 3\phi, & Q(3 + j^2) &= 17, & N(10 - 3\phi) &= 61.
   \end{aligned} \tag{2.8}$$
2. Because $(2 + \phi)(3 - \phi) = 6 - \phi - \phi^2 + 2\phi = 5$, every contact current $i = (\rho - 1)d$ ($\rho = j^2$) relates to its displacement $d$ in $\mathbb{Q}(\phi)$ by:
   $$h(i) = (2 + \phi)\,h(d), \qquad h(d) = \frac{3 - \phi}{5}\,h(i), \qquad \sigma_2(h(i)) = (3 - \phi)\,\sigma_2(h(d)). \tag{2.9}$$
   (When the opposite convention $\tilde{\rho} = j^4$ is used, $\tilde{\imath} = (j^4 - 1)d$ has $h(\tilde{\imath}) = (3 - \phi)h(d)$ and $h(d) = \frac{2+\phi}{5}h(\tilde{\imath})$.)
3. For every $c \in O$ with $h(c) = A_c + B_c\phi$:
   $$\begin{aligned}
   h\big((1 - j^2)c\big) &= (2 + \phi)(A_c + B_c\phi) = (2A_c + B_c) + (A_c + 3B_c)\phi, \\
   h\big((1 - j^4)c\big) &= (3 - \phi)(A_c + B_c\phi) = (3A_c - B_c) + (2B_c - A_c)\phi.
   \end{aligned} \tag{2.10}$$
   Taking the real-subfield trace $Q(A + B\phi) = 2A + B$ gives:
   $$\boxed{Q\big((1 - j^2)c\big) = 5(A_c + B_c), \qquad Q\big((1 - j^4)c\big) = 5A_c, \qquad Q\big((1 - j^2)c\big) + Q\big((1 - j^4)c\big) = 5(2A_c + B_c) = 5\,Q(c).} \tag{2.11}$$
   In particular, $Q((1 - j^2)c)$ and $Q((1 - j^4)c)$ are not individually equal to $5Q(c)$: they coincide ($5(A_c + B_c) = 5A_c$) if and only if $B_c = 0$, in which case both equal $5A_c = \frac{5}{2}Q(c)$. For $c_1 = 1 - j^2$ ($h(c_1) = 2 + \phi$, $Q(c_1) = 5$) and $c_2 = 1 - j^4$ ($h(c_2) = 3 - \phi$, $Q(c_2) = 5$), $Q((1 - j^2)c_1) = 15 \neq 10 = Q((1 - j^2)c_2)$.

*Proof.* Equations `(2.8)`–`(2.10)` follow by direct expansion using $\phi^2 = \phi + 1$. In `(2.10)`,
$$Q\big((1 - j^2)c\big) = 2(2A_c + B_c) + (A_c + 3B_c) = 5A_c + 5B_c = 5(A_c + B_c),$$
$$Q\big((1 - j^4)c\big) = 2(3A_c - B_c) + (2B_c - A_c) = 5A_c,$$
and their sum is $5(2A_c + B_c) = 5Q(c)$. $\square$

---

## 3. Theorem 2 (`A2`): Iff resonance theorem for the 2-contact returning selector

Consider a pre-charged selector port at vertex $B$ consisting of a helper slot $h_0 = a + 2c$, a blank record slot $z_0 = 0$, and an untouched neutralizing spectator $u = -(a + h_0)$ (so $h_0 + z_0 + u = -a$), paired with signal $x_0 = a \in O$ at vertex $A$ and field $F_0 = -a$. Apply the chronological two-contact word:
$$W_{\mathrm{sel}} := C(x, z) \circ C(x, h). \tag{3.1}$$

**Proposition 1 (Three-slot sum obstruction to arbitrary $(a, c)$ return).**
Every contact preserves the sum of its two active slots, so any contact word on $(x, h, z)$ preserves $x + h + z$. For initial state $(a, a + 2c, 0)$ and proposed target state $(a, 2a, (1 - \rho)c)$, equality of slot sums requires:
$$a + (a + 2c) + 0 = a + 2a + (1 - \rho)c \iff 2a + 2c = 3a + (1 - \rho)c \iff a = (1 + \rho)c = Jc. \tag{3.2}$$
In particular, for $(a, c) = (1, 1)$, $2a + 2c = 4 \neq 4 - j^2 = 3a + (1 - \rho)c$, so no contact word on $(x, h, z)$ can map $(a, a+2c, 0) \mapsto (a, 2a, (1-\rho)c)$ away from the resonance locus $a = Jc$.

**Theorem 2 (Exact two-contact return and record iff $a = Jc$).**
Let $a \in O$ and $c \in O \setminus \{0\}$, and apply $W_{\mathrm{sel}} = C(x, z) \circ C(x, h)$ to $(x_0, h_0, z_0) = (a, a + 2c, 0)$ with $F_0 = -a$.
1. The first contact $C(x, h)$ has displacement $d_1 = (h_0 - x_0)/2 = c \in O$, so it is always admitted with current $i_1 = (\rho - 1)c$ and post-step state:
   $$x_1 = a + (1 - \rho)c, \qquad h_1 = a + (1 + \rho)c = a + Jc, \qquad z_1 = 0, \qquad F_1 = -x_1. \tag{3.3}$$
2. The second contact $C(x, z)$ has trial displacement $d_2 = (0 - x_1)/2 = -x_1/2$. The second contact is admitted ($d_2 \in O$) **and** restores the signal $x_2 = a$ (equivalently $F_2 = -a$, or equivalently leaves a non-zero record $z_2 \neq 0$ while returning $x_2 = a$) **if and only if**:
   $$\boxed{a = (1 + \rho)c = Jc.} \tag{3.4}$$
3. At the resonant locus $a = Jc$, we have $h_0 = (J + 2)c = (3 + \rho)c$, $d_1 = c$, $x_1 = 2c \in 2O$, $h_1 = 2Jc = 2a$, $d_2 = -c \in O$, $i_2 = (1 - \rho)c$, and the two-step trajectory is:
   $$\big(Jc,\; (3 + \rho)c,\; 0\big) \xrightarrow{C(x,h)} \big(2c,\; 2Jc,\; 0\big) \xrightarrow{C(x,z)} \big(Jc,\; 2Jc,\; (1 - \rho)c\big), \tag{3.5}$$
   with restored field $F_2 = -Jc = F_0$ and total two-step contact area $h(d_1) + h(d_2) = 2h(c)$.
4. Pointwise in $\mathbb{Z}[\phi]$, the universal polynomial identity
   $$h(3 + \rho) = 10 - 3\phi = 4(2 - \phi) + (2 + \phi) = 4\,h(J) + h(1 - \rho) \tag{3.6}$$
   multiplied by $h(c)$ gives exact helper-to-record Hermitian conservation:
   $$h(h_0) = h(h_1) + h(z_2), \tag{3.7}$$
   and in rational traces ($h(c) = A_c + B_c\phi$):
   $$Q(h_0) = 17A_c + B_c, \qquad Q(h_1) = 12A_c - 4B_c, \qquad Q(z_2) = Q(h_0) - Q(h_1) = 5(A_c + B_c). \tag{3.8}$$

*Proof.*
Step 1 is immediate from `(1.2)`–`(1.3)`. For Step 2, if $C(x, z)$ is admitted with $d_2 = -x_1/2 \in O$, then $x_1 = -2d_2$ and $x_2 = x_1 - (\rho - 1)d_2 = -2d_2 + (\rho - 1)d_2 = -(1 + \rho)d_2 = -Jd_2$. Thus $x_2 = a$ holds if and only if $a = -Jd_2$ and $x_1 = -2d_2$. Substituting $a = -Jd_2$ and $x_1 = -2d_2$ into `(3.3)` gives:
$$-2d_2 = -Jd_2 + (1 - \rho)c \iff (J - 2)d_2 = (1 - \rho)c \iff (\rho - 1)d_2 = (1 - \rho)c \iff (\rho - 1)(d_2 + c) = 0.$$
Since $O$ is an integral domain and $\rho - 1 = j^2 - 1 \neq 0$, this holds if and only if $d_2 = -c \in O$ and $a = -Jd_2 = Jc$. Conversely, if $a = Jc$, then $x_1 = (1 + \rho)c + (1 - \rho)c = 2c \in 2O$, so $d_2 = -c \in O$ is admitted and produces `(3.5)`. Finally, for $h(c) = A_c + B_c\phi$:
$$h(h_0) = (10 - 3\phi)(A_c + B_c\phi) = (10A_c - 3B_c) + (7B_c - 3A_c)\phi \implies Q(h_0) = 2(10A_c - 3B_c) + (7B_c - 3A_c) = 17A_c + B_c,$$
$$h(h_1) = (8 - 4\phi)(A_c + B_c\phi) = (8A_c - 4B_c) + (4B_c - 4A_c)\phi \implies Q(h_1) = 2(8A_c - 4B_c) + (4B_c - 4A_c) = 12A_c - 4B_c,$$
 whose difference is $5A_c + 5B_c = 5(A_c + B_c) = Q(z_2)$. $\square$

---

## 4. Theorem 3 (`A3`): $\mathbb{F}_{16}$ inertness and 5-phase one-hot selectivity iff $c \notin 2O$

For any non-zero seed $c \in O \setminus \{0\}$, define the 5-channel resonant target family:
$$a_k := Jc\rho^k, \qquad h_k := a_k + 2c\rho^k = (3 + \rho)c\rho^k, \qquad z_k := 0, \qquad u_k := -h_k \qquad (k \in \{0, 1, 2, 3, 4\}). \tag{4.1}$$
Place the incoming signal $x = a_m = Jc\rho^m$ ($m \in \{0, 1, 2, 3, 4\}$) at vertex $A$, place the five selector channels $(h_k, z_k, u_k)_{k=0}^4$ together with the signal companion $u_x = -a_m$ at vertex $B$, and set $F = -x = -a_m$. Then both Gauss laws `(1.1)` hold initially ($F + x = 0$ and $\sum_{v \in B} v = -a_m + \sum_{k=0}^4 (h_k + 0 - h_k) = -a_m = F$).

Apply the fixed 10-contact chronological bank word independent of $m$:
$$W_{\mathrm{bank}} := W_{\mathrm{sel}, 4} \circ W_{\mathrm{sel}, 3} \circ W_{\mathrm{sel}, 2} \circ W_{\mathrm{sel}, 1} \circ W_{\mathrm{sel}, 0}, \qquad W_{\mathrm{sel}, k} := C(x, z_k) \circ C(x, h_k). \tag{4.2}$$

**Lemma 1 (Inertness of $2$ in $O = \mathbb{Z}[j]$).**
Since $2$ is a primitive root modulo $5$ ($2^1 \equiv 2, 2^2 \equiv 4, 2^3 \equiv 3, 2^4 \equiv 1 \pmod 5$), the fifth cyclotomic polynomial $\Phi_5(t) = 1 + t + t^2 + t^3 + t^4$ is irreducible over $\mathbb{F}_2$. Consequently, $2O$ is a maximal ideal in $O$, and the quotient ring $O / 2O \cong \mathbb{F}_2[t]/(\Phi_5(t)) \cong \mathbb{F}_{16}$ is the finite field of $16$ elements. In particular, $O / 2O$ has **no zero divisors**: a product of elements of $O$ lies in $2O$ if and only if at least one factor lies in $2O$.

**Theorem 3 (One-hot 5-phase selectivity iff $c \notin 2O$).**
Let $c \in O \setminus \{0\}$. Across the five resonant phase inputs $x = a_m = Jc\rho^m$ ($m \in \{0, 1, 2, 3, 4\}$), the 10-contact bank $W_{\mathrm{bank}}$ leaves all four off-target channels untouched ($(h_k', z_k') = (h_k, 0)$ for all $k \neq m$), writes the target channel $z_m' = (1 - \rho)c\rho^m$ with $h_m' = 2Jc\rho^m$, and restores $(x', F') = (a_m, -a_m)$ **if and only if** $c \notin 2O$.
When $c \notin 2O$:
1. Every primitive cut $1, \dots, 10$ preserves both Gauss equations `(1.1)`, all slot residues mod $5$, the complete scalar account $E_{\mathrm{full}} = 2\big(2Q(Jc) + 10\,Q((3+\rho)c)\big) = 4Q(Jc) + 20\,Q((3+\rho)c)$, and the complete Hermitian account $H_{\mathrm{full}} = 4h(Jc) + 20\,h((3+\rho)c)$.
2. Exactly $2$ of the $10$ contacts are admitted (the two contacts of channel $k = m$), while all $8$ off-target contacts ($k \neq m$) are refused.
3. The recorded vector $(z_0', \dots, z_4')$ is one-hot at index $m$ with phase-independent Hermitian record norm and rational record quantum:
   $$h(z_m') = (2 + \phi)\,h(c), \qquad w_0 := Q(z_m') = 5(A_c + B_c), \tag{4.3}$$
   and total 10-contact path area $H_{\mathrm{path}} = 2\,h(c)$.

*Proof.*
- **($\Leftarrow$) Suppose $c \notin 2O$.** Fix $m \in \{0, 1, 2, 3, 4\}$. Suppose inductively that entering channel $k$, the vertex-$A$ signal is $x = a_m = (1 + \rho)c\rho^m$.
  - If $k \neq m$: at Contact 1 ($C(x, h_k)$), the numerator of $d_{1,k} = (h_k - x)/2$ is:
    $$h_k - x = (3 + \rho)c\rho^k - (1 + \rho)c\rho^m = 2c\rho^k + (1 + \rho)(\rho^k - \rho^m)c \equiv (1 + \rho)(\rho^k - \rho^m)c \pmod{2O}. \tag{4.4}$$
    In $O / 2O \cong \mathbb{F}_{16}$, $1 + \rho = 1 + j^2 \neq 0$, $\rho^k - \rho^m = j^{2k} - j^{2m} \neq 0$ (since $k \not\equiv m \pmod 5$ and $j^2$ has order $5$), and $c \not\equiv 0 \pmod{2O}$. Since $\mathbb{F}_{16}$ is a field (Lemma 1), $(1 + \rho)(\rho^k - \rho^m)c \notin 2O$, so $d_{1,k} \notin O$ and Contact 1 is refused ($x$ remains $a_m$ and $h_k$ remains unchanged). At Contact 2 ($C(x, z_k)$ with $z_k = 0$), the numerator of $d_{2,k} = -x/2$ is $-(1 + \rho)c\rho^m \notin 2O$ for the same reason, so Contact 2 is also refused ($z_k$ remains $0$ and $x$ remains $a_m$).
  - If $k = m$: by Theorem 2, both contacts of $W_{\mathrm{sel}, m}$ are admitted, setting $h_m' = 2Jc\rho^m$, $z_m' = (1 - \rho)c\rho^m$, and restoring $x = a_m$ and $F = -a_m$ before channel $m + 1$ begins.
  Since $h(\rho^m) = 1$, $h(z_m') = h((1-\rho)c\rho^m) = (2+\phi)h(c)$ and $Q(z_m') = 5(A_c + B_c)$ are independent of $m$.
- **($\Rightarrow$) Conversely, suppose $c \in 2O \setminus \{0\}$.** Write $c = 2u$ with $u \in O \setminus \{0\}$. Consider input $m = 1$ ($x = a_1 = 2J u \rho$) at the very first channel $k = 0$ ($h_0 = 2(3 + \rho)u$). At Contact 1 ($C(x, h_0)$),
  $$d_{1,0} = \frac{h_0 - x}{2} = \big((3 + \rho) - (1 + \rho)\rho\big)u \in O. \tag{4.5}$$
  Hence Contact 1 on channel $k = 0 \neq m$ is admitted! Moreover, $h(3 + \rho) = 10 - 3\phi \neq 2 - \phi = h((1 + \rho)\rho)$, so $(3 + \rho) - (1 + \rho)\rho \neq 0$. Since $O$ is an integral domain and $u \neq 0$, $d_{1,0} \neq 0$ and $i_{1,0} = (\rho - 1)d_{1,0} \neq 0$. Thus Contact 1 sets $h_0' = h_0 + i_{1,0} \neq h_0$. Because the remaining contacts $2, \dots, 10$ act only on $z_0$ and $(h_k, z_k)_{k=1}^4$ and never touch $h_0$ again, the off-target helper $h_0$ remains permanently disturbed ($h_0' \neq h_0$) at the end of $W_{\mathrm{bank}}$. $\square$

---

## 5. Proposition 2 (`A4`): Exact instantiation of the PR `#1957` `35`-quantum

In `C-COLOCATED-READOUT-PATH-1` (`#1955` / PR `#1957`), the path-recorder targets are $a_0 = 1 - \rho = 1 - j^2$ and $a_1 = (1 - \rho)\rho^4$.
Since $J = 1 + j^2$ has norm $N_{\mathbb{Q}(j)/\mathbb{Q}}(J) = N_{\mathbb{Q}(\phi)/\mathbb{Q}}(2 - \phi) = 4 - 2 - 1 = 1$, $J$ is a unit in $O$. Using $1 + j + j^2 + j^3 + j^4 = 0$, we have:
$$(1 + j^2)(-j - j^2) = -j - j^2 - j^3 - j^4 = -(j + j^2 + j^3 + j^4) = 1, \tag{5.1}$$
so the exact inverse of $J$ in the power basis $(1, j, j^2, j^3)$ is:
$$\boxed{J^{-1} = -j - j^2 = (0, -1, -1, 0).} \tag{5.2}$$
Therefore, for $a_0 = 1 - j^2$:
$$c_{\#1957} = a_0 J^{-1} = (1 - j^2)(-j - j^2) = -j - j^2 + j^3 + j^4 = -1 - 2j - 2j^2 = (-1, -2, -2, 0) \in O \setminus 2O! \tag{5.3}$$
Computing its Hermitian square via `(2.2)` for $(-1, -2, -2, 0)$:
- $S_0 = 1 + 4 + 4 + 0 = 9$, $S_1 = 2 + 4 + 0 = 6$, $S_2 = 2 + 0 + 0 = 2$,
- $A_c = S_0 - S_1 = 3$, $B_c = S_1 - S_2 = 4$,
$$\boxed{h(c_{\#1957}) = 3 + 4\phi, \qquad Q(c_{\#1957}) = 2(3) + 4 = 10.} \tag{5.4}$$
By Theorems 1–3, for every phase $k \in \{0, 1, 2, 3, 4\}$ of $c_k = c_{\#1957}\rho^k$:
- Target signal $a_k = Jc_k = (1 - \rho)\rho^k$: $h(a_k) = (2 - \phi)(3 + 4\phi) = 2 + \phi$, $Q(a_k) = 5$.
- Initial helper $h_{0,k} = (3 + \rho)c_k$: $h(h_{0,k}) = (10 - 3\phi)(3 + 4\phi) = 18 + 19\phi$, $Q(h_{0,k}) = 17(3) + 4 = 55$.
- Post-click helper $h_{1,k} = 2Jc_k$: $h(h_{1,k}) = 4(2 + \phi) = 8 + 4\phi$, $Q(h_{1,k}) = 12(3) - 4(4) = 20$.
- Recorded click $z_{2,k} = (1 - \rho)c_k$: $h(z_{2,k}) = (2 + \phi)(3 + 4\phi) = 10 + 15\phi$, $w_0 = Q(z_{2,k}) = 5(3 + 4) = 35$.
- Active selector contact area: $h(d_1) + h(d_2) = 2h(c_{\#1957}) = 6 + 8\phi$ (real-subfield trace $20$, full $K/\mathbb{Q}$ trace $40$).

---

## 6. Theorem 4 (`A5`): Conditional closure of the work-to-count identity `(9a)`

In `C-NATIVE-ENERGY-OCCURRENCE-DERIVATION-N`, equation `(9a)` states that for a multi-channel detector with non-negative recorded channel works $W_{\mathrm{rec}, k} = \sum_{e=1}^{N_k} w_{k, e}$ and positive event counts $N_k > 0$ ($\bar{w}_k := W_{\mathrm{rec}, k} / N_k$),
$$\frac{W_{\mathrm{rec}, k}}{\sum_{i} W_{\mathrm{rec}, i}} = \frac{\big(N_k / \sum_l N_l\big)\,\bar{w}_k}{\sum_i \big(N_i / \sum_l N_l\big)\,\bar{w}_i}. \tag{6.1}$$
For a passive blank loaded detector (`#1945`), each absorbed event deposits work proportional to $\cos^2(n\omega)$, so $w_{k, e}$ varies with the arrival tick $n$ and amplitude scale.

**Theorem 4 (Constant-quantum click record on the resonant 5-phase bank).**
Fix any odd seed $c \in O \setminus 2O$ ($h(c) = A_c + B_c\phi$). Consider any sequence of $T \ge 1$ resonant signal arrivals $x^{(t)} = Jc\rho^{m_t}$ ($m_t \in \{0, 1, 2, 3, 4\}$) routed through freshly prepared (or between-event recharged) 5-channel banks $\mathcal{B}(c)$. Then:
1. At every event $t$, exactly one channel $k = m_t$ fires, depositing the phase- and time-independent record quantum
   $$w_{m_t, e} = w_0(c) := 5(A_c + B_c) \in 5\mathbb{Z}_{>0} \tag{6.2}$$
   (and two-place Hermitian quantum $h(z'_{m_t}) = (2 + \phi)h(c) \in \mathbb{Z}[\phi]$) while restoring the signal $(x^{(t)}, F^{(t)})$ without drain.
2. After $T$ events with channel click counts $(N_0, N_1, N_2, N_3, N_4)$ ($\sum_{k=0}^4 N_k = T > 0$), the cumulative recorded account on channel $k$ is $W_{\mathrm{rec}, k} = N_k w_0(c)$, the conditional mean recorded work on every active channel is $\bar{w}_k = w_0(c)$, and both the rational work share and the two-place Hermitian record share equal the event-count share identically:
   $$\boxed{\frac{W_{\mathrm{rec}, k}}{\sum_{i=0}^4 W_{\mathrm{rec}, i}} = \frac{N_k}{\sum_{i=0}^4 N_i}, \qquad \frac{H_{\mathrm{rec}, k}}{\sum_{i=0}^4 H_{\mathrm{rec}, i}} = \frac{N_k}{\sum_{i=0}^4 N_i} \quad \text{in } \mathbb{Q}(\phi).} \tag{6.3}$$

*Proof.* Immediate from Theorem 3: every event $t$ sets $z'_{m_t} = (1 - \rho)c\rho^{m_t}$ and $z'_k = 0$ for $k \neq m_t$, so $Q(z'_{m_t}) = 5(A_c + B_c) = w_0(c)$ and $h(z'_{m_t}) = (2 + \phi)h(c)$ depend only on $c$. Factoring $w_0(c) > 0$ (and $(2+\phi)h(c) \neq 0$) out of the numerator and denominator of `(6.1)` yields `(6.3)`. $\square$

---

## 7. Theorem 5 (`A6`): Exact operational boundaries

To prevent over-interpretation of Theorems 1–4, we prove three sharp boundaries within the same model:

**Theorem 5 (Dead-time lock, unarchived record backreaction, and free-mode denominator obstruction).**
Let $c \in O \setminus 2O$ and $m \in \{0, 1, 2, 3, 4\}$. After one resonant pulse $x = Jc\rho^m$ has passed through channel $m$, the helper is in the discharged state $h_m^{(1)} = 2Jc\rho^m$ and the record slot is in the occupied state $z_m^{(1)} = (1 - \rho)c\rho^m$. Suppose a second identical pulse $x = Jc\rho^m$ arrives at channel $m$ without recharging $h_m^{(1)}$:
1. **Dead-time lock with tape advance ($z_m$ replaced by a fresh blank $0$):** On $(x, h_m^{(1)}, 0) = (Jc\rho^m, 2Jc\rho^m, 0)$, the two trial displacements are:
   $$d_1 = \frac{2Jc\rho^m - Jc\rho^m}{2} = \frac{Jc\rho^m}{2} \notin O, \qquad d_2 = \frac{0 - Jc\rho^m}{2} = -\frac{Jc\rho^m}{2} \notin O, \tag{7.1}$$
   because $J, \rho^m, c$ are all non-zero in the field $O / 2O \cong \mathbb{F}_{16}$. Thus both contacts are refused: the discharged helper is dead-time locked and cannot write a second click until $h_m^{(1)} = 2Jc\rho^m$ is recharged to $(3 + \rho)c\rho^m$ (which requires supplying external account $\Delta Q_h = 5(A_c + B_c) = w_0$).
2. **Unarchived record backreaction ($z_m^{(1)} = (1 - \rho)c\rho^m$ left in the active port):** On $(x, h_m^{(1)}, z_m^{(1)}) = (Jc\rho^m, 2Jc\rho^m, (1 - \rho)c\rho^m)$, Contact 1 on $h_m^{(1)}$ still refuses ($d_1 \notin O$), so $x$ enters Contact 2 unchanged. At Contact 2 ($C(x, z_m^{(1)})$), the trial displacement is:
   $$d_2 = \frac{z_m^{(1)} - x}{2} = \frac{(1 - \rho)c\rho^m - (1 + \rho)c\rho^m}{2} = -\rho^{m+1}c \in O! \tag{7.2}$$
   Because $d_2 \in O$ is non-zero, Contact 2 is **admitted** with current $i_2 = (1 - \rho)\rho^{m+1}c \neq 0$, disturbing both the signal and the stored record to:
   $$x' = (1 + \rho^2)c\rho^m \neq Jc\rho^m, \qquad z_m^{(2)} = (1 - \rho^2)c\rho^m \neq z_m^{(1)}. \tag{7.3}$$
   Hence multi-click operation in Theorem 4 strictly requires advancing the record tape to a fresh blank $z = 0$ (or isolating the written record) after each click.
3. **Free-mode denominator obstruction (`#1945`):** For the two inherited transverse modes $\lambda_1 = 3/4$ ($\cos\omega_1 = 5/8 = a_0/(2b)$ with $(a_0, b) = (5, 4)$) and $\lambda_2 = 5/6$ ($\cos\omega_2 = 7/12$ with $(a_0, b) = (7, 6)$), free evolution scales an initial integral polarization $e_0 = (e_{0,0}, e_{0,1}, e_{0,2}, e_{0,3}) \in O \setminus \{0\}$ by $\cos(n\omega) = P_n / (2b^n)$, where
   $$P_0 = 2, \qquad P_1 = a_0, \qquad P_{n+1} = a_0 P_n - b^2 P_{n-1} \qquad (n \ge 1). \tag{7.4}$$
   For every $n \ge 1$, $P_n$ is odd and $\gcd(P_n, b) = 1$, so $\gcd(P_n, 2b^n) = 1$ and the reduced denominator of $\cos(n\omega)$ is $D_n = 2\cdot 4^n$ (for $\lambda_1 = 3/4$) or $D_n = 2\cdot 6^n$ (for $\lambda_2 = 5/6$). Call $e_0 \in O$ *primitive* if $\gcd(e_{0,0}, e_{0,1}, e_{0,2}, e_{0,3}) = 1$. Co-location reduces the contact admission guard from mod $4$ to mod $2$ inside $O$, but requires the input slot $x$ to lie in $O$; hence for any primitive $e_0 \in O$, unscaled free-mode pulses $F_n = e_0 \cos(n\omega)$ do not lie in $O$ for any $n \ge 1$, and still require a finite-horizon integer multiplier ($2b^N$ for $F_n \in O$, or $M_N = 8b^N$ in the `#1945` loaded apparatus).

*Proof.*
`(7.1)` follows from Lemma 1 since $J = 1 + j^2 \notin 2O$, $\rho^m \notin 2O$, and $c \notin 2O$. In `(7.2)`, $(1 - \rho) - (1 + \rho) = -2\rho \in 2O$, so $d_2 = -\rho c\rho^m = -\rho^{m+1}c \in O$, and `(1.3)` gives $x' = (1 + \rho)c\rho^m - (1 - \rho)\rho c\rho^m = (1 + \rho^2)c\rho^m$ and $z_m^{(2)} = (1 - \rho)c\rho^m + (1 - \rho)\rho c\rho^m = (1 - \rho^2)c\rho^m$. For `(7.4)`, let $p$ be any prime dividing $2b$ (so $p = 2$ for $b = 4$, and $p \in \{2, 3\}$ for $b = 6$). Since $p \mid b$, $b^2 \equiv 0 \pmod p$, so the recurrence `(7.4)` reduces modulo $p$ for all $n \ge 1$ to $P_{n+1} \equiv a_0 P_n \pmod p$. By induction on $n \ge 1$, $P_n \equiv a_0^{n-1} P_1 = a_0^n \pmod p$. Since $\gcd(5, 4) = 1$ and $\gcd(7, 6) = 1$, $a_0 \not\equiv 0 \pmod p$, so $P_n \not\equiv 0 \pmod p$ for all $n \ge 1$. Thus $\gcd(P_n, 2b^n) = 1$. Finally, if $e_0$ has $\gcd(e_{0,0}, e_{0,1}, e_{0,2}, e_{0,3}) = 1$, then $\gcd(e_{0,0} P_n, \dots, e_{0,3} P_n, 2b^n) = 1 < 2b^n$ for all $n \ge 1$, so $e_0 P_n / (2b^n) \notin O$. $\square$
