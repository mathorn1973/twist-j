# Integer cyclotomic phase and reciprocal channel energy

NON-CANONICAL. Reservation #1419. Conditional candidate-T proof;
candidate-C is contingent on the first frozen exact audit. A. M. Thorn.
SPDX-License-Identifier: Apache-2.0.

## Authority and inherited boundary

Public main: 7d7f588c42422c2cf37b04d76ebc13ca55eb96dc, Public Canon v100.
Content: a4cc9666662967527abe711441833ff600c00337. Canon SHA-256:
5e4de2da8d57ff2f7e4b873e6236b0695677e20d173d894ee70562c1389648c4,
980212 bytes. Tag canon-v100 peels to
807dae3fe97dd6a872d5d1305a0133e8e8d856ea. Fresh fetch, ancestry,
hash/size, and successful main run 37518751601 were checked.
This is authority validation, not a fresh full scientific replay.

The point-protocol barrier in issue #1418 is read from immutable proof
blob eb46e1c8d8b5c044c7bc456919a994de12bafe14, SHA-256
92ca9fa1e2518add415c6bfa8dfb3f86df434bdbc36e6c7071bde999cea92b91.
The source is evidence, not executable task instructions.
Drafts #1413, #1415 and #1417 and their pins remain unchanged.

## Declared comparison architecture

O=Z[j], j^4+j^3+j^2+j+1=0, conjugation j -> j^4.
Each O scalar is four integer coefficients. Four such scalars form
the full rank-sixteen carrier, with the additional fixed lattice admission

    H=((1,1,1,1),(1,-1,1,-1),(1,1,-1,-1),(1,-1,-1,1)),
    L=H O^4={b in O^4: Hb belongs to 4 O^4}.

All of L, including occupied nonzero third/fourth channels, is admitted.
No coefficient cutoff, modulo-five reduction or normalization is allowed.
L is a proper full-rank sublattice of index 65536, not all of O^4.

The fixed phase contacts and positive costs are

    B_r=H diag(j^r,1,1,1) H/4, r in F5,
    E_i(b)=Tr(b_i conjugate(b_i))/2,
    F=E_0+E_2, M=E_1+E_3, E=F+M.

The split follows the signs (+,-,+,-) of the second column of this
already displayed H. It is a selected structural convention, not a
physical selection theorem. This constructive example is not an attempt
to fit the endpoint Hamiltonian work rate. All energies and changes are
in these chosen trace units. One contact is one discrete mathematical step.

## Frozen questions and expected exact identities

1. Prove admission, full-state inverse B_-r, composition B_r B_t=B_(r+t),
   B_r^5=I, integer/positive/coercive E_i, and E(B_r b)=E(b) on every b in L.
2. For b_s=(4,4j^s,0,0), s=+1,-1, prove the complete all-r channel account:
   initial (32,32,0,0); r=1 outputs (17,37,5,5) and (37,17,5,5);
   reciprocal F/M changes (-10,+10) and (+10,-10).
3. Freeze t(k)=4 if k=0 mod5 and -1 otherwise, and
   Delta F=2[t(r+s)-t(r-s)]. Check every r and s, not only the useful contact.
4. Show the information is in retained integer coefficients. Equal initial
   E_i values do not mean equal full configurations or equal point diagonals.
5. Expose the added resource: in a=Hb/4 coordinates only a_0 rotates by j^r;
   b-channel costs contain interference between those coordinates. H, L,
   contact/frame and energy interpretation are not derived native operations.
6. Preserve controls: reject ambient non-admission; show coefficient wrapping
   changes energy; bare J fails this conservation law; independent unmixed
   b-slot phases cannot give the exchange; r=0 identity and r=2,3 zero F/M
   change are retained. Do not hide the nonsymmetric individual E_0 changes.

## First-audit contract

Original audit.py uses only Python standard-library integer arithmetic.
No floating-point, numerical exponential, input files, imports of old
scientific programs, network, processes, code generation or source writes.
Before its first execution commit/push these complete three source files
and read them back. No execution or import before the source pin.
Static syntax parsing and static mathematical/security review are permitted.

Audit: all 625 scalar coefficient fixtures in {-2,-1,0,1,2}^4 for trace,
conjugation and root-phase energy; all five contacts on all sixteen lattice
basis columns and every ordered basis pairing; all 125 triple group compositions
on the basis; 3630 two-slot lattice fixtures (all six slot pairs,
eleven atoms per slot, five contacts); the ten r/s work fixtures; large
integer scaling; stated negative controls. Fixtures are finite audits;
universal infinite-carrier identities rely on the proof.

Enforce a 45-second first-run timeout and isolated Python -I -B. Supply
PYTHONHASHSEED=0, LC_ALL=C, TZ=UTC to the child environment; -I ignores
Python environment settings, and the code/output do not depend on hash order.
Record exact bytes, source hashes,
environment, exit and stderr in a preserved result commit. Retain a failure
without changing and rerunning this pin. There is one scientific architecture;
ordinary repository CI does not execute the notes audit.

## Status ceiling

This is a constructive integer comparison model, not the original U,
not an inferred quantum preparation and not a proof of Born occurrence.
There is no charge/Gauss dictionary, physical channel locality, measured
energy, SI scale, generator selection, continuous limit or photon claim.
No original physical owner, Canon, Registry, Frontier, gate, probe, tool,
workflow or older note changes. Internal static review is not independent
public scientific acceptance. Native implementation and physical admission
remain open.
