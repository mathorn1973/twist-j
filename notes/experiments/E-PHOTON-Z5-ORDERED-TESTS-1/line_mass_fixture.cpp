#define main inherited_main
#include "kernel64/photon_z5.cpp"
#undef main

#include <chrono>

namespace {

struct Fixture {
    Lattice::LineFaces faces;
    std::vector<std::uint8_t> flux;

    void add(int residue, int sign) {
        faces.entries[faces.count++] = {flux.size(), sign};
        flux.push_back(static_cast<std::uint8_t>(residue));
    }
};

using Masses = std::array<QPhi, 5>;

Masses direct_products(const Fixture &fixture) {
    Masses result{};
    for (int delta = 0; delta < 5; ++delta) {
        QPhi product{1, 0};
        for (const auto &entry : fixture.faces) {
            const int shifted = mod5(fixture.flux[entry.id] + entry.sign*delta);
            product = product * face_weights()[shifted];
        }
        result[delta] = std::move(product);
    }
    return result;
}

// Existing implementation's repeated five face passes and binary powering.
Masses old_counted(const Fixture &fixture) {
    Masses result{};
    for (int delta = 0; delta < 5; ++delta) {
        std::array<unsigned, 5> counts{};
        for (const auto &entry : fixture.faces) {
            const int shifted = mod5(fixture.flux[entry.id] + entry.sign * delta);
            ++counts[shifted];
        }
        QPhi mass{1, 0};
        for (int value = 0; value < 5; ++value) {
            QPhi base_weight = face_weights()[value];
            unsigned exponent = counts[value];
            while (exponent != 0) {
                if (exponent & 1u) mass = mass * base_weight;
                exponent >>= 1u;
                if (exponent != 0) base_weight = base_weight * base_weight;
            }
        }
        if (sign_qphi(mass) <= 0) throw std::runtime_error("nonpositive old mass");
        result[delta] = mass;
    }
    return result;
}

Masses optimized(const Fixture &fixture) {
    return Lattice::line_masses_from_faces(fixture.faces, fixture.flux);
}

void compare(const Fixture &fixture) {
    const auto direct = direct_products(fixture);
    if (optimized(fixture) != direct || old_counted(fixture) != direct)
        throw std::runtime_error("exact coefficient disagreement");
}

void enumerate(unsigned category, unsigned remaining, Fixture &fixture, unsigned &tested) {
    if (category == 10) {
        compare(fixture);
        ++tested;
        return;
    }
    const auto length = fixture.flux.size();
    for (unsigned count = 0; count <= remaining; ++count) {
        enumerate(category+1, remaining-count, fixture, tested);
        if (count != remaining)
            fixture.add(category % 5, category < 5 ? +1 : -1);
    }
    fixture.faces.count = length;
    fixture.flux.resize(length);
}

std::vector<Fixture> maximum_lines() {
    std::vector<Fixture> result;
    for (int sign : {+1, -1}) {
        for (int residue = 0; residue < 5; ++residue) {
            Fixture &fixture = result.emplace_back();
            for (int n = 0; n < 384; ++n) fixture.add(residue, sign);
        }
    }
    std::uint32_t word = 0x23456789;
    for (int mixed = 0; mixed < 24; ++mixed) {
        Fixture &fixture = result.emplace_back();
        for (int n = 0; n < 384; ++n) {
            word = 1664525u*word + 1013904223u;
            fixture.add((word >> 8) % 5, (word >> 31) ? +1 : -1);
        }
    }
    return result;
}

template<class Measure>
std::pair<double, std::uint64_t> benchmark(Measure measure, const std::vector<Fixture> &inputs) {
    const auto start = std::chrono::steady_clock::now();
    std::uint64_t checksum = 0;
    for (int repeat = 0; repeat < 250; ++repeat) {
        for (const auto &fixture : inputs) {
            const auto output = measure(fixture);
            for (const auto &mass : output)
                checksum += mass.a.backend().size() + mass.b.backend().size();
        }
    }
    return {std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count(), checksum};
}

} // namespace

int main() {
    Fixture fixture;
    unsigned small = 0;
    enumerate(0, 6, fixture, small);
    const auto largest = maximum_lines();
    for (const auto &line : largest) compare(line);
    if (small != 8008) throw std::runtime_error("wrong signed-histogram census");
    std::cout << "EXACT_LINE_MASS_COEFFICIENT_PASS small_signed_histograms=" << small
              << " maximum_384_face_lines=" << largest.size()
              << " candidates_per_line=5\n";
    const auto [old_seconds, old_checksum] = benchmark(old_counted, largest);
    const auto [new_seconds, new_checksum] = benchmark(optimized, largest);
    if (old_checksum != new_checksum) throw std::runtime_error("timing checksum mismatch");
    std::cout << "SYNTHETIC_LINE_MASS_ONLY old_seconds=" << old_seconds
              << " new_seconds=" << new_seconds
              << " speedup=" << old_seconds/new_seconds << '\n';
}
