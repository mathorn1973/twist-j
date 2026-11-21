# Receiver and native-clock finite audit preregistration

Status: **NON-CANONICAL / L1**, prospective candidate-C only after execution.
Action layer: L1. This successor audit preserves the earlier reduced and
full-field sources and results unchanged. It neither reruns their tests
nor promotes their status.

## Freeze and execution rule

Before the first scientific execution, commit and publicly pin
verify_receiver.py, this file, RECEIVER-CONTACT.md, RECEIVER-DYNAMICS.md,
and RECEIVER-OBSTRUCTION.md, with a source SHA-256 manifest.
Only syntax parsing, source reading, and hashing are permitted before pin.
The parent run record must identify the immutable pin and exact source hash.

Command after pin: python3 verify_receiver.py from this note directory.
Use Python standard library only, no network, and no floating point.
Per architecture: one bounded process, 300 seconds wall time, 1 GiB memory.
Required architectures are x86_64 and aarch64 on the same frozen source.
Both must exit zero with empty stderr and byte-identical deterministic
stdout. No budget increase or source repair is permitted under this pin.
Any assertion failure, exception, timeout, memory limit, or mismatched
stdout is a failed gate and must be retained and reported.

## Declared objects and fixed choices

The ring is Z[j] with Phi_5(j)=0, represented by four integer coefficients.
The quadratic account is Q(z)=(5 sum z_i^2-(sum z_i)^2)/2.
The ordinary total contact uses rho=j^2 and refuses odd coefficient
differences. The receiver stock is fixed before any unknown input:

R=(3,4,2,0), a=(1,2,1,0), Q(R)=32.

The receiver word is five repetitions of C(0,2), C(0,1). It has ten
contacts; its literal reversed C^4 inverse has forty. The stock is a
supplied asymmetric frame, not a selected physical law. The native
clock family and its compressed and padded words are declared in
RECEIVER-DYNAMICS.md. Padded words use 23 ordinary contacts and eight
slot swaps for every member. They preserve final state but no additional
path-action accumulator is asserted.

## Exact finite inventory

1. Check j^5=1, the three stock preparation norms, word lengths, and the
   five explicit stock states and norms from RECEIVER-CONTACT.md.
2. For all 81 ordered pairs from the fixed nine-element alphabet
   (0,1,j,j^2,j^3,-1,J,a,R), check contact powers 0 through 5, Q and sum
   conservation, the global fifth-power identity, and the literal inverse.
   Every audited local operation checks full Q and slot sum; every refused
   contact checks literal identity.
3. For all five prepared high digits, check all ten admission decisions,
   every intermediate stock state, final Q=(32,17,2,7,27), account 36,
   pointer backreaction, and complete inverse. Append the untouched -R
   companion and check neutrality and account 68.
4. For all 25 physical two-pair labels, check the terminal high-digit
   response, unchanged low pair, total account 40, complete inverse, and
   optional neutral companion account 72. For all 125 pairs (r,t), check
   the actual reencoding (1+5t)r mod25 preserves the low digit and produces
   five distinct readings precisely when r mod5 is nonzero. Freeze the
   r=13 labels (13,3,18,8,23), response (2,32,7,17,27), and signed stock
   work (-30,0,-25,-15,-5). In five semantic controls keep the exact
   physical r=13 state unchanged and check the identical complete output
   and terminal Q=2.
5. For all 729 raw occupied triples from that alphabet, check the ten-step
   receiver and its forty-step inverse, exact total Q and total sum.
   Check the explicit all-refused input (1,j,0).
6. For each of the five native clock members, use 45 basis-amplitude
   fixtures (five sites times the nine-element alphabet) plus the following
   eight fixed amplitude vectors:
   (0,0,0,0,0); (1,0,0,0,0); (0,0,0,0,J);
   (1,j,j^2,j^3,J); (R,a,-1,0,phi);
   2*(1,j,j^2,j^3,J); (1,0,J,0,-j); (1,1,1,1,1).
   Check exact native-word equality with the amplitude formula, padded
   equality, literal inverse, and fifth power j on every neutral amplitude.
   Check twenty-fifth power on the eight dense fixtures.
7. Use nine deterministic raw ten-slot clock fixtures, with slot k at
   offset o equal to alphabet[(o+2k+k^2) mod9], for o=0,...,8.
   For each clock member check padded/compressed equality, literal inverse,
   fifth power C^3 on every complete pair, and twenty-fifth power identity.
   No neutral-carrier assumption is made for these controls.
8. From the common delta clock preparation, check every actual V_m step
   reaches j^m at known pair site 1. Attach the same stock receiver at
   that fixed site, check response (32,17,2,7,27), complete account 36,
   receiver reversal and clock reversal. Check the delta fifth power is
   not the delta, so its period is 25 rather than a proper divisor.
9. Apply thirteen actual padded native ticks to the same delta preparation
   for every m. Check the only occupied pair is site 3 with amplitude
   j^(13m+2). Attach the same receiver at site 3; check response
   (2,32,7,17,27), complete account 36 and pointer backreaction.
   Check an untouched -R companion gives total zero and account 68.
   Reverse the entire receiver and thirteen ticks literally.

## Output and boundaries

The deterministic stdout contains the status line; fixed stock and
word lengths; the five high-digit readings; witness labels and readings;
the semantic-control readings; one-tick and thirteen-tick native-clock
readings; signed witness stock work; the complete accounts; padded word
operation counts; fixture counts; the exact assertion count; and PASS.
There are no timings, machine names, random seeds, paths, or floating values
in scientific stdout. The first run supplies the exact byte artifact.

The stock actively supplies energy to the pointer; all listed terminal
stock energies are at most 32. The audit does not integrate a funded
archive, derive a passive detector, identify a Born rule, choose a
character or native clock dynamics, implement the full field-driven
Gamma controller, or derive electromagnetic coupling. It distinguishes
physical state or dynamics changes from semantic character changes
under one explicitly fixed receiver calibration.