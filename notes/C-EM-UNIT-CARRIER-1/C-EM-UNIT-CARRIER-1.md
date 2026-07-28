# C-EM-UNIT-CARRIER-1

NON-CANONICAL. Candidate. No authority. Promotes nothing.

```text
candidate_id    C-EM-UNIT-CARRIER-1
target line     mathorn1973/twist-j (public)
status now      candidate, unlabelled until the verifier runs
status ceiling  C. No T is sought and no T is available from this argument.
layer           L6 (measure)
basis           Public Canon v25, tag canon-v25, content commit b914755b,
                canon/CANON.md sha256 53fa5acc9f2d910b26293d5152d93deac6596abd012997c7ff195397d9e476bb
```

## 1. Why this candidate exists

The Canon declares one calibration anchor, m_e, and nothing else. The
electromagnetic impedance quantities of the laboratory are usually spoken of as
if they were independent measured constants. If any of them were, the single
anchor declaration would be false, and the declaration is a normative line of
the public register, not a slogan.

This candidate audits that exposure. It is a bookkeeping claim about units and
empirical content. It derives no constant and it supports no physics.

## 2. Evidential weight, stated first

Zero bits. By the surplus criterion, surplus = log2(1/eps) - log2|S|, a
statement that is an identity of definitions has no target uncertainty to
consume and buys no evidence. The value of a null of this kind is that it
removes a possible defeater of the anchor declaration. Anyone quoting this
candidate as support for the axiom is misusing it.

In particular the relation

```text
Z_0 / R_K = 2 alpha
```

is an identity of the SI definitions, not a discovery, and the candidate says
so explicitly. The only non-tautological content in its neighbourhood is the
reading of the two circle factors 2 pi and 4 pi as one closure of each channel,
and that reading is NOT part of this candidate and is not asserted here.

## 3. The claim

Let the audited set be the five constants of the h-e sub-sector:

```text
R_K   = h / e^2                    von Klitzing constant
Z_0   = 4 pi alpha (hbar / e^2)    plenum impedance
G_0   = 2 e^2 / h                  conductance quantum
Phi_0 = h / (2 e)                  magnetic flux quantum
K_J   = 2 e / h                    Josephson constant
```

CLAIM. In the post-2019 SI, where h and e are exact by definition:

```text
A  every member of the audited set is a monomial in h, e and alpha with
   rational exponents and a rational or Q(zeta_5, pi) coefficient;
B  the total empirical content of the audited set is exactly the single
   dimensionless number alpha, which the public register derives with no free
   parameter; the count of independent empirical inputs is zero for the four
   members not containing alpha and one for Z_0;
C  the exact identity Z_0 / R_K = 2 alpha follows symbolically from
   alpha = e^2 / (4 pi eps_0 hbar c) and mu_0 eps_0 c^2 = 1, with no numerical
   input and no float;
D  no member of the audited set requires m_e, and no monomial in h and e alone
   has the dimension of mass, so the sub-sector neither supplies nor consumes
   the declared anchor;
E  no electromagnetic row of the Public Canon v25 register cites a calibration
   input other than m_e.
```

Reading: the electromagnetic impedance sub-sector is anchor-free. The Canon's
single anchor declaration survives contact with it.

## 4. The falsifier

Any one of these fires the candidate:

```text
F1  a member of the audited set that, in the post-2019 SI, requires an
    empirical input beyond alpha;
F2  a monomial in h and e alone carrying the dimension of mass;
F3  symbolic failure of Z_0 / R_K = 2 alpha under the frozen definitions;
F4  an electromagnetic row of the Public Canon v25 register citing a
    calibration input that is neither m_e nor derived;
F5  any float appearing in an assertion of the verifier.
```

A fired falsifier is archived here with its witness. The threshold is not
moved afterwards.

## 5. What this candidate does not claim

```text
not claimed  that alpha is derived by this candidate; the derivation is a
             separate register row and is untouched here
not claimed  that the two circle factors 2 pi and 4 pi have a channel reading
not claimed  any statement about the ampere, the kilogram, or SI base unit
             realization
not claimed  anything at any layer other than L6
```

## 6. Lane

Freeze this candidate and its preregistration, then write the verifier, run it,
attempt to break it by an independent path, and only then package a promotion
proposal. Validation is a public probe under POLICY.md, not this directory.
