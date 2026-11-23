# Blind answer commitment

**Status O.** The public preregistration pin is `1cb47b7ec72bc0c4556bde8e37f64347584739dd`. The blind reader was given the shuffled port records and the code for its fixed public calibration and decision. It returned 6,420 ordered answer records. These identities commit the full input and answer streams before the permutation or truth is disclosed.

| Stream | Bytes | SHA-256 |
| --- | ---: | --- |
| Anonymous inputs | 14294636 | `de2b6c2f4c56991435a90c448b00e08238c0ce6d019f2fed56e45910c9ddfe00` |
| Blind answers | 905506 | `1571870bbdf4fdf6ced741f9491832a9113b13d2b3019d654c9159f19413ba7a` |

To reproduce the sealed order after opening, use the seed in RUN.md and the acquisition and batch commands there. The registered batch encoding uses compact sorted-key ASCII JSON and one final LF.
