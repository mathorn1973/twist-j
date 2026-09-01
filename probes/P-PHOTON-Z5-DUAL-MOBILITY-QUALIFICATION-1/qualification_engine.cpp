// qualification_engine.cpp
//
// Dependency-free implementation of the exact hard-state sector-umbrella
// kernel used by P-PHOTON-Z5-DUAL-MOBILITY-QUALIFICATION-1.  There is no
// default schedule and no embedded run seed.  Development is explicit;
// qualification additionally requires the public pin commit and receipt.
//
// Product target at level s:
//
//   pi_s(n) proportional to 2^(-support(n) + s B(n)),
//   B(n) = 1[j(n) != 0] + 1[H_2(n) != 0],
//   s = 0,...,max(15,L^2).
//
// Every state is a closed Z_5 two-cycle with residues only in {0,1,4}.
// The random-scan components are: an explicit hold, the immutable #767
// random-word Metropolis transition with positive probability, charge
// conjugation, exact cube/tri-star/translated-plane orbit heat baths, and
// exact adjacent replica swaps.  The selector probabilities and RNG call
// order match sector_ladder.py.  All stochastic choices use the SHA-256
// counter bitstream below; no host PRNG or floating-point arithmetic occurs.

#include <algorithm>
#include <array>
#include <cctype>
#include <cstdint>
#include <cstdio>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <limits>
#include <locale>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <stdexcept>
#include <string>
#include <string_view>
#include <utility>
#include <vector>

#ifdef _WIN32
#include <fcntl.h>
#include <io.h>
#endif

namespace qualification {

class IntegrityError : public std::runtime_error {
  public:
    explicit IntegrityError(const std::string &message) : std::runtime_error(message) {}
};

constexpr int DIM = 4;
constexpr int N_PAIRS = 6;
constexpr int N_TRIPLES = 4;
constexpr std::array<std::array<int, 2>, N_PAIRS> PAIRS{{
    {{0, 1}}, {{0, 2}}, {{0, 3}}, {{1, 2}}, {{1, 3}}, {{2, 3}},
}};
constexpr std::array<std::array<int, 3>, N_TRIPLES> TRIPLES{{
    {{0, 1, 2}}, {{0, 1, 3}}, {{0, 2, 3}}, {{1, 2, 3}},
}};
constexpr std::string_view BITSTREAM_DOMAIN = "photon-z5-dual-mobility-qualification-1";

int mod5(int value) {
    int result = value % 5;
    return result < 0 ? result + 5 : result;
}

bool hard_allowed(int residue) {
    const int value = mod5(residue);
    return value == 0 || value == 1 || value == 4;
}

int principal(int residue) {
    const int value = mod5(residue);
    if (value == 4) return -1;
    if (value == 0 || value == 1) return value;
    throw IntegrityError("principal_forbidden_residue");
}

int pair_index(int a, int b) {
    if (a > b) std::swap(a, b);
    for (int index = 0; index < N_PAIRS; ++index) {
        if (PAIRS[index][0] == a && PAIRS[index][1] == b) return index;
    }
    throw IntegrityError("invalid_pair");
}

int triple_index(std::array<int, 3> axes) {
    std::sort(axes.begin(), axes.end());
    for (int index = 0; index < N_TRIPLES; ++index) {
        if (TRIPLES[index] == axes) return index;
    }
    throw IntegrityError("invalid_triple");
}

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

    void update(const std::vector<std::uint8_t> &data) {
        if (!data.empty()) update(data.data(), data.size());
    }

