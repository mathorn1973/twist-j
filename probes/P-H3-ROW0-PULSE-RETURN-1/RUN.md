# H3 pulse-return run record

```text
pin_commit: 1cb47b7ec72bc0c4556bde8e37f64347584739dd
verifier_sha256: 4259f3c0209d97cd4c932f1f93f2796f27eb6a82873b8793b73fd9428f80c857
command: python3 probes/P-H3-ROW0-PULSE-RETURN-1/verify.py
platform: Ubuntu 22.04.5 LTS
architecture: x86_64
python: CPython 3.10.12
exit_code: 0
stdout_bytes: 62143
stdout_lines: 1
stdout_sha256: 6330720d5177e133c22c92796e5fd1094810b5a3be9fea35bed38b385a3465aa
stderr_bytes: 0
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
environment: LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1
```

The six pinned files were fetched from the public branch and compared byte for byte before prospective evolution. The root command was executed on Linux, starting at 2026-11-22T00:42:19.109303+00:00 and finishing at 2026-11-22T00:47:11.179108+00:00. EXPECTED.txt contains its scientific stdout verbatim.

| File at the preregistration pin | Bytes | SHA-256 |
| --- | ---: | --- |
| PREREG.md | 7010 | `38cb1d76a0c141c7c1c77c85ad4b7e673082ee52ce11a743e11e5f3c1dd1e9ca` |
| calibrate.py | 4090 | `81c18aeddd49977a5715d234df25d4361601a85af2436e0f3d968c0fa1452c7d` |
| custody.py | 4254 | `b6718de47ce3cf693f0acc19b5e03ef8f1128953183a52f9e80866c365b0ae75` |
| physical.py | 9229 | `17541d2f599e39d330540ae6a9736d1ed0935209a76f58c9963be83a91e24443` |
| reader.py | 8676 | `43ca945b0882319fe04e9624e539caa822082264d7ba89c19b7df0dcf133ecbf` |
| verify.py | 12797 | `4259f3c0209d97cd4c932f1f93f2796f27eb6a82873b8793b73fd9428f80c857` |

## Opening the blind run

The reader received the permuted projections, its source, calibration code, station evolution and the public H3 kernel. Its working directory contained no permutation secret or packet identities. It ran one isolated batch invocation. Commit `dad53aa85bf7e003507525ac343ac69d273e6064` published the hashes of its entire input and answer streams before opening. The acquired data and committed answers were regenerated and checked record by record. The verifier independently rescored the canonical ordering with the same frozen reader.

| Identity | Value |
| --- | --- |
| Opening, 32 bytes in hexadecimal | `18cbd00508103fa96c2eb95a779ab1cb12a5a2950a4838efad97bc223686a348` |
| Anonymous records | `de2b6c2f4c56991435a90c448b00e08238c0ce6d019f2fed56e45910c9ddfe00` |
| Blind answers | `1571870bbdf4fdf6ced741f9491832a9113b13d2b3019d654c9159f19413ba7a` |
| Answers in canonical roster order | `974e575231cdda6ad36d2d6e0e592a23be8ce7b8e2b38dc350b38f6e8ff9d60d` |
| Verified answer records | 6,420 |

From a clean checkout, use an empty temporary working directory for replay files. The two commands that produce new files use exclusive creation.

```sh
p=probes/P-H3-ROW0-PULSE-RETURN-1
d=$(mktemp -d)
python3 -c "from pathlib import Path; import sys; Path(sys.argv[1]).write_bytes(bytes.fromhex(sys.argv[2]))" "$d/seed.bin" 18cbd00508103fa96c2eb95a779ab1cb12a5a2950a4838efad97bc223686a348
python3 "$p/custody.py" acquire "$d/seed.bin" "$d/anon.json"
python3 -I -B "$p/reader.py" batch reproduce/h3-referenced-record/verify.py "$d/anon.json" "$d/calls.json"
python3 "$p/custody.py" audit "$d/seed.bin" "$d/anon.json" "$d/calls.json"
```
