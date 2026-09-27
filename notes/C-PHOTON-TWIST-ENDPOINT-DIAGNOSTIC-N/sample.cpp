// NON-CANONICAL, floating-point engineering diagnostic; not a proof.
// Compile: g++ -std=c++17 -O3 -Wall -Wextra -pedantic sample.cpp -o /tmp/twist-endpoint
// Execute only after the public preregistration pin has been read back.
// CLI: sample L k chain | sample --audit
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
#include <stdexcept>
#include <string>
#include <utility>
#include <vector>

namespace {
constexpr int warmup_sweeps = 512;
constexpr int production_sweeps = 4096;
constexpr int block_length = 128;
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

struct Geometry {
    int L, volume, edges, plaquettes;
    std::array<int, 4> stride;
    std::vector<std::array<int, 4>> plus;
    std::vector<std::array<int, 4>> minus;
    std::vector<std::array<Incidence, 6>> incidence;
    std::vector<int> seam;
    std::vector<unsigned char> is_seam;

    explicit Geometry(int length)
        : L(length), volume(length * length * length * length),
          edges(4 * volume), plaquettes(6 * volume),
          stride{{1, length, length * length, length * length * length}},
          plus(volume), minus(volume), incidence(edges), is_seam(plaquettes, 0) {
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
                const std::array<int, 4> boundary{{
                    4 * x + mu, 4 * plus[x][mu] + nu,
                    4 * plus[x][nu] + mu, 4 * x + nu
                }};
                const std::array<int, 4> signs{{1, 1, -1, -1}};
                for (int j = 0; j < 4; ++j) {
                    require(degree[boundary[j]] < 6, "edge incidence overflow");
                    incidence[boundary[j]][degree[boundary[j]]++] = {p, signs[j]};
                }
                if (pair == 0 && x % L == 0 && (x / L) % L == 0) {
                    seam.push_back(p);
                    is_seam[p] = 1;
                }
            }
        }
        require(static_cast<int>(seam.size()) == L * L, "wrong seam cardinality");
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

