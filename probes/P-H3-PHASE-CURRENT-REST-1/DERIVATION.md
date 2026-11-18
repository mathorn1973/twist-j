# Phase and oriented current in the native H3 law

The carrier is the integer cyclotomic ring \(R=\mathbb Z[j]\), where \(j\) is a primitive fifth root, \(\rho=j^2\), \(J=1+\rho\), and \(h(a)=a\bar a\). Write \(\theta=h(J)\). The matching C and collision B are the unchanged maps in the [funded-reference reproduction](../../reproduce/h3-referenced-record/verify.py).

## Five native receivers with one common budget

In columns \(r=0,\ldots,4\), the first vertical matching pairs a receiver with center \(c\) and material half-gap \(2\rho^r\) with a donor with center \(-c\) and half-gap \(2\rho^k\). Both matter contacts admit on parity. On the first two rows, the uniform radiation rails \((2J,-2J)\) are fixed by the first matching. At receiver \(r\), C sends the center to \(\rho c\), and the post-C material half-gap is
\[
d=\rho^r P_{k-r},\qquad
P_s=J+(1-\rho)\rho^s,\qquad
h(P_s)=4+(\rho^{-1}-\rho)(\rho^s-\rho^{-s}).
\]
The five Hermitian norms are distinct. Their rational traces are \(8,13,8,8,3\), so the trace by itself loses the distinction among three phase codes. The radiation half-gap \(f=2J\) makes B1 equivalent to \(h(P_{k-r})=4\), which holds exactly at \(r=k\). B2 would require \(h(P_{k-r})=4\theta^2\). In the \(j=\exp(2\pi i/5)\) embedding, \(0<\theta<1/2\) and all five norms exceed \(7/4\). Thus the other four receivers execute B0. These statements concern the five receivers, with donor collisions governed by the same native law.

The centers \(+\rho^2,1,-\rho^2\) all have norm one. For every center and phase code, the full initial ledger is \(M=U=0\), \(H=100+128\theta\), \(Q=584\). Independent common multiplication of the matter and radiation sectors by norm-one ring units preserves parity, norms and branch tags. The compared matter rotations may reorient the fixed integer projection below.

At the selected receiver \(d=2\rho^k\) and \(f=2J\). B1 writes \(d'=Jd\), \(f'=2\), with both centers fixed. Hence \(d'f'=df\) and \((d'/f')/(d/f)=J^2=\rho\theta\). B2 reverses this change. The phase increment of the ratio is \(\rho\) at either embedding, since \(\theta\) is positive at both. The paid radiation response is
\[
\Delta H_{\rm rad}=8(1-\theta)=8(\phi-1),\qquad
\Delta H_{\rm mat}=-\Delta H_{\rm rad},\qquad
\Delta Q_{\rm rad}=-8,\quad \Delta Q_{\rm mat}=+8,
\]
where \(\phi=-(\rho+\rho^{-1})\) and \(Q\) is the real-subfield trace of \(H\). This response is even under reversal of the signed material center and identifies the active receiver through a local exchange. Its physical calibration remains open.

## Oriented current and the signed-source obstruction

On an oriented C edge with incoming rail values \(a,b\), let \(I=(1-\rho)(a-b)/2\) when the difference is even and \(I=0\) otherwise. The outputs are \(a-I,b+I\). B preserves the sum of each species pair at every site. Summing the C rail currents for each species therefore gives an exact lattice continuity equation, in \(R\) and after any additive projection. Moreover \(j\mapsto1\) defines a ring homomorphism to \(\mathbb F_5\), and \(1-\rho\) maps to zero. The residue of each site's species sum remains fixed at every C and B.

For \(z=a_0+a_1j+a_2j^2+a_3j^3\), set \(\ell(z)=a_3-a_1\). This is the covector used by the earlier referenced archive, where
\[
\frac{\operatorname{Tr}_{\mathbb Q(j)/\mathbb Q}((\rho-\rho^2)z)}{30}
=\frac{\ell(z)}6
\]
is evaluated on archive minus reference. The projected sum of the first two material currents on each of the five oriented receiver-to-donor edges is \(\ell(2(1-\rho)c)\), giving \(+2,0,-2\) for \(c=+\rho^2,1,-\rho^2\) respectively, independent of \(k\). The corresponding single-rail edge with values \(2\rho^2,0\) gives \(+1\). This defines an oriented integer current on the specified phase and budget axes. Its sign uses the fixed covector and edge orientation.

The local involution \((r_0,r_2,\mathrm{CLK},\mathrm{CORR})\mapsto(-r_2,-r_0,\mathrm{CLK},\mathrm{CORR})\) reverses the material center and fixes its half-gap. It commutes with C because both matter rails have the same matching and parity rule. It commutes with B because branch selection and gap updates are center-independent. Thus the two opposite prepared centers are related at every cut by the same involution. Their material species currents reverse, while the entire radiation history and B tags agree. Any reader of those radiation coordinates and tags has identical outputs on these two signed histories. The obstruction applies to this symmetry-related pair class, with no conclusion about other source preparations. The conserved projection and local exchange provide native mathematical observables at L1. Identification with electric charge or mass remains open.
