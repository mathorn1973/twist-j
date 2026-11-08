# P-SOURCE-PHASE-NATIVE-1 preregistration

Status: FORMAL PREREGISTRATION / RESULT-EXPOSED / L1 ONLY.
Candidate: `C-SOURCE-PHASE-NATIVE-1`.
Owner: A. M. Thorn, Codex-source-phase-native-20261024.
Date: 2026-10-24.
Public claim: [issue #1738](https://github.com/mathorn1973/twist-j/issues/1738).
Branch: `probe/P-SOURCE-PHASE-NATIVE-1`.

## Authority, exposure and prospective custody

The authority is ACTIVE Public Canon v105, public main
`892a0b11089d34e241e1eb76d2c03247022d18e6`, content
`b8cdfd6ea58ae798545bc6000c817147fa0f0dcc`, tag `canon-v105`.
The canonical Git bytes of CANON.md have length 1295029 and SHA256
`73894f331dac3226fe30c86f1ccd893bc2761b0220557e0bfb374d049aa2fa31`.
The declared content and tag are ancestors of main. Its x86_64, aarch64 and
aggregate checks passed. Open issues, local probes and registry and 290
explicit remote heads were scanned before claiming this identifier.

This is a source/phase/memory continuation in the thematic scope of closed
[issue #866](https://github.com/mathorn1973/twist-j/issues/866).
It neither reuses nor reopens P-U-PREPARATION-EVENT-RECORD-1.
The chosen construction and its analytical answers are already exposed.
Earlier exploratory computations are not preregistered public evidence.
This fresh accepted verifier has not been imported or executed before its
public pin. Source inspection and static syntax checks are permitted before
pinning. This is an exact construction audit, not a blind empirical test.

Commit this preregistration, the fresh self-contained verify.py and the
complete proposal directory named below in one fresh public commit; push
and read back their exact bytes before the first scientific execution.
RUN.md will identify that immutable commit and every accepted file hash.
No amendment, rebase, squash or force push is allowed after the pin.
A defect in accepted code or a fired mathematical falsifier must be
recorded, not repaired under the same frozen identifier.

The proposal at
[notes/canon/C-SOURCE-PHASE-NATIVE-1/PROPOSAL.md](../../notes/canon/C-SOURCE-PHASE-NATIVE-1/PROPOSAL.md)
contains the complete definitions and analytical candidate proofs.
The notes and their proposed T rows assign no current Canon status.
Independent theorem-grade review remains outstanding.

## Field 1: equations and predicted exact outcomes

Let t=zeta20, O=Z[t]/(t^8-t^6+t^4-t^2+1), i=t^5 and zeta=t^4.
Coefficients use the fixed basis 1,t,...,t^7. Set
M=I+2iX and channel displacements
(-1,0),(0,-1),(0,1),(1,0). On finite-support four-channel fields,

    (Aa)_(x,c)=g(x) sum_d (M tensor M)_(c,d) a_(x-delta_c,d),
    g(R,r)=zeta^(-1) if r=0, and 1 otherwise.
    W=A/5, p=1+2i, A_LC=p^2 A, W_LC=A_LC/25.

The predicted Gram gains are 25 and 625. The amplitude maps are
automorphisms over O[1/5]. Raw multiplication by A is injective but not onto
the integral direct sum. Initial unit-state normalization is one fixed
scalar 1/||a_0|| in the complex reading, never per-port normalization or a
change to the raw residue representative.

The two ring maps rho_j:t->j in F5, j=2,3, yield

    rho_2(M tensor M)=h h^T, h=(1,-1,-1,1)^T,
    q_x=h^T rho_2(a_x), q'=Adj q,
    epsilon_k=4^(-k) q_k, epsilon_(k+1)=B epsilon_k,
    B=4 Adj,
    rho_3(M tensor M)=e e^T, e=(1,1,1,1)^T,
    rho_3(p^2)=4, q_x^+=e^T rho_3(a_x), q^{+prime}=B q^+.

Use the actual native g_j, J_n and initial antecedents explicitly given in
the frozen proposal and separately transcribed in verify.py. The raw
macrostep occurs when n+1 is divisible by three. Its first occurrence is
2->3. The candidate identity is Pi_loc U_tilde=U_net Pi_loc for all ticks,
with separate full-sheet and reachable-sheet statements and the
time-dependent vacuum specified in the proposal.

For the residue carrier F5[u,u^-1,v,v^-1], B is multiplication by

    b=4(u+u^-1+v+v^-1)=4(uv)^-1(u+v)(uv+1).

It is injective on this domain; evaluation at (1,-1) shows that 1 has no
finite-support preimage. For N=5^m the characteristic-five Frobenius identity
predicts the complete impulse profile

    B^N delta_0=4(delta_(N,0)+delta_(-N,0)+delta_(0,N)+delta_(0,-N)).

This is a claim about residue labels, not amplitudes over Z or O.
The four extreme coefficients at every positive k are 4^k in F5.
The special profiles occur at microscopic times 3*5^m.

For R=F5[u,u^-1], the formal Laurent-series extension R((v)) has a common
lower bound in v and finite Laurent-polynomial coefficients in u. There,

    b^-1=4v sum_(j>=0) [-(u+u^-1)v-v^2]^j.

This specifies an oriented extension, not an inverse on all bilateral
configurations. The latter have the nonzero kernel (-1)^R. In characteristic
zero the coefficient of (4 Adj)^5 delta_0 at (3,0) is 25*4^5=25600, so the
four-point conclusion cannot be transported unchanged to characteristic zero.
If the real averaging operator Adj/4 is chosen instead, that coefficient
is 25/1024; this is a different normalization of the same counterexample.

## Field 2: accepted code and execution

The only executable scientific input is [verify.py](verify.py), written with
the Python standard library and exact integer/rational arithmetic. No
legacy helper, external dataset, random generator, mutable service or
precomputed output is read. It writes no files and performs no network or
subprocess operations. It uses explicit fixed data in its source.

The exact accepted command, run from the clean repository root after
public pin verification, is

    python3 probes/P-SOURCE-PHASE-NATIVE-1/verify.py

The initial execution uses Linux Python 3.12 with a 600-second process
ceiling and neutral environment LC_ALL=C, LANG=C, TZ=UTC,
PYTHONHASHSEED=0 and PYTHONDONTWRITEBYTECODE=1.
All exact stdout bytes and stderr bytes are captured separately.
EXPECTED.txt is created from the actual first completed scientific stdout,
not copied from earlier exploratory output. RUN.md records the pin,
file hashes, command, platform, architecture, Python, exit code, bytes,
line count and SHA256 identities. The unchanged pinned code is then replayed
by the existing x86_64 and aarch64 pull-request jobs.

## Field 3: carrier, data and finite audit boundary

The complex-amplitude source is the declared integral direct sum over O,
with localization only for the amplitude reading; the native field is the
finite-support direct sum over F5 on the infinite lattice Z^2.
No finite periodic box substitutes for that lattice. All support
dictionaries remove exact zero entries.

The accepted finite ranges and fixtures are fixed by verify.py and are
listed below before the public pin. No range or input may be selected after
seeing a formal result.

1. The eight-element integral basis of O; all 64 ordered pairs for star
   multiplication and both residue homomorphisms; declared root/phase laws.
   Both row and column four-by-four Gram matrices have squared gains 25/625.
2. Eight source fields F0,...,F7. Keys below are (R,r,c); absent ports are zero:
   - F0={(0,0,0):1}.
   - F1={(0,0,2):1}.
   - F2={(0,-1,2):t, (0,1,1):1+t^3}.
   - F3={(1,0,3):i, (-1,1,0):2-t}.
   - F4={(0,0,0):1, (0,0,1):t, (0,0,2):t^2, (0,0,3):t^3}.
   - F5={(0,2,1):-2, (0,0,0):1+2i}.
   - F6={} (the algebraic zero field).
   - F7={(0,0,0):5} (a nonzero field with both residue fields zero).
   For every field and both phase variants, four raw macrosteps test the
   port reduction, scalar adjacency law, full exact norm gain and retained
   phase. Two specific coefficients test target contact:
   (A F1)_(0,1,2)=1 and (A F2)_(0,0,2)=zeta^(-1)t.
3. All 25 (q,z) pairs at each of the two residue places test the declared
   two-port preparation formulas.
4. All 3125 native chart labels, and all five antecedents per label, test
   initial sheet and F3 and exhaust all 15625 native heads. Chart inverse
   and one-tick transport are tested at the 20 times
   3,...,15,31,32,63,64,255,256,1023.
5. Every one of the eight raw source fields, both phase variants and all
   15 microscopic transitions n=0,...,14 test the separately implemented
   native network against the projected raw update, including 2->3.
   F0,...,F5 use lambda=(1,2,3,4) at (0,0) and (4,0,2,1) at (1,-1),
   zero elsewhere. F6,F7 use lambda=0 everywhere and test the full vacuum.
   Zero is admitted algebraically; unit Hilbert reading requires nonzero
   input and is not applied to F6.
6. Residue impulse extreme fronts are checked for every k=1,...,125, with
   the entire four-point support compared at 1,5,25,125. Generic Laurent
   fifth powers check Frobenius for m=0,...,8, alongside the exact
   factorization and evaluation witness for the missing finite preimage.
7. The explicit formal inverse prefix has v degrees 1,...,32; its product
   with b must equal 1 through degree 31 and have a nonzero higher-degree
   remainder. The pointwise bilateral-kernel identity is checked at all
   81 coordinates in [-4,4]^2, with integer parity signs.
8. The characteristic-zero fifth power is separately multiplied with
   integer coefficients; its (3,0) coefficient must be 25600, versus zero
   after reduction modulo five.
9. The exact rational T tensor T example starts at (1,2,-1,3), N0=15,
   and checks k=0,...,12 using fixed initial normalization. Scaling the
   unit raw vector by five preserves its positive ray but changes its raw
   residue from 1 to 0. The weights from amplitudes (1,2) are computed
   before and after individual-port normalization and must disagree.
   The localized rational amplitude inverse is checked explicitly.

These are finite audit bounds and declared input fixtures, not a search
over all possible architectures. Expected output consists of the fifteen
ASCII lines in the accepted source, each terminated by one LF byte.
No total number of atomic comparisons is claimed.

The all-time proofs are separate mathematical arguments. This finite audit
cannot by itself establish an all-time theorem or certify every arbitrary
raw coefficient field. The full spatial/logarithmic/spectral statements in
the proposal are not silently included in this finite computational scope.

## Field 4: systematics, alternative carriers and negative controls

All equality comparisons are exact in the declared ring or field.
No floating tolerance, empirical fit, truncation of a complex amplitude or
renormalization of individual ports is admitted.

The implementation distinguishes the raw field from its residue and from
its normalized Hilbert reading, initial from target contact, the two
residue places, and the pre-update from post-update clock.
The series calculation checks a stated finite prefix, not an unspecified
infinite numerical summation. The analytic geometric-series proof supplies
the infinite statement.

Negative controls must preserve the following exposed counterexamples:
normalizing a positive ray does not preserve its chosen raw residue;
per-port normalization changes coherent weights; the unreduced integer
convolution does not have the four-point profile; the unit impulse is not
a finite-support image of B; all bilateral fields need not have injective B;
and the wrong residue place annihilates the full-phase numerator.

Same-session source and proof reviews are authoring checks, not external
independent scientific acceptance. A later independent adversarial review
must name its frozen inputs and identify whether it found a counterexample,
a bounded negative search, or a complete proof in a declared class.
No failure to find a witness proves an unrestricted absence.

## Field 5: failure thresholds and disposition

Every registered assertion must agree exactly. The allowed number of
mismatches, missing cases and failed negative controls is zero. A failure
raises an exception and produces nonzero exit status. A timeout, syntax
failure, missing fixture, nonzero exit, nonempty stderr or changed pinned
byte is an unsuccessful execution, never a pass. Preserve its actual record
and follow the repository's abandoned-pin or completed-result disposition
as applicable. Do not change the accepted verifier, threshold or proof
under this identifier to obtain agreement.

A completed pass has the deterministic ASCII/LF stdout specified by the
source, exit 0 and no stderr. The stdout is byte-identical on both required
architecture jobs, each using the same pinned verifier SHA256.
One-architecture agreement is finite computational evidence at most C.
Two-architecture agreement is a reproducibility gate, not independent
acceptance of an all-time proof.

Predicted negative witnesses are part of the successful conclusion; they
must not be suppressed as inconveniences. Any other counterexample to the
stated candidate is retained and narrows or defeats the corresponding
claim. The result does not assign a public scientific status or close a
Frontier item.

## Field 6: action layer and exclusions

All source, ring, operator, native-chart and residue assertions are
mathematical L1. The fixed carrier, coin, routing and coupling are declared
construction data. This work does not force them from J, equate the two
particle factors with a new spatial Dirac family, establish physical
transport or occurrence, derive an arrow of time, quantify hardware energy
or memory cost, or transfer to L2 through L6. No SI calibration is included.

The target public proposal remains NON-CANONICAL under notes/canon.
A future promotion dossier must carry the earned exact scope, actual
independent review, complete formal pins and outputs and the concrete
requested Canon changes. Such a dossier and a later authorized Canon fold
are distinct from this probe's setup and finite execution.
