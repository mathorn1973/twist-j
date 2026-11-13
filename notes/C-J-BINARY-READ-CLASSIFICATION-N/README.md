# Complete binary classification of periodic J-world readers

**C-J-BINARY-READ-CLASSIFICATION-N. NON-CANONICAL, L1.**

For the finite quotient R_n(u)=O/(u^n-1) with tick x->u*x, this note
classifies every horizon n at which a freely selected invariant support,
with a fixed labeling and a uniform start, produces an exact uniform binary
n-word.

```text
u = J        exists exactly for n not in {1, 5}
u = phi^-1   exists exactly for n not in {1, 2, 3, 4, 5, 7}
```

J=zeta*phi^-1, so the two units share modulus and growth. They differ only
in finite exceptions. This is a preparation-capacity statement about finite
closed J-worlds. It is not a native sampler, a Born occurrence law, an
apparatus or a layer lift.

- [PREREG.md](PREREG.md) freezes the claim, the exposure record, the
  decision rules, the certificates and the failure threshold before any
  execution.
- [PROOF.md](PROOF.md) is self-contained. It restates the cycle criterion,
  the c=n construction and the tail onset from draft pull request #1727,
  specialized to two letters.
- verify.py is the proof-structured exact audit, break.py the code-distinct
  attempt to break it, and compare.py checks that their rows agree.
