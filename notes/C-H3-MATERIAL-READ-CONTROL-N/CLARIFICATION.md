# Pre-execution reference-cut clarification

NON-CANONICAL / NO AUTHORITY. L1. Claim #2139.

The blind checker requested these exact conventions before any new
trajectory was executed. This supplement leaves PREREG.md at
0fabe9ffdb8b387614344aa484589e3898bdb784 byte-for-byte unchanged. It fixes
ambiguous reference-cut wording before source execution or output inspection.

1. The predecessor endpoint digest encodes ten fields in order
   (oldbit=0,newroot=0..4), then (oldbit=1,newroot=0..4). Each field is its
   192 ordered ring elements in x,y,rail order; each element is the four
   coefficients in basis(1,j,j^2,j^3). Use compact JSON as declared, with
   no trailing newline. Inert reserve values are not part of this field
   digest and are not identified by it.
2. In A1 and A2, every literal S0/old-archive loss and every strict old-
   archive gate refers to the corresponding actual background at full121.
   The reference does not move with later native transport. Two-class
   retention is scored independently and can survive literal movement.
3. In B2 the old-archive reference is the corresponding UNMODIFIED
   predecessor field at the same full target cut tau. Thus this check
   asks whether the explicit probe preserved the old archive's actual
   native evolution during the read tick. It does not require the old
   material coordinates to be stationary between start s and tau.
   The identical reference applies to both material-donor controls on
   that background, because the donor swap touches column4 material only.
4. In B3 literal radiation-pair and old-archive losses refer to each
   loaded run's own full tau output. Two-class losses remain separate.

No horizon, candidate label, deterministic selection order, native law,
input set or account condition changes. No observed data motivated these
choices: all new scientific execution remains pending the source freezes.
