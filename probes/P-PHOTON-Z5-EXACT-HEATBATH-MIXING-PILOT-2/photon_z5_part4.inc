
class VectorBits {
  public:
    explicit VectorBits(std::vector<int> values) : values_(std::move(values)) {}
    int next() {
        if (cursor_ >= values_.size()) throw std::runtime_error("test bit source exhausted");
        return values_[cursor_++];
    }
    std::string label() const { return "vector_test_bits"; }
  private:
    std::vector<int> values_;
    std::size_t cursor_{0};
};

class FifthBoundaryBits {
  public:
    int next() {
        remainder_ *= 2;
        if (remainder_ >= 5) {
            remainder_ -= 5;
            return 1;
        }
        return 0;
    }
    std::string label() const { return "negative_exact_boundary"; }
  private:
    int remainder_{1};  // binary expansion of the exact boundary U=1/5
};

class RejectOnceRng {
  public:
    std::uint64_t u64(RandomKind, std::uint32_t, std::uint32_t, std::uint32_t block) const {
        return block == 0 ? std::numeric_limits<std::uint64_t>::max() : 7u;
    }
};

void test_exact_prefix_boundaries() {
    SamplerStats upper_stats;
    std::vector<int> upper_bits(64, 1);
    upper_bits[0] = 0;  // prefix=2^63-1: upper endpoint is exactly 1/2.
    VectorBits upper_source(std::move(upper_bits));
    const int lower_category = exact_category(
        equal_masses<2>(), upper_source, upper_stats
    );
    if (lower_category != 0 || upper_stats.max_bits != 64)
        throw std::runtime_error("upper threshold endpoint test failed");

    SamplerStats lower_stats;
    std::vector<int> lower_bits(64, 0);
    lower_bits[0] = 1;  // prefix=2^63: lower endpoint is exactly 1/2.
    VectorBits lower_source(std::move(lower_bits));
    const int upper_category = exact_category(
        equal_masses<2>(), lower_source, lower_stats
    );
    if (upper_category != 1 || lower_stats.max_bits != 64)
        throw std::runtime_error("lower threshold endpoint test failed");
}

void test_cap_stop_integrity() {
    SamplerStats stats;
    FifthBoundaryBits source;
    bool stopped = false;
    try {
        (void)exact_category(equal_masses<5>(), source, stats);
    } catch (const StopIntegrity &error) {
        stopped = std::string(error.what()).find("STOP_INTEGRITY") == 0;
    }
    if (!stopped || stats.attempts != 1 || stats.completed != 0 || stats.stops != 1)
        throw std::runtime_error("categorical cap negative test failed");
}

void test_rng_namespaces() {
    auto domains = RANDOM_DOMAINS;
    std::sort(domains.begin(), domains.end());
    if (std::adjacent_find(domains.begin(), domains.end()) != domains.end())
        throw std::runtime_error("random kind domains are not injective");
    const CounterRng rng(0x123456789abcdef0ULL);
    std::array<std::uint64_t, RANDOM_KIND_COUNT> words{};
    for (std::size_t slot = 0; slot < RANDOM_KIND_COUNT; ++slot) {
        CounterBits bits(rng, static_cast<RandomKind>(slot), 7, 11);
        std::uint64_t word = 0;
        for (int bit = 0; bit < 64; ++bit) word = (word << 1) | bits.next();
        words[slot] = word;
    }
    auto sorted = words;
    std::sort(sorted.begin(), sorted.end());
    if (std::adjacent_find(sorted.begin(), sorted.end()) != sorted.end())
        throw std::runtime_error("random namespace collision in known tuple");
    const std::array<std::uint64_t, RANDOM_KIND_COUNT> expected{{
        0x97ce33141a291992ULL,
        0xd585ccc9abe0f907ULL,
        0xe5d6e154ae60448eULL,
        0xb486ef61e40d0516ULL,
        0x080d764bf04c4e9aULL,
    }};
    if (words != expected) throw std::runtime_error("random namespace known-answer mismatch");

    CounterBits untouched_a(rng, RandomKind::LINE, 9, 4);
    std::uint64_t before = 0;
    for (int bit = 0; bit < 64; ++bit) before = (before << 1) | untouched_a.next();
    CounterBits noise(rng, RandomKind::LOCAL, 9, 4);
    for (int bit = 0; bit < 256; ++bit) (void)noise.next();
    CounterBits untouched_b(rng, RandomKind::LINE, 9, 4);
    std::uint64_t after = 0;
    for (int bit = 0; bit < 64; ++bit) after = (after << 1) | untouched_b.next();
    if (before != after) throw std::runtime_error("counter namespace shifted after variable consumption");

    std::uint64_t rejections = 0;
    const int uniform = static_cast<int>(exact_uniform5(
        RejectOnceRng{}, RandomKind::HOT, 0, 0, rejections
    ));
    if (uniform != 2 || rejections != 1)
        throw std::runtime_error("exact uniform5 rejection endpoint failed");
    if (((rng.block(RandomKind::CHARGE, 7, 11, 0)[0] >> 31) & 1u) != 0u)
        throw std::runtime_error("charge first-bit convention failed");
}

