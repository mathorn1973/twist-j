# P-FIRED-COMMUTATOR-NOGO-1 result

## Status and scope

RESULT 10/10 ALL PASS at the immutable pin
cb2c7d74352a356f8b94a35677a6d47ae0cbc7ee. No falsifier fired (F1 to F5
clear; F6 awaits the GitHub x86_64 required check at pull-request time).

Earned scope, L1 state only, on the five public census involutions of
(Z/5Z)^6:

- On the sheet z5 in {1, 4} the selector i = (z5 + 2 t) mod 5 takes only
  values {1, 3, 4}: only b, d, e ever fire; a and c are silent.
- The three fired pair commutators are pure fiber translations with zero
  piston component: [d,e] = T_(0,0,0,0,3,0), [b,d] = T_(0,0,0,0,3,3),
  [b,e] = T_(0,0,0,0,1,3).
- The linear parts of b, d, e lie in the abelian Klein group
  {I, -I, B, -B} of exponent 2, so every group commutator in <b, d, e>
  is a pure translation; the word sweep confirms zero piston on all 1521
  ordered pairs of words up to length 3; the three commutator vectors
  generate the full 25-element fiber plane and conjugation preserves it.
- Conclusion at the audited proof level: the derived subgroup
  D(<b, d, e>) is exactly the 25 fiber translations. The fired dynamics
  is spatially abelian; piston-block noncommutativity cannot arise from
  the fired steps. Negative control: [a, c] is not a translation
  (5 distinct displacements), so the fired-set restriction is essential.

The result is a group-theoretic no-go at L1. It selects no curvature
operator and computes no curvature value; CURVATURE-OPERATOR-CANONICAL,
CURVATURE-HISTORICAL-TRACE, CURVATURE-HISTORICAL-GAUSS-SPLIT, and
KERNEL-MACRO-READING are untouched and complementary. No physical
reading is claimed here; a separate dictionary candidate lives in the
project incubation lane and enters, if ever, by its own fold.

## Architecture record

Owner formal leg (RUN.md): Ubuntu 24.04.4 LTS aarch64, Python 3.12.3,
exit 0, stdout SHA-256
8d5472d7906ff71eeeabbd6099536f6accdcedafdd6874b58e5947823be3c04f
(1418 bytes), stderr empty.

Informational local witness at the same pin, before any pull request:
Debian GNU/Linux 13 x86_64, Python 3.13.5, kernel Linux
6.12.90+deb13-amd64, exit 0, stderr empty, same verifier SHA-256, same
stdout SHA-256 and byte count. Two distinct local architectures and
Python versions agree byte for byte; the formal two-architecture gate
per AGENTS.md section 6 remains the GitHub x86_64 ubuntu-latest required
check at pull-request time.

## Proposed follow-up (not enacted here)

A later sealed fold may add the registry row FIRED-COMMUTATOR-NOGO [T]
with evidence probes/P-FIRED-COMMUTATOR-NOGO-1 and the falsifier
"fires if any pinned gate fails on re-run, a commutator in <b, d, e>
with nonzero piston component is exhibited, or the two-architecture
transcripts differ". This probe changes no canon file.
