# One clock and one passive H3 receiver

Status: PASS. Prospective finite computational result at L1, submitted for review.

On the specified \(8\times4\) H3 torus, only raw ready rank **44** moved the passive receiver in the 85 controlled trials. It moved during vertical matter transport on tick two. Its values persisted through the collision that completed the tick. All trials began one tick before their ready cut, with identical reader and receiver stock. Here “44” uses the raw ready enumeration defined in the preregistration.

| Observation | Result |
| --- | --- |
| Passive write on the first tick | None of the 85 trials |
| Passive write on the second tick | Rank 44 alone |
| Raw rank 4 | Parity admitted, both norm equalities false, head and receiver quiet |
| Bare-clock period | 622 native ticks |
| Passive writes without intervening reloads | Ticks 75, 697, 1319, 1941 and 2563 |
| First complete return of the funded circuit with its matching bit | Tick 3110 |
| Preregistered falsifiers in the bare, controlled and recurrent gates | None |

## The write and the clock's response

Write \(F=1025,\ \rho=j^2,\ J=1+\rho\) and let \(A\) be the single fixed target field value. Rank 4 presents the distinct field value \((0,0,3,-1)\) in the \(1,j,j^2,j^3\) basis. Its difference from \(A=(-2,0,-1,-5)\) has even coefficients. Both input half-differences exist. Testing the two H3 norm equalities gives false in both cases. Thus the control tests the second decision of the native law.

For rank 44, branch \(B_2\) on tick one changes the head matter half-difference from \(JF\) to \(F\). At the head the CLK gains \(F\rho\) and CORR loses \(F\rho\). The passive rails stay fixed. On tick two the native matching couples the two matter pairs at equal half-difference \(F\). It moves their midpoints from \(0,4\) to \(2-2\rho,2+2\rho\) respectively. The receiver therefore holds
\[
(2+2\rho+F,\;2+2\rho-F).
\]
The head takes \(B_1\) in the collision of that same tick. Its half-difference and CLK recover their prepared values. All original clock coordinates recover the bare clock's state at the corresponding cut after separating the six explicitly funded stock rails. Those six rails are also checked individually against their expected values, including both changed matter midpoints. The passive receiver keeps its new value. The original clock projection and the complete funded circuit therefore have distinct return conditions.

## Accounting and renewal

The two linear rail sums, full Hermitian norm sum and scalar trace, in the preregistered ordering and basis, were constant at every checked transport and collision:
\[
Q_m=(8,0,0,0),\quad Q_r=(2066,6,7,5),\quad
Q_h=(10498377,0,2089051,2089051),\quad Q=18907703 .
\]
For each of the 170 controlled ticks and 3110 uninterrupted ticks, the collision inverse returned the complete post-transport field with the opposite branch tags. Inverse transport at the recovered bit returned the full incoming field. These comparisons include both stock sites and all 128 ring coordinates.

The uninterrupted run starts at raw rank zero. Each of the five writes comes one tick after the corresponding raw-44 ready cut. After the \(n\)-th write the passive midpoint is \(2+2\rho^n\), and the head midpoint is \(2-2\rho^n\). The passive scalar matter changes over those writes are \(-40,0,0,0,+40\). On each of the three zero-scalar writes both passive matter rails change. A detector watching only scalar energy would miss them. The fifth write restores the initial midpoints. The entire circuit, including the remaining clock coordinates and matching bit, first returns to its initial state at tick 3110.

## Evidence and scope

The first Linux run returned the three scientific gates as PASS with no falsifiers. A separate Linux aarch64 replay of the same published pin using Python 3.12.3 reproduced the 615 stdout bytes from the x86-64 run with exit zero and empty stderr. A separately coded same-session checker also reproduced all 85 controlled trials and the first two uninterrupted laps. The full five-lap result is covered by the pinned verifier. [Preregistration](PREREG.md) · [First run](RUN.md) · [Exact output](EXPECTED.txt) · [Verifier](verify.py)

This circuit implements one calibrated yes/no predicate on the declared prepared family. It uses one bare clock, one local head, one passive pair and the unchanged forward H3 update. The fixed target \(A\) and stock are preparation data. Distinguishing every rank in a single material register and deriving a physical observation law remain open.
