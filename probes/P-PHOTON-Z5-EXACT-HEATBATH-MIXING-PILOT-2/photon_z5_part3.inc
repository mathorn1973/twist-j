
class KernelAccess {
  public:
    static void line_sweep(Lattice &lattice, std::uint32_t cycle, bool reverse) {
        struct Line { int base; int mu; std::uint32_t ordinal; };
        std::vector<Line> lines;
        const std::uint32_t expected = static_cast<std::uint32_t>(
            D * lattice.L_ * lattice.L_ * lattice.L_
        );
        lines.reserve(expected);
        std::uint32_t ordinal = 0;
        for (int mu = 0; mu < D; ++mu) {
            for (int base = 0; base < lattice.V_; ++base) {
                if (lattice.coords_[base][mu] == 0)
                    lines.push_back({base, mu, ordinal++});
            }
        }
        if (lines.size() != expected) throw StopIntegrity("STOP_INTEGRITY line_sweep_census_failed");
        if (reverse) {
            ++lattice.diagnostics_.line_reverse_sweeps;
            std::reverse(lines.begin(), lines.end());
        } else {
            ++lattice.diagnostics_.line_forward_sweeps;
        }

        for (const Line &line : lines) {
            const Lattice::LineFaces affected = lattice.line_faces(line.base, line.mu);
            const auto masses = lattice.line_masses(affected);
            CounterBits bits(lattice.rng_, RandomKind::LINE, cycle, line.ordinal);
            const int delta = exact_category(
                masses,
                bits,
                lattice.diagnostics_.sampler[kind_slot(RandomKind::LINE)]
            );
            ++lattice.diagnostics_.line_updates;
            if (delta != 0) {
                ++lattice.diagnostics_.line_changes;
                ++lattice.diagnostics_.line_changes_by_direction[line.mu];
                lattice.apply_line_delta(line.base, line.mu, delta, affected);
            }
        }
    }

    static void flat_sheet(Lattice &lattice, std::uint32_t cycle, int mu) {
        const auto cache_before = lattice.flux_;
        const int shift = static_cast<int>(exact_uniform5(
            lattice.rng_, RandomKind::FLAT, cycle, static_cast<std::uint32_t>(mu),
            lattice.diagnostics_.uniform_rejections[kind_slot(RandomKind::FLAT)]
        ));
        ++lattice.diagnostics_.flat_trials;
        if (shift != 0) {
            ++lattice.diagnostics_.flat_nonzero;
            for (int site = 0; site < lattice.V_; ++site) {
                if (lattice.coords_[site][mu] != 0) continue;
                auto &link = lattice.links_[static_cast<std::size_t>(site) * D + mu];
                link = static_cast<std::uint8_t>(mod5(link + shift));
            }
        }
        // The operation never writes the cache: demand literal byte identity.
        // A single fresh curl audit follows at the macrocycle boundary.
        if (lattice.flux_ != cache_before)
            throw StopIntegrity("STOP_INTEGRITY flat_sheet_changed_flux_cache_bytes");
        ++lattice.diagnostics_.flat_flux_identity_checks;
    }

    static void charge_conjugation(Lattice &lattice, std::uint32_t cycle) {
        const auto words = lattice.rng_.block(RandomKind::CHARGE, cycle, 0, 0);
        const int apply = static_cast<int>((words[0] >> 31) & 1u);
        ++lattice.diagnostics_.charge_trials;
        if (apply != 0) {
            ++lattice.diagnostics_.charge_applied;
            for (auto &link : lattice.links_) link = static_cast<std::uint8_t>(mod5(-link));
            for (auto &value : lattice.flux_) value = static_cast<std::uint8_t>(mod5(-value));
        }
        // Fresh curvature/cache consistency is audited once at macrocycle end.
        ++lattice.diagnostics_.charge_flux_identity_checks;
    }

    static void macro_cycle(Lattice &lattice, std::uint32_t cycle) {
        const bool reverse = (cycle & 1u) != 0;
        lattice.local_sweep(cycle, reverse);
        line_sweep(lattice, cycle, reverse);
        for (int mu = 0; mu < D; ++mu) flat_sheet(lattice, cycle, mu);
        charge_conjugation(lattice, cycle);
        lattice.assert_flux_consistent();
        ++lattice.diagnostics_.macro_cycles;
    }
};

