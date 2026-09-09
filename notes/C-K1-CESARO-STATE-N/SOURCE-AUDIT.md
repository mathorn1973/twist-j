# Public basis readback

This audit concerns source identity, not a new scientific confirmation.

The GitHub connector read STATUS.md first, followed by POLICY.md, AGENTS.md,
canon/CORE.md and canon/FRONTIER.md from public main. The relevant Canon
sections, registry/evidence/dependency rows and K1 notes were read at the
immutable activation commit.

A fresh read-only clone of the public Git repository confirmed:

- main and canon-v82 resolve to
  f6baa1fbfe320e5e6cef610f9da6a500e1ba8f08;
- the tag and declared content commit
  4e65adf0b483311d2a031cf2a23a65f2caf5af8a are ancestors of main;
- all five entries in canon/SHA256SUMS match;
- canon/CANON.md has exactly 580724 bytes and the declared SHA-256;
- repository `tools/check_activation.py --post-activation
  --expected-tag canon-v82` passed with full=False, including policy,
  Canon, ledger, reconciliation, external-source and preregistration-draft
  checks.

GitHub readback reported success for the reviewed release head jobs
architecture-x86_64, architecture-aarch64 and check in workflow 34274090870.
The activation commit's published workflow runs 34280908503, 34277815342
and 34277507390 reported success. Release metadata reports immutable=true,
draft=false, and the expected content and activation identity.

The full scientific inventory and both architecture jobs were not rerun by
this session. They were read as the existing public checks. The candidate
scripts in this package ran locally on one x86_64 lane only.

Collision review read open issues and pull requests, all explicit remote
branch refs, the current registry/probe/notes tree, and relevant K1 textual
matches. Issue 911 already owns the cubic ADM/FRW predefinition. This
candidate does not execute or modify that lane. No K1 Cesaro-state match
was returned by the scoped textual search. Such a search does not establish
novelty against all mathematical literature.

No public repository file, branch, issue, pull request, tag or release was
changed by this session.
