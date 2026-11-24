# Custody and static validation

NON-CANONICAL. No authority. Date: 23 November 2026.

The public basis was main 93c36089db57032a6cbca482ff62c95884567d0f,
Public Canon v116. At bootstrap its authority, tag/content ancestry,
normative hashes and required base checks were inspected. Main was read
again before final packaging and remained at the same commit. The new
work is restricted to this notes directory.

## Immutable scientific pins

- Local original preregistration: 70d7421928fc9b62fc246870aa17362929755c27.
- Public preregistration with identical tree:
  3418bd94e0ac8e4ff47393e4706291729845ff23.
- Local development code: 335779e8969b5b1f1b4db9e017216bce4d8b2813.
- Local blind opposition code: 42cb3d9d19b7d9ea7e6fd03b6d8446f69440521f.
- Both programs published and remotely read back before execution:
  72ff97914a1b56ad616d8e603d9776364ae90968.

RESULTS.md contains SHA-256 values for the actual files and first-run
stdout. No amend, force push, repaired scientific rerun or threshold change
was used. Program stdout is preserved including the documented reporting
label error.

Local authoring commits use A. M. Thorn <thorn@twistj.com>. Terminal
publication lacked GitHub credentials, so the authenticated GitHub connector
transported the same content. Its commit API exposes no author-email
override and uses the connected A. M. Thorn account's GitHub no-reply
address. Transport messages preserve the requested author attribution and
the local source commit identifiers. Public scientific custody is the
remotely read-back file bytes at the public pins above, not an assertion
that the local and connector commit objects are identical.

## Static repository checks

The repository's own tools returned:

    POLICY PASS
    CANON PASS v116 claims=634

The initial shallow checkout was deepened before the ancestry-sensitive
Canon check. Git whitespace checking of the final content passed after
removing an extra terminal blank line from the newly authored source map.
This was an editorial file change, not a scientific-program change.

These checks are static repository validation. The new mathematical
computations remain the two first runs on x86_64 recorded in RESULTS.md.
There was no Lean execution, release, Canon fold or public promotion.