void test_local_witness_and_balance() {
    Lattice lattice(3, 0x123456789abcdef0ULL, "hot");
    if (lattice.links()[0] != 2) throw std::runtime_error("local witness old-link mismatch");
    const std::array<std::pair<int, int>, 6> expected_raw{{
        {0, +1}, {2, -1}, {2, +1}, {0, -1}, {4, +1}, {0, -1},
    }};
    const auto affected = lattice.incident(0, 0);
    for (std::size_t index = 0; index < affected.size(); ++index) {
        const auto &[base, pair, sign] = affected[index];
        const int residual = mod5(lattice.flux()[static_cast<std::size_t>(base) * NPAIR + pair]
                                  - sign * lattice.links()[0]);
        if (std::pair<int, int>{residual, sign} != expected_raw[index])
            throw std::runtime_error("local raw residual/sign witness mismatch");
    }
    const auto masses = lattice.local_masses(0, 0);
    const std::array<QPhi, 5> expected{{
        {128, -64}, {20, 32}, {8, -4}, {52, -32}, {2, 3},
    }};
    if (masses != expected) throw std::runtime_error("local exact geometry witness mismatch");

    std::array<QPhi, 5> complete{};
    for (int candidate = 0; candidate < 5; ++candidate) {
        Lattice shifted = lattice;
        shifted.apply_link_value_for_test(0, 0, candidate);
        shifted.assert_flux_consistent();
        complete[candidate] = shifted.global_weight();
    }
    for (int i = 0; i < 5; ++i) {
        for (int j = 0; j < 5; ++j) {
            if (!(complete[i] * masses[j] == complete[j] * masses[i]))
                throw std::runtime_error("local heat-bath detailed balance failed");
        }
    }
}

void test_line_orbit_action_and_balance() {
    for (int L : {3, 4}) {
        Lattice lattice(L, 0x0f1e2d3c4b5a6978ULL, "hot");
        const int base = 0;
        const int mu = 0;
        const auto masses = lattice.line_masses(base, mu);
        std::array<QPhi, 5> complete{};
        for (int delta = 0; delta < 5; ++delta) {
            Lattice shifted = lattice;
            shifted.apply_line_delta_for_test(base, mu, delta);
            shifted.assert_flux_consistent();
            complete[delta] = shifted.global_weight();
            const auto shifted_masses = shifted.line_masses(base, mu);
            for (int next_delta = 0; next_delta < 5; ++next_delta) {
                if (!(shifted_masses[next_delta] == masses[mod5(delta + next_delta)]))
                    throw std::runtime_error("line relative-delta orbit rotation failed");
            }
        }
        for (int i = 0; i < 5; ++i) {
            for (int j = 0; j < 5; ++j) {
                // Orbit mass is the complete action up to one common unaffected factor;
                // this is also pi_i K(i,j)=pi_j K(j,i) after cancelling the orbit sum.
                if (!(complete[i] * masses[j] == complete[j] * masses[i]))
                    throw std::runtime_error("line orbit action/detailed balance failed");
            }
        }
    }
}

