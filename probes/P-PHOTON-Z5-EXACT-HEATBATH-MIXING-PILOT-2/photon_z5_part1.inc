#include <algorithm>
#include <array>
#include <cctype>
#include <cmath>
#include <complex>
#include <cstdint>
#include <iomanip>
#include <iostream>
#include <limits>
#include <sstream>
#include <stdexcept>
#include <string>
#include <tuple>
#include <utility>
#include <vector>

#include <boost/multiprecision/cpp_int.hpp>

#ifdef _WIN32
#include <fcntl.h>
#include <io.h>
#endif

namespace {

using boost::multiprecision::cpp_int;

constexpr int D = 4;
constexpr int NPAIR = 6;
constexpr std::uint32_t CATEGORICAL_CAP = 256;
constexpr std::array<std::array<int, 2>, NPAIR> PAIRS{{
    {{0, 1}}, {{0, 2}}, {{0, 3}}, {{1, 2}}, {{1, 3}}, {{2, 3}},
}};

int mod5(int value) {
    value %= 5;
    if (value < 0) value += 5;
    return value;
}

int principal5(int value) {
    value = mod5(value);
    if (value >= 3) value -= 5;
    return value;
}

class StopIntegrity : public std::runtime_error {
  public:
    explicit StopIntegrity(const std::string &message) : std::runtime_error(message) {}
};

int pair_index(int a, int b) {
    if (a > b) std::swap(a, b);
    for (int p = 0; p < NPAIR; ++p) {
        if (PAIRS[p][0] == a && PAIRS[p][1] == b) return p;
    }
    throw StopIntegrity("STOP_INTEGRITY invalid_orientation_pair");
}

struct QPhi {
    cpp_int a{0};
    cpp_int b{0};

    QPhi() = default;
    QPhi(long long aa, long long bb = 0) : a(aa), b(bb) {}
    QPhi(cpp_int aa, cpp_int bb) : a(std::move(aa)), b(std::move(bb)) {}

