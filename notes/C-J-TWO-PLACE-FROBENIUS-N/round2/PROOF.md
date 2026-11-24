# Round 2 proof: copies on one native trajectory

NON-CANONICAL. No authority. All new conclusions candidate-D, L1.
Paper continuation of C-J-TWO-PLACE-FROBENIUS-N, issue #2080.

## 1. Observation contract and inherited chart

Fix one arbitrary origin-zero seed \(x_0\in\mathbb F_5^6\). Write
\(\psi_n\) for its actual native checkpoint after \(n\) ticks, and put

\[
\theta_n=s_2(n)\bmod2,\qquad
\Theta_n=2^{s_2(n)}\bmod5,\qquad
Y_n=(\psi_n,\Theta_n).
\]

Here \(s_2\) is the binary digit sum. The clock index is used to define
the trajectory; it is not supplied to the observer. A finite window has
fixed integer offsets \(A\le i\le B\), and its endpoint \(r\) must
satisfy \(r+A\ge3\). A causal window has \(B\le0\). Allowing finitely
many future offsets only strengthens the negative results below.

The registered native chart has a conserved label
\(\ell=(\alpha,\beta,\gamma,\delta,\epsilon)\in\mathbb F_5^5\) for this
seed after synchronization. Define

\[
S(0)=0,\qquad S(m)=m-S(\lfloor m/2\rfloor).
\tag{1.1}
\]

At times \(2m+1\) and \(2m+2\), respectively, the entire checkpoint is
a fixed function of \(\ell\), the parity within the pair,
\(S(m)\bmod5\), and \(\theta_m\). In particular, the native coordinate
called \(r\) in the source, denoted \(R\) here to avoid confusion with
the window endpoint, is

\[
R_{2m+1}=\epsilon+S(m)-1,\qquad
R_{2m+2}=-(\epsilon+S(m)-1)
\quad\text{in }\mathbb F_5.
\tag{1.2}
\]

The source's inverse chart proves this statement for all six
coordinates. The intermediate clock model has an additional coordinate
\(m\bmod5\), but the checkpoint at fixed \(\ell\) does not depend on
it. This distinction is essential.

## 2. Binary digit weights

**Lemma 2.1 [candidate-D].** If \(m=\sum_i b_i2^i\), then

\[
S(m)=\sum_i b_i w_i,\qquad
w_i=\frac{2^{i+1}+(-1)^i}{3}.
\tag{2.1}
\]

The displayed fractions are integers. Expanding (1.1) gives
\(S(m)=m-\lfloor m/2\rfloor+\lfloor m/4\rfloor-\cdots\). The
contribution of bit \(i\) is the alternating geometric sum
\(2^i-2^{i-1}+\cdots+(-1)^i\), which is \(w_i\).

Modulo five the weights have period four:

\[
(w_0,w_1,w_2,w_3)=(1,1,3,0)\pmod5,
\qquad w_{i+4}-w_i=5\cdot2^{i+1}.
\tag{2.2}
\]

Consequently, whenever \(4\mid K\) and \(0\le v<2^K\),

\[
S(2^K H+v)\equiv S(H)+S(v)\pmod5,
\quad s_2(2^K H+v)=s_2(H)+s_2(v).
\tag{2.3}
\]

## 3. Exact copies in every odd residue class

**Theorem 3.1 [candidate-D].** Fix a seed, a synchronized window
\((Y_{r+i})_{A\le i\le B}\), an odd integer \(q>1\), and \(a\ge0\).
There are arbitrarily late exact copies of that window on the same
trajectory in every residue class modulo \(q\), each with endpoint
congruent to \(r\) modulo \(2^a\).

**Proof.** Let

\[
D=\operatorname{lcm}(4,\operatorname{ord}_q2).
\]

Choose a sufficiently large multiple \(K\) of \(D\), with \(K+1\ge a\)
and \(r+B<2^{K+1}\). Put \(M=2^K\). Choose a positive multiple \(C\)
of twenty satisfying \(C\ge q-1\). For each \(t=0,\ldots,q-1\), form
an integer \(H_t\) with \(C\) distinct set bits: put \(t\) of them
at positions congruent to one modulo \(D\), and the other \(C-t\)
at positions congruent to zero modulo \(D\). There are arbitrarily
many available positions of each kind. Then

\[
s_2(H_t)=C\equiv0\pmod4,
\qquad S(H_t)\equiv C=0\pmod5,
\qquad H_t\equiv C+t\pmod q.
\tag{3.1}
\]