std::string masses_text(const std::array<QPhi, 5> &masses) {
    std::ostringstream out;
    for (int index = 0; index < 5; ++index) {
        if (index != 0) out << ';';
        out << masses[index].a << ',' << masses[index].b;
    }
    return out.str();
}

std::uint64_t local_table_digest() {
    std::uint64_t hash = 1469598103934665603ULL;
    auto absorb = [&](const std::string &text) {
        for (unsigned char byte : text) {
            hash ^= byte;
            hash *= 1099511628211ULL;
        }
    };
    for (const auto &environment : local_mass_table()) {
        for (const QPhi &mass : environment) {
            absorb(mass.a.str());
            absorb(",");
            absorb(mass.b.str());
            absorb(";");
        }
    }
    return hash;
}

void test_flat_and_charge_identities();
std::uint64_t two_cycle_fixture_hash(int L, std::uint64_t expected);

void fixture_output() {
    const auto known = philox4x32_10({0, 0, 0, 0}, {0, 0});
    const std::array<std::uint32_t, 4> expected_philox{{
        0x6627e8d5u, 0xe169c58du, 0xbc57ac4cu, 0x9b00dbd8u,
    }};
    if (known != expected_philox) throw std::runtime_error("fixture Philox mismatch");
    test_exact_prefix_boundaries();
    test_cap_stop_integrity();
    test_rng_namespaces();
    test_local_witness_and_balance();
    test_line_orbit_action_and_balance();
    test_flat_and_charge_identities();

    Lattice local(3, 0x123456789abcdef0ULL, "hot");
    Lattice line3(3, 0x0f1e2d3c4b5a6978ULL, "hot");
    Lattice line4(4, 0x0f1e2d3c4b5a6978ULL, "hot");
    const std::uint64_t hash_l3 = two_cycle_fixture_hash(3, 0xf2ddb5b90debf718ULL);
    const std::uint64_t hash_l4 = two_cycle_fixture_hash(4, 0x6119d2e215a1020bULL);

    std::cout << "FIXTURE PHILOX_ZERO 6627e8d5e169c58dbc57ac4c9b00dbd8\n";
    std::cout << "FIXTURE NAMESPACE HOT=97ce33141a291992 LOCAL=d585ccc9abe0f907"
                 " LINE=e5d6e154ae60448e FLAT=b486ef61e40d0516 CHARGE=080d764bf04c4e9a\n";
    std::cout << "FIXTURE PREFIX_ENDPOINTS PASS\n";
    std::cout << "FIXTURE CAP256_STOP_INTEGRITY PASS\n";
    std::cout << "FIXTURE UNIFORM5_REJECTION PASS\n";
    std::cout << "FIXTURE HASH_SCHEME TWISTJ_FNVLIKE64_V1\n";
    std::cout << "FIXTURE LOCAL_ENVIRONMENTS count=15625 digest=" << std::hex
              << std::setw(16) << std::setfill('0') << local_table_digest()
              << std::dec << std::setfill(' ') << '\n';
    std::cout << "FIXTURE LOCAL_WITNESS old=" << static_cast<int>(local.links()[0])
              << " residual_plus=0,2,4 residual_minus=2,0,0 key=1800"
              << " masses=" << masses_text(local.local_masses(0, 0)) << '\n';
    std::cout << "FIXTURE LINE_L3 masses=" << masses_text(line3.line_masses(0, 0)) << '\n';
    std::cout << "FIXTURE LINE_L4 masses=" << masses_text(line4.line_masses(0, 0)) << '\n';
    std::cout << "FIXTURE L3_TWO_CYCLE_STATE_HASH " << std::hex << std::setw(16)
              << std::setfill('0') << hash_l3 << '\n';
    std::cout << "FIXTURE L4_TWO_CYCLE_STATE_HASH " << std::setw(16) << hash_l4
              << std::dec << std::setfill(' ') << '\n';
    std::cout << "FIXTURE RESULT PASS\n";
}

