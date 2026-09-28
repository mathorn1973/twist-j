// NON-CANONICAL floating-point transport diagnostic; no scientific evidential weight.
// Successor to C-PHOTON-TWIST-ENDPOINT-DIAGNOSTIC-N/sample.cpp (PR #1250).
// Compile: g++ -std=c++17 -O3 -Wall -Wextra -pedantic sample.cpp -o sample
// Execute only after this complete successor's public pin has been read back.
// CLI: sample L k base chain | sample --audit
#include <algorithm>
#include <array>
#include <cmath>
#include <cstdint>
#include <iomanip>
#include <iostream>
#include <random>
#include <stdexcept>
#include <string>
#include <utility>
#include <vector>

namespace {
constexpr int warmup_sweeps = 2048;
constexpr int production_sweeps = 16384;
constexpr int block_length = 128;
constexpr int pattern_count = 15625; // 5^6
constexpr std::array<std::array<int, 2>, 6> pairs{{
    {{0, 1}}, {{0, 2}}, {{0, 3}}, {{1, 2}}, {{1, 3}}, {{2, 3}}
}};
void require(bool ok, const std::string& message) {
    if (!ok) throw std::runtime_error(message);
}
int mod5(int value) { value %= 5; return value < 0 ? value + 5 : value; }
int representative(int value) { value = mod5(value); return value <= 2 ? value : value - 5; }
void close(double a, double b, double tolerance, const std::string& label) {
    require(std::isfinite(a) && std::isfinite(b)
            && std::abs(a - b) <= tolerance * (1 + std::abs(a) + std::abs(b)), label);
}
struct Incidence { int plaquette = 0, sign = 0; };
struct Geometry {
    int L, volume, edges, plaquettes;
    std::array<int, 4> stride;
    std::vector<std::array<int, 4>> plus, minus;
    std::vector<std::array<Incidence, 6>> incidence;
    std::vector<int> cut_degree, seam, cut;
    std::vector<unsigned char> is_seam, is_cut;
    std::vector<std::vector<int>> sheet_links;
    std::vector<std::vector<std::pair<int, int>>> sheet_faces;
    explicit Geometry(int length)
        : L(length), volume(L * L * L * L), edges(4 * volume), plaquettes(6 * volume),
          stride{{1, L, L * L, L * L * L}}, plus(volume), minus(volume),
          incidence(edges), cut_degree(edges, 0), is_seam(plaquettes, 0),
          is_cut(plaquettes, 0), sheet_links(L), sheet_faces(L) {
        require(L == 4, "this frozen transport pilot supports L=4 only");
        for (int x = 0; x < volume; ++x) for (int mu = 0; mu < 4; ++mu) {
            const int c = (x / stride[mu]) % L;
            plus[x][mu] = x + (c + 1 == L ? 1 - L : 1) * stride[mu];
            minus[x][mu] = x + (c == 0 ? L - 1 : -1) * stride[mu];
        }
        std::vector<int> degree(edges, 0);
        for (int x = 0; x < volume; ++x) for (int pair = 0; pair < 6; ++pair) {
            const int mu = pairs[pair][0], nu = pairs[pair][1], p = 6 * x + pair;
            const std::array<int, 4> boundary{{4 * x + mu, 4 * plus[x][mu] + nu,
                                             4 * plus[x][nu] + mu, 4 * x + nu}};
            const std::array<int, 4> signs{{1, 1, -1, -1}};
            for (int j = 0; j < 4; ++j) {
                require(degree[boundary[j]] < 6, "edge incidence overflow");
                incidence[boundary[j]][degree[boundary[j]]++] = {p, signs[j]};
            }
            if (pair == 0 && x % L == 0) {
                cut.push_back(p); is_cut[p] = 1;
                const int j = (x / L) % L;
                sheet_links[j].push_back(4 * x);
                sheet_faces[j].push_back({p, 6 * minus[x][1]});
                if (j == 0) { seam.push_back(p); is_seam[p] = 1; }
            }
        }
        require(static_cast<int>(seam.size()) == L * L && static_cast<int>(cut.size()) == L * L * L,
                "wrong seam or cut cardinality");
        for (int edge = 0; edge < edges; ++edge) {
            require(degree[edge] == 6, "wrong edge degree");
            // The first m entries are precisely the cut factors in every lookup pattern.
            std::stable_sort(incidence[edge].begin(), incidence[edge].end(),
                [&](const Incidence& a, const Incidence& b) { return is_cut[a.plaquette] > is_cut[b.plaquette]; });
            for (int a = 0; a < 6; ++a) {
                cut_degree[edge] += is_cut[incidence[edge][a].plaquette];
                for (int b = a + 1; b < 6; ++b)
                    require(incidence[edge][a].plaquette != incidence[edge][b].plaquette,
                            "duplicate plaquette at edge");
            }
            require(cut_degree[edge] <= 2, "more than two cut incidences");
        }
        for (int j = 0; j < L; ++j)
            require(static_cast<int>(sheet_links[j].size()) == L * L
                    && sheet_faces[j].size() == sheet_links[j].size(), "wrong sheet orbit size");
    }
    int pair_index(int mu, int nu) const {
        for (int j = 0; j < 6; ++j) if (pairs[j][0] == mu && pairs[j][1] == nu) return j;
        throw std::runtime_error("invalid oriented pair");
    }
    int direct_flux(const std::vector<unsigned char>& links, int p, int endpoint, int k, int base) const {
        const int x = p / 6, pair = p % 6, mu = pairs[pair][0], nu = pairs[pair][1];
        return mod5(static_cast<int>(links[4 * x + mu]) + links[4 * plus[x][mu] + nu]
                    - links[4 * plus[x][nu] + mu] - links[4 * x + nu]
                    + (base + endpoint) * k * is_seam[p]);
    }
};
struct Random {
    std::mt19937_64 engine;
    explicit Random(std::uint64_t seed) : engine(seed) {}
    double unit() { return static_cast<double>(engine() >> 11) * 0x1.0p-53; }
    int five() {
        constexpr std::uint64_t threshold = (std::uint64_t(0) - 5) % 5;
        std::uint64_t value; do { value = engine(); } while (value < threshold);
        return static_cast<int>(value % 5);
    }
    bool metropolis(double log_ratio) { return log_ratio >= 0 || unit() < std::exp(log_ratio); }
};
struct Weights {
    std::array<double, 5> value, log_value, tangent;
    Weights() {
        const double phi = (1 + std::sqrt(5.0)) / 2;
        value = {{4, phi * phi, 1 / (phi * phi), 1 / (phi * phi), phi * phi}};
        for (int f = 0; f < 5; ++f) log_value[f] = std::log(value[f]);
        const double pi = std::acos(-1.0);
        tangent = {{0, std::tan(pi / 5), std::tan(2 * pi / 5), 0, 0}};
        tangent[3] = -tangent[2]; tangent[4] = -tangent[1];
    }
};
struct State {
    std::vector<unsigned char> links, flux;
    int endpoint = 0, id = 0;
    double score = 0, cut_score = 0; // native score includes cut; log density=score+(lambda-1)*cut_score
};
void rebuild(State& state, const Geometry& g, const Weights& w, int k, int base) {
    state.flux.resize(g.plaquettes);
    long double score = 0, cut_score = 0;
    for (int p = 0; p < g.plaquettes; ++p) {
        state.flux[p] = static_cast<unsigned char>(g.direct_flux(state.links, p, state.endpoint, k, base));
        const double v = w.log_value[state.flux[p]];
        score += v; if (g.is_cut[p]) cut_score += v;
    }
    state.score = static_cast<double>(score); state.cut_score = static_cast<double>(cut_score);
}
void validate(State& state, const Geometry& g, const Weights& w, int k, int base) {
    require(state.endpoint == 0 || state.endpoint == 1, "invalid endpoint");
    require(static_cast<int>(state.links.size()) == g.edges
            && static_cast<int>(state.flux.size()) == g.plaquettes, "invalid state size");
    for (unsigned char a : state.links) require(a < 5, "invalid link");
    long double score = 0, cut_score = 0;
    for (int p = 0; p < g.plaquettes; ++p) {
        const int f = g.direct_flux(state.links, p, state.endpoint, k, base);
        require(state.flux[p] == f, "cached flux differs from direct curl");
        score += w.log_value[f]; if (g.is_cut[p]) cut_score += w.log_value[f];
    }
    close(state.score, static_cast<double>(score), 1e-11, "native score drift");
    close(state.cut_score, static_cast<double>(cut_score), 1e-10, "cut score drift");
    state.score = static_cast<double>(score); state.cut_score = static_cast<double>(cut_score);
}
using Table = std::vector<std::array<double, 5>>;
Table make_table(int m, double lambda, const Weights& w) {
    Table cdf(pattern_count);
    std::array<double, 5> power{};
    for (int a = 0; a < 5; ++a) power[a] = std::exp(lambda * w.log_value[a]);
    for (int key = 0; key < pattern_count; ++key) {
        std::array<int, 6> staple{};
        int remaining = key;
        for (int i = 0; i < 6; ++i) { staple[i] = remaining % 5; remaining /= 5; }
        double sum = 0;
        for (int a = 0; a < 5; ++a) {
            double product = 1;
            for (int i = 0; i < 6; ++i)
                product *= i < m ? power[(staple[i] + a) % 5] : w.value[(staple[i] + a) % 5];
            sum += product; cdf[key][a] = sum;
        }
        require(std::isfinite(sum) && sum > 0, "invalid heatbath normalization");
        for (double& v : cdf[key]) v /= sum;
        cdf[key][4] = 1;
    }
    return cdf;
}
struct Heatbath {
    double lambda;
    const Table* bulk;
    std::array<Table, 2> cut_tables;
    Heatbath(double l, const Weights& w, const Table& common)
        : lambda(l), bulk(&common), cut_tables{{make_table(1, l, w), make_table(2, l, w)}} {}
    int pattern(const State& state, const Geometry& g, int edge) const {
        int key = 0, multiplier = 1;
        for (const Incidence& inc : g.incidence[edge]) {
            key += mod5(inc.sign * static_cast<int>(state.flux[inc.plaquette]) - state.links[edge]) * multiplier;
            multiplier *= 5;
        }
        return key;
    }
    const std::array<double, 5>& conditional(const State& state, const Geometry& g, int edge) const {
        const int m = g.cut_degree[edge], key = pattern(state, g, edge);
        return m == 0 ? (*bulk)[key] : cut_tables[m - 1][key];
    }
    void sweep(State& state, const Geometry& g, const Weights& w, Random& rng) const {
        for (int edge = 0; edge < g.edges; ++edge) {
            const auto& cdf = conditional(state, g, edge);
            const double u = rng.unit();
            int a = 0; while (a < 4 && u >= cdf[a]) ++a;
            const int delta = a - state.links[edge];
            if (delta == 0) continue;
            state.links[edge] = static_cast<unsigned char>(a);
            for (const Incidence& inc : g.incidence[edge]) {
                auto& f = state.flux[inc.plaquette];
                const int changed = mod5(f + inc.sign * delta);
                const double d = w.log_value[changed] - w.log_value[f];
                state.score += d; if (g.is_cut[inc.plaquette]) state.cut_score += d;
                f = static_cast<unsigned char>(changed);
            }
        }
    }
};
std::array<double, 5> sheet_probabilities(const State& state, const Geometry& g, const Weights& w,
                                         int j, double lambda) {
    std::array<double, 5> logs{}, probability{};
    for (int a = 0; a < 5; ++a) for (const auto& face : g.sheet_faces[j])
        logs[a] += lambda * (w.log_value[mod5(state.flux[face.first] + a)]
                          + w.log_value[mod5(state.flux[face.second] - a)]);
    const double maximum = *std::max_element(logs.begin(), logs.end());
    double sum = 0;
    for (int a = 0; a < 5; ++a) { probability[a] = std::exp(logs[a] - maximum); sum += probability[a]; }
    require(std::isfinite(sum) && sum > 0, "invalid sheet orbit normalization");
    for (double& v : probability) v /= sum;
    return probability;
}
void apply_sheet(State& state, const Geometry& g, const Weights& w, int j, int a) {
    if (a == 0) return;
    for (int edge : g.sheet_links[j]) state.links[edge] = static_cast<unsigned char>(mod5(state.links[edge] + a));
    double change = 0;
    for (const auto& face : g.sheet_faces[j]) {
        for (const auto& signed_face : {std::pair<int, int>{face.first, a}, {face.second, -a}}) {
            auto& f = state.flux[signed_face.first];
            const int changed = mod5(f + signed_face.second);
            change += w.log_value[changed] - w.log_value[f];
            f = static_cast<unsigned char>(changed);
        }
    }
    state.score += change; state.cut_score += change;
}
void sheet_sweep(State& state, const Geometry& g, const Weights& w, double lambda, Random& rng) {
    for (int j = 0; j < g.L; ++j) {
        const auto probability = sheet_probabilities(state, g, w, j, lambda);
        const double u = rng.unit();
        double sum = probability[0]; int a = 0;
        while (a < 4 && u >= sum) { ++a; sum += probability[a]; }
        apply_sheet(state, g, w, j, a);
    }
}
double endpoint_difference(const State& state, const Geometry& g, const Weights& w, int k) {
    const int delta = state.endpoint == 0 ? k : -k;
    double change = 0;
    for (int p : g.seam) change += w.log_value[mod5(state.flux[p] + delta)] - w.log_value[state.flux[p]];
    return change;
}
void apply_endpoint(State& state, const Geometry& g, int k, double change) {
    const int delta = state.endpoint == 0 ? k : -k;
    for (int p : g.seam) state.flux[p] = static_cast<unsigned char>(mod5(state.flux[p] + delta));
    state.endpoint = 1 - state.endpoint;
    state.score += change; state.cut_score += change;
}
bool endpoint_flip(State& state, const Geometry& g, const Weights& w, int k, double lambda, Random& rng) {
    const double change = endpoint_difference(state, g, w, k);
    if (!rng.metropolis(lambda * change)) return false;
    apply_endpoint(state, g, k, change); return true;
}
double observable(const State& state, const Geometry& g, const Weights& w) {
    double sum = 0;
    for (int x = 0; x < g.volume; ++x) sum += w.tangent[state.flux[6 * x]];
    return sum / (g.L * g.L);
}
struct Winding { double mean = 0, negative = 0, positive = 0; };
Winding winding(const State& state, const Geometry& g, int k, int base) {
    Winding result;
    const int q = representative(k * (base + state.endpoint));
    for (int x3 = 0; x3 < g.L; ++x3) for (int x2 = 0; x2 < g.L; ++x2) {
        int sum = 0;
        for (int x1 = 0; x1 < g.L; ++x1) for (int x0 = 0; x0 < g.L; ++x0) {
            const int x = x0 + g.L * (x1 + g.L * (x2 + g.L * x3));
            sum += representative(state.flux[6 * x]);
        }
        require((sum - q) % 5 == 0, "slice winding is not an integer");
        const int wind = (sum - q) / 5;
        result.mean += wind; result.negative += wind < 0; result.positive += wind > 0;
    }
    result.mean /= g.L * g.L; result.negative /= g.L * g.L; result.positive /= g.L * g.L;
    return result;
}
double swap_log_ratio(double l, double r, const State& left, const State& right) {
    return (l - r) * (right.cut_score - left.cut_score);
}
struct Counts {
    int n = 0, n0 = 0, nTpos = 0, nTneg = 0, target_T_sign_changes = 0;
    long double sumT = 0, sumT2 = 0, sumY0 = 0, sumY0sq = 0, sumPosT = 0, sumNegT = 0;
    long double sumW1 = 0, sumW0 = 0, sumM1 = 0, sumM0 = 0, sumP1 = 0, sumP0 = 0;
    long double sum_action = 0, sum_action2 = 0;
    int target_flip_attempts = 0, target_flip_accepts = 0, target_endpoint_changes = 0, roundtrips = 0;
    std::vector<int> attempts, accepts;
    explicit Counts(int n_edges) : attempts(n_edges, 0), accepts(n_edges, 0) {}
};
void print_block(int L, int k, int base, int chain, int block, const Counts& c) {
    int attempts = 0, accepts = 0; double minimum = 1;
    for (std::size_t j = 0; j < c.attempts.size(); ++j) {
        require(c.attempts[j] > 0, "unattempted ladder edge in block");
        attempts += c.attempts[j]; accepts += c.accepts[j];
        minimum = std::min(minimum, static_cast<double>(c.accepts[j]) / c.attempts[j]);
    }
    std::cout << L << '\t' << k << '\t' << base << '\t' << chain << '\t' << block << '\t'
              << c.n << '\t' << c.n0 << '\t' << c.sumT << '\t' << c.sumT2 << '\t'
              << c.sumY0 << '\t' << c.sumY0sq << '\t' << c.sumPosT << '\t' << c.sumNegT << '\t'
              << c.sumW1 << '\t' << c.sumW0 << '\t' << c.sumM1 << '\t' << c.sumM0 << '\t'
              << c.sumP1 << '\t' << c.sumP0 << '\t' << c.nTpos << '\t' << c.nTneg << '\t'
              << c.target_T_sign_changes << '\t' << c.sum_action << '\t' << c.sum_action2 << '\t'
              << c.target_flip_attempts << '\t' << c.target_flip_accepts << '\t'
              << c.target_endpoint_changes << '\t' << attempts << '\t' << accepts << '\t'
              << minimum << '\t' << c.roundtrips << '\n';
}
const std::array<std::string, 5> start_names{{"cold0", "hot0", "cold1", "hot1", "alt1"}};
void initialize(State& state, const Geometry& g, const Weights& w, int k, int base, int chain, Random& rng) {
    state.links.assign(g.edges, 0); state.endpoint = chain >= 2 ? 1 : 0;
    if (chain == 1 || chain == 3)
        for (auto& a : state.links) a = static_cast<unsigned char>(rng.five());
    if (chain == 4) {
        const int q = representative(k * (base + 1));
        require(q != 0, "alternate fixture requires nonzero source");
        const int a = mod5(q > 0 ? 2 : -2);
        for (int edge : g.sheet_links[0]) state.links[edge] = static_cast<unsigned char>(a);
    }
    rebuild(state, g, w, k, base); validate(state, g, w, k, base);
}
void run(int L, int k, int base, int chain) {
    require(L == 4 && (k == 1 || k == 2) && (base == 0 || base == 2) && chain >= 0 && chain < 5,
            "allowed arguments: L=4, k in {1,2}, base in {0,2}, chain in {0,1,2,3,4}");
    const Geometry g(L); const Weights w; const int replicas = 4 * L * L + 1;
    const std::uint64_t seed = UINT64_C(202609280000) + 10000 * base + 1000 * L + 100 * k + chain;
    Random rng(seed); const Table bulk = make_table(0, 1, w);
    std::vector<Heatbath> kernels; kernels.reserve(replicas);
    std::vector<State> states(replicas);
    for (int j = 0; j < replicas; ++j) {
        kernels.emplace_back(static_cast<double>(j) / (4 * L * L), w, bulk);
        states[j].id = j; initialize(states[j], g, w, k, base, chain, rng);
    }
    std::cout << std::setprecision(17)
              << "# format\ttwist_cut_transport_blocks_v1\n"
              << "# status\tNON-CANONICAL floating-point engineering diagnostic\n"
              << "# L\t" << L << "\n# k\t" << k << "\n# base\t" << base << "\n# chain\t" << chain
              << "\n# seed\t" << seed << "\n# replicas\t" << replicas
              << "\n# warmup_sweeps\t" << warmup_sweeps << "\n# production_sweeps\t" << production_sweeps
              << "\n# block_length\t" << block_length << "\n# chain_initial\t" << start_names[chain]
              << "\n# cut\tall_01_plaquettes_x0_equals_0"
              << "\n# sheet_orbits\tall_x1_slices_every_replica_every_sweep"
              << "\n# lambda_ladder\t";
    for (int j = 0; j < replicas; ++j) { if (j) std::cout << ','; std::cout << kernels[j].lambda; }
    std::cout << "\n# endpoint_proposal_probability\t0.5\n"
              << "# action_density\tminus_native_sum_logW_divided_by_6L4\n"
              << "# sampling\tevery_production_sweep_after_local_sheet_endpoint_and_exchange_updates\n"
              << "L\tk\tbase\tchain\tblock\tn\tn0\tsumT\tsumT2\tsumY0\tsumY0sq\tsumPosT\tsumNegT"
              << "\tsumW1\tsumW0\tsumM1\tsumM0\tsumP1\tsumP0\tnTpos\tnTneg\ttarget_T_sign_changes"
              << "\tsum_action\tsum_action2\ttarget_flip_attempts\ttarget_flip_accepts"
              << "\ttarget_endpoint_changes\tswap_attempts\tswap_accepts\tmin_swap_accept\troundtrips\n";
    Counts block(replicas - 1);
    std::vector<int> total_attempts(replicas - 1, 0), total_accepts(replicas - 1, 0);
    std::vector<int> trip_stage(replicas, 0), trips(replicas, 0);
    int previous_endpoint = states.back().endpoint, previous_T_sign = 0;
    for (int sweep = 0; sweep < warmup_sweeps + production_sweeps; ++sweep) {
        const bool production = sweep >= warmup_sweeps;
        if (sweep == warmup_sweeps) {
            trip_stage.assign(replicas, 0); trip_stage[states.front().id] = 1;
            previous_endpoint = states.back().endpoint; previous_T_sign = 0;
        }
        for (int j = 0; j < replicas; ++j) {
            kernels[j].sweep(states[j], g, w, rng);
            sheet_sweep(states[j], g, w, kernels[j].lambda, rng);
            if (rng.unit() < 0.5) {
                const bool accepted = endpoint_flip(states[j], g, w, k, kernels[j].lambda, rng);
                if (production && j == replicas - 1) { ++block.target_flip_attempts; block.target_flip_accepts += accepted; }
            }
        }
        for (int j = sweep % 2; j + 1 < replicas; j += 2) {
            const bool accepted = rng.metropolis(swap_log_ratio(kernels[j].lambda, kernels[j + 1].lambda,
                                                                states[j], states[j + 1]));
            if (accepted) std::swap(states[j], states[j + 1]);
            if (production) {
                ++block.attempts[j]; block.accepts[j] += accepted;
                ++total_attempts[j]; total_accepts[j] += accepted;
            }
        }
        if ((sweep + 1) % block_length == 0) {
            std::vector<int> seen(replicas, 0);
            for (auto& state : states) {
                validate(state, g, w, k, base);
                require(state.id >= 0 && state.id < replicas, "invalid travelling id"); ++seen[state.id];
            }
            for (int count : seen) require(count == 1, "duplicate travelling id");
        }
        if (!production) continue;
        int& low = trip_stage[states.front().id];
        if (low == 2) { ++trips[states.front().id]; ++block.roundtrips; }
        low = 1;
        int& high = trip_stage[states.back().id]; if (high == 1) high = 2;
        const State& target = states.back();
        block.target_endpoint_changes += target.endpoint != previous_endpoint; previous_endpoint = target.endpoint;
        const double Y = observable(target, g, w), T = target.endpoint ? Y : 0,
                     Y0 = target.endpoint ? 0 : Y, action = -target.score / g.plaquettes;
        const Winding wind = winding(target, g, k, base);
        require(std::isfinite(Y) && std::isfinite(action), "nonfinite observable");
        ++block.n; block.n0 += target.endpoint == 0;
        block.sumT += T; block.sumT2 += T * T; block.sumY0 += Y0; block.sumY0sq += Y0 * Y0;
        block.sumPosT += std::max(T, 0.0); block.sumNegT += std::max(-T, 0.0);
        if (target.endpoint) {
            block.sumW1 += wind.mean; block.sumM1 += wind.negative; block.sumP1 += wind.positive;
            const int sign = Y > 0 ? 1 : (Y < 0 ? -1 : 0);
            block.nTpos += sign > 0; block.nTneg += sign < 0;
            if (sign != 0) {
                if (previous_T_sign != 0 && sign != previous_T_sign) ++block.target_T_sign_changes;
                previous_T_sign = sign;
            }
        } else { block.sumW0 += wind.mean; block.sumM0 += wind.negative; block.sumP0 += wind.positive; }
        block.sum_action += action; block.sum_action2 += action * action;
        if (block.n == block_length) {
            print_block(L, k, base, chain, (sweep - warmup_sweeps) / block_length, block);
            block = Counts(replicas - 1);
        }
    }
    require(block.n == 0, "incomplete production block");
    for (auto& state : states) validate(state, g, w, k, base);
    for (int j = 0; j + 1 < replicas; ++j)
        std::cout << "# swap_edge\t" << j << '\t' << total_attempts[j] << '\t' << total_accepts[j] << '\n';
    for (int id = 0; id < replicas; ++id)
        std::cout << "# replica_roundtrips\t" << id << '\t' << trips[id] << '\n';
    std::cout << "# completion\tPASS\n";
}

void audit() {
    const Geometry g(4); const Weights w; const Table bulk = make_table(0, 1, w);
    std::vector<Heatbath> kernels;
    for (double lambda : {0.0, 0.5, 1.0}) kernels.emplace_back(lambda, w, bulk);
    for (int x = 0; x < g.volume; ++x) for (int mu = 0; mu < 4; ++mu) {
        require(g.minus[g.plus[x][mu]][mu] == x, "neighbor inverse failed");
        for (int nu = 0; nu < 4; ++nu)
            require(g.plus[g.plus[x][mu]][nu] == g.plus[g.plus[x][nu]][mu], "neighbors do not commute");
    }
    std::array<int, 3> type_edge{{-1, -1, -1}};
    for (int edge = 0; edge < g.edges; ++edge) type_edge[g.cut_degree[edge]] = edge;
    for (int edge : type_edge) require(edge >= 0, "missing local cut type");
    for (int base : {0, 2}) for (int k : {1, 2}) for (int endpoint : {0, 1}) {
        State state; state.endpoint = endpoint; state.links.resize(g.edges);
        for (int edge = 0; edge < g.edges; ++edge)
            state.links[edge] = static_cast<unsigned char>((edge * edge + edge / 7 + 3) % 5);
        rebuild(state, g, w, k, base); validate(state, g, w, k, base);
        (void)winding(state, g, k, base);
        for (int x = 0; x < g.volume; ++x) for (int mu = 0; mu < 4; ++mu)
            for (int nu = mu + 1; nu < 4; ++nu) for (int rho = nu + 1; rho < 4; ++rho) {
                const int nr = g.pair_index(nu, rho), mr = g.pair_index(mu, rho), mn = g.pair_index(mu, nu);
                const int d = state.flux[6 * g.plus[x][mu] + nr] - state.flux[6 * x + nr]
                    - state.flux[6 * g.plus[x][nu] + mr] + state.flux[6 * x + mr]
                    + state.flux[6 * g.plus[x][rho] + mn] - state.flux[6 * x + mn];
                require(mod5(d) == 0, "d squared is not zero");
            }
        // An isolated link change has precisely the six geometrically listed effects.
        for (int edge : type_edge) {
            State changed = state;
            changed.links[edge] = static_cast<unsigned char>(mod5(changed.links[edge] + 1));
            rebuild(changed, g, w, k, base);
            std::vector<int> expected(g.plaquettes, 0);
            for (const Incidence& inc : g.incidence[edge]) expected[inc.plaquette] = mod5(inc.sign);
            for (int p = 0; p < g.plaquettes; ++p)
                require(mod5(changed.flux[p] - state.flux[p]) == expected[p], "incidence versus curl mismatch");
        }
        for (const auto& kernel : kernels) {
            State changed = state; Random rng(17);
            kernel.sweep(changed, g, w, rng);
            validate(changed, g, w, k, base);
            sheet_sweep(changed, g, w, kernel.lambda, rng);
            validate(changed, g, w, k, base);
        }
        for (const auto& kernel : kernels) for (int edge : type_edge) {
            const auto& cdf = kernel.conditional(state, g, edge);
            std::array<double, 5> probability{}, scores{};
            for (int a = 0; a < 5; ++a) {
                probability[a] = cdf[a] - (a == 0 ? 0 : cdf[a - 1]);
                require(probability[a] > 0, "nonpositive local conditional probability");
                auto links = state.links; links[edge] = static_cast<unsigned char>(a);
                for (const Incidence& inc : g.incidence[edge]) {
                    const int p = inc.plaquette;
                    scores[a] += (g.is_cut[p] ? kernel.lambda : 1) * w.log_value[g.direct_flux(links, p, endpoint, k, base)];
                }
            }
            for (int a = 0; a < 5; ++a) for (int b = 0; b < 5; ++b)
                close(std::log(probability[a]) - std::log(probability[b]), scores[a] - scores[b], 2e-9,
                      "local conditional balance failed");
        }
        for (int j = 0; j < g.L; ++j) for (const auto& kernel : kernels) {
            const auto probability = sheet_probabilities(state, g, w, j, kernel.lambda);
            double total = 0;
            for (int a = 0; a < 5; ++a) {
                total += probability[a]; require(probability[a] > 0, "nonpositive orbit weight");
                State changed = state; apply_sheet(changed, g, w, j, a);
                validate(changed, g, w, k, base);
                close(changed.score - state.score, changed.cut_score - state.cut_score, 2e-11,
                      "sheet changed bulk score");
                close(std::log(probability[a]) - std::log(probability[0]),
                      kernel.lambda * (changed.cut_score - state.cut_score), 2e-11, "sheet conditional ratio failed");
                const auto back = sheet_probabilities(changed, g, w, j, kernel.lambda);
                close(probability[a], back[0], 1e-12, "sheet translated conditional normalization failed");
                close(std::log(probability[a]) - std::log(back[mod5(-a)]),
                      kernel.lambda * (changed.cut_score - state.cut_score), 2e-11, "sheet balance failed");
                apply_sheet(changed, g, w, j, mod5(-a));
                require(changed.links == state.links && changed.flux == state.flux, "sheet inverse failed");
                if (kernel.lambda == 0) close(probability[a], 0.2, 1e-15, "zero-cut orbit is not uniform");
            }
            close(total, 1, 1e-15, "sheet probability normalization failed");
        }
        const double change = endpoint_difference(state, g, w, k);
        State flipped = state; apply_endpoint(flipped, g, k, change); validate(flipped, g, w, k, base);
        close(endpoint_difference(flipped, g, w, k), -change, 1e-12, "endpoint inverse difference failed");
        close(flipped.score - state.score, change, 2e-11, "endpoint native score failed");
        close(flipped.cut_score - state.cut_score, change, 2e-11, "endpoint cut score failed");
        for (double lambda : {0.0, 0.5, 1.0})
            close(std::min(0.0, lambda * change) - std::min(0.0, -lambda * change), lambda * change,
                  1e-14, "endpoint balance failed");
        const double ratio = swap_log_ratio(0.25, 0.75, state, flipped);
        close(ratio, -swap_log_ratio(0.25, 0.75, flipped, state), 1e-14, "swap inverse failed");
        const auto density = [](const State& s, double lambda) { return s.score + (lambda - 1) * s.cut_score; };
        close(ratio, density(flipped, 0.25) + density(state, 0.75)
                     - density(state, 0.25) - density(flipped, 0.75), 2e-10, "swap target ratio failed");
        if (base == 2) {
            State reversed = state; reversed.endpoint = 1 - endpoint;
            for (auto& a : reversed.links) a = static_cast<unsigned char>(mod5(-a));
            rebuild(reversed, g, w, k, base);
            for (int p = 0; p < g.plaquettes; ++p)
                require(reversed.flux[p] == mod5(-state.flux[p]), "control reversal flux mismatch");
            close(state.score, reversed.score, 1e-14, "control reversal native score mismatch");
            close(state.cut_score, reversed.cut_score, 1e-14, "control reversal cut score mismatch");
            close(observable(state, g, w), -observable(reversed, g, w), 1e-13, "control reversal Y mismatch");
            const auto a = winding(state, g, k, base), b = winding(reversed, g, k, base);
            close(a.mean, -b.mean, 1e-14, "control reversal winding mismatch");
            close(a.negative, b.positive, 1e-14, "control reversal winding sign mismatch");
            reversed.endpoint = 1 - reversed.endpoint;
            for (auto& link : reversed.links) link = static_cast<unsigned char>(mod5(-link));
            require(reversed.links == state.links && reversed.endpoint == state.endpoint, "control reversal not involutive");
        }
        for (int corruption = 0; corruption < 3; ++corruption) {
            State broken = state;
            if (corruption == 0) broken.flux[0] = static_cast<unsigned char>(mod5(broken.flux[0] + 1));
            if (corruption == 1) broken.score += 1;
            if (corruption == 2) broken.cut_score += 1;
            bool caught = false;
            try { validate(broken, g, w, k, base); } catch (const std::runtime_error&) { caught = true; }
            require(caught, "frozen cache corruption escaped validation");
        }
    }
    for (int base : {0, 2}) for (int k : {1, 2}) {
        Random rng(0); State state; initialize(state, g, w, k, base, 4, rng);
        const Winding a = winding(state, g, k, base);
        const int q = representative(k * (base + 1));
        close(a.mean, q > 0 ? -1 : 1, 1e-15, "alternate slice fixture has wrong winding");
        close(a.negative + a.positive, 1, 1e-15, "alternate fixture has a zero slice");
    }
    std::cout << "NON-CANONICAL floating-point engineering audit\nresult\tPASS\n";
}
} // namespace
int main(int argc, char** argv) {
    try {
        if (argc == 2 && std::string(argv[1]) == "--audit") audit();
        else {
            require(argc == 5, "usage: sample L k base chain | sample --audit");
            std::array<int, 4> argument{};
            for (int j = 0; j < 4; ++j) {
                std::size_t consumed = 0; argument[j] = std::stoi(argv[j + 1], &consumed);
                require(consumed == std::string(argv[j + 1]).size(), "noninteger argument");
            }
            run(argument[0], argument[1], argument[2], argument[3]);
        }
        require(static_cast<bool>(std::cout), "stdout write failed"); return 0;
    } catch (const std::exception& error) { std::cerr << "ERROR: " << error.what() << '\n'; return 1; }
}
