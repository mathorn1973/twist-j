# Funded two-pass source renewal on one infinite input cylinder

**NON-CANONICAL / L1. Analytical proofs: candidate-T. Finite replay: candidate-C on the executed architecture only.**

This note constructs two actual source renewals following the four-chart
contact interface in [PR #1867](https://github.com/mathorn1973/twist-j/pull/1867).
It starts with that interface and four explicitly supplied auxiliary slots.
It changes the two occupied source leftovers by native contacts, retains both
new depth archives and every declared old archive literally, and produces a
ready source after each pass.

For every integer h>=0 and supplied initial chart d in {1,2,3,4}, the input
and the two successive arithmetic values are

    n0=64h+3, n1=96h+5, n2=18h+1.

Their division depths are exactly 1 and 4. The active charts change as
d -> 4d -> 3d modulo five. At h=0 this is the concrete chain 3 -> 5 -> 1.

The four auxiliary values are fixed integral affine functions of h. They are
loaded once, before the whole word. No Collatz routine, current output,
depth reader, target lookup or mid-run loading is called by the contact word.
**The known two-step itinerary is compiled into those coefficients and the
schedule.** This is a supplied, branch-specific affine loader. It is not an
autonomous selector for other valuation itineraries, and it does not prepare
the donor bank from the active integer by contacts.

## Concrete result

- One fixed word for each supplied initial chart, independent of h.
- **34 powered contacts, exactly 85 repetitions of the native contact C.**
- **33 core slots**: three source ports, two separate 13-slot depth archives,
  and four funded donor ports. The finite replay appends two occupied old
  archive slots, for 35 slots in total.
- Both renewals act on the actual occupied output of the preceding pass.
  The old source content remains in the donor residues.
- The current active value, depth and chart can be read at both boundaries.
- All four chart constructions are Galois-related at corresponding powered
  contact boundaries. No physical Galois gate is added.

The initial donor account is exactly

    B(h)=5422160h^2+555480h+14368.

At h=0 the first renewal uses two donors with total account 10504 and leaves
5969 in them. Thus the earlier necessary 3->5 bound 4535 is now accompanied
by an explicit attainable, nonminimal construction. The other two donors,
needed for the second renewal, start with account 3864. After the whole
3->5->1 chain, all four donor residues have account 14798, the retained
depth records cost 1650, and the ready source costs 272. These sum to the
initial source-and-bank account 16720. Any old archives cancel unchanged.

## General finite-itinerary construction

The proof also gives a general construction for any predeclared finite word
of positive division depths. That word determines one odd input cylinder.
Every intermediate arithmetic value is affine in its cylinder parameter.
The constant labelled source residues then allow two integral affine donors
per stage, a fixed contact schedule, fresh literal records and a ready source
after every stage. The bank and schedule depend on the chosen finite word.

This is an analytical corollary. The finite verifier below tests only the
explicit depth word (1,4). Neither statement chooses the depth word for an
unrestricted input or supplies an indefinitely reusable finite apparatus.

## Files and evidence

- [PROOF.md](PROOF.md): native overwrite lemma, integral donor coefficients,
  complete layout, both source renewals, exact accounts and scope.
- [REPLAY-SPEC.md](REPLAY-SPEC.md): frozen finite corpus, whole-state checks,
  execution order and failure conditions.
- [verify.py](verify.py): standalone exact-integer replay. Its source must be
  publicly pinned and read back before its first execution.

At this source stage no execution result is claimed. The evidence commit
will add the actual stdout, neutral run record and hash manifest. Required
repository CI does not execute this notes-only verifier.

## Boundary

The result constructs funded two-pass reachability on the entire declared
input cylinder. It does not establish a funding minimum, an initial source
loader, a universal chart controller, renewal on an unannounced valuation
branch, an indefinitely reusable finite bank, or Collatz convergence.
The common-apparatus obligation remains open outside this explicit scope.
No Canon, registry, workflow, probe or reproduction file changes.

Source context: #1867 at `252ae587293419243870deb3700ea6918aa07692`;
#1865 at `b67b5f0783a81bd38475eefc4d10dfaa4ff78bda`.
