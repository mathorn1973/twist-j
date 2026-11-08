#!/usr/bin/env python3
"""Exact prospective replay of one supplied five-input contact word.

No search, numerical library, predecessor import, or input-dependent program.
The two arithmetic paths meet only at checkpoint comparisons and reporting.
"""

from hashlib import sha256
import json
from pathlib import Path


WORD_SHA256 = "6fed5cf015526726db5e47b060e583db00af77db21b54c5dbe47b79de78b65a7"
WORD_BYTES = 966
CONTACTS = 322
TS = (-2, -1, 0, 1, 2)
LABELS = {str(i + 1) + str(k + 1): (i, k)
          for i in range(6) for k in range(i + 1, 6)}


def encoded(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode("ascii")


def emit(kind, **fields):
    print(encoded(dict(kind=kind, **fields)).decode("ascii"))


# Path A: power basis 1,j,j^2,j^3, with Phi_5(j)=0.
def contact4(x, y):
    delta = tuple(x[i] - y[i] for i in range(4))
    if any(n % 2 for n in delta):
        return x, y, False
    a, b, c, d = (n // 2 for n in delta)
    rotated = (d - c, -c, a - c, b - c)  # j^2 * (x-y)/2
    mean = tuple((x[i] + y[i]) // 2 for i in range(4))
    return (tuple(mean[i] + rotated[i] for i in range(4)),
            tuple(mean[i] - rotated[i] for i in range(4)), True)


def preparation4(t):
    return ((t, 0, -t, 0), (-t, 0, t, 0),
            (1, -1, 0, 0), (1, -1, 0, 0), (1, 1, 0, -2), (2, 0, 0, 0))


def target4(t):
    return ((1 + t, -1, -t, 0), (1 - t, -1, t, 0),
            (0, 0, 0, 0), (0, 0, 0, 0), (1, 1, 0, -2), (2, 0, 0, 0))


def invariants4(state):
    ring_sum = tuple(sum(v[i] for v in state) for i in range(4))
    account = sum((5 * sum(a * a for a in v) - sum(v) ** 2) // 2 for v in state)
    residues = tuple(sum(v) % 5 for v in state)
    return ring_sum, account, residues


# Path B: Z^5 / Z(1,1,1,1,1), with minimum coefficient zero.
# Multiplication by j^2 is a cyclic rotation before quotient normalization.
def gauge5(v):
    minimum = min(v)
    return tuple(a - minimum for a in v)


def contact5(x, y):
    delta = [a - b for a, b in zip(x, y)]
    # A quotient class is even iff all representative coefficients have
    # the same parity. They need not themselves all be even in this gauge.
    if any((a - delta[0]) % 2 for a in delta):
        return x, y, False
    total = [a + b for a, b in zip(x, y)]
    rotated = delta[-2:] + delta[:-2]
    left = gauge5(tuple((a + b) // 2 for a, b in zip(total, rotated)))
    right = gauge5(tuple((a - b) // 2 for a, b in zip(total, rotated)))
    return left, right, True


def preparation5(t):
    u = (1, -1, 0, 0, 0)
    b = (1, 0, -1, 0, 0)
    return tuple(gauge5(v) for v in
                 (tuple(t * a for a in b), tuple(-t * a for a in b),
                  u, u, (1, 1, 0, -2, 0), (2, 0, 0, 0, 0)))


def target5(t):
    u = (1, -1, 0, 0, 0)
    b = (1, 0, -1, 0, 0)
    return tuple(gauge5(v) for v in
                 (tuple(a + t * c for a, c in zip(u, b)),
                  tuple(a - t * c for a, c in zip(u, b)),
                  (0, 0, 0, 0, 0), (0, 0, 0, 0, 0),
                  (1, 1, 0, -2, 0), (2, 0, 0, 0, 0)))


def invariants5(state):
    ring_sum = gauge5(tuple(sum(v[i] for v in state) for i in range(5)))
    account = sum(sum((v[i] - v[k]) ** 2
                      for i in range(5) for k in range(i + 1, 5)) // 2
                  for v in state)
    residues = tuple(sum(v) % 5 for v in state)
    return ring_sum, account, residues


def power4(v):
    return tuple(a - v[4] for a in v[:4])


def converted_invariants(value):
    ring_sum, account, residues = value
    return power4(ring_sum), account, residues


class Audit:
    def __init__(self):
        self.checks = 0
        self.failures = 0
        self.first_failures = []

    def require(self, condition, name, **context):
        self.checks += 1
        if not condition:
            self.failures += 1
            if len(self.first_failures) < 20:
                self.first_failures.append(dict(check=name, **context))

    def checkpoint(self, s4, s5, baseline4, baseline5, context):
        self.require(tuple(map(power4, s5)) == s4, "representations", **context)
        self.require(invariants4(s4) == baseline4, "power_invariants", **context)
        self.require(invariants5(s5) == baseline5, "cyclic_invariants", **context)
        self.require(converted_invariants(invariants5(s5)) == invariants4(s4),
                     "invariant_representations", **context)


def replay(audit, s4, s5, word, baseline4, baseline5, name, t, direction):
    trace = []
    trajectory = sha256()
    context = dict(word=name, t=t, direction=direction, step=0)
    audit.checkpoint(s4, s5, baseline4, baseline5, context)
    trajectory.update(encoded(s4) + b"\n")
    for step, (i, k) in enumerate(word, 1):
        before4, before5 = (s4[i], s4[k]), (s5[i], s5[k])
        x4, y4, admitted4 = contact4(*before4)
        x5, y5, admitted5 = contact5(*before5)
        changed4, changed5 = (x4, y4) != before4, (x5, y5) != before5
        context = dict(word=name, t=t, direction=direction, step=step)
        audit.require(admitted4 == admitted5, "admission", **context)
        audit.require(changed4 == changed5, "state_change", **context)
        audit.require(not changed4 or admitted4, "change_requires_admission", **context)
        next4, next5 = list(s4), list(s5)
        next4[i], next4[k] = x4, y4
        next5[i], next5[k] = x5, y5
        s4, s5 = tuple(next4), tuple(next5)
        audit.checkpoint(s4, s5, baseline4, baseline5, context)
        trace.append("C" if changed4 else "D" if admitted4 else "R")
        trajectory.update(encoded(s4) + b"\n")
    trace = "".join(trace)
    record = dict(contacts=len(word), admitted=len(trace) - trace.count("R"),
                  refused=trace.count("R"), diagonal=trace.count("D"),
                  changed=trace.count("C"),
                  branch_sha256=sha256(trace.encode("ascii")).hexdigest(),
                  trajectory_sha256=trajectory.hexdigest())
    return s4, s5, trace, record


def load_word():
    raw = Path(__file__).with_name("WORD.txt").read_bytes()
    if len(raw) != WORD_BYTES or sha256(raw).hexdigest() != WORD_SHA256:
        raise ValueError("WORD.txt custody mismatch")
    labels = raw.decode("ascii").split()
    if (len(labels) != CONTACTS or any(label not in LABELS for label in labels)
            or raw != (" ".join(labels) + "\n").encode("ascii")):
        raise ValueError("WORD.txt is not the frozen canonical labelled word")
    return tuple(LABELS[label] for label in labels)


def swapped_word(word):
    permutation = (1, 0, 2, 3, 4, 5)
    return tuple(tuple(sorted((permutation[i], permutation[k]))) for i, k in word)


def word_bytes(word):
    return (" ".join(str(i + 1) + str(k + 1) for i, k in word) + "\n").encode("ascii")


def main():
    word = load_word()
    sigma = swapped_word(word)
    audit = Audit()
    audit.require(swapped_word(sigma) == word, "sigma_involution")
    emit("SOURCE", word_sha256=WORD_SHA256, word_bytes=WORD_BYTES,
         contacts=CONTACTS, sigma_sha256=sha256(word_bytes(sigma)).hexdigest(),
         trace_alphabet=dict(C="admitted_state_change", D="admitted_diagonal", R="refused"))
    traces = {}
    for name, program in (("w", word), ("sigma_w", sigma)):
        inverse = tuple(edge for edge in reversed(program) for _ in range(4))
        for t in TS:
            start4, start5 = preparation4(t), preparation5(t)
            baseline4, baseline5 = invariants4(start4), invariants5(start5)
            expected_invariants = ((5, -1, 0, -2), 10 * t * t + 33,
                                   (0, 0, 0, 0, 0, 2))
            audit.require(baseline4 == expected_invariants,
                          "declared_preparation_invariants", word=name, t=t)
            end4, end5, forward_trace, forward = replay(
                audit, start4, start5, program, baseline4, baseline5, name, t, "forward")
            target_hit4, target_hit5 = end4 == target4(t), end5 == target5(t)
            audit.require(target_hit4, "complete_power_target", word=name, t=t,
                          observed=end4, expected=target4(t))
            audit.require(target_hit5, "complete_cyclic_target", word=name, t=t,
                          observed=end5, expected=target5(t))
            back4, back5, reverse_trace, backward = replay(
                audit, end4, end5, inverse, baseline4, baseline5, name, t, "inverse")
            recovered4, recovered5 = back4 == start4, back5 == start5
            audit.require(recovered4, "complete_power_inverse", word=name, t=t,
                          observed=back4, expected=start4)
            audit.require(recovered5, "complete_cyclic_inverse", word=name, t=t,
                          observed=back5, expected=start5)
            traces[name, t] = (forward_trace, reverse_trace)
            if name == "sigma_w":
                audit.require(traces[name, t] == traces["w", -t],
                              "sigma_branch_covariance", t=t)
            emit("REPLAY", word=name, t=t, endpoint=end4, recovered=back4,
                 full_target=target_hit4 and target_hit5,
                 full_inverse=recovered4 and recovered5,
                 initial_invariants=baseline4, forward=forward, inverse=backward,
                 forward_branch_trace=forward_trace)
    emit("RESULT", status="PASS" if audit.failures == 0 else "F",
         scope="NON-CANONICAL L1 fixed word, five preparations, complete six-slot equality",
         cases=10, checks=audit.checks, failures=audit.failures,
         first_failures=audit.first_failures)


if __name__ == "__main__":
    main()