    friend QPhi operator+(const QPhi &x, const QPhi &y) {
        return {x.a + y.a, x.b + y.b};
    }
    friend QPhi operator-(const QPhi &x, const QPhi &y) {
        return {x.a - y.a, x.b - y.b};
    }
    friend QPhi operator*(const QPhi &x, const QPhi &y) {
        // phi^2 = phi + 1.
        return {
            x.a * y.a + x.b * y.b,
            x.a * y.b + x.b * y.a + x.b * y.b,
        };
    }
    friend QPhi operator*(const QPhi &x, const cpp_int &n) {
        return {x.a * n, x.b * n};
    }
    friend QPhi operator*(const cpp_int &n, const QPhi &x) { return x * n; }
    friend bool operator==(const QPhi &x, const QPhi &y) {
        return x.a == y.a && x.b == y.b;
    }
};

int sign_qphi(const QPhi &x) {
    // 2(a+b phi) = (2a+b) + b sqrt(5).  Integer squares make this exact.
    const cpp_int p = 2 * x.a + x.b;
    const cpp_int q = x.b;
    if (p == 0 && q == 0) return 0;
    if (p >= 0 && q >= 0) return 1;
    if (p <= 0 && q <= 0) return -1;
    const cpp_int p2 = p * p;
    const cpp_int five_q2 = 5 * q * q;
    if (p >= 0) return p2 > five_q2 ? 1 : -1;
    return five_q2 > p2 ? 1 : -1;
}

const std::array<QPhi, 5> &face_weights() {
    static const std::array<QPhi, 5> weights{{
        {4, 0}, {1, 1}, {2, -1}, {2, -1}, {1, 1},
    }};
    return weights;
}

const std::array<std::array<QPhi, 5>, 15625> &local_mass_table() {
    // The exact PR #760 local kernel has only 5^6 residual environments.
    // Residual digits 0..2 have + incidence and digits 3..5 have - incidence.
    static const auto table = [] {
        std::array<std::array<QPhi, 5>, 15625> result{};
        for (int key = 0; key < 15625; ++key) {
            int cursor = key;
            std::array<int, 6> residual{};
            for (int digit = 5; digit >= 0; --digit) {
                residual[digit] = cursor % 5;
                cursor /= 5;
            }
            for (int candidate = 0; candidate < 5; ++candidate) {
                QPhi mass{1, 0};
                for (int digit = 0; digit < 3; ++digit)
                    mass = mass * face_weights()[mod5(residual[digit] + candidate)];
                for (int digit = 3; digit < 6; ++digit)
                    mass = mass * face_weights()[mod5(residual[digit] - candidate)];
                if (sign_qphi(mass) <= 0)
                    throw StopIntegrity("STOP_INTEGRITY nonpositive_precomputed_local_mass");
                result[key][candidate] = std::move(mass);
            }
        }
        return result;
    }();
    return table;
}

std::uint32_t mul_hi(std::uint32_t a, std::uint32_t b, std::uint32_t &lo) {
    const std::uint64_t product = static_cast<std::uint64_t>(a) * b;
    lo = static_cast<std::uint32_t>(product);
    return static_cast<std::uint32_t>(product >> 32);
}

std::array<std::uint32_t, 4> philox4x32_10(
    std::array<std::uint32_t, 4> counter,
    std::array<std::uint32_t, 2> key
) {
    constexpr std::uint32_t M0 = 0xD2511F53u;
    constexpr std::uint32_t M1 = 0xCD9E8D57u;
    constexpr std::uint32_t W0 = 0x9E3779B9u;
    constexpr std::uint32_t W1 = 0xBB67AE85u;
    for (int round = 0; round < 10; ++round) {
        std::uint32_t lo0 = 0, lo1 = 0;
        const std::uint32_t hi0 = mul_hi(M0, counter[0], lo0);
        const std::uint32_t hi1 = mul_hi(M1, counter[2], lo1);
        counter = {
            static_cast<std::uint32_t>(hi1 ^ counter[1] ^ key[0]),
            lo1,
            static_cast<std::uint32_t>(hi0 ^ counter[3] ^ key[1]),
            lo0,
        };
        if (round != 9) {
            key[0] += W0;
            key[1] += W1;
        }
    }
    return counter;
}

enum class RandomKind : std::uint32_t { HOT = 0, LOCAL = 1, LINE = 2, FLAT = 3, CHARGE = 4 };
constexpr std::size_t RANDOM_KIND_COUNT = 5;
constexpr std::array<std::uint32_t, RANDOM_KIND_COUNT> RANDOM_DOMAINS{{
    0x484f5401u,  // HOT\x01
    0x4c4f4302u,  // LOC\x02
    0x4c494e03u,  // LIN\x03
    0x464c5404u,  // FLT\x04
    0x43484705u,  // CHG\x05
}};

std::size_t kind_slot(RandomKind kind) { return static_cast<std::size_t>(kind); }

const char *kind_name(RandomKind kind) {
    switch (kind) {
        case RandomKind::HOT: return "HOT";
        case RandomKind::LOCAL: return "LOCAL";
        case RandomKind::LINE: return "LINE";
        case RandomKind::FLAT: return "FLAT";
        case RandomKind::CHARGE: return "CHARGE";
    }
    throw StopIntegrity("STOP_INTEGRITY invalid_random_kind");
}

class CounterRng {
  public:
    explicit CounterRng(std::uint64_t seed)
        : key_{static_cast<std::uint32_t>(seed), static_cast<std::uint32_t>(seed >> 32)} {}

    std::array<std::uint32_t, 4> block(
        RandomKind kind,
        std::uint32_t cycle,
        std::uint32_t ordinal,
        std::uint32_t block_index
    ) const {
        // Frozen injective namespace inside the preregistered uint32 ranges:
        // counter=(cycle, ordinal, kind-domain, 64-bit-block), key=seed.
        return philox4x32_10(
            {cycle, ordinal, RANDOM_DOMAINS[kind_slot(kind)], block_index}, key_
        );
    }

    std::uint64_t u64(
        RandomKind kind,
        std::uint32_t cycle,
        std::uint32_t ordinal,
        std::uint32_t block_index
    ) const {
        const auto words = block(kind, cycle, ordinal, block_index);
        return (static_cast<std::uint64_t>(words[0]) << 32) | words[1];
    }

