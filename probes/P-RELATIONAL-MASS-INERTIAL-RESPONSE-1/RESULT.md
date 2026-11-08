# Result: the existing action does not supply a moving inertial branch

Status: PASS at the frozen exact-algebra audit; NON-CANONICAL, L1.
Analytical scope: candidate-T. Finite audit scope: candidate-C.
No physical inertial mass, native realization or Canon promotion.

The full Hamiltonian of #1689 already determines local dynamics for
nonzero total P. It does not select a unique moving bound-state energy.
The failure is more specific than a missing calculation:

| Question | Exact conclusion |
| --- | --- |
| Same action and complete initial state | Unique local flow on G SPD, rho+/-P nonzero |
| Retain the old constant elliptic internal j | Impossible on an interval with P!=0 |
| Fix full J=J*, minimize energy | Infimum is 10 at P=0, zero and unattained for every P!=0 |
| Fix full elliptic J and P!=0 locally | No constrained critical point or local energy minimum |
| Continue the rest affine relative equilibrium | No affine relative equilibrium on that moving level |
| Fix internal initial witness and expand energy | Hessian diag(1/6,0), rank one |
| Keep same rest point, P path and full J but allow preparation sections | Every real energy quadratic coefficient is possible |
| Fix rest initial data and observe center over old period | Mean displacement derivative diag(1/12,1/24) |

## Sharp falsifiers

For the same exact full charge J*=[[0,4],[-2,0]], the fixed-internal
preparation gives H(s e1)=4+sqrt(36+s^2), but H(s e2)=10 for |s|<6.
A forced positive isotropic instantaneous inertia is false.

More strongly, the smooth same-rest-point initial sections (PROOF.md (7))
have H_c=10+(2c+1/12)epsilon^2+O(epsilon^4) for every real c, while
P=epsilon e1 and full J=J* exactly. Thus charges and rest point do not even
fix the sign of the preparation energy curvature. These are not proved
stable moving branches, and no negative physical mass is inferred.

The exact full-charge low-energy family (PROOF.md (10)) gives
H=s sqrt(epsilon^2+16)+3s^2 for every epsilon!=0 and s>0. At epsilon=3,
s=1/4 it has H=23/16<10. As s->0 the energy tends to zero without attaining
it. The proof extends to every nonzero P by the centralizer of J*.
These competitor states are not claimed to generate complete bound flows.

## First exact execution

The six-file prospective pin 95d108a75a87f9ad2f11f382aed4104c85e0a05e was
pushed and every file read back through the public repository API before
execution. Full text and Git blob identities matched the prepared bytes.
The worktree was clean at the exact pin.

The first run on Linux aarch64, Python 3.11.2, completed in 0.777 seconds:
exit 0, empty stderr, 178-byte stdout, RESULT=PASS. Its SHA-256 is
00438d53106d8694d43841f11e049472c67f6307fe8c08b379f1904c7349ce77.
All 24 field cases, 54 Hessian directions, six energy witnesses, three
preparation sections, four mean/phase identities, 12 low-energy cases and
seven negative controls passed. No corrective scientific rerun occurred.
All six prospective files remain unchanged. EXPECTED.txt is the exact
captured stdout. RUN.md records the historical first execution.

The required public x86_64/aarch64 exact-head workflow is a separate merge
gate; its current outcome belongs to the PR. It does not change this first
run record. The verifier is one implementation comparing automatic
derivatives and explicit equations; no second independent program is claimed.

## Additional assumptions, precisely separated

To make a finite-time response unique, supply the preparation section,
phase/scale/origin comparison, time interval and observable. The unchanged
action then determines it. Its second-order preparation data suffice for
the quadratic energy coefficient.

To define a bound-state mass by energy curvature, one additionally needs
a separately justified smooth, unique and stable moving bound family and
its intrinsic constraints and reference momentum norm. The old fixed-J
minimization and affine relative-equilibrium mechanisms fail here; declaring
a preparation section does not create such a family. Positive definite
curvature would give a mathematical mass tensor. Scalar isotropy and the
physical momentum/velocity/force and time/energy identifications require
further justification.

The finite-period response is a positive result at a specified observable,
not a replacement dispersion law. If one chooses the period-averaged inverse
metric, its ratio is 18. That number is not identified with physical mass
or the rest energy 10. No arbitrary moving binding or completeness theorem
is claimed. The prior rest-sector binding result remains intact.
