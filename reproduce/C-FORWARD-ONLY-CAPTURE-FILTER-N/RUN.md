# Author audit run

NON-CANONICAL L1. Design-exposed exact audit, not blind confirmation.

- prospective pin: `c1f7f52fd5803a6dd6b5447b31427e4415e7d42e`
- platform: Linux
- architecture: aarch64
- Python: 3.12.3
- command: `python3 reproduce/C-FORWARD-ONLY-CAPTURE-FILTER-N/verify.py`
- environment: LC_ALL=C, LANG=C, PYTHONDONTWRITEBYTECODE=1, PYTHONHASHSEED=0, TZ=UTC
- exit code: 0
- verifier SHA-256: `d37bd5ecfac85fd05329ef83f745775c72764536f20661ed481511d45ac18617`
- stdout: 558 bytes, SHA-256 `97b92dc97a91c3227e2ab8851530fd071c39f0059e5eef217c60c7e0009b7969`
- stderr: 0 bytes, SHA-256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`

The pin was pushed and read back before this first execution. The source tree
was clean before and after the run. No scientific code was edited or retried.
788 exact assertions passed, within the scope of PREREG and PROOF. Small
examples audit the analytic arguments; they do not exhaust the full apparatus
or prove physical admission. Cross-architecture reproduction and independent
mathematical acceptance are separate obligations.
