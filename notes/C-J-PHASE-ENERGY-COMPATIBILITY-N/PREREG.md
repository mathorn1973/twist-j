# Phase, energy and kinematic mass: compatibility contract

PUBLIC / NON-CANONICAL / L1. Candidate C-J-PHASE-ENERGY-COMPATIBILITY-N.
Owner: ChatGPT-phase-energy-compatibility-20261017. Author: A. M. Thorn.
SPDX-License-Identifier: Apache-2.0.
Reservation: https://github.com/mathorn1973/twist-j/issues/1603

## Authority and exposed provenance

Public Canon v103 main/tag dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d;
content 01fb76f6b3b14a6a5ec05d0017ea922390ab6f66; CANON.md SHA-256
d87657aeccc568dd668718fb9cbea6136643e5db32dd4e289a4de328e64f824b,
1052518 bytes. All normative hashes, ancestries and successful required
main run 39022927713 were checked. Collision inventory included 253 remote
heads, issues, probes and registry. No source is modified.

A uses #1585 at bb04eb3c582e2ec06f90b1a5768ecdfb1ac2044e,
source prereg pin a4ec92176c9f8ace9f884254e05d57a5466b84e0,
probes/P-FUNDED-AREA-PHASE-RECORD-1/PREREG.md and PROOF.md.
B uses DIRAC-STEP and DIRAC-STEP-THEOREMS at the stated Canon basis.
The complete normalized Fourier step below is an explicitly added comparison,
not a newly discovered native law. Two analytical assistants helped identify
the tests; they are not the independent reviewer.

These are exposed hypotheses, not blind predictions. #1404/#1420 already
separate stored energy from period, and #1418 already treats ambiguity of
continuous generators sampled at integer times. This work claims neither
result as new. Native-interface and physical-reading owners are unchanged.

## 1. Equations and claims to test

A. Complete state s=(q,p,u,v,b,sigma,eta,c) is in
Z^4 x N_0 x {+1,-1}^2 x C4, H=q^2+p^2+u^2+v^2, E=H+b.
Q_h changes q to q+h; P_h changes (p,u,v) to (p+h,u+hq,v+hq).
For requested (axis,epsilon), h=epsilon sigma. Accept if b>=Delta H,
refund/pay b'=b-Delta H, otherwise keep integers and bank and flip sigma.
The controller requests Q+, P_eta, Q-, P_-eta at c=0,1,2,3,
respectively, then increments c modulo four. This defines T.
Define a(s)=q(p(Ts)-p(s)) modulo 5 from actual motion, including rejection.

For any finite permutation with conserved E, test the exact equivalence

    a(s)=kappa E(s)+beta+chi(Ts)-chi(s) in F5
    iff sum_C a = |C| (kappa E(C)+beta) for every complete orbit C.

For the source, seek all universal (kappa,beta) on the whole carrier.
Expected obstruction: a is a state difference, so complete cycles have zero
sum; explicit low-energy orbits force kappa=beta=0. Test also just the
prepared orbits from (0,0,1,-1,B,1,1,0) at B=0 and B=4.
No identification of this area scalar with the full open-path Weyl operator
or with a physical temporal phase is assumed.

B. For m>0 let D_m(k)=diag(exp(ik),exp(-ik))(I+i m X) and explicitly
define W_m=D_m/sqrt(1+m^2). On its positive principal eigenphase band,
test cos(omega)=cos(k)/sqrt(1+m^2), omega(0)=atan(m), omega''(0)=1/m.
For common A,B>0, E_phase=A omega, p_phase=B k and c=A/B fixed by the
massless branch, compare inverse curvature M_curv=1/E_phase''(p=0)
with E_phase(0)/c^2. Expected ratio m/atan(m)>1.
M_curv is only the defined dispersion-curvature quantity, not measured
force-response inertia. No varying energy offset or m-dependent clock fits.

Test the positive alternative Ehat=sqrt(1+m^2) sin(omega), phat=sin(k):
Ehat^2-phat^2=m^2 and omega'(k)=phat/Ehat=dEhat/dphat on a local chart.
Test global phase loss at k and pi-k. Derive the weak-step rest limit
m=epsilon M and its integral error bound. This is an additional family,
not native coarse-graining or a repair of the fixed declared rung m=2.

## 2. Code and pre-execution freeze

audit.py will implement A using integer arithmetic and the Python standard
library only. It will not import the source verifier or read runtime files.
B is an analytic proof, not a numerical fit or numerical derivative test.
No new scientific code has run. Static syntax and security checks only are
allowed before the complete source pin. PREREG.md, PROOF.md and audit.py
will be committed, pushed and read back before the first audit execution.
They then remain unchanged. Any failed conclusion is retained, not repaired
by changing a threshold. Record exact pin, source hashes, command, UTC times,
OS, architecture, Python, stdout/stderr bytes and hashes in RUN.md.

## 3. Complete finite inventory and analytic domain

Enumerate every complete source state with E<=6: coordinates in [-2,2]^4,
H<=6, b=0..6-H, both signs sigma/eta and all four c. Every state is
included because each coordinate square is <=6. Check conserved E, both
inverse compositions and a=Delta u=Delta v at every state. Partition this
entire finite carrier into full cycles; test each cycle's zero area sum.
Enumerate all 25 (kappa,beta) in F5 against every cycle constraint.
Separately print full periods, conserved E and area sums for the E=0 and
E=1 zero-bank witnesses and cold B=0 and B=4 preparations. The expected
allowed pairs are only (0,0), both globally and for the two cold orbits.
Counts are reported, not chosen as pass criteria. The universal conclusion
depends on the written proof, not extrapolation from this inventory.

B has all real k and m>0 on omega in (0,pi); curvature is local at k=0.
The exact rest error bound is for epsilon,M>0. No measured input is used.

## 4. Systematics and excluded scope

A is modulo five, for the full energy account including records and bank.
It does not forbid a U(1) lift, a different energy reading, a selected
subcarrier, a different clock, or a separately established dynamical phase.
Complete-state return differs from return of the base q,p alone.
B uses a chosen normalization and linear phase readings. Nonlinear readings
can satisfy other conditions. Universal calibration means the same A,B
for the massive branch and its massless speed reference. The two tests are
on different constructions; no common native carrier is supplied by them.

## 5. Falsifiers and execution

An exact counterexample to the cycle criterion, witness, derivative, shell
or bound rejects the affected claim. An allowed nonzero (kappa,beta) in the
declared finite inventory rejects the corresponding expected audit result.
audit.py reports every scientific test as PASS/FAIL, ends AUDIT PASS/FAIL,
and exits zero even for a scientific failure. Exceptions, timeout, nonzero
exit or nonempty stderr are execution failures, not scientific evidence.
Run once from the clean source pin with LC_ALL=C LANG=C TZ=UTC,
PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1 and a 60-second limit:

    python3 notes/C-J-PHASE-ENERGY-COMPATIBILITY-N/audit.py

Capture outputs outside the repository; retain exact short stdout in RUN.md
with bytes/hash. No unapproved raw transcript file is committed.

## 6. Action layer, review and promotion

L1 conditional mathematical comparisons only. Authored claims have ceiling
candidate-T; finite audit ceiling candidate-C. An independent agent will
freeze an analytical attack contract in Git before seeing the author's
PROOF.md or audit.py, then provide a scoped review through Git. This is a
separate agent within the same assistant system, not external peer review.
Notes CI does not execute audit.py and is not a two-architecture scientific
reproduction. No Canon change, native/physical admission, merge or release.
