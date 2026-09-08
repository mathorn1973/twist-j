#!/usr/bin/env python3
"""Current Public Canon theorem/dictionary separation audit.

Standard library only. This witness checks the ledger boundary introduced by
Genesis review G2B. It does not establish new physics or new mathematics; it
verifies that named exact rows remain at T and that their physical readings
are carried by explicit D, C, H, or O rows.
"""

import csv
import hashlib
import io
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "canon" / "REGISTRY.tsv"
NORMATIVE = ROOT / "canon" / "NORMATIVE.tsv"
DEPENDENCIES = ROOT / "canon" / "DEPENDENCIES.tsv"
EVIDENCE = ROOT / "canon" / "EVIDENCE.tsv"
HISTORY = ROOT / "canon" / "HISTORY.tsv"
GATES = ROOT / "canon" / "GATES.tsv"
FRONTIER_PROGRAMS = ROOT / "canon" / "FRONTIER_PROGRAMS.tsv"
CORE = ROOT / "canon" / "CORE.md"
CORE_SELECTION = ROOT / "canon" / "CORE_SELECTION.tsv"
FRONTIER = ROOT / "canon" / "FRONTIER.md"
CANON = ROOT / "canon" / "CANON.md"
REPRODUCE = ROOT / "reproduce"
SUCCESSOR_MANIFEST_DIR = (
    ROOT / "notes" / "canon" / "QDD-ALGEBRAIC-DMATTER-SUCCESSOR-V70"
)


# Frozen from the public v82 proposal merge, still carrying the v81 ledgers:
# dc10fba7c0501e08d6843aaab49ae32d1239a79f. Remove only the exact v82 additions;
# every recovered byte must equal that immutable base before older guards run.
V82_LEDGER_PATCH = {
    "REGISTRY.tsv": {
        "prior_sha256": "ce8906de1b427d0b79714a2abece6d8b7efe5f74ebd53ec46f8b195373a354eb",
        "remove": ("a22f3ca417a67c98766a6e43c5e8090b35baac40a4c1c14d90465e9af97e8f45",),
    },
    "NORMATIVE.tsv": {
        "prior_sha256": "8f3e71ad64e56b2cfd0ce0b0ceef1db15ec28a6eca0ea8e51562642a8fa58486",
        "remove": (
            "60cef2d630857d230ab87e9049596f0be6d709d17ab8df337da2785b9001b580",
            "e323ca695286544bcf321f7e3a31470e9c6d65fa3ce2d44fb2394f959fb41227",
        ),
    },
    "DEPENDENCIES.tsv": {
        "prior_sha256": "eb68977b3e5b886c07d4d897bfeaef1152c4632a651d457de2bb2d1bdb76060c",
        "remove": (
            "b776e8404c557538ea7a434a3eee8719be67af19cda36fa31730e8c4b7fbf86b",
            "99c5ea6d1605dca026e0ce4409da313192fd86501febb9bdeeadff396d817bcc",
            "61ac2c3e724be1404ec15f113d5f36affbcb234d768eb8954efd4d7c6d6bc749",
            "6ec4941f7fa705796ad1c1e352383d130ca44f615c416241995bd24f40a77caa",
            "90f10ecc5f53cc886f447c426a19f31faa753cfc7e991c6a1fe2e143a050d9a8",
            "faf98c74fbe9df95ba08414514ee92890f27d0471ae2b41ec3afb174e5a0611d",
            "7854a49740827f3cfddc34d4ffae20095ff6a52461bf93c1fa351d4da2acddb4",
        ),
    },
    "EVIDENCE.tsv": {
        "prior_sha256": "8981e3ef5349dc3e2990cc8d475fba70eb45fa150f6fdd4ffb7b0f697a32ff9d",
        "remove": ("bcd371f77365535676b89aa5c0c7a546b27dd1f6481e4bfc580914f6f7936732",),
    },
    "HISTORY.tsv": {
        "prior_sha256": "dd0f10a0355820cecc633ba6bfce25ef1bc1d8da9b1a6b5df64093b010e372ff",
        "remove": ("88906bab82b9599477b6501fd6aee92845d5840188b82dde7b7108e1b8edf611",),
    },
    "GATES.tsv": {
        "prior_sha256": "f1f7fb10abf68f248c47933bd220209dc13f7c45ec60c0d44d26a92ee0e1a333",
        "remove": (),
    },
    "FRONTIER_PROGRAMS.tsv": {
        "prior_sha256": "95db755bb7b2f49e2642123649767a7036fd69099db5d2148ef43fac655b97e2",
        "remove": (),
    },
    "CORE_SELECTION.tsv": {
        "prior_sha256": "eee121dd437d06fc2b0fda5377ea6c2e6e01b220e5f1bfb9aa09727885d03d4e",
        "remove": (),
    },
}
V82_DEFINITION = "DEF-K1-LINEAR-METRIC"
V82_CLAIM = "K1-LINEAR-METRIC-COMPLETION"
V82_SCOPE_SHA256 = "fccb3c0857cb84865abcc9dfd84199d25dc905c361a541bf664104ebe99697f1"
V82_CANON_BYTES = 11800
V82_CANON_SHA256 = "374f23a670a5a6df3d8c4ebc3c7dc36339a13434408954e6671e232305b72f45"


# Frozen from public v80 activation 4577448dba85c492b27773a64e5fd557abc02b30.
# Remove only these exact new v81 lines, then verify every restored v80 byte.
# This outermost reconstruction feeds the unchanged v80 and v79 patches below.
V81_LEDGER_PATCH = {'REGISTRY.tsv': {'prior_sha256': '3ccc7a32b115c9433874497126fd975fe3bca33406ba735456ae60c5e5f2300a',
                  'remove': ('6a2d0243d5bfb58f741be64f25b8868a76411f752889ba3facbb1b90202590e6',
                             'dd5bde630c1428dea5c754f55cfbcf0328dc896aaac076d7e21630d143c9f7a7',
                             '310f4671cca9680b4bba5ea878750b0804cb9c43152f22740650bb3957b132b7',
                             'cfcbc6bebf8789ecdc5ac17227338edb449ef825356317eb4eb3ad782e9d6337',
                             'db8cf9a9b30133fbcab74f9347b923bfefb41d7b530ce870fb452466089f771f',
                             'd62838f75a4a2e4d46ff9286eb543354dfaa1973f88f9474202ffa0f2f3dd3f5',
                             '9e15d35b7febeb70d5143ef1ac3ca8b7c5c7bb2cd849f8aceff54095bfb9583a',
                             '1bb68b57fcd1b34bf1d023e2bbb9172aa4d203a3b0604d10a69c47ad7661e5a9')},
 'NORMATIVE.tsv': {'prior_sha256': '588f49ef42a2ae5bc79ea406bc0d545f67487d4c2360a38d3860d160d27d5520',
                   'remove': ('03296814759c641185477b60f387f8dadc9bca0747a433a25fc454ae73f37cd6',
                              'c5051bf6032004ff97a98e5f307f3c3eb3e65aa764600dfe8739c90a408c000b',
                              'ba55f633e019c39113ccd93b4793b63069215015ac892343c9897dbff0a436fe',
                              '643fc2a59274672127390a4f1482bb1594fb1f40d52b051fa2a93fd91651f308',
                              '35fd7a058179e6f3de4a01df34f9fddad4309a93e3a572fa797d4628b36af551',
                              '98257fcacb8136a169d615de91d4351e8dd06e8eb09e5fb165fafefcff4de600',
                              '3f79cfc35a873744f1ff30e8780d21ba87884be6bebe5901247d13f1f36ce391',
                              'e3c75143aeb60c40fd92010114188740f5521eec551ebef14e834d65688b0aa0')},
 'DEPENDENCIES.tsv': {'prior_sha256': 'ded15d0852ca9c3da2c6eabcc1ca24059e3599663f1b2d864ddff766d4621228',
                      'remove': ('eeaa5c04dbff7e2b7752bee5f9bc41709a535f3d1d321713bbf79b502cb46c64',
                                 'f80a80dabdc14ee0f903dd17e8b745618bc83854ee334c8888c3367508a0f4ed',
                                 '9f66bc671c393c7e9876d557e45780d6fabd6f683a61958efdd927995b886bb0',
                                 'd9b580d2e2a56b106a38775351961e61b8b3f253ab78fe129aae4368dfc7c61b',
                                 '46b9dfbd46f2c18405e57c195a49d41ca28f734b8aef7122a204680a9d16ec44',
                                 '39beeb168ad1ddc6c62e83c40593a5a702b1c8ab1f594141ee5b3ef4838ffcd7',
                                 '2c0876237518c194959e3fca139f73e247835c8f9bfcfe91c413f865c1a641b1',
                                 '7bad33667ac4944779ed54acf73b148386e6b58ce3b56eb1405ef68a1571a72d',
                                 'edb2293ec92c5b9731749eb337e4dec48e25b4da09850ff625c3855ee1439d86',
                                 'fbf8e4b64849b20ca8a1a9f320347595924aa689c57243f94319a63bd532e3f6',
                                 'f0b0cbf8068684d348b6f2e9c2e1e5de1ff16e141a36c17e0cbeb81ed30d3d98',
                                 'f1064d2b32adcac064c7ded79fadd6a361b4b5c0e702078736d3108941ef2793',
                                 '1513311dc355ff97bdbf67109a0db4c330a500200bbc1a465893b517fe31b9af',
                                 '02c5b99979df30635e817542eb2f99602913145641a152367283a847eac20427',
                                 'b1a6120da62a46eeb7e4649c20d76a958b190ca46d54478a903901f387cae82d',
                                 '3205161165af13149445e93ddf62f1581e4b70202af9b0d46d42e60c9278089c',
                                 '2fe600873d605b1e80811edc07ee83a310f511029ea8c41d3434cacdd7f3c34e',
                                 'e31e1858e1e097d27440a98947f7496c503f34586fd5ec7a2d1457f3fa4e18a9',
                                 '724207204bde022de1308de18ae99ad306eec035e5da4dc747276759a4de98fe',
                                 '61d97e5b0658dee9fede84531eb4aa983864c6b14b7df2072f6d72c9c95a0957',
                                 '12cf2310e4294d20f45092fd0b7eda0d902a8aa46a40498493ce52e65e6d4bde',
                                 'f1ff5c72aa6a6f11cac87826ffe2b8fc73a015fc969ee2b937aae5191b2eb5e1',
                                 'dd8c7499043f5889a8d9da2757dbedd1f82ef62681ae7e5c5fe9ac9498fed395',
                                 '1631c1543da0daef71b05356a765f8bbaf0f0d04dcb092dff8594fc1ffc80410',
                                 'df1581a84e461e106ce8f0842f82efdc827872eb5cfa2338b0ed277fff379c98',
                                 'dde5f0ae921cfac71495292262e5dd0d2ff4b155bb49f3c30de01ed989250fb8',
                                 'bf0ae5bcdae67df9878846e6b04b83a25f55abf0cff5a44ce5f3828da6cbf9dd',
                                 'efa86964dcfd542dd0bdcb7c9b8451dc2c4fd67a17ca45ae5fa0d930198023a6',
                                 '426dd0f2b7b40a657e418e22795cc1f8c8e0a16eff21576f950147d640ecb2b1')},
 'EVIDENCE.tsv': {'prior_sha256': '8aad6feefac1694b5424a257c3ff438ff77973bc77849a423e5ed636da05eeb2',
                  'remove': ('37c156052427d5e219d45c5aa8cdf4905c5c36c4fa4d9ae698b5cba1ea5e5e80',
                             '0d9cc3629325c06b7ed524941a22c6fb742af6602a35d6a8e963b2bc7c3123fe',
                             '7b9f7821a6e4c1547de20ed21aafb63fe54cb09860a915d2f0a0613c855cd648',
                             'ed74e42c785f9165a3b5562bff8c029c6b0fc6adb174f873d75998c0c226acc0',
                             'b72fff00d73f0c96b6aaa30e9fa94bf8b08a175ad7ebff5ed92d604370564d37',
                             '91acf13c325db68d0fa4c7716e89728c18a394c9dfd193ed551ebf17667fb8bd',
                             '95c977bbde3d6b289f63d64bee3a084b8a4184ce84c47249e52f58b26a359e4f',
                             '00bfc76cc4c06b49d9bc5ba6e65c6a9473beb090c3c416a087c9f7a386ea2ab8')},
 'HISTORY.tsv': {'prior_sha256': '99f899ff2d23f11ba99ecf3db259b24b80f12e5caa67bbd240aef4c651573ffd',
                 'remove': ('d7296f932bc9782cc43c48f6e75876a608132ab0701d89531d9c0ad415bab7a2',
                            '8a4f85d06c1d75ca300f1df2b571cbf528ccaa461b19180e6d142aa2bec76d30',
                            'f82eecbaa15361eaa61710703f6f2b761ec0fd62870638644797c37d6530a937',
                            '44370370ea7c2999e7550956ad914c2022afb9ddb114d489130628ae6de37294',
                            'a8c2444fa3e4fe66605bc6b7d86e67b80985afcd45e096193bf75f0d8bebb9ce',
                            'd8f2d88f61e49a84c79acbb1f7bff1b60319ee19df8c2083f8b7a4c13c921d2f',
                            '471b0db481f53926ef93d65281dd884f1f18256c11313ac381b4a52d6d800b90',
                            'fc1248e0133f7352d5c91bad9f7d51f3f27dd42b96f6672e75c5ce202583228a')},
 'GATES.tsv': {'prior_sha256': 'f1f7fb10abf68f248c47933bd220209dc13f7c45ec60c0d44d26a92ee0e1a333',
               'remove': ()},
 'FRONTIER_PROGRAMS.tsv': {'prior_sha256': '95db755bb7b2f49e2642123649767a7036fd69099db5d2148ef43fac655b97e2',
                           'remove': ()},
 'CORE_SELECTION.tsv': {'prior_sha256': 'eee121dd437d06fc2b0fda5377ea6c2e6e01b220e5f1bfb9aa09727885d03d4e',
                        'remove': ()}}

# Frozen from public v79 parent a51df34fe1f1f433062faeb18f5e03fd0a8082b2.
# Remove only these exact new v80 lines, then verify every restored v79 byte.
# This outer reconstruction feeds the unchanged historical v79 patch below.
V80_LEDGER_PATCH = {'REGISTRY.tsv': {'prior_sha256': '97df96660bd4502149e94aecc7d99b5d10d20834caaf11e1deec6068f800e23d',
                  'remove': ('e581493eabe1fdfb95bf0fed207930a926f15ffb41ebfd3bb1c8b113adb40866',
                             'a2b1416e67e9d9068bb9dd2fed64501cd4ef7f76ebe1f033e673fd4a1feeb281',
                             '5f2665447865a37ef7413ef0908bd7b7dd595c57233a8df0d1cdeff4e56e7779',
                             '224aa164b9eacd94aaddff328af998a24ec64abb3d4fcf5c3b8729fecc58b731',
                             '12f77c34b20d4f5df9d54876445cdeea8add061c1c97195b841944c9e3157319')},
 'NORMATIVE.tsv': {'prior_sha256': '8c9e096e4475f087d133c2bcb90a5de9ca7fa7e0d3caad54fe05baddffad7e37',
                   'remove': ('b02eacd455ba0715dbaadbce2caf8ad348329c02b919af20e500d71953da44f0',
                              'fecd1c8d16d9feb6763b8db27914cb6cc5ac0a6e0d8670ee428ca0cc825f3c52',
                              'ea40943c980076493b7bdc5bc02a8832a25b11a2655078c5de4b78493f4e80be',
                              '1a22b9eb81238cf88beccfc83419cb28423544c396982fcb24b32968ab8370ed',
                              'f2c3c89ac38cd17a5062454d39f4fc98fb45ea7ba0ce02d44349bc82f5b2ea8f')},
 'DEPENDENCIES.tsv': {'prior_sha256': 'edec64ae31f78eaa8fcbc1908d0e2b1bbf322ade5c3204537950b007373ada4a',
                      'remove': ('1b479bf69300de6622ba5300af491291eed9ef7cdfb4cc343ec4398304eec2ab',
                                 'ea028000987e8b184a4a9564f7be0182f51d5ee4ceabea488cd1f8ab06e83d91',
                                 'e64872f23a0ecdb9f367df4de706a99d2c25237fc8992f298ecc7a020190ce1b',
                                 '9f694374e926e92960dac2db4f3aef80209004937101514d2be8b5dc8f18d1e9',
                                 'b4fe4130f4d96a4f0982c45847d833ce14b3e9ed96c4829e21141e18c6c0e1c6',
                                 '4ee1ec7540e7c94a2ff29334c53491af10ad04515706d010d9c470670dde47c7',
                                 'a375781aa68903eb7055b4db6a28e5bcbfd6617f702c856ee636173193d3bf7e',
                                 '07dabeb78b4af65d003d62a129493bdbf759c9f14216a152fdf71c474babc7c7',
                                 'fbb50a0fdde33aef730ed7cb6cf2b388b9e35a5a1ca8d4bfc5c82057769ee909',
                                 '001b7425a22e73e2b2db9c288359d0c8e17a3afed2a00f763618558e3825edcb',
                                 'cc0c9a2450e3f583b1372098cc4351e7fc7f58b10bbac98c1ab7c81429d30e6f',
                                 '0ef8c82c60030253a2a2e93db7359b8a09849f9492828ba36092b2ba0c841399',
                                 'c6a85e2ba37b4b587d92eeedfbb6fd807baeeb01c8bb689cc75cbbfbc391090b')},
 'EVIDENCE.tsv': {'prior_sha256': 'db34b27c5317130f8698ff3b980d6e5575f02e78cbfb11b36cc870405b93682c',
                  'remove': ('008444b38c2e1e11cc397e9ba7af07133fb9077d4180ec8bd2d7ccf8b84af3c7',
                             '7f1f03a97935c703ce6a0c9c5e11e9255f04573e46dd59ec5b8f4029a29c0f21',
                             '4d273df907444fd3d795e48077c09d3e7b997ce2795faee84a386a87492f2a76',
                             '8b84b4e4ab3a6334191a0a111202bd82985ece5655b56067b21b392a20795bf3',
                             'a02d00cb3912cef3b278a037136698284a23460ef8e37894e6dbed820396640a')},
 'HISTORY.tsv': {'prior_sha256': 'ef5b47d2f789e517d6302d679de6ff175d5b3162d5441ec153741f078906bd03',
                 'remove': ('dd8bbb3f3d9b3fe2bbacfcd918deea83ff5544703ac25c45873892026a5c2903',
                            'dac9d93ff566214b25418717b41f6c69e55a0356155595250c0a730e798aaa27',
                            '189e37aeaca0bcdb864b5a9491e79cd726f0510dcf2e6455069daffc78e2226c',
                            'f85092da5fadd9f65a32d1228511eea58e942ab555cdeb5776d05a900a3cec7c',
                            '8f69dc4008a1af96662e506df8e3a0ef8f11b094137b92ceebadf3529139097a')},
 'GATES.tsv': {'prior_sha256': 'f1f7fb10abf68f248c47933bd220209dc13f7c45ec60c0d44d26a92ee0e1a333',
               'remove': ()},
 'FRONTIER_PROGRAMS.tsv': {'prior_sha256': '95db755bb7b2f49e2642123649767a7036fd69099db5d2148ef43fac655b97e2',
                           'remove': ()},
 'CORE_SELECTION.tsv': {'prior_sha256': 'eee121dd437d06fc2b0fda5377ea6c2e6e01b220e5f1bfb9aa09727885d03d4e',
                        'remove': ()}}
V80_ROWS = {'U-NATIVE-COMMON-READY-SOURCE-RETENTION': ('L1', 'NATIVE-PROOF.md'),
 'QDD-INCIDENCE-FIRST-HIT-CLASSIFICATION': ('L1', 'OCCURRENCE-PROOF.md'),
 'QDD-MIXED-CHANNEL-ATTENUATION-RIGIDITY': ('L4', 'MIXED-PROOF.md')}
V80_PROOF_HASHES = {'NATIVE-PROOF.md': '97c592f2b00ca2e03b8c0fc74abd658c4a804d6b6f20bc7722af881b9a76a295',
 'OCCURRENCE-PROOF.md': '4fa925dbe8de9841c787033567f07f00782be2affe002bdc92d75edbe878633c',
 'MIXED-PROOF.md': '93e08d44c30e670257779ce57c102d719d6449a0e861554c2f53d1efcf1e3a8d',
 'PREREG.md': '61b1fb07bb7508d84ba4b8211ef64b1a9b7875272dbe87d75a45f75143dacea8'}
V80_PHYSICAL_ROW_HASHES = {'QDD-INSTRUMENT-APPARATUS': '06288f428275ed4dd79e399c3ea0b8f298e838ba32d4ab5d427c1cbed3133d21',
 'QDD-TERMINAL-EVENT-SEMANTICS': '192a82f813a7412cc36e88c23a7d125e71fb61df2545b5e36c43a63db96cd384',
 'QDD-INSTRUMENT-CLASS-COMPLETENESS': '9fb047888d6c1df4b2045ab3170efa87475e21e9440d7b161277f205f3b8f40a'}
V80_PROBE = "probes/P-QDD-V80-CLOSURE-BOUNDARIES-1"
V80_BUNDLE_SHA256 = "11a94b96b9879450f216d8079adecf828687fd51f587df4e71d98a6dde81d505"
# The two later v80 reading-boundary theorems. Their normative evidence is the
# self-contained inline Canon proof, keyed by the exact registry scope hash.
V80_R3_ROWS = {
    'A4-RATIONAL-FRAME-WEIGHT-NONUNIQUENESS':
        ('L4', '230c7563ab84a21fec0bc0b51584463dc52251094709c206cb0c9472ca7814b6'),
    'QDD-SIMPLEX-PAIR-INCIDENCE':
        ('L4', 'd39e676eaf7ec15b9f1e36ba0afa561d0674c4e4650df79ec998933b8ab6d8f0'),
}
V80_R3_SECTION = "2. Time, space, and the decoder"
# The eight v81 decoder-boundary theorems, each on its own completed public
# probe bundle, keyed by probe directory and frozen bundle manifest hash.
V81_ROWS = {
    'BINARY-RECORD-VALUATION-NONSELECTION':
        ('probes/P-BINARY-RECORD-QUADRATIC-SELECTION-1',
         '6bf433d1594b1ed19441033790f1ef0df7a5da17f68fd575c0d1a5521b9e11c9'),
    'RECORD-OCCURRENCE-SELECTION-CRITERIA':
        ('probes/P-RECORD-OCCURRENCE-SYMMETRY-1',
         '65ce6a38beddbd27cd809b4ae505cf87dcf05bd04424a76647d9f74097f9dd46'),
    'RELATIONAL-GROWTH-SATURATION-BOUNDARY':
        ('probes/P-RELATIONAL-GROWTH-SATURATION-1',
         '0d1161f53fcfadedbc96ce104dd435de97f920ebe1e01ecb1de35528ebe2ec65'),
    'U-FINITE-READER-INDEPENDENCE-OBSTRUCTION':
        ('probes/P-U-FINITE-READER-INDEPENDENCE-1',
         'f92442e562b04743bcd1c77eae4c24143c72d9a172bf79207200eac502abf5b0'),
    'OCCURRENCE-ADDRESS-AND-LOG-EQUALITY':
        ('probes/P-SNAP-OCCURRENCE-IDENTITY-1',
         '7218d3848c5b089316eaa8a50ac919f12b9cf82fbf1c5f431b70f065afc90f7a'),
    'RECORD-LOADER-RETENTION-CLASS':
        ('probes/P-SNAP-INTERACTION-READBACK-1',
         'd67d6cb185640e24430fa69dcbca22837b5230b00e762d38ba349cbeb4a47a9e'),
    'REGISTRATION-PAIR-RECOVERY-INVERSE':
        ('probes/P-REGISTRATION-PAIR-RECOVERY-1',
         '0277e3c0e8d6356836a3ce741b2ff02aa62cb2e088e4307e547ad738ab056725'),
    'TRC1-CALIBRATION-IDENTIFIABILITY':
        ('probes/P-TRC1-END-TO-END-IDENTIFIABILITY-1',
         '28dde06306d6799f33ff0f8aabcdaad753f66866a6f8c2e65e9576aa02b9520e'),
}
V81_SECTION = "2. Time, space, and the decoder"
V81_OWNERS = (
    "QDD-INSTRUMENT-APPARATUS", "QDD-TERMINAL-EVENT-SEMANTICS",
    "TRACEKERNEL-CURVATURE-FORCING",
)


# Frozen from public base 07b123a4082f174c37bf09c9aa8815bd2c0e1660.
# Prior rows and hashes are never inferred from filtered current data.
# Each patch removes only SHA-256-pinned new/replacement rows and restores the
# literal old rows at their original line positions. The complete reconstructed
# byte stream must match its immutable base hash before a historical check uses it.
V79_LEDGER_PATCH = {'REGISTRY.tsv': {'prior_sha256': 'cb8ebc384e6159551a1554472c944eb28a2ae943b7fa915b94443e6fa0808aef',
                  'remove': ('08c0e1b5538c8174600ed423b101badf2d63869a94413496b02a6d3f98964d1b',
                             '11fa7bbdc751a945e0606ecd6e052deb6c765b5aee50118ef64503e16acb677e',
                             '1716108b26a3253cf7052930d90592d0a46d98bcdaa7d17e149dbeeb54b76e6e',
                             '181477c4f05668561b5c0d3137255dab4c4248dc6b9be6630b6387fa77656813',
                             '30480bd591cb8c18371471651ad5d4afc4836a1771f919025314e2a1e42ec119',
                             '3ce6fbcd6616f3cc0fceed6cb1b4fe6e2b1b5b6c456a09b2e1c7ff0c48d09f1f',
                             '482bc8a1e2b5657750cfb7fcd5b777b02f9c3abd937f416c4c6d82a5711bb56c',
                             '7250248196c76efbc04ed67ea933944427305cf9ea7ab521b9a93482fe228694',
                             '8d8a9f8cc0285cb0bd51e8249d849581bf15b497425d4d88ec1848abef97878b',
                             'b6fd7c11a0400e72bfedd047e02f75c09e024a4685f5c9597ad6e331c91b3a84'),
                  'restore': ((225,
                               'CURVATURE-OPERATOR-CANONICAL\tO\twhether the public architecture '
                               'determines exactly one equivalence class of spatial-curvature operator '
                               'after its carrier, measure, projection group, and ambient versus '
                               'intrinsic commutator choice are fixed publicly\t2. Time, space, and the '
                               'decoder\tinline\tcloses UNIQUE if exactly one class survives, NONUNIQUE '
                               'if at least two survive, EMPTY if none survives, and STOP if the '
                               'classification is incomplete or inexact\n'),
                              (282,
                               'TIME-CUT-READING\tD\tthe dictionary composition of registered public '
                               'rows: the counter n is cut by theta_n = s_2(n) mod 2 into the selection '
                               'law i = (z5 + 2 theta_n) mod 5, and the ramified lift realizes the cut '
                               'as the sign quotient of the four-phase J-channel (RAMIFIED-TM-LIFT); '
                               'the matter channel reads the named isolated pair (theta_(n-1), theta_n) '
                               '= (0, 0), density 1/6 (GYRON-DENSITY), each knot bracketed 1 00 1 by '
                               'cube-freeness of the drive; the spatial channel does not sit on the '
                               'noncommutativity of the fired steps, which is exactly the fiber '
                               'translation plane (FIRED-COMMUTATOR-NOGO), but on the silent pair a, c, '
                               'never fired on the sheet, whose commutator reading is carried by '
                               'CURVATURE-HISTORICAL-TRACE and KERNEL-MACRO-READING with the canonical '
                               'operator open (CURVATURE-OPERATOR-CANONICAL); the dimensionless proper '
                               'time is the terminal reading delta tau hat = 2 pi/5 per tick '
                               '(METRO-TICK); no forcing, uniqueness, or completeness of this '
                               'dictionary is claimed, and no component row is strengthened by the '
                               'composition\t2. Time, space, and the decoder\tinline\tfires if any '
                               'cited component row falls or is re-scoped below the use made of it '
                               'here, or if any clause misstates the scope of the row it names\n'))},
 'NORMATIVE.tsv': {'prior_sha256': 'fe93c49aefdefe6ec767d70ee450634ab9337d7e815c84d62161614881f43c0b',
                   'remove': ('09fbebc7fc9fc0301116738b92804171390056d36e4b4f86665f7371e6d58a86',
                              '31784b596a397b8a360b8a4d90e445a7da0fc134de76776926952887bf08c348',
                              '35ef7ad72854a6183b3968581a81784304791b6e2222ac639be244b806f06eea',
                              '422063a262a4f5c01243822512388ab139dfba03d8bb8b2d417b81e9a706d439',
                              '4dac061e5c2c2a8f73925c5459fd1b4c91d02b9a61c7fb9a28d1045107c6c592',
                              '5758066044bc5ade045cf792d1968b1fd99a34d8eb61ae381563e8d4f6cc8cab',
                              '68662b7451728234d974ee89265e37c192d3cd874e5bccc0e167a5301be90e5b',
                              '6f9e21045b6d80ccc9485f0a868c29dda0d58f23642fcc3abcd24d871a7de181',
                              '9b9fd5ddd05b0eeaa40370ab13981b08ffc1a52d2fcdf12789c6dd732f76c4f7',
                              'a0bf7fd0e4888c58fad7666c72818a588c6676b82c408d1ed994ba9b8c725226',
                              'b3002857a4811f819967be8aed94b799e1d03d633b48fb1aa75e0cbdfb387ead',
                              'ba9300cff8f6015e4006dabadc8cc45dabcb98478bfd27e9ceb1afae7604c902'),
                   'restore': ((224,
                                'CURVATURE-OPERATOR-CANONICAL\tOBLIGATION\t'
                                'CURVATURE-OPERATOR-CANONICAL\tO\tL2\tGATE-L1-L2-CURVATURE-CANONICAL\t'
                                'canon/CANON.md::2. Time, space, and the decoder\n'),)},
 'DEPENDENCIES.tsv': {'prior_sha256': '0c953243f9c48bcefd5f5b4d29639066cdd6c513fb6ccff17b5cba5479846ab8',
                      'remove': ('00e2c1b269df092cb7ef27f2f1f7d95e7df85394875b455bb1b7e7be1c65f784',
                                 '0d582a041a95800033a369226b18319384782eca54238858a5b879b4c2c9efb7',
                                 '211857c0f4e037641b09fed54676eea5db79751541edb6a35635d74737b047f4',
                                 '214adbff2d75f3a62264167bea5bb11f6caff896990a3adb67bce2ddd458a42f',
                                 '3d2bfdbc0a4db542d6ec9ef5d0e12b37a37830e3fd8c4ae1108dd941c7e3b80d',
                                 '3dad08565a207053c4c8b3748de0a3ce49a507ad4cc6127404b0ec945ba23c30',
                                 '4866423cea076e1633d5f1f796160daec7be6064db47d1080d759235c50c5a9a',
                                 '4a80d54e28e716e63a3dd1a3344bc3af7cda9884027310595b311487b9c8704d',
                                 '573ae11915980e486a7cd7c2878f2242b0318219a0ee326e2b5a55ee00b318ab',
                                 '5b0383d1b4429c653e8031292538da0bcabf7ca38db02b10f97da595bc047fe6',
                                 '67e7fe11547c7f8fcfedb11058cbb972265cb59db823c25942911d504ae893ca',
                                 '6cab77bef598d21baf67c165eee3b0200995dbe7cc9cd6fea6f164a19f79d0f2',
                                 '6ec4e46332e40fa07f5bdcdd374e507a1743b701c4dc7928dbfcb151a12ce76f',
                                 '71fdb34b519984a274d511b4256882ab597bf7938cecaed098adcbc8553a3a8c',
                                 '730ab53848dcc691c83e454b773c1f5356ba42b56bdf1159617cf91e1578b296',
                                 '7486532de6f135ae5bbf5bd08a5507b74284ecffb8b9e3d11ccce547db257df9',
                                 '75e1f92e72249ce597ea5bc9f1f77a379789797705f9a3c3329be13856bfee64',
                                 '7bf68eafc32967b2e52a9d02a35480b2e0d55c2340a9245e786d69c4b7c86654',
                                 '8932f460a35c96b1e54ae8ff0dce3721c9b74e72a8b499ba82686f10d9742c2f',
                                 '898ac363e30033ca8162df81e8d8e42b4c0006bbed36241897bf1de783a808cc',
                                 '8d8fc04005113acf810bdc7bce5bec5bbae7a5dad2d96d56c0dcfc4e12fe5816',
                                 '8ec6b5a69be8bb673f79f172e1044e7a21a81e3bd62b39a470923d686e704ee6',
                                 '950089c8f4bdcb22b4ee5b44ba2ae14d41811f830e18b9db62d69f9061131518',
                                 '9722f7f8c19e8c0043fc70272624d5866ac6a09b9de98ef062b135e1fdfb277e',
                                 '9e600a921b517ee432614f661045536acfeff68c5c0ea546c7343b12507413e2',
                                 'aac85484d53c24ee47ee178dbe7ce2dc694b4e3a746e873c67e8d1bb2a5e4d66',
                                 'af308bdfe54e0bbf8131b0313a0ea57a169dea61fa89c7f415164a7b203cdc5e',
                                 'b4c21111e36bf45ebb97f3f0fd716a6ee2d7e9c5e02d46d1833849fe8382de77',
                                 'b5f45d00a125ba6913bbdb8e5b0e5614afb5c54abd69a57ba0f3ae99b0efe564',
                                 'c30d22fcaf92848f173363d83ce8403ebec87e33985ff6107246a64b46ca8255',
                                 'c55dc0bb9699cc903fc026b2d27c3207ead7b8ca60704ff3124b1d83ac28648d',
                                 'dcedb272de1cbf5b87c9fb7b569bbafb3bff06bc808721a92d29f1a04aac9f0e',
                                 'eb79bc3780c5546fdddb2cc350e59cc124dc6b245d3740e76ff36b9b98af822a',
                                 'f7b691a62b90ba2054cb088fb67019a1e4b050d529484952d9eb61f6086e9654'),
                      'restore': ((318,
                                   'CURVATURE-OPERATOR-CANONICAL\tDEF-ARCHITECTURE\tREQUIRES\tCanon '
                                   'definition boundary: canonical spatial-curvature selection is '
                                   'conditional on the declared architecture\n'),
                                  (364,
                                   'CURVATURE-OPERATOR-CANONICAL\tCURVATURE-HISTORICAL-GAUSS-SPLIT\t'
                                   'BOUNDED_BY\tthe exact historical equality constrains one declared '
                                   'full-carrier candidate but does not select a canonical operator '
                                   'class\n'),
                                  (440,
                                   'TIME-CUT-READING\tCURVATURE-OPERATOR-CANONICAL\tBOUNDED_BY\tthe '
                                   'canonical curvature operator remains explicitly open and is not '
                                   'selected by this composition\n'),
                                  (636,
                                   'TRACEKERNEL-CURVATURE-FORCING\tCURVATURE-OPERATOR-CANONICAL\t'
                                   'REQUIRES\tthe forcing classification cannot advance until the '
                                   'upstream obligation publishes the carrier and complete admissible '
                                   'L2 operator or commutator class; UNIQUE versus NONUNIQUE does not '
                                   'itself decide the common Hodge-home property\n'))},
 'EVIDENCE.tsv': {'prior_sha256': 'd3705a2a51c904e2c0f7cfd1aa87e07bf62073550ce48ccb9aab6e27e763e93f',
                  'remove': ('35a07e370d07d36f615ab187392cfd0fb98ef945aee7a0e37f586ff3809876de',
                             '46f10be5d7e1c79eff371ff365cf68bbb206a5b1640795f57c07907001ddc05b',
                             '5648ab9eff0b83a4a52487c5e3d43b1784d6e0ad0a6b44c47db4947caad2ec89',
                             '8d904838594e1756ac235de7bc72b13dd45c3081cf9cc66ebfd949472d577c9a',
                             'a85f9e1eaf26e5643a2c5f3470fe4f5848485b9849108b0474da2e31edf6de03',
                             'd49ac9e4335950a4460d9b6275d5bc542987187558dcde37e9a18186a9f268fd',
                             'd7342964254e066db6268d9af89ca500595659a01a1fac2796cbfff213f7ffd1',
                             'def693f319b1238ca65961625fb41db8b9274b7b43e7db6dfc33fee3739ddaed',
                             'f429679060fec4500e55c5d16c97837b0d1cdd11ce876c1895c0119043209d9e',
                             'fa6121b3434f278df50f5d80a492c1f04ed1539ab6e462e434776271bb4c1f58'),
                  'restore': ((216,
                               'CURVATURE-OPERATOR-CANONICAL\tEV-CURVATURE-OPERATOR-CANONICAL\t'
                               'INLINE_CANON\tinline\t'
                               '253142e1d51b0d18d8dcb866ad3de64579ee1782e32983f2b4d0fe0c2d3bbfa5\t'
                               'registry-scope-sha256-v1\tnone\n'),
                              (273,
                               'TIME-CUT-READING\tEV-TIME-CUT-READING\tINLINE_CANON\tinline\t'
                               '4f1455918565d3a87602223bb72d189913da408963d0f25012468c857bc584c9\t'
                               'registry-scope-sha256-v1\tnone\n'))},
 'HISTORY.tsv': {'prior_sha256': 'a2517350a13a5617ae57a4c0b50bd381dbe8ce332435dd9fd50f5b5e2432d573',
                 'remove': ('2dc6071647d988e4552a48957d188b2dce574c472c4fba41cff8eaae316d781c',
                            '3adce02895643fbbf917c4f0f4fb8e0aacb48fef7f3649cb2d05bf20df590f6b',
                            '728691534a357947a149ae236fdd6c5b18ba8b3d7bf961f5e5aa4a98cd10aae3',
                            '8e7712301ede7be79134aac79e4c22e890c4863e0bba61dc2c9b086fa8374831',
                            '9b070870cbb297b1901186a1565313c3ecf2571409f6a82bec056d293393ef20',
                            'd993b02e301001e2389019e27049d5c5272a564e35982b410e5bab63adffb196',
                            'e6b246469efec396c2c58746d8a8fde7b22fa75611815fc259aea7c11877e8f3',
                            'e6be34e6a48390c4219b10ce7e5c8bb8983ab920281236622b0e5a85d5964cfb',
                            'efde8eea7cb1315265718cbcf508a9f2299332274ae0acb09190781bcdef5941',
                            'fb9efe08ea494d15eee9d2d5e59ce02c53e6847aca890fb5ad5fd206334d60e7'),
                 'restore': ()},
 'GATES.tsv': {'prior_sha256': '4f38b0d8c95a43d37190e57f416e865e6c1adf70378c0f9d4625c63bf8842ca3',
               'remove': ('17eefc1dd4d98d9fdc61c5dce355252af94dcb8356784cf885f4f80b1d889d91',
                          'b06fcdd3bff4bcfff6a6e092dd40c1edec65503156d7f3a36b261dae169cab05'),
               'restore': ((2,
                            'GATE-L1-L2-CURVATURE-CANONICAL\tCURVATURE-OPERATOR-CANONICAL\tL1\tL2\t'
                            'OPEN_LIFT\tcloses UNIQUE if exactly one equivalence class survives the '
                            'frozen public classification, NONUNIQUE if at least two survive, EMPTY if '
                            'none survives, and STOP if completeness or exactness fails\n'),)},
 'FRONTIER_PROGRAMS.tsv': {'prior_sha256': 'd7f7205acd461ff05ec7b31c45cc8e3b0ca3d4960432eb6053556fc5357da0d8',
                           'remove': (),
                           'restore': ((4,
                                        'CURVATURE-OPERATOR-CANONICAL\tDECODER_CORE\tROOT\tSTOP\t'
                                        'FORMAL\n'),)},
 'CORE_SELECTION.tsv': {'prior_sha256': 'eee121dd437d06fc2b0fda5377ea6c2e6e01b220e5f1bfb9aa09727885d03d4e',
                        'remove': (),
                        'restore': ()}}
V79_NATIVE_ROWS = {
    "U-NATIVE-CHART-AND-QDD-READBACK": ("T", "L1"),
    "U-NATIVE-INVARIANT-AND-NOWRITE": ("T", "L1"),
    "U-FINITE-HISTORY-CLOCK-PHASE": ("T", "L1"),
    "U-NATIVE-READER-STREAM-SPECTRA": ("T", "L5"),
    "U-NATIVE-APPARATUS-HISTORY-FACTOR": ("T", "L1"),
    "QDD-CONDITIONAL-INCIDENCE-AND-SYMBOLIC-RECORD": ("T", "L1"),
    "QDD-CONDITIONAL-INCIDENCE-FINITE-AUDIT": ("C", "L1"),
}


def v82_previous_bytes(path):
    """Recover byte-identical v81 tables using only the frozen v82 additions."""
    patch = V82_LEDGER_PATCH[path.name]
    removed = {digest: 0 for digest in patch["remove"]}
    kept = []
    for position, line in enumerate(path.read_bytes().splitlines(keepends=True)):
        digest = hashlib.sha256(line).hexdigest()
        if position and digest in removed:
            removed[digest] += 1
        else:
            kept.append(line)
    if any(count != 1 for count in removed.values()):
        return None
    previous = b"".join(kept)
    if hashlib.sha256(previous).hexdigest() != patch["prior_sha256"]:
        return None
    return previous


def v81_previous_bytes(path):
    """Recover byte-identical v80 tables using only the frozen v81 additions."""
    patch = V81_LEDGER_PATCH[path.name]
    current_v81 = v82_previous_bytes(path)
    if current_v81 is None:
        return None
    removed = {digest: 0 for digest in patch["remove"]}
    kept = []
    for position, line in enumerate(current_v81.splitlines(keepends=True)):
        digest = hashlib.sha256(line).hexdigest()
        if position and digest in removed:
            removed[digest] += 1
        else:
            kept.append(line)
    if any(count != 1 for count in removed.values()):
        return None
    previous = b"".join(kept)
    if hashlib.sha256(previous).hexdigest() != patch["prior_sha256"]:
        return None
    return previous


def v80_previous_bytes(path):
    """Recover byte-identical v79 tables using only the frozen v80 additions."""
    patch = V80_LEDGER_PATCH[path.name]
    current_v80 = v81_previous_bytes(path)
    if current_v80 is None:
        return None
    removed = {digest: 0 for digest in patch["remove"]}
    kept = []
    for position, line in enumerate(current_v80.splitlines(keepends=True)):
        digest = hashlib.sha256(line).hexdigest()
        if position and digest in removed:
            removed[digest] += 1
        else:
            kept.append(line)
    if any(count != 1 for count in removed.values()):
        return None
    previous = b"".join(kept)
    if hashlib.sha256(previous).hexdigest() != patch["prior_sha256"]:
        return None
    return previous


def v79_previous_bytes(path):
    patch = V79_LEDGER_PATCH[path.name]
    current_v79 = v80_previous_bytes(path)
    if current_v79 is None:
        return None
    lines = current_v79.splitlines(keepends=True)
    removed = {digest: 0 for digest in patch["remove"]}
    kept = []
    for position, line in enumerate(lines):
        digest = hashlib.sha256(line).hexdigest()
        if position and digest in removed:
            removed[digest] += 1
        else:
            kept.append(line)
    if any(count != 1 for count in removed.values()):
        return None
    for position, old_line in patch["restore"]:
        if position > len(kept):
            return None
        kept.insert(position, old_line.encode("utf-8"))
    previous = b"".join(kept)
    if hashlib.sha256(previous).hexdigest() != patch["prior_sha256"]:
        return None
    return previous


def v79_previous_rows(path):
    previous = v79_previous_bytes(path)
    if previous is None:
        return []
    return list(csv.DictReader(io.StringIO(previous.decode("utf-8")), delimiter="\t"))


def v79_historical_tables(excluded_claims, excluded_releases):
    previous = {
        "REGISTRY": v79_previous_rows(REGISTRY),
        "NORMATIVE": v79_previous_rows(NORMATIVE),
        "DEPENDENCIES": v79_previous_rows(DEPENDENCIES),
        "EVIDENCE": v79_previous_rows(EVIDENCE),
        "HISTORY": v79_previous_rows(HISTORY),
        "GATES": v79_previous_rows(GATES),
        "FRONTIER_PROGRAMS": v79_previous_rows(FRONTIER_PROGRAMS),
        "CORE_SELECTION": v79_previous_rows(CORE_SELECTION),
    }
    for name, column in (
        ("REGISTRY", "claim_id"), ("NORMATIVE", "item_id"),
        ("DEPENDENCIES", "item_id"), ("EVIDENCE", "claim_id"),
    ):
        previous[name] = [
            row for row in previous[name] if row[column] not in excluded_claims
        ]
    previous["HISTORY"] = [
        row for row in previous["HISTORY"] if row["release"] not in excluded_releases
    ]
    return previous


def load_table(path):
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def load_rows():
    rows = load_table(REGISTRY)
    normative_rows = load_table(NORMATIVE)
    dependencies = load_table(DEPENDENCIES)
    evidence_rows = load_table(EVIDENCE)
    history_rows = load_table(HISTORY)
    gate_rows = load_table(GATES)
    program_rows = load_table(FRONTIER_PROGRAMS)
    return (
        rows,
        {row["claim_id"]: row for row in rows},
        {row["item_id"]: row for row in normative_rows},
        dependencies,
        {row["claim_id"]: row for row in evidence_rows},
        history_rows,
        {row["gate_id"]: row for row in gate_rows},
        {row["claim_id"]: row for row in program_rows},
    )


def dependency_graph(rows):
    graph = {}
    for row in rows:
        graph.setdefault(row["item_id"], set()).add(row["depends_on"])
    return graph


def reaches(graph, start, target):
    seen = set()
    stack = list(graph.get(start, ()))
    while stack:
        item = stack.pop()
        if item == target:
            return True
        if item in seen:
            continue
        seen.add(item)
        stack.extend(graph.get(item, ()))
    return False


def has_cycle(graph):
    visiting = set()
    visited = set()

    def visit(item):
        if item in visiting:
            return True
        if item in visited:
            return False
        visiting.add(item)
        for dependency in graph.get(item, ()):
            if visit(dependency):
                return True
        visiting.remove(item)
        visited.add(item)
        return False

    return any(visit(item) for item in graph)


def has_status(index, claim_id, status):
    return claim_id in index and index[claim_id]["status"] == status


def scope_lacks(index, claim_id, words):
    scope = index[claim_id]["scope"].lower()
    return all(word.lower() not in scope for word in words)


def scope_contains_all(index, claim_id, phrases):
    scope = index[claim_id]["scope"].lower()
    return all(phrase.lower() in scope for phrase in phrases)


def scope_sha256(index, claim_id):
    return hashlib.sha256(index[claim_id]["scope"].encode("utf-8")).hexdigest()


def registry_row_sha256(index, claim_id):
    row = index[claim_id]
    fields = (
        "claim_id", "status", "scope", "canon_section", "evidence", "falsifier",
    )
    payload = "\t".join(row[field] for field in fields)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def table_row_sha256(row):
    payload = "\t".join(row.values())
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def projected_file_sha256(path, column=None, excluded=()):
    """Hash original TSV bytes after removing only named release rows.

    The frozen selector columns contain unquoted ASCII identifiers. Keep the
    header, every retained row, its order and its exact line ending unchanged.
    """
    previous = v79_previous_bytes(path)
    if previous is None:
        return "INVALID-V79-RECONSTRUCTION"
    lines = previous.splitlines(keepends=True)
    if column is None:
        return hashlib.sha256(b"".join(lines)).hexdigest()
    fields = lines[0].rstrip(b"\r\n").decode("utf-8").split("\t")
    position = fields.index(column)
    excluded_bytes = {value.encode("utf-8") for value in excluded}
    kept = [lines[0]] + [
        line for line in lines[1:]
        if line.rstrip(b"\r\n").split(b"\t")[position] not in excluded_bytes
    ]
    return hashlib.sha256(b"".join(kept)).hexdigest()


INDEPENDENCE_ROWS = (
    "SPLIT-PRIME-RAPIDITY-INDEPENDENCE",
    "REDUCED-SPLIT-GENERATOR-HEIGHT",
    "SPLIT-PRIME-RAPIDITY-QUANTITATIVE-SEPARATION",
    "SPLIT-RAPIDITY-FEJER-GRAM-BOUND",
)


def run():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(newline="\n")

    (
        rows,
        index,
        normative,
        dependencies,
        evidence,
        history,
        gates,
        programs,
    ) = load_rows()
    canon_text = CANON.read_text(encoding="utf-8")
    core_text = CORE.read_text(encoding="utf-8")
    frontier_text = FRONTIER.read_text(encoding="utf-8")
    core_selection_rows = load_table(CORE_SELECTION)
    checks = []

    qdd_predecessor = "QUADRATIC-DECODER-DATA"
    qdd_successor = "ALGEBRAIC-DMATTER"
    qdd_apparatus = "QDD-INSTRUMENT-APPARATUS"
    qdd_current_split = (
        qdd_predecessor not in index
        and qdd_predecessor not in normative
        and qdd_predecessor not in evidence
        and qdd_predecessor not in programs
        and all(
            row["item_id"] != qdd_predecessor
            and row["depends_on"] != qdd_predecessor
            for row in dependencies
        )
        and has_status(index, qdd_successor, "D")
        and normative.get(qdd_successor, {}).get("item_type") == "DICTIONARY"
        and normative.get(qdd_successor, {}).get("status") == "D"
        and normative.get(qdd_successor, {}).get("layer") == "L1"
        and normative.get(qdd_successor, {}).get("gate_ids") == ""
        and evidence.get(qdd_successor, {}).get("evidence_kind") == "INLINE_CANON"
        and evidence.get(qdd_successor, {}).get("location") == "inline"
        and evidence.get(qdd_successor, {}).get("sha256")
        == scope_sha256(index, qdd_successor)
        and evidence.get(qdd_successor, {}).get("hash_mode")
        == "registry-scope-sha256-v1"
        and evidence.get(qdd_successor, {}).get("architecture_requirement") == "none"
        and qdd_successor not in programs
        and all(row["owner_item_id"] != qdd_successor for row in gates.values())
        and has_status(index, qdd_apparatus, "O")
        and normative.get(qdd_apparatus, {}).get("item_type") == "OBLIGATION"
        and normative.get(qdd_apparatus, {}).get("status") == "O"
        and normative.get(qdd_apparatus, {}).get("layer") == "MULTI"
        and normative.get(qdd_apparatus, {}).get("gate_ids") == ""
        and programs.get(qdd_apparatus) == {
            "claim_id": qdd_apparatus,
            "program_id": "DECODER_CORE",
            "queue_role": "FOLLOWUP",
            "work_state": "STOP",
            "work_mode": "FORMAL",
        }
    )

    counts = {}
    for row in rows:
        counts[row["status"]] = counts.get(row["status"], 0) + 1
    two_architecture = sum(
        row["architecture_requirement"] == "two-architecture"
        for row in evidence.values()
    )
    expected_counts = {"T": 275, "D": 45, "C": 39, "F": 18,
                       "O": 28, "H": 2}
    checks.append((
        "COUNTS",
        "registry and companion-ledger counts match Public Canon v82",
        len(rows) == 407
        and counts == expected_counts
        and len(normative) == 457
        and len(dependencies) == 780
        and len(evidence) == 407
        and two_architecture == 316
        and len(history) == 940
        and len(gates) == 15
        and len(programs) == 30
        and len({row["program_id"] for row in programs.values()}) == 8
        and len(core_selection_rows) == 30
        and sum(path.is_dir() for path in REPRODUCE.iterdir()) == 24,
    ))

    checks.append((
        "AXIOM",
        "J and plenum algebra stay T; projection and plenum physics are D",
        all(has_status(index, claim, "T") for claim in
            ("J-PROJECTIONS", "PLENUM-POINT", "J-MODULUS-CHORD",
             "J-RAMIFIED-CHORD"))
        and has_status(index, "AXIOM-PROJECTION-DICTIONARY", "D")
        and scope_lacks(index, "J-PROJECTIONS",
                        ("gravity", "electromagnetism", "force"))
        and scope_lacks(index, "PLENUM-POINT",
                        ("gravity", "space channel", "writes", "reads")),
    ))

    checks.append((
        "PLACES",
        "field and Galois facts stay T; place and CPT physics are D",
        all(has_status(index, claim, "T") for claim in
            ("DEGREES-BY-PRIME", "Z2-PLACES-SPLIT",
             "METAL-TRACE-CASCADE"))
        and has_status(index, "TWO-PLACE-PHYSICS", "D")
        and scope_lacks(index, "DEGREES-BY-PRIME",
                        ("magic", "qubit", "gravity", "born"))
        and scope_lacks(index, "Z2-PLACES-SPLIT", ("cpt", "force", "spin")),
    ))

    kernel = "KERNEL-Z6-SYNCHRONIZATION"
    kernel_path = "probes/P-KERNEL-Z6-SYNCHRONIZATION-1"
    kernel_digest = "7ac0cae9685575c8bd92f1c3f39603e0fc7a148fae5db80746fbcc1e5e4de1b9"
    kernel_dependencies = [
        row for row in dependencies if row["item_id"] == kernel
    ]
    c8 = "C8-BILINEAR-SHADOW"
    c8_path = "probes/P-C8-BILINEAR-SHADOW-2"
    c8_digest = "72728a88f45af777656a39d313b79c8189e2dfa2fa587e08fac5bf02aa6b234d"
    c8_dependencies = {
        (row["depends_on"], row["relation"])
        for row in dependencies if row["item_id"] == c8
    }
    checks.append((
        "CARRY",
        "carry, synchronization, and C8 shadow theorems stay T and physically fenced",
        all(has_status(index, claim, "T") for claim in
            ("RAMIFIED-TM-LIFT", "CARRY-J-CHECKPOINT", "CARRY-PENTAD",
             "SQRT-PHI-DIGIT-LIFT", kernel, c8))
        and scope_contains_all(index, "CARRY-PENTAD",
                               ("selects no prime", "physical reading"))
        and scope_contains_all(index, "RAMIFIED-TM-LIFT",
                               ("no checkpoint factorization",
                                "physical carry/phase reading"))
        and scope_contains_all(index, "CARRY-J-CHECKPOINT",
                               ("full forward carrier", "no restricted carrier",
                                "physical reading"))
        and scope_contains_all(index, "SQRT-PHI-DIGIT-LIFT",
                               ("not constant", "no sign-branch selection",
                                "gravity dynamics"))
        and scope_contains_all(index, c8,
                               ("<tau> = F_5^* union tau F_5^*",
                                "branch invariant",
                                "mixed-parity products are off-axis and branch-dependent",
                                "no branch selection",
                                "broader physical or gauge equivalence",
                                "lift to L2-L6"))
        and scope_contains_all(index, kernel,
                               ("at each fixed known n",
                                "q_n is a sheet label and not the checkpoint coordinate q",
                                "no unknown-time or unindexed checkpoint-fiber",
                                "physical-irreversibility",
                                "no L2-L6 claim is included"))
        and normative[kernel]["item_type"] == "THEOREM"
        and normative[kernel]["status"] == "T"
        and normative[kernel]["layer"] == "L1"
        and normative[kernel]["gate_ids"] == ""
        and len(kernel_dependencies) == 1
        and kernel_dependencies[0]["depends_on"] == "DEF-AUTONOMOUS-STATE"
        and kernel_dependencies[0]["relation"] == "REQUIRES"
        and evidence[kernel]["evidence_kind"] == "PUBLIC_PROBE"
        and evidence[kernel]["location"] == kernel_path
        and evidence[kernel]["sha256"] == kernel_digest
        and evidence[kernel]["hash_mode"] == "bundle-manifest-sha256-v1"
        and evidence[kernel]["architecture_requirement"] == "two-architecture"
        and kernel not in programs
        and normative[c8]["item_type"] == "THEOREM"
        and normative[c8]["status"] == "T"
        and normative[c8]["layer"] == "L1"
        and normative[c8]["gate_ids"] == ""
        and c8_dependencies == {
            ("PENTIT-ROOT-FACTS", "REQUIRES"),
            ("RAMIFIED-TM-LIFT", "REQUIRES"),
            ("SQRT-PHI-DIGIT-LIFT", "REQUIRES"),
        }
        and evidence[c8]["evidence_kind"] == "PUBLIC_PROBE"
        and evidence[c8]["location"] == c8_path
        and evidence[c8]["sha256"] == c8_digest
        and evidence[c8]["hash_mode"] == "bundle-manifest-sha256-v1"
        and evidence[c8]["architecture_requirement"] == "two-architecture"
        and c8 not in programs,
    ))

    drift = "DRIFT-IS-THE-READ"
    coin_selector = "COIN-SELECTION-CONDITIONAL"
    coin_premise = "COIN-MINIMAL-READ"
    coin_derivation = "MINIMAL-READ-DERIVATION"
    retired_observer = "OBSERVER-WRITE-PORT"
    coin_gate = "GATE-L5-L1-MINIMAL-READ"
    boost_path = "probes/P-BOOST-COHERENCE-1"
    boost_digest = (
        "0e2c9daaee5a7c189615f1941894015be2b9e59a71a1183cfc6ed207c9c8d083"
    )
    boost_items = (drift, coin_selector, coin_premise, coin_derivation)
    expected_boost_dependencies = {
        drift: {
            ("BOOST-READING-SPLIT", "REQUIRES"),
            ("BOOST-COUNT-LADDER", "BOUNDED_BY"),
        },
        coin_selector: {
            ("BOOST-READING-SPLIT", "REQUIRES"),
            ("BOOST-COUNT-LADDER", "BOUNDED_BY"),
            (drift, "REQUIRES"),
        },
        coin_premise: {(coin_selector, "REQUIRES")},
        coin_derivation: {
            ("DEF-ARCHITECTURE", "REQUIRES"),
            ("DEF-ACTION-LAYERS", "REQUIRES"),
            (coin_selector, "REQUIRES"),
        },
    }
    actual_boost_dependencies = {
        item: {
            (row["depends_on"], row["relation"])
            for row in dependencies if row["item_id"] == item
        }
        for item in boost_items
    }
    checks.append((
        "BOOST",
        "exact drift and selector ranking stay T; retired observer no longer blocks derivation O",
        has_status(index, drift, "T")
        and has_status(index, coin_selector, "T")
        and has_status(index, coin_premise, "D")
        and has_status(index, coin_derivation, "O")
        and normative.get(drift, {}).get("item_type") == "THEOREM"
        and normative.get(drift, {}).get("layer") == "L5"
        and normative.get(drift, {}).get("gate_ids") == ""
        and normative.get(coin_selector, {}).get("item_type") == "THEOREM"
        and normative.get(coin_selector, {}).get("layer") == "MULTI"
        and normative.get(coin_selector, {}).get("gate_ids") == ""
        and normative.get(coin_premise, {}).get("item_type") == "DICTIONARY"
        and normative.get(coin_premise, {}).get("status") == "D"
        and normative.get(coin_premise, {}).get("layer") == "L1"
        and normative.get(coin_premise, {}).get("gate_ids") == ""
        and normative.get(coin_derivation, {}).get("item_type") == "OBLIGATION"
        and normative.get(coin_derivation, {}).get("layer") == "MULTI"
        and normative.get(coin_derivation, {}).get("gate_ids") == coin_gate
        and actual_boost_dependencies == expected_boost_dependencies
        and all(
            evidence.get(item, {}).get("evidence_kind") == "PUBLIC_PROBE"
            and evidence.get(item, {}).get("location") == boost_path
            and evidence.get(item, {}).get("sha256") == boost_digest
            and evidence.get(item, {}).get("hash_mode")
                == "bundle-manifest-sha256-v1"
            and evidence.get(item, {}).get("architecture_requirement")
                == "two-architecture"
            for item in boost_items
        )
        and scope_contains_all(
            index, drift,
            ("division-free spectral skeleton",
             "minimum 16/5",
             "V_inf(1) = -beta_1 A_1",
             "for every N >= 1",
             "P1 and P2 are premises rather than conclusions",
             "no decoherence"),
        )
        and scope_contains_all(
            index, coin_selector,
            ("exactly {beta_1,beta_3}",
             "generic/rung multiplicities 2/1",
             "non-integral half-rung",
             "S1 minimum generic multiplicity",
             "S3 maximum coherent half-width",
             "theorem adopts no selector"),
        )
        and scope_contains_all(
            index, coin_premise,
            ("adopts beta_1 by MINIMAL-READ",
             "MAXIMAL-REACH",
             "not a general equivalence",
             "no claim that the decoder architecture forces MINIMAL-READ"),
        )
        and scope_contains_all(
            index, coin_derivation,
            ("complete registered decoder architecture",
             "without adopting MINIMAL-READ as a premise",
             "typed L5-read to L1-coin selection route"),
        )
        and all(
            phrase.lower() in index[coin_derivation]["falsifier"].lower()
            for phrase in (
                "complete admissible decoder class is proved nonempty",
                "fully compliant beta_1 and beta_3 realizations",
                "failure of no-feedback or any one favored route is STOP",
                "classifies the complete admissible class",
            )
        )
        and gates.get(coin_gate, {}).get("owner_item_id") == coin_derivation
        and gates.get(coin_gate, {}).get("from_layer") == "L5"
        and gates.get(coin_gate, {}).get("to_layer") == "L1"
        and gates.get(coin_gate, {}).get("gate_kind") == "OPEN_SELECTION"
        and all(
            phrase.lower() in gates[coin_gate]["decision_condition"].lower()
            for phrase in (
                "complete typed decoder carrier",
                "cover-to-output map",
                "accumulator/equality rule",
                "redundancy theorem",
                "uniquely force w = 1 and beta_1",
                "complete admissible class is proved nonempty",
                "fully compliant beta_1 and beta_3 realizations",
                "failure of one favored route is only STOP",
            )
        )
        and drift not in programs
        and coin_selector not in programs
        and coin_premise not in programs
        and programs.get(coin_derivation, {}).get("program_id") == "DECODER_CORE"
        and programs.get(coin_derivation, {}).get("queue_role") == "ROOT"
        and programs.get(coin_derivation, {}).get("work_state") == "STOP"
        and programs.get(coin_derivation, {}).get("work_mode") == "FORMAL"
        and retired_observer not in index
        and retired_observer not in normative
        and retired_observer not in evidence
        and retired_observer not in programs
        and all(
            retired_observer not in (row["item_id"], row["depends_on"])
            for row in dependencies
        )
        and all(
            row["owner_item_id"] != retired_observer
            for row in gates.values()
        ),
    ))

    checks.append((
        "FORCE",
        "the finite Weyl commutator stays T; force as curvature is D",
        has_status(index, "FORCE-WEYL-HOLONOMY", "T")
        and has_status(index, "FORCE-AS-CURVATURE", "D")
        and scope_lacks(index, "FORCE-WEYL-HOLONOMY",
                        ("force", "curvature", "gravity", "electromagnetism")),
    ))

    scheme = "SCHEME-DICTIONARY"
    scheme_dependencies = {
        (row["depends_on"], row["relation"])
        for row in dependencies if row["item_id"] == scheme
    }
    checks.append((
        "SCHEME",
        "scheme dictionary stays O and is explicitly STOP before definition",
        has_status(index, scheme, "O")
        and normative.get(scheme, {}).get("item_type") == "OBLIGATION"
        and normative.get(scheme, {}).get("status") == "O"
        and normative.get(scheme, {}).get("layer") == "NOT_APPLICABLE"
        and normative.get(scheme, {}).get("gate_ids") == ""
        and evidence.get(scheme, {}).get("evidence_kind") == "INLINE_CANON"
        and evidence.get(scheme, {}).get("location") == "inline"
        and evidence.get(scheme, {}).get("sha256")
        == scope_sha256(index, scheme)
        and evidence.get(scheme, {}).get("architecture_requirement") == "none"
        and scheme_dependencies == {("DEF-ARCHITECTURE", "REQUIRES")}
        and all(
            phrase.lower() in index[scheme]["falsifier"].lower()
            for phrase in (
                "STOP until the exact source-seed domain",
                "named measurement scheme",
                "scale and threshold conventions",
                "total map with equality and window semantics",
                "source manifests",
                "complete acyclic dependency graph",
                "failure of one candidate is STOP",
                "exact dictionary at that frozen scope requiring no new free dimensionless parameter",
                "every admissible dictionary requires a new free dimensionless parameter",
            )
        )
        and programs.get(scheme, {}) == {
            "claim_id": scheme,
            "program_id": "DECODER_CORE",
            "queue_role": "ROOT",
            "work_state": "STOP",
            "work_mode": "FORMAL",
        }
        and all(row["owner_item_id"] != scheme for row in gates.values())
    ))

    checks.append((
        "MAXWELL",
        "four exact chain rows stay T; the classical Maxwell reading is D",
        all(has_status(index, claim, "T") for claim in
            ("MAXWELL-BIANCHI", "MAXWELL-GAUSS-CHAIN",
             "MAXWELL-AMPERE-CHAIN", "MAXWELL-OBSTRUCTION-P"))
        and has_status(index, "MAXWELL-CLOSED", "D"),
    ))

    checks.append((
        "BORN",
        "finite Born algebra stays T; measurement and cell readings are D",
        all(has_status(index, claim, "T") for claim in
            ("BORN-FACE-WEIGHTS", "BORN-HALF-ANGLE",
             "BORN-RESIDUAL-SPLIT", "SPIN-BISECTOR",
             "BORN-ORDER-STAIRCASE", "SUBSTRATE-KNIT"))
        and all(has_status(index, claim, "D") for claim in
                ("MEASURE-BORN-VERB", "KERNEL-CELL-DICTIONARY"))
        and scope_lacks(index, "SUBSTRATE-KNIT",
                        ("born", "measurement", "abelian face")),
    ))

    central = "CENTRAL-LIFT-PHASE"
    central_path = "probes/P-CENTRAL-LIFT-PHASE-1"
    central_digest = (
        "ff0ffb98cbc3197d18a86a22dd3cabe853b5f50a80e099ede48b1ae6a7a258e0"
    )
    central_dependencies = {
        (row["depends_on"], row["relation"])
        for row in dependencies if row["item_id"] == central
    }
    checks.append((
        "CENTRAL",
        "central Herm/Sym phase stays T at L4; cone, decoder, and physics stay outside",
        has_status(index, central, "T")
        and normative.get(central, {}).get("item_type") == "THEOREM"
        and normative.get(central, {}).get("status") == "T"
        and normative.get(central, {}).get("layer") == "L4"
        and normative.get(central, {}).get("gate_ids") == ""
        and index.get(central, {}).get("canon_section") == "4. The two places"
        and index.get(central, {}).get("evidence") == central_path
        and evidence.get(central, {}).get("evidence_id")
        == "EV-CENTRAL-LIFT-PHASE"
        and evidence.get(central, {}).get("evidence_kind") == "PUBLIC_PROBE"
        and evidence.get(central, {}).get("location") == central_path
        and evidence.get(central, {}).get("sha256") == central_digest
        and evidence.get(central, {}).get("hash_mode")
        == "bundle-manifest-sha256-v1"
        and evidence.get(central, {}).get("architecture_requirement")
        == "two-architecture"
        and central_dependencies == {
            ("J-PROJECTIONS", "REQUIRES"),
            ("J-TENTH-ROOT", "REQUIRES"),
            ("J-GOLDEN-BRIDGE", "REQUIRES"),
            ("DEF-ACTION-LAYERS", "REQUIRES"),
        }
        and scope_contains_all(
            index, central,
            ("fifth projective Herm power is a pure boost",
             "H_(cA) = H_A", "central Sym factor zeta_5^2",
             "image of O_K^x", "exactly mu_5",
             "mu_10 \\ mu_5", "L4 quadratic-support",
             "no Herm2 positive/Born/causal cone", "decoder Q or QCarrier",
             "MatterData", "L5 stream", "L6 measure", "cross-layer lift"),
        )
        and all(
            phrase.lower() in index[central]["falsifier"].lower()
            for phrase in (
                "unit-phase image differs from mu_5",
                "1-J lies in mu_5",
                "excluded physical, decoder, cone, carrier, or cross-layer",
                "integrity STOP, not a scientific falsifier",
            )
        )
        and qdd_current_split
        and central not in programs,
    ))

    quartic = "QUARTIC-CYCLOTOMIC-TOTAL-RAMIFICATION-CENSUS"
    quartic_path = (
        "probes/P-QUARTIC-CYCLOTOMIC-TOTAL-RAMIFICATION-CENSUS-1"
    )
    quartic_digest = (
        "05f6a5c1e29b5e962c357f323ec2104d39f771230ea5cb6953a6b25126bbe5ee"
    )
    quartic_dependencies = {
        (row["depends_on"], row["relation"])
        for row in dependencies if row["item_id"] == quartic
    }
    checks.append((
        "QUARTIC",
        "quartic total ramification stays T at L1; no field selection or physical lift",
        has_status(index, quartic, "T")
        and normative.get(quartic, {}).get("item_type") == "THEOREM"
        and normative.get(quartic, {}).get("status") == "T"
        and normative.get(quartic, {}).get("layer") == "L1"
        and normative.get(quartic, {}).get("gate_ids") == ""
        and index.get(quartic, {}).get("canon_section") == "4. The two places"
        and index.get(quartic, {}).get("evidence") == quartic_path
        and evidence.get(quartic, {}).get("evidence_id")
        == "EV-QUARTIC-CYCLOTOMIC-TOTAL-RAMIFICATION-CENSUS"
        and evidence.get(quartic, {}).get("evidence_kind") == "PUBLIC_PROBE"
        and evidence.get(quartic, {}).get("location") == quartic_path
        and evidence.get(quartic, {}).get("sha256") == quartic_digest
        and evidence.get(quartic, {}).get("hash_mode")
        == "bundle-manifest-sha256-v1"
        and evidence.get(quartic, {}).get("architecture_requirement")
        == "two-architecture"
        and quartic_dependencies == {
            ("C20-TEICHMULLER-SPLIT", "REQUIRES"),
            ("RAMIFIED-TM-LIFT", "REQUIRES"),
            ("DEF-ACTION-LAYERS", "REQUIRES"),
        }
        and scope_contains_all(
            index, quartic,
            ("phi(n)=4 exactly for n in {5,8,10,12}",
             "Q(zeta_10)=Q(zeta_5)",
             "total-ramification locus is exactly {(K_5,5),(K_8,2)}",
             "(e,f,g)=(2,2,1)", "F_5^x=C_4", "F_2^x=C_1",
             "F_4^x=C_3", "F_9^x=C_8", "J mod p_(5,5)=2",
             "L1 exact arithmetic only", "no selection of degree four",
             "TWO-PLACE-PHYSICS promotion", "lift to L2-L6"),
        )
        and all(
            phrase.lower() in index[quartic]["falsifier"].lower()
            for phrase in (
                "solution set of phi(n)=4 differs",
                "total-ramification locus differs",
                "J-reduction mismatch requires correction",
                "integrity STOP, not a scientific falsifier",
            )
        )
        and has_status(index, "TWO-PLACE-PHYSICS", "D")
        and quartic not in programs,
    ))

    abelian_cm = "ABELIAN-CM-UNIQUE-EVEN-BIT-DISCRIMINANT-MINIMUM"
    abelian_cm_path = (
        "probes/P-ABELIAN-CM-UNIQUE-EVEN-BIT-DISCRIMINANT-MINIMUM-1"
    )
    abelian_cm_digest = (
        "31a4d20d4cd73778a7c058435ccc9e8bb1b7fcdc5a5475a5181c1e3aa739e2e0"
    )
    abelian_cm_dependencies = {
        (row["depends_on"], row["relation"])
        for row in dependencies if row["item_id"] == abelian_cm
    }
    checks.append((
        "ABELIAN-CM",
        "unique even-bit minimum stays T at L1; its class is not a physical selector",
        has_status(index, abelian_cm, "T")
        and normative.get(abelian_cm, {}).get("item_type") == "THEOREM"
        and normative.get(abelian_cm, {}).get("status") == "T"
        and normative.get(abelian_cm, {}).get("layer") == "L1"
        and normative.get(abelian_cm, {}).get("gate_ids") == ""
        and index.get(abelian_cm, {}).get("canon_section")
        == "4. The two places"
        and index.get(abelian_cm, {}).get("evidence") == abelian_cm_path
        and evidence.get(abelian_cm, {}).get("evidence_id")
        == "EV-ABELIAN-CM-UNIQUE-EVEN-BIT-DISCRIMINANT-MINIMUM"
        and evidence.get(abelian_cm, {}).get("evidence_kind")
        == "PUBLIC_PROBE"
        and evidence.get(abelian_cm, {}).get("location") == abelian_cm_path
        and evidence.get(abelian_cm, {}).get("sha256") == abelian_cm_digest
        and evidence.get(abelian_cm, {}).get("hash_mode")
        == "bundle-manifest-sha256-v1"
        and evidence.get(abelian_cm, {}).get("architecture_requirement")
        == "two-architecture"
        and abelian_cm_dependencies == {
            ("DEF-ACTION-LAYERS", "REQUIRES"),
        }
        and scope_contains_all(
            index, abelian_cm,
            ("Q(zeta_5) belongs to A",
             "|Hom(G_K,C_2)|=2 including the trivial character",
             "absDisc(K)>=125",
             "unique absolute-discriminant minimizer",
             "primitive character epsilon associated to the pointwise square psi^2",
             "pure 2-primary control (16,8) giving floor 2048",
             "no total-ramification premise",
             "no claim that A or discriminant minimization is selected",
             "TWO-PLACE-PHYSICS promotion", "lift to L2-L6"),
        )
        and all(
            phrase.lower() in index[abelian_cm]["falsifier"].lower()
            for phrase in (
                "field K in A has absDisc(K)<125",
                "not Q-isomorphic to Q(zeta_5) has absDisc(K)=125",
                "Q(zeta_5) fails an admissibility condition",
                "field conductor-discriminant identity",
                "integrity STOP, not a scientific falsifier",
            )
        )
        and "## Two field characterisations involving five" in core_text
        and "{(K_5,5),(K_8,2)}" in core_text
        and "unique absolute-discriminant" in core_text
        and "separate frozen classes, not a physical-selection chain or evidence"
        in core_text
        and has_status(index, "TWO-PLACE-PHYSICS", "D")
        and abelian_cm not in programs,
    ))

    cm_pencil = "CM-ALTERNATING-PENCIL"
    cm_pencil_path = "probes/P-CM-ALTERNATING-PENCIL-1"
    cm_pencil_digest = (
        "74e15b610ef60afab903b241ff550febd08ce6ca8a685f0b1be698e1528163ed"
    )
    cm_pencil_dependencies = {
        (row["depends_on"], row["relation"])
        for row in dependencies if row["item_id"] == cm_pencil
    }
    checks.append((
        "CM-PENCIL",
        "alternating trace pencil stays T at L1; repaired similitude boundary stays exact",
        has_status(index, cm_pencil, "T")
        and normative.get(cm_pencil, {}).get("item_type") == "THEOREM"
        and normative.get(cm_pencil, {}).get("status") == "T"
        and normative.get(cm_pencil, {}).get("layer") == "L1"
        and normative.get(cm_pencil, {}).get("gate_ids") == ""
        and index.get(cm_pencil, {}).get("canon_section")
        == "4. The two places"
        and index.get(cm_pencil, {}).get("evidence") == cm_pencil_path
        and evidence.get(cm_pencil, {}).get("evidence_id")
        == "EV-CM-ALTERNATING-PENCIL"
        and evidence.get(cm_pencil, {}).get("evidence_kind")
        == "PUBLIC_PROBE"
        and evidence.get(cm_pencil, {}).get("location") == cm_pencil_path
        and evidence.get(cm_pencil, {}).get("sha256") == cm_pencil_digest
        and evidence.get(cm_pencil, {}).get("hash_mode")
        == "bundle-manifest-sha256-v1"
        and evidence.get(cm_pencil, {}).get("architecture_requirement")
        == "two-architecture"
        and cm_pencil_dependencies == {
            ("J-GOLDEN-BRIDGE", "REQUIRES"),
            ("J-STEP", "REQUIRES"),
            ("DEF-ACTION-LAYERS", "REQUIRES"),
        }
        and scope_contains_all(
            index, cm_pencil,
            ("L = lambda_1 Z[phi]",
             "Omega_lam(x,y) = Tr(lam x conjugate(y))/5",
             "unimodular exactly when (lam) = (lambda_1)",
             "Pf(Omega_(a,b)) = a^2-a b-b^2",
             "Pell unit orbit",
             "action kernel is exactly {+zeta_5^k,-zeta_5^k : 0<=k<5}",
             "A_J=[[1,-1],[-1,2]]",
             "A_J is the inverse of its square",
             "unit multiplication has a scalar multiplier only at +1",
             "conjugation acts with multiplier -1",
             "L1 exact algebra only",
             "lift to L2-L6"),
        )
        and all(
            phrase.lower() in index[cm_pencil]["falsifier"].lower()
            for phrase in (
                "unimodular locus differs",
                "relative-norm kernel other than the ten roots of unity",
                "integral determinant-one scalar similitude has multiplier outside {+1,-1}",
                "unit other than a root of unity fixes Omega_1",
                "conjugation does not act by -1",
                "changed evidence bundle or architecture transcript",
                "integrity STOP",
            )
        )
        and cm_pencil not in programs,
    ))

    color_theorems = (
        "COLOR-RETURN-D5", "COLOR-TORSOR-HOLONOMY",
        "COLOR-KIN-NORMALIZER", "COLOR-CORE-2I", "COLOR-GOLDEN-TABLE",
        "COLOR-MCKAY-E8", "COLOR-MOMENT-FINGERPRINT",
        "COLOR-SPECTRAL-INVARIANTS", "COLOR-DICKSON-RAMIFICATION",
        "COLOR-KLEIN-REDUCTION", "COLOR-INTEGRAL-LIFT",
        "COLOR-MEASURE-TRANSPORT",
    )
    checks.append((
        "COLOR",
        "finite group and invariant rungs stay T; the color reading is D",
        all(has_status(index, claim, "T") for claim in color_theorems)
        and has_status(index, "COLOR-LADDER-DICTIONARY", "D"),
    ))

    cm_pair = "COLOR-CM-2I-SEMILINEAR-PAIR"
    cm_path = "probes/P-CM-2I-QCARRIER-1"
    cm_digest = "2d480767d992215fe0c7328c8fb794484cd7c99c22d6b56f65b340c8b9d09bee"
    cm_dependencies = {
        (row["depends_on"], row["relation"])
        for row in dependencies if row["item_id"] == cm_pair
    }
    checks.append((
        "CM-2I",
        "marked semilinear pair stays T at L4; the algebraic decoder dictionary stays D while physical apparatus and measure stay O/STOP",
        has_status(index, cm_pair, "T")
        and normative.get(cm_pair, {}).get("item_type") == "THEOREM"
        and normative.get(cm_pair, {}).get("status") == "T"
        and normative.get(cm_pair, {}).get("layer") == "L4"
        and normative.get(cm_pair, {}).get("gate_ids") == ""
        and index.get(cm_pair, {}).get("canon_section") == "12. The color door"
        and index.get(cm_pair, {}).get("evidence") == cm_path
        and evidence.get(cm_pair, {}).get("evidence_id")
        == "EV-COLOR-CM-2I-SEMILINEAR-PAIR"
        and evidence.get(cm_pair, {}).get("evidence_kind") == "PUBLIC_PROBE"
        and evidence.get(cm_pair, {}).get("location") == cm_path
        and evidence.get(cm_pair, {}).get("sha256") == cm_digest
        and evidence.get(cm_pair, {}).get("hash_mode")
        == "bundle-manifest-sha256-v1"
        and evidence.get(cm_pair, {}).get("architecture_requirement")
        == "two-architecture"
        and cm_dependencies == {
            ("COLOR-INTEGRAL-LIFT", "REQUIRES"),
            ("DEF-ACTION-LAYERS", "REQUIRES"),
        }
        and scope_contains_all(
            index, cm_pair,
            ("marked twist-isomorphism stabilizer is exactly {1,sigma}",
             "Galois-stable K-isomorphism class through explicit intertwiners",
             "Hom_G(rho^tau,rho) = 0",
             "Hom_G(rho^sigma,rho) = K C0",
             "End_G(rho^tau) = K I2",
             "Hom_G(rho^sigma,rho^tau) = 0",
             "exhaustive antidiagonal form",
             "cocycle class [-1]", "order four is impossible",
             "eight is the smallest attainable finite order",
             "invariant sigma-Hermitian forms",
             "exactly the F-line F H0",
             "phi^2 forced by determinants and positivity",
             "no claim is made that the full space of invariant forms",
             "no Q-form or coherent C4 descent datum",
             "no uniqueness or selection of a marked lift",
             "decoder Q or QCarrier", "decoder Gram",
             "orbit-to-amplitude map", "MatterData",
             "physical U(1)", "L5-L6 measure lift"),
        )
        and all(
            phrase.lower() in index[cm_pair]["falsifier"].lower()
            for phrase in (
                "pair character is not Q-valued",
                "an explicit Galois pair intertwiner fails",
                "H0 is not totally positive definite",
                "balanced multiplier is not forced to phi^2",
            )
        )
        and has_status(index, "SPIN-LIFT-FORCED", "F")
        and qdd_current_split
        and has_status(index, "COLOR-MEASURE-SELECTION", "O")
        and programs.get("COLOR-MEASURE-SELECTION", {}).get("program_id")
        == "NONABELIAN_QCD"
        and programs.get("COLOR-MEASURE-SELECTION", {}).get("queue_role")
        == "ROOT"
        and programs.get("COLOR-MEASURE-SELECTION", {}).get("work_state")
        == "STOP"
        and programs.get("COLOR-MEASURE-SELECTION", {}).get("work_mode")
        == "FORMAL"
        and cm_pair not in programs,
    ))

    gyron_density = "GYRON-DENSITY"
    gyron_discrepancy = "GYRON-DISCREPANCY-LOG"
    gyron_fixed_point = "TM-PAIR-SUBSTITUTION-FIXED-POINT"
    gyron_items = (gyron_density, gyron_discrepancy, gyron_fixed_point)
    gyron_path = "probes/P-GYRON-DISCREPANCY-LOG-3"
    gyron_digest = "b4e7eba23b815d0964a8516f25fe3cdc6db363e3646d658253ea5e9289e9382e"
    expected_gyron_dependencies = {
        gyron_density: {
            ("DEF-ARCHITECTURE", "REQUIRES"),
            (gyron_discrepancy, "REQUIRES"),
            (gyron_fixed_point, "REQUIRES"),
        },
        gyron_discrepancy: {("DEF-ARCHITECTURE", "REQUIRES")},
        gyron_fixed_point: {("DEF-ARCHITECTURE", "REQUIRES")},
    }
    actual_gyron_dependencies = {
        item: {
            (row["depends_on"], row["relation"])
            for row in dependencies if row["item_id"] == item
        }
        for item in gyron_items
    }
    checks.append((
        "COSMOLOGY",
        "exact L1 Gyron theorems stay T; their physical reading stays D",
        all(has_status(index, claim, "T") for claim in
            ("TT-LINEAR-ZERO",) + gyron_items)
        and has_status(index, "COSMOLOGY-READING-DICTIONARY", "D")
        and scope_lacks(index, "TT-LINEAR-ZERO",
                        ("tensor", "isotropic", "r = 0", "cosmology"))
        and scope_lacks(index, gyron_density,
                        ("proton", "cosmology", "mass ladder", "basel"))
        and scope_contains_all(index, gyron_density,
                               ("both prefix normalizations",
                                "holds iff L is even",
                                "fixed I(v_*) and B(v_*) phase readouts",
                                "physical probability or measure"))
        and scope_contains_all(index, gyron_discrepancy,
                               ("complete 96-path",
                                "d(4L) = d(L) iff L is even",
                                "audit rather than proof",
                                "L2-L6 claim"))
        and scope_contains_all(index, gyron_fixed_point,
                               ("full maps are unequal",
                                "spectrum {1,-1/2,0}",
                                "only under their frozen equal average",
                                "not coarse-graining",
                                "decoder factor"))
        and all(
            normative[item]["item_type"] == "THEOREM"
            and normative[item]["status"] == "T"
            and normative[item]["layer"] == "L1"
            and normative[item]["gate_ids"] == ""
            for item in gyron_items
        )
        and all(
            evidence[item]["evidence_kind"] == "PUBLIC_PROBE"
            and evidence[item]["location"] == gyron_path
            and evidence[item]["sha256"] == gyron_digest
            and evidence[item]["hash_mode"]
                == "bundle-manifest-sha256-v1"
            and evidence[item]["architecture_requirement"]
                == "two-architecture"
            for item in gyron_items
        )
        and actual_gyron_dependencies == expected_gyron_dependencies,
    ))

    checks.append((
        "SCHWINGER",
        "the exact target stays T while its physical realization stays O",
        has_status(index, "QUANT-SCHWINGER-TARGET", "T")
        and has_status(index, "QUANT-SUBSTRATE", "O")
        and all(has_status(index, claim, "T") for claim in
                ("J-MODULUS-CHORD", "BRIDGE-DEFECT"))
        and scope_contains_all(
            index, "QUANT-SCHWINGER-TARGET",
            ("J Jbar / script-Q = 1/(2 pi)", "arithmetic only",
             "no identification"),
        )
        and scope_contains_all(
            index, "QUANT-SUBSTRATE",
            ("physical-realization gate", "remains open"),
        ),
    ))

    c20 = "C20-TEICHMULLER-SPLIT"
    time_tower = "TIME-QUANTUM-TOWER"
    graph = dependency_graph(dependencies)
    c20_outgoing = [
        (row["depends_on"], row["relation"], row["basis"])
        for row in dependencies
        if row["item_id"] == c20
    ]
    checks.append((
        "C20",
        "the L1 C20 theorem stays separate from time and decoder readings",
        has_status(index, c20, "T")
        and normative.get(c20, {}).get("item_type") == "THEOREM"
        and normative.get(c20, {}).get("status") == "T"
        and normative.get(c20, {}).get("layer") == "L1"
        and normative.get(c20, {}).get("gate_ids") == ""
        and normative.get(c20, {}).get("statement_source")
        == "canon/CANON.md::1. The axiom and the two projections"
        and index.get(c20, {}).get("canon_section")
        == "1. The axiom and the two projections"
        and index.get(c20, {}).get("evidence")
        == "probes/P-C20-TEICHMULLER-SPLIT-2"
        and evidence.get(c20, {}).get("location")
        == "probes/P-C20-TEICHMULLER-SPLIT-2"
        and evidence.get(c20, {}).get("evidence_id")
        == "EV-C20-TEICHMULLER-SPLIT"
        and evidence.get(c20, {}).get("evidence_kind") == "PUBLIC_PROBE"
        and evidence.get(c20, {}).get("sha256")
        == "bca1d2850ed40871bc8304defca46ee33f84f31f71a7197b30dfdbc2ded4db90"
        and evidence.get(c20, {}).get("hash_mode")
        == "bundle-manifest-sha256-v1"
        and evidence.get(c20, {}).get("architecture_requirement")
        == "two-architecture"
        and scope_contains_all(
            index, c20,
            ("(5) = (lambda)^4 is an equality of ideals",
             "not an element equality", "finite local ring",
             "<J> = <t> x <u> isomorphic to C_4 x C_5",
             "for every m >= 1 the Sylow 2-subgroup of A_m^* is C_4",
             "no A_m contains an element of order 8",
             "no all-k order claim for M_J modulo 5^k",
             "L1 exact arithmetic only", "time", "decoder",
             "L2-L6 claim"),
        )
        and has_status(index, "J-STEP", "T")
        and c20_outgoing == [
            ("J-STEP", "REQUIRES",
             "the reduced matrix leg reconstructs M_R from the four public "
             "J-STEP columns and identifies it with multiplication by J")
        ]
        and has_status(index, time_tower, "C")
        and scope_contains_all(
            index, time_tower,
            ("computed exhaustively for k = 1 to 4",
             "no all-k theorem is claimed"),
        )
        and index.get(time_tower, {}).get("evidence")
        == "reproduce/foundations-places"
        and evidence.get(time_tower, {}).get("location")
        == "reproduce/foundations-places"
        and evidence.get(time_tower, {}).get("evidence_kind") == "REPRODUCTION"
        and not reaches(graph, c20, time_tower)
        and not reaches(graph, time_tower, c20),
    ))

    projective = "TM-SYM2-PROJECTIVE-FOURFOLD"
    semilinear = "TM-SYM2-SEMILINEAR-TWOFOLD"
    reversal = "TM-SYM2-REVERSAL-CLOSURE"
    spectral = "TM-SYM2-SPECTRAL-COHERENCE"
    frozen_owner = "TM-SYM2-MEASURE"
    physical_owner = "TM-SYM2-PHYSICAL-MEASURE"
    orientation_source = "DEF-TM-SYM2-ORIENTATION-SOURCE"
    monomial_lift = "DEF-TM-SYM2-MONOMIAL-VERB-LIFT"
    selector_gate = "GATE-L1-L5-TM-SYM2-SELECTOR-STREAM"
    born_gate = "GATE-L5-L6-TM-SYM2-BORN-MEASURE"
    tm_theorems = (projective, semilinear, reversal, spectral)
    expected_tm_dependencies = {
        projective: {
            ("DEF-ARCHITECTURE", "REQUIRES"),
            ("DEF-ACTION-LAYERS", "REQUIRES"),
            ("RAMIFIED-TM-LIFT", "REQUIRES"),
            ("GOLDEN-SIX-LINE-SYM2-FRAME", "REQUIRES"),
        },
        semilinear: {
            ("DEF-ARCHITECTURE", "REQUIRES"),
            (projective, "REQUIRES"),
        },
        reversal: {
            ("DEF-ARCHITECTURE", "REQUIRES"),
            (semilinear, "REQUIRES"),
        },
        spectral: {
            ("DEF-ARCHITECTURE", "REQUIRES"),
            (projective, "REQUIRES"),
            (semilinear, "REQUIRES"),
        },
        orientation_source: {
            (projective, "REQUIRES"),
            (semilinear, "REQUIRES"),
            (reversal, "REQUIRES"),
        },
        monomial_lift: {
            ("J-UNIT", "REQUIRES"),
            ("J-GOLDEN-BRIDGE", "REQUIRES"),
        },
        physical_owner: {
            ("DEF-ARCHITECTURE", "REQUIRES"),
            ("DEF-ACTION-LAYERS", "REQUIRES"),
            ("GOLDEN-SIX-LINE-SYM2-FRAME", "REQUIRES"),
            (projective, "REQUIRES"),
            (orientation_source, "REQUIRES"),
            (monomial_lift, "REQUIRES"),
            ("MEASURE-BORN-VERB", "REQUIRES"),
            ("ABELIAN-FACE-DICTIONARY", "REQUIRES"),
            (frozen_owner, "BOUNDED_BY"),
            (semilinear, "BOUNDED_BY"),
            (reversal, "BOUNDED_BY"),
            (spectral, "BOUNDED_BY"),
        },
    }
    actual_tm_dependencies = {
        item: {
            (row["depends_on"], row["relation"])
            for row in dependencies if row["item_id"] == item
        }
        for item in expected_tm_dependencies
    }
    theorem_to_owner = any(
        row["item_id"] in tm_theorems
        and row["depends_on"] in {frozen_owner, physical_owner}
        for row in dependencies
    )
    theorem_scopes = " ".join(index[item]["scope"].lower()
                              for item in tm_theorems)
    expected_evidence = {
        projective: (
            "probes/P-TM-SYM2-MEASURE-1",
            "f943c0fc8412fd6f39a0d21a6e51fffe4bda2d06ad8ec78e41816e44a35b113d",
        ),
        semilinear: (
            "probes/P-TM-SYM2-SEMILINEAR-GAUGE-1",
            "016bd059695ed9eb9ba21f7f36c9bd1ef90798fc130816ef6537c971080cfa1a",
        ),
        reversal: (
            "probes/P-TM-SYM2-REVERSAL-CLOSURE-1",
            "b329f3a65f821690e8ab1514b6ab2cc9c307ba05ebcccaf6c0d326bd36dc619e",
        ),
        spectral: (
            "probes/P-TM-SYM2-SPECTRAL-COHERENCE-1",
            "22662135d6e5e6a7cd6729690a98f6c2998bcedd24f8cd696feb5cc16d81e60c",
        ),
    }
    checks.append((
        "TM-SYM2",
        "four exact classifications stay T; fired selector stays F; physical successor closes only at D",
        all(has_status(index, item, "T") for item in tm_theorems)
        and normative.get(projective, {}).get("item_type") == "THEOREM"
        and normative.get(projective, {}).get("layer") == "MULTI"
        and normative.get(semilinear, {}).get("layer") == "L5"
        and normative.get(reversal, {}).get("layer") == "L5"
        and normative.get(spectral, {}).get("item_type") == "THEOREM"
        and normative.get(spectral, {}).get("layer") == "L5"
        and normative.get(spectral, {}).get("gate_ids") == ""
        and all(
            index.get(item, {}).get("evidence") == path
            and evidence.get(item, {}).get("location") == path
            and evidence.get(item, {}).get("sha256") == digest
            and evidence.get(item, {}).get("evidence_kind") == "PUBLIC_PROBE"
            and evidence.get(item, {}).get("hash_mode")
            == "bundle-manifest-sha256-v1"
            and evidence.get(item, {}).get("architecture_requirement")
            == "two-architecture"
            for item, (path, digest) in expected_evidence.items()
        )
        and scope_contains_all(
            index, projective,
            ("|Sel_class| = 48", "order 12 and acts freely",
             "four G-orbits of size 12", "NONCANONICAL",
             "nu_s(v_i) = 1/6", "M_s = (1/3)P1 + (2/15)P5",
             "no preferred selector", "or L6 measure"),
        )
        and scope_contains_all(
            index, semilinear,
            ("Gamma_sl = ker(chi_Q chi_F)", "order 24",
             "12 exponent-one members", "two selector orbits of size 24",
             "not adopted as gauge"),
        )
        and scope_contains_all(
            index, reversal,
            ("t_N = (0,1)", "t_R = (1,0)", "t_NR = (1,1)",
             "NONREALIZABLE", "REALIZABLE-E1", "one orbit of size 48",
             "precomposition closure only", "not a postcomposition"),
        )
        and scope_contains_all(
            index, spectral,
            ("frozen v16 S_TM carrier", "48-selector class", "L5"),
        )
        and has_status(index, frozen_owner, "F")
        and normative.get(frozen_owner, {}).get("item_type") == "FALSIFIED"
        and normative.get(frozen_owner, {}).get("gate_ids") == selector_gate
        and index.get(frozen_owner, {}).get("evidence")
        == "probes/P-TM-SYM2-MEASURE-1"
        and scope_contains_all(
            index, frozen_owner,
            ("frozen v16 S_TM compound route is falsified",
             "48 exact selectors", "four free projective-linear",
             "NONCANONICAL and N2 fires", "Born branch is not reached",
             "does not falsify", "every future TM-to-measure definition"),
        )
        and has_status(index, physical_owner, "D")
        and normative.get(physical_owner, {}).get("item_type") == "DICTIONARY"
        and normative.get(physical_owner, {}).get("layer") == "MULTI"
        and normative.get(physical_owner, {}).get("gate_ids") == born_gate
        and normative.get(orientation_source, {}).get("item_type") == "DEFINITION"
        and normative.get(orientation_source, {}).get("layer") == "L5"
        and normative.get(monomial_lift, {}).get("item_type") == "DEFINITION"
        and normative.get(monomial_lift, {}).get("layer") == "L5"
        and index.get(physical_owner, {}).get("evidence") == "probes/P-TM-SYM2-BORN-HALVING-1"
        and evidence.get(physical_owner, {}).get("evidence_id") == "EV-TM-SYM2-PHYSICAL-MEASURE"
        and evidence.get(physical_owner, {}).get("evidence_kind") == "PUBLIC_PROBE"
        and evidence.get(physical_owner, {}).get("location") == "probes/P-TM-SYM2-BORN-HALVING-1"
        and evidence.get(physical_owner, {}).get("sha256") == "acc598e670eb7e57f689a6ecc970438ce7211d1a097514a78847100e8871fa59"
        and evidence.get(physical_owner, {}).get("hash_mode") == "bundle-manifest-sha256-v1"
        and evidence.get(physical_owner, {}).get("architecture_requirement") == "two-architecture"
        and scope_contains_all(
            index, physical_owner,
            ("owner-approved typed L5-to-L6 physical dictionary bridge",
             "C_sel = Sel_class/G with four classes",
             "epsilon_read = chi_Q chi_F", "omega(a,b,c) = c-a",
             "separately frozen monomial verb-lift class",
             "same normalized two-sheet law for every t",
             "six equal line weights 1/6 only as an output",
             "no selector representative is chosen",
             "no postcomposition gauge is enlarged",
             "same-modulus nonmonomial lift has unequal coefficient Born weights",
             "no uniqueness among all amplitude lifts",
             "GYRON identification"),
        )
        and gates.get(selector_gate, {}).get("owner_item_id") == frozen_owner
        and gates.get(selector_gate, {}).get("gate_kind") == "FIRED_NEGATIVE"
        and gates.get(selector_gate, {}).get("from_layer") == "L1"
        and gates.get(selector_gate, {}).get("to_layer") == "L5"
        and "four free projective-linear gauge orbits of size 12"
        in gates.get(selector_gate, {}).get("decision_condition", "")
        and gates.get(born_gate, {}).get("owner_item_id") == physical_owner
        and gates.get(born_gate, {}).get("gate_kind") == "DICTIONARY_LIFT"
        and gates.get(born_gate, {}).get("from_layer") == "L5"
        and gates.get(born_gate, {}).get("to_layer") == "L6"
        and "complete orientation-retaining L5 source"
        in gates.get(born_gate, {}).get("decision_condition", "")
        and frozen_owner not in programs
        and spectral not in programs
        and physical_owner not in programs
        and actual_tm_dependencies == expected_tm_dependencies
        and not theorem_to_owner
        and not has_cycle(graph)
        and "nullity" not in theorem_scopes
        and "q(zeta_5)" not in theorem_scopes
    ))

    wall = "WALL-LI2-RUNG"
    wall_dependencies = {
        (row["depends_on"], row["relation"])
        for row in dependencies if row["item_id"] == wall
    }
    wall_quant_edges = [
        row for row in dependencies
        if {row["item_id"], row["depends_on"]} == {wall, "QUANT-SUBSTRATE"}
    ]
    checks.append((
        "WALL-LI2",
        "the exact Li_2 rung stays T while substrate coupling stays O",
        has_status(index, wall, "T")
        and normative.get(wall, {}).get("item_type") == "THEOREM"
        and normative.get(wall, {}).get("layer") == "NOT_APPLICABLE"
        and index.get(wall, {}).get("evidence") == "inline"
        and evidence.get(wall, {}).get("evidence_kind") == "INLINE_CANON"
        and evidence.get(wall, {}).get("location") == "inline"
        and evidence.get(wall, {}).get("sha256")
        == "520d79c7fb2fd2a3c1909877f1a7576ea61488be6652cf5c1a2a7541624b20cd"
        and evidence.get(wall, {}).get("hash_mode")
        == "registry-scope-sha256-v1"
        and evidence.get(wall, {}).get("architecture_requirement") == "none"
        and wall_dependencies == {
            ("J-PROJECTIONS", "REQUIRES"),
            ("PI-FROM-J", "REQUIRES"),
        }
        and not wall_quant_edges
        and scope_contains_all(
            index, wall,
            ("principal dilogarithm", "pi^2/100", "9 pi^2/100",
             "Galois-orbit real-part sum", "no field-trace claim",
             "substrate coupling", "Schwinger coefficient"),
        )
        and has_status(index, "QUANT-SUBSTRATE", "O")
    ))

    circle = "WALL-CIRCLE-LEMMA"
    circle_dependencies = {
        (row["depends_on"], row["relation"])
        for row in dependencies if row["item_id"] == circle
    }
    circle_reverse_edges = [
        row for row in dependencies
        if row["item_id"] == wall and row["depends_on"] == circle
    ]
    circle_quant_edges = [
        row for row in dependencies
        if {row["item_id"], row["depends_on"]}
        == {circle, "QUANT-SUBSTRATE"}
    ]
    checks.append((
        "WALL-CIRCLE",
        "the uniform root-circle theorem stays exact and outside physics",
        has_status(index, circle, "T")
        and normative.get(circle, {}).get("item_type") == "THEOREM"
        and normative.get(circle, {}).get("status") == "T"
        and normative.get(circle, {}).get("layer") == "NOT_APPLICABLE"
        and normative.get(circle, {}).get("gate_ids") == ""
        and index.get(circle, {}).get("evidence") == "inline"
        and evidence.get(circle, {}).get("evidence_id")
        == "EV-WALL-CIRCLE-LEMMA"
        and evidence.get(circle, {}).get("evidence_kind") == "INLINE_CANON"
        and evidence.get(circle, {}).get("location") == "inline"
        and evidence.get(circle, {}).get("sha256")
        == scope_sha256(index, circle)
        and evidence.get(circle, {}).get("hash_mode")
        == "registry-scope-sha256-v1"
        and evidence.get(circle, {}).get("architecture_requirement") == "none"
        and circle_dependencies == {
            ("J-PROJECTIONS", "REQUIRES"),
            ("PI-FROM-J", "REQUIRES"),
        }
        and not circle_reverse_edges
        and not circle_quant_edges
        and scope_contains_all(
            index, circle,
            ("psi = -Arg(-zeta_N^a)",
             "midpoint 2a = N proved directly from z = 0",
             "Li_1(0) = Li_2(0) = 0",
             "full nontrivial-root sum",
             "N = 5 specialization reproduces WALL-LI2-RUNG",
             "no statement about substrate coupling",
             "physical observables", "or uniqueness"),
        )
        and has_status(index, wall, "T")
        and has_status(index, "QUANT-SUBSTRATE", "O")
    ))

    metro = "METRO-FINITE-STATE-RATIONALITY"
    metro_calculus = "METRO-REDUCTION-CALCULUS"
    metro_arrows = "METRO-REDUCTION-ARROWS"
    metro_child = "METRO-ADMISSIBILITY-DIM"
    metro_residual = "METRO-ADMISSIBILITY"
    metro_gate = "GATE-L5-L6-METRO-NORMALIZATION"
    metro_dependencies = {
        item: {
            (row["depends_on"], row["relation"])
            for row in dependencies if row["item_id"] == item
        }
        for item in (metro, metro_arrows, metro_calculus, metro_child, metro_residual)
    }
    metro_residual_edges = [
        row for row in dependencies
        if {row["item_id"], row["depends_on"]} == {metro, metro_residual}
    ]
    checks.append((
        "METRO",
        "finite-state theorem stays T; reduction arrows stay C; typed calculus, dimensional child, and residual stay O",
        has_status(index, metro, "T")
        and normative.get(metro, {}).get("item_type") == "THEOREM"
        and normative.get(metro, {}).get("status") == "T"
        and normative.get(metro, {}).get("layer") == "L5"
        and normative.get(metro, {}).get("gate_ids") == ""
        and index.get(metro, {}).get("evidence") == "inline"
        and evidence.get(metro, {}).get("evidence_id")
        == "EV-METRO-FINITE-STATE-RATIONALITY"
        and evidence.get(metro, {}).get("evidence_kind") == "INLINE_CANON"
        and evidence.get(metro, {}).get("location") == "inline"
        and evidence.get(metro, {}).get("sha256")
        == scope_sha256(index, metro)
        and evidence.get(metro, {}).get("hash_mode")
        == "registry-scope-sha256-v1"
        and evidence.get(metro, {}).get("architecture_requirement") == "none"
        and metro_dependencies[metro] == set()
        and not metro_residual_edges
        and scope_contains_all(
            index, metro,
            ("accessible q-DFAO", "rational output vector",
             "every row sum of B is q", "converge entrywise to L 1",
             "then L is rational", "q-primary spectral projector",
             "conditional rationality of an existing common limit only",
             "no convergence existence criterion", "L5-to-L6 lift"),
        )
        and "row-sum mismatch is outside the declared q-dfao input schema"
        in index[metro]["falsifier"].lower()
        and has_status(index, metro_arrows, "C")
        and normative.get(metro_arrows, {}).get("item_type") == "COMPUTATION"
        and normative.get(metro_arrows, {}).get("status") == "C"
        and normative.get(metro_arrows, {}).get("layer") == "L5"
        and normative.get(metro_arrows, {}).get("gate_ids") == ""
        and index.get(metro_arrows, {}).get("evidence")
        == "probes/P-METRO-REDUCTION-ARROWS-4"
        and evidence.get(metro_arrows, {}).get("evidence_id")
        == "EV-METRO-REDUCTION-ARROWS"
        and evidence.get(metro_arrows, {}).get("evidence_kind")
        == "PUBLIC_PROBE"
        and evidence.get(metro_arrows, {}).get("location")
        == "probes/P-METRO-REDUCTION-ARROWS-4"
        and evidence.get(metro_arrows, {}).get("sha256")
        == "7864cb2ea6a6939cc477efa89f005fd71943091b446866decfa5a4db9036e8c6"
        and evidence.get(metro_arrows, {}).get("hash_mode")
        == "bundle-manifest-sha256-v1"
        and evidence.get(metro_arrows, {}).get("architecture_requirement")
        == "one-architecture"
        and metro_dependencies[metro_arrows] == {
            ("DEF-ARCHITECTURE", "REQUIRES"),
        }
        and scope_contains_all(
            index, metro_arrows,
            ("typed L5 U_RF tuple",
             "four admitted reductions have exact preconditions and transports",
             "state relabeling by a bijection",
             "closure of A0 under every single-digit map",
             "multi-action Nerode quotient",
             "congruence for every coordinate i >= 2",
             "coordinate 1 automatic",
             "coordinate permutation transporting coordinate names",
             "tau_R = identity",
             "exact pointwise transported L5-stream equality",
             "zero congruence counterexamples",
             "exactly 1024 two-state and 4251528 three-state protocols",
             "computation-only L5 scope",
             "no forbidden-transformation catalogue",
             "common q^k blocking",
             "completeness of approx_red",
             "or L6, cross-layer, physical, or SI claim"),
        )
        and all(
            phrase.lower() in index[metro_arrows]["falsifier"].lower()
            for phrase in (
                "pinned evidence bundle or exact stdout differs",
                "17 frozen gates fails",
                "admitted arrow changes a transported pointwise L5 stream",
                "either exhaustive family yields a congruence counterexample",
                "obligation B", "common q^k blocking",
                "approx_red completeness", "every L6",
            )
        )
        and metro_arrows not in programs
        and has_status(index, metro_calculus, "O")
        and normative.get(metro_calculus, {}).get("item_type") == "OBLIGATION"
        and normative.get(metro_calculus, {}).get("status") == "O"
        and normative.get(metro_calculus, {}).get("layer") == "L5"
        and normative.get(metro_calculus, {}).get("gate_ids") == ""
        and evidence.get(metro_calculus, {}).get("evidence_id")
        == "EV-METRO-REDUCTION-CALCULUS"
        and evidence.get(metro_calculus, {}).get("evidence_kind")
        == "INLINE_CANON"
        and evidence.get(metro_calculus, {}).get("location") == "inline"
        and evidence.get(metro_calculus, {}).get("sha256")
        == scope_sha256(index, metro_calculus)
        and evidence.get(metro_calculus, {}).get("hash_mode")
        == "registry-scope-sha256-v1"
        and evidence.get(metro_calculus, {}).get("architecture_requirement")
        == "none"
        and metro_dependencies[metro_calculus] == {
            ("DEF-ARCHITECTURE", "REQUIRES"),
            (metro, "REQUIRES"),
            (metro_arrows, "REQUIRES"),
        }
        and scope_contains_all(
            index, metro_calculus,
            ("remaining open L5 reduction-calculus obligations",
             "after METRO-REDUCTION-ARROWS [C]",
             "obligation B",
             "complete forbidden-transformation catalogue",
             "obligation D", "common q^k blocking",
             "scientific decision", "terminal value",
             "obligation E",
             "completeness of the finite-zig-zag equivalence approx_red",
             "obligations A and C are separated",
             "do not close B, D, or E",
             "no normalization or cross-layer gate is owned"),
        )
        and all(
            phrase.lower() in index[metro_calculus]["falsifier"].lower()
            for phrase in (
                "every forbidden entry has an exact witness",
                "common q^k blocking",
                "decision and terminal-value transport",
                "approx_red is complete",
                "STOP while any forbidden-witness",
                "closes only obligations A and C",
                "leaves this row O and STOP",
            )
        )
        and programs.get(metro_calculus, {}).get("program_id") == "DECODER_CORE"
        and programs.get(metro_calculus, {}).get("queue_role") == "ROOT"
        and programs.get(metro_calculus, {}).get("work_state") == "STOP"
        and programs.get(metro_calculus, {}).get("work_mode") == "FORMAL"
        and has_status(index, metro_child, "O")
        and normative.get(metro_child, {}).get("item_type") == "OBLIGATION"
        and normative.get(metro_child, {}).get("status") == "O"
        and normative.get(metro_child, {}).get("layer") == "MULTI"
        and normative.get(metro_child, {}).get("gate_ids") == metro_gate
        and evidence.get(metro_child, {}).get("evidence_id")
        == "EV-METRO-ADMISSIBILITY-DIM"
        and evidence.get(metro_child, {}).get("evidence_kind")
        == "INLINE_CANON"
        and evidence.get(metro_child, {}).get("location") == "inline"
        and evidence.get(metro_child, {}).get("sha256")
        == scope_sha256(index, metro_child)
        and evidence.get(metro_child, {}).get("hash_mode")
        == "registry-scope-sha256-v1"
        and evidence.get(metro_child, {}).get("architecture_requirement")
        == "none"
        and metro_dependencies[metro_child] == {
            ("DEF-ARCHITECTURE", "REQUIRES"),
            ("DEF-ACTION-LAYERS", "REQUIRES"),
            (metro_calculus, "REQUIRES"),
            (metro, "REQUIRES"),
        }
        and scope_contains_all(
            index, metro_child,
            ("finite N^a-indexed commuting digit-word systems",
             "complete raw L5 stream", "total tagged L6 normalization Y_r",
             "uniform translated-box convergence with an effective modulus",
             "independently defined joint certificate",
             "sound, complete, and decision-coherent"),
        )
        and gates.get(metro_gate, {}).get("owner_item_id") == metro_child
        and gates.get(metro_gate, {}).get("gate_kind") == "OPEN_LIFT"
        and gates.get(metro_gate, {}).get("from_layer") == "L5"
        and gates.get(metro_gate, {}).get("to_layer") == "L6"
        and all(
            phrase.lower() in gates[metro_gate]["decision_condition"].lower()
            for phrase in (
                "complete raw L5 stream", "total tagged L6 normalization",
                "effective modulus", "independent joint certificate",
                "invariant under every allowed reduction",
            )
        )
        and programs.get(metro_child, {}).get("program_id") == "DECODER_CORE"
        and programs.get(metro_child, {}).get("queue_role") == "FOLLOWUP"
        and programs.get(metro_child, {}).get("work_state") == "STOP"
        and programs.get(metro_child, {}).get("work_mode") == "FORMAL"
        and has_status(index, metro_residual, "O")
        and normative.get(metro_residual, {}).get("item_type") == "OBLIGATION"
        and normative.get(metro_residual, {}).get("status") == "O"
        and normative.get(metro_residual, {}).get("layer")
        == "NOT_APPLICABLE"
        and normative.get(metro_residual, {}).get("gate_ids") == ""
        and evidence.get(metro_residual, {}).get("evidence_id")
        == "EV-METRO-ADMISSIBILITY"
        and evidence.get(metro_residual, {}).get("evidence_kind")
        == "INLINE_CANON"
        and evidence.get(metro_residual, {}).get("location") == "inline"
        and evidence.get(metro_residual, {}).get("sha256")
        == scope_sha256(index, metro_residual)
        and evidence.get(metro_residual, {}).get("hash_mode")
        == "registry-scope-sha256-v1"
        and evidence.get(metro_residual, {}).get("architecture_requirement")
        == "none"
        and metro_dependencies[metro_residual] == {
            ("DEF-ARCHITECTURE", "REQUIRES"),
            (metro_calculus, "REQUIRES"),
        }
        and scope_contains_all(
            index, metro_residual,
            ("exhaustive residual cover R1 through R8",
             "R1=U_RF minus the commuting higher-rank "
             "METRO-ADMISSIBILITY-DIM child",
             "rank-one", "noncommuting", "non-finite-state",
             "unbounded-memory adaptive", "non-reducible stochastic",
             "irrational", "out-of-child cross-layer", "physical-unit",
             "mixed-class protocols"),
        )
        and all(
            phrase.lower() in index[metro_residual]["falsifier"].lower()
            for phrase in (
                "STOP until R1 through R8 each has a typed child",
                "closes only when all eight children close",
            )
        )
        and programs.get(metro_residual, {}).get("program_id")
        == "DECODER_CORE"
        and programs.get(metro_residual, {}).get("queue_role") == "FOLLOWUP"
        and programs.get(metro_residual, {}).get("work_state") == "STOP"
        and programs.get(metro_residual, {}).get("work_mode") == "FORMAL"
        and metro not in programs
    ))

    entropy = "ENTROPY-CYLINDER-NOGO-CURSOR"
    entropy_cut = "ENTROPY-CYLINDER-CUT"
    entropy_bridge = "ENTROPY-LAYER-BRIDGE"
    entropy_gate = "GATE-L2-L5-ENTROPY-BRIDGE"
    entropy_dependencies = {
        (row["depends_on"], row["relation"])
        for row in dependencies if row["item_id"] == entropy
    }
    entropy_bridge_edges = {
        (row["depends_on"], row["relation"])
        for row in dependencies
        if row["item_id"] == entropy_bridge
        and row["depends_on"] in {entropy, entropy_cut}
    }
    entropy_cut_edges = [
        row for row in dependencies
        if {row["item_id"], row["depends_on"]} == {entropy, entropy_cut}
    ]
    checks.append((
        "ENTROPY",
        "cursor cylinder no-go stays T; narrow cut stays F and Route A bridge stays O",
        has_status(index, entropy, "T")
        and normative.get(entropy, {}).get("item_type") == "THEOREM"
        and normative.get(entropy, {}).get("status") == "T"
        and normative.get(entropy, {}).get("layer") == "L5"
        and normative.get(entropy, {}).get("gate_ids") == ""
        and index.get(entropy, {}).get("evidence")
        == "probes/P-ENTROPY-CURSOR-CLOSURE-1"
        and evidence.get(entropy, {}).get("evidence_id")
        == "EV-ENTROPY-CYLINDER-NOGO-CURSOR"
        and evidence.get(entropy, {}).get("evidence_kind") == "PUBLIC_PROBE"
        and evidence.get(entropy, {}).get("location")
        == "probes/P-ENTROPY-CURSOR-CLOSURE-1"
        and evidence.get(entropy, {}).get("sha256")
        == "422ca1708e351b067f31134965f70d150194c4a6041be0351c9c131b3086f370"
        and evidence.get(entropy, {}).get("hash_mode")
        == "bundle-manifest-sha256-v1"
        and evidence.get(entropy, {}).get("architecture_requirement")
        == "two-architecture"
        and entropy_dependencies == {("DEF-ARCHITECTURE", "REQUIRES")}
        and not entropy_cut_edges
        and scope_contains_all(
            index, entropy,
            ("exact L5 finite-cylindrical constraint graph on F_5^6",
             "two-sided Thue-Morse factor language",
             "every pure-word system at every cursor c = 0..L-1",
             "every window L = 4..32", "global solution count zero",
             "labelled graph projects exactly to the pure-word graph",
             "zero residue is fixed by multiplication by J",
             "same obstruction holds at every finite lambda-depth",
             "27 direct checks", "audits, not the source",
             "no non-cylindrical cut", "P_5 construction",
             "measurable selection", "L6", "physical claim"),
        )
        and entropy not in programs
        and has_status(index, entropy_cut, "F")
        and normative.get(entropy_cut, {}).get("item_type") == "FALSIFIED"
        and normative.get(entropy_cut, {}).get("status") == "F"
        and normative.get(entropy_cut, {}).get("layer") == "L5"
        and evidence.get(entropy_cut, {}).get("evidence_kind")
        == "PUBLIC_PROBE"
        and evidence.get(entropy_cut, {}).get("sha256")
        == "950f20397d23f395730e408a2400804c8a8dded2ac1c5e515e86a2f96ebd5f29"
        and evidence.get(entropy_cut, {}).get("architecture_requirement")
        == "two-architecture"
        and scope_contains_all(
            index, entropy_cut,
            ("cursor c = 0 for L = 4..16",
             "(L,c) = (5,1), (6,1), (6,2)",
             "no other cursor or window is included"),
        )
        and has_status(index, entropy_bridge, "O")
        and normative.get(entropy_bridge, {}).get("item_type") == "OBLIGATION"
        and normative.get(entropy_bridge, {}).get("status") == "O"
        and normative.get(entropy_bridge, {}).get("layer") == "MULTI"
        and normative.get(entropy_bridge, {}).get("gate_ids") == entropy_gate
        and evidence.get(entropy_bridge, {}).get("evidence_id")
        == "EV-ENTROPY-LAYER-BRIDGE"
        and evidence.get(entropy_bridge, {}).get("evidence_kind")
        == "PUBLIC_PROBE"
        and evidence.get(entropy_bridge, {}).get("location")
        == "probes/P-ENTROPY-BRIDGE-1"
        and evidence.get(entropy_bridge, {}).get("sha256")
        == "96cca583006f7090d094fd4a025a78e6ee4f98fb7627af7c880f829beafccb57"
        and evidence.get(entropy_bridge, {}).get("hash_mode")
        == "bundle-manifest-sha256-v1"
        and evidence.get(entropy_bridge, {}).get("architecture_requirement")
        == "two-architecture"
        and scope_contains_all(
            index, entropy_bridge,
            ("measurable total maps P_5", "mu-almost-everywhere",
             "exact equivariance", "exact pushforward Law_W",
             "equal cardinalities do not construct an element of A_A"),
        )
        and all(
            phrase.lower() in index[entropy_bridge]["falsifier"].lower()
            for phrase in (
                "any registered (L,c) with 4 <= L <= 32",
                "at any finite lambda-depth",
                "would refute ENTROPY-CYLINDER-NOGO-CURSOR",
                "rather than close this row",
                "inside the older ENTROPY-CYLINDER-CUT scope",
                "correction of that F row",
            )
        )
        and entropy_bridge_edges == {
            (entropy_cut, "REQUIRES"),
            (entropy, "BOUNDED_BY"),
        }
        and gates.get(entropy_gate, {}).get("owner_item_id") == entropy_bridge
        and gates.get(entropy_gate, {}).get("gate_kind") == "OPEN_LIFT"
        and gates.get(entropy_gate, {}).get("from_layer") == "L2"
        and gates.get(entropy_gate, {}).get("to_layer") == "L5"
        and all(
            phrase.lower() in gates[entropy_gate]["decision_condition"].lower()
            for phrase in (
                "A_A is proved nonempty by one exact map",
                "mu-almost-everywhere equivariance",
                "pushforward Law_W", "A_A=empty",
                "failure of one proposal is STOP",
            )
        )
        and programs.get(entropy_bridge, {}).get("program_id") == "MEASURE"
        and programs.get(entropy_bridge, {}).get("queue_role") == "ROOT"
        and programs.get(entropy_bridge, {}).get("work_state") == "STOP"
        and programs.get(entropy_bridge, {}).get("work_mode") == "FORMAL"
    ))

    photon_child = "PHOTON-KAPPA-LEMMA"
    photon_parent = "PHOTON-WINDOW-PROOF"
    photon_path = "probes/P-PHOTON-KAPPA-LEMMA-1"
    photon_digest = (
        "b0f14e92c008fdd5fcdbc6f0960aac0e1b5b55bb85b1e05dd3945fa67b31f0d6"
    )
    photon_child_dependencies = {
        (row["depends_on"], row["relation"])
        for row in dependencies if row["item_id"] == photon_child
    }
    photon_parent_dependencies = {
        (row["depends_on"], row["relation"])
        for row in dependencies if row["item_id"] == photon_parent
    }
    roughening = "PHOTON-ROUGHENING-CERTIFICATE"
    checks.append((
        "PHOTON",
        "Kappa universal proposition and compound route are F; roughening stays unregistered",
        has_status(index, photon_child, "F")
        and normative.get(photon_child, {}).get("item_type") == "FALSIFIED"
        and normative.get(photon_child, {}).get("status") == "F"
        and normative.get(photon_child, {}).get("layer") == "L4"
        and normative.get(photon_child, {}).get("gate_ids") == ""
        and evidence.get(photon_child, {}).get("evidence_id")
        == "EV-PHOTON-KAPPA-LEMMA"
        and evidence.get(photon_child, {}).get("evidence_kind")
        == "PUBLIC_PROBE"
        and evidence.get(photon_child, {}).get("location") == photon_path
        and evidence.get(photon_child, {}).get("sha256") == photon_digest
        and evidence.get(photon_child, {}).get("hash_mode")
        == "bundle-manifest-sha256-v1"
        and evidence.get(photon_child, {}).get("architecture_requirement")
        == "two-architecture"
        and photon_child_dependencies == {
            ("DEF-ARCHITECTURE", "REQUIRES"),
            ("MONOPOLE-FIFTHS", "REQUIRES"),
        }
        and scope_contains_all(
            index, photon_child,
            ("positive proposition", "is false on the frozen L4 carrier",
             "no connectedness restriction", "partial n=5j",
             "F_occ(j_*)<=7993", "neither equality nor optimality",
             "no roughening", "no roughening, Froehlich-Spencer, Coulomb"),
        )
        and all(
            phrase.lower() in index[photon_child]["falsifier"].lower()
            for phrase in (
                "fired", "public two-architecture exact certificate",
                "2^7993<=7^3240", "no value of F_occ(j_*) is computed",
            )
        )
        and photon_child not in programs
        and has_status(index, photon_parent, "F")
        and normative.get(photon_parent, {}).get("item_type") == "FALSIFIED"
        and normative.get(photon_parent, {}).get("status") == "F"
        and evidence.get(photon_parent, {}).get("evidence_kind")
        == "PUBLIC_PROBE"
        and evidence.get(photon_parent, {}).get("location") == photon_path
        and evidence.get(photon_parent, {}).get("sha256") == photon_digest
        and evidence.get(photon_parent, {}).get("architecture_requirement")
        == "two-architecture"
        and photon_parent_dependencies == {
            ("DEF-ARCHITECTURE", "REQUIRES"),
            (photon_child, "REQUIRES"),
        }
        and scope_contains_all(
            index, photon_parent,
            ("requires both (i)", "and (ii)",
             "electric-face roughening certificate"),
        )
        and photon_parent not in programs
        and roughening not in index
        and roughening not in normative
        and roughening not in programs
        and has_status(index, "KAPPA-SHAPES", "C")
        and has_status(index, "MONOPOLE-COST", "C")
    ))

    collapse = "LAMBDA-COCYCLE-BRANCH-COLLAPSE"
    grid = "LAMBDA-COCYCLE-GRID-EQUIVALENCE"
    angles = "LAMBDA-COCYCLE-ANGLES"
    collapse_path = "probes/P-LAMBDA-COCYCLE-ANGLES-1"
    grid_path = "probes/P-LAMBDA-COCYCLE-ANGLES-2"
    collapse_digest = (
        "6fa30375944a0c5ad2ed84705191552442dc1024b4248046a1382f5a0caf7710"
    )
    grid_digest = (
        "d721d7dea495f447f136a30fc310d99fee27b5fa3af7515c62fb662d120486f2"
    )
    lambda_dependencies = {
        (row["item_id"], row["depends_on"], row["relation"])
        for row in dependencies if row["item_id"] in {collapse, grid}
    }
    checks.append((
        "LAMBDA-COC",
        "both wall reductions stay T at L6; the cocycle hypothesis stays H and unfired",
        all(
            has_status(index, claim, "T")
            and normative.get(claim, {}).get("item_type") == "THEOREM"
            and normative.get(claim, {}).get("status") == "T"
            and normative.get(claim, {}).get("layer") == "L6"
            and normative.get(claim, {}).get("gate_ids") == ""
            and index.get(claim, {}).get("canon_section")
            == "16. p = 5 and the wall"
            and evidence.get(claim, {}).get("evidence_kind") == "PUBLIC_PROBE"
            and evidence.get(claim, {}).get("hash_mode")
            == "bundle-manifest-sha256-v1"
            and evidence.get(claim, {}).get("architecture_requirement")
            == "two-architecture"
            and claim not in programs
            for claim in (collapse, grid)
        )
        and index.get(collapse, {}).get("evidence") == collapse_path
        and evidence.get(collapse, {}).get("location") == collapse_path
        and evidence.get(collapse, {}).get("sha256") == collapse_digest
        and index.get(grid, {}).get("evidence") == grid_path
        and evidence.get(grid, {}).get("location") == grid_path
        and evidence.get(grid, {}).get("sha256") == grid_digest
        and lambda_dependencies == {
            (collapse, angles, "BOUNDED_BY"),
            (grid, collapse, "REQUIRES"),
        }
        and scope_contains_all(
            index, collapse,
            ("1 - 1/rho = e^(i alpha_gamma)",
             "0 <= M - t_n <= 2 M is necessary at every n",
             "no general finite-profile nonfalsifiability or realization theorem",
             "a finite ordinate window"),
        )
        and scope_contains_all(
            index, grid,
            ("y = 0 is the unique orbit of length 1",
             "exact positive level k",
             "ord_(lambda^(4m))(J) = 4 . 5^m for every m >= 1",
             "n_0 = 4 occurs at level 1",
             "dist(4 . 5^A x,Z) -> 0",
             "pure point spectrum with eigenvalue angle set exactly",
             "if and only if RH holds"),
        )
        and has_status(index, angles, "H")
        and normative.get(angles, {}).get("item_type") == "HYPOTHESIS"
        and normative.get(angles, {}).get("layer") == "L6"
        and programs.get(angles, {}) == {
            "claim_id": angles, "program_id": "ENRICHMENT",
            "queue_role": "ROOT", "work_state": "BLOCKED",
            "work_mode": "ENRICHMENT",
        }
        and evidence.get(angles, {}).get("sha256")
        == "811c41d0d1b1ec00fa1d114385c7915bd648dfea8c0e773ca41c292768156bdc"
        and scope_contains_all(
            index, angles,
            ("if and only if RH holds",
             "rho = 1/(1 - xi) with xi != 1",
             "n_A = 4 . 5^A",
             "no general finite-profile nonfalsifiability or realization theorem"),
        )
        and all(
            phrase.lower() in index[angles]["falsifier"].lower()
            for phrase in (
                "fires if rh is disproved",
                "for a critical-line zero that is exactly the exclusion",
                "exact finite violation",
                "finite satisfaction does not decide the row",
            )
        )
    ))

    seam = "J-HARMONIC-SEAM"
    seam_path = "probes/P-J-HARMONIC-SEAM-1"
    seam_digest = (
        "9054c62b919f5edb1b67ae9100d5ab733fd78a6b094662424a24a43a8bfe21cd"
    )
    seam_dependencies = {
        (row["depends_on"], row["relation"])
        for row in dependencies if row["item_id"] == seam
    }
    checks.append((
        "J-SEAM",
        "harmonic seam stays T at L1; dictionary, places, decoder, and physics stay outside",
        has_status(index, seam, "T")
        and normative.get(seam, {}).get("item_type") == "THEOREM"
        and normative.get(seam, {}).get("status") == "T"
        and normative.get(seam, {}).get("layer") == "L1"
        and normative.get(seam, {}).get("gate_ids") == ""
        and index.get(seam, {}).get("canon_section")
        == "1. The axiom and the two projections"
        and index.get(seam, {}).get("evidence") == seam_path
        and evidence.get(seam, {}).get("evidence_id") == "EV-J-HARMONIC-SEAM"
        and evidence.get(seam, {}).get("evidence_kind") == "PUBLIC_PROBE"
        and evidence.get(seam, {}).get("location") == seam_path
        and evidence.get(seam, {}).get("sha256") == seam_digest
        and evidence.get(seam, {}).get("hash_mode")
        == "bundle-manifest-sha256-v1"
        and evidence.get(seam, {}).get("architecture_requirement")
        == "two-architecture"
        and seam_dependencies == {
            ("J-GOLDEN-BRIDGE", "REQUIRES"),
            ("J-TENTH-ROOT", "REQUIRES"),
        }
        and scope_contains_all(
            index, seam,
            ("u_n=-psi^n=-F_(n+1)-F_n zeta_5^2-F_n zeta_5^3",
             "H(x) is real iff x in {1,-1}",
             "Re H(x)=0 iff x in {-zeta_5,-zeta_5^-1}",
             "O_K^x=mu_10 x <phi>",
             "Log J=-H(1)-2H(-zeta_5)",
             "no promotion of AXIOM-PROJECTION-DICTIONARY or TWO-PLACE-PHYSICS",
             "no decoder, measure, observer, force, spacetime, SI bridge",
             "lift to L2-L6"),
        )
        and all(
            phrase.lower() in index[seam]["falsifier"].lower()
            for phrase in (
                "universal integral numerator identity",
                "complete mu_10 axis classification",
                "unit-group product",
                "principal-branch reconstruction of Log J",
                "integrity STOP",
            )
        )
        and has_status(index, "AXIOM-PROJECTION-DICTIONARY", "D")
        and has_status(index, "TWO-PLACE-PHYSICS", "D")
        and has_status(index, "BOOST-COUNT-LADDER", "D")
        and has_status(index, "LOG-AXES-INDEPENDENCE", "T")
        and qdd_current_split
        and seam not in programs,
    ))

    mobius = "MOBIUS-TM-PRIME2-BRIDGE"
    mobius_path = "probes/P-MOBIUS-TM-PRIME2-1"
    mobius_digest = (
        "94c8338bb78d2836c4bb707ce3dc13ed00b38f423645e17c78d6d3bc07cd501a"
    )
    mobius_dependencies = {
        (row["depends_on"], row["relation"])
        for row in dependencies if row["item_id"] == mobius
    }
    checks.append((
        "MOBIUS-TM",
        "prime-2 bridge stays exact L1 arithmetic with no fermionizer or physical lift",
        has_status(index, mobius, "T")
        and normative.get(mobius, {}).get("item_type") == "THEOREM"
        and normative.get(mobius, {}).get("status") == "T"
        and normative.get(mobius, {}).get("layer") == "L1"
        and normative.get(mobius, {}).get("gate_ids") == ""
        and index.get(mobius, {}).get("canon_section")
        == "9. The photon and the electron"
        and index.get(mobius, {}).get("evidence") == mobius_path
        and evidence.get(mobius, {}).get("evidence_id")
        == "EV-MOBIUS-TM-PRIME2-BRIDGE"
        and evidence.get(mobius, {}).get("evidence_kind") == "PUBLIC_PROBE"
        and evidence.get(mobius, {}).get("location") == mobius_path
        and evidence.get(mobius, {}).get("sha256") == mobius_digest
        and evidence.get(mobius, {}).get("hash_mode")
        == "bundle-manifest-sha256-v1"
        and evidence.get(mobius, {}).get("architecture_requirement")
        == "two-architecture"
        and mobius_dependencies == set()
        and all(row["depends_on"] != mobius for row in dependencies)
        and scope_contains_all(
            index, mobius,
            ("D_p f=f on all positive integers iff",
             "c_TM(2n)=0 for every n>=1",
             "unique odd-supported arithmetic function",
             "with I the identity operator",
             "c_TM(n)=product_(p|n)(D_p-I)tau_TM(1)",
             "c_TM(15)=-2",
             "product_(j>=0)(1-x^(2^j))-1",
             "zeta_odd(s)C_TM(s)=T_TM,odd(s)",
             "tau=sqrt(J)",
             "mu(2x)=-mu(x) restricted to odd x",
             "no multiplicativity or Euler-product claim",
             "not equal to FERMIONIZER's Phi_f(s)=1-2^(1-s) at the same argument",
             "although it equals Phi_f(s+1)",
             "unused shift creating no dependency or physical identification",
             "no RH, zeta-zero, Nyman-Beurling, Baez-Duarte",
             "pointwise or averaged/Cesaro Moebius-Thue-Morse orthogonality",
             "Sarnak-type correlation",
             "asymptotic cancellation",
             "physical-vacuum",
             "L2-L6 conclusion"),
        )
        and all(
            phrase.lower() in index[mobius]["falsifier"].lower()
            for phrase in (
                "prime-dilation equivalence",
                "even-support annihilation",
                "odd-supported uniqueness or reconstruction",
                "odd-squarefree Boolean formula",
                "Lambert identity in |x|<1",
                "Dirichlet identities",
                "integrity STOP",
            )
        )
        and has_status(index, "FERMIONIZER", "T")
        and has_status(index, "TM-BREATH-TOWER", "T")
        and mobius not in programs
        and all(row["owner_item_id"] != mobius for row in gates.values()),
    ))

    carry_mul = "TM-MULTIPLICATION-CARRY-DEFECT"
    carry_mul_path = "probes/P-TM-MULTIPLICATION-CARRY-DEFECT-1"
    carry_mul_digest = (
        "348e359dd2c2566c7c142ac9f7217bec3dd4ab3e725584e89a477420354e50bf"
    )
    carry_mul_dependencies = {
        (row["depends_on"], row["relation"])
        for row in dependencies if row["item_id"] == carry_mul
    }
    checks.append((
        "TM-MUL-CARRY",
        "multiplication carry defect stays standalone L1 arithmetic with no physical lift",
        has_status(index, carry_mul, "T")
        and normative.get(carry_mul, {}).get("item_type") == "THEOREM"
        and normative.get(carry_mul, {}).get("status") == "T"
        and normative.get(carry_mul, {}).get("layer") == "L1"
        and normative.get(carry_mul, {}).get("gate_ids") == ""
        and index.get(carry_mul, {}).get("canon_section")
        == "9. The photon and the electron"
        and index.get(carry_mul, {}).get("evidence") == carry_mul_path
        and evidence.get(carry_mul, {}).get("evidence_id")
        == "EV-TM-MULTIPLICATION-CARRY-DEFECT"
        and evidence.get(carry_mul, {}).get("evidence_kind") == "PUBLIC_PROBE"
        and evidence.get(carry_mul, {}).get("location") == carry_mul_path
        and evidence.get(carry_mul, {}).get("sha256") == carry_mul_digest
        and evidence.get(carry_mul, {}).get("hash_mode")
        == "bundle-manifest-sha256-v1"
        and evidence.get(carry_mul, {}).get("architecture_requirement")
        == "two-architecture"
        and carry_mul_dependencies == set()
        and all(row["depends_on"] != carry_mul for row in dependencies)
        and scope_contains_all(
            index, carry_mul,
            ("kappa_(2,mul)(a,b)=s_2(a)s_2(b)-s_2(ab)>=0",
             "normalization-order-independent count of unit moves",
             "R=(P AND Q) XOR K",
             "tau_TM(ab)tau_TM(a)tau_TM(b)=(-1)^((P OR Q) XOR K)",
             "takes the values -2,-4,0,-2,0,-2,0,2",
             "vanishes iff K=0 and (P OR Q)=1",
             "kappa_(2,mul)(3,11)=4 and c_TM(33)=0",
             "c_TM(p^2)=0 iff kappa_(2,mul)(p,p) is even",
             "Delta_mul(empty)=0",
             "c_TM(n)=sum_(S subseteq {1,...,m})",
             "finite-vector-space e_2 carry layer of CARRY-PENTAD",
             "chronological nu_2(n+1) carry cocycle of RAMIFIED-TM-LIFT",
             "semiprime table not asserting realization",
             "c_TM=0 not implying zero carries or trivial multiplication",
             "no multiplicativity claim for c_TM",
             "no dependence on MOBIUS-TM-PRIME2-BRIDGE as a theorem premise",
             "decoder, measure, Born, observer",
             "physical-vacuum, matter, light, entanglement, curvature",
             "L2-L6 conclusion"),
        )
        and all(
            phrase.lower() in index[carry_mul]["falsifier"].lower()
            for phrase in (
                "raw-column recurrence",
                "carry-mass identity",
                "unit-normalization-order independence",
                "lexicographic semiprime table entry",
                "prime-square identity",
                "odd-squarefree carry-parity-cube formula",
                "integrity STOP",
            )
        )
        and carry_mul not in programs
        and all(
            row["owner_item_id"] != carry_mul for row in gates.values()
        ),
    ))

    hankel_path = "probes/P-TM-HANKEL-K3-TRANSFER-1"
    hankel_digest = (
        "364f459aee2910edc27e3fa7c85e692f0a8f93cf7c17e7bc0771daa334b53592"
    )
    hankel_rows = {
        "TM-HANKEL-DIVISOR-BRIDGE": ("T", "THEOREM"),
        "TM-HANKEL-SQUAREFUL-RANK-NOGO": ("T", "THEOREM"),
        "TM-HANKEL-EXTREMAL-WITT-SKELETON": ("T", "THEOREM"),
        "TM-HANKEL-K2-TRANSFER": ("T", "THEOREM"),
        "TM-HANKEL-K3-UNIVERSAL-TRANSFER": ("F", "FALSIFIED"),
        "TM-HANKEL-K3-TWO-SCALAR-CLASSIFICATION": ("C", "COMPUTATION"),
        "TM-HANKEL-K3-QUADRATIC-INVARIANT-SUFFICIENCY": ("C", "COMPUTATION"),
    }
    checks.append((
        "TM-HANKEL",
        "Hankel divisor block splits T, F, and C exactly; no physical lift",
        all(
            has_status(index, claim, status)
            and normative.get(claim, {}).get("item_type") == item_type
            and normative.get(claim, {}).get("status") == status
            and normative.get(claim, {}).get("layer") == "L1"
            and normative.get(claim, {}).get("gate_ids") == ""
            and index.get(claim, {}).get("canon_section")
            == "9. The photon and the electron"
            and index.get(claim, {}).get("evidence") == hankel_path
            and evidence.get(claim, {}).get("evidence_id") == "EV-" + claim
            and evidence.get(claim, {}).get("evidence_kind") == "PUBLIC_PROBE"
            and evidence.get(claim, {}).get("location") == hankel_path
            and evidence.get(claim, {}).get("sha256") == hankel_digest
            and evidence.get(claim, {}).get("hash_mode")
            == "bundle-manifest-sha256-v1"
            and evidence.get(claim, {}).get("architecture_requirement")
            == "two-architecture"
            and all(row["item_id"] != claim for row in dependencies)
            and all(row["depends_on"] != claim for row in dependencies)
            and claim not in programs
            and all(
                row["owner_item_id"] != claim for row in gates.values()
            )
            for claim, (status, item_type) in hankel_rows.items()
        )
        and scope_contains_all(
            index, "TM-HANKEL-K2-TRANSFER",
            ("h(s)=-9+s(3D+3E+F)-s^2(A+D)^2/(3+sA)-s^2(B+E)^2/(3+sB)"
             "<=-9+7s<=-2<0",
             "NEG 2 ZERO 0 POS 2",
             "universal at k=2"),
        )
        and scope_contains_all(
            index, "TM-HANKEL-K3-UNIVERSAL-TRANSFER",
            ("147965=5.101.293",
             "NEG 5 ZERO 0 POS 3",
             "determinant -3840",
             "157 extremal triples with n<=200000",
             "unique nonbalanced case"),
        )
        and index["TM-HANKEL-K3-UNIVERSAL-TRANSFER"]["falsifier"]
        .startswith("fired:")
        and scope_contains_all(
            index, "TM-HANKEL-K3-TWO-SCALAR-CLASSIFICATION",
            ("32398/110/260",
             "518368/1760/4160",
             "522462 tables",
             "FAIL iff det G_6<0 and det K<=0",
             "computation grade"),
        )
        and scope_contains_all(
            index, "TM-HANKEL-K3-QUADRATIC-INVARIANT-SUFFICIENCY",
            ("3584 buckets of which exactly 58 are mixed",
             "88352 buckets with zero mixed",
             "factors through the quadratic invariant map",
             "(2^19+3.2^12+2.2^7)/6=89472",
             "merging 1120 orbit distinctions",
             "no claim is made that the deciding function is itself a "
             "polynomial of degree two"),
        ),
    ))

    rapidity_path = "probes/P-ARITH-RAPIDITY-1"
    rapidity_digest = (
        "e053d4950e368c7815f6df723b4dde316c6bb5a17d4f8d62f8fcee8eeb105fda"
    )
    rapidity_rows = {
        "ARITHMETIC-RAPIDITY-DECOMPOSITION": ("T", "THEOREM"),
        "SPLIT-PRIME-RAPIDITY-CLASS": ("T", "THEOREM"),
        "SPLIT-PRIME-RAPIDITY-CONSTRUCTION-AGREEMENT": ("C", "COMPUTATION"),
    }
    checks.append((
        "RAPIDITY",
        "arithmetic rapidity rows split T and C exactly; no physical lift",
        all(
            has_status(index, claim, status)
            and normative.get(claim, {}).get("item_type") == item_type
            and normative.get(claim, {}).get("status") == status
            and normative.get(claim, {}).get("layer") == "L1"
            and normative.get(claim, {}).get("gate_ids") == ""
            and index.get(claim, {}).get("canon_section")
            == "10. Relativity as counting"
            and index.get(claim, {}).get("evidence") == rapidity_path
            and evidence.get(claim, {}).get("evidence_id") == "EV-" + claim
            and evidence.get(claim, {}).get("evidence_kind") == "PUBLIC_PROBE"
            and evidence.get(claim, {}).get("location") == rapidity_path
            and evidence.get(claim, {}).get("sha256") == rapidity_digest
            and evidence.get(claim, {}).get("hash_mode")
            == "bundle-manifest-sha256-v1"
            and evidence.get(claim, {}).get("architecture_requirement")
            == "two-architecture"
            and all(row["item_id"] != claim for row in dependencies)
            and all(
                row["item_id"] in (
                    *INDEPENDENCE_ROWS,
                    "J-IDEAL-RAPIDITY-CHARACTER-LIFT",
                    "RAPIDITY-GOLDEN-LADDER",
                )
                for row in dependencies
                if row["depends_on"] == claim
            )
            and claim not in programs
            and all(
                row["owner_item_id"] != claim for row in gates.values()
            )
            for claim, (status, item_type) in rapidity_rows.items()
        )
        and scope_contains_all(
            index, "ARITHMETIC-RAPIDITY-DECOMPOSITION",
            ("t^2-s^2=N(x)",
             "null locus is empty",
             "dense, not discrete",
             "Lucas always the time reading",
             "with no conflict"),
        )
        and scope_contains_all(
            index, "SPLIT-PRIME-RAPIDITY-CLASS",
            ("R(p)={r,-r}",
             "|Tr(w)|=L_(2m)",
             "class zero exactly",
             "not merely 0 modulo the lattice"),
        )
        and scope_contains_all(
            index, "SPLIT-PRIME-RAPIDITY-CONSTRUCTION-AGREEMENT",
            ("all 146 of them",
             "R1(p)=R2(p) in every case",
             "70 pairs agreeing oriented and 76 only after conjugation",
             "computation grade"),
        ),
    ))

    independence_path = "probes/P-SPLIT-PRIME-INDEPENDENCE-1"
    independence_digest = (
        "8c293da2f9b3af5d96e20fea472be19676d18328350bb2c0800ed68de2e7ffbf"
    )
    independence_rows = {
        "SPLIT-PRIME-RAPIDITY-INDEPENDENCE": ("T", "THEOREM"),
        "REDUCED-SPLIT-GENERATOR-HEIGHT": ("T", "THEOREM"),
    }
    checks.append((
        "INDEPENDENCE",
        "split-prime independence rows stay exact L1 arithmetic with no "
        "analytic or ordering lift",
        all(
            has_status(index, claim, status)
            and normative.get(claim, {}).get("item_type") == item_type
            and normative.get(claim, {}).get("status") == status
            and normative.get(claim, {}).get("layer") == "L1"
            and normative.get(claim, {}).get("gate_ids") == ""
            and index.get(claim, {}).get("canon_section")
            == "10. Relativity as counting"
            and index.get(claim, {}).get("evidence") == independence_path
            and evidence.get(claim, {}).get("evidence_id") == "EV-" + claim
            and evidence.get(claim, {}).get("evidence_kind") == "PUBLIC_PROBE"
            and evidence.get(claim, {}).get("location") == independence_path
            and evidence.get(claim, {}).get("sha256") == independence_digest
            and evidence.get(claim, {}).get("hash_mode")
            == "bundle-manifest-sha256-v1"
            and evidence.get(claim, {}).get("architecture_requirement")
            == "two-architecture"
            and claim not in programs
            and all(
                row["owner_item_id"] != claim for row in gates.values()
            )
            for claim, (status, item_type) in independence_rows.items()
        )
        and scope_contains_all(
            index, "SPLIT-PRIME-RAPIDITY-INDEPENDENCE",
            ("forces every m_i=0",
             "unique factorisation of fractional ideals",
             "the statement is orientation-free",
             "NOT about the distribution of primes as p grows"),
        )
        and scope_contains_all(
            index, "REDUCED-SPLIT-GENERATOR-HEIGHT",
            ("open fundamental half-period",
             "both real embeddings exceed one",
             "h(pi) = (1/2) log p",
             "the height is unbounded at fixed class"),
        ),
    ))

    separation = "SPLIT-PRIME-RAPIDITY-QUANTITATIVE-SEPARATION"
    fejer = "SPLIT-RAPIDITY-FEJER-GRAM-BOUND"
    separation_path = "probes/P-SPLIT-RAPIDITY-QUANTITATIVE-SEPARATION-1"
    separation_digest = (
        "ea59451558e513f16ee471b3bf9ccddfa0bc6e1cabbed70d27809cedfeb25ecb"
    )
    separation_dependencies = {
        (row["depends_on"], row["relation"])
        for row in dependencies if row["item_id"] == separation
    }
    fejer_dependencies = {
        (row["depends_on"], row["relation"])
        for row in dependencies if row["item_id"] == fejer
    }
    checks.append((
        "SEPARATION",
        "quantitative separation and finite Fejer rows stay exact, distinct, and normalization-fenced",
        all(
            has_status(index, claim, "T")
            and normative.get(claim, {}).get("item_type") == "THEOREM"
            and normative.get(claim, {}).get("status") == "T"
            and normative.get(claim, {}).get("layer") == "L1"
            and normative.get(claim, {}).get("gate_ids") == ""
            and index.get(claim, {}).get("canon_section")
            == "10. Relativity as counting"
            and index.get(claim, {}).get("evidence") == separation_path
            and evidence.get(claim, {}).get("evidence_id") == "EV-" + claim
            and evidence.get(claim, {}).get("evidence_kind") == "PUBLIC_PROBE"
            and evidence.get(claim, {}).get("location") == separation_path
            and evidence.get(claim, {}).get("sha256") == separation_digest
            and evidence.get(claim, {}).get("hash_mode")
            == "bundle-manifest-sha256-v1"
            and evidence.get(claim, {}).get("architecture_requirement")
            == "two-architecture"
            and claim not in programs
            and all(row["owner_item_id"] != claim for row in gates.values())
            for claim in (separation, fejer)
        )
        and evidence[separation]["sha256"] == evidence[fejer]["sha256"]
        and separation_dependencies == {
            ("ARITHMETIC-RAPIDITY-DECOMPOSITION", "REQUIRES"),
            ("SPLIT-PRIME-RAPIDITY-CLASS", "REQUIRES"),
            ("SPLIT-PRIME-RAPIDITY-INDEPENDENCE", "REQUIRES"),
            ("REDUCED-SPLIT-GENERATOR-HEIGHT", "REQUIRES"),
        }
        and fejer_dependencies == {(separation, "REQUIRES")}
        and scope_contains_all(
            index, separation,
            ("finite nonzero integer vector c=(c_p)",
             "signed norm +p",
             "|D_c| in sqrt5 Z_{>0} for even n",
             "|D_c| in Z_{>0} for odd n",
             "d_L=0.0011737895036417",
             "d_2L=0.4800380355559618",
             "valid determinant may be negative",
             "selects no global orientation or parity sheet",
             "minimizing signed channel is unique up to simultaneous conjugation"),
        )
        and all(
            phrase.lower() in index[separation]["falsifier"].lower()
            for phrase in (
                "|D_c| in sqrt5 Z_{>0} for even n",
                "|D_c| in Z_{>0} for odd n",
                "negative D_c",
                "-182sqrt5",
            )
        )
        and scope_contains_all(
            index, fejer,
            ("finite set A of distinct oriented split prime-power addresses",
             "delta_A>=asinh(1/(2X))",
             "character chi_h(a)",
             "ordinary signed-channel rungs are |b|=22 and |b|=182",
             "doubled-phase falsifier is the effective vector (2,2)",
             "phi^-3 x^2",
             "trace 29",
             "numerator 841",
             "correct P(c)^2 budget",
             "no Hecke"),
        )
        and all(
            phrase.lower() in index[fejer]["falsifier"].lower()
            for phrase in (
                "two distinct declared finite addresses collide",
                "operator-norm bound",
                "singleton Gram matrix differs from [1]",
                "normalization STOP",
            )
        ),
    ))

    qdd_path = "reproduce/qdd-route-a"
    checks.append((
        "QDD-ROUTE-A",
        "the QDD Route A algebra stays three L1 theorems on two-architecture evidence while the retired composite is split into an algebraic D and a separate apparatus O; no physical gate or L6 row exists",
        all(
            has_status(index, claim, "T")
            and normative.get(claim, {}).get("layer") == "L1"
            and normative.get(claim, {}).get("gate_ids") == ""
            and index.get(claim, {}).get("evidence") == qdd_path
            and evidence.get(claim, {}).get("architecture_requirement")
            == "two-architecture"
            for claim in ("QDD-ALGEBRAIC-FACTORIZATION", "QDD-PROJECTOR-PAIR-TR4",
                          "QDD-QCARRIER-DIAGONAL-BOUNDARY")
        )
        and qdd_current_split
        and "QDD-BORN-READOUT-MEASURE" not in index
        and "DEF-BRIDGE-QDD-TR4-EFFECT-SELECTION" not in normative
        and "GATE-L1-L6-QDD-BORN-READOUT" not in gates
        and normative.get("DEF-QDD-PROJECTOR-LOW", {}).get("item_type")
        == "DEFINITION"
        and scope_contains_all(index, "QDD-ALGEBRAIC-FACTORIZATION",
                               ("ordered algebraic projector pair",
                                "algebraic branch-weight pairing",
                                "not its definition source",
                                "does not mathematically force",
                                "supplies no independent readout, physical effect or apparatus"))
        and scope_contains_all(index, "QDD-PROJECTOR-PAIR-TR4",
                               ("no uniqueness-from-j",))
        and scope_contains_all(index, "QDD-QCARRIER-DIAGONAL-BOUNDARY",
                               ("a_dagger = a_t = v v^t",
                                "no physical central phase"))
        and "GATE-L1-L5-QDD-INSTRUMENT-APPARATUS" not in gates
        and "GATE-L1-L6-QDD-BORN-READOUT" not in gates,
    ))

    nonselection = "QDD-INSTRUMENT-NONSELECTION"
    nonselection_path = "probes/P-QDD-INSTRUMENT-NONSELECTION-1"
    nonselection_digest = (
        "d49930ce735413cb58601d85d697b6dc049e5571f50cdf16d837206db26727e2"
    )
    nonselection_dependencies = {
        (row["depends_on"], row["relation"])
        for row in dependencies if row["item_id"] == nonselection
    }
    apparatus_dependencies = {
        (row["depends_on"], row["relation"])
        for row in dependencies if row["item_id"] == "QDD-INSTRUMENT-APPARATUS"
    }
    checks.append((
        "QDD-NONSELECTION",
        "the L4 fibre theorem remains exact while the apparatus O is sharpened to independent selection of law and equality plus realized-event sampling",
        has_status(index, nonselection, "T")
        and normative.get(nonselection, {}).get("item_type") == "THEOREM"
        and normative.get(nonselection, {}).get("status") == "T"
        and normative.get(nonselection, {}).get("layer") == "L4"
        and normative.get(nonselection, {}).get("gate_ids") == ""
        and index.get(nonselection, {}).get("evidence") == nonselection_path
        and evidence.get(nonselection, {}).get("evidence_kind") == "PUBLIC_PROBE"
        and evidence.get(nonselection, {}).get("location") == nonselection_path
        and evidence.get(nonselection, {}).get("sha256") == nonselection_digest
        and evidence.get(nonselection, {}).get("architecture_requirement")
        == "two-architecture"
        and nonselection not in programs
        and all(row["owner_item_id"] != nonselection for row in gates.values())
        and nonselection_dependencies == set()
        and apparatus_dependencies == {
            ("DEF-QDD-PROJECTOR-LOW", "REQUIRES"),
            ("DEF-QDD-PROJECTOR-HIGH", "REQUIRES"),
            ("DEF-QDD-GRAM", "REQUIRES"),
            ("DEF-DECODER-COMPLETION-CONTRACT", "REQUIRES"),
        }
        and scope_contains_all(
            index, nonselection,
            ("one branchwise O(G,Q) x O(G,Q) orbit",
             "injects Q into physically distinct post-state instrument classes",
             "not an instrument-selection principle",
             "mathematical positive-square-root section",
             "no L5 realized-event stream",
             "no L6 measure",
             "SAMPLING NOT PROVIDED rather than SAMPLING IMPOSSIBLE"),
        )
        and scope_contains_all(
            index, "QDD-INSTRUMENT-APPARATUS",
            ("sole owner of the physical debt split from QUADRATIC-DECODER-DATA",
             "transferred but not satisfied",
             "all remain UNRESOLVED",
             "O2 is the compatible conjunction of QDD-TERMINAL-EVENT-SEMANTICS",
             "QDD-INSTRUMENT-CLASS-COMPLETENESS",
             "O1 remains the typed realized-event and sampling obligation",
             "SAMPLING NOT PROVIDED",
             "rather than impossible"),
        )
        and has_status(index, "QDD-INSTRUMENT-APPARATUS", "O")
        and qdd_current_split,
    ))

    qdd_v59_rows = (
        "QDD-J-AFFINE-APPARATUS-NONSELECTION",
        "QDD-J-CENTRALIZER-NONSELECTION",
        "QDD-J-TERMINALITY-SELECTION",
        "QDD-FRESH-RECORD-EXTENSION",
        "QDD-PROJECTIVE-IDEMPOTENCE-NONIMPLICATION",
        "QDD-RECORD-SUFFICIENCY-TERMINALITY",
        "QDD-RECORD-COMPLETE-LUEDER-SELECTION",
        "QDD-LAW-NATURALITY-VS-GAUGE-BOUNDARY",
    )
    qdd_v59_evidence = {
        qdd_v59_rows[0]: (
            "probes/P-QDD-J-AFFINE-APPARATUS-1",
            "c533652710c6a3cea58ee40473233b46ab64cdfbae4f0a6ee17e6733ecc035d2",
        ),
        qdd_v59_rows[1]: (
            "probes/P-QDD-J-CENTRALIZER-TERMINALITY-1",
            "f13fbcd080aa618c6896fe00c0b2157514b97beeb446cd1b49f8928e6789cd3e",
        ),
        qdd_v59_rows[2]: (
            "probes/P-QDD-J-CENTRALIZER-TERMINALITY-1",
            "f13fbcd080aa618c6896fe00c0b2157514b97beeb446cd1b49f8928e6789cd3e",
        ),
        qdd_v59_rows[3]: (
            "probes/P-QDD-FRESH-RECORD-NOFEEDBACK-2",
            "9b2cf5cfeb18f6c1b68a526b8d6f88c9e4b1ddfc72a3576e401357e2f4336b49",
        ),
        qdd_v59_rows[4]: (
            "probes/P-QDD-FRESH-RECORD-NOFEEDBACK-2",
            "9b2cf5cfeb18f6c1b68a526b8d6f88c9e4b1ddfc72a3576e401357e2f4336b49",
        ),
        qdd_v59_rows[5]: (
            "probes/P-QDD-FRESH-RECORD-NOFEEDBACK-2",
            "9b2cf5cfeb18f6c1b68a526b8d6f88c9e4b1ddfc72a3576e401357e2f4336b49",
        ),
        qdd_v59_rows[6]: (
            "probes/P-QDD-RECORD-COMPLETE-STABILIZER-1",
            "d8f756317e7394c41a589fa69143bb4ac7d32c69ccddfb4cfe8fa2f5257a6322",
        ),
        qdd_v59_rows[7]: (
            "probes/P-QDD-RECORD-NATURALITY-FORK-1",
            "135951e6ad63f7ef0825ce63557e22e7e8a1301c0ca58c583b7756782fc2673d",
        ),
    }
    qdd_v59_dependencies = {
        qdd_v59_rows[0]: {
            ("QDD-INSTRUMENT-NONSELECTION", "REQUIRES"),
            ("QDD-INSTRUMENT-APPARATUS", "BOUNDED_BY"),
        },
        qdd_v59_rows[1]: {
            ("QDD-INSTRUMENT-NONSELECTION", "REQUIRES"),
            ("QDD-INSTRUMENT-APPARATUS", "BOUNDED_BY"),
        },
        qdd_v59_rows[2]: {
            (qdd_v59_rows[1], "REQUIRES"),
            ("QDD-INSTRUMENT-APPARATUS", "BOUNDED_BY"),
        },
        qdd_v59_rows[3]: {
            ("QDD-INSTRUMENT-NONSELECTION", "REQUIRES"),
            ("QDD-INSTRUMENT-APPARATUS", "BOUNDED_BY"),
        },
        qdd_v59_rows[4]: {
            (qdd_v59_rows[3], "REQUIRES"),
            (qdd_v59_rows[1], "REQUIRES"),
            ("QDD-INSTRUMENT-APPARATUS", "BOUNDED_BY"),
        },
        qdd_v59_rows[5]: {
            (qdd_v59_rows[3], "REQUIRES"),
            ("QDD-INSTRUMENT-APPARATUS", "BOUNDED_BY"),
        },
        qdd_v59_rows[6]: {
            (qdd_v59_rows[1], "REQUIRES"),
            ("QDD-INSTRUMENT-APPARATUS", "BOUNDED_BY"),
        },
        qdd_v59_rows[7]: {
            (qdd_v59_rows[6], "REQUIRES"),
            ("QDD-INSTRUMENT-APPARATUS", "BOUNDED_BY"),
        },
    }
    checks.append((
        "QDD-SELECTION-BOUNDARY",
        "eight public L4 QDD rows register exact nonselectors and conditional selectors while O2, O1, the weaker-hypothesis strengthening, and sampling stay open",
        all(
            has_status(index, claim, "T")
            and normative.get(claim, {}).get("item_type") == "THEOREM"
            and normative.get(claim, {}).get("status") == "T"
            and normative.get(claim, {}).get("layer") == "L4"
            and normative.get(claim, {}).get("gate_ids") == ""
            and index.get(claim, {}).get("evidence")
            == qdd_v59_evidence[claim][0]
            and evidence.get(claim, {}).get("evidence_kind") == "PUBLIC_PROBE"
            and evidence.get(claim, {}).get("location")
            == qdd_v59_evidence[claim][0]
            and evidence.get(claim, {}).get("sha256")
            == qdd_v59_evidence[claim][1]
            and evidence.get(claim, {}).get("architecture_requirement")
            == "two-architecture"
            and claim not in programs
            and {
                (row["depends_on"], row["relation"])
                for row in dependencies if row["item_id"] == claim
            } == qdd_v59_dependencies[claim]
            and all(row["owner_item_id"] != claim for row in gates.values())
            for claim in qdd_v59_rows
        )
        and scope_contains_all(
            index, qdd_v59_rows[0],
            ("complete frozen target-independent affine family",
             "four registered sign classes",
             "self-adjoint involutivity leaves a in {1,4}",
             "SAMPLING NOT PROVIDED"),
        )
        and scope_contains_all(
            index, qdd_v59_rows[1],
            ("Q R_k direct-sum Q C_k direct-sum Q J_k",
             "infinitely many registered sign classes",
             "four algebraic members and two sign classes",
             "k=2 gives P_2=E_low and Q_2=E_high"),
        )
        and scope_contains_all(
            index, qdd_v59_rows[2],
            ("fresh-pointer ray terminality forces",
             "strict representative idempotence",
             "neither terminality nor strict idempotence is derived or adopted"),
        )
        and scope_contains_all(
            index, qdd_v59_rows[3],
            ("P^2=P=P^sharp", "TP=PT=0", "QT=TQ=T",
             "N HIGH outcomes leave conditioned state T^N v",
             "these protocol records are not D_clock"),
        )
        and scope_contains_all(
            index, qdd_v59_rows[4],
            ("T_*=R_k-C_k", "T_*^2=Q_k",
             "distinct first and second conditioned rays"),
        )
        and scope_contains_all(
            index, qdd_v59_rows[5],
            ("dim(QV)>=2", "TP=PT=0", "QT=TQ=T",
             "weaker one-sided hypotheses", "T^2=+T or T^2=-T"),
        )
        and scope_contains_all(
            index, qdd_v59_rows[6],
            ("strict microscopic law naturality",
             "T rho(g)=rho(g) T for every g in Gamma_k",
             "fails 16 of 24 Gamma_k tests"),
        )
        and scope_contains_all(
            index, qdd_v59_rows[7],
            ("Aut(S_4)=Inn(S_4)",
             "48 algebraic members and 24 registered sign classes",
             "commutes with four of 24 Gamma_k elements",
             "failing twenty strict naturality squares",
             "new +/-S_4 orbit equality"),
        )
        and evidence["QDD-INSTRUMENT-APPARATUS"]["sha256"]
        == scope_sha256(index, "QDD-INSTRUMENT-APPARATUS")
        and has_status(index, "QDD-INSTRUMENT-APPARATUS", "O")
        and qdd_current_split
        and "QDD-RELABELING-CEILING" not in normative
        and "QDD-CLASS-IDEMPOTENCE-SELECTION" not in normative,
    ))

    suzuki = "SUZUKI-LOCAL-CAPACITY-NOGO"
    suzuki_path = "probes/P-SUZUKI-LOCAL-CAPACITY-NOGO-1"
    suzuki_digest = (
        "0891418a788e7e2d1d4795af8883020dbcd78c7ea2f9f9fefb41b055131deb65"
    )
    suzuki_window = "SUZUKI-PRIME-FREE-WINDOW"
    suzuki_count = "SUZUKI-EVENT-COUNT"
    suzuki_rows = (suzuki, suzuki_window, suzuki_count)
    suzuki_dependencies = {
        (row["depends_on"], row["relation"])
        for row in dependencies if row["item_id"] in suzuki_rows
    }
    checks.append((
        "SUZUKI-CAPACITY-NOGO",
        "the L1 no-go complex for the Suzuki completion capacity enters at T with two finite C computations, all pinned to the two-architecture public probe bundle and free of dependency, gate and frontier ownership",
        has_status(index, suzuki, "T")
        and has_status(index, suzuki_window, "C")
        and has_status(index, suzuki_count, "C")
        and normative.get(suzuki, {}).get("item_type") == "THEOREM"
        and normative.get(suzuki, {}).get("status") == "T"
        and normative.get(suzuki, {}).get("layer") == "L1"
        and normative.get(suzuki, {}).get("gate_ids") == ""
        and normative.get(suzuki_window, {}).get("item_type") == "COMPUTATION"
        and normative.get(suzuki_count, {}).get("item_type") == "COMPUTATION"
        and all(index.get(row, {}).get("evidence") == suzuki_path for row in suzuki_rows)
        and all(evidence.get(row, {}).get("evidence_kind") == "PUBLIC_PROBE" for row in suzuki_rows)
        and all(evidence.get(row, {}).get("location") == suzuki_path for row in suzuki_rows)
        and all(evidence.get(row, {}).get("sha256") == suzuki_digest for row in suzuki_rows)
        and all(
            evidence.get(row, {}).get("architecture_requirement") == "two-architecture"
            for row in suzuki_rows
        )
        and all(row not in programs for row in suzuki_rows)
        and all(row["owner_item_id"] not in suzuki_rows for row in gates.values())
        and suzuki_dependencies == set()
        and scope_contains_all(
            index, suzuki,
            ("orthogonal increments",
             "the nonnegative ramp class is empty",
             "at the first event q = 2",
             "separately indefinite",
             "the norm is exactly one",
             "nonlocal in t",
             "no J-coupling, no L2--L6 lift"),
        )
        and scope_contains_all(
            index, suzuki_window,
            ("[1/128, 45/64]", "zero undecided leaves"),
        )
        and scope_contains_all(
            index, suzuki_count,
            ("78734", "two independent counting paths"),
        ),
    ))

    tt_moment = "TT-VECTOR-MOMENT-UNDERDETERMINATION"
    tt_moment_path = "probes/P-TT-VECTOR-MOMENT-UNDERDETERMINATION-1"
    tt_moment_digest = (
        "302e0403e5b1a0027555a39c33dddbe55e17b6ec76ee9292da8407630d5b10bf"
    )
    tt_moment_dependencies = {
        (row["depends_on"], row["relation"])
        for row in dependencies if row["item_id"] == tt_moment
    }
    checks.append((
        "TT-MOMENT",
        "the exact L1 moment family proves fourth-order underdetermination while state normalization remains O and no numerical tensor ratio is produced",
        has_status(index, tt_moment, "T")
        and normative.get(tt_moment, {}).get("item_type") == "THEOREM"
        and normative.get(tt_moment, {}).get("layer") == "L1"
        and normative.get(tt_moment, {}).get("gate_ids") == ""
        and evidence.get(tt_moment, {}).get("evidence_kind") == "PUBLIC_PROBE"
        and evidence.get(tt_moment, {}).get("location") == tt_moment_path
        and evidence.get(tt_moment, {}).get("sha256") == tt_moment_digest
        and evidence.get(tt_moment, {}).get("architecture_requirement")
        == "two-architecture"
        and tt_moment_dependencies == {
            ("TT-SQUARING-DECODER", "BOUNDED_BY"),
            ("POL-READ", "BOUNDED_BY"),
            ("TT-VECTOR-STATE-NORMALIZATION", "BOUNDED_BY"),
        }
        and scope_contains_all(
            index, tt_moment,
            ("every polynomial functional of total degree at most three",
             "minimal separating degree is exactly four",
             "no gaussian or wick closure exists at fixed modulus",
             "no normalization", "r_t(k)", "l2-l6 lift"),
        )
        and has_status(index, "TT-VECTOR-STATE-NORMALIZATION", "O")
        and scope_contains_all(
            index, "TT-VECTOR-STATE-NORMALIZATION",
            ("fourth-moment data", "explicit non-gaussian closure rule",
             "neither that choice nor a numerical r_t(k)"),
        )
        and evidence["TT-VECTOR-STATE-NORMALIZATION"]["sha256"]
        == scope_sha256(index, "TT-VECTOR-STATE-NORMALIZATION")
        and tt_moment not in programs
        and all(row["owner_item_id"] != tt_moment for row in gates.values()),
    ))

    qdd_u_channel = "QDD-U-INDUCED-CHANNEL"
    qdd_u_finite = "QDD-U-INDUCED-FINITE-NONSELECTION"
    qdd_u_path = "probes/P-QDD-INSTRUMENT-U-INDUCED-1"
    qdd_u_digest = (
        "17f5e001c9fce5360b021781fbb3910ed5045a5e9666ab7624a90e7880eae60f"
    )
    qdd_u_dependencies = {
        claim: {
            (row["depends_on"], row["relation"])
            for row in dependencies if row["item_id"] == claim
        }
        for claim in (qdd_u_channel, qdd_u_finite)
    }
    checks.append((
        "QDD-U",
        "the registered update supplies an exact L1 channel and a complete finite multi-layer nonselection computation while apparatus selection and sampling remain O and STOP",
        has_status(index, qdd_u_channel, "T")
        and has_status(index, qdd_u_finite, "C")
        and normative.get(qdd_u_channel, {}).get("item_type") == "THEOREM"
        and normative.get(qdd_u_channel, {}).get("layer") == "L1"
        and normative.get(qdd_u_finite, {}).get("item_type") == "COMPUTATION"
        and normative.get(qdd_u_finite, {}).get("layer") == "MULTI"
        and all(
            evidence.get(claim, {}).get("evidence_kind") == "PUBLIC_PROBE"
            and evidence.get(claim, {}).get("location") == qdd_u_path
            and evidence.get(claim, {}).get("sha256") == qdd_u_digest
            and evidence.get(claim, {}).get("architecture_requirement")
            == "two-architecture"
            for claim in (qdd_u_channel, qdd_u_finite)
        )
        and qdd_u_dependencies[qdd_u_channel] == {
            ("DEF-AUTONOMOUS-STATE", "REQUIRES"),
            ("DEF-QDD-BALANCED-PISTON", "REQUIRES"),
            ("QDD-INSTRUMENT-APPARATUS", "BOUNDED_BY"),
        }
        and qdd_u_dependencies[qdd_u_finite] == {
            (qdd_u_channel, "REQUIRES"),
            ("DEF-QDD-BRANCH-WEIGHT-PAIRING", "REQUIRES"),
            ("DEF-QDD-MATTER-RECORD", "REQUIRES"),
            ("QDD-INSTRUMENT-NONSELECTION", "REQUIRES"),
            ("QDD-INSTRUMENT-APPARATUS", "BOUNDED_BY"),
        }
        and scope_contains_all(
            index, qdd_u_channel,
            ("five generator fibers are exactly", "delay one",
             "exact bidirectional algebraic channel structure only",
             "no physical measurement"),
        )
        and scope_contains_all(
            index, qdd_u_finite,
            ("180 two-cell maps", "900 record-delay pairs",
             "info is true for exactly 150", "functional=0",
             "post-undefined-or-zero=900", "evaluated/member/outside=0/0/0",
             "multi-layer scope", "no limit", "sampling impossibility"),
        )
        and scope_contains_all(
            index, "QDD-INSTRUMENT-APPARATUS",
            ("pure-record, COMM-SAT, finite-memory and 22-context carry-bank results",
             "delimit frozen mathematical classes",
             "adopt no physical effect, instrument, carrier, complete family",
             "do not close or partially satisfy this row"),
        )
        and evidence["QDD-INSTRUMENT-APPARATUS"]["sha256"]
        == scope_sha256(index, "QDD-INSTRUMENT-APPARATUS")
        and has_status(index, "QDD-INSTRUMENT-APPARATUS", "O")
        and programs.get("QDD-INSTRUMENT-APPARATUS", {}).get("work_state")
        == "STOP",
    ))

    field_cut = "FIELD-ZERO-NONZERO-MULTIPLICATIVE-CUT"
    field_cut_path = "probes/P-FIELD-ZERO-NONZERO-CUT-1"
    field_cut_digest = (
        "baf65d43b2016d629f1442dea3e20191631e5b0f2729e8020eb6d36e9fe3384c"
    )
    checks.append((
        "FIELD-CUT",
        "the unique total multiplicative field bit is exactly the two oriented zero/nonzero cuts and remains independent of QDD and fifth-prime selection",
        has_status(index, field_cut, "T")
        and normative.get(field_cut, {}).get("item_type") == "THEOREM"
        and normative.get(field_cut, {}).get("layer") == "L1"
        and evidence.get(field_cut, {}).get("location") == field_cut_path
        and evidence.get(field_cut, {}).get("sha256") == field_cut_digest
        and evidence.get(field_cut, {}).get("architecture_requirement")
        == "two-architecture"
        and all(row["item_id"] != field_cut for row in dependencies)
        and scope_contains_all(
            index, field_cut,
            ("for every field f", "a={0} with b=or",
             "a=f^x with b=and", "b is unique",
             "qr/xnor and nqr/xor", "no five-specific selection",
             "no qdd equation", "dependency edge"),
        )
        and field_cut not in programs
        and all(row["owner_item_id"] != field_cut for row in gates.values()),
    ))

    tensor_path = "probes/P-QPAIR-SYM2-TENSOR-DEFECT-1"
    tensor_digest = (
        "ae345af394adf1693b5515d038743dc3f3697fa0c55340972eb979682538fed5"
    )
    tensor_rows = (
        "QPAIR-PRODUCT-COMPOSITION",
        "QPAIR-CROSS-SECTOR-NONDESCENT",
        "QPAIR-SYM2-TENSOR-DEFECT",
    )
    checks.append((
        "QPAIR-TENSOR",
        "matched quadratic sectors compose on product vectors, cross sectors fail factor-gauge descent, and the symmetric target has the exact determinant 9+1 defect",
        all(
            has_status(index, claim, "T")
            and normative.get(claim, {}).get("item_type") == "THEOREM"
            and normative.get(claim, {}).get("layer") == "L1"
            and evidence.get(claim, {}).get("location") == tensor_path
            and evidence.get(claim, {}).get("sha256") == tensor_digest
            and evidence.get(claim, {}).get("architecture_requirement")
            == "two-architecture"
            and all(row["item_id"] != claim for row in dependencies)
            and claim not in programs
            for claim in tensor_rows
        )
        and scope_contains_all(
            index, tensor_rows[0],
            ("natural, associative, symmetric and unital",
             "exact for product vectors", "no surjectivity"),
        )
        and scope_contains_all(
            index, tensor_rows[1],
            ("c(lambda)/lambda", "lambda/c(lambda)",
             "zeta_5^3 and zeta_5^2", "no fifth-prime physical"),
        )
        and scope_contains_all(
            index, tensor_rows[2],
            ("10=9+1", "product squares span exactly",
             "((ad-bc)/2)kappa", "not a bell state",
             "not a claim that a full hermitian-plus-symmetric defect"),
        )
        and all(row["owner_item_id"] not in tensor_rows for row in gates.values()),
    ))

    qpair_path = "probes/P-QPAIR-C4-2I-MINIMALITY-1"
    qpair_digest = (
        "6f1d5a5859a193cb68eb53f6ed58f5da21b25f3c0084c3875eede690317ea592"
    )
    qpair_t = (
        "QPAIR-HERM-INTEGER-NONDESCENT",
        "QPAIR-TRANSPOSE-FIBER-REDUNDANCY",
        "QPAIR-TYPED-MIXED-C4-CLOSURE",
        "QPAIR-SYM2-2I-IRREDUCIBLE",
        "QPAIR-MINIMAL-2I-CLOSURE-OF-HERM-UNDER-MIXED-C4",
    )
    qpair_f = (
        "QPAIR-2I-ONLY-PAIR-FORCING",
        "QPAIR-MIXED-C4-NORMALIZES-2I",
    )
    qpair_definitions = {
        "DEF-QPAIR-SPIN-CARRIER",
        "DEF-QPAIR-HERM-SLOT",
        "DEF-QPAIR-SYM-SLOT",
        "DEF-QPAIR-MIXED-C4",
        "DEF-QPAIR-ADMISSIBLE-LINEAR-CLASS",
    }
    qpair_dependency_map = {
        item: {
            (row["depends_on"], row["relation"])
            for row in dependencies if row["item_id"] == item
        }
        for item in qpair_definitions | set(qpair_t) | set(qpair_f)
    }
    checks.append((
        "QPAIR-C4-2I",
        "the independent integral carrier has exact mixed closure and relative 2I minimality while set redundancy, 2I-only pair forcing, and normalization firewalls remain explicit",
        all(has_status(index, claim, "T") for claim in qpair_t)
        and all(has_status(index, claim, "F") for claim in qpair_f)
        and all(
            normative.get(item, {}).get("item_type") == "DEFINITION"
            and normative.get(item, {}).get("layer") == "L1"
            for item in qpair_definitions
        )
        and all(
            evidence.get(claim, {}).get("location") == qpair_path
            and evidence.get(claim, {}).get("sha256") == qpair_digest
            and evidence.get(claim, {}).get("architecture_requirement")
            == "two-architecture"
            and normative.get(claim, {}).get("layer") == "L1"
            for claim in qpair_t + qpair_f
        )
        and qpair_dependency_map["QPAIR-SYM2-2I-IRREDUCIBLE"] == {
            ("COLOR-CORE-2I", "REQUIRES"),
            ("COLOR-GOLDEN-TABLE", "REQUIRES"),
            ("COLOR-INTEGRAL-LIFT", "REQUIRES"),
            ("DEF-ACTION-LAYERS", "REQUIRES"),
        }
        and qpair_dependency_map[
            "QPAIR-MINIMAL-2I-CLOSURE-OF-HERM-UNDER-MIXED-C4"
        ] == {
            ("QPAIR-SYM2-2I-IRREDUCIBLE", "REQUIRES"),
            ("DEF-QPAIR-SPIN-CARRIER", "REQUIRES"),
            ("DEF-QPAIR-HERM-SLOT", "REQUIRES"),
            ("DEF-QPAIR-SYM-SLOT", "REQUIRES"),
            ("DEF-QPAIR-MIXED-C4", "REQUIRES"),
            ("DEF-QPAIR-ADMISSIBLE-LINEAR-CLASS", "REQUIRES"),
            ("DEF-ACTION-LAYERS", "REQUIRES"),
        }
        and all(
            qpair_dependency_map[claim] == set()
            for claim in qpair_t[:3] + qpair_f
        )
        and qpair_dependency_map["DEF-QPAIR-SPIN-CARRIER"] == set()
        and qpair_dependency_map["DEF-QPAIR-HERM-SLOT"]
        == {("DEF-QPAIR-SPIN-CARRIER", "REQUIRES")}
        and qpair_dependency_map["DEF-QPAIR-SYM-SLOT"]
        == {("DEF-QPAIR-SPIN-CARRIER", "REQUIRES")}
        and qpair_dependency_map["DEF-QPAIR-MIXED-C4"]
        == {("DEF-QPAIR-SPIN-CARRIER", "REQUIRES")}
        and qpair_dependency_map["DEF-QPAIR-ADMISSIBLE-LINEAR-CLASS"] == {
            ("DEF-QPAIR-HERM-SLOT", "REQUIRES"),
            ("DEF-QPAIR-SYM-SLOT", "REQUIRES"),
            ("DEF-QPAIR-MIXED-C4", "REQUIRES"),
            ("COLOR-INTEGRAL-LIFT", "REQUIRES"),
        }
        and scope_contains_all(
            index, qpair_t[0],
            ("independent carrier", "no total set map",
             "field fiber is k^1 v", "fixed nonzero content layer",
             "full lattice can have wider fibers"),
        )
        and scope_contains_all(
            index, qpair_t[1],
            ("s(v)=s(w) iff w=+-v", "set-theoretic redundancy only",
             "no informational defense of two slots"),
        )
        and scope_contains_all(
            index, qpair_t[4],
            ("frozen class a_rel", "absolute determinant 64",
             "relative minimality", "not minimality of slot count"),
        )
        and scope_contains_all(
            index, qpair_f[0],
            ("universal proposition", "single symmetric slot"),
        )
        and "disproving the universal pair-forcing proposition"
        in index[qpair_f[0]]["falsifier"].lower()
        and scope_contains_all(
            index, qpair_f[1],
            ("not complex-linear or k-linear",),
        )
        and "disproving normalization"
        in index[qpair_f[1]]["falsifier"].lower()
        and all(claim not in programs for claim in qpair_t + qpair_f),
    ))


    qpair_area_rows = (
        "QPAIR-DET-AREA-SLOT-COMPARISON",
        "QPAIR-DET-AREA-PLACE-PAIR",
    )
    qpair_area_path = "probes/P-QPAIR-RELATIONAL-AREA-1"
    qpair_area_digest = (
        "5c02838a8d0bfe822fd30d703b6b0dad71cc459cbede3b9347ed8dfccd25a47f"
    )
    qpair_area_definitions = {
        "DEF-QPAIR-TYPED-PARTIAL-TRACE",
        "DEF-QPAIR-DET-AREA",
    }
    checks.append((
        "QPAIR-AREA",
        "typed determinant slots and the two cyclotomic places stay exact L1 algebra with no physical lift",
        all(
            has_status(index, claim, "T")
            and normative.get(claim, {}).get("item_type") == "THEOREM"
            and normative.get(claim, {}).get("layer") == "L1"
            and evidence.get(claim, {}).get("location") == qpair_area_path
            and evidence.get(claim, {}).get("sha256") == qpair_area_digest
            and evidence.get(claim, {}).get("hash_mode")
            == "bundle-manifest-sha256-v1"
            and evidence.get(claim, {}).get("architecture_requirement")
            == "two-architecture"
            and claim not in programs
            and all(row["item_id"] != claim for row in dependencies)
            for claim in qpair_area_rows
        )
        and all(
            normative.get(item, {}).get("item_type") == "DEFINITION"
            and normative.get(item, {}).get("layer") == "L1"
            for item in qpair_area_definitions
        )
        and scope_contains_all(
            index, qpair_area_rows[0],
            ("4n(d/2)=det rho_v", "beta_b+4a=1",
             "no necessity", "physical-qubit"),
        )
        and scope_contains_all(
            index, qpair_area_rows[1],
            ("every nonzero x in o_k^4", "f_5^x/{+-1}",
             "[0,1/4]", "conservative common scope o_k^4",
             "fresh lock for any field-wide promotion", "no qubit"),
        )
        and all(row["owner_item_id"] not in qpair_area_rows
                for row in gates.values()),
    ))

    piston_rows = (
        "PISTON-2X2-RESHAPE-WEDGE",
        "QDD-TR4-OCCURRENCE-WEIGHT-WEDGE-BLIND",
        "PISTON-WEDGE-LIFT-CENSUS",
    )
    piston_path = "probes/P-PISTON-RELATIONAL-WEDGE-1"
    piston_digest = (
        "680d4ea3a134d3523f67260b64d21720f4ed5777b36c055b9d23ae3f4c00d2b8"
    )
    piston_dependencies = {
        claim: {
            (row["depends_on"], row["relation"])
            for row in dependencies if row["item_id"] == claim
        }
        for claim in piston_rows
    }
    checks.append((
        "PISTON-WEDGE",
        "the rational piston reshape, occurrence-weight boundary, and lift census stay exact and decoder-fenced",
        all(
            has_status(index, claim, "T")
            and normative.get(claim, {}).get("item_type") == "THEOREM"
            and normative.get(claim, {}).get("layer") == "L1"
            and evidence.get(claim, {}).get("location") == piston_path
            and evidence.get(claim, {}).get("sha256") == piston_digest
            and evidence.get(claim, {}).get("architecture_requirement")
            == "two-architecture"
            and claim not in programs
            for claim in piston_rows
        )
        and all(
            normative.get(item, {}).get("item_type") == "DEFINITION"
            and normative.get(item, {}).get("layer") == "L1"
            for item in ("DEF-PISTON-2X2-RESHAPE", "DEF-PISTON-WEDGE")
        )
        and piston_dependencies[piston_rows[0]] == {
            ("KERNEL-WEDGE-AFFINITY", "REQUIRES"),
            ("DEF-QDD-BALANCED-PISTON", "REQUIRES"),
            ("DEF-QDD-QPAIR", "REQUIRES"),
            ("DEF-QDD-TRANSPOSE", "REQUIRES"),
            ("QPAIR-SYM2-TENSOR-DEFECT", "REQUIRES"),
        }
        and piston_dependencies[piston_rows[1]] == {
            ("QDD-PROJECTOR-PAIR-TR4", "REQUIRES"),
            ("QDD-ALGEBRAIC-FACTORIZATION", "REQUIRES"),
            (piston_rows[0], "REQUIRES"),
        }
        and piston_dependencies[piston_rows[2]]
        == {(piston_rows[0], "REQUIRES")}
        and scope_contains_all(
            index, piston_rows[0],
            ("exactly 8 of 24", "d_z/2", "exactly 145",
             "no carrier bridge"),
        )
        and scope_contains_all(
            index, piston_rows[1],
            ("same (m,w_low,w_high)", "full registered quadratic record is not wedge-blind",
             "no claim about what a decoder should read"),
        )
        and scope_contains_all(
            index, piston_rows[2],
            ("145", "129+16", "exactly 48", "no concurrence"),
        )
        and all(row["owner_item_id"] not in piston_rows
                for row in gates.values()),
    ))

    pure_rows = (
        "PURE-QUBIT-RELATIONAL-AREA",
        "PURE-QUBIT-LOCAL-RELATION-PYTHAGORAS",
        "PURE-QUBIT-RELATIONAL-CHSH",
        "PURE-QUBIT-RELATIONAL-READING",
    )
    pure_path = "probes/P-PURE-QUBIT-RELATIONAL-GEOMETRY-2"
    pure_digest = (
        "bcfc2d7c1552fb4b42e64f4bca7a3025415893152129aea67a45585f6d15320e"
    )
    pure_dependencies = {
        claim: {
            (row["depends_on"], row["relation"])
            for row in dependencies if row["item_id"] == claim
        }
        for claim in pure_rows
    }
    checks.append((
        "PURE-QUBIT",
        "conditional pure-two-qubit area, Pythagoras, CHSH, and reading stay on the external standard-QM scope",
        all(has_status(index, claim, "T") for claim in pure_rows[:3])
        and has_status(index, pure_rows[3], "D")
        and all(
            normative.get(claim, {}).get("layer") == "L1"
            and evidence.get(claim, {}).get("location") == pure_path
            and evidence.get(claim, {}).get("sha256") == pure_digest
            and evidence.get(claim, {}).get("hash_mode")
            == "bundle-manifest-sha256-v1"
            and evidence.get(claim, {}).get("architecture_requirement")
            == "two-architecture"
            and claim not in programs
            and all(row["owner_item_id"] != claim for row in gates.values())
            for claim in pure_rows
        )
        and all(normative.get(claim, {}).get("item_type") == "THEOREM"
                for claim in pure_rows[:3])
        and normative.get(pure_rows[3], {}).get("item_type") == "DICTIONARY"
        and pure_dependencies[pure_rows[0]]
        == {("QPAIR-SYM2-TENSOR-DEFECT", "REQUIRES")}
        and pure_dependencies[pure_rows[1]]
        == {(pure_rows[0], "REQUIRES")}
        and pure_dependencies[pure_rows[2]] == {
            (pure_rows[0], "REQUIRES"),
            ("BELL-CAUSAL-ACCOUNTING", "BOUNDED_BY"),
        }
        and pure_dependencies[pure_rows[3]]
        == {(pure_rows[0], "REQUIRES")}
        and scope_contains_all(
            index, pure_rows[0],
            ("externally supplying", "||kappa||^2=4",
             "(1/2)||u wedge v||_tensor^2", "including a possible zero",
             "determinant phase", "external standard-qm"),
        )
        and scope_contains_all(
            index, pure_rows[1],
            ("|b_vec|^2+c^2=1", "not a mixed-state conservation law",
             "werner p=1/2"),
        )
        and scope_contains_all(
            index, pure_rows[2],
            ("maximum absolute expectation", "optimized model value",
             "no-signalling test", "causal account"),
        )
        and scope_contains_all(
            index, pure_rows[3],
            ("only after externally supplying", "not a third particle",
             "no map from the integral qpair carrier", "l6 measure"),
        ),
    ))

    bell = "BELL-CAUSAL-ACCOUNTING"
    bell_incoming = {
        (row["item_id"], row["relation"])
        for row in dependencies if row["depends_on"] == bell
    }
    bell_outgoing = {
        (row["depends_on"], row["relation"])
        for row in dependencies if row["item_id"] == bell
    }
    checks.append((
        "BELL-CAUSAL",
        "the Bell row remains an inline O/STOP accounting barrier with no experiment or causal conclusion",
        has_status(index, bell, "O")
        and normative.get(bell, {}).get("item_type") == "OBLIGATION"
        and normative.get(bell, {}).get("status") == "O"
        and normative.get(bell, {}).get("layer") == "MULTI"
        and normative.get(bell, {}).get("gate_ids") == ""
        and index.get(bell, {}).get("canon_section") == "18. The frontier"
        and index.get(bell, {}).get("evidence") == "inline"
        and evidence.get(bell, {}).get("evidence_kind") == "INLINE_CANON"
        and evidence.get(bell, {}).get("location") == "inline"
        and evidence.get(bell, {}).get("sha256") == scope_sha256(index, bell)
        and evidence.get(bell, {}).get("hash_mode")
        == "registry-scope-sha256-v1"
        and evidence.get(bell, {}).get("architecture_requirement") == "none"
        and programs.get(bell, {}).get("program_id") == "QUANTUM_EM"
        and programs.get(bell, {}).get("queue_role") == "ROOT"
        and programs.get(bell, {}).get("work_state") == "STOP"
        and programs.get(bell, {}).get("work_mode") == "FORMAL"
        and bell_outgoing == set()
        and bell_incoming == {
            ("BELL-MAGIC-BOUNDARY", "BOUNDED_BY"),
            ("PURE-QUBIT-RELATIONAL-CHSH", "BOUNDED_BY"),
            ("DQRC-INTEGER-CENSUS-ARITHMETIC", "BOUNDED_BY"),
            ("DQRC-HORODECKI-REENCODING", "BOUNDED_BY"),
            ("DQRC-H-COEFFICIENT-NONSELECTION", "BOUNDED_BY"),
            ("DQRC-ORIGIN-NONSELECTION", "BOUNDED_BY"),
            ("DQRC-MAXIMAL-SECTOR-FIELD-BOUNDARY", "BOUNDED_BY"),
        }
        and all(row["owner_item_id"] != bell for row in gates.values())
        and scope_contains_all(
            index, bell,
            ("source state or variable lambda", "setting-selection mechanism",
             "normalized kernel p(a,b|x,y,lambda)", "bell-local factorization",
             "measurement independence", "no-signalling marginal equalities",
             "controllable-superluminal-signalling test",
             "l1-to-l4, l4-to-l5, and l5-to-l6",
             "complete dimensional audit", "failure of factorization alone",
             "no latent-variable", "selected in advance"),
        )
        and "partial accounts and failed individual candidates remain stop"
        in index[bell]["falsifier"].lower(),
    ))

    dqrc_rows = (
        "DQRC-INTEGER-CENSUS-ARITHMETIC",
        "DQRC-HORODECKI-REENCODING",
        "DQRC-H-COEFFICIENT-NONSELECTION",
        "DQRC-ORIGIN-NONSELECTION",
        "DQRC-MAXIMAL-SECTOR-FIELD-BOUNDARY",
    )
    dqrc_definition = "DEF-DQRC-INTEGER-CENSUS"
    dqrc_path = "probes/P-DQRC-ARITHMETIC-RECONSTRUCTION-1"
    dqrc_digest = (
        "25af7d719a244e4d877cf364736f9f9d0c4d0d45ff07a3611f7ff39b1679ee4b"
    )
    dqrc_dependencies = {
        claim: {
            (row["depends_on"], row["relation"])
            for row in dependencies if row["item_id"] == claim
        }
        for claim in dqrc_rows
    }
    checks.append((
        "DQRC",
        "the deterministic integer census and four boundary theorems stay exact L1 results while coefficient, origin, apparatus, event, measure, Bell, and physical readings remain unselected",
        {claim for claim in index if claim.startswith("DQRC-")}
        == set(dqrc_rows)
        and all(has_status(index, claim, "T") for claim in dqrc_rows)
        and dqrc_definition not in index
        and normative.get(dqrc_definition, {}).get("item_type") == "DEFINITION"
        and normative.get(dqrc_definition, {}).get("claim_id") == ""
        and normative.get(dqrc_definition, {}).get("status") == ""
        and normative.get(dqrc_definition, {}).get("layer") == "L1"
        and all(
            normative.get(claim, {}).get("item_type") == "THEOREM"
            and normative.get(claim, {}).get("status") == "T"
            and normative.get(claim, {}).get("layer") == "L1"
            and normative.get(claim, {}).get("gate_ids") == ""
            and evidence.get(claim, {}).get("location") == dqrc_path
            and evidence.get(claim, {}).get("sha256") == dqrc_digest
            and evidence.get(claim, {}).get("hash_mode")
            == "bundle-manifest-sha256-v1"
            and evidence.get(claim, {}).get("architecture_requirement")
            == "two-architecture"
            and claim not in programs
            and all(row["owner_item_id"] != claim for row in gates.values())
            for claim in dqrc_rows
        )
        and dqrc_dependencies[dqrc_rows[0]] == {
            (dqrc_definition, "REQUIRES"),
            ("DEF-ACTION-LAYERS", "REQUIRES"),
            ("BELL-CAUSAL-ACCOUNTING", "BOUNDED_BY"),
        }
        and dqrc_dependencies[dqrc_rows[1]] == {
            (dqrc_rows[0], "REQUIRES"),
            ("PURE-QUBIT-RELATIONAL-CHSH", "REQUIRES"),
            ("BELL-CAUSAL-ACCOUNTING", "BOUNDED_BY"),
        }
        and dqrc_dependencies[dqrc_rows[2]] == {
            (dqrc_rows[0], "REQUIRES"),
            (dqrc_rows[1], "REQUIRES"),
            ("BELL-CAUSAL-ACCOUNTING", "BOUNDED_BY"),
        }
        and dqrc_dependencies[dqrc_rows[3]] == {
            (dqrc_rows[0], "REQUIRES"),
            ("BELL-CAUSAL-ACCOUNTING", "BOUNDED_BY"),
        }
        and dqrc_dependencies[dqrc_rows[4]] == {
            (dqrc_rows[0], "REQUIRES"),
            ("DEGREES-BY-PRIME", "REQUIRES"),
            ("BELL-CAUSAL-ACCOUNTING", "BOUNDED_BY"),
        }
        and scope_contains_all(
            index, dqrc_rows[0],
            ("exact integral l1 carrier", "margin exactly 2k",
             "inserted t involution", "parity solely from sigma_xy",
             "no realized setting", "no-signalling"),
        )
        and scope_contains_all(
            index, dqrc_rows[1],
            ("externally supplying", "exactly reencodes",
             "local singular-value rotations", "not an intrinsic derivation"),
        )
        and scope_contains_all(
            index, dqrc_rows[2],
            ("every integer beta>=0", "if and only if beta=4",
             "do not select 4", "no claim excludes a richer"),
        )
        and scope_contains_all(
            index, dqrc_rows[3],
            ("s_1^[0]=0", "s_1^[1]=4", "not origin invariant",
             "not an intrinsic physical prediction"),
        )
        and scope_contains_all(
            index, dqrc_rows[4],
            ("proper subfield of q(zeta_40)", "integer substitution",
             "not an integer limiting frequency", "no physical place"),
        )
        and has_status(index, "BELL-CAUSAL-ACCOUNTING", "O")
        and has_status(index, "QDD-INSTRUMENT-APPARATUS", "O")
        and qdd_current_split
        and has_status(index, "BELL-MAGIC-BOUNDARY", "T")
        and has_status(index, "PURE-QUBIT-RELATIONAL-CHSH", "T")
        and has_status(index, "TWO-PLACE-PHYSICS", "D")
        and has_status(index, "SILVER-RING-FACTS", "C")
        and has_status(index, "SILVER-SIBLING", "D")
        and "P-DQRC-FINITE-DEFICIT-1" not in normative
        and "P-DQRC-FINITE-DEFICIT-1" not in programs
        and all(row["owner_item_id"] != "P-DQRC-FINITE-DEFICIT-1"
                for row in gates.values()),
    ))

    de_w_edges = {
        (row["item_id"], row["depends_on"], row["relation"])
        for row in dependencies
        if "DE-W-CONSTANT" in (row["item_id"], row["depends_on"])
    }
    checks.append((
        "DE-W-CONSTANT",
        "the immutable dark-energy reading fires at F on the exact DESI DR2 R1 witness while its three declared edges remain fixed, the register dictionary and conformal-weight obligation do not move, and its L6 reading-only layer creates no gate, frontier program or replacement selection premise",
        has_status(index, "DE-W-CONSTANT", "F")
        and index["DE-W-CONSTANT"]["evidence"] == "probes/P-DE-W-ARMING-2"
        and index["DE-W-CONSTANT"]["canon_section"] == "13. Gravity and cosmology"
        and normative["DE-W-CONSTANT"]["item_type"] == "FALSIFIED"
        and normative["DE-W-CONSTANT"]["status"] == "F"
        and evidence["DE-W-CONSTANT"]["evidence_kind"] == "PUBLIC_PROBE"
        and evidence["DE-W-CONSTANT"]["location"]
        == "probes/P-DE-W-ARMING-2"
        and evidence["DE-W-CONSTANT"]["sha256"]
        == "de047b7352a06cfa2ab5a71f128bc9f57bef41c9be4456af3ddc21e2863b5f17"
        and evidence["DE-W-CONSTANT"]["hash_mode"]
        == "bundle-manifest-sha256-v1"
        and evidence["DE-W-CONSTANT"]["architecture_requirement"]
        == "two-architecture"
        and normative["DE-W-CONSTANT"]["layer"] == "L6"
        and normative["DE-W-CONSTANT"]["gate_ids"] == ""
        and "DE-W-CONSTANT" not in programs
        and de_w_edges == {
            ("COSMOLOGY-REGISTER", "DE-W-CONSTANT", "BOUNDED_BY"),
            ("DE-CONFORMAL-WEIGHT", "DE-W-CONSTANT", "BOUNDED_BY"),
            ("DE-W-CONSTANT", "DEF-ARCHITECTURE", "REQUIRES"),
        }
        and scope_contains_all(
            index, "DE-W-CONSTANT",
            ("-14/15", "constantly in a", "-211/200 +- 9/250",
             "365/108", "322/125", "45625>34776", "10849/13500",
             "only the committed register reading"),
        )
        and has_status(index, "COSMOLOGY-REGISTER", "D")
        and has_status(index, "DE-CONFORMAL-WEIGHT", "O")
        and has_status(index, "NS-TILT", "H")
        and all(row["owner_item_id"] != "DE-W-CONSTANT"
                for row in gates.values()),
    ))

    wall_new = (
        "J-LI-PENTAGON-DILATION-DEFICIENCY",
        "PENTAGON-ONLY-DILATIONS",
        "J-LI-CYCLIC-CARRIER-DIMENSION",
    )
    wall_edges = {
        (row["item_id"], row["depends_on"], row["relation"])
        for row in dependencies
        if any(claim in (row["item_id"], row["depends_on"])
               for claim in wall_new)
    }
    checks.append((
        "J-LI-WALL-CLOSURES",
        "the pentagon-tower dilation route is dead by the exact constant deficiency with the fired route recorded at F, and every finite-dimensional cyclic carrier is excluded, while the three registered carrier no-gos and the live cocycle-vector hypothesis keep their statuses and no gate or program row is created",
        has_status(index, "J-LI-PENTAGON-DILATION-DEFICIENCY", "T")
        and has_status(index, "PENTAGON-ONLY-DILATIONS", "F")
        and has_status(index, "J-LI-CYCLIC-CARRIER-DIMENSION", "T")
        and all(index[claim]["canon_section"] == "16. p = 5 and the wall"
                and evidence[claim]["evidence_kind"] == "PUBLIC_PROBE"
                and evidence[claim]["architecture_requirement"]
                == "two-architecture"
                and normative[claim]["layer"] == "NOT_APPLICABLE"
                and normative[claim]["gate_ids"] == ""
                for claim in wall_new)
        and index["J-LI-PENTAGON-DILATION-DEFICIENCY"]["evidence"]
        == "probes/P-PENTAGON-ONLY-DILATIONS-1"
        and index["PENTAGON-ONLY-DILATIONS"]["evidence"]
        == "probes/P-PENTAGON-ONLY-DILATIONS-1"
        and index["J-LI-CYCLIC-CARRIER-DIMENSION"]["evidence"]
        == "probes/P-J-LI-CARRIER-NOGO-1"
        and scope_contains_all(
            index, "J-LI-PENTAGON-DILATION-DEFICIENCY",
            ("(1/12)(1 - 1/q^2)", "constant in the tower height",
             "(1/q) g_1"),
        )
        and scope_contains_all(
            index, "PENTAGON-ONLY-DILATIONS",
            ("falsified", "unreachable"),
        )
        and scope_contains_all(
            index, "J-LI-CYCLIC-CARRIER-DIMENSION",
            ("finite-dimensional cyclic", "infinite spectral support",
             "no atom at 1"),
        )
        and wall_edges == {
            ("PENTAGON-ONLY-DILATIONS",
             "J-LI-PENTAGON-DILATION-DEFICIENCY", "REQUIRES"),
        }
        and has_status(index, "J-LI-TORAL-HAAR-NOGO", "T")
        and has_status(index, "J-LI-LAMBDA-HAAR-HS-NOGO", "T")
        and has_status(index, "J-LI-LAMBDA-SHIFT-NOGO", "T")
        and has_status(index, "LAMBDA-COCYCLE-ANGLES", "H")
        and all(row["owner_item_id"] not in wall_new
                for row in gates.values())
        and all(claim not in programs for claim in wall_new),
    ))

    anchor_new = (
        "KERNEL-SUBSET-LANDSCAPE",
        "J-TORAL-ENTROPY",
        "TM-ENTROPY-ZERO",
        "BINARY-READ-RELATIVE-ENTROPY",
    )
    anchor_edges = {
        (row["item_id"], row["depends_on"], row["relation"])
        for row in dependencies
        if any(claim in (row["item_id"], row["depends_on"])
               for claim in anchor_new)
    }
    checks.append((
        "ENTROPY-KERNEL-ANCHORS",
        "the subset landscape decides the exact 32-entry table with connectivity iff dim U_S = 6, and the rate 2 log phi enters with the toral anchor, the zero-entropy driver, and the binary residue bracket, while the layer-bridge obligation keeps its exact scope and no gate or program row is created",
        has_status(index, "KERNEL-SUBSET-LANDSCAPE", "T")
        and has_status(index, "J-TORAL-ENTROPY", "T")
        and has_status(index, "TM-ENTROPY-ZERO", "T")
        and has_status(index, "BINARY-READ-RELATIVE-ENTROPY", "T")
        and all(evidence[claim]["evidence_kind"] == "PUBLIC_PROBE"
                and evidence[claim]["architecture_requirement"]
                == "two-architecture"
                and normative[claim]["gate_ids"] == ""
                for claim in anchor_new)
        and index["KERNEL-SUBSET-LANDSCAPE"]["evidence"]
        == "probes/P-KERNEL-SUBSET-LANDSCAPE-1"
        and all(index[claim]["evidence"]
                == "probes/P-ENTROPY-RESIDUE-MATH-1"
                for claim in ("J-TORAL-ENTROPY", "TM-ENTROPY-ZERO",
                              "BINARY-READ-RELATIVE-ENTROPY"))
        and index["KERNEL-SUBSET-LANDSCAPE"]["canon_section"]
        == "3. The kernel and the census"
        and index["TM-ENTROPY-ZERO"]["canon_section"]
        == "3. The kernel and the census"
        and index["J-TORAL-ENTROPY"]["canon_section"]
        == "2. Time, space, and the decoder"
        and index["BINARY-READ-RELATIVE-ENTROPY"]["canon_section"]
        == "2. Time, space, and the decoder"
        and normative["KERNEL-SUBSET-LANDSCAPE"]["layer"] == "L1"
        and normative["J-TORAL-ENTROPY"]["layer"] == "L2"
        and normative["TM-ENTROPY-ZERO"]["layer"] == "L5"
        and normative["BINARY-READ-RELATIVE-ENTROPY"]["layer"]
        == "NOT_APPLICABLE"
        and scope_contains_all(
            index, "KERNEL-SUBSET-LANDSCAPE",
            ("dim U_S = 6", "acde", "abcde"),
        )
        and scope_contains_all(
            index, "J-TORAL-ENTROPY",
            ("2 log phi", "#fix(t^n)", "1860496"),
        )
        and scope_contains_all(
            index, "TM-ENTROPY-ZERO",
            ("linear factor complexity", "entropy rate 0"),
        )
        and scope_contains_all(
            index, "BINARY-READ-RELATIVE-ENTROPY",
            ("log(phi^2/2)", "2 log phi = log 2 + log(phi^2/2)"),
        )
        and anchor_edges == {
            ("KERNEL-SUBSET-LANDSCAPE", "KERNEL-CONNECT-ALL-K",
             "REQUIRES"),
            ("KERNEL-SUBSET-LANDSCAPE", "KERNEL-WEDGE-AFFINITY",
             "REQUIRES"),
            ("J-TORAL-ENTROPY", "J-STEP", "REQUIRES"),
            ("J-TORAL-PERIODIC-POINTS", "J-TORAL-ENTROPY", "REQUIRES"),
        }
        and has_status(index, "KERNEL-CONNECT-ALL-K", "T")
        and has_status(index, "ENTROPY-LAYER-BRIDGE", "O")
        and scope_contains_all(
            index, "ENTROPY-LAYER-BRIDGE",
            ("equal cardinalities do not construct",),
        )
        and all(row["owner_item_id"] not in anchor_new
                for row in gates.values())
        and all(claim not in programs for claim in anchor_new),
    ))

    arith_new = ("J-MAHLER-MEASURE", "REGULATOR-TWO-LOG-PHI",
                 "CYCLOTOMIC-CLASS-NUMBER-ONE", "J-TORAL-PERIODIC-POINTS")
    arith_edges = {
        (row["item_id"], row["depends_on"], row["relation"])
        for row in dependencies
        if any(claim in (row["item_id"], row["depends_on"])
               for claim in arith_new)
    }
    checks.append((
        "TWOLOGPHI-ARITHMETIC-ANCHOR",
        "2 log phi gains its arithmetic anchor as a Mahler measure and a regulator, with class number one proved rather than imported and the periodic-point structure entering at C, while the entropy bridge keeps its exact scope and every new row carries the fence as a ledger edge",
        has_status(index, "J-MAHLER-MEASURE", "T")
        and has_status(index, "REGULATOR-TWO-LOG-PHI", "T")
        and has_status(index, "CYCLOTOMIC-CLASS-NUMBER-ONE", "T")
        and has_status(index, "J-TORAL-PERIODIC-POINTS", "C")
        and all(index[claim]["evidence"] == "probes/P-TWOLOGPHI-INVARIANTS-1"
                and evidence[claim]["evidence_kind"] == "PUBLIC_PROBE"
                and evidence[claim]["architecture_requirement"]
                == "two-architecture"
                and normative[claim]["gate_ids"] == ""
                for claim in arith_new)
        and index["J-MAHLER-MEASURE"]["canon_section"]
        == "1. The axiom and the two projections"
        and index["REGULATOR-TWO-LOG-PHI"]["canon_section"]
        == "4. The two places"
        and index["CYCLOTOMIC-CLASS-NUMBER-ONE"]["canon_section"]
        == "4. The two places"
        and index["J-TORAL-PERIODIC-POINTS"]["canon_section"]
        == "2. Time, space, and the decoder"
        and normative["J-MAHLER-MEASURE"]["layer"] == "L1"
        and normative["REGULATOR-TWO-LOG-PHI"]["layer"] == "L1"
        and normative["CYCLOTOMIC-CLASS-NUMBER-ONE"]["layer"] == "L1"
        and normative["J-TORAL-PERIODIC-POINTS"]["layer"] == "L2"
        and scope_contains_all(index, "J-MAHLER-MEASURE",
                               ("mahler measure", "log m(j) = 2 log phi",
                                "irreducible over q"))
        and scope_contains_all(index, "REGULATOR-TWO-LOG-PHI",
                               ("reg(q(zeta_5)) = 2 log phi",
                                "fundamental unit", "labeled imports"))
        and scope_contains_all(index, "CYCLOTOMIC-CLASS-NUMBER-ONE",
                               ("1125 < 16 pi^4", "5 < 16",
                                "proved not imported"))
        and scope_contains_all(index, "J-TORAL-PERIODIC-POINTS",
                               ("l_n^2", "(l_n - 2)^2", "finite-range"))
        and arith_edges == {
            ("J-IDEAL-COUNT-QUADRATIC-CHARACTER",
             "REGULATOR-TWO-LOG-PHI", "REQUIRES"),
            ("J-IDEAL-COUNT-QUADRATIC-CHARACTER",
             "CYCLOTOMIC-CLASS-NUMBER-ONE", "REQUIRES"),
            ("J-IDEAL-RAPIDITY-CHARACTER-LIFT",
             "CYCLOTOMIC-CLASS-NUMBER-ONE", "REQUIRES"),
            ("J-SIGNED-TRACE-MAHLER-RIGIDITY",
             "J-MAHLER-MEASURE", "REQUIRES"),
            ("J-MAHLER-MEASURE", "J-STEP", "REQUIRES"),
            ("J-MAHLER-MEASURE", "ENTROPY-LAYER-BRIDGE", "BOUNDED_BY"),
            ("REGULATOR-TWO-LOG-PHI", "J-PROJECTIONS", "REQUIRES"),
            ("REGULATOR-TWO-LOG-PHI", "ENTROPY-LAYER-BRIDGE", "BOUNDED_BY"),
            ("CYCLOTOMIC-CLASS-NUMBER-ONE",
             "QUARTIC-CYCLOTOMIC-TOTAL-RAMIFICATION-CENSUS", "REQUIRES"),
            ("J-TORAL-PERIODIC-POINTS", "J-TORAL-ENTROPY", "REQUIRES"),
            ("J-TORAL-PERIODIC-POINTS", "ENTROPY-LAYER-BRIDGE", "BOUNDED_BY"),
        }
        and has_status(index, "J-TORAL-ENTROPY", "T")
        and has_status(index, "J-UNIT", "T")
        and has_status(index, "ENTROPY-LAYER-BRIDGE", "O")
        and scope_contains_all(index, "ENTROPY-LAYER-BRIDGE",
                               ("equal cardinalities do not construct",))
        and all(row["owner_item_id"] not in arith_new
                for row in gates.values())
        and all(claim not in programs for claim in arith_new),
    ))

    metro_edges = {
        (row["item_id"], row["depends_on"], row["relation"])
        for row in dependencies
        if "METRO-FORBIDDEN-WITNESSES" in (row["item_id"], row["depends_on"])
    }
    checks.append((
        "METRO-FORBIDDEN-WITNESSES",
        "obligation B is discharged for the five entries section 15 names, at C on the completed public probe with exactly its two declared edges, while the parent keeps status O and STOP with only its obligation B clause changed and the arrows row does not move",
        has_status(index, "METRO-FORBIDDEN-WITNESSES", "C")
        and index["METRO-FORBIDDEN-WITNESSES"]["evidence"]
        == "probes/P-METRO-FORBIDDEN-WITNESSES-1"
        and index["METRO-FORBIDDEN-WITNESSES"]["canon_section"]
        == "15. Couplings, instruments, and metrology"
        and evidence["METRO-FORBIDDEN-WITNESSES"]["evidence_kind"]
        == "PUBLIC_PROBE"
        and evidence["METRO-FORBIDDEN-WITNESSES"]["architecture_requirement"]
        == "two-architecture"
        and normative["METRO-FORBIDDEN-WITNESSES"]["layer"] == "L5"
        and normative["METRO-FORBIDDEN-WITNESSES"]["gate_ids"] == ""
        and metro_edges == {
            ("METRO-FORBIDDEN-WITNESSES", "METRO-REDUCTION-ARROWS",
             "REQUIRES"),
            ("METRO-FORBIDDEN-WITNESSES", "METRO-REDUCTION-CALCULUS",
             "BOUNDED_BY"),
        }
        and scope_contains_all(
            index, "METRO-FORBIDDEN-WITNESSES",
            ("functional obstruction", "16140", "21987",
             "distinctions of the stream"),
        )
        and has_status(index, "METRO-REDUCTION-CALCULUS", "O")
        and has_status(index, "METRO-REDUCTION-ARROWS", "C")
        and scope_contains_all(
            index, "METRO-REDUCTION-CALCULUS",
            ("discharged for the five entries section 15 names",
             "obligation d", "obligation e"),
        )
        and "METRO-FORBIDDEN-WITNESSES" not in programs
        and all(row["owner_item_id"] != "METRO-FORBIDDEN-WITNESSES"
                for row in gates.values()),
    ))

    v60_theorems = {
        "AFFINE-READING-DEGREE-CENSUS": (
            "L1", "3. The kernel and the census",
            "probes/P-AFFINE-QUADRATIC-READING-1",
            "95a3d91f6707fda16b7baecdc1e17d54eda884e9a4e622540950014777d8f255",
        ),
        "AFFINE-QUADRATIC-FORM-UNIQUENESS": (
            "L1", "3. The kernel and the census",
            "probes/P-AFFINE-QUADRATIC-READING-1",
            "95a3d91f6707fda16b7baecdc1e17d54eda884e9a4e622540950014777d8f255",
        ),
        "CARRY-QUADRATIC-SYMMETRY": (
            "L1", "3. The kernel and the census",
            "probes/P-CARRY-QUADRATIC-SYMMETRY-2",
            "7799ef57695141d74409eccdc5da69a0d6aadfcf17783ee5623e91eaa499d9a1",
        ),
        "J-BINARY-NORM-DESCENT": (
            "L1", "3. The kernel and the census",
            "probes/P-J-BINARY-NORM-DESCENT-1",
            "1170f93a879410a1cd8f2119b731f305d94608e15dc11792620e604efe8ead97",
        ),
        "QDD-RECORD-SATURATION-DESCENT": (
            "L4", "2. Time, space, and the decoder",
            "probes/P-QDD-RECORD-MONOID-DESCENT-2",
            "0f0fdb9f053d9c7498908a7ba105c1c509e339bd194b801bdcfa33e4a5815fcf",
        ),
        "QDD-COMMUTATOR-READOUT-EQUALITY-FORK": (
            "L4", "2. Time, space, and the decoder",
            "probes/P-QDD-COMMUTATOR-READOUT-FORK-2",
            "94ab2859cd0bbd5ac43bb4699bd48ac14a7bde781b96d00dce6a5998f86c673b",
        ),
        "QDD-PURE-RECORD-COMMUTATOR-FAITHFULNESS": (
            "MULTI", "2. Time, space, and the decoder",
            "probes/P-QDD-AFFINE-PURE-RECORD-BRIDGE-1",
            "03c4f81854fad29baa6f4fa5112e93733861b0b770f4f2752e5d79ea555f0932",
        ),
        "QDD-PURE-RECORD-TYPED-BRIDGE-BOUNDARY": (
            "MULTI", "2. Time, space, and the decoder",
            "probes/P-QDD-PURE-RECORD-TYPED-BRIDGE-1",
            "0804101ff4a53f5b0954360c518149add2f94cc6ff51eacb81f1ce18ec32632b",
        ),
        "QDD-PURE-RECORD-PORT-UNIQUENESS": (
            "MULTI", "2. Time, space, and the decoder",
            "probes/P-QDD-PURE-RECORD-PORT-CANONICAL-1",
            "f6d5d8098f76f3402d7865c7b10ded2d6f6e3533538c2b961467e5824f2b18cf",
        ),
        "QDD-COMMUTATOR-SATURATION-SELECTION": (
            "L4", "2. Time, space, and the decoder",
            "probes/P-QDD-COMMUTATOR-SATURATION-CLOSURE-1",
            "b2912abe0eda6018ee6cc00eb9c6d7e51bae0ed8cc672f72fce7ee74da350b5f",
        ),
        "QDD-MECHANICAL-EVENT-SAMPLER": (
            "MULTI", "2. Time, space, and the decoder",
            "probes/P-QDD-DETERMINISTIC-EVENT-SAMPLER-1",
            "657946b5ab07aeb41808ccdde9be1bca01a1e001ddf43e356b468aaba57e25ba",
        ),
        "QDD-FINITE-MEMORY-O2B-BOUNDARY": (
            "L4", "2. Time, space, and the decoder",
            "probes/P-QDD-INSTRUMENT-CLASS-COMPLETENESS-1",
            "f6cf413cfc6dd8bb1e3d621fd545281f8fe7df7a0de0126804ed9fd43b4dd270",
        ),
        "QDD-EVENT-CONTEXT-BANK": (
            "MULTI", "2. Time, space, and the decoder",
            "probes/P-QDD-EVENT-CARRY-BANK-1",
            "234fea8f560c0f49c9676cb043f41116ca074110fcb4dee7e57929fca338a34c",
        ),
    }
    v60_obligations = {
        "QDD-TERMINAL-EVENT-SEMANTICS": (
            "MULTI",
            "aa11aa00883b70a3ba6d2170e5554f4b757e8368a47f4b8f3fb33c5db1778b2c",
        ),
        "QDD-INSTRUMENT-CLASS-COMPLETENESS": (
            "L4",
            "99b14df0bda674d2723f4f2d567a74e2e0ece546a73da9a24bd99d3b07786408",
        ),
    }
    v60_scope_hashes = {
        "AFFINE-READING-DEGREE-CENSUS":
            "9504b8dbbdd578c3e0edf9a89a0a6568289841b5f253b03cf6d0bd7fccdff202",
        "AFFINE-QUADRATIC-FORM-UNIQUENESS":
            "c1e6013d1fbf9029dc3e96d48308bebe87951d25652387769273bf3f0b8c70a8",
        "CARRY-QUADRATIC-SYMMETRY":
            "787b4724282e76a2fe958722bd7b668bf09df624a5a4f21eecdec45d694d4b8a",
        "J-BINARY-NORM-DESCENT":
            "e579c9e094c2969f60c73c6d2af4bc7cb6df7b533b4957df9ea2385c3cfb383a",
        "QDD-RECORD-SATURATION-DESCENT":
            "c641854947500c4cbe89a16125f406dded5d37de8f00a5d37883af457b40dfc7",
        "QDD-COMMUTATOR-READOUT-EQUALITY-FORK":
            "ba1e6bd1a9f1d7cb3195f241379092a008e9fa06706a1349a2c841eaec5e65dc",
        "QDD-PURE-RECORD-COMMUTATOR-FAITHFULNESS":
            "96ac7e9ca1452aeb72f00c1edc1f634cf362343a0ae7e16120e39020a26981b9",
        "QDD-PURE-RECORD-TYPED-BRIDGE-BOUNDARY":
            "85633904bf6e6a76331277011c08ea14765f1de569bd375667e0c70e26eaa568",
        "QDD-PURE-RECORD-PORT-UNIQUENESS":
            "d707322d96f9e27f280e0dbc17d3e86c6c2cca5245dea8caa1813a5e23497849",
        "QDD-COMMUTATOR-SATURATION-SELECTION":
            "e0f515f8c14cfe92d20f5bdb7878e7ef16953f6eb4218b44a40fd8226cf845a9",
        "QDD-MECHANICAL-EVENT-SAMPLER":
            "ca9463a2e776e9dd9e7d33b80c9c8645298904746f23eda757901c63ecf9f170",
        "QDD-FINITE-MEMORY-O2B-BOUNDARY":
            "33553b206c40ccbf1fd3e925c838e3431806b3e993eec75dae09db9597af10a5",
        "QDD-EVENT-CONTEXT-BANK":
            "677f3ce093bbc430438120d701c7586e2e446961a2ac33242f3bc90409073316",
        "QDD-INSTRUMENT-CLASS-COMPLETENESS":
            "99b14df0bda674d2723f4f2d567a74e2e0ece546a73da9a24bd99d3b07786408",
    }
    v60_dependencies = {
        "AFFINE-READING-DEGREE-CENSUS": {
            ("J-STEP", "REQUIRES"),
            ("J-UNIT", "REQUIRES"),
        },
        "AFFINE-QUADRATIC-FORM-UNIQUENESS": {
            ("AFFINE-READING-DEGREE-CENSUS", "REQUIRES"),
        },
        "CARRY-QUADRATIC-SYMMETRY": {
            ("CARRY-PENTAD", "REQUIRES"),
        },
        "J-BINARY-NORM-DESCENT": {
            ("AFFINE-QUADRATIC-FORM-UNIQUENESS", "REQUIRES"),
            ("CARRY-PENTAD", "REQUIRES"),
        },
        "QDD-RECORD-SATURATION-DESCENT": {
            ("QDD-FRESH-RECORD-EXTENSION", "REQUIRES"),
            ("QDD-INSTRUMENT-APPARATUS", "BOUNDED_BY"),
            ("QDD-INSTRUMENT-NONSELECTION", "REQUIRES"),
        },
        "QDD-COMMUTATOR-READOUT-EQUALITY-FORK": {
            ("QDD-INSTRUMENT-APPARATUS", "BOUNDED_BY"),
            ("QDD-INSTRUMENT-NONSELECTION", "REQUIRES"),
            ("QDD-J-CENTRALIZER-NONSELECTION", "REQUIRES"),
        },
        "QDD-PURE-RECORD-COMMUTATOR-FAITHFULNESS": {
            ("QDD-ALGEBRAIC-FACTORIZATION", "REQUIRES"),
            ("QDD-COMMUTATOR-READOUT-EQUALITY-FORK", "REQUIRES"),
            ("QDD-INSTRUMENT-APPARATUS", "BOUNDED_BY"),
        },
        "QDD-PURE-RECORD-TYPED-BRIDGE-BOUNDARY": {
            ("DEF-DECODER-MATTER", "REQUIRES"),
            ("QDD-INSTRUMENT-APPARATUS", "BOUNDED_BY"),
            ("QDD-PURE-RECORD-COMMUTATOR-FAITHFULNESS", "REQUIRES"),
        },
        "QDD-PURE-RECORD-PORT-UNIQUENESS": {
            ("AFFINE-QUADRATIC-FORM-UNIQUENESS", "REQUIRES"),
            ("QDD-INSTRUMENT-APPARATUS", "BOUNDED_BY"),
            ("QDD-PURE-RECORD-TYPED-BRIDGE-BOUNDARY", "REQUIRES"),
        },
        "QDD-COMMUTATOR-SATURATION-SELECTION": {
            ("QDD-INSTRUMENT-APPARATUS", "BOUNDED_BY"),
            ("QDD-INSTRUMENT-NONSELECTION", "REQUIRES"),
            ("QDD-PURE-RECORD-PORT-UNIQUENESS", "REQUIRES"),
        },
        "QDD-MECHANICAL-EVENT-SAMPLER": {
            ("DEF-AUTONOMOUS-STATE", "REQUIRES"),
            ("QDD-ALGEBRAIC-FACTORIZATION", "REQUIRES"),
            ("QDD-INSTRUMENT-APPARATUS", "BOUNDED_BY"),
        },
        "QDD-FINITE-MEMORY-O2B-BOUNDARY": {
            ("QDD-INSTRUMENT-APPARATUS", "BOUNDED_BY"),
            ("QDD-INSTRUMENT-NONSELECTION", "REQUIRES"),
        },
        "QDD-EVENT-CONTEXT-BANK": {
            ("DEF-AUTONOMOUS-STATE", "REQUIRES"),
            ("QDD-FRESH-RECORD-EXTENSION", "REQUIRES"),
            ("QDD-INSTRUMENT-APPARATUS", "BOUNDED_BY"),
            ("QDD-MECHANICAL-EVENT-SAMPLER", "REQUIRES"),
        },
        "QDD-TERMINAL-EVENT-SEMANTICS": {
            ("QDD-COMMUTATOR-SATURATION-SELECTION", "REQUIRES"),
            ("QDD-INSTRUMENT-APPARATUS", "BOUNDED_BY"),
            ("QDD-PURE-RECORD-PORT-UNIQUENESS", "REQUIRES"),
            ("QDD-RECORD-SATURATION-DESCENT", "REQUIRES"),
        },
        "QDD-INSTRUMENT-CLASS-COMPLETENESS": {
            ("QDD-FINITE-MEMORY-O2B-BOUNDARY", "REQUIRES"),
            ("QDD-INSTRUMENT-APPARATUS", "BOUNDED_BY"),
        },
    }
    v60_scope_boundaries = {
        "AFFINE-READING-DEGREE-CENSUS": (
            "degree two is the first nonzero invariant scalar degree",
            "no nonzero lossy G-equivariant linear reading exists",
            "no Born, decoder, effect, apparatus, event, measure or L2-L6 lift",
        ),
        "AFFINE-QUADRATIC-FORM-UNIQUENESS": (
            "unique invariant symmetric line",
            "additional premises q!=0 and q>=0 fix the positive ray",
            "no carrier-basis identification beyond P",
        ),
        "CARRY-QUADRATIC-SYMMETRY": (
            "bounded S_5 clause imported from CARRY-PENTAD",
            "five is an output cardinality, not a selected rational prime",
            "no cycle, orientation, exponent, J, decoder, physical reading or L2-L6 lift",
        ),
        "J-BINARY-NORM-DESCENT": (
            "explicit isometries rather than literal carrier equality",
            "differs from Frobenius",
            "no uniqueness of J, 2, 5, order five, Born, decoder, apparatus, event, measure or L2-L6 lift",
        ),
        "QDD-RECORD-SATURATION-DESCENT": (
            "no physical saturation law",
            "L5 stream",
            "L6 measure or exhaustive apparatus conclusion",
        ),
        "QDD-COMMUTATOR-READOUT-EQUALITY-FORK": (
            "decoder completeness relative only to event equality is insufficient",
            "no decoder completion, adopted bridge, event stream or measure",
        ),
        "QDD-PURE-RECORD-COMMUTATOR-FAITHFULNESS": (
            "decoder ownership, totality and the named layer gate remain absent",
        ),
        "QDD-PURE-RECORD-TYPED-BRIDGE-BOUNDARY": (
            "no source ownership, equality or L4-to-L1 gate is adopted",
        ),
        "QDD-PURE-RECORD-PORT-UNIQUENESS": (
            "public physical ownership and the named gate remain absent",
        ),
        "QDD-COMMUTATOR-SATURATION-SELECTION": (
            "no physical saturation dictionary or globally complete apparatus class is adopted",
        ),
        "QDD-MECHANICAL-EVENT-SAMPLER": (
            "for those interior weights its b phases share frequency and remain unselected",
            "for every interior weight global-tick substitution admits all-LOW/all-HIGH subsequences",
            "single accumulator initialized by x_0=0",
            "no physical context, counter origin, update law, sampler, randomness or L6 measure",
        ),
        "QDD-FINITE-MEMORY-O2B-BOUNDARY": (
            "unbounded, nonlinear, mixed, irrational and differently typed architectures remain outside scope",
        ),
        "QDD-EVENT-CONTEXT-BANK": (
            "active architecture supplies no ready phase, persistence law or registered gate",
            "no O1 closure, randomness or L6 measure",
        ),
    }
    v60_rows = set(v60_theorems) | set(v60_obligations)
    v60_actual_dependencies = {
        claim: {
            (row["depends_on"], row["relation"])
            for row in dependencies if row["item_id"] == claim
        }
        for claim in v60_rows
    }
    checks.append((
        "V60-BOUNDARY",
        "thirteen post-v59 theorem rows and two explicit O2 children keep exact evidence and dependency contracts while O1, the parent apparatus, physical adoption, gates, and sampling stay open",
        all(
            has_status(index, claim, "T")
            and normative.get(claim, {}).get("item_type") == "THEOREM"
            and normative.get(claim, {}).get("status") == "T"
            and normative.get(claim, {}).get("layer") == layer
            and normative.get(claim, {}).get("gate_ids") == ""
            and index.get(claim, {}).get("canon_section") == section
            and index.get(claim, {}).get("evidence") == path
            and evidence.get(claim, {}).get("evidence_kind") == "PUBLIC_PROBE"
            and evidence.get(claim, {}).get("location") == path
            and evidence.get(claim, {}).get("sha256") == digest
            and evidence.get(claim, {}).get("hash_mode")
            == "bundle-manifest-sha256-v1"
            and evidence.get(claim, {}).get("architecture_requirement")
            == "two-architecture"
            and claim not in programs
            and scope_contains_all(index, claim, v60_scope_boundaries[claim])
            for claim, (layer, section, path, digest) in v60_theorems.items()
        )
        and all(
            has_status(index, claim, "O")
            and normative.get(claim, {}).get("item_type") == "OBLIGATION"
            and normative.get(claim, {}).get("status") == "O"
            and normative.get(claim, {}).get("layer") == layer
            and normative.get(claim, {}).get("gate_ids") == ""
            and index.get(claim, {}).get("canon_section")
            == "2. Time, space, and the decoder"
            and index.get(claim, {}).get("evidence") == "inline"
            and evidence.get(claim, {}).get("evidence_kind") == "INLINE_CANON"
            and evidence.get(claim, {}).get("location") == "inline"
            and evidence.get(claim, {}).get("sha256") == digest
            and evidence.get(claim, {}).get("sha256")
            == scope_sha256(index, claim)
            and evidence.get(claim, {}).get("hash_mode")
            == "registry-scope-sha256-v1"
            and evidence.get(claim, {}).get("architecture_requirement") == "none"
            and programs.get(claim) == {
                "claim_id": claim,
                "program_id": "DECODER_CORE",
                "queue_role": "FOLLOWUP",
                "work_state": "STOP",
                "work_mode": "FORMAL",
            }
            for claim, (layer, digest) in v60_obligations.items()
        )
        and v60_actual_dependencies == v60_dependencies
        and all(
            scope_sha256(index, claim) == digest
            for claim, digest in v60_scope_hashes.items()
        )
        and all(row["owner_item_id"] not in v60_rows for row in gates.values())
        and "GATE-L4-L1-QDD-PURE-RECORD" not in gates
        and "GATE-L1-L5-QDD-EVENT-CARRY-BANK" not in gates
        and has_status(index, "CARRY-PENTAD", "T")
        and has_status(index, "QDD-INSTRUMENT-APPARATUS", "O")
        and qdd_current_split
        and has_status(index, "BELL-CAUSAL-ACCOUNTING", "O")
        and evidence["QDD-INSTRUMENT-APPARATUS"]["sha256"]
        == scope_sha256(index, "QDD-INSTRUMENT-APPARATUS")
        and programs.get("QDD-INSTRUMENT-APPARATUS") == {
            "claim_id": "QDD-INSTRUMENT-APPARATUS",
            "program_id": "DECODER_CORE",
            "queue_role": "FOLLOWUP",
            "work_state": "STOP",
            "work_mode": "FORMAL",
        }
        and scope_contains_all(
            index, "QDD-TERMINAL-EVENT-SEMANTICS",
            ("independently justified target-independent physical meaning",
             "functional terminality, read-only decoder output and completion-contract conformance provably do not imply saturation",
             "no physical saturation law is adopted",
             "without COMM-SAT, Xi_T=0, projective idempotence, +/-Q, Lueder or target effects as construction inputs",
             "independently testable consequence outside the selector target"),
        )
        and scope_contains_all(
            index, "QDD-INSTRUMENT-CLASS-COMPLETENESS",
            ("complete target-independent physical preselection class and equality",
             "every admitted memory and ready/preparation state",
             "supplies neither global physical completeness nor phase independence",
             "finite and unbounded memory, nonlinear, mixed, irrational and differently typed architectures",
             "phase relabeling, ready phases, transition permutations and future-output dependence"),
        )
        and scope_contains_all(
            index, "QDD-INSTRUMENT-APPARATUS",
            ("sole owner of the physical debt split from QUADRATIC-DECODER-DATA",
             "effect_ids, instrument_ids, apparatus_carrier_id",
             "target-independence and class-completeness certificates",
             "persistence/update/reset law",
             "all remain UNRESOLVED",
             "L1-to-L5 gate",
             "any L6 measure requiring a separate gate",
             "sampling, randomness or independence",
             "SAMPLING NOT PROVIDED rather than impossible"),
        ),
    ))

    v61_rows = {
        "J-BINARY-NORM-INDEX": (
            "T", "THEOREM", "probes/P-J-BINARY-NORM-INDEX-1",
            "626f598fb7a4cdd331208d28c60ed9fc15d9ac6412ecc003c5bf4dd0dfc4682e",
            "279407082e3182d01812cba3e2e5cdc6fa8bdb790a33199f96edbbed99b12c89",
            (
                "index exactly p-1",
                "can generate the whole inert residue multiplicative group only at p=2",
                "four 1+zeta_5^a form one Frobenius orbit",
                "no axiom exponent or physical characteristic-two selection is claimed",
            ),
        ),
        "J-BINARY-NORM-ORDER-CENSUS": (
            "C", "COMPUTATION", "probes/P-J-BINARY-NORM-INDEX-1",
            "626f598fb7a4cdd331208d28c60ed9fc15d9ac6412ecc003c5bf4dd0dfc4682e",
            "3fd14ba4c97679659010b9067bb290dd255b51a55d714d1d820e450760c3f23a",
            (
                "156 rational primes p<2000",
                "exactly at p=2 and p=3",
                "finite range only, no all-prime theorem",
            ),
        ),
        "RECORD-QUOTIENT-CALCULUS": (
            "T", "THEOREM", "probes/P-RECORD-QUOTIENT-CALCULUS-1",
            "5b0c0a4327539b7426de78bb54f03d525c32c94673c5113ce1c009bb274e92ff",
            "f8c28c6ef063d004a30b72069e89772062b12422e8f09247762cfa32ba7ebf5b",
            (
                "Idem(R/I)~=P(Supp(I))",
                "R/I->R/rad(I) is bijective on idempotents",
                "L(R/I)=max_P e_P",
                "exists uniquely exactly when I is contained in J",
                "no ideal, atom, event semantics, decoder, measure, coarse-graining, RG or continuum reading",
            ),
        ),
        "J-ODD-MOTOR-MEDIATED-BRIDGE": (
            "T", "THEOREM", "probes/P-J-ODD-MOTOR-MEDIATED-BRIDGE-COVERAGE-2",
            "f6b2ca8bf117ee709eba29356b4e5ad61e60801c1975e5405cab1fefbbaa624b",
            "a1f5d43376bafced23478edd0857dfc2c2d1566ee960db32e8d67d493191ad9a",
            (
                "exactly two primitive nonzero rank-two invariant sectors",
                "exact block graph is P<->C<->R",
                "B^sharp B=(5/4)R",
                "active C-line squared overlap 1/5",
                "repeated 2V remains a nonselection boundary",
                "no physical resonance or L2-L6 reading",
            ),
        ),
    }
    v61_dependencies = {
        "J-BINARY-NORM-INDEX": {("J-UNIT", "REQUIRES")},
        "J-BINARY-NORM-ORDER-CENSUS": {
            ("J-BINARY-NORM-INDEX", "REQUIRES"),
        },
        "RECORD-QUOTIENT-CALCULUS": set(),
        "J-ODD-MOTOR-MEDIATED-BRIDGE": {
            ("AFFINE-READING-DEGREE-CENSUS", "REQUIRES"),
            ("AFFINE-QUADRATIC-FORM-UNIQUENESS", "REQUIRES"),
        },
    }
    v61_actual_dependencies = {
        claim: {
            (row["depends_on"], row["relation"])
            for row in dependencies if row["item_id"] == claim
        }
        for claim in v61_rows
    }
    v61_incoming_dependencies = {
        (row["item_id"], row["depends_on"], row["relation"])
        for row in dependencies if row["depends_on"] in v61_rows
    }
    v61_carry_pentad_dependencies = {
        (row["depends_on"], row["relation"])
        for row in dependencies if row["item_id"] == "CARRY-PENTAD"
    }
    v61_history = {
        row["claim_id"]: row
        for row in history
        if row["event_id"].startswith("CANON61-DECLARE-")
    }
    checks.append((
        "V61-EXACT",
        "four post-v60 L1 rows keep exact status, evidence, dependencies and nonselection firewalls with no gate or frontier move",
        all(
            has_status(index, claim, status)
            and normative.get(claim, {}).get("item_type") == item_type
            and normative.get(claim, {}).get("claim_id") == claim
            and normative.get(claim, {}).get("status") == status
            and normative.get(claim, {}).get("layer") == "L1"
            and normative.get(claim, {}).get("gate_ids") == ""
            and normative.get(claim, {}).get("statement_source")
            == "canon/CANON.md::3. The kernel and the census"
            and index.get(claim, {}).get("canon_section")
            == "3. The kernel and the census"
            and index.get(claim, {}).get("evidence") == path
            and evidence.get(claim, {}).get("evidence_id") == f"EV-{claim}"
            and evidence.get(claim, {}).get("evidence_kind") == "PUBLIC_PROBE"
            and evidence.get(claim, {}).get("location") == path
            and evidence.get(claim, {}).get("sha256") == evidence_hash
            and evidence.get(claim, {}).get("hash_mode")
            == "bundle-manifest-sha256-v1"
            and evidence.get(claim, {}).get("architecture_requirement")
            == "two-architecture"
            and scope_sha256(index, claim) == scope_hash
            and scope_contains_all(index, claim, boundaries)
            and claim not in programs
            for claim, (
                status, item_type, path, evidence_hash, scope_hash, boundaries
            ) in v61_rows.items()
        )
        and v61_actual_dependencies == v61_dependencies
        and v61_incoming_dependencies == {
            ("J-BINARY-NORM-ORDER-CENSUS", "J-BINARY-NORM-INDEX", "REQUIRES"),
        }
        and v61_carry_pentad_dependencies == {
            ("J-UNIT", "REQUIRES"),
            ("J-STEP", "REQUIRES"),
            ("CODEC-TR4", "REQUIRES"),
        }
        and set(v61_history) == set(v61_rows)
        and all(
            row["event_id"] == f"CANON61-DECLARE-{claim}"
            and row["event_sequence"] == "1"
            and row["event_date"] == "2026-08-23"
            and row["release"] == "canon-v61-candidate"
            and row["event_type"] == "DECLARE"
            and row["previous_status"] == "-"
            and row["new_status"] == v61_rows[claim][0]
            and row["scope_sha256"] == v61_rows[claim][4]
            and row["evidence_id"] == f"EV-{claim}"
            and row["evidence_location"] == (
                "probes/P-J-ODD-MOTOR-MEDIATED-BRIDGE-2" if claim == "J-ODD-MOTOR-MEDIATED-BRIDGE"
                else v61_rows[claim][2]
            )
            and row["evidence_sha256"] == (
                "03db973566ae068b5ed8eb65f4e79ae13af398ac067f325c26a25c1553bf636b" if claim == "J-ODD-MOTOR-MEDIATED-BRIDGE"
                else v61_rows[claim][3]
            )
            for claim, row in v61_history.items()
        )
        and all(row["owner_item_id"] not in v61_rows for row in gates.values()),
    ))

    v62_events = [
        row for row in history
        if row["claim_id"] == "J-ODD-MOTOR-MEDIATED-BRIDGE"
        and row["event_id"] == "CANON62-EVIDENCE-J-ODD-MOTOR-MEDIATED-BRIDGE"
    ]
    checks.append((
        "V62-MAINTENANCE",
        "v62 changes only the odd-motor evidence pointer and one lifecycle event while status, scope, dependencies, gates and science counts stay fixed",
        len(v62_events) == 1
        and has_status(index, "J-ODD-MOTOR-MEDIATED-BRIDGE", "T")
        and scope_sha256(index, "J-ODD-MOTOR-MEDIATED-BRIDGE") == "a1f5d43376bafced23478edd0857dfc2c2d1566ee960db32e8d67d493191ad9a"
        and index["J-ODD-MOTOR-MEDIATED-BRIDGE"]["evidence"] == "probes/P-J-ODD-MOTOR-MEDIATED-BRIDGE-COVERAGE-2"
        and evidence["J-ODD-MOTOR-MEDIATED-BRIDGE"]["evidence_id"] == "EV-J-ODD-MOTOR-MEDIATED-BRIDGE"
        and evidence["J-ODD-MOTOR-MEDIATED-BRIDGE"]["evidence_kind"] == "PUBLIC_PROBE"
        and evidence["J-ODD-MOTOR-MEDIATED-BRIDGE"]["location"] == "probes/P-J-ODD-MOTOR-MEDIATED-BRIDGE-COVERAGE-2"
        and evidence["J-ODD-MOTOR-MEDIATED-BRIDGE"]["sha256"] == "f6b2ca8bf117ee709eba29356b4e5ad61e60801c1975e5405cab1fefbbaa624b"
        and evidence["J-ODD-MOTOR-MEDIATED-BRIDGE"]["hash_mode"] == "bundle-manifest-sha256-v1"
        and evidence["J-ODD-MOTOR-MEDIATED-BRIDGE"]["architecture_requirement"] == "two-architecture"
        and {
            (row["depends_on"], row["relation"])
            for row in dependencies if row["item_id"] == "J-ODD-MOTOR-MEDIATED-BRIDGE"
        } == {
            ("AFFINE-READING-DEGREE-CENSUS", "REQUIRES"),
            ("AFFINE-QUADRATIC-FORM-UNIQUENESS", "REQUIRES"),
        }
        and normative["J-ODD-MOTOR-MEDIATED-BRIDGE"]["status"] == "T"
        and normative["J-ODD-MOTOR-MEDIATED-BRIDGE"]["layer"] == "L1"
        and normative["J-ODD-MOTOR-MEDIATED-BRIDGE"]["gate_ids"] == ""
        and all(row["owner_item_id"] != "J-ODD-MOTOR-MEDIATED-BRIDGE" for row in gates.values())
        and v62_events[0]["event_sequence"] == "2"
        and v62_events[0]["event_date"] == "2026-08-24"
        and v62_events[0]["release"] == "canon-v62-candidate"
        and v62_events[0]["event_type"] == "EVIDENCE_CHANGE"
        and v62_events[0]["previous_status"] == "T"
        and v62_events[0]["new_status"] == "T"
        and v62_events[0]["scope_sha256"] == "a1f5d43376bafced23478edd0857dfc2c2d1566ee960db32e8d67d493191ad9a"
        and v62_events[0]["evidence_id"] == "EV-J-ODD-MOTOR-MEDIATED-BRIDGE"
        and v62_events[0]["evidence_location"] == "probes/P-J-ODD-MOTOR-MEDIATED-BRIDGE-COVERAGE-2"
        and v62_events[0]["evidence_sha256"] == "f6b2ca8bf117ee709eba29356b4e5ad61e60801c1975e5405cab1fefbbaa624b"
    ))

    fw_requires = {}
    for row in dependencies:
        fw_requires.setdefault(row["item_id"], set()).add(row["depends_on"])
    fw_seen, fw_stack = set(), ["DEF-QDD-DIRECT-WRITE"]
    while fw_stack:
        fw_cur = fw_stack.pop()
        for fw_nxt in fw_requires.get(fw_cur, ()):
            if fw_nxt not in fw_seen:
                fw_seen.add(fw_nxt)
                fw_stack.append(fw_nxt)
    fw_qdd = {x for x in fw_seen if x.startswith("DEF-QDD-") or x.startswith("QDD-")}
    v63_events = [
        row for row in history if row["release"].startswith("canon-v63")
    ]
    checks.append((
        "V63-HYGIENE",
        "v63 moves no registry row, evidence pointer or lifecycle event; the "
        "fold is repository hygiene and fifteen terminal pin records",
        not v63_events,
    ))

    v64_claim = "J-SIGNED-TRACE-MAHLER-RIGIDITY"
    v64_events = [
        row for row in history
        if row["claim_id"] == v64_claim
        and row["event_id"] == "CANON64-DECLARE-J-SIGNED-TRACE-MAHLER-RIGIDITY"
    ]
    checks.append((
        "V64-MAHLER",
        "signed-trace Mahler rigidity enters at T/L1 on its completed "
        "two-architecture public probe while broader binary facts remain "
        "non-owning probe controls and no matrix, selector, physical or higher-layer claim moves",
        has_status(index, v64_claim, "T")
        and index[v64_claim]["canon_section"]
        == "1. The axiom and the two projections"
        and index[v64_claim]["evidence"]
        == "probes/P-J-SIGNED-TRACE-MAHLER-RIGIDITY-1"
        and scope_sha256(index, v64_claim)
        == "fa27353483b531477c53e4b34b9c1035571e9a334882eb9b11592a8b67312f09"
        and scope_contains_all(index, v64_claim, (
            "every monic integer quartic",
            "no unit-circle root",
            "exactly two roots outside and two inside",
            "m(f)>=phi^2",
            "equality iff",
            "j-mahler-measure retains ownership",
            "this row owns only the global lower bound and unique equality case",
            "characteristic-polynomial classification only",
            "no integral conjugacy",
            "no integral conjugacy, ideal-class, marked-lift, basis, selector, decoder, generation, sampling, physical or l2-l6 claim",
        ))
        and normative[v64_claim]["item_type"] == "THEOREM"
        and normative[v64_claim]["status"] == "T"
        and normative[v64_claim]["layer"] == "L1"
        and normative[v64_claim]["gate_ids"] == ""
        and evidence[v64_claim]["evidence_id"]
        == "EV-J-SIGNED-TRACE-MAHLER-RIGIDITY"
        and evidence[v64_claim]["evidence_kind"] == "PUBLIC_PROBE"
        and evidence[v64_claim]["location"]
        == "probes/P-J-SIGNED-TRACE-MAHLER-RIGIDITY-1"
        and evidence[v64_claim]["sha256"]
        == "bad0139dd99002460039021687a7770822a877993ab1d40f97ebfb587407f7e5"
        and evidence[v64_claim]["hash_mode"] == "bundle-manifest-sha256-v1"
        and evidence[v64_claim]["architecture_requirement"] == "two-architecture"
        and {
            (row["depends_on"], row["relation"])
            for row in dependencies if row["item_id"] == v64_claim
        } == {("J-MAHLER-MEASURE", "REQUIRES")}
        and has_status(index, "J-MAHLER-MEASURE", "T")
        and all(row["owner_item_id"] != v64_claim for row in gates.values())
        and v64_claim not in programs
        and len(v64_events) == 1
        and v64_events[0]["event_sequence"] == "1"
        and v64_events[0]["event_date"] == "2026-08-25"
        and v64_events[0]["release"] == "canon-v64-candidate"
        and v64_events[0]["event_type"] == "DECLARE"
        and v64_events[0]["previous_status"] == "-"
        and v64_events[0]["new_status"] == "T"
        and v64_events[0]["scope_sha256"]
        == "fa27353483b531477c53e4b34b9c1035571e9a334882eb9b11592a8b67312f09"
        and v64_events[0]["evidence_id"]
        == "EV-J-SIGNED-TRACE-MAHLER-RIGIDITY"
        and v64_events[0]["evidence_location"]
        == "probes/P-J-SIGNED-TRACE-MAHLER-RIGIDITY-1"
        and v64_events[0]["evidence_sha256"]
        == "bad0139dd99002460039021687a7770822a877993ab1d40f97ebfb587407f7e5",
    ))

    checks.append((
        "QDD-DIRECT-FIREWALL",
        "the definitional closure of DEF-QDD-DIRECT-WRITE in the dependency ledger is exactly the domain, the balanced piston, the amplitude, the coefficient data, the trace pairing, the LOW LINE and the record schema, and contains no factor-side object (Gram, dagger, transpose, Q_QDD, the carrier equality, the projectors, the branch-weight pairing, the factor map)",
        fw_qdd == {"DEF-QDD-DOMAIN-K0", "DEF-QDD-BALANCED-PISTON",
                   "DEF-QDD-AMPLITUDE-B0", "DEF-QDD-COEFFICIENT-Q",
                   "DEF-QDD-TRACE-PAIRING", "DEF-QDD-LOW-LINE",
                   "DEF-QDD-MATTER-RECORD"}
        and not fw_seen & {"DEF-QDD-GRAM", "DEF-QDD-DAGGER", "DEF-QDD-TRANSPOSE",
                           "DEF-QDD-QPAIR", "DEF-QDD-QCARRIER-EQUALITY",
                           "DEF-QDD-PROJECTOR-LOW", "DEF-QDD-PROJECTOR-HIGH",
                           "DEF-QDD-BRANCH-WEIGHT-PAIRING", "DEF-QDD-FACTOR-MAP"},
    ))

    v65_period = "J-RESIDUE-PERIOD"
    v65_collapse = "J-RESIDUE-COLLAPSE-FIVE"
    v65_probe = "probes/P-J-RESIDUE-PERIOD-1"
    v65_bundle = "c09e55027c62d7af1e2deb256275a1a392f2374218c0e74d1dca088b45f2708e"
    v65_events = {
        row["claim_id"]: row for row in history
        if row["event_id"] in (
            "CANON65-DECLARE-J-RESIDUE-PERIOD",
            "CANON65-DECLARE-J-RESIDUE-COLLAPSE-FIVE",
        )
    }
    checks.append((
        "V65-RESIDUE",
        "the rational-modulus residue period of J and the exact five-fold "
        "collapse at one chosen prime enter at T/L1 on their completed "
        "two-architecture public probe, with the inert prime two left to "
        "J-BINARY-NORM-INDEX and no archimedean, automaton, spectrum, "
        "selector, physical or higher-layer claim moving",
        all(has_status(index, claim, "T") for claim in (v65_period, v65_collapse))
        and all(index[claim]["canon_section"] == "1. The axiom and the two projections"
                for claim in (v65_period, v65_collapse))
        and all(index[claim]["evidence"] == v65_probe
                for claim in (v65_period, v65_collapse))
        and scope_sha256(index, v65_period)
        == "41567caea0bb7f7373f0d2468a62bfdcfdac9b0c0cf85dd0e53b561b195854a8"
        and scope_sha256(index, v65_collapse)
        == "77228dcd68dc66bbc0eab3d22ed6a428579baadfa18195e1fdc5a55f626d98b2"
        and scope_contains_all(index, v65_period, (
            "every rational integer m >= 2",
            "the pisano period of m",
            "det m_j = 1 makes x -> jx a permutation",
            "the word rational is load-bearing",
            "j-binary-norm-index and is cited here, not restated",
            "no automaton interpretation",
            "no hamiltonian spectrum",
        ))
        and scope_contains_all(index, v65_collapse, (
            "the quotient l/k divides 5",
            "the prime ideal above 11 carrying zeta_5 -> 3 in f_11",
            "the cost of that choice is exactly the factor five",
            "no physical reading of the collapse factor",
        ))
        and scope_lacks(index, v65_period, ("gravity", "electromagnetism", "hamiltonian spectrum is"))
        and all(normative[claim]["item_type"] == "THEOREM"
                and normative[claim]["status"] == "T"
                and normative[claim]["layer"] == "L1"
                and normative[claim]["gate_ids"] == ""
                for claim in (v65_period, v65_collapse))
        and all(evidence[claim]["evidence_id"] == "EV-" + claim
                and evidence[claim]["evidence_kind"] == "PUBLIC_PROBE"
                and evidence[claim]["location"] == v65_probe
                and evidence[claim]["sha256"] == v65_bundle
                and evidence[claim]["hash_mode"] == "bundle-manifest-sha256-v1"
                and evidence[claim]["architecture_requirement"] == "two-architecture"
                for claim in (v65_period, v65_collapse))
        and {
            (row["depends_on"], row["relation"])
            for row in dependencies if row["item_id"] == v65_period
        } == {("J-UNIT", "REQUIRES"), ("J-STEP", "REQUIRES")}
        and {
            (row["depends_on"], row["relation"])
            for row in dependencies if row["item_id"] == v65_collapse
        } == {(v65_period, "REQUIRES")}
        and all(has_status(index, claim, "T")
                for claim in ("J-UNIT", "J-STEP", "J-BINARY-NORM-INDEX"))
        and all(row["owner_item_id"] not in (v65_period, v65_collapse)
                for row in gates.values())
        and v65_period not in programs
        and v65_collapse not in programs
        and set(v65_events) == {v65_period, v65_collapse}
        and all(v65_events[claim]["event_sequence"] == "1"
                and v65_events[claim]["event_date"] == "2026-08-25"
                and v65_events[claim]["release"] == "canon-v65-candidate"
                and v65_events[claim]["event_type"] == "DECLARE"
                and v65_events[claim]["previous_status"] == "-"
                and v65_events[claim]["new_status"] == "T"
                and v65_events[claim]["scope_sha256"] == scope_sha256(index, claim)
                and v65_events[claim]["evidence_id"] == "EV-" + claim
                and v65_events[claim]["evidence_location"] == v65_probe
                and v65_events[claim]["evidence_sha256"] == v65_bundle
                for claim in (v65_period, v65_collapse)),
    ))

    v66_row = "QUADRATIC-DECODER-DATA"
    v66_named = {
        "DEF-QDD-COEFFICIENT-Q", "DEF-QDD-BALANCED-PISTON", "DEF-QDD-DOMAIN-K0",
        "DEF-QDD-AMPLITUDE-B0", "DEF-QDD-GRAM", "DEF-QDD-DAGGER",
        "DEF-QDD-TRANSPOSE", "DEF-QDD-QCARRIER-EQUALITY", "DEF-QDD-QPAIR",
        "DEF-QDD-PROJECTOR-LOW", "DEF-QDD-PROJECTOR-HIGH",
        "DEF-QDD-BRANCH-WEIGHT-PAIRING", "DEF-QDD-MATTER-RECORD",
        "DEF-QDD-DIRECT-WRITE",
    }
    v66_lineage = {
        "DEF-ARCHITECTURE", "DEF-DECODER-MATTER",
        "DEF-DECODER-COMPLETION-CONTRACT", "COUPLINGS-DETERMINE",
        "QDD-ALGEBRAIC-FACTORIZATION",
    }
    v66_edges = {
        row["depends_on"] for row in dependencies
        if row["item_id"] == v66_row and row["relation"] == "REQUIRES"
    }
    v70_successor_edges = {
        row["depends_on"] for row in dependencies
        if row["item_id"] == qdd_successor and row["relation"] == "REQUIRES"
    }
    v66_events = [
        row for row in history if row["release"].startswith("canon-v66")
    ]
    checks.append((
        "V66-QDD-WIRING",
        "the historical nineteen-edge quadratic wiring is transferred exactly "
        "to the algebraic dictionary, with the Born lineage removed, the "
        "predecessor inactive, and the direct-write firewall unchanged",
        not v66_edges
        and v70_successor_edges == v66_named | v66_lineage
        and len(v70_successor_edges) == 19
        and "MEASURE-BORN-VERB" not in v70_successor_edges
        and qdd_current_split
        and not v66_events
        and not fw_qdd & (v66_named - {
            "DEF-QDD-COEFFICIENT-Q", "DEF-QDD-BALANCED-PISTON",
            "DEF-QDD-DOMAIN-K0", "DEF-QDD-AMPLITUDE-B0",
            "DEF-QDD-MATTER-RECORD", "DEF-QDD-DIRECT-WRITE",
        }),
    ))

    v67_theorems = (
        "J-RAPIDITY-GALOIS-EQUIVARIANT-PRIME-SHELL",
        "J-IDEAL-COUNT-QUADRATIC-CHARACTER",
        "J-IDEAL-RATIONAL-MOBIUS-DESCENT",
        "J-MERTENS-IDEAL-TWOSUM",
        "J-IDEAL-RAPIDITY-CHARACTER-LIFT",
        "J-RAPIDITY-TERNARY-SHELL-CENSUS",
        "J-ZERO-RAPIDITY-ORIENTATION-FACTORIZATION",
        "J-RAPIDITY-TERM-WISE-TRIANGLE-NOGO",
    )
    v67_bridge = "TRIVIAL-RAPIDITY-EVALUATION-BRIDGE"
    v67_probe_contract = {
        "J-RAPIDITY-GALOIS-EQUIVARIANT-PRIME-SHELL": (
            "probes/P-J-RAPIDITY-GALOIS-EQUIVARIANT-PRIME-SHELL-1",
            "99570433ba6df1b0af9d122b8d346626c00c1d9987a93f9c766624af05fbdb7c",
        ),
        "J-IDEAL-COUNT-QUADRATIC-CHARACTER": (
            "probes/P-J-IDEAL-RATIONAL-MOBIUS-DESCENT-1",
            "91bc03ae58804f952e83b59567eb2f257f06f533ec473a2b99c77c7d032e46ee",
        ),
        "J-IDEAL-RATIONAL-MOBIUS-DESCENT": (
            "probes/P-J-IDEAL-RATIONAL-MOBIUS-DESCENT-1",
            "91bc03ae58804f952e83b59567eb2f257f06f533ec473a2b99c77c7d032e46ee",
        ),
        "J-MERTENS-IDEAL-TWOSUM": (
            "probes/P-J-IDEAL-RATIONAL-MOBIUS-DESCENT-1",
            "91bc03ae58804f952e83b59567eb2f257f06f533ec473a2b99c77c7d032e46ee",
        ),
        "J-IDEAL-RAPIDITY-CHARACTER-LIFT": (
            "probes/P-J-IDEAL-RAPIDITY-CHARACTER-LIFT-1",
            "2463bbddbd5bc7158599d1493029331b2e7eb6a7bdfe6d87b15f52e154f11163",
        ),
        "J-RAPIDITY-TERNARY-SHELL-CENSUS": (
            "probes/P-J-IDEAL-RAPIDITY-CHARACTER-LIFT-1",
            "2463bbddbd5bc7158599d1493029331b2e7eb6a7bdfe6d87b15f52e154f11163",
        ),
        "J-ZERO-RAPIDITY-ORIENTATION-FACTORIZATION": (
            "probes/P-J-IDEAL-RAPIDITY-CHARACTER-LIFT-1",
            "2463bbddbd5bc7158599d1493029331b2e7eb6a7bdfe6d87b15f52e154f11163",
        ),
        "J-RAPIDITY-TERM-WISE-TRIANGLE-NOGO": (
            "probes/P-J-IDEAL-RAPIDITY-CHARACTER-LIFT-1",
            "2463bbddbd5bc7158599d1493029331b2e7eb6a7bdfe6d87b15f52e154f11163",
        ),
    }
    v67_dependency_contract = {
        "J-RAPIDITY-GALOIS-EQUIVARIANT-PRIME-SHELL": {
            "SPLIT-PRIME-RAPIDITY-INDEPENDENCE",
        },
        "J-IDEAL-COUNT-QUADRATIC-CHARACTER": {
            "J-GOLDEN-BRIDGE",
            "REGULATOR-TWO-LOG-PHI",
            "CYCLOTOMIC-CLASS-NUMBER-ONE",
        },
        "J-IDEAL-RATIONAL-MOBIUS-DESCENT": {
            "J-IDEAL-COUNT-QUADRATIC-CHARACTER",
        },
        "J-MERTENS-IDEAL-TWOSUM": {
            "J-IDEAL-RATIONAL-MOBIUS-DESCENT",
        },
        "J-IDEAL-RAPIDITY-CHARACTER-LIFT": {
            "J-IDEAL-RATIONAL-MOBIUS-DESCENT",
            "J-RAPIDITY-GALOIS-EQUIVARIANT-PRIME-SHELL",
            "ARITHMETIC-RAPIDITY-DECOMPOSITION",
            "SPLIT-PRIME-RAPIDITY-CLASS",
            "SPLIT-PRIME-RAPIDITY-INDEPENDENCE",
            "CYCLOTOMIC-CLASS-NUMBER-ONE",
        },
        "J-RAPIDITY-TERNARY-SHELL-CENSUS": {
            "J-IDEAL-RAPIDITY-CHARACTER-LIFT",
            "SPLIT-PRIME-RAPIDITY-INDEPENDENCE",
        },
        "J-ZERO-RAPIDITY-ORIENTATION-FACTORIZATION": {
            "J-IDEAL-RAPIDITY-CHARACTER-LIFT",
        },
        "J-RAPIDITY-TERM-WISE-TRIANGLE-NOGO": {
            "J-IDEAL-RAPIDITY-CHARACTER-LIFT",
        },
        v67_bridge: {
            "J-IDEAL-RAPIDITY-CHARACTER-LIFT",
        },
    }
    v67_actual_dependencies = {
        claim: {
            (row["depends_on"], row["relation"])
            for row in dependencies if row["item_id"] == claim
        }
        for claim in (*v67_theorems, v67_bridge)
    }
    v67_history_rows = [
        row for row in history if row["release"] == "canon-v67-candidate"
    ]
    v67_events = {row["claim_id"]: row for row in v67_history_rows}
    v67_event_claims = {*v67_theorems, v67_bridge, "DE-W-CONSTANT"}
    checks.append((
        "V67-RAPIDITY",
        "eight exact rapidity and ideal rows enter at T/L1 on their frozen public probes, the trivial-evaluation transfer stays an inline O/STOP obligation, and the exact dependency, lifecycle, gate and frontier boundaries create no analytic, physical or higher-layer promotion",
        all(has_status(index, claim, "T") for claim in v67_theorems)
        and all(index[claim]["canon_section"] == "10. Relativity as counting"
                for claim in v67_theorems)
        and all(normative[claim]["item_type"] == "THEOREM"
                and normative[claim]["status"] == "T"
                and normative[claim]["layer"] == "L1"
                and normative[claim]["gate_ids"] == ""
                for claim in v67_theorems)
        and all(evidence[claim]["evidence_id"] == "EV-" + claim
                and evidence[claim]["evidence_kind"] == "PUBLIC_PROBE"
                and evidence[claim]["location"] == v67_probe_contract[claim][0]
                and evidence[claim]["sha256"] == v67_probe_contract[claim][1]
                and evidence[claim]["hash_mode"]
                == "bundle-manifest-sha256-v1"
                and evidence[claim]["architecture_requirement"]
                == "two-architecture"
                for claim in v67_theorems)
        and all(v67_actual_dependencies[claim] == {
                    (dependency, "REQUIRES")
                    for dependency in v67_dependency_contract[claim]
                }
                for claim in v67_theorems)
        and all(row["owner_item_id"] not in v67_theorems
                for row in gates.values())
        and all(claim not in programs for claim in v67_theorems)
        and scope_contains_all(
            index, "J-RAPIDITY-GALOIS-EQUIVARIANT-PRIME-SHELL",
            ("without choosing an orientation", "nonsplit extension",
             "normalized Reynolds factor", "no global orientation"),
        )
        and scope_contains_all(
            index, "J-IDEAL-COUNT-QUADRATIC-CHARACTER",
            ("chi_A = chi_5", "exactly (1*chi_5)(n)",
             "sharp complete coefficient bound", "no rapidity orientation"),
        )
        and scope_contains_all(
            index, "J-IDEAL-RATIONAL-MOBIUS-DESCENT",
            ("mu = b*chi_5 = b*chi_A", "before scalarization",
             "no cancellation"),
        )
        and scope_contains_all(
            index, "J-MERTENS-IDEAL-TWOSUM",
            ("for every N>=1", "exact identities", "not an estimate"),
        )
        and scope_contains_all(
            index, "J-IDEAL-RAPIDITY-CHARACTER-LIFT",
            ("integral group-ring function bold_mu",
             "augmentation sends every local factor to 1-T",
             "distinct from the rational squarefree Reynolds lift"),
        )
        and scope_contains_all(
            index, "J-RAPIDITY-TERNARY-SHELL-CENSUS",
            ("exactly 3^a", "squarefree-only", "augmentation zero"),
        )
        and scope_contains_all(
            index, "J-ZERO-RAPIDITY-ORIENTATION-FACTORIZATION",
            ("C_0(s)", "O_5(s)",
             "neither a rapidity character nor a twist"),
        )
        and scope_contains_all(
            index, "J-RAPIDITY-TERM-WISE-TRIANGLE-NOGO",
            ("T(N)", "N/4", "narrow attack-route no-go",
             "l2 cancellation"),
        )
        and has_status(index, v67_bridge, "O")
        and index[v67_bridge]["evidence"] == "inline"
        and index[v67_bridge]["canon_section"] == "18. The frontier"
        and normative[v67_bridge]["item_type"] == "OBLIGATION"
        and normative[v67_bridge]["status"] == "O"
        and normative[v67_bridge]["layer"] == "NOT_APPLICABLE"
        and normative[v67_bridge]["gate_ids"] == ""
        and evidence[v67_bridge]["evidence_id"] == "EV-" + v67_bridge
        and evidence[v67_bridge]["evidence_kind"] == "INLINE_CANON"
        and evidence[v67_bridge]["location"] == "inline"
        and evidence[v67_bridge]["sha256"] == scope_sha256(index, v67_bridge)
        and evidence[v67_bridge]["hash_mode"]
        == "registry-scope-sha256-v1"
        and evidence[v67_bridge]["architecture_requirement"] == "none"
        and v67_actual_dependencies[v67_bridge] == {
            ("J-IDEAL-RAPIDITY-CHARACTER-LIFT", "REQUIRES"),
        }
        and tuple(programs[v67_bridge][field] for field in
                  ("program_id", "queue_role", "work_state", "work_mode"))
        == ("ENRICHMENT", "ROOT", "STOP", "ENRICHMENT")
        and all(row["owner_item_id"] != v67_bridge for row in gates.values())
        and scope_contains_all(
            index, v67_bridge,
            ("uniform growing-mode diagonal route",
             "non-diagonal mixing or kernel route",
             "fixed nonzero integer mode", "no Hecke"),
        )
        and len(v67_history_rows) == 10
        and set(v67_events) == v67_event_claims
        and all(v67_events[claim]["event_sequence"] == "1"
                and v67_events[claim]["event_date"] == "2026-08-27"
                and v67_events[claim]["event_type"] == "DECLARE"
                and v67_events[claim]["previous_status"] == "-"
                and v67_events[claim]["new_status"] == "T"
                and v67_events[claim]["scope_sha256"]
                == scope_sha256(index, claim)
                and v67_events[claim]["evidence_id"] == "EV-" + claim
                and v67_events[claim]["evidence_location"]
                == v67_probe_contract[claim][0]
                and v67_events[claim]["evidence_sha256"]
                == v67_probe_contract[claim][1]
                for claim in v67_theorems)
        and v67_events[v67_bridge]["event_sequence"] == "1"
        and v67_events[v67_bridge]["event_date"] == "2026-08-27"
        and v67_events[v67_bridge]["event_type"] == "DECLARE"
        and v67_events[v67_bridge]["previous_status"] == "-"
        and v67_events[v67_bridge]["new_status"] == "O"
        and v67_events[v67_bridge]["scope_sha256"]
        == scope_sha256(index, v67_bridge)
        and v67_events[v67_bridge]["evidence_id"] == "EV-" + v67_bridge
        and v67_events[v67_bridge]["evidence_location"] == "inline"
        and v67_events[v67_bridge]["evidence_sha256"]
        == scope_sha256(index, v67_bridge)
        and v67_events["DE-W-CONSTANT"]["event_sequence"] == "2"
        and v67_events["DE-W-CONSTANT"]["event_date"] == "2026-08-27"
        and v67_events["DE-W-CONSTANT"]["event_type"] == "STATUS_CHANGE"
        and v67_events["DE-W-CONSTANT"]["previous_status"] == "H"
        and v67_events["DE-W-CONSTANT"]["new_status"] == "F"
        and v67_events["DE-W-CONSTANT"]["scope_sha256"]
        == scope_sha256(index, "DE-W-CONSTANT")
        and v67_events["DE-W-CONSTANT"]["evidence_id"]
        == "EV-DE-W-CONSTANT"
        and v67_events["DE-W-CONSTANT"]["evidence_location"]
        == "probes/P-DE-W-ARMING-2"
        and v67_events["DE-W-CONSTANT"]["evidence_sha256"]
        == "de047b7352a06cfa2ab5a71f128bc9f57bef41c9be4456af3ddc21e2863b5f17",
    ))

    v68_claim = "SO3-FINITE-ANISOTROPY-MAXIMUM"
    v68_events = [
        row for row in history
        if row["event_id"]
        == "CANON68-DECLARE-SO3-FINITE-ANISOTROPY-MAXIMUM"
    ]
    checks.append((
        "V68-SO3",
        "the finite SO(3) harmonic-depth maximum enters at T/L1 on its "
        "proof-first two-architecture public probe while no boost, "
        "Lorentz-density, J, physical p=5, decoder, measure, dynamics or "
        "higher-layer selection moves",
        has_status(index, v68_claim, "T")
        and index[v68_claim]["canon_section"] == "10. Relativity as counting"
        and index[v68_claim]["evidence"]
        == "probes/P-SO3-FINITE-ANISOTROPY-DEPTH-1"
        and scope_sha256(index, v68_claim)
        == "e5641ef4a454429e4756d652b9215dea4e80560613607050626eb9fa892ef75b"
        and scope_contains_all(index, v68_claim, (
            "for every finite subgroup g <= so(3)",
            "a(c_n)=1",
            "a(d_n)=2",
            "a(a_4)=3",
            "a(s_4)=4",
            "a(a_5)=6",
            "equality iff g is conjugate to the rotational icosahedral group a_5",
            "difference sqrt5 generates character field q(sqrt5)",
            "finite-rotation representation theory only",
            "no selection of j",
            "physical prime p=5",
            "no selection of j, the physical prime p=5, a boost or rapidity, lorentz density, decoder, measure, dynamics or l2-l6 lift",
        ))
        and normative[v68_claim]["item_type"] == "THEOREM"
        and normative[v68_claim]["status"] == "T"
        and normative[v68_claim]["layer"] == "L1"
        and normative[v68_claim]["gate_ids"] == ""
        and evidence[v68_claim]["evidence_id"] == "EV-" + v68_claim
        and evidence[v68_claim]["evidence_kind"] == "PUBLIC_PROBE"
        and evidence[v68_claim]["location"]
        == "probes/P-SO3-FINITE-ANISOTROPY-DEPTH-1"
        and evidence[v68_claim]["sha256"]
        == "0fd88c1b604fd351ad147e8b0fdecc553e6e27c96f7c861f28fc10b0eb527a15"
        and evidence[v68_claim]["hash_mode"] == "bundle-manifest-sha256-v1"
        and evidence[v68_claim]["architecture_requirement"]
        == "two-architecture"
        and not any(row["item_id"] == v68_claim for row in dependencies)
        and all(row["owner_item_id"] != v68_claim for row in gates.values())
        and v68_claim not in programs
        and f"- {v68_claim} [" not in core_text
        and len(v68_events) == 1
        and v68_events[0]["event_sequence"] == "1"
        and v68_events[0]["event_date"] == "2026-08-28"
        and v68_events[0]["release"] == "canon-v68-candidate"
        and v68_events[0]["claim_id"] == v68_claim
        and v68_events[0]["event_type"] == "DECLARE"
        and v68_events[0]["previous_status"] == "-"
        and v68_events[0]["new_status"] == "T"
        and v68_events[0]["scope_sha256"] == scope_sha256(index, v68_claim)
        and v68_events[0]["evidence_id"] == "EV-" + v68_claim
        and v68_events[0]["evidence_location"]
        == "probes/P-SO3-FINITE-ANISOTROPY-DEPTH-1"
        and v68_events[0]["evidence_sha256"]
        == "0fd88c1b604fd351ad147e8b0fdecc553e6e27c96f7c861f28fc10b0eb527a15",
    ))

    v69_contract = {
        "CM-ALTERNATING-PRIMARY-LATTICE-SEAM": {
            "section": "4. The two places",
            "path": "probes/P-CM-ALTERNATING-PRIMARY-LATTICE-SEAM-1",
            "scope_sha": (
                "4350d7f162389982e612565e05ab9e89c2ec772da28b0de56331b0ea1cdb8625"
            ),
            "row_sha": (
                "758bad67f00df98996e256861438780a3c031c615dee36c09b1bf952ac2f434a"
            ),
            "bundle": (
                "7261b8e5aaf485df7e5494c74239de8689c5247b6b13484544ffe763ac0f6cb6"
            ),
            "dependencies": {"CM-ALTERNATING-PENCIL", "J-STEP"},
            "scope_markers": (
                "index five and quotient Q=Z/5",
                "exact denominator five",
                "no Z[P]-linear retraction",
                "no action, h, hbar, phase, 2 pi",
                "L2-L6 lift is selected",
            ),
        },
        "CM-REAL-DIFFERENT-PRIMARY-SEAM": {
            "section": "4. The two places",
            "path": "probes/P-CM-REAL-DIFFERENT-PRIMARY-SEAM-1",
            "scope_sha": (
                "ea6f8e80853a919499a4fa35b620c42c6e03edc144d4d45c674193c99753db64"
            ),
            "row_sha": (
                "84be744f266a347462aa82183d9f91717967999d31676c8470a5eaf25d34830a"
            ),
            "bundle": (
                "2a6e4157d03890af972b8f6c29cea6b425e420802551daf6875825e9bbb7ba9e"
            ),
            "dependencies": {
                "CM-ALTERNATING-PRIMARY-LATTICE-SEAM",
                "CM-ALTERNATING-PENCIL",
                "PLENUM-POINT",
            },
            "scope_markers": (
                "e_H(E_Z)=d_F^-1 H_Z",
                "Ann_O(Q_seam)=d_F",
                "nonreduced order-25 resultant layer",
                "reduced order-five residue line O/d_F",
                "no discriminant-form isometry",
                "h, hbar, phase law, decoder, SI normalization or L2-L6 lift",
            ),
        },
        "RAMIFIED-TM-SYMPLECTIC-ORIENTATION": {
            "section": "3. The kernel and the census",
            "path": "probes/P-RAMIFIED-TM-SYMPLECTIC-ORIENTATION-2",
            "scope_sha": (
                "2dbd861d1def2874297db0699f13bdf01db85e634bd2ba011bcdf1786df7f696"
            ),
            "row_sha": (
                "e8b9bc06a16ac6fbcd8a87e0b31c836fd8a708ce474998fd68f9b3a07ccfcd63"
            ),
            "bundle": (
                "216fb9aebba6456046edfd16a5c29d8172db2364797011bcdfed37880d69d452"
            ),
            "dependencies": {
                "CM-ALTERNATING-PENCIL",
                "RAMIFIED-TM-LIFT",
                "CARRY-J-CHECKPOINT",
            },
            "scope_markers": (
                "epsilon(Omega_k)=chi_5(2^k)=(-1)^k",
                "equality of one binary count character on two different carriers",
                "psi_4=psi_6 carries opposite values",
                "direct Pfaffian reduction is not the QR/NQR bridge",
                "Pf(-w)=Pf(w)",
                "no action, h, hbar, 2 pi, phase law",
                "L2-L6 lift is selected",
            ),
        },
        "CM-RAMIFIED-PFAFFIAN-ROOT": {
            "section": "4. The two places",
            "path": "probes/P-CM-RAMIFIED-PFAFFIAN-ROOT-1",
            "scope_sha": (
                "553ae20d6f268b1ea093c4bc40979092e3074e4d769ded06f4c5cd8bed18fd1d"
            ),
            "row_sha": (
                "f102891bdd444e21ab188ca9263ad47607b7ea1b49cb55feb4f45524cd1cfbcc"
            ),
            "bundle": (
                "5c949e8f15a411942c41f6a9c85316642b37f3c25ede2a439a68f73d3094d722"
            ),
            "dependencies": {
                "CM-ALTERNATING-PENCIL",
                "RAMIFIED-TM-LIFT",
                "J-HARMONIC-SEAM",
                "J-GOLDEN-BRIDGE",
                "RAMIFIED-TM-SYMPLECTIC-ORIENTATION",
            },
            "scope_markers": (
                "five is the unique rational prime",
                "C2 quotient of this marked C4 phase",
                "kernel <-phi^2>",
                "marked is load-bearing",
                "the additive index-five primary-lattice seam is a different object",
                "no unmarked or Galois-invariant selector",
                "selector, action, h, hbar, 2 pi, SI normalization",
                "L2-L6 lift is selected",
            ),
        },
        "CM-PERIOD-LATTICE-NONSELECTION": {
            "section": "4. The two places",
            "path": "probes/P-CM-PERIOD-LATTICE-NONSELECTION-1",
            "scope_sha": (
                "0308870109048b23a7d0a6a9cf9a0f9b551735cd794d5e3f2718e67054b76a7b"
            ),
            "row_sha": (
                "95e6cf05f176c25f7f563fd6710a6fa739efa4f41952411d617dc14fe3c3fd0c"
            ),
            "bundle": (
                "a8b728effa5c936929e06a9da61447d8ae133dda4ba9b3030b0b84065ea2dc31"
            ),
            "dependencies": {"CM-ALTERNATING-PENCIL"},
            "scope_markers": (
                "Per_Z(Omega)={Omega(C):C in Lambda^2 L}",
                "every GL_4(Z) pullback preserves Per_Z",
                "one J-pullback does not scale it by phi^-2",
                "can return a unit-period bivector",
                "no nonzero decomposable rational fixed bivector",
                "integer image subgroup rather than a geometric period integral",
                "no torus, manifold, homology, cohomology, action, h, hbar, 2 pi",
                "L2-L6 lift is selected",
            ),
        },
    }
    v69_claims = tuple(v69_contract)
    v69_actual_dependencies = {
        claim: {
            (row["depends_on"], row["relation"])
            for row in dependencies if row["item_id"] == claim
        }
        for claim in v69_claims
    }
    v69_history_rows = [
        row for row in history if row["release"].startswith("canon-v69")
    ]
    v69_events = {row["claim_id"]: row for row in v69_history_rows}
    v69_excluded_claims = {
        "J-QUADRATIC-CARRY-NORM-SEAM",
        "THORN-PLENUM-QUADRANT-CHARACTERIZATION",
        "THORN-TRIANGLE-PENTAGON-RIGIDITY",
    }
    v69_excluded_evidence_locations = {
        "probes/P-J-QUADRATIC-CARRY-NORM-SEAM-1",
        "probes/P-J-QUADRATIC-CARRY-NORM-SEAM-2",
        "probes/P-RAMIFIED-TM-SYMPLECTIC-ORIENTATION-1",
        "probes/P-THORN-PLENUM-QUADRANT-CHARACTERIZATION-1",
        "probes/P-THORN-PLENUM-QUADRANT-CHARACTERIZATION-2",
        "probes/P-THORN-TRIANGLE-PENTAGON-RIGIDITY-1",
    }
    checks.append((
        "V69-CM",
        "five focused L1 CM lattice and ramification theorems keep exact "
        "scopes, evidence, dependencies and nonselection firewalls with no "
        "gate, Frontier, CORE or action bridge",
        all(has_status(index, claim, "T") for claim in v69_claims)
        and all(
            index[claim]["canon_section"] == v69_contract[claim]["section"]
            and index[claim]["evidence"] == v69_contract[claim]["path"]
            and scope_sha256(index, claim) == v69_contract[claim]["scope_sha"]
            and registry_row_sha256(index, claim)
            == v69_contract[claim]["row_sha"]
            and scope_contains_all(
                index, claim, v69_contract[claim]["scope_markers"]
            )
            for claim in v69_claims
        )
        and all(
            normative[claim]["item_type"] == "THEOREM"
            and normative[claim]["claim_id"] == claim
            and normative[claim]["status"] == "T"
            and normative[claim]["layer"] == "L1"
            and normative[claim]["gate_ids"] == ""
            and normative[claim]["statement_source"]
            == f"canon/CANON.md::{claim} [T]"
            for claim in v69_claims
        )
        and all(
            evidence[claim]["evidence_id"] == "EV-" + claim
            and evidence[claim]["evidence_kind"] == "PUBLIC_PROBE"
            and evidence[claim]["location"] == v69_contract[claim]["path"]
            and evidence[claim]["sha256"] == v69_contract[claim]["bundle"]
            and evidence[claim]["hash_mode"] == "bundle-manifest-sha256-v1"
            and evidence[claim]["architecture_requirement"]
            == "two-architecture"
            for claim in v69_claims
        )
        and all(
            v69_actual_dependencies[claim] == {
                (dependency, "REQUIRES")
                for dependency in v69_contract[claim]["dependencies"]
            }
            for claim in v69_claims
        )
        and all(
            normative[dependency]["status"] == "T"
            and normative[dependency]["layer"] in {"L1", "NOT_APPLICABLE"}
            for claim in v69_claims
            for dependency in v69_contract[claim]["dependencies"]
        )
        and len(v69_history_rows) == 5
        and set(v69_events) == set(v69_claims)
        and all(
            v69_events[claim]["event_id"] == f"CANON69-DECLARE-{claim}"
            and v69_events[claim]["event_sequence"] == "1"
            and v69_events[claim]["event_date"] == "2026-08-29"
            and v69_events[claim]["release"] == "canon-v69-candidate"
            and v69_events[claim]["event_type"] == "DECLARE"
            and v69_events[claim]["previous_status"] == "-"
            and v69_events[claim]["new_status"] == "T"
            and v69_events[claim]["scope_sha256"]
            == v69_contract[claim]["scope_sha"]
            and v69_events[claim]["evidence_id"] == "EV-" + claim
            and v69_events[claim]["evidence_location"]
            == v69_contract[claim]["path"]
            and v69_events[claim]["evidence_sha256"]
            == v69_contract[claim]["bundle"]
            for claim in v69_claims
        )
        and all(row["owner_item_id"] not in v69_claims for row in gates.values())
        and all(claim not in programs for claim in v69_claims)
        and all(f"- {claim} [" not in core_text for claim in v69_claims)
        and all(
            row["claim_id"] not in v69_claims for row in core_selection_rows
        )
        and all(
            claim not in index
            and claim not in normative
            and claim not in evidence
            and claim not in programs
            for claim in v69_excluded_claims
        )
        and all(
            row["location"] not in v69_excluded_evidence_locations
            for row in evidence.values()
        )
        and hashlib.sha256(CORE_SELECTION.read_bytes()).hexdigest() == (
            "eee121dd437d06fc2b0fda5377ea6c2e6e01b220e5f1bfb9aa09727885d03d4e"
        ),
    ))

    v70_contract = {
        "ALGEBRAIC-DMATTER": {
            "event_id": "CANON70-DECLARE-ALGEBRAIC-DMATTER",
            "sequence": "1",
            "event_type": "DECLARE",
            "previous": "-",
            "new": "D",
            "scope_sha": "b542d0f6d40c8ade93589334670156c2b5788ef5414a3a3efddc777ea7635d75",
            "row_sha": "41d4f53def45ba05ecd5d532ff2a145a0d16259a6df75a86d68a2e25950d71d4",
            "evidence_id": "EV-ALGEBRAIC-DMATTER",
            "evidence_location": "inline",
            "evidence_sha": "b542d0f6d40c8ade93589334670156c2b5788ef5414a3a3efddc777ea7635d75",
        },
        "READING-SPLIT": {
            "event_id": "CANON70-SCOPE-READING-SPLIT",
            "sequence": "14",
            "event_type": "SCOPE_CHANGE",
            "previous": "D",
            "new": "D",
            "scope_sha": "b503f0f6a30965623a09e826795bce4ce626b171340b2fecfa86fd0cf2818922",
            "row_sha": "e762db5b7554d1b57f9d7666338a672aec6d957235dbcfc7b6f2081c0d5b8151",
            "evidence_id": "EV-READING-SPLIT",
            "evidence_location": "inline",
            "evidence_sha": "b503f0f6a30965623a09e826795bce4ce626b171340b2fecfa86fd0cf2818922",
        },
        "QDD-ALGEBRAIC-FACTORIZATION": {
            "event_id": "CANON70-SCOPE-QDD-ALGEBRAIC-FACTORIZATION",
            "sequence": "2",
            "event_type": "SCOPE_CHANGE",
            "previous": "T",
            "new": "T",
            "scope_sha": "873c418ffee3ad66eaf9d7e279929aaa4172785a12c2081c4d2734e041ea939f",
            "row_sha": "8655df8ba78aca0c007ee5808605161247546d172935a43ead51f6f45fbe1999",
            "evidence_id": "EV-QDD-ALGEBRAIC-FACTORIZATION",
            "evidence_location": "reproduce/qdd-route-a",
            "evidence_sha": "897f18e27e822a96ece61048cb17d4a5488b267d014f2bb10787f1a56edc8c6a",
        },
        "QPAIR-HERM-INTEGER-NONDESCENT": {
            "event_id": "CANON70-SCOPE-QPAIR-HERM-INTEGER-NONDESCENT",
            "sequence": "2",
            "event_type": "SCOPE_CHANGE",
            "previous": "T",
            "new": "T",
            "scope_sha": "54c0338ff722ffe8e69a7435477adf43c704c15bbbf82967c50184f89dc4c697",
            "row_sha": "84ee9b37aaac46311ff4458ea3ea117258c8c4e418813c420284dc23b20706b3",
            "evidence_id": "EV-QPAIR-HERM-INTEGER-NONDESCENT",
            "evidence_location": "probes/P-QPAIR-C4-2I-MINIMALITY-1",
            "evidence_sha": "6f1d5a5859a193cb68eb53f6ed58f5da21b25f3c0084c3875eede690317ea592",
        },
        "QDD-INSTRUMENT-APPARATUS": {
            "event_id": "CANON70-SCOPE-QDD-INSTRUMENT-APPARATUS",
            "sequence": "6",
            "event_type": "SCOPE_CHANGE",
            "previous": "O",
            "new": "O",
            "scope_sha": "2aa1688ede2fa319cd0fad5467195f1df8a1ab5308f6cf725c0030abf48cb6f5",
            "row_sha": "06288f428275ed4dd79e399c3ea0b8f298e838ba32d4ab5d427c1cbed3133d21",
            "evidence_id": "EV-QDD-INSTRUMENT-APPARATUS",
            "evidence_location": "inline",
            "evidence_sha": "2aa1688ede2fa319cd0fad5467195f1df8a1ab5308f6cf725c0030abf48cb6f5",
        },
    }
    v70_retirement = {
        "event_id": "CANON70-RETIRE-QUADRATIC-DECODER-DATA",
        "sequence": "14",
        "event_type": "RETIRE",
        "previous": "O",
        "new": "RETIRED",
        "scope_sha": "8b2b79b5060bbea943429afda25f24affcda2bd9a55961965cf63a962b3cee8d",
        "evidence_id": "EV-QUADRATIC-DECODER-DATA",
        "evidence_location": "inline",
        "evidence_sha": "8b2b79b5060bbea943429afda25f24affcda2bd9a55961965cf63a962b3cee8d",
    }
    v70_history_rows = [
        row for row in history if row["release"] == "canon-v70-candidate"
    ]
    v70_events = {row["claim_id"]: row for row in v70_history_rows}
    v70_successor_dependencies = {
        "DEF-ARCHITECTURE", "DEF-DECODER-MATTER",
        "DEF-DECODER-COMPLETION-CONTRACT", "COUPLINGS-DETERMINE",
        "QDD-ALGEBRAIC-FACTORIZATION", "DEF-QDD-COEFFICIENT-Q",
        "DEF-QDD-BALANCED-PISTON", "DEF-QDD-DOMAIN-K0",
        "DEF-QDD-AMPLITUDE-B0", "DEF-QDD-GRAM", "DEF-QDD-DAGGER",
        "DEF-QDD-TRANSPOSE", "DEF-QDD-QCARRIER-EQUALITY",
        "DEF-QDD-QPAIR", "DEF-QDD-PROJECTOR-LOW",
        "DEF-QDD-PROJECTOR-HIGH", "DEF-QDD-BRANCH-WEIGHT-PAIRING",
        "DEF-QDD-MATTER-RECORD", "DEF-QDD-DIRECT-WRITE",
    }
    v70_reading_dependencies = {
        (row["depends_on"], row["relation"])
        for row in dependencies if row["item_id"] == "READING-SPLIT"
    }
    v70_apparatus_dependencies = {
        (row["depends_on"], row["relation"])
        for row in dependencies if row["item_id"] == qdd_apparatus
    }
    v70_successor_consumers = {
        (row["item_id"], row["relation"])
        for row in dependencies if row["depends_on"] == qdd_successor
    }
    v70_live_frontier = {
        row["claim_id"] for row in rows if row["status"] in {"H", "O"}
    }
    v70_apparatus_manifest_lines = (
        "apparatus_manifest.projector_target_ids =",
        "apparatus_manifest.effect_ids = (UNRESOLVED)",
        "apparatus_manifest.instrument_ids = (UNRESOLVED)",
        "apparatus_manifest.apparatus_carrier_id = UNRESOLVED",
        "apparatus_manifest.ready_state_id = UNRESOLVED",
        "apparatus_manifest.physical_context_key_id = UNRESOLVED",
        "apparatus_manifest.selected_ready_phase_id = UNRESOLVED",
        "apparatus_manifest.coupling_id = UNRESOLVED",
        "apparatus_manifest.pointer_id = UNRESOLVED",
        "apparatus_manifest.reduction_id = UNRESOLVED",
        "apparatus_manifest.target_comparison_relation_id = UNRESOLVED",
        "apparatus_manifest.target_comparison_domain_id = UNRESOLVED",
        "apparatus_manifest.complete_apparatus_family_class_id = UNRESOLVED",
        "apparatus_manifest.apparatus_family_equality_id = UNRESOLVED",
        "apparatus_manifest.phase_equality_id = UNRESOLVED",
        "apparatus_manifest.target_independence_certificate_id = UNRESOLVED",
        "apparatus_manifest.class_completeness_certificate_id = UNRESOLVED",
        "apparatus_manifest.realization_certificate_ids = (UNRESOLVED)",
        "apparatus_manifest.realized_outcome_ids = (UNRESOLVED)",
        "apparatus_manifest.realized_event_semantics_id = UNRESOLVED",
        "apparatus_manifest.occurrence_law_id = UNRESOLVED",
        "apparatus_manifest.post_state_instrument_ids = (UNRESOLVED)",
        "apparatus_manifest.persistence_update_reset_law_id = UNRESOLVED",
        "apparatus_manifest.zero_support_semantics_id = UNRESOLVED",
        "apparatus_manifest.l1_to_l5_gate_id = UNRESOLVED",
        "apparatus_manifest.l6_measure_boundary = REQUIRES_SEPARATE_GATE",
    )
    v70_algebraic_manifest_lines = (
        "stage_id = D_matter",
        "leg_id = D_quadratic",
        "domain_id = DEF-QDD-DOMAIN-K0",
        "codomain_id = DEF-QDD-MATTER-RECORD",
        "write_map_id = DEF-QDD-DIRECT-WRITE",
        "totality_domain_id = DEF-QDD-DOMAIN-K0",
        "(support_state, total_weight, branch_weights,",
        "density_state, normalized_weight_state)",
        "quadratic_manifest.coefficient_ring_id = DEF-QDD-COEFFICIENT-Q",
        "quadratic_manifest.effective_carrier_id = DEF-QDD-BALANCED-PISTON",
        "quadratic_manifest.orbit_to_amplitude_bridge_id = DEF-QDD-AMPLITUDE-B0",
        "quadratic_manifest.gram_id = DEF-QDD-GRAM",
        "quadratic_manifest.dagger_id = DEF-QDD-DAGGER",
        "quadratic_manifest.transpose_id = DEF-QDD-TRANSPOSE",
        "quadratic_manifest.qcarrier_id = DEF-QDD-QCARRIER-EQUALITY",
        "quadratic_manifest.q_equality_id = DEF-QDD-QCARRIER-EQUALITY",
        "quadratic_manifest.q_map_id = DEF-QDD-QPAIR",
        "quadratic_manifest.projector_ids =",
        "(DEF-QDD-PROJECTOR-LOW, DEF-QDD-PROJECTOR-HIGH)",
        "quadratic_manifest.branch_weight_pairing_id =",
        "DEF-QDD-BRANCH-WEIGHT-PAIRING",
        "quadratic_manifest.factorization_map_id = DEF-QDD-FACTOR-MAP",
        "quadratic_manifest.slot_boundary_id = QDD-QCARRIER-DIAGONAL-BOUNDARY",
        "quadratic_manifest.factorization_theorem_id =",
        "QDD-ALGEBRAIC-FACTORIZATION",
    )
    v70_frozen_manifest = {
        "EXPECTED.txt": (1145, "931b8de96b408a7a427103949e2d0a53111081df0a4d7072ad3b6788264f3880"),
        "MANIFEST.json": (16083, "561cfd403c126981342393c473846acbb7d54c2194cecff43ae1b3dc835636c7"),
        "README.md": (7162, "948df790610f4fde4e64013192ceda52dc0990bdfe1a16c650631700337154fa"),
        "verify.py": (34325, "32510c01386db17589104190424ddb76f47a05b4a7f429a613e2b83dd78af58e"),
    }
    v70_actual_manifest = {
        path.name: (
            path.stat().st_size,
            hashlib.sha256(path.read_bytes()).hexdigest(),
        )
        for path in SUCCESSOR_MANIFEST_DIR.iterdir() if path.is_file()
    }
    checks.append((
        "V70-QDD-SPLIT",
        "the composite quadratic O retires as a split; ALGEBRAIC-DMATTER is "
        "an owner-selected D/L1 dictionary with exact algebraic wiring and no "
        "gate, while all transferred physical debt stays on "
        "QDD-INSTRUMENT-APPARATUS at O/STOP",
        qdd_current_split
        and len(v70_history_rows) == 6
        and set(v70_events) == set(v70_contract) | {qdd_predecessor}
        and all(
            v70_events[claim]["event_id"] == contract["event_id"]
            and v70_events[claim]["event_sequence"] == contract["sequence"]
            and v70_events[claim]["event_date"] == "2026-08-29"
            and v70_events[claim]["event_type"] == contract["event_type"]
            and v70_events[claim]["previous_status"] == contract["previous"]
            and v70_events[claim]["new_status"] == contract["new"]
            and v70_events[claim]["scope_sha256"] == contract["scope_sha"]
            and v70_events[claim]["evidence_id"] == contract["evidence_id"]
            and v70_events[claim]["evidence_location"]
            == contract["evidence_location"]
            and v70_events[claim]["evidence_sha256"] == contract["evidence_sha"]
            and scope_sha256(index, claim) == contract["scope_sha"]
            and registry_row_sha256(index, claim) == contract["row_sha"]
            and evidence[claim]["evidence_id"] == contract["evidence_id"]
            and evidence[claim]["location"] == contract["evidence_location"]
            and evidence[claim]["sha256"] == contract["evidence_sha"]
            for claim, contract in v70_contract.items()
        )
        and all(
            v70_events[qdd_predecessor][field] == expected
            for field, expected in {
                "event_id": v70_retirement["event_id"],
                "event_sequence": v70_retirement["sequence"],
                "event_type": v70_retirement["event_type"],
                "previous_status": v70_retirement["previous"],
                "new_status": v70_retirement["new"],
                "scope_sha256": v70_retirement["scope_sha"],
                "evidence_id": v70_retirement["evidence_id"],
                "evidence_location": v70_retirement["evidence_location"],
                "evidence_sha256": v70_retirement["evidence_sha"],
            }.items()
        )
        and v70_events[qdd_predecessor]["event_date"] == "2026-08-29"
        and all(
            phrase in v70_events[qdd_predecessor]["rationale"].lower()
            for phrase in ("no falsifier fired",
                           "no positive closure or scientific result is recorded",
                           "rather than satisfied")
        )
        and v70_successor_edges == v70_successor_dependencies
        and v70_reading_dependencies == {
            ("DEF-ARCHITECTURE", "REQUIRES"),
            ("CODEC-TR4", "REQUIRES"),
            (qdd_successor, "REQUIRES"),
        }
        and v70_apparatus_dependencies == {
            ("DEF-QDD-PROJECTOR-LOW", "REQUIRES"),
            ("DEF-QDD-PROJECTOR-HIGH", "REQUIRES"),
            ("DEF-QDD-GRAM", "REQUIRES"),
            ("DEF-DECODER-COMPLETION-CONTRACT", "REQUIRES"),
        }
        and v70_successor_consumers == {
            ("READING-SPLIT", "REQUIRES"),
            ("POINTED-DECODER-PREFIX-CONSISTENCY", "BOUNDED_BY"),
        }
        and "MEASURE-BORN-VERB" not in v70_successor_edges
        and scope_contains_all(
            index, qdd_successor,
            ("owner-adopted L1 algebraic dictionary binds only",
             "D_matter|_(K_QDD,D_quadratic) := D_QDD_direct",
             "exactly five fields", "ordered algebraic projector pair",
             "algebraic branch-weight pairing", "total only on K_QDD",
             "owner architecture choice",
             "not a mathematically forced, unique or canonical route",
             "PHYSICAL-DMATTER remains unadopted, not falsified and not shown complete"),
        )
        and index[qdd_successor]["falsifier"] == ""
        and scope_contains_all(
            index, "READING-SPLIT",
            ("ALGEBRAIC-DMATTER only on (K_QDD,D_quadratic)",
             "L1 algebraic data", "not a physical effect, apparatus",
             "no totality beyond K_QDD", "other-leg closure"),
        )
        and scope_contains_all(
            index, "QPAIR-HERM-INTEGER-NONDESCENT",
            ("no bridge to DEF-QDD-QPAIR", "algebraic branch-weight pairing",
             "decoder write map", "or ALGEBRAIC-DMATTER",
             "no physical U(1), apparatus"),
        )
        and scope_contains_all(
            index, qdd_apparatus,
            ("sole owner of the physical debt split from QUADRATIC-DECODER-DATA",
             "transferred but not satisfied", "projector_target_ids",
             "are algebraic targets and are not aliases for physical effects",
             "effect_ids, instrument_ids, apparatus_carrier_id",
             "target-independence and class-completeness certificates",
             "persistence/update/reset law", "all remain UNRESOLVED",
             "any L6 measure requiring a separate gate",
             "do not close or partially satisfy this row",
             "PHYSICAL-DMATTER remains unadopted, not falsified and not shown complete",
             "SAMPLING NOT PROVIDED rather than impossible"),
        )
        and all(line in canon_text for line in v70_algebraic_manifest_lines)
        and all(line in canon_text for line in v70_apparatus_manifest_lines)
        and "an `ALGEBRAIC_ONLY` L1 `READOUT`" in canon_text
        and "there is no sixth field" in canon_text
        and "no `effect_ids` or `born_pairing_id`" in canon_text
        and "no algebraic identifier is an alias for a physical" in canon_text
        and "The debt is TRANSFERRED_NOT_SATISFIED." in canon_text
        and "PHYSICAL-DMATTER" not in index
        and "PHYSICAL-DMATTER" not in normative
        and "PHYSICAL-DMATTER" not in evidence
        and "PHYSICAL-DMATTER" not in programs
        and "QDD-PROJECTOR-APPARATUS" not in index
        and v70_live_frontier == set(programs)
        and f"- {qdd_predecessor} [" not in frontier_text
        and f"- {qdd_successor} [" not in frontier_text
        and f"- {qdd_apparatus} [O]:" in frontier_text
        and all(row["claim_id"] != qdd_successor for row in core_selection_rows)
        and f"- {qdd_successor} [" not in core_text
        and v70_actual_manifest == v70_frozen_manifest,
    ))

    v72_contract = {
        "FCC-WEIGHTED-SHELL-SYMBOL": {
            "status": "T",
            "item_type": "THEOREM",
            "layer": "L2",
            "gate_ids": "",
            "row_sha": "3d381847735954398dec73af73d3b85d6b113fc5a9847e67837c2fbc4b542f9f",
            "scope_sha": "c444163e61c5df5727b4d6925e49515d00db2ee3e607f58267489b544358ae53",
            "evidence_kind": "PUBLIC_PROBE",
            "location": "probes/P-FCC-WEIGHTED-SHELL-SYMBOL-1",
            "evidence_sha": "23522dc6c0fc91b8e7b6953be5922726e8de1d09f15bc3e43e5f63e1a162bd3f",
            "hash_mode": "bundle-manifest-sha256-v1",
            "architecture": "two-architecture",
            "scope_markers": (
                "unique positive integral solution of minimum total weight 24",
                "the exact sixth-order term is anisotropic",
                "no global remainder",
                "physical-photon conclusion",
            ),
        },
        "PHOTON-WILSON-VILLAIN-FINITE-COUPLING-NONMEMBERSHIP": {
            "status": "T",
            "item_type": "THEOREM",
            "layer": "L4",
            "gate_ids": "",
            "row_sha": "262439e776ad0da4a6d2e1c542b591c543d462b690b0eabd596a5a2334094dc3",
            "scope_sha": "a8cf70ace567afe5090d0927d30c6dbf5c3defc1aafae3ebca75a267d1199177",
            "evidence_kind": "PUBLIC_PROBE",
            "location": "probes/P-PHOTON-WILSON-VILLAIN-BRIDGE-1",
            "evidence_sha": "ea6cb44943cc5d98ffd4257d5ab84dfeefa4f06f929532369af186f2dd828bb7",
            "hash_mode": "bundle-manifest-sha256-v1",
            "architecture": "two-architecture",
            "scope_markers": (
                "unordered bi-support",
                "direct finite-coupling nonmembership",
                "no parameter limit",
                "no parameter limit, projective closure",
                "massless",
                "physical-photon conclusion",
            ),
        },
        "PHOTON-CONE-CONVERGENCE": {
            "status": "O",
            "item_type": "OBLIGATION",
            "layer": "MULTI",
            "gate_ids": (
                "GATE-L2-L5-PHOTON-TEMPORAL-CHARACTERISTIC;"
                "GATE-L4-L5-PHOTON-CONE-IDENTIFICATION"
            ),
            "row_sha": "ddbb22ed4ec217af13846e7213e0d8c853e119ab815f7727aca1f307d1fa5a4c",
            "scope_sha": "be3311e71496820cf13256dcee526143e196517255cb1542bea9d35301412ee6",
            "evidence_kind": "INLINE_CANON",
            "location": "inline",
            "evidence_sha": "be3311e71496820cf13256dcee526143e196517255cb1542bea9d35301412ee6",
            "hash_mode": "registry-scope-sha256-v1",
            "architecture": "none",
            "scope_markers": (
                "convergence here means agreement of the two typed routes",
                "not a continuum limit",
                "no Lorentz invariance",
                "physical-photon conclusion",
            ),
        },
        "PHOTON-MASSLESS-PHASE": {
            "status": "O",
            "item_type": "OBLIGATION",
            "layer": "MULTI",
            "gate_ids": "GATE-L4-L6-PHOTON-MASSLESS-PHASE",
            "row_sha": "387d2f49e94f2b27a9a74f910d65f6feb34a8c2e0bc91f0b60c8364874309a4e",
            "scope_sha": "0a65f92a89de6cfc15080d3dfca601f7cf371b8de5b8c783dd0f23e83ef52add",
            "evidence_kind": "INLINE_CANON",
            "location": "inline",
            "evidence_sha": "0a65f92a89de6cfc15080d3dfca601f7cf371b8de5b8c783dd0f23e83ef52add",
            "hash_mode": "registry-scope-sha256-v1",
            "architecture": "none",
            "scope_markers": (
                "complete theorem-preserving comparison with explicit constants",
                "finite-volume configuration space and action",
                "no roughening slogan",
                "uncited Froehlich-Spencer import",
                "physical-photon conclusion",
            ),
        },
    }
    v72_current_contract = {
        claim: contract for claim, contract in v72_contract.items()
        if claim != "PHOTON-CONE-CONVERGENCE"
    }
    v72_dependencies = {
        "FCC-WEIGHTED-SHELL-SYMBOL": set(),
        "PHOTON-WILSON-VILLAIN-FINITE-COUPLING-NONMEMBERSHIP": {
            ("PHOTON-WINDOW-COORDINATES", "REQUIRES"),
        },
        "PHOTON-MASSLESS-PHASE": {
            ("DEF-ACTION-LAYERS", "REQUIRES"),
            ("PHOTON-WINDOW-COORDINATES", "REQUIRES"),
            (
                "PHOTON-WILSON-VILLAIN-FINITE-COUPLING-NONMEMBERSHIP",
                "BOUNDED_BY",
            ),
        },
    }
    v72_dependency_hashes = {
        ("PHOTON-WILSON-VILLAIN-FINITE-COUPLING-NONMEMBERSHIP", "PHOTON-WINDOW-COORDINATES", "REQUIRES"): "ba3ec189da893464ac7fb1b579abd73fad28760bbf0d80e85363d3f939d2a189",
        ("PHOTON-MASSLESS-PHASE", "DEF-ACTION-LAYERS", "REQUIRES"): "5a205f0cb5e04826724742c39e59c521126cd0b3527b5e44519915a2ecc116f7",
        ("PHOTON-MASSLESS-PHASE", "PHOTON-WINDOW-COORDINATES", "REQUIRES"): "ba559c1dd1a9b6e4879e61df82fc067be6c6045aa753ba5d341a1524ea9df66d",
        ("PHOTON-MASSLESS-PHASE", "PHOTON-WILSON-VILLAIN-FINITE-COUPLING-NONMEMBERSHIP", "BOUNDED_BY"): "898d9103e3f4a17b53b8888f33eeaaba959bb313d39989c0692e51110dea958d",
    }
    v72_gate_contract = {
        "GATE-L4-L6-PHOTON-MASSLESS-PHASE": {
            "owner": "PHOTON-MASSLESS-PHASE",
            "source": "L4",
            "target": "L6",
            "markers": (
                "thermodynamic limit",
                "named L6 massless observable",
                "otherwise STOP",
            ),
            "row_sha": "68a9c49f82e039e09e5cdd99ffb7d0e5dce62d842d5eefaeb77ae7cb2cbbdb35",
        },
    }
    v72_history_hashes = {
        "FCC-WEIGHTED-SHELL-SYMBOL": "fee15622899178ea188a5879e5e33fb85bf4ebb8924a69371194ce0d8756d3c5",
        "PHOTON-WILSON-VILLAIN-FINITE-COUPLING-NONMEMBERSHIP": "dbf27e54507911a3ad6ed37a3ab9601d9f8b6f92747ba3a2f64634108e962522",
        "PHOTON-CONE-CONVERGENCE": "3e2d6aca42d3d5aad7072260e72ff280f2de61897e1b26fe62edce8ce5cca0f9",
        "PHOTON-MASSLESS-PHASE": "7e92caff74858a8d54c69de86eeb0bdf73f8bca4cdd41e9662fe2b6a8c1a03ac",
    }
    v72_claims = tuple(v72_contract)
    v72_history_rows = [
        row for row in history if row["release"] == "canon-v72-candidate"
    ]
    v72_events = {row["claim_id"]: row for row in v72_history_rows}
    v72_actual_dependencies = {
        claim: {
            (row["depends_on"], row["relation"])
            for row in dependencies if row["item_id"] == claim
        }
        for claim in v72_current_contract
    }
    v72_actual_dependency_hashes = {
        (row["item_id"], row["depends_on"], row["relation"]): table_row_sha256(row)
        for row in dependencies if row["item_id"] in v72_current_contract
    }
    v72_expected_consumers = {
        "PHOTON-WILSON-VILLAIN-FINITE-COUPLING-NONMEMBERSHIP": {
            ("PHOTON-MASSLESS-PHASE", "BOUNDED_BY"),
        },
        "PHOTON-MASSLESS-PHASE": set(),
    }
    v72_actual_consumers = {
        claim: {
            (row["item_id"], row["relation"])
            for row in dependencies if row["depends_on"] == claim
        }
        for claim in v72_expected_consumers
    }
    v72_photon_gate_ids = set(v72_gate_contract)
    v72_owned_gate_ids = {
        gate_id for gate_id, row in gates.items()
        if row["owner_item_id"] == "PHOTON-MASSLESS-PHASE"
    }
    v72_canon_start = canon_text.find("### FCC-WEIGHTED-SHELL-SYMBOL [T]")
    v72_canon_end = (
        canon_text.find("### Photon successor roots", v72_canon_start)
        if v72_canon_start >= 0 else -1
    )
    v72_canon_block = (
        canon_text[v72_canon_start:v72_canon_end]
        if v72_canon_start >= 0 and v72_canon_end >= 0 else ""
    )
    checks.append((
        "V72-PHOTON",
        "the v72 boundary theorems and declarations remain pinned while the "
        "massless route stays O/STOP and later folds own the cone route",
        all(
            has_status(index, claim, contract["status"])
            and scope_sha256(index, claim) == contract["scope_sha"]
            and registry_row_sha256(index, claim) == contract["row_sha"]
            and index[claim]["canon_section"] == "9. The photon and the electron"
            and scope_contains_all(index, claim, contract["scope_markers"])
            and normative[claim]["item_type"] == contract["item_type"]
            and normative[claim]["claim_id"] == claim
            and normative[claim]["status"] == contract["status"]
            and normative[claim]["layer"] == contract["layer"]
            and normative[claim]["gate_ids"] == contract["gate_ids"]
            and normative[claim]["statement_source"] == "canon/CANON.md::9. The photon and the electron"
            and evidence[claim]["evidence_id"] == "EV-" + claim
            and evidence[claim]["evidence_kind"] == contract["evidence_kind"]
            and evidence[claim]["location"] == contract["location"]
            and evidence[claim]["sha256"] == contract["evidence_sha"]
            and evidence[claim]["hash_mode"] == contract["hash_mode"]
            and evidence[claim]["architecture_requirement"]
            == contract["architecture"]
            for claim, contract in v72_current_contract.items()
        )
        and v72_actual_dependencies == v72_dependencies
        and v72_actual_dependency_hashes == v72_dependency_hashes
        and v72_actual_consumers == v72_expected_consumers
        and len(v72_history_rows) == 4
        and set(v72_events) == set(v72_claims)
        and all(
            v72_events[claim]["event_id"] == f"CANON72-DECLARE-{claim}"
            and v72_events[claim]["event_sequence"] == "1"
            and v72_events[claim]["event_date"] == "2026-08-30"
            and v72_events[claim]["event_type"] == "DECLARE"
            and v72_events[claim]["previous_status"] == "-"
            and v72_events[claim]["new_status"] == contract["status"]
            and v72_events[claim]["scope_sha256"] == contract["scope_sha"]
            and v72_events[claim]["evidence_id"] == "EV-" + claim
            and v72_events[claim]["evidence_location"] == contract["location"]
            and v72_events[claim]["evidence_sha256"]
            == contract["evidence_sha"]
            and table_row_sha256(v72_events[claim]) == v72_history_hashes[claim]
            for claim, contract in v72_contract.items()
        )
        and v72_owned_gate_ids == v72_photon_gate_ids
        and all(
            gate_id in gates
            and gates[gate_id]["owner_item_id"] == contract["owner"]
            and gates[gate_id]["from_layer"] == contract["source"]
            and gates[gate_id]["to_layer"] == contract["target"]
            and gates[gate_id]["gate_kind"] == "OPEN_LIFT"
            and table_row_sha256(gates[gate_id]) == contract["row_sha"]
            and all(
                marker.lower() in gates[gate_id]["decision_condition"].lower()
                for marker in contract["markers"]
            )
            for gate_id, contract in v72_gate_contract.items()
        )
        and programs.get("PHOTON-CONE-CONVERGENCE") == {
            "claim_id": "PHOTON-CONE-CONVERGENCE",
            "program_id": "PHOTON_CONTINUUM",
            "queue_role": "ROOT",
            "work_state": "STOP",
            "work_mode": "FORMAL",
        }
        and programs.get("PHOTON-MASSLESS-PHASE") == {
            "claim_id": "PHOTON-MASSLESS-PHASE",
            "program_id": "PHOTON_CONTINUUM",
            "queue_role": "ROOT",
            "work_state": "STOP",
            "work_mode": "FORMAL",
        }
        and "FCC-WEIGHTED-SHELL-SYMBOL" not in programs
        and "PHOTON-WILSON-VILLAIN-FINITE-COUPLING-NONMEMBERSHIP" not in programs
        and f"- PHOTON-CONE-CONVERGENCE [O]:" in frontier_text
        and f"- PHOTON-MASSLESS-PHASE [O]:" in frontier_text
        and f"- FCC-WEIGHTED-SHELL-SYMBOL [" not in frontier_text
        and (
            f"- PHOTON-WILSON-VILLAIN-FINITE-COUPLING-NONMEMBERSHIP ["
            not in frontier_text
        )
        and all(row["claim_id"] not in v72_claims for row in core_selection_rows)
        and all(f"- {claim} [" not in core_text for claim in v72_claims)
        and len(v72_canon_block.encode("utf-8")) == 2740
        and hashlib.sha256(v72_canon_block.encode("utf-8")).hexdigest()
        == "dcb94cbfd9283e371a1c9904f5f8d84541bcc2dc48081a547dfa7bf43ccd3fd0"
        and all(
            phrase in canon_text
            for phrase in (
                "This is one displayed L2 scalar symbol. It does not select the FCC carrier,",
                "This is direct finite-coupling nonmembership only.",
                "It proves no Gibbs state, thermodynamic",
                "The preceding theorems do not repair or reopen `PHOTON-KAPPA-LEMMA [F]`",
                "Wilson/Villain nonmembership theorem is boundary information only; it is not",
                "Both successor roots are `ROOT / STOP / FORMAL`.",
                "Neither adopts a roughening",
                "an uncited Froehlich-Spencer import, Lorentz invariance, a continuum",
                "physical readout or a physical photon.",
            )
        )
        and has_status(index, "PHOTON-KAPPA-LEMMA", "F")
        and has_status(index, "PHOTON-WINDOW-PROOF", "F")
        and "PHOTON-KAPPA-LEMMA" not in programs
        and "PHOTON-WINDOW-PROOF" not in programs
        and all(
            all("ROUGHEN" not in claim_id for claim_id in collection)
            for collection in (index, normative, evidence, programs)
        )
        and all(
            "ROUGHEN" not in row["item_id"]
            and "ROUGHEN" not in row["depends_on"]
            for row in dependencies
        ),
    ))

    v73_contract = {
        "C8-MARKING-RIGIDITY": {
            "status": "T",
            "item_type": "THEOREM",
            "layer": "L1",
            "section": "3. The kernel and the census",
            "row_sha": "d341c1696adf64fba058f0b0e931aad1050ec724f51fda391ee2515157308b82",
            "scope_sha": "1de8ab00e9113b12983eb54caae4340d491aad6b614d086376670db6979a8627",
            "evidence_kind": "PUBLIC_PROBE",
            "location": "probes/P-C8-MARKING-RIGIDITY-2",
            "evidence_sha": "85310f5ac782aed62c976c8ad35be241d8076e48d2b9c6fc91a0e5cce0b7b378",
            "hash_mode": "bundle-manifest-sha256-v1",
            "architecture": "two-architecture",
            "scope_markers": (
                "the marking J_lambda=2 is an input and is not derived",
                "no unique C8 generator orientation is selected",
                "relative no-go",
            ),
        },
        "C8-PAULI-QUOTIENT-TRANSPORT": {
            "status": "T",
            "item_type": "THEOREM",
            "layer": "L1",
            "section": "3. The kernel and the census",
            "row_sha": "26358db400f51ca40d3321c867e793a073b66cc230fee9a75008348705a175fb",
            "scope_sha": "2b7897be4bdad094e8a90c82dc9f99b04de2b7408d1b63003057f66e68d11a57",
            "evidence_kind": "PUBLIC_PROBE",
            "location": "probes/P-C8-PAULI-QUOTIENT-TRANSPORT-1",
            "evidence_sha": "d86f710667b0afe241d8f115325c1c2fd074e27bbd20714891ce9184b221c016",
            "hash_mode": "bundle-manifest-sha256-v1",
            "architecture": "two-architecture",
            "scope_markers": (
                "complete transport for one named multiplicative record",
                "not a Born-norm or field embedding",
                "no branch selector, new coordinate, lost component or new physical gauge",
            ),
        },
        "FCC-WEIGHTED-SHELL-REMAINDER": {
            "status": "T",
            "item_type": "THEOREM",
            "layer": "L2",
            "section": "9. The photon and the electron",
            "row_sha": "f22893357599a98ca6b2fc927620cc23559dad731c46957b5a396f6a1be8c749",
            "scope_sha": "648be021804c48838c3156e155d861475ec36371fa4848e7939b1265277009a2",
            "evidence_kind": "PUBLIC_PROBE",
            "location": "probes/P-FCC-WEIGHTED-SHELL-REMAINDER-1",
            "evidence_sha": "64dd69e762b3bd8be2ebf1f1a4e693e8c70f934beb8151f22e02c10114ecafba",
            "hash_mode": "bundle-manifest-sha256-v1",
            "architecture": "two-architecture",
            "scope_markers": (
                "no sharpness claim for the displayed constants",
                "not an architecture-to-physical-continuum lift",
                "are not two photons or two polarizations",
            ),
        },
        "PHOTON-Z5-STAR-QUADRATURE": {
            "status": "C",
            "item_type": "COMPUTATION",
            "layer": "L4",
            "section": "9. The photon and the electron",
            "row_sha": "37a277e979fbb4d1c1424e44e5b71a8c21967796cedc79ed8b987dcdd207d698",
            "scope_sha": "0f3a6cd2a3916d47bc26c65327e9d8dd46ccc0d5c47178ff62ddcd86dd0749f1",
            "evidence_kind": "PUBLIC_PROBE",
            "location": "probes/P-PHOTON-Z5-STAR-QUADRATURE-1",
            "evidence_sha": "942901869d5296f6d6bdf41423b0fb0d438ac582bf3d582c73fb9a21999aa6a9",
            "hash_mode": "bundle-manifest-sha256-v1",
            "architecture": "two-architecture",
            "scope_markers": (
                "theta_star=(82+50 sqrt(5))/361",
                "exactly these five refute the frozen predicate HALF",
                "adopt no L6 probability law",
            ),
        },
    }
    v73_dependencies = {
        "C8-MARKING-RIGIDITY": {
            ("I-BILOCATED", "BOUNDED_BY"),
        },
        "C8-PAULI-QUOTIENT-TRANSPORT": {
            ("C8-BILINEAR-SHADOW", "REQUIRES"),
            ("I-BILOCATED", "BOUNDED_BY"),
        },
        "FCC-WEIGHTED-SHELL-REMAINDER": {
            ("FCC-WEIGHTED-SHELL-SYMBOL", "REQUIRES"),
        },
        "PHOTON-Z5-STAR-QUADRATURE": set(),
    }
    v73_dependency_hashes = {
        ("C8-MARKING-RIGIDITY", "I-BILOCATED", "BOUNDED_BY"): "282225ab1380251e5ee7efa8be5d1fa05ceee0b5ea0d8230225308e26a938a64",
        ("C8-PAULI-QUOTIENT-TRANSPORT", "C8-BILINEAR-SHADOW", "REQUIRES"): "242b8fc98b282b93e216500f5d4d63d0a0f842b738276e44299d7f5b178592c4",
        ("C8-PAULI-QUOTIENT-TRANSPORT", "I-BILOCATED", "BOUNDED_BY"): "7b9462114648b25db6c69a25730eb948e7c721cf26f251fd2cc0016bba5d7bf2",
        ("FCC-WEIGHTED-SHELL-REMAINDER", "FCC-WEIGHTED-SHELL-SYMBOL", "REQUIRES"): "fa3e42047adb81fd43ecc8e2ec843d5b3f4f0ca3ab96836a0a16dbd12d4d3dd9",
    }
    v73_history_hashes = {
        "C8-MARKING-RIGIDITY": "a6613333db41ea9fd1f57b4c312fc6a796397c433fc8258caae08f0ad3967006",
        "C8-PAULI-QUOTIENT-TRANSPORT": "2847f6d1aaa748fa2be11a9b0c5982f38b8aec9f783f16cbd5148460c13ebb51",
        "FCC-WEIGHTED-SHELL-REMAINDER": "9632a74512c5f6590ce37f729ff646f10bb3d75a3158f607abc372e8621a166b",
        "PHOTON-Z5-STAR-QUADRATURE": "a7c3360606a580a25ab36ca5a47ecb36cf1b847f37cf75fdf3bd3d38d64de05c",
    }
    v73_claims = tuple(v73_contract)
    v73_history_rows = [
        row for row in history if row["release"] == "canon-v73-candidate"
    ]
    v73_events = {row["claim_id"]: row for row in v73_history_rows}
    v73_actual_dependencies = {
        claim: {
            (row["depends_on"], row["relation"])
            for row in dependencies if row["item_id"] == claim
        }
        for claim in v73_claims
    }
    v73_actual_dependency_hashes = {
        (row["item_id"], row["depends_on"], row["relation"]): table_row_sha256(row)
        for row in dependencies if row["item_id"] in v73_claims
    }
    checks.append((
        "V73-FOLD",
        "three proof-first rows and one complete finite classification enter at "
        "their earned status, the C8 marking stays a dictionary input, the "
        "refuted HALF predicate is preserved, and no gate, program or frontier "
        "row moves",
        all(
            has_status(index, claim, contract["status"])
            and scope_sha256(index, claim) == contract["scope_sha"]
            and registry_row_sha256(index, claim) == contract["row_sha"]
            and index[claim]["canon_section"] == contract["section"]
            and scope_contains_all(index, claim, contract["scope_markers"])
            and normative[claim]["item_type"] == contract["item_type"]
            and normative[claim]["claim_id"] == claim
            and normative[claim]["status"] == contract["status"]
            and normative[claim]["layer"] == contract["layer"]
            and normative[claim]["gate_ids"] == ""
            and normative[claim]["statement_source"]
            == "canon/CANON.md::" + contract["section"]
            and evidence[claim]["evidence_id"] == "EV-" + claim
            and evidence[claim]["evidence_kind"] == contract["evidence_kind"]
            and evidence[claim]["location"] == contract["location"]
            and evidence[claim]["sha256"] == contract["evidence_sha"]
            and evidence[claim]["hash_mode"] == contract["hash_mode"]
            and evidence[claim]["architecture_requirement"]
            == contract["architecture"]
            and "### " + claim + " [" + contract["status"] + "]" in canon_text
            for claim, contract in v73_contract.items()
        )
        and v73_actual_dependencies == v73_dependencies
        and v73_actual_dependency_hashes == v73_dependency_hashes
        and len(v73_history_rows) == 4
        and set(v73_events) == set(v73_claims)
        and all(
            v73_events[claim]["event_id"] == "CANON73-DECLARE-" + claim
            and v73_events[claim]["event_sequence"] == "1"
            and v73_events[claim]["event_date"] == "2026-08-31"
            and v73_events[claim]["event_type"] == "DECLARE"
            and v73_events[claim]["previous_status"] == "-"
            and v73_events[claim]["new_status"] == contract["status"]
            and v73_events[claim]["scope_sha256"] == contract["scope_sha"]
            and v73_events[claim]["evidence_id"] == "EV-" + claim
            and v73_events[claim]["evidence_location"] == contract["location"]
            and v73_events[claim]["evidence_sha256"] == contract["evidence_sha"]
            and table_row_sha256(v73_events[claim]) == v73_history_hashes[claim]
            for claim, contract in v73_contract.items()
        )
        and not any(
            row["owner_item_id"] in v73_claims for row in gates.values()
        )
        and all(claim not in programs for claim in v73_claims)
        and all("- " + claim + " [" not in frontier_text for claim in v73_claims)
        and has_status(index, "I-BILOCATED", "D")
        and has_status(index, "C8-BILINEAR-SHADOW", "T")
        and has_status(index, "FCC-WEIGHTED-SHELL-SYMBOL", "T")
        and has_status(index, "PHOTON-CONE-CONVERGENCE", "O")
        and has_status(index, "PHOTON-MASSLESS-PHASE", "O")
        and has_status(index, "PHOTON-KAPPA-LEMMA", "F")
        and has_status(index, "PHOTON-WINDOW-PROOF", "F")
    ))

    v74_bundle = (
        "5216488c404111736d9e6d4d60b81ff52ae36791f693c21bf7d99dc6b4e035f3"
    )
    v74_contract = {
        "PHOTON-SPATIAL-TEMPORAL-TRANSFER": {
            "status": "D",
            "item_type": "DICTIONARY",
            "layer": "MULTI",
            "gate_ids": "GATE-L2-L5-PHOTON-TEMPORAL-CHARACTERISTIC",
            "row_sha": "77976e84dde6735e836e1e8bdcbfba42a3a028d2dbdc37539319427aed482474",
            "scope_sha": "e916ffddedaffad5ed980436438481e4fbfd5254e5011276432551db2e9b0a6e",
            "evidence_kind": "PUBLIC_PROBE",
            "location": "probes/P-PHOTON-TEMPORAL-CHARACTERISTIC-1",
            "evidence_sha": v74_bundle,
            "hash_mode": "bundle-manifest-sha256-v1",
            "architecture": "two-architecture",
            "scope_markers": (
                "owner-adopted L2-to-L5 dictionary",
                "(a,b)=(-2,1)",
                "claims no completeness or uniqueness outside the displayed class",
                "SI speed",
                "physical photon",
            ),
        },
        "PHOTON-TEMPORAL-CHARACTERISTIC": {
            "status": "T",
            "item_type": "THEOREM",
            "layer": "L5",
            "gate_ids": "",
            "row_sha": "33eb50d4ea884fef565ff376f8750425a967579beeb6c371ba3cd968595f1424",
            "scope_sha": "626c8fd13d05da7180f9ddcf05e57b52a840074bb1d68998f2ce265656207c3c",
            "evidence_kind": "PUBLIC_PROBE",
            "location": "probes/P-PHOTON-TEMPORAL-CHARACTERISTIC-1",
            "evidence_sha": v74_bundle,
            "hash_mode": "bundle-manifest-sha256-v1",
            "architecture": "two-architecture",
            "scope_markers": (
                "total exact characteristic",
                "reciprocal conjugate unit-modulus multipliers",
                "uniformly on bounded lifted sets",
                "unit phases rather than contraction/expansion amplitudes",
                "Herm2 carrier",
                "physical photon",
            ),
        },
    }
    v74_dependencies = {
        "PHOTON-SPATIAL-TEMPORAL-TRANSFER": {
            ("DEF-ACTION-LAYERS", "REQUIRES"),
            ("FCC-WEIGHTED-SHELL-SYMBOL", "REQUIRES"),
            ("FCC-WEIGHTED-SHELL-REMAINDER", "REQUIRES"),
        },
        "PHOTON-TEMPORAL-CHARACTERISTIC": {
            ("PHOTON-SPATIAL-TEMPORAL-TRANSFER", "BOUNDED_BY"),
        },
    }
    v74_dependency_hashes = {
        ("PHOTON-SPATIAL-TEMPORAL-TRANSFER", "DEF-ACTION-LAYERS", "REQUIRES"):
            "53493f4ac821a8a456fc075f17fe5fe2b50f6d0d400c9d45db8e83acb4f90b03",
        ("PHOTON-SPATIAL-TEMPORAL-TRANSFER", "FCC-WEIGHTED-SHELL-SYMBOL", "REQUIRES"):
            "81660bd76e84a9ecda54055acfc894564529fcf69d971188b0d71e6eb0d28c1c",
        ("PHOTON-SPATIAL-TEMPORAL-TRANSFER", "FCC-WEIGHTED-SHELL-REMAINDER", "REQUIRES"):
            "0ba4d0fe90d4d1d6f5c00c5c1b493d80c97e0fc58366a881d68a49e0d05e7453",
        ("PHOTON-TEMPORAL-CHARACTERISTIC", "PHOTON-SPATIAL-TEMPORAL-TRANSFER", "BOUNDED_BY"):
            "748aab7ab1efbc50cf12fe28c21917d183b7a10d483bf554bfab0202510263a7",
    }
    v74_expected_consumers = {
        "FCC-WEIGHTED-SHELL-SYMBOL": {
            ("FCC-WEIGHTED-SHELL-REMAINDER", "REQUIRES"),
            ("PHOTON-SPATIAL-TEMPORAL-TRANSFER", "REQUIRES"),
        },
        "FCC-WEIGHTED-SHELL-REMAINDER": {
            ("PHOTON-SPATIAL-TEMPORAL-TRANSFER", "REQUIRES"),
        },
        "PHOTON-SPATIAL-TEMPORAL-TRANSFER": {
            ("PHOTON-TEMPORAL-CHARACTERISTIC", "BOUNDED_BY"),
            ("PHOTON-CONE-CONVERGENCE", "REQUIRES"),
            ("PHOTON-HERM2-SEPARATED-GLOBAL-OBSTRUCTION", "BOUNDED_BY"),
            ("POINTED-DECODER-PREFIX-CONSISTENCY", "BOUNDED_BY"),
            ("DECODER-RETARDED-LOCAL-ENERGY-TRANSPORT", "BOUNDED_BY"),
        },
        "PHOTON-TEMPORAL-CHARACTERISTIC": {
            ("PHOTON-CONE-CONVERGENCE", "REQUIRES"),
            ("MATTER-SCALAR-TEMPORAL-CHARACTERISTIC", "REQUIRES"),
            ("PHOTON-HERM2-TANGENT-GERM", "REQUIRES"),
        },
        "PHOTON-CONE-CONVERGENCE": set(),
    }
    v74_actual_dependencies = {
        claim: {
            (row["depends_on"], row["relation"])
            for row in dependencies if row["item_id"] == claim
        }
        for claim in v74_contract
    }
    v74_actual_dependency_hashes = {
        (row["item_id"], row["depends_on"], row["relation"]):
            table_row_sha256(row)
        for row in dependencies if row["item_id"] in v74_contract
    }
    # Keep the historical consumer contract unchanged. The exact v82 intake
    # below owns its added BOUNDED_BY consumer; only a byte-verified v81
    # dependency table may feed this older boundary check.
    v81_dependency_bytes = v82_previous_bytes(DEPENDENCIES)
    v81_dependency_rows = (
        list(csv.DictReader(io.StringIO(v81_dependency_bytes.decode("utf-8")),
                            delimiter="\t"))
        if v81_dependency_bytes is not None else []
    )
    v74_actual_consumers = {
        claim: {
            (row["item_id"], row["relation"])
            for row in v81_dependency_rows if row["depends_on"] == claim
        }
        for claim in v74_expected_consumers
    }
    v74_history_rows = [
        row for row in history if row["release"] == "canon-v74-candidate"
    ]
    v74_history_by_event = {
        row["event_id"]: row for row in v74_history_rows
    }
    v74_history_contract = {
        "CANON74-DECLARE-PHOTON-SPATIAL-TEMPORAL-TRANSFER": {
            "claim": "PHOTON-SPATIAL-TEMPORAL-TRANSFER",
            "sequence": "1", "type": "DECLARE", "previous": "-", "new": "D",
            "scope": "e916ffddedaffad5ed980436438481e4fbfd5254e5011276432551db2e9b0a6e",
            "evidence": "EV-PHOTON-SPATIAL-TEMPORAL-TRANSFER",
            "location": "probes/P-PHOTON-TEMPORAL-CHARACTERISTIC-1",
            "evidence_sha": v74_bundle,
            "row_sha": "30c6733f64f5115f7a9bc07435c79424d5ca92d875b953eb46b0a85e7027d826",
        },
        "CANON74-DECLARE-PHOTON-TEMPORAL-CHARACTERISTIC": {
            "claim": "PHOTON-TEMPORAL-CHARACTERISTIC",
            "sequence": "1", "type": "DECLARE", "previous": "-", "new": "T",
            "scope": "626c8fd13d05da7180f9ddcf05e57b52a840074bb1d68998f2ce265656207c3c",
            "evidence": "EV-PHOTON-TEMPORAL-CHARACTERISTIC",
            "location": "probes/P-PHOTON-TEMPORAL-CHARACTERISTIC-1",
            "evidence_sha": v74_bundle,
            "row_sha": "e999bf6e3a6fb8a33858e06711c15b9cf1523e7cebfd814f935a3f6a0b4f5df0",
        },
        "CANON74-SCOPE-PHOTON-CONE-CONVERGENCE": {
            "claim": "PHOTON-CONE-CONVERGENCE",
            "sequence": "2", "type": "SCOPE_CHANGE", "previous": "O", "new": "O",
            "scope": "f67b713037517aac2a0f2ca119b7f7176e0c49f6ad4414031353cd67c9577853",
            "evidence": "EV-PHOTON-CONE-CONVERGENCE",
            "location": "inline",
            "evidence_sha": "f67b713037517aac2a0f2ca119b7f7176e0c49f6ad4414031353cd67c9577853",
            "row_sha": "1156887c7abfb280fd615d32f972e00a5fb2ffd54cda4086786fdcab5294ff16",
        },
    }
    v74_gate_contract = {
        "GATE-L2-L5-PHOTON-TEMPORAL-CHARACTERISTIC": {
            "owner": "PHOTON-SPATIAL-TEMPORAL-TRANSFER",
            "source": "L2", "target": "L5", "kind": "DICTIONARY_LIFT",
            "markers": ("closed at status D", "supported by", "no Herm2 carrier"),
            "row_sha": "14e3328125b6b1dd653b697178ecd1320c1923434d787b21b381a9613937c74d",
        },
    }
    v74_dt_start = canon_text.find(
        "### PHOTON-SPATIAL-TEMPORAL-TRANSFER [D]"
    )
    v74_dt_end = canon_text.find(
        "### PHOTON-HERM2-TANGENT-GERM [T]", v74_dt_start
    )
    v74_dt_block = (
        canon_text[v74_dt_start:v74_dt_end]
        if v74_dt_start >= 0 and v74_dt_end >= 0 else ""
    )
    v74_successor_start = canon_text.find("### Photon successor roots")
    v74_successor_end = canon_text.find(
        "The electron:", v74_successor_start
    )
    v74_successor_block = (
        canon_text[v74_successor_start:v74_successor_end]
        if v74_successor_start >= 0 and v74_successor_end >= 0 else ""
    )
    checks.append((
        "V74-PHOTON",
        "selected D3 transfer enters at D/MULTI and its exact characteristic "
        "at T/L5, closing the L2-to-L5 dictionary lift while v75 owns the "
        "later Herm2 and global-carrier disposition",
        all(
            has_status(index, claim, contract["status"])
            and scope_sha256(index, claim) == contract["scope_sha"]
            and registry_row_sha256(index, claim) == contract["row_sha"]
            and index[claim]["canon_section"] == "9. The photon and the electron"
            and scope_contains_all(index, claim, contract["scope_markers"])
            and normative[claim]["item_type"] == contract["item_type"]
            and normative[claim]["claim_id"] == claim
            and normative[claim]["status"] == contract["status"]
            and normative[claim]["layer"] == contract["layer"]
            and normative[claim]["gate_ids"] == contract["gate_ids"]
            and normative[claim]["statement_source"]
            == "canon/CANON.md::9. The photon and the electron"
            and evidence[claim]["evidence_id"] == "EV-" + claim
            and evidence[claim]["evidence_kind"] == contract["evidence_kind"]
            and evidence[claim]["location"] == contract["location"]
            and evidence[claim]["sha256"] == contract["evidence_sha"]
            and evidence[claim]["hash_mode"] == contract["hash_mode"]
            and evidence[claim]["architecture_requirement"]
            == contract["architecture"]
            for claim, contract in v74_contract.items()
        )
        and v74_actual_dependencies == v74_dependencies
        and v74_actual_dependency_hashes == v74_dependency_hashes
        and v74_actual_consumers == v74_expected_consumers
        and len(v74_history_rows) == 3
        and set(v74_history_by_event) == set(v74_history_contract)
        and all(
            v74_history_by_event[event_id]["claim_id"] == contract["claim"]
            and v74_history_by_event[event_id]["event_sequence"]
            == contract["sequence"]
            and v74_history_by_event[event_id]["event_date"] == "2026-09-01"
            and v74_history_by_event[event_id]["event_type"] == contract["type"]
            and v74_history_by_event[event_id]["previous_status"]
            == contract["previous"]
            and v74_history_by_event[event_id]["new_status"] == contract["new"]
            and v74_history_by_event[event_id]["scope_sha256"] == contract["scope"]
            and v74_history_by_event[event_id]["evidence_id"]
            == contract["evidence"]
            and v74_history_by_event[event_id]["evidence_location"]
            == contract["location"]
            and v74_history_by_event[event_id]["evidence_sha256"]
            == contract["evidence_sha"]
            and table_row_sha256(v74_history_by_event[event_id])
            == contract["row_sha"]
            for event_id, contract in v74_history_contract.items()
        )
        and all(
            gate_id in gates
            and gates[gate_id]["owner_item_id"] == contract["owner"]
            and gates[gate_id]["from_layer"] == contract["source"]
            and gates[gate_id]["to_layer"] == contract["target"]
            and gates[gate_id]["gate_kind"] == contract["kind"]
            and table_row_sha256(gates[gate_id]) == contract["row_sha"]
            and all(
                marker.lower() in gates[gate_id]["decision_condition"].lower()
                for marker in contract["markers"]
            )
            for gate_id, contract in v74_gate_contract.items()
        )
        # Historical v74 count: the independently pinned v79 check below owns
        # the later curvature-gate transition rather than changing this constant.
        and sum(row["gate_kind"] == "OPEN_LIFT" for row in v79_previous_rows(GATES)) == 7
        and sum(
            row["gate_kind"] == "DICTIONARY_LIFT" for row in v79_previous_rows(GATES)
        ) == 3
        and programs.get("PHOTON-CONE-CONVERGENCE") == {
            "claim_id": "PHOTON-CONE-CONVERGENCE",
            "program_id": "PHOTON_CONTINUUM",
            "queue_role": "ROOT",
            "work_state": "STOP",
            "work_mode": "FORMAL",
        }
        and all(
            claim not in programs
            for claim in (
                "PHOTON-SPATIAL-TEMPORAL-TRANSFER",
                "PHOTON-TEMPORAL-CHARACTERISTIC",
            )
        )
        and "- PHOTON-CONE-CONVERGENCE [O]:" in frontier_text
        and all(
            "- " + claim + " [" not in frontier_text
            and "- " + claim + " [" not in core_text
            and all(row["claim_id"] != claim for row in core_selection_rows)
            for claim in (
                "PHOTON-SPATIAL-TEMPORAL-TRANSFER",
                "PHOTON-TEMPORAL-CHARACTERISTIC",
            )
        )
        and has_status(index, "PHOTON-MASSLESS-PHASE", "O")
        and len(v74_dt_block.encode("utf-8")) == 4216
        and hashlib.sha256(v74_dt_block.encode("utf-8")).hexdigest()
        == "04de7998932b896c0a62a9c9d7e1a29e31a2e5ce3c37f23d2b3e56e64428ad2d"
        and all(
            phrase in canon_text
            for phrase in (
                "The L2-to-L5 temporal-characteristic gate is\nclosed positively as a dictionary lift.",
                "unit-modulus phases, not a contraction/expansion pair",
                "No Herm2 carrier, positive cone,\nBorn rule",
                "interpretation is neither assumed nor refuted.",
            )
        )
    ))

    v75_contract = {
        "JIPC-WP3D-QPOS-SCALAR-SLICE": {
            "layer": "L1", "section": "4. The two places",
            "source": "canon/CANON.md::4. The two places",
            "scope": "a51bdf354575dfd530f0ca5574f3b0b3cf3b1e7862a1390d15c810b645195dc7",
            "row": "2191b0c35918bf45d95e6c0016fd856326fc1688ee3f76fdad272a3940fec89c",
            "location": "probes/P-JIPC-WP3D-QPOS-MELLIN-1",
            "bundle": "11d95eb9b0ede432f55bb2d2d7bafa37182ad51304b3a353005bcdda0bd116ad",
            "markers": ("positive rational", "written proof", "no irrational or complex"),
        },
        "MATTER-SCALAR-TEMPORAL-CHARACTERISTIC": {
            "layer": "L5", "section": "9. The photon and the electron",
            "source": "canon/CANON.md::9. The photon and the electron",
            "scope": "d4c4487c1d3cf13feb03da42a56de833f55a47dffbccda8e8996b418a4fea5eb",
            "row": "9a14d7195d3cfc31a92e944ff68bb0d16978c3ff00c0d61d5cd1cb73dcb77c55",
            "location": "probes/P-MATTER-SCALAR-TEMPORAL-CHARACTERISTIC-1",
            "bundle": "ca4917c2e2c48cc4a3c62d33a3d0be5211b00740a5bb8d3096f4ba1eb5d4d1f2",
            "markers": ("dimensionless", "20/9", "physical mass"),
        },
        "MATTER-SCALAR-BRANCH-CLASSIFICATION": {
            "layer": "L5", "section": "9. The photon and the electron",
            "source": "canon/CANON.md::9. The photon and the electron",
            "scope": "485032bc07738f9147600648718aec7e0a4f84592b9b792643e256220ce31e6e",
            "row": "22fb41d08e4a3048e525008e192a72db30b76c8a28db297efeb1f09870098fe3",
            "location": "probes/P-MATTER-SCALAR-TEMPORAL-CHARACTERISTIC-1",
            "bundle": "ca4917c2e2c48cc4a3c62d33a3d0be5211b00740a5bb8d3096f4ba1eb5d4d1f2",
            "markers": ("q=0", "q>4", "not particle content"),
        },
        "MATTER-SCALAR-MASSIVE-GERM": {
            "layer": "MULTI", "section": "9. The photon and the electron",
            "source": "canon/CANON.md::9. The photon and the electron",
            "scope": "351027804da90de69abf8d1de75c2ee18ff6fd021c51feee14711cc51a695fcb",
            "row": "fa1bd34b2b6a39dabfe6370fb2aa84996cbe7e1c19fae29f5829f86315ae4941",
            "location": "probes/P-MATTER-SCALAR-TEMPORAL-CHARACTERISTIC-1",
            "bundle": "ca4917c2e2c48cc4a3c62d33a3d0be5211b00740a5bb8d3096f4ba1eb5d4d1f2",
            "markers": ("fixed M>0", "unique member of the power family", "SI mass"),
        },
        "PHOTON-HERM2-TANGENT-GERM": {
            "layer": "MULTI", "section": "9. The photon and the electron",
            "source": "canon/CANON.md::9. The photon and the electron",
            "scope": "0d21b720c172ebcacd7c306890dad64c822be68cad98ce26868aa415b0f0e685",
            "row": "15eba91ea36f4570e2fe269b48f454ed0cf6d299bcea08543882b8e6a71c329e",
            "location": "probes/P-PHOTON-HERM2-GERM-AND-GLOBAL-OBSTRUCTION-1",
            "bundle": "6a5d66e6770a2514af48422db58e79dd6abcc1b4b2df13bc2fa77f5aec0aaa70",
            "markers": ("same exact quadratic germ", "not exact equality", "apparatus or photon"),
        },
        "PHOTON-HERM2-SEPARATED-GLOBAL-OBSTRUCTION": {
            "layer": "MULTI", "section": "9. The photon and the electron",
            "source": "canon/CANON.md::9. The photon and the electron",
            "scope": "ef1f18ffb0e38bba049b80e81cea3024b038705ee938ecccc25ef2482b1c0448",
            "row": "1c69d06947e880e0c6503b569fa1deb8958b11aea62e0b8101fd4993dba9ecbb",
            "location": "probes/P-PHOTON-HERM2-GERM-AND-GLOBAL-OBSTRUCTION-1",
            "bundle": "6a5d66e6770a2514af48422db58e79dd6abcc1b4b2df13bc2fa77f5aec0aaa70",
            "markers": ("two-torsion", "is empty", "multichart or twisted-bundle"),
        },
        "QDD-DIRECT-RECORD-E-NONCONGRUENCE": {
            "layer": "L1", "section": "2. Time, space, and the decoder",
            "source": "canon/CANON.md::QDD Route A dictionary",
            "scope": "d973ba0e43d2ef928bc89e3bef90ddd93bbb8a0350ece971f0d5291681d4d477",
            "row": "77b7f34d29a85a0bd6d530b4332b080c3ac2c60508231b4b02f194d97435a687",
            "location": "probes/P-QDD-DIRECT-RECORD-E-NONCONGRUENCE-1",
            "bundle": "e84e94d407c2f9e1c1d3d5d6bca6681dd11fecd363e202f60b9c92d4e6d823b0",
            "markers": ("exactly 313", "zero-centre control", "contextual, stream-level"),
        },
        "TM-CHECKPOINT-HULL-STABLE-IMAGE": {
            "layer": "L1", "section": "3. The kernel and the census",
            "source": "canon/CANON.md::3. The kernel and the census",
            "scope": "f5cf225cf3abba81040b62e97cd2391fbaf52a1befb719bf023d9dbddfa05f0d",
            "row": "3abd4793c875b13cddd219114533aa6df19bdb0d85d4a4bd21c3b4cd90eb3ecb",
            "location": "probes/P-TM-CHECKPOINT-HULL-STABLE-IMAGE-1",
            "bundle": "2ff3871d715eddfc2c5346d236949039975aeefcd18e964a29d97bdc44d7eebb",
            "markers": ("exactly V_hull^9", "involutive reversor", "not identified with public U"),
        },
    }
    v75_dependencies = {
        "JIPC-WP3D-QPOS-SCALAR-SLICE": set(),
        "MATTER-SCALAR-TEMPORAL-CHARACTERISTIC": {
            ("PHOTON-TEMPORAL-CHARACTERISTIC", "REQUIRES"),
        },
        "MATTER-SCALAR-BRANCH-CLASSIFICATION": {
            ("MATTER-SCALAR-TEMPORAL-CHARACTERISTIC", "REQUIRES"),
        },
        "MATTER-SCALAR-MASSIVE-GERM": {
            ("MATTER-SCALAR-TEMPORAL-CHARACTERISTIC", "REQUIRES"),
            ("PHOTON-HERM2-TANGENT-GERM", "REQUIRES"),
        },
        "PHOTON-HERM2-TANGENT-GERM": {
            ("PHOTON-TEMPORAL-CHARACTERISTIC", "REQUIRES"),
        },
        "PHOTON-HERM2-SEPARATED-GLOBAL-OBSTRUCTION": {
            ("PHOTON-SPATIAL-TEMPORAL-TRANSFER", "BOUNDED_BY"),
        },
        "QDD-DIRECT-RECORD-E-NONCONGRUENCE": {
            ("DEF-AUTONOMOUS-STATE", "REQUIRES"),
            ("QDD-ALGEBRAIC-FACTORIZATION", "REQUIRES"),
            ("QDD-INSTRUMENT-APPARATUS", "BOUNDED_BY"),
        },
        "TM-CHECKPOINT-HULL-STABLE-IMAGE": {
            ("DEF-KERNEL-GENERATORS", "REQUIRES"),
            ("DEF-SELECTOR", "REQUIRES"),
            ("TM-SHEET-SYNCHRONIZING-GRAPH", "REQUIRES"),
        },
        "PHOTON-CONE-CONVERGENCE": {
            ("DEF-ACTION-LAYERS", "REQUIRES"),
            ("CENTRAL-LIFT-PHASE", "BOUNDED_BY"),
            ("PHOTON-SPATIAL-TEMPORAL-TRANSFER", "REQUIRES"),
            ("PHOTON-TEMPORAL-CHARACTERISTIC", "REQUIRES"),
            ("PHOTON-HERM2-TANGENT-GERM", "REQUIRES"),
            ("PHOTON-HERM2-SEPARATED-GLOBAL-OBSTRUCTION", "BOUNDED_BY"),
        },
    }
    v75_dependency_hashes = {
        ("MATTER-SCALAR-TEMPORAL-CHARACTERISTIC", "PHOTON-TEMPORAL-CHARACTERISTIC", "REQUIRES"): "e12254c46974cef93079fc707512b0dbe4d853ceff6ff2fc560acb51a699fb4d",
        ("MATTER-SCALAR-BRANCH-CLASSIFICATION", "MATTER-SCALAR-TEMPORAL-CHARACTERISTIC", "REQUIRES"): "b5b004eab60fcc6fe9304d721c2e87e4897b329b01e55dc3c94f4fa439845336",
        ("MATTER-SCALAR-MASSIVE-GERM", "MATTER-SCALAR-TEMPORAL-CHARACTERISTIC", "REQUIRES"): "b919cced8cb4e2621e7e18b27858463af222768319756f3028a3a465f56b2543",
        ("MATTER-SCALAR-MASSIVE-GERM", "PHOTON-HERM2-TANGENT-GERM", "REQUIRES"): "3d2673981183a0a22ca4b0fb7923da90984c587eec30a407f44ae526ab1ac466",
        ("PHOTON-HERM2-TANGENT-GERM", "PHOTON-TEMPORAL-CHARACTERISTIC", "REQUIRES"): "f849b94ec7e3af9ce98a3fa82187c8d98a1f6859805a536e84c5c81fed527f49",
        ("PHOTON-HERM2-SEPARATED-GLOBAL-OBSTRUCTION", "PHOTON-SPATIAL-TEMPORAL-TRANSFER", "BOUNDED_BY"): "53bd6c9f8ecb204d67352eac8ce631d9f561c80bd85fdd68140750a9662f54d4",
        ("QDD-DIRECT-RECORD-E-NONCONGRUENCE", "DEF-AUTONOMOUS-STATE", "REQUIRES"): "5d9fa8ffcad76d839b63d651ef5da289f02e47eb639909a63fbeb7fc6cd59a2f",
        ("QDD-DIRECT-RECORD-E-NONCONGRUENCE", "QDD-ALGEBRAIC-FACTORIZATION", "REQUIRES"): "6b2c84e924cba822d3b21df270e76ba984c18e263b4aa09cee93846c68d11f89",
        ("QDD-DIRECT-RECORD-E-NONCONGRUENCE", "QDD-INSTRUMENT-APPARATUS", "BOUNDED_BY"): "a3ddc744d6d52cefc31f6eabcfef1a0fa5348d255ddd19c1f4599d8154244a80",
        ("TM-CHECKPOINT-HULL-STABLE-IMAGE", "DEF-KERNEL-GENERATORS", "REQUIRES"): "bdcd3400914bd682964691b80ac97cb7c5e6e1855f4874dce36f64e7a22e171a",
        ("TM-CHECKPOINT-HULL-STABLE-IMAGE", "DEF-SELECTOR", "REQUIRES"): "33a1cd35b8c656db5db105eea003d02d8889544293a73f9a756fdbe48b017ddf",
        ("TM-CHECKPOINT-HULL-STABLE-IMAGE", "TM-SHEET-SYNCHRONIZING-GRAPH", "REQUIRES"): "84f312a338a4f58897b6c0a49b7a71e6aa361cde05b23299915d44798fe288d5",
        ("PHOTON-CONE-CONVERGENCE", "DEF-ACTION-LAYERS", "REQUIRES"): "c638f52b92f436f365576bd18fca072d588bd15b866f8a0807e031eb1d9850e8",
        ("PHOTON-CONE-CONVERGENCE", "CENTRAL-LIFT-PHASE", "BOUNDED_BY"): "4c4c10082e52ca01a32de03b681e875427ba5228214df234b87eeaeb31c22a1d",
        ("PHOTON-CONE-CONVERGENCE", "PHOTON-SPATIAL-TEMPORAL-TRANSFER", "REQUIRES"): "878e099160b534bd12c4e96a8f2f0caaf9b93a14ab5a17bb7a56153c3d2d42f9",
        ("PHOTON-CONE-CONVERGENCE", "PHOTON-TEMPORAL-CHARACTERISTIC", "REQUIRES"): "a0bbff1c179b980ea2312bd9d2b2b43243ea8e07a5c6523c0a727140d6eac656",
        ("PHOTON-CONE-CONVERGENCE", "PHOTON-HERM2-TANGENT-GERM", "REQUIRES"): "37cfcecd1fae146081128cc3dbc313d449815bdf2cfe00d8dd280d427aeb3fb4",
        ("PHOTON-CONE-CONVERGENCE", "PHOTON-HERM2-SEPARATED-GLOBAL-OBSTRUCTION", "BOUNDED_BY"): "f4cca9141354150a654333da2507bab2ba5b0f1fc8eb41fa0401d1b4fc4f38c9",
    }
    v75_history_hashes = {
        "CANON75-DECLARE-JIPC-WP3D-QPOS-SCALAR-SLICE": "df0e1308b39898304c0e1ee4e6365ccf4b6ae52a918ca1d6fd35a02f511b0181",
        "CANON75-DECLARE-MATTER-SCALAR-TEMPORAL-CHARACTERISTIC": "9d79390cccc9cd42b3211dc82ac2152fd4c603db5d90e3914094985025da8391",
        "CANON75-DECLARE-MATTER-SCALAR-BRANCH-CLASSIFICATION": "283089f336688d641520ccf90bc68456220639c9886057395324bb89d4385fb2",
        "CANON75-DECLARE-MATTER-SCALAR-MASSIVE-GERM": "27dc70b5ad3bab4a7fc851a20cd6221d56e51c64d0aa35516f269952fb9409d2",
        "CANON75-DECLARE-PHOTON-HERM2-TANGENT-GERM": "3b938f1424a2dda6fbdedec636f5f27640f881a89e903fde6aad77320c65a3b7",
        "CANON75-DECLARE-PHOTON-HERM2-SEPARATED-GLOBAL-OBSTRUCTION": "3e633e148443b62b7cac4aeebdb2aa81da4f3e7da6955fa897ba966edd6e0677",
        "CANON75-DECLARE-QDD-DIRECT-RECORD-E-NONCONGRUENCE": "080e19f029cee606fed6f73b82a0da1d60b9116c632ac20ab479bcb224136931",
        "CANON75-DECLARE-TM-CHECKPOINT-HULL-STABLE-IMAGE": "09e7a15b430232a2d42ef83c24ddef51f3124375c2b65fac76085b1c31956915",
        "CANON75-SCOPE-PHOTON-CONE-CONVERGENCE": "af639028ecaaded685c17842ea79bcf5ae279a9aa15e4ac538e70cf588d1a663",
    }
    v75_claims = set(v75_contract)
    v75_dependency_items = v75_claims | {"PHOTON-CONE-CONVERGENCE"}
    v75_actual_dependencies = {
        claim: {
            (row["depends_on"], row["relation"])
            for row in dependencies if row["item_id"] == claim
        }
        for claim in v75_dependency_items
    }
    v75_actual_dependency_hashes = {
        (row["item_id"], row["depends_on"], row["relation"]):
            table_row_sha256(row)
        for row in dependencies if row["item_id"] in v75_dependency_items
    }
    v75_history = [
        row for row in history if row["release"] == "canon-v75-candidate"
    ]
    v75_history_by_event = {row["event_id"]: row for row in v75_history}
    v75_bad_claim = "TM-FOURPHASE-HULL-NONDESCENT"
    v75_bad_probe = "P-TM-FOURPHASE-HULL-NONDESCENT-1"
    checks.append((
        "V75-CLOSURE",
        "eight qualified theorems enter at exact scope while the photon germ "
        "closes locally, the broader global carrier stays O, and the stopped "
        "four-phase probe remains excluded",
        all(
            has_status(index, claim, "T")
            and scope_sha256(index, claim) == contract["scope"]
            and registry_row_sha256(index, claim) == contract["row"]
            and index[claim]["canon_section"] == contract["section"]
            and scope_contains_all(index, claim, contract["markers"])
            and normative[claim]["item_type"] == "THEOREM"
            and normative[claim]["claim_id"] == claim
            and normative[claim]["status"] == "T"
            and normative[claim]["layer"] == contract["layer"]
            and normative[claim]["gate_ids"] == ""
            and normative[claim]["statement_source"] == contract["source"]
            and evidence[claim]["evidence_id"] == "EV-" + claim
            and evidence[claim]["evidence_kind"] == "PUBLIC_PROBE"
            and evidence[claim]["location"] == contract["location"]
            and evidence[claim]["sha256"] == contract["bundle"]
            and evidence[claim]["hash_mode"] == "bundle-manifest-sha256-v1"
            and evidence[claim]["architecture_requirement"] == "two-architecture"
            and f"### {claim} [T]" in canon_text
            for claim, contract in v75_contract.items()
        )
        and v75_actual_dependencies == v75_dependencies
        and v75_actual_dependency_hashes == v75_dependency_hashes
        and len(v75_history) == 9
        and set(v75_history_by_event) == set(v75_history_hashes)
        and all(
            row["event_date"] == "2026-09-02"
            and row["release"] == "canon-v75-candidate"
            and table_row_sha256(row) == v75_history_hashes[event_id]
            and row["scope_sha256"] == scope_sha256(index, row["claim_id"])
            and row["evidence_id"] == evidence[row["claim_id"]]["evidence_id"]
            and row["evidence_location"] == evidence[row["claim_id"]]["location"]
            and row["evidence_sha256"] == evidence[row["claim_id"]]["sha256"]
            and (
                row["event_sequence"] == "1"
                and row["event_type"] == "DECLARE"
                and row["previous_status"] == "-"
                and row["new_status"] == "T"
                if row["claim_id"] in v75_claims
                else row["event_sequence"] == "3"
                and row["event_type"] == "SCOPE_CHANGE"
                and row["previous_status"] == "O"
                and row["new_status"] == "O"
            )
            for event_id, row in v75_history_by_event.items()
        )
        and has_status(index, "PHOTON-CONE-CONVERGENCE", "O")
        and scope_sha256(index, "PHOTON-CONE-CONVERGENCE")
        == "5c97f9bed2b084b792ed3f83e75507dd0bf9880d8191c7ff0e53712cdd9db245"
        and registry_row_sha256(index, "PHOTON-CONE-CONVERGENCE")
        == "d28ab8402d271dae36fe19861d007f807b03c3033bcf2c36f0a355b2c24119fc"
        and normative["PHOTON-CONE-CONVERGENCE"]["gate_ids"]
        == "GATE-L4-L5-PHOTON-GLOBAL-CARRIER"
        and evidence["PHOTON-CONE-CONVERGENCE"]["sha256"]
        == "5c97f9bed2b084b792ed3f83e75507dd0bf9880d8191c7ff0e53712cdd9db245"
        and "GATE-L4-L5-PHOTON-CONE-IDENTIFICATION" not in gates
        and "GATE-L4-L5-PHOTON-GLOBAL-CARRIER" in gates
        and gates["GATE-L4-L5-PHOTON-GLOBAL-CARRIER"]["owner_item_id"]
        == "PHOTON-CONE-CONVERGENCE"
        and gates["GATE-L4-L5-PHOTON-GLOBAL-CARRIER"]["from_layer"] == "L4"
        and gates["GATE-L4-L5-PHOTON-GLOBAL-CARRIER"]["to_layer"] == "L5"
        and gates["GATE-L4-L5-PHOTON-GLOBAL-CARRIER"]["gate_kind"] == "OPEN_LIFT"
        and table_row_sha256(gates["GATE-L4-L5-PHOTON-GLOBAL-CARRIER"])
        == "a0ba8c014ec012acf082f8a45e010d0161b7e6a5e5077472dd2266318596a711"
        and all(
            claim not in programs
            and all(row["owner_item_id"] != claim for row in gates.values())
            and all(row["claim_id"] != claim for row in core_selection_rows)
            and f"- {claim} [" not in frontier_text
            and f"- {claim} [" not in core_text
            for claim in v75_claims
        )
        and v75_bad_claim not in index
        and v75_bad_claim not in normative
        and v75_bad_claim not in evidence
        and v75_bad_claim not in programs
        and all(
            v75_bad_claim not in row["item_id"]
            and v75_bad_claim not in row["depends_on"]
            for row in dependencies
        )
        and all(v75_bad_claim not in row["claim_id"] for row in history)
        and all(v75_bad_probe not in row["location"] for row in evidence.values())
        and all(v75_bad_probe not in row["evidence_location"] for row in history)
        and v75_bad_claim not in canon_text
        and v75_bad_probe not in canon_text
    ))


    # Later additions are excluded only from the immutable earlier projections.
    v78_names = {
        "QDD-STABILIZER-UNCOMPUTE-POSTSTATES",
        "QDD-STABILIZER-COMMON-LATTICE-OBSTRUCTION",
    }
    v77_contract = {'J-CENTERING-IMAGE-INDEX': {'row': '7d24294dd1aede7199dc689145625078bac07409b74f9f847b83f480dc3e8cf6',
                                 'normative': '94bbcc18f771807885c4dffcd5045d18124ca0c456d6c038eb0c29b4d3f4c6bf',
                                 'evidence': '7c858185c0efd43083557ca58cf04248fb933c222064fafab32a408bde9b0877',
                                 'history': 'b0e4a2664c3592fa0fc61040ceebe477e79ddd0d66edf9e84ed867efb94634cd',
                                 'status': 'T',
                                 'layer': 'L1'},
     'RAPIDITY-GOLDEN-LADDER': {'row': 'd362173c2aba511bb23a402d6b3f45cb705a599c4d763c761ec09f8237882afb',
                                'normative': '4b465d1ebdd060943be2a34a5c9e94f9e5c58b6fe61432dab8f61ef523468ed9',
                                'evidence': 'baec375dc9d24d8b498c1ec1472957e140c6b86e8681eb33d6271b1d4d610e1b',
                                'history': '663a9b8c031ad6906f4c6dd8103e7528a908e436891be6977ef203adf2df713e',
                                'status': 'T',
                                'layer': 'NOT_APPLICABLE'},
     'RAPIDITY-TARGET-RECONSTRUCTION': {'row': '00c6ad9bb30bfc932c0cb2123e7cb5ce68ace447f7aff8c1d77ff368be0e73cd',
                                        'normative': 'b576ccce3821159f5f48904f0df847b8fd6a0290a7ea84411ea86382cbf237f8',
                                        'evidence': '114690f085c0e5e9888c753892dd5cac59386c2e6247a0cb547b082790b79299',
                                        'history': 'd6dd31b766f5600c7ac3c594ae43b4b8ac5082e9c6f0b5244a98d2dfe1f278f9',
                                        'status': 'T',
                                        'layer': 'NOT_APPLICABLE'},
     'POINTED-DECODER-PREFIX-CONSISTENCY': {'row': 'a0fc8e6aa1875e36cb373aa0408a718c9c2a7a44ecaa136391f5dfa4020ac1db',
                                            'normative': '14797cb7f7855ab67fe42a16c493cef38d51eaa03e77dbd212631bdeeff79171',
                                            'evidence': '6e35671bada33dd81061c445d718cd1f316518f9e362e7a20cb864e2bc0c175c',
                                            'history': '142dff01c8ba8bad3badc70dcca0c54beaa5f480e366ed28b615134ca5081dee',
                                            'status': 'T',
                                            'layer': 'L1'},
     'DECODER-RETARDED-LOCAL-ENERGY-TRANSPORT': {'row': '2b8b2deae4b73c7021a37293d55ab4731a4682f781e6cccf51a8e24bd85cab1c',
                                                 'normative': 'd2e0f694673bcce9447842191c23ae40abe72bdb337ea3319e1af8242af6534f',
                                                 'evidence': '1d8faa525f1d112dddd01e6e3625bf87a85d1d8a650310ce6a82a9fc5548e4b3',
                                                 'history': 'dada3835357bb39800d930b651411b911f94b9d5e5d24431cba53c5e2090356c',
                                                 'status': 'T',
                                                 'layer': 'L1'},
     'DECODER-RESERVOIR-RECORD-ACCOUNTING': {'row': '6da1dfaffc3ff259d665b4b68910a87b4ff7d1e8b712d0c4d0db668e8ab0c653',
                                             'normative': '9361aaee2fde659b8d1db7748e6c369ea532cbaa365bbde1dec39dbcce331f5e',
                                             'evidence': '8b8b90db46a974ae871fba8de9d0ec35267d69a4b0fff3e319b332283c546d17',
                                             'history': 'fc560d73e40f5b270e77fda1c9345bfa89f6dd82c5e664ba40b6bd04fed62e9a',
                                             'status': 'T',
                                             'layer': 'L1'},
     'DECODER-RESERVOIR-QUADRATIC-PARTITION': {'row': 'e7a2d32f343379c2967f3b163aba3dd90829e2b3d7e816739ad90389c7bdfb79',
                                               'normative': 'e3401903aca4e826690b2a397292d8441ff966a8b3953d73c31b40fe180c64cf',
                                               'evidence': '6eb13ac7c515ea772713d8b2ca55f4424ad8192eb604850fcbd0a71087dbb91f',
                                               'history': 'ff029d4bf642ad336a93b1c12f36229a41207066b64023cb049c47dc59dc41c6',
                                               'status': 'T',
                                               'layer': 'L1'},
     'DECODER-RESERVOIR-QDD-POSTPROCESSING-OBSTRUCTION': {'row': 'f1446d0cdc1b244842993f48e6fc4b11328663faee8f038d848cc099bdd7960d',
                                                          'normative': '7ac9ac88063f45a74d331de2fcdca8b9c5a35e01f48dc43fe792ef5a6b7300f3',
                                                          'evidence': '7fed264024c7e459b5bc58d572a8567b096b72ce15b7356b18023f75ad1bed4a',
                                                          'history': '8a7bf1555809878c81d10137531c7664aae5b9eeaae734ae5dc845e8167b5f86',
                                                          'status': 'T',
                                                          'layer': 'L1'},
     'NIST-RAW-PREFIX-CODEC-QUALIFICATION': {'row': 'f5c71075e26df473a44721561494e18acd95e3b1ba5fff5630c8036793f445bb',
                                             'normative': '522fb368f9dc724c6c49e5b2dcbc7f5aa9357d42ce7294101c514eef66500398',
                                             'evidence': 'ce4162911bdb70492f5c355535192d4d770c1d6b1455b0e0ccecb7f94d7ffdfb',
                                             'history': '6f5d382cee789546470600d1eeed35f7d7c3a768105a21e6972e93042a68ffbc',
                                             'status': 'C',
                                             'layer': 'L5'},
     'NIST-RUN3-RECORD-INTERVAL-ONEHOT': {'row': '4405ed039b7fd46d0147a7b3e5c66553173dfa320753a5ea9bb72cac3c868fcc',
                                          'normative': '5574f321aa847cc7bea3848e93e366b6a1015166a848f150ae44f9180abcd1e4',
                                          'evidence': '6240cb652cbbe5a3b8e803f2e5deb507f0fddb4682992fcef669e7b3a8fb165f',
                                          'history': '07fa151ba1c3ed8fbb09277bb5527deb1419cf16e1e6541c4c1d77b0c33f7fca',
                                          'status': 'C',
                                          'layer': 'L5'},
     'NIST-LOCAL-OBSERVATION-LOSSLESS': {'row': 'be4a6e19d7ecd61b026611d19cc1a78b8ce2ebe66340404c471be9335b0e9d43',
                                         'normative': '85015a1fcd44bc5a5da4ac809b9590fa13037a2ca929b7650e405c19fe83e6f1',
                                         'evidence': 'd1b478997155e2e6b5cf12a1871914cfa2ef75eaae85773e3772037e48b8f233',
                                         'history': '445ef8ccda0ccb4673eae6f515e588890d1e90b874ce2fa108493e89f6794967',
                                         'status': 'C',
                                         'layer': 'L5'},
     'NIST-LOCAL-OBSERVATION-PREFIX-CAUSALITY': {'row': '8ee08bf22c87f84ca34dd1d17460eaba16c63ddbd63de015590da4f64eafc50a',
                                                 'normative': '72fa9ed9b3fc633d85502d6f4e2853bae54c53069fdef2b073501c7fbb1f3c26',
                                                 'evidence': 'e07a810ecdfed6d176757ea0521267c78f6299ceab7d483b2c9dc65646c894b4',
                                                 'history': '627495b12b5835396b797869b8de7744265059c0ead14b7f707015a5731734bd',
                                                 'status': 'C',
                                                 'layer': 'L5'}}
    v77_names = set(v77_contract)

    # The v76 theorem-only fold preserves every previously registered row.
    v76_contract = {'J-CM-FIBONACCI-BRAID-PROJECTIVE-NONMEMBERSHIP': {'row': '358774de5e5ee215c2a728be0b3e66ef1a9d1ae24385c7c32cc663fa64a88bab',
                                                       'normative': '00b4f90e1fb8f23ae50c445ffeb5dc3c9eb40505951088bc60acd8824f59e8e0',
                                                       'evidence': 'bd80d92c79e3d1c90c5aea2e46d8471440ed536a95eebcd897a32c799caf9956',
                                                       'history': '42c3cb7a1d2a6f0f206baacce922124527b3486fb4e1870557124ecdbce84366'},
     'J-CIRCULAR-FIBONACCI-DETERMINANT-CHARACTER': {'row': '5690ac4968c4b98857f7c82b92f7261dfe5c07a8654f9204317121903d5c52bf',
                                                    'normative': 'aa29bf8beb36f9742ba196f937624cccd7b5ad41367685568a9678a95241a965',
                                                    'evidence': '2e327e2c17f8d4855fc08df04cef2b191b502837e5cf6f1f967aac4d316636e5',
                                                    'history': 'bd4698c5e95053c1390794234f4a7ccdff5b4db7a71254cf807ab957343ff6c7'},
     'J-GALOIS-CIRCULAR-QUOTIENT-SEMIDIRECT-UNITARY': {'row': '8877881b741ce23e0d9adb9a3cbacb66d8eb190175ac29e3cb7daf4dbd2ad74f',
                                                       'normative': '440412ff54080b6bdca372d59bb96a04bac4c97c79887d48a5d2d0b18ff89c02',
                                                       'evidence': '52ba8b1782ffd2125bffd78166398ca8a35c6a30246040c080ad4b8524558a17',
                                                       'history': '367391e45b6502101ff206ac1e2955dc646b158f8c7ba9c3e7c359aae6c0fd2c'},
     'J-GALOIS-CIRCULAR-ODD-CHARACTER': {'row': '24ec2afdbe23223048bc35ed8ab21433efd8bdc6c39a018af4483736ad604dc6',
                                         'normative': '9b160fd532587af6f6905256423c44d3d286194a132cdd376100995f4ecfa31f',
                                         'evidence': '228de8f5c40a71ad4104a49e41de03c408d851ea26fa30fadb033e526a7cdb0b',
                                         'history': 'bd82fdfd31663ac159e4c75a979a57a91186e08b8e10f1e0dd10a885dec6529e'},
     'J-CIRCULAR-QDD-DUAL-SIMPLEX-BRIDGE': {'row': 'd8d72ed56e8f729412e283f471a97717cdc5df343cb01ab6d3e10abc33880219',
                                            'normative': 'f685588556141102dd1d7a33e30e3d8aff1b772a61aeeb48416bd583e7202ba2',
                                            'evidence': '8781ffcd362f96df760ca7e50679568aa2310f6f65de5fe74869abb6031b73c2',
                                            'history': '206df14ea810d41183fc6df9b282aa3d1e46a62497dc59d476f627f284652aea'},
     'J-CIRCULAR-QDD-SIGNED-AFFINE-PROJECTOR-INTERTWINER': {'row': '6bc065bb2b38653430db68e659f472a4c7e1d2bc276654dc37c63f62a0a58fb2',
                                                            'normative': '3e922beb8819b0a3cbc5454fcce65dd7c73309edd603d9248eb63186eacb45e7',
                                                            'evidence': '8f7611ee3e8d5d8ff43cc12e10bce38170aaafbcb62e269aa1458a7c48d5710a',
                                                            'history': 'b45b42390bbcf8d480ceaf31dccc81b3d079d6512c9fe11b27d6b8226d3f138e'},
     'J-PLENUM-POLAR-ORBIT-SEPARATION': {'row': '0e85fd7a784863aeee31410282b8f8241b9f9403cab3402f6bcdabc4bebc8306',
                                         'normative': '771b5bfa55bcb7092f88e2273b178e05d0508611cae2621592f9e1fd5d185605',
                                         'evidence': 'ed570dc8064008f8f75ed1359b43d1201e35c2cb40839abb534d400c9dd0dbd8',
                                         'history': 'ba503dcf6dc601eb8fe06d309a7f0dbcc21fc7be3c182602bb4a38875d11be8c'},
     'J-SIMPLEX-TIGHT-FRAME-DILATION': {'row': '55701198cd97fd9baa7c0527aa4ea797cb6bac8f8f1c11b403347f3b1dd5f342',
                                        'normative': '60615a56933f26d8fb52fb401a39510dfe4acb00b5aba640895c524c88f9e884',
                                        'evidence': 'd79621a7f140ddaa4e09dda2cdafde0212fc7f5b8e35ff1f53edf86bb1e6d734',
                                        'history': 'ec2eb048e9a3bc0f1b03b8070c510ef835557266642da9a9bc48963e32ab3bad'},
     'J-SIMPLEX-QUADRATIC-SUPPORT-RIGIDITY': {'row': 'd8ac3d8b478c4b0bc174281ce3f76ac2270576cf35b0fef63b12f7f4876f8df5',
                                              'normative': '48224ca86cac176ead49768f4b4f0384d7f1607c52c5fa0e4cb2078d00016a81',
                                              'evidence': 'c79faf19c9343a2448686341831666bd54d19b98027b856f5aca4714c912d57f',
                                              'history': 'f2fc4fc0a489e6cb8491e74e2fe430e3cfe2873355563f886f4d8684a4a566ed'},
     'J-RESIDUAL-UNIT-NORMAL-FORM': {'row': '095f1e8c42bd695ff8715afb9f1049d22a0d02c0ceb869df516794e1cf4a3492',
                                     'normative': 'aab1281b4230094b0422769291348d6639b1bdb88425260711de4c0d8506668c',
                                     'evidence': '2e01a4aac5ad9c215cfcc68bff0c2a2528f591509836ae4b6b0c8cfdbf9aa2b5',
                                     'history': '9887673d9c22068dd10b412f2fd9ce5f4c8092ace78fdd8d78bcc853c25b91be'},
     'J-COINCIDENCE-CARTESIAN-GRAM-SEAM': {'row': '0e77b99202f6e9eb487e8d6f5d6e836645ed2d9ccbfaf8b0ee70041988bd5cf3',
                                           'normative': '1a33eed8f78033a2714486cfe8f99c663b8d671092e57e5c0a34ffd98c1ee9df',
                                           'evidence': '079aa2bd48f8c416844fbc9b6ed402a36c32485871f9c3e1d5287151f8e920b5',
                                           'history': '07ee8a05121dc9706d4d9003ebc2a69cf0700cde3a5aa7dc61b9f557b75c6832'}}
    v76_prior = {'CORE_SELECTION': 'a6fbcb3d9f353d9e86afb71a0c4ac770333eb1d070dbe782d1d2e4de9147e225',
     'DEPENDENCIES': 'b19d307f9054354ceb69c42692c42503f326e7d75c550c46cab8306feca6a8e9',
     'EVIDENCE': '9a0d70bdcff8edc24abdd930828f6d16ff637c3eed2a33f97ae36798cfa060f6',
     'FRONTIER_PROGRAMS': '5266805122ab90ee1e643c2026838c08dcbe6f707d09e46058b71dc891b21877',
     'GATES': 'dba992ba687c15778ad8873fbccaba372633a8d2a3579c387c4b79c5dec3be6b',
     'HISTORY': '9a2a53fb9e6017071dca75f4c8a61904ba5048c06d134a23f7882ca57863c6dd',
     'NORMATIVE': '6f5b7026cf1dfe4455d91dc28894c930d10d61f4a21a80dc7250dbe47973b33c',
     'REGISTRY': '60b85789e1a2cda52c089c8fc3e34b7db3418ca831477e497b9012a30c9582c8'}
    v76_dependency_hash = 'b9d85c1321ca35ff9be5e027cc2c77d5a32da6b62e6e83ee515420bd314123f1'
    v76_names = set(v76_contract)
    def v76_table_hash(table):
        return hashlib.sha256("\n".join(sorted(
            table_row_sha256(row) for row in table
        )).encode("utf-8")).hexdigest()
    v76_events = [row for row in history if row["release"] == "canon-v76-candidate"]
    v76_events_by_claim = {row["claim_id"]: row for row in v76_events}
    v76_old_tables = v79_historical_tables(
        v76_names | v77_names | v78_names,
        {"canon-v76-candidate", "canon-v77-candidate", "canon-v78-candidate"},
    )
    checks.append((
        "V76-L1-FOLD",
        "eleven L1 theorem rows enter with exact probe evidence; prior claims, "
        "gates and frontier stay fixed; fired polar-A and physical coincidence stay excluded",
        len(v76_contract) == 11
        and all(v76_table_hash(v76_old_tables[k]) == h for k,h in v76_prior.items())
        and len(v76_events) == 11 and set(v76_events_by_claim) == v76_names
        and v76_table_hash([r for r in dependencies if r["item_id"] in v76_names])
            == v76_dependency_hash
        and all(
            has_status(index, claim, "T")
            and registry_row_sha256(index, claim) == contract["row"]
            and table_row_sha256(normative[claim]) == contract["normative"]
            and normative[claim]["layer"] == "L1" and not normative[claim]["gate_ids"]
            and table_row_sha256(evidence[claim]) == contract["evidence"]
            and evidence[claim]["architecture_requirement"] == "two-architecture"
            and table_row_sha256(v76_events_by_claim[claim]) == contract["history"]
            and claim not in programs
            for claim,contract in v76_contract.items()
        )
        and "J-PLENUM-POLAR-GAUSS" not in index
        and "COINCIDENCE-RECORD-FREQUENCY" not in index
        and all("P-J-CIRCULAR-QDD-DUAL-SIMPLEX-BRIDGE-1" not in r["location"]
                for r in evidence.values())
    ))


    # The v77 release boundary requires exactly the new rows and the complete old ledger.
    v77_prior = {'CORE_SELECTION': 'a6fbcb3d9f353d9e86afb71a0c4ac770333eb1d070dbe782d1d2e4de9147e225',
     'DEPENDENCIES': '8a6ca647d68b2b260aa1d57dbb0773ca5d4924e8400f5b628714b59352dfa962',
     'EVIDENCE': '1982e26df439c2bd4528a5a1c89d2b1882fd97ff618e6ea677f599fa15bf55ea',
     'FRONTIER_PROGRAMS': '5266805122ab90ee1e643c2026838c08dcbe6f707d09e46058b71dc891b21877',
     'GATES': 'dba992ba687c15778ad8873fbccaba372633a8d2a3579c387c4b79c5dec3be6b',
     'HISTORY': '0cf95b030a24d6b3593528da5085381f577fea721e3b9201ec68fdcf69237245',
     'NORMATIVE': 'ac011815c65131d869730af5f66a2ab172f9dcadfd2045284883c4d4fa8726b6',
     'REGISTRY': '7a8f37d291dbbb8bb0ce0ad7a1e196328e18f093778b46b1fe74dfae8b3c2eae'}
    v77_dependency_hash = 'c0c8b11ac70c3504128f706649ed1df44c7a4a5805cec0a6c72c7af8e80da5cf'
    v77_events = [r for r in history if r["release"] == "canon-v77-candidate"]
    v77_events_by_claim = {r["claim_id"]: r for r in v77_events}
    v77_old_tables = v79_historical_tables(
        v77_names | v78_names,
        {"canon-v77-candidate", "canon-v78-candidate"},
    )
    checks.append((
        "V77-EARNED-FOLD",
        "eight conditional theorems and four bounded archive computations; exact source "
        "evidence and prior ledgers persist; physical Born and apparatus owners stay open",
        len(v77_contract) == 12
        and all(v76_table_hash(v77_old_tables[k]) == h for k,h in v77_prior.items())
        and len(v77_events) == 12 and set(v77_events_by_claim) == v77_names
        and v76_table_hash([r for r in dependencies if r["item_id"] in v77_names]) == v77_dependency_hash
        and all(
            has_status(index, claim, contract["status"])
            and registry_row_sha256(index, claim) == contract["row"]
            and table_row_sha256(normative[claim]) == contract["normative"]
            and normative[claim]["layer"] == contract["layer"]
            and not normative[claim]["gate_ids"]
            and table_row_sha256(evidence[claim]) == contract["evidence"]
            and evidence[claim]["architecture_requirement"] == "two-architecture"
            and table_row_sha256(v77_events_by_claim[claim]) == contract["history"]
            and claim not in programs
            for claim,contract in v77_contract.items()
        )
        and "J-PLENUM-POLAR-GAUSS" not in index
        and "COINCIDENCE-RECORD-FREQUENCY" not in index
    ))

    # Raw prior-table pins are from git show at the reviewed public main base
    # b349ffd76591b48fb7c2cccd1a2f42cf2066df6e, not from a filtered current tree.
    v78_prior = {
        "REGISTRY": "2e108c589cc1c1b7369d213ca9422c92f90da1ad7566a91c496b6e5444e9780d",
        "NORMATIVE": "24402d66df973634fd4ed5de704f9169a438e52453012332837ed2a1cf0e0aac",
        "DEPENDENCIES": "b61b5e15df5ec241565e49ff0480085a1f486be11c9a79dfea57209a870f76d3",
        "EVIDENCE": "6e2041809541b04f25cc5b1bc6a0aeda9e9810af3777da32786a5ddad58f1790",
        "HISTORY": "ba90121202a1ce00a9f75779b3cb15fd6e7123f51e80c2413a34defb6c1bb926",
        "GATES": "4f38b0d8c95a43d37190e57f416e865e6c1adf70378c0f9d4625c63bf8842ca3",
        "FRONTIER_PROGRAMS": "d7f7205acd461ff05ec7b31c45cc8e3b0ca3d4960432eb6053556fc5357da0d8",
        "CORE_SELECTION": "eee121dd437d06fc2b0fda5377ea6c2e6e01b220e5f1bfb9aa09727885d03d4e",
    }
    v78_contract = {
        "QDD-STABILIZER-UNCOMPUTE-POSTSTATES": {
            "row": "83e0a539945f02ba955dc1e88b40d1d548a18ef2c541b10f8f5afc11d21edc19",
            "normative": "f0b779d954fd739848942383ca10ff285c884f5632afaf459d37248a7913e22b",
            "evidence": "17794136dd02bddf589a65813fd3d0e59b6dedaa46141fc7c98360dc399a48fb",
            "history": "53bf05395db17f08fa0eb50485ff45abb481563e872825700a0f889a85bdcf46",
        },
        "QDD-STABILIZER-COMMON-LATTICE-OBSTRUCTION": {
            "row": "1e3a26b3739e05b9cb4b182aea3a1a476f82991063da3a5e3504369c01502ebb",
            "normative": "b408b2624331f2524bbdc0a77c620b4242857c9288a7713bb3783e988b9c3f5b",
            "evidence": "99101e0a95c4b63859e47d6f904534c98daa9de14a8bfe541c38d7a58ae8a634",
            "history": "e1d8fae4e00799c32952350412c1eda5df0b0c39a7d6668c7c03844bf8b47d1f",
        },
    }
    v78_projection = {
        "REGISTRY": (REGISTRY, "claim_id", v78_names),
        "NORMATIVE": (NORMATIVE, "item_id", v78_names),
        "DEPENDENCIES": (DEPENDENCIES, "item_id", v78_names),
        "EVIDENCE": (EVIDENCE, "claim_id", v78_names),
        "HISTORY": (HISTORY, "release", {"canon-v78-candidate"}),
        "GATES": (GATES, None, ()),
        "FRONTIER_PROGRAMS": (FRONTIER_PROGRAMS, None, ()),
        "CORE_SELECTION": (CORE_SELECTION, None, ()),
    }
    v78_events = [r for r in history if r["release"] == "canon-v78-candidate"]
    v78_events_by_claim = {r["claim_id"]: r for r in v78_events}
    v78_dependencies = [r for r in dependencies if r["item_id"] in v78_names]
    checks.append((
        "V78-QDD-STABILIZER",
        "two conditional L4 circuit and lattice theorems enter on exact probe evidence; "
        "the complete prior ledger and every physical open obligation remain unchanged",
        set(v78_contract) == v78_names
        and all(
            projected_file_sha256(*v78_projection[name]) == digest
            for name, digest in v78_prior.items()
        )
        and len(v78_events) == 2 and set(v78_events_by_claim) == v78_names
        and len(v78_dependencies) == 4
        and v76_table_hash(v78_dependencies)
        == "a2d3c505df9a24a387272cd9158bfa3bb6e72ab4477a5c5a364241ebcca29fb2"
        and all(
            has_status(index, claim, "T")
            and registry_row_sha256(index, claim) == contract["row"]
            and table_row_sha256(normative[claim]) == contract["normative"]
            and normative[claim]["item_type"] == "THEOREM"
            and normative[claim]["layer"] == "L4" and not normative[claim]["gate_ids"]
            and table_row_sha256(evidence[claim]) == contract["evidence"]
            and evidence[claim]["evidence_kind"] == "PUBLIC_PROBE"
            and evidence[claim]["location"] == "probes/P-QDD-STABILIZER-APPARATUS-1/RESULT.md"
            and evidence[claim]["hash_mode"] == "bundle-manifest-sha256-v1"
            and evidence[claim]["sha256"]
            == "c1d33c7dbd7513862431a17b24b231f8ca53f94df274c9914f1a196c938058f3"
            and evidence[claim]["architecture_requirement"] == "two-architecture"
            and table_row_sha256(v78_events_by_claim[claim]) == contract["history"]
            and f"### {claim} [T]" in canon_text
            and claim not in programs
            and all(r["owner_item_id"] != claim for r in gates.values())
            and all(r["claim_id"] != claim for r in core_selection_rows)
            and claim not in frontier_text
            for claim, contract in v78_contract.items()
        )
        and all(has_status(index, claim, "O") for claim in (
            "QDD-INSTRUMENT-APPARATUS", "QDD-TERMINAL-EVENT-SEMANTICS",
            "QDD-INSTRUMENT-CLASS-COMPLETENESS",
        ))
        and qdd_current_split
    ))

    checks.append((
        "V79-PRIOR-LEDGERS",
        "exact pinned row replacements reconstruct every byte of the prior v78 "
        "ledger; no earlier hash, lifecycle row or unlisted claim is relaxed",
        set(V79_LEDGER_PATCH) == {
            "REGISTRY.tsv", "NORMATIVE.tsv", "DEPENDENCIES.tsv", "EVIDENCE.tsv",
            "HISTORY.tsv", "GATES.tsv", "FRONTIER_PROGRAMS.tsv", "CORE_SELECTION.tsv",
        }
        and all(
            v79_previous_bytes(ROOT / "canon" / name) is not None
            for name in V79_LEDGER_PATCH
        ),
    ))
    curvature = "CURVATURE-OPERATOR-CANONICAL"
    trace_claim = "CURVATURE-TRACE-READOUT-UNIQUE"
    curvature_gate = "GATE-L1-L2-CURVATURE-CANONICAL"
    checks.append((
        "V79-CURVATURE",
        "raw-class nonuniqueness closes the named O at T; the separate trace "
        "readout strengthening is F and owns the terminal gate; time cut stays D",
        has_status(index, curvature, "T")
        and normative.get(curvature, {}).get("item_type") == "THEOREM"
        and normative.get(curvature, {}).get("layer") == "L2"
        and normative.get(curvature, {}).get("gate_ids") == ""
        and curvature not in programs
        and has_status(index, trace_claim, "F")
        and normative.get(trace_claim, {}).get("item_type") == "FALSIFIED"
        and normative.get(trace_claim, {}).get("layer") == "L2"
        and normative.get(trace_claim, {}).get("gate_ids") == curvature_gate
        and gates.get(curvature_gate, {}).get("owner_item_id") == trace_claim
        and gates.get(curvature_gate, {}).get("gate_kind") == "FIRED_NEGATIVE"
        and gates.get(curvature_gate, {}).get("from_layer") == "L1"
        and gates.get(curvature_gate, {}).get("to_layer") == "L2"
        and has_status(index, "TIME-CUT-READING", "D")
        and any(
            row["claim_id"] == curvature and row["event_type"] == "STATUS_CHANGE"
            and row["previous_status"] == "O" and row["new_status"] == "T"
            and row["release"] == "canon-v79-candidate"
            for row in history
        )
        and any(
            row["claim_id"] == "TIME-CUT-READING"
            and row["event_type"] == "SCOPE_CHANGE"
            and row["previous_status"] == row["new_status"] == "D"
            and row["release"] == "canon-v79-candidate"
            for row in history
        )
        and all(
            normative.get(name, {}).get("item_type") == "DEFINITION"
            and normative.get(name, {}).get("layer") == "L2"
            for name in (
                "DEF-NATIVE-WORD-CURVATURE-CLASS", "DEF-CURVATURE-TRACE-SUBRECORD",
            )
        ),
    ))
    stream_definition = "DEF-NATIVE-READER-STREAM"
    stream_gate = "GATE-L1-L5-NATIVE-READER-STREAM"
    checks.append((
        "V79-NATIVE-DECODER",
        "six conditional mathematical theorems and one finite C audit retain "
        "their exact sources; L5 spectra use a typed projection and physical QDD stays O",
        all(
            has_status(index, claim, status)
            and normative.get(claim, {}).get("layer") == layer
            and normative.get(claim, {}).get("item_type")
                == ("THEOREM" if status == "T" else "COMPUTATION")
            and evidence.get(claim, {}).get("evidence_kind") == "PUBLIC_PROBE"
            and evidence.get(claim, {}).get("hash_mode") == "bundle-manifest-sha256-v1"
            and evidence.get(claim, {}).get("architecture_requirement") == "two-architecture"
            and claim not in programs
            and any(
                row["claim_id"] == claim and row["event_type"] == "DECLARE"
                and row["previous_status"] == "-" and row["new_status"] == status
                and row["release"] == "canon-v79-candidate"
                for row in history
            )
            for claim, (status, layer) in V79_NATIVE_ROWS.items()
        )
        and normative.get(stream_definition, {}).get("item_type") == "DEFINITION"
        and normative.get(stream_definition, {}).get("layer") == "L5"
        and normative.get(stream_definition, {}).get("gate_ids") == stream_gate
        and gates.get(stream_gate, {}).get("owner_item_id") == stream_definition
        and gates.get(stream_gate, {}).get("gate_kind") == "DEFINITION_PROJECTION"
        and gates.get(stream_gate, {}).get("from_layer") == "L1"
        and gates.get(stream_gate, {}).get("to_layer") == "L5"
        and any(
            row["item_id"] == "U-NATIVE-READER-STREAM-SPECTRA"
            and row["depends_on"] == stream_definition and row["relation"] == "REQUIRES"
            for row in dependencies
        )
        and all(has_status(index, claim, "O") for claim in (
            "QDD-INSTRUMENT-APPARATUS", "QDD-TERMINAL-EVENT-SEMANTICS",
            "QDD-INSTRUMENT-CLASS-COMPLETENESS",
        ))
        and qdd_current_split,
    ))

    checks.append((
        "V80-PRIOR-LEDGERS",
        "only exact pinned v80 additions are removed to recover every v79 byte; "
        "the unchanged v79 reconstruction still enforces every older ledger hash",
        set(V80_LEDGER_PATCH) == set(V79_LEDGER_PATCH)
        and tuple(len(V80_LEDGER_PATCH[name]["remove"]) for name in (
            "REGISTRY.tsv", "NORMATIVE.tsv", "DEPENDENCIES.tsv", "EVIDENCE.tsv",
            "HISTORY.tsv", "GATES.tsv", "FRONTIER_PROGRAMS.tsv", "CORE_SELECTION.tsv",
        )) == (5, 5, 13, 5, 5, 0, 0, 0)
        and all(
            v80_previous_bytes(ROOT / "canon" / name) is not None
            and v79_previous_bytes(ROOT / "canon" / name) is not None
            for name in V80_LEDGER_PATCH
        ),
    ))
    v80_names = set(V80_ROWS)
    v80_events = [
        row for row in history
        if row["release"] == "canon-v80-candidate" and row["claim_id"] in v80_names
    ]
    v80_dependencies = [row for row in dependencies if row["item_id"] in v80_names]
    checks.append((
        "V80-CLOSURE-BOUNDARIES",
        "three proof-backed T rows retain complete-source and onset conditions at L1 "
        "and full CP three-pass rigidity at L4 on one exact two-architecture probe",
        len(v80_names) == 3
        and len(v80_events) == 3
        and {row["claim_id"] for row in v80_events} == v80_names
        and len(v80_dependencies) == 13
        and all(
            has_status(index, claim, "T")
            and index[claim]["evidence"] == V80_PROBE + "/RESULT.md"
            and normative.get(claim, {}).get("item_type") == "THEOREM"
            and normative.get(claim, {}).get("status") == "T"
            and normative.get(claim, {}).get("layer") == layer
            and normative.get(claim, {}).get("gate_ids") == ""
            and evidence.get(claim, {}).get("evidence_kind") == "PUBLIC_PROBE"
            and evidence.get(claim, {}).get("location") == V80_PROBE + "/RESULT.md"
            and evidence.get(claim, {}).get("sha256") == V80_BUNDLE_SHA256
            and evidence.get(claim, {}).get("hash_mode") == "bundle-manifest-sha256-v1"
            and evidence.get(claim, {}).get("architecture_requirement") == "two-architecture"
            and f"### {claim} [T]" in canon_text
            and proof in V80_PROOF_HASHES
            and claim not in programs
            and claim not in frontier_text
            and all(row["owner_item_id"] != claim for row in gates.values())
            and all(row["claim_id"] != claim for row in core_selection_rows)
            for claim, (layer, proof) in V80_ROWS.items()
        )
        and all(
            (ROOT / V80_PROBE / name).is_file()
            and hashlib.sha256((ROOT / V80_PROBE / name).read_bytes()).hexdigest() == digest
            for name, digest in V80_PROOF_HASHES.items()
        )
        and all(
            row["event_type"] == "DECLARE"
            and row["event_sequence"] == "1"
            and row["previous_status"] == "-" and row["new_status"] == "T"
            and row["scope_sha256"] == scope_sha256(index, row["claim_id"])
            and row["evidence_location"] == V80_PROBE + "/RESULT.md"
            and row["evidence_sha256"] == V80_BUNDLE_SHA256
            for row in v80_events
        )
        and all(
            row["depends_on"] not in v80_names
            and (
                row["relation"] != "REQUIRES"
                or normative[row["item_id"]]["layer"]
                   == normative[row["depends_on"]]["layer"]
            )
            for row in v80_dependencies
        )
        and scope_contains_all(index, "U-NATIVE-COMMON-READY-SOURCE-RETENTION", (
            "all 25 common source-independent readies", "at the 21 readies",
            "125 double and 375 single fibres", "at least 124 pairs are supported",
            "factor exactly through F3", "full-state access and common readiness are conditions",
            "virtual readback supplies no physical preparation",
        ))
        and scope_contains_all(index, "QDD-INCIDENCE-FIRST-HIT-CLASSIFICATION", (
            "inclusive predecessor-gap partition", "empty support NO_EVENT and no ratio",
            "identical first-label functions at all 1024 onsets", "1/6 and 1/26",
            "excluding every common source-independent onset law",
            "when A,B>0 the accepted cyclic word", "without-replacement ordered law",
            "not derived physical occurrence, storage, reset or L6 measure",
        ))
        and scope_contains_all(index, "QDD-MIXED-CHANNEL-ATTENUATION-RIGIDITY", (
            "supports over R or C", "complete CP repeatable branch fibre",
            "full unnormalized operators", "spanning determinant -1024",
            "first two B_n admit a rational nonidentity pinching channel",
            "rational 72-Kraus depolarizing witness", "exact reduced-channel equality",
            "no physical attenuation-preservation law",
        )),
    ))
    checks.append((
        "V80-PHYSICAL-OWNERS",
        "all three physical QDD obligations retain their exact v79 rows at O; "
        "readback, conditional onset laws and mixed-channel selection create no physical gate",
        all(
            has_status(index, claim, "O")
            and registry_row_sha256(index, claim) == digest
            and normative.get(claim, {}).get("item_type") == "OBLIGATION"
            and normative.get(claim, {}).get("status") == "O"
            and programs.get(claim, {}).get("work_state") == "STOP"
            for claim, digest in V80_PHYSICAL_ROW_HASHES.items()
        )
        and qdd_current_split
        and scope_contains_all(index, "QDD-INSTRUMENT-APPARATUS", (
            "SAMPLING NOT PROVIDED", "UNRESOLVED",
            "PHYSICAL-DMATTER remains unadopted",
        ))
        and "GATE-L1-L5-QDD-INSTRUMENT-APPARATUS" not in gates
        and "GATE-L1-L6-QDD-BORN-READOUT" not in gates
        and "QDD-BORN-READOUT-MEASURE" not in index
        and all(
            not V80_LEDGER_PATCH[name]["remove"]
            for name in ("GATES.tsv", "FRONTIER_PROGRAMS.tsv", "CORE_SELECTION.tsv")
        ),
    ))
    r3_names = set(V80_R3_ROWS)
    r3_events = [
        row for row in history
        if row["release"] == "canon-v80-candidate" and row["claim_id"] in r3_names
    ]
    checks.append((
        "V80-READING-BOUNDARIES",
        "two later L4 theorems bound the quadratic decoder on self-contained inline "
        "Canon proof; they add no dependency, gate, program or CORE selection and "
        "leave every physical QDD owner open",
        len(r3_names) == 2
        and len(r3_events) == 2
        and {row["claim_id"] for row in r3_events} == r3_names
        and not (r3_names & v80_names)
        and all(
            has_status(index, claim, "T")
            and index[claim]["evidence"] == "inline"
            and index[claim]["canon_section"] == V80_R3_SECTION
            and scope_sha256(index, claim) == digest
            and normative.get(claim, {}).get("item_type") == "THEOREM"
            and normative.get(claim, {}).get("status") == "T"
            and normative.get(claim, {}).get("layer") == layer
            and normative.get(claim, {}).get("gate_ids") == ""
            and evidence.get(claim, {}).get("evidence_kind") == "INLINE_CANON"
            and evidence.get(claim, {}).get("location") == "inline"
            and evidence.get(claim, {}).get("sha256") == digest
            and evidence.get(claim, {}).get("hash_mode") == "registry-scope-sha256-v1"
            and evidence.get(claim, {}).get("architecture_requirement") == "none"
            and f"### {claim} [T]" in canon_text
            and claim not in programs
            and claim not in frontier_text
            and all(row["owner_item_id"] != claim for row in gates.values())
            and all(row["claim_id"] != claim for row in core_selection_rows)
            and all(
                row["item_id"] != claim and row["depends_on"] != claim
                for row in dependencies
            )
            for claim, (layer, digest) in V80_R3_ROWS.items()
        )
        and all(
            row["event_type"] == "DECLARE"
            and row["event_sequence"] == "1"
            and row["previous_status"] == "-" and row["new_status"] == "T"
            and row["scope_sha256"] == scope_sha256(index, row["claim_id"])
            and row["evidence_location"] == "inline"
            and row["evidence_sha256"] == scope_sha256(index, row["claim_id"])
            for row in r3_events
        )
        and scope_contains_all(index, "A4-RATIONAL-FRAME-WEIGHT-NONUNIQUENESS", (
            "the ternary norm-residue H([v])=h_3(q(v))", "sum H=0 on every complete frame",
            "all 30 inner Cl(4) rays retain 1/4", "defect D=3t",
            "do not force the owner-adopted quadratic reading",
            "without asserting a physical realization of the alternative weights",
        ))
        and scope_contains_all(index, "QDD-SIMPLEX-PAIR-INCIDENCE", (
            "U is the least universal integer clearing both x and P_kx",
            "a_k=N e_k-1 is the primitive LOW generator with q(a_k)=U",
            "literal ordered Cartesian-pair cardinalities",
            "second-order integer pair-incidence census", "at N=p=5, U=20",
            "no uniqueness, physical apparatus, occurrence, sampling or L6 measure is claimed",
        ))
        and all(has_status(index, claim, "O") for claim in (
            "QDD-INSTRUMENT-APPARATUS", "QDD-TERMINAL-EVENT-SEMANTICS",
            "QDD-INSTRUMENT-CLASS-COMPLETENESS",
        )),
    ))
    checks.append((
        "V81-PRIOR-LEDGERS",
        "only exact pinned v81 additions are removed to recover every v80 byte; "
        "the unchanged v80 and v79 reconstructions still enforce every older ledger hash",
        set(V81_LEDGER_PATCH) == set(V80_LEDGER_PATCH)
        and tuple(len(V81_LEDGER_PATCH[name]["remove"]) for name in (
            "REGISTRY.tsv", "NORMATIVE.tsv", "DEPENDENCIES.tsv", "EVIDENCE.tsv",
            "HISTORY.tsv", "GATES.tsv", "FRONTIER_PROGRAMS.tsv", "CORE_SELECTION.tsv",
        )) == (8, 8, 29, 8, 8, 0, 0, 0)
        and all(
            v81_previous_bytes(ROOT / "canon" / name) is not None
            for name in V81_LEDGER_PATCH
        ),
    ))
    v81_names = set(V81_ROWS)
    v81_events = [
        row for row in history
        if row["release"] == "canon-v81-candidate" and row["claim_id"] in v81_names
    ]
    v81_dependencies = [row for row in dependencies if row["item_id"] in v81_names]
    checks.append((
        "V81-DECODER-BOUNDARY",
        "eight L1 theorems delimit relational reading, occurrence, native readers, "
        "addresses, loaders, registration pairs and the composed record chain on exact "
        "two-architecture probes; they add no gate, program or CORE selection, declare "
        "only same-layer requirements and owner boundaries, and leave every physical "
        "QDD owner open",
        len(v81_names) == 8
        and len(v81_events) == 8
        and {row["claim_id"] for row in v81_events} == v81_names
        and not (v81_names & v80_names)
        and not (v81_names & set(V80_R3_ROWS))
        and all(
            has_status(index, claim, "T")
            and index[claim]["evidence"] == probe + "/RESULT.md"
            and index[claim]["canon_section"] == V81_SECTION
            and normative.get(claim, {}).get("item_type") == "THEOREM"
            and normative.get(claim, {}).get("status") == "T"
            and normative.get(claim, {}).get("layer") == "L1"
            and normative.get(claim, {}).get("gate_ids") == ""
            and evidence.get(claim, {}).get("evidence_kind") == "PUBLIC_PROBE"
            and evidence.get(claim, {}).get("location") == probe + "/RESULT.md"
            and evidence.get(claim, {}).get("sha256") == digest
            and evidence.get(claim, {}).get("hash_mode") == "bundle-manifest-sha256-v1"
            and evidence.get(claim, {}).get("architecture_requirement") == "two-architecture"
            and f"### {claim} [T]" in canon_text
            and all(
                (ROOT / probe / name).is_file()
                for name in ("PREREG.md", "PROOF.md", "verify.py", "EXPECTED.txt",
                             "RUN.md", "RESULT.md")
            )
            and claim not in programs
            and claim not in frontier_text
            and all(row["owner_item_id"] != claim for row in gates.values())
            and all(row["claim_id"] != claim for row in core_selection_rows)
            for claim, (probe, digest) in V81_ROWS.items()
        )
        and all(
            row["event_type"] == "DECLARE"
            and row["event_sequence"] == "1"
            and row["previous_status"] == "-" and row["new_status"] == "T"
            and row["scope_sha256"] == scope_sha256(index, row["claim_id"])
            and row["evidence_location"] == V81_ROWS[row["claim_id"]][0] + "/RESULT.md"
            and row["evidence_sha256"] == V81_ROWS[row["claim_id"]][1]
            for row in v81_events
        )
        and len(v81_dependencies) == 29
        and all(
            (
                row["relation"] == "REQUIRES"
                and normative[row["depends_on"]]["layer"] == "L1"
                and normative[row["depends_on"]]["item_type"] in ("THEOREM", "DEFINITION")
            ) or (
                row["relation"] == "BOUNDED_BY"
                and row["depends_on"] in V81_OWNERS
                and has_status(index, row["depends_on"], "O")
            )
            for row in v81_dependencies
        )
        and all(has_status(index, claim, "O") for claim in (
            "QDD-INSTRUMENT-APPARATUS", "QDD-TERMINAL-EVENT-SEMANTICS",
            "QDD-INSTRUMENT-CLASS-COMPLETENESS",
        )),
    ))

    checks.append((
        "V82-PRIOR-LEDGERS",
        "only exact pinned v82 additions are removed to recover every v81 byte; "
        "the unchanged v81, v80 and v79 contracts still enforce every older ledger hash",
        set(V82_LEDGER_PATCH) == set(V81_LEDGER_PATCH)
        and tuple(len(V82_LEDGER_PATCH[name]["remove"]) for name in (
            "REGISTRY.tsv", "NORMATIVE.tsv", "DEPENDENCIES.tsv", "EVIDENCE.tsv",
            "HISTORY.tsv", "GATES.tsv", "FRONTIER_PROGRAMS.tsv", "CORE_SELECTION.tsv",
        )) == (1, 2, 7, 1, 1, 0, 0, 0)
        and all(
            v82_previous_bytes(ROOT / "canon" / name) is not None
            for name in V82_LEDGER_PATCH
        ),
    ))
    v82_items = {V82_DEFINITION, V82_CLAIM}
    v82_boundaries = {
        "TT-SQUARING-DECODER": "D",
        "PHOTON-SPATIAL-TEMPORAL-TRANSFER": "D",
        "FRW-INHOM": "O",
        "TT-SOURCE": "O",
        "TT-VECTOR-STATE-NORMALIZATION": "O",
    }
    v82_expected_edges = {
        (V82_DEFINITION, "DEF-ARCHITECTURE", "REQUIRES"),
        (V82_CLAIM, V82_DEFINITION, "REQUIRES"),
    } | {(V82_CLAIM, owner, "BOUNDED_BY") for owner in v82_boundaries}
    v82_actual_edges = {
        (row["item_id"], row["depends_on"], row["relation"])
        for row in dependencies
        if row["item_id"] in v82_items or row["depends_on"] in v82_items
    }
    v82_events = [row for row in history if row["claim_id"] == V82_CLAIM]
    v82_start = canon_text.find("### DEF-K1-LINEAR-METRIC\n")
    v82_end = canon_text.find("## 15. Couplings, instruments, and metrology", v82_start)
    v82_block = (
        canon_text[v82_start:v82_end].encode("utf-8")
        if v82_start >= 0 and v82_end > v82_start else b""
    )
    checks.append((
        "V82-K1-LINEAR-METRIC",
        "one explicit L1 definition and one inline-proof theorem fix the K1 matrix "
        "history, full linear equations and all-time signature; exact boundary edges "
        "preserve physical readings and open owners without a native-U or nonlinear closure",
        has_status(index, V82_CLAIM, "T")
        and V82_DEFINITION not in index
        and V82_DEFINITION not in evidence
        and scope_sha256(index, V82_CLAIM) == V82_SCOPE_SHA256
        and index[V82_CLAIM]["canon_section"] == "14. The gravitational wave program"
        and index[V82_CLAIM]["evidence"] == "inline"
        and normative.get(V82_DEFINITION) == {
            "item_id": V82_DEFINITION, "item_type": "DEFINITION", "claim_id": "",
            "status": "", "layer": "L1", "gate_ids": "",
            "statement_source": "canon/CANON.md::" + V82_DEFINITION,
        }
        and normative.get(V82_CLAIM) == {
            "item_id": V82_CLAIM, "item_type": "THEOREM", "claim_id": V82_CLAIM,
            "status": "T", "layer": "L1", "gate_ids": "",
            "statement_source": "canon/CANON.md::" + V82_CLAIM,
        }
        and evidence.get(V82_CLAIM) == {
            "claim_id": V82_CLAIM, "evidence_id": "EV-" + V82_CLAIM,
            "evidence_kind": "INLINE_CANON", "location": "inline",
            "sha256": V82_SCOPE_SHA256, "hash_mode": "registry-scope-sha256-v1",
            "architecture_requirement": "none",
        }
        and len(v82_events) == 1
        and v82_events[0]["event_id"] == "CANON82-DECLARE-" + V82_CLAIM
        and v82_events[0]["event_sequence"] == "1"
        and v82_events[0]["release"] == "canon-v82-candidate"
        and v82_events[0]["event_type"] == "DECLARE"
        and v82_events[0]["previous_status"] == "-"
        and v82_events[0]["new_status"] == "T"
        and v82_events[0]["scope_sha256"] == V82_SCOPE_SHA256
        and v82_events[0]["evidence_id"] == "EV-" + V82_CLAIM
        and v82_events[0]["evidence_location"] == "inline"
        and v82_events[0]["evidence_sha256"] == V82_SCOPE_SHA256
        and not any(row["claim_id"] == V82_DEFINITION for row in history)
        and v82_actual_edges == v82_expected_edges
        and len(v82_block) == V82_CANON_BYTES
        and hashlib.sha256(v82_block).hexdigest() == V82_CANON_SHA256
        and b"### K1-LINEAR-METRIC-COMPLETION [T]" in v82_block
        and all(has_status(index, owner, status)
                for owner, status in v82_boundaries.items())
        and all(item not in programs and item not in frontier_text for item in v82_items)
        and all(row["owner_item_id"] not in v82_items for row in gates.values())
        and all(row["claim_id"] not in v82_items for row in core_selection_rows),
    ))

    print("TWIST-J theorem/dictionary separation audit")
    print("exact algebra and finite computations remain distinct from physical readings")
    print()
    passed = 0
    for number, (tag, description, ok) in enumerate(checks, 1):
        state = "PASS" if ok else "FAIL"
        print(f"{state} {number:02d} {tag:<10} {description}")
        passed += int(ok)
    print()
    print(f"RESULT {passed}/{len(checks)} "
          f"{'ALL PASS' if passed == len(checks) else 'FAIL'}")
    return 0 if passed == len(checks) else 1


if __name__ == "__main__":
    sys.exit(run())
