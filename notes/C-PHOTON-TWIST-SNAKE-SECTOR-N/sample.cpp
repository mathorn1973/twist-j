// NON-CANONICAL, floating-point engineering diagnostic; not a proof.
// Compile: g++ -std=c++17 -O3 -ffp-contract=off -Wall -Wextra -pedantic sample.cpp -o <binary>
// Declared sampling jobs run only after the public preregistration pin has
// been read back. `--audit` is a deterministic implementation test that
// prints no estimate of any target quantity.
// CLI: sample L k chain kind | sample --audit
//   kind 0 main round trip (base 0), 2 exact control round trip (base 2),
//   3 step-zero group (four chains: dwell at twist 0, one step, dwell at twist 1),
//   4 class-0 restricted (chains 0,1 up-only ladder; chain 2 dwell at L^2),
//   5 class-minus restricted (chains 0,1 up-only ladder; chain 2 dwell at L^2).
// No external libraries; all production budgets and seeds are fixed below.
#include <algorithm>
#include <array>
#include <cmath>
#include <cstdint>
#include <cstdlib>
#include <iomanip>
#include <iostream>
#include <limits>
#include <random>
#include <sstream>
#include <stdexcept>
#include <string>
#include <utility>
#include <vector>

namespace {
constexpr int warmup_sweeps = 512;
constexpr int dwell_sweeps = 16384;
constexpr int dwell_long_sweeps = 32768; // step-zero dwells and restricted endpoint dwells
constexpr int visit_sweeps = 2048;
constexpr int equilibration_sweeps = 32;
constexpr int post_forcing_sweeps = 512; // after an up step that reset a slice
constexpr int block_length = 512;
constexpr int pattern_count = 15625; // 5^6
constexpr int field_count = 49;
constexpr std::uint64_t seed_base = UINT64_C(202609300000);
constexpr std::array<std::array<int, 2>, 6> pairs{{
    {{0, 1}}, {{0, 2}}, {{0, 3}}, {{1, 2}}, {{1, 3}}, {{2, 3}}
}};

enum Kind { kind_main = 0, kind_control = 2, kind_pi1 = 3, kind_class0 = 4, kind_classM = 5 };
constexpr int no_restriction = -1; // State::restriction: -1 none, 0 class 0, 1 class minus

void require(bool condition, const std::string& message) {
    if (!condition) throw std::runtime_error(message);
}

int mod5(int value) {
    value %= 5;
    return value < 0 ? value + 5 : value;
}

int representative(int f) { return f <= 2 ? f : f - 5; }

// Class of an integer twisted-slice sum W at twist count n:
// class 0 is W >= -n/2, class minus is W < -n/2 (2W < -n in integers).
int class_of(int W, int n) { return 2 * W >= -n ? 0 : 1; }

struct Incidence {
    int plaquette = 0;
    int sign = 0;
};

// Periodic cubical four-torus. Plaquette p = 6 x + pair, links 4 x + mu.
// The seam is the set of positive 01 plaquettes at x0 = x1 = 0, ordered by
// j = x2 + L x3 (x2 fastest). The partially twisted ensemble with twist
// count n adds the source k to the first n seam plaquettes in this order.
struct Geometry {
    int L, volume, edges, plaquettes;
    std::array<int, 4> stride;
    std::vector<std::array<int, 4>> plus;
    std::vector<std::array<int, 4>> minus;
    std::vector<std::array<Incidence, 6>> incidence;      // link -> six plaquettes
    std::vector<std::array<Incidence, 4>> boundary;       // plaquette -> four links
    std::vector<int> seam;                                // ordered seam plaquettes
    std::vector<int> seam_index;                          // plaquette -> seam order or -1
    std::vector<std::array<Incidence, 2>> zero_one;       // 0/1-link -> its two 01 plaquettes

    explicit Geometry(int length)
        : L(length), volume(length * length * length * length),
          edges(4 * volume), plaquettes(6 * volume),
          stride{{1, length, length * length, length * length * length}},
          plus(volume), minus(volume), incidence(edges), boundary(plaquettes),
          seam_index(plaquettes, -1), zero_one(edges) {
        require(L >= 4 && L % 2 == 0, "geometry requires even L >= 4");
        for (int x = 0; x < volume; ++x) {
            for (int mu = 0; mu < 4; ++mu) {
                const int coordinate = (x / stride[mu]) % L;
                plus[x][mu] = x + (coordinate + 1 == L ? 1 - L : 1) * stride[mu];
                minus[x][mu] = x + (coordinate == 0 ? L - 1 : -1) * stride[mu];
            }
        }
        std::vector<int> degree(edges, 0);
        for (int x = 0; x < volume; ++x) {
            for (int pair = 0; pair < 6; ++pair) {
                const int mu = pairs[pair][0], nu = pairs[pair][1];
                const int p = 6 * x + pair;
                const std::array<int, 4> links{{
                    4 * x + mu, 4 * plus[x][mu] + nu,
                    4 * plus[x][nu] + mu, 4 * x + nu
                }};
                const std::array<int, 4> signs{{1, 1, -1, -1}};
                for (int j = 0; j < 4; ++j) {
                    boundary[p][j] = {links[j], signs[j]};
                    require(degree[links[j]] < 6, "edge incidence overflow");
                    incidence[links[j]][degree[links[j]]++] = {p, signs[j]};
                }
                if (pair == 0 && x % L == 0 && (x / L) % L == 0) {
                    seam_index[p] = static_cast<int>(seam.size());
                    seam.push_back(p);
                }
            }
        }
        require(static_cast<int>(seam.size()) == L * L, "wrong seam cardinality");
        for (int j = 0; j < L * L; ++j) {
            // Seam plaquette j sits at x = L^2 (x2 + L x3) with x2 = j % L, x3 = j / L.
            const int x = L * L * ((j % L) + L * (j / L));
            require(seam[j] == 6 * x, "seam order differs from x2-fastest lexicographic order");
        }
        for (int edge = 0; edge < edges; ++edge) {
            require(degree[edge] == 6, "wrong edge degree");
            for (int a = 0; a < 6; ++a)
                for (int b = a + 1; b < 6; ++b)
                    require(incidence[edge][a].plaquette != incidence[edge][b].plaquette,
                            "duplicate plaquette at edge");
            int found = 0;
            for (const Incidence& incident : incidence[edge])
                if (incident.plaquette % 6 == 0) {
                    require(found < 2, "more than two 01 plaquettes at a link");
                    zero_one[edge][found++] = incident;
                }
            require(found == (edge % 4 < 2 ? 2 : 0), "01 plaquette count at a link");
            for (int i = 0; i < found; ++i)
                require(slice_of_01(zero_one[edge][i].plaquette / 6) == slice_of_site(edge / 4),
                        "01 plaquette of a link lies in another slice");
        }
    }

    int pair_index(int mu, int nu) const {
        for (int j = 0; j < 6; ++j)
            if (pairs[j][0] == mu && pairs[j][1] == nu) return j;
        throw std::runtime_error("invalid oriented pair");
    }

    // Seam plaquette j lies in slice j = x2 + L x3; every 01 plaquette 6x lies
    // in slice x / L^2, as does every site x and every link at x. The source of
    // a seam plaquette is k times (base plus one if its seam rank is below the
    // twist count); other plaquettes have none.
    int slice_of_01(int x) const { return x / (L * L); }
    int slice_of_site(int x) const { return x / (L * L); }

    int source(int p, int twist, int base, int k) const {
        const int j = seam_index[p];
        if (j < 0) return 0;
        return mod5(k * (base + (j < twist ? 1 : 0)));
    }

    // Representative of the source of the seam plaquette of slice j.
    int slice_source(int j, int twist, int base, int k) const {
        return representative(source(seam[j], twist, base, k));
    }

    int direct_curl(const std::vector<unsigned char>& links, int p) const {
        const int x = p / 6, pair = p % 6;
        const int mu = pairs[pair][0], nu = pairs[pair][1];
        return mod5(static_cast<int>(links[4 * x + mu])
                    + links[4 * plus[x][mu] + nu]
                    - links[4 * plus[x][nu] + mu] - links[4 * x + nu]);
    }

