# PREREG: J/phi ramified area and Weyl covariance

PUBLIC / NON-CANONICAL / L1.
Probe: P-J-RAMIFIED-AREA-WEYL-1.
Owner: ChatGPT-j-area-weyl-20261017, A. M. Thorn.
Reservation: https://github.com/mathorn1973/twist-j/issues/1582
License: Apache-2.0.
Authority: Public Canon v103, main dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d, content commit 01fb76f6b3b14a6a5ec05d0017ea922390ab6f66, Canon SHA-256 d87657aeccc568dd668718fb9cbea6136643e5db32dd4e289a4de328e64f824b, 1052518 bytes.
No Canon, Registry, Frontier, GATES, policy, workflow, previous probe or previous notes edits.

## 1. Equation (frozen before execution)

Fix O=Z[j] with j^4+j^3+j^2+j+1=0 and j^5=1,
J=1+j^2 and phi=-j^2-j^3. Thus J*phi=j.

Define on O^2 the **chosen** alternating O-bilinear form

  omega((a,b),(c,d))=ad-bc

and the invertible O-linear marked pair step

  T(a,b)=(Ja,phi b).

Gate G2: omega(Tu,Tv)=j omega(u,v) for all u,v, hence omega(T^5u,T^5v)=omega(u,v); exact one-step preservation is false. This is a conformal, fifth-order phase covariance, NOT a stepwise invariant real action.

At the distinguished ramified prime p=(1-j) the residue ring O/p is F5. Let rho(sum a_k j^k)=sum a_k mod 5. Gate G1/G3: rho(j)=1, rho(J)=2, rho(phi)=3; rho(T)=A=diag(2,3), det(A)=1 in F5, and omega(Au,Av)=omega(u,v) for all u,v in F5^2. The map rho erases the *complex* phase j; it is NOT itself a complex phase readout.

On the **chosen**, explicitly additional 5-state complex Weyl carrier (basis labelled k in F5), set
Z|k>=j^k|k>, X|k>=|k+1>, W(a,b)=Z^a X^b and D|k>=|3k>.
Gate G4: D Z D^-1=Z^2, D X D^-1=X^3, D W(a,b) D^-1=W(2a,3b);
W(u)W(v)=j^omega(u,v) W(v)W(u) for every u,v in F5^2.
The last equation invokes the **selected additive character** chi_1(t)=j^t; it does not arise by mapping the residue j through rho.

Gate G5: all four faithful additive characters chi_t(a)=j^(t a) for t in F5^* are distinct and A-area-invariant. No physical phase-orientation selector is inferred from their coexistence. In the marked principal embedding j is already distinguished, so this is a reader-class comparison, not a rejection of the algebraic axiom.

Gate G6: the entire rational diagonal cost class fixed by conjugation under D is exactly
H=diag(h0,h1,h1,h1,h1), h0,h1 in Q. If a diagonal H also commutes with X (and Z), it must be scalar. Positive nonconstant D-invariant gap examples 1 and 2 prove that this algebra alone cannot force a nonzero energy unit, an action quantum or SI hbar.

## 2. Accepted code

Only probes/P-J-RAMIFIED-AREA-WEYL-1/verify.py is accepted. Python standard library only.
Ring arithmetic is exact four-integer reduction modulo Phi_5, with no approximation.
The verifier audits all 16 ring-basis products for residue consistency, all 64 ordered O^2-basis pairs for each bilinear relation, 625 ordered F5 vector pairs for alternating invariance, all 25 Weyl conjugations, all 625 ordered Weyl commutator pairs, four characters on 625 pairs each, and all 5^5 diagonal cost vectors on {-2,-1,0,1,2}. These finite audits do not alone establish universality of the infinite-ring and rational-energy claims; the accompanying algebraic proof must do so.

All scientific statements, thresholds, code and counting domains are frozen here BEFORE first formal verifier execution. Static parsing, compilation and source/security review may precede the immutable pin; **no formal scientific execution or dry run may precede it**.
Commit/push PREREG.md and verify.py; then publicly read both back and record the immutable commit and both SHA-256 hashes. No changes after the pin.

## 3. Carrier, source and data

L1 carriers: O^2 (infinite integer rank eight), marked residue F5^2, five-dimensional abstract Weyl module with monomial operators, and rational diagonal costs. The exact finite fixtures above are generated deterministically in verify.py. No external datasets, numerical constants, measurements, clock input, stochastic events, network calls or file reads. Runtime source authority is the pinned verify.py alone. Public inherited facts: J-PROJECTIONS [T], J-GOLDEN-BRIDGE [T], FORCE-WEYL-HOLONOMY [T], KERNEL-WEDGE-COUPLING [T]. Earlier #1419 integer phase/energy contact and #1576-#1580 phase/readout work have distinct scopes; none is resumed.

## 4. Systematics / known negative controls

The O-valued omega is multiplied by j at ONE step, rather than preserved: a failure of one-step symplecticity is intended, not repaired. Over the residue rho(j)=1, so an assertion that reduction transports a nontrivial complex phase is false. The Weyl module and D are chosen algebraic representations, not a compiled original native U step. A D-invariant nonzero excitation gap remains selectable, so an hbar derivation from area covariance alone is excluded at this precise class scope, without excluding other physical decoders. Results stay within L1; no unnamed lifts to L2-L6, no Planck-scale or electron-mass fit, and no claim that a photon is physically identified.

## 5. Failure threshold and execution

Each named gate G1-G6 is a universal exact identity or exhaustive finite test, with tolerance zero. A single wrong identity, source/ring reduction, finite pair, full carrier inverse, conjugation, central phase, character count or cost classification fires its falsifier. A scientific falsifier emits FALSIFIER / AUDIT FAIL, exit 0, no PASS. A runtime exception, changed source hash, nonzero process exit, nonempty stderr or timeout is an execution failure, not an earned result. Do not repair the pin or move thresholds after running.

First command from a local directory containing the byte-identical pinned verifier, with environment LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1:
python3 verify.py

After the completed local scientific run, record exact stdout in EXPECTED.txt and neutral platform/architecture/Python/exit/stderr/hash fields in RUN.md, plus the status/scope in RESULT.md. Open a single-probe draft PR. Required x86_64 and aarch64 checks must compare the same verifier hash and stdout to EXPECTED.txt. An x86_64 local run alone is only reproduction, not the two-architecture computation gate. One-session authored proof is not independent external review.

## 6. Action layer and promotion ceiling

L1 ONLY. No source-preparation, energy-contact, physical apparatus, native U realization, action S, h/hbar, physical frequency or SI calibration claim. Candidate-T exact algebraic proof, candidate-C local execution, non-canonical until independent review and lawful fold. METRO-EDGE-SCALE [O] and the existing physical apparatus/native contact owners remain OPEN. A successor physical bridging probe requires a new owner, typed complete contact, energy and phase observables, independent choice rule, and named cross-layer gates.