    int direct_flux(const std::vector<unsigned char>& links, int p, int endpoint, int k) const {
        const int x = p / 6, pair = p % 6;
        const int mu = pairs[pair][0], nu = pairs[pair][1];
        return mod5(static_cast<int>(links[4 * x + mu])
                    + links[4 * plus[x][mu] + nu]
                    - links[4 * plus[x][nu] + mu] - links[4 * x + nu]
                    + endpoint * k * is_seam[p]);
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
    bool metropolis(double log_ratio) {
        return log_ratio >= 0.0 || unit() < std::exp(log_ratio);
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
    std::vector<unsigned char> links, flux;
    int endpoint = 0;
    int id = 0;
    double score = 0.0; // sum_p log W(f_p), not negative action
};

void rebuild(State& state, const Geometry& geometry, const Weights& weight, int k) {
    state.flux.resize(geometry.plaquettes);
    long double score = 0;
    for (int p = 0; p < geometry.plaquettes; ++p) {
        state.flux[p] = static_cast<unsigned char>(geometry.direct_flux(state.links, p, state.endpoint, k));
        score += weight.log_value[state.flux[p]];
    }
    state.score = static_cast<double>(score);
}

void validate(State& state, const Geometry& geometry, const Weights& weight, int k) {
    require(state.endpoint == 0 || state.endpoint == 1, "invalid endpoint");
    require(static_cast<int>(state.links.size()) == geometry.edges
            && static_cast<int>(state.flux.size()) == geometry.plaquettes, "invalid state size");
    for (unsigned char a : state.links) require(a < 5, "invalid link value");
    long double score = 0;
    for (int p = 0; p < geometry.plaquettes; ++p) {
        const int exact = geometry.direct_flux(state.links, p, state.endpoint, k);
        require(state.flux[p] == exact, "cached plaquette differs from direct curl");
        score += weight.log_value[exact];
    }
    const double recomputed = static_cast<double>(score);
    const double tolerance = 1e-8 * geometry.plaquettes;
    require(std::isfinite(state.score) && std::abs(state.score - recomputed) <= tolerance,
            "cached score drift exceeds 1e-8 times plaquette count");
    state.score = recomputed;
}

// All 5^6 staple patterns. W is even, so b_i=sign_i*f_i-alpha_e
// gives conditional weight prod_i W(b_i+a)^beta for link candidate a.
struct Heatbath {
    double beta;
    std::vector<std::array<double, 5>> cdf;
    Heatbath(double inverse_temperature, const Weights& weight)
        : beta(inverse_temperature), cdf(pattern_count) {
        std::array<double, 5> power{};
        for (int a = 0; a < 5; ++a) power[a] = std::exp(beta * weight.log_value[a]);
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
                for (int b : staple) product *= power[(b + a) % 5];
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

    void sweep(State& state, const Geometry& geometry, const Weights& weight, Random& random) const {
        for (int edge = 0; edge < geometry.edges; ++edge) {
            const auto& cumulative = cdf[pattern(state, geometry, edge)];
            const double uniform = random.unit();
            int selected = 0;
            while (selected < 4 && uniform >= cumulative[selected]) ++selected;
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

double endpoint_score_difference(const State& state, const Geometry& geometry,
                                 const Weights& weight, int k) {
    const int delta = (state.endpoint == 0 ? k : -k);
    double change = 0;
    for (int p : geometry.seam)
        change += weight.log_value[mod5(state.flux[p] + delta)] - weight.log_value[state.flux[p]];
    return change;
}

void apply_endpoint_flip(State& state, const Geometry& geometry, int k, double score_difference) {
    const int delta = (state.endpoint == 0 ? k : -k);
    for (int p : geometry.seam) state.flux[p] = static_cast<unsigned char>(mod5(state.flux[p] + delta));
    state.endpoint = 1 - state.endpoint;
    state.score += score_difference;
}

bool endpoint_flip(State& state, const Geometry& geometry, const Weights& weight,
                   int k, double beta, Random& random) {
    const double change = endpoint_score_difference(state, geometry, weight, k);
    if (!random.metropolis(beta * change)) return false;
    apply_endpoint_flip(state, geometry, k, change);
    return true;
}

double observable(const State& state, const Geometry& geometry, const Weights& weight) {
    double sum = 0;
    for (int x = 0; x < geometry.volume; ++x) sum += weight.tangent[state.flux[6 * x]];
    return sum / (geometry.L * geometry.L);
}

double swap_log_ratio(double beta_left, double beta_right, const State& left, const State& right) {
    return (beta_left - beta_right) * (right.score - left.score);
}

struct Counts {
    int n = 0, n0 = 0;
    long double sumT = 0, sumT2 = 0, sumY0 = 0, sumY0sq = 0;
    long double sum_action = 0, sum_action2 = 0;
    int target_flip_attempts = 0, target_flip_accepts = 0, target_endpoint_changes = 0;
    int roundtrips = 0;
    std::vector<int> attempts, accepts;
    explicit Counts(int edges) : attempts(edges, 0), accepts(edges, 0) {}
};

void print_block(int L, int k, int chain, int block, const Counts& count) {
    int attempts = 0, accepts = 0;
    double minimum = 1;
    for (std::size_t j = 0; j < count.attempts.size(); ++j) {
        require(count.attempts[j] > 0, "unattempted temperature edge in block");
        attempts += count.attempts[j];
        accepts += count.accepts[j];
        minimum = std::min(minimum, static_cast<double>(count.accepts[j]) / count.attempts[j]);
    }
    std::cout << L << '\t' << k << '\t' << chain << '\t' << block << '\t'
              << count.n << '\t' << count.n0 << '\t' << count.sumT << '\t' << count.sumT2 << '\t'
              << count.sumY0 << '\t' << count.sumY0sq << '\t'
              << count.sum_action << '\t' << count.sum_action2 << '\t'
              << count.target_flip_attempts << '\t' << count.target_flip_accepts << '\t'
              << count.target_endpoint_changes << '\t' << attempts << '\t' << accepts << '\t'
              << minimum << '\t' << count.roundtrips << '\n';
}

void run(int L, int k, int chain) {
    require((L == 4 || L == 6 || L == 8) && (k == 1 || k == 2) && chain >= 0 && chain < 4,
            "allowed arguments: L in {4,6,8}, k in {1,2}, chain in {0,1,2,3}");
    const Geometry geometry(L);
    const Weights weight;
    const int replicas = 2 * L + 1;
    const std::uint64_t seed = UINT64_C(202609270000) + 1000 * L + 100 * k + chain;
    Random random(seed);
    std::vector<Heatbath> kernels;
    kernels.reserve(replicas);
    std::vector<State> states(replicas);
    for (int j = 0; j < replicas; ++j) {
        kernels.emplace_back(static_cast<double>(j) / (2 * L), weight);
        states[j].links.resize(geometry.edges, 0);
        states[j].endpoint = chain >= 2 ? 1 : 0;
        states[j].id = j;
        if (chain % 2 == 1)
            for (auto& a : states[j].links) a = static_cast<unsigned char>(random.five());
        rebuild(states[j], geometry, weight, k);
        validate(states[j], geometry, weight, k);
    }
    std::cout << std::setprecision(17)
              << "# format\ttwist_endpoint_blocks_v1\n"
              << "# status\tNON-CANONICAL floating-point engineering diagnostic\n"
              << "# L\t" << L << "\n# k\t" << k << "\n# chain\t" << chain
              << "\n# seed\t" << seed << "\n# replicas\t" << replicas
              << "\n# warmup_sweeps\t" << warmup_sweeps
              << "\n# production_sweeps\t" << production_sweeps
              << "\n# block_length\t" << block_length
              << "\n# start\t" << (chain % 2 ? "hot" : "cold") << ",s=" << (chain >= 2 ? 1 : 0)
              << "\n# chain_initial\t" << (chain % 2 ? "hot" : "cold") << (chain >= 2 ? 1 : 0)
              << "\n# beta_ladder\t";
    for (int j = 0; j < replicas; ++j) {
        if (j != 0) std::cout << ',';
        std::cout << kernels[j].beta;
    }
    std::cout << "\n# endpoint_proposal_probability\t0.5\n"
              << "# action_density\tminus_sum_logW_divided_by_6L4\n"
              << "# sampling\tevery_production_sweep_after_local_endpoint_and_exchange_updates\n"
              << "L\tk\tchain\tblock\tn\tn0\tsumT\tsumT2\tsumY0\tsumY0sq"
              << "\tsum_action\tsum_action2\ttarget_flip_attempts\ttarget_flip_accepts"
              << "\ttarget_endpoint_changes\tswap_attempts\tswap_accepts\tmin_swap_accept\troundtrips\n";
    Counts block(replicas - 1);
    std::vector<int> total_attempts(replicas - 1, 0), total_accepts(replicas - 1, 0);
    std::vector<int> trip_stage(replicas, 0), trips(replicas, 0);
    int previous_endpoint = states.back().endpoint;
    for (int sweep = 0; sweep < warmup_sweeps + production_sweeps; ++sweep) {
        const bool production = sweep >= warmup_sweeps;
        if (sweep == warmup_sweeps) {
            trip_stage.assign(replicas, 0);
            trip_stage[states.front().id] = 1;
            previous_endpoint = states.back().endpoint;
        }
        for (int j = 0; j < replicas; ++j) {
            kernels[j].sweep(states[j], geometry, weight, random);
            if (random.unit() < 0.5) {
                const bool accepted = endpoint_flip(states[j], geometry, weight, k, kernels[j].beta, random);
                if (production && j == replicas - 1) {
                    ++block.target_flip_attempts;
                    block.target_flip_accepts += accepted;
                }
            }
        }
        for (int j = sweep % 2; j + 1 < replicas; j += 2) {
            const bool accepted = random.metropolis(swap_log_ratio(kernels[j].beta, kernels[j + 1].beta,
                                                                  states[j], states[j + 1]));
            if (accepted) std::swap(states[j], states[j + 1]);
            if (production) {
                ++block.attempts[j];
                block.accepts[j] += accepted;
                ++total_attempts[j];
                total_accepts[j] += accepted;
            }
        }
        if ((sweep + 1) % block_length == 0) {
            std::vector<int> seen(replicas, 0);
            for (auto& state : states) {
                validate(state, geometry, weight, k);
                require(state.id >= 0 && state.id < replicas, "invalid travelling replica id");
                ++seen[state.id];
            }
            for (int count : seen) require(count == 1, "replica identity duplicated during exchange");
        }
        if (!production) continue;
        int& low_stage = trip_stage[states.front().id];
        if (low_stage == 2) {
            ++trips[states.front().id];
            ++block.roundtrips;
        }
        low_stage = 1;
        int& high_stage = trip_stage[states.back().id];
        if (high_stage == 1) high_stage = 2;
        const State& target = states.back();
        block.target_endpoint_changes += target.endpoint != previous_endpoint;
        previous_endpoint = target.endpoint;
        const double Y = observable(target, geometry, weight);
        const double T = target.endpoint ? Y : 0.0;
        const double Y0 = target.endpoint ? 0.0 : Y;
        const double action = -target.score / geometry.plaquettes;
        require(std::isfinite(Y) && std::isfinite(action), "nonfinite observable");
        ++block.n;
        block.n0 += target.endpoint == 0;
        block.sumT += T;
        block.sumT2 += T * T;
        block.sumY0 += Y0;
        block.sumY0sq += Y0 * Y0;
        block.sum_action += action;
        block.sum_action2 += action * action;
        if (block.n == block_length) {
            print_block(L, k, chain, (sweep - warmup_sweeps) / block_length, block);
            block = Counts(replicas - 1);
        }
    }
    require(block.n == 0, "incomplete production block");
    for (auto& state : states) validate(state, geometry, weight, k);
    for (int j = 0; j + 1 < replicas; ++j)
        std::cout << "# swap_edge\t" << j << '\t' << total_attempts[j] << '\t' << total_accepts[j] << '\n';
    for (int id = 0; id < replicas; ++id)
        std::cout << "# replica_roundtrips\t" << id << '\t' << trips[id] << '\n';
    std::cout << "# completion\tPASS\n";
}

void close(double left, double right, double tolerance, const std::string& label) {
    require(std::isfinite(left) && std::isfinite(right)
            && std::abs(left - right) <= tolerance * (1.0 + std::abs(left) + std::abs(right)), label);
}

void audit() {
    const Weights weight;
    int geometries = 0, states_checked = 0, mutations_caught = 0;
    for (int L : {4, 6, 8}) {
        const Geometry geometry(L);
        ++geometries;
        for (int x = 0; x < geometry.volume; ++x)
            for (int mu = 0; mu < 4; ++mu) {
                require(geometry.minus[geometry.plus[x][mu]][mu] == x, "neighbor inverse failed");
                for (int nu = 0; nu < 4; ++nu)
                    require(geometry.plus[geometry.plus[x][mu]][nu]
                            == geometry.plus[geometry.plus[x][nu]][mu], "neighbors do not commute");
            }
        for (int k : {1, 2}) for (int endpoint : {0, 1}) {
            State state;
            state.links.resize(geometry.edges);
            state.endpoint = endpoint;
            for (int edge = 0; edge < geometry.edges; ++edge)
                state.links[edge] = static_cast<unsigned char>((edge * edge + edge / 7 + 3) % 5);
            rebuild(state, geometry, weight, k);
            validate(state, geometry, weight, k);
            ++states_checked;
            // Independently sum the six faces of every elementary 3-cell.
            for (int x = 0; x < geometry.volume; ++x)
                for (int mu = 0; mu < 4; ++mu)
                    for (int nu = mu + 1; nu < 4; ++nu)
                        for (int rho = nu + 1; rho < 4; ++rho) {
                            const int nr = geometry.pair_index(nu, rho);
                            const int mr = geometry.pair_index(mu, rho);
                            const int mn = geometry.pair_index(mu, nu);
                            const int boundary = state.flux[6 * geometry.plus[x][mu] + nr] - state.flux[6 * x + nr]
                                - state.flux[6 * geometry.plus[x][nu] + mr] + state.flux[6 * x + mr]
                                + state.flux[6 * geometry.plus[x][rho] + mn] - state.flux[6 * x + mn];
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
            for (double beta : {0.0, 0.5, 1.0}) {
                const Heatbath kernel(beta, weight);
                for (int edge : {0, 1, geometry.edges / 2, geometry.edges - 1}) {
                    const auto& cdf = kernel.cdf[kernel.pattern(state, geometry, edge)];
                    std::array<double, 5> probability{}, scores{};
                    for (int a = 0; a < 5; ++a) {
                        probability[a] = cdf[a] - (a == 0 ? 0.0 : cdf[a - 1]);
                        require(probability[a] > 0, "nonpositive heatbath probability");
                        auto links = state.links;
                        links[edge] = static_cast<unsigned char>(a);
                        for (const auto& incident : geometry.incidence[edge])
                            scores[a] += weight.log_value[geometry.direct_flux(links, incident.plaquette, endpoint, k)];
                    }
                    for (int a = 0; a < 5; ++a) for (int b = 0; b < 5; ++b)
                        close(std::log(probability[a]) - std::log(probability[b]), beta * (scores[a] - scores[b]),
                              2e-10, "heatbath pairwise balance failed");
                }
            }
            const double change = endpoint_score_difference(state, geometry, weight, k);
            State flipped = state;
            apply_endpoint_flip(flipped, geometry, k, change);
            validate(flipped, geometry, weight, k);
            close(endpoint_score_difference(flipped, geometry, weight, k), -change, 1e-12,
                  "endpoint reverse difference failed");
            close(flipped.score - state.score, change, 1e-10, "endpoint score difference failed");
            for (double beta : {0.0, 0.5, 1.0})
                close(std::min(0.0, beta * change) - std::min(0.0, -beta * change), beta * change,
                      1e-13, "endpoint Metropolis balance failed");
            const double lr = swap_log_ratio(0.25, 0.75, state, flipped);
            const double reverse = swap_log_ratio(0.25, 0.75, flipped, state);
            close(lr, -reverse, 1e-13, "swap reverse ratio failed");
            close(lr, (0.25 * flipped.score + 0.75 * state.score)
                      - (0.25 * state.score + 0.75 * flipped.score), 1e-10, "swap target ratio failed");
            // Frozen corruptions must be rejected by full-state validation.
            State broken = state;
            broken.flux[0] = static_cast<unsigned char>((broken.flux[0] + 1) % 5);
            bool caught = false;
            try { validate(broken, geometry, weight, k); } catch (const std::runtime_error&) { caught = true; }
            require(caught, "flux corruption escaped validation");
            ++mutations_caught;
            broken = state;
            broken.score += geometry.plaquettes;
            caught = false;
            try { validate(broken, geometry, weight, k); } catch (const std::runtime_error&) { caught = true; }
            require(caught, "score corruption escaped validation");
            ++mutations_caught;
        }
    }
    std::cout << "NON-CANONICAL floating-point engineering audit\n"
              << "geometries\t" << geometries << "\nfixture_states\t" << states_checked
              << "\nmutations_caught\t" << mutations_caught << "\nresult\tPASS\n";
}
} // namespace

int main(int argc, char** argv) {
    try {
        if (argc == 2 && std::string(argv[1]) == "--audit") {
            audit();
        } else {
            require(argc == 4, "usage: sample L k chain | sample --audit");
            std::array<int, 3> argument{};
            for (int j = 0; j < 3; ++j) {
                std::size_t consumed = 0;
                argument[j] = std::stoi(argv[j + 1], &consumed);
                require(consumed == std::string(argv[j + 1]).size(), "noninteger argument");
            }
            run(argument[0], argument[1], argument[2]);
        }
        require(static_cast<bool>(std::cout), "stdout write failed");
        return 0;
    } catch (const std::exception& error) {
        std::cerr << "ERROR: " << error.what() << '\n';
        return 1;
    }
}
