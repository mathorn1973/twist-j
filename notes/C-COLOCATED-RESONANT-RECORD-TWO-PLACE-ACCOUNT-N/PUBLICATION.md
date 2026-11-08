<!-- SPDX-License-Identifier: Apache-2.0 -->

# Public intake provenance

**NON-CANONICAL / L1.** This intake was prepared after local execution.
It is not a prospective public preregistration or a formal public probe.

## Source preservation and intake boundary

Original local source pin: 19ff593512de31d8018edfc63d87f7294da7757e.
Original local outcome: f7e2ea7dfacf9870bc1bc67f0d121d3b14019b37.
Their original baseline is d4d363722f052141a4ce65e9da39f11a74b43b95.

These are retained local archival identifiers, not claimed public ancestor
commits. The original history and bundle remain intact. This intake has a
separate lineage from public main a8482d068156c8f42a390a81e817566b1c5abeda;
it does not publish the original private history.

PROOF.md, PREREG.md, both executable files and both expected files are exact
copies. ERRATA.md corrects one intermediate sign in the preserved proof.
The preregistration's source hashes describe the original local files;
they must not be mistaken for hashes of the edited intake README or source
guide. The original six-file freeze is retained locally without alteration.

README.md, SOURCES.md, RUN.md, RESULT.md and REVIEW.md were edited after
execution to correct reporting, state limits accurately and remove private
coordination metadata. ERRATA.md and this provenance record are additive.
The intake SHA256SUMS covers the intake files, excluding itself.

No exact code, finite fixture, pass/fail threshold or committed expected
output has changed. Raw Windows stdout still fails direct comparison with
the LF expected output; RUN.md preserves that finding and the separately
successful newline-normalized comparison. This is not retroactive repair of
the original execution record.

## File mapping

SHA-256 values identify bytes. A changed prose file is explicitly marked
edited; it is not represented as an unchanged frozen source.

| File | Original bytes | Original SHA-256 | Intake bytes | Intake SHA-256 | Relation |
| --- | ---: | --- | ---: | --- | --- |
| BREAK_EXPECTED.txt | 576 | a9e13f041b866a4dcae3b17754e01d5c2f6184835b02b1b26d7e3e8bb204c1f4 | 576 | a9e13f041b866a4dcae3b17754e01d5c2f6184835b02b1b26d7e3e8bb204c1f4 | identical |
| EXPECTED.txt | 576 | a9e13f041b866a4dcae3b17754e01d5c2f6184835b02b1b26d7e3e8bb204c1f4 | 576 | a9e13f041b866a4dcae3b17754e01d5c2f6184835b02b1b26d7e3e8bb204c1f4 | identical |
| PREREG.md | 7441 | 7f562d5b351a6e7bb19345ba05dca64bf3db4d518355693ffba26dd87bf667e0 | 7441 | 7f562d5b351a6e7bb19345ba05dca64bf3db4d518355693ffba26dd87bf667e0 | identical |
| PROOF.md | 25877 | 428b9ca0072bf9e997898b9d3e6de5b9f9a4a23c4b855169c4782ec693a75c04 | 25877 | 428b9ca0072bf9e997898b9d3e6de5b9f9a4a23c4b855169c4782ec693a75c04 | identical |
| README.md | 4231 | 6ef418c8e8d372e99888a32112543d77f851d9d17c2e01fce68062206e309216 | 4117 | fa7c33b6a4bc60856a24627817af1ce14ec41980633b9ddd87e02a5b56779e54 | edited after execution |
| RESULT.md | 4875 | a5e625520e10266d5b6af284b7f6327591dfcd47416b20646c849b47dd187891 | 2875 | e4ab2a81815bcdac56a5f5d2d032079fdb62d460ed5c8098439a699387609c5b | edited after execution |
| REVIEW.md | 6054 | 8b1c79eaa735750bb520b26d9b1962f668167d31f163e94b43d33aafae9a2ce6 | 3183 | 32202c982bc7ce8edef048a3972f810725723aff35d37ffea6bd23b068ea8394 | edited after execution |
| RUN.md | 2123 | 4c65873d2ffe548a37ee7406ccb08c9a6c7a659bbbf725103ff7e1b56b5ce27a | 3151 | fd020bb1064f6f7d21464807e89b491b40298cdbe829b8a37b9c7c0d76acd6b1 | edited after execution |
| SOURCES.md | 3127 | 416714dcd949f2d93633459e76d44e44abd974c98a40842d315ce546176acc25 | 2974 | c478330437b310616d544967c64a4b59f78119c5b871585bb31d37457fac19a2 | edited after execution |
| break.py | 31928 | a1dd4213b92731f7f5050eccbfc36a2cf30a2f92c4c0b2755574afcf8f96f9ec | 31928 | a1dd4213b92731f7f5050eccbfc36a2cf30a2f92c4c0b2755574afcf8f96f9ec | identical |
| verify.py | 30892 | e2daf2f53e1e2e1410bb1fdd5a09a108c081e8b7a1ecb9090809c9ea05edc692 | 30892 | e2daf2f53e1e2e1410bb1fdd5a09a108c081e8b7a1ecb9090809c9ea05edc692 | identical |

The original checksum file was 844 bytes, SHA-256
32cdae9d511d5db3d24990d256a54ee444d9b02d029fdc014fb2e2814d1dd504. All eleven entries were checked
against the original files before intake. The original bundle was 38538 bytes,
SHA-256 892076e01783ef921da271df33a2c010391504870a8e6b73851042fdac3a397d;
its Git prerequisite and recorded head were verified.

## Acceptance boundary

The local freeze, model consultation and successful mathematical replay do not
supply a prospective public pin, an aarch64 replay or independent scientific
acceptance. Routine repository CI does not by itself replay note verifiers.
The public note remains conditional NON-CANONICAL / L1 evidence pending review.
No Canon, probe, reproduction, tool or workflow file is part of this intake.