    std::array<std::uint8_t, 32> final() const {
        Sha256 copy = *this;
        const std::uint64_t bit_length = copy.total_bytes_ * 8ULL;
        std::array<std::uint8_t, 64> padding{};
        padding[0] = 0x80;
        const std::size_t padding_size = copy.used_ < 56 ? 56 - copy.used_ : 120 - copy.used_;
        copy.update(padding.data(), padding_size);
        std::array<std::uint8_t, 8> length_bytes{};
        for (int index = 0; index < 8; ++index) {
            length_bytes[7 - index] = static_cast<std::uint8_t>(bit_length >> (8 * index));
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
                ^ rotate_right(words[index - 15], 18) ^ (words[index - 15] >> 3);
            const std::uint32_t s1 = rotate_right(words[index - 2], 17)
                ^ rotate_right(words[index - 2], 19) ^ (words[index - 2] >> 10);
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
            const std::uint32_t sum1 = rotate_right(e, 6) ^ rotate_right(e, 11) ^ rotate_right(e, 25);
            const std::uint32_t choose = (e & f) ^ ((~e) & g);
            const std::uint32_t temp1 = h + sum1 + choose + K[index] + words[index];
            const std::uint32_t sum0 = rotate_right(a, 2) ^ rotate_right(a, 13) ^ rotate_right(a, 22);
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

std::string sha256(std::string_view text) {
    Sha256 hash;
    hash.update(text);
    return hex_digest(hash.final());
}

std::string sha256(const std::vector<std::uint8_t> &data) {
    Sha256 hash;
    hash.update(data);
    return hex_digest(hash.final());
}

struct Seed128 {
    std::array<std::uint8_t, 16> bytes{};
};

Seed128 parse_seed(std::string_view text) {
    if (text.size() >= 2 && text[0] == '0' && (text[1] == 'x' || text[1] == 'X')) text.remove_prefix(2);
    if (text.empty() || text.size() > 32) throw IntegrityError("seed_must_be_1_to_32_hex_digits");
    for (unsigned char character : text) {
        if (!std::isxdigit(character)) throw IntegrityError("seed_not_hexadecimal");
    }
    std::string padded(32 - text.size(), '0');
    padded.append(text.begin(), text.end());
    Seed128 result;
    auto nibble = [](char character) -> std::uint8_t {
        if (character >= '0' && character <= '9') return static_cast<std::uint8_t>(character - '0');
        if (character >= 'a' && character <= 'f') return static_cast<std::uint8_t>(character - 'a' + 10);
        return static_cast<std::uint8_t>(character - 'A' + 10);
    };
    for (int index = 0; index < 16; ++index) {
        result.bytes[index] = static_cast<std::uint8_t>(
            (nibble(padded[2 * index]) << 4) | nibble(padded[2 * index + 1])
        );
    }
    return result;
}

std::string seed_hex(const Seed128 &seed) {
    static constexpr char HEX[] = "0123456789abcdef";
    std::string result(32, '0');
    for (int index = 0; index < 16; ++index) {
        result[2 * index] = HEX[seed.bytes[index] >> 4];
        result[2 * index + 1] = HEX[seed.bytes[index] & 15];
    }
    return result;
}

class BitStream {
  public:
    explicit BitStream(Seed128 seed, std::string domain = std::string(BITSTREAM_DOMAIN))
        : seed_(seed), domain_(std::move(domain)) {
        counter_.fill(0);
    }

    int bit() {
        if (bit_position_ == 256) refill();
        const int result = (digest_[bit_position_ / 8] >> (7 - (bit_position_ % 8))) & 1;
        ++bit_position_;
        return result;
    }

    std::uint64_t bits(unsigned count) {
        if (count > 63) throw IntegrityError("bitstream_bits_width_exceeds_63");
        std::uint64_t value = 0;
        for (unsigned index = 0; index < count; ++index) value = (value << 1) | static_cast<unsigned>(bit());
        return value;
    }

    std::uint64_t bounded(std::uint64_t bound) {
        if (bound == 0) throw IntegrityError("bitstream_zero_bound");
        unsigned width = 0;
        for (std::uint64_t value = bound - 1; value != 0; value >>= 1) ++width;
        while (true) {
            const std::uint64_t value = bits(width);
            if (value < bound) return value;
        }
    }

    std::uint64_t geometric_half() {
        std::uint64_t length = 0;
        while (bit() == 0) {
            if (length == std::numeric_limits<std::uint64_t>::max()) {
                throw IntegrityError("geometric_length_overflow");
            }
            ++length;
        }
        return length;
    }

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

    void set_counter_for_selftest(const std::array<std::uint8_t, 16> &counter) {
        counter_ = counter;
        bit_position_ = 256;
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
};

using SparseGenerator = std::vector<std::pair<int, std::uint8_t>>;
using FaceBoundary = std::array<std::pair<int, std::int8_t>, 4>;

class Torus4 {
  public:
    explicit Torus4(int extent) : L(extent), volume(extent * extent * extent * extent) {
        if (L < 3 || L > 4) throw IntegrityError("extent_must_be_3_or_4");
        n_links = volume * DIM;
        n_plaq = volume * N_PAIRS;
        n_cubes = volume * N_TRIPLES;
        coords.resize(volume);
        for (int site = 0; site < volume; ++site) coords[site] = site_coord(site);
        for (int axis = 0; axis < DIM; ++axis) {
            forward[axis].resize(volume);
            backward[axis].resize(volume);
            for (int site = 0; site < volume; ++site) {
                auto upper = coords[site];
                auto lower = coords[site];
                upper[axis] = (upper[axis] + 1) % L;
                lower[axis] = (lower[axis] + L - 1) % L;
                forward[axis][site] = site_index(upper);
                backward[axis][site] = site_index(lower);
            }
        }
        build_face_boundaries();
        build_cube_generators();
        build_translated_planes();
        build_tristars();
    }

    int site_index(const std::array<int, 4> &x) const {
        int value = 0;
        for (int coordinate : x) value = value * L + mod5_coordinate(coordinate);
        return value;
    }

    std::array<int, 4> site_coord(int index) const {
        if (index < 0 || index >= volume) throw IntegrityError("site_index_out_of_range");
        std::array<int, 4> result{};
        for (int axis = DIM - 1; axis >= 0; --axis) {
            result[axis] = index % L;
            index /= L;
        }
        return result;
    }

    int plaq_index(int site, int orientation) const {
        return site * N_PAIRS + orientation;
    }

    const SparseGenerator &cube(int index) const { return cubes.at(static_cast<std::size_t>(index)); }
    const SparseGenerator &tristar(int plaquette, int omitted) const {
        return tristars.at(static_cast<std::size_t>(plaquette * 4 + omitted));
    }
    const SparseGenerator &translated_plane(int orientation, int translation) const {
        return planes.at(static_cast<std::size_t>(orientation * L * L + translation));
    }
    const SparseGenerator &fixed_plane(int orientation) const {
        return translated_plane(orientation, 0);
    }

    int L;
    int volume;
    int n_links{0};
    int n_plaq{0};
    int n_cubes{0};
    std::vector<std::array<int, 4>> coords;
    std::array<std::vector<int>, DIM> forward;
    std::array<std::vector<int>, DIM> backward;
    std::vector<FaceBoundary> face_boundaries;

  private:
    int mod5_coordinate(int coordinate) const {
        int result = coordinate % L;
        return result < 0 ? result + L : result;
    }

    static SparseGenerator normalized(const std::map<int, int> &raw) {
        SparseGenerator result;
        for (const auto &[index, coefficient] : raw) {
            const int value = mod5(coefficient);
            if (value != 0) result.emplace_back(index, static_cast<std::uint8_t>(value));
        }
        return result;
    }

    static SparseGenerator scaled(const SparseGenerator &source, int scalar) {
        SparseGenerator result;
        result.reserve(source.size());
        for (const auto &[index, coefficient] : source) {
            const int value = mod5(scalar * static_cast<int>(coefficient));
            if (value != 0) result.emplace_back(index, static_cast<std::uint8_t>(value));
        }
        return result;
    }

    static SparseGenerator added(const std::vector<SparseGenerator> &sources) {
        std::map<int, int> raw;
        for (const auto &source : sources) {
            for (const auto &[index, coefficient] : source) raw[index] += coefficient;
        }
        return normalized(raw);
    }

    int coefficient_at(const SparseGenerator &generator, int plaquette) const {
        for (const auto &[index, coefficient] : generator) {
            if (index == plaquette) return coefficient;
        }
        return 0;
    }

    void build_face_boundaries() {
        face_boundaries.resize(n_plaq);
        for (int site = 0; site < volume; ++site) {
            for (int orientation = 0; orientation < N_PAIRS; ++orientation) {
                const int a = PAIRS[orientation][0];
                const int b = PAIRS[orientation][1];
                face_boundaries[plaq_index(site, orientation)] = {{
                    {site * DIM + a, 1},
                    {forward[a][site] * DIM + b, 1},
                    {forward[b][site] * DIM + a, -1},
                    {site * DIM + b, -1},
                }};
            }
        }
    }

    void build_cube_generators() {
        cubes.reserve(n_cubes);
        for (int site = 0; site < volume; ++site) {
            for (int triple = 0; triple < N_TRIPLES; ++triple) {
                std::map<int, int> raw;
                const auto axes = TRIPLES[triple];
                for (int position = 0; position < 3; ++position) {
                    const int axis = axes[position];
                    std::array<int, 2> face{};
                    int cursor = 0;
                    for (int candidate : axes) if (candidate != axis) face[cursor++] = candidate;
                    const int orientation = pair_index(face[0], face[1]);
                    const int sign = (position % 2 == 0) ? 1 : -1;
                    raw[plaq_index(forward[axis][site], orientation)] += sign;
                    raw[plaq_index(site, orientation)] -= sign;
                }
                SparseGenerator generator = normalized(raw);
                if (generator.size() != 6) throw IntegrityError("cube_support_not_six");
                cubes.push_back(std::move(generator));
            }
        }
    }

    void build_translated_planes() {
        planes.reserve(static_cast<std::size_t>(N_PAIRS * L * L));
        for (int orientation = 0; orientation < N_PAIRS; ++orientation) {
            const int a = PAIRS[orientation][0];
            const int b = PAIRS[orientation][1];
            std::array<int, 2> complement{};
            int cursor = 0;
            for (int axis = 0; axis < DIM; ++axis) if (axis != a && axis != b) complement[cursor++] = axis;
            for (int translation = 0; translation < L * L; ++translation) {
                const int fixed0 = translation / L;
                const int fixed1 = translation % L;
                SparseGenerator plane;
                plane.reserve(static_cast<std::size_t>(L * L));
                for (int ia = 0; ia < L; ++ia) {
                    for (int ib = 0; ib < L; ++ib) {
                        std::array<int, 4> x{};
                        x[a] = ia;
                        x[b] = ib;
                        x[complement[0]] = fixed0;
                        x[complement[1]] = fixed1;
                        plane.emplace_back(plaq_index(site_index(x), orientation), 1);
                    }
                }
                std::sort(plane.begin(), plane.end());
                planes.push_back(std::move(plane));
            }
        }
    }

    void build_tristars() {
        tristars.reserve(static_cast<std::size_t>(n_plaq * 4));
        for (int plaquette = 0; plaquette < n_plaq; ++plaquette) {
            const int site = plaquette / N_PAIRS;
            const int orientation = plaquette % N_PAIRS;
            const int a = PAIRS[orientation][0];
            const int b = PAIRS[orientation][1];
            std::vector<SparseGenerator> arms;
            arms.reserve(4);
            for (int axis = 0; axis < DIM; ++axis) {
                if (axis == a || axis == b) continue;
                std::array<int, 3> axes{{a, b, axis}};
                const int triple = triple_index(axes);
                for (int base : {site, backward[axis][site]}) {
                    const auto &source = cube(base * N_TRIPLES + triple);
                    const int central = coefficient_at(source, plaquette);
                    if (central != 1 && central != 4) throw IntegrityError("incident_cube_missing_central_face");
                    arms.push_back(scaled(source, central == 1 ? 1 : 4));
                }
            }
            if (arms.size() != 4) throw IntegrityError("tristar_incident_count");
            for (int omitted = 0; omitted < 4; ++omitted) {
                std::vector<SparseGenerator> selected;
                for (int index = 0; index < 4; ++index) if (index != omitted) selected.push_back(arms[index]);
                SparseGenerator generator = added(selected);
                if (coefficient_at(generator, plaquette) != 3) throw IntegrityError("tristar_central_coefficient");
                if (generator.size() != 16) throw IntegrityError("tristar_support_not_sixteen");
                tristars.push_back(std::move(generator));
            }
        }
    }

    std::vector<SparseGenerator> cubes;
    std::vector<SparseGenerator> planes;
    std::vector<SparseGenerator> tristars;
};

int inverse_mod5(int value) {
    const int normalized = mod5(value);
    for (int candidate = 1; candidate < 5; ++candidate) {
        if (mod5(normalized * candidate) == 1) return candidate;
    }
    throw IntegrityError("noninvertible_mod5_value");
}

struct Census {
    int support{0};
    std::vector<int> current;
    int current_nonzero{0};
    std::array<std::uint8_t, N_PAIRS> homology{};
    int homology_nonzero{0};
};

Census full_census(const Torus4 &lattice, const std::vector<std::uint8_t> &state) {
    if (static_cast<int>(state.size()) != lattice.n_plaq) throw IntegrityError("state_length_mismatch");
    Census result;
    std::vector<int> modular_boundary(static_cast<std::size_t>(lattice.n_links), 0);
    std::vector<int> integer_boundary(static_cast<std::size_t>(lattice.n_links), 0);
    std::array<std::int64_t, N_PAIRS> homology_totals{};
    for (int plaquette = 0; plaquette < lattice.n_plaq; ++plaquette) {
        const int residue = state[plaquette];
        if (!hard_allowed(residue)) throw IntegrityError("state_left_hard_support");
        result.support += residue != 0;
        homology_totals[plaquette % N_PAIRS] += residue;
        if (residue == 0) continue;
        const int lifted = principal(residue);
        for (const auto &[link, coefficient] : lattice.face_boundaries[plaquette]) {
            modular_boundary[link] += static_cast<int>(coefficient) * residue;
            integer_boundary[link] += static_cast<int>(coefficient) * lifted;
        }
    }
    result.current.resize(static_cast<std::size_t>(lattice.n_links));
    for (int link = 0; link < lattice.n_links; ++link) {
        if (mod5(modular_boundary[link]) != 0) throw IntegrityError("state_not_closed_mod5");
        if (integer_boundary[link] % 5 != 0) throw IntegrityError("integer_boundary_not_divisible_by_five");
        result.current[link] = integer_boundary[link] / 5;
        result.current_nonzero += result.current[link] != 0;
    }
    std::vector<int> divergence(static_cast<std::size_t>(lattice.volume), 0);
    for (int site = 0; site < lattice.volume; ++site) {
        for (int axis = 0; axis < DIM; ++axis) {
            const int value = result.current[site * DIM + axis];
            divergence[site] -= value;
            divergence[lattice.forward[axis][site]] += value;
        }
    }
    if (std::any_of(divergence.begin(), divergence.end(), [](int value) { return value != 0; })) {
        throw IntegrityError("integer_current_not_conserved");
    }
    const int inverse = inverse_mod5(mod5(lattice.L * lattice.L));
    for (int orientation = 0; orientation < N_PAIRS; ++orientation) {
        const int value = mod5(static_cast<int>(homology_totals[orientation] % 5));
        result.homology[orientation] = static_cast<std::uint8_t>(mod5(inverse * value));
        result.homology_nonzero += result.homology[orientation] != 0;
    }
    return result;
}

struct Replica {
    std::vector<std::uint8_t> state;
    int support{0};
    std::vector<int> current;
    int current_nonzero{0};
    std::array<std::uint8_t, N_PAIRS> homology{};
    int homology_nonzero{0};
    int walker_id{0};

    int score() const {
        return static_cast<int>(current_nonzero != 0) + static_cast<int>(homology_nonzero != 0);
    }
};

Replica make_replica(const Torus4 &lattice, std::vector<std::uint8_t> state, int walker_id) {
    const Census census = full_census(lattice, state);
    Replica result;
    result.state = std::move(state);
    result.support = census.support;
    result.current = census.current;
    result.current_nonzero = census.current_nonzero;
    result.homology = census.homology;
    result.homology_nonzero = census.homology_nonzero;
    result.walker_id = walker_id;
    return result;
}

void validate_replica(const Torus4 &lattice, const Replica &replica) {
    const Census census = full_census(lattice, replica.state);
    if (census.support != replica.support) throw IntegrityError("replica_support_census_mismatch");
    if (census.current != replica.current) throw IntegrityError("replica_current_census_mismatch");
    if (census.current_nonzero != replica.current_nonzero) throw IntegrityError("replica_current_nonzero_mismatch");
    if (census.homology != replica.homology) throw IntegrityError("replica_homology_census_mismatch");
    if (census.homology_nonzero != replica.homology_nonzero) throw IntegrityError("replica_homology_nonzero_mismatch");
}

struct Candidate {
    int k{0};
    int support{0};
    int current_nonzero{0};
    int homology_nonzero{0};
    std::array<std::uint8_t, N_PAIRS> homology{};
    int exponent{0};
    std::uint64_t weight{0};
    std::vector<std::pair<int, std::uint8_t>> changes;
    std::vector<std::pair<int, int>> current_changes;
};

enum class Family : int {
    Hold = 0,
    Legacy = 1,
    Conjugation = 2,
    Cube = 3,
    Tristar = 4,
    Homology = 5,
    Swap = 6,
    Count = 7,
};

constexpr std::array<std::string_view, static_cast<int>(Family::Count)> FAMILY_NAMES{{
    "hold", "legacy", "conjugation", "cube", "tristar", "homology", "swap",
}};

struct Diagnostics {
    std::uint64_t transitions{0};
    std::array<std::uint64_t, static_cast<int>(Family::Count)> family_attempts{};
    std::vector<std::uint64_t> swap_attempts;
    std::vector<std::uint64_t> swap_accepts;
    std::vector<std::uint64_t> local_current_births;
    std::vector<std::uint64_t> local_current_deaths;
    std::vector<std::uint64_t> local_current_vector_moves;
    std::vector<std::uint64_t> local_homology_births;
    std::vector<std::uint64_t> local_homology_deaths;
    std::vector<std::uint64_t> local_homology_moves;
    std::vector<std::uint64_t> walker_roundtrips;
    std::vector<int> walker_phase;
    std::uint64_t legacy_max_word{0};
    std::uint64_t legacy_accepts{0};
    std::uint64_t legacy_firewall_rejects{0};
    std::uint64_t legacy_metropolis_rejects{0};
    std::uint64_t target_current_entries{0};
    std::uint64_t target_current_exits{0};
};

struct MeasuredDiagnostics {
    std::uint64_t transitions{0};
    std::array<std::uint64_t, static_cast<int>(Family::Count)> family_attempts{};
    std::vector<std::uint64_t> swap_attempts;
    std::vector<std::uint64_t> swap_accepts;
    std::vector<std::uint64_t> local_current_births;
    std::vector<std::uint64_t> local_current_deaths;
    std::vector<std::uint64_t> local_current_vector_moves;
    std::vector<std::uint64_t> local_homology_births;
    std::vector<std::uint64_t> local_homology_deaths;
    std::vector<std::uint64_t> local_homology_moves;
    std::vector<std::uint64_t> current_swap_down;
    std::vector<std::uint64_t> current_swap_up;
    std::vector<std::uint64_t> homology_swap_down;
    std::vector<std::uint64_t> homology_swap_up;
    std::vector<std::uint64_t> walker_roundtrips;
    std::vector<int> walker_phase;
    std::uint64_t legacy_max_word{0};
    std::uint64_t legacy_accepts{0};
    std::uint64_t legacy_firewall_rejects{0};
    std::uint64_t legacy_metropolis_rejects{0};
    std::uint64_t target_current_entries{0};
    std::uint64_t target_current_exits{0};
    std::uint64_t target_current_imports{0};
    std::uint64_t target_current_exports{0};
};

struct DevelopmentBudget {
    std::uint64_t warm_bottom{0};
    std::uint64_t checkpoints{0};
    std::uint64_t thin{0};
    std::uint64_t validation_stride{0};
    std::uint64_t transition_cap{0};
};

struct FormalSpec {
    int L;
    std::string_view start;
    std::string_view seed_token;
};

constexpr DevelopmentBudget FORMAL_BUDGET{
    16'384,
    2'048,
    256,
    256,
    67'108'864,
};

constexpr std::array<FormalSpec, 8> FORMAL_SPECS{{
    {3, "cold",       "0xf7560000000000000000000000030101"},
    {3, "cold",       "0xf7560000000000000000000000030102"},
    {3, "stratified", "0xf7560000000000000000000000030201"},
    {3, "stratified", "0xf7560000000000000000000000030202"},
    {4, "cold",       "0xf7560000000000000000000000040101"},
    {4, "cold",       "0xf7560000000000000000000000040102"},
    {4, "stratified", "0xf7560000000000000000000000040201"},
    {4, "stratified", "0xf7560000000000000000000000040202"},
}};

bool same_budget(const DevelopmentBudget &left, const DevelopmentBudget &right) {
    return left.warm_bottom == right.warm_bottom
        && left.checkpoints == right.checkpoints
        && left.thin == right.thin
        && left.validation_stride == right.validation_stride
        && left.transition_cap == right.transition_cap;
}

bool qualification_spec_matches(
    int L,
    std::string_view start,
    std::string_view seed_token,
    const Seed128 &seed
) {
    for (const auto &spec : FORMAL_SPECS) {
        if (L == spec.L && start == spec.start && seed_token == spec.seed_token
            && seed_token.substr(2) == seed_hex(seed)) {
            return true;
        }
    }
    return false;
}

bool valid_pin_commit(std::string_view token) {
    return token.size() == 40
        && std::all_of(token.begin(), token.end(), [](unsigned char character) {
            return (character >= '0' && character <= '9') || (character >= 'a' && character <= 'f');
        });
}

bool valid_pin_receipt(std::string_view token) {
    constexpr std::string_view prefix =
        "https://github.com/mathorn1973/twist-j/issues/756#issuecomment-";
    return token.size() > prefix.size()
        && token.compare(0, prefix.size(), prefix) == 0
        && std::all_of(
            token.begin() + static_cast<std::ptrdiff_t>(prefix.size()),
            token.end(),
            [](unsigned char character) { return character >= '0' && character <= '9'; }
        );
}

std::string json_string(std::string_view text) {
    std::string result = "\"";
    for (unsigned char character : text) {
        switch (character) {
            case '\"': result += "\\\""; break;
            case '\\': result += "\\\\"; break;
            case '\b': result += "\\b"; break;
            case '\f': result += "\\f"; break;
            case '\n': result += "\\n"; break;
            case '\r': result += "\\r"; break;
            case '\t': result += "\\t"; break;
            default:
                if (character < 0x20 || character > 0x7e) throw IntegrityError("json_non_ascii_text");
                result.push_back(static_cast<char>(character));
        }
    }
    result.push_back('\"');
    return result;
}

template <typename T>
std::string integer_vector_json(const std::vector<T> &values) {
    std::ostringstream output;
    output.imbue(std::locale::classic());
    output << '[';
    for (std::size_t index = 0; index < values.size(); ++index) {
        if (index != 0) output << ',';
        output << values[index];
    }
    output << ']';
    return output.str();
}

std::string homology_json(const std::array<std::uint8_t, N_PAIRS> &values) {
    std::ostringstream output;
    output.imbue(std::locale::classic());
    output << '[';
    for (int index = 0; index < N_PAIRS; ++index) {
        if (index != 0) output << ',';
        output << static_cast<unsigned>(values[index]);
    }
    output << ']';
    return output.str();
}

std::string state_hash(const Replica &replica) {
    return sha256(replica.state);
}

std::string current_hash(const Replica &replica) {
    std::ostringstream payload;
    payload.imbue(std::locale::classic());
    for (std::size_t index = 0; index < replica.current.size(); ++index) {
        if (index != 0) payload << ',';
        payload << replica.current[index];
    }
    return sha256(payload.str());
}

std::int64_t principal_sum(const Replica &replica) {
    std::int64_t total = 0;
    for (std::uint8_t value : replica.state) total += principal(value);
    return total;
}

std::uint64_t current_l2_sum(const Replica &replica) {
    std::uint64_t total = 0;
    for (int value : replica.current) {
        const std::int64_t wide = value;
        const std::uint64_t square = static_cast<std::uint64_t>(wide * wide);
        if (total > std::numeric_limits<std::uint64_t>::max() - square) {
            throw IntegrityError("current_l2_sum_overflow");
        }
        total += square;
    }
    return total;
}

struct MoveOutcome {
    bool state_changed{false};
    bool current_changed{false};
    bool homology_changed{false};
};

struct ByteVectorLess {
    bool operator()(
        const std::vector<std::uint8_t> &left,
        const std::vector<std::uint8_t> &right
    ) const noexcept {
        const std::size_t common = std::min(left.size(), right.size());
        for (std::size_t index = 0; index < common; ++index) {
            if (left[index] < right[index]) return true;
            if (left[index] > right[index]) return false;
        }
        return left.size() < right.size();
    }
};

class SectorEngine {
  public:
    SectorEngine(
        int L,
        Seed128 seed,
        std::string start,
        DevelopmentBudget budget,
        bool development_only = true
    )
        : lattice_(L),
          S_(std::max(15, L * L)),
          rng_(seed),
          seed_(seed),
          start_(std::move(start)),
          budget_(budget),
          development_only_(development_only) {
        replicas_ = initial_replicas(start_);
        diagnostics_.swap_attempts.assign(static_cast<std::size_t>(S_), 0);
        diagnostics_.swap_accepts.assign(static_cast<std::size_t>(S_), 0);
        diagnostics_.local_current_births.assign(static_cast<std::size_t>(S_ + 1), 0);
        diagnostics_.local_current_deaths.assign(static_cast<std::size_t>(S_ + 1), 0);
        diagnostics_.local_current_vector_moves.assign(static_cast<std::size_t>(S_ + 1), 0);
        diagnostics_.local_homology_births.assign(static_cast<std::size_t>(S_ + 1), 0);
        diagnostics_.local_homology_deaths.assign(static_cast<std::size_t>(S_ + 1), 0);
        diagnostics_.local_homology_moves.assign(static_cast<std::size_t>(S_ + 1), 0);
        diagnostics_.walker_roundtrips.assign(static_cast<std::size_t>(S_ + 1), 0);
        diagnostics_.walker_phase.assign(static_cast<std::size_t>(S_ + 1), 0);
        diagnostics_.walker_phase[0] = 1;
        measured_.swap_attempts.assign(static_cast<std::size_t>(S_), 0);
        measured_.swap_accepts.assign(static_cast<std::size_t>(S_), 0);
        measured_.local_current_births.assign(static_cast<std::size_t>(S_ + 1), 0);
        measured_.local_current_deaths.assign(static_cast<std::size_t>(S_ + 1), 0);
        measured_.local_current_vector_moves.assign(static_cast<std::size_t>(S_ + 1), 0);
        measured_.local_homology_births.assign(static_cast<std::size_t>(S_ + 1), 0);
        measured_.local_homology_deaths.assign(static_cast<std::size_t>(S_ + 1), 0);
        measured_.local_homology_moves.assign(static_cast<std::size_t>(S_ + 1), 0);
        measured_.current_swap_down.assign(static_cast<std::size_t>(S_), 0);
        measured_.current_swap_up.assign(static_cast<std::size_t>(S_), 0);
        measured_.homology_swap_down.assign(static_cast<std::size_t>(S_), 0);
        measured_.homology_swap_up.assign(static_cast<std::size_t>(S_), 0);
        measured_.walker_roundtrips.assign(static_cast<std::size_t>(S_ + 1), 0);
        measured_.walker_phase.assign(static_cast<std::size_t>(S_ + 1), 0);
        boundary_delta_.assign(static_cast<std::size_t>(lattice_.n_links), 0);
        boundary_mark_.assign(static_cast<std::size_t>(lattice_.n_links), 0);
        legacy_increment_.assign(static_cast<std::size_t>(lattice_.n_plaq), 0);
        if (budget_.thin == 0 || budget_.validation_stride == 0 || budget_.checkpoints == 0
            || budget_.checkpoints > std::numeric_limits<std::uint64_t>::max() / budget_.thin) {
            throw IntegrityError("invalid_post_warm_bottom_budget");
        }
        expected_post_warm_bottom_attempts_ = budget_.checkpoints * budget_.thin;
        validate_product();
        if (budget_.warm_bottom == 0) begin_measurement();
    }

    int extent() const { return lattice_.L; }
    int levels() const { return S_; }
    const Seed128 &seed() const { return seed_; }
    const std::string &start() const { return start_; }
    const DevelopmentBudget &budget() const { return budget_; }
    const Diagnostics &diagnostics() const { return diagnostics_; }
    std::uint64_t bottom_attempts() const { return bottom_attempts_; }
    std::uint64_t emitted_checkpoints() const { return emitted_checkpoints_; }
    bool complete() const { return emitted_checkpoints_ >= budget_.checkpoints; }
    const Replica &target() const { return replicas_[0]; }

    void run(std::ostream &output) {
        emit_run(output);
        while (!complete()) {
            if (diagnostics_.transitions >= budget_.transition_cap) {
                throw IntegrityError("transition_cap_reached");
            }
            step(output);
        }
        validate_product();
        if (post_warm_bottom_attempts_ != expected_post_warm_bottom_attempts_) {
            throw IntegrityError("post_warm_bottom_budget_mismatch");
        }
        if (measured_.target_current_entries
            != measured_.local_current_births[0] + measured_.target_current_imports) {
            throw IntegrityError("target_current_entry_decomposition_mismatch");
        }
        if (measured_.target_current_exits
            != measured_.local_current_deaths[0] + measured_.target_current_exports) {
            throw IntegrityError("target_current_exit_decomposition_mismatch");
        }
        emit_summary(output);
    }

    void validate_product() const {
        if (static_cast<int>(replicas_.size()) != S_ + 1) throw IntegrityError("replica_count_mismatch");
        std::vector<int> walker_seen(static_cast<std::size_t>(S_ + 1), 0);
        for (const Replica &replica : replicas_) {
            validate_replica(lattice_, replica);
            if (replica.walker_id < 0 || replica.walker_id > S_) throw IntegrityError("walker_id_out_of_range");
            ++walker_seen[replica.walker_id];
        }
        if (std::any_of(walker_seen.begin(), walker_seen.end(), [](int count) { return count != 1; })) {
            throw IntegrityError("walker_ids_not_a_permutation");
        }
    }

    void selftest_kernel_details() {
        if (start_ != "stratified") throw IntegrityError("selftest_requires_stratified_start");
        const std::vector<std::uint8_t> zero(static_cast<std::size_t>(lattice_.n_plaq), 0);
        const Replica cold = make_replica(lattice_, zero, 0);
        selftest_orbit(cold, lattice_.cube(0), 0, 3, "cube");
        selftest_orbit(cold, lattice_.translated_plane(0, 0), 0, 3, "plane");

        const std::array<int, 4> x{{1, 1, 1, 1}};
        const int plaquette = lattice_.plaq_index(lattice_.site_index(x), 0);
        selftest_orbit(replicas_[1], lattice_.tristar(plaquette, 0), 1, 2, "tristar");

        for (int lower_score = 0; lower_score <= 2; ++lower_score) {
            for (int upper_score = 0; upper_score <= 2; ++upper_score) {
                const int difference = lower_score - upper_score;
                const unsigned denominator = difference >= 0 ? 1u : 1u << static_cast<unsigned>(-difference);
                const unsigned expected = lower_score >= upper_score
                    ? 1u : (lower_score + 1 == upper_score ? 2u : 4u);
                if (denominator != expected) throw IntegrityError("swap_score_table_failed");
            }
        }
    }

  private:
    std::vector<Replica> initial_replicas(const std::string &start) {
        std::vector<std::uint8_t> zero(static_cast<std::size_t>(lattice_.n_plaq), 0);
        std::vector<Replica> result;
        result.reserve(static_cast<std::size_t>(S_ + 1));
        if (start == "cold") {
            for (int level = 0; level <= S_; ++level) result.push_back(make_replica(lattice_, zero, level));
            return result;
        }
        if (start != "stratified") throw IntegrityError("start_must_be_cold_or_stratified");

        std::array<int, 4> x{{1, 1, 1, 1}};
        const int plaquette = lattice_.plaq_index(lattice_.site_index(x), 0);
        const SparseGenerator &generator = lattice_.tristar(plaquette, 0);
        const int a = PAIRS[0][0];
        const int b = PAIRS[0][1];
        int first_complement = -1;
        for (int axis = 0; axis < DIM; ++axis) if (axis != a && axis != b) { first_complement = axis; break; }
        if (first_complement < 0) throw IntegrityError("witness_complement_missing");
        std::array<int, 3> axes{{a, b, first_complement}};
        const int tri = triple_index(axes);
        const SparseGenerator &before_cycle = lattice_.cube(lattice_.site_index(x) * N_TRIPLES + tri);
        int central = 0;
        for (const auto &[index, coefficient] : before_cycle) if (index == plaquette) central = coefficient;
        SparseGenerator aligned_before;
        const int scale = central == 1 ? 1 : 4;
        for (const auto &[index, coefficient] : before_cycle) {
            aligned_before.emplace_back(index, static_cast<std::uint8_t>(mod5(scale * coefficient)));
        }
        std::vector<std::uint8_t> before = zero;
        for (const auto &[index, coefficient] : aligned_before) before[index] = coefficient;
        std::vector<std::uint8_t> witness = before;
        for (const auto &[index, coefficient] : generator) witness[index] = static_cast<std::uint8_t>(mod5(witness[index] + coefficient));
        Replica witness_replica = make_replica(lattice_, witness, 0);
        if (witness_replica.support != 21 || witness_replica.current_nonzero != 4) {
            throw IntegrityError("stratified_current_witness_failed");
        }
        std::vector<std::uint8_t> minus_witness = witness;
        for (auto &value : minus_witness) value = static_cast<std::uint8_t>(mod5(-value));
        std::vector<std::uint8_t> plane = zero;
        for (const auto &[index, coefficient] : lattice_.fixed_plane(0)) plane[index] = coefficient;
        std::vector<std::uint8_t> minus_plane = plane;
        for (auto &value : minus_plane) value = static_cast<std::uint8_t>(mod5(-value));
        const std::array<std::vector<std::uint8_t>, 4> starts{{witness, minus_witness, plane, minus_plane}};
        result.push_back(make_replica(lattice_, zero, 0));
        for (int level = 1; level <= S_; ++level) {
            result.push_back(make_replica(lattice_, starts[(level - 1) % 4], level));
        }
        return result;
    }

    Candidate build_candidate(const Replica &replica, const SparseGenerator &generator, int k, int level) {
        Candidate candidate;
        candidate.k = k;
        candidate.support = replica.support;
        candidate.current_nonzero = replica.current_nonzero;
        candidate.homology = replica.homology;
        candidate.homology_nonzero = replica.homology_nonzero;
        std::array<int, N_PAIRS> homology_delta{};
        for (const auto &[plaquette, coefficient] : generator) {
            const std::uint8_t old = replica.state[plaquette];
            const std::uint8_t value = static_cast<std::uint8_t>(mod5(old + k * coefficient));
            if (!hard_allowed(value)) {
                candidate.k = -1;
                return candidate;
            }
            candidate.support += static_cast<int>(value != 0) - static_cast<int>(old != 0);
            if (value != old) {
                candidate.changes.emplace_back(plaquette, value);
                homology_delta[plaquette % N_PAIRS] += static_cast<int>(value) - static_cast<int>(old);
            }
        }

        next_boundary_stamp();
        touched_links_.clear();
        for (const auto &[plaquette, value] : candidate.changes) {
            const int delta = principal(value) - principal(replica.state[plaquette]);
            if (delta == 0) continue;
            for (const auto &[link, coefficient] : lattice_.face_boundaries[plaquette]) {
                if (boundary_mark_[link] != boundary_stamp_) {
                    boundary_mark_[link] = boundary_stamp_;
                    boundary_delta_[link] = 0;
                    touched_links_.push_back(link);
                }
                boundary_delta_[link] += static_cast<int>(coefficient) * delta;
            }
        }
        for (int link : touched_links_) {
            const int delta = boundary_delta_[link];
            if (delta % 5 != 0) throw IntegrityError("orbit_candidate_current_not_integral");
            const int old = replica.current[link];
            const int value = old + delta / 5;
            if (value != old) {
                candidate.current_nonzero += static_cast<int>(value != 0) - static_cast<int>(old != 0);
                candidate.current_changes.emplace_back(link, value);
            }
        }
        const int inverse = inverse_mod5(mod5(lattice_.L * lattice_.L));
        candidate.homology_nonzero = 0;
        for (int orientation = 0; orientation < N_PAIRS; ++orientation) {
            candidate.homology[orientation] = static_cast<std::uint8_t>(mod5(
                candidate.homology[orientation] + inverse * homology_delta[orientation]
            ));
            candidate.homology_nonzero += candidate.homology[orientation] != 0;
        }
        const int score = static_cast<int>(candidate.current_nonzero != 0)
            + static_cast<int>(candidate.homology_nonzero != 0);
        candidate.exponent = level * score - candidate.support;
        return candidate;
    }

    static void apply_candidate(Replica &replica, const Candidate &candidate) {
        for (const auto &[plaquette, value] : candidate.changes) replica.state[plaquette] = value;
        for (const auto &[link, value] : candidate.current_changes) replica.current[link] = value;
        replica.support = candidate.support;
        replica.current_nonzero = candidate.current_nonzero;
        replica.homology = candidate.homology;
        replica.homology_nonzero = candidate.homology_nonzero;
    }

    std::map<std::vector<std::uint8_t>, int, ByteVectorLess> orbit_signature(
        const Replica &replica,
        const SparseGenerator &generator,
        int level
    ) {
        std::map<std::vector<std::uint8_t>, int, ByteVectorLess> signature;
        for (int k = 0; k < 5; ++k) {
            const Candidate candidate = build_candidate(replica, generator, k, level);
            if (candidate.k < 0) continue;
            Replica moved = replica;
            apply_candidate(moved, candidate);
            const auto inserted = signature.emplace(moved.state, candidate.exponent);
            if (!inserted.second) throw IntegrityError("orbit_duplicate_state");
        }
        return signature;
    }

    void selftest_orbit(
        const Replica &base,
        const SparseGenerator &generator,
        int level,
        std::size_t minimum_states,
        const char *family
    ) {
        const auto base_signature = orbit_signature(base, generator, level);
        if (base_signature.size() < minimum_states) {
            throw IntegrityError(std::string("selftest_") + family + "_orbit_too_small");
        }
        for (int k = 0; k < 5; ++k) {
            const Candidate forward = build_candidate(base, generator, k, level);
            if (forward.k < 0) continue;
            Replica moved = base;
            apply_candidate(moved, forward);
            validate_replica(lattice_, moved);
            if (orbit_signature(moved, generator, level) != base_signature) {
                throw IntegrityError(std::string("selftest_") + family + "_detail_balance_orbit_failed");
            }
            const Candidate reverse = build_candidate(moved, generator, mod5(-k), level);
            if (reverse.k < 0) {
                throw IntegrityError(std::string("selftest_") + family + "_reverse_forbidden");
            }
            apply_candidate(moved, reverse);
            if (moved.state != base.state || moved.support != base.support
                || moved.current != base.current || moved.current_nonzero != base.current_nonzero
                || moved.homology != base.homology || moved.homology_nonzero != base.homology_nonzero) {
                throw IntegrityError(std::string("selftest_") + family + "_reverse_failed");
            }
        }
    }

    MoveOutcome orbit_heatbath(Replica &replica, const SparseGenerator &generator, int level) {
        std::vector<Candidate> candidates;
        candidates.reserve(5);
        for (int k = 0; k < 5; ++k) {
            Candidate candidate = build_candidate(replica, generator, k, level);
            if (candidate.k >= 0) candidates.push_back(std::move(candidate));
        }
        if (candidates.empty()) throw IntegrityError("orbit_lost_k_zero");
        int minimum = candidates.front().exponent;
        for (const Candidate &candidate : candidates) minimum = std::min(minimum, candidate.exponent);
        std::uint64_t total = 0;
        for (Candidate &candidate : candidates) {
            const int shift = candidate.exponent - minimum;
            if (shift < 0 || shift >= 63) throw IntegrityError("orbit_integer_weight_overflow");
            candidate.weight = std::uint64_t{1} << shift;
            if (total > std::numeric_limits<std::uint64_t>::max() - candidate.weight) {
                throw IntegrityError("orbit_weight_sum_overflow");
            }
            total += candidate.weight;
        }
        const std::uint64_t draw = rng_.bounded(total);
        std::uint64_t cumulative = 0;
        Candidate *chosen = &candidates.back();
        for (Candidate &candidate : candidates) {
            cumulative += candidate.weight;
            if (draw < cumulative) {
                chosen = &candidate;
                break;
            }
        }
        MoveOutcome outcome;
        outcome.state_changed = !chosen->changes.empty();
        outcome.current_changed = !chosen->current_changes.empty();
        outcome.homology_changed = chosen->homology != replica.homology;
        apply_candidate(replica, *chosen);
        return outcome;
    }

    void next_boundary_stamp() {
        ++boundary_stamp_;
        if (boundary_stamp_ == 0) {
            std::fill(boundary_mark_.begin(), boundary_mark_.end(), 0);
            boundary_stamp_ = 1;
        }
    }

    bool legacy_step(Replica &replica) {
        std::fill(legacy_increment_.begin(), legacy_increment_.end(), 0);
        const std::uint64_t length = rng_.geometric_half();
        diagnostics_.legacy_max_word = std::max(diagnostics_.legacy_max_word, length);
        if (measurement_active_) measured_.legacy_max_word = std::max(measured_.legacy_max_word, length);
        for (std::uint64_t letter = 0; letter < length; ++letter) {
            const int kind = rng_.bit();
            const SparseGenerator &generator = kind == 0
                ? lattice_.cube(static_cast<int>(rng_.bounded(static_cast<std::uint64_t>(lattice_.n_cubes))))
                : lattice_.fixed_plane(static_cast<int>(rng_.bounded(N_PAIRS)));
            const int sign = rng_.bit() == 0 ? 1 : 4;
            for (const auto &[plaquette, coefficient] : generator) {
                legacy_increment_[plaquette] = static_cast<std::uint8_t>(mod5(
                    legacy_increment_[plaquette] + sign * coefficient
                ));
            }
        }
        int support_delta = 0;
        bool changed = false;
        for (int plaquette = 0; plaquette < lattice_.n_plaq; ++plaquette) {
            if (legacy_increment_[plaquette] == 0) continue;
            const std::uint8_t old = replica.state[plaquette];
            const std::uint8_t value = static_cast<std::uint8_t>(mod5(old + legacy_increment_[plaquette]));
            if (!hard_allowed(value)) {
                ++diagnostics_.legacy_firewall_rejects;
                if (measurement_active_) ++measured_.legacy_firewall_rejects;
                return false;
            }
            support_delta += static_cast<int>(value != 0) - static_cast<int>(old != 0);
            changed = changed || value != old;
        }
        if (support_delta > 0) {
            for (int index = 0; index < support_delta; ++index) {
                if (rng_.bit() != 0) {
                    ++diagnostics_.legacy_metropolis_rejects;
                    if (measurement_active_) ++measured_.legacy_metropolis_rejects;
                    return false;
                }
            }
        }
        if (changed) {
            for (int plaquette = 0; plaquette < lattice_.n_plaq; ++plaquette) {
                replica.state[plaquette] = static_cast<std::uint8_t>(mod5(
                    replica.state[plaquette] + legacy_increment_[plaquette]
                ));
            }
            const int walker = replica.walker_id;
            replica = make_replica(lattice_, std::move(replica.state), walker);
        }
        ++diagnostics_.legacy_accepts;
        if (measurement_active_) ++measured_.legacy_accepts;
        return changed;
    }

    void record_local_change(
        int level,
        bool old_current_nonzero,
        const std::array<std::uint8_t, N_PAIRS> &old_homology,
        bool current_vector_changed
    ) {
        const Replica &replica = replicas_[level];
        const bool new_current_nonzero = replica.current_nonzero != 0;
        const bool birth = !old_current_nonzero && new_current_nonzero;
        const bool death = old_current_nonzero && !new_current_nonzero;
        const bool homology_changed = replica.homology != old_homology;
        const bool old_homology_nonzero = std::any_of(
            old_homology.begin(), old_homology.end(), [](std::uint8_t value) { return value != 0; }
        );
        const bool new_homology_nonzero = replica.homology_nonzero != 0;
        const bool homology_birth = !old_homology_nonzero && new_homology_nonzero;
        const bool homology_death = old_homology_nonzero && !new_homology_nonzero;
        if (birth) ++diagnostics_.local_current_births[level];
        if (death) ++diagnostics_.local_current_deaths[level];
        if (current_vector_changed) ++diagnostics_.local_current_vector_moves[level];
        if (homology_birth) ++diagnostics_.local_homology_births[level];
        if (homology_death) ++diagnostics_.local_homology_deaths[level];
        if (homology_changed) ++diagnostics_.local_homology_moves[level];
        if (measurement_active_) {
            if (birth) ++measured_.local_current_births[level];
            if (death) ++measured_.local_current_deaths[level];
            if (current_vector_changed) ++measured_.local_current_vector_moves[level];
            if (homology_birth) ++measured_.local_homology_births[level];
            if (homology_death) ++measured_.local_homology_deaths[level];
            if (homology_changed) ++measured_.local_homology_moves[level];
        }
    }

    void record_target_transition(bool old_current_nonzero) {
        const bool new_current_nonzero = replicas_[0].current_nonzero != 0;
        if (!old_current_nonzero && new_current_nonzero) ++diagnostics_.target_current_entries;
        if (old_current_nonzero && !new_current_nonzero) ++diagnostics_.target_current_exits;
        if (measurement_active_) {
            if (!old_current_nonzero && new_current_nonzero) ++measured_.target_current_entries;
            if (old_current_nonzero && !new_current_nonzero) ++measured_.target_current_exits;
        }
    }

    bool sector_swap_accept(const Replica &lower, const Replica &upper) {
        const int exponent = lower.score() - upper.score();
        if (exponent >= 0) return true;
        return rng_.bits(static_cast<unsigned>(-exponent)) == 0;
    }

    void update_walker_endpoint(int level) {
        const int walker = replicas_[level].walker_id;
        if (level == 0) {
            if (diagnostics_.walker_phase[walker] == 2) ++diagnostics_.walker_roundtrips[walker];
            diagnostics_.walker_phase[walker] = 1;
            if (measurement_active_) {
                if (measured_.walker_phase[walker] == 2) ++measured_.walker_roundtrips[walker];
                measured_.walker_phase[walker] = 1;
            }
        } else if (level == S_) {
            if (diagnostics_.walker_phase[walker] == 1) diagnostics_.walker_phase[walker] = 2;
            if (measurement_active_ && measured_.walker_phase[walker] == 1) measured_.walker_phase[walker] = 2;
        }
    }

    void begin_measurement() {
        if (measurement_active_) throw IntegrityError("measurement_started_twice");
        measurement_active_ = true;
        measurement_start_transition_ = diagnostics_.transitions;
        std::fill(measured_.walker_phase.begin(), measured_.walker_phase.end(), 0);
        measured_.walker_phase[replicas_[0].walker_id] = 1;
        census_baseline_ready_ = false;
        checkpoint_baseline_ready_ = false;
    }

    void conjugate(Replica &replica) {
        if (replica.support == 0) return;
        for (auto &value : replica.state) value = static_cast<std::uint8_t>(mod5(-value));
        for (int &value : replica.current) value = -value;
        for (auto &value : replica.homology) value = static_cast<std::uint8_t>(mod5(-value));
    }

    void step(std::ostream &output) {
        const int selector = static_cast<int>(rng_.bits(4));
        const bool old_target_current = replicas_[0].current_nonzero != 0;
        bool target_touched = false;
        bool bottom_attempt = false;
        bool bottom_accepted = false;
        Family family = Family::Hold;

        if (selector == 0) {
            family = Family::Hold;
        } else if (selector == 1) {
            family = Family::Legacy;
            const bool old_current = replicas_[0].current_nonzero != 0;
            const auto old_homology = replicas_[0].homology;
            const std::vector<int> old_vector = replicas_[0].current;
            const bool changed = legacy_step(replicas_[0]);
            record_local_change(0, old_current, old_homology, old_vector != replicas_[0].current);
            target_touched = changed;
        } else if (selector == 2) {
            family = Family::Conjugation;
            const int level = static_cast<int>(rng_.bounded(static_cast<std::uint64_t>(S_ + 1)));
            const bool old_current = replicas_[level].current_nonzero != 0;
            const auto old_homology = replicas_[level].homology;
            const bool current_changed = replicas_[level].current_nonzero != 0;
            const bool changed = replicas_[level].support != 0;
            conjugate(replicas_[level]);
            record_local_change(level, old_current, old_homology, current_changed);
            target_touched = level == 0 && changed;
        } else if (selector >= 3 && selector <= 5) {
            family = Family::Cube;
            const int level = static_cast<int>(rng_.bounded(static_cast<std::uint64_t>(S_ + 1)));
            const bool old_current = replicas_[level].current_nonzero != 0;
            const auto old_homology = replicas_[level].homology;
            const auto &generator = lattice_.cube(static_cast<int>(rng_.bounded(static_cast<std::uint64_t>(lattice_.n_cubes))));
            const MoveOutcome outcome = orbit_heatbath(replicas_[level], generator, level);
            record_local_change(level, old_current, old_homology, outcome.current_changed);
            target_touched = level == 0 && outcome.state_changed;
        } else if (selector >= 6 && selector <= 9) {
            family = Family::Tristar;
            const int level = static_cast<int>(rng_.bounded(static_cast<std::uint64_t>(S_ + 1)));
            const int plaquette = static_cast<int>(rng_.bounded(static_cast<std::uint64_t>(lattice_.n_plaq)));
            const int omitted = static_cast<int>(rng_.bounded(4));
            const bool old_current = replicas_[level].current_nonzero != 0;
            const auto old_homology = replicas_[level].homology;
            const MoveOutcome outcome = orbit_heatbath(replicas_[level], lattice_.tristar(plaquette, omitted), level);
            record_local_change(level, old_current, old_homology, outcome.current_changed);
            target_touched = level == 0 && outcome.state_changed;
        } else if (selector == 10 || selector == 11) {
            family = Family::Homology;
            const int level = static_cast<int>(rng_.bounded(static_cast<std::uint64_t>(S_ + 1)));
            const int orientation = static_cast<int>(rng_.bounded(N_PAIRS));
            const int translation = static_cast<int>(rng_.bounded(static_cast<std::uint64_t>(lattice_.L * lattice_.L)));
            const bool old_current = replicas_[level].current_nonzero != 0;
            const auto old_homology = replicas_[level].homology;
            const MoveOutcome outcome = orbit_heatbath(
                replicas_[level], lattice_.translated_plane(orientation, translation), level
            );
            record_local_change(level, old_current, old_homology, outcome.current_changed);
            target_touched = level == 0 && outcome.state_changed;
        } else {
            family = Family::Swap;
            const int level = static_cast<int>(rng_.bounded(static_cast<std::uint64_t>(S_)));
            ++diagnostics_.swap_attempts[level];
            if (measurement_active_) ++measured_.swap_attempts[level];
            const bool lower_current = replicas_[level].current_nonzero != 0;
            const bool upper_current = replicas_[level + 1].current_nonzero != 0;
            const bool lower_homology = replicas_[level].homology_nonzero != 0;
            const bool upper_homology = replicas_[level + 1].homology_nonzero != 0;
            const bool accepted = sector_swap_accept(replicas_[level], replicas_[level + 1]);
            if (accepted) {
                std::swap(replicas_[level], replicas_[level + 1]);
                ++diagnostics_.swap_accepts[level];
                if (measurement_active_) {
                    ++measured_.swap_accepts[level];
                    if (lower_current) ++measured_.current_swap_up[level];
                    if (upper_current) ++measured_.current_swap_down[level];
                    if (lower_homology) ++measured_.homology_swap_up[level];
                    if (upper_homology) ++measured_.homology_swap_down[level];
                    if (level == 0 && !lower_current && upper_current) {
                        ++measured_.target_current_imports;
                    }
                    if (level == 0 && lower_current && !upper_current) {
                        ++measured_.target_current_exports;
                    }
                }
                update_walker_endpoint(level);
                update_walker_endpoint(level + 1);
                target_touched = level == 0;
            }
            if (level == 0) {
                bottom_attempt = true;
                bottom_accepted = accepted;
            }
        }

        ++diagnostics_.transitions;
        ++diagnostics_.family_attempts[static_cast<int>(family)];
        if (measurement_active_) {
            ++measured_.transitions;
            ++measured_.family_attempts[static_cast<int>(family)];
        }
        if (target_touched) record_target_transition(old_target_current);
        if (bottom_attempt) handle_bottom_checkpoint(output, bottom_accepted);
    }

    void validate_walker_permutation() const {
        std::vector<int> seen(static_cast<std::size_t>(S_ + 1), 0);
        for (const Replica &replica : replicas_) {
            if (replica.walker_id < 0 || replica.walker_id > S_) throw IntegrityError("walker_id_out_of_range");
            ++seen[replica.walker_id];
        }
        if (std::any_of(seen.begin(), seen.end(), [](int count) { return count != 1; })) {
            throw IntegrityError("walker_ids_not_a_permutation");
        }
    }

    int census_quartile(std::uint64_t one_based_index) const {
        if (one_based_index == 0 || one_based_index > expected_post_warm_bottom_attempts_) {
            throw IntegrityError("census_index_out_of_range");
        }
        const std::uint64_t quotient = expected_post_warm_bottom_attempts_ / 4;
        const std::uint64_t remainder = expected_post_warm_bottom_attempts_ % 4;
        for (int quartile = 0; quartile < 4; ++quartile) {
            const std::uint64_t k = static_cast<std::uint64_t>(quartile + 1);
            const std::uint64_t boundary = k * quotient + (k * remainder) / 4;
            if (one_based_index <= boundary) return quartile;
        }
        throw IntegrityError("census_quartile_failure");
    }

    void handle_bottom_checkpoint(std::ostream &output, bool accepted) {
        ++bottom_attempts_;
        const Replica &target = replicas_[0];
        const bool current_nonzero = target.current_nonzero != 0;
        const auto homology = target.homology;
        if (!measurement_active_) {
            if (bottom_attempts_ != budget_.warm_bottom) return;
            begin_measurement();
            return;
        }

        ++post_warm_bottom_attempts_;
        const int quartile = census_quartile(post_warm_bottom_attempts_);
        const bool emit_now = post_warm_bottom_attempts_ % budget_.thin == 0;
        const bool validate_now = post_warm_bottom_attempts_ == 1
            || post_warm_bottom_attempts_ % budget_.validation_stride == 0
            || emit_now;
        if (validate_now) {
            validate_replica(lattice_, target);
            validate_walker_permutation();
            ++bottom_target_validations_;
            if (emit_now) ++checkpoint_target_validations_;
        }

        if (census_baseline_ready_) {
            if (!last_census_current_ && current_nonzero) {
                ++bottom_census_current_entries_;
                ++quartile_current_entries_[quartile];
            }
            if (last_census_current_ && !current_nonzero) {
                ++bottom_census_current_exits_;
                ++quartile_current_exits_[quartile];
            }
            for (int index = 0; index < N_PAIRS; ++index) {
                if (homology[index] != last_census_homology_[index]) {
                    ++homology_component_changes_[index];
                    ++quartile_homology_component_changes_[quartile][index];
                }
            }
        } else {
            census_baseline_ready_ = true;
        }
        last_census_current_ = current_nonzero;
        last_census_homology_ = homology;

        if (current_nonzero) {
            ++nonzero_current_bottom_censuses_;
            ++quartile_nonzero_current_censuses_[quartile];
            nonzero_current_hashes_.insert(current_hash(target));
            nonzero_current_walkers_.insert(target.walker_id);
            ++current_excursion_;
            zero_wait_ = 0;
            max_current_excursion_ = std::max(max_current_excursion_, current_excursion_);
        } else {
            ++zero_wait_;
            current_excursion_ = 0;
            max_zero_wait_ = std::max(max_zero_wait_, zero_wait_);
        }
        for (int index = 0; index < N_PAIRS; ++index) {
            homology_value_masks_[index] |= static_cast<std::uint8_t>(1u << homology[index]);
            quartile_homology_value_masks_[quartile][index] |= static_cast<std::uint8_t>(1u << homology[index]);
        }
        homology_vectors_.insert(homology);
        quartile_homology_vectors_[quartile].insert(homology);
        unique_state_hashes_.insert(state_hash(target));

        if (!checkpoint_baseline_ready_) {
            checkpoint_baseline_ready_ = true;
            last_checkpoint_current_ = current_nonzero;
        }
        if (!emit_now) return;

        ++emitted_checkpoints_;
        if (current_nonzero) ++nonzero_current_checkpoints_;
        if (!last_checkpoint_current_ && current_nonzero) ++checkpoint_current_entries_;
        if (last_checkpoint_current_ && !current_nonzero) ++checkpoint_current_exits_;
        last_checkpoint_current_ = current_nonzero;
        emit_checkpoint(output, accepted);
    }

    void emit_run(std::ostream &output) const {
        output
            << "{\"L\":" << lattice_.L
            << ",\"S\":" << S_
            << ",\"bitstream_domain\":" << json_string(BITSTREAM_DOMAIN)
            << ",\"checkpoints\":" << budget_.checkpoints
            << ",\"development_only\":" << (development_only_ ? "true" : "false")
            << ",\"legacy_selector_probability\":\"1/16\""
            << ",\"seed\":" << json_string("0x" + seed_hex(seed_))
            << ",\"start\":" << json_string(start_)
            << ",\"thin\":" << budget_.thin
            << ",\"transition_cap\":" << budget_.transition_cap
            << ",\"type\":\"run\""
            << ",\"validation_stride\":" << budget_.validation_stride
            << ",\"warm_bottom\":" << budget_.warm_bottom
            << "}\n";
    }

    void emit_checkpoint(std::ostream &output, bool accepted) const {
        const Replica &target = replicas_[0];
        const std::string j_hash = target.current_nonzero ? current_hash(target) : std::string();
        output
            << "{\"L\":" << lattice_.L
            << ",\"checkpoint\":" << emitted_checkpoints_
            << ",\"current_hash\":" << json_string(j_hash)
            << ",\"current_nonzero\":" << static_cast<int>(target.current_nonzero != 0)
            << ",\"homology\":" << homology_json(target.homology)
            << ",\"j_nnz\":" << target.current_nonzero
            << ",\"j2_sum\":" << current_l2_sum(target)
            << ",\"n_sum\":" << principal_sum(target)
            << ",\"post_warm_bottom_attempt\":" << post_warm_bottom_attempts_
            << ",\"state_sha256\":" << json_string(state_hash(target))
            << ",\"support\":" << target.support
            << ",\"swap_accepted\":" << static_cast<int>(accepted)
            << ",\"transition\":" << diagnostics_.transitions
            << ",\"type\":\"checkpoint\""
            << ",\"walker_id\":" << target.walker_id
            << "}\n";
    }

    std::string family_attempts_json(
        const std::array<std::uint64_t, static_cast<int>(Family::Count)> &counts
    ) const {
        std::ostringstream output;
        output.imbue(std::locale::classic());
        output << '{';
        for (int index = 0; index < static_cast<int>(Family::Count); ++index) {
            if (index != 0) output << ',';
            output << json_string(FAMILY_NAMES[index]) << ':' << counts[index];
        }
        output << '}';
        return output.str();
    }

    std::string quartile_homology_changes_json() const {
        std::ostringstream output;
        output.imbue(std::locale::classic());
        output << '[';
        for (int quartile = 0; quartile < 4; ++quartile) {
            if (quartile != 0) output << ',';
            output << '[';
            for (int component = 0; component < N_PAIRS; ++component) {
                if (component != 0) output << ',';
                output << quartile_homology_component_changes_[quartile][component];
            }
            output << ']';
        }
        output << ']';
        return output.str();
    }

    std::string quartile_homology_values_json() const {
        std::ostringstream output;
        output.imbue(std::locale::classic());
        output << '[';
        for (int quartile = 0; quartile < 4; ++quartile) {
            if (quartile != 0) output << ',';
            output << '[';
            for (int component = 0; component < N_PAIRS; ++component) {
                if (component != 0) output << ',';
                output << '[';
                bool first = true;
                for (int value = 0; value < 5; ++value) {
                    if ((quartile_homology_value_masks_[quartile][component] & (1u << value)) == 0) continue;
                    if (!first) output << ',';
                    output << value;
                    first = false;
                }
                output << ']';
            }
            output << ']';
        }
        output << ']';
        return output.str();
    }

    std::string homology_values_json() const {
        std::ostringstream output;
        output.imbue(std::locale::classic());
        output << '[';
        for (int index = 0; index < N_PAIRS; ++index) {
            if (index != 0) output << ',';
            output << '[';
            bool first = true;
            for (int value = 0; value < 5; ++value) {
                if ((homology_value_masks_[index] & (1u << value)) == 0) continue;
                if (!first) output << ',';
                output << value;
                first = false;
            }
            output << ']';
        }
        output << ']';
        return output.str();
    }

    std::string string_set_json(const std::set<std::string> &values) const {
        std::ostringstream output;
        output.imbue(std::locale::classic());
        output << '[';
        bool first = true;
        for (const std::string &value : values) {
            if (!first) output << ',';
            output << json_string(value);
            first = false;
        }
        output << ']';
        return output.str();
    }

    std::string int_set_json(const std::set<int> &values) const {
        std::vector<int> ordered(values.begin(), values.end());
        return integer_vector_json(ordered);
    }

    void emit_summary(std::ostream &output) const {
        const Replica &target = replicas_[0];
        const std::uint64_t total_roundtrips = std::accumulate(
            diagnostics_.walker_roundtrips.begin(), diagnostics_.walker_roundtrips.end(), std::uint64_t{0}
        );
        const std::uint64_t measured_roundtrips = std::accumulate(
            measured_.walker_roundtrips.begin(), measured_.walker_roundtrips.end(), std::uint64_t{0}
        );
        output
            << "{\"L\":" << lattice_.L
            << ",\"S\":" << S_
            << ",\"bottom_attempts\":" << bottom_attempts_
            << ",\"bottom_census_current_entries\":" << bottom_census_current_entries_
            << ",\"bottom_census_current_exits\":" << bottom_census_current_exits_
            << ",\"bottom_target_validations\":" << bottom_target_validations_
            << ",\"checkpoint_current_entries\":" << checkpoint_current_entries_
            << ",\"checkpoint_current_exits\":" << checkpoint_current_exits_
            << ",\"checkpoint_target_validations\":" << checkpoint_target_validations_
            << ",\"checkpoints\":" << emitted_checkpoints_
            << ",\"distinct_H2_vectors\":" << homology_vectors_.size()
            << ",\"distinct_nonzero_current_hashes\":" << nonzero_current_hashes_.size()
            << ",\"distinct_nonzero_current_walkers\":" << nonzero_current_walkers_.size()
            << ",\"final_homology\":" << homology_json(target.homology)
            << ",\"final_state_sha256\":" << json_string(state_hash(target))
            << ",\"final_support\":" << target.support
            << ",\"homology_component_changes\":" << integer_vector_json(std::vector<std::uint64_t>(homology_component_changes_.begin(), homology_component_changes_.end()))
            << ",\"homology_visited_values\":" << homology_values_json()
            << ",\"max_current_excursion_bottom_attempts\":" << max_current_excursion_
            << ",\"max_zero_wait_bottom_attempts\":" << max_zero_wait_
            << ",\"measured_current_swap_down\":" << integer_vector_json(measured_.current_swap_down)
            << ",\"measured_current_swap_up\":" << integer_vector_json(measured_.current_swap_up)
            << ",\"measured_family_attempts\":" << family_attempts_json(measured_.family_attempts)
            << ",\"measured_homology_swap_down\":" << integer_vector_json(measured_.homology_swap_down)
            << ",\"measured_homology_swap_up\":" << integer_vector_json(measured_.homology_swap_up)
            << ",\"measured_legacy_accepts\":" << measured_.legacy_accepts
            << ",\"measured_legacy_firewall_rejects\":" << measured_.legacy_firewall_rejects
            << ",\"measured_legacy_max_word\":" << measured_.legacy_max_word
            << ",\"measured_legacy_metropolis_rejects\":" << measured_.legacy_metropolis_rejects
            << ",\"measured_local_current_births\":" << integer_vector_json(measured_.local_current_births)
            << ",\"measured_local_current_deaths\":" << integer_vector_json(measured_.local_current_deaths)
            << ",\"measured_local_current_vector_moves\":" << integer_vector_json(measured_.local_current_vector_moves)
            << ",\"measured_local_homology_births\":" << integer_vector_json(measured_.local_homology_births)
            << ",\"measured_local_homology_deaths\":" << integer_vector_json(measured_.local_homology_deaths)
            << ",\"measured_local_homology_moves\":" << integer_vector_json(measured_.local_homology_moves)
            << ",\"measured_roundtrips\":" << measured_roundtrips
            << ",\"measured_swap_accepts\":" << integer_vector_json(measured_.swap_accepts)
            << ",\"measured_swap_attempts\":" << integer_vector_json(measured_.swap_attempts)
            << ",\"measured_target_current_entries\":" << measured_.target_current_entries
            << ",\"measured_target_current_exits\":" << measured_.target_current_exits
            << ",\"measured_target_current_exports\":" << measured_.target_current_exports
            << ",\"measured_target_current_imports\":" << measured_.target_current_imports
            << ",\"measured_target_local_current_births\":" << measured_.local_current_births[0]
            << ",\"measured_transitions\":" << measured_.transitions
            << ",\"measured_walker_roundtrips\":" << integer_vector_json(measured_.walker_roundtrips)
            << ",\"measurement_start_transition\":" << measurement_start_transition_
            << ",\"nonzero_current_bottom_censuses\":" << nonzero_current_bottom_censuses_
            << ",\"nonzero_current_checkpoints\":" << nonzero_current_checkpoints_
            << ",\"nonzero_current_hashes\":" << string_set_json(nonzero_current_hashes_)
            << ",\"nonzero_current_walker_ids\":" << int_set_json(nonzero_current_walkers_)
            << ",\"post_warm_bottom_attempts\":" << post_warm_bottom_attempts_
            << ",\"product_validations\":2"
            << ",\"quartile_current_entries\":" << integer_vector_json(std::vector<std::uint64_t>(quartile_current_entries_.begin(), quartile_current_entries_.end()))
            << ",\"quartile_current_exits\":" << integer_vector_json(std::vector<std::uint64_t>(quartile_current_exits_.begin(), quartile_current_exits_.end()))
            << ",\"quartile_H2_component_changes\":" << quartile_homology_changes_json()
            << ",\"quartile_H2_vector_counts\":" << integer_vector_json(std::vector<std::uint64_t>{
                static_cast<std::uint64_t>(quartile_homology_vectors_[0].size()),
                static_cast<std::uint64_t>(quartile_homology_vectors_[1].size()),
                static_cast<std::uint64_t>(quartile_homology_vectors_[2].size()),
                static_cast<std::uint64_t>(quartile_homology_vectors_[3].size())
            })
            << ",\"quartile_H2_visited_values\":" << quartile_homology_values_json()
            << ",\"quartile_nonzero_current_censuses\":" << integer_vector_json(std::vector<std::uint64_t>(quartile_nonzero_current_censuses_.begin(), quartile_nonzero_current_censuses_.end()))
            << ",\"state_hashes\":" << unique_state_hashes_.size()
            << ",\"thin\":" << budget_.thin
            << ",\"total_family_attempts\":" << family_attempts_json(diagnostics_.family_attempts)
            << ",\"total_legacy_accepts\":" << diagnostics_.legacy_accepts
            << ",\"total_legacy_firewall_rejects\":" << diagnostics_.legacy_firewall_rejects
            << ",\"total_legacy_max_word\":" << diagnostics_.legacy_max_word
            << ",\"total_legacy_metropolis_rejects\":" << diagnostics_.legacy_metropolis_rejects
            << ",\"total_local_current_births\":" << integer_vector_json(diagnostics_.local_current_births)
            << ",\"total_local_current_deaths\":" << integer_vector_json(diagnostics_.local_current_deaths)
            << ",\"total_local_current_vector_moves\":" << integer_vector_json(diagnostics_.local_current_vector_moves)
            << ",\"total_local_homology_births\":" << integer_vector_json(diagnostics_.local_homology_births)
            << ",\"total_local_homology_deaths\":" << integer_vector_json(diagnostics_.local_homology_deaths)
            << ",\"total_local_homology_moves\":" << integer_vector_json(diagnostics_.local_homology_moves)
            << ",\"total_roundtrips\":" << total_roundtrips
            << ",\"total_swap_accepts\":" << integer_vector_json(diagnostics_.swap_accepts)
            << ",\"total_swap_attempts\":" << integer_vector_json(diagnostics_.swap_attempts)
            << ",\"total_target_current_entries\":" << diagnostics_.target_current_entries
            << ",\"total_target_current_exits\":" << diagnostics_.target_current_exits
            << ",\"total_transitions\":" << diagnostics_.transitions
            << ",\"total_walker_roundtrips\":" << integer_vector_json(diagnostics_.walker_roundtrips)
            << ",\"type\":\"summary\""
            << ",\"validation_stride\":" << budget_.validation_stride
            << "}\n";
    }

    Torus4 lattice_;
    int S_;
    BitStream rng_;
    Seed128 seed_;
    std::string start_;
    DevelopmentBudget budget_;
    bool development_only_{true};
    std::vector<Replica> replicas_;
    Diagnostics diagnostics_;
    MeasuredDiagnostics measured_;

    std::vector<int> boundary_delta_;
    std::vector<std::uint32_t> boundary_mark_;
    std::uint32_t boundary_stamp_{0};
    std::vector<int> touched_links_;
    std::vector<std::uint8_t> legacy_increment_;

    std::uint64_t bottom_attempts_{0};
    std::uint64_t post_warm_bottom_attempts_{0};
    std::uint64_t expected_post_warm_bottom_attempts_{0};
    std::uint64_t emitted_checkpoints_{0};
    std::uint64_t bottom_target_validations_{0};
    std::uint64_t checkpoint_target_validations_{0};
    std::uint64_t nonzero_current_checkpoints_{0};
    std::uint64_t nonzero_current_bottom_censuses_{0};
    std::uint64_t bottom_census_current_entries_{0};
    std::uint64_t bottom_census_current_exits_{0};
    std::uint64_t checkpoint_current_entries_{0};
    std::uint64_t checkpoint_current_exits_{0};
    bool measurement_active_{false};
    std::uint64_t measurement_start_transition_{0};
    bool census_baseline_ready_{false};
    bool checkpoint_baseline_ready_{false};
    bool last_census_current_{false};
    bool last_checkpoint_current_{false};
    std::array<std::uint8_t, N_PAIRS> last_census_homology_{};
    std::array<std::uint64_t, 4> quartile_current_entries_{};
    std::array<std::uint64_t, 4> quartile_current_exits_{};
    std::array<std::uint64_t, 4> quartile_nonzero_current_censuses_{};
    std::array<std::array<std::uint64_t, N_PAIRS>, 4> quartile_homology_component_changes_{};
    std::array<std::array<std::uint8_t, N_PAIRS>, 4> quartile_homology_value_masks_{};
    std::array<std::set<std::array<std::uint8_t, N_PAIRS>>, 4> quartile_homology_vectors_{};
    std::uint64_t zero_wait_{0};
    std::uint64_t current_excursion_{0};
    std::uint64_t max_zero_wait_{0};
    std::uint64_t max_current_excursion_{0};
    std::array<std::uint64_t, N_PAIRS> homology_component_changes_{};
    std::array<std::uint8_t, N_PAIRS> homology_value_masks_{};
    std::set<std::array<std::uint8_t, N_PAIRS>> homology_vectors_;
    std::set<std::string> nonzero_current_hashes_;
    std::set<int> nonzero_current_walkers_;
    std::set<std::string> unique_state_hashes_;
};

std::uint64_t canonical_uint(std::string_view text, const char *name) {
    if (text.empty() || (text.size() > 1 && text.front() == '0')) {
        throw IntegrityError(std::string(name) + "_not_canonical_decimal");
    }
    std::uint64_t result = 0;
    for (unsigned char character : text) {
        if (!std::isdigit(character)) throw IntegrityError(std::string(name) + "_not_decimal");
        const unsigned digit = character - '0';
        if (result > (std::numeric_limits<std::uint64_t>::max() - digit) / 10) {
            throw IntegrityError(std::string(name) + "_decimal_overflow");
        }
        result = result * 10 + digit;
    }
    return result;
}

void require(bool condition, const char *message) {
    if (!condition) throw IntegrityError(message);
}

void selftest_qualification_firewall() {
    std::set<std::string> tuples;
    std::set<std::string> tokens;
    for (const auto &spec : FORMAL_SPECS) {
        const Seed128 parsed = parse_seed(spec.seed_token);
        require(
            qualification_spec_matches(spec.L, spec.start, spec.seed_token, parsed),
            "formal_spec_rejected"
        );
        require(
            tokens.insert(std::string(spec.seed_token)).second,
            "formal_seed_token_not_unique"
        );
        require(
            tuples.insert(
                std::to_string(spec.L) + ":" + std::string(spec.start) + ":" + std::string(spec.seed_token)
            ).second,
            "formal_spec_not_unique"
        );

        std::string uppercase_token(spec.seed_token);
        uppercase_token[2] = 'F';
        require(
            !qualification_spec_matches(spec.L, spec.start, uppercase_token, parsed),
            "noncanonical_formal_seed_accepted"
        );
        require(
            !qualification_spec_matches(7 - spec.L, spec.start, spec.seed_token, parsed),
            "wrong_formal_L_accepted"
        );
        const std::string_view other_start = spec.start == "cold" ? "stratified" : "cold";
        require(
            !qualification_spec_matches(spec.L, other_start, spec.seed_token, parsed),
            "wrong_formal_start_accepted"
        );
    }
    require(tuples.size() == 8 && tokens.size() == 8, "formal_spec_count_failed");
    require(same_budget(FORMAL_BUDGET, FORMAL_BUDGET), "formal_budget_rejected");

    DevelopmentBudget changed = FORMAL_BUDGET;
    ++changed.warm_bottom;
    require(!same_budget(changed, FORMAL_BUDGET), "wrong_formal_warm_accepted");
    changed = FORMAL_BUDGET;
    ++changed.checkpoints;
    require(!same_budget(changed, FORMAL_BUDGET), "wrong_formal_checkpoints_accepted");
    changed = FORMAL_BUDGET;
    ++changed.thin;
    require(!same_budget(changed, FORMAL_BUDGET), "wrong_formal_thin_accepted");
    changed = FORMAL_BUDGET;
    ++changed.validation_stride;
    require(!same_budget(changed, FORMAL_BUDGET), "wrong_formal_validation_stride_accepted");
    changed = FORMAL_BUDGET;
    ++changed.transition_cap;
    require(!same_budget(changed, FORMAL_BUDGET), "wrong_formal_transition_cap_accepted");

    require(valid_pin_commit("0123456789abcdef0123456789abcdef01234567"), "valid_pin_commit_rejected");
    require(!valid_pin_commit("0123456789abcdef0123456789abcdef0123456A"), "uppercase_pin_commit_accepted");
    require(
        valid_pin_receipt("https://github.com/mathorn1973/twist-j/issues/756#issuecomment-123456"),
        "valid_pin_receipt_rejected"
    );
    require(
        !valid_pin_receipt("https://github.com/mathorn1973/twist-j/issues/755#issuecomment-123456"),
        "wrong_issue_pin_receipt_accepted"
    );
    require(
        !valid_pin_receipt("https://github.com/mathorn1973/twist-j/issues/756#issuecomment-12x456"),
        "nondigit_pin_receipt_accepted"
    );
}

void run_selftest(std::ostream &output) {
    require(
        sha256(std::string_view()) == "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
        "sha256_empty_KAT_failed"
    );
    require(
        sha256("abc") == "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad",
        "sha256_abc_KAT_failed"
    );
    Seed128 seed;
    for (int index = 0; index < 16; ++index) seed.bytes[index] = static_cast<std::uint8_t>(index);
    std::array<std::uint8_t, 16> counter{};
    require(
        hex_digest(BitStream::counter_digest(seed, BITSTREAM_DOMAIN, counter))
            == "9434ecd5f984de773ffb5102bcfa3ea618482759831459004ef75d9f407db889",
        "bitstream_counter_zero_digest_failed"
    );
    counter[15] = 1;
    require(
        hex_digest(BitStream::counter_digest(seed, BITSTREAM_DOMAIN, counter))
            == "c6169ccdc799385b57004919a8bf83866a5e962068162ff7ec6971b1e58d3dbb",
        "bitstream_counter_one_digest_failed"
    );
    BitStream stream(seed);
    const std::array<std::uint64_t, 8> bounds{{1, 2, 3, 5, 7, 16, 17, 1000}};
    const std::array<std::uint64_t, 8> expected{{0, 1, 0, 0, 3, 4, 10, 38}};
    for (std::size_t index = 0; index < bounds.size(); ++index) {
        require(stream.bounded(bounds[index]) == expected[index], "bitstream_bounded_fixture_failed");
    }
    require(stream.bits(60) == 1097646845997440637ULL, "bitstream_bits_fixture_failed");

    std::array<std::uint8_t, 16> carry_counter{};
    carry_counter[15] = 0xff;
    BitStream carry_stream(seed);
    carry_stream.set_counter_for_selftest(carry_counter);
    std::vector<std::uint8_t> block255(32);
    std::vector<std::uint8_t> block256(32);
    for (auto &value : block255) value = static_cast<std::uint8_t>(carry_stream.bits(8));
    for (auto &value : block256) value = static_cast<std::uint8_t>(carry_stream.bits(8));
    require(
        hex_digest([&]() {
            std::array<std::uint8_t, 32> value{};
            std::copy(block255.begin(), block255.end(), value.begin());
            return value;
        }()) == "5bf6dbee66dcea5e20a14e16d721e71bbdf53342def66e6d7148a51365d9b22d",
        "bitstream_counter_255_fixture_failed"
    );
    require(
        hex_digest([&]() {
            std::array<std::uint8_t, 32> value{};
            std::copy(block256.begin(), block256.end(), value.begin());
            return value;
        }()) == "8ade186aa1bc73bb766ba84bcea5cf51491fbc148dfcc83d85d1cc723bfdc5bb",
        "bitstream_counter_carry_fixture_failed"
    );

    const DevelopmentBudget fixture_budget{0, 1, 1, 1, 1000};
    SectorEngine fixture3(3, seed, "stratified", fixture_budget);
    SectorEngine fixture4(4, seed, "stratified", fixture_budget);
    fixture3.validate_product();
    fixture4.validate_product();
    fixture3.selftest_kernel_details();
    fixture4.selftest_kernel_details();
    selftest_qualification_firewall();
    output
        << "{\"bitstream\":\"PASS\",\"development_only\":true"
        << ",\"detailed_balance_orbits\":\"PASS\""
        << ",\"lattice_L3\":\"PASS\",\"lattice_L4\":\"PASS\""
        << ",\"sha256\":\"PASS\",\"swap_score_table\":\"PASS\""
        << ",\"type\":\"selftest\"}\n";
}

struct Options {
    bool development{false};
    bool qualification{false};
    bool selftest{false};
    bool help{false};
    bool have_L{false};
    bool have_seed{false};
    bool have_start{false};
    bool have_warm{false};
    bool have_checkpoints{false};
    bool have_thin{false};
    bool have_validation_stride{false};
    bool have_cap{false};
    bool have_pin_commit{false};
    bool have_pin_receipt{false};
    int L{0};
    Seed128 seed{};
    std::string seed_token;
    std::string start;
    std::string pin_commit;
    std::string pin_receipt;
    DevelopmentBudget budget{};
};

void usage(std::ostream &output) {
    output
        << "usage:\n"
        << "  qualification_engine --selftest\n"
        << "  qualification_engine --development --L {3|4} --seed HEX128"
        << " --start {cold|stratified} --warm-bottom N --checkpoints N"
        << " --thin N --validation-stride N --transition-cap N\n"
        << "  qualification_engine --qualification --pin-commit HEX40"
        << " --pin-receipt ISSUE_COMMENT_URL --L {3|4} --seed HEX128"
        << " --start {cold|stratified} --warm-bottom N --checkpoints N"
        << " --thin N --validation-stride N --transition-cap N\n";
}

Options parse_options(int argc, char **argv) {
    Options options;
    auto take = [&](int &index, const char *name) -> std::string_view {
        if (index + 1 >= argc) throw IntegrityError(std::string(name) + "_missing_value");
        return argv[++index];
    };
    for (int index = 1; index < argc; ++index) {
        const std::string_view argument = argv[index];
        if (argument == "--development") {
            if (options.development) throw IntegrityError("duplicate_development_flag");
            options.development = true;
        } else if (argument == "--qualification") {
            if (options.qualification) throw IntegrityError("duplicate_qualification_flag");
            options.qualification = true;
        } else if (argument == "--selftest") {
            if (options.selftest) throw IntegrityError("duplicate_selftest_flag");
            options.selftest = true;
        } else if (argument == "--help" || argument == "-h") {
            options.help = true;
        } else if (argument == "--L") {
            if (options.have_L) throw IntegrityError("duplicate_L");
            const std::uint64_t value = canonical_uint(take(index, "L"), "L");
            if (value > static_cast<std::uint64_t>(std::numeric_limits<int>::max())) throw IntegrityError("L_out_of_range");
            options.L = static_cast<int>(value);
            options.have_L = true;
        } else if (argument == "--seed") {
            if (options.have_seed) throw IntegrityError("duplicate_seed");
            options.seed_token = std::string(take(index, "seed"));
            options.seed = parse_seed(options.seed_token);
            options.have_seed = true;
        } else if (argument == "--start") {
            if (options.have_start) throw IntegrityError("duplicate_start");
            options.start = std::string(take(index, "start"));
            options.have_start = true;
        } else if (argument == "--warm-bottom") {
            if (options.have_warm) throw IntegrityError("duplicate_warm_bottom");
            options.budget.warm_bottom = canonical_uint(take(index, "warm_bottom"), "warm_bottom");
            options.have_warm = true;
        } else if (argument == "--checkpoints") {
            if (options.have_checkpoints) throw IntegrityError("duplicate_checkpoints");
            options.budget.checkpoints = canonical_uint(take(index, "checkpoints"), "checkpoints");
            options.have_checkpoints = true;
        } else if (argument == "--thin") {
            if (options.have_thin) throw IntegrityError("duplicate_thin");
            options.budget.thin = canonical_uint(take(index, "thin"), "thin");
            options.have_thin = true;
        } else if (argument == "--validation-stride") {
            if (options.have_validation_stride) throw IntegrityError("duplicate_validation_stride");
            options.budget.validation_stride = canonical_uint(
                take(index, "validation_stride"), "validation_stride"
            );
            options.have_validation_stride = true;
        } else if (argument == "--transition-cap") {
            if (options.have_cap) throw IntegrityError("duplicate_transition_cap");
            options.budget.transition_cap = canonical_uint(take(index, "transition_cap"), "transition_cap");
            options.have_cap = true;
        } else if (argument == "--pin-commit") {
            if (options.have_pin_commit) throw IntegrityError("duplicate_pin_commit");
            options.pin_commit = std::string(take(index, "pin_commit"));
            options.have_pin_commit = true;
        } else if (argument == "--pin-receipt") {
            if (options.have_pin_receipt) throw IntegrityError("duplicate_pin_receipt");
            options.pin_receipt = std::string(take(index, "pin_receipt"));
            options.have_pin_receipt = true;
        } else {
            throw IntegrityError("unknown_argument_" + std::string(argument));
        }
    }
    return options;
}

int program_main(int argc, char **argv) {
    const Options options = parse_options(argc, argv);
    if (options.help) {
        usage(std::cout);
        return 0;
    }
    if (options.selftest) {
        if (options.development || options.qualification || options.have_L || options.have_seed || options.have_start
            || options.have_warm || options.have_checkpoints || options.have_thin
            || options.have_validation_stride || options.have_cap || options.have_pin_commit
            || options.have_pin_receipt) {
            throw IntegrityError("selftest_cannot_be_combined_with_run_arguments");
        }
        run_selftest(std::cout);
        return 0;
    }
    if (options.development == options.qualification) {
        throw IntegrityError("select_exactly_one_of_development_or_qualification");
    }
    if (!(options.have_L && options.have_seed && options.have_start && options.have_warm
        && options.have_checkpoints && options.have_thin && options.have_validation_stride
        && options.have_cap)) {
        throw IntegrityError("run_requires_all_explicit_arguments");
    }
    if (options.L != 3 && options.L != 4) throw IntegrityError("run_L_must_be_3_or_4");
    if (options.development && (options.have_pin_commit || options.have_pin_receipt)) {
        throw IntegrityError("development_forbids_pin_arguments");
    }
    if (options.qualification) {
        if (!(options.have_pin_commit && options.have_pin_receipt)) {
            throw IntegrityError("qualification_requires_pin_commit_and_receipt");
        }
        if (!valid_pin_commit(options.pin_commit)) {
            throw IntegrityError("pin_commit_must_be_lower_hex40");
        }
        if (!valid_pin_receipt(options.pin_receipt)) {
            throw IntegrityError("pin_receipt_must_be_issue_756_comment_URL");
        }
        if (!qualification_spec_matches(options.L, options.start, options.seed_token, options.seed)) {
            throw IntegrityError("qualification_spec_not_frozen");
        }
        if (!same_budget(options.budget, FORMAL_BUDGET)) {
            throw IntegrityError("qualification_schedule_not_frozen");
        }
    }
    if (options.start != "cold" && options.start != "stratified") throw IntegrityError("start_must_be_cold_or_stratified");
    if (options.budget.checkpoints == 0) throw IntegrityError("checkpoints_must_be_positive");
    if (options.budget.thin == 0) throw IntegrityError("thin_must_be_positive");
    if (options.budget.validation_stride == 0) throw IntegrityError("validation_stride_must_be_positive");
    if (options.budget.transition_cap == 0) throw IntegrityError("transition_cap_must_be_positive");
    if (options.budget.checkpoints > std::numeric_limits<std::uint64_t>::max() / options.budget.thin) {
        throw IntegrityError("post_warm_bottom_budget_overflow");
    }
    const std::uint64_t post_warm_bottom = options.budget.checkpoints * options.budget.thin;
    if (options.budget.warm_bottom > std::numeric_limits<std::uint64_t>::max() - post_warm_bottom) {
        throw IntegrityError("bottom_budget_overflow");
    }
    SectorEngine engine(
        options.L,
        options.seed,
        options.start,
        options.budget,
        options.development
    );
    engine.run(std::cout);
    if (!std::cout.good()) throw IntegrityError("stdout_write_failure");
    return 0;
}

}  // namespace qualification

int main(int argc, char **argv) {
#ifdef _WIN32
    if (_setmode(_fileno(stdout), _O_BINARY) == -1) {
        std::fprintf(stderr, "ERROR stdout_binary_mode_failed\n");
        return 2;
    }
#endif
    std::locale::global(std::locale::classic());
    std::cout.imbue(std::locale::classic());
    std::cerr.imbue(std::locale::classic());
    try {
        return qualification::program_main(argc, argv);
    } catch (const std::exception &error) {
        std::cerr << "ERROR " << error.what() << '\n';
        return 2;
    }
}
