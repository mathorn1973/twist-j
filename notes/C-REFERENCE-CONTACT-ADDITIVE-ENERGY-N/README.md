# Reference contact and complete energy accounts

**PUBLIC / NON-CANONICAL / L1.** A. M. Thorn. Claim
[#1622](https://github.com/mathorn1973/twist-j/issues/1622).
Analytical successor to
[#1621](https://github.com/mathorn1973/twist-j/pull/1621).
No Canon promotion or new scientific executable.

The same reference-reading contact can conserve different energy accounts
on exactly the same complete state. What matters is which interactions
the account includes. The source's square-price theorem remains correct
for its declared two-edge star.

For the same three cells define

\[
\mathcal E_{\kappa,\eta}
=D_\kappa(h_1,h_0)+D_\kappa(h_2,h_0)
+\eta D_\kappa(h_1,h_2),
\quad D_\kappa(x,y)=2\sum_j f_\kappa(x_j-y_j),
\]

where f(0)=0, f(+-1)=1, f(+-2)=kappa>0 and eta>=0.
The fixed contact T0 exchanges
(rho,rho+(2,0),rho) with
(rho,rho+(1,1),rho+(1,1)), and fixes all other states.

| Question | Exact result | Proof |
| --- | --- | --- |
| Which full accounts does the same T0 conserve? | Precisely kappa(1+eta)=4. The square star (4,0) and equal-edge triangle (2,1) have the same frozen calibration but differ elsewhere. | section 2 |
| What would one further contact decide? | For the separately supplied T1=S01 T0 S01, conservation also requires kappa=1+eta. Together they select (2,1) within this family. | section 3 |
| Can the energy instead be a common one-cell price on each signal plus a fixed reference account? | Conservation for all reference contents forces that one-cell price to be constant. Pair interactions, different readings and restricted preparations are outside this no-go. | section 4 |
| What would preserve the square price with all three edges? | A separately priced store must receive +8 on T0's forward branch and return it on the inverse. T0 itself has no such changing coordinate. | section 5 |
| Does minimum contact size select the square? | In the separate prepared star class, kappa=p/q reduced has minimum ceil(max(p,q)/2) signal blocks and minimum common account 2p. Eight prices, including 4, require exactly two blocks. | section 6 |

These are full-carrier proofs, including fixed branches and actual
checkpoint reconstruction. The finite maximum argument and integer
count bounds need no enumeration. The separately supplied contacts
commute with original continuation, but that fact does not make them
steps executed by original U.

The next physical task is concrete: establish which contact operations
and pair interactions actually occur, and supply the independently
priced reference/store update when required. Account symmetry alone
does not establish symmetry of the device. Neither the graph nor its
weights nor the comparison contact T1 is admitted as native here.

Read [PROOF.md](PROOF.md) for the derivations and exact limits,
[CONTRACT.md](CONTRACT.md) and [SOURCES.md](SOURCES.md) for the public
pin and inheritance, [REVIEW.md](REVIEW.md) for same-session analytical
review, and [CHECKS.md](CHECKS.md) for validation provenance. The pin was
made after manual discovery and before the final proof; this is not a
blind preregistration or external independent confirmation. Canon v103
and the physical-energy and native-admission obligations remain open.
