// orbit_qualification.cpp
//
// Source-only qualification of the exact orbit heat-bath sampler used by the
// photon Z_5 dual engine.  This is deliberately not a Ward run: it contains
// no formal CROSSCHECK-2 seed, lattice state, residual, or decision chain.
//
// The legacy sampler represents the relative masses 2^(e_i-min(e)) in
// uint64_t and refuses a shift >= 63 or a sum overflow.  The qualified
// sampler keeps that byte-for-byte RNG path whenever the legacy table is
// representable, and otherwise uses boost::multiprecision::cpp_int for both
// the powers of two and unbiased bounded rejection.

#include <algorithm>
#include <array>
#include <cstdint>
#include <cstring>
#include <iostream>
#include <limits>
#include <locale>
#include <stdexcept>
#include <string>
#include <string_view>
#include <utility>
#include <vector>

#include <boost/multiprecision/cpp_int.hpp>

#ifdef _WIN32
#include <fcntl.h>
#include <io.h>
#endif

namespace orbit_qualification {

using boost::multiprecision::cpp_int;

class IntegrityError : public std::runtime_error {
  public:
    explicit IntegrityError(const std::string &message) : std::runtime_error(message) {}
};

void require(bool condition, const char *message) {
    if (!condition) throw IntegrityError(message);
}

constexpr std::string_view BITSTREAM_DOMAIN =
    "photon-z5-dual-mobility-qualification-1";

class Sha256 {
  public:
    Sha256() { reset(); }

    void update(const std::uint8_t *data, std::size_t size) {
        total_bytes_ += size;
        while (size != 0) {
            const std::size_t take = std::min(size, block_.size() - used_);
            std::memcpy(block_.data() + used_, data, take);
            used_ += take;
            data += take;
            size -= take;
            if (used_ == block_.size()) {
                transform(block_.data());
                used_ = 0;
            }
        }
    }

    void update(std::string_view text) {
        update(reinterpret_cast<const std::uint8_t *>(text.data()), text.size());
    }

    std::array<std::uint8_t, 32> final() const {
        Sha256 copy = *this;
        const std::uint64_t bit_length = copy.total_bytes_ * 8ULL;
        std::array<std::uint8_t, 64> padding{};
        padding[0] = 0x80;
        const std::size_t padding_size = copy.used_ < 56
            ? 56 - copy.used_ : 120 - copy.used_;
        copy.update(padding.data(), padding_size);
        std::array<std::uint8_t, 8> length_bytes{};
        for (int index = 0; index < 8; ++index) {
            length_bytes[7 - index] = static_cast<std::uint8_t>(
                bit_length >> (8 * index)
            );
        }
        copy.update(length_bytes.data(), length_bytes.size());
        if (copy.used_ != 0) throw IntegrityError("sha256_finalization_failure");
        std::array<std::uint8_t, 32> result{};
        for (int word = 0; word < 8; ++word) {
            for (int byte = 0; byte < 4; ++byte) {
                result[4 * word + byte] = static_cast<std::uint8_t>(
                    copy.state_[word] >> (24 - 8 * byte)
                );
            }
        }
        return result;
    }

  private:
    static constexpr std::array<std::uint32_t, 64> K{{
        0x428a2f98u, 0x71374491u, 0xb5c0fbcfu, 0xe9b5dba5u,
        0x3956c25bu, 0x59f111f1u, 0x923f82a4u, 0xab1c5ed5u,
        0xd807aa98u, 0x12835b01u, 0x243185beu, 0x550c7dc3u,
        0x72be5d74u, 0x80deb1feu, 0x9bdc06a7u, 0xc19bf174u,
        0xe49b69c1u, 0xefbe4786u, 0x0fc19dc6u, 0x240ca1ccu,
        0x2de92c6fu, 0x4a7484aau, 0x5cb0a9dcu, 0x76f988dau,
        0x983e5152u, 0xa831c66du, 0xb00327c8u, 0xbf597fc7u,
        0xc6e00bf3u, 0xd5a79147u, 0x06ca6351u, 0x14292967u,
        0x27b70a85u, 0x2e1b2138u, 0x4d2c6dfcu, 0x53380d13u,
        0x650a7354u, 0x766a0abbu, 0x81c2c92eu, 0x92722c85u,
        0xa2bfe8a1u, 0xa81a664bu, 0xc24b8b70u, 0xc76c51a3u,
        0xd192e819u, 0xd6990624u, 0xf40e3585u, 0x106aa070u,
        0x19a4c116u, 0x1e376c08u, 0x2748774cu, 0x34b0bcb5u,
        0x391c0cb3u, 0x4ed8aa4au, 0x5b9cca4fu, 0x682e6ff3u,
        0x748f82eeu, 0x78a5636fu, 0x84c87814u, 0x8cc70208u,
        0x90befffau, 0xa4506cebu, 0xbef9a3f7u, 0xc67178f2u,
    }};

