# P-U-TWO-TRACE-PORT-CONTACTS-1: two contacts with a declared trace exchange

NON-CANONICAL, L1 construction candidate. No scientific execution is authorized until the complete accepted contract, primary and independent verifier are publicly committed, pushed and read back. The proposed result is a bounded two-use construction in an explicitly enlarged architecture. It is not a native derivation of the added operation, an indefinitely reusable apparatus, or a full SUM gate.

## 1. One admitted architectural resource

Admit an addressed reversible exchange between a supplied source pentit s and the existing native selector trace `z(psi)=sum(psi) mod5` of one receiver cell. With `psi=(P,q,r)`, `P=(p1,p4,p1p,p4p)` and `kappa=sum(P)`, define on the complete product `F5 x F5^6`:

```text
C(s,(P,q,r)) = (kappa+q+r, (P,s-kappa-r,r)).
```

All displayed pentit arithmetic is modulo five. This is the coordinate SWAP `(s,z)<->(z,s)` in the invertible native chart `(P,q,r)<->(P,z,r)`. It is an involution on its entire domain, not merely on the prepared states. It changes no piston coordinate and no r coordinate. It neither computes a carry nor adds the source to an old memory value. The port z is the already declared trace used by the native selector, independently of the record target.

The admitted resource includes two fixed physical address roles, `S1:R1` and `S2:R2`, and their fixed activation at native counter values 0 and 6. Availability of this trace-port exchange and its address/clock control is the explicit architectural change. It is not claimed to be a word selected by original U. Its scalar formula uses the full receiver trace; no elementary two-body locality or physical interaction duration is inferred from calling the receiver a cell.

## 2. Complete carrier and preparation

The complete state is exactly

`omega=(n,s1,s2,psi1,psi2) in N0 x F5 x F5 x F5^6 x F5^6`.

There are fourteen pentit coordinates and the one original-style monotone counter. At a fixed counter the complete admitted carrier has `5^14` states. The receivers and the two stored input ports are real factors of this enlarged mathematical carrier; they are not renamed coordinates inside one original checkpoint. There is no battery, hidden source copy, auxiliary register, movable head, reset flag, phase bit or variable programme outside this displayed state. The fixed address schedule is part of the declared transition law.

Choose independent input labels `a1,a2 in {0,1,2,3,4}`. All 25 pairs are admitted. Let `rho=(0,0,0,0,1,0)`. The common preparation is

`E(a1,a2)=(0,a1+1 mod5,a2+1 mod5,rho,rho)`.

Both receiver preparations are identical and independent of both inputs. The source encoding is the same affine bijection `a -> a+1` used by #987; it does not precompute the carry predicate. The sources are prepared together in two counted five-state ports. S2 is not used or changed until its time-six contact. Causal independence permits its value to be specified independently of the first source; this model does not supply a separate physical arrival/reloading mechanism at time six.

Two common prepared receivers and two input ports are paid initial resources. No receiver is created, reset, exchanged out, stopped or restored during this run. No further fresh receiver supply is assumed after the two contacts.

## 3. Complete enlarged transition law

Let `theta_n=popcount(n) mod2` and let `g0,...,g4` be exactly the original native generators a,b,c,d,e. From a boundary state at counter n:

1. At n=0, apply C to `(s1,psi1)`. At n=6, apply C to `(s2,psi2)`. At every other n, apply no exchange. The other source port and receiver are unchanged by this exchange stage.
2. For EACH receiver, evaluate the actual native selector on its state after that stage and set `psi_i'=g_(z(psi_i)+2theta_n mod5)(psi_i)`.
3. Retain the source ports from stage 1 and set `n'=n+1`.

This defines one autonomous discrete map on the displayed complete state. The exchange and the native updates form one explicitly enlarged update. Its algebraic pre/post-exchange snapshots are retained for audit; they are not claimed to be separate elapsed native transitions or zero-duration physical pulses. At both contact updates the native selector sees the actual exchanged state. No native generator is chosen manually, and no clock is rewound. Between and after the two contacts the dynamics is the product of two actual U steps with static source ports and one shared counter.

The first three native driver bits are 011; those at n=6,7,8 are also 011. The first write is complete at n=3, before the second contact. The second receiver keeps evolving from n=0 throughout; it is not held in its original state.

## 4. Record interface and exact required result

For one receiver define the already existing #987 pointer and reader

`A(psi)=p1+p1p mod5`, `B(psi)=p4+p4p mod5`, `W(psi)=A(psi)^2 mod5`.

Read the two records by the SAME fixed source-independent map `(W(psi1),W(psi2))`. The reader has no access to a1,a2 or source-port values. It is fixed before execution and is not selected from endpoint data. Define the target unit-carry predicate on the integer representatives by `c(a)=floor((a+1)/5)`, equal to 1 only at a=4.

For every input pair the construction must satisfy:

- `W(psi1(n))=c(a1)` for every n>=3, including during and after the second contact.
- `W(psi2(n))=c(a2)` for every n>=9.
- The entire R2 boundary state at n=6 BEFORE its contact is the common source-independent `(2,1,3,4,0,4)`, with `(z,A,B)=(4,0,0)`.
- The exchange returns the old trace to its source slot: S1 becomes 1 at the first contact; S2 remains `a2+1` through the boundary at n=6 and becomes 4 at the second contact. These exports remain in the complete output.
- R1's entire trajectory is independent of a2. R2's trajectory before its contact is independent of both sources; its later trajectory is independent of a1.

