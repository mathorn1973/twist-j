// NON-CANONICAL, floating-point engineering diagnostic; not a proof.
// Compile: g++ -std=c++17 -O3 -ffp-contract=off -Wall -Wextra -pedantic sample.cpp -o <binary>
// Declared sampling jobs run only after the public preregistration pin has
// been read back. `--audit` is a deterministic implementation test that
// prints no estimate of any target quantity.
// CLI: sample L k chain base | sample --audit
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
constexpr int visit_sweeps = 2048;
constexpr int equilibration_sweeps = 32;
constexpr int block_length = 512;
constexpr int pattern_count = 15625; // 5^6
constexpr std::array<std::array<int, 2>, 6> pairs{{
    {{0, 1}}, {{0, 2}}, {{0, 3}}, {{1, 2}}, {{1, 3}}, {{2, 3}}
}};

void require(bool condition, const std::string& message) {
    if (!condition) throw std::runtime_error(message);
}

int mod5(int value) {
    value %= 5;
    return value < 0 ? value + 5 : value;
}

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

    explicit Geometry(int length)
        : L(length), volume(length * length * length * length),
          edges(4 * volume), plaquettes(6 * volume),
          stride{{1, length, length * length, length * length * length}},
          plus(volume), minus(volume), incidence(edges), boundary(plaquettes),
          seam_index(plaquettes, -1) {
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
        }
    }

    int pair_index(int mu, int nu) const {
        for (int j = 0; j < 6; ++j)
            if (pairs[j][0] == mu && pairs[j][1] == nu) return j;
        throw std::runtime_error("invalid oriented pair");
    }

    // Seam plaquette j lies in slice j = x2 + L x3; every 01 plaquette 6x lies
    // in slice x / L^2. The source of a seam plaquette is k times (base plus
    // one if its seam rank is below the twist count); other plaquettes have none.
    int slice_of_01(int x) const { return x / (L * L); }

    int source(int p, int twist, int base, int k) const {
        const int j = seam_index[p];
        if (j < 0) return 0;
        return mod5(k * (base + (j < twist ? 1 : 0)));
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

struct State {
    std::vector<unsigned char> links, flux; // flux = curl + source, mod 5
    int twist = 0;                          // number of seam plaquettes with the extra source k
    int base = 0;                           // whole-seam source multiple (0 main, 2 control)
    double score = 0.0;                     // sum_p log W(flux_p)
};

void rebuild(State& state, const Geometry& geometry, const Weights& weight, int k) {
    state.flux.resize(geometry.plaquettes);
    long double score = 0;
    for (int p = 0; p < geometry.plaquettes; ++p) {
        state.flux[p] = static_cast<unsigned char>(geometry.direct_flux(state.links, p, state.twist, state.base, k));
        score += weight.log_value[state.flux[p]];
    }
    state.score = static_cast<double>(score);
}

void validate(State& state, const Geometry& geometry, const Weights& weight, int k) {
    require(state.twist >= 0 && state.twist <= geometry.L * geometry.L, "invalid twist count");
    require(state.base == 0 || state.base == 2, "invalid base source multiple");
    require(static_cast<int>(state.links.size()) == geometry.edges
            && static_cast<int>(state.flux.size()) == geometry.plaquettes, "invalid state size");
    for (unsigned char a : state.links) require(a < 5, "invalid link value");
    long double score = 0;
    for (int p = 0; p < geometry.plaquettes; ++p) {
        const int exact = geometry.direct_flux(state.links, p, state.twist, state.base, k);
        require(state.flux[p] == exact, "cached plaquette differs from direct curl plus source");
        score += weight.log_value[exact];
    }
    const double recomputed = static_cast<double>(score);
    const double tolerance = 1e-8 * geometry.plaquettes;
    require(std::isfinite(state.score) && std::abs(state.score - recomputed) <= tolerance,
            "cached score drift exceeds 1e-8 times plaquette count");
    state.score = recomputed;
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

    void sweep(State& state, const Geometry& geometry, const Weights& weight, Random& random) const {
        for (int edge = 0; edge < geometry.edges; ++edge) {
            const int selected = select(cdf[pattern(state, geometry, edge)], random.unit());
            const int delta = selected - static_cast<int>(state.links[edge]);
            if (delta == 0) continue;
            state.links[edge] = static_cast<unsigned char>(selected);
            for (const Incidence& incident : geometry.incidence[edge]) {
                auto& f = state.flux[incident.plaquette];
                const int changed = mod5(static_cast<int>(f) + incident.sign * delta);
                state.score += weight.log_value[changed] - weight.log_value[f];
                f = static_cast<unsigned char>(changed);
            }
        }
    }
};

// Change the twist count by +1 (add the source k to seam plaquette twist)
// or -1 (remove it from seam plaquette twist-1). Returns the score change.
double advance(State& state, const Geometry& geometry, const Weights& weight, int k, int direction) {
    require(direction == 1 || direction == -1, "invalid twist direction");
    const int q = direction == 1 ? geometry.seam.at(state.twist) : geometry.seam.at(state.twist - 1);
    const int shift = direction == 1 ? k : -k;
    const int before = state.flux[q];
    const int after = mod5(before + shift);
    const double change = weight.log_value[after] - weight.log_value[before];
    state.flux[q] = static_cast<unsigned char>(after);
    state.score += change;
    state.twist += direction;
    return change;
}

// Naive ratio W(F_q + shift) / W(F_q) of the weight of plaquette q.
double naive_ratio(const State& state, const Weights& weight, int q, int shift) {
    const int f = state.flux[q];
    return weight.value[mod5(f + shift)] / weight.value[f];
}

// Conditional-expectation (Rao-Blackwellised) ratio: the heat-bath
// normaliser of link e after the shift of plaquette q divided by the
// normaliser before it. Its mean under the current ensemble equals the mean
// of the naive ratio (tower property); no claim about time correlations.
double local_ratio(const State& state, const Geometry& geometry, const Weights& weight,
                   int q, int shift, int edge) {
    const int old = state.links[edge];
    double numerator = 0, denominator = 0;
    for (int a = 0; a < 5; ++a) {
        double product = 1, shifted = 1;
        for (const Incidence& incident : geometry.incidence[edge]) {
            const int f = mod5(static_cast<int>(state.flux[incident.plaquette]) + incident.sign * (a - old));
            product *= weight.value[f];
            shifted *= weight.value[incident.plaquette == q ? mod5(f + shift) : f];
        }
        denominator += product;
        numerator += shifted;
    }
    require(std::isfinite(numerator) && std::isfinite(denominator) && denominator > 0,
            "invalid local normaliser");
    return numerator / denominator;
}

double conditional_ratio(const State& state, const Geometry& geometry, const Weights& weight,
                      int q, int shift) {
    double sum = 0;
    for (const Incidence& incident : geometry.boundary[q])
        sum += local_ratio(state, geometry, weight, q, shift, incident.plaquette);
    return sum / 4;
}

double observable(const State& state, const Geometry& geometry, const Weights& weight) {
    double sum = 0;
    for (int x = 0; x < geometry.volume; ++x) sum += weight.tangent[state.flux[6 * x]];
    return sum / (geometry.L * geometry.L);
}

int representative(int f) { return f <= 2 ? f : f - 5; }

// Exact integer sector bookkeeping. In slice j the sum over its L^2 01
// plaquettes of the representative in {-2,...,2} of the effective flux is
// congruent to the slice's source modulo five; the quotient w_j of the
// difference from the representative of that source is an integer. Twisted
// slices are counted by w_j in {0, -1, +1, other}; untwisted slices by
// whether w_j differs from zero. A twisted layout is "pure" when every
// twisted slice has the same w in {0, -1, +1} and every untwisted slice has
// w = 0. This is bookkeeping about the sampled configuration, not a
// conserved quantity of the kernel.
struct Sector {
    int twisted0 = 0, twisted_minus = 0, twisted_plus = 0, twisted_other = 0, untwisted_nonzero = 0;
    int label = 3; // 0: pure w=0, 1: pure w=-1, 2: pure w=+1, 3: mixed or untwisted
};

Sector sector(const State& state, const Geometry& geometry, int k) {
    const int L = geometry.L, slices = L * L;
    Sector result;
    for (int j = 0; j < slices; ++j) {
        int sum = 0;
        for (int i = 0; i < slices; ++i) sum += representative(state.flux[6 * (i + slices * j)]);
        const bool twisted = j < state.twist;
        const int source = mod5(k * (state.base + (twisted ? 1 : 0)));
        const int difference = sum - representative(source);
        require(difference % 5 == 0, "slice flux sum is not congruent to its source");
        const int w = difference / 5;
        if (twisted) {
            if (w == 0) ++result.twisted0;
            else if (w == -1) ++result.twisted_minus;
            else if (w == 1) ++result.twisted_plus;
            else ++result.twisted_other;
        } else if (w != 0) {
            ++result.untwisted_nonzero;
        }
    }
    if (state.twist > 0 && result.untwisted_nonzero == 0) {
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
    long double sumY = 0, sumY2 = 0, sumS = 0, sumS2 = 0;
    std::array<int, 5> histF{}, histB{}; // effective flux of q_n and of q_{n-1}
    long sec0 = 0, secMinus = 0, secPlus = 0, secOther = 0, secUntwisted = 0;
    int pure0 = 0, pureMinus = 0, purePlus = 0, flips = 0;
};

struct Recorder {
    const Geometry& geometry;
    const Weights& weight;
    std::ostream& out;
    int L, k, chain, segment = 0, block_index = 0, segment_twist = -1, previous_label = -1;
    std::string phase;
    Block block;
    Recorder(const Geometry& g, const Weights& w, std::ostream& stream, int size, int mode, int c)
        : geometry(g), weight(w), out(stream), L(size), k(mode), chain(c) {}

    void begin_segment(const std::string& name, int twist) {
        require(block.count == 0, "segment began inside an open block");
        phase = name;
        segment_twist = twist;
        block_index = 0;
        previous_label = -1;
    }

    void end_segment() {
        require(block.count == 0, "segment ended inside an open block");
        ++segment;
    }

    void measure(const State& state) {
        require(state.twist == segment_twist, "twist count changed inside a segment");
        const int seam_size = geometry.L * geometry.L;
        double Fn = 0, Fi = 0, Bn = 0, Bi = 0;
        if (state.twist < seam_size) {
            const int q = geometry.seam[state.twist];
            Fn = naive_ratio(state, weight, q, k);
            Fi = conditional_ratio(state, geometry, weight, q, k);
            ++block.histF[state.flux[q]];
        }
        if (state.twist > 0) {
            const int q = geometry.seam[state.twist - 1];
            Bn = naive_ratio(state, weight, q, -k);
            Bi = conditional_ratio(state, geometry, weight, q, -k);
            ++block.histB[state.flux[q]];
        }
        const double Y = observable(state, geometry, weight);
        const double S = -state.score / geometry.plaquettes;
        require(std::isfinite(Fn) && std::isfinite(Fi) && std::isfinite(Bn) && std::isfinite(Bi)
                && std::isfinite(Y) && std::isfinite(S), "nonfinite measurement");
        const Sector layout = sector(state, geometry, k);
        block.sec0 += layout.twisted0;
        block.secMinus += layout.twisted_minus;
        block.secPlus += layout.twisted_plus;
        block.secOther += layout.twisted_other;
        block.secUntwisted += layout.untwisted_nonzero;
        block.pure0 += layout.label == 0;
        block.pureMinus += layout.label == 1;
        block.purePlus += layout.label == 2;
        if (previous_label >= 0 && layout.label != previous_label) ++block.flips;
        previous_label = layout.label;
        ++block.count;
        block.sumFn += Fn; block.sumFn2 += Fn * Fn;
        block.sumFi += Fi; block.sumFi2 += Fi * Fi;
        block.sumBn += Bn; block.sumBn2 += Bn * Bn;
        block.sumBi += Bi; block.sumBi2 += Bi * Bi;
        block.sumY += Y; block.sumY2 += Y * Y;
        block.sumS += S; block.sumS2 += S * S;
        if (block.count == block_length) {
            // Sums accumulate in long double and are printed as double with 15
            // significant digits; every analyzer comparison carries a tolerance.
            const auto d = [](long double value) { return static_cast<double>(value); };
            out << L << '\t' << k << '\t' << chain << '\t' << segment << '\t' << state.twist
                      << '\t' << phase << '\t' << block_index << '\t' << block.count
                      << '\t' << d(block.sumFn) << '\t' << d(block.sumFn2)
                      << '\t' << d(block.sumFi) << '\t' << d(block.sumFi2)
                      << '\t' << d(block.sumBn) << '\t' << d(block.sumBn2)
                      << '\t' << d(block.sumBi) << '\t' << d(block.sumBi2)
                      << '\t' << d(block.sumY) << '\t' << d(block.sumY2)
                      << '\t' << d(block.sumS) << '\t' << d(block.sumS2);
            for (int f : block.histF) out << '\t' << f;
            for (int f : block.histB) out << '\t' << f;
            out << '\t' << block.sec0 << '\t' << block.secMinus << '\t' << block.secPlus
                << '\t' << block.secOther << '\t' << block.secUntwisted
                << '\t' << block.pure0 << '\t' << block.pureMinus << '\t' << block.purePlus
                << '\t' << block.flips << '\n';
            block = Block();
            ++block_index;
        }
    }
};

struct Schedule {
    int warmup, dwell, visit, equilibration;
};

constexpr Schedule frozen_schedule{warmup_sweeps, dwell_sweeps, visit_sweeps, equilibration_sweeps};

// The declared initial state of a chain: chains 0,1 at twist 0 and chains
// 2,3,4 at twist L^2; even chains cold (all links zero), odd chains hot
// (independently uniform links); chain 4 the alternative-sector cold layout
// with alpha_0 = 2 on the 0-link at x0 = x1 = 0 of every slice, which shifts
// the seam plaquette flux by +2 and the 01 plaquette at x1 = L-1 by -2.
State initial_state(const Geometry& geometry, const Weights& weight, Random& random,
                    int k, int chain, int base) {
    const int seam_size = geometry.L * geometry.L;
    State state;
    state.links.resize(geometry.edges, 0);
    state.base = base;
    state.twist = chain >= 2 ? seam_size : 0;
    if (chain % 2 == 1)
        for (auto& a : state.links) a = static_cast<unsigned char>(random.five());
    if (chain == 4)
        for (int j = 0; j < seam_size; ++j) state.links[4 * (seam_size * j)] = 2;
    rebuild(state, geometry, weight, k);
    validate(state, geometry, weight, k);
    return state;
}

std::string initial_name(int chain) {
    return chain == 4 ? "coldAltT" : std::string(chain % 2 ? "hot" : "cold") + (chain >= 2 ? "T" : "0");
}

// The complete chain: header, warmup, dwell, pass, dwell, pass back, footer.
// run() executes it with the frozen schedule on standard output; the audit
// executes it with a tiny schedule into a discarded buffer.
void execute(const Geometry& geometry, const Weights& weight, const Heatbath& kernel, State& state,
             Random& random, int k, int chain, int base, std::uint64_t seed,
             const Schedule& schedule, std::ostream& out) {
    const int L = geometry.L;
    const int seam_size = L * L;
    require(schedule.dwell % block_length == 0 && schedule.visit % block_length == 0
            && schedule.dwell > 0 && schedule.visit > 0, "schedule is not a whole number of blocks");
    out << std::setprecision(15)
        << "# format\ttwist_snake_blocks_v1\n"
        << "# status\tNON-CANONICAL floating-point engineering diagnostic\n"
        << "# L\t" << L << "\n# k\t" << k << "\n# chain\t" << chain
        << "\n# base\t" << base
        << "\n# seed\t" << seed << "\n# seam_size\t" << seam_size
        << "\n# start_twist\t" << state.twist
        << "\n# chain_initial\t" << initial_name(chain)
        << "\n# warmup_sweeps\t" << schedule.warmup
        << "\n# dwell_sweeps\t" << schedule.dwell
        << "\n# visit_sweeps\t" << schedule.visit
        << "\n# equilibration_sweeps\t" << schedule.equilibration
        << "\n# block_length\t" << block_length
        << "\n# segments\t" << 2 * seam_size
        << "\n# seam_order\tx2_fastest_then_x3\n"
        << "# action_density\tminus_sum_logW_divided_by_6L4\n"
        << "# sampling\tevery_production_sweep_after_full_heatbath_sweep\n"
        << "L\tk\tchain\tsegment\tn\tphase\tblock\tcount"
        << "\tsumFn\tsumFn2\tsumFi\tsumFi2\tsumBn\tsumBn2\tsumBi\tsumBi2"
        << "\tsumY\tsumY2\tsumS\tsumS2\thF0\thF1\thF2\thF3\thF4\thB0\thB1\thB2\thB3\thB4"
        << "\tsec0\tsecMinus\tsecPlus\tsecOther\tsecUntwisted\tpure0\tpureMinus\tpurePlus\tflips\n";
    Recorder recorder(geometry, weight, out, L, k, chain);

    auto equilibrate = [&](int sweeps) {
        for (int sweep = 0; sweep < sweeps; ++sweep) kernel.sweep(state, geometry, weight, random);
    };
    auto produce = [&](int sweeps, const std::string& phase) {
        recorder.begin_segment(phase, state.twist);
        for (int sweep = 0; sweep < sweeps; ++sweep) {
            kernel.sweep(state, geometry, weight, random);
            recorder.measure(state);
            if ((sweep + 1) % block_length == 0) validate(state, geometry, weight, k);
        }
        recorder.end_segment();
    };
    auto move = [&](int direction) {
        advance(state, geometry, weight, k, direction);
        validate(state, geometry, weight, k);
        equilibrate(schedule.equilibration);
    };

    equilibrate(schedule.warmup);
    validate(state, geometry, weight, k);
    produce(schedule.dwell, "dwell");
    int direction = state.twist == 0 ? 1 : -1;
    for (int pass = 0; pass < 2; ++pass) {
        for (int step = 1; step < seam_size; ++step) {
            move(direction);
            produce(schedule.visit, direction == 1 ? "up" : "down");
        }
        if (pass == 0) {
            move(direction);
            require(state.twist == 0 || state.twist == seam_size, "pass did not reach an endpoint");
            produce(schedule.dwell, "dwell");
            direction = -direction;
        }
    }
    require(recorder.segment == 2 * seam_size, "unexpected segment count");
    validate(state, geometry, weight, k);
    out << "# final_twist\t" << state.twist << "\n# completion\tPASS\n";
}

void run(int L, int k, int chain, int base) {
    require((L == 4 || L == 6 || L == 8 || L == 10) && (k == 1 || k == 2) && (base == 0 || base == 2),
            "allowed arguments: L in {4,6,8,10}, k in {1,2}, base in {0,2}");
    require(base == 0 ? (chain >= 0 && chain < 5) : (chain >= 0 && chain < 4 && (L == 4 || L == 6)),
            "allowed chains: 0..4 for base 0; 0..3 with L in {4,6} for base 2");
    const Geometry geometry(L);
    const Weights weight;
    const Heatbath kernel(weight);
    const std::uint64_t seed = UINT64_C(202609280000) + 1000 * L + 100 * k + 10 * base + chain;
    Random random(seed);
    State state = initial_state(geometry, weight, random, k, chain, base);
    execute(geometry, weight, kernel, state, random, k, chain, base, seed, frozen_schedule, std::cout);
}

void close(double left, double right, double tolerance, const std::string& label) {
    require(std::isfinite(left) && std::isfinite(right)
            && std::abs(left - right) <= tolerance * (1.0 + std::abs(left) + std::abs(right)), label);
}

State fixture(const Geometry& geometry, const Weights& weight, int k, int twist, int base) {
    State state;
    state.links.resize(geometry.edges);
    state.twist = twist;
    state.base = base;
    for (int edge = 0; edge < geometry.edges; ++edge)
        state.links[edge] = static_cast<unsigned char>((edge * edge + edge / 7 + 3) % 5);
    rebuild(state, geometry, weight, k);
    validate(state, geometry, weight, k);
    return state;
}

int expect_throw(State broken, const Geometry& geometry, const Weights& weight, int k,
                 const std::string& label) {
    bool caught = false;
    try { validate(broken, geometry, weight, k); } catch (const std::runtime_error&) { caught = true; }
    require(caught, label);
    return 1;
}

// Recompute the cached effective flux of the listed plaquettes only.
void refresh(State& state, const Geometry& geometry, const std::vector<int>& plaquettes, int k) {
    for (int p : plaquettes)
        state.flux[p] = static_cast<unsigned char>(geometry.direct_flux(state.links, p, state.twist, state.base, k));
}

// Exact local enumeration: the four links of the step plaquette q take all
// 625 assignments with every other link fixed. Over this local Gibbs law the
// naive and conditional estimators must average exactly to the ratio of the
// local partition sums of the two ensembles, in both directions.
int local_enumeration(const State& state, const Geometry& geometry, const Weights& weight,
                      int k, int direction) {
    const int n = state.twist, m = n + direction;
    const int q = direction == 1 ? geometry.seam[n] : geometry.seam[n - 1];
    const int shift = direction == 1 ? k : -k;
    std::array<int, 4> links{};
    std::vector<int> plaquettes;
    for (int j = 0; j < 4; ++j) {
        links[j] = geometry.boundary[q][j].plaquette;
        for (const Incidence& incident : geometry.incidence[links[j]])
            if (std::find(plaquettes.begin(), plaquettes.end(), incident.plaquette) == plaquettes.end())
                plaquettes.push_back(incident.plaquette);
    }
    require(plaquettes.size() == 21, "local neighbourhood is not 21 plaquettes");
    long double Zn = 0, Zm = 0, naive_n = 0, cond_n = 0, naive_m = 0, cond_m = 0;
    State work = state;
    for (int code = 0; code < 625; ++code) {
        int remaining = code;
        for (int j = 0; j < 4; ++j) {
            work.links[links[j]] = static_cast<unsigned char>(remaining % 5);
            remaining /= 5;
        }
        long double hn = 1, hm = 1;
        for (int p : plaquettes) {
            hn *= weight.value[geometry.direct_flux(work.links, p, n, state.base, k)];
            hm *= weight.value[geometry.direct_flux(work.links, p, m, state.base, k)];
        }
        Zn += hn;
        Zm += hm;
        work.twist = n;
        refresh(work, geometry, plaquettes, k);
        naive_n += hn * naive_ratio(work, weight, q, shift);
        cond_n += hn * conditional_ratio(work, geometry, weight, q, shift);
        work.twist = m;
        refresh(work, geometry, plaquettes, k);
        naive_m += hm * naive_ratio(work, weight, q, -shift);
        cond_m += hm * conditional_ratio(work, geometry, weight, q, -shift);
    }
    const double ratio = static_cast<double>(Zm / Zn);
    close(static_cast<double>(naive_n / Zn), ratio, 1e-12, "local naive estimator mean failed");
    close(static_cast<double>(cond_n / Zn), ratio, 1e-12, "local conditional estimator mean failed");
    close(static_cast<double>(naive_m / Zm), 1.0 / ratio, 1e-12, "local naive reverse mean failed");
    close(static_cast<double>(cond_m / Zm), 1.0 / ratio, 1e-12, "local conditional reverse mean failed");
    return 1;
}

void audit() {
    const Weights weight;
    const Heatbath kernel(weight);
    int geometries = 0, fixture_states = 0, estimator_identities = 0, local_enumerations = 0;
    int invariance_checks = 0, inversion_checks = 0, mutations_caught = 0, exercise_sweeps = 0;
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
                State cold;
                cold.links.assign(geometry.edges, 0);
                cold.twist = twist;
                cold.base = base;
                rebuild(cold, geometry, weight, k);
                const Sector cold_layout = sector(cold, geometry, k);
                require(cold_layout.untwisted_nonzero == 0 && cold_layout.twisted0 == twist
                        && (twist == 0 || cold_layout.label == 0), "all-zero layout is not pure w = 0");
                for (int j = 0; j < seam_size; ++j) cold.links[4 * (seam_size * j)] = 2;
                rebuild(cold, geometry, weight, k);
                const Sector alt_layout = sector(cold, geometry, k);
                // With base 0 every twisted slice of the alternative layout has w = -1
                // (seam flux k+2 and -2 on the neighbouring plaquette) and every
                // untwisted slice has representatives 2 and -2, hence w = 0.
                if (base == 0)
                    require(alt_layout.twisted_minus == twist && alt_layout.untwisted_nonzero == 0
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
            // A unit link change must produce precisely the six listed incidences.
            for (int edge : {0, 1, geometry.edges / 2, geometry.edges - 1}) {
                State changed = state;
                changed.links[edge] = static_cast<unsigned char>((changed.links[edge] + 1) % 5);
                rebuild(changed, geometry, weight, k);
                std::vector<int> expected(geometry.plaquettes, 0);
                for (const auto& incident : geometry.incidence[edge]) expected[incident.plaquette] = mod5(incident.sign);
                for (int p = 0; p < geometry.plaquettes; ++p)
                    require(mod5(changed.flux[p] - state.flux[p]) == expected[p], "incidence versus curl mismatch");
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
                require(stepped.flux == state.flux && stepped.twist == twist, "twist step round trip failed");
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
                    const double lambda = local_ratio(state, geometry, weight, q, shift, edge);
                    close(lambda, expected, 1e-10, "local ratio identity failed");
                    ++estimator_identities;
                    // The conditional estimator must not depend on the value of its own link.
                    for (int a = 0; a < 5; ++a) {
                        State moved = state;
                        moved.links[edge] = static_cast<unsigned char>(a);
                        std::vector<int> touched;
                        for (const auto& inc : geometry.incidence[edge]) touched.push_back(inc.plaquette);
                        refresh(moved, geometry, touched, k);
                        close(local_ratio(moved, geometry, weight, q, shift, edge), lambda, 1e-12,
                              "local ratio depends on its own link");
                    }
                    ++invariance_checks;
                }
                const double naive = naive_ratio(state, weight, q, shift);
                close(naive, std::exp(predicted), 1e-13, "naive ratio failed");
                local_enumerations += local_enumeration(state, geometry, weight, k, direction);
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
        }
        // The declared chain-4 initial state itself must be the pure w = -1 layout,
        // and the declared chains 0 and 2 the pure w = 0 layouts.
        for (int k : {1, 2}) {
            Random r(0);
            const State alt = initial_state(geometry, weight, r, k, 4, 0);
            const Sector layout = sector(alt, geometry, k);
            require(layout.label == 1 && layout.twisted_minus == seam_size && layout.untwisted_nonzero == 0,
                    "chain 4 initial state is not pure w = -1");
            const State cold_top = initial_state(geometry, weight, r, k, 2, 0);
            require(sector(cold_top, geometry, k).label == 0, "chain 2 initial state is not pure w = 0");
            const State cold_bottom = initial_state(geometry, weight, r, k, 0, 0);
            require(sector(cold_bottom, geometry, k).untwisted_nonzero == 0, "chain 0 initial state has w != 0");
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
                    (void)sector(state, geometry, k);
                    ++exercise_sweeps;
                }
            }
        }
    }
    // Schedule exercise: the complete chain code path with a tiny schedule on
    // L=4, written into a buffer that is inspected for structure and discarded.
    // No sum, histogram or sector value from it is printed or retained.
    int schedule_rows = 0;
    {
        const Geometry geometry(4);
        const Heatbath kernel(weight);
        const Schedule tiny{4, block_length, block_length, 2};
        for (int k : {1, 2}) for (int base : {0, 2}) for (int chain : {0, 4, 2}) {
            if (base == 2 && chain == 4) continue;
            Random random(7);
            State state = initial_state(geometry, weight, random, k, chain, base);
            std::ostringstream buffer;
            execute(geometry, weight, kernel, state, random, k, chain, base, 0, tiny, buffer);
            std::istringstream lines(buffer.str());
            std::string line;
            int rows = 0, expected_segment = 0;
            bool completed = false;
            const int seam_size = 16;
            int twist = chain >= 2 ? seam_size : 0, direction = twist == 0 ? 1 : -1, visited = 0;
            while (std::getline(lines, line)) {
                if (line == "# completion\tPASS") { completed = true; continue; }
                if (line.empty() || line[0] == '#' || line[0] == 'L') continue;
                std::vector<std::string> fields;
                std::size_t start = 0;
                for (std::size_t tab = line.find('\t'); tab != std::string::npos; tab = line.find('\t', start)) {
                    fields.push_back(line.substr(start, tab - start));
                    start = tab + 1;
                }
                fields.push_back(line.substr(start));
                require(fields.size() == 39, "schedule exercise row has wrong field count");
                require(std::stoi(fields[3]) == expected_segment, "schedule exercise segment order");
                require(std::stoi(fields[4]) == twist, "schedule exercise twist order");
                require(std::stoi(fields[7]) == block_length, "schedule exercise block count");
                const std::string phase = fields[5];
                const bool dwell = (visited == 0 || visited == seam_size);
                require(phase == (dwell ? "dwell" : (direction == 1 ? "up" : "down")), "schedule exercise phase");
                ++rows;
                ++expected_segment;
                ++visited;
                if (visited == seam_size) { twist += direction; }
                else if (visited == seam_size + 1) { direction = -direction; twist += direction; }
                else if (visited < 2 * seam_size) { twist += direction; }
            }
            require(completed && rows == 2 * seam_size, "schedule exercise did not complete every segment");
            schedule_rows += rows;
        }
    }
    std::cout << "NON-CANONICAL floating-point engineering audit\n"
              << "geometries\t" << geometries << "\nfixture_states\t" << fixture_states
              << "\nestimator_identities\t" << estimator_identities
              << "\nlocal_enumerations\t" << local_enumerations
              << "\ninvariance_checks\t" << invariance_checks
              << "\ninversion_checks\t" << inversion_checks
              << "\nexercise_sweeps\t" << exercise_sweeps
              << "\nschedule_rows\t" << schedule_rows
              << "\nmutations_caught\t" << mutations_caught << "\nresult\tPASS\n";
}
} // namespace

int main(int argc, char** argv) {
    try {
        if (argc == 2 && std::string(argv[1]) == "--audit") {
            audit();
        } else {
            require(argc == 5, "usage: sample L k chain base | sample --audit");
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