Set \(N_t=2MH_t+r\). At each selected offset the low native index
\(r+i\) lies in \([3,2M)\); the high and low binary blocks do not
overlap. Thus the four-phase decoration is unchanged, because its
digit sum increases by \(C\), a multiple of four. The paired index is

\[
\left\lfloor\frac{N_t+i-1}{2}\right\rfloor
=MH_t+\left\lfloor\frac{r+i-1}{2}\right\rfloor,
\]

with the low part in \([0,M)\). Equations (2.3) and (3.1) preserve
its \(S\)-value modulo five and its digit-sum parity. Native time
parity is also unchanged. The seed has the same conserved chart label
at both times, so the complete checkpoints agree.

The endpoint shift is divisible by \(2^a\). Since \(2^K\equiv1\pmod q\),

\[
N_t\equiv r+2(C+t)\pmod q.
\]

As \(t\) varies these are all classes, because two is invertible modulo
odd \(q\). The high bit positions, or \(K\), can be taken arbitrarily
large. This also proves that the same construction works simultaneously
for every seed, without replacing any seed. QED.

## 4. Exact periodic factor classification

**Theorem 4.1 [candidate-D].** Let \(m=2^a q\), \(q\) odd. Fix any set
of admitted residue classes modulo \(m\), and let \(b\) be an output
function on those classes. On any fixed seed, some fixed finite
synchronized window reads \(b(n\bmod m)\) at every sufficiently late
admitted time if and only if \(b\) is constant among admitted classes
having the same residue modulo \(2^a\).

For necessity, take any sufficiently late admitted endpoint and its
finite observation window. Theorem 3.1 copies it into every other
admitted class with the same dyadic phase. Equal inputs force equal
outputs. The copied endpoints can exceed any proposed warmup threshold.
For sufficiency, the registered finite-history clock-phase theorem
reads \(n\bmod2^a\); apply the given function of that phase. For
\(a=0\) the admitted output is constant. For \(q=1\) only the
registered positive direction is needed.

The reader may depend on the fixed seed as a parameter. No change to
the proof results. At period sixty this says exactly that only the
modulo-four part survives in fixed native windows. Restricting to times
coprime to thirty still excludes the inert flag
\(\mathbf1_{\chi_3(n)\chi_5(n)=+1}\), since it varies within a fixed
modulo-four class.

**Corollary 4.2 [candidate-D, finite adaptive queries].** The same
negative conclusion holds for a deterministic observer that, at each
evaluation, adaptively asks for relative native observations and stops
after finitely many such queries, when its decisions depend only on
that transcript and fixed parameters.

For an actual terminating evaluation, enclose its finite set of queried
offsets in one interval. Theorem 3.1 reproduces every answer in an
opposite admissible odd class. Inductively the observer makes the same
next query and reaches the same output. Every queried point is required
to be in the synchronized region. The conclusion does not include a
query reporting the origin boundary, the total available history length,
an absolute index, or extra state retained between evaluations.

## 5. Explicit long collisions

**Theorem 5.1 [candidate-D].** Put \(M=16^k\), \(k\ge1\), and
\(R=2M-5\). The length-\(R\) windows ending at

\[
n=4M-5=2M+R,\qquad n'=6M-5=4M+R
\tag{5.1}
\]

agree exactly on every fixed seed, including \(\Theta\).

For each offset \(i=1-R,\ldots,0\), the common low index \(R+i\)
is in \([1,R]\subset[0,2M)\). The two high blocks are one and two.
They have the same digit sum and the same \(S\)-value:

\[
s_2(1)=s_2(2)=1,\qquad S(1)=S(2)=1.
\]

Since \(\log_2M=4k\), (2.3) and the chart prove the checkpoint
identities, and equality of digit sums proves the decorations agree.
All actual translated observation times exceed three, even though the
low binary block starts at one. No claim about a physical trajectory
before synchronization is used.

Now \(M\equiv16\pmod{30}\), hence \(n\equiv29\) and \(n'\equiv1\)
modulo thirty. Both are admitted unit times. At 29 the product
\(\chi_3\chi_5\) is negative; at one it is positive. For \(M=16\)
the endpoints are 59 and 91 and the common window length is 27.

If a uniform causal width-\(W\) reader is correct at all admitted
synchronized endpoints up to \(N_k=6M-5\), then \(W\le R\) would
give equal inputs at these two endpoints and opposite required outputs.
They are both eligible for such a width. Therefore

\[
W(N_k)\ge R+1=2\cdot16^k-4.
\tag{5.2}
\]

This is a horizon-dependent lower bound for a fixed-width,
time-independent reading rule. It does not count a window length or
an endpoint label as free access to the absolute time.
