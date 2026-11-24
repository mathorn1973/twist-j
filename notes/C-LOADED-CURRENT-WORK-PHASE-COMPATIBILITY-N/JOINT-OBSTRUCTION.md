# Joint preparation: residue supply, retained information and recurrence

**NON-CANONICAL / L1. Conditional analytical candidate-T. Hand proofs; no new execution or independent acceptance.**

This note bounds the ordinary-contact/swap constructions in JOINT-CONSTRUCTION.md. It does not assert that common-phase covariance forbids relative alignment. The positive construction aligns a source with an initially prepared reference while retaining the old relative phase in the used helper.

## 1. A residue invariant stronger than account and total sum

Put `lambda=1-j`. The quotient is

    O/(lambda) = F5,
    epsilon(c0+c1*j+c2*j^2+c3*j^3)=c0+c1+c2+c3 modulo5.

Indeed setting j=1 in Phi_5 gives 5. For an admitted contact, with relative coordinate t in O,

    p'=p+(rho-1)t,       q'=q-(rho-1)t,
    rho-1=-lambda(1+j).

Consequently each contacted slot retains its own epsilon value. A refused contact is identity and has the same property. Slot swaps only permute these values. Every fixed word therefore preserves the complete multiset of slot residues. This remains true for any sequence chosen by a controller, since every actual primitive preserves that multiset. All participating O slots, including controller or funding slots if used, must be counted.

For the supplied reference bank `B(h)` with `a_k=b_k=-h*j^k` and `h=j^s`, all ten references have epsilon=-1. A blank slot has epsilon=0, as does every lambda-divisible funding slot. Such funding cannot create the missing nonzero residues, regardless of its Q account. Returning any extra auxiliaries unchanged cannot help: their common residue multiset cancels from the initial/final comparison.

This is a preparation obstruction, not a phase-selection law. Every j^r has epsilon=1, so this invariant does not distinguish the five root phases or prohibit the positive aligning word.

### An equal-account, equal-sum counterexample

Use twelve slots and the exact preparation

    z_in=(1,-1,lambda,-lambda,lambda,-lambda,0,0,0,0,0,0).

The proposed target is

    z_ready=(1,-1,a_0,b_0,...,a_4,b_4),
    a_k=b_k=-j^k.

Since Q(1)=2 and Q(lambda)=5, both states have account24. Both have exact total ring sum zero. The initial ten prospective reference slots contain four lambda-divisible funding values and six zeros; they are not an already prepared reference bank.

In residue order 0,1,2,3,4 their histograms are

    z_in:    (10,1,0,0,1),
    z_ready: ( 0,1,0,0,11).

No ordinary-contact/swap word connects them. In particular sufficient numerical account and neutrality do not supply the required reference preparation. Padding both states with identical vacant slots gives the same obstruction when more clock or funding ports are retained. A bank that is literally blank with four separate lambda-funding slots gives the analogous sixteen-slot example.

A legitimate transport operation does not contradict this result. Swapping an already supplied nonzero donor pair into vacant ports moves its residues and leaves its old ports empty; it does not create another copy or return the donor still occupied. The donor state and any correlations it supplies remain preparation resources.

## 2. Relative alignment is allowed, clean erasure is not

Fix one reference phase h and five distinct source preparations `(j^r,-j^r)`, with all other initial states common. Let F be any complete bijection obtained from the declared primitives. Suppose the final source and all retained visible references are the same for every r. Then the remaining final state must take at least five different values. Otherwise two distinct inputs would have the same complete output, contradicting injectivity.

Thus alignment cannot also return every helper, archive, controller and reference to one common state unless some other retained degree of freedom records the initial distinction. This is a five-state information lower bound, not a bound on physical bits, energy, slot count or a universally minimal garbage device.

The new one-helper construction attains that cardinality bound on its prepared family. With source phase r and helper phase s, its fixed word gives

    P(r,s)=(s,2s-r) modulo5.

