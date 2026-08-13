# Exact run

The G0 source/field replay was also executed after the preregistration pin:

```bash
python3 verify_g0_g1.py AME46_ORIGINAL.m > SOURCE_FIELD_OUTPUT.txt
cmp EXPECTED_G0_G1.txt SOURCE_FIELD_OUTPUT.txt
```

It exited zero and was byte-identical.  The transcript SHA-256 is

```text
3ed4587d8526cc3625cfbceefa4a8ab66983795c0bd90111e7486dd296d964cb  SOURCE_FIELD_OUTPUT.txt
```

```bash
python3 verify_galois_descent.py AME46_ORIGINAL.m \
  --output-certificate TRANSPORTER_CERT.txt > OUTPUT.txt
sha256sum verify_galois_descent.py OUTPUT.txt TRANSPORTER_CERT.txt
```

Expected SHA-256:

```text
25f38f1e66650bcc52150c2c9c74240c02535bc892cdce9544bc8d1a0efc9998  verify_galois_descent.py
bdeae71e195d9c456e49384e65efc7644172a54c720d5c1bc9e7e527793be56c  OUTPUT.txt
399b7a1bb6f9b954f1b3e266a0e7ee329a9d406661e52b79d690854ca11f93b3  TRANSPORTER_CERT.txt
```

The sole source input must have SHA-256
`55fbc0ba2747b4e5adc5a5abd15ac7241a461ff8182268ebdae464d8a29cc9ae`.

Recorded environment and replay:

```text
Python 3.12.13
Linux 6.18.35 x86_64
elapsed 1.186 s
exit code 0
stderr empty
OUTPUT.txt and TRANSPORTER_CERT.txt byte-identical on rerun
PYTHONHASHSEED=1 and PYTHONHASHSEED=987654321 byte-identical
```

Independent cross-check:

```bash
python3 crosscheck.py AME46_ORIGINAL.m --output CROSSCHECK.json \
  > EXPECTED_CROSSCHECK.txt
```

It was replayed under a changed `PYTHONHASHSEED`; both JSON and stdout were
byte-identical.
