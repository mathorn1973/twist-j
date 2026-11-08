# First pinned Linux execution

NON-CANONICAL / L1 / exact finite audit of a disclosed analytic prediction.

pin_commit: 44bbe51404dc4627cc2212c7997ab38ca0f49797
verifier_sha256: 6e55c7e78d28389de69527830af33e543cb4e25489694398021eb7b57a18a34b
command: python3 probes/P-AUTONOMOUS-CONTACT-RING-1/verify.py
platform: Debian GNU/Linux 13 (trixie)
architecture: x86_64
python: 3.12.14
exit_code: 0
stdout_sha256: 64d0d0a22701adfdfe29f5f968b33857bc72bb2b1647b8d2f40c2782409d04c1
stdout_bytes: 1110
stdout_lines: 1
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0

started_utc: 2026-11-08T22:27:23.174362+00:00
completed_utc: 2026-11-08T22:27:35.129384+00:00

The document contract and both independent implementations were frozen in
local Git before comparison. Those local commits are preparation provenance,
not the public execution pin or claimed ancestors of it. Under the author's
explicit authorization, the connected account's default commit identity
published the exact prepared tree 2bcd7aed50fdb8f568a4cd004bfa107ac9394127
as the public pin above. All five scientific sources were fetched at that
public SHA and matched byte for byte before the first execution from a clean
public checkout. No scientific source changed afterward.

The command ran with assertions enabled. Inherited PYTHON* and TWISTJ*
environment variables were removed, then PYTHONDONTWRITEBYTECODE=1,
PYTHONHASHSEED=0, LC_ALL=C, LANG=C and TZ=UTC were set. The timeout was
600 seconds. Observed wall duration was approximately 11.957 seconds; this
is operational timing, not a scientific duration or acceptance threshold.

The primary four-coefficient polynomial implementation completed its audit,
then loaded the frozen independently authored five-coefficient cyclic
implementation. Their complete report dictionaries agreed. The one printed
JSON object records independent_match=true and status=PASS. Exact stdout
was saved as EXPECTED.txt only after exit zero and empty stderr were observed.

## Pinned scientific sources

| File | SHA-256 | Bytes |
| --- | --- | ---: |
| PREREG.md | `b4eaea2be90cb357569c728498b930746ce3f64c1d90be84e8ab8c30cd5749af` | 8948 |
| CONTRACT.md | `9e1d637a45b8bd85a86d51a0c12e133516d41a8c26ebbbab76fad0eb5420c56d` | 7665 |
| PROOF.md | `5e3dc5960910808f44f90ce9900a50f3e54fb9b81c3f30288a319570d1220a42` | 10906 |
| verify.py | `6e55c7e78d28389de69527830af33e543cb4e25489694398021eb7b57a18a34b` | 12324 |
| break.py | `dcc968b731763d52423336288c11065b87d6a3a3107264f03b65de7cdbb621cd` | 17865 |

## Preparation provenance

Reservation: https://github.com/mathorn1973/twist-j/issues/1966.
The reservation recorded these local immutable commits before execution:

- frozen document contract: 75a528ca7f5a447b34ae9d333d006815d85dfdf7;
- primary source: 293c909db757d9472c5c87631ae6a85495fb1b29;
- separate breaker source: 1daab122d97506c34050cbce3133376df2547778;
- combined prepared tree: c252215554893ef073af5ec6c9b8ec48cee8ba6d.

The breaker's scientific inputs were only the frozen PREREG.md and
CONTRACT.md. It did not read verify.py, PROOF.md or primary output before
its own source was frozen. The later joint static review inspected both
already frozen programs and is not represented as another blind review.
The source tree and all five content hashes are preserved by the public pin.
The separate local provenance SHAs are not substituted for public evidence.

This record describes the first local x86_64 execution. It does not claim
the required GitHub x86_64 and aarch64 results in advance. The pull request
records their actual head, jobs and outcomes. Both architecture jobs must
replay the unchanged accepted verifier against these same EXPECTED.txt
bytes. Same-architecture replay is reproduction, not another architecture
or another independently authored implementation.
