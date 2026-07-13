# TWIST-J frontier

This file is generated from `canon/REGISTRY.tsv`. Every live row has
one public scope and one concrete falsifier or decision condition.
Closed claims are excluded.

## Hypotheses [H]

- KC3-PLENUM-READOUT [H]: the ramified place acquires the archimedean readout s; the residue class readout stays open
  Decision: fires if the residue class readout of the ramified place disagrees with the archimedean value s = abs(1 - zeta_5)
- KERNEL-CONNECT-ALL-K [H]: for every k >= 2 the generator set {a, c, d, e} with the two way CSUM ring coupling connects (F_5^6)^k into one component
  Decision: closes positively by a public proof for every k >= 2; fires on any public exact computation exhibiting more than one component at any k >= 2
- NS-TILT [H]: the scalar tilt read as n_s - 1 = -5 alpha
  Decision: live: the tilt n_s - 1 = -5 alpha fails against CMB-S4
- OBSERVER-WRITE-PORT [H]: the declared decoder is read-only: no admissible observer output writes back into the autonomous state
  Decision: fires when a typed public decoder construction supplies a nontrivial write channel into U; closes positively when the completed decoder dependency graph proves that every output is terminal
- QUADRATIC-ENVELOPE-DECODER [H]: the full decoder carrier as the pair of quadratic readings of one square
  Decision: fires if a decoder observable is exhibited that is not a function of the pair (psi psi^dagger, psi psi^T), or if the pair fails to separate two states the decoder distinguishes
- TM-SYM2-MEASURE [H]: the symmetric square measure; the residual is the Born phase halving 1/6 = (1/2)(1/3)
  Decision: fires if the Thue-Morse symmetric square average departs from the proposed 5 : 2 frame ratio at any exactly computed order, or if the Born phase halving 1/6 = (1/2)(1/3) is inconsistent with the public GYRON-DENSITY result

## Open obligations [O]

- ALPHA-S-RUNNING [O]: the strong coupling running above the 3/4 seed
  Decision: closes positively by a running derived from the 3/4 seed matching the measured strong coupling at a named scale within its stated window; closes negatively if every derived scheme from the seed misses the measured value or breaks the seed ratio 15 : 4
- BELL-MAGIC-BOUNDARY [O]: state a precise CHSH functional and determine its exact maxima over the zeta_5 and zeta_8 phase sets; no Bell cap or Tsirelson value is currently asserted
  Decision: closes positively when both exact maxima are proved for the stated functional; closes negatively if the functional is ill-defined on either phase set or the two exact optimizations do not support the proposed comparison
- COLOR-MEASURE-SELECTION [O]: the non abelian measure lift onto SL_3(F_5); 24 carrier orbits, 16 observable types
  Decision: closes positively by a derivation selecting the weight vector over the 24 orbits constrained by the 16 observable types; closes negatively if the constraint set is exhausted with no surviving weight vector, or if two inequivalent vectors survive every named constraint
- CURVATURE-TRACE-VALUE [O]: commit a public discrete-curvature operator and exact witness deciding the proposed trace value -21/8; no operator, value, or golden spectrum is currently asserted
  Decision: closes positively when the public operator has the registered proposed trace and a proved spectrum; closes negatively if the committed operator gives a different trace or refutes the proposed spectrum
- DE-CONFORMAL-WEIGHT [O]: the dark energy conformal weight
  Decision: closes positively by deriving the conformal weight of the dark energy trace direction; closes negatively if the derived weight contradicts w = -14/15
- DRESS-CROSSCOUNT [O]: the integer crossing count per observable
  Decision: closes positively when the integer crossing count per observable is derived; until then the form decision is armed: an exact witness departing from 72 alpha^4 (about 0.204 ppm, labeled) fires the exponential reading
- FRW-INHOM [O]: the inhomogeneous sector, the named classical horizon
  Decision: closes positively by an inhomogeneous source construction that reproduces the public FRW-CANONICAL-FORM identities in the homogeneous limit; closes negatively if every inhomogeneous extension breaks the exact chain of twelves
- GENERATIONS-L3 [O]: the generation structure at the standard model L3 frontier
  Decision: closes positively by deriving the generation count at the L3 boundary layer; closes negatively if the derived count differs from three
