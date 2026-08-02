# RESULT P-CM-2I-QCARRIER-1

## Decision

The pinned verifier (19 gates, pin commit
`c223955229239858913c554bd5d6149d352d0472`) exited 0 with empty stderr
and stdout byte-identical to the committed `EXPECTED.txt`
(sha256 `138cda2609bd712089ac550e508830d6bd42efe33fde39d0a01ed2badbd2fd86`,
1483 bytes) on the local formal leg, 19 of 19 PASS. The required
GitHub x86_64 and aarch64 jobs on this pull request rerun the same
pinned verifier and enforce byte identity against the same
`EXPECTED.txt`; their records are in `RUN.md`. Byte-identical stdout on
two different architectures satisfies the POLICY section 4
two-architecture computation gate.

### Chronology and post-CI ratification

The first version of this `RESULT.md` was committed in
`57b92bc8d4819ac1cd7cc58cc8e371302abe979d` before the required GitHub
jobs had completed, because the repository policy checker requires
`RESULT.md` to be present in every probe directory. It was therefore
provisional only as to the two-architecture conclusion. Workflow run
`30737458873` subsequently completed successfully for that PR head:
aarch64 job `91468760543` and x86_64 job `91468760576` both reported
`VERIFY PASS` for verifier SHA-256
`d031470193a1e6035769c64c75c5ab98e4e4f381af2dbdf6307d81f8e33c100f`
and stdout SHA-256
`138cda2609bd712089ac550e508830d6bd42efe33fde39d0a01ed2badbd2fd86`.
Commit `adc43d3cf80dd26ddf56649d0cc1f09fa5549bbd` then recorded that leg
in `RUN.md`, and workflow run `30737517851` passed both architecture
jobs and the aggregate check while classifying the record
`TWO-ARCHITECTURE`. This paragraph ratifies the two-architecture
conclusion after the evidence existed. It changes no frozen equation,
verifier, expected output, threshold, falsifier, or action layer.

The frozen decisions E1-E4 of `PREREG.md` are audited positively:

```text
E1  marked twist stabilizer {1,sigma}         M1-M4        PASS
E2  pair character, Galois-stable class,
    Hom data (0, K C0, K I2, 0)               M5-M10       PASS
E3  cocycle class [-1], order four
    impossible, order eight attained
    (nu^4 = -I, nu^8 = I, a = 1, d = phi)     M11-M15      PASS
E4  Gram line F H0, total positivity,
    balanced similitude phi^2 tau(H_pair)     M16-M19      PASS
```

## Falsification

No falsifier fired. F-CM-1 through F-CM-5 were armed before the pin
and remain the standing falsifiers of the recorded claims. No
threshold moved after the pin.

## Status and scope

- The audited finite identities carry the two-architecture computation
  gate and earn at most `C` on that basis (POLICY section 4).
- `T` for E1-E4 is available only through owner acceptance of the
  `PREREG.md` section 7 proof as an independent derivation, with this
  verifier as its audit. That acceptance is a separate act and is not
  claimed by this record.
- RESULT-EXPOSED: the incubation outputs (notes/C-CM-2I-QCARRIER-1,
  notes/C-CM-2I-QCARRIER-2, and the reviewed prep surface of PR #244)
  were known before the pin; this probe is confirmatory, as disclosed
  in `PREREG.md` section 0.
- Scope boundary: L4 support only, relative to the one displayed
  `S, T` representative; `SPIN-LIFT-FORCED [F]` is respected; the
  decoder rows `QUADRATIC-DECODER-DATA [O]` and
  `COLOR-MEASURE-SELECTION [O]` remain STOP and untouched.
- No registry, frontier, or Canon file is changed by this probe. Any
  registration of E1-E4 is a later, separately sealed fold.
