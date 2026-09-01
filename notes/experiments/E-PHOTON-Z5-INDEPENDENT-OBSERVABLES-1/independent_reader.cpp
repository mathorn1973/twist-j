#include <algorithm>
#include <array>
#include <cctype>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <fstream>
#include <functional>
#include <iomanip>
#include <iostream>
#include <limits>
#include <locale>
#include <sstream>
#include <stdexcept>
#include <string>
#include <string_view>
#include <unordered_map>
#include <utility>
#include <vector>

#ifdef _WIN32
#include <fcntl.h>
#include <io.h>
#endif

namespace photon_reader {

constexpr int DIM = 4;
constexpr int NPAIR = 6;
constexpr std::array<std::array<int, 2>, NPAIR> PAIRS{{
    {{0, 1}}, {{0, 2}}, {{0, 3}}, {{1, 2}}, {{1, 3}}, {{2, 3}},
}};
constexpr std::array<std::array<int, 3>, 4> TRIPLES{{
    {{0, 1, 2}}, {{0, 1, 3}}, {{0, 2, 3}}, {{1, 2, 3}},
}};
constexpr std::uint64_t FNVLIKE_OFFSET = 1469598103934665603ULL;
constexpr std::uint64_t FNVLIKE_PRIME = 1099511628211ULL;
// Seven canonical lines at L=32, a 64-byte CHAIN token and two uint64 maxima.
constexpr std::streamoff MAX_CANONICAL_STATE_BYTES = 4194475;

class IntegrityError : public std::runtime_error {
  public:
    explicit IntegrityError(const std::string &message) : std::runtime_error(message) {}
};

int mod5(int value) {
    value %= 5;
    return value < 0 ? value + 5 : value;
}

int principal5(std::uint8_t value) {
    static constexpr std::array<int, 5> PRINCIPAL{{0, 1, 2, -2, -1}};
    if (value >= PRINCIPAL.size()) throw IntegrityError("flux_residue_out_of_range");
    return PRINCIPAL[value];
}

int pair_index(int a, int b) {
    if (a > b) std::swap(a, b);
    for (int index = 0; index < NPAIR; ++index) {
        if (PAIRS[index][0] == a && PAIRS[index][1] == b) return index;
    }
    throw IntegrityError("invalid_orientation_pair");
}

int levi_sign(const std::array<int, 4> &axes) {
    int inversions = 0;
    for (int i = 0; i < 4; ++i) {
        for (int j = i + 1; j < 4; ++j) {
            if (axes[i] > axes[j]) ++inversions;
        }
    }
    return (inversions & 1) ? -1 : 1;
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

    void update(const std::string &data) {
        update(reinterpret_cast<const std::uint8_t *>(data.data()), data.size());
    }

    void update(const std::vector<std::uint8_t> &data) {
        update(data.data(), data.size());
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

std::string sha256(const std::string &data) {
    Sha256 hash;
    hash.update(data);
    return hex_digest(hash.final());
}

std::string sha256(const std::vector<std::uint8_t> &data) {
    Sha256 hash;
    hash.update(data);
    return hex_digest(hash.final());
}

bool canonical_sha256(std::string_view value) {
    if (value.size() != 64) return false;
    return std::all_of(value.begin(), value.end(), [](unsigned char character) {
        return (character >= '0' && character <= '9')
            || (character >= 'a' && character <= 'f');
    });
}

std::uint64_t canonical_uint(std::string_view value, const char *name) {
    if (value.empty() || (value.size() > 1 && value.front() == '0')) {
        throw IntegrityError(std::string(name) + "_not_canonical_decimal");
    }
    std::uint64_t result = 0;
    for (unsigned char character : value) {
        if (!std::isdigit(character)) {
            throw IntegrityError(std::string(name) + "_not_canonical_decimal");
        }
        const unsigned digit = character - '0';
        if (result > (std::numeric_limits<std::uint64_t>::max() - digit) / 10) {
            throw IntegrityError(std::string(name) + "_decimal_overflow");
        }
        result = result * 10 + digit;
    }
    return result;
}

struct LinkState {
    std::uint32_t L{};
    std::string chain;
    std::uint64_t sample{};
    std::uint64_t macrocycle{};
    std::vector<std::uint8_t> links;
    std::string file_sha256;
    std::uint64_t file_bytes{};
};

std::string_view after_prefix(std::string_view line, std::string_view prefix, const char *name) {
    if (!line.starts_with(prefix)) throw IntegrityError(std::string(name) + "_record_mismatch");
    return line.substr(prefix.size());
}

LinkState parse_state_bytes(const std::string &data, const std::string &expected_sha256) {
    if (!canonical_sha256(expected_sha256)) throw IntegrityError("expected_sha256_not_canonical");
    const std::string actual_sha256 = sha256(data);
    if (actual_sha256 != expected_sha256) throw IntegrityError("state_file_sha256_mismatch");
    if (data.empty() || data.back() != '\n' || data.find('\r') != std::string::npos) {
        throw IntegrityError("state_not_LF_with_final_LF");
    }
    for (unsigned char character : data) {
        if (character != '\n' && (character < 32 || character > 126)) {
            throw IntegrityError("state_not_printable_ASCII");
        }
    }
    std::vector<std::string_view> lines;
    std::size_t begin = 0;
    while (begin < data.size()) {
        const std::size_t end = data.find('\n', begin);
        if (end == std::string::npos) throw IntegrityError("state_line_split_failure");
        lines.emplace_back(data.data() + begin, end - begin);
        begin = end + 1;
    }
    if (lines.size() != 7) throw IntegrityError("state_record_count_mismatch");
    if (lines[0] != "TWISTJ_Z5_LINK_STATE_V1") throw IntegrityError("state_magic_mismatch");
    if (lines[6] != "END") throw IntegrityError("state_END_mismatch");

    const std::uint64_t L64 = canonical_uint(after_prefix(lines[1], "L=", "L"), "L");
    if (L64 < 2 || L64 > 32) throw IntegrityError("L_outside_frozen_reader_scope");
    const std::string_view chain = after_prefix(lines[2], "CHAIN=", "CHAIN");
    if (chain.empty() || chain.size() > 64
        || !std::isalnum(static_cast<unsigned char>(chain.front()))) {
        throw IntegrityError("CHAIN_not_canonical_token");
    }
    for (unsigned char character : chain) {
        if (!std::isalnum(character) && character != '_' && character != '.' && character != '-') {
            throw IntegrityError("CHAIN_not_canonical_token");
        }
    }
    const std::uint64_t sample = canonical_uint(
        after_prefix(lines[3], "SAMPLE=", "SAMPLE"), "SAMPLE"
    );
    const std::uint64_t macrocycle = canonical_uint(
        after_prefix(lines[4], "MACROCYCLE=", "MACROCYCLE"), "MACROCYCLE"
    );
    const std::string_view link_digits = after_prefix(lines[5], "LINKS=", "LINKS");
    const std::uint64_t volume = L64 * L64 * L64 * L64;
    const std::uint64_t link_count = DIM * volume;
    if (link_digits.size() != link_count) throw IntegrityError("LINKS_length_mismatch");
    std::vector<std::uint8_t> links;
    links.reserve(static_cast<std::size_t>(link_count));
    for (unsigned char character : link_digits) {
        if (character < '0' || character > '4') throw IntegrityError("LINKS_residue_out_of_range");
        links.push_back(static_cast<std::uint8_t>(character - '0'));
    }

    std::string canonical;
    canonical.reserve(data.size());
    canonical += "TWISTJ_Z5_LINK_STATE_V1\nL=";
    canonical += std::to_string(L64);
    canonical += "\nCHAIN=";
    canonical.append(chain);
    canonical += "\nSAMPLE=";
    canonical += std::to_string(sample);
    canonical += "\nMACROCYCLE=";
    canonical += std::to_string(macrocycle);
    canonical += "\nLINKS=";
    for (std::uint8_t value : links) {
        canonical.push_back(static_cast<char>('0' + value));
    }
    canonical += "\nEND\n";
    if (canonical != data) throw IntegrityError("state_canonical_reserialization_mismatch");

    LinkState state;
    state.L = static_cast<std::uint32_t>(L64);
    state.chain.assign(chain);
    state.sample = sample;
    state.macrocycle = macrocycle;
    state.links = std::move(links);
    state.file_sha256 = actual_sha256;
    state.file_bytes = data.size();
    return state;
}

LinkState read_state(const std::string &path, const std::string &expected_sha256) {
    std::ifstream input(path, std::ios::binary);
    if (!input) throw IntegrityError("state_file_open_failed");
    input.seekg(0, std::ios::end);
    const std::streamoff length = input.tellg();
    if (length < 0) throw IntegrityError("state_file_size_failed");
    if (length > MAX_CANONICAL_STATE_BYTES) {
        throw IntegrityError("state_file_exceeds_canonical_L32_maximum");
    }
    input.seekg(0, std::ios::beg);
    std::string data(static_cast<std::size_t>(length), '\0');
    if (!data.empty()) input.read(data.data(), length);
    if (!input || input.peek() != std::char_traits<char>::eof()) {
        throw IntegrityError("state_file_read_failed");
    }
    return parse_state_bytes(data, expected_sha256);
}

class Geometry {
  public:
    explicit Geometry(std::uint32_t linear_size) : L(linear_size), volume(1) {
        for (int mu = DIM - 1; mu >= 0; --mu) {
            stride[mu] = volume;
            volume *= L;
        }
    }

    std::uint32_t coordinate(std::uint64_t site, int mu) const {
        return static_cast<std::uint32_t>((site / stride[mu]) % L);
    }

    std::uint64_t shift(std::uint64_t site, int mu, int delta = 1) const {
        int coordinate_value = static_cast<int>(coordinate(site, mu));
        int shifted = (coordinate_value + delta) % static_cast<int>(L);
        if (shifted < 0) shifted += L;
        return static_cast<std::uint64_t>(
            static_cast<std::int64_t>(site)
            + static_cast<std::int64_t>(shifted - coordinate_value)
                * static_cast<std::int64_t>(stride[mu])
        );
    }

    std::uint32_t L;
    std::uint64_t volume;
    std::array<std::uint64_t, DIM> stride{};
};

std::uint64_t fnvlike_absorb(std::uint64_t hash, std::uint8_t value) {
    hash ^= value;
    hash *= FNVLIKE_PRIME;
    return hash;
}

std::string hex16(std::uint64_t value) {
    std::ostringstream output;
    output.imbue(std::locale::classic());
    output << std::hex << std::nouppercase << std::setw(16) << std::setfill('0') << value;
    return output.str();
}

class CompactDsu {
  public:
    explicit CompactDsu(std::size_t count) : parent_(count, 0) {}

    void activate(std::uint32_t item) {
        if (parent_.at(item) == 0) parent_[item] = -1;
    }

    bool active(std::uint32_t item) const { return parent_.at(item) != 0; }

    std::uint32_t find(std::uint32_t item) {
        if (!active(item)) throw IntegrityError("DSU_find_on_inactive_item");
        std::uint32_t root = item;
        while (parent_[root] > 0) root = static_cast<std::uint32_t>(parent_[root] - 1);
        while (item != root) {
            const std::uint32_t next = static_cast<std::uint32_t>(parent_[item] - 1);
            parent_[item] = static_cast<std::int32_t>(root + 1);
            item = next;
        }
        return root;
    }

    void unite(std::uint32_t left, std::uint32_t right) {
        std::uint32_t root_left = find(left);
        std::uint32_t root_right = find(right);
        if (root_left == root_right) return;
        if (parent_[root_left] > parent_[root_right]) std::swap(root_left, root_right);
        parent_[root_left] += parent_[root_right];
        parent_[root_right] = static_cast<std::int32_t>(root_left + 1);
    }

  private:
    std::vector<std::int32_t> parent_;
};

struct VortexComponent {
    std::uint64_t anchor_face{};
    std::uint64_t support_faces{};
    std::uint64_t charged_area{};
    std::array<int, NPAIR> charged_homology{};
    bool wraps{false};
};

struct VortexObservations {
    std::uint64_t occupied_faces{};
    std::uint64_t charged_area{};
    std::vector<VortexComponent> components;
    std::array<int, NPAIR> global_homology{};
    std::vector<std::uint64_t> support_tail;
    bool wraps{false};
};

struct MonopoleComponent {
    std::uint64_t anchor_link{};
    std::uint64_t support_links{};
    std::uint64_t charged_length{};
    std::array<std::int64_t, DIM> windings{};
    bool wraps{false};
};

struct MonopoleObservations {
    std::uint64_t occupied_links{};
    std::uint64_t charged_length{};
    std::array<std::uint64_t, 5> current_counts{};
    std::vector<MonopoleComponent> components;
    std::array<std::int64_t, DIM> global_windings{};
    std::vector<std::uint64_t> support_tail;
    std::vector<std::uint64_t> charged_length_tail;
    bool wraps{false};
};

struct CorrelatorSeparation {
    int n{};
    std::uint64_t count{};
    std::array<std::uint64_t, 5> product_counts{};
    std::array<std::uint64_t, 5> left_counts{};
    std::array<std::uint64_t, 5> right_counts{};
};

struct CorrelatorTerm {
    bool plus{};
    int rho{};
    int pair{};
    std::vector<CorrelatorSeparation> separations;
};

struct Observations {
    Geometry geometry;
    std::vector<std::uint8_t> flux;
    std::array<std::uint64_t, 5> flux_counts{};
    std::array<std::array<std::uint64_t, 5>, NPAIR> oriented_flux_counts{};
    std::array<std::array<std::uint64_t, 5>, DIM> polyakov_counts{};
    VortexObservations vortex;
    MonopoleObservations monopole;
    std::vector<CorrelatorTerm> correlator;
    std::string state_fingerprint;
    std::string cache_fingerprint;
    std::string links_sha256;

    explicit Observations(std::uint32_t L) : geometry(L) {}
};

std::array<std::pair<std::uint32_t, int>, 6> cube_terms(
    const Geometry &geometry,
    const std::array<int, 3> &axes,
    std::uint64_t site
) {
    std::array<std::pair<std::uint32_t, int>, 6> result{};
    int cursor = 0;
    for (int position = 0; position < 3; ++position) {
        const int axis = axes[position];
        std::array<int, 2> face{};
        int face_cursor = 0;
        for (int value : axes) {
            if (value != axis) face[face_cursor++] = value;
        }
        const int pair = pair_index(face[0], face[1]);
        const int sign = (position & 1) ? -1 : 1;
        const std::uint64_t upper = geometry.shift(site, axis);
        result[cursor++] = {
            static_cast<std::uint32_t>(upper * NPAIR + pair), sign,
        };
        result[cursor++] = {
            static_cast<std::uint32_t>(site * NPAIR + pair), -sign,
        };
    }
    return result;
}

VortexObservations observe_vortices(
    const Geometry &geometry,
    const std::vector<std::uint8_t> &flux
) {
    const std::uint64_t face_count = geometry.volume * NPAIR;
    CompactDsu dsu(static_cast<std::size_t>(face_count));
    for (std::uint64_t face = 0; face < face_count; ++face) {
        if (flux[face] != 0) dsu.activate(static_cast<std::uint32_t>(face));
    }
    // A dual vortex face is incident on a dual edge precisely when its primal
    // plaquette is a face of the corresponding primal three-cell.  This is
    // deliberately not primal-edge support adjacency.
    for (std::uint64_t site = 0; site < geometry.volume; ++site) {
        for (const auto &axes : TRIPLES) {
            const auto terms = cube_terms(geometry, axes, site);
            std::uint32_t first = std::numeric_limits<std::uint32_t>::max();
            for (const auto &[face, sign] : terms) {
                (void)sign;
                if (!dsu.active(face)) continue;
                if (first == std::numeric_limits<std::uint32_t>::max()) first = face;
                else dsu.unite(first, face);
            }
        }
    }

    VortexObservations result;
    std::unordered_map<std::uint32_t, std::size_t> root_to_component;
    for (std::uint64_t face = 0; face < face_count; ++face) {
        if (!dsu.active(static_cast<std::uint32_t>(face))) continue;
        const std::uint32_t root = dsu.find(static_cast<std::uint32_t>(face));
        auto [iterator, inserted] = root_to_component.emplace(root, result.components.size());
        if (inserted) {
            VortexComponent component;
            component.anchor_face = face;
            result.components.push_back(component);
        }
        VortexComponent &component = result.components[iterator->second];
        ++component.support_faces;
        component.charged_area += static_cast<std::uint64_t>(std::abs(principal5(flux[face])));
        ++result.occupied_faces;
    }
    for (const VortexComponent &component : result.components) {
        result.charged_area += component.charged_area;
    }

    // Per-component mod-5 closure is checked on every dual edge.  All nonzero
    // terms at one edge must already be in the same support component.
    for (std::uint64_t site = 0; site < geometry.volume; ++site) {
        for (const auto &axes : TRIPLES) {
            const auto terms = cube_terms(geometry, axes, site);
            int boundary = 0;
            std::uint32_t root = std::numeric_limits<std::uint32_t>::max();
            for (const auto &[face, sign] : terms) {
                if (flux[face] == 0) continue;
                const std::uint32_t face_root = dsu.find(face);
                if (root == std::numeric_limits<std::uint32_t>::max()) root = face_root;
                else if (root != face_root) throw IntegrityError("vortex_dual_edge_component_split");
                boundary += sign * static_cast<int>(flux[face]);
            }
            if (mod5(boundary) != 0) throw IntegrityError("vortex_component_closure_failure");
        }
    }

    // Each primal F_ab period is audited on all L^2 transverse slices.  Hodge
    // duality maps it to the complementary oriented dual two-torus.  With the
    // PAIRS order this is exactly h01=F23, h02=-F13, h03=F12,
    // h12=F03, h13=-F02, h23=F01 (all residues in F_5).
    const std::uint64_t slice_count = static_cast<std::uint64_t>(geometry.L) * geometry.L;
    for (int primal_pair = 0; primal_pair < NPAIR; ++primal_pair) {
        const int a = PAIRS[primal_pair][0];
        const int b = PAIRS[primal_pair][1];
        std::array<int, 2> transverse{};
        int transverse_cursor = 0;
        for (int mu = 0; mu < DIM; ++mu) {
            if (mu != a && mu != b) transverse[transverse_cursor++] = mu;
        }
        const int dual_pair = pair_index(transverse[0], transverse[1]);
        const int hodge_sign = levi_sign({{a, b, transverse[0], transverse[1]}});
        std::unordered_map<std::uint64_t, std::uint8_t> slice_sums;
        for (std::uint64_t site = 0; site < geometry.volume; ++site) {
            const std::uint32_t face = static_cast<std::uint32_t>(site * NPAIR + primal_pair);
            if (flux[face] == 0) continue;
            const std::uint32_t root = dsu.find(face);
            const std::size_t component = root_to_component.at(root);
            const std::uint64_t slice =
                static_cast<std::uint64_t>(geometry.coordinate(site, transverse[0])) * geometry.L
                + geometry.coordinate(site, transverse[1]);
            const std::uint64_t key = static_cast<std::uint64_t>(component) * slice_count + slice;
            std::uint8_t &sum = slice_sums[key];
            sum = static_cast<std::uint8_t>((sum + flux[face]) % 5);
        }
        std::vector<int> expected(result.components.size(), 0);
        std::vector<std::uint64_t> seen(result.components.size(), 0);
        for (std::size_t component = 0; component < result.components.size(); ++component) {
            const auto iterator = slice_sums.find(static_cast<std::uint64_t>(component) * slice_count);
            if (iterator != slice_sums.end()) expected[component] = iterator->second;
        }
        for (const auto &[key, sum] : slice_sums) {
            const std::size_t component = static_cast<std::size_t>(key / slice_count);
            if (component >= result.components.size()) throw IntegrityError("vortex_slice_component_index");
            ++seen[component];
            if (sum != expected[component]) throw IntegrityError("vortex_period_slice_disagreement");
        }
        for (std::size_t component = 0; component < result.components.size(); ++component) {
            if (expected[component] != 0 && seen[component] != slice_count) {
                throw IntegrityError("vortex_nonzero_period_missing_slice");
            }
            result.components[component].charged_homology[dual_pair] =
                mod5(hodge_sign * expected[component]);
        }
    }

    for (VortexComponent &component : result.components) {
        component.wraps = std::any_of(
            component.charged_homology.begin(), component.charged_homology.end(),
            [](int value) { return value != 0; }
        );
        result.wraps = result.wraps || component.wraps;
        result.support_tail.push_back(component.support_faces);
        for (int pair = 0; pair < NPAIR; ++pair) {
            result.global_homology[pair] = mod5(
                result.global_homology[pair] + component.charged_homology[pair]
            );
        }
    }
    if (std::any_of(result.global_homology.begin(), result.global_homology.end(),
                    [](int value) { return value != 0; })) {
        throw IntegrityError("exact_link_state_global_vortex_homology_nonzero");
    }
    std::sort(result.support_tail.begin(), result.support_tail.end(), std::greater<>());
    return result;
}

MonopoleObservations observe_monopoles(
    const Geometry &geometry,
    const std::vector<std::uint8_t> &flux
) {
    const std::uint64_t link_count = geometry.volume * DIM;
    std::vector<std::int8_t> current(static_cast<std::size_t>(link_count), 0);
    for (int missing = 0; missing < DIM; ++missing) {
        std::array<int, 3> axes{};
        int cursor = 0;
        for (int mu = 0; mu < DIM; ++mu) {
            if (mu != missing) axes[cursor++] = mu;
        }
        const int a = axes[0];
        const int b = axes[1];
        const int c = axes[2];
        const int pbc = pair_index(b, c);
        const int pac = pair_index(a, c);
        const int pab = pair_index(a, b);
        const int hodge_sign = levi_sign({{missing, a, b, c}});
        for (std::uint64_t site = 0; site < geometry.volume; ++site) {
            const int df =
                principal5(flux[geometry.shift(site, a) * NPAIR + pbc])
                - principal5(flux[site * NPAIR + pbc])
                - principal5(flux[geometry.shift(site, b) * NPAIR + pac])
                + principal5(flux[site * NPAIR + pac])
                + principal5(flux[geometry.shift(site, c) * NPAIR + pab])
                - principal5(flux[site * NPAIR + pab]);
            if (df % 5 != 0) throw IntegrityError("monopole_df_not_divisible_by_five");
            const int value = hodge_sign * (df / 5);
            if (value < -2 || value > 2) throw IntegrityError("monopole_current_out_of_range");
            const std::uint64_t dual_base = geometry.shift(site, missing, -1);
            current[dual_base * DIM + missing] = static_cast<std::int8_t>(value);
        }
    }

    MonopoleObservations result;
    for (std::int8_t value : current) {
        ++result.current_counts[static_cast<std::size_t>(value + 2)];
        if (value != 0) {
            ++result.occupied_links;
            result.charged_length += static_cast<std::uint64_t>(std::abs(static_cast<int>(value)));
        }
    }

    CompactDsu dsu(static_cast<std::size_t>(link_count));
    for (std::uint64_t link = 0; link < link_count; ++link) {
        if (current[link] != 0) dsu.activate(static_cast<std::uint32_t>(link));
    }
    // Support connectivity partitions the current only.  It never decides
    // wrapping; the signed integral cut periods below own that decision.
    for (std::uint64_t vertex = 0; vertex < geometry.volume; ++vertex) {
        std::uint32_t first = std::numeric_limits<std::uint32_t>::max();
        for (int mu = 0; mu < DIM; ++mu) {
            const std::array<std::uint32_t, 2> incident{{
                static_cast<std::uint32_t>(vertex * DIM + mu),
                static_cast<std::uint32_t>(geometry.shift(vertex, mu, -1) * DIM + mu),
            }};
            for (std::uint32_t link : incident) {
                if (!dsu.active(link)) continue;
                if (first == std::numeric_limits<std::uint32_t>::max()) first = link;
                else dsu.unite(first, link);
            }
        }
    }

    std::unordered_map<std::uint32_t, std::size_t> root_to_component;
    for (std::uint64_t link = 0; link < link_count; ++link) {
        if (!dsu.active(static_cast<std::uint32_t>(link))) continue;
        const std::uint32_t root = dsu.find(static_cast<std::uint32_t>(link));
        auto [iterator, inserted] = root_to_component.emplace(root, result.components.size());
        if (inserted) {
            MonopoleComponent component;
            component.anchor_link = link;
            result.components.push_back(component);
        }
        MonopoleComponent &component = result.components[iterator->second];
        ++component.support_links;
        component.charged_length += static_cast<std::uint64_t>(
            std::abs(static_cast<int>(current[link]))
        );
    }

    // Exact integer closure is audited at every dual vertex and therefore in
    // every support component (all nonzero incident links were unioned above).
    for (std::uint64_t vertex = 0; vertex < geometry.volume; ++vertex) {
        int divergence = 0;
        std::uint32_t root = std::numeric_limits<std::uint32_t>::max();
        for (int mu = 0; mu < DIM; ++mu) {
            const std::uint32_t outgoing = static_cast<std::uint32_t>(vertex * DIM + mu);
            const std::uint32_t incoming = static_cast<std::uint32_t>(
                geometry.shift(vertex, mu, -1) * DIM + mu
            );
            divergence += current[outgoing];
            divergence -= current[incoming];
            for (std::uint32_t link : {outgoing, incoming}) {
                if (!dsu.active(link)) continue;
                const std::uint32_t link_root = dsu.find(link);
                if (root == std::numeric_limits<std::uint32_t>::max()) root = link_root;
                else if (root != link_root) throw IntegrityError("monopole_vertex_component_split");
            }
        }
        if (divergence != 0) throw IntegrityError("monopole_integer_closure_failure");
    }

    for (std::uint64_t link = 0; link < link_count; ++link) {
        if (current[link] == 0) continue;
        const int mu = static_cast<int>(link % DIM);
        const std::uint64_t base = link / DIM;
        if (geometry.coordinate(base, mu) != geometry.L - 1) continue;
        const std::uint32_t root = dsu.find(static_cast<std::uint32_t>(link));
        MonopoleComponent &component = result.components[root_to_component.at(root)];
        component.windings[mu] += current[link];
    }
    for (MonopoleComponent &component : result.components) {
        component.wraps = std::any_of(
            component.windings.begin(), component.windings.end(),
            [](std::int64_t value) { return value != 0; }
        );
        result.wraps = result.wraps || component.wraps;
        result.support_tail.push_back(component.support_links);
        result.charged_length_tail.push_back(component.charged_length);
        for (int mu = 0; mu < DIM; ++mu) result.global_windings[mu] += component.windings[mu];
    }
    if (std::any_of(result.global_windings.begin(), result.global_windings.end(),
                    [](std::int64_t value) { return value != 0; })) {
        throw IntegrityError("exact_link_state_global_monopole_winding_nonzero");
    }
    std::sort(result.support_tail.begin(), result.support_tail.end(), std::greater<>());
    std::sort(
        result.charged_length_tail.begin(), result.charged_length_tail.end(), std::greater<>()
    );
    return result;
}

std::vector<CorrelatorTerm> observe_correlator(
    const Geometry &geometry,
    const std::vector<std::uint8_t> &flux,
    const std::array<std::array<std::uint64_t, 5>, NPAIR> &oriented_flux_counts
) {
    std::vector<CorrelatorTerm> terms;
    for (bool plus : {true, false}) {
        for (int rho = 0; rho < DIM; ++rho) {
            for (int pair = 0; pair < NPAIR; ++pair) {
                const bool longitudinal = PAIRS[pair][0] == rho || PAIRS[pair][1] == rho;
                if (longitudinal != plus) continue;
                CorrelatorTerm term;
                term.plus = plus;
                term.rho = rho;
                term.pair = pair;
                for (int n = 1; n <= static_cast<int>(geometry.L / 2); ++n) {
                    CorrelatorSeparation separation;
                    separation.n = n;
                    separation.count = geometry.volume;
                    separation.right_counts = oriented_flux_counts[pair];
                    if (plus) {
                        separation.left_counts = oriented_flux_counts[pair];
                    } else {
                        for (int residue = 0; residue < 5; ++residue) {
                            separation.left_counts[mod5(-residue)] +=
                                oriented_flux_counts[pair][residue];
                        }
                    }
                    for (std::uint64_t site = 0; site < geometry.volume; ++site) {
                        const std::uint8_t left = flux[site * NPAIR + pair];
                        const std::uint64_t shifted = geometry.shift(site, rho, n);
                        const std::uint8_t right = flux[shifted * NPAIR + pair];
                        const int exponent = plus
                            ? mod5(static_cast<int>(left) + right)
                            : mod5(-static_cast<int>(left) + right);
                        ++separation.product_counts[exponent];
                    }
                    term.separations.push_back(separation);
                }
                terms.push_back(std::move(term));
            }
        }
    }
    if (terms.size() != 24
        || std::count_if(terms.begin(), terms.end(), [](const CorrelatorTerm &term) {
               return term.plus;
           }) != 12) {
        throw IntegrityError("correlator_orientation_census_failure");
    }
    return terms;
}

Observations observe(const LinkState &state) {
    Observations result(state.L);
    if (state.links.size() != result.geometry.volume * DIM) {
        throw IntegrityError("state_link_count_internal_mismatch");
    }
    result.links_sha256 = sha256(state.links);
    result.flux.resize(static_cast<std::size_t>(result.geometry.volume * NPAIR));
    std::uint64_t state_fingerprint = FNVLIKE_OFFSET;
    for (std::uint8_t value : state.links) state_fingerprint = fnvlike_absorb(state_fingerprint, value);
    std::uint64_t cache_fingerprint = FNVLIKE_OFFSET;
    for (std::uint64_t site = 0; site < result.geometry.volume; ++site) {
        for (int pair = 0; pair < NPAIR; ++pair) {
            const int a = PAIRS[pair][0];
            const int b = PAIRS[pair][1];
            const std::uint8_t value = static_cast<std::uint8_t>(mod5(
                state.links[site * DIM + a]
                + state.links[result.geometry.shift(site, a) * DIM + b]
                - state.links[result.geometry.shift(site, b) * DIM + a]
                - state.links[site * DIM + b]
            ));
            result.flux[site * NPAIR + pair] = value;
            ++result.flux_counts[value];
            ++result.oriented_flux_counts[pair][value];
            cache_fingerprint = fnvlike_absorb(cache_fingerprint, value);
            state_fingerprint = fnvlike_absorb(state_fingerprint, value);
        }
    }
    result.state_fingerprint = hex16(state_fingerprint);
    result.cache_fingerprint = hex16(cache_fingerprint);

    for (int mu = 0; mu < DIM; ++mu) {
        for (std::uint64_t base = 0; base < result.geometry.volume; ++base) {
            if (result.geometry.coordinate(base, mu) != 0) continue;
            int phase = 0;
            std::uint64_t site = base;
            for (std::uint32_t step = 0; step < result.geometry.L; ++step) {
                phase = mod5(phase + state.links[site * DIM + mu]);
                site = result.geometry.shift(site, mu);
            }
            ++result.polyakov_counts[mu][phase];
        }
    }

    result.vortex = observe_vortices(result.geometry, result.flux);
    result.monopole = observe_monopoles(result.geometry, result.flux);
    result.correlator = observe_correlator(
        result.geometry, result.flux, result.oriented_flux_counts
    );
    return result;
}

template <class Container>
void write_integer_array(std::ostream &output, const Container &values) {
    output << '[';
    bool first = true;
    for (const auto &value : values) {
        if (!first) output << ',';
        first = false;
        output << +value;
    }
    output << ']';
}

void write_json_string(std::ostream &output, std::string_view value) {
    static constexpr char HEX[] = "0123456789abcdef";
    output << '"';
    for (unsigned char character : value) {
        if (character == '"' || character == '\\') {
            output << '\\' << static_cast<char>(character);
        } else if (character >= 32 && character <= 126) {
            output << static_cast<char>(character);
        } else {
            output << "\\u00" << HEX[character >> 4] << HEX[character & 15];
        }
    }
    output << '"';
}

void write_json(
    std::ostream &output,
    const LinkState &state,
    const Observations &observations
) {
    // Object keys are emitted recursively in Python's Unicode lexicographic
    // order, matching json.dumps(sort_keys=True,separators=(",",":"),
    // ensure_ascii=True).  All numerical sufficient statistics are integers.
    output << "{\"correlator\":{\"n_max\":" << observations.geometry.L / 2
           << ",\"terms\":[";
    for (std::size_t term_index = 0; term_index < observations.correlator.size(); ++term_index) {
        if (term_index != 0) output << ',';
        const CorrelatorTerm &term = observations.correlator[term_index];
        output << "{\"kind\":\"" << (term.plus ? "plus" : "minus") << "\",\"pair\":["
               << PAIRS[term.pair][0] << ',' << PAIRS[term.pair][1]
               << "],\"rho\":" << term.rho << ",\"separations\":[";
        for (std::size_t separation_index = 0;
             separation_index < term.separations.size(); ++separation_index) {
            if (separation_index != 0) output << ',';
            const CorrelatorSeparation &separation = term.separations[separation_index];
            output << "{\"count\":" << separation.count << ",\"left_counts\":";
            write_integer_array(output, separation.left_counts);
            output << ",\"n\":" << separation.n << ",\"product_counts\":";
            write_integer_array(output, separation.product_counts);
            output << ",\"right_counts\":";
            write_integer_array(output, separation.right_counts);
            output << '}';
        }
        output << "]}";
    }
    output << "]},\"flux\":{\"counts\":";
    write_integer_array(output, observations.flux_counts);
    output << "},\"monopole\":{\"charged_length\":" << observations.monopole.charged_length
           << ",\"charged_length_tail_desc\":";
    write_integer_array(output, observations.monopole.charged_length_tail);
    output << ",\"closure\":\"PASS\",\"components\":[";
    for (std::size_t index = 0; index < observations.monopole.components.size(); ++index) {
        if (index != 0) output << ',';
        const MonopoleComponent &component = observations.monopole.components[index];
        output << "{\"anchor_link\":" << component.anchor_link
               << ",\"charged_length\":" << component.charged_length
               << ",\"support_links\":" << component.support_links
               << ",\"windings_z\":";
        write_integer_array(output, component.windings);
        output << ",\"wraps\":" << (component.wraps ? "true" : "false") << '}';
    }
    output << "],\"current_count_order\":[-2,-1,0,1,2],\"current_counts\":";
    write_integer_array(output, observations.monopole.current_counts);
    output << ",\"global_windings_z\":";
    write_integer_array(output, observations.monopole.global_windings);
    const std::uint64_t largest_support = observations.monopole.support_tail.empty()
        ? 0 : observations.monopole.support_tail.front();
    output << ",\"largest_support_over_volume\":[" << largest_support << ','
           << observations.geometry.volume << "],\"occupied_links\":"
           << observations.monopole.occupied_links << ",\"support_size_tail_desc\":";
    write_integer_array(output, observations.monopole.support_tail);
    output << ",\"wraps\":" << (observations.monopole.wraps ? "true" : "false")
           << "},\"polyakov\":{\"directions\":[";
    for (int mu = 0; mu < DIM; ++mu) {
        if (mu != 0) output << ',';
        output << "{\"mu\":" << mu << ",\"phase_counts\":";
        write_integer_array(output, observations.polyakov_counts[mu]);
        output << '}';
    }
    const std::uint64_t line_count = observations.geometry.volume / observations.geometry.L;
    output << "],\"line_count\":" << line_count << "},\"schema\":"
           << "\"TWISTJ_Z5_INDEPENDENT_OBSERVABLES_V1\",\"state\":{\"L\":"
           << state.L << ",\"bytes\":" << state.file_bytes << ",\"cache_fingerprint\":";
    write_json_string(output, observations.cache_fingerprint);
    output << ",\"chain\":";
    write_json_string(output, state.chain);
    output << ",\"links_sha256\":";
    write_json_string(output, observations.links_sha256);
    output << ",\"macrocycle\":" << state.macrocycle << ",\"sample\":" << state.sample
           << ",\"schema\":\"TWISTJ_Z5_LINK_STATE_V1\",\"sha256\":";
    write_json_string(output, state.file_sha256);
    output << ",\"state_fingerprint\":";
    write_json_string(output, observations.state_fingerprint);
    output << "},\"vortex\":{\"charged_area\":" << observations.vortex.charged_area
           << ",\"closure\":\"PASS\",\"components\":[";
    for (std::size_t index = 0; index < observations.vortex.components.size(); ++index) {
        if (index != 0) output << ',';
        const VortexComponent &component = observations.vortex.components[index];
        output << "{\"anchor_face\":" << component.anchor_face
               << ",\"charged_area\":" << component.charged_area
               << ",\"charged_homology_f5\":";
        write_integer_array(output, component.charged_homology);
        output << ",\"support_faces\":" << component.support_faces
               << ",\"wraps\":" << (component.wraps ? "true" : "false") << '}';
    }
    output << "],\"global_charged_homology_f5\":";
    write_integer_array(output, observations.vortex.global_homology);
    output << ",\"homology_order\":[\"01\",\"02\",\"03\",\"12\",\"13\",\"23\"]"
           << ",\"occupied_faces\":" << observations.vortex.occupied_faces
           << ",\"support_size_tail_desc\":";
    write_integer_array(output, observations.vortex.support_tail);
    output << ",\"wraps\":" << (observations.vortex.wraps ? "true" : "false") << "}}\n";
}

std::string safe_reason(std::string_view reason) {
    std::string result;
    result.reserve(reason.size());
    for (unsigned char character : reason) {
        result.push_back(
            std::isalnum(character) || character == '_' || character == '-'
                ? static_cast<char>(character) : '_'
        );
    }
    return result.empty() ? "unknown" : result;
}

}  // namespace photon_reader

int main(int argc, char **argv) {
    using namespace photon_reader;
    try {
#ifdef _WIN32
        if (_setmode(_fileno(stdout), _O_BINARY) == -1
            || _setmode(_fileno(stderr), _O_BINARY) == -1) {
            throw IntegrityError("binary_stdio_mode_failed");
        }
#endif
        if (argc != 5 || std::string_view(argv[1]) != "--state"
            || std::string_view(argv[3]) != "--expected-sha256") {
            throw IntegrityError("usage_requires_--state_PATH_--expected-sha256_HEX");
        }
        std::cout.imbue(std::locale::classic());
        const LinkState state = read_state(argv[2], argv[4]);
        const Observations observations = observe(state);
        write_json(std::cout, state, observations);
        if (!std::cout) throw IntegrityError("stdout_write_failure");
        return 0;
    } catch (const IntegrityError &error) {
        std::cerr << "STOP_INTEGRITY " << safe_reason(error.what()) << '\n';
        return 2;
    } catch (const std::exception &error) {
        std::cerr << "STOP_INTEGRITY unexpected_" << safe_reason(error.what()) << '\n';
        return 2;
    }
}
