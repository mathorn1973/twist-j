// SPDX-License-Identifier: Apache-2.0
#define CASCADE_LIBRARY
#include "cascade.cpp"

namespace dual {
using cascade::State;
using cascade::Step;
using cascade::Ledger;
constexpr unsigned writer = cascade::worker;
constexpr unsigned cut = cascade::fork_tick;
constexpr Ring minus_one{-1};
constexpr int no_site = -1;
constexpr std::array<unsigned, 6> original_clock{0, 1, 4, 5, 8, 9};

struct Observation {
    State state;
    Step last;
    Cell before;
    unsigned first_active{}, first_b2{}, earlier_active{}, earlier_b2{};
    unsigned first_tag{}, first_function{};
};

Observation replay(Kernel &k, Ledger &ledger, State start, unsigned first, unsigned last,
                   unsigned site, const Pair &t, const Pair &w) {
    Observation result{};
    result.state = start;
    for (unsigned tick = first; tick <= last; ++tick) {
        const unsigned bit = result.state.bit;
        const Step step = cascade::advance(k, ledger, result.state.field, bit);
        if (tick < cut && step.tag[writer]) {
            if (!result.first_active) result.first_active = tick;
            ++result.earlier_active;
            if (step.tag[writer] == 2) {
                if (!result.first_b2) result.first_b2 = tick;
                ++result.earlier_b2;
            }
        }
        if (tick == 159) {
            result.first_tag = step.tag[writer];
            result.first_function = cascade::functional(k, bit, result.state.field, step, t, w);
        }
        if (tick == last) {
            result.before = result.state.field[site];
            result.last = step;
        }
        result.state = {step.b, bit ^ 1};
    }
    State recovered = result.state;
    cascade::rewind(k, ledger, recovered, last - first + 1);
    if (recovered.field != start.field || recovered.bit != start.bit)
        throw std::logic_error("dual terminal inverse mismatch");
    return result;
}

bool antipodal(const Kernel &k, const Cell &cell) {
    return add(k.value(cell[0]), k.value(cell[1])) == zero;
}

void rotate(Kernel &k, Field &field, unsigned site, const Ring &factor) {
    if (!antipodal(k, field[site]))
        return;
    for (unsigned lane = 0; lane < 2; ++lane)
        field[site][lane] = k.intern(mul(k.value(field[site][lane]), factor));
}

bool emitted(const Observation &observation) {
    return observation.last.tag[writer] &&
           matter(observation.last.c[writer]) != matter(observation.last.b[writer]);
}

bool distinct_emissions(const Observation &a, const Observation &b) {
    return emitted(a) && emitted(b) &&
           matter(a.last.b[writer]) != matter(b.last.b[writer]);
}

struct Outcome {
    bool same_pre, same_radiation, distinct_matter_c, distinct_matter_b;
    unsigned live_tag, other_tag;
    bool decoding() const {
        return same_pre && same_radiation && distinct_matter_c && distinct_matter_b &&
               (live_tag || other_tag);
    }
};

Outcome outcome(const Observation &a, const Observation &b, unsigned site) {
    return {a.before == b.before,
            cascade::radiation_equal(a.last.c[site], b.last.c[site]),
            matter(a.last.c[site]) != matter(b.last.c[site]),
            matter(a.last.b[site]) != matter(b.last.b[site]),
            a.last.tag[site], b.last.tag[site]};
}

void emit_outcome(Kernel &kernel, const char *label, unsigned rank, unsigned tick, unsigned site,
                  const Observation &a, const Observation &b) {
    const Outcome info = outcome(a, b, site);
    std::cout << label << '\t' << rank << '\t' << tick << '\t' << site
              << '\t' << info.same_pre << '\t' << info.same_radiation
              << '\t' << info.distinct_matter_c << '\t' << info.distinct_matter_b
              << '\t' << info.live_tag << '\t' << info.other_tag;
    for (const Observation *arm : {&a, &b}) {
        cascade::emit_cell(kernel, arm->before);
        cascade::emit_cell(kernel, arm->last.c[site]);
        cascade::emit_cell(kernel, arm->last.b[site]);
    }
    std::cout << '\n';
}

struct Mode {
    int site = no_site;
    unsigned exponent{};
    unsigned negative{};
    Ring factor{};
    Ring inverse{};
};

Mode screen(Kernel &k, Ledger &ledger, const Field &launch, const Observation &actual,
            unsigned target, unsigned site, const Pair &t, const Pair &w) {
    unsigned tested = 0, distinct = 0, decoded = 0;
    Mode winner;
    Observation actual_at{};
    if (target)
        actual_at = replay(k, ledger, actual.state, cut + 1, target, site, t, w);
    for (unsigned start = 0; start < launch.size(); ++start) {
        if (!antipodal(k, launch[start]) || k.value(launch[start][0]) == zero)
            continue;
        Ring unit = one;
        const Ring j{0, 1};
        const Ring inv_j{-1, -1, -1, -1};
        Ring inverse = one;
        for (unsigned exponent = 0; exponent < 5; ++exponent) {
            for (unsigned negative = 0; negative < 2; ++negative) {
                if (!exponent && !negative) continue;
                const Ring factor = negative ? mul(unit, minus_one) : unit;
                const Ring undo = negative ? mul(inverse, minus_one) : inverse;
                Field alternate = launch;
                rotate(k, alternate, start, factor);
                if (alternate == launch)
                    throw std::logic_error("nonidentity launch phase changed nothing");
                ledger.check(k, alternate);
                ++tested;
                const Observation other = replay(k, ledger, {alternate, 1}, 1, cut, writer, t, w);
                if (!distinct_emissions(actual, other)) continue;
                ++distinct;
                if (!target) continue;
                const Observation on_target = replay(k, ledger, other.state, cut + 1, target, site, t, w);
                if (!outcome(actual_at, on_target, site).decoding()) continue;
                ++decoded;
                if (winner.site == no_site)
                    winner = {static_cast<int>(start), exponent, negative, factor, undo};
            }
            unit = mul(unit, j);
            inverse = mul(inverse, inv_j);
        }
    }
    std::cout << "SCREEN\t" << 43 << '\t' << tested << '\t' << distinct << '\t' << decoded
              << '\t' << winner.site << '\t' << winner.exponent << '\t' << winner.negative << '\n';
    return winner;
}

void emit_worker(Kernel &k, const Observation &observation) {
    std::cout << '\t' << observation.last.tag[writer] << '\t' << observation.first_active
              << '\t' << observation.first_b2 << '\t' << observation.earlier_active
              << '\t' << observation.earlier_b2 << '\t' << observation.first_tag
              << '\t' << observation.first_function;
    cascade::emit_cell(k, observation.before);
    cascade::emit_cell(k, observation.last.c[writer]);
    cascade::emit_cell(k, observation.last.b[writer]);
}

void family(Kernel &k, Ledger &ledger, const Query &query, unsigned rank,
            const Observation &actual, unsigned target, unsigned site, const Pair &t, const Pair &w) {
    const Field &launch = query.cut;
    State programmed = actual.state;
    rotate(k, programmed.field, writer, cascade::phase);
    ledger.check(k, programmed.field);
    State alternate = programmed;
    cascade::rewind(k, ledger, alternate, cut);
    const Observation other = replay(k, ledger, alternate, 1, cut, writer, t, w);
    if (other.state.field != programmed.field || other.state.bit != programmed.bit ||
        alternate.bit != 1)
        throw std::logic_error("coded launch does not reach prescribed complete state");
    State original = other.state;
    rotate(k, original.field, writer, cascade::inverse_phase);
    if (original.field != actual.state.field || original.bit != actual.state.bit)
        throw std::logic_error("coded launch cut map failed inversion");
    cascade::rewind(k, ledger, original, cut);
    if (original.field != launch || original.bit != 1)
        throw std::logic_error("coded launch did not recover original launch");
    unsigned matter_diff = 0, clk_diff = 0, corr_diff = 0, corr_stock_diff = 0;
    for (unsigned s = 0; s < launch.size(); ++s) {
        matter_diff += matter(launch[s]) != matter(alternate.field[s]);
        clk_diff += launch[s][2] != alternate.field[s][2];
        corr_diff += launch[s][3] != alternate.field[s][3];
    }
    for (unsigned s : original_clock)
        corr_stock_diff += launch[s][3] != alternate.field[s][3];
    std::cout << "ENCODED\t" << rank << '\t' << matter_diff << '\t' << clk_diff
              << '\t' << corr_diff << '\t' << corr_stock_diff;
    emit_worker(k, actual);
    emit_worker(k, other);
    std::cout << '\n' << "LAUNCH\t" << rank;
    for (const Cell &cell : alternate.field)
        cascade::emit_cell(k, cell);
    std::cout << '\n';
    if (rank == 43 && (!distinct_emissions(actual, other) ||
                      actual.last.tag[writer] != 2 || other.last.tag[writer] != 2))
        throw std::logic_error("rank 43 did not emit two distinct B2 material words");
    if (target && (rank == 0 || rank == 22 || rank == 43)) {
        const Observation a = replay(k, ledger, actual.state, cut + 1, target, site, t, w);
        const Observation b = replay(k, ledger, other.state, cut + 1, target, site, t, w);
        emit_outcome(k, "ENCODED_GATE", rank, target, site, a, b);
    }
}

void test_mode(Kernel &k, Ledger &ledger, const Field &launch, unsigned rank, const Mode &mode,
               const Observation &actual, unsigned target, unsigned site,
               const Pair &t, const Pair &w) {
    if (mode.site == no_site) return;
    const unsigned source = static_cast<unsigned>(mode.site);
    Field changed = launch;
    rotate(k, changed, source, mode.factor);
    ledger.check(k, changed);
    Field recovered = changed;
    rotate(k, recovered, source, mode.inverse);
    if (recovered != launch)
        throw std::logic_error("simple launch phase failed inversion");
    const Observation other = replay(k, ledger, {changed, 1}, 1, cut, writer, t, w);
    const bool distinct = distinct_emissions(actual, other);
    std::cout << "SIMPLE\t" << rank << '\t' << (changed != launch) << '\t' << distinct;
    emit_worker(k, actual);
    emit_worker(k, other);
    std::cout << '\n';
    if (distinct) {
        const Observation a = replay(k, ledger, actual.state, cut + 1, target, site, t, w);
        const Observation b = replay(k, ledger, other.state, cut + 1, target, site, t, w);
        emit_outcome(k, "SIMPLE_GATE", rank, target, site, a, b);
    }
}
}

