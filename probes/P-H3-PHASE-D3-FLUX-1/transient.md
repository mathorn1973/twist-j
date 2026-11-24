# D3 scalar turn-on and discrete character phase

This module uses the registered D3 weighted long-edge spatial operator and its selected scalar temporal transfer. It treats the external source as prescribed. The observations are scalar lattice flux and discrete temporal phase.

## Source switch from rest

On the infinite lattice $D_3=\{x\in\mathbb Z^3:\sum_i x_i\text{ is even}\}$ take $u_{-1}=u_0=0$ and apply a unit source at the origin at every update $t\ge0$:

$$
 u_{t+1}=2u_t-Au_t-u_{t-1}+\delta_0,\qquad
 (Au)(x)=\frac1{324}\sum_v w_v[u(x)-u(x+v)].
$$

Use the same full shell stencil as the [grounded static comparison](shell.md). Store finite support exactly as integers $X_t=324^{t-1}u_t$ at $t\ge1$, with $X_0=0$ and $X_1=\delta_0$. With $L=324A$, advance $X_{t+1}=(648I-L)X_t-324^2X_{t-1}+324^t\delta_0$. Each step enlarges support by at most one permitted edge. Store through $t=7$ to measure the second time difference at $t=6$.

For times $t=0,1,2,4,6$ and closed Euclidean balls $B_r$ with $r=1,2,3,4$, sum outward graph flux directly over every weighted edge with one endpoint $x\in B_r$ and the other endpoint $x+v\notin B_r$. Each contribution is $w_v[u_t(x)-u_t(x+v)]/324$. Separately sum the actual second time difference $u_{t+1}-2u_t+u_{t-1}$ at all sites in the ball. Use independent boundary and temporal sums. Their sum must equal one in every scored case. At $t=0$ the field and flux are zero and acceleration carries the full source. At $t=1$ the field is the unit source, so the four boundary fluxes must be $8/9,35/54,5/54,0$. The stencil's long edges all count even when a proper cut excludes intermediate sites. A failed exact check rejects the corresponding finite prediction.

A time-independent solution of $Au=\delta_0$ has zero temporal second difference and integrated flux one across these closed cuts. Use this unit benchmark and record which transient rows equal it. The recurrence and finite support specify a causal turn-on for the declared scalar model. They provide neither an asymptotic approach to the grounded solution nor a Maxwell field equation.

## Constant eigenphase and common phase-step test

Use the exact isolated characters $k=(\pi/2,0,0)$ and $k=(\pi,0,0)$. The two cosine tables at integer $v_x$ are respectively $(1,0,-1,0)$ and $(1,-1)$, extended periodically. Sum the registered shell symbol with these tables. Freeze the expected spatial values $77/81$ and $32/81$, giving temporal traces $85/81$ and $130/81$. A pure character eigenmode multiplies by one fixed eigenvalue each update, satisfying

$$
 \lambda^2-(2-s(k))\lambda+1=0.
$$

At both selected characters $0<s<4$, so the two roots are conjugate unit phases. If a root were a root of unity, then $\lambda+\lambda^{-1}$ would be an algebraic integer. Each trace here is rational and nonintegral, which rules out any root of unity. The discriminants give distinct imaginary quadratic fields with squarefree radicands $-19019$ and $-146$. Under any choice of the temporal branch at each character, nonzero eigenvalue powers cannot agree. An equality would lie in the intersection $\mathbb Q$ of the two fields. Since the common value would have unit modulus it would be $1$ or $-1$, contradicting the root-of-unity obstruction. Consequently no common angular generator, even of infinite order, can produce both eigenphases as its nonzero integer powers. This concerns those two characters and the frozen scalar update. The native H3 contact phase is a separate observable.