    int direct_flux(const std::vector<unsigned char>& links, int p, int twist, int base, int k) const {
        return mod5(direct_curl(links, p) + source(p, twist, base, k));
    }
};

struct Random {
    std::mt19937_64 engine;
    explicit Random(std::uint64_t seed) : engine(seed) {}
    double unit() { return static_cast<double>(engine() >> 11) * 0x1.0p-53; }
    int five() {
        // Rejection eliminates modulo bias, independent of standard distributions.
        constexpr std::uint64_t threshold = (std::uint64_t(0) - 5) % 5;
        std::uint64_t value;
        do { value = engine(); } while (value < threshold);
        return static_cast<int>(value % 5);
    }
};

struct Weights {
    std::array<double, 5> value, log_value, tangent;
    Weights() {
        const double phi = (1.0 + std::sqrt(5.0)) / 2.0;
        value = {{4.0, phi * phi, 1.0 / (phi * phi), 1.0 / (phi * phi), phi * phi}};
        for (int f = 0; f < 5; ++f) log_value[f] = std::log(value[f]);
        const double pi = std::acos(-1.0);
        // Assign odd partners explicitly rather than relying on trig roundoff.
        tangent[0] = 0.0;
        tangent[1] = std::tan(pi / 5.0);
        tangent[2] = std::tan(2.0 * pi / 5.0);
        tangent[3] = -tangent[2];
        tangent[4] = -tangent[1];
    }
};

// Exact integer sector bookkeeping (PROOF.md section 6). slice_sum[j] is the
// sum over the L^2 01 plaquettes of slice j of the representative in
// {-2,...,2} of the effective flux; w_j = (slice_sum[j] - rep(source_j)) / 5
// is an integer; W is the sum of w_j over the twisted slices j < twist.
struct State {
    std::vector<unsigned char> links, flux; // flux = curl + source, mod 5
    std::vector<int> slice_sum;             // per-slice sum of flux representatives
    int twist = 0;                          // number of seam plaquettes with the extra source k
    int base = 0;                           // whole-seam source multiple (0 main, 2 control)
    int restriction = no_restriction;       // -1 unrestricted, 0 class 0, 1 class minus
    int W = 0;                              // twisted-slice sum of w_j
    double score = 0.0;                     // sum_p log W(flux_p)
};

int slice_w(const State& state, const Geometry& geometry, int j, int k) {
    const int difference = state.slice_sum[j] - geometry.slice_source(j, state.twist, state.base, k);
    require(difference % 5 == 0, "slice flux sum is not congruent to its source");
    return difference / 5;
}

bool in_class(const State& state, int W, int n) {
    return state.restriction == no_restriction || class_of(W, n) == state.restriction;
}

void rebuild(State& state, const Geometry& geometry, const Weights& weight, int k) {
    const int slices = geometry.L * geometry.L;
    state.flux.resize(geometry.plaquettes);
    state.slice_sum.assign(slices, 0);
    long double score = 0;
    for (int p = 0; p < geometry.plaquettes; ++p) {
        state.flux[p] = static_cast<unsigned char>(geometry.direct_flux(state.links, p, state.twist, state.base, k));
        score += weight.log_value[state.flux[p]];
        if (p % 6 == 0) state.slice_sum[geometry.slice_of_01(p / 6)] += representative(state.flux[p]);
    }
    state.score = static_cast<double>(score);
    state.W = 0;
    for (int j = 0; j < state.twist; ++j) state.W += slice_w(state, geometry, j, k);
}

void validate(State& state, const Geometry& geometry, const Weights& weight, int k) {
    const int slices = geometry.L * geometry.L;
    require(state.twist >= 0 && state.twist <= slices, "invalid twist count");
    require(state.base == 0 || state.base == 2, "invalid base source multiple");
    require(state.restriction >= no_restriction && state.restriction <= 1, "invalid restriction");
    require(state.restriction == no_restriction || state.base == 0, "restricted chain with base source");
    require(static_cast<int>(state.links.size()) == geometry.edges
            && static_cast<int>(state.flux.size()) == geometry.plaquettes
            && static_cast<int>(state.slice_sum.size()) == slices, "invalid state size");
    for (unsigned char a : state.links) require(a < 5, "invalid link value");
    long double score = 0;
    std::vector<int> sums(slices, 0);
    for (int p = 0; p < geometry.plaquettes; ++p) {
        const int exact = geometry.direct_flux(state.links, p, state.twist, state.base, k);
        require(state.flux[p] == exact, "cached plaquette differs from direct curl plus source");
        score += weight.log_value[exact];
        if (p % 6 == 0) sums[geometry.slice_of_01(p / 6)] += representative(exact);
    }
    require(sums == state.slice_sum, "cached slice sums differ from direct recomputation");
    int W = 0;
    for (int j = 0; j < state.twist; ++j) W += slice_w(state, geometry, j, k);
    require(W == state.W, "cached twisted-slice sum differs from direct recomputation");
    require(in_class(state, state.W, state.twist), "restricted state outside its class");
    const double recomputed = static_cast<double>(score);
    const double tolerance = 1e-8 * geometry.plaquettes;
    require(std::isfinite(state.score) && std::abs(state.score - recomputed) <= tolerance,
            "cached score drift exceeds 1e-8 times plaquette count");
    state.score = recomputed;
}

// Change of the slice sum of the link's slice when link `edge` takes the
// value a instead of its current value: the sum over its two 01 plaquettes
// of the change of the flux representative. Always 0 or +-5.
int slice_change(const State& state, const Geometry& geometry, int edge, int a) {
    if (edge % 4 >= 2) return 0;
    const int old = state.links[edge];
    int change = 0;
    for (const Incidence& incident : geometry.zero_one[edge]) {
        const int f = state.flux[incident.plaquette];
        change += representative(mod5(f + incident.sign * (a - old))) - representative(f);
    }
    require(change % 5 == 0, "slice change is not a multiple of five");
    return change;
}

// Whether link `edge` is a 0- or 1-link of a twisted slice: only these links
// change W under the single-link update.
bool twisted_link(const State& state, const Geometry& geometry, int edge) {
    return edge % 4 < 2 && geometry.slice_of_site(edge / 4) < state.twist;
}

// All 5^6 staple patterns at the target weight. W is even, so
// b_i = sign_i * F_i - alpha_e gives conditional weight prod_i W(b_i + a)
// for link candidate a, where F_i is the cached effective flux.
struct Heatbath {
    std::vector<std::array<double, 5>> cdf;
    explicit Heatbath(const Weights& weight) : cdf(pattern_count) {
        for (int pattern = 0; pattern < pattern_count; ++pattern) {
            std::array<int, 6> staple{};
            int remaining = pattern;
            for (int i = 0; i < 6; ++i) {
                staple[i] = remaining % 5;
                remaining /= 5;
            }
            double sum = 0;
            for (int a = 0; a < 5; ++a) {
                double product = 1;
                for (int b : staple) product *= weight.value[(b + a) % 5];
                sum += product;
                cdf[pattern][a] = sum;
            }
            require(std::isfinite(sum) && sum > 0, "invalid heatbath normalization");
            for (double& value : cdf[pattern]) value /= sum;
            cdf[pattern][4] = 1.0;
        }
    }

    int pattern(const State& state, const Geometry& geometry, int edge) const {
        int key = 0, multiplier = 1;
        const int old = state.links[edge];
        for (const Incidence& incident : geometry.incidence[edge]) {
            key += mod5(incident.sign * static_cast<int>(state.flux[incident.plaquette]) - old) * multiplier;
            multiplier *= 5;
        }
        return key;
    }

    static int select(const std::array<double, 5>& cumulative, double uniform) {
        int selected = 0;
        while (selected < 4 && uniform >= cumulative[selected]) ++selected;
        return selected;
    }

    // Restricted single-link law: the ordinary heat-bath probabilities with
    // the candidates that leave the class given weight zero, renormalised.
    // The current value is always allowed, so the normaliser is positive.
    std::array<double, 5> restricted_cdf(const State& state, const Geometry& geometry, int edge) const {
        const auto& cumulative = cdf[pattern(state, geometry, edge)];
        std::array<double, 5> result{};
        double total = 0;
        for (int a = 0; a < 5; ++a) {
            const double probability = cumulative[a] - (a == 0 ? 0.0 : cumulative[a - 1]);
            const int change = twisted_link(state, geometry, edge) ? slice_change(state, geometry, edge, a) : 0;
            const bool allowed = in_class(state, state.W + change / 5, state.twist);
            total += allowed ? probability : 0.0;
            result[a] = total;
        }
        require(total > 0 && std::isfinite(total), "restricted normaliser is not positive");
        for (double& value : result) value /= total;
        result[4] = 1.0;
        return result;
    }

