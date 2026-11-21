# Native auxiliary contacts before the fifth head return

Prospective finite L1 experiment. [Claim #2013](https://github.com/mathorn1973/twist-j/issues/2013). The [Q725 construction](https://github.com/mathorn1973/twist-j/blob/8a92a1200996e63953ffca176f857abaf51d1176/probes/P-H3-CORR-PARITY-1/RESULT.md) writes distinct words and restores the two radiation rails of the read head. On the raw-4 history an isolated upper pair returns to its starting values after five odd contacts, opening an unwanted even head-to-receiver contact on tick 12. This study changes the initial state of nearby cells. All timings are observation indices. The complete forward step always uses the native matching and collision.

Public authority at reservation is ACTIVE Canon v113, main c089e7ec7ecc82f4838c27663d94c040f5cc4ea3, content 50d0e94d81e4954b7351bff755ed1889290bb7b8, annotated tag object 3a91e2bee83a3045b17f3aa2895f69deef62d89c, Canon SHA-256 47114cb616069242cff36bb499e5fe9b11266a92c744ba3f15a9085c11956b34, 1555510 bytes. The preceding published trajectory and single-contact symbolic substitutions informed the choice of stocks. The four newly loaded trajectories are prospective.

## Carrier and law

Use coordinates in the integral basis (1,j,j²,j³), j a primitive fifth root, ρ=j², J=1+ρ. All 32 sites of the periodic 8 by 4 grid carry (R₀,R₂,CLK,CORR). At bit b, transport acts on the vertical matching of the first three rails and on the horizontal matching of CORR, with pairs starting at b modulo two. Every admitted same-parity pair with midpoint m and half-difference d goes to (m+ρd,m−ρd). A refused pair is fixed. On each site, write d and f for integral half-differences of the two matter and two radiation rails. For h(z)=z conjugate(z), B1 applies (Jd,f/J) if d≠0 and h(f)=h(J)h(d). B2 applies (d/J,Jf) if f≠0 and h(d)=h(J)h(f). The midpoints are preserved. Other sites stay fixed. Flip b after the collision.

Initialize the original 622-tick clock and enumerate all 85 ready cards as in the byte-identical prior kernel.py. On each predecessor install the Q725 stock. Put (D,−D,(0,2,−1,1)) on the first three rails of the head H=(1,0), with D=(1,−1,−1,1) and g=JD. Put (−3g,−g,(−2,0,−1,0)) on the first three rails at receiver R=(1,1). Add (3,4,4,8) to CORR(7,1), put (0,−1,−1,0) on CLK of S=(1,2), and (−1,0,−1,0) on the upper rail of A=(1,3). Measure the physical word R₀ at R.

## Fixed interventions

Each of the four alternatives starts with all Q725 stock. Values in the table are additional initial stock. No switches are used during evolution.

| Mode | Extra initial matter | Extra initial radiation | Predicted Q |
| --- | --- | --- | ---: |
| baseline | None | None | 725 |
| ingress_active | (4,2,3,1) on R₂ at A | (0,−2,−2,0) on CORR at both A and (2,3) | 774 |
| ingress_sham | (−4,−2,−3,−1) on R₂ at A | Same as ingress_active | 774 |
| delayed_active | (3,−1,−1,1) on R₀ at S | None | 753 |
| delayed_sham | (−3,1,1,−1) on R₀ at S | None | 753 |

Each sign-control pair has identical initial Hermitian energy and parity. Report the linear sector sums separately. Ingress aims to trigger B2 at A on tick 3 following a target work. With upper input (2,2,3,1) the active local gaps are d=−1 and f=(0,1,1,0) with Jf=−1. Changing the input lower sign tests this guard. Test whether a following native contact keeps the local collision from immediately reversing and whether the next odd H–A transport loses its previous upper movement. Measure the ranks at which A actually takes B2 at tick 3. A trigger shared by the targets cannot alone identify which target wrote.

The delayed alternative acts through the even S–A upper edge. On the known raw-4 Q725 history A has upper value a=(−3,1,1,−1) when entering tick 10. The two controls supply −a and a respectively. If the prior guards persist, the active contact rotates the opposite pair at 10 C while the equal pair has zero displacement. Compare H–A at 11 C and the receiver at 12 C. A changing movement count alone does not demonstrate a skipped unit on a fixed-order rotor. Check the actual states and the first later loss. Record all collateral writes.

## Coverage, systematics and decision

* The primary audit runs all five preparations on each fresh predecessor for 24 ticks. On the first two ticks require no early write, two distinct net writes at 44 and 4 with the reference words (−3,2,−5,1) and (−5,0,−5,0), and zero receiver changes on every other card. At the target work cut require original paid head CLK and the exact reference CORR. Record full radiation and carrier comparisons separately. Inspect both C and B at every tick.
* Follow each preparation without reset from raw zero and from each target predecessor for 3110 ticks (five original laps). A read requires the matching bit, literal agreement with the funded phase template on the 122 coordinates outside the original six head/receiver stock lanes, and actual head B1. Work is the following tick. Count genuine net writes and first loss of each written word outside qualified work. Require both labels, continuous hold between writes, disjoint word classes, and full state-plus-bit return for a reusable two-phase register. Record synchronized aliases at equal cut and equal age after distinct writes. A missed read, literal overwrite or alias falsifies the corresponding claim. An empty class gives no positive decoding evidence.
* Compare the actual nonidentity upper transport cuts in fixed intervals to the baseline. Record added and missing movements separately. Finite upper-rail activity supplies neither a signed winding coordinate nor a long-time rate law. A physical propagation law is outside the test.
* Check exact matter sum, radiation sum, total ring Hermitian energy, half its field trace, and recover every input and the matching bit by reversing B and then C on each Python step. Cross-check using a four-coefficient C++ implementation, with conservation and inverse on new nonidentity maps and whole-cut audits no less often than every 4096 ticks and at endpoints.
* The supplemental census covers every mode and every predecessor to 3110 ticks or first full return. For each mode also run the two target predecessors and raw zero to 1000000 ticks or first return. For both active modes extend every remaining predecessor to that same bound. Report per-start returns, class coverage and first actual losses. Report incomplete periods as lower bounds.

Freeze PREREG.md, kernel.py, verify.py, period.cpp and sweep.py before executing the new fixtures. Commands from the repository root for the primary and from the probe directory for the supplement are:

```sh
python3 probes/P-H3-HEAD-PULSE-1/verify.py
g++ -std=c++20 -O3 period.cpp -o period
python3 sweep.py ./period /tmp/head-pulse-runs --jobs 4
```

The last command requires a fresh output directory. The sweep writes per-case stdout and compact coverage and class tables. The experiment is restricted to the stated L1 carriers and native law. A repeatable delay, a true recurrent register, a new event-rate law, and a Canon claim all require their own evidence.