void print_diagnostics(const KernelDiagnostics &diagnostics) {
    std::cout
        << "DIAGNOSTICS"
        << " macro_cycles=" << diagnostics.macro_cycles
        << " local_forward=" << diagnostics.local_forward_sweeps
        << " local_reverse=" << diagnostics.local_reverse_sweeps
        << " local_updates=" << diagnostics.local_updates
        << " local_changes=" << diagnostics.local_changes
        << " line_forward=" << diagnostics.line_forward_sweeps
        << " line_reverse=" << diagnostics.line_reverse_sweeps
        << " line_updates=" << diagnostics.line_updates
        << " line_changes=" << diagnostics.line_changes
        << " flat_trials=" << diagnostics.flat_trials
        << " flat_nonzero=" << diagnostics.flat_nonzero
        << " flat_flux_identity_checks=" << diagnostics.flat_flux_identity_checks
        << " charge_trials=" << diagnostics.charge_trials
        << " charge_applied=" << diagnostics.charge_applied
        << " charge_flux_identity_checks=" << diagnostics.charge_flux_identity_checks
        << '\n';
    std::cout << "LINE_CHANGES_BY_DIRECTION";
    for (int mu = 0; mu < D; ++mu)
        std::cout << " mu" << mu << '=' << diagnostics.line_changes_by_direction[mu];
    std::cout << '\n';
    for (std::size_t slot = 0; slot < RANDOM_KIND_COUNT; ++slot) {
        const auto kind = static_cast<RandomKind>(slot);
        const SamplerStats &stats = diagnostics.sampler[slot];
        std::cout
            << "CATEGORICAL kind=" << kind_name(kind)
            << " attempts=" << stats.attempts
            << " completed=" << stats.completed
            << " total_bits=" << stats.total_bits
            << " max_bits=" << stats.max_bits
            << " over32=" << stats.over32
            << " over64=" << stats.over64
            << " over128=" << stats.over128
            << " stops=" << stats.stops
            << " uniform_rejections=" << diagnostics.uniform_rejections[slot]
            << '\n';
    }
}

void run_kernel(const Options &options) {
    Lattice lattice(options.L, options.seed, options.start);
    for (std::uint32_t cycle = 0; cycle < options.macro_cycles; ++cycle)
        KernelAccess::macro_cycle(lattice, cycle);
    lattice.assert_flux_consistent();
    std::cout
        << "KERNEL model=TWIST_Z5_FACE_WEIGHT_V1"
        << " arithmetic=CPP_INT_Z_PHI"
        << " categorical=EXACT_PROGRESSIVE_64X4"
        << " cap=" << CATEGORICAL_CAP
        << " L=" << options.L
        << " t=1"
        << " seed=" << options.seed
        << " start=" << options.start
        << " macro_cycles=" << options.macro_cycles
        << '\n';
    std::cout << "STATE hash=" << std::hex << std::setw(16) << std::setfill('0')
              << lattice.state_hash() << std::dec << std::setfill(' ') << '\n';
    print_diagnostics(lattice.diagnostics());
    std::cout << "STOP_INTEGRITY 0\n";
}

void print_sample(const Lattice &lattice, std::uint32_t index) {
    const auto radii = lattice.polyakov_radii();
    const auto histogram = lattice.flux_histogram();
    const long double total_flux = static_cast<long double>(lattice.flux().size());
    std::array<long double, 5> fraction{};
    for (int value = 0; value < 5; ++value)
        fraction[value] = static_cast<long double>(histogram[value]) / total_flux;
    long double radius_mean = 0;
    for (long double value : radii) radius_mean += value;
    radius_mean /= D;

    std::cout << std::setprecision(17)
        << "SAMPLE index=" << index
        << " logw=" << static_cast<double>(lattice.mean_log_weight())
        << " polyakov_radius_mean=" << static_cast<double>(radius_mean)
        << " polyakov_radius_0=" << static_cast<double>(radii[0])
        << " polyakov_radius_1=" << static_cast<double>(radii[1])
        << " polyakov_radius_2=" << static_cast<double>(radii[2])
        << " polyakov_radius_3=" << static_cast<double>(radii[3])
        << " vortex_density=" << static_cast<double>(lattice.vortex_density())
        << " monopole_density=" << static_cast<double>(lattice.monopole_density())
        << " score_mean=" << static_cast<double>(lattice.score_mean())
        << " flux_asym_14=" << static_cast<double>(fraction[1] - fraction[4])
        << " flux_asym_23=" << static_cast<double>(fraction[2] - fraction[3]);
    for (int value = 0; value < 5; ++value)
        std::cout << " flux_fraction_" << value << '=' << static_cast<double>(fraction[value]);
    for (int value = 0; value < 5; ++value)
        std::cout << " flux_count_" << value << '=' << histogram[value];
    std::cout << " state_hash=" << std::hex << std::setw(16) << std::setfill('0')
              << lattice.state_hash()
              << " cache_hash=" << std::setw(16) << lattice.flux_cache_hash()
              << std::dec << std::setfill(' ') << '\n';
}