int main(int argc, char **argv) try {
    if (argc != 4) throw std::runtime_error("usage: dual query-file target-tick target-site");
    std::ifstream input(argv[1]);
    if (!input) throw std::runtime_error("cannot open query file");
    const unsigned target = std::stoul(argv[2]), site = std::stoul(argv[3]);
    if (target && (target <= dual::cut || target > cascade::principal_limit ||
                   site >= Field{}.size() || site == cascade::worker || site == cascade::memory))
        throw std::runtime_error("invalid target");
    Kernel k;
    dual::Ledger ledger;
    const Queries queries = read_queries(k, input);
    if (queries.size() != rank_count)
        throw std::runtime_error("expected all 85 launches");
    const Pair t{k.intern(t_word), k.intern(scale(t_word, -1))};
    const Pair w{k.intern(w_word), k.intern(scale(w_word, -1))};
    const Field &principal = queries.at({2, 43}).cut;
    const dual::Observation actual =
        dual::replay(k, ledger, {principal, 1}, 1, dual::cut, dual::writer, t, w);
    const dual::Mode mode = dual::screen(k, ledger, principal, actual, target, site, t, w);
    for (const auto &[key, query] : queries) {
        const auto [mode_number, rank] = key;
        if (mode_number != 2 || query.depth != 0)
            throw std::runtime_error("expected mode 2, depth 0 query");
        const dual::Observation first = rank == 43 ? actual :
            dual::replay(k, ledger, {query.cut, 1}, 1, dual::cut, dual::writer, t, w);
        dual::family(k, ledger, query, rank, first, target, site, t, w);
        dual::test_mode(k, ledger, query.cut, rank, mode, first, target, site, t, w);
    }
    if (!std::cout) throw std::runtime_error("failed writing dual records");
    return 0;
} catch (const std::exception &error) {
    std::cerr << error.what() << '\n';
    return 2;
}
