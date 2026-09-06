# P-U-NATIVE-MEMORY-EVENT-1 preregistration

Status: FORMAL PREREGISTRATION / RESULT-EXPOSED / PROOF-FIRST / L1 ONLY.
Owner: A. M. Thorn, Codex-native-event-20260906. Date: 2026-09-06.
Public claim: [issue #862](https://github.com/mathorn1973/twist-j/issues/862).
Branch: `probe/P-U-NATIVE-MEMORY-EVENT-1`.
Directory: `probes/P-U-NATIVE-MEMORY-EVENT-1/`.

## Authority, prior exposure and prospective pin

Public authority is ACTIVE Public Canon v78, public main
`5de2e71f4000e02599919bf3dcb18c7671b67445`, content commit
`767b136713ae12f5f30869642852dcb8a3f671b0`, tag `canon-v78`.
CANON.md is 473631 bytes with SHA-256
`82b29c75eb007c71d73dc33e63270d0e0895fdf41886499fcf79b928826855b5`.
The tag and declared content commit are ancestors of main, all five normative
hashes match, and required main workflow 34024518651 passed both architecture
jobs and aggregate check. Local policy, Canon, ledger and gate-contract
checks passed. Open issues, registry, probes and explicit remote heads were
scanned; the new identifier has no collision. Issue #861 is the completed
incubation, not a sealed formal probe being resumed. P-QDD-U-NATIVE-READBACK-1
is inherited public evidence; U-INDUCED-2 and NULL-ANATOMY remain separate.

All proposed results are exposed. The public NON-CANONICAL incubation
`C-U-NATIVE-MEMORY-EVENT-N`, issue #861, froze its preregistration at
`9eef145d285325f2b3b48efcc740adf04d574632`, SHA-256
`912f0c3f7897a3d0684ea8618da0d8775c7e6d9f01c52c2b4c1dbf3b42a8bcef`.
It froze its proof and code at `164da1efcf5222d934ffe3b22c32baf01b9cceaf`.
Its verifier SHA-256 was
`bcfc0cc415bcf8b8e2398f7d3ce63929275533ec8a91888b6d428ebddf04f459`.
Its inspected Linux x86_64 run passed 463333 exact comparisons and produced
20271 stdout bytes, SHA-256
`76ec658b7b1c4860952898db5d999b7d0d1987efedbd9ee2482dc77a8c457e09`.
The complete incubation result is preserved at
`8d94058055eaeb03f9e854f1ac64fac768ec2529`. The frozen source identity for
the mathematical input is the immutable code/proof pin above, not a mutable
summary. No incubation stdout is substituted for the new formal run.

This formal verifier adapts the exposed incubation implementation, changing
only its identifier and provenance text. It is not a new blind implementation
and not blind independent confirmation. All mathematical functions and
finite domains remain identical. The accepted formal verifier has not been
executed or imported before its new formal pin; only static parsing and
comparison precede it. The written proofs were independently reviewed by
a second collaborator in the same session; that is review, not blind evidence.

Freeze PREREG.md, PROOF.md, MEMORY-PROOF.md, CLOCK-PROOF.md,
FREQUENCY-PROOF.md and verify.py together in one fresh commit, push and
read back their exact bytes, and confirm a clean tree before the first
formal execution. The pin is never amended, rebased, squashed or force-pushed.
No Canon change or public theorem status is created by this preregistration.

## Field 1: equation and exact proposition

Use the unchanged native state `Omega=N0 x F5^6`, checkpoint
`x=(p1,p4,p1p,p4p,q,r)`, phase `z=sum(x) mod 5`, and

    theta_n = popcount(n) mod 2,
    U(n,x) = (n+1, g_((z+2*theta_n) mod 5)(x)),
    (g_0,g_1,g_2,g_3,g_4) = (a,b,c,d,e).

All checkpoint arithmetic is modulo five. The exact source formulas are

    a(x)=(p4,p1,p4p,p1p,q,r),
    b(x)=(-p1p,-p4p,-p1,-p4,-q,-r),
    c(x)=(-p1p+2,-p4p+1+r,-p1+2,-p4+1-r,1-q,-r),
    d(x)=(2-p1,1-p4,3-p1p,4-p4p,1-q,1-r),
    e(x)=(2-p1,1-p4,3-p1p,4-p4p,2-q,1-r).

On `X14={x:z in {1,4}}`, set `chi(1)=1`, `chi(4)=-1` and

    V(x)=(p1+p1p, p4+p4p,
          chi(z)*(p1-p1p-2), chi(z)*(p4-p4p-1)),
    R(x)={V(x),-V(x)}.

The proposed conjunction has separately audited components A-F:

A. `V(next)=-V(x)` for every X14 checkpoint and both bits. R has exactly
313 fibres, 312 of size 20 and one of size 10. These fibres are the complete
directed strongly connected components under both controls. All invariant
fixed checkpoint readers factor uniquely through R.

B. With `S(0)=0`, `S(m)=m-S(floor(m/2))`, define

    c_m=(m mod 5,S(m) mod 5,theta_m,theta_(m+1)),
    T0(r,s,u,v)=(2r,2r-s,u,1-u),
    T1(r,s,u,v)=(2r+1,2r+1-s,1-u,v),
    c_0=(0,0,0,1).

First two coordinates are reduced modulo five. The full 100-state alphabet
is reachable, strongly connected and aperiodic, with exact fixed-origin
letter density 1/150 for u=v and 1/75 otherwise. Stationarity is certified
by integer incoming sums. Explicit digit words give primitive M^77>0;
the exhaustive shorter-path audit predicts M^29 with minimum 1778335 and
row mass 536870912. The proof transports contraction on all dyadic blocks
to all prefix lengths. Samples do not prove this universal assertion.

C. Use the inherited five-label chart, `l=(alpha,beta,gamma,delta,epsilon)`:

    odd n=2m+1: t=1,h=(-1)^(1+u),N=s-1,z=4-3u,theta_n=1-u;
    even n=2m+2: t=-1,h=(-1)^(1+u),N=s-1,z=1+3u,theta_n=v;
    A=t*alpha,B=t*beta,C=2+h*gamma,D=1+h*delta,
    r=t*(epsilon+N),p1=3*(A+C),p1p=3*(A-C),
    p4=3*(B+D),p4p=3*(B-D),q=z-A-B-r.

This chart is inherited on native times n>=3. For nonzero first four labels,
checkpoint atoms are 20 copies of 1/20 and decorated atoms are ten copies
each of 1/60,2/60,3/60. For zero first four labels, checkpoint atoms are
10 copies of 1/10 and decorated atoms ten copies each of 1/30,2/30.
All 3125 labels are included; epsilon changes no weight multiset.

D. Classify all fixed readers by whole-atom partitions. Let F_D be all
rationals in [0,1] with reduced denominator at most D. Accepted LOW ratios
for the decorated class are exactly F_60 for a nonzero protected vector and
F_30 for the zero vector. Restricting acceptance to either driver bit gives
F_30 and F_15, respectively. Empty acceptance is UNDEFINED. Full unconditional,
checkpoint-only and bit-conditioned sets are stated in FREQUENCY-PROOF.
Only after computing all these sets compare all supported QDD head weights.
The eight predicted exclusions from the largest set are
`1/256,1/176,1/136,1/96,9/224,9/104,9/64,49/64`.

E. Every point of the native record fibre has positive limiting frequency
along each actual synchronized chart trajectory. Therefore a fixed checkpoint
reader eventually constant on such a trajectory was already constant on its
whole fibre. It cannot change permanently from BLANK to distinct WRITTEN
after synchronization under unchanged U.

F. The target-independent static encoder at z=1,r=0 in MEMORY-PROOF realizes
all 313 invariant messages. It does not recover QDD records lost in mergers.
Both the inherited first-tick collision with original LOW values 0 and 9/14,
and the synchronized same-R pair with current LOW 1/16 and 1/136, are checked.

## Field 2: accepted exact code

`verify.py` is self-contained Python standard-library code. It uses integers,
mod-five arithmetic and Fraction, with no floating point, random sampling,
external files, network, subprocesses or private imports. It writes only
deterministic ASCII scientific JSON to stdout, with one final LF.
Its accepted source is 25849 bytes, SHA-256
`61b84f7d6f9c02f74c2227b29ae43bd90c1253a8056ca2e0a1c4f37266797528`.

The frozen audit includes every one of 6250 X14 checkpoints and both bits;
the full graph/SCC comparison; all 313 static encoder roundtrips; all 100
clock states and all incoming stationary identities; literal Thue-Morse
and switch counts for every m from 0 through 65535; the four exact digit-word
identities and every row of the primitive integer power; all 3125 labels
and all clock atoms; native/chart agreement at every n from 3 through 34;
the first nine labels in lexicographic order at `2**127` and `10**100+123`;
the complete finite one-bin and two-bin whole-atom subset sums; all 624
supported piston tuples; and both exact QDD collision witnesses.

There are six required work packages and a predicted 463333 comparisons.
This is a count of exact comparisons, not independent experiments. A fully
completed audit reports PASS or FALSIFIED and exits zero; FALSIFIED retains
the mismatches. Exceptions or incomplete groups are STOP and exit nonzero.
The scientific disposition must distinguish a genuine theorem counterexample
from an implementation or reference defect.

## Field 3: carriers, readings and source

The checkpoint reader class is ALL maps `f:X14->A` for a finite alphabet A.
The decorated reader class is ALL maps
`f:X14 x {0,1}->{LOW,HIGH,SILENT}` evaluated at `(x_n,theta_n)`.
Equality is equality of the output symbols, and record equality is the
unordered sign quotient, not scaling equivalence. SILENT permits a fixed
present-state acceptance rule. Each atom is allocated whole to one symbol.
No absolute time, longer clock word, extra memory, context change,
intervention, reset, additional copies or changed dynamics belongs to this
class. It is not asserted complete as a physical apparatus class.

Both restrictions theta=0 and theta=1 are reported. The incubation used
Snap/Flow aliases without a specified bit assignment; the spectra are
identical for both bits and no unverified assignment is inferred. This
clarifies names without altering the mathematical domain.

Results classify each fixed orbit's possible frequencies. One common reader
need not realize arbitrary independent target choices on overlapping orbits.
No preparation ensemble average, physical measure, or choice after target
inspection is permitted as a substitute for the specified trajectory limit.

For QDD targets let `v=ell(p)` with `ell=(0,1,2,-2,-1)`, `s=sum(v)`,
`Q=sum(v_i^2)`. Supported LOW is `s^2/(4*(5Q-s^2))`. The denominator is
positive for every nonzero piston vector. Zero support is excluded from
normalized comparisons and is never divided by zero. There are 624
supported piston tuples and 15600 supported full heads. These rational
algebraic weights are inherited targets, not an adopted occurrence law.

The full native generator, synchronization, five-label chart and QDD source
is `probes/P-QDD-U-NATIVE-READBACK-1/PROOF.md` at the public main commit above. Its
proof is inherited as a mathematical lemma and its prior source statuses
are not promoted here. Canon is at its stated hash. Source bytes and hashes
are listed in PROOF.md. The accepted verifier makes no runtime source import.
No external dataset or third-party licensed material is introduced.

## Field 4: systematics and custody

The principal risks are a wrong sign or clock offset, confusing free-control
reachability with actual Thue-Morse recurrence, mistaking stationarity for
fixed-origin frequencies, splitting an atom to manufacture a desired weight,
claiming joint-reader existence from per-orbit membership, or calling a
prepared invariant label a writable apparatus. The independent algebraic
component proof, all-prefix contraction argument, exact chart audit, complete
whole-atom dynamic programs and explicit scope statements address them.

From the exact publicly fetched formal pin and a clean worktree, run from
the repository root on Linux or a Linux-compatible environment:

    python3 probes/P-U-NATIVE-MEMORY-EVENT-1/verify.py

Use `LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1`.
Capture stdout and stderr as separate bytes, require exit 0 and empty stderr,
record neutral OS/architecture/Python metadata and exact hashes in RUN.md,
and save the actual new stdout as EXPECTED.txt. Recheck pinned source bytes
after execution. Later commits add only run and result records, never adjust
the accepted mathematics, code, carrier or threshold. Required PR checks run
the same verifier on clean GitHub x86_64 and aarch64 Python 3.12 and compare
their output byte for byte to the one committed EXPECTED.

## Field 5: failure threshold and stop rules

Zero mathematical mismatches are tolerated. Any exact violation of the V
identity, claimed fibre/SCC classification, stationary or primitive certificate,
native/chart identity, complete atom spectra, support assertion, codebook
roundtrip or QDD witness falsifies its named component. Any omitted admitted
reader allocation or attainable excluded target falsifies completeness of
the corresponding stated spectrum. A genuine native trajectory and fixed
checkpoint reader with a permanent synchronized blank-to-written transition
falsify the no-write proposition. Every mathematical falsifier is retained.

Source or pin hash drift, an implementation defect, nonzero exit, nonempty
stderr, omitted group, hidden class expansion or cross-layer premise is
integrity STOP, not mathematical success. If no valid formal gate completes,
preserve the original pin and close the consumed identifier as ABANDONED
under POLICY; a corrected experiment requires a new identifier and pin.
If the gate completes with a mathematical falsifier, keep EXPECTED/RUN/RESULT
and preserve that negative instead of relabeling it abandoned.

## Field 6: action layer and explicit boundaries

L1 only. The proposed result combines positive native static storage with
negative permanent-writing and complete-QDD-frequency conclusions in the
frozen restricted reader class. The registered orbit-input QDD decoder
remains unaffected. General physical sampling is not shown impossible.

No physical effect, instrument, coupling, ready state, selected phase,
physical context, realization certificate, realized outcome, occurrence law,
reset, complete apparatus family or L1-to-L5/L6 bridge is asserted.
QDD-INSTRUMENT-APPARATUS and its children remain open. Neither the formal
probe nor its test output closes the whole decoder or edits Public Canon v78.