void test_flat_and_charge_identities() {
    Lattice lattice(3, 0x8877665544332211ULL, "hot");
    for (int mu = 0; mu < D; ++mu) lattice.apply_flat_sheet_for_test(mu, mu + 1);
    lattice.apply_charge_for_test();
    lattice.assert_flux_consistent();
}

void test_pilot_observables() {
    Lattice lattice(3, 0x3141592653589793ULL, "hot");
    KernelAccess::macro_cycle(lattice, 0);
    const auto radii = lattice.polyakov_radii();
    for (long double value : radii)
        if (!std::isfinite(value) || value < 0 || value > 1)
            throw std::runtime_error("invalid Polyakov radius fixture");
    const std::array<long double, 4> scalars{{
        lattice.mean_log_weight(), lattice.vortex_density(),
        lattice.monopole_density(), lattice.score_mean(),
    }};
    for (long double value : scalars)
        if (!std::isfinite(value)) throw std::runtime_error("nonfinite pilot observable fixture");
    const auto histogram = lattice.flux_histogram();
    std::uint64_t total = 0;
    for (std::uint64_t count : histogram) total += count;
    if (total != lattice.flux().size()) throw std::runtime_error("flux histogram census failed");
    (void)lattice.flux_cache_hash();
}

std::uint64_t two_cycle_fixture_hash(int L, std::uint64_t expected) {
    constexpr std::uint64_t seed = 0x123456789abcdef0ULL;
    Lattice lattice(L, seed, "hot");
    KernelAccess::macro_cycle(lattice, 0);
    KernelAccess::macro_cycle(lattice, 1);
    lattice.assert_flux_consistent();
    const KernelDiagnostics &diag = lattice.diagnostics();
    const std::uint64_t local_per_cycle = static_cast<std::uint64_t>(D) * lattice.volume();
    const std::uint64_t lines_per_cycle = static_cast<std::uint64_t>(D) * L * L * L;
    if (diag.macro_cycles != 2
        || diag.local_forward_sweeps != 1 || diag.local_reverse_sweeps != 1
        || diag.line_forward_sweeps != 1 || diag.line_reverse_sweeps != 1
        || diag.local_updates != 2 * local_per_cycle
        || diag.line_updates != 2 * lines_per_cycle
        || diag.flat_trials != 2 * D || diag.flat_flux_identity_checks != 2 * D
        || diag.charge_trials != 2 || diag.charge_flux_identity_checks != 2) {
        throw std::runtime_error("complete macro-cycle census failed");
    }
    for (const SamplerStats &stats : diag.sampler) {
        if (stats.stops != 0 || stats.attempts != stats.completed || stats.max_bits > CATEGORICAL_CAP)
            throw std::runtime_error("successful fixture categorical diagnostics failed");
    }
    const std::uint64_t actual = lattice.state_hash();
    if (actual != expected) {
        std::ostringstream message;
        message << "deterministic L=" << L << " state hash failed: got "
                << std::hex << std::setw(16) << std::setfill('0') << actual;
        throw std::runtime_error(message.str());
    }
    return actual;
}