    void sweep(State& state, const Geometry& geometry, const Weights& weight, Random& random) const {
        for (int edge = 0; edge < geometry.edges; ++edge) {
            const bool restricted = state.restriction != no_restriction && twisted_link(state, geometry, edge);
            const int selected = restricted
                ? select(restricted_cdf(state, geometry, edge), random.unit())
                : select(cdf[pattern(state, geometry, edge)], random.unit());
            const int delta = selected - static_cast<int>(state.links[edge]);
            if (delta == 0) continue;
            int change = 0;
            state.links[edge] = static_cast<unsigned char>(selected);
            for (const Incidence& incident : geometry.incidence[edge]) {
                auto& f = state.flux[incident.plaquette];
                const int changed = mod5(static_cast<int>(f) + incident.sign * delta);
                state.score += weight.log_value[changed] - weight.log_value[f];
                if (incident.plaquette % 6 == 0) change += representative(changed) - representative(f);
                f = static_cast<unsigned char>(changed);
            }
            if (edge % 4 < 2) {
                require(change % 5 == 0, "slice sum changed by a non-multiple of five");
                const int j = geometry.slice_of_site(edge / 4);
                state.slice_sum[j] += change;
                if (j < state.twist) state.W += change / 5;
            }
        }
    }
};

// Change the twist count by +1 (add the source k to seam plaquette twist)
// or -1 (remove it from seam plaquette twist-1). Returns the score change.
// The slice sum of the step plaquette's slice and the twisted-slice sum W
// follow the source exactly.
double advance(State& state, const Geometry& geometry, const Weights& weight, int k, int direction) {
    require(direction == 1 || direction == -1, "invalid twist direction");
    const int n = direction == 1 ? state.twist : state.twist - 1;
    const int q = geometry.seam.at(n);
    const int shift = direction == 1 ? k : -k;
    if (direction == -1) state.W -= slice_w(state, geometry, n, k);
    const int before = state.flux[q];
    const int after = mod5(before + shift);
    const double change = weight.log_value[after] - weight.log_value[before];
    state.flux[q] = static_cast<unsigned char>(after);
    state.slice_sum[n] += representative(after) - representative(before);
    state.score += change;
    state.twist += direction;
    if (direction == 1) state.W += slice_w(state, geometry, n, k);
    return change;
}

// Reset the 0- and 1-links of slice j to the all-zero layout (w_j = 0) or to
// the alternative layout with alpha_0 = 2 on the 0-link at x0 = x1 = 0
// (w_j = -1 for a twisted slice with base 0). Touches no other slice's 01
// plaquettes; the full cache is rebuilt.
void force_slice(State& state, const Geometry& geometry, const Weights& weight, int k, int j, bool alternative) {
    const int slices = geometry.L * geometry.L;
    for (int x = slices * j; x < slices * (j + 1); ++x) {
        state.links[4 * x] = 0;
        state.links[4 * x + 1] = 0;
    }
    if (alternative) state.links[4 * (slices * j)] = 2;
    rebuild(state, geometry, weight, k);
}

// Naive ratio W(F_q + shift) / W(F_q) of the weight of plaquette q.
double naive_ratio(const State& state, const Weights& weight, int q, int shift) {
    const int f = state.flux[q];
    return weight.value[mod5(f + shift)] / weight.value[f];
}

// Indicator that the state, after the source shift of the step plaquette q
// in slice n, lies in the class evaluated at the new twist count n + 1
// (forward step at twist n). Unrestricted chains: always true.
bool forward_indicator(const State& state, const Geometry& geometry, int k) {
    if (state.restriction == no_restriction) return true;
    const int n = state.twist;
    const int q = geometry.seam[n];
    const int f = state.flux[q];
    const int sum = state.slice_sum[n] + representative(mod5(f + k)) - representative(f);
    const int difference = sum - geometry.slice_source(n, n + 1, state.base, k);
    require(difference % 5 == 0, "forward slice sum is not congruent to its source");
    return class_of(state.W + difference / 5, n + 1) == state.restriction;
}

// Indicator that the state at twist m = n + 1 lies in the class evaluated at
// twist n, i.e. without slice n (reverse step). Unrestricted: always true.
bool reverse_indicator(const State& state, const Geometry& geometry, int k) {
    if (state.restriction == no_restriction) return true;
    const int n = state.twist - 1;
    return class_of(state.W - slice_w(state, geometry, n, k), n) == state.restriction;
}

// Local (Rao-Blackwellised) estimators of PROOF.md at link e of the step
// plaquette q, with the class indicators of the restricted ensembles.
// `forward` is true at twist n (estimators F and PF), false at twist n + 1
// (estimator Bw). Results: forward -> {lambda_F, lambda_PF}; reverse ->
// {lambda_Bw, 0}. Every sum runs over the five candidates a of link e.
struct Local { double first = 0, second = 0; };

Local local_ratio(const State& state, const Geometry& geometry, const Weights& weight,
                  int q, int k, int edge, bool forward) {
    const int old = state.links[edge];
    const int shift = forward ? k : -k;
    const int n = forward ? state.twist : state.twist - 1;
    Local result;
    double numerator = 0, numerator2 = 0, denominator = 0;
    for (int a = 0; a < 5; ++a) {
        double product = 1, shifted = 1;
        for (const Incidence& incident : geometry.incidence[edge]) {
            const int f = mod5(static_cast<int>(state.flux[incident.plaquette]) + incident.sign * (a - old));
            product *= weight.value[f];
            shifted *= weight.value[incident.plaquette == q ? mod5(f + shift) : f];
        }
        bool indicator = true;
        if (state.restriction != no_restriction) {
            // Twisted-slice sum with link e at value a, in the ensemble n + 1.
            int W = state.W + slice_change(state, geometry, edge, a) / 5;
            if (forward) {
                // At twist n slice n is untwisted: add the source at q to its sum.
                int fq = state.flux[q];
                for (const Incidence& incident : geometry.zero_one[edge])
                    if (incident.plaquette == q) fq = mod5(fq + incident.sign * (a - old));
                const int sum = state.slice_sum[n] + slice_change(state, geometry, edge, a)
                                + representative(mod5(fq + k)) - representative(fq);
                const int difference = sum - geometry.slice_source(n, n + 1, state.base, k);
                require(difference % 5 == 0, "candidate slice sum is not congruent to its source");
                W = state.W + difference / 5;
            }
            indicator = class_of(W, n + 1) == state.restriction;
        }
        if (forward) {
            denominator += product;
            numerator += indicator ? shifted : 0.0;
            numerator2 += indicator ? product : 0.0;
        } else {
            denominator += indicator ? product : 0.0;
            numerator += indicator ? shifted : 0.0;
        }
    }
    require(std::isfinite(numerator) && std::isfinite(denominator) && denominator > 0,
            "invalid local normaliser");
    result.first = numerator / denominator;
    result.second = forward ? numerator2 / denominator : 0.0;
    if (!forward && !reverse_indicator(state, geometry, k)) result.first = 0.0;
    return result;
}

Local conditional_ratio(const State& state, const Geometry& geometry, const Weights& weight,
                        int q, int k, bool forward) {
    Local sum;
    for (const Incidence& incident : geometry.boundary[q]) {
        const Local local = local_ratio(state, geometry, weight, q, k, incident.plaquette, forward);
        sum.first += local.first;
        sum.second += local.second;
    }
    sum.first /= 4;
    sum.second /= 4;
    return sum;
}

double observable(const State& state, const Geometry& geometry, const Weights& weight) {
    double sum = 0;
    for (int x = 0; x < geometry.volume; ++x) sum += weight.tangent[state.flux[6 * x]];
    return sum / (geometry.L * geometry.L);
}

// Per-sweep sector bookkeeping computed directly from the cached fluxes:
// twisted slices by w in {0, -1, +1, other}, untwisted slices by w in
// {-1, +1, other nonzero}, the direct twisted-slice sum, and the pure-layout
// label (descriptive only). This is bookkeeping about the sampled
// configuration, not a conserved quantity of the kernel.
struct Sector {
    int twisted0 = 0, twisted_minus = 0, twisted_plus = 0, twisted_other = 0;
    int untwisted_minus = 0, untwisted_plus = 0, untwisted_other = 0;
    int W = 0;
    int label = 3; // 0: pure w=0, 1: pure w=-1, 2: pure w=+1, 3: mixed or untwisted
};

Sector sector(const State& state, const Geometry& geometry, int k) {
    const int L = geometry.L, slices = L * L;
    Sector result;
    for (int j = 0; j < slices; ++j) {
        int sum = 0;
        for (int i = 0; i < slices; ++i) sum += representative(state.flux[6 * (i + slices * j)]);
        require(sum == state.slice_sum[j], "cached slice sum differs from the direct sum");
        const bool twisted = j < state.twist;
        const int difference = sum - geometry.slice_source(j, state.twist, state.base, k);
        require(difference % 5 == 0, "slice flux sum is not congruent to its source");
        const int w = difference / 5;
        if (twisted) {
            result.W += w;
            if (w == 0) ++result.twisted0;
            else if (w == -1) ++result.twisted_minus;
            else if (w == 1) ++result.twisted_plus;
            else ++result.twisted_other;
        } else if (w == -1) {
            ++result.untwisted_minus;
        } else if (w == 1) {
            ++result.untwisted_plus;
        } else if (w != 0) {
            ++result.untwisted_other;
        }
    }
    const int untwisted_nonzero = result.untwisted_minus + result.untwisted_plus + result.untwisted_other;
    if (state.twist > 0 && untwisted_nonzero == 0) {
        if (result.twisted0 == state.twist) result.label = 0;
        else if (result.twisted_minus == state.twist) result.label = 1;
        else if (result.twisted_plus == state.twist) result.label = 2;
    }
    return result;
}

struct Block {
    int count = 0;
    long double sumFn = 0, sumFn2 = 0, sumFi = 0, sumFi2 = 0;
    long double sumBn = 0, sumBn2 = 0, sumBi = 0, sumBi2 = 0;
    long double sumPFi = 0, sumPFi2 = 0;
    long double sumY = 0, sumY2 = 0, sumS = 0, sumS2 = 0;
    std::array<int, 5> histF{}, histB{}; // effective flux of q_n and of q_{n-1}, indicator-1 sweeps
    long sec0 = 0, secMinus = 0, secPlus = 0, secOther = 0;
    long untMinus = 0, untPlus = 0, untOther = 0;
    int pure0 = 0, pureMinus = 0, purePlus = 0, flips = 0;
    int classMinus = 0;
    long sumW = 0;
    int minW = 0, maxW = 0;
};

struct Recorder {
    const Geometry& geometry;
    const Weights& weight;
    std::ostream& out;
    int L, k, chain, kind, segment = 0, block_index = 0, segment_twist = -1, previous_label = -1;
    int forced = 0; // 1 when the up step that opened this segment reset slice n-1
    std::string phase;
    Block block;
    Recorder(const Geometry& g, const Weights& w, std::ostream& stream, int size, int mode, int c, int kd)
        : geometry(g), weight(w), out(stream), L(size), k(mode), chain(c), kind(kd) {}

    void begin_segment(const std::string& name, int twist, int forced_step) {
        require(block.count == 0, "segment began inside an open block");
        phase = name;
        segment_twist = twist;
        block_index = 0;
        previous_label = -1;
        forced = forced_step;
    }

    void end_segment() {
        require(block.count == 0, "segment ended inside an open block");
        ++segment;
    }

