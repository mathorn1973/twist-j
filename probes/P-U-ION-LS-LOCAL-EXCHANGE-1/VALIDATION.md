# Repository validation

NON-CANONICAL. These checks validate the formal record and repository;
they do not calibrate a physical ion device.

The accepted nine-file scientific candidate is unchanged from public pin
`b1b2019f35fc2cc3bc5b3d364f9d6ad8c2051a11`. New files after that pin are
actual stdout, run/outcome records and neutral review/validation material.
No old probe, Canon file, registry, policy, workflow or replay mechanism is
changed by this PR.

Local checks completed on 2026-10-04:

```text
python tools/check_policy.py           POLICY PASS
python tools/check_canon.py            CANON PASS v97 claims=492
python tools/check_ledger.py           LEDGER PASS
python tools/check_gate_contract.py    GATE CONTRACT PASS
python3 -m unittest discover -s tools -p 'test_*.py'
                                      172 tests OK (Linux)
python3 tools/check_verifier.py --base 2973a432303e046aacb2cee3cea97254ea3ab8eb
                                      VERIFY PASS P-U-ION-LS-LOCAL-EXCHANGE-1
python tools/check_reproduce.py --base 2973a432303e046aacb2cee3cea97254ea3ab8eb
                                      REPRODUCE NOT APPLICABLE
```

The Linux replay matched verifier SHA-256
`0a12e3ff056638ee4b9c373f7848b338b7a7c335ea5876c620ea0d0b2a530eee`
and stdout SHA-256
`baa2242ce69f4d28872a88048697e3447acb5ac60e48e26150649861fe7106fd`.
It is a replay of the recorded execution, not a new candidate or new pin.

The initial infrastructure-test invocation found that RUN.md's human-readable
table lacked the parser's required lowercase field names. The neutral run
record was given the required machine-readable block with the same observed
values; all 172 tests then passed. No scientific code, input, expected output
or threshold changed. Deliberate failure-fixture messages printed by that
successful test suite are not failed scientific probes.

Required public x86_64, aarch64 and aggregate check results must be read at
the exact final PR head. Local success alone is not the cross-architecture
gate. Publication/release work is outside this probe.

Security and scope review found only the declared source/proof files,
small exact Python checks, custody manifest and neutral result records.
No credentials, private identifiers, private logs, third-party source copies,
large data, binary output or machine nickname is committed. Files were staged
by name, and whitespace checking passed before the evidence commit.
