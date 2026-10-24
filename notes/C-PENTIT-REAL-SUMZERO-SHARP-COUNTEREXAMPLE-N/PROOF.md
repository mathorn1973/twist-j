# A real sum-zero counterexample to the proposed sharp pentit bound

**NON-CANONICAL / candidate-T / L1. Exposed analytical derivation.**
This proves a mathematical statement about the declared pentit reading. It
does not construct a native preparation or a physical occurrence law.

## 1. Fixed convention and question

Work in the orthonormal basis indexed by `j in F_5`, with
`zeta = exp(2*pi*i/5)` and

$$
A_{q,r}|j\rangle=\zeta^{2r(q-j)}|2q-j\rangle,\qquad
W_\psi(q,r)=\frac15\langle\psi|A_{q,r}|\psi\rangle,
\quad \mathcal N(\psi)=\sum_{q,r}\max(0,-W_\psi(q,r)).
$$

These are exactly the conventions of
`C-NATIVE-FIBRE-PENTIT-WIGNER-N/PREREG.md` on merged input
`01821412879dba442e1c864c61855fb4a4dfea99` (original note head
`8945af5d05c5a9e54de015600d6fc40ec8fa6049`).

The question is whether the finite-census minimum
`phi/5 = (1+sqrt(5))/10` is also the infimum over **all** nonzero
real sum-zero vectors, after normalization. The finite census only ranges
over the 624 nonzero balanced-source preparations. It is not this larger
continuous class.

## 2. A continuous family with an explicit Wigner table

For any real `alpha`, set

$$
\psi_j=\sqrt{\frac25}\cos\left(\frac{2\pi j}{5}+\alpha\right).
$$

The sums of nontrivial fifth-root characters vanish. Hence
`sum_j psi_j = 0` and `sum_j psi_j^2 = 1`.
In the phase-point expectation substitute `j=q+t`. The product identity is

$$
\psi_{q+t}\psi_{q-t}
=\frac15\left[
\cos\left(\frac{4\pi q}{5}+2\alpha\right)
+\cos\left(\frac{4\pi t}{5}\right)\right].
$$

Indices in the subscripts are modulo five; the cosine expression is
unchanged by this convention. Consequently

$$
W_\psi(q,r)=\frac1{25}\sum_{t\in\mathbb F_5}
\left[C_q+\frac{\zeta^{2t}+\zeta^{-2t}}2\right]\zeta^{-2rt},
\qquad C_q=\cos\left(\frac{4\pi q}{5}+2\alpha\right).
$$

Character orthogonality gives the complete 25-cell table:

$$
\boxed{
W_\psi(q,r)=\frac{C_q}{5}\mathbf1_{r=0}
+\frac1{10}\bigl(\mathbf1_{r=1}+\mathbf1_{r=-1}\bigr).
}
$$

In particular the constant strips are `r=+/-1`; they are not `q=+/-1`.

## 3. An exact counterexample

Take `alpha = pi/20`, and write
`C = cos(pi/10)`, `S = sin(pi/5) = cos(3*pi/10)`.
Both `C` and `S` are strictly positive, since their cosine angles lie in
the first quadrant. The table is

| r, with q running from 0 to 4 | W(q,r) |
| --- | --- |
| 0 | `(C,-C,S,0,-S)/5` |
| 1 | `(1,1,1,1,1)/10` |
| 2 | `(0,0,0,0,0)` |
| 3 | `(0,0,0,0,0)` |
| 4 | `(1,1,1,1,1)/10` |

Exactly two cells are negative, `(1,0)` and `(4,0)`. Thus

$$
\mathcal N(\psi)=\frac{C+S}{5}.
$$

The usual exact fifth-root cosine identities give

$$
C^2=\frac{5+\sqrt5}{8},\quad
S^2=\frac{5-\sqrt5}{8},\quad CS=\frac{\sqrt5}{4}.
$$

Therefore `(C+S)^2 = (5+2*sqrt(5))/4`. Positivity fixes the root, so

$$
\boxed{\mathcal N(\psi)=\frac{\sqrt{5+2\sqrt5}}{10}.}
$$

For the proposed bound, the exact comparison is

$$
\left(\frac{1+\sqrt5}{10}\right)^2
-\mathcal N(\psi)^2=\frac1{100}>0.
$$

Both quantities are positive. This proves strict inequality and refutes
the proposed universal sharp value. It does **not** prove that this witness
attains the global minimum.

## 4. Relation to the four-source reading

Let `c_j = cos(2*pi*j/5+pi/20)` and choose a real four-source vector
`v_i = c_i-c_0`, `i=1,...,4`. Then `sum_i v_i = -5*c_0`, since
`sum_j c_j=0`. The declared augmentation

$$
\widetilde v=(0,v_1,v_2,v_3,v_4)
-\frac{\sum_i v_i}{5}(1,1,1,1,1)
$$

is exactly `c`, with squared norm `5/2`. Its normalization is the witness.
This identifies it in the larger real-source reading. It supplies no native
preparation of these real amplitudes. The finite 624-state census and its
minimum remain untouched.

## 5. What is and is not closed

The universal proposed value `phi/5` is disproved in this declared class.
The new witness gives a rigorous upper bound on the global minimum. The
separate `LOWER-BOUND.md` proves a stronger general lower bound, leaving

$$
\frac12\tan\frac{\pi}{10}
\ \le\ \min_{\substack{\psi\in\mathbb R^5,\ \sum\psi_j=0\,;\ \|\psi\|=1}}
\mathcal N(\psi)
\ \le\ \frac{\sqrt{5+2\sqrt5}}{10}.
$$

The minimum exists by compactness of the normalized real sum-zero sphere
and continuity of this finite sum of negative parts. Its exact value remains
open. No native dynamics, line-reader obstruction, original negative-Wigner
theorem, finite preparation count, actual-event transducer, Gate 0 disposition,
or Canon status changes as a consequence of this proof.
