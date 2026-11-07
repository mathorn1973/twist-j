# Composing the supplied five-contact reader with the root clock

**NON-CANONICAL / L1. Conditional analytical candidate-T. Proof-only composition; no new finite audit or independent scientific acceptance.**

The supplied #1925 reader can read the five actual clock laws of this note with a neutral total preparation of account 24. This uses a labelled relational readout, not the single terminal-stock-Q readout optimized in STOCK-RESULT.md. Neither construction selects an absolute phase assignment.

## 1. Premises and source custody

The reader definitions and its existing reported outcome are public in the [completed construction in issue #1925](https://github.com/mathorn1973/twist-j/issues/1925#issuecomment-6683808099). The source is credited there; this note does not re-own or newly discover that reader, its work-source composition, or its separate two-arm construction.

The reported standalone bundle head 1e671e59043238e4e37ed90f2fb32acef543ba82 is not a commit available in the public scientific repository. This note neither imports nor claims to have replayed that bundle. Its exact readout rule is derived below directly from the supplied definitions and the ordinary contact law.

The clock premise is [RECEIVER-DYNAMICS.md at 3d8d364cb981bb5d53bbede432fb5a4ac4181709](https://github.com/mathorn1973/twist-j/blob/3d8d364cb981bb5d53bbede432fb5a4ac4181709/notes/C-LOADED-CURRENT-WORK-PHASE-COMPATIBILITY-N/RECEIVER-DYNAMICS.md). All earlier frozen sources, manifests and results remain unchanged. The existing receiver and stock audits did not execute the new combined twenty-slot apparatus.

Write O=Z[j], j^5=1 with j primitive, rho=j^2, and Q(a)=Tr(a abar)/2. Ordinary C(p,q) is identity unless p-q belongs to 2O. On admission, it rotates the relative coordinate by rho, preserving p+q and Q(p)+Q(q). It is a total bijection with C^-1=C^4.

## 2. The reference bank and its complete reading

At the reading cut let the known pointer pair be

    (p,q)=(j^r,-j^r),        r in {0,1,2,3,4}.

Append ten separate reference slots

    a_k=b_k=-j^k,            k=0,...,4,

and execute C(p,a_0), C(p,a_1), ..., C(p,a_4), in this order. Every b_k and q is retained and untouched.

The residues of j^k modulo 2 are distinct. Before k=r, each contact refuses. At k=r the contacted pair is (j^r,-j^r), so p becomes j^(r+2) and a_r becomes -j^(r+2). Consequently

    a_r-b_r=(1-rho)j^r,      Q(a_r-b_r)=5.

If a further matching label r+2 lies ahead in the calendar, that contact repeats this rotation. Once the matching label wraps past 4 it is already behind the reader and no further hit occurs. Thus the changed indices are exactly

    M_r={r+2h : h>=0 and r+2h<=4}.

At every changed k, a_k=-j^(k+2), while b_k=-j^k. Every changed difference has Q=5. All other differences remain zero. Define the terminal labelled vector D(r) by D_k(r)=Q(a_k-b_k):

| r | D(r) |
|---|---|
| 0 | (5,0,5,0,5) |
| 1 | (0,5,0,5,0) |
| 2 | (0,0,5,0,5) |
| 3 | (0,0,0,5,0) |
| 4 | (0,0,0,0,5) |

The first nonzero index is r, so the reading is injective.

All twelve individual slot accounts are 2 on this untranslated prepared family, both before and after reading. The record resides in relations between slots. The five difference accounts are observables, not extra occupied slots or new account debits. Their scalar sum is (15,10,10,5,5) for r=0,...,4 and does not identify r. This construction therefore does not supply the same one-slot-Q output contract as the optimized stock receiver.

Reversing the five edges and replacing each contact by four copies gives twenty contacts and restores every reader slot. This inverse holds on arbitrary occupied inputs because C^-1=C^4. In the prepared family it restores the pointer while erasing the new reference record. There is no nondisturbing forward read or retained-record reset.

## 3. A neutral account-24 clock-and-reader preparation

The bank is neutral:

    sum_k(a_k+b_k)=-2 sum_k j^k=0.

Its account is ten times Q(1)=2, hence 20. The five-neutral-pair clock starts from amplitudes e_0 and has ten retained slots, account 4 and zero ring sum. Adding the bank before the clock runs, and leaving it idle until the reading cut, gives

    total account=4+20=24,       total ring sum=0.        (N1)

There are twenty cyclotomic slots: all ten clock slots and all ten references. A standalone known pointer pair with the same bank has twelve slots and the same account 24; it is not the complete five-pair clock. The preparation account excludes a physical detector or an independently derived autonomous controller.

The specified clock laws are V_m=j^m V, with V(z_0,...,z_4)=(jz_4,z_0,...,z_3). For a prescribed nonnegative tick count n,

    V_m^n e_0 = j^(mn+floor(n/5)) e_(n mod 5).           (N2)

Indeed each wrap contributes one j and each tick contributes j^m. The occupied port n mod 5 is known independently of m. Attach the same five-contact reader there, retaining all other clock slots.

The terminal reference vector is therefore

    D((mn+floor(n/5)) mod 5).                           (N3)

After one actual tick the first changed index is m. After thirteen actual ticks it is (2+3m) mod 5, with indices (2,0,3,1,4) for m=0,...,4. Both tests distinguish the five actual laws. Thirteen remains a supplied horizon, not a value inferred from the field controller.

More generally this endpoint experiment distinguishes all five laws exactly when 5 does not divide n. If 5 divides n, their complete clock states at this cut coincide, and the previously idle identical bank produces identical outputs. This last statement concerns this endpoint experiment; it does not exclude an additional apparatus that recorded an earlier history.

The full inverse first applies the twenty-contact reader inverse and then reverses the actual n clock words. All clock slots, references and account are restored; the newly created record is erased. Neither neutrality nor the smaller account creates a free repeatable measurement.

## 4. Two different receiver contracts

For the same account-4 prepared pointer or clock:

| Receiver attachment | Added account | Complete account | Complete ring sum | Reader forward / inverse |
|---|---:|---:|---|---:|
| Ten-reference bank of #1925 | 20 | 24 | 0 | 5 / 20 contacts |
| Stock T=1+2j-2j^3 | 22 | 26 | T | 10 / 40 contacts |
| Stock T and untouched -T | 44 | 48 | 0 | 10 / 40 contacts |

For the complete five-pair clock these rows retain respectively 20, 11 and 12 cyclotomic slots. The bank uses five labelled helper/reference differences, whereas the stock construction has one terminal-slot-Q output. A smaller account here costs more slots and uses a different reading. The last row is the declared single-spectator neutral completion, not a minimum over all neutral completions.

The exact stock minimum 22 remains valid only for its fixed ten-contact word, five prepared inputs and terminal-stock-Q output. The reference-bank construction does not belong to that class. Conversely 20 is a reference minimum only within the ten-nonzero-reference-slot template, not over all receivers.

The supplied #1924 composition remains a separate accounting statement: its already complete account 150 plus these same ten references gives 170 and preserves its work records. A zero-sum reference bank preserves whatever ring sum that source already has; it does not make an arbitrary nonneutral source neutral. Its work-law and conditional form-uniqueness results are not reopened by this comparison.

## 5. The frame remains relative

For u=+j^s or -j^s the total contact law satisfies C(up,uq)=uC(p,q), including refusal, and Q(ua)=Q(a). Multiplying the entire clock and reference bank by u therefore preserves every D_k and the first changed index.

More specifically rotate only the bank by j^s, keeping its marked indices and calendar fixed:

    a_k=b_k=-j^(k+s).

For input j^r the first matching label is (r-s) mod 5 and the full output is D((r-s) mod 5). Thus the combined experiment reads

    D((mn+floor(n/5)-s) mod 5).                         (N4)

This is a change of the argument of D, not a cyclic permutation of the displayed vector's components: the linear calendar stops at label 4.

All five bank orientations have account 20 and zero ring sum. Requiring minimal reference account, neutrality, reversibility and an input-independent contact word therefore does not select one orientation. The bank's phase values, marked labels, contact order, reading cut and interpretation remain declared preparation and interface data.

If five character names are assigned to exactly the same actual clock state and the same complete receiver preparation, this deterministic receiver gives exactly the same result. It distinguishes actual relative inputs, not names for an unchanged trajectory. The new composition supplies no physical coherent-phase law or electromagnetic normalization.

## 6. Evidence boundary

This note contains a symbolic composition proof and a direct derivation of the five reference patterns. Same-session analytical reviews checked its admission sequence, neutrality, complete account, inverse, clock endpoint law, and readout distinctions. These are authoring checks, not independent scientific acceptance.

No new scientific code was written or executed. No earlier candidate-C count is attributed to this combined apparatus. A separately specified and prospectively pinned finite audit would be required before reporting new finite execution evidence for it. No Canon, merge, release, physical phase or alpha claim is made.
