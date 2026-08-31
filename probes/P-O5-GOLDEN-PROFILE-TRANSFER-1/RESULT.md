# P-O5-GOLDEN-PROFILE-TRANSFER-1 result

Status: **CANDIDATE-T / PROOF-FIRST / LOCAL FORMAL LEG PASS / PUBLIC TWO-ARCHITECTURE REPLAY PENDING / CANON UNCHANGED**

## Verdict

The frozen written proof survives the accepted exact audit.

Put

```text
alpha=phi^2,
X_k=L_(2k)-1=floor(alpha^k),
M_k=floor(X_k/11),
r_k=X_k-11M_k.
```

The cutoff geometry obeys

```text
X_(k+1)=3X_k-X_(k-1)+1,
r_k mod 11=(1,2,6,6,2) periodically,
M_(k+1)-3M_k+M_(k-1)=c_k,
(c_1,c_2,c_3,c_4,c_5)=(0,1,1,0,0),
```

and the resulting homogeneous order-seven recurrence frozen in `PREREG.md`.
This is a fixed finite recurrence for cutoff geometry, not for the signed
amplitude.

For the complete golden shells, exact shell index `kappa` and reduced
mantissa `z`, multiplication is the one-carry skew product

```text
epsilon=0 if z(a)z(b)<=alpha, else 1,
kappa(ab)=kappa(a)+kappa(b)+epsilon,
z(ab)=z(a)z(b)alpha^(-epsilon).
```

This includes the unit shell. Every finite signed shell pairing is exactly a
pairing of the two sparse profiles against

```text
K_T(x,y)=1_(xy<=T).
```

At `N=X_K`, the three nontrivial boundary thresholds are exactly

```text
T_K^+     = alpha-alpha^(1-K)+alpha^(1-2K),
T_(K,3)^- = [alpha^3+alpha^(3-2K)
              -(1+r_K)alpha^(3-K)]/11,
T_(K,4)^- = alpha T_(K,3)^-.
```

The two lower boundary terms use complementary kernels `1-K_T`. The profile
therefore reconstructs the four-diagonal form at each fixed Lucas-top cutoff,
but it is not a uniformly finite-dimensional state.

The scalar closure fails on the frozen natural finite-selector class. The two
sequences

```text
f=-delta_19,
g=-delta_41
```

have the same complete shell-mass sequence and the same complete diagonal
scalars, yet

```text
Q_f(842)=1,
Q_g(842)=0.
```

Thus no readout from only those complete scalar masses determines the annulus
universally on that class. This does not exclude a special recurrence for the
one actual restricted Mobius sequence or a summary retaining within-shell
information.

For the actual restricted Mobius carrier,

```text
(Q_11(X_4),Q_11(X_5),Q_11(X_6))=(-8,-22,-52),
```

whereas the directly inherited Lucas rule with `c_5=0` predicts `-58`. Only
that naive inherited rule is excluded.

## Accepted exact audit

```text
pin_commit:       07d017ccec9ea533a8643b1f20283023f41774a3
verifier_sha256:  c3bae78f402be52deb583cf7ac94db9c34f8e3a0bb3a750b7eb4283037d70963
stdout_sha256:    8bee1581eb97ee521108e124ae354aafe8292442574d04ac96f84ffeb783f46a
stdout_bytes:     419
stdout_lines:     9
exit_code:        0
stderr_bytes:     0
readout:          VERIFY RESULT 8/8 ALL PASS
```

Frozen breakers fired at their preregistered witnesses:

```text
B1 deleted +1 in the cutoff recurrence:       k=1, 5 instead of 6
B2 forced zero multiplication carry:          41^2, shell 6 instead of 7
B3 replaced profile kernel by scalar mass:    -delta_41 at Y=842, 1 vs 0
B4 replaced period five by period four:       k=4, 1 instead of 2
B5 imposed the naive actual-Q recurrence:     -58 instead of -52
```

## Scientific boundary

The cutoff recurrence, residue cycle, multiplication skew product, exact
profile-kernel representation, Lucas-top thresholds, scalar shell-mass no-go
on the frozen class and the displayed naive-recurrence failure are
`candidate-T`.

The cancellation estimate remains open. No RH or GRH result, summatory
estimate, spectral-radius bound, contraction, zero-free region, analytic
continuation, fixed-dimensional closure for the actual restricted Mobius
sequence, selected orientation, physical dictionary, probability statement,
SI statement or L1-L6 lift is claimed.

Public Canon v67, Registry, Frontier, dependencies, gates, evidence, Notes and
all existing public rows remain unchanged.
