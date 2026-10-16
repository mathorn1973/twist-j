// P-PHOTON-AXIS-POS-PRIMAL-1 production engine.
//
// The accepted pilot-2 exact primal sampler is compiled byte for byte from its
// own public probe directory. Only its main() symbol is renamed, so every pilot
// mode keeps its exact behaviour and the macrocycle, random namespaces, exact
// Z[phi] heat baths, line moves, flat sheets and charge conjugation are the
// accepted ones. This file adds:
//   --axis          one production chain with stdin endpoint control,
//   --axis-fixture  a deterministic synthetic link field for reduction checks.
// The AXIS output is the exact integer slice sums S_{I,r}(t) in Z[phi].

#define main pilot2_engine_main
#include "../P-PHOTON-Z5-EXACT-HEATBATH-MIXING-PILOT-2/photon_z5.cpp"
#undef main

#include <cstdio>
#include <fstream>

namespace {

// #1116 ordered orientations (01,02,03,23,31,12) mapped to the engine's
// positive pair index and sign; F_31 = -F_13.
struct AxisOrientation { const char *name; int pair; int sign; };
constexpr std::array<AxisOrientation, 6> AXIS_ORIENT{{
    {"01", 0, +1}, {"02", 1, +1}, {"03", 2, +1},
    {"23", 5, +1}, {"31", 4, -1}, {"12", 3, +1},
}};

// Score G = (0, 1, 2+sqrt5, -(2+sqrt5), -1) as u + v*phi, 2+sqrt5 = 1+2phi.
constexpr std::array<std::array<long long, 2>, 5> SCORE_UV{{
    {{0, 0}}, {{1, 0}}, {{1, 2}}, {{-1, -2}}, {{-1, 0}},
}};

std::vector<std::array<long long, 2>> axis_sums(const Lattice &lattice) {
    const int L = lattice.L();
    std::vector<std::array<long long, 2>> s(static_cast<std::size_t>(6) * D * L, {0, 0});
    const auto &flux = lattice.flux();
    const auto &coords = lattice.coordinates();
    for (int site = 0; site < lattice.volume(); ++site) {
        for (int I = 0; I < 6; ++I) {
            int f = flux[static_cast<std::size_t>(site) * NPAIR + AXIS_ORIENT[I].pair];
            if (AXIS_ORIENT[I].sign < 0) f = mod5(-f);
            const auto &g = SCORE_UV[f];
            for (int r = 0; r < D; ++r) {
                auto &cell = s[(static_cast<std::size_t>(I) * D + r) * L + coords[site][r]];
                cell[0] += g[0];
                cell[1] += g[1];
            }
        }
    }
    return s;
}

void print_axis_sums(const Lattice &lattice, const char *tag, std::uint64_t index) {
    const int L = lattice.L();
    const auto s = axis_sums(lattice);
    for (int I = 0; I < 6; ++I) {
        for (int r = 0; r < D; ++r) {
            std::cout << tag << " index=" << index << " I=" << AXIS_ORIENT[I].name << " r=" << r << " S=";
            for (int t = 0; t < L; ++t) {
                const auto &cell = s[(static_cast<std::size_t>(I) * D + r) * L + t];
                if (t) std::cout << ';';
                std::cout << cell[0] << ',' << cell[1];
            }
            std::cout << '\n';
        }
    }
}

void write_link_state(const Lattice &lattice, const std::string &path, const std::string &chain,
                      std::uint64_t sample, std::uint64_t macrocycle) {
    std::ofstream out(path, std::ios::binary | std::ios::trunc);
    if (!out) throw StopIntegrity("STOP_INTEGRITY state_file_open_failed");
    std::string payload(lattice.links().size(), '0');
    for (std::size_t i = 0; i < payload.size(); ++i)
        payload[i] = static_cast<char>('0' + lattice.links()[i]);
    out << "TWISTJ_Z5_LINK_STATE_V1\n" << "L=" << lattice.L() << '\n' << "CHAIN=" << chain << '\n'
        << "SAMPLE=" << sample << '\n' << "MACROCYCLE=" << macrocycle << '\n'
        << "LINKS=" << payload << '\n' << "END\n";
    out.close();
    if (!out) throw StopIntegrity("STOP_INTEGRITY state_file_write_failed");
}

void print_progress_diagnostics(const char *tag, const Lattice &lattice, std::uint64_t done) {
    const KernelDiagnostics &d = lattice.diagnostics();
    std::uint64_t cap_exhaustions = 0;
    std::uint32_t max_prefix_bits = 0;
    for (const SamplerStats &stats : d.sampler) {
        cap_exhaustions += stats.stops;
        max_prefix_bits = std::max(max_prefix_bits, stats.max_bits);
    }
    // The census is the pilot-2 UPDATE_DIAGNOSTICS census evaluated at `done`.
    const std::uint64_t L = static_cast<std::uint64_t>(lattice.L());
    const std::uint64_t expected_local = done * D * static_cast<std::uint64_t>(lattice.volume());
    const std::uint64_t expected_lines = done * D * L * L * L;
    const bool census = d.macro_cycles == done
        && d.local_forward_sweeps == (done + 1) / 2 && d.local_reverse_sweeps == done / 2
        && d.line_forward_sweeps == (done + 1) / 2 && d.line_reverse_sweeps == done / 2
        && d.local_updates == expected_local && d.line_updates == expected_lines
        && d.flat_trials == done * D && d.flat_flux_identity_checks == done * D
        && d.charge_trials == done && d.charge_flux_identity_checks == done
        && d.sampler[kind_slot(RandomKind::LOCAL)].attempts == expected_local
        && d.sampler[kind_slot(RandomKind::LOCAL)].completed == expected_local
        && d.sampler[kind_slot(RandomKind::LINE)].attempts == expected_lines
        && d.sampler[kind_slot(RandomKind::LINE)].completed == expected_lines
        && cap_exhaustions == 0;
    std::cout << tag << " completed=" << done
              << " state_hash=" << std::hex << std::setw(16) << std::setfill('0') << lattice.state_hash()
              << std::dec << std::setfill(' ')
              << " line_nonzero_0=" << d.line_changes_by_direction[0]
              << " line_nonzero_1=" << d.line_changes_by_direction[1]
              << " line_nonzero_2=" << d.line_changes_by_direction[2]
              << " line_nonzero_3=" << d.line_changes_by_direction[3]
              << " bit_cap_exhaustions=" << cap_exhaustions
              << " max_prefix_bits=" << max_prefix_bits
              << " local_decisions=" << d.local_updates
              << " line_decisions=" << d.line_updates
              << " census=" << (census ? "PASS" : "FAIL") << std::endl;
    if (!census) throw StopIntegrity("STOP_INTEGRITY axis_census_failed");
}

struct AxisOptions {
    int L{0};
    std::uint64_t seed{0};
    std::string start;
    std::string chain;
    std::vector<std::uint64_t> endpoints;
    std::uint64_t window{0};
    std::uint64_t samples{0};
    std::uint64_t spacing{0};
    std::string state_dir;
};

std::vector<std::uint64_t> parse_list(const std::string &text) {
    std::vector<std::uint64_t> values;
    std::size_t begin = 0;
    while (true) {
        const std::size_t end = text.find(',', begin);
        values.push_back(parse_u64(text.substr(begin, end == std::string::npos ? std::string::npos : end - begin),
                                   "--endpoints"));
        if (end == std::string::npos) break;
        begin = end + 1;
    }
    return values;
}

AxisOptions parse_axis(int argc, char **argv) {
    AxisOptions o;
    for (int i = 2; i < argc; i += 2) {
        if (i + 1 >= argc) throw std::runtime_error("axis option without value");
        const std::string key = argv[i], value = argv[i + 1];
        if (key == "--L") o.L = static_cast<int>(parse_i64(value, "--L"));
        else if (key == "--seed") o.seed = parse_u64(value, "--seed");
        else if (key == "--start") o.start = value;
        else if (key == "--chain") o.chain = value;
        else if (key == "--endpoints") o.endpoints = parse_list(value);
        else if (key == "--window") o.window = parse_u64(value, "--window");
        else if (key == "--samples") o.samples = parse_u64(value, "--samples");
        else if (key == "--spacing") o.spacing = parse_u64(value, "--spacing");
        else if (key == "--state-dir") o.state_dir = value;
        else throw std::runtime_error("unknown axis option " + key);
    }
    if (o.L < 2 || o.L > 32 || o.endpoints.empty() || o.window == 0 || o.spacing == 0
        || (o.start != "cold" && o.start != "hot") || o.chain.empty())
        throw std::runtime_error("invalid axis options");
    for (std::size_t i = 0; i < o.endpoints.size(); ++i) {
        if (o.endpoints[i] < o.window || (i && o.endpoints[i] <= o.endpoints[i - 1]))
            throw std::runtime_error("invalid axis endpoint schedule");
    }
    const std::uint64_t last = o.endpoints.back() + o.samples * o.spacing;
    if (last > std::numeric_limits<std::uint32_t>::max())
        throw std::runtime_error("macrocycle counter range");
    return o;
}

int run_axis(int argc, char **argv) {
    const AxisOptions o = parse_axis(argc, argv);
    Lattice lattice(o.L, o.seed, o.start);
    std::cout << "AXIS_RUN model=TWIST_Z5_FACE_WEIGHT_V1 L=" << o.L << " t=1 seed=0x" << std::hex
              << std::setw(16) << std::setfill('0') << o.seed << std::dec << std::setfill(' ')
              << " start=" << o.start << " chain=" << o.chain << " window=" << o.window
              << " samples=" << o.samples << " spacing=" << o.spacing << " bit_cap=" << CATEGORICAL_CAP
              << std::endl;
    std::uint64_t done = 0;
    std::uint64_t accepted = 0;
    for (std::size_t e = 0; e < o.endpoints.size() && accepted == 0; ++e) {
        const std::uint64_t endpoint = o.endpoints[e];
        while (done < endpoint) {
            KernelAccess::macro_cycle(lattice, static_cast<std::uint32_t>(done));
            ++done;
            if (done > endpoint - o.window) print_sample(lattice, static_cast<std::uint32_t>(done));
        }
        lattice.assert_flux_consistent();
        print_progress_diagnostics("ENDPOINT", lattice, done);
        std::string command;
        if (!std::getline(std::cin, command)) throw StopIntegrity("STOP_INTEGRITY endpoint_command_missing");
        if (command == "MEASURE") accepted = endpoint;
        else if (command != "CONTINUE") throw StopIntegrity("STOP_INTEGRITY endpoint_command_invalid");
    }
    if (accepted == 0) {
        std::cout << "THERMAL_EXHAUSTED completed=" << done << '\n';
        std::cout << "AXIS_STATUS THERMAL_EXHAUSTED\nEVIDENTIAL_STATUS ZERO_UNTIL_ANALYSIS\n";
        return 0;
    }
    std::cout << "MEASURE_BEGIN thermal_endpoint=" << accepted << '\n';
    for (std::uint64_t s = 0; s < o.samples; ++s) {
        for (std::uint64_t k = 0; k < o.spacing; ++k) {
            KernelAccess::macro_cycle(lattice, static_cast<std::uint32_t>(done));
            ++done;
        }
        lattice.assert_flux_consistent();
        print_sample(lattice, static_cast<std::uint32_t>(s));
        print_axis_sums(lattice, "AXIS_S", s);
        if (!o.state_dir.empty()) {
            char name[64];
            std::snprintf(name, sizeof name, "/s%06llu.state", static_cast<unsigned long long>(s));
            write_link_state(lattice, o.state_dir + name, o.chain, s, done);
        }
    }
    print_progress_diagnostics("AXIS_DIAGNOSTICS", lattice, done);
    std::cout << "AXIS_STATUS PASS\nEVIDENTIAL_STATUS ZERO_UNTIL_ANALYSIS\n";
    return 0;
}

// Deterministic synthetic link field for exact reduction fixtures.
int run_axis_fixture(int argc, char **argv) {
    if (argc != 3) throw std::runtime_error("usage: --axis-fixture L");
    const int L = static_cast<int>(parse_i64(argv[2], "L"));
    if (L < 2 || L > 8) throw std::runtime_error("fixture L range");
    Lattice lattice(L, 1, "cold");
    for (int site = 0; site < lattice.volume(); ++site)
        for (int mu = 0; mu < D; ++mu)
            lattice.apply_link_value_for_test(site, mu, (7 * site + 3 * mu + site / 3) % 5);
    lattice.assert_flux_consistent();
    std::cout << "AXIS_FIXTURE L=" << L << " links=";
    for (std::uint8_t v : lattice.links()) std::cout << static_cast<int>(v);
    std::cout << '\n';
    print_axis_sums(lattice, "AXIS_FIXTURE_S", 0);
    return 0;
}

}  // namespace

int main(int argc, char **argv) {
#ifdef _WIN32
    _setmode(_fileno(stdout), _O_BINARY);
    _setmode(_fileno(stderr), _O_BINARY);
#endif
    if (argc >= 2 && std::string(argv[1]) == "--axis") {
        try {
            return run_axis(argc, argv);
        } catch (const StopIntegrity &error) {
            std::cout << "AXIS_STATUS STOP_INTEGRITY\nINTEGRITY_REASON value=" << error.what() << '\n';
            return 0;
        } catch (const std::exception &error) {
            std::cerr << "ERROR: " << error.what() << '\n';
            return 2;
        }
    }
    if (argc >= 2 && std::string(argv[1]) == "--axis-fixture") {
        try {
            return run_axis_fixture(argc, argv);
        } catch (const std::exception &error) {
            std::cerr << "ERROR: " << error.what() << '\n';
            return 2;
        }
    }
    return pilot2_engine_main(argc, argv);
}
