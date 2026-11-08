# Předem stanovená algebraická kontrola spojení se spektrem W

Task: LOCAL-C-W-SPECTRUM-APPARATUS-1. Status LOCAL / NON-CANONICAL / L1.
The obsolete attachments are outside this continuation. Previously frozen
packages are read-only inputs. No new scientific executable has been run
before this specification. Analytical derivation and independent proof
review are separate from the finite exact audit below.

## Fixed operator and universal claims

On ell2(Z_R x Z_r) tensor C4, W=Gamma S G, contact after streaming,
G=((I+2iX) tensor (I+2iX))/5, Gamma=I+(exp(-ig)-1)V, g=2pi/5.
The free symbol is diag(z,w,w^-1,z^-1)G.

The analytical proof must establish a common gap for the ENTIRE contact
W, an exponentially decaying exact logarithm H, a finite-capacity
continuous-spectrum battery lift of the actual kick, and a controlled
connection to the original finite packet response. It must distinguish
finite energy capacity from finite Hilbert dimension, exponential tails
from strictly finite range, a nominated coherent battery from a derived
preparation, and a one-shot unitary from an internal stopping mechanism.
No finite audit is taken as proof of any infinite-spectrum assertion.

## Exact checks (fixed, no parameter search)

Use Gaussian rational arithmetic and formal Laurent polynomials only.
No floating-point pass decision, finite-volume spectrum, fitted gap,
sampled momenta, grid approximation of energy, or adjusted tolerance.

1. Form the WHOLE 4 by 4 matrix G from its tensor factors, not from the
   expected characteristic coefficients. Check G*G=I and det(G)=1.
2. Form the formal Laurent matrix Wf=diag(z,w,w^-1,z^-1)G. Check its
   symbolic unitarity (conjugation sends z,w to their inverses) and
   its entire characteristic polynomial:

       det(lambda I-Wf)=lambda^4-a lambda^3+b lambda^2-a lambda+1,
       a=(z+z^-1+w+w^-1)/5,
       b=((z+z^-1)(w+w^-1)-6)/5.

3. With A=(1,0,0,-1) and S=(1,0,0,1), check GA=A and
   (S*GS)/(S*S)=-3/5. Normalization square roots are unnecessary.
4. From the rational half-angle parameter 1/2 compute cos(b)=3/5,
   sin(b)=4/5, cos(delta)=7/25 where delta=pi-2b.
   Check the exact sign certificate

       5-(1+4*(7/25))^2=316/625>0.

   Together with the stated angle intervals, this proves
   cos(2pi/5)=(sqrt(5)-1)/4>7/25 and delta>2pi/5.
5. Record beta_lower=3(1+sqrt(5))/80 from the proven spectral argument.
   The finite audit verifies its algebraic coefficient conversion from
   (3/20)cos(pi/5), not the spectral inequality itself.

## Independent implementations and immutable first attempts

The root implementation uses a generic Leibniz determinant over sparse
Gaussian-rational Laurent polynomials. A separate author implements the
same identities independently, preferably using traces/Newton identities,
without reading the root code, outputs, or certificate before its first run.
Both follow CERTIFICATE_SCHEMA.md and are SHA-256 frozen before either
is executed. Both first attempts retain source hash, exact command,
timestamps, stdout, stderr and return code. Repairs require a new source
filename and a new recorded attempt; earlier evidence is never overwritten.

Passing requires both identity checks to succeed and their canonical JSON
certificates to be byte-identical. Shared Python standard libraries and
the mathematical specification are declared; no cross-architecture or
public CI admission is claimed. The proof review remains necessary even
after a passing finite audit.

## Falsifiers and fixed scope

Any nonzero symbolic remainder, failed exact sign, wrong contact/phase
convention, unsupported full-operator locality claim, mismatch between
certificates, or missing energy-boundary sector is a failure of the
corresponding claim. A positive global gap is an inclusion theorem, not
an assertion that the two enclosing arcs are the exact contact spectrum.
Work must use V*HV-H on the actual state, including its scattering
component; no silent projection onto the bound branch is permitted.
