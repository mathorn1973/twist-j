# One early flag measurement followed by the original-port output

**NON-CANONICAL, L1, conditional analytical candidate-T. Independent
acceptance pending.** Author: A. M. Thorn. Date: 2026-10-25.
License: Apache-2.0.

This is a new, separately stated consequence of the supplied autonomous
history construction. It leaves the frozen 21-obligation package unchanged.
It adds one explicitly supplied ideal projective measurement of its first
flag. The measurement changes the clock distribution, but the accepted
final payload still has the same completed word. This statement supplies
neither an autonomous detector nor an energy account for that intervention.

No scientific executable, numerical simulation or physical experiment was
run. Same-session analytical checks are not independent acceptance. The
separate reported 24-obligation repeated-writing package is not a premise
or an object of review here.

## 1. Exact inherited premises and the new operation

Use the complete apparatus, raw Hamiltonian, input family and fixed physical
ports of
[STATIC_CONTROLLER](../C-AUTONOMOUS-ORIGINAL-PORT-SOURCE-N/STATIC_CONTROLLER.md)
and
[THERMAL_CHANNEL](../C-AUTONOMOUS-ORIGINAL-PORT-SOURCE-N/THERMAL_CHANNEL.md).
Their source preparation and three-step target retain their conditional
dependence on the unchanged predecessor and the active-source identities
of [#1775](https://github.com/mathorn1973/twist-j/issues/1775#issuecomment-6399173427).
The source package's independent acceptance is not supplied by this note.

Write the two physical flag projectors as A and B_f. Set

```text
z=2^(-k-1),  k>=8,
beta=exp(-3B/32)<z/4,
gamma=(3/4)^(6B)<beta,
eta=D(rho_th,rho_0)<=z,
xi=M(2/3)^r<z.                                      (M1)
```

Here B is the padding integer, K=12B, rho_th is the actual complete
thermal input, and rho_0 its cold-ground comparison. The latter retains
all hot donors, mixed zero-energy helpers, information and reference.
Its fuel-excited active component has weight 1/3; its fuel-ground
component has weight 2/3 and is dormant. None of the actual thermal or
reset-failure branches is removed from the experiment.

Fix, before observing any result, an early time t_A in the exact interval
I_src of THERMAL_CHANNEL (T20), and a later time t_B in [T_h,2T_h].
The first interval precedes T_h. Define U_H(t)=exp(-iHt/hbar).
At t_A apply the two-outcome ideal Lueders instrument

```text
rho -> A rho A,   rho -> (I-A) rho (I-A).             (M2)
```

Continue both branches under the same U_H(t_B-t_A). At t_B read B_f.
Thus all four outcome pairs (a,b) are retained in a complete instrument.
For a=b=1 its Kraus operator on the apparatus is

```text
K_11=B_f U_H(t_B-t_A) A U_H(t_A).                    (M3)
```

Every map acts as identity on the passive reference. Classical labels a,b
are outcome labels of the supplied instrument; their physical detector,
storage and preparation costs are not included in the autonomous source
inventory. A receiver measurement at t_B may refine b=1 into P_W and
I-P_W, retaining every complementary outcome.

## 2. Why the measurement acts only on the history coordinate

Let K_in be the admissible active input space, including the hot-donor
and helper configurations and all permitted information inputs. The
history isometries V_j from STATIC_CONTROLLER Section 7 give an isometry

```text
V: C^(K+1) tensor K_in -> H_apparatus,
V(|j> tensor v)=V_j v.                              (M4)
```

Distinct j have orthogonal cursor/fuel configurations. Each V_j is an
isometry on the whole K_in, including unsuccessful reset configurations;
the exact raw gates do not select successful cooling. The restriction of
the propagation Hamiltonian is

```text
V* H_prop V = h_clk tensor I,
h_clk = g I - sum_j a_j(|j+1><j|+|j><j+1|).           (M5)
```

The bare free factor also has to be checked. Put E_in=V_0*H_0 V_0.
Each legal edge conserves H_0, so H_0 V_j=V_j E_in. Consequently

```text
V* H V = h_clk tensor I + I tensor E_in.             (M6)
```

The active comparison input Sigma, including its reference extension,
commutes with E_in: the thermal hardware is diagonal, the setting has
zero gap, and the old-memory code has one constant bare energy. Hence
the free E_in evolution cancels on this density even with the inserted
measurements below. This cancellation is not asserted for an arbitrary
raw input outside that declared family.

On the history range the *physical* flag projectors are exactly

```text
V* A V   = P_A tensor I,   P_A=sum_(j>=2B)|j><j|,
V* B_f V = P_B tensor I,   P_B=sum_(j>=6B)|j><j|.      (M7)
```

The range is therefore preserved by both measurements, as well as by
H. This fact is stronger than an estimate on a generic measurement
disturbance. In the coordinates (M4), the unnormalized accepted active
state is

```text
|phi_11><phi_11| tensor Sigma,
phi_11=P_B exp(-i h_clk(t_B-t_A)/hbar)
             P_A exp(-i h_clk t_A/hbar)|0>.          (M8)
```

In particular its weight r_11=||phi_11||^2 is independent of the unknown
memory, setting, reference and reset outcome. Subsequent interference
between history nodes is retained in phi_11; no classical trajectory
approximation or independence of the two readings has been used.

## 3. A joint completion bound from one thermal launch

Let psi_A=exp(-i h_clk t_A/hbar)|0> and
q_A=||(I-P_A)psi_A||^2. The unchanged early tail estimate gives
q_A<=beta. The unmeasured final tail estimate gives

```text
w_B=||P_B exp(-i h_clk(t_B-t_A)/hbar)psi_A||^2
   >=1-gamma.                                       (M9)
```

Subtract the omitted vector (I-P_A)psi_A before this final propagation.
Unitarity and the projector contraction, followed by the triangle
inequality, yield

```text
sqrt(r_11) >= sqrt(w_B)-sqrt(q_A),
r_11 >= (sqrt(1-gamma)-sqrt(beta))^2
      >= 1-gamma-2sqrt(beta).                        (M10)
```

The quantities in the first square-root difference are ordered because
beta+gamma<1. This is a bound for the *modified* measured history, not a
reuse of its old binomial law. With k>=8, beta<1/2048 and sqrt(beta)<1/32,
so

```text
r_11 > 1-1/2048-1/16 = 1919/2048 > 7/8.             (M11)
```

The dormant comparison branch never produces a=1. Its accepted weight
is zero. Thus the comparison probability of the joint event is exactly
r_11/3. Contractivity of the complete four-outcome instrument applied to
rho_th and rho_0 gives

```text
p_11:=Pr_actual(a=1,b=1) >= r_11/3-eta
    > 7/24-1/512 > 1/4.                            (M12)
```

There is one factor 1/3 for fuel activation. Neither a product of the two
old bounds 1/4 nor a second independent activation factor is inserted.
The first reading's marginal is exactly the first instrument in the
original theorem, so its original source-ready statement remains valid
at t_A. It does not make A a permanent readiness certificate.

## 4. The same completed payload after both accepted readings

At every history node j>=6B, both excursions are complete. The reverse
SWAP identities have restored all future copies to their original sites,
and the same complete payload word acts on the original row. The tail
after node 6B is identity on that payload. Therefore tracing the clock
and unused hardware in the normalized state (M8) gives precisely the
same endpoint channel E_fin as in the *unmeasured cold comparison*.
Only its probability has changed.

The donor-inclusive reset estimate (T16), propagated through that full
word, consequently gives

```text
D(E_fin(rho_info), P_fin(rho_info)) <= xi,            (M13)
```

where P_fin=Ad_(U_rec^3) o P_src and all original source, setting,
receiver and reference factors have the same meanings as before.
This includes coherent setting blocks and arbitrary admitted
memory/reference correlations. No successful-reset conditioning is
added at this step.

The endpoint states in (M13)-(M15) are reduced to these original source,
setting, receiver and reference factors. They are not a claim that the
entire apparatus, clock or spent donors equal the ideal endpoint state.

For completeness, the normalization estimate can be applied to the
single accepted pair (1,1) and the aggregate of all other outcomes.
Let sigma,tau be their accepted substates for actual and comparison
inputs, p=Tr sigma and p_0=Tr tau=r_11/3. The complete instrument gives

```text
(||sigma-tau||_1+|p-p_0|)/2 <= eta.
```

Writing sigma/p-tau/p_0 as
(sigma-tau)/p_0 + sigma(1/p-1/p_0) proves
D(sigma/p,tau/p_0)<=eta/p_0. Since eta<p_0 by (M11), both accepted
states are defined. Together with (M13) this yields

```text
delta_11:=D(rho_actual|(a,b)=(1,1), P_fin(rho_info))
         <= xi+3eta/r_11
         < (31/7)z < 6z.                            (M14)
```

Thus k=40 still suffices for the separate measured-continuation claim

```text
p_11>1/4,       delta_11<6*2^(-41).                 (M15)
```

The square-root disturbance in (M10) affects the completion denominator.
It is not added as a payload error: (M7)-(M8) and the common completed
word prove the stronger endpoint statement. Without those identities,
an appeal to a gentle-measurement estimate alone would not prove (M14).

## 5. Receiver contrast and its conditioning

Preparation and the joint-state result are valid on the full 26-state
memory code. Recognition of a new write by P_W=|d0><d0| and the claimed
contrast retain the original restriction K_mem=span(d1,...,d25).

For the two separately supplied settings C=0 and C=1, the inherited
ideal contrast is Delta_p>1/50. The complete reference-uniform endpoint
bound implies

```text
Pr_+(P_W|a=b=1)-Pr_-(P_W|a=b=1)
   >1/50-12z>1/100                         (k=40).   (M16)
```

For the retained Gibbs-setting variant C=I/2, initially independent of
the old memory/reference, the ideal target P_fin(rho_info) in (M14)
assigns probability 1/2 to each setting. The clock factor r_11 is
setting independent. Apply a final setting instrument to (M14) and
normalize against those ideal masses. This costs at most a factor
two in delta_11 for each setting; no separate claim that every
reset-failure branch preserves the setting is needed. Hence its setting-conditioned
contrast exceeds 1/50-24z>1/100 at k=40. An arbitrarily rare outcome of
a general coherent setting is not covered by that denominator.

There is also an unconditioned joint-event statement. Clock independence
and (M13) give, for the same two supplied settings,

```text
Pr_+(a=b=1,P_W)-Pr_-(a=b=1,P_W)
 >= (r_11/3)Delta_p-2(r_11 xi/3+eta)
 > 7/1200-8z/3 > 1/200                    (k=40).   (M17)
```

Here r_11<=1 was used in the error term, and 2^41>3200 suffices for the
last strict inequality. The flag pair is completion information; it
is not the successful-write event P_W.

## 6. Scope of the added result

The new statement is a two-time instrument theorem for one use of the
supplied apparatus. It proves a final endpoint after a specified early
flag measurement. The original warning about concatenating two
unmeasured cuts without a new proof remains correct; (M4)-(M14) are
the additional proof in this restricted ideal-instrument case.

The operation (M2) is an extra physical assumption. Its projector commutes
with the bare H_0 but generally not with the full H; its apparatus,
work, disturbance of interaction energy, time control and output storage
are not derived or funded here. No further measurement of the source,
clock position, receiver or reset donors is inserted at t_A. Such an
operation would require its own history and channel analysis.

In particular this note does not assert the old exact 3T_h return for
the measured process, permanent retention, renewed resources, a second
write, an autonomous detector, a source derived from the six-pentit rule,
or identification of the conserved occupation energy with Q. None of
those conclusions follows from the near-unit active joint weight.

## 7. Separate review obligations

These eight obligations belong to this new analytical note. They do not
replace or enlarge the frozen 20-, 21- or reported 24-obligation lists.

1. Verify the source pins, admitted information family, two prescribed
   time windows and all four bounds in (M1), without importing acceptance
   from PR #1770 or treating reset failure as a discarded branch.
2. Verify the whole-input history isometry, H_0 intertwining and
   density-level free-factor cancellation in (M4)-(M6), including arbitrary
   passive references and the actual hot/helper mixture.
3. Verify that the physical Lueders A and B_f projectors restrict exactly
   as (M7), preserve the history range and give the ordered joint Kraus
   operator (M3), with the complete complementary outcome instrument.
4. Verify the vector norm estimate (M10), its positive-root condition,
   the constant 7/8 and the single-launch probability (M12), without
   assuming independent readings or a binomial law after measurement.
5. Verify the common payload word for every accepted final node, the
   restoration of future copies and reference-uniform estimate (M13).
   Check why clock disturbance does not add a payload error here.
6. Verify complete-instrument contraction, the denominator r_11/3,
   normalization algebra and (M14)-(M15) for the true thermal input.
7. Verify both setting conventions, the 26-state versus 25-state scope,
   and the conditional and unconditioned contrast bounds (M16)-(M17).
8. Check that the ideal measurement is explicitly added and that its
   detector, work and storage are not represented as already funded;
   preserve the separate recurrence, repeated-write and native-energy
   obligations and the unchanged status of all source packages.