void self_test() {
    const auto known = philox4x32_10({0, 0, 0, 0}, {0, 0});
    const std::array<std::uint32_t, 4> expected_philox{{
        0x6627e8d5u, 0xe169c58du, 0xbc57ac4cu, 0x9b00dbd8u,
    }};
    if (known != expected_philox) throw std::runtime_error("Philox known-answer test failed");

    const auto &weights = face_weights();
    if (!(weights[1] * weights[2] == QPhi{1, 0})
        || !(weights[1] + weights[2] == QPhi{3, 0}))
        throw std::runtime_error("exact Z[phi] face-weight identities failed");

    test_exact_prefix_boundaries();
    test_cap_stop_integrity();
    test_rng_namespaces();
    test_local_witness_and_balance();

    Lattice gauge(3, 0x1020304050607080ULL, "hot");
    const auto flux_before = gauge.flux();
    gauge.gauge_transform_for_test();
    gauge.assert_flux_consistent();
    if (gauge.flux() != flux_before) throw std::runtime_error("gauge invariance failed");

    test_line_orbit_action_and_balance();
    test_flat_and_charge_identities();
    test_pilot_observables();

    // Values are frozen jointly with the independent Python implementation.
    constexpr std::uint64_t expected_l3 = 0xf2ddb5b90debf718ULL;
    constexpr std::uint64_t expected_l4 = 0x6119d2e215a1020bULL;
    const std::uint64_t hash_l3 = two_cycle_fixture_hash(3, expected_l3);
    const std::uint64_t hash_l4 = two_cycle_fixture_hash(4, expected_l4);

    std::cout << "SELF_TEST PHILOX PASS\n";
    std::cout << "SELF_TEST Z_PHI_CPP_INT PASS\n";
    std::cout << "SELF_TEST EXACT_PREFIX_64X4_ENDPOINTS PASS\n";
    std::cout << "SELF_TEST CAP256_STOP_INTEGRITY_NEGATIVE PASS\n";
    std::cout << "SELF_TEST COUNTER_NAMESPACES PASS\n";
    std::cout << "SELF_TEST UNIFORM5_REJECTION_AND_CHARGE_BIT PASS\n";
    std::cout << "SELF_TEST LOCAL_WITNESS_AND_DETAILED_BALANCE PASS\n";
    std::cout << "SELF_TEST GAUGE_AND_FLUX_CACHE PASS\n";
    std::cout << "SELF_TEST LINE_ORBIT_COMPLETE_ACTION PASS\n";
    std::cout << "SELF_TEST LINE_DETAILED_BALANCE PASS\n";
    std::cout << "SELF_TEST COMPLETE_FORWARD_REVERSE_SWEEPS PASS\n";
    std::cout << "SELF_TEST FLAT_SHEET_FLUX_IDENTITY PASS\n";
    std::cout << "SELF_TEST CHARGE_CONJUGATION_HALF PASS\n";
    std::cout << "SELF_TEST PILOT_OBSERVABLES PASS\n";
    std::cout << "SELF_TEST L3_TWO_CYCLE_STATE_HASH " << std::hex << std::setw(16)
              << std::setfill('0') << hash_l3 << '\n';
    std::cout << "SELF_TEST L4_TWO_CYCLE_STATE_HASH " << std::setw(16) << hash_l4
              << std::dec << std::setfill(' ') << '\n';
    std::cout << "SELF_TEST RESULT PASS\n";
}

int emit_modeled_stop(const std::string &message) {
    std::string reason = message;
    for (char &character : reason) {
        const unsigned char byte = static_cast<unsigned char>(character);
        if (!std::isalnum(byte) && character != '_' && character != '-' && character != '=')
            character = '_';
    }
    std::cout << "KERNEL_STATUS STOP_INTEGRITY\n";
    std::cout << "INTEGRITY_REASON value=" << reason << '\n';
    std::cout << "EVIDENTIAL_STATUS ZERO_PILOT_ONLY\n";
    return 0;
}

}  // namespace

int main(int argc, char **argv) {
#ifdef _WIN32
    _setmode(_fileno(stdout), _O_BINARY);
    _setmode(_fileno(stderr), _O_BINARY);
#endif
    Options options;
    bool options_ready = false;
    try {
        options = parse_options(argc, argv);
        options_ready = true;
        if (options.self_test) self_test();
        else if (options.fixture) fixture_output();
        else if (options.stop_integrity_fixture)
            throw StopIntegrity("STOP_INTEGRITY modeled_cap_fixture");
        else if (options.kernel_run) run_kernel(options);
        else run_pilot(options);
        return 0;
    } catch (const StopIntegrity &error) {
        if (options_ready && (options.pilot || options.stop_integrity_fixture)) {
            return emit_modeled_stop(error.what());
        }
        std::cerr << error.what() << '\n';
        return 3;
    } catch (const std::exception &error) {
        if (options_ready && options.pilot) return emit_modeled_stop(error.what());
        std::cerr << "ERROR: " << error.what() << '\n';
        return 2;
    }
}
