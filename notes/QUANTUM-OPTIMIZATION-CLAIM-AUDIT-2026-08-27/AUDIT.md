# AUDIT: quantum optimization claims, challenge text of 2026-08-27

```text
status   NON-CANONICAL. Notes lane. Moves nothing. No Canon row, no probe,
         no registry entry, no falsifier. Rules on one external argument.
date     2026-08-27
scope    The "oq challenge" text asserting that hybrid quantum optimization
         delivers operational results classical hardware cannot match.
method   Arithmetic gates in check_quantum_claims.py (18/18 pass), plus
         source checks on the four attributed industrial facts.
```

## 0. Summary

The challenge text mixes **two real deployments** with **four false numbers**
and **one misattributed aggregate**. The deployments happened. The physics
story told about them is wrong, and — the load-bearing point — none of the
cited results is measured against the control that would make it a claim
about quantum computing rather than a claim about replacing a spreadsheet.

The text is not snake oil. It is something more ordinary and harder to see:
a real engineering win with a missing baseline arm.

## 1. The arithmetic, decided

Run `check_quantum_claims.py`. Four assertions, all false as stated.

### 1.1 "20 stops → more permutations than atoms in the universe"

```text
20!                 = 2 432 902 008 176 640 000   ~ 2.4e18
atoms (observable)  ~ 1e80
```

20! is **61 orders of magnitude smaller** than the atom count, not larger.
`n!` first passes `1e80` at **n = 59**. And the relevant count for a closed
tour is smaller still: `19!/2 = 6.08e16`.

This is not a quibble about a rhetorical flourish. The sentence is the
text's entire argument for why the problem is hard, and at the size the text
itself chooses, the problem is not hard.

### 1.2 "Classical computers must check these pathways one by one"

They must not, and have not had to since **1962**. Held–Karp dynamic
programming proves the optimum by recursion over subsets:

```text
tours in the space          60 822 550 204 416 000
Held-Karp inner steps               49 807 360
ratio                        1 221 155 873 : 1
```

The checker solves the pinned 20-node instance to a **proven optimum**
(cost 33 636) in **19.7 s of pure interpreted Python on one core**, and
cross-validates the DP against exhaustive search at n = 10. In C, or with
Concorde's branch-and-cut, this instance is milliseconds; Concorde has
closed instances of tens of thousands of nodes to proven optimality.

### 1.3 "Cancels bad schedules, amplifies the perfect schedule, instantly"

Two errors, one of physics and one of logic.

**Physics.** This describes Grover's algorithm, which D-Wave's hardware does
not run — D-Wave builds a quantum **annealer**, not a gate-model machine.
And Grover is not instant: it needs `Θ(√N)` queries. Here that is
`√(19!/2) ≈ 2.47e8` oracle calls, each a full *reversible* tour evaluation
on error-corrected logical qubits. Grover's speedup is **quadratic**, so it
cannot turn an exponential space into a polynomial one.

The comparison that matters:

```text
n = 20   Grover 2.47e8 queries    Held-Karp 4.19e8 steps
n = 21   Grover 1.10e9            Held-Karp 9.25e8      <- classical wins
n = 30   Grover 2.10e15           Held-Karp 9.66e11     <- by 2175x
```

From **n = 21 upward a perfect, noiseless, fault-tolerant Grover search
needs more oracle queries than Held–Karp needs elementary steps**, and the
classical margin widens without bound. Grover treats a structured problem as
unstructured, and throws away the structure that makes the classical
algorithm fast.

**Logic.** Annealers and hybrid samplers return *samples*. They carry **no
optimality certificate**. Held–Karp and branch-and-cut return a proof. The
text's "revealing the ideal factory floor plan" claims exactly the property
the quantum method lacks and the classical method has.

### 1.4 The Atari

The text's conclusion is right and its stated reason is wrong.

```text
brute force on a 1.19 MHz 6507   ~1.6 million years
age of the universe             ~13.8 billion years
```

That is **8 512× shorter** than the age of the universe, not longer. What
actually stops an Atari 2600 is the Held–Karp table at ~19.9 MB against
**128 bytes** of RAM — a memory wall, not a time wall.

## 2. The industrial facts, checked

Two are real and both are misdescribed. One is misattributed.

### 2.1 Ford → **Ford Otosan** [REAL, RESTATED]

Not Ford Motor Company. **Ford Otosan**, the Ford/Koç joint venture in
Turkey, deployed a production hybrid application built on D-Wave's annealing
technology for Ford Transit body-shop sequencing (announced 2025-03-31).

```text
claimed in text   "hours to recalculate"  ->  "near real-time"
actually reported  30 minutes             ->  under 5 minutes
                   for 1 000 vehicles per run; an 83% reduction
```

Real, deployed, and useful. But "hours → near real-time" overstates a
reported 30 → 5 minutes, and the 30-minute baseline is **Ford Otosan's prior
method**, not a tuned classical solver.

### 2.2 "Patterson Food Group" → **Pattison Food Group** [REAL, RESTATED]

