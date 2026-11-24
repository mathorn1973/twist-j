# A finite autonomous clock for the complete forward program

**NON-CANONICAL, L1, candidate-T analytical construction.**
Independent mathematical acceptance is pending. This is a declared extension
of the capture law, not a derivation of new actuators from the original law.

## 1. Scope and complete carrier

The input circuit is the complete retained-history construction in
[PR #1746, pinned proof][forward-proof]. The source, native capture steps,
Fourier registers, preparation mark and acceptance predicate are retained.
No accepted branch is identified with applying the acceptance effect to the
input vector. The present construction schedules the entire unitary circuit,
including its rejected branches.

Let Dcal denote the data Hilbert space containing the object, token-or-pulse
carrier, its labels and banks, the receiver, all five-state registers, every
binary workspace register and the final flag. A reference Rcal is arbitrary
and untouched. First use the predecessor's infinite spatial data carrier;
Section 5 gives a finite periodic realization on the stated finite-horizon
input domain. The clock is an additional M-dimensional factor with basis
|c>, 0 <= c < M. It is initialized once in |0>.

Every specified data operation below is a total unitary on Dcal, including
inputs with dirty workspace or the wrong preparation mark. Correct program
semantics require the stated initial workspace; invertibility does not.
The ordered word is hardwired into the law. Its description and individually
addressed couplings are supplied resources, not a stored-program compiler or
an independently derived uniform local interaction.

## 2. An explicit word and its count

Set

    m_R = 32768, m_W = 8192, n = 8,
    D = n(m_R + m_W) = 327680.

Use the following chronological word G_0,...,G_(L-1).

1. Apply the predecessor's basis-source loader: one F5, two disjoint
   transpositions applied as two gates, and two phase gates. Its other
   preparation branches remain present. This uses one five-state register
   and five named gates.
2. Apply T complete copies of the original U_rec, without modifying their
   native internal order.
3. Apply eight trials of m_R blocks for V_R = T_R and eight trials of m_W
   blocks for V_W = z_g^(-1) W. Each block is the ordered word F5, controlled
   V, F5*. Each of the D blocks addresses a distinct five-state register.
   This gives 3D named gates, comprising D controlled object operations and
   2D auxiliary Fourier changes of basis. No inverse object operation occurs.
4. Compute the acceptance predicate reversibly into fresh binary targets,
   retaining every intermediate value as specified below.

The controlled z_g^(-1) W is one named operation in this accounting, matching
the predecessor's abstraction. Its phase, control routing and object walk
have not been compiled into elementary local interactions here.

For Step 4, every operation is of the form

    (controls, t) -> (controls, t XOR f(controls)).

This is an involution on the complete computational basis, even when t is
initially one. It extends linearly to a unitary and leaves all controls.
For the intended evaluation, initialize every target to zero. Use:

| Operation | Number of gates and fresh binary targets |
| --- | ---: |
| Test whether each Fourier register equals zero | D |
| Binary AND trees inside the sixteen trial words | D - 16 |
| Two binary OR trees, each over eight trial indicators | 14 |
| Test the source-loader mark h = 0 | 1 |
| Test the specified carrier position, bank and arrangement | 1 |
| Binary AND tree combining the four final inputs | 3 |
| Total B | 2D + 3 |

The final four inputs are the two filter-success bits, the source-mark bit
and the carrier-front bit. The last AND target is the acceptance flag. An
AND tree with k leaves has k-1 internal nodes, so the trial-tree count is
8(m_R-1) + 8(m_W-1) = D-16. The two OR trees contribute 2(8-1).
No workspace is uncomputed. In particular, the detector stores all D
five-state outcomes and both successful and unsuccessful trial histories.
The carrier-front test is a supplied finite predicate-controlled gate; its
spatial acquisition and routing are not elementary operations proved here.

Consequently

    B = 655363,
    L = 5 + T + 3D + B = T + 5D + 8 = T + 1638408.

The named object-operation counts remain 262144 controlled T_R operations
and 65536 controlled z_g^(-1) W operations. There are D+1 five-state registers
including the loader, and B binary targets including the final flag.
These are sufficient counts for this explicit circuit, not minimum counts.

## 3. One time-independent discrete law

Choose a desired post-filter native horizon H >= 0. Extend the word by

    G_c = U_rec,  L <= c < L+H,
    G_(L+H) = I,
    M = L+H+1.

The new single-tick law is

    U_clock = sum_(c=0)^(M-1) |c+1 mod M><c| tensor G_c.       (1)

It is independent of an external tick index: the clock value is part of the
state and determines the operation. Its inverse is

    U_clock* = sum_(c=0)^(M-1) |c><c+1 mod M| tensor G_c*.      (2)

Multiplying (1) and (2), orthogonality of distinct clock labels eliminates
cross terms, leaving identity because each G_c is unitary. The opposite
product is identity for the same reason. This proves the law on arbitrary
clock superpositions and arbitrary dirty data, not only on the ready path.
The adjoints in (2) describe the inverse law; they are not executed in the
forward program (1).

For every data/reference vector Psi and every 0 <= k <= L+H, induction gives

    (U_clock^k tensor I_Rcal)(|0> tensor Psi)
      = |k> tensor ((G_(k-1)...G_0) tensor I_Rcal) Psi.         (3)

At k=0 the product is identity. One further application of (1) gives the
induction step. Thus complete-state comparison with the ideal word has zero
error at every indicated boundary, uniformly in the reference and in the
data input. When initialized at zero the clock remains unentangled with the
data on this trajectory; the data registers can remain mutually entangled.
There is no summation over hypothetical independent trials in this argument.

For the short example T=2 and H=1,

    L = 1638410,     M = 1638412.

The acceptance flag is ready at clock value L. The next H target ticks apply U_rec in U_clock; ENERGY.md treats the
funded extension separately. The following identity tick wraps the clock. The complete
data state need not return when the clock returns to zero. Reexecuting the
word on its dirty registers has no fresh-experiment interpretation.

## 4. Holding, release and what autonomy means here

The object-only filter gates are identity on the complete carrier and receiver
factors. The carrier-front test is instead a diagonal control on carrier
position, bank and arrangement: it preserves their spectral projectors and
does not transport the carrier, but it can entangle the carrier with its
predicate bit and the final flag. All these gates are identity on the receiver
as a full subsystem, not merely on its basis populations. Thus the carrier is
spatially held throughout filtering and predicate evaluation, with its
intentional readout correlations retained. These statements include rejected
histories. At clock L the native evolution resumes for H steps. No external
instruction is needed to select the release tick.

For s=99, T=H+1 and the predecessor's accepted source-label-one branch, the
carrier is at x=100+H when the filter starts and remains there until release.
Its maximum native speed is one site per macrostep, and the unique memory
coupling is the bond (99,100). Therefore the receiver retains d1 at all
native boundaries 0,...,H following release, exactly as in the predecessor's
finite buffer argument. This conclusion concerns the record, not permanent
binding. Its source/filter weight remains conditional on the predecessor's
candidate proof and is not promoted here.

Equation (1) supplies discrete scheduling autonomy within a new law. It
explicitly turns off native carrier/receiver evolution while other registers
operate. That selective identity is an added coupling choice. The original
U_rec alone has not been shown to generate it, nor has the original
checkpoint evolution been shown to generate this enlarged carrier. The
[native-locality audit][native-audit] separates those issues.

A named-operation tick in (1) is not a measured time unit. In particular, one
native macrostep, one global controlled object step, one F5 and one spatial
predicate are not proved to require the same number of local operations or
the same physical duration. Assigning a common duration tau makes the formal
completion time L tau, but choosing and physically realizing tau is a further
premise. No duration in seconds or local gate speed follows from (1).

## 5. Finite spatial realization and its exact domain

Let N_W=65536 and N_R=262144. The predecessor's finite-range support argument,
extended by the H release steps, gives the following bounds for every branch
of the ideal word, including rejected histories:

    s-T-N_W-H <= R <= s+T+N_W+N_R+H,
    |r| <= T+N_W+H,
    s-T-H <= x_carrier <= s+T+H.                              (4)

The five loader operations, Fourier changes and Boolean gates do not move
these coordinates. Each W operation changes R and r by at most one, each
T_R changes R by one, and each native release step increases the conservative
coordinate bounds by at most one. These statements hold for amplitudes in
every coherent history; no failed branch is removed to obtain (4).

A finite realization can use cyclic integer coordinates with representatives
-R_box,...,R_box. Make the explicit choice

    R_box = |s| + T + N_W + N_R + H + 3,
    N = 2R_box+1.

Wrap each translation of the already specified factorized walk modulo N;
keep its finite coin/contact factors and receiver calibration as total
unitaries on these coordinates. Contact equalities are evaluated in the
finite coordinates, and the receiver calibration is specified on every
representative. Their products give finite unitary walk steps; the auxiliary
and controlled gates have the same total finite extensions. The margins
place every reached coordinate, the receiver and each single-step
intermediate translation strictly away from the artificial wrap seam.
Induction over the specified factors therefore identifies the ideal finite
and infinite evolutions on the prepared source and all admitted logical/
reference inputs throughout the stated horizon. This is a comparison of
reached states, not a claim that the infinite and finite spectra coincide.
No sharp position projection or spectral truncation is executed.

The finite box is a model completion outside the reached domain. It does not
prove that the required couplings have bounded physical range, that their
control distribution is local, or that this large box has a physical
preparation protocol.

An arbitrary spectral energy dressing can mix positions nonlocally, so its
support cone cannot be inherited without proof. The particular diagonal
ledger in [ENERGY.md](ENERGY.md) preserves configuration-transition zeros:
its energy projectors are diagonal in this same configuration basis, and
the lifted matrix attaches a battery shift to an existing data transition.
That separate argument preserves the spatial support bound on the prepared
full-sector domain; it is not a consequence of energy conservation alone.
The same file proves when an actual tensor spectator remains a spectator.
The front test intentionally creates carrier/readout correlations and must
not be called identity on the complete carrier. Where output coherences or
conditional binding comparisons differ from the ideal word, the uniform
joint error eta and the corresponding conditioning bounds must still be used.

## 6. Wrapping is not an absorbing halt

This construction intentionally has a cyclic clock and a finite guaranteed
read/release window. Its full law remains defined after that window. It has
no transition that merges the last clock state with a fixed absorbing clock
state, and it does not reset or erase its retained histories.

For a finite-dimensional unitary, any forward-invariant halt subspace is
also mapped onto itself. Its orthogonal complement is then invariant, so a
state outside cannot enter that subspace. The same proof works in an
infinite-dimensional model if the stipulated halt-sector restriction is
itself unitary onto that sector. Merely having finitely many clock labels,
while allowing arbitrary infinite data memory, is not enough to invoke the
finite-dimensional statement. No universal no-go for all clocks or all
finite-time output records is claimed.

The existing [finite-controller recurrence note][recurrence] likewise
separates all-time recurrent claims from allowed finite cyclic scheduling.
The present clock does not supply a reusable detector, a renewed source,
an archive with unlimited capacity or an occurrence law.

## 7. A Hamiltonian boundary

Equation (1) is a discrete unitary law. A proposed nearest-neighbour
continuous-time history Hamiltonian with clock blocks

    K_(c+1,c) = gamma_c G_c

must, by Hermiticity, also have

    K_(c,c+1) = conjugate(gamma_c) G_c*.

A nonzero purely forward hopping matrix is therefore not Hermitian. The
usual clock-hopping route includes reverse clock edges with adjoint data
blocks. This observation obstructs that particular attempt to retain
exclusively forward elementary clock hops; it does not rule out autonomous
Hamiltonians realizing the required endpoint or all other chiral schemes.

A spectral logarithm of U_clock is also not an energy/locality certificate.
It need not preserve the named-operation intermediate states, have local
couplings, or coincide with an independently specified additive energy.
The physically calibrated generator, its energy source and local
implementation remain separate requirements.

## 8. Prior art and status

The canonical [FIELD-FETCHED-PROGRAM-CONTROL theorem][fetched-program] already
uses a station-plus-shift unitary with the same general structure as (1).
It proves exact complete-operator execution for its specified finite
catalogue and graph, including correlated dirty buses. Its supplied
catalogue, graph, preparation, abstract ticks and nonphysical-drive-work
qualifications are explicit. The general autonomous compiler construction
is therefore not claimed as new here.

The present contribution is the exact forward-filter schedule, its retained
Boolean construction, finite read/release interval, support accounting and
explicit interface to the energy question. These authored statements remain
conditional L1 mathematics, not native admission or independent physical
validation. No scientific executable was run for this derivation.

[forward-proof]: https://github.com/mathorn1973/twist-j/blob/01acc42b78f75095587765e9a5b91ee70dc28f37/notes/C-FORWARD-ONLY-CAPTURE-FILTER-N/PROOF.md
[native-audit]: https://github.com/mathorn1973/twist-j/blob/6f085f00e5788f1ebecc83a6b8a4fde5a65265a7/notes/C-FINITE-CONTROLLER-A-NATIVE-LOCALITY-N/LOCALITY_REPORT.md
[fetched-program]: https://github.com/mathorn1973/twist-j/blob/892a0b11089d34e241e1eb76d2c03247022d18e6/canon/CANON.md#L8625
[recurrence]: https://github.com/mathorn1973/twist-j/blob/892a0b11089d34e241e1eb76d2c03247022d18e6/notes/C-U-FINITE-REVERSIBLE-CONTROLLER-RECURRENCE-N/PROOF.md