    void measure(const State& state) {
        require(state.twist == segment_twist, "twist count changed inside a segment");
        const int seam_size = geometry.L * geometry.L;
        double Fn = 0, Fi = 0, PFi = 0, Bn = 0, Bi = 0;
        if (state.twist < seam_size) {
            const int q = geometry.seam[state.twist];
            const bool indicator = forward_indicator(state, geometry, k);
            Fn = indicator ? naive_ratio(state, weight, q, k) : 0.0;
            const Local local = conditional_ratio(state, geometry, weight, q, k, true);
            Fi = local.first;
            PFi = local.second;
            if (indicator) ++block.histF[state.flux[q]];
        }
        if (state.twist > 0) {
            const int q = geometry.seam[state.twist - 1];
            const bool indicator = reverse_indicator(state, geometry, k);
            Bn = indicator ? naive_ratio(state, weight, q, -k) : 0.0;
            Bi = conditional_ratio(state, geometry, weight, q, k, false).first;
            if (indicator) ++block.histB[state.flux[q]];
        }
        const double Y = observable(state, geometry, weight);
        const double S = -state.score / geometry.plaquettes;
        require(std::isfinite(Fn) && std::isfinite(Fi) && std::isfinite(PFi) && std::isfinite(Bn)
                && std::isfinite(Bi) && std::isfinite(Y) && std::isfinite(S), "nonfinite measurement");
        const Sector layout = sector(state, geometry, k);
        require(layout.W == state.W, "cached twisted-slice sum differs from the direct sum");
        require(in_class(state, state.W, state.twist), "recorded state outside its class");
        block.sec0 += layout.twisted0;
        block.secMinus += layout.twisted_minus;
        block.secPlus += layout.twisted_plus;
        block.secOther += layout.twisted_other;
        block.untMinus += layout.untwisted_minus;
        block.untPlus += layout.untwisted_plus;
        block.untOther += layout.untwisted_other;
        block.pure0 += layout.label == 0;
        block.pureMinus += layout.label == 1;
        block.purePlus += layout.label == 2;
        if (previous_label >= 0 && layout.label != previous_label) ++block.flips;
        previous_label = layout.label;
        block.classMinus += class_of(state.W, state.twist) == 1;
        block.sumW += state.W;
        if (block.count == 0 || state.W < block.minW) block.minW = state.W;
        if (block.count == 0 || state.W > block.maxW) block.maxW = state.W;
        ++block.count;
        block.sumFn += Fn; block.sumFn2 += Fn * Fn;
        block.sumFi += Fi; block.sumFi2 += Fi * Fi;
        block.sumBn += Bn; block.sumBn2 += Bn * Bn;
        block.sumBi += Bi; block.sumBi2 += Bi * Bi;
        block.sumPFi += PFi; block.sumPFi2 += PFi * PFi;
        block.sumY += Y; block.sumY2 += Y * Y;
        block.sumS += S; block.sumS2 += S * S;
        if (block.count == block_length) {
            // Sums accumulate in long double and are printed as double with 15
            // significant digits; every analyzer comparison carries a tolerance.
            const auto d = [](long double value) { return static_cast<double>(value); };
            out << L << '\t' << k << '\t' << chain << '\t' << kind << '\t' << segment << '\t' << state.twist
                      << '\t' << phase << '\t' << block_index << '\t' << block.count
                      << '\t' << d(block.sumFn) << '\t' << d(block.sumFn2)
                      << '\t' << d(block.sumFi) << '\t' << d(block.sumFi2)
                      << '\t' << d(block.sumBn) << '\t' << d(block.sumBn2)
                      << '\t' << d(block.sumBi) << '\t' << d(block.sumBi2)
                      << '\t' << d(block.sumPFi) << '\t' << d(block.sumPFi2)
                      << '\t' << d(block.sumY) << '\t' << d(block.sumY2)
                      << '\t' << d(block.sumS) << '\t' << d(block.sumS2);
            for (int f : block.histF) out << '\t' << f;
            for (int f : block.histB) out << '\t' << f;
            out << '\t' << block.sec0 << '\t' << block.secMinus << '\t' << block.secPlus
                << '\t' << block.secOther << '\t' << block.untMinus << '\t' << block.untPlus
                << '\t' << block.untOther
                << '\t' << block.pure0 << '\t' << block.pureMinus << '\t' << block.purePlus
                << '\t' << block.flips << '\t' << block.classMinus << '\t' << block.sumW
                << '\t' << block.minW << '\t' << block.maxW << '\t' << forced << '\n';
            block = Block();
            ++block_index;
        }
    }
};

struct Schedule {
    int warmup, dwell, dwell_long, visit, equilibration, post_forcing;
};

constexpr Schedule frozen_schedule{warmup_sweeps, dwell_sweeps, dwell_long_sweeps, visit_sweeps,
                                   equilibration_sweeps, post_forcing_sweeps};

int base_of(int kind) { return kind == kind_control ? 2 : 0; }
int restriction_of(int kind) { return kind == kind_class0 ? 0 : kind == kind_classM ? 1 : no_restriction; }
bool round_trip(int kind) { return kind == kind_main || kind == kind_control; }

std::string kind_name(int kind) {
    switch (kind) {
        case kind_main: return "main";
        case kind_control: return "control";
        case kind_pi1: return "pi1";
        case kind_class0: return "class0";
        case kind_classM: return "classMinus";
    }
    throw std::runtime_error("invalid kind");
}

bool restricted_kind(int kind) { return kind == kind_class0 || kind == kind_classM; }
bool top_dwell(int kind, int chain) { return restricted_kind(kind) && chain == 2; }

std::string schedule_name(int kind, int chain) {
    if (round_trip(kind)) return "round_trip";
    if (kind == kind_pi1) return "step_zero";
    return top_dwell(kind, chain) ? "dwell_at_top" : "up_only";
}

int start_twist(const Geometry& geometry, int chain, int kind) {
    const int seam_size = geometry.L * geometry.L;
    if (round_trip(kind)) return chain >= 2 ? seam_size : 0;
    if (kind == kind_pi1) return 0;
    return top_dwell(kind, chain) ? seam_size : 1;
}

int segment_count(const Geometry& geometry, int chain, int kind) {
    const int seam_size = geometry.L * geometry.L;
    if (round_trip(kind)) return 2 * seam_size;
    if (kind == kind_pi1) return 2;
    return top_dwell(kind, chain) ? 1 : seam_size;
}

std::string initial_name(int chain, int kind) {
    if (round_trip(kind))
        return chain == 4 ? "coldAltT" : std::string(chain % 2 ? "hot" : "cold") + (chain >= 2 ? "T" : "0");
    if (kind == kind_pi1) return chain % 2 ? "hot0" : "cold0";
    const std::string suffix = kind == kind_class0 ? "C0" : "CM";
    if (top_dwell(kind, chain)) return (kind == kind_classM ? "coldAltT" : "coldT") + suffix;
    return (chain % 2 ? "hot1" : (kind == kind_classM ? "coldAlt1" : "cold1")) + suffix;
}

// The declared initial state of a chain. Round-trip kinds: chains 0,1 at
// twist 0 and chains 2,3,4 at twist L^2; even chains cold (all links zero),
// odd chains hot (independently uniform links); chain 4 the alternative-
// sector cold layout with alpha_0 = 2 on the 0-link at x0 = x1 = 0 of every
// slice. Kind 3 starts at twist 0 (chain 0 cold, chain 1 hot). Restricted
// kinds: chains 0 (cold; kind 5 with the alternative layout on slice 0) and
// 1 (hot) start at twist 1 and are reset on slice 0 to the class layout when
// the drawn field lies outside the class; chain 2 starts at twist L^2 in the
// cold class layout (kind 4 all zero, kind 5 the alternative layout on every
// slice, the consumed chain-4 state).
State initial_state(const Geometry& geometry, const Weights& weight, Random& random,
                    int k, int chain, int kind) {
    const int seam_size = geometry.L * geometry.L;
    State state;
    state.links.resize(geometry.edges, 0);
    state.base = base_of(kind);
    state.restriction = restriction_of(kind);
    state.twist = start_twist(geometry, chain, kind);
    if (chain % 2 == 1)
        for (auto& a : state.links) a = static_cast<unsigned char>(random.five());
    if ((round_trip(kind) && chain == 4) || (kind == kind_classM && chain == 2))
        for (int j = 0; j < seam_size; ++j) state.links[4 * (seam_size * j)] = 2;
    if (kind == kind_classM && chain == 0) state.links[0] = 2;
    rebuild(state, geometry, weight, k);
    if (state.restriction != no_restriction && !in_class(state, state.W, state.twist))
        force_slice(state, geometry, weight, k, 0, state.restriction == 1);
    validate(state, geometry, weight, k);
    return state;
}

// The complete chain. Round-trip kinds: header, warmup, dwell, pass, dwell,
// pass back, footer. Kind 3: warmup and one dwell at twist 1. Kinds 4, 5:
// warmup at twist 1, a visit at every twist 1..L^2-1 (class-changing steps
// reset slice n to the class layout before the discarded equilibration
// sweeps), a dwell at L^2. run() executes it with the frozen schedule on
// standard output; the audit executes it with a tiny schedule into a buffer.
void execute(const Geometry& geometry, const Weights& weight, const Heatbath& kernel, State& state,
             Random& random, int k, int chain, int kind, std::uint64_t seed,
             const Schedule& schedule, std::ostream& out) {
    const int L = geometry.L;
    const int seam_size = L * L;
    require(schedule.dwell % block_length == 0 && schedule.visit % block_length == 0
            && schedule.dwell_long % block_length == 0 && schedule.dwell > 0 && schedule.visit > 0
            && schedule.dwell_long > 0, "schedule is not a whole number of blocks");
    const int segments = segment_count(geometry, chain, kind);
    out << std::setprecision(15)
        << "# format\ttwist_snake_sector_blocks_v2\n"
        << "# status\tNON-CANONICAL floating-point engineering diagnostic\n"
        << "# L\t" << L << "\n# k\t" << k << "\n# chain\t" << chain
        << "\n# kind\t" << kind << "\n# kind_name\t" << kind_name(kind)
        << "\n# base\t" << state.base
        << "\n# restriction\t" << state.restriction
        << "\n# schedule\t" << schedule_name(kind, chain)
        << "\n# seed\t" << seed << "\n# seam_size\t" << seam_size
        << "\n# start_twist\t" << state.twist
        << "\n# chain_initial\t" << initial_name(chain, kind)
        << "\n# warmup_sweeps\t" << schedule.warmup
        << "\n# dwell_sweeps\t" << schedule.dwell
        << "\n# dwell_long_sweeps\t" << schedule.dwell_long
        << "\n# visit_sweeps\t" << schedule.visit
        << "\n# equilibration_sweeps\t" << schedule.equilibration
        << "\n# post_forcing_sweeps\t" << schedule.post_forcing
        << "\n# block_length\t" << block_length
        << "\n# segments\t" << segments
        << "\n# seam_order\tx2_fastest_then_x3\n"
        << "# class_rule\tclass0_if_2W_ge_minus_n_else_classMinus\n"
        << "# action_density\tminus_sum_logW_divided_by_6L4\n"
        << "# sampling\tevery_production_sweep_after_full_heatbath_sweep\n"
        << "L\tk\tchain\tkind\tsegment\tn\tphase\tblock\tcount"
        << "\tsumFn\tsumFn2\tsumFi\tsumFi2\tsumBn\tsumBn2\tsumBi\tsumBi2\tsumPFi\tsumPFi2"
        << "\tsumY\tsumY2\tsumS\tsumS2\thF0\thF1\thF2\thF3\thF4\thB0\thB1\thB2\thB3\thB4"
        << "\tsec0\tsecMinus\tsecPlus\tsecOther\tuntMinus\tuntPlus\tuntOther"
        << "\tpure0\tpureMinus\tpurePlus\tflips\tclassMinus\tsumW\tminW\tmaxW\tforced\n";
    Recorder recorder(geometry, weight, out, L, k, chain, kind);
    int forced_total = 0;
    long sweeps_total = 0; // every heat-bath sweep of the chain, discarded or measured

    auto equilibrate = [&](int sweeps) {
        for (int sweep = 0; sweep < sweeps; ++sweep) kernel.sweep(state, geometry, weight, random);
        sweeps_total += sweeps;
    };
    auto produce = [&](int sweeps, const std::string& phase, int forced_step) {
        recorder.begin_segment(phase, state.twist, forced_step);
        for (int sweep = 0; sweep < sweeps; ++sweep) {
            kernel.sweep(state, geometry, weight, random);
            ++sweeps_total;
            recorder.measure(state);
            if ((sweep + 1) % block_length == 0) validate(state, geometry, weight, k);
        }
        recorder.end_segment();
    };
    // A twist step; on a restricted chain an up step whose field leaves the
    // class resets the newly twisted slice to the class layout. Returns 1
    // when that reset happened.
    auto move = [&](int direction) {
        const int n = direction == 1 ? state.twist : state.twist - 1;
        advance(state, geometry, weight, k, direction);
        int forced_step = 0;
        if (state.restriction != no_restriction && !in_class(state, state.W, state.twist)) {
            require(direction == 1, "restricted chain left its class on a down step");
            force_slice(state, geometry, weight, k, n, state.restriction == 1);
            forced_step = 1;
            ++forced_total;
        }
        validate(state, geometry, weight, k);
        equilibrate(forced_step ? schedule.post_forcing : schedule.equilibration);
        return forced_step;
    };

    equilibrate(schedule.warmup);
    validate(state, geometry, weight, k);
    if (round_trip(kind)) {
        produce(schedule.dwell, "dwell", 0);
        int direction = state.twist == 0 ? 1 : -1;
        for (int pass = 0; pass < 2; ++pass) {
            for (int step = 1; step < seam_size; ++step) {
                move(direction);
                produce(schedule.visit, direction == 1 ? "up" : "down", 0);
            }
            if (pass == 0) {
                move(direction);
                require(state.twist == 0 || state.twist == seam_size, "pass did not reach an endpoint");
                produce(schedule.dwell, "dwell", 0);
                direction = -direction;
            }
        }
    } else if (kind == kind_pi1) {
        require(state.twist == 0, "step-zero chain is not at twist 0");
        produce(schedule.dwell_long, "dwell", 0);
        move(1);
        require(state.twist == 1, "step-zero chain did not reach twist 1");
        produce(schedule.dwell_long, "dwell", 0);
    } else if (top_dwell(kind, chain)) {
        require(state.twist == seam_size, "top-dwell chain is not at the twisted endpoint");
        produce(schedule.dwell_long, "dwell", 0);
    } else {
        require(state.twist == 1, "restricted chain is not at twist 1");
        produce(schedule.visit, "up", 0);
        for (int step = 2; step < seam_size; ++step) {
            const int forced_step = move(1);
            produce(schedule.visit, "up", forced_step);
        }
        const int forced_step = move(1);
        require(state.twist == seam_size, "up-only ladder did not reach the twisted endpoint");
        produce(schedule.dwell_long, "dwell", forced_step);
    }
    require(recorder.segment == segments, "unexpected segment count");
    validate(state, geometry, weight, k);
    out << "# final_twist\t" << state.twist << "\n# forced_steps\t" << forced_total
        << "\n# sweeps_total\t" << sweeps_total << "\n# completion\tPASS\n";
}

void run(int L, int k, int chain, int kind) {
    require((L == 4 || L == 6 || L == 8 || L == 10) && (k == 1 || k == 2),
            "allowed arguments: L in {4,6,8,10}, k in {1,2}");
    require(kind == kind_main || kind == kind_control || kind == kind_pi1 || kind == kind_class0
            || kind == kind_classM, "allowed kinds: 0, 2, 3, 4, 5");
    if (kind == kind_main) require(chain >= 0 && chain < 5, "allowed chains for kind 0: 0..4");
    else if (kind == kind_control) require(chain >= 0 && chain < 4 && (L == 4 || L == 6),
                                           "allowed chains for kind 2: 0..3 with L in {4,6}");
    else if (kind == kind_pi1) require(chain >= 0 && chain < 4, "allowed chains for kind 3: 0..3");
    else require(chain >= 0 && chain < 3, "allowed chains for kinds 4, 5: 0..2");
    const Geometry geometry(L);
    const Weights weight;
    const Heatbath kernel(weight);
    const std::uint64_t seed = seed_base + 1000 * L + 100 * k + 10 * kind + chain;
    Random random(seed);
    State state = initial_state(geometry, weight, random, k, chain, kind);
    execute(geometry, weight, kernel, state, random, k, chain, kind, seed, frozen_schedule, std::cout);
}

void close(double left, double right, double tolerance, const std::string& label) {
    require(std::isfinite(left) && std::isfinite(right)
            && std::abs(left - right) <= tolerance * (1.0 + std::abs(left) + std::abs(right)), label);
}

State fixture(const Geometry& geometry, const Weights& weight, int k, int twist, int base,
              int restriction = no_restriction) {
    State state;
    state.links.resize(geometry.edges);
    state.twist = twist;
    state.base = base;
    state.restriction = restriction;
    for (int edge = 0; edge < geometry.edges; ++edge)
        state.links[edge] = static_cast<unsigned char>((edge * edge + edge / 7 + 3) % 5);
    rebuild(state, geometry, weight, k);
    if (restriction == no_restriction) validate(state, geometry, weight, k);
    return state;
}

int expect_throw(State broken, const Geometry& geometry, const Weights& weight, int k,
                 const std::string& label) {
    bool caught = false;
    try { validate(broken, geometry, weight, k); } catch (const std::runtime_error&) { caught = true; }
    require(caught, label);
    return 1;
}

// Recompute the cached effective flux of the listed plaquettes only, and the
// slice sums and W from scratch.
void refresh(State& state, const Geometry& geometry, const std::vector<int>& plaquettes, int k) {
    for (int p : plaquettes)
        state.flux[p] = static_cast<unsigned char>(geometry.direct_flux(state.links, p, state.twist, state.base, k));
    const int slices = geometry.L * geometry.L;
    state.slice_sum.assign(slices, 0);
    for (int p = 0; p < geometry.plaquettes; p += 6)
        state.slice_sum[geometry.slice_of_01(p / 6)] += representative(state.flux[p]);
    state.W = 0;
    for (int j = 0; j < state.twist; ++j) state.W += slice_w(state, geometry, j, k);
}

// Direct w of one slice of a link field at a twist count, from scratch.
int direct_w(const std::vector<unsigned char>& links, const Geometry& geometry, int j, int twist, int base, int k) {
    const int slices = geometry.L * geometry.L;
    int sum = 0;
    for (int i = 0; i < slices; ++i)
        sum += representative(geometry.direct_flux(links, 6 * (i + slices * j), twist, base, k));
    const int difference = sum - geometry.slice_source(j, twist, base, k);
    require(difference % 5 == 0, "direct slice sum is not congruent to its source");
    return difference / 5;
}

// Direct class membership of a link field at a twist count, from scratch.
int direct_class(const std::vector<unsigned char>& links, const Geometry& geometry, int twist, int base, int k) {
    int W = 0;
    for (int j = 0; j < twist; ++j) W += direct_w(links, geometry, j, twist, base, k);
    return class_of(W, twist);
}

// Exact local enumeration: the four links of the step plaquette q take all
// 625 assignments with every other link fixed. Over this local Gibbs law
// the naive and conditional estimators must average exactly to the ratio
// of the local partition sums of the two ensembles, in both directions;
// with a restriction the four estimators F, PF, PB, Bw must average to the
// restricted local identities of PREREG.md. Returns the number of
// assignments outside the class at twist n + 1 (0 when unrestricted).
int local_enumeration(const State& state, const Geometry& geometry, const Weights& weight,
                      int k, int direction, int& mixed) {
    const int n = state.twist, m = n + direction;
    const int q = direction == 1 ? geometry.seam[n] : geometry.seam[n - 1];
    const int shift = direction == 1 ? k : -k;
    const int lower = direction == 1 ? n : m; // the smaller twist count
    std::array<int, 4> links{};
    std::vector<int> plaquettes;
    for (int j = 0; j < 4; ++j) {
        links[j] = geometry.boundary[q][j].plaquette;
        for (const Incidence& incident : geometry.incidence[links[j]])
            if (std::find(plaquettes.begin(), plaquettes.end(), incident.plaquette) == plaquettes.end())
                plaquettes.push_back(incident.plaquette);
    }
    require(plaquettes.size() == 21, "local neighbourhood is not 21 plaquettes");
    const bool restricted = state.restriction != no_restriction;
    // Partition sums: Zlow over all assignments in the class at `lower` (that
    // class does not depend on the four links), A = sum_I h_{lower+1},
    // B = sum_I h_lower over the intersection I, Zhigh over the class at lower+1.
    long double Zlow = 0, Zhigh = 0, A = 0, B = 0;
    long double naive_F = 0, cond_F = 0, cond_PF = 0, naive_PF = 0;
    long double naive_Bw = 0, cond_Bw = 0, PB = 0;
    int outside = 0;
    int W_other = 0;
    for (int j = 0; j < lower; ++j) W_other += direct_w(state.links, geometry, j, lower, state.base, k);
    require(!restricted || class_of(W_other, lower) == state.restriction, "enumeration state outside the lower class");
    State work = state;
    for (int code = 0; code < 625; ++code) {
        int remaining = code;
        for (int j = 0; j < 4; ++j) {
            work.links[links[j]] = static_cast<unsigned char>(remaining % 5);
            remaining /= 5;
        }
        long double hlow = 1, hhigh = 1;
        for (int p : plaquettes) {
            hlow *= weight.value[geometry.direct_flux(work.links, p, lower, state.base, k)];
            hhigh *= weight.value[geometry.direct_flux(work.links, p, lower + 1, state.base, k)];
        }
        // The four links lie in slice `lower`; the other twisted slices are fixed,
        // so their direct sum W_other is computed once and slice `lower` directly
        // per assignment (the class at `lower` does not involve slice `lower`).
        const bool in_low = !restricted || class_of(W_other, lower) == state.restriction;
        const bool in_high = !restricted
            || class_of(W_other + direct_w(work.links, geometry, lower, lower + 1, state.base, k), lower + 1)
               == state.restriction;
        require(!restricted || direct_class(work.links, geometry, lower, state.base, k) == (in_low ? state.restriction : 1 - state.restriction)
                || code % 125 != 0, "direct class at the lower twist disagrees");
        if (!in_high) ++outside;
        if (in_low) Zlow += hlow;
        if (in_high) Zhigh += hhigh;
        if (in_low && in_high) { A += hhigh; B += hlow; }
        // Forward estimators at twist `lower` (only when the state is in the class there).
        if (in_low) {
            work.twist = lower;
            refresh(work, geometry, plaquettes, k);
            const bool indicator = forward_indicator(work, geometry, k);
            require(indicator == in_high, "forward indicator differs from the direct class");
            naive_F += hlow * (indicator ? naive_ratio(work, weight, q, k) : 0.0);
            naive_PF += hlow * (indicator ? 1.0 : 0.0);
            const Local local = conditional_ratio(work, geometry, weight, q, k, true);
            cond_F += hlow * local.first;
            cond_PF += hlow * local.second;
        }
        // Reverse estimators at twist lower + 1 (only when in the class there).
        if (in_high) {
            work.twist = lower + 1;
            refresh(work, geometry, plaquettes, k);
            const bool indicator = reverse_indicator(work, geometry, k);
            require(indicator == in_low, "reverse indicator differs from the direct class");
            naive_Bw += hhigh * (indicator ? naive_ratio(work, weight, q, -k) : 0.0);
            PB += hhigh * (indicator ? 1.0 : 0.0);
            cond_Bw += hhigh * conditional_ratio(work, geometry, weight, q, k, false).first;
        }
    }
    (void)shift;
    require(Zlow > 0, "empty local class at the lower twist");
    if (Zhigh == 0) {
        // No assignment of the four links reaches the class at the higher
        // twist: every forward estimator vanishes identically.
        require(A == 0 && B == 0 && naive_F == 0 && cond_F == 0 && naive_PF == 0 && cond_PF == 0,
                "forward estimators do not vanish on an empty higher class");
        return 1;
    }
    close(static_cast<double>(naive_F / Zlow), static_cast<double>(A / Zlow), 1e-12, "local naive F mean failed");
    close(static_cast<double>(cond_F / Zlow), static_cast<double>(A / Zlow), 1e-12, "local conditional F mean failed");
    close(static_cast<double>(naive_PF / Zlow), static_cast<double>(B / Zlow), 1e-12, "local naive PF mean failed");
    close(static_cast<double>(cond_PF / Zlow), static_cast<double>(B / Zlow), 1e-12, "local conditional PF mean failed");
    close(static_cast<double>(PB / Zhigh), static_cast<double>(A / Zhigh), 1e-12, "local PB mean failed");
    close(static_cast<double>(naive_Bw / Zhigh), static_cast<double>(B / Zhigh), 1e-12, "local naive Bw mean failed");
    close(static_cast<double>(cond_Bw / Zhigh), static_cast<double>(B / Zhigh), 1e-12, "local conditional Bw mean failed");
    // Both pairings give the restricted local ratio Zhigh / Zlow.
    const double ratio = static_cast<double>(Zhigh / Zlow);
    close(static_cast<double>((cond_F / Zlow) / (PB / Zhigh)), ratio, 1e-12, "pairing A failed");
    close(static_cast<double>((cond_PF / Zlow) / (cond_Bw / Zhigh)), ratio, 1e-12, "pairing B failed");
    if (!restricted) {
        close(static_cast<double>(naive_PF / Zlow), 1.0, 1e-15, "unrestricted PF is not one");
        close(static_cast<double>(PB / Zhigh), 1.0, 1e-15, "unrestricted PB is not one");
    }
    mixed += (outside > 0 && outside < 625) ? 1 : 0;
    return 1;
}

// A state at twist n with prescribed twisted-slice sum: the first `minus`
// twisted slices carry the alternative layout (w = -1), every other slice is
// all-zero (w = 0); slice n carries the given layout (0 zeros, 1
// alternative, 2 the fixture pattern on its 0- and 1-links).
State layout_state(const Geometry& geometry, const Weights& weight, int k, int n, int minus,
                   int slice_n_layout, int restriction) {
    const int slices = geometry.L * geometry.L;
    State state;
    state.links.assign(geometry.edges, 0);
    state.twist = n;
    state.base = 0;
    state.restriction = restriction;
    for (int j = 0; j < minus; ++j) state.links[4 * (slices * j)] = 2;
    if (n < slices) {
        if (slice_n_layout == 1) state.links[4 * (slices * n)] = 2;
        if (slice_n_layout == 2)
            for (int x = slices * n; x < slices * (n + 1); ++x)
                for (int mu = 0; mu < 2; ++mu)
                    state.links[4 * x + mu] = static_cast<unsigned char>((x * x + mu * 3 + x / 5) % 5);
    }
    rebuild(state, geometry, weight, k);
    require(state.W == -minus, "layout state has the wrong twisted-slice sum");
    return state;
}

void audit() {
    const Weights weight;
    const Heatbath kernel(weight);
    int geometries = 0, fixture_states = 0, estimator_identities = 0, local_enumerations = 0;
    int restricted_enumerations = 0, mixed_enumerations = 0, forcing_checks = 0, restricted_law_checks = 0;
    int invariance_checks = 0, inversion_checks = 0, mutations_caught = 0, exercise_sweeps = 0;
    int restricted_sweeps = 0, forbidden_candidates = 0;
    // Inversion of the cumulative table at midpoints and at the boundaries.
    for (int pattern : {0, pattern_count / 2, pattern_count - 1}) {
        const auto& cdf = kernel.cdf[pattern];
        for (int a = 0; a < 5; ++a) {
            const double lower = a == 0 ? 0.0 : cdf[a - 1];
            require(Heatbath::select(cdf, 0.5 * (lower + cdf[a])) == a, "cdf midpoint inversion failed");
            require(Heatbath::select(cdf, lower) == a, "cdf lower boundary inversion failed");
            inversion_checks += 2;
            if (a < 4) {
                require(Heatbath::select(cdf, std::nextafter(cdf[a], 0.0)) == a, "cdf upper inversion failed");
                ++inversion_checks;
            }
        }
    }
    for (int L : {4, 6, 8, 10}) {
        const Geometry geometry(L);
        const int seam_size = L * L;
        ++geometries;
        for (int x = 0; x < geometry.volume; ++x)
            for (int mu = 0; mu < 4; ++mu) {
                require(geometry.minus[geometry.plus[x][mu]][mu] == x, "neighbor inverse failed");
                for (int nu = 0; nu < 4; ++nu)
                    require(geometry.plus[geometry.plus[x][mu]][nu]
                            == geometry.plus[geometry.plus[x][nu]][mu], "neighbors do not commute");
            }
        for (int p = 0; p < geometry.plaquettes; ++p)
            for (const Incidence& incident : geometry.boundary[p]) {
                bool found = false;
                for (const Incidence& back : geometry.incidence[incident.plaquette])
                    found = found || (back.plaquette == p && back.sign == incident.sign);
                require(found, "plaquette boundary and link incidence disagree");
            }
        for (int k : {1, 2}) for (int base : {0, 2}) for (int twist : {0, 1, seam_size / 2, seam_size}) {
            State state = fixture(geometry, weight, k, twist, base);
            ++fixture_states;
            // The curl alone is closed; the effective flux differs from it by the source.
            std::vector<int> curl(geometry.plaquettes);
            for (int p = 0; p < geometry.plaquettes; ++p) {
                curl[p] = geometry.direct_curl(state.links, p);
                require(mod5(state.flux[p] - curl[p]) == geometry.source(p, twist, base, k),
                        "effective flux minus curl differs from source");
                const int j = geometry.seam_index[p];
                if (j >= 0) require(geometry.slice_of_01(p / 6) == j, "seam rank differs from slice index");
            }
            // Sector bookkeeping: the slice sums are congruent to their sources, and the
            // all-zero and alternative cold layouts are pure in the expected sectors.
            {
                const Sector layout = sector(state, geometry, k);
                require(layout.twisted0 + layout.twisted_minus + layout.twisted_plus + layout.twisted_other == twist,
                        "twisted slice count");
                require(layout.W == state.W, "direct twisted-slice sum differs from the cache");
                State cold;
                cold.links.assign(geometry.edges, 0);
                cold.twist = twist;
                cold.base = base;
                rebuild(cold, geometry, weight, k);
                const Sector cold_layout = sector(cold, geometry, k);
                require(cold_layout.untwisted_minus + cold_layout.untwisted_plus + cold_layout.untwisted_other == 0
                        && cold_layout.twisted0 == twist && cold.W == 0
                        && (twist == 0 || cold_layout.label == 0), "all-zero layout is not pure w = 0");
                for (int j = 0; j < seam_size; ++j) cold.links[4 * (seam_size * j)] = 2;
                rebuild(cold, geometry, weight, k);
                const Sector alt_layout = sector(cold, geometry, k);
                // With base 0 every twisted slice of the alternative layout has w = -1
                // (seam flux k+2 and -2 on the neighbouring plaquette) and every
                // untwisted slice has representatives 2 and -2, hence w = 0.
                if (base == 0)
                    require(alt_layout.twisted_minus == twist && cold.W == -twist
                            && alt_layout.untwisted_minus + alt_layout.untwisted_plus + alt_layout.untwisted_other == 0
                            && (twist == 0 || alt_layout.label == 1),
                            "alternative layout is not pure w = -1");
            }
            for (int x = 0; x < geometry.volume; ++x)
                for (int mu = 0; mu < 4; ++mu)
                    for (int nu = mu + 1; nu < 4; ++nu)
                        for (int rho = nu + 1; rho < 4; ++rho) {
                            const int nr = geometry.pair_index(nu, rho);
                            const int mr = geometry.pair_index(mu, rho);
                            const int mn = geometry.pair_index(mu, nu);
                            const int boundary = curl[6 * geometry.plus[x][mu] + nr] - curl[6 * x + nr]
                                - curl[6 * geometry.plus[x][nu] + mr] + curl[6 * x + mr]
                                + curl[6 * geometry.plus[x][rho] + mn] - curl[6 * x + mn];
                            require(mod5(boundary) == 0, "d squared is not zero");
                        }
            // A unit link change must produce precisely the six listed incidences,
            // and the slice change of a 0/1-link must be the direct slice-sum change.
            for (int edge : {0, 1, geometry.edges / 2, geometry.edges - 1}) {
                State changed = state;
                changed.links[edge] = static_cast<unsigned char>((changed.links[edge] + 1) % 5);
                rebuild(changed, geometry, weight, k);
                std::vector<int> expected(geometry.plaquettes, 0);
                for (const auto& incident : geometry.incidence[edge]) expected[incident.plaquette] = mod5(incident.sign);
                for (int p = 0; p < geometry.plaquettes; ++p)
                    require(mod5(changed.flux[p] - state.flux[p]) == expected[p], "incidence versus curl mismatch");
                for (int a = 0; a < 5; ++a) {
                    State moved = state;
                    moved.links[edge] = static_cast<unsigned char>(a);
                    rebuild(moved, geometry, weight, k);
                    int direct = 0;
                    for (int j = 0; j < seam_size; ++j) direct += moved.slice_sum[j] - state.slice_sum[j];
                    require(direct == slice_change(state, geometry, edge, a), "slice change differs from direct");
                    const int j = geometry.slice_of_site(edge / 4);
                    require(moved.slice_sum[j] - state.slice_sum[j] == slice_change(state, geometry, edge, a),
                            "slice change lands in another slice");
                }
            }
            // Heat-bath conditional probabilities against direct effective-flux scores.
            auto conditional = [&](const State& s, int edge) {
                const auto& cdf = kernel.cdf[kernel.pattern(s, geometry, edge)];
                std::array<double, 5> probability{};
                for (int a = 0; a < 5; ++a) {
                    probability[a] = cdf[a] - (a == 0 ? 0.0 : cdf[a - 1]);
                    require(probability[a] > 0, "nonpositive heatbath probability");
                }
                return probability;
            };
            for (int edge : {0, 1, geometry.edges / 2, geometry.edges - 1}) {
                const auto probability = conditional(state, edge);
                std::array<double, 5> scores{};
                for (int a = 0; a < 5; ++a) {
                    auto links = state.links;
                    links[edge] = static_cast<unsigned char>(a);
                    for (const auto& incident : geometry.incidence[edge])
                        scores[a] += weight.log_value[geometry.direct_flux(links, incident.plaquette, twist, base, k)];
                }
                for (int a = 0; a < 5; ++a) for (int b = 0; b < 5; ++b)
                    close(std::log(probability[a]) - std::log(probability[b]), scores[a] - scores[b],
                          2e-10, "heatbath pairwise balance failed");
            }
            // Twist steps in both directions, the local-ratio identity, exact local enumeration.
            for (int direction : {1, -1}) {
                if ((direction == 1 && twist == seam_size) || (direction == -1 && twist == 0)) continue;
                const int other = twist + direction;
                const int q = direction == 1 ? geometry.seam[twist] : geometry.seam[twist - 1];
                const int shift = direction == 1 ? k : -k;
                const double predicted = weight.log_value[mod5(state.flux[q] + shift)] - weight.log_value[state.flux[q]];
                State stepped = state;
                const double change = advance(stepped, geometry, weight, k, direction);
                validate(stepped, geometry, weight, k);
                close(stepped.score - state.score, change, 1e-10, "twist step cached score failed");
                require(stepped.twist == other, "twist count did not change");
                const double back = advance(stepped, geometry, weight, k, -direction);
                validate(stepped, geometry, weight, k);
                close(back, -change, 1e-13, "twist step reversal failed");
                require(stepped.flux == state.flux && stepped.twist == twist && stepped.W == state.W
                        && stepped.slice_sum == state.slice_sum, "twist step round trip failed");
                for (const Incidence& incident : geometry.boundary[q]) {
                    const int edge = incident.plaquette;
                    const auto probability = conditional(state, edge);
                    double expected = 0;
                    for (int a = 0; a < 5; ++a) {
                        auto links = state.links;
                        links[edge] = static_cast<unsigned char>(a);
                        // Independent evaluation through both ensembles' direct fluxes.
                        expected += probability[a] * weight.value[geometry.direct_flux(links, q, other, base, k)]
                                    / weight.value[geometry.direct_flux(links, q, twist, base, k)];
                    }
                    const Local local = local_ratio(state, geometry, weight, q, k, edge, direction == 1);
                    close(local.first, expected, 1e-10, "local ratio identity failed");
                    if (direction == 1) close(local.second, 1.0, 1e-15, "unrestricted local PF is not one");
                    ++estimator_identities;
                    // The conditional estimator must not depend on the value of its own link.
                    for (int a = 0; a < 5; ++a) {
                        State moved = state;
                        moved.links[edge] = static_cast<unsigned char>(a);
                        std::vector<int> touched;
                        for (const auto& inc : geometry.incidence[edge]) touched.push_back(inc.plaquette);
                        refresh(moved, geometry, touched, k);
                        close(local_ratio(moved, geometry, weight, q, k, edge, direction == 1).first, local.first,
                              1e-12, "local ratio depends on its own link");
                    }
                    ++invariance_checks;
                }
                const double naive = naive_ratio(state, weight, q, shift);
                close(naive, std::exp(predicted), 1e-13, "naive ratio failed");
                int mixed = 0;
                local_enumerations += local_enumeration(state, geometry, weight, k, direction, mixed);
                require(mixed == 0, "unrestricted enumeration reported a mixed class");
            }
            // Frozen corruptions must be rejected by full-state validation.
            State broken = state;
            broken.flux[0] = static_cast<unsigned char>((broken.flux[0] + 1) % 5);
            mutations_caught += expect_throw(broken, geometry, weight, k, "flux corruption escaped validation");
            broken = state;
            broken.score += geometry.plaquettes;
            mutations_caught += expect_throw(broken, geometry, weight, k, "score corruption escaped validation");
            broken = state;
            broken.twist += twist < seam_size ? 1 : -1;
            mutations_caught += expect_throw(broken, geometry, weight, k, "twist corruption escaped validation");
            broken = state;
            broken.slice_sum[0] += 5;
            mutations_caught += expect_throw(broken, geometry, weight, k, "slice sum corruption escaped validation");
            broken = state;
            broken.W += 1;
            mutations_caught += expect_throw(broken, geometry, weight, k, "twisted-slice sum corruption escaped validation");
        }
        // Restricted classes (base 0 only): layout states at and away from the
        // class boundary for both classes and both parities of n; forcing
        // keeps the class and touches only slice n; restricted local
        // enumeration with mixed indicators; restricted local law.
        for (int k : {1, 2}) for (int n : {1, 2, 3, 4, seam_size / 2, seam_size / 2 + 1}) {
            if (n >= seam_size) continue;
            for (int restriction : {0, 1}) {
                // Twisted-slice sums W = -minus with minus in 0..n; class 0 needs 2W >= -n.
                std::vector<int> candidates;
                for (int minus : {0, 1, 2, n / 2 - 1, n / 2, n / 2 + 1, n - 1, n})
                    if (minus >= 0 && minus <= n && class_of(-minus, n) == restriction
                        && std::find(candidates.begin(), candidates.end(), minus) == candidates.end())
                        candidates.push_back(minus);
                for (int minus : candidates) {
                    const bool boundary = (restriction == 0 && class_of(-minus - 1, n) != 0)
                                          || (restriction == 1 && class_of(-minus + 1, n) != 1);
                    for (int layout : {0, 1, 2}) {
                        State state = layout_state(geometry, weight, k, n, minus, layout, restriction);
                        validate(state, geometry, weight, k);
                        ++fixture_states;
                        // Up step with forcing when the field leaves the class.
                        State stepped = state;
                        advance(stepped, geometry, weight, k, 1);
                        const bool left = !in_class(stepped, stepped.W, stepped.twist);
                        const int expected_w = slice_w(stepped, geometry, n, k);
                        require(class_of(-minus + expected_w, n + 1) != restriction ? left : !left,
                                "class after the step differs from the layout arithmetic");
                        if (left) {
                            force_slice(stepped, geometry, weight, k, n, restriction == 1);
                            require(slice_w(stepped, geometry, n, k) == (restriction == 1 ? -1 : 0),
                                    "forced slice has the wrong w");
                        }
                        validate(stepped, geometry, weight, k);
                        require(in_class(stepped, stepped.W, stepped.twist), "forcing did not restore the class");
                        for (int j = 0; j < seam_size; ++j)
                            if (j != n) require(stepped.slice_sum[j] == state.slice_sum[j], "forcing touched another slice");
                        require(stepped.W - (left ? (restriction == 1 ? -1 : 0) : expected_w) == state.W,
                                "forcing changed the sum of the other twisted slices");
                        ++forcing_checks;
                        // On the fixture pattern at twist n + 1 (slice n twisted, as after an up
                        // step) the reset must change no link outside the 0- and 1-links of
                        // slice n and no other slice sum, and must give slice n its class w.
                        {
                            State patterned = fixture(geometry, weight, k, n + 1, 0, restriction);
                            State reset = patterned;
                            force_slice(reset, geometry, weight, k, n, restriction == 1);
                            for (int edge = 0; edge < geometry.edges; ++edge)
                                if (!(edge % 4 < 2 && geometry.slice_of_site(edge / 4) == n))
                                    require(reset.links[edge] == patterned.links[edge], "forcing touched a link outside slice n");
                            for (int j = 0; j < seam_size; ++j)
                                if (j != n) require(reset.slice_sum[j] == patterned.slice_sum[j], "forcing touched another slice sum");
                            require(slice_w(reset, geometry, n, k) == (restriction == 1 ? -1 : 0), "forced pattern slice has the wrong w");
                            ++forcing_checks;
                        }
                        // Exact local enumeration with the class indicators, forward and reverse.
                        int mixed = 0;
                        restricted_enumerations += local_enumeration(state, geometry, weight, k, 1, mixed);
                        if (boundary && layout == 2) mixed_enumerations += mixed;
                        if (!left) {
                            int mixed_reverse = 0;
                            restricted_enumerations += local_enumeration(stepped, geometry, weight, k, -1, mixed_reverse);
                        }
                        // Restricted single-link law: zero weight outside the class, the
                        // unrestricted ratios inside, checked against direct class recomputation.
                        for (int edge : {4 * (seam_size * (n - 1)), 4 * (seam_size * (n - 1)) + 1,
                                         4 * (seam_size * n) + 1, 4 * (seam_size * (n - 1) + 3)}) {
                            const auto restricted = kernel.restricted_cdf(state, geometry, edge);
                            const auto& plain = kernel.cdf[kernel.pattern(state, geometry, edge)];
                            double allowed_mass = 0;
                            std::array<bool, 5> allowed{};
                            for (int a = 0; a < 5; ++a) {
                                auto links = state.links;
                                links[edge] = static_cast<unsigned char>(a);
                                allowed[a] = direct_class(links, geometry, n, 0, k) == restriction;
                                allowed_mass += allowed[a] ? plain[a] - (a == 0 ? 0.0 : plain[a - 1]) : 0.0;
                            }
                            require(allowed[state.links[edge]], "current link value is not allowed");
                            for (int a = 0; a < 5; ++a) {
                                const double p_restricted = restricted[a] - (a == 0 ? 0.0 : restricted[a - 1]);
                                const double p_plain = plain[a] - (a == 0 ? 0.0 : plain[a - 1]);
                                close(p_restricted, allowed[a] ? p_plain / allowed_mass : 0.0, 1e-12,
                                      "restricted law differs from the renormalised heat bath");
                            }
                            ++restricted_law_checks;
                        }
                    }
                }
            }
        }
        // The declared chain-4 initial state itself must be the pure w = -1 layout,
        // the declared chains 0 and 2 the pure w = 0 layouts, and the declared
        // restricted and pi1 initial states in their classes at twist 1.
        for (int k : {1, 2}) {
            Random r(0);
            const State alt = initial_state(geometry, weight, r, k, 4, kind_main);
            const Sector layout = sector(alt, geometry, k);
            require(layout.label == 1 && layout.twisted_minus == seam_size && alt.W == -seam_size,
                    "chain 4 initial state is not pure w = -1");
            const State cold_top = initial_state(geometry, weight, r, k, 2, kind_main);
            require(sector(cold_top, geometry, k).label == 0 && cold_top.W == 0, "chain 2 initial state is not pure w = 0");
            const State cold_bottom = initial_state(geometry, weight, r, k, 0, kind_main);
            require(sector(cold_bottom, geometry, k).label == 0 || cold_bottom.twist == 0, "chain 0 initial state");
            for (int kind : {kind_pi1, kind_class0, kind_classM}) for (int chain : {0, 1, 2, 3}) {
                if (kind != kind_pi1 && chain == 3) continue;
                Random rr(3);
                const State start = initial_state(geometry, weight, rr, k, chain, kind);
                require(start.twist == start_twist(geometry, chain, kind) && start.base == 0
                        && start.restriction == restriction_of(kind), "declared initial state twist");
                if (kind == kind_pi1) require(start.twist == 0 && start.W == 0, "step-zero initial state");
                if (kind == kind_class0) require(class_of(start.W, start.twist) == 0 && (chain != 2 || start.W == 0),
                                                 "class-0 initial state outside its class");
                if (kind == kind_classM) require(class_of(start.W, start.twist) == 1
                                                 && (chain == 1 || slice_w(start, geometry, 0, k) == -1)
                                                 && (chain != 2 || start.W == -seam_size),
                                                 "class-minus initial state outside its class");
                ++fixture_states;
            }
        }
    }
    // Kernel exercise: random sweeps with validation after every sweep, at
    // several twist counts reached by validated steps. No estimate is printed.
    {
        const Geometry geometry(4);
        Random random(1);
        for (int k : {1, 2}) for (int base : {0, 2}) {
            State state;
            state.links.resize(geometry.edges);
            state.base = base;
            for (auto& a : state.links) a = static_cast<unsigned char>(random.five());
            rebuild(state, geometry, weight, k);
            validate(state, geometry, weight, k);
            for (int target : {0, 1, 8, 16, 0}) {
                while (state.twist != target) {
                    advance(state, geometry, weight, k, target > state.twist ? 1 : -1);
                    validate(state, geometry, weight, k);
                }
                for (int sweep = 0; sweep < 8; ++sweep) {
                    kernel.sweep(state, geometry, weight, random);
                    validate(state, geometry, weight, k);
                    require(std::isfinite(observable(state, geometry, weight)), "nonfinite observable");
                    require(sector(state, geometry, k).W == state.W, "direct twisted-slice sum after a sweep");
                    ++exercise_sweeps;
                }
            }
        }
        // Restricted kernel exercise: both classes, several twists reached by
        // forced up steps; the class is validated after every sweep, and
        // the restricted law is compared with direct class recomputation on
        // every 0/1-link of the twisted slices once per twist.
        for (int k : {1, 2}) for (int restriction : {0, 1}) {
            Random r(2);
            State state = initial_state(geometry, weight, r, k, 1, restriction == 0 ? kind_class0 : kind_classM);
            for (int target : {1, 2, 5, 8, 16}) {
                while (state.twist != target) {
                    const int n = state.twist;
                    advance(state, geometry, weight, k, 1);
                    if (!in_class(state, state.W, state.twist))
                        force_slice(state, geometry, weight, k, n, restriction == 1);
                    validate(state, geometry, weight, k);
                }
                for (int edge = 0; edge < geometry.edges; ++edge) {
                    if (!twisted_link(state, geometry, edge)) continue;
                    const auto restricted = kernel.restricted_cdf(state, geometry, edge);
                    int last_allowed = -1;
                    for (int a = 0; a < 5; ++a) {
                        auto links = state.links;
                        links[edge] = static_cast<unsigned char>(a);
                        const bool allowed = direct_class(links, geometry, state.twist, 0, k) == restriction;
                        const double p = restricted[a] - (a == 0 ? 0.0 : restricted[a - 1]);
                        require(allowed ? p > 0 : p == 0.0, "restricted law support differs from the direct class");
                        if (allowed) last_allowed = a; else ++forbidden_candidates;
                        // Inversion never returns a forbidden candidate, at midpoints and boundaries.
                        if (allowed) {
                            const double lower = a == 0 ? 0.0 : restricted[a - 1];
                            require(Heatbath::select(restricted, 0.5 * (lower + restricted[a])) == a
                                    && Heatbath::select(restricted, lower) == a, "restricted inversion failed");
                        }
                    }
                    require(last_allowed >= 0 && restricted[last_allowed] == 1.0, "restricted cumulative does not end at one");
                    require(Heatbath::select(restricted, std::nextafter(1.0, 0.0)) == last_allowed,
                            "restricted inversion at the upper end selects a forbidden candidate");
                    ++restricted_law_checks;
                }
                std::ostringstream sink;
                Recorder scratch(geometry, weight, sink, 4, k, 1, restriction == 0 ? kind_class0 : kind_classM);
                scratch.begin_segment("up", state.twist, 0);
                for (int sweep = 0; sweep < 8; ++sweep) {
                    kernel.sweep(state, geometry, weight, random);
                    validate(state, geometry, weight, k);
                    require(class_of(state.W, state.twist) == restriction, "restricted sweep left the class");
                    require(sector(state, geometry, k).W == state.W, "direct twisted-slice sum after a restricted sweep");
                    // The indicator-1 histograms count exactly the sweeps whose indicator is set.
                    const int before_f = scratch.block.histF[0] + scratch.block.histF[1] + scratch.block.histF[2]
                                         + scratch.block.histF[3] + scratch.block.histF[4];
                    const int before_b = scratch.block.histB[0] + scratch.block.histB[1] + scratch.block.histB[2]
                                         + scratch.block.histB[3] + scratch.block.histB[4];
                    scratch.measure(state);
                    const int after_f = scratch.block.histF[0] + scratch.block.histF[1] + scratch.block.histF[2]
                                        + scratch.block.histF[3] + scratch.block.histF[4];
                    const int after_b = scratch.block.histB[0] + scratch.block.histB[1] + scratch.block.histB[2]
                                        + scratch.block.histB[3] + scratch.block.histB[4];
                    const bool expect_f = state.twist < 16 && forward_indicator(state, geometry, k);
                    const bool expect_b = state.twist > 0 && reverse_indicator(state, geometry, k);
                    require(after_f - before_f == (expect_f ? 1 : 0), "forward histogram does not follow the indicator");
                    require(after_b - before_b == (expect_b ? 1 : 0), "reverse histogram does not follow the indicator");
                    ++restricted_sweeps;
                }
                require(sink.str().empty(), "scratch recorder printed a block");
            }
        }
    }
    // Schedule exercise: the complete chain code path of every kind with a
    // tiny schedule on L=4, written into a buffer that is inspected for
    // structure and discarded. No sum, histogram or sector value from it is
    // printed or retained.
    int schedule_rows = 0;
    {
        const Geometry geometry(4);
        const Heatbath kernel(weight);
        const Schedule tiny{4, block_length, block_length, block_length, 2, 4};
        const int seam_size = 16;
        struct Case { int kind, chain; };
        for (int k : {1, 2}) for (Case c : {Case{kind_main, 0}, Case{kind_main, 4}, Case{kind_main, 2},
                                            Case{kind_control, 0}, Case{kind_control, 2},
                                            Case{kind_pi1, 0}, Case{kind_pi1, 1}, Case{kind_pi1, 3},
                                            Case{kind_class0, 0}, Case{kind_class0, 1}, Case{kind_class0, 2},
                                            Case{kind_classM, 0}, Case{kind_classM, 1}, Case{kind_classM, 2}}) {
            Random random(7);
            State state = initial_state(geometry, weight, random, k, c.chain, c.kind);
            std::ostringstream buffer;
            execute(geometry, weight, kernel, state, random, k, c.chain, c.kind, 0, tiny, buffer);
            std::istringstream lines(buffer.str());
            std::string line;
            int rows = 0, expected_segment = 0, forced_segments = 0;
            long production = 0, sweeps_total = -1;
            bool completed = false;
            const bool trip = round_trip(c.kind);
            int twist = start_twist(geometry, c.chain, c.kind), direction = twist == 0 ? 1 : -1, visited = 0;
            while (std::getline(lines, line)) {
                if (line == "# completion\tPASS") { completed = true; continue; }
                if (line.rfind("# sweeps_total\t", 0) == 0) { sweeps_total = std::stol(line.substr(15)); continue; }
                if (line.empty() || line[0] == '#' || line[0] == 'L') continue;
                std::vector<std::string> fields;
                std::size_t start = 0;
                for (std::size_t tab = line.find('\t'); tab != std::string::npos; tab = line.find('\t', start)) {
                    fields.push_back(line.substr(start, tab - start));
                    start = tab + 1;
                }
                fields.push_back(line.substr(start));
                require(static_cast<int>(fields.size()) == field_count, "schedule exercise row has wrong field count");
                require(std::stoi(fields[3]) == c.kind, "schedule exercise kind");
                require(std::stoi(fields[4]) == expected_segment, "schedule exercise segment order");
                require(std::stoi(fields[5]) == twist, "schedule exercise twist order");
                require(std::stoi(fields[8]) == block_length, "schedule exercise block count");
                production += block_length;
                const int forced_flag = std::stoi(fields[field_count - 1]);
                require(forced_flag == 0 || forced_flag == 1, "schedule exercise forced flag");
                if (std::stoi(fields[7]) == 0) forced_segments += forced_flag;
                if (!restricted_kind(c.kind) || top_dwell(c.kind, c.chain) || expected_segment == 0)
                    require(forced_flag == 0, "forced flag on a segment without a restricted up step");
                const std::string phase = fields[6];
                const int class_minus = std::stoi(fields[field_count - 5]);
                const int minW = std::stoi(fields[field_count - 3]), maxW = std::stoi(fields[field_count - 2]);
                require(minW <= maxW, "block W extremes out of order");
                if (c.kind == kind_class0) require(class_minus == 0 && 2 * minW >= -twist, "class-0 rows in class minus");
                if (c.kind == kind_classM) require(class_minus == block_length && 2 * maxW < -twist,
                                                   "class-minus rows outside class minus");
                if (trip) {
                    const bool dwell = (visited == 0 || visited == seam_size);
                    require(phase == (dwell ? "dwell" : (direction == 1 ? "up" : "down")), "schedule exercise phase");
                    ++visited;
                    if (visited == seam_size) { twist += direction; }
                    else if (visited == seam_size + 1) { direction = -direction; twist += direction; }
                    else if (visited < 2 * seam_size) { twist += direction; }
                } else if (c.kind == kind_pi1) {
                    require(phase == "dwell" && twist == expected_segment, "step-zero schedule exercise phase");
                    ++twist;
                } else if (top_dwell(c.kind, c.chain)) {
                    require(phase == "dwell" && twist == seam_size, "top-dwell schedule exercise phase");
                } else {
                    require(phase == (twist == seam_size ? "dwell" : "up"), "up-only schedule exercise phase");
                    ++twist;
                }
                ++rows;
                ++expected_segment;
            }
            const int expected_rows = segment_count(geometry, c.chain, c.kind);
            require(completed && rows == expected_rows, "schedule exercise did not complete every segment");
            // Every sweep is accounted for: warmup, production, one equilibration per twist
            // step (post-reset length after a forced step). Segments are one block here.
            const int steps = expected_rows - 1;
            require(sweeps_total == tiny.warmup + production + (steps - forced_segments) * tiny.equilibration
                                    + forced_segments * tiny.post_forcing, "schedule exercise sweep count");
            schedule_rows += rows;
        }
    }
    std::cout << "NON-CANONICAL floating-point engineering audit\n"
              << "geometries\t" << geometries << "\nfixture_states\t" << fixture_states
              << "\nestimator_identities\t" << estimator_identities
              << "\nlocal_enumerations\t" << local_enumerations
              << "\nrestricted_enumerations\t" << restricted_enumerations
              << "\nmixed_enumerations\t" << mixed_enumerations
              << "\nforcing_checks\t" << forcing_checks
              << "\nrestricted_law_checks\t" << restricted_law_checks
              << "\ninvariance_checks\t" << invariance_checks
              << "\ninversion_checks\t" << inversion_checks
              << "\nexercise_sweeps\t" << exercise_sweeps
              << "\nrestricted_sweeps\t" << restricted_sweeps
              << "\nforbidden_candidates\t" << forbidden_candidates
              << "\nschedule_rows\t" << schedule_rows
              << "\nmutations_caught\t" << mutations_caught << "\nresult\tPASS\n";
}
} // namespace

int main(int argc, char** argv) {
    try {
        if (argc == 2 && std::string(argv[1]) == "--audit") {
            audit();
        } else {
            require(argc == 5, "usage: sample L k chain kind | sample --audit");
            std::array<int, 4> argument{};
            for (int j = 0; j < 4; ++j) {
                std::size_t consumed = 0;
                argument[j] = std::stoi(argv[j + 1], &consumed);
                require(consumed == std::string(argv[j + 1]).size(), "noninteger argument");
            }
            run(argument[0], argument[1], argument[2], argument[3]);
        }
        require(static_cast<bool>(std::cout), "stdout write failed");
        return 0;
    } catch (const std::exception& error) {
        std::cerr << "ERROR: " << error.what() << '\n';
        return 1;
    }
}
