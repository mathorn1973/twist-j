# Pointed batch decoder candidate

**NON-CANONICAL.** This is an executable mathematical decoder candidate with
explicit choices. It does not certify a complete physical decoder or a Born
frequency law. The actual scientific verdict belongs to `RESULT.md`; the
immutable source pin and execution receipts belong to `RUN.md`.

From the repository root, using Python 3.12 or later:

```sh
python3 probes/P-DECODER-POINTED-BATCH-CONFORMANCE-1/decoder.py \
  --head 0 1 1 1 1 0 0 --cuts 3
```

The seven head integers are `n0 p1 p4 p1prime p4prime q r`. The counter is
nonnegative; the six pentits use representatives 0 through 4. `--cuts L`
returns the source header and exactly L consecutive frames, beginning at
relative cut zero. Fractions use exact `{numerator,denominator}` objects.

Each frame contains:

* `matter`: the head-anchored five-field QDD record, balanced piston,
  current F5 trace covector and current Thue-Morse binary read;
* `geometry`: the two separately tagged finite Maxwell constructions and
  the current finite-support rational D3 wave;
* `clock`: the actual autonomous checkpoint, absolute and relative counters,
  cycle coordinate, complete compact batch and atomic-write terminal flag.

The batch stores a complete finite pair bank through exact ranges. For a
Python caller, `frame.clock.batch.pair_at(i)` passively reads its i-th pair;
`.counts`, `.total_count`, `.ratio` and `.outcome` expose the derived values.
This is not repeated sampling or a sequence of new physical events. Zero
support produces a recorded empty batch and `ZERO_DENOMINATOR`.

In the displayed head the QDD LOW/HIGH result and the five-cell population
have different codomains and must remain separate. No cell is singled out by
an occurrence sampler. Source, wave initialization, full incidence and
clock alignment are declared candidate choices.

The callable interface is `Decoder((n0, tuple6)).prefix(L)` or `.stream()`.
Only compatible generated histories are the claimed domain; manually forged
dataclass instances are not certificates of reachability. Finite exact
computations can still require large memory and time. The mathematical
totality statement is about finite prefixes with unbounded ideal resources.

Read `PREREG.md` for the complete chosen equations, uniform proof and frozen
failure conditions; `PROFILE.json` for every field owner and unresolved
physical requirement; and
[`C-DECODER-POINTED-BATCH-1`](../../notes/canon/C-DECODER-POINTED-BATCH-1.md)
for the broader mathematical map and Canon boundary.

The accepted exact audit is:

```sh
python3 probes/P-DECODER-POINTED-BATCH-CONFORMANCE-1/verify.py
```

The verifier and all its dependencies must match the public preregistration
pin. Passing conformance does not change any public claim or Canon version.