void run_pilot(const Options &options) {
    Lattice lattice(options.L, options.seed, options.start);
    std::cout
        << "RUN model=TWIST_Z5_FACE_WEIGHT_V1"
        << " L=" << options.L
        << " t=1"
        << " seed=0x" << std::hex << std::setw(16) << std::setfill('0') << options.seed
        << std::dec << std::setfill(' ')
        << " start=" << options.start
        << " replica=" << options.replica
        << " thermal_cycles=" << options.thermal_cycles
        << " measurements=" << options.measurements
        << " between_cycles=" << options.between_cycles
        << " bit_cap=" << CATEGORICAL_CAP
        << '\n';

    std::uint32_t cycle = 0;
    for (; cycle < options.thermal_cycles; ++cycle)
        KernelAccess::macro_cycle(lattice, cycle);
    for (std::uint32_t sample = 0; sample < options.measurements; ++sample) {
        for (std::uint32_t between = 0; between < options.between_cycles; ++between)
            KernelAccess::macro_cycle(lattice, cycle++);
        lattice.assert_flux_consistent();
        print_sample(lattice, sample);
    }

    const KernelDiagnostics &diagnostics = lattice.diagnostics();
    std::uint64_t cap_exhaustions = 0;
    std::uint32_t max_prefix_bits = 0;
    for (const SamplerStats &stats : diagnostics.sampler) {
        cap_exhaustions += stats.stops;
        max_prefix_bits = std::max(max_prefix_bits, stats.max_bits);
    }
    const std::uint64_t expected_cycles = static_cast<std::uint64_t>(options.thermal_cycles)
        + static_cast<std::uint64_t>(options.measurements) * options.between_cycles;
    const std::uint64_t expected_local = expected_cycles * D * lattice.volume();
    const std::uint64_t expected_lines = expected_cycles * D * options.L * options.L * options.L;
    const std::uint64_t expected_flat_checks = expected_cycles * D;
    const bool flat_pass = diagnostics.flat_flux_identity_checks == expected_flat_checks;
    const bool census_pass = diagnostics.macro_cycles == expected_cycles
        && diagnostics.local_forward_sweeps == (expected_cycles + 1) / 2
        && diagnostics.local_reverse_sweeps == expected_cycles / 2
        && diagnostics.line_forward_sweeps == (expected_cycles + 1) / 2
        && diagnostics.line_reverse_sweeps == expected_cycles / 2
        && diagnostics.local_updates == expected_local
        && diagnostics.line_updates == expected_lines
        && diagnostics.flat_trials == expected_flat_checks
        && diagnostics.charge_trials == expected_cycles
        && diagnostics.charge_flux_identity_checks == expected_cycles
        && diagnostics.sampler[kind_slot(RandomKind::LOCAL)].attempts == expected_local
        && diagnostics.sampler[kind_slot(RandomKind::LOCAL)].completed == expected_local
        && diagnostics.sampler[kind_slot(RandomKind::LINE)].attempts == expected_lines
        && diagnostics.sampler[kind_slot(RandomKind::LINE)].completed == expected_lines;
    std::cout
        << "UPDATE_DIAGNOSTICS"
        << " line_nonzero_0=" << diagnostics.line_changes_by_direction[0]
        << " line_nonzero_1=" << diagnostics.line_changes_by_direction[1]
        << " line_nonzero_2=" << diagnostics.line_changes_by_direction[2]
        << " line_nonzero_3=" << diagnostics.line_changes_by_direction[3]
        << " flat_cache_identity=" << (flat_pass ? "PASS" : "FAIL")
        << " bit_cap_exhaustions=" << cap_exhaustions
        << " max_prefix_bits=" << max_prefix_bits
        << " local_decisions=" << diagnostics.local_updates
        << " line_decisions=" << diagnostics.line_updates
        << " flat_sheets=" << diagnostics.flat_trials
        << " charge_trials=" << diagnostics.charge_trials
        << '\n';
    if (!flat_pass || !census_pass || cap_exhaustions != 0)
        throw StopIntegrity("STOP_INTEGRITY pilot_diagnostics_failed");
    std::cout << "KERNEL_STATUS PASS\n";
    std::cout << "EVIDENTIAL_STATUS ZERO_PILOT_ONLY\n";
}