    static std::uint32_t rotate_right(std::uint32_t value, int count) {
        return (value >> count) | (value << (32 - count));
    }

    void reset() {
        state_ = {{
            0x6a09e667u, 0xbb67ae85u, 0x3c6ef372u, 0xa54ff53au,
            0x510e527fu, 0x9b05688cu, 0x1f83d9abu, 0x5be0cd19u,
        }};
        block_.fill(0);
        used_ = 0;
        total_bytes_ = 0;
    }

    void transform(const std::uint8_t *block) {
        std::array<std::uint32_t, 64> words{};
        for (int index = 0; index < 16; ++index) {
            words[index] =
                (static_cast<std::uint32_t>(block[4 * index]) << 24)
                | (static_cast<std::uint32_t>(block[4 * index + 1]) << 16)
                | (static_cast<std::uint32_t>(block[4 * index + 2]) << 8)
                | static_cast<std::uint32_t>(block[4 * index + 3]);
        }
        for (int index = 16; index < 64; ++index) {
            const std::uint32_t s0 = rotate_right(words[index - 15], 7)
                ^ rotate_right(words[index - 15], 18)
                ^ (words[index - 15] >> 3);
            const std::uint32_t s1 = rotate_right(words[index - 2], 17)
                ^ rotate_right(words[index - 2], 19)
                ^ (words[index - 2] >> 10);
            words[index] = words[index - 16] + s0 + words[index - 7] + s1;
        }
        std::uint32_t a = state_[0];
        std::uint32_t b = state_[1];
        std::uint32_t c = state_[2];
        std::uint32_t d = state_[3];
        std::uint32_t e = state_[4];
        std::uint32_t f = state_[5];
        std::uint32_t g = state_[6];
        std::uint32_t h = state_[7];
        for (int index = 0; index < 64; ++index) {
            const std::uint32_t sum1 = rotate_right(e, 6)
                ^ rotate_right(e, 11) ^ rotate_right(e, 25);
            const std::uint32_t choose = (e & f) ^ ((~e) & g);
            const std::uint32_t temp1 = h + sum1 + choose + K[index] + words[index];
            const std::uint32_t sum0 = rotate_right(a, 2)
                ^ rotate_right(a, 13) ^ rotate_right(a, 22);
            const std::uint32_t majority = (a & b) ^ (a & c) ^ (b & c);
            const std::uint32_t temp2 = sum0 + majority;
            h = g;
            g = f;
            f = e;
            e = d + temp1;
            d = c;
            c = b;
            b = a;
            a = temp1 + temp2;
        }
        state_[0] += a;
        state_[1] += b;
        state_[2] += c;
        state_[3] += d;
        state_[4] += e;
        state_[5] += f;
        state_[6] += g;
        state_[7] += h;
    }

    std::array<std::uint32_t, 8> state_{};
    std::array<std::uint8_t, 64> block_{};
    std::size_t used_{0};
    std::uint64_t total_bytes_{0};
};

std::string hex_digest(const std::array<std::uint8_t, 32> &digest) {
    static constexpr char HEX[] = "0123456789abcdef";
    std::string result(64, '0');
    for (std::size_t index = 0; index < digest.size(); ++index) {
        result[2 * index] = HEX[digest[index] >> 4];
        result[2 * index + 1] = HEX[digest[index] & 15];
    }
    return result;
}

struct Seed128 {
    std::array<std::uint8_t, 16> bytes{};
};

Seed128 sequential_seed() {
    Seed128 result;
    for (std::size_t index = 0; index < result.bytes.size(); ++index) {
        result.bytes[index] = static_cast<std::uint8_t>(index);
    }
    return result;
}

Seed128 property_seed(std::uint32_t serial) {
    Seed128 result;
    for (std::size_t index = 0; index < result.bytes.size(); ++index) {
        const std::uint32_t mixed = serial * 0x9e3779b9u
            + static_cast<std::uint32_t>(index) * 0x45d9f3bu
            + 0xa5u;
        result.bytes[index] = static_cast<std::uint8_t>(
            mixed >> (8 * (index % 4))
        );
    }
    return result;
}

class BitStream {
  public:
    explicit BitStream(
        Seed128 seed,
        std::string domain = std::string(BITSTREAM_DOMAIN)
    ) : seed_(seed), domain_(std::move(domain)) {
        counter_.fill(0);
    }

    int bit() {
        if (bit_position_ == 256) refill();
        const int result =
            (digest_[bit_position_ / 8] >> (7 - (bit_position_ % 8))) & 1;
        ++bit_position_;
        ++bits_read_;
        return result;
    }

