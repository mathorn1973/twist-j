# Result: selected two-wing law and complete five-setting Bell exclusion

PUBLIC; candidate-T, L1, NON-CANONICAL.
Probe: P-QDD-SELECTED-BIPARTITE-LAW-1.
Lock: https://github.com/mathorn1973/twist-j/issues/1095.
Verdict: SELECTED-BIPARTITE-LAW, conditional on the declared selections.
Public Canon v90 and the existing scientific registry are unchanged.

## Completed mathematical result

ETH-QDD-2 supplies a specified two-wing extension of ETH-QDD-1: tensor
carrier, fixed entangled preparation, the existing five local binary
instruments, independent external settings, complete records, renewal and
a normalized joint occurrence law. Its adopted source is

    phi=vec(G^-1)/2,  rho_Phi=phi phi* (G tensor G),
    G=I4-ones4/5,  Pr(x,y,a,b)=p_Phi(a,b|x,y)/25.

The five settings are unchanged from the predecessor. The complete joint
table is

| Settings | LOW,LOW | LOW,HIGH | HIGH,LOW | HIGH,HIGH |
| --- | ---: | ---: | ---: | ---: |
| x=y | 1/4 | 0 | 0 | 3/4 |
| x differs from y | 1/64 | 15/64 | 15/64 | 33/64 |

Both LOW marginals are 1/4. The full five-setting Bell statistic is

    B=2 sum_k p(LL|k,k)-sum_(k!=l) p(LL|k,l),

with all twenty ordered unequal pairs included. Every setting-independent
Bell-local response model satisfies B<=2, while the selected table gives
B=35/16. The proof covers arbitrary measurable hidden-variable refinements
and stochastic local responses by a complete convex reduction to the 1024
deterministic vertices. It does not restrict the original hidden-variable
space to finite support.

For these fixed effects, the Bell operator has eigenvalues 35/16 once,
5/4 four times and -25/16 eleven times. Thus 35/16 is the sharp maximum
over all joint densities, and rho_Phi is its unique maximizing density.
This is not an optimum over unrestricted measurement families or an
apparatus uniqueness theorem.

Every CHSH restriction of this same table has absolute value at most two,
with maximum exactly two, including repeated settings and all eight sign
variants. Passing those two-setting tests therefore does not establish
locality of the full table. The chosen mixture
rho_v=v rho_Phi+(1-v)I16/16 has B(v)=(45v-10)/16; this fixed witness
violates its local bound exactly for v>14/15. Below that threshold no
complete locality conclusion is drawn.

## Histories, no-message theorem and exact controls

The written proof establishes normalized joint branches and finite ordered
history laws for arbitrary complex densities, explicit finite local
memories, arbitrary fixed initial correlations, local adaptive controls and
bounded local stopping. Complete local instruments preserve total trace;
zero-weight branches have no normalized successor. Product sources
factorize. Whole-pair replacement supplies fresh trials; merely rereading
or resetting a pointer does not.

With the full preparation independent of a new remote message, a fixed
receiving policy and only local trace-preserving protocols, the entire
receiving record distribution is independent of the remote control. Every
decision formed solely from that local record consequently has the same
distribution for both messages. The result holds in both directions and
does not presume an uncorrelated reduced source channel. It is an
operational theorem in the selected tensor model, not a physical statement
about a measured distance, speed or spacelike separation.

The exact boundary controls are retained:

- Selective remote outcomes produce the conditional local states P_y and
  Q_y/3, whereas the unselected mean remains I4/4. Using the remote result
  to sort records requires access to that result.
- Setting-dependent separable sources sigma_(x,y) reproduce the entire
  entangled table at their promised settings and retain both reduced
  densities I4/4. They violate the common setting-independent preparation
  premise. Marginal equality alone does not certify that premise.
- Letting the prepared source depend on a remote message can change the
  local marginal; it falls outside the no-message hypotheses.
- If Bob actually communicates his context-zero outcome and Alice chooses
  context zero after LOW and context one after HIGH, her LOW probability
  is 31/64 rather than the fixed-context value 1/4. This is an explicit
  communicated protocol, not a counterexample to the local-only theorem.

Tensor-code transport uses two supplied coherent code copies and their
inherited restricted free evolution. It does not factor one native Omega
checkpoint into two wings, derive an entangled native source, or supply
physical clocks and separation.

## First formal execution and evidence roles

The first scientific execution completed on the clean immutable public pin

    08d83cb231cccee901081803a081a1fcc3f0304c

with all frozen gates G1-G10 passing. The recorded environment was Ubuntu
24.04.3 LTS, x86_64, Python 3.12.14; exit code was zero and stderr empty.
The exact stdout has 886 bytes and 11 lines, SHA-256

    d3d548ac0fcea66b52179645427866d94167c9c97b3247606ce53dc621faf533

RUN.md records execution and custody; EXPECTED.txt preserves the actual
completed stdout. No frozen mathematical falsifier fired. No change to the
six frozen files was needed to obtain this result.

The exact finite audit includes the joint table and operator identities,
all 1024 local vertices, the spectral certificate, all 5000 CHSH forms,
the specified noise controls, 1024 adaptive-history leaf pairs and 1360
prefix pairs, and the declared negative controls. The universal statements
about all complex states, all stochastic Bell-local refinements and all
finite local-memory protocols rest on PROOF.md. Finite histories and
fixtures audit the proof's prerequisites and consequences; they do not
replace those universal arguments. REVIEW.md is the independent written
mathematical review conducted before its reviewer read the verifier.

At creation of this result record, public x86_64 and aarch64 replay and the
aggregate check remain pending. ACCEPTANCE.md and the linked pull-request
record will separately record their immutable evidence and subsequent
final-head and merged-main readback.
This result file records the completed first run, not a public gate that
has not yet completed.

## Adopted inputs and retained obligations

The predecessor's eight choices remain explicit: CH-SOURCE, CH-CONTEXT,
CH-CP, CH-ATTENUATION, CH-BORN, CH-RECORD, CH-RENEWAL and CH-CONTROL.
This extension adds CH-TENSOR, CH-PAIR-SOURCE,
CH-SETTING-INDEPENDENCE, CH-LOCAL-ACCESS and CH-PAIR-RECORD. Independent
uniform controller probabilities are supplied, not generated from U.
The fixed preparation, real chart alignment, local-access restriction and
single-event Born law are selections, not new native deductions.

No experimental data were acquired, no material random source or complete
physical apparatus was built, and no empirical or priority claim is made.
The exact numbers are known theoretical consequences of the selected
model. The white-noise parameter is not a fitted laboratory error budget.

BELL-CAUSAL-ACCOUNTING, QDD-INSTRUMENT-APPARATUS,
QDD-TERMINAL-EVENT-SEMANTICS and QDD-INSTRUMENT-CLASS-COMPLETENESS retain
their broader physical scopes. The #539 contract and feeds_U=false
boundary are unchanged. The three named pair, record and occurrence
bridges remain proposed future dictionary boundaries, not passed gates.
The accompanying fold proposal concerns this conditional theory only;
this probe does not change canon/, STATUS, authority or release state.
