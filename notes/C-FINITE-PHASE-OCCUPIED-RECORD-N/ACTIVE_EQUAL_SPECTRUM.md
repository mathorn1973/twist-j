# An auxiliary finite isospectral pair with an active contact

**Status:** NON-CANONICAL, L1, same-session analytical exploration.
**Scope:** a separate extension for review, outside the frozen primary
calibration in `EXPERIMENT.md` and `SPECTRAL.md`. This file does not change
the primary preparations or claim their prospective registration covers
this extension. No scientific executable was run to obtain these results.

Author: A. M. Thorn. Date: 2026-10-25. Apache-2.0.
The result-exposed analytical scope was separately published at
[#1775, issuecomment6399077081](https://github.com/mathorn1973/twist-j/issues/1775#issuecomment-6399077081)
before this note was committed. Separate scientific acceptance remains
pending.

Use the unchanged
[Public Canon v105](https://github.com/mathorn1973/twist-j/blob/892a0b11089d34e241e1eb76d2c03247022d18e6/canon/CANON.md)
`HOMOGENEOUS-CAPTURE-CURRENT-RECORD` operator, coordinates, label basis,
receiver and Fourier convention. The worktree base is
`3abf054e435e31c51e6e50528b09fe3cf7cffe13`; the authority and content
identity are recorded in [SPECTRAL.md](SPECTRAL.md). In particular,
the receiver is at 100, the incoming label index is 0, the old-memory space
is

\[
 \mathcal K=\operatorname{span}\{d_1,\ldots,d_{25}\},
 \qquad P_W=I\otimes|d_0\rangle\langle d_0|\otimes I_{\rm ref}.
\]

The arbitrary old-memory/reference input is
\(\Xi=\sum_{j=1}^{25}d_j\otimes\phi_j\), of norm one. All statements
extend to mixed inputs by purification. Inner products are linear in the
second argument.

The result below is a finite contact-active alternative, with the same
full spectral-energy law and the same initial configuration populations
for its two phases. Its preparations contain coherent token and pulse
components. It does not establish the native preparation of these
components, and it is not an experiment beginning with a pure standing
token.

## 0. Fixed step and notation

The object coordinates are \((R,r)\in\mathbb Z^2\), with physical
positions \(R+r,R-r\). In the coin order \((++,+-,-+,--)\),

\[
 M_2=\frac{(I+2iX)\otimes(I+2iX)}5,\qquad
 \Gamma=I+(e^{-ig}-1)P_{r=0},\qquad W=\Gamma SM_2,
 \qquad g=2\pi/5.
\]

The streaming displacements of the four coins are respectively
\((-1,0),(0,-1),(0,1),(1,0)\). Set
\(A=(e_1-e_4)/\sqrt2\), \(B=(e_2-e_3)/\sqrt2\), and
\(A_a=|R=a,r=0,A\rangle\). At each site and label index the
two contact ports are

\[
 \alpha_{a,j}=|R=a,r=0,iB;\ y=a,t_j\rangle,\qquad
 \gamma_{a,j}=|R=a,r=0,A;\ x=a,1,p_j\rangle.
\]

The contact is the rotation
\(\left(\begin{smallmatrix}3/5&-4/5\\4/5&3/5\end{smallmatrix}\right)\)
on each ordered pair \((\alpha_{a,j},\gamma_{a,j})\), and identity
off these pairs. In a Laurent variable \(z\) representing the right
translation of the pulse, its free two-bank step is

\[
 V(z)=\frac15
 \begin{pmatrix}1-4z^{-1}&-2-2z^{-1}\\2+2z&1-4z\end{pmatrix}.
\]

With \(\beta=4\pi/5\), the uncalibrated full step is

\[
 U=U_0C,\qquad
 U_0=e^{-i\beta}\bigl((W\otimes I_{\rm tok})
                   \oplus(W\otimes V)\bigr).
\]

The memory calibration \(\mathcal T=\mathcal T^{-1}=\mathcal T^*\)
swaps the carrier and memory label indices if the carrier coordinate
\(y\) or \(x\) is at least 100, and is identity otherwise. Thus
\(U_{\rm rec}=\mathcal T(U\otimes I_{\rm mem,ref})\mathcal T\).
The label index is conserved by the uncalibrated step. Whenever label
and memory factors are suppressed below, their identity action or the
explicit calibration is understood; they are never discarded.

## 1. A general exact spectral-filter identity

Let \(\mathscr U\) be unitary, \(\chi\) normalized, and \(\theta\) fixed. Put

\[
 D_\theta=e^{i\theta}\mathscr U^2-e^{-i\theta}\mathscr U^{-2},\qquad
 Z=1+\|D_\theta\chi\|^2,\qquad
 \psi_\pm=\frac{(I\pm D_\theta)\chi}{\sqrt Z}.
 \tag{A1}
\]

Then \(D_\theta^*=-D_\theta\), so the two numerators have the same
squared norm \(Z\), and \(1\le Z\le5\). The complete spectral laws
of \(\mathscr U\) in \(\psi_+\) and \(\psi_-\) agree exactly. Indeed, for
\(z\in\mathbb T\),

\[
 d_\theta(z)=e^{i\theta}z^2-e^{-i\theta}z^{-2}\in i\mathbb R,
 \qquad |1+d_\theta(z)|^2=|1-d_\theta(z)|^2.
\]

Their common law is therefore

\[
 d\mu_{\psi_\pm}(z)
 =\frac{1+|d_\theta(z)|^2}{Z}\,d\mu_\chi(z).
 \tag{A2}
\]

In particular every fixed Borel energy reading of this same unitary,
including \(H_*=f(\mathscr U)\) and \(E_0H_*\), has the same distribution and
equal moments whenever those moments exist. For the selected bounded
reading \(f(e^{-i\omega})=\omega\), \(0\le\omega<2\pi\), every
nonnegative integer moment exists and is equal. This is an exact full-operator
identity. Finite propagation is used below for support and the readout,
not to approximate the spectral measure.

For the application of (A1)--(A2), take \(\mathscr U=U_{\rm rec}\),

\[
 s=97,\qquad
 \chi=\alpha_{s,0}\otimes\Xi
 =|R=s,r=0,iB;\ y=s,t_0\rangle\otimes\Xi,
 \qquad \theta=0,\qquad D=U_{\rm rec}^2-U_{\rm rec}^{-2}.
 \tag{A3}
\]

Equation (A1) specifies two finite coefficient tables. It does not require
adding \(D_\theta\), a reverse-time operation, or any new gate to the
subsequent apparatus evolution. Native preparation of those tables is a
separate gate.

## 2. Equal populations, finite support and an active contact

The carrier displacement in one forward or inverse macrostep is at most
one. Consequently \(U_{\rm rec}^{\pm2}\chi\) is supported entirely
on carrier coordinates at most 99. The initial receiver calibration is
identity on the complete support of both preparations. Their carrier
label index remains 0, their old memory remains exactly \(\Xi\), and
\(P_W\psi_\pm=0\).

To prove equality of all initial configuration populations, define

\[
 \Sigma=\mathsf P_o\,\eta,\qquad
 \eta=+I\text{ on tokens},\quad \eta=-I\text{ on pulses},
\]

where \(\mathsf P_o|R,r,e_j\rangle=|R,-r,F e_j\rangle\), and
\(F\) exchanges coins 2 and 3 while fixing coins 1 and 4. The matrix
\(F\) exchanges the tensor factors of \(M_2\). Together with
\(r\mapsto-r\) it preserves streaming and the contact line \(r=0\),
so \([\mathsf P_o,W]=0\). The free factors and the receiver therefore
commute with \(\Sigma\).
At each contact, \(\alpha\) is object-odd in the token arrangement
and \(\gamma\) is object-even in the pulse arrangement. Both therefore
have \(\Sigma=-1\), so \([\Sigma,C]=0\) and
\([\Sigma,U_{\rm rec}]=0\).

The input \(\chi\) lies in the \(\Sigma=-1\) sector. On its
source-coordinate fiber \((R,r,y)=(s,0,s)\) in the token arrangement,
the \(\Sigma=-1\) object-coin space is one-dimensional, spanned by
\(B\). The projection of \(D\chi\) onto that fiber is
therefore \(q\chi\), with

\[
 q=\langle\chi,D\chi\rangle
  =2i\operatorname{Im}\langle\chi,U_{\rm rec}^2\chi\rangle.
\]

In fact \(q=0\). Set \(h=e^{-ig}\), \(k=e^{-i\beta}\). The
initial retained token has amplitude \(3/5\). Its object has
\(r=\pm1\) before the second contact, and its two-step source return
coefficient is \(4h/5\). A pulse emitted at the first step can convert
back at the second contact only at \(s-1\), so it cannot return to
the source token coordinate \(y=s\) at time 2. Therefore

\[
 \langle\chi,U_{\rm rec}^2\chi\rangle
  =k^2\frac35\frac{4h}5=\frac{12}{25},
 \qquad k^2h=1.
 \tag{A3a}
\]

The common memory/reference factor is unaffected on the entire initial
support. On the two nonzero configuration ports of \(\chi\), the
two preparations agree exactly and \(D\chi\) vanishes. Everywhere
else their coefficients are exact negatives. Thus they have identical
configuration probabilities and differ only by relative signs. The
normalization in (A1) is one common normalization of each complete state.

Their contact is active already at the first macrostep: each has the
nonzero \(\alpha_{s,0}\) coefficient \(1/\sqrt Z\).
The contact rotation has no eigenvalue 1 on its two-dimensional port
space, so a nonzero port projection implies \(C\psi_\pm\ne\psi_\pm\).
This construction is not confined to the reducing pulse sector used by
the primary experiment.

### 2.1 Complete supplied preparation unitaries

The preparations can be specified by complete fixed unitaries that act
only on the source apparatus and are identity on the unknown old memory
and every reference. This is a specification of a supplied preparation,
not a claim of native synthesis.

To avoid defining any gate using an unknown memory state, work first on
the source Hilbert space without memory or reference. Put

\[
 \chi_s=\alpha_{97,0},\qquad
 d_s=(U^2-U^{-2})\chi_s,\qquad
 r=\|d_s\|=\sqrt{Z-1},\qquad e_s=d_s/r,
\]

where \(U=U_0C\) is the fixed uncalibrated source operator of Section
0. Both \(U^{\pm2}\chi_s\) are supported on carrier coordinates
at most 99. Thus, for every admitted \(\Xi\),

\[
 (U_{\rm rec}^2-U_{\rm rec}^{-2})(\chi_s\otimes\Xi)
 =d_s\otimes\Xi.
\]

Equation (A3a) gives \(\langle\chi_s,d_s\rangle=0\). The exact
normalization proved in Section 4.3 gives
\(r^2=(23896+154\sqrt5)/15625>0\). Therefore
\((\chi_s,e_s)\) is an orthonormal pair, determined entirely by
the fixed source operator. Define

\[
 G_\pm\big|_{\operatorname{span}\{\chi_s,e_s\}}
 =\frac1{\sqrt Z}
   \begin{pmatrix}1&\mp r\\\pm r&1\end{pmatrix},
 \qquad
 G_\pm\big|_{\operatorname{span}\{\chi_s,e_s\}^{\perp}}=I.
 \tag{A3b}
\]

Since \(Z=1+r^2\), these are unitary, and

\[
 (G_\pm\otimes I_{\rm mem,ref})(\chi_s\otimes\Xi)
 =\psi_\pm.
\]

The same two gates work for every allowed old memory, including arbitrary
reference correlations. No projector onto an unknown
\(\chi_s\otimes\Xi\) is used. They are identity outside a fixed
two-dimensional source span and are not applied during the subsequent
three steps of \(U_{\rm rec}\).

For completeness, even the seed \(\chi_s=iB\) has a fully specified
supplied two-port loader. On the ordered source basis ports
\(u_2=|R=97,r=0,e_2;\ y=97,t_0\rangle\) and
\(u_3=|R=97,r=0,e_3;\ y=97,t_0\rangle\), set

\[
 L\big|_{\operatorname{span}\{u_2,u_3\}}
 =\frac{i}{\sqrt2}\begin{pmatrix}1&1\\-1&1\end{pmatrix},
 \qquad L\big|_{\operatorname{span}\{u_2,u_3\}^{\perp}}=I.
\]

It is unitary and \(Lu_2=\chi_s\). Thus
\((G_\pm L)\otimes I_{\rm mem,ref}\) is a complete supplied
preparation from that specified basis source. Neither \(L\) nor
\(G_\pm\) is claimed to be derived from the original six-pentit rule.

One common loader and a finite phase selector also suffice. Let
\(P_{\rm src}=|u_2\rangle\langle u_2|+|u_3\rangle\langle u_3|\)
on the source space, and put \(F=I-2P_{\rm src}\).
This complete diagonal unitary changes the signs of just those two
source coordinates, with identity on its full complement and on
memory/reference. Since \(d_s\) vanishes on both coordinates,
\[
(F\otimes I_{\rm mem,ref})\psi_+=-\psi_-.
\]
The global minus has no observable effect. Thus the same supplied
\(G_+L\) can prepare the source in both settings, with either identity
or \(F\) as the relative-phase choice before the three forward steps.
This explicitly specified selector has no dependence on the unknown
receiver contents; its native realization is still a preparation
resource rather than a derived part of the spatial law.

## 3. Reduction of the three-step readout to one cross term

After three unchanged steps,

\[
 U_{\rm rec}^3\psi_\pm
 =\frac{U_{\rm rec}^3\chi
 \pm U_{\rm rec}^5\chi
 \mp U_{\rm rec}\chi}{\sqrt Z}.
\]

The one-step state has carrier coordinates at most 98, so
\(P_WU_{\rm rec}\chi=0\). Hence the difference of receiver-only
flag weights is

\[
 p_\pm^{(3)}
 =\frac1Z\bigl\|P_W(U_{\rm rec}^3\pm U_{\rm rec}^5)\chi\bigr\|^2,
 \qquad
 p_+^{(3)}-p_-^{(3)}=\frac4Z\operatorname{Re}c,
 \qquad
 c=\langle U_{\rm rec}^3\chi,
               P_WU_{\rm rec}^5\chi\rangle.
 \tag{A4}
\]

The only receiver-side component of \(U_{\rm rec}^3\chi\) is the
pulse at \(x=s+3=100\), bank 2. It comes from conversion at the first
contact and three successive right moves. A later conversion cannot
reach that position in time.

Let \(Q_{\rm front}\) project onto this position, bank and arrangement, with
identity on all remaining factors. Since
\(U_{\rm rec}^n=\mathcal T U^n\mathcal T^*\), the input is on the
left, and \(\mathcal T\) commutes with position and bank projectors,
the inner product in (A4) equals

\[
 c=\langle Q_{\rm front} U^3\alpha_s,
               Q_{\rm front} U^5\alpha_s\rangle.
 \tag{A5}
\]

Here the uncalibrated \(U\) acts on the unlabeled source
\(\alpha_s\); the normalized memory/reference factor cancels from
the inner product. The label 0 and the restriction of old memory to
\(\mathcal K\) justify replacing the memory flag by arrival in this
inner product. This is not a global equality of the two projectors.

For the individual weights, let \(Q_R\) denote the full right-side
carrier projector, including every token or pulse with carrier
coordinate at least 100. Then the exact finite weight definitions are

\[
 p_\pm^{(3)}
 =\frac1Z\bigl\|Q_R(U^3\pm U^5)\alpha_s\bigr\|^2.
 \tag{A5a}
\]

One must use \(Q_R\), not just \(Q_{\rm front}\), in (A5a):
\(U^5\alpha_s\) can have other right-side components. Only the
cross term with \(U^3\alpha_s\) reduces to its extreme front.

## 4. Exact evaluation of the finite cross term

Write

\[
 h=e^{-ig}=e^{-2\pi i/5},\qquad k=e^{-i\beta}=e^{-4\pi i/5},
 \qquad U=k\widehat U,\qquad \widehat U=\widehat U_0C.
\]

Let \(A_a=|R=a,r=0,A\rangle\). The coefficient of a pulse emitted
with bank 1 and taking \(m\ge1\) successive right moves is

\[
 f_m=\frac25\left(-\frac45\right)^{m-1}.
\]

The three-step front is therefore

\[
 Q_{\rm front}\widehat U^3\alpha_s
 =a_3\,W^3A_s\otimes|s+3,2\rangle,
 \qquad a_3=\frac45f_3=\frac{128}{625}.
 \tag{A6}
\]

The five-step amplitude at that same carrier position has the following
exhaustive decomposition.

1. The initial emission propagates freely for all five steps.
2. The initial token component is retained, returns to its source contact
   before step 3, and emits there.
3. The initially emitted pulse meets one further contact, with a
   pulse-to-pulse correction \(3/5-1=-2/5\), before a step
   \(t\in\{2,3,4,5\}\).

For completeness of item 3, before that contact put \(n=t-1\).
A pulse in bank 1 after \(n\) steps has position at most
\(s+n-1\). Object streaming changes \(R+r\) and \(R-r\) by an
odd integer at every step, so at \(r=0\) it requires
\(R-s\equiv n\pmod2\). Contact requires \(x=R\), reducing the
maximum contact position to \(s+n-2=s+t-3\). To reach \(s+3\)
at time 5, this bound must be saturated and all remaining moves must
be right moves. After the first such move the bank is 2, so no further
contact can contribute. Conversion to a token at that contact also loses
the required right displacement and cannot contribute.

For item 2, a retained token has no contact at step 2 because its object
has \(r=\pm1\). A conversion at step 4 or later cannot reach 100.
Its step-3 source return coefficient is

\[
 \langle\alpha_s,W^2\alpha_s\rangle=\frac{4h}5.
\]

### 4.1 Free pulse and late token emission

The free pulse coefficient is

\[
 b_5=\langle s+3,2|V^5|s,1\rangle=-\frac{608}{3125},
 \qquad \langle A_s,W^2A_s\rangle=\frac{4h^2}5.
\]

Thus, after taking the inner product against the object factor in (A6),
the free contribution to \(c/(k^2a_3)\) is

\[
 \frac45 b_5\frac{4h^2}5=-\frac{9728h^2}{78125}.
\]

The late token contribution to that same quotient is

\[
 \frac35\frac{4h}5\frac45 f_3
 =\frac{1536h}{15625}.
\]

One way to check \(b_5\) without enumerating paths is to write the
right-translation variable as \(z\):

\[
 V(z)=\frac15
 \begin{pmatrix}1-4z^{-1}&-2-2z^{-1}\\2+2z&1-4z\end{pmatrix},
 \qquad H(z)=2-4(z+z^{-1}).
\]

The determinant is 1. Cayley--Hamilton gives
\((V^5)_{21}=(t^4-3t^2+1)V_{21}\), where \(t=H/5\).
The coefficients of \(z^3,z^2\) in
\(H^4-75H^2+625\) are \(-512,208\), respectively. Multiplication
by \(2+2z\) yields \(2(-512+208)=-608\), with denominator
\(5^5=3125\).

### 4.2 All four pulse self-contact corrections

For \(t=2,3,4,5\), put

\[
 n=t-1,\quad m=6-t,\quad c_t=s+t-3,
\]
\[
 b_n=\langle c_t,1|V^n|s,1\rangle,\qquad
 r_n=\langle A_{c_t},W^nA_s\rangle,\qquad
 o_t=\langle W^3A_s,W^mA_{c_t}\rangle.
\]

The contribution to \(c/(k^2a_3)\) is exactly

\[
 -\frac8{25}\,b_n r_n f_m o_t.
 \tag{A7}
\]

The finite coefficients are:

| Contact step \(t\) | \(b_n\) | \(r_n\) | \(f_m\) | \(o_t\) |
|---|---:|---:|---:|---:|
| 2 | \(-4/5\) | \(h/2\) | \(-128/625\) | \(h/2\) |
| 3 | \(-7/25\) | \(4h^2/5\) | \(32/125\) | \(1\) |
| 4 | \(4/25\) | \(12h^3/25\) | \(-8/25\) | \(h^{-1}/2\) |
| 5 | \(-48/625\) | \((20h^4+16h^3)/125\) | \(2/5\) | \(h^{-2}/10\) |

The pulse entries follow from
\(V^2=tV-I\), \(V^3=(t^2-1)V-tI\), and
\(V^4=(t^3-2t)V-(t^2-1)I\) with the same Laurent matrix above.
For the object entries, \(M_2A=A\). Near the front \(R=s+n-2\)
there is either one left center move among right center moves, or one
opposite pair of relative moves. The latter can contribute to an
\(A\)-projection only for \(n=4\): the first and last moves are
right center moves, and the two middle relative moves are opposite.
They contribute \(8h^3/125\) each. The four single-left paths
contribute \((2+8+8+2)h^4/125\). This proves the last object entry;
the shorter entries follow from the same paths. The \(o_t\) entries
then follow by unitarity from one- and two-step object overlaps.

Substitution in (A7) gives:

| Source of the contribution | Contribution to \(c/(k^2a_3)\) |
|---|---:|
| Free initial emission | \(-9728h^2/78125\) |
| Retained token emits at step 3 | \(1536h/15625\) |
| Pulse self-contact at step 2 | \(-1024h^2/78125\) |
| Pulse self-contact at step 3 | \(7168h^2/390625\) |
| Pulse self-contact at step 4 | \(1536h^2/390625\) |
| Pulse self-contact at step 5 | \((7680h^2+6144h)/48828125\) |

Their sum is

\[
 \frac{4806144h-5624320h^2}{48828125}.
\]

Multiplying by \(k^2a_3\) and removing common factors gives the exact
cross term

\[
 \boxed{c=k^2\frac{65536}{5^{15}}
             \bigl(9387h-10985h^2\bigr)
       =\frac{65536}{5^{15}}(9387-10985h).}
 \tag{A8}
\]

The factor \(k^2\) is required: the first vector carries \(k^3\)
and the second \(k^5\), and the inner product is conjugate-linear
in its first slot.

### 4.3 Exact common normalization

For the sign-only choice \(D=U_{\rm rec}^2-U_{\rm rec}^{-2}\),

\[
 Z=3-2\operatorname{Re}m_4,\qquad
 m_4=\langle\chi,U_{\rm rec}^4\chi\rangle.
\]

The receiver conjugation drops out of this source-to-source matrix
element because \(\mathcal T\chi=\chi\). Its purely object
four-step return is

\[
 \langle B,W^4B\rangle=\frac{80h^2-28h}{125}.
 \tag{A8a}
\]

Here is an exhaustive short path check of (A8a). The first and last
moves must be relative moves because the input and output coins are in
\(B\). If all four moves are relative, the two monotone-out-and-back
paths each contribute \(2h/125\); the other four contribute
\((32+8+8+32)h^2/125\). The only remaining possibility has an initial
relative move, two opposite center moves, and the final relative return.
There are four such paths, each contributing \(-8h/125\). This gives
\((80h^2+4h-32h)/125\).

Exactly three contributions can return to the source token in four
steps:

* The initial token amplitude \(3/5\) propagates freely, giving
  \((3/5)k^4(80h^2-28h)/125\).
* The retained token meets its source contact before step 3. The
  self-contact correction \(-2/5\) between two return coefficients
  \(4h/5\) gives
  \(k^4(3/5)(4h/5)(-2/5)(4h/5)=-96/625\).
* The initial pulse emission returns to \(\gamma_s\) before step 3.
  Its coefficient is
  \((4/5)(4h^2/5)(-7/25)=-112h^2/625\). Conversion to the token
  contributes \(-4/5\), followed by the two-step token return
  \(4h/5\). Including \(k^4\), this gives \(1792h/15625\).

At the step-2 contact the source port has zero amplitude. An earlier pulse contact can
only be at \(s-1\); a conversion there retains that token coordinate,
while a right move returning the pulse to \(s\) gives bank 2 and
cannot feed the step-3 source port. A conversion at step 4 leaves only
one object step, which takes \(B\) to \(r=\pm1\) and has zero
source overlap. These facts exclude additional contact histories.

Using \(k^4h^2=1\), \(k^4h=h^{-1}\), and \(k^4h^3=h\),

\[
 m_4=\frac{3600-2100h^{-1}+1792h}{15625},\qquad
 \operatorname{Re}m_4=\frac{3677-77\sqrt5}{15625}.
\]

The common preparation normalization is therefore exactly

\[
 \boxed{Z=\frac{39521+154\sqrt5}{15625}.}
 \tag{A8b}
\]

## 5. Strict phase contrast with equal full energy law

For the chosen \(\theta=0\), use
\(\cos(2\pi/5)=(\sqrt5-1)/4\) in (A8):

\[
 \operatorname{Re}c
 =\frac{16384}{5^{15}}(48533-10985\sqrt5)>0.
\]

Consequently the finite three-step experiment has

\[
 \boxed{p_+^{(3)}-p_-^{(3)}
   =\frac{65536(48533-10985\sqrt5)}{Z\,5^{15}},
   \qquad 1\le Z\le5.}
 \tag{A9}
\]

Substituting (A8b) gives an exact expression and a stronger strict lower
bound:

\[
 \boxed{p_+^{(3)}-p_-^{(3)}
 =\frac{65536(48533-10985\sqrt5)}
        {5^9(39521+154\sqrt5)}
 >\frac1{50}.}
 \tag{A10}
\]

Indeed, \(\sqrt5<9/4\) bounds the numerator from below and the
denominator from above, giving

\[
 p_+^{(3)}-p_-^{(3)}
 >\frac{32768\cdot95267}{79735\cdot5^9}>\frac1{50}.
\]

The last rational comparison is
\(50\cdot32768\cdot95267=156085452800>
155732421875=79735\cdot5^9\).

Both preparations have identical full spectral laws by (A2), identical
initial configuration populations by Section 2, an initially untriggered
receiver flag, and an active unchanged contact. This conclusion follows
from finite exact amplitudes and symmetry; it is not a finite-time
approximation to the spectral energy.

On every receiver-side carrier branch, the unchanged label calibration
performs

\[
 |\kappa_0\rangle\sum_{j=1}^{25}|d_j\rangle|\phi_j\rangle
 \longmapsto
 \sum_{j=1}^{25}|\kappa_j\rangle|d_0\rangle|\phi_j\rangle,
\]

where \(\kappa\) is the branch's token or pulse arrangement with its
position and bank held fixed. The old memory and its reference
correlations are transferred coherently. This is the same label isometry
for both phases, although their carrier wave packets need not be the
same after conditioning.

This also describes the full channel, including coherences between
arrival and nonarrival. Let \(\Phi_t\) be the uncalibrated evolved
apparatus state with carrier label index 0, and let \(L_j\) change
that index from 0 to \(j\) without changing any position, coin or
arrangement. The complete calibrated state is

\[
 (I-Q_R)\Phi_t\otimes\sum_{j=1}^{25}d_j\otimes\phi_j
 +\sum_{j=1}^{25}L_jQ_R\Phi_t\otimes d_0\otimes\phi_j.
 \tag{A11}
\]

It is exactly \(\mathcal T(\Phi_t\otimes\Xi)\), so it is an
isometry on every admitted old-memory/reference input. Equation (A11)
does not trace out the reference or replace the old memory by a classical
label. It applies to either phase and every integer time; the present
readout evaluates it at time 3.

The arithmetic reading remains finite, using the inherited
[full-record arithmetic result](https://github.com/mathorn1973/twist-j/blob/3abf054e435e31c51e6e50528b09fe3cf7cffe13/notes/C-FULL-RECORD-SCALE-LIFT-N/PROOF.md).
For a memory basis input, put
\(\chi_0=\sqrt2\chi\), whose two object-coin coefficients are
\(i,-i\), and \(\mathcal A=25U_{\rm rec}\). Then

\[
 a_\pm=\bigl[625I\pm(\mathcal A^2-(\mathcal A^*)^2)\bigr]\chi_0
       \in\mathbb Z[\zeta_{20}]^{(\mathrm{finite})}.
\]

Their common complex normalization is \(625\sqrt{2Z}\). This supplies finite arithmetic
tables in principle; no executable table was generated or tested here.
The arbitrary complex reference statement remains a Hilbert-space
operator identity and is not a claim of finite integer representation
for every reference state.

The remaining preparation and physics boundaries are substantive. These
inputs already contain pulse components; their spectral-filter formula
does not supply a native preparation process from a pure token or the
original six-pentit update. The proof does not identify the Borel energy
with a local physical energy density, prove occurrence, or establish a
finite receiver's retention and renewal.
