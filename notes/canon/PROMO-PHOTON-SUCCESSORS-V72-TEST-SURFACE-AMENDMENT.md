# PROMO-PHOTON-SUCCESSORS-V72-TEST-SURFACE-AMENDMENT

Status: **NON-CANONICAL / NO AUTHORITY / PROMOTION AMENDMENT ONLY.**

Public lock: [issue #702](https://github.com/mathorn1973/twist-j/issues/702).

This note amends only the exact content-commit file surface frozen by
`PROMO-PHOTON-SUCCESSORS-V72`. It creates no claim, status, Canon version,
Registry row, Frontier row, gate, tag or release, and it changes none of the
four frozen scientific scopes.

```text
basis main:                 c862642a41fe798b6c510f3c4f817d258f75afec
parent promotion package:  notes/canon/PROMO-PHOTON-SUCCESSORS-V72.md
parent promotion commit:   8727e6dabf8ff4bbd5532715a0eacb50fdc7f4e8
parent promotion PR:       #701
parent promotion merge:    c862642a41fe798b6c510f3c4f817d258f75afec
parent package git blob:   113bfa98f3e2c00ff96593a617802ebc9b26659c
parent package bytes:      36112

amended file:              tools/test_architecture_map_report.py
preimage git blob:         279cef02801d24a25c23123d50b3e06831faa763
preimage bytes:            13534
required postimage blob:   c334dc179b473dcabd5ec9e3fb54f5be9e8970dc
required postimage bytes:  14439
```

## Reason for the amendment

The parent package correctly freezes a `342 -> 346` Registry move, but its
section 13 lists only the thirteen changed `canon/` files. The repository's
non-normative architecture-map test intentionally pins the live public
Registry, evidence and graph counts. Applying the exact frozen four-row delta
without updating that fixture makes two unit tests fail:

```text
expected claims 342, observed 346
expected transitive architecture dependents 238, observed 240
```

The test then also needs the already-frozen status and evidence totals and the
new terminal count. Omitting this file is not an admissible workaround: the
required 142-test release gate would remain red. Changing the report logic is
also not admissible. The only authorized repair is the exact fixture and
topology delta below.

## Exact authorized test delta

```diff
diff --git a/tools/test_architecture_map_report.py b/tools/test_architecture_map_report.py
index 279cef0..c334dc1 100644
--- a/tools/test_architecture_map_report.py
+++ b/tools/test_architecture_map_report.py
@@ -27 +27 @@ class ArchitectureMapReportTests(unittest.TestCase):
-        self.assertEqual(self.report.claims, 342)
+        self.assertEqual(self.report.claims, 346)
@@ -30 +30 @@ class ArchitectureMapReportTests(unittest.TestCase):
-            {"C": 33, "D": 44, "F": 17, "H": 2, "O": 27, "T": 219},
+            {"C": 33, "D": 44, "F": 17, "H": 2, "O": 29, "T": 221},
@@ -35 +35 @@ class ArchitectureMapReportTests(unittest.TestCase):
-                "none": 45,
+                "none": 47,
@@ -38 +38 @@ class ArchitectureMapReportTests(unittest.TestCase):
-                "two-architecture": 257,
+                "two-architecture": 259,
@@ -46 +46 @@ class ArchitectureMapReportTests(unittest.TestCase):
-            len(self.report.transitive_architecture_dependents), 238
+            len(self.report.transitive_architecture_dependents), 240
@@ -48 +48 @@ class ArchitectureMapReportTests(unittest.TestCase):
-        self.assertEqual(len(self.report.dependency_terminals), 51)
+        self.assertEqual(len(self.report.dependency_terminals), 52)
@@ -71,0 +72,24 @@ class ArchitectureMapReportTests(unittest.TestCase):
+        )
+        self.assertIn(
+            "FCC-WEIGHTED-SHELL-SYMBOL", self.report.dependency_terminals
+        )
+        self.assertNotIn(
+            "FCC-WEIGHTED-SHELL-SYMBOL",
+            self.report.transitive_architecture_dependents,
+        )
+        for claim in (
+            "PHOTON-WILSON-VILLAIN-FINITE-COUPLING-NONMEMBERSHIP",
+            "PHOTON-MASSLESS-PHASE",
+        ):
+            self.assertNotIn(claim, self.report.direct_architecture_requires)
+            self.assertIn(
+                claim, self.report.transitive_architecture_dependents
+            )
+            self.assertNotIn(claim, self.report.dependency_terminals)
+        self.assertNotIn(
+            "PHOTON-CONE-CONVERGENCE",
+            self.report.direct_architecture_requires,
+        )
+        self.assertNotIn(
+            "PHOTON-CONE-CONVERGENCE",
+            self.report.transitive_architecture_dependents,
```

The resulting report totals are frozen as:

```text
claims:                              346
status counts:                       C33 D44 F17 H2 O29 T221
evidence counts:                     none47 one-architecture9
                                     recorded-audit31 two-architecture259
direct DEF-ARCHITECTURE requires:    178  (unchanged)
transitive architecture dependents: 240  (+2)
dependency terminals:                52   (+1)
```

The two new transitive dependents are
`PHOTON-WILSON-VILLAIN-FINITE-COUPLING-NONMEMBERSHIP` and
`PHOTON-MASSLESS-PHASE`, through their exact registered dependency paths.
`FCC-WEIGHTED-SHELL-SYMBOL` is the one new dependency terminal.
`PHOTON-CONE-CONVERGENCE` is neither a direct nor transitive
`DEF-ARCHITECTURE` dependent. These are graph classifications only; they add
no scientific premise or conclusion.

## Amended exact content surface

Section 13 of the parent package is replaced only for the first content-file
list. The complete later v72 content commit may change exactly:

```text
canon/CANON.md
canon/CORE.md
canon/FRONTIER.md
canon/REGISTRY.tsv
canon/CHANGELOG.md
canon/SHA256SUMS
canon/NORMATIVE.tsv
canon/DEPENDENCIES.tsv
canon/EVIDENCE.tsv
canon/HISTORY.tsv
canon/GATES.tsv
canon/FRONTIER_PROGRAMS.tsv
canon/STATUS_COUNTS.tsv
tools/test_architecture_map_report.py
```

Every other parent-package instruction remains byte-for-byte binding. In
particular, `canon/CORE_SELECTION.tsv`, every probe byte, every reproduction
byte, all four scopes, seven dependency edges, three gates, two Frontier
roots, evidence hashes, changelog delta, counts and the separate three-file
release form do not change.

The release branch must be based on the public merge of this amendment and
must still contain exactly two commits after that basis: one immutable content
commit and one release-form commit. The amendment note itself is part of the
basis main, not part of either release commit.

## Verification and STOP conditions

The amended fold requires all parent checks and additionally:

```text
git blob preimage == 279cef02801d24a25c23123d50b3e06831faa763
git blob postimage == c334dc179b473dcabd5ec9e3fb54f5be9e8970dc
python tools/architecture_map_report.py --format json yields the frozen totals
python -m unittest discover -s tools -p 'test_*.py' passes all 142 tests
```

STOP on any different test byte, any change to
`tools/architecture_map_report.py`, any additional content file, any changed
scientific scope or ledger row, any changed probe or reproduction byte, or
any release branch not based on the public amendment merge. If an intervening
Canon content fold lands first, the v72 package must be re-gated rather than
silently rebased.