  private:
    std::array<std::uint32_t, 2> key_;
};

template <class Rng>
std::uint32_t exact_uniform5(
    const Rng &rng,
    RandomKind kind,
    std::uint32_t cycle,
    std::uint32_t ordinal,
    std::uint64_t &rejections
) {
    // 2^64-1 is divisible by five.  Reject only UINT64_MAX, then reduce the
    // remaining exactly equal residue classes.  A rejection advances only
    // this decision's namespaced block counter.
    constexpr std::uint64_t limit = std::numeric_limits<std::uint64_t>::max();
    for (std::uint32_t block = 0;; ++block) {
        const std::uint64_t value = rng.u64(kind, cycle, ordinal, block);
        if (value < limit) return static_cast<std::uint32_t>(value % 5u);
        ++rejections;
        if (block == std::numeric_limits<std::uint32_t>::max())
            throw StopIntegrity("STOP_INTEGRITY uniform5_counter_exhausted");
    }
}

class CounterBits {
  public:
    CounterBits(
        const CounterRng &rng,
        RandomKind kind,
        std::uint32_t cycle,
        std::uint32_t ordinal
    ) : rng_(rng), kind_(kind), cycle_(cycle), ordinal_(ordinal) {}

    int next() {
        const std::uint32_t block_index = used_ / 64u;
        if (!loaded_ || block_index != loaded_block_) {
            cache_ = rng_.block(kind_, cycle_, ordinal_, block_index);
            loaded_ = true;
            loaded_block_ = block_index;
        }
        const std::uint32_t offset = used_ % 64u;
        const std::uint32_t word = offset / 32u;
        const std::uint32_t shift = 31u - offset % 32u;
        ++used_;
        return static_cast<int>((cache_[word] >> shift) & 1u);
    }

    std::string label() const {
        std::ostringstream out;
        out << "kind=" << kind_name(kind_) << " cycle=" << cycle_ << " ordinal=" << ordinal_;
        return out.str();
    }

  private:
    const CounterRng &rng_;
    RandomKind kind_;
    std::uint32_t cycle_;
    std::uint32_t ordinal_;
    std::uint32_t used_{0};
    bool loaded_{false};
    std::uint32_t loaded_block_{0};
    std::array<std::uint32_t, 4> cache_{};
};

struct SamplerStats {
    std::uint64_t attempts{0};
    std::uint64_t completed{0};
    std::uint64_t total_bits{0};
    std::uint64_t over32{0};
    std::uint64_t over64{0};
    std::uint64_t over128{0};
    std::uint64_t stops{0};
    std::uint32_t max_bits{0};