    std::uint64_t bits_u64(unsigned count) {
        if (count > 63) throw IntegrityError("bitstream_bits_width_exceeds_63");
        std::uint64_t value = 0;
        for (unsigned index = 0; index < count; ++index) {
            value = (value << 1) | static_cast<unsigned>(bit());
        }
        return value;
    }

    std::uint64_t bounded_u64(std::uint64_t bound) {
        if (bound == 0) throw IntegrityError("bitstream_zero_bound");
        unsigned width = 0;
        for (std::uint64_t value = bound - 1; value != 0; value >>= 1) ++width;
        while (true) {
            const std::uint64_t value = bits_u64(width);
            if (value < bound) return value;
        }
    }

    cpp_int bits_big(std::size_t count) {
        cpp_int value = 0;
        for (std::size_t index = 0; index < count; ++index) {
            value <<= 1;
            value += bit();
        }
        return value;
    }

    cpp_int bounded_big(const cpp_int &bound) {
        if (bound <= 0) throw IntegrityError("bitstream_nonpositive_big_bound");
        const cpp_int top = bound - 1;
        const std::size_t width = top == 0
            ? 0 : static_cast<std::size_t>(boost::multiprecision::msb(top)) + 1;
        while (true) {
            const cpp_int value = bits_big(width);
            if (value < bound) return value;
        }
    }

    std::uint64_t bits_read() const { return bits_read_; }

    static std::array<std::uint8_t, 32> counter_digest(
        const Seed128 &seed,
        std::string_view domain,
        const std::array<std::uint8_t, 16> &counter
    ) {
        Sha256 hash;
        hash.update(domain);
        hash.update(seed.bytes.data(), seed.bytes.size());
        hash.update(counter.data(), counter.size());
        return hash.final();
    }

  private:
    void refill() {
        digest_ = counter_digest(seed_, domain_, counter_);
        bool carry = true;
        for (int index = 15; index >= 0 && carry; --index) {
            const std::uint8_t old = counter_[index];
            counter_[index] = static_cast<std::uint8_t>(old + 1);
            carry = old == 0xff;
        }
        if (carry) throw IntegrityError("bitstream_counter_overflow");
        bit_position_ = 0;
    }