- METRO-ADMISSIBILITY [O]: state a precise admissibility criterion for named protocol classes beyond normalized one dimensional rational finite state protocols
  Decision: closes positively when a public criterion classifies a named residual class and is proved invariant under its allowed reductions; closes negatively when an exact counterexample violates the proposed criterion or two reduction-equivalent protocols receive different classifications
- METRO-EDGE-SCALE [O]: the canonical selector on the commutator phi ladder and the SI clause
  Decision: closes by deriving the canonical selector on the commutator phi ladder (the kinetic coefficient and dressing insertion routes) and the SI clause over the single m_e bridge; closes negatively if two inequivalent selectors survive every named gate, so no canonical selector exists
- NEUTRON-DELTA-EM [O]: the interior compression channel of the neutron electromagnetic delta
  Decision: closes positively by deriving the interior compression channel value; closes negatively if the derived electromagnetic delta moves the neutron outside its measured tier window
- PHOTON-WINDOW-PROOF [O]: completion of the photon window requires both (i) every closed charge 5 worldline of length L to satisfy F_occ >= kappa L for an admissible kappa with 2^(4 kappa) > 2401, and (ii) an electric face roughening certificate sufficient for the declared Froehlich-Spencer class import; the exact electric face facts already registered are not re-registered here
  Decision: closes positively only when both obligations have public exact certificates; an exact counterexample to the kappa bound or a certified failure of the declared roughening criterion closes the corresponding route negatively; until both close, no massless Coulomb conclusion is promoted
- POL-READ [O]: the polarization readout
  Decision: closes positively by deriving the polarization readout from the TT squaring decoder; closes negatively if the readout requires a propagation outside the single law c = 1 - s^2
- PROTON-RESIDUAL-IS-QCD [O]: the proton residual, gated on QCD dynamics
  Decision: closes positively when the QCD dynamics sector derives the proton residual; closes negatively if the derived residual is incompatible with the measured proton moment within its comparison window
- QNM-LEAVER-MU [O]: the quasinormal mu decision after a public inference rule maps an external shadow measurement to a preregistered mu interval
  Decision: closes positively when the public continued fraction computation and the preregistered inference rule decide mu; closes negatively when the exact spectrum is incompatible with that public interval
- QUADRATIC-DECODER-DATA [O]: a typed public action of the quadratic decoder on data, including every dependency it reads
  Decision: closes positively when the data action is derived from registered public inputs with an acyclic dependency graph; closes negatively if two states separated by the declared decoder receive inconsistent data actions or if an unregistered input is required
- QUANT-SUBSTRATE [O]: the Larmor gate and the Schwinger term gate on the archimedean wall
  Decision: the two gates decide: exact gate values close the Larmor clause; the Schwinger term carries the hypothesis value 1/(2 pi) and a failed gate fires it
- SCHEME-DICTIONARY [O]: the scheme dictionary between exact seeds and measured couplings
  Decision: closes positively by an exact dictionary between the seed normalization and a named measurement scheme; closes negatively if any dictionary requires a new free dimensionless parameter
- SPIN-LIFT-FORCED [O]: whether the dicyclic spin lift is forced
  Decision: closes positively by proving the dicyclic lift is the unique lift of the axiom pair; closes negatively by exhibiting a second inequivalent lift surviving the same constraints
- SQRT-PHI-TIME-GRAVITY [O]: the dynamical face of the time gravity door; the gravity face is furnished
  Decision: closes positively by furnishing the dynamical face: a dynamics whose time quantum realizes the gate line square root; closes negatively if the dynamical face is proven empty
- TT-SOURCE [O]: the emission map from an explicitly defined public source object
  Decision: closes positively by deriving the typed emission map and its source dependency; closes negatively if no map satisfies the registered TT propagation and conservation constraints
- TT-VECTOR-STATE-NORMALIZATION [O]: the vector doublet state, its two point and pseudo covariance spectra, the action normalization, the scalar comparison; the only gate yielding a numerical r(k)
  Decision: closes positively by a public vector-doublet normalization yielding a numerical r(k); closes negatively if every admissible normalization violates the registered TT identities or requires an extra free dimensionless input

Live total: 28.
