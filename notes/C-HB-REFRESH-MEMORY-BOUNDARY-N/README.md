# Minimal finite-horizon memory for two supplied contacts

NON-CANONICAL / conditional L1 / no scientific authority.
Owner [#1525](https://github.com/mathorn1973/twist-j/issues/1525).

[PROOF.md](PROOF.md) classifies all fixed rational linear wave summaries for
two exact reading horizons. Three coordinates suffice for times {0,2}; four
are necessary for {0,1,2}. Initial tape is known separately. The same three
wave coordinates predict the guards and work of two supplied contacts
separated by two F steps, including arbitrary occupied waves and both refusals.
An exact equal-energy/equal-tape pair defeats the old rho-plus-gamma proposal.

This does not construct native sensors, an all-time compressed wave state,
physical actuation, finite-bit memory or reusable apparatus. It narrows one
finite acquisition problem without changing its supplied rational model.

[RESULT.md](RESULT.md) gives scopes and first-run evidence.
[PREREG.md](PREREG.md) freezes definitions, target exposure and checks.
[RUN.md](RUN.md) and [EXPECTED.txt](EXPECTED.txt) retain the first exact run.
[CODE_SHA256SUMS](CODE_SHA256SUMS) binds all frozen inputs and
[SOURCES.tsv](SOURCES.tsv) their public source identities.

From the repository root:

    PYTHONHASHSEED=0 PYTHONUTF8=1 PYTHONDONTWRITEBYTECODE=1 \
    LC_ALL=C LANG=C TZ=UTC \
    python3 notes/C-HB-REFRESH-MEMORY-BOUNDARY-N/verify.py

Compare the entire stdout byte for byte with EXPECTED.txt and require zero
exit and empty stderr. Notes-only CI is not this scientific reproduction.
Independent review is pending. [PROMO.md](PROMO.md) states that next contract.