The guarantee is two separately retained predicate records, not recovery of both five-valued sources, preservation of either original source value, a full adder, or a return of a used receiver to the input interface. Sources are consumed. Earlier transient pointer excursions do not count as completion or physical arrival events. Completion times are the fixed proved n=3 and n=9 boundaries; no extra completion flag is claimed.

## 5. Exact resource account and necessity boundary

The resources are two six-pentit native receiver carriers, two source pentits, one shared unbounded counter, two preassigned exchange address roles and two scheduled applications of the same new involution. Before the second contact there have been six actual steps of EACH receiver, including its three-step passive ready evolution after the first completion boundary. Through n=9 there are nine actual steps of EACH receiver and exactly two exchanges. The initial twelve receiver coordinates are common prepared resources, not free disposal sites that may be restored later.

The exchange alone is reversible. The composite apparatus generally is not: native U has the already exposed many-to-one trajectories of #987. Complete source consumption and complete-state collisions must be retained rather than hidden in a reduced output description.

Without either source exchange, both cells start in the synchronized set `X14={z=1 or4}` with W=0 and remain there with W=0 forever. More generally native continuation within X14 cannot change W. The necessary missing capability in this prepared port class is a source-dependent intervention that can leave that protected class, or a separately admitted fresh transient carrier. The chosen C provides the former on a counted unspent receiver, while leaving the earlier record's carrier alone. This is a restricted necessity statement, not a global minimum number of cells or a no-go for other readers/architectures.

## 6. Frozen exact audit, controls and failure rule

The primary verifier is newly authored; it imports no old scientific program. It retypes the current canonical full native generators and uses `n.bit_count()` for the actual selector. It must:

1. Check the generic exchange on every one of its 78125 source/receiver inputs: involution, exchanged trace/source, unchanged P,r and canonical output. This is the exact primitive's complete domain audit, not a new search over architectures.
2. Run all 25 independent input pairs under the fixed enlarged law through boundary n=9. Preserve all fourteen pentits and the counter at every boundary n=0,...,9, both actual selected indices for every native step, and complete pre/post snapshots of both exchanges.
3. Verify both recorded predicates, preservation of the first record from n=3, the complete common R2 ready state, source exports, all declared independence properties and the exact operation counts.
4. Retain the known complete collision between inputs `(a1,a2)=(0,0)` and `(1,0)` after the first native write, and at n=9, to prevent a false reversibility/source-preservation conclusion.
5. Run the separately labelled NO-EXCHANGE control on all 25 initial preparations, with the same native evolution and reader. Require both records remain zero, sources remain in their initial slots, and the control fails the target on an input containing a=4. This is a fixed negative-control law, not a selectable branch offered as part of the successful interaction.

All arithmetic is exact integers modulo five. No numerical embedding, randomized sampling, fit, target-dependent loading, post-run reader selection, alternate contact time or search for an improved table is allowed. Deterministic CSV/JSON evidence must be retained; no JSONL or log format is needed. Every evidence artifact must be below 5 MiB. The author output is deterministic UTF-8/LF JSON with computed evidence hashes and a trailing newline. The independently frozen verifier must be prepared before exposure to primary code. A coordinator wrapper may bind all accepted files and compare author/reviewer outputs; both execute only after the public pre-run pin.

Zero tolerance: any failed domain, source, selector, timing, independence, complete-state, primitive-inverse or retention assertion is a falsifier/STOP at its declared cause. Preserve the failed version and outputs. No target, time, carrier, reader, source encoding or threshold may change after the pin. Exact stdout becomes EXPECTED.txt only after a successful recorded execution. Required public architecture checks and independent proof review remain separate gates.

## 7. Lineage and explicit limits

The native nonlinear write, fixed W reader, quotient proof and X14 retention are inherited from public issue #987, particularly comments 5652485189 (original audit freeze) and 5652509288 (proof/outcome). Their status is NON-CANONICAL candidate-T for the analytical statements and candidate-C for the original local finite audit; no authority is raised by reuse. The current generators and counter/selector are the normative public v97 definitions at baseline `5e872c22a18043c8126945a982efad55472cea82`.

The new contribution is this explicit finite trace-exchange law, its complete state/resource account, and the two sequential contacts with a freely evolving second ready cell under a proved calendar. No CSUM is assumed, no Omega24 battery/helper circuit is reconstructed, and #1349's source-preserving SUM and full source/counter-holding contract are not discharged. The prior full-product single-checkpoint capacity and literal-clock window boundaries are respected by declaring a larger carrier and a changed contact update.

The added trace exchange, preparation of the two cells/input ports and hardware addressing have NOT been derived from the original single-cell U or from a physical Hamiltonian. Their physical availability, locality, energy, error tolerance, physical arrival semantics, reset and indefinite renewal remain open. A successful mathematical construction establishes exactly the admitted two-use architecture, not a realized physical apparatus.
