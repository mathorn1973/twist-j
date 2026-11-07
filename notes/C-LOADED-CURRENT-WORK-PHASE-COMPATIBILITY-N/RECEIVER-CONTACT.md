# Receiver interface, stock provenance, and semantic controls

Status: **NON-CANONICAL / L1**, conditional candidate-T in the declared
ordinary-contact model. The complete clock and receiver proof is in
RECEIVER-DYNAMICS.md, equations (R1)-(R10). RECEIVER-PREREG.md freezes the
separate finite audit; no physical phase or coupling is selected here.

## 1. One supplied receiver, unchanged across the candidates

The actual high pointer input is (j^b,-j^b). Add one fixed stock

\[
 a=1+2j+j^2,\qquad R=1+2a=3+4j+2j^2,\qquad Q(R)=32.
\]

Apply five repetitions of the ordered contacts C(p,R), C(p,q), and read
the final Q of the stock slot. This is one fixed ten-contact word.
Neither its word, stock, output observable, nor normalization depends
on b, the character index, or the candidate clock member.

The stock was chosen constructively so that its five possible terminal
energies are distinct. It is an explicitly supplied asymmetric receiver
frame. No dynamical selection, uniqueness, minimality, or independent
physical necessity of this stock is asserted. The original unscaled
pointer is used directly; no free preparation of a doubled amplitude,
copy of an unknown phase, or conversion to a new carrier is assumed.

For reproducible exact fixtures, the proof gives first hit k=2b mod5,
with k in {0,...,4}. After n admitted stock contacts,

\[
 p_n=1+a-\rho^n a,\qquad R_n=1+a+\rho^n a,\qquad n=5-k
\]

at the terminal stock cut. The explicit four-coefficient stock states are:

| n | R_n | Q(R_n) |
|---|---|---:|
| 1 | (1,1,1,1) | 2 |
| 2 | (3,2,0,-1) | 27 |
| 3 | (2,3,3,1) | 17 |
| 4 | (1,0,-1,-1) | 7 |
| 5 | (3,4,2,0) | 32 |

Thus b=0,1,2,3,4 gives the injective response (32,17,2,7,27).
The proof of every admitted/refused branch is in RECEIVER-DYNAMICS.md.
The literal inverse reverses the word and replaces every C by C^4:
forty ordinary contacts, valid on arbitrary occupied input triples.

## 2. The stock is active and the record has backreaction

The initial high-pair account is 4. The stock begins with 32 and ends
at one of the values above. Its signed change is offset exactly by

\[
 Q(p_{\rm out})+Q(q_{\rm out})=36-Q(R_{\rm out}).
\]

The stock supplies between 0 and 30 account units to the pointer.
Its terminal Q is a receiver-work response, not a passive measurement
of an independently emitted source energy. The pointer is disturbed.

High pair plus stock costs 36. The existing two-pair label pointer
plus this stock costs 40; its low pair is untouched. A native five-pair
clock in the common delta preparation plus stock costs 36.
All have the same fixed total slot sum R across their candidates.
Appending the untouched slot -R makes the complete preparation neutral
and raises those accounts to 68, 72, and 68, respectively.

The output stock retains the contact record while the output is retained.
Complete reversal removes it. No funded archive, permanent record after
reversal, nondisturbing measurement, Born rule, or empirical calorimeter
implementation is integrated into this construction.

## 3. Changing a character name and changing a physical state differ

For the existing two-pair encoding r=r_0+5r_1 mod25, the low and high
pair amplitudes are j^(r_0) and j^(r_1). Hold the actual state r=13 fixed.
Assigning the five names chi_t(r)=exp(2pi i (1+5t)r/25) does not change
any input slot. The unchanged receiver therefore produces the same
complete state, with terminal Q=2, for all five names.

An actual reencoding r_t=(1+5t)13 mod25 changes the high pair:

\[
 r_t=(13,3,18,8,23),\quad r_{1,t}=(2,0,3,1,4).
\]

Then the same receiver gives

\[
 Q(R_{\rm out})=(2,32,7,17,27),\qquad
 \Delta Q_R=(-30,0,-25,-15,-5).
\]

This distinguishes five physical preparations. It supplies no physical
operation implementing the reencoding itself. For general r, the five
reencodings have distinct high digits exactly when r mod5 is nonzero;
when r mod5=0 all five physical labels coincide.

## 4. Interface to an actual native clock experiment

The native words for V_m in RECEIVER-DYNAMICS.md act on one common delta
preparation of account 4. One actual tick produces j^m at known pair
site 1. The same stock receiver at that one fixed site reads
(32,17,2,7,27), with complete account 36.

Thirteen actual native ticks produce j^(13m+2) at known pair site 3.
At that same fixed site for every m, the same receiver reads
(2,32,7,17,27). The finite audit includes both literal experiments and
their complete reversals, including the stock. Optional neutral
companions are separately checked for neutrality, account, and preservation.

Thirteen unit clock steps are an explicitly supplied test horizon.
They do not compile the earlier field transition with Gamma mod25=13
into an ordinary-contact clock controller. Likewise the equal-attempt
padding of the native words is a supplied calendar, not a derivation
of physical time or of an accumulated phase action.

The receiver discriminates actual coupled dynamics relative to its fixed
stock frame. It does not distinguish five semantic names for one unchanged
trajectory or select the physical dynamics without an independently
determined coupling/reference frame or an observed response.