# P-J-PLENUM-CENTERING-INDEX-1 result

Status: **candidate-T / L1 / LOCAL MATHEMATICAL CLAIM CONFIRMED /
TWO-ARCHITECTURE COMPUTATION GATE PENDING / PUBLIC CLAIM UNREGISTERED /
CANON UNCHANGED**.

## Recorded local decision

```text
J-CENTERING-IMAGE-INDEX:       LOCAL CONFIRMED
gates:                         6/6 PASS
terminal:                      CONFIRMED
exit/stderr:                   0 / empty
stdout:                        328 bytes / 10 lines
stdout SHA-256:                a48a88c3545f9d355b89b125e873882968ddad4771502c9462e1a9dd489d983c
scientific falsifier:          NOT FIRED
integrity disposition:         captured hashes and counts PASS
architecture gate:             PENDING
post-result security review:   PASS, A. M. Thorn
```

The verifier was executed once locally after public pin
`89047f3921959457f635687bd120e323ea9df05a` and its public byte readback on
[issue #814](https://github.com/mathorn1973/twist-j/issues/814#issuecomment-5546492828).
The recorded verifier hashes before and after execution are identical to
the public readback hash. The exact captured stdout is preserved in
`EXPECTED.txt`; the complete local metadata and custody checks are in
`RUN.md`.

## Exact mathematical conclusion

For `E=Z^5`, `u=(1,1,1,1,1)^T`, `V_Z=ker(sum)` and `D=5I-u u^T`, the
confirmed claim is

```text
ker_Z D=Z u,
im_Z D={d in V_Z : d_i=d_j mod 5 for every i,j},
[V_Z:im_Z D]=125,
V_Z/im_Z D is isomorphic to (Z/5Z)^3.
```

The universal image statement rests on the explicit proof in `PREREG.md`,
not a finite sample of integer vectors. If the common residue of `d` is
`r`, then `c=(d-r u)/5` is integral, has coordinate sum `-r`, and satisfies
`D(c)=d`.

With `f_i=e_i-e_4` for `i=0,1,2,3`, the image-generator matrix has
coordinates

```text
u_4=(1,1,1,1)^T,  M_image=5I_4-u_4 u_4^T,
F M_image=[D(e_0) D(e_1) D(e_2) D(e_3)],
det M_image=125.
```

The fifth image column is minus the sum of the first four. Their
independence follows from the determinant. The separately supplied
integral matrices `U_smith,V_smith` have determinants one and obey

```text
U_smith M_image V_smith=diag(1,5,5,5).
```

This unimodular identity certifies the quotient group, rather than inferring
its structure from its cardinality alone.

The operator restriction is a different map, with

```text
D F=F R_restriction,
R_restriction=5I_4,
det R_restriction=625,
D(V_Z)=5V_Z.
```

The exact negative control rejects `det R_restriction=125`. The remaining
centering identities are `D^2=5D`, `Dg=gD` and `DJ=JD` for the declared
five-cycle and register operator `J=I+g^2`.

## Relation to the predecessor

The predecessor `P-J-PLENUM-POLAR-GAUSS-1` remains unchanged. Its combined
claim A, `J-PLENUM-POLAR-GAUSS`, remains `SCIENTIFIC-FIRED` under its
original decision rule. This separately named successor distinguishes the
image-generator matrix from the operator restriction and adds an explicit
Smith certificate. It does not repair, rerun, resume, reclassify or promote
the predecessor's combined claim or its other components.

Both correct determinants and their distinction were exposed before this
execution. This is proof-first verification of a disclosed result, not a
blind prediction.

## Remaining validation and scope

Required public x86_64 and aarch64 jobs must reproduce the same verifier and
the same `EXPECTED.txt` bytes with exit zero and empty stderr. The aggregate
`check` remain pending. Post-result manual security review by A. M. Thorn
passed: the five named text files contain only exact mathematics and neutral
run metadata, with no secrets, private infrastructure, executable payloads
beyond the accepted verifier, external data or unreviewed dependencies. No public
architecture receipt is asserted by this local result.

The claim is limited to exact p=5 integer lattices and their finite matrix
certificates at L1. No polar decomposition, Gauss sum, finite polar group,
coordinate-square probability, Born selection, unit population, physical
preparation, apparatus, event, record, occurrence, sampling, self-location,
decoder completion, photon, gravity, time, SI scale or L2--L6 lift is
established.

Public Canon, Registry, Frontier, dictionaries, dependencies, gates and
`STATUS.md` are unchanged. Any public claim registration requires a later
separate reviewed Canon fold.
