# Result: STOP before scientific output

Status: PUBLIC NON-CANONICAL.
Owner: #1253.
Disposition: STOP / identifier consumed.

The prospective pin
2e4055ab899271cc0597325a76dcb76d44e13ee7
was publicly read back unchanged and then executed.

Execution exited nonzero before any scientific stdout. The failure was an
implementation-type mismatch in the control calculation: the event-model
module and the independently loaded Hodge verifier each instantiate their own
Python Q5 class, and the frozen verifier attempted to multiply an instance
from one implementation by a matrix entry from the other.

The salient exception was:

    TypeError: argument should be a string or a Rational instance

This is an integrity/runtime STOP, not a mathematical counterexample to any
G1-G6 statement. No threshold, equality, metric target or scientific class was
changed. PREREG.md and verify.py remain frozen and unchanged.

This identifier is consumed and must not be reused. A successor must use a new
candidate identifier and its own public pin. The intended technical repair is
only to construct the predecessor hypothetical control entirely inside one
loaded Q5 implementation.
