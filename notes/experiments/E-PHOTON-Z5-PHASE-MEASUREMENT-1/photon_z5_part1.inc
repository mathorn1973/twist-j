#include <algorithm>
#include <array>
#include <cmath>
#include <complex>
#include <cstdint>
#include <iomanip>
#include <iostream>
#include <limits>
#include <queue>
#include <stdexcept>
#include <string>
#include <tuple>
#include <utility>
#include <vector>

#include <boost/multiprecision/cpp_int.hpp>

namespace {

using boost::multiprecision::int256_t;

constexpr int D = 4;
constexpr int NPAIR = 6;
constexpr std::array<std::array<int, 2>, NPAIR> PAIRS{{
    {{0, 1}}, {{0, 2}}, {{0, 3}}, {{1, 2}}, {{1, 3}}, {{2, 3}},
}};

struct PhiInt {
    std::int64_t a{0};
    std::int64_t b{0};

    friend PhiInt operator+(const PhiInt &x, const PhiInt &y) {
        return {x.a + y.a, x.b + y.b};
    }
    friend PhiInt operator*(const PhiInt &x, const PhiInt &y) {
        // phi^2=phi+1. A local product contains only six face weights.
        return {
            x.a * y.a + x.b * y.b,
            x.a * y.b + x.b * y.a + x.b * y.b,
        };
    }
    friend bool operator==(const PhiInt &x, const PhiInt &y) {
        return x.a == y.a && x.b == y.b;
    }
};

int sign_phi(const PhiInt &x) {
    // 2(a+b phi)=(2a+b)+b sqrt(5); local coefficients are below 2^15.
    const std::int64_t p = 2 * x.a + x.b;
    const std::int64_t q = x.b;
    if (p == 0 && q == 0) return 0;
    if (p >= 0 && q >= 0) return 1;
    if (p <= 0 && q <= 0) return -1;
    const std::int64_t p2 = p * p;
    const std::int64_t five_q2 = 5 * q * q;
    if (p >= 0) return p2 > five_q2 ? 1 : -1;
    return five_q2 > p2 ? 1 : -1;
}

int sign_phi_wide(const int256_t &a, const int256_t &b) {
    const int256_t p = 2 * a + b;
    const int256_t q = b;
    if (p == 0 && q == 0) return 0;
    if (p >= 0 && q >= 0) return 1;
    if (p <= 0 && q <= 0) return -1;
    const int256_t p2 = p * p;
    const int256_t five_q2 = 5 * q * q;
    if (p >= 0) return p2 > five_q2 ? 1 : -1;
    return five_q2 > p2 ? 1 : -1;
}

int pair_index(int a, int b) {
    if (a > b) std::swap(a, b);
    for (int p = 0; p < NPAIR; ++p) {
        if (PAIRS[p][0] == a && PAIRS[p][1] == b) return p;
    }
    throw std::runtime_error("invalid orientation pair");
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

class CounterRng {
  public:
    explicit CounterRng(std::uint64_t seed)
        : key_{static_cast<std::uint32_t>(seed), static_cast<std::uint32_t>(seed >> 32)} {}

    std::uint64_t u64(std::uint32_t stream, std::uint64_t counter, std::uint32_t lane = 0) const {
        const auto out = philox4x32_10(
            {
                static_cast<std::uint32_t>(counter),
                static_cast<std::uint32_t>(counter >> 32),
                stream,
                lane,
            },
            key_
        );
        return (static_cast<std::uint64_t>(out[0]) << 32) | out[1];
    }

    std::uint32_t bounded5(std::uint32_t stream, std::uint64_t counter) const {
        constexpr std::uint64_t LIMIT =
            (std::numeric_limits<std::uint64_t>::max() / 5u) * 5u;
        for (std::uint32_t lane = 0;; ++lane) {
            const std::uint64_t value = u64(stream, counter, lane);
            if (value < LIMIT) return static_cast<std::uint32_t>(value % 5u);
        }
    }

  private:
    std::array<std::uint32_t, 2> key_;
};

struct Options {
    int L = 0;
    std::uint64_t seed = 0;
    std::string start = "cold";
    int thermal_sweeps = 0;
    int measurements = 0;
    int between_sweeps = 1;
    int max_n = 0;
    bool self_test = false;
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
        else if (argument == "--L") options.L = static_cast<int>(parse_i64(need("--L"), "L"));
        else if (argument == "--t") {
            if (need("--t") != "1") throw std::runtime_error("physical pilot freezes t=1 exactly");
        }
        else if (argument == "--seed") options.seed = parse_u64(need("--seed"), "seed");
        else if (argument == "--start") options.start = need("--start");
        else if (argument == "--thermal-sweeps")
            options.thermal_sweeps = static_cast<int>(parse_i64(need("--thermal-sweeps"), "thermal-sweeps"));
        else if (argument == "--measurements")
            options.measurements = static_cast<int>(parse_i64(need("--measurements"), "measurements"));
        else if (argument == "--between-sweeps")
            options.between_sweeps = static_cast<int>(parse_i64(need("--between-sweeps"), "between-sweeps"));
        else if (argument == "--max-n")
            options.max_n = static_cast<int>(parse_i64(need("--max-n"), "max-n"));
        else throw std::runtime_error("unknown argument: " + argument);
    }
    if (options.self_test) return options;
    if (options.L < 2) throw std::runtime_error("L must be at least 2");
    if (options.start != "cold" && options.start != "hot")
        throw std::runtime_error("start must be cold or hot");
    if (options.thermal_sweeps < 0 || options.measurements <= 0 || options.between_sweeps <= 0)
        throw std::runtime_error("invalid sweep or measurement count");
    if (options.max_n <= 0) options.max_n = std::max(1, options.L / 2 - 1);
    if (options.max_n >= options.L) throw std::runtime_error("max-n must be below L");
    return options;
}

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

struct ComponentStats {
    bool wraps = false;
    int occupied = 0;
    int weighted_occupied = 0;
    int largest = 0;
    int components = 0;
};

