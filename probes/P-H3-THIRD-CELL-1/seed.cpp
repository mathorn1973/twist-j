// SPDX-License-Identifier: Apache-2.0
#define CASCADE_LIBRARY
#include "cascade.cpp"

namespace seed {
constexpr unsigned third = 29;
constexpr std::array<unsigned, 3> eligible{0, 22, 43};
constexpr Ring negate{-1};

bool antipodal(Kernel &k, const Cell &cell) {
    return add(k.value(cell[0]), k.value(cell[1])) == zero;
}

struct Recipe {
    unsigned site, power, negative;
    Ring factor, inverse;
};

bool seed_launch(Kernel &k, cascade::Ledger &ledger, const Field &launch,
                 Field &seeded, const Recipe &recipe) {
    if (matter(launch[third]) != Pair{0, 0})
        throw std::logic_error("site 29 is not empty at launch");
    const Cell &donor = launch[recipe.site];
    if (!antipodal(k, donor) || matter(donor) == Pair{0, 0})
        return false;
    seeded = launch;
    for (unsigned lane = 0; lane < 2; ++lane) {
        seeded[third][lane] = k.intern(mul(k.value(donor[lane]), recipe.factor));
        seeded[recipe.site][lane] = 0;
    }
    ledger.check(k, seeded);
    Field recovered = seeded;
    for (unsigned lane = 0; lane < 2; ++lane) {
        recovered[recipe.site][lane] = k.intern(mul(k.value(seeded[third][lane]), recipe.inverse));
        recovered[third][lane] = 0;
    }
    if (recovered != launch)
        throw std::logic_error("permuted and rotated launch matter failed its inverse");
    return true;
}

struct Outcome {
    unsigned source125{}, restore157{}, held158{}, first159{}, later{}, exact181{};
    unsigned live_c_moved{}, phase_c_moved{}, sign_c_moved{};
    unsigned live_tag{}, phase_tag{}, sign_tag{};
    unsigned phase_matched{}, sign_matched{};
    unsigned phase_c{}, phase_b{}, sign_c{}, sign_b{};
};

Outcome screen(Kernel &k, cascade::Ledger &ledger, const Field &launch,
               const Pair &t, const Pair &w, const Pair &o) {
    Outcome result;
    cascade::State state{launch, 1};
    Cell worker_c{};
    for (unsigned tick = 1; tick <= 181; ++tick) {
        const cascade::Step step = cascade::advance(k, ledger, state.field, state.bit);
        if (tick == 125) result.source125 = step.tag[source] == 2;
        if (tick == 157)
            result.restore157 = matter(step.c[cascade::memory]) == t &&
                                matter(step.b[cascade::memory]) == w &&
                                step.tag[cascade::memory] == 1;
        if (tick == 158)
            result.held158 = matter(state.field[cascade::memory]) == w &&
                             matter(step.c[cascade::memory]) == w &&
                             matter(step.b[cascade::memory]) == w;
        if (tick == 159)
            result.first159 = cascade::functional(k, state.bit, state.field, step, t, w);
        if (tick > 159 && !result.later &&
            cascade::functional(k, state.bit, state.field, step, t, w))
            result.later = tick;
        if (tick == 181) worker_c = step.c[cascade::worker];
        state = {step.b, state.bit ^ 1};
    }
    result.exact181 = matter(state.field[cascade::worker]) == o;
    if (result.source125 && result.restore157 && result.held158 && result.first159 &&
        result.later == 181 && result.exact181) {
        const auto alternatives = cascade::fork(k, ledger, state, worker_c, w);
        const auto live = cascade::advance(k, ledger, state.field, state.bit);
        const auto phase = cascade::advance(k, ledger, alternatives[0].field, state.bit);
        const auto sign = cascade::advance(k, ledger, alternatives[1].field, state.bit);
        result.live_c_moved = matter(state.field[third]) != matter(live.c[third]);
        result.phase_c_moved = matter(state.field[third]) != matter(phase.c[third]);
        result.sign_c_moved = matter(state.field[third]) != matter(sign.c[third]);
        result.live_tag = live.tag[third];
        result.phase_tag = phase.tag[third];
        result.sign_tag = sign.tag[third];
        result.phase_matched = state.field[third] == alternatives[0].field[third] &&
            cascade::radiation_equal(live.c[third], phase.c[third]);
        result.sign_matched = state.field[third] == alternatives[1].field[third] &&
            cascade::radiation_equal(live.c[third], sign.c[third]);
        result.phase_c = matter(live.c[third]) != matter(phase.c[third]);
        result.phase_b = matter(live.b[third]) != matter(phase.b[third]);
        result.sign_c = matter(live.c[third]) != matter(sign.c[third]);
        result.sign_b = matter(live.b[third]) != matter(sign.b[third]);
        if (!result.phase_matched || !result.sign_matched)
            throw std::logic_error("local material controls disturbed receiver readiness");
    }
    cascade::rewind(k, ledger, state, 181);
    if (state.field != launch || state.bit != 1)
        throw std::logic_error("seeded trajectory inverse mismatch");
    return result;
}

bool chain(const Outcome &result) {
    return result.source125 && result.restore157 && result.held158 && result.first159 &&
           result.later == 181 && result.exact181;
}

bool phase_gate(const Outcome &result) {
    return result.live_c_moved && result.phase_matched && result.phase_c && result.phase_b &&
           result.live_tag && !result.phase_tag;
}

bool sign_gate(const Outcome &result) {
    return result.live_c_moved && result.sign_matched && result.sign_c && result.sign_b &&
           result.live_tag && !result.sign_tag;
}

bool sign_active(const Outcome &result) {
    return result.live_c_moved && result.sign_c_moved && result.sign_matched && result.sign_c &&
           result.sign_b && result.live_tag && result.sign_tag;
}

void emit(unsigned rank, const Recipe &recipe, bool applicable, const Outcome &r) {
    const std::array<unsigned, 16> results{
        r.source125, r.restore157, r.held158, r.first159, r.later, r.exact181,
        r.live_c_moved, r.phase_c_moved, r.sign_c_moved, r.live_tag, r.phase_tag, r.sign_tag,
        r.phase_c, r.phase_b, r.sign_c, r.sign_b
    };
    std::cout << "SEED\t" << rank << '\t' << recipe.site << '\t' << recipe.power << '\t'
              << recipe.negative << '\t' << applicable;
    for (unsigned v : results) std::cout << '\t' << v;
    std::cout << '\n';
}

void sweep(Kernel &k, cascade::Ledger &ledger, const Queries &queries,
           const Pair &t, const Pair &w, const Pair &o) {
    unsigned recipes = 0, arms = 0, sources = 0, restores = 0, first = 0;
    unsigned later = 0, chains = 0, phase_gates = 0, sign_gates = 0, sign_writes = 0;
    unsigned recipes_phase = 0, recipes_sign = 0, recipes_sign_writes = 0;
    for (unsigned site = 0; site / height != third / height; ++site) {
        Ring unit = one, undo = one;
        for (unsigned power = 0; power < 5; ++power) {
            for (unsigned negative = 0; negative < 2; ++negative) {
                const Recipe recipe{site, power, negative,
                    negative ? mul(unit, negate) : unit, negative ? mul(undo, negate) : undo};
                bool available = false, some_phase = false, some_sign = false, some_write = false;
                for (unsigned rank : eligible) {
                    const Field &launch = queries.at({2, rank}).cut;
                    Field seeded;
                    if (!seed_launch(k, ledger, launch, seeded, recipe)) continue;
                    available = true;
                    ++arms;
                    const Outcome result = screen(k, ledger, seeded, t, w, o);
                    sources += result.source125;
                    restores += result.source125 && result.restore157 && result.held158;
                    first += result.source125 && result.restore157 && result.held158 && result.first159;
                    later += result.source125 && result.restore157 && result.held158 &&
                             result.first159 && result.later == 181;
                    chains += chain(result);
                    phase_gates += phase_gate(result);
                    sign_gates += sign_gate(result);
                    sign_writes += sign_active(result);
                    some_phase |= phase_gate(result);
                    some_sign |= sign_gate(result);
                    some_write |= sign_active(result);
                    emit(rank, recipe, true, result);
                }
                recipes += available;
                recipes_phase += some_phase;
                recipes_sign += some_sign;
                recipes_sign_writes += some_write;
            }
            unit = mul(unit, rho);
            undo = mul(undo, Ring{0, 0, 0, 1});
        }
    }
    const std::array<unsigned, 13> counts{
        recipes, arms, sources, restores, first, later, chains, phase_gates, sign_gates,
        sign_writes, recipes_phase, recipes_sign, recipes_sign_writes
    };
    std::cout << "SEED_SUMMARY";
    for (unsigned v : counts) std::cout << '\t' << v;
    std::cout << '\n';
}
}

int main(int argc, char **argv) try {
    if (argc != 2) throw std::runtime_error("usage: seed query-file");
    std::ifstream input(argv[1]);
    if (!input) throw std::runtime_error("cannot open query file");
    Kernel k;
    cascade::Ledger ledger;
    const Queries queries = read_queries(k, input);
    if (queries.size() != rank_count)
        throw std::runtime_error("expected all 85 launches");
    for (const auto &[key, query] : queries)
        if (key.first != 2 || query.depth != 0)
            throw std::runtime_error("expected mode 2, depth 0 query");
    const Pair t{k.intern(t_word), k.intern(scale(t_word, -1))};
    const Pair w{k.intern(w_word), k.intern(scale(w_word, -1))};
    const Pair o{k.intern(cascade::output), k.intern(scale(cascade::output, -1))};
    seed::sweep(k, ledger, queries, t, w, o);
    if (!std::cout) throw std::runtime_error("failed writing seed records");
    return 0;
} catch (const std::exception &error) {
    std::cerr << error.what() << '\n';
    return 2;
}
