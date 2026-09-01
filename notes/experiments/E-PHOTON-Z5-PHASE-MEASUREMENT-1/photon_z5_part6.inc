void run_chain(const Options &options) {
    Lattice lattice(options.L, options.seed, options.start);
    for (int sweep = 0; sweep < options.thermal_sweeps; ++sweep)
        lattice.sweep(static_cast<std::uint64_t>(sweep));

    CorrelatorAccumulator correlator(options.max_n, options.measurements);
    long double sum_log_weight = 0;
    long double sum_polyakov_radius = 0;
    long double sum_polyakov_abs5 = 0;
    std::complex<long double> sum_polyakov_fifth{0, 0};
    long double sum_vortex_density = 0;
    long double sum_vortex_largest = 0;
    long double sum_vortex_wrap = 0;
    long double sum_monopole_density = 0;
    long double sum_monopole_weighted_density = 0;
    long double sum_monopole_largest = 0;
    long double sum_monopole_wrap = 0;
    long double sum_score = 0;
    std::array<long double, 5> flux_fraction{};

    std::uint64_t sweep_index = static_cast<std::uint64_t>(options.thermal_sweeps);
    std::cout << std::setprecision(17);
    std::cout << "RUN model=TWIST_Z5_FACE_WEIGHT_V1 kernel=EXACT_PHI_HEATBATH"
              << " L=" << options.L
              << " t=1"
              << " seed=" << options.seed
              << " start=" << options.start
              << " thermal_sweeps=" << options.thermal_sweeps
              << " measurements=" << options.measurements
              << " between_sweeps=" << options.between_sweeps
              << " max_n=" << options.max_n << "\n";

    for (int measurement = 0; measurement < options.measurements; ++measurement) {
        for (int sweep = 0; sweep < options.between_sweeps; ++sweep)
            lattice.sweep(sweep_index++);
        lattice.assert_flux_consistent();

        const auto polyakov = lattice.polyakov();
        long double radius = 0;
        long double abs5 = 0;
        std::complex<long double> fifth{0, 0};
        for (const auto &value : polyakov) {
            const long double magnitude = std::abs(value);
            radius += magnitude;
            abs5 += std::pow(magnitude, 5);
            fifth += std::pow(value, 5);
        }
        radius /= D;
        abs5 /= D;
        fifth /= static_cast<long double>(D);

        const auto vortex = lattice.vortex_components();
        const auto current = lattice.monopole_current();
        const auto monopole = lattice.monopole_components(current);
        const auto histogram = lattice.flux_histogram();
        const long double log_weight = lattice.mean_log_weight();
        const long double score = lattice.score_mean();
        correlator.add(lattice);

        const long double vortex_density =
            static_cast<long double>(vortex.occupied) / (lattice.volume() * NPAIR);
        const long double vortex_largest =
            static_cast<long double>(vortex.largest) / (lattice.volume() * NPAIR);
        const long double monopole_density =
            static_cast<long double>(monopole.occupied) / (lattice.volume() * D);
        const long double monopole_weighted_density =
            static_cast<long double>(monopole.weighted_occupied) / (lattice.volume() * D);
        const long double monopole_largest =
            static_cast<long double>(monopole.largest) / lattice.volume();

        sum_log_weight += log_weight;
        sum_polyakov_radius += radius;
        sum_polyakov_abs5 += abs5;
        sum_polyakov_fifth += fifth;
        sum_vortex_density += vortex_density;
        sum_vortex_largest += vortex_largest;
        sum_vortex_wrap += vortex.wraps ? 1.0L : 0.0L;
        sum_monopole_density += monopole_density;
        sum_monopole_weighted_density += monopole_weighted_density;
        sum_monopole_largest += monopole_largest;
        sum_monopole_wrap += monopole.wraps ? 1.0L : 0.0L;
        sum_score += score;
        for (int f = 0; f < 5; ++f)
            flux_fraction[f] += static_cast<long double>(histogram[f]) /
                (lattice.volume() * NPAIR);

        std::cout << "SAMPLE index=" << measurement
                  << " logw=" << static_cast<double>(log_weight)
                  << " polyakov_radius=" << static_cast<double>(radius)
                  << " p0_re=" << static_cast<double>(polyakov[0].real())
                  << " p0_im=" << static_cast<double>(polyakov[0].imag())
                  << " vortex_density=" << static_cast<double>(vortex_density)
                  << " vortex_wrap=" << (vortex.wraps ? 1 : 0)
                  << " vortex_largest=" << static_cast<double>(vortex_largest)
                  << " vortex_components=" << vortex.components
                  << " monopole_density=" << static_cast<double>(monopole_density)
                  << " monopole_weighted_density=" << static_cast<double>(monopole_weighted_density)
                  << " monopole_wrap=" << (monopole.wraps ? 1 : 0)
                  << " monopole_largest=" << static_cast<double>(monopole_largest)
                  << " monopole_components=" << monopole.components
                  << " score_mean=" << static_cast<double>(score)
                  << " state_hash=" << std::hex << lattice.state_hash() << std::dec
                  << "\n";
    }

    const long double norm = 1.0L / options.measurements;
    const long double anisotropy = sum_polyakov_abs5 > 0
        ? std::abs(sum_polyakov_fifth * norm) / (sum_polyakov_abs5 * norm)
        : 0;
    std::cout << "SUMMARY"
              << " mean_logw=" << static_cast<double>(sum_log_weight * norm)
              << " polyakov_radius=" << static_cast<double>(sum_polyakov_radius * norm)
              << " polyakov_a5=" << static_cast<double>(anisotropy)
              << " vortex_density=" << static_cast<double>(sum_vortex_density * norm)
              << " vortex_wrap_probability=" << static_cast<double>(sum_vortex_wrap * norm)
              << " vortex_largest_fraction=" << static_cast<double>(sum_vortex_largest * norm)
              << " monopole_density=" << static_cast<double>(sum_monopole_density * norm)
              << " monopole_weighted_density=" << static_cast<double>(sum_monopole_weighted_density * norm)
              << " monopole_wrap_probability=" << static_cast<double>(sum_monopole_wrap * norm)
              << " monopole_largest_per_volume=" << static_cast<double>(sum_monopole_largest * norm)
              << " score_mean=" << static_cast<double>(sum_score * norm)
              << "\n";
    std::cout << "FLUX_FRACTIONS";
    for (int f = 0; f < 5; ++f)
        std::cout << " f" << f << "=" << static_cast<double>(flux_fraction[f] * norm);
    std::cout << "\n";

    for (int n = 1; n <= options.max_n; ++n) {
        const auto value = correlator.total(n);
        std::cout << "CORRELATOR n=" << n
                  << " real=" << static_cast<double>(value.real())
                  << " imag=" << static_cast<double>(value.imag());
        if (n < options.max_n) {
            const auto next = correlator.total(n + 1);
            const long double ratio = next.real() != 0
                ? value.real() / next.real()
                : std::numeric_limits<long double>::quiet_NaN();
            const long double target =
                (std::pow(static_cast<long double>(n), -4)
                 + std::pow(static_cast<long double>(options.L - n), -4)) /
                (std::pow(static_cast<long double>(n + 1), -4)
                 + std::pow(static_cast<long double>(options.L - n - 1), -4));
            std::cout << " ratio=" << static_cast<double>(ratio)
                      << " q4_target=" << static_cast<double>(target);
        }
        std::cout << "\n";
    }
    std::cout << "DUAL_WARD_STATUS NOT_IMPLEMENTED_PILOT\n";
    std::cout << "CORRELATOR_UNCERTAINTY_STATUS NOT_IMPLEMENTED_PILOT\n";
    std::cout << "EVIDENTIAL_STATUS ZERO_PILOT_ONLY\n";
}

}  // namespace

int main(int argc, char **argv) {
    try {
        const Options options = parse_options(argc, argv);
        if (options.self_test) self_test();
        else run_chain(options);
        return 0;
    } catch (const std::exception &error) {
        std::cerr << "ERROR: " << error.what() << '\n';
        return 2;
    }
}
