# Two overlapping contacts with one fixed full form

Status: NON-CANONICAL / L1. Conditional analytical candidate-T;
exact finite audit PASS, local candidate-C. The computation gate is satisfied
only when the required x86_64/aarch64 jobs reproduce this identical stdout.
No Canon promotion or independent acceptance is asserted by this record.

The declared real architecture implements C12 followed by C23 with one
fixed smooth symplectic form, one autonomous Hamiltonian H=E_lambda+b,
one bank, one circle clock and one counted canonical controller pair.
The controller computes the current pair parity, enables the total contact
and uncomputes itself. The overlapping second contact therefore receives
the correct new parity. The controller resets after each contact, and the
clock hand returns after the six-pulse block. The data generally change.

## Conditional analytical result

PROOF.md establishes the full continuous construction, including its
critical-point selectors and the nonzero time derivative dot B=-partial_t h
in the product coordinates. The full form is specified once as a function
of the internal clock coordinate; it is not manually replaced between
contacts. All pulse seams are smooth, and negative-time flow is the inverse.

For three data slots define

    R=sum Q, I=Q(x-y)+Q(y-z), C_ctrl=4*((q-1/2)^2+p^2),
    E_lambda=R+lambda I+C_ctrl.

On integral data with the controller ready at (0,0), its account is 1.
The exact identity 3R-I=Q(x+y+z)+Q(x-z) proves that the sufficient initial
reserve b>=lambda(3R-I) funds the entire real path. It remains sufficient
at every block boundary, so the same bank/controller can be reused for
arbitrarily many positive or negative blocks on this prepared family.
No fresh bank or controller reset operation is supplied between blocks.
These universal assertions rest on the proof, not on finite extrapolation.

## Exact finite audit

All 343 triples from the frozen seven-value set, four lambda values and
specified deduplicated bank sets gave 3,770 funded cases. Each case ran two
complete blocks and their entire inverse, checking all pulse midpoints and
endpoints in both arithmetic representations. The finite-family totals are
90,480 forward and 90,480 inverse half-pulse snapshots. Forward counts are
7,434 active contact half-pulses, 22,726 held contact half-pulses and
14,868 active controller half-pulses. Other controller half-pulses hold.

Including the exact matrix/selector checks, formal polynomial identities
and named witnesses, 2,183,903 checks passed with zero fired falsifiers.
The generic form/Hamilton equation is checked coefficientwise in 29 formal
variables on the full 16-dimensional carrier. Finite-family snapshot SHA-256:
d035ee8f6c18f662eb2bce9352cba7b331e1281ae4e9badced2a4c8d5b58ac2d.

The two routes use power-basis arithmetic and independent u-basis polynomial
reduction with a trace Gram form. The primary half-window hand is modulo 12;
the checker independently stores rational clock phase modulo 6. Complete
state comparisons include data, bank, clock and both controller coordinates.
All literal inverse snapshots recover their forward predecessors.

## Boundaries witnessed explicitly

- Stale parity fails: (2,0,0) changes pair23 from admitted to refused after
  C12; forcing the old admitted branch produces half-integral coefficients.
  The opposite predicate change also occurs on (2,0,1-j^2), where the new
  pair is diagonal. That second example is a predicate error, not a different
  data endpoint under holding.
- Reusing the isolated C12 form fails for C23: on (2,2,0) the first relative
  Q changes from 0 to 5/4, making h12 change. The resulting nonzero defect is
  -dt wedge d(h12 after C23-h12). This excludes that naive reuse only.
- Whole-path funding matters: (u,-u,-ju) has first-contact I=35,40,35.
  Its net endpoint payment is zero, but the sharp first-contact reserve is
  5lambda. The uniform repeated-block guard here requires 10lambda.
- Both overlapping contacts can do work: on (2u,-2u,2u), R=60 and I changes
  160 ->120 ->135. The bank first gains 40lambda, then pays 15lambda. A common
  initial bank 60 ends at 85 for lambda=1 and 110 for lambda=2. Both contacts
  are active and the final data/controller/clock states agree.

The full projected trajectories and chosen on-shell action agree across
these lambda values by the proof. The explicit cross-lambda comparison in
verify.py compares final projected states. The full symplectic forms and
off-shell action functionals differ with lambda, so this does not select
the relative work coefficient or contradict fixed-form Hamiltonian rigidity.

## Custody and limits

The first run's stdout is 3,304 bytes and 15 LF lines, SHA-256
97c61a91ec2d6d3c06045d2da9c78ade30455ccbef9bac0036644bb93181ffbc.
Source pin 43fe4fef2cff6952cf753df888bb7b1928dd744d was publicly read back
before execution. All five source files remain unchanged; see RUN.md.

This is an added smooth real controller, coefficientwise cosine selection,
pulse schedule, clock and energy-dependent form. Intermediate states need
not be integral. Nonnegative bank is guaranteed only for the declared funded
integral/ready family and its trajectories. No complete underfunded HOLD law,
native-U implementation, physical work/action selector, action quantum,
electromagnetic response or alpha value follows. The conditional smooth
composition problem is resolved at this declared scope; those derivation
and physical-selection obligations remain open.
