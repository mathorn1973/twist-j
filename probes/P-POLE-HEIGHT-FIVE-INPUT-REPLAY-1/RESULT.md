# Common five-input loader: fixed witness result

Status: PASS / NON-CANONICAL L1 computation certificate.

The supplied 322-contact WORD.txt maps every complete preparation
I_t=(tB,-tB,u,u,X,2) to G_t=(u+tB,u-tB,0,0,X,2), for
all t in {-2,-1,0,1,2}. Both helpers return exactly at their original
addresses. The same word is used without selecting a program by t.
Its 1288-contact literal inverse recovers every initial six-slot state.
The slot-1/2 image sigma(W) passes the same complete contract.

## Exact recorded observations

The independently implemented power-basis and minimum-zero cyclic routes
agree after every forward and inverse contact, including admission and
state-change flags. Ring sum, summed Q and all six residues modulo u are
preserved throughout. All ten cases and 112836 checks pass with zero
fired falsifiers. EXPECTED.txt contains complete endpoints, recovered
states, the full forward branch traces and trajectory/branch hashes.

| t | Admitted | Refused | State-changing | Admitted diagonal |
|---|---:|---:|---:|---:|
| -2 | 137 | 185 | 135 | 2 |
| -1 | 177 | 145 | 170 | 7 |
| 0 | 112 | 210 | 100 | 12 |
| 1 | 177 | 145 | 170 | 7 |
| 2 | 123 | 199 | 123 | 0 |

For sigma(W), the full admission/change traces at t equal those of W at
-t, in both directions. The recorded counts agree with the exposed source
review, but were not used as adjustable success thresholds.

The first clean Linux x86_64 run exited zero with empty stderr. Exact
stdout has 11887 bytes and 12 LF-terminated lines, SHA-256
b09680df8f50e115fed0640c9ec3eb388db4e6729ded438abd7fcbefec0cb448.
RUN.md binds the five immutable sources and the local environment.
A one-architecture computation is at most candidate-C. Byte-identical
replay of this same head on the required x86_64 and aarch64 jobs satisfies
the computation gate for this finite existence certificate; those actual
job results are reported on the PR. This record makes no Canon promotion.

## Scope and remaining questions

This is a constructive upper bound of 322 attempted contacts for the stated
common-five contract. It supplies neither the global minimum nor the
claimed 38-contact or 21-macro lower bounds. No large orbit, stabilizer
transitivity, stock census or witness-search history is newly reproduced.
The earlier probes' bounded misses remain accurate records of their own
searches and do not conflict with this successful new fixed witness.

The parity branch is intrinsic to the supplied total contact law. The
six-slot preparation, two helpers, addressed alphabet and chronological
schedule remain supplied. This is not autonomous execution, a native-U
compilation, a physical clock or an action/alpha normalization. The source
review's broader physical language is not a tested consequence here.

The result stays in its new probe directory for review. No prior probe,
Canon, registry, website, workflow, release or merge is changed.
