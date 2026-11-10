#!/usr/bin/env python3
"""Tests for the non-normative architecture-map ledger report."""

from __future__ import annotations

import contextlib
import io
from pathlib import Path
import sys
import unittest


TOOLS = Path(__file__).resolve().parent
ROOT = TOOLS.parent
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

import architecture_map_report as architecture  # noqa: E402


class ArchitectureMapReportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.report = architecture.audit(ROOT)

    def test_v106_exact_declared_dependency_extension(self) -> None:
        # These are declared mathematical premises. A path in this graph
        # does not supply preparation, a physical reading or an apparatus.
        normative = architecture.read_tsv(
            ROOT / "canon/NORMATIVE.tsv", architecture.NORMATIVE_FIELDS
        )
        dependencies = architecture.read_tsv(
            ROOT / "canon/DEPENDENCIES.tsv", architecture.DEPENDENCY_FIELDS
        )
        requires = architecture.dependency_graph(
            (row["item_id"] for row in normative), dependencies, "REQUIRES"
        )
        expected = {
            "ACTIVE-ISOSPECTRAL-RECORD": {
                "HOMOGENEOUS-CAPTURE-CURRENT-RECORD",
            },
            "COHERENT-W-LOCAL-NATIVE-NETWORK": {
                "DEF-COHERENT-INTEGER-W",
                "U-NATIVE-CHART-AND-QDD-READBACK",
            },
            "COHERENT-W-LOCALIZED-RING-CLOSURE": {
                "DEF-COHERENT-INTEGER-W",
                "GOLDEN-CLIFFORD-COIN-IDENTITY",
            },
            "COHERENT-W-NATIVE-FROBENIUS-PROPAGATION": {
                "COHERENT-W-LOCAL-NATIVE-NETWORK",
                "DEF-COHERENT-INTEGER-W",
            },
            "COHERENT-W-PHASE-RETAINED-LOCAL-FACTOR": {
                "COHERENT-W-LOCAL-NATIVE-NETWORK",
                "COHERENT-W-LOCALIZED-RING-CLOSURE",
                "DEF-COHERENT-INTEGER-W",
                "GOLDEN-CLIFFORD-COIN-IDENTITY",
            },
            "COHERENT-W-SPATIAL-CLIFFORD-PROPAGATION": {
                "DEF-COHERENT-INTEGER-W",
                "GOLDEN-CLIFFORD-COIN-IDENTITY",
            },
            "COMPACT-ACTIVE-RECORD-APPARATUS": {
                "ACTIVE-ISOSPECTRAL-RECORD",
            },
            "DEF-COHERENT-INTEGER-W": set(),
            "DIRAC-CONTACT-COMPLETE-ACCOUNT": set(),
            "DIRAC-CONTACT-SOURCE-COHERENCE": {
                "DIRAC-CONTACT-COMPLETE-ACCOUNT",
            },
            "FINITE-COHERENT-BATTERY-DRIFT": set(),
            "GOLDEN-CLIFFORD-COIN-IDENTITY": {
                "DEF-COHERENT-INTEGER-W",
            },
            "INTEGER-W-SPECTRAL-ENERGY-PULLBACK": {
                "COHERENT-W-LOCALIZED-RING-CLOSURE",
                "COHERENT-W-PHASE-RETAINED-LOCAL-FACTOR",
                "CONTACT-W-SPECTRAL-READING",
                "DEF-COHERENT-INTEGER-W",
            },
            "LOCAL-THERMAL-TWO-ATTEMPT": {
                "OCCUPIED-RECORD-EXPORT-REUSE",
            },
            "OCCUPIED-RECORD-EXPORT-REUSE": set(),
            "THERMAL-ORIGINAL-PORT-APPARATUS": {
                "ACTIVE-ISOSPECTRAL-RECORD",
            },
            "U-NATIVE-WHOLE-SHEET-RETURN-WINDOWS": {
                "DEF-ARCHITECTURE",
                "DEF-KERNEL-GENERATORS",
                "TT-NATIVE-FOUR-WORD-LAW",
            },
        }
        for item, parents in expected.items():
            self.assertEqual(requires[item], parents)
        self.assertEqual(
            set(expected) & set(self.report.direct_architecture_requires),
            {
                "U-NATIVE-WHOLE-SHEET-RETURN-WINDOWS",
            },
        )
        self.assertEqual(
            set(expected) & set(self.report.transitive_architecture_dependents),
            {
                "COHERENT-W-LOCAL-NATIVE-NETWORK",
                "COHERENT-W-NATIVE-FROBENIUS-PROPAGATION",
                "COHERENT-W-PHASE-RETAINED-LOCAL-FACTOR",
                "INTEGER-W-SPECTRAL-ENERGY-PULLBACK",
                "U-NATIVE-WHOLE-SHEET-RETURN-WINDOWS",
            },
        )
        self.assertEqual(
            set(expected) & set(self.report.dependency_terminals),
            {
                "DEF-COHERENT-INTEGER-W",
                "DIRAC-CONTACT-COMPLETE-ACCOUNT",
                "FINITE-COHERENT-BATTERY-DRIFT",
                "OCCUPIED-RECORD-EXPORT-REUSE",
            },
        )

    def test_v110_contact_scope_and_finite_apparatus_closure(self) -> None:
        normative_rows = architecture.read_tsv(
            ROOT / "canon/NORMATIVE.tsv", architecture.NORMATIVE_FIELDS
        )
        dependency_rows = architecture.read_tsv(
            ROOT / "canon/DEPENDENCIES.tsv", architecture.DEPENDENCY_FIELDS
        )
        registry = {
            row["claim_id"]: row
            for row in architecture.read_tsv(
                ROOT / "canon/REGISTRY.tsv", architecture.REGISTRY_FIELDS
            )
        }
        evidence = {
            row["claim_id"]: row
            for row in architecture.read_tsv(
                ROOT / "canon/EVIDENCE.tsv", architecture.EVIDENCE_FIELDS
            )
        }
        normative = {row["item_id"]: row for row in normative_rows}
        requires = architecture.dependency_graph(
            normative, dependency_rows, "REQUIRES"
        )
        bounded_by = architecture.dependency_graph(
            normative, dependency_rows, "BOUNDED_BY"
        )
        contact = "RELATIVE-CONTACT-INTEGRAL-LAW"
        minimum = "RELATIVE-CONTACT-FOUR-SLOT-MINIMUM"
        renewal = "RELATIVE-CONTACT-RETAINED-BANK-CAPACITY"
        fixed_word = "RELATIVE-CONTACT-FIXED-WORD-RESIDUE-BOUNDARY"
        owner = "RELATIVE-CONTACT-COMMON-APPARATUS-OPEN"
        compiler = "RELATIVE-CONTACT-FIVE-HEIGHT-COMPILER"
        apparatus = "RELATIVE-CONTACT-PREPARED-HEIGHT-FINITE-APPARATUS"
        obstruction = "RELATIVE-CONTACT-AFFINE-FIVE-PHASE-OBSTRUCTION"
        expected = {
            contact: {"J-UNIT"},
            minimum: {contact},
            renewal: {contact, minimum},
            fixed_word: {contact},
            owner: {contact},
            "RELATIVE-CONTACT-RHYTHM-CLASSIFICATION": {contact},
            "RELATIVE-CONTACT-RHYTHM-ACCOUNT-BOUNDS": {"RELATIVE-CONTACT-RHYTHM-CLASSIFICATION"},
            "RELATIVE-CONTACT-RHYTHM-FIVEFOLD-PHASE": {"RELATIVE-CONTACT-RHYTHM-CLASSIFICATION"},
            "RELATIVE-CONTACT-COEFFICIENT-READ-INJECTIVITY": {contact},
            'RELATIVE-CONTACT-POSITIONAL-BANK-COPY': {'RELATIVE-CONTACT-INTEGRAL-LAW'},
            'RELATIVE-CONTACT-FOUR-PLACE-COPY-OBSTRUCTION': {'RELATIVE-CONTACT-INTEGRAL-LAW'},
            'RELATIVE-CONTACT-FINITE-WORKBANK-REUSE': {'RELATIVE-CONTACT-COMMON-APPARATUS-OPEN', 'RELATIVE-CONTACT-INTEGRAL-LAW', 'RELATIVE-CONTACT-POSITIONAL-BANK-COPY'},
            compiler: {contact, "J-UNIT"},
            apparatus: {contact, compiler, "RELATIVE-CONTACT-FINITE-WORKBANK-REUSE"},
            obstruction: {contact},
        }
        # These supplied contact premises do not derive a native-U operation.
        # The optional Gram/archive notes have no new public claim rows.
        self.assertEqual(
            {item for item in normative if item.startswith("RELATIVE-CONTACT-")},
            set(expected),
        )
        for item, parents in expected.items():
            self.assertEqual(requires[item], parents)
            self.assertEqual(normative[item]["layer"], "L1")
            self.assertNotIn(item, self.report.direct_architecture_requires)
            self.assertNotIn(item, self.report.transitive_architecture_dependents)
            self.assertNotIn(item, self.report.dependency_terminals)
            self.assertEqual(
                registry[item]["status"], "T"
            )
            self.assertEqual(
                normative[item]["status"], registry[item]["status"]
            )
        self.assertEqual(bounded_by[owner], {minimum, renewal, fixed_word})
        self.assertEqual(bounded_by[compiler], {obstruction, fixed_word})
        self.assertEqual(bounded_by[apparatus], {renewal, fixed_word})
        self.assertEqual(bounded_by[obstruction], set())
        for claim in (compiler, apparatus, obstruction):
            self.assertEqual(normative[claim]["item_type"], "THEOREM")
            self.assertEqual(normative[claim]["gate_ids"], "")
            self.assertEqual(evidence[claim]["evidence_id"], "EV-" + claim)
            self.assertEqual(evidence[claim]["location"], "inline")
            self.assertEqual(
                evidence[claim]["hash_mode"], "registry-scope-sha256-v1"
            )
        self.assertEqual(normative[owner]["item_type"], "THEOREM")
        self.assertEqual(normative[owner]["gate_ids"], "")
        # This finite same-carrier witness closes only its exact L1 owner.
        # The physical apparatus and native memory-contact owners stay open.
        for unchanged_owner in (
            "QDD-INSTRUMENT-APPARATUS",
            "QUADRATIC-MEMORY-NATIVE-CONTACT",
        ):
            self.assertEqual(registry[unchanged_owner]["status"], "O")
        expected_evidence = {
            contact: ("INLINE_CANON", "none"),
            minimum: ("PUBLIC_PROBE", "two-architecture"),
            renewal: ("INLINE_CANON", "none"),
            fixed_word: ("INLINE_CANON", "none"),
            owner: ("PUBLIC_PROBE", "two-architecture"),
            "RELATIVE-CONTACT-RHYTHM-CLASSIFICATION": ("INLINE_CANON", "none"),
            "RELATIVE-CONTACT-RHYTHM-ACCOUNT-BOUNDS": ("INLINE_CANON", "none"),
            "RELATIVE-CONTACT-RHYTHM-FIVEFOLD-PHASE": ("INLINE_CANON", "none"),
            "RELATIVE-CONTACT-COEFFICIENT-READ-INJECTIVITY": ("INLINE_CANON", "none"),
            'RELATIVE-CONTACT-POSITIONAL-BANK-COPY': ("INLINE_CANON", "none"),
            'RELATIVE-CONTACT-FOUR-PLACE-COPY-OBSTRUCTION': ("INLINE_CANON", "none"),
            'RELATIVE-CONTACT-FINITE-WORKBANK-REUSE': ("INLINE_CANON", "none"),
            compiler: ("INLINE_CANON", "none"),
            apparatus: ("INLINE_CANON", "none"),
            obstruction: ("INLINE_CANON", "none"),
        }
        for item, (kind, architecture_requirement) in expected_evidence.items():
            self.assertEqual(evidence[item]["evidence_kind"], kind)
            self.assertEqual(
                evidence[item]["architecture_requirement"], architecture_requirement
            )
            # REGISTRY evidence is one path or exactly inline, never a
            # semicolon-separated list of paths.
            self.assertEqual(
                registry[item]["evidence"],
                "probes/P-RELATIVE-CONTACT-FOUR-SLOT-MINIMUM-1/RESULT.md"
                if item == minimum else
                "probes/P-RELATIVE-CONTACT-INDEPENDENT-RELOAD-1/RESULT.md"
                if item == owner else "inline",
            )


    def test_v109_exact_declared_claims_and_evidence(self) -> None:
        # Exact ledger boundaries: the graph is not a physical implementation.
        normative_rows = architecture.read_tsv(
            ROOT / "canon/NORMATIVE.tsv", architecture.NORMATIVE_FIELDS
        )
        dependency_rows = architecture.read_tsv(
            ROOT / "canon/DEPENDENCIES.tsv", architecture.DEPENDENCY_FIELDS
        )
        registry = {row["claim_id"]: row for row in architecture.read_tsv(
            ROOT / "canon/REGISTRY.tsv", architecture.REGISTRY_FIELDS
        )}
        evidence = {row["claim_id"]: row for row in architecture.read_tsv(
            ROOT / "canon/EVIDENCE.tsv", architecture.EVIDENCE_FIELDS
        )}
        normative = {row["item_id"]: row for row in normative_rows}
        requires = architecture.dependency_graph(normative, dependency_rows, "REQUIRES")
        bounded_by = architecture.dependency_graph(normative, dependency_rows, "BOUNDED_BY")
        expected = (
        {'RELATIVE-CONTACT-POSITIONAL-BANK-COPY': {'status': 'T',
                                                   'item_type': 'THEOREM',
                                                   'requires': ('RELATIVE-CONTACT-INTEGRAL-LAW',),
                                                   'bounded_by': (),
                                                   'evidence_kind': 'INLINE_CANON',
                                                   'location': 'inline',
                                                   'hash_mode': 'registry-scope-sha256-v1',
                                                   'sha256': '1c4b6d0b712cdcac1876ab8d05b7508ffab73ff9738747be0f5348ada8f815fb',
                                                   'architecture_requirement': 'none'},
         'RELATIVE-CONTACT-FOUR-PLACE-COPY-OBSTRUCTION': {'status': 'T',
                                                          'item_type': 'THEOREM',
                                                          'requires': ('RELATIVE-CONTACT-INTEGRAL-LAW',),
                                                          'bounded_by': (),
                                                          'evidence_kind': 'INLINE_CANON',
                                                          'location': 'inline',
                                                          'hash_mode': 'registry-scope-sha256-v1',
                                                          'sha256': '1b9ffabfa4f016bbbc820a421e0240593a6a1e8cdb0b8a16e68e965efe1faf4c',
                                                          'architecture_requirement': 'none'},
         'RELATIVE-CONTACT-FINITE-WORKBANK-REUSE': {'status': 'T',
                                                    'item_type': 'THEOREM',
                                                    'requires': ('RELATIVE-CONTACT-COMMON-APPARATUS-OPEN',
                                                                 'RELATIVE-CONTACT-INTEGRAL-LAW',
                                                                 'RELATIVE-CONTACT-POSITIONAL-BANK-COPY'),
                                                    'bounded_by': ('RELATIVE-CONTACT-FIXED-WORD-RESIDUE-BOUNDARY',
                                                                   'RELATIVE-CONTACT-RETAINED-BANK-CAPACITY'),
                                                    'evidence_kind': 'INLINE_CANON',
                                                    'location': 'inline',
                                                    'hash_mode': 'registry-scope-sha256-v1',
                                                    'sha256': 'ef7f84cf9d59cbd9fccbf87de306b06be21194809c702a85e2e5d9c609c94d99',
                                                    'architecture_requirement': 'none'},
         'U-FIRST-TICK-AFFINE-TRACE-TRANSFER': {'status': 'T',
                                                'item_type': 'THEOREM',
                                                'requires': ('DEF-AUTONOMOUS-STATE',),
                                                'bounded_by': (),
                                                'evidence_kind': 'INLINE_CANON',
                                                'location': 'inline',
                                                'hash_mode': 'registry-scope-sha256-v1',
                                                'sha256': 'bc1581785aba917af1ce3ca93aaec9960134f86663ce89cff08cdd2988a8892d',
                                                'architecture_requirement': 'none'},
         'J-MARKED-CARRY-MIRROR': {'status': 'T',
                                   'item_type': 'THEOREM',
                                   'requires': ('J-UNIT', 'U-FIRST-TICK-AFFINE-TRACE-TRANSFER'),
                                   'bounded_by': (),
                                   'evidence_kind': 'INLINE_CANON',
                                   'location': 'inline',
                                   'hash_mode': 'registry-scope-sha256-v1',
                                   'sha256': 'ea9d98706f941718a28af38c50060847d4d3694edee18f35f3ec1725e2312207',
                                   'architecture_requirement': 'none'},
         'J-FIXED-INPUT-CARRY-PRECISION': {'status': 'T',
                                           'item_type': 'THEOREM',
                                           'requires': ('J-UNIT',),
                                           'bounded_by': (),
                                           'evidence_kind': 'INLINE_CANON',
                                           'location': 'inline',
                                           'hash_mode': 'registry-scope-sha256-v1',
                                           'sha256': '4fb162778ca28c8228c32bc7943c9babd06f209ad6a20c5767cc8ed72be16228',
                                           'architecture_requirement': 'none'},
         'U-CARRY-MIRROR-FINITE-CIRCUIT': {'status': 'C',
                                           'item_type': 'COMPUTATION',
                                           'requires': ('J-MARKED-CARRY-MIRROR',
                                                        'U-FIRST-TICK-AFFINE-TRACE-TRANSFER'),
                                           'bounded_by': (),
                                           'evidence_kind': 'PUBLIC_PROBE',
                                           'location': 'probes/P-NATIVE-RECEIVER-CARRY-MIRROR-1/RESULT.md',
                                           'hash_mode': 'bundle-manifest-sha256-v1',
                                           'sha256': '843e4a03c8765d732c09588f869bd70e6e2a9108c1576229055d7a4ddc326040',
                                           'architecture_requirement': 'two-architecture'}}
        )
        expected_edges = (
        [('J-FIXED-INPUT-CARRY-PRECISION', 'J-UNIT', 'REQUIRES'),
         ('J-MARKED-CARRY-MIRROR', 'J-UNIT', 'REQUIRES'),
         ('J-MARKED-CARRY-MIRROR', 'U-FIRST-TICK-AFFINE-TRACE-TRANSFER', 'REQUIRES'),
         ('RELATIVE-CONTACT-FINITE-WORKBANK-REUSE', 'RELATIVE-CONTACT-COMMON-APPARATUS-OPEN', 'REQUIRES'),
         ('RELATIVE-CONTACT-FINITE-WORKBANK-REUSE',
          'RELATIVE-CONTACT-FIXED-WORD-RESIDUE-BOUNDARY',
          'BOUNDED_BY'),
         ('RELATIVE-CONTACT-FINITE-WORKBANK-REUSE', 'RELATIVE-CONTACT-INTEGRAL-LAW', 'REQUIRES'),
         ('RELATIVE-CONTACT-FINITE-WORKBANK-REUSE', 'RELATIVE-CONTACT-POSITIONAL-BANK-COPY', 'REQUIRES'),
         ('RELATIVE-CONTACT-FINITE-WORKBANK-REUSE',
          'RELATIVE-CONTACT-RETAINED-BANK-CAPACITY',
          'BOUNDED_BY'),
         ('RELATIVE-CONTACT-FOUR-PLACE-COPY-OBSTRUCTION', 'RELATIVE-CONTACT-INTEGRAL-LAW', 'REQUIRES'),
         ('RELATIVE-CONTACT-POSITIONAL-BANK-COPY', 'RELATIVE-CONTACT-INTEGRAL-LAW', 'REQUIRES'),
         ('U-CARRY-MIRROR-FINITE-CIRCUIT', 'J-MARKED-CARRY-MIRROR', 'REQUIRES'),
         ('U-CARRY-MIRROR-FINITE-CIRCUIT', 'U-FIRST-TICK-AFFINE-TRACE-TRANSFER', 'REQUIRES'),
         ('U-FIRST-TICK-AFFINE-TRACE-TRANSFER', 'DEF-AUTONOMOUS-STATE', 'REQUIRES')]
        )
        self.assertEqual(sorted((row["item_id"], row["depends_on"], row["relation"])
                                for row in dependency_rows if row["item_id"] in expected),
                         expected_edges)
        for claim, contract in expected.items():
            self.assertEqual(registry[claim]["status"], contract["status"])
            self.assertEqual(normative[claim]["status"], contract["status"])
            self.assertEqual(normative[claim]["item_type"], contract["item_type"])
            self.assertEqual(normative[claim]["layer"], "L1")
            self.assertEqual(normative[claim]["gate_ids"], "")
            self.assertEqual(requires[claim], set(contract["requires"]))
            self.assertEqual(bounded_by[claim], set(contract["bounded_by"]))
            self.assertEqual(registry[claim]["evidence"], contract["location"])
            self.assertEqual(evidence[claim]["evidence_id"], "EV-" + claim)
            for field in ("evidence_kind", "location", "hash_mode", "sha256", "architecture_requirement"):
                self.assertEqual(evidence[claim][field], contract[field])
        memberships = (
        {'dependency_terminals': (),
         'direct_architecture_requires': (),
         'transitive_architecture_dependents': ()}
        )
        for field, exact in memberships.items():
            self.assertEqual(set(expected) & set(getattr(self.report, field)), set(exact))
        for owner in ("QUADRATIC-MEMORY-NATIVE-CONTACT", "QDD-INSTRUMENT-APPARATUS"):
            self.assertEqual(registry[owner]["status"], "O")

    def test_current_counts_match_the_public_summary(self) -> None:
        # audit(ROOT) reads this checkout, not the historical v10 map note.
        # v111 adds seven inline L1 theorems and two reproduced C claims.
        # All 612 prior claim statuses stay unchanged.
        self.assertEqual(self.report.claims, 621)
        self.assertEqual(
            self.report.status_counts,
            {"C": 42, "D": 59, "F": 19, "H": 2, "O": 24, "T": 475},
        )
        self.assertEqual(
            self.report.evidence_counts,
            {
                "none": 198,
                "one-architecture": 9,
                "recorded-audit": 31,
                "two-architecture": 383,
            },
        )
        self.assertFalse(self.report.count_mismatches)

    def test_architecture_is_a_hub_not_the_only_non_algebraic_root(self) -> None:
        self.assertEqual(len(self.report.direct_architecture_requires), 202)
        self.assertEqual(
            len(self.report.transitive_architecture_dependents), 385
        )
        self.assertEqual(len(self.report.dependency_terminals), 84)
        # v95 adds ten inline theorems (architecture_requirement=none).
        # Their declared premise edges add four terminals and no path to
        # DEF-ARCHITECTURE; this is a graph fact, not physical independence.
        terminals_v95 = {
            "INTEGER-F-JG-INVARIANTS",
            "INTEGER-ENERGY-FUNDED-INVOLUTION",
            "FIELD-SHEAR-ENERGY-BOUNDARY",
            "INTEGER-SEPARATED-FACTOR-CERTIFICATE",
        }
        nonterminals_v95 = {
            "U-NATIVE-SOURCE-RECEIVER-RECORD",
            "U-NATIVE-RECORD-CONTINUATION-BOUNDARY",
            "FIELD-GAUSS-CONTACT-MEMORY",
            "FIELD-EISENSTEIN-RESONANCE",
            "INTEGER-FINITE-PREACTIVATION-QUOTIENT",
            "FIELD-CHARGED-SEPARATION-BOUND",
        }
        for item in terminals_v95 | nonterminals_v95:
            self.assertNotIn(item, self.report.direct_architecture_requires)
            self.assertNotIn(item, self.report.transitive_architecture_dependents)
            self.assertEqual(item in self.report.dependency_terminals, item in terminals_v95)
        # v96 supplies one selected architecture definition and three
        # theorems. Their exact premise graph does not derive this choice
        # from DEF-ARCHITECTURE (the unchanged native-U architecture).
        normative = architecture.read_tsv(
            ROOT / "canon" / "NORMATIVE.tsv", architecture.NORMATIVE_FIELDS
        )
        dependencies = architecture.read_tsv(
            ROOT / "canon" / "DEPENDENCIES.tsv", architecture.DEPENDENCY_FIELDS
        )
        requires = architecture.dependency_graph(
            (row["item_id"] for row in normative), dependencies, "REQUIRES"
        )
        # The v101 raw-input readers and checkpoint obstruction depend on
        # the unchanged native architecture; none admits a physical reader.
        v101_edges = {
            "U-NATIVE-RAW-RESIDUE-READOUT": {
                "DEF-AUTONOMOUS-STATE", "U-NATIVE-APPARATUS-HISTORY-FACTOR",
            },
            "U-NATIVE-RECEIVER-ONLY-RESIDUE-NOGO": {
                "DEF-AUTONOMOUS-STATE", "U-NATIVE-APPARATUS-HISTORY-FACTOR",
                "U-NATIVE-INVARIANT-AND-NOWRITE",
            },
            "U-NATIVE-RAW-RESIDUE-PRESENCE-BOUNDARY": {
                "U-NATIVE-APPARATUS-HISTORY-FACTOR",
                "U-NATIVE-RAW-RESIDUE-READOUT",
            },
            "U-J-POWER-CHECKPOINT-NOGO": {
                "DEF-AUTONOMOUS-STATE", "CARRY-J-CHECKPOINT", "J-UNIT",
            },
        }
        for item, expected in v101_edges.items():
            self.assertEqual(requires[item], expected)
            self.assertIn(item, self.report.transitive_architecture_dependents)
            self.assertNotIn(item, self.report.direct_architecture_requires)
            self.assertNotIn(item, self.report.dependency_terminals)
        # The v100 conditional architecture and its three theorems reach
        # existing native definitions. These exact graph edges do not
        # independently admit the added interfaces or close the open owner.
        v100_edges = {
            "DEF-RESIDUAL-CONTACT-ARCHITECTURE": {
                "DEF-KERNEL-GENERATORS", "DEF-PISTON-2X2-RESHAPE",
                "DEF-QUADRATIC-MEMORY-L5",
            },
            "CONTACT-RECORD": {"DEF-RESIDUAL-CONTACT-ARCHITECTURE"},
            "ALGEBRAIC-RESIDUAL-REALIZATION": {"DEF-RESIDUAL-CONTACT-ARCHITECTURE"},
            "RESIDUAL-STEP-RECORD": {
                "CONTACT-RECORD", "ALGEBRAIC-RESIDUAL-REALIZATION",
            },
        }
        for item, expected in v100_edges.items():
            self.assertEqual(requires[item], expected)
            self.assertIn(item, self.report.transitive_architecture_dependents)
            self.assertNotIn(item, self.report.direct_architecture_requires)
            self.assertNotIn(item, self.report.dependency_terminals)
        # The generic finite-set lift is a new terminal. The other nine new
        # items reach the architecture through already registered premises;
        # this graph fact neither selects C nor supplies a native contact.
        self.assertEqual(requires["FINITE-READOUT-INITIALIZED-MEMORY"], set())
        self.assertIn("FINITE-READOUT-INITIALIZED-MEMORY", self.report.dependency_terminals)
        self.assertEqual(requires["DEF-QUADRATIC-MEMORY-L5"], {
            "TRACEKERNEL-F5-HODGE-BRACKET", "J-HODGE-PREDICTIVE-CLOSURE",
            "A4-RAMIFIED-HODGE-TRACEKERNEL",
        })
        self.assertEqual(requires["QUADRATIC-MEMORY-NATIVE-CONTACT"], {
            "DEF-QUADRATIC-MEMORY-L5",
        })
        # v98 adds seven declared items and fifteen exact premise edges.
        # Five Hodge comparisons reach DEF-ARCHITECTURE through their
        # existing Hodge premises; the readout definition and LS response
        # do not. This records the graph, not physical independence.
        v98_edges = {
            "DEF-U-ION-HODGE-READOUT-DOMAIN": {
                "DEF-AUTONOMOUS-STATE",
            },
            "U-HODGE-FAITHFUL-DIRECT-MEMORY": {
                "DEF-U-ION-HODGE-READOUT-DOMAIN",
                "J-HODGE-SEMILINEAR-MEMORY",
            },
            "ION-LS-CONNECTED-RESPONSE": {
                "DEF-U-ION-HODGE-READOUT-DOMAIN",
            },
            "U-ION-HODGE-AFFINE-OBSTRUCTION": {
                "DEF-U-ION-HODGE-READOUT-DOMAIN",
                "ION-LS-CONNECTED-RESPONSE",
                "J-HODGE-HERM2-LOXODROME",
            },
            "U-ION-HODGE-RESPONSE-FIBRE-CLASSIFICATION": {
                "DEF-U-ION-HODGE-READOUT-DOMAIN",
                "ION-LS-CONNECTED-RESPONSE",
                "J-HODGE-HERM2-LOXODROME",
            },
            "U-ION-HODGE-MEAN-SUFFICIENCY": {
                "DEF-U-ION-HODGE-READOUT-DOMAIN",
                "U-ION-HODGE-AFFINE-OBSTRUCTION",
            },
            "U-ION-HODGE-SCORED-CODE-TRANSPORT": {
                "DEF-U-ION-HODGE-READOUT-DOMAIN",
                "ION-LS-CONNECTED-RESPONSE",
                "J-HODGE-SEMILINEAR-MEMORY",
            },
        }
        v98_without_architecture_path = {
            "DEF-U-ION-HODGE-READOUT-DOMAIN",
            "ION-LS-CONNECTED-RESPONSE",
        }
        for item, expected in v98_edges.items():
            self.assertEqual(requires[item], expected)
            self.assertNotIn(item, self.report.direct_architecture_requires)
            self.assertNotIn(item, self.report.dependency_terminals)
            self.assertEqual(
                item in self.report.transitive_architecture_dependents,
                item not in v98_without_architecture_path,
            )
        definition = "DEF-FIELD-WORK-RECORD-CHAIN"
        law = "FIELD-CONSERVATIVE-CHAIN-LAW"
        work = "FIELD-CHAIN-FIRST-WORK"
        record = "FIELD-LOCAL-WORK-RECORD"
        self.assertEqual(requires[definition], set())
        self.assertEqual(requires[law], {definition})
        self.assertEqual(requires[work], {law})
        self.assertEqual(requires[record], {definition, law, work})
        self.assertIn(definition, self.report.dependency_terminals)
        for item in (definition, law, work, record):
            self.assertNotIn(item, self.report.direct_architecture_requires)
            self.assertNotIn(item, self.report.transitive_architecture_dependents)
        for claim in (law, work, record):
            self.assertTrue(architecture.reaches(requires, claim, definition))
            self.assertFalse(
                architecture.reaches(requires, claim, architecture.ARCHITECTURE_ITEM)
            )
            self.assertNotIn(claim, self.report.dependency_terminals)
        # v94 adds three theorem rows with existing theorem premises: two
        # public-probe evidence rows and one inline composition. All three
        # reach the declared architecture transitively, with no new root.
        # v92 adds one architecture-dependent L5 blocking theorem. The Bell
        # comparison has only a BOUNDED_BY edge; the self-contained finite
        # photon measure is one new dependency terminal. These are exact
        # declared graph additions, not inferred physical dependencies.
        self.assertIn("METRO-COMMON-BLOCKING", self.report.direct_architecture_requires)
        self.assertNotIn("COUNTER-BELL-PRICE", self.report.transitive_architecture_dependents)
        self.assertIn("PHOTON-CONDITIONAL-VARIANCE-FLOOR", self.report.dependency_terminals)
        # Five v93 L1 theorems have declared premises that eventually
        # reach the public architecture, but none requires DEF-ARCHITECTURE
        # directly and none is a declared-dependency terminal.
        for item in (
            "ZETA5-DEDEKIND-RESIDUE",
            "J-UNIT-STRIP-NORMAL-FORM",
            "J-SCALAR-CODE-CAPACITY-3125",
            "QDD-GALOIS-SUM-RATIO",
            "ZETA5-IDEAL-COUNT-LANDAU",
        ):
            self.assertIn(item, self.report.transitive_architecture_dependents)
            self.assertNotIn(item, self.report.direct_architecture_requires)
            self.assertNotIn(item, self.report.dependency_terminals)
        # The sixth v93 theorem depends on the exact J projection and axiom,
        # not the native architecture. It has a premise, so it is not a terminal.
        self.assertNotIn("J-ENDPOINT-GROWTH", self.report.transitive_architecture_dependents)
        self.assertNotIn("J-ENDPOINT-GROWTH", self.report.direct_architecture_requires)
        self.assertNotIn("J-ENDPOINT-GROWTH", self.report.dependency_terminals)
        # v91 adds four direct native requirements. The selected dictionaries
        # consume their explicit mathematical models through separate gates;
        # the closed TT existence owner now depends on its adopted witness.
        for item in (
            "ENTROPY-MEASURABLE-OBSTRUCTION",
            "U-STABLE-PAIRED-PORT-TRANSPORT",
            "QDD-PORT-QUOTIENT-ORIGIN-BOUNDARY",
            "QDD-NATIVE-AFFINE-ENTRANCE-MINIMUM",
        ):
            self.assertIn(item, self.report.direct_architecture_requires)
        for item in (
            "QDD-SELECTED-BORN", "QDD-SELECTED-PAIR-LAW",
            "SELECTED-COSMOLOGICAL-COMPARISON",
            "TT-VECTOR-STATE-NORMALIZATION",
        ):
            self.assertIn(item, self.report.transitive_architecture_dependents)
            self.assertNotIn(item, self.report.dependency_terminals)
        # v90 adds six direct native requirements. The remaining Hodge and
        # native theorems reach architecture through CARRY-PENTAD, the digit
        # lift, or the complete native linear group; no new item is terminal.
        direct_v90 = (
            "NATIVE-BC-HODGE-D5-OBSTRUCTION",
            "NATIVE-LINEAR-HODGE-ORDER5-OBSTRUCTION",
            "U-COUNTER-SEPARABLE-QUOTIENT",
            "U-COUNTER-REACHABLE-AMPLITUDE-CLASS",
            "U-SELECTOR-AMPLITUDE-COMMON-FACTOR",
            "U-COUNTER-ADDITIVE-AMPLITUDE-OBSTRUCTION",
        )
        indirect_v90 = (
            "J-HODGE-PREDICTIVE-CLOSURE",
            "A4-RAMIFIED-HODGE-TRACEKERNEL",
            "J-HODGE-HERM2-LOXODROME",
            "J-C5-HODGE-CONIC-ATLAS",
            "U-J-HODGE-FINITE-READER-BOUNDARY",
            "J-HODGE-RATIONAL-CLOSURE",
            "NATIVE-LINEAR-JHODGE-STEP-OBSTRUCTION",
            "J-HODGE-COUNTER-CARRY-EXPONENT",
            "J-HODGE-SEMILINEAR-MEMORY",
        )
        for claim in direct_v90:
            self.assertIn(claim, self.report.direct_architecture_requires)
        for claim in indirect_v90:
            self.assertNotIn(claim, self.report.direct_architecture_requires)
        for claim in direct_v90 + indirect_v90:
            self.assertIn(claim, self.report.transitive_architecture_dependents)
            self.assertNotIn(claim, self.report.dependency_terminals)
        # v89 adds one direct native point-port theorem and two coherent-code
        # channel theorems that require architecture through the existing code.
        point_port = "QDD-NATIVE-POINT-PORT-CAPACITY"
        self.assertIn(point_port, self.report.direct_architecture_requires)
        for claim in (
            point_port,
            "U-GALOIS-CPTP-POINT-COMPATIBILITY",
            "U-GALOIS-OPTIMAL-AUXILIARY-DIMENSION",
        ):
            self.assertIn(claim, self.report.transitive_architecture_dependents)
            self.assertNotIn(claim, self.report.dependency_terminals)
        for claim in (
            "U-GALOIS-CPTP-POINT-COMPATIBILITY",
            "U-GALOIS-OPTIMAL-AUXILIARY-DIMENSION",
        ):
            self.assertNotIn(claim, self.report.direct_architecture_requires)
        # v88 adds only three L1 theorem items; all reach architecture
        # transitively through exact existing passive source definitions.
        for item in (
            "QDD-PASSIVE-QUADRATIC-CALIBRATION",
            "QDD-PASSIVE-THRESHOLD-MOMENT-COMPLETION",
            "QDD-PASSIVE-NATIVE-MEMORY",
        ):
            self.assertNotIn(item, self.report.direct_architecture_requires)
            self.assertIn(item, self.report.transitive_architecture_dependents)
            self.assertNotIn(item, self.report.dependency_terminals)
        # v87 adds one direct owner-selected passive dictionary. Its source
        # maps and theorem reach architecture through the existing K_QDD
        # domain; the partition/record definitions require only exact algebra.
        reading = "QDD-OBSERVABLE-READING-FAMILY"
        self.assertIn(reading, self.report.direct_architecture_requires)
        self.assertIn(reading, self.report.transitive_architecture_dependents)
        self.assertNotIn(reading, self.report.dependency_terminals)
        for item in (
            "DEF-QDD-PASSIVE-READING-MAPS",
            "QDD-THREE-ATOM-PARTITION-COMPLETENESS",
        ):
            self.assertNotIn(item, self.report.direct_architecture_requires)
            self.assertIn(item, self.report.transitive_architecture_dependents)
            self.assertNotIn(item, self.report.dependency_terminals)
        for item in (
            "DEF-QDD-PASSIVE-PARTITION-FAMILY",
            "DEF-QDD-PASSIVE-WEIGHT-RECORD",
        ):
            self.assertNotIn(item, self.report.direct_architecture_requires)
            self.assertNotIn(item, self.report.transitive_architecture_dependents)
            self.assertNotIn(item, self.report.dependency_terminals)
        # v86 adds two direct native requirements and one dependent split.
        code = "U-GALOIS-FIBER-CODE"
        split = "U-GALOIS-FIBER-QDD-SPLIT"
        point = "U-POINT-SOURCE-SHARP-READOUT-NOGO"
        for claim in (code, point):
            self.assertIn(claim, self.report.direct_architecture_requires)
        self.assertNotIn(split, self.report.direct_architecture_requires)
        for claim in (code, split, point):
            self.assertIn(claim, self.report.transitive_architecture_dependents)
            self.assertNotIn(claim, self.report.dependency_terminals)
        # v85 separates four L1 mathematical results from the existing
        # isolated-emission dictionary. Only the native word-law theorem
        # adds a direct architecture edge; all four reach it transitively.
        word_law = "TT-NATIVE-FOUR-WORD-LAW"
        self.assertIn(word_law, self.report.direct_architecture_requires)
        for claim in (
            word_law,
            "TT-QUADRATIC-SOURCE-CLASSIFICATION",
            "TT-ISOLATED-EMISSION-TOTALITY",
            "TT-ISOLATED-EMISSION-WORK-BALANCE",
        ):
            self.assertIn(claim, self.report.transitive_architecture_dependents)
            self.assertNotIn(claim, self.report.dependency_terminals)
        # v84 adds one isolated-emission definition through existing K1
        # definitions. TT-SOURCE changes O to D and retains its direct edge.
        emission = "DEF-K1-ISOLATED-TT-EMISSION"
        self.assertNotIn(emission, self.report.direct_architecture_requires)
        self.assertIn(emission, self.report.transitive_architecture_dependents)
        self.assertNotIn(emission, self.report.dependency_terminals)
        self.assertIn("TT-SOURCE", self.report.direct_architecture_requires)
        # v83 adds one explicit hybrid definition. FRW-INHOM changes O to D
        # while retaining its architecture dependency through the selected gate.
        hybrid = "DEF-K1-HYBRID-FRW-CELL-METRIC"
        self.assertIn(hybrid, self.report.direct_architecture_requires)
        self.assertIn(hybrid, self.report.transitive_architecture_dependents)
        self.assertNotIn(hybrid, self.report.dependency_terminals)
        self.assertIn("FRW-INHOM", self.report.direct_architecture_requires)
        # v82 adds an explicit mathematical definition requiring the
        # architecture and a theorem requiring only that definition.
        self.assertIn("DEF-K1-LINEAR-METRIC", self.report.direct_architecture_requires)
        self.assertNotIn(
            "K1-LINEAR-METRIC-COMPLETION", self.report.direct_architecture_requires
        )
        for item in ("DEF-K1-LINEAR-METRIC", "K1-LINEAR-METRIC-COMPLETION"):
            self.assertIn(item, self.report.transitive_architecture_dependents)
            self.assertNotIn(item, self.report.dependency_terminals)
        # The eight v81 decoder-boundary theorems declare same-layer L1
        # requirements and owner boundaries only. Seven reach the architecture
        # transitively through registered native rows; the renewal inverse
        # declares no requirement, so it is neither an architecture dependent
        # nor, because of its declared owner boundaries, a terminal.
        for claim in (
            "BINARY-RECORD-VALUATION-NONSELECTION",
            "RECORD-OCCURRENCE-SELECTION-CRITERIA",
            "RELATIONAL-GROWTH-SATURATION-BOUNDARY",
            "U-FINITE-READER-INDEPENDENCE-OBSTRUCTION",
            "OCCURRENCE-ADDRESS-AND-LOG-EQUALITY",
            "RECORD-LOADER-RETENTION-CLASS",
            "TRC1-CALIBRATION-IDENTIFIABILITY",
        ):
            self.assertNotIn(claim, self.report.direct_architecture_requires)
            self.assertIn(claim, self.report.transitive_architecture_dependents)
            self.assertNotIn(claim, self.report.dependency_terminals)
        renewal = "REGISTRATION-PAIR-RECOVERY-INVERSE"
        self.assertNotIn(renewal, self.report.direct_architecture_requires)
        self.assertNotIn(renewal, self.report.transitive_architecture_dependents)
        self.assertNotIn(renewal, self.report.dependency_terminals)
        # The two v80 reading-boundary theorems declare no dependency edge, so
        # they are declared-dependency terminals and add no architecture
        # coupling in either direction.
        for claim in (
            "A4-RATIONAL-FRAME-WEIGHT-NONUNIQUENESS",
            "QDD-SIMPLEX-PAIR-INCIDENCE",
        ):
            self.assertNotIn(claim, self.report.direct_architecture_requires)
            self.assertNotIn(
                claim, self.report.transitive_architecture_dependents
            )
            self.assertIn(claim, self.report.dependency_terminals)
        for claim in (
            "U-NATIVE-COMMON-READY-SOURCE-RETENTION",
            "QDD-INCIDENCE-FIRST-HIT-CLASSIFICATION",
        ):
            self.assertNotIn(claim, self.report.direct_architecture_requires)
            self.assertIn(claim, self.report.transitive_architecture_dependents)
            self.assertNotIn(claim, self.report.dependency_terminals)
        mixed_claim = "QDD-MIXED-CHANNEL-ATTENUATION-RIGIDITY"
        self.assertNotIn(mixed_claim, self.report.direct_architecture_requires)
        self.assertNotIn(mixed_claim, self.report.transitive_architecture_dependents)
        self.assertNotIn(mixed_claim, self.report.dependency_terminals)
        self.assertIn(
            "JIPC-WP3D-QPOS-SCALAR-SLICE",
            self.report.dependency_terminals,
        )
        # The adopted v91 accounting witness consumes the three pair gates.
        self.assertNotIn("BELL-CAUSAL-ACCOUNTING", self.report.dependency_terminals)
        self.assertIn(
            "BELL-CAUSAL-ACCOUNTING", self.report.transitive_architecture_dependents
        )
        self.assertNotIn(
            "DQRC-MAXIMAL-SECTOR-FIELD-BOUNDARY",
            self.report.direct_architecture_requires,
        )
        self.assertIn(
            "DQRC-MAXIMAL-SECTOR-FIELD-BOUNDARY",
            self.report.transitive_architecture_dependents,
        )
        self.assertIn(
            "DEF-DQRC-INTEGER-CENSUS", self.report.dependency_terminals
        )
        self.assertIn(
            "SO3-FINITE-ANISOTROPY-MAXIMUM",
            self.report.dependency_terminals,
        )
        self.assertNotIn(
            "SO3-FINITE-ANISOTROPY-MAXIMUM",
            self.report.direct_architecture_requires,
        )
        self.assertNotIn(
            "SO3-FINITE-ANISOTROPY-MAXIMUM",
            self.report.transitive_architecture_dependents,
        )
        self.assertIn(
            "FCC-WEIGHTED-SHELL-SYMBOL", self.report.dependency_terminals
        )
        self.assertNotIn(
            "FCC-WEIGHTED-SHELL-SYMBOL",
            self.report.transitive_architecture_dependents,
        )
        for claim in (
            "PHOTON-WILSON-VILLAIN-FINITE-COUPLING-NONMEMBERSHIP",
            "PHOTON-MASSLESS-PHASE",
        ):
            self.assertNotIn(claim, self.report.direct_architecture_requires)
            self.assertIn(
                claim, self.report.transitive_architecture_dependents
            )
            self.assertNotIn(claim, self.report.dependency_terminals)
        self.assertNotIn(
            "PHOTON-CONE-CONVERGENCE",
            self.report.direct_architecture_requires,
        )
        self.assertNotIn(
            "PHOTON-CONE-CONVERGENCE",
            self.report.transitive_architecture_dependents,
        )
        self.assertIn(
            "DE-W-CONSTANT", self.report.direct_architecture_requires
        )
        self.assertNotIn("DE-W-CONSTANT", self.report.dependency_terminals)
        self.assertIn(
            "KERNEL-SUBSET-LANDSCAPE",
            self.report.transitive_architecture_dependents,
        )
        self.assertNotIn(
            "KERNEL-SUBSET-LANDSCAPE", self.report.dependency_terminals
        )
        for claim in (
            "J-LI-PENTAGON-DILATION-DEFICIENCY",
            "J-LI-CYCLIC-CARRIER-DIMENSION",
            "TM-ENTROPY-ZERO",
            "BINARY-READ-RELATIVE-ENTROPY",
        ):
            self.assertIn(claim, self.report.dependency_terminals)
            self.assertNotIn(claim, self.report.direct_architecture_requires)
        for claim in ("PENTAGON-ONLY-DILATIONS", "J-TORAL-ENTROPY"):
            self.assertNotIn(claim, self.report.dependency_terminals)
            self.assertNotIn(
                claim, self.report.transitive_architecture_dependents
            )
        for claim in (
            "CYCLOTOMIC-CLASS-NUMBER-ONE",
            "METRO-FORBIDDEN-WITNESSES",
        ):
            self.assertIn(
                claim, self.report.transitive_architecture_dependents
            )
            self.assertNotIn(claim, self.report.dependency_terminals)
        for claim in (
            "J-MAHLER-MEASURE",
            "REGULATOR-TWO-LOG-PHI",
            "J-TORAL-PERIODIC-POINTS",
        ):
            self.assertNotIn(claim, self.report.dependency_terminals)
            self.assertNotIn(
                claim, self.report.transitive_architecture_dependents
            )
        for claim in (
            "SPLIT-PRIME-RAPIDITY-QUANTITATIVE-SEPARATION",
            "SPLIT-RAPIDITY-FEJER-GRAM-BOUND",
        ):
            self.assertNotIn(claim, self.report.direct_architecture_requires)
            self.assertNotIn(
                claim, self.report.transitive_architecture_dependents
            )
            self.assertNotIn(claim, self.report.dependency_terminals)
        self.assertNotIn(
            "KERNEL-Z6-SYNCHRONIZATION",
            self.report.direct_architecture_requires,
        )
        self.assertNotIn(
            "KERNEL-Z6-SYNCHRONIZATION",
            self.report.transitive_architecture_dependents,
        )
        self.assertIn(
            "GYRON-DISCREPANCY-LOG",
            self.report.direct_architecture_requires,
        )
        self.assertIn(
            "METRO-REDUCTION-ARROWS",
            self.report.direct_architecture_requires,
        )
        self.assertIn(
            "METRO-REDUCTION-ARROWS",
            self.report.transitive_architecture_dependents,
        )
        self.assertIn(
            "TM-PAIR-SUBSTITUTION-FIXED-POINT",
            self.report.direct_architecture_requires,
        )
        self.assertIn(
            "MINIMAL-READ-DERIVATION",
            self.report.direct_architecture_requires,
        )
        self.assertNotIn(
            "OBSERVER-WRITE-PORT",
            self.report.direct_architecture_requires,
        )
        self.assertNotIn(
            "OBSERVER-WRITE-PORT",
            self.report.transitive_architecture_dependents,
        )
        self.assertIn(
            "TM-SYM2-SPECTRAL-COHERENCE",
            self.report.direct_architecture_requires,
        )
        self.assertNotIn(
            "DRIFT-IS-THE-READ",
            self.report.direct_architecture_requires,
        )
        self.assertNotIn(
            "COLOR-CM-2I-SEMILINEAR-PAIR",
            self.report.direct_architecture_requires,
        )
        self.assertIn(
            "COLOR-CM-2I-SEMILINEAR-PAIR",
            self.report.transitive_architecture_dependents,
        )
        self.assertNotIn(
            "CENTRAL-LIFT-PHASE",
            self.report.direct_architecture_requires,
        )
        self.assertNotIn(
            "CENTRAL-LIFT-PHASE",
            self.report.transitive_architecture_dependents,
        )
        self.assertNotIn(
            "QUARTIC-CYCLOTOMIC-TOTAL-RAMIFICATION-CENSUS",
            self.report.direct_architecture_requires,
        )
        self.assertIn(
            "QUARTIC-CYCLOTOMIC-TOTAL-RAMIFICATION-CENSUS",
            self.report.transitive_architecture_dependents,
        )
        self.assertNotIn(
            "ABELIAN-CM-UNIQUE-EVEN-BIT-DISCRIMINANT-MINIMUM",
            self.report.direct_architecture_requires,
        )
        self.assertNotIn(
            "ABELIAN-CM-UNIQUE-EVEN-BIT-DISCRIMINANT-MINIMUM",
            self.report.transitive_architecture_dependents,
        )
        self.assertNotIn(
            "CM-ALTERNATING-PENCIL",
            self.report.direct_architecture_requires,
        )
        self.assertNotIn(
            "CM-ALTERNATING-PENCIL",
            self.report.transitive_architecture_dependents,
        )
        for claim in (
            "CM-ALTERNATING-PRIMARY-LATTICE-SEAM",
            "CM-REAL-DIFFERENT-PRIMARY-SEAM",
            "CM-PERIOD-LATTICE-NONSELECTION",
        ):
            self.assertNotIn(claim, self.report.direct_architecture_requires)
            self.assertNotIn(
                claim, self.report.transitive_architecture_dependents
            )
            self.assertNotIn(claim, self.report.dependency_terminals)
        for claim in (
            "RAMIFIED-TM-SYMPLECTIC-ORIENTATION",
            "CM-RAMIFIED-PFAFFIAN-ROOT",
        ):
            self.assertNotIn(claim, self.report.direct_architecture_requires)
            self.assertIn(
                claim, self.report.transitive_architecture_dependents
            )
            self.assertNotIn(claim, self.report.dependency_terminals)
        self.assertNotIn(
            "J-HARMONIC-SEAM",
            self.report.direct_architecture_requires,
        )
        self.assertNotIn(
            "J-HARMONIC-SEAM",
            self.report.transitive_architecture_dependents,
        )
        self.assertNotIn(
            "MOBIUS-TM-PRIME2-BRIDGE",
            self.report.direct_architecture_requires,
        )
        self.assertNotIn(
            "MOBIUS-TM-PRIME2-BRIDGE",
            self.report.transitive_architecture_dependents,
        )
        self.assertIn(
            "MOBIUS-TM-PRIME2-BRIDGE", self.report.dependency_terminals
        )
        self.assertNotIn(
            "TM-MULTIPLICATION-CARRY-DEFECT",
            self.report.direct_architecture_requires,
        )
        self.assertNotIn(
            "TM-MULTIPLICATION-CARRY-DEFECT",
            self.report.transitive_architecture_dependents,
        )
        self.assertIn(
            "TM-MULTIPLICATION-CARRY-DEFECT",
            self.report.dependency_terminals,
        )
        for claim in (
            "TM-HANKEL-DIVISOR-BRIDGE",
            "TM-HANKEL-SQUAREFUL-RANK-NOGO",
            "TM-HANKEL-EXTREMAL-WITT-SKELETON",
            "TM-HANKEL-K2-TRANSFER",
            "TM-HANKEL-K3-UNIVERSAL-TRANSFER",
            "TM-HANKEL-K3-TWO-SCALAR-CLASSIFICATION",
            "TM-HANKEL-K3-QUADRATIC-INVARIANT-SUFFICIENCY",
            "ARITHMETIC-RAPIDITY-DECOMPOSITION",
            "SPLIT-PRIME-RAPIDITY-CLASS",
            "SPLIT-PRIME-RAPIDITY-CONSTRUCTION-AGREEMENT",
        ):
            self.assertIn(claim, self.report.dependency_terminals)
            self.assertNotIn(claim, self.report.direct_architecture_requires)
            self.assertNotIn(
                claim, self.report.transitive_architecture_dependents
            )
        for claim in (
            "DRIFT-IS-THE-READ",
            "COIN-SELECTION-CONDITIONAL",
            "COIN-MINIMAL-READ",
            "MINIMAL-READ-DERIVATION",
        ):
            self.assertIn(
                claim, self.report.transitive_architecture_dependents
            )
        self.assertIn("ANCHOR-ELECTRON-MASS", self.report.dependency_terminals)
        self.assertIn(
            "METRO-FINITE-STATE-RATIONALITY", self.report.dependency_terminals
        )

    def test_section_16_wall_is_mixed(self) -> None:
        self.assertIn(
            "P5-ROOT-SELECTION", self.report.wall_architecture_dependent
        )
        self.assertIn(
            "J-LI-E8-SHELL-MULTIPLICITY-NOGO",
            self.report.wall_architecture_dependent,
        )
        self.assertIn(
            "MCKAY-THETA-FUNCTIONAL-CALCULUS-CARRIER",
            self.report.wall_architecture_dependent,
        )
        self.assertIn(
            "PENTAGON-NORMALIZATION", self.report.wall_architecture_free
        )
        self.assertIn("WALL-LI2-RUNG", self.report.wall_architecture_free)
        self.assertIn(
            "WALL-CIRCLE-LEMMA", self.report.wall_architecture_free
        )
        self.assertIn("J-LI-TORAL-HAAR-NOGO", self.report.wall_architecture_free)
        self.assertTrue(self.report.wall_architecture_dependent)
        self.assertTrue(self.report.wall_architecture_free)

    def test_census_edges_are_missing_or_honest_bounds(self) -> None:
        expected_missing = tuple(
            item
            for item in architecture.CENSUS_CONSUMERS
            if not self.report.census_edges[item]
        )
        self.assertEqual(self.report.census_missing, expected_missing)
        for relations in self.report.census_edges.values():
            self.assertNotIn("REQUIRES", relations)
            if relations:
                self.assertIn("BOUNDED_BY", relations)

    def test_census_debt_messages_distinguish_missing_bound_and_premise(self) -> None:
        def make_report(relations: tuple[str, ...]) -> architecture.AuditReport:
            edges = {item: relations for item in architecture.CENSUS_CONSUMERS}
            missing = tuple(item for item, values in edges.items() if not values)
            wrong = tuple(
                item
                for item, values in edges.items()
                if values and "BOUNDED_BY" not in values
            )
            return architecture.AuditReport(
                claims=0,
                status_counts={},
                evidence_counts={},
                direct_architecture_requires=(),
                transitive_architecture_dependents=(),
                dependency_terminals=(),
                wall_architecture_dependent=("BOUND",),
                wall_architecture_free=("FREE",),
                census_edges=edges,
                census_missing=missing,
                census_wrong_relation=wrong,
                count_mismatches=(),
            )

        self.assertIn("missing CENSUS-313 bounds", make_report(()).debt[0])
        self.assertFalse(make_report(("BOUNDED_BY",)).debt)
        self.assertIn("must include BOUNDED_BY", make_report(("REQUIRES",)).debt[0])

    def test_cli_exit_codes_distinguish_report_from_gate(self) -> None:
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            default_code = architecture.main(["--root", str(ROOT)])
            strict_code = architecture.main(["--root", str(ROOT), "--strict"])
        self.assertEqual(default_code, 0)
        self.assertEqual(strict_code, 1 if self.report.debt else 0)
        if self.report.debt:
            self.assertIn("Debt", output.getvalue())


if __name__ == "__main__":
    unittest.main()
