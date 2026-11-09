# Analytical author-side review

NON-CANONICAL / L1. Date: 2026-11-09.

This is a review within the authoring session. It is neither independent
scientific acceptance nor an independent reproduction. The reviewer read the
supplied network proof and the complete final `CONSTRUCTION.md`, followed the
algebraic branches by hand, and checked the symbolic resource formulas.
No scientific executable, verifier import, simulation or numerical search ran.

Reviewed `CONSTRUCTION.md` SHA-256:
`0c4631607466abec0a9c66535cc1e47702454321598e2c2fc17012d4afaf608c`.
The result is an analytically supported candidate requiring a new prospective
verification and independent review before promotion.

## Checks and findings

1. **A real unknown-sign interface.** Both preparations use the same high
   launch pair. At the first tick, the positive writer's payer `(W,0)` has
   odd difference and rejects the interface; the negative payer
   `(rho,-rho)` accepts it. The exact relative updates are
   `(rho,J)->(W,1)` and `(W,1)->(rho,J)`. The resulting emission times
   `{1,3}` and `{2,3}` follow from the stated source-state table. No
   message-dependent rail preparation is substituted for the local sign.

2. **Occupied continuation.** The states `D_a` and `Z_a` are fixed by the
   isolated four-cell writer for the stated equal-account and parity reasons.
   Coupling them to the launch site gives the complete finite transition table
   in section 8. In particular returned pulses cannot be ignored or treated as
   fresh blank input.

3. **Exact return certificates.** The positive data array returns to its
   initial state at `2L+4`, and the negative array at `L+2`. In the positive
   case the essential events are `A_+` with rail `{L-1}` at `L+1`, `B_+`
   with `{0}` at `L+2`, `Z_+` with an empty rail at `L+3`, `C_+` with `{1}`
   at `L+4`, and `D_+` with `{2,1}` at `L+5`. The next return yields
   `A_+` with `{0}` at `2L+4`. In the negative case `D_-` with
   `{0,L-1}` at `L+1` yields `A_-` with `{0}` at `L+2`.
   These are sufficient common-period certificates; no minimal-period claim
   is needed.

4. **A substantive failed first design is preserved.** The entire positive
   data rail at `L+5` equals the negative data rail at `3`. Their shifted
   first-window receiver states consequently alias. Every instantaneous
   fixed rail-only reader that accepts the negative first window must give
   that same negative answer on the later positive passage. This is stronger
   than a defect of one particular gap formula. It requires an additional
   phase-distinguishing resource for this architecture and stronger contract;
   it is not a universal lower bound requiring a clock for every conceivable
   apparatus.

5. **The paid phase reference repairs that alias.** A separate B-only rail
   with `2P` sites and one high marker has period `P=2L+4`. Its local
   canonical-code corridor is enabled exactly at the specified first-window
   phases. The whole data state recurs at this same period for either sign.
   Therefore each enabled window repeats the proved first window, while the
   later aliased passage occurs half a period away and is suppressed. The
   clock does not switch the data law or supply uncounted input.

6. **The finite hold includes layer boundaries.** Reading a contiguous data
   corridor admits the odd anchor after `K0`, as well as the even anchors at
   full ticks. Running the clock and data conveyor layers in parallel and
   reading the contiguous clock corridor
   `[2tau,2(tau+h)-1]` prevents intermediate clock holes. The first arrival is
   after `K1` at `tau`; the reader remains correct through the intermediate
   layers before expiry and becomes BLANK at the common expiry `K1` boundary.
   This is a discrete boundary statement, not a claim about physical evolution
   inside an unspecified realization of a layer.

7. **Remoteness and full resources.** The final choice `L=2d+h+3` makes the
   entire data receiver at least `2d` ring bonds from launch in either
   direction. The earlier smaller-ring choice would have provided an
   arbitrarily long delay without arbitrary shortest-path remoteness; the
   final geometry removes that ambiguity. Data and clock receiving corridors
   are explicitly co-located in the supplied layout. They comprise
   `8h+8` raw receiving cells. The complete apparatus has
   `12L+20=24d+12h+56` raw cells,
   `H=12L+28-6phi`, and `E=24L+50=48d+24h+122`.
   All five full-carrier involutive layers preserve `S,H,E`; reversing their
   order gives the stated full inverse. These are construction costs, not
   optimality or physical-energy claims.

## Remaining scope

The record is a moving two-pulse word retained inside a bounded occupied
receiver region, qualified by a counted local phase reference. It is not a
stationary one-cell latch. The common clock phase, geometry, five-layer order,
initial stock and semantic reader are supplied structure. Recurrent readings
reuse the same original sign and do not constitute independent new messages.
The existing fixed-pair no-export theorem remains intact: changing the source
pairing enables the encoder, after which the fixed-pair rail transports the
new account word.

A fresh prospective verifier must test both arithmetic implementations,
complete raw states, all five intermediate boundaries, inverse and full
accounts, both explicit return tables, common-period reader truth, local
receiver access, and the mandatory ungated false-passage control. No such
computational gate or independent acceptance is asserted by this review.
