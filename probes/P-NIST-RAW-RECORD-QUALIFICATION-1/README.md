# NIST archived record qualification

NON-CANONICAL / PUBLIC CLAIMS UNREGISTERED / CANON UNCHANGED.

The frozen [preregistration](PREREG.md) defines a bounded audit of original
detector-server records. [SOURCE.json](SOURCE.json) binds four complete
compressed archives, their custody history and the required NIST notice.
Only the first 1,048,576 records of each nominated member are decoded.

From a clean Linux checkout of the formal pin or an unchanged descendant:

```text
python3 probes/P-NIST-RAW-RECORD-QUALIFICATION-1/verify.py
```

Python 3.12 standard library suffices. A cold replay downloads 746,878,746
compressed bytes to a temporary directory; allow network access to the four
literal NIST S3 URLs and sufficient temporary disk space. The optional
`TWISTJ_NIST_CACHE_DIR` points to externally held `<id>.zip` files. Every cache
hit is fully rehashed before ZIP access and cannot change the output.
Preserve the [NIST notice](../../notes/NIST-RAW-CUSTODY-1.md) with data copies.
Do not commit archives or decompressed records to this repository.

The resulting JSON preserves integer counts and bounded witnesses in original
record order. Record intervals and empty detector-row counts do not certify
physical trials, no-click outcomes, apparatus completeness or a Born law.
See RESULT.md and RUN.md once the first pinned execution has been recorded.
