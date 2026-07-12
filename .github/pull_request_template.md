## Scope

Type: `probe | canon | synthesis | activation | policy | maintenance`

Probe, Canon section, or layer affected:

## Canon synthesis or activation

Complete this section for `synthesis` and `activation` changes.

- Public Canon version:
- Synthesis content commit:
- Canon SHA-256:
- Canon bytes:
- Registry claim count:
- Reconciliation audit:
- Intentional omissions or lowered claims:
- Status transition: `GENESIS -> GENESIS | GENESIS -> ACTIVE | not applicable`
- Legacy `twistj.com/canon/` pointer unchanged during GENESIS: `yes | no | not applicable`

## Probe pins

Complete this section for probe changes.

- Preregistration commit:
- Verifier SHA-256:
- Local platform and architecture, neutral names only:
- Local stdout SHA-256:
- GitHub byte match: `pass | pending | not applicable`
- Two architectures: `yes | no | not applicable`

## Checks

- [ ] Scope and status are exact.
- [ ] Canon registry, frontier, citations, and SHA-256 manifest pass, or are not applicable.
- [ ] Minimal reproductions exit 0 with byte-identical stdout, or are not applicable.
- [ ] Formal execution followed the public pin.
- [ ] Fired falsifiers are recorded.
- [ ] Security review passed.
- [ ] Required `check` job passed.