    Seed128 seed_{};
    std::string domain_;
    std::array<std::uint8_t, 16> counter_{};
    std::array<std::uint8_t, 32> digest_{};
    int bit_position_{256};
    std::uint64_t bits_read_{0};
};

struct WeightTable {
    std::vector<long long> exponents;
    long long minimum{0};
    long long maximum{0};
    unsigned long long span{0};
    std::vector<cpp_int> weights;
    cpp_int total{0};
    bool legacy_representable{false};
};

WeightTable make_weight_table(const std::vector<long long> &exponents) {
    if (exponents.empty()) throw IntegrityError("orbit_has_no_candidates");
    const auto bounds = std::minmax_element(exponents.begin(), exponents.end());
    WeightTable table;
    table.exponents = exponents;
    table.minimum = *bounds.first;
    table.maximum = *bounds.second;
    const cpp_int span_big = cpp_int(table.maximum) - cpp_int(table.minimum);
    if (span_big < 0 || span_big > std::numeric_limits<unsigned long long>::max()) {
        throw IntegrityError("orbit_exponent_span_out_of_range");
    }
    table.span = span_big.convert_to<unsigned long long>();
    table.weights.reserve(exponents.size());
    for (const long long exponent : exponents) {
        const cpp_int shift_big = cpp_int(exponent) - cpp_int(table.minimum);
        if (shift_big < 0 || shift_big > std::numeric_limits<unsigned long long>::max()) {
            throw IntegrityError("orbit_exponent_shift_out_of_range");
        }
        const auto shift = shift_big.convert_to<unsigned long long>();
        cpp_int weight = 1;
        weight <<= shift;
        table.weights.push_back(weight);
        table.total += weight;
    }
    // The old bounded sampler can assemble at most 63 bits.  A uint64 total
    // alone is therefore insufficient: total=2^63+1 would request width 64.
    const cpp_int legacy_total_limit = cpp_int(1) << 63;
    table.legacy_representable = table.span < 63
        && table.total <= std::numeric_limits<std::uint64_t>::max()
        && table.total <= legacy_total_limit;
    return table;
}

std::size_t choose_from_draw(const WeightTable &table, const cpp_int &draw) {
    if (draw < 0 || draw >= table.total) throw IntegrityError("draw_out_of_range");
    cpp_int cumulative = 0;
    for (std::size_t index = 0; index < table.weights.size(); ++index) {
        cumulative += table.weights[index];
        if (draw < cumulative) return index;
    }
    throw IntegrityError("orbit_selection_fell_through");
}

struct SampleResult {
    std::size_t choice{0};
    cpp_int draw{0};
    std::uint64_t bits{0};
    std::string path;
};

SampleResult legacy_sample(
    const std::vector<long long> &exponents,
    BitStream &stream
) {
    if (exponents.empty()) throw IntegrityError("orbit_has_no_candidates");
    const long long minimum = *std::min_element(exponents.begin(), exponents.end());
    std::vector<std::uint64_t> weights;
    weights.reserve(exponents.size());
    std::uint64_t total = 0;
    for (const long long exponent : exponents) {
        const cpp_int shift_big = cpp_int(exponent) - cpp_int(minimum);
        if (shift_big < 0 || shift_big >= 63) {
            throw IntegrityError("orbit_integer_weight_overflow");
        }
        const unsigned shift = shift_big.convert_to<unsigned>();
        const std::uint64_t weight = std::uint64_t{1} << shift;
        if (total > std::numeric_limits<std::uint64_t>::max() - weight) {
            throw IntegrityError("orbit_weight_sum_overflow");
        }
        total += weight;
        weights.push_back(weight);
    }
    const std::uint64_t before = stream.bits_read();
    const std::uint64_t draw = stream.bounded_u64(total);
    std::uint64_t cumulative = 0;
    for (std::size_t index = 0; index < weights.size(); ++index) {
        cumulative += weights[index];
        if (draw < cumulative) {
            return {index, cpp_int(draw), stream.bits_read() - before, "legacy-u64"};
        }
    }
    throw IntegrityError("legacy_orbit_selection_fell_through");
}

SampleResult exact_sample(const WeightTable &table, BitStream &stream) {
    if (table.legacy_representable) {
        // Preserve the complete old path, including uint64 accumulation,
        // bounded draw, cumulative selection, and every consumed RNG bit.
        return legacy_sample(table.exponents, stream);
    }
    const std::uint64_t before = stream.bits_read();
    const cpp_int draw = stream.bounded_big(table.total);
    return {
        choose_from_draw(table, draw),
        draw,
        stream.bits_read() - before,
        "cpp-int",
    };
}

std::string decimal(const cpp_int &value) {
    return value.convert_to<std::string>();
}

std::string weight_list(const WeightTable &table) {
    std::string result;
    for (std::size_t index = 0; index < table.weights.size(); ++index) {
        if (index != 0) result.push_back(',');
        result += decimal(table.weights[index]);
    }
    return result;
}

std::string legacy_guard(
    const std::vector<long long> &exponents,
    const Seed128 &seed
) {
    BitStream stream(seed);
    try {
        static_cast<void>(legacy_sample(exponents, stream));
    } catch (const IntegrityError &error) {
        require(stream.bits_read() == 0, "legacy_guard_consumed_random_bits");
        return error.what();
    }
    return "NONE";
}

struct AuditCounts {
    std::uint64_t tables{0};
    std::uint64_t weight_ratios{0};
    std::uint64_t detailed_balance_pairs{0};
    std::uint64_t interval_endpoints{0};
    std::uint64_t exhaustive_draws{0};
};

void audit_table(const WeightTable &table, bool exhaust_small, AuditCounts &counts) {
    ++counts.tables;
    require(table.weights.size() == table.exponents.size(), "weight_table_size_mismatch");
    require(table.total > 0, "weight_table_nonpositive_total");
    cpp_int sum = 0;
    cpp_int cumulative = 0;
    for (std::size_t i = 0; i < table.weights.size(); ++i) {
        require(table.weights[i] > 0, "weight_table_nonpositive_weight");
        sum += table.weights[i];

        require(
            choose_from_draw(table, cumulative) == i,
            "interval_left_endpoint_selection_failed"
        );
        require(
            choose_from_draw(table, cumulative + table.weights[i] - 1) == i,
            "interval_right_endpoint_selection_failed"
        );
        counts.interval_endpoints += 2;
        cumulative += table.weights[i];

        for (std::size_t j = 0; j < table.weights.size(); ++j) {
            const long long delta = table.exponents[i] - table.exponents[j];
            if (delta >= 0) {
                cpp_int expected = table.weights[j];
                expected <<= static_cast<unsigned long long>(delta);
                require(table.weights[i] == expected, "exact_weight_ratio_failed");
            } else {
                cpp_int expected = table.weights[i];
                expected <<= static_cast<unsigned long long>(-delta);
                require(table.weights[j] == expected, "exact_weight_ratio_failed");
            }
            ++counts.weight_ratios;

            // For the orbit heat bath P(i->j)=w_j/W.  Multiplication by W
            // reduces detailed balance to the exact symmetric product below.
            require(
                table.weights[i] * table.weights[j]
                    == table.weights[j] * table.weights[i],
                "exact_detailed_balance_failed"
            );
            ++counts.detailed_balance_pairs;
        }
    }
    require(sum == table.total, "weight_table_total_failed");
    require(cumulative == table.total, "weight_table_partition_failed");

    if (exhaust_small) {
        require(table.total <= 1024, "exhaustive_table_too_large");
        std::vector<cpp_int> observed(table.weights.size());
        const auto total = table.total.convert_to<unsigned long long>();
        for (unsigned long long raw = 0; raw < total; ++raw) {
            ++observed[choose_from_draw(table, cpp_int(raw))];
            ++counts.exhaustive_draws;
        }
        require(observed == table.weights, "exhaustive_selection_mass_failed");
    }
}

void audit_bounded_rejection() {
    for (std::uint64_t bound = 1; bound <= 257; ++bound) {
        unsigned width = 0;
        for (std::uint64_t value = bound - 1; value != 0; value >>= 1) ++width;
        const std::uint64_t raw_limit = std::uint64_t{1} << width;
        std::vector<unsigned> accepted(static_cast<std::size_t>(bound), 0);
        std::uint64_t rejected = 0;
        for (std::uint64_t raw = 0; raw < raw_limit; ++raw) {
            if (raw < bound) {
                ++accepted[static_cast<std::size_t>(raw)];
            } else {
                ++rejected;
            }
        }
        for (const unsigned count : accepted) {
            require(count == 1, "bounded_rejection_first_pass_not_uniform");
        }
        require(rejected == raw_limit - bound, "bounded_rejection_count_failed");
    }
}

std::uint64_t audit_legacy_equivalence() {
    constexpr std::array<unsigned, 4> SPANS{{0, 1, 32, 62}};
    std::uint64_t cases = 0;
    for (const unsigned span : SPANS) {
        const std::vector<long long> exponents{
            0,
            -static_cast<long long>(span),
            -static_cast<long long>(span),
        };
        const WeightTable table = make_weight_table(exponents);
        require(table.legacy_representable, "legacy_equivalence_table_not_representable");
        for (std::uint32_t serial = 0; serial < 512; ++serial) {
            const Seed128 seed = property_seed(serial + 1000u * span);
            BitStream old_stream(seed);
            BitStream exact_stream(seed);
            const SampleResult old_result = legacy_sample(exponents, old_stream);
            const SampleResult exact_result = exact_sample(table, exact_stream);
            require(old_result.choice == exact_result.choice, "legacy_choice_changed");
            require(old_result.draw == exact_result.draw, "legacy_draw_changed");
            require(old_result.bits == exact_result.bits, "legacy_bit_consumption_changed");
            require(exact_result.path == "legacy-u64", "legacy_path_not_preserved");
            require(
                old_stream.bits_u64(63) == exact_stream.bits_u64(63),
                "legacy_successor_bits_changed"
            );
            require(old_stream.bits_read() == exact_stream.bits_read(), "legacy_rng_offset_changed");
            ++cases;
        }
    }
    return cases;
}

struct SmallEnvelopeCounts {
    std::uint64_t tables{0};
    std::uint64_t draws{0};
    std::uint64_t transcripts{0};
};

void audit_small_envelope_table(
    const std::vector<long long> &normalized_q,
    AuditCounts &audit_counts,
    SmallEnvelopeCounts &small_counts
) {
    require(!normalized_q.empty(), "small_envelope_empty_table");
    require(
        *std::min_element(normalized_q.begin(), normalized_q.end()) == 0,
        "small_envelope_not_normalized"
    );
    const WeightTable table = make_weight_table(normalized_q);
    require(table.legacy_representable, "small_envelope_not_legacy_representable");
    audit_table(table, false, audit_counts);

    std::vector<std::uint64_t> old_weights;
    old_weights.reserve(normalized_q.size());
    std::uint64_t old_total = 0;
    for (const long long shift : normalized_q) {
        require(shift >= 0 && shift <= 8, "small_envelope_shift_out_of_range");
        const std::uint64_t weight = std::uint64_t{1} << static_cast<unsigned>(shift);
        old_weights.push_back(weight);
        old_total += weight;
    }
    require(table.total == old_total, "small_envelope_total_parity_failed");
    for (std::size_t index = 0; index < old_weights.size(); ++index) {
        require(table.weights[index] == old_weights[index], "small_envelope_weight_parity_failed");
    }

    for (std::uint64_t raw = 0; raw < old_total; ++raw) {
        std::uint64_t cumulative = 0;
        std::size_t old_choice = old_weights.size();
        for (std::size_t index = 0; index < old_weights.size(); ++index) {
            cumulative += old_weights[index];
            if (raw < cumulative) {
                old_choice = index;
                break;
            }
        }
        require(old_choice < old_weights.size(), "small_envelope_old_choice_fell_through");
        require(
            choose_from_draw(table, cpp_int(raw)) == old_choice,
            "small_envelope_draw_choice_changed"
        );
        ++small_counts.draws;
    }

    const Seed128 seed = property_seed(static_cast<std::uint32_t>(small_counts.tables));
    BitStream old_stream(seed);
    BitStream exact_stream(seed);
    const SampleResult old_result = legacy_sample(normalized_q, old_stream);
    const SampleResult exact_result = exact_sample(table, exact_stream);
    require(old_result.choice == exact_result.choice, "small_envelope_rng_choice_changed");
    require(old_result.draw == exact_result.draw, "small_envelope_rng_draw_changed");
    require(old_result.bits == exact_result.bits, "small_envelope_rng_bits_changed");
    require(exact_result.path == "legacy-u64", "small_envelope_rng_path_changed");
    require(
        old_stream.bits_u64(63) == exact_stream.bits_u64(63),
        "small_envelope_rng_successor_changed"
    );
    require(old_stream.bits_read() == exact_stream.bits_read(), "small_envelope_rng_offset_changed");
    ++small_counts.tables;
    ++small_counts.transcripts;
}

void enumerate_small_envelope(
    std::vector<long long> &normalized_q,
    std::size_t position,
    AuditCounts &audit_counts,
    SmallEnvelopeCounts &small_counts
) {
    if (position == normalized_q.size()) {
        if (*std::min_element(normalized_q.begin(), normalized_q.end()) == 0) {
            audit_small_envelope_table(normalized_q, audit_counts, small_counts);
        }
        return;
    }
    for (long long shift = 0; shift <= 8; ++shift) {
        normalized_q[position] = shift;
        enumerate_small_envelope(normalized_q, position + 1, audit_counts, small_counts);
    }
}

SmallEnvelopeCounts audit_small_envelope(AuditCounts &audit_counts) {
    SmallEnvelopeCounts result;
    for (std::size_t length = 1; length <= 5; ++length) {
        std::vector<long long> normalized_q(length, 0);
        enumerate_small_envelope(normalized_q, 0, audit_counts, result);
    }
    require(result.tables == 28981, "small_envelope_table_count_changed");
    require(result.transcripts == result.tables, "small_envelope_transcript_count_changed");
    return result;
}

struct SpanRecord {
    unsigned span{0};
    WeightTable table;
    SampleResult result;
};

std::vector<SpanRecord> run_span_kats(AuditCounts &counts) {
    struct Expected {
        unsigned span;
        std::string_view weights;
        std::string_view total;
        std::string_view path;
        std::size_t choice;
        std::string_view draw;
        std::uint64_t bits;
    };
    constexpr std::array<Expected, 9> EXPECTED{{
        {0, "1,1,1", "3", "legacy-u64", 2, "2", 2},
        {1, "2,1,1", "4", "legacy-u64", 1, "2", 2},
        {32, "4294967296,1,1", "4294967298", "legacy-u64", 0,
            "3306569747", 198},
        {62, "4611686018427387904,1,1", "4611686018427387906", "legacy-u64", 0,
            "355632474548067208", 252},
        {63, "9223372036854775808,1,1", "9223372036854775810", "cpp-int", 0,
            "4610367715746135718", 128},
        {64, "18446744073709551616,1,1", "18446744073709551618", "cpp-int", 0,
            "18441470862984542872", 130},
        {72, "4722366482869645213696,1,1", "4722366482869645213698", "cpp-int", 0,
            "4485372269814102570263", 365},
        {128, "340282366920938463463374607431768211456,1,1",
            "340282366920938463463374607431768211458", "cpp-int", 0,
            "129104461514002519291654946113109549607", 258},
        {192, "6277101735386680763835789423207666416102355444464034512896,1,1",
            "6277101735386680763835789423207666416102355444464034512898", "cpp-int", 0,
            "344787069990799528478562258756344962750274670445818510001", 772},
    }};
    std::vector<SpanRecord> records;
    for (const Expected &expected : EXPECTED) {
        const unsigned span = expected.span;
        const std::vector<long long> exponents{
            0,
            -static_cast<long long>(span),
            -static_cast<long long>(span),
        };
        WeightTable table = make_weight_table(exponents);
        audit_table(table, span <= 1, counts);
        BitStream stream(sequential_seed());
        SampleResult result = exact_sample(table, stream);
        require(weight_list(table) == expected.weights, "span_KAT_weights_changed");
        require(decimal(table.total) == expected.total, "span_KAT_total_changed");
        require(result.path == expected.path, "span_KAT_path_changed");
        require(result.choice == expected.choice, "span_KAT_choice_changed");
        require(decimal(result.draw) == expected.draw, "span_KAT_draw_changed");
        require(result.bits == expected.bits, "span_KAT_bits_changed");
        records.push_back({span, std::move(table), std::move(result)});
    }
    return records;
}

void run_fixture(std::ostream &output) {
    require(
        hex_digest(BitStream::counter_digest(
            sequential_seed(), BITSTREAM_DOMAIN, std::array<std::uint8_t, 16>{}
        )) == "9434ecd5f984de773ffb5102bcfa3ea618482759831459004ef75d9f407db889",
        "bitstream_counter_zero_digest_failed"
    );
    audit_bounded_rejection();
    const std::uint64_t legacy_cases = audit_legacy_equivalence();

    AuditCounts counts;
    const SmallEnvelopeCounts small_counts = audit_small_envelope(counts);
    const std::vector<SpanRecord> records = run_span_kats(counts);

    const std::vector<long long> sum_overflow_exponents{0, 0, 0, 0, -62};
    const WeightTable sum_overflow = make_weight_table(sum_overflow_exponents);
    require(sum_overflow.span == 62, "sum_overflow_span_changed");
    require(!sum_overflow.legacy_representable, "sum_overflow_legacy_path_accepted");
    require(
        legacy_guard(sum_overflow_exponents, sequential_seed())
            == "orbit_weight_sum_overflow",
        "sum_overflow_legacy_guard_changed"
    );
    audit_table(sum_overflow, false, counts);
    BitStream sum_stream(sequential_seed());
    const SampleResult sum_result = exact_sample(sum_overflow, sum_stream);
    require(sum_result.path == "cpp-int", "sum_overflow_did_not_use_cpp_int");
    require(
        weight_list(sum_overflow)
            == "4611686018427387904,4611686018427387904,4611686018427387904,4611686018427387904,1",
        "sum_overflow_weights_changed"
    );
    require(decimal(sum_overflow.total) == "18446744073709551617", "sum_overflow_total_changed");
    require(sum_result.choice == 3, "sum_overflow_choice_changed");
    require(decimal(sum_result.draw) == "18441470862984542872", "sum_overflow_draw_changed");
    require(sum_result.bits == 130, "sum_overflow_bits_changed");

    const std::vector<long long> width64_exponents{0, 0, -62};
    const WeightTable width64 = make_weight_table(width64_exponents);
    require(width64.span == 62, "width64_span_changed");
    require(!width64.legacy_representable, "width64_legacy_path_accepted");
    require(
        legacy_guard(width64_exponents, sequential_seed())
            == "bitstream_bits_width_exceeds_63",
        "width64_legacy_guard_changed"
    );
    audit_table(width64, false, counts);
    BitStream width64_stream(sequential_seed());
    const SampleResult width64_result = exact_sample(width64, width64_stream);
    require(width64_result.path == "cpp-int", "width64_did_not_use_cpp_int");
    require(
        weight_list(width64) == "4611686018427387904,4611686018427387904,1",
        "width64_weights_changed"
    );
    require(decimal(width64.total) == "9223372036854775809", "width64_total_changed");
    require(width64_result.choice == 0, "width64_choice_changed");
    require(
        decimal(width64_result.draw) == "4610367715746135718",
        "width64_draw_changed"
    );
    require(width64_result.bits == 128, "width64_bits_changed");

    struct EnvelopeRecord {
        int L;
        unsigned spread;
        WeightTable table;
        SampleResult result;
        std::string guard;
    };
    std::vector<EnvelopeRecord> envelopes;
    for (const int L : {6, 8}) {
        const unsigned area = static_cast<unsigned>(L * L);
        const unsigned spread = 2 * area;
        // Synthetic algebraic envelope only.  P0 and P1 are disjoint,
        // translated, homologous positive (a,b) planes.  At level S=L^2,
        // n=-P0 and generator g=P1 give the allowed k=0,1,4 states
        // (support,B)=(S,1),(2S,0),(2S,1), hence e=(0,-2S,-S).
        const std::vector<long long> exponents{
            0,
            -static_cast<long long>(spread),
            -static_cast<long long>(area),
        };
        WeightTable table = make_weight_table(exponents);
        audit_table(table, false, counts);
        const std::string guard = legacy_guard(exponents, sequential_seed());
        require(guard == "orbit_integer_weight_overflow", "two_plane_guard_changed");
        BitStream stream(sequential_seed());
        SampleResult result = exact_sample(table, stream);
        require(result.path == "cpp-int", "two_plane_did_not_use_cpp_int");
        if (L == 6) {
            require(
                weight_list(table) == "4722366482869645213696,1,68719476736",
                "two_plane_L6_weights_changed"
            );
            require(decimal(table.total) == "4722366482938364690433", "two_plane_L6_total_changed");
            require(result.choice == 0, "two_plane_L6_choice_changed");
            require(
                decimal(result.draw) == "4485372269814102570263",
                "two_plane_L6_draw_changed"
            );
            require(result.bits == 365, "two_plane_L6_bits_changed");
        } else {
            require(
                weight_list(table)
                    == "340282366920938463463374607431768211456,1,18446744073709551616",
                "two_plane_L8_weights_changed"
            );
            require(
                decimal(table.total) == "340282366920938463481821351505477763073",
                "two_plane_L8_total_changed"
            );
            require(result.choice == 0, "two_plane_L8_choice_changed");
            require(
                decimal(result.draw) == "129104461514002519291654946113109549607",
                "two_plane_L8_draw_changed"
            );
            require(result.bits == 258, "two_plane_L8_bits_changed");
        }
        envelopes.push_back({L, spread, std::move(table), std::move(result), guard});
    }

    require(small_counts.draws == 6791443, "small_envelope_draw_count_changed");
    require(counts.tables == 28994, "exact_audit_table_count_changed");
    require(counts.weight_ratios == 698620, "exact_audit_weight_ratio_count_changed");
    require(
        counts.detailed_balance_pairs == 698620,
        "exact_audit_detailed_balance_count_changed"
    );
    require(counts.interval_endpoints == 283984, "exact_audit_interval_count_changed");
    require(counts.exhaustive_draws == 7, "exact_audit_draw_count_changed");

    output
        << "ORBIT_QUALIFICATION bitstream=sha256-counter-msb-first"
        << " bounded_rejection=PASS legacy_equivalence_cases=" << legacy_cases
        << " status=PASS\n";
    output
        << "SMALL_ENVELOPE_EXHAUSTIVE lengths=1..5 normalized_q=0..8"
        << " tables=" << small_counts.tables
        << " draws=" << small_counts.draws
        << " transcripts=" << small_counts.transcripts
        << " status=PASS\n";
    for (const SpanRecord &record : records) {
        output
            << "SPAN_KAT span=" << record.span
            << " weights=" << weight_list(record.table)
            << " total=" << decimal(record.table.total)
            << " path=" << record.result.path
            << " choice=" << record.result.choice
            << " draw=" << decimal(record.result.draw)
            << " bits=" << record.result.bits
            << " status=PASS\n";
    }
    output
        << "SUM_OVERFLOW_KAT span=62 weights=" << weight_list(sum_overflow)
        << " total=" << decimal(sum_overflow.total)
        << " old_guard=orbit_weight_sum_overflow"
        << " path=" << sum_result.path
        << " choice=" << sum_result.choice
        << " draw=" << decimal(sum_result.draw)
        << " bits=" << sum_result.bits
        << " status=PASS\n";
    output
        << "WIDTH64_KAT span=62 weights=" << weight_list(width64)
        << " total=" << decimal(width64.total)
        << " old_guard=bitstream_bits_width_exceeds_63"
        << " guard_bits=0"
        << " path=" << width64_result.path
        << " choice=" << width64_result.choice
        << " draw=" << decimal(width64_result.draw)
        << " bits=" << width64_result.bits
        << " status=PASS\n";
    for (const EnvelopeRecord &record : envelopes) {
        output
            << "TWO_PLANE_ENVELOPE L=" << record.L
            << " spread=" << record.spread
            << " states=k0,k1,k4"
            << " support_B=" << record.L * record.L << ":1,"
            << 2 * record.L * record.L << ":0,"
            << 2 * record.L * record.L << ":1"
            << " exponents=0,-" << record.spread << ",-" << record.L * record.L
            << " weights=" << weight_list(record.table)
            << " total=" << decimal(record.table.total)
            << " old_guard=" << record.guard
            << " guard_bits=0"
            << " path=" << record.result.path
            << " choice=" << record.result.choice
            << " draw=" << decimal(record.result.draw)
            << " bits=" << record.result.bits
            << " status=PASS\n";
    }
    output
        << "EXACT_AUDIT tables=" << counts.tables
        << " weight_ratios=" << counts.weight_ratios
        << " detailed_balance_pairs=" << counts.detailed_balance_pairs
        << " interval_endpoints=" << counts.interval_endpoints
        << " exhaustive_draws=" << counts.exhaustive_draws
        << " totals_above_2^64=YES status=PASS\n"
        << "ORBIT_QUALIFICATION PASS\n";
}

}  // namespace orbit_qualification

int main(int argc, char **argv) {
    using namespace orbit_qualification;
    try {
        std::locale::global(std::locale::classic());
        std::cout.imbue(std::locale::classic());
        std::cerr.imbue(std::locale::classic());
#ifdef _WIN32
        if (_setmode(_fileno(stdout), _O_BINARY) == -1) {
            throw IntegrityError("stdout_binary_mode_failed");
        }
        if (_setmode(_fileno(stderr), _O_BINARY) == -1) {
            throw IntegrityError("stderr_binary_mode_failed");
        }
#endif
        if (argc != 2 || std::string_view(argv[1]) != "--fixture") {
            throw IntegrityError("usage: orbit_qualification --fixture");
        }
        run_fixture(std::cout);
        if (!std::cout) throw IntegrityError("stdout_write_failed");
        return 0;
    } catch (const std::exception &error) {
        std::cerr << "ERROR " << error.what() << '\n';
        return 2;
    }
}