The name is wrong in the text. Pattison Food Group (western Canadian
grocery) automated e-commerce driver scheduling with a D-Wave hybrid solver:
one weekly task went from **25 hours to about 2 minutes**, roughly an **80%
reduction in weekly manual scheduling effort**.

Read that baseline carefully. The 25 hours was **human, manual** scheduling
effort. The comparison is quantum-hybrid **against people with a
spreadsheet** — not against OR-Tools, CP-SAT, Gurobi, or CPLEX. Any
competent classical scheduler would also have collapsed 25 hours of manual
work. The result is real and says nothing about quantum advantage.

### 2.3 "$300 million ... HSBC, Allstate, and Ford" [MISATTRIBUTED]

This is the clearest error. The **$300 million is a Boston Consulting Group
figure for total enterprise quantum spending across the entire industry in
2025** — the first year enterprise spend outranked labs and governments
combined. It is an industry aggregate.

The text attributes it to three named companies as if they spent it between
them. It also gets the roster wrong: the reporting names **HSBC, Allstate,
and EY**. Ford does not appear in it.

An industry-wide total presented as three firms' budget is a category error,
and it is the number doing the most persuasive work in the passage.

### 2.4 What "hybrid quantum" actually runs [MATERIAL OMISSION]

D-Wave's hybrid solvers are not a quantum computer with a classical wrapper.
The Metasolver runs **classical heuristics — simulated annealing, tabu
search, and proprietary methods — on CPUs and GPUs** as the primary engine,
while the QPU searches small subproblems and feeds promising starting points
back to those classical threads.

The peer-reviewed critique (arXiv:2409.05542) states the problem plainly:
the hybrid solver is a **black box**, D-Wave does not publish the internal
split, and this "hinders attributing the better performance solely to the
quantum routines." It further notes D-Wave's classical server is **stronger
hardware** than the local baselines it gets compared against.

So the honest statement of the Ford Otosan and Pattison results is: *a
well-engineered classical heuristic stack, with quantum-annealer assistance
of unpublished contribution, beat the customer's previous manual process.*

## 3. The methodological finding

Strip the physics and one pattern remains in every cited result:

```text
measured        new integrated system  vs  the incumbent process
not measured    quantum component      vs  the same system without it
```

There is **no ablation**. Nobody reports the pipeline with the QPU calls
switched off. Until that arm exists, the speedup is attributable to
formalizing the problem, to the classical heuristics, to better hardware, or
to the QPU — and the published evidence cannot separate them.

In this repository's vocabulary: the claim has **no falsifier**, and no
control arm, so it earns no status. It would not pass `check_policy.py` as a
preregistration. That is the correct verdict, and it is a verdict about
**evidence**, not about physics or about anyone's honesty.

## 4. What survives

Stated fairly, and this part is genuinely interesting:

- Quantum annealing is a **real heuristic** that sometimes finds good
  solutions to Ising-embeddable problems.
- Hybrid pipelines are **shipping in production** at Ford Otosan and
  Pattison, and the operational wins are real wins.
- Shor's algorithm is a **genuine exponential** speedup on a structured
  problem, which is why post-quantum cryptography migration is urgent and
  real. The text does not mention it — the strongest case for quantum
  computing is missing from an argument for quantum computing.

None of that requires the claim that classical computers must check tours
one by one, or that 20 stops exceed the atoms in the universe.

## 5. Answering the text's two closing offers

**"Would you like to see the Traveling Salesperson Problem that triggers
this computer breakdown?"** — TSP does not break at 20 nodes. It is solved
here to proven optimality in 19.7 s of interpreted Python. TSP is, in fact,
the standard example of a problem where classical exact methods vastly
outperform every known quantum approach.

**"Log into a real quantum computer for free"** — genuinely worth doing, and
the offer is sound: IBM Quantum and D-Wave Leap both have free tiers. Run a
20-city TSP on one, then run `check_quantum_claims.py`, and compare both the
answers and the certificates.

## 6. Bottom line

The Atari is not the interesting comparator; **one modern core running a
1962 algorithm** is, and it wins outright at the size the challenge chose.
The industrial deployments are real, the operational gains are real, and the
physics story attached to them is not. The missing measurement is not exotic
— it is the ablation arm — and until someone publishes it, the correct
status for "quantum solved the factory schedule" is **unproven**, not false.

## Sources

- Ford Otosan / D-Wave deployment —
  https://www.dwavequantum.com/company/newsroom/press-release/in-production-ford-otosan-deploys-vehicle-manufacturing-application-built-with-d-wave-technology/
- Ford Otosan 83% figure —
  https://www.iotworldtoday.com/quantum/ford-improves-vehicle-production-time-83-with-quantum
- Pattison Food Group case story —
  https://www.dwavequantum.com/resources/application/e-comm-driver-auto-scheduling-pattison-food-group/
- BCG $300M enterprise quantum spending —
  https://oodaloop.com/briefs/technology/businesses-are-spending-big-on-quantum/
- Peer-reviewed limitations of annealing vs classical solvers —
  https://arxiv.org/abs/2409.05542
- Quantum computing overview —
  https://en.wikipedia.org/wiki/Quantum_computing
