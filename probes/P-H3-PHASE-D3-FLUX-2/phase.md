# Local phase steps and remote H3 phase reads

This finite L1 experiment compares a local C difference, the leading received CORR word, the free walk's Fourier eigenphase and two loaded detector outputs. Each phase belongs to a declared observable. The tests use the pinned native H3 law and exact cyclotomic words.

## Distinct free and local observables

Write $\rho=j^2$, $J=1+\rho$, $L=1-\rho$ and $\phi=-(\rho+\rho^{-1})$. For admitted C on a pair, the center stays fixed and the half-difference is multiplied by $\rho$. Its phase angle modulo one turn is $2/5$ turns in embedding one and $4/5$ turns in embedding two. A clean newly reached site, with incoming pair words $(s,0)$ or $(0,s)$, receives $Ls/2$. This leading multiplier has phase $-1/20$ turns in embedding one and $3/20$ turns in embedding two and modulus squared $h(L)/4$ in the respective embedding. Its parity requirement and the zero receiver word are part of the statement. The native pair sentinels compare the actual outputs for $(2,0)$ and $(2,2J)$, which share a first input word and have different components after C.

In the free, admitted, horizontal sector, set $\alpha=J/2$ and $\beta=L/2$. At two-site cell character $z$ a two-tick map is

$$
 M(z)=
 \begin{pmatrix}\alpha&\beta z^{-1}\\\beta z&\alpha\end{pmatrix}
 \begin{pmatrix}\alpha&\beta\\\beta&\alpha\end{pmatrix}.
$$

Its determinant is $\rho^2$ and its trace is $2\alpha^2+\beta^2(z+z^{-1})$. At staggered $z=-e^{iq}$ the eigenvalues in an embedding are $\rho e^{\pm i\Omega(q)}$ with $\cos\Omega(q)=1-\nu+\nu\cos q$ and $\nu=\sigma(2+\phi)/4$. Log the exact cosine values at $q=0,\pi/2,\pi$. These are temporal phases of pure eigenmodes per two native ticks. At $q=0$ the carrier is exactly $\rho I$, and at a ten-tick strobe its carrier phase cancels. Mixed local samples can have different phases and amplitudes because their components superpose. The eigenphase, local C difference and leading CORR factor use different inputs and cuts.

## Funded launches and apparatus

Use a complete 80 by 4 torus, initial matching bit zero, receiver $(1,0)$, and eight native ticks. Set $u=2L^5$. Prepare no unlisted coordinates. The source distance $d$ runs from 1 through 5 bonds and the phase code $k$ runs from 0 through 4. The source lies to the left when $d$ is odd and to the right when $d$ is even. In either case its tick-one matching faces the receiver. The same apparatus and matching bit are used in all launches within a mode.

For every $d$ keep a pair of words $\pm2^{d+2}L^{5-d}J$ on row zero, with slots $30+2(d-1)$ and $31+2(d-1)$. For the active distance, multiply both words of its pair by $\rho^k$, and move only the positive word to the specified source site. The other distances remain parked. The null launch keeps all pairs parked and unrotated. Remote slots remain outside the receiver causal cone through tick eight. The rotated pair has the same $h$ stock, and its linear sum is zero. Complete initial ledgers agree within each mode, across both distance and phase code and with the null. This calibrates amplitudes analytically with distance. It makes no equal-source-amplitude assertion across distances.

The reference is a separate funded CLK column at $x=65$ with word $u$ at each row, and zero matter there. Read a complex ratio against its literal row-zero word using exact numerator $a\overline u$ and denominator $h(u)$. The two modes are separate preparations. Both use constant material columns at $x=1$, with each row initialized as follows.

- **Coherent read.** Matter is $(u,-u)$ and CLK is zero. The admitted front reaches the target at post-C tick $d$ as $W=2uJ\rho^k$. B1 is independent of $k$ because $h(\rho)=1$. The actual emitted CLK is $u\rho^{k+1}$ and the receiver matter becomes $(uJ,-uJ)$. This signed output retains the input's relative phase changes against the common reference while the branch and material work agree across the five phase codes. The asserted phase is a prepared remote transfer, with its offset fixed by the read equation.
- **Biased read.** Matter is $(uL,-uL)$, and CLK is $b=2uJ$ on all four receiver rows. Before the incident front, the baseline gives gap ratio $h(J)/h(L)$. Its real-subfield norm is $1/5$, so it cannot equal $h(J)$ or $h(J)^{-1}$, each of norm one. At tick $d$ the field half-gap is $uJ(1-\rho^k)$. The exact norm ratios in order $k=0,1,2,3,4$ are $0,T,T^2,T^2,T$, where $T=h(J)$ and $1-\rho^2=LJ$. B1 is therefore predicted exactly at $k=1,4$, and B0 at the other phases. At a write, the emitted CLK shift from $b$ is $u\rho(\rho^k-1)$. At a B0 the shift is zero. This is a native phase-selective branch against a fixed CLK bias at matched full stock, with radiative and material backreaction included.

## Reads and criteria

Record first nonzero target CORR, each clean path's same-cut check $2s_{\rm next}=Ls_{\rm previous}$, incident word, phase ratio, B branch, Hermitian and scalar work, and outgoing material and radiation at tick $d$. At tick $d+1$ read the actual CLK shift in the separate matched vertical neighbor, row 3 for odd $d$ and row 1 for even $d$. The just-written shift is even and the neighbor still has the baseline, so post-C transfer to that neighbor is $L/2$ times the write. Record this word before and after B and whether the nonzero shift survives that B. Retain all subsequent branch tags through tick eight, and whether the fixed reference column stays constant. The null should produce no receiver arrival or active branch within the declared horizon. Wrong first-arrival, per-edge factor, read branch, written word or delayed transfer rejects the corresponding finite prediction. A scientific disagreement is retained in the output.

Run sparse C across every edge with a nonzero input and native B on every site with material. Zero pairs are fixed, and B on zero material is inactive by the native guards. Compare the first two cuts in the distance-one, code-zero arm of each mode to the full dense pinned engine. Check all complete accounts at all cuts, every inverse transition and full restoration from the terminal state. Such implementation and integrity discrepancies stop the run. The parity, legal preparations, funding, reader and horizons bound the result. In particular, an exact phase-selective contact does not identify a universal phase step or an embedding or phase selected by physical light.
