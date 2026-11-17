# Can a CORR relay clear the read head and retain its phase word?

Prospective finite L1 circuit test under [claim #2011](https://github.com/mathorn1973/twist-j/issues/2011). The [preceding circuit](https://github.com/mathorn1973/twist-j/pull/2010) generated distinct fresh writes through a selective CLK transfer. Its loaded head missed the clearing collision. Published bare cuts and cut-local symbolic arithmetic informed the four preparations below. Their decorated trajectories are prospective.

The active authority at reservation was Public Canon v113, main c089e7ec7ecc82f4838c27663d94c040f5cc4ea3, annotated tag object 3a91e2bee83a3045b17f3aa2895f69deef62d89c, content commit 50d0e94d81e4954b7351bff755ed1889290bb7b8. The declared Canon has 1555510 bytes and SHA-256 47114cb616069242cff36bb499e5fe9b11266a92c744ba3f15a9085c11956b34.

## Native law and preparations

The state consists of all four rails (upper and lower matter, CLK, CORR) at every site of the periodic 8 by 4 grid and one matching bit. Work over the cyclotomic integers, using the ordered basis (1,j,j²,j³), j⁵=1, ρ=j², J=1+ρ, h(z)=z conjugate(z). Each tick transports the first three rails vertically and CORR horizontally on native matching b, scatters at all sites, and flips b. For same-residue pairs the contact fixes their midpoint and multiplies the half-difference by ρ. For other pairs it acts as the identity. At each site with integral matter and radiation half-differences d and f, branch B1 applies (Jd,f/J) if d is nonzero and h(f)=h(J)h(d). Branch B2 applies (d/J,Jf) if f is nonzero and h(d)=h(J)h(f). Both preserve the two midpoints. Forward runs use only this rule.

Reconstruct the bare clock from its raw-zero cut. Column zero carries (2J,−2J,1) in the first three rails. Rows 0 and 1 carry the CORR triple (−3,−3,5) at columns 0,1,2. Rows 2 and 3 carry J−ρ²−2ρJ(2+ρ+ρ²) at column zero. All remaining entries vanish. Enumerate the 85 ready cards by applying a left and a right triple contact. Locate each whole ready field on the even cuts of the 622-tick bare clock. A fresh test starts one tick before that card. In particular, raw 44 and raw 4 use bare offsets 73 and 189. The raw-zero launch starts at offset 0 and differs from the predecessor of card 0.

Set D=(1,−1,−1,1), g=JD. Install (D,−D,(0,2,−1,1)) on the first three head rails at (1,0), and (−3g,−g,(−2,0,−1,0)) on the corresponding receiver rails at (1,1). The output is the literal upper receiver rail. Each row adds the stated stock to the preceding row for every input, with no other non-bare entries.

| Preparation | Additional stock | Predicted Q |
| --- | --- | ---: |
| no_bridge | Common head and receiver only | 637 |
| bridge | Add (3,4,4,8) to CORR at (7,1) | 719 |
| supported | Set CLK at (1,2) to (0,−1,−1,0) | 722 |
| material_support | Set upper matter at (1,3) to (−1,0,−1,0) | 725 |

## Predictions and falsifiers

1. All 85 fresh inputs start with identical work stock. At the read substep the original upper word is (−9,0,−3,−3). Require no earlier change, a genuine write from the common stock on the work tick for both targets, and zero changes at both substeps of both ticks for each of the 83 foils. Inspect late foil writes separately. The common upper transport gives w=(−3,2,−5,1). In the control both targets end there. In each bridge preparation raw 44 should end at w and raw 4 at v=(−5,0,−5,0).
2. The receiver CLK equals the raw-4 post-read head CLK, so their admitted contact has zero displacement. An odd read matching connects (7,1) to (0,1). On the following even matching the receiver CORR should move to (−4,2,1,−2) only for raw 4 among the two targets. This makes f=D. The expected work branches (head,receiver) are (2,2) on raw 4 with the relay, and (2,0) on raw 44 and the two no-relay controls. Require the head at each target to recover its exact paid CLK, reference CORR, and original material half-gap norm. Record the actual material rails, whose midpoint may move as work is delivered.
3. Score retention at every transport and collision except within a qualified work tick. A single out-of-window upper-rail change refutes exact hold. Test the next two ticks on every fresh input. The CLK support is intended to block the immediate inverse collision. The extra material support is intended to block the subsequent upper-rail transport. Test persistence independently of both local guard predictions.
4. Read qualification is observational. Require the bit, all 122 rails outside the original six head/receiver stock slots (including auxiliary stock at its baseline), and a native head B1. A qualified work is the tick following such a read. Record actual net writes separately from nominal samples. Compare the two classes of completed words and the classes of words on all held cuts identifiable by their preceding qualified work. Check for aliases within streams and across admissible starts, distinguishing different prior net writes. An overlapping word with different last labels refutes a phase decoder from this rail. Missing phase coverage prevents a positive separation finding.
5. Compare the local head, the bare carrier outside explicitly stocked slots, paid radiation, paid coordinates outside the two receiver matter rails, and full state plus bit. Positive recurrent operation needs both reads, genuine writes, uninterrupted hold, disjoint classes and a complete return. An external clock label cannot supply a missing native read. Each finite prefix is reported with its own observation horizon. A prefix containing a counterexample settles the corresponding universal claim even when the loaded period is unknown.
6. Compute total matter, radiation, the ring-valued Hermitian sum over all 128 rails and half its field trace. On the primary runs audit every C and B cut and invert B then transport with the matching recovered from the bit. Record every violation. Independent C++ arithmetic checks conservation and inverse on new local maps, and checks complete cuts and inverse at least every 4096 ticks and at termination.

## Code, coverage and action layer

Freeze this file, verify.py, kernel.py and period.cpp, together with the sweep.py reporting driver, before decorated execution. kernel.py extracts the exact native arithmetic, ready-card generator, stock helpers and inverse audit of [the preceding verifier](https://github.com/mathorn1973/twist-j/blob/f9f90fedbaa35715612f452dc09a321dc94e39f2/probes/P-H3-CLK-TO-RAIL-1/verify.py). Run from the repository root:

```sh
python3 probes/P-H3-CORR-PARITY-1/verify.py
```

The primary gate tests all four preparations on every fresh card for four ticks, then follows three uninterrupted starts per preparation for 3110 ticks each (five bare periods). Reconstruct every substep from the recorded inputs. The C++ supplement also runs each of the 85 predecessor starts per preparation for 3110 ticks or first full return, whichever comes first. For the three distinguished starts per preparation use an additional bound of 1000000 ticks or first exact return. In the probe directory:

```sh
g++ -std=c++20 -O3 period.cpp -o period
# Arguments are preparation, starting cut, tick bound.
./period material_support raw4 1000000
./period bridge rawzero 1000000
./period supported raw17 3110
python3 sweep.py ./period
```

Record the primary stdout verbatim and give reproducible supplemental counts and hashes. Results apply to these fixed, fully funded preparations and initial states. This experiment does not change H3 or assign a Canon status.