    void record(std::uint32_t bits) {
        ++completed;
        total_bits += bits;
        max_bits = std::max(max_bits, bits);
        if (bits > 32) ++over32;
        if (bits > 64) ++over64;
        if (bits > 128) ++over128;
    }
};

template <std::size_t N, class BitSource>
int exact_category(
    const std::array<QPhi, N> &weights,
    BitSource &bits,
    SamplerStats &stats,
    std::uint32_t cap = CATEGORICAL_CAP
) {
    static_assert(N > 0, "categorical distribution must not be empty");
    if (cap == 0) throw StopIntegrity("STOP_INTEGRITY zero_categorical_cap");
    ++stats.attempts;
    std::array<QPhi, N + 1> cumulative{};
    for (std::size_t i = 0; i < N; ++i) {
        cumulative[i + 1] = cumulative[i] + weights[i];
    }
    const QPhi total = cumulative.back();
    cpp_int prefix = 0;
    if (cap % 64u != 0)
        throw StopIntegrity("STOP_INTEGRITY categorical_cap_not_multiple_of_64");
    for (std::uint32_t n = 64; n <= cap; n += 64) {
        for (int bit = 0; bit < 64; ++bit) {
            prefix <<= 1;
            prefix += bits.next();
        }
        const cpp_int scale = cpp_int(1) << n;
        for (std::size_t category = 0; category < N; ++category) {
            // [prefix/2^n,(prefix+1)/2^n] lies inside the category interval.
            const QPhi lower = total * prefix - cumulative[category] * scale;
            const QPhi upper = cumulative[category + 1] * scale - total * (prefix + 1);
            if (sign_qphi(lower) >= 0 && sign_qphi(upper) >= 0) {
                stats.record(n);
                return static_cast<int>(category);
            }
        }
    }
    ++stats.stops;
    throw StopIntegrity(
        "STOP_INTEGRITY categorical_cap_exhausted cap=" + std::to_string(cap) + " " + bits.label()
    );
}

template <std::size_t N>
std::array<QPhi, N> equal_masses() {
    std::array<QPhi, N> result{};
    for (QPhi &mass : result) mass = QPhi{1, 0};
    return result;
}

struct KernelDiagnostics {
    std::array<SamplerStats, RANDOM_KIND_COUNT> sampler{};
    std::array<std::uint64_t, RANDOM_KIND_COUNT> uniform_rejections{};
    std::uint64_t macro_cycles{0};
    std::uint64_t local_forward_sweeps{0};
    std::uint64_t local_reverse_sweeps{0};
    std::uint64_t local_updates{0};
    std::uint64_t local_changes{0};
    std::uint64_t line_forward_sweeps{0};
    std::uint64_t line_reverse_sweeps{0};
    std::uint64_t line_updates{0};
    std::uint64_t line_changes{0};
    std::array<std::uint64_t, D> line_changes_by_direction{};
    std::uint64_t flat_trials{0};
    std::uint64_t flat_nonzero{0};
    std::uint64_t flat_flux_identity_checks{0};
    std::uint64_t charge_trials{0};
    std::uint64_t charge_applied{0};
    std::uint64_t charge_flux_identity_checks{0};
};

struct Options {
    bool self_test{false};
    bool fixture{false};
    bool stop_integrity_fixture{false};
    bool kernel_run{false};
    bool pilot{false};
    int L{0};
    bool L_set{false};
    std::uint64_t seed{0};
    bool seed_set{false};
    std::string start{"cold"};
    bool start_set{false};
    std::uint32_t macro_cycles{0};
    bool macro_cycles_set{false};
    int replica{0};
    bool replica_set{false};
    std::uint32_t thermal_cycles{0};
    bool thermal_cycles_set{false};
    std::uint32_t measurements{0};
    bool measurements_set{false};
    std::uint32_t between_cycles{0};
    bool between_cycles_set{false};
    bool t_set{false};
};

long long parse_i64(const std::string &value, const char *name) {
    std::size_t position = 0;
    long long result = 0;
    try {
        result = std::stoll(value, &position, 0);
    } catch (...) {
        throw std::runtime_error(std::string("invalid ") + name + ": " + value);
    }
    if (position != value.size())
        throw std::runtime_error(std::string("invalid ") + name + ": " + value);
    return result;
}

std::uint64_t parse_u64(const std::string &value, const char *name) {
    std::size_t position = 0;
    unsigned long long result = 0;
    try {
        result = std::stoull(value, &position, 0);
    } catch (...) {
        throw std::runtime_error(std::string("invalid ") + name + ": " + value);
    }
    if (position != value.size())
        throw std::runtime_error(std::string("invalid ") + name + ": " + value);
    return static_cast<std::uint64_t>(result);
}

Options parse_options(int argc, char **argv) {
    Options options;
    for (int i = 1; i < argc; ++i) {
        const std::string argument = argv[i];
        auto need = [&](const char *name) -> std::string {
            if (++i >= argc) throw std::runtime_error(std::string("missing value for ") + name);
            return argv[i];
        };
        if (argument == "--self-test") options.self_test = true;
        else if (argument == "--fixture") options.fixture = true;
        else if (argument == "--stop-integrity-fixture") options.stop_integrity_fixture = true;
        else if (argument == "--kernel-run") options.kernel_run = true;
        else if (argument == "--pilot") options.pilot = true;
        else if (argument == "--L") {
            options.L_set = true;
            options.L = static_cast<int>(parse_i64(need("--L"), "L"));
        } else if (argument == "--seed") {
            options.seed_set = true;
            options.seed = parse_u64(need("--seed"), "seed");
        } else if (argument == "--start") {
            options.start_set = true;
            options.start = need("--start");
        } else if (argument == "--replica") {
            options.replica_set = true;
            options.replica = static_cast<int>(parse_i64(need("--replica"), "replica"));
        } else if (argument == "--macro-cycles") {
            options.macro_cycles_set = true;
            const long long value = parse_i64(need("--macro-cycles"), "macro-cycles");
            if (value < 0 || value > std::numeric_limits<std::uint32_t>::max())
                throw std::runtime_error("macro-cycles outside uint32 range");
            options.macro_cycles = static_cast<std::uint32_t>(value);
        } else if (argument == "--thermal-cycles") {
            options.thermal_cycles_set = true;
            const long long value = parse_i64(need("--thermal-cycles"), "thermal-cycles");
            if (value < 0 || value > std::numeric_limits<std::uint32_t>::max())
                throw std::runtime_error("thermal-cycles outside uint32 range");
            options.thermal_cycles = static_cast<std::uint32_t>(value);
        } else if (argument == "--measurements") {
            options.measurements_set = true;
            const long long value = parse_i64(need("--measurements"), "measurements");
            if (value < 0 || value > std::numeric_limits<std::uint32_t>::max())
                throw std::runtime_error("measurements outside uint32 range");
            options.measurements = static_cast<std::uint32_t>(value);
        } else if (argument == "--between-cycles") {
            options.between_cycles_set = true;
            const long long value = parse_i64(need("--between-cycles"), "between-cycles");
            if (value < 0 || value > std::numeric_limits<std::uint32_t>::max())
                throw std::runtime_error("between-cycles outside uint32 range");
            options.between_cycles = static_cast<std::uint32_t>(value);
        } else if (argument == "--t") {
            options.t_set = true;
            if (need("--t") != "1") throw std::runtime_error("kernel freezes t=1 exactly");
        } else {
            throw std::runtime_error("unknown argument: " + argument);
        }
    }
    const int modes = static_cast<int>(options.self_test)
        + static_cast<int>(options.fixture) + static_cast<int>(options.stop_integrity_fixture)
        + static_cast<int>(options.kernel_run)
        + static_cast<int>(options.pilot);
    if (modes != 1)
        throw std::runtime_error(
            "select exactly one of --self-test, --fixture, --stop-integrity-fixture, --kernel-run and --pilot"
        );
    const bool any_run_option = options.L_set || options.seed_set || options.start_set
        || options.macro_cycles_set || options.replica_set || options.thermal_cycles_set
        || options.measurements_set || options.between_cycles_set || options.t_set;
    if (options.self_test || options.fixture || options.stop_integrity_fixture) {
        if (any_run_option)
            throw std::runtime_error("selected fixture mode does not accept run options");
        return options;
    }
    if (options.kernel_run) {
        if (options.replica_set || options.thermal_cycles_set || options.measurements_set
            || options.between_cycles_set)
            throw std::runtime_error("--kernel-run does not accept pilot schedule options");
        if (!options.L_set || !options.seed_set || !options.start_set || !options.macro_cycles_set)
            throw std::runtime_error("--kernel-run requires L, seed, start and macro-cycles");
    } else {
        if (!options.L_set || !options.seed_set || !options.start_set || !options.replica_set
            || !options.thermal_cycles_set || !options.measurements_set
            || !options.between_cycles_set || !options.t_set)
            throw std::runtime_error("--pilot requires every frozen run option");
    }
    if (options.L < 2 || options.L > 16) throw std::runtime_error("L must be in [2,16]");
    if (options.start != "cold" && options.start != "hot")
        throw std::runtime_error("start must be cold or hot");
    if (options.kernel_run) return options;

    if (options.L != 6 && options.L != 8) throw std::runtime_error("pilot L must be 6 or 8");
    if (options.macro_cycles_set)
        throw std::runtime_error("--macro-cycles is not valid in --pilot mode");
    if (options.replica != 1 && options.replica != 2) throw std::runtime_error("pilot replica must be 1 or 2");
    const std::uint32_t frozen_thermal = options.L == 6 ? 512u : 1024u;
    const std::uint32_t frozen_between = options.L == 6 ? 4u : 8u;
    if (options.thermal_cycles != frozen_thermal || options.measurements != 512u
        || options.between_cycles != frozen_between)
        throw std::runtime_error("pilot schedule differs from frozen schedule");
    const std::uint64_t base = options.L == 6
        ? 0xE755060000000000ULL : 0xE755080000000000ULL;
    const std::uint64_t start_code = options.start == "cold" ? 0x100ULL : 0x200ULL;
    const std::uint64_t expected_seed = base + start_code + static_cast<std::uint64_t>(options.replica);
    if (options.seed != expected_seed) throw std::runtime_error("pilot seed differs from frozen seed");
    return options;
}