For fixed s, the five helper outputs are distinct. The source now agrees with the initial helper phase, or with a separately retained bank B(j^s); it does not generally agree with the used helper's new phase. The old difference is preserved:

    r_out-s_out=r-s.

The complete account is8 on four slots with zero total ring sum; adding the untouched bank gives28 on fourteen slots. These are supplied preparations, not derivations of the helper or bank from blank resources.

For the word proof, before block K^k the difference is `r-s+2k`. If r=s, none of the blocks k=1,...,4 hits. Otherwise precisely one does. Its simultaneous source/helper advance is `2k=s-r`, while the five source-only contacts total zero modulo5. This proves the displayed map and avoids counting a nonexistent hit at k=0.

The equal-thirty-contact family described in JOINT-CONSTRUCTION.md has

    P_t(r,s)=(s+t,2s+t-r).

All five choices have the same prepared account and contact count. They align the source to different offsets relative to the unchanged bank. The chosen word and its reference preparation are therefore selection data. A controller can implement a definite relative alignment; covariance alone neither prohibits it nor selects its offset.

## 3. The autonomous finite-carrier limit

Fix N and a finite total account E for O^N. If c_i is any power-basis coefficient of one slot, positivity of Q and its exact coefficient bound give

    c_i^2 <= 4Q(slot)/5 <= 4E/5.

The account shell is therefore finite. Add a finite calendar or controller and assume that its COMPLETE joint transition with the O slots is a bijection. The resulting autonomous map is a permutation of a finite state set.

Every orbit is periodic from its starting point. It cannot converge to a different complete state: convergence on a finite set would be eventual constancy, and an invertible orbit cannot enter a fixed point from outside. More generally a forward-invariant subset A satisfies F(A)=A, by finiteness and injectivity. No state outside A can enter it. Applying this to the set of states whose present and all future visible phases are aligned excludes permanent attracting alignment from a previously unaligned state under this complete finite autonomous contract.

A finite controller is not automatically reversible. If it overwrites branch information, its joint transition needs a separate inverse or a retained record before this permutation argument applies. Conversely, merely observing a many-to-one subsystem reading does not establish loss of complete-state information.

The constructive word P is a controlled endpoint map, not an attractor. On its prepared family, with d=r-s,

    P^n(r,s)=(r-n*d,s-n*d),       P^5=I.

For d nonzero the original bank alignment occurs after one application and is lost on the next; the helper carries the missing history. The same finite recurrence prevents a genuinely irreversible reset. Externally stopping the word at its read cut is consistent with the construction, but supplies a stopping schedule rather than autonomous convergence.

The theorem does not cover unbounded calendars, growing memory, added reservoirs, an unrestricted rational field carrier, or different primitives. It also does not rule out finite-time alignment with garbage, approximate statistics, or a preparation followed by an externally selected observation cut. The native common-phase symmetry on O is the torsion-unit group `{+j^s,-j^s}`; arbitrary continuous U(1) rotations need not remain in this integral carrier.

## 4. Existing transport and arithmetic keep their separate scope

The completed [common-clock transport construction in #1934](https://github.com/mathorn1973/twist-j/issues/1934#issuecomment-6705242023) already prepares transported reference pairs using the same actual clock as the signal. It explicitly supplies the donor pairs, returns the common transport core blank between loads, and retains the complete resources. Its reported account324, and the conditional account224 corollary using the smaller stock, are distinct constructions. The residue invariant does not invalidate transport; it explains why transport of supplied resources is different from creation of a bank from residue-zero funding.

The [separate native-selector arithmetic task #1937](https://github.com/mathorn1973/twist-j/issues/1937) uses prepared native U cells and explicitly does not claim that original U is globally invertible. This note neither takes over nor audits that task. Its operations are not silently placed inside the ordinary-contact/swap permutation class proved above.

The result is a bounded separation: native reversible dynamics can relocate phase information and align a source at a chosen cut, but account alone does not prepare the reference, complete reversibility does not erase the old relative phase, and finite autonomous recurrence does not select an attracting physical phase law. None of these statements derives an action normalization or electromagnetic coupling.
