# Material Bloch rest branches, gap, curvature and signed group speed

Use the native cold material rail with zero radiation. B is inactive.
The all-admitted linear transfer is an exact contact law on any native
window in which the parity guards admit. Its spectral analysis uses the
principal complex embedding with `rho=exp(4 pi i/5)`. Return to the same
matching color after two native steps. Use dimer position n, with even
and odd site amplitudes `(u,v) z^n` and `z=exp(i k)`. Put
`A=(1+rho)/2`, `B=(1-rho)/2`, and use even C before odd C. The symbols are

    E=[[A,B],[B,A]]
    O(z)=[[A,B/z],[B z,A]]
    T(z)=O(z) E
    det T(z)=rho^2
    tr T(z)=2 A^2+B^2(z+1/z)

Both factors are unitary for |z|=1. The unitary determinant-one
normalization rho^-1 T has branches exp(+/-i Omega), where

    phi=-(rho+rho^-1), b=(phi+2)/4, 0<b<1,
    cos Omega=(2-phi)/4-b cos k = 1-b(1+cos k),
    0<=Omega<=4 pi/5.

These are exact formulas for the selected sector; the finite replay does
not discretize the derivatives.

## Unstaggered rest and staggered crossing

At k=0, E and O coincide. The uniform vector (1,1) has eigenvalue 1,
and the optical vector (1,-1) has eigenvalue rho^2, with raw optical
phase step -2 pi/5 modulo 2 pi per two-step cycle. The same-cycle
relative optical phase against the co-evolved uniform reference is
therefore rho^2. Sampling once per cycle determines a frequency modulo
2 pi. Halving a two-step phase does not determine a unique one-step
frequency branch. The fixed same-color reference marks the raw cycle
frequency without an extra carrier rephasing. The native one-step
subcuts resolve the unstaggered optical phase as rho, because both
matching factors equal E at z=1. This is not the principal square root
of rho^2. These unstaggered fields stay admitted indefinitely at
integer amplitude: for the optical field the difference at each paired
contact is twice its signed word, and each matching multiplies it by rho.

In the convention `lambda=exp(-i omega)`, use the continuous local lift
`omega_opt(k)=2 pi-4 pi/5-Omega(k)` around k=0. It has
`omega_0=2 pi/5`, zero group velocity and

    omega_opt''(0)=b/sin(4 pi/5)>0
    omega_opt(k)^2-omega_0^2
        = [omega_0 b/sin(4 pi/5)] k^2 + O(k^4).

This fixes the sign of the leading optical spectral mass-shell
coefficient for this frequency origin and clock. The zero-frequency
rest branch uses `omega_uni(k)=Omega(k)-4 pi/5`: it has the negative
quadratic curvature, also zero group velocity, so this zero frequency
does not itself yield a linear massless cone.

At k=pi, `T(-1)=rho I` exactly. Relative to that raw carrier, put
`q=k-pi`; the local relative crossing has analytic signed branches

    omega_rel(q)=+/- 2 asin(sqrt(b) sin(q/2)).

Thus its two local slopes are +/-sqrt(b). For nondegenerate k the
signed group velocity in the optical lift is
`b sin(k)/sin(Omega(k))`, and the complementary branch has the
opposite slope. Their magnitudes are bounded by sqrt(b), as the same
formula near the crossing can be written with absolute value
`sqrt(b) |cos(q/2)|/sqrt(1-b sin^2(q/2))`. Units are dimers per
two-step cycle, numerically equal to sites per one native update.
This bound concerns spectral group velocity. An exact finite signal
front or a native confined packet is a different observable.

The optical coefficient divided by the staggered squared speed b is
`(2 pi/5)/sin(pi/5)>1`, since sin x < x for x>0 here. Thus with these
fixed frequency origins the optical small-k deformation and the
staggered crossing do not furnish a single relativistic coefficient.
Changing the relative carrier changes the optical squared-frequency
coefficient. Spectral k is independently defined by the dimer
translation eigenvalue z on this linear sector. It is periodic modulo
2 pi, with inversion sending k to -k, and needs no source readout.
It does not give an additive native collision momentum or an inertial
mass. Deriving an exchange law with a calibrated momentum observable,
or a mapping to the D3 characteristic, needs additional evidence.

## Exact finite native checks and falsifiers

Use the 8 by 20 native torus in initial matching color zero. Launch
one material rail in column 0 and a simultaneous, uniform reference
in column 4. No radiation is present. Evaluate z in `{1,-1,rho,rho^-1}`,
all of which obey `z^10=1`. Use uniform and optical vectors at 1 and
two coordinate basis vectors at each of the other three roots. Both
the target and the reference use initial common scale 2^8. For eight
single steps, every target word before step t is divisible by at
least `2^(9-t)`, by the 2-denominator of each accepted pair's matrix.
The checker also checks every target contact's actual parity, each
complete C/B state against the symbol prediction, each full inverse and
the full native accounts. At every even cut divide the chosen column-0
entry by the co-evolved column-4 entry with the same row. Report exact
cyclotomic ratios, including both rest eigenratios, both staggered basis
ratios, and the two generic roots and their inverse comparison.
A failed admitted comparison, trace, determinant, scalar crossing,
or ratio is a recorded negative result. Ill-typed preparations and
native account/inverse failures are integrity failures. The test makes
no indefinitely admissible generic integer-wave or physical mass claim.
