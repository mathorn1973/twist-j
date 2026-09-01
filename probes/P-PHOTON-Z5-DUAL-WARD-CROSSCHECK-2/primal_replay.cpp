#define main photon_z5_pilot_2_disabled_main
#include "../P-PHOTON-Z5-EXACT-HEATBATH-MIXING-PILOT-2/photon_z5.cpp"
#undef main

#include <array>
#include <cstdint>
#include <cstdlib>
#include <cctype>
#include <iomanip>
#include <map>
#include <sstream>
#include <stdexcept>
#include <string>

namespace {

struct ReplayOptions {
    bool formal{false};
    std::string pin_commit;
    std::string pin_receipt;
    int L{0};
    std::uint64_t seed{0};
    std::string start;
    std::uint32_t thermal{0};
    std::uint32_t samples{0};
    std::uint32_t between{0};
};

bool lower_hex(const std::string &text, std::size_t size) {
    if (text.size() != size) return false;
    for (const char character : text) {
        if (!((character >= '0' && character <= '9')
            || (character >= 'a' && character <= 'f'))) return false;
    }
    return true;
}

bool issue_756_receipt(const std::string &text) {
    const std::string prefix =
        "https://github.com/mathorn1973/twist-j/issues/756#issuecomment-";
    if (text.rfind(prefix, 0) != 0 || text.size() == prefix.size()) return false;
    for (std::size_t index = prefix.size(); index < text.size(); ++index)
        if (!std::isdigit(static_cast<unsigned char>(text[index]))) return false;
    return text != prefix + "5498022449";
}

std::string canonical_seed(std::uint64_t seed) {
    std::ostringstream stream;
    stream << "0x" << std::hex << std::setw(16) << std::setfill('0') << seed;
    return stream.str();
}

bool exact_formal_replay(const ReplayOptions &options, const std::string &seed_token) {
    struct Spec {
        int L;
        const char *start;
        std::uint64_t seed;
        std::uint32_t thermal;
        std::uint32_t between;
    };
    constexpr std::array<Spec, 4> specs{{
        {6, "cold", 0xe755060000000101ULL, 512, 4},
        {6, "hot", 0xe755060000000201ULL, 512, 4},
        {8, "cold", 0xe755080000000101ULL, 1024, 8},
        {8, "hot", 0xe755080000000201ULL, 1024, 8},
    }};
    for (const auto &spec : specs) {
        if (options.L == spec.L && options.start == spec.start
            && options.seed == spec.seed && seed_token == canonical_seed(spec.seed)
            && options.thermal == spec.thermal && options.samples == 512
            && options.between == spec.between) return true;
    }
    return false;
}

std::uint64_t parse_u64_replay(const std::string &text) {
    std::size_t used = 0;
    const std::uint64_t value = std::stoull(text, &used, 0);
    if (used != text.size()) throw std::runtime_error("invalid integer: " + text);
    return value;
}

ReplayOptions replay_options(int argc, char **argv) {
    ReplayOptions options;
    std::map<std::string, std::string> values;
    for (int i = 1; i < argc;) {
        const std::string key = argv[i];
        if (key == "--formal") {
            if (options.formal) throw std::runtime_error("duplicate --formal");
            options.formal = true;
            ++i;
            continue;
        }
        if (i + 1 >= argc) throw std::runtime_error("missing option value");
        if (!values.emplace(key, argv[i + 1]).second)
            throw std::runtime_error("duplicate option: " + key);
        i += 2;
    }
    const std::array<std::string, 8> required{{
        "--pin-commit", "--pin-receipt", "--L", "--seed", "--start",
        "--thermal", "--samples", "--between"
    }};
    for (const auto &key : required)
        if (!values.count(key)) throw std::runtime_error("missing option: " + key);
    if (!options.formal) throw std::runtime_error("formal replay flag required");
    if (values.size() != required.size()) throw std::runtime_error("unknown option");
    options.pin_commit = values.at("--pin-commit");
    options.pin_receipt = values.at("--pin-receipt");
    options.L = static_cast<int>(parse_u64_replay(values.at("--L")));
    options.seed = parse_u64_replay(values.at("--seed"));
    options.start = values.at("--start");
    options.thermal = static_cast<std::uint32_t>(parse_u64_replay(values.at("--thermal")));
    options.samples = static_cast<std::uint32_t>(parse_u64_replay(values.at("--samples")));
    options.between = static_cast<std::uint32_t>(parse_u64_replay(values.at("--between")));
    if (!lower_hex(options.pin_commit, 40))
        throw std::runtime_error("pin commit must be lowercase hex40");
    if (!issue_756_receipt(options.pin_receipt))
        throw std::runtime_error("pin receipt must be a non-reservation issue-756 comment");
    if (!exact_formal_replay(options, values.at("--seed")))
        throw std::runtime_error("formal replay spec rejected");
    return options;
}

int encode_replay(const std::array<int, D> &x, int L) {
    int site = 0;
    for (int mu = 0; mu < D; ++mu)
        site = site * L + ((x[mu] % L) + L) % L;
    return site;
}

int shifted_site_replay(
    const std::array<int, D> &x,
    int axis,
    int delta,
    int L
) {
    auto shifted = x;
    shifted[axis] = (shifted[axis] + delta) % L;
    if (shifted[axis] < 0) shifted[axis] += L;
    return encode_replay(shifted, L);
}

struct ReplayStats {
    long double g_mean{0};
    long double g2_mean{0};
    long double x2_mean{0};
    std::array<long double, 4> pair{};
    std::array<long double, D> rho_power{};
};

ReplayStats replay_stats(const Lattice &lattice) {
    const int L = lattice.L();
    const int V = lattice.volume();
    const auto &coords = lattice.coordinates();
    const auto &flux = lattice.flux();
    const long double sqrt5 = std::sqrt(5.0L);
    const long double kappa2 = 5.0L - 2.0L * sqrt5;
    const long double kappa = std::sqrt(kappa2);
    const std::array<long double, 5> g{{
        0.0L, 1.0L, 2.0L + sqrt5, -(2.0L + sqrt5), -1.0L
    }};
    const std::size_t face_count = static_cast<std::size_t>(V) * NPAIR;
    ReplayStats result;
    for (std::uint8_t q : flux) {
        result.g_mean += g[q];
        result.g2_mean += g[q] * g[q];
    }
    result.g_mean /= static_cast<long double>(face_count);
    result.g2_mean /= static_cast<long double>(face_count);
    result.x2_mean = kappa2 * result.g2_mean;

    for (int site = 0; site < V; ++site) {
        const auto &x = coords[site];
        for (int p = 0; p < NPAIR; ++p) {
            const int a = PAIRS[p][0];
            const int b = PAIRS[p][1];
            int c = 0;
            while (c == a || c == b) ++c;
            const long double left = g[flux[static_cast<std::size_t>(site) * NPAIR + p]];
            const std::array<std::pair<int, int>, 4> shifts{{
                {a, 1}, {c, 1}, {a, 2}, {c, 2}
            }};
            for (std::size_t family = 0; family < shifts.size(); ++family) {
                const int other = shifted_site_replay(
                    x, shifts[family].first, shifts[family].second, L
                );
                const long double right =
                    g[flux[static_cast<std::size_t>(other) * NPAIR + p]];
                result.pair[family] += left * right;
            }
        }
    }
    for (long double &value : result.pair)
        value /= static_cast<long double>(face_count);

    constexpr std::array<std::array<int, 3>, 4> triples{{
        {{0, 1, 2}}, {{0, 1, 3}}, {{0, 2, 3}}, {{1, 2, 3}}
    }};
    const long double pi = std::acos(-1.0L);
    for (int momentum_axis = 0; momentum_axis < D; ++momentum_axis) {
        long double trace = 0;
        for (const auto &triple : triples) {
            std::complex<long double> amplitude{0.0L, 0.0L};
            for (int site = 0; site < V; ++site) {
                const auto &x = coords[site];
                long double rho = 0;
                for (int position = 0; position < 3; ++position) {
                    const int axis = triple[position];
                    std::array<int, 2> face{};
                    int out = 0;
                    for (int value : triple)
                        if (value != axis) face[out++] = value;
                    const int p = pair_index(face[0], face[1]);
                    const int upper = shifted_site_replay(x, axis, 1, L);
                    const long double sign = position % 2 == 0 ? 1.0L : -1.0L;
                    const long double upper_x =
                        kappa * g[flux[static_cast<std::size_t>(upper) * NPAIR + p]];
                    const long double lower_x =
                        kappa * g[flux[static_cast<std::size_t>(site) * NPAIR + p]];
                    rho += sign * (upper_x - lower_x);
                }
                const long double angle =
                    -2.0L * pi * static_cast<long double>(x[momentum_axis]) / L;
                amplitude += std::complex<long double>{
                    rho * std::cos(angle), rho * std::sin(angle)
                };
            }
            trace += std::norm(amplitude);
        }
        result.rho_power[momentum_axis] = trace / static_cast<long double>(V);
    }
    return result;
}

void emit_replay_sample(const Lattice &lattice, std::uint32_t index) {
    const ReplayStats stats = replay_stats(lattice);
    const auto histogram = lattice.flux_histogram();
    std::cout << std::setprecision(17)
        << "SAMPLE index=" << index
        << " g_mean=" << static_cast<double>(stats.g_mean)
        << " g2_mean=" << static_cast<double>(stats.g2_mean)
        << " x2_mean=" << static_cast<double>(stats.x2_mean)
        << " pair_inline1=" << static_cast<double>(stats.pair[0])
        << " pair_transverse1=" << static_cast<double>(stats.pair[1])
        << " pair_inline2=" << static_cast<double>(stats.pair[2])
        << " pair_transverse2=" << static_cast<double>(stats.pair[3]);
    for (int axis = 0; axis < D; ++axis)
        std::cout << " rho_power_" << axis << '='
                  << static_cast<double>(stats.rho_power[axis]);
    for (int value = 0; value < 5; ++value)
        std::cout << " flux_count_" << value << '=' << histogram[value];
    std::cout << " state_hash=" << std::hex << std::setw(16) << std::setfill('0')
              << lattice.state_hash()
              << " cache_hash=" << std::setw(16) << lattice.flux_cache_hash()
              << std::dec << std::setfill(' ') << '\n';
}

void run_replay(const ReplayOptions &options) {
    Lattice lattice(options.L, options.seed, options.start);
    std::cout << "RUN model=TWIST_Z5_FACE_WEIGHT_V1"
              << " dependency=P-PHOTON-Z5-EXACT-HEATBATH-MIXING-PILOT-2"
              << " L=" << options.L
              << " seed=0x" << std::hex << std::setw(16) << std::setfill('0')
              << options.seed << std::dec << std::setfill(' ')
              << " start=" << options.start
              << " thermal_cycles=" << options.thermal
              << " measurements=" << options.samples
              << " between_cycles=" << options.between << '\n';
    std::uint32_t cycle = 0;
    while (cycle < options.thermal) KernelAccess::macro_cycle(lattice, cycle++);
    for (std::uint32_t sample = 0; sample < options.samples; ++sample) {
        for (std::uint32_t gap = 0; gap < options.between; ++gap)
            KernelAccess::macro_cycle(lattice, cycle++);
        lattice.assert_flux_consistent();
        emit_replay_sample(lattice, sample);
    }
    const auto &diagnostics = lattice.diagnostics();
    std::uint64_t stops = 0;
    std::uint32_t max_bits = 0;
    for (const auto &entry : diagnostics.sampler) {
        stops += entry.stops;
        max_bits = std::max(max_bits, entry.max_bits);
    }
    std::cout << "SUMMARY macro_cycles=" << diagnostics.macro_cycles
              << " cap_exhaustions=" << stops
              << " max_prefix_bits=" << max_bits
              << " state_hash=" << std::hex << std::setw(16) << std::setfill('0')
              << lattice.state_hash() << std::dec << std::setfill(' ')
              << " status=" << (stops == 0 ? "PASS" : "STOP_INTEGRITY") << '\n';
}

}  // namespace

int main(int argc, char **argv) {
#ifdef _WIN32
    _setmode(_fileno(stdout), _O_BINARY);
    _setmode(_fileno(stderr), _O_BINARY);
#endif
    try {
        run_replay(replay_options(argc, argv));
        return 0;
    } catch (const std::exception &error) {
        std::cerr << "ERROR: " << error.what() << '\n';
        return 2;
    }
}
