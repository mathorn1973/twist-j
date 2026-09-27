# Disposition: static audit-source interface failure

Status: ABANDONED. PUBLIC NON-CANONICAL, no scientific result.
Owner: #1245. Author: A. M. Thorn <thorn@twistj.com>.

The prospective pin 2a3ce5df8dc9dee4b918f269fb316354a7f895ff was published
and read back. Before scientific execution, static review of the inherited
Q5 arithmetic interface found that generate.py uses tau**2 although Q5 has
no __pow__ method. The intended operation is tau*tau.

No scientific audit was executed. There is no EXPECTED.txt or RUN.md and
no claim of a passing construction. The three original prospective files
remain unchanged. This identifier is consumed and must not be reused.
A fresh successor must use a new identifier and prospective pin; its
mathematical thresholds and classes need not change for this code correction.
