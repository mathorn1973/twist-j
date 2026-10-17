# Result: native shell gate of U

PUBLIC / NON-CANONICAL / L1 / candidate-T. Issue #1550; program #1548 lane A.
Owner Claude-20261016-v103-aframe-gate; author A. M. Thorn, Apache-2.0.

Public pin 7b06ea6b377930f6edeb84cb330b9d69f1b82c51. All nine preregistered
falsifiers survived the first default run: exit 0, empty stderr, exact
stdout in EXPECTED.txt, receipt in RUN.md. No falsifier fired.

| Falsifier | First-run result |
|---|---|
| F1 inherited native premises | PASS: 15625 checkpoints, 78125 involution checks, sheet maps, 011 synchronization |
| F2 field algebra and L image | PASS: all identities exact, det L=25, image of L mod 5 is C with 25 residues |
| F3 comparison map and gate | PASS: W is the piston action of a, W(ker h)=C, H(e0)=2, H(We0)=3 |
| F4 generator laws | PASS: four exposed laws and the a law on all 15625 checkpoints |
| F5 every branch | PASS: ten-row table on all 31250 checkpoint-bit pairs |
| F6 absorbing sheet | PASS: Klein law on 12500 pairs, one fixed point per bit, 249 of 250 moved |
| F7 inherited V relation | PASS: G14=V^-1(S), 13 whole R fibres |
| F8 origin-zero prefix | PASS: zero start a,c,e; 625 gated from n=3; 401 gated at every n |
| F9 finite regression | PASS: labelled regression only, not the proof |

## Answers at the frozen scope

All arithmetic in F5, `h=(p4+2p1,p4p+2p1p)`, `J(u,v)=(v,u)`, `G={h=0}`.

1. The exposed laws hold on every checkpoint: `h(bx)=-Jh`,
   `h(dx)=h(ex)=-h`, `h(cx)=-Jh+(r,-r)`.
2. The actual `a` law is `h(ax)=(p1+2p4,p1p+2p4p)=2h+2(p1,p1p)`. It is not
   an `h`-only law: `p->(h(p),h(ap))` is a bijection of `F5^4`, so for each
   value of `h(x)` all 25 values of `h(ax)` occur. On `G`, `a` keeps only
   the zero piston and `c` keeps only `r=0`.
3. The image of `L mod 5` is `C={y0+2y1=y2+2y3=0}`, 25 residues, and
   `x in G` iff `W(p) mod 5` is in `C` iff every integer lift of `W(p)` lies
   in `L Z^4`. `W` is not an `H`-isometry.
4. On `X14` only `b,d,e` are selected, `T_t(X14)` lies in `X_(4+2t mod 5)`,
   and `h` moves by `-J` or `-I`. By induction, for every driver sequence,
   gate status on `X14` never changes: `G14` and its complement are both
   absorbing. The gate is kept as a set, not pointwise: each `T_t` has one
   fixed point on `X14` (`(1,3,4,2,1,3)` for t=0, `(1,3,4,2,3,3)` for t=1,
   both gated) and moves 249 of the 250 gated checkpoints.
5. Origin-zero prefix: words `ace,bbd,cce,dbd,ebd` on sheets 0..4. From
   `n=3` on, a trajectory is gated iff `h0=0` on sheets 1..4, and iff
   `p1p+2p4p=r0` and `p1+2p4=-r0` on sheet 0. That is 125 initial
   checkpoints per sheet, 625 in total. Gated at every `n>=0`: 401, of
   which the zero start is the only one on sheet 0. The zero start runs
   `0 -> 0 -> (2,1,2,1,1,0) -> (0,0,1,3,1,1)` with traces `0,0,2,1`,
   `h=0` throughout and `r3=1`; it is gated for all time without `r=0`.

## Inherited versus new

Inherited and only rechecked: generators, selector, sheet maps, 011
synchronization, `(z,q,r)` quotient, fixed-point table, `A_f`/`L`/`Vinv`
algebra and the integer image criterion. The all-time gate invariance on
`X14` is an inherited corollary of U-NATIVE-INVARIANT-AND-NOWRITE, because
`G14=V^-1(S)` with `S=-S`; the direct induction is a second route, and the
Klein law is the same information restricted to two functionals of `V`.
New at L1, candidate-T: the typed identification of the native gate with
the `L` image residue through `W`; the complete five-generator `h` table
with the `a` non-closure certificate and the `r` term of `c`; the ten-row
branch table; the explicit prefix classification (sheet-0 condition, 625
gated from `n=3`, 401 gated at every time, uniqueness of the zero start on
sheet 0); and the separation of set preservation from pointwise fixation.

Computed record digests: G14 `373778349c9cb18ff376e726b23d381d0c62a26c7c5d6c9f2d8c31e2e395b097`;
permanently gated initial checkpoints `1640c7f998e9fb47a45e2b08182e34ee847b0c7073e91d0864fb3307a165b312`.

## Exact scope

L1 residue arithmetic only. The zero start's piston at `n=3` is
`(0,0,1,3)`, whose `W` residue is `(0,0,3,1)`; this lane makes no claim
about that residue's integer lift, unit preimage or energy minimum. No
universal integer lift of U, H-isometry of `W`, physical port, contact,
field preparation, `r=0` law, affine trace law or seventh register is
asserted; checkpoints are F5 states, not `Z^6` trajectories. Same-session
static code review is part of authoring, not independent review. Required
public x86_64/aarch64 replays are pending when this record is written.

Proposed next step, not started: a separately preregistered L1 question on
which residues of `C` the actual gated synchronized orbits visit under the
Klein law, compared at its own scope with lane B's classified unit residues.
No merge, Canon promotion, registry change or release is authorized here.
