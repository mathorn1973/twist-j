// SPDX-License-Identifier: Apache-2.0
#define main predecessor_main
#include "audit.cpp"
#undef main

namespace cascade {
constexpr unsigned worker = 28, memory = 31, fork_tick = 181;
constexpr Ring output{0, 1, 0, 1};
constexpr Ring phase{0, 0, 0, -1}, inverse_phase{0, 0, -1};
constexpr unsigned local_limit = 4096, principal_limit = 65536;

class Ledger {
    std::vector<Ring> norms;
public:
    void check(const Kernel &kernel, const Field &field) {
        std::array<Ring, 3> sum{};
        for (const Cell &cell : field) {
            for (unsigned lane = 0; lane < cell.size(); ++lane) {
                const Id id = cell[lane];
                while (norms.size() <= id)
                    norms.push_back(norm(kernel.value(static_cast<Id>(norms.size()))));
                const Ring &word = kernel.value(id);
                for (unsigned i = 0; i < word.size(); ++i) {
                    sum[lane / 2][i] += word[i];
                    sum[2][i] += norms[id][i];
                }
            }
        }
        if (sum != published_ledger)
            throw std::logic_error("stage ledger mismatch");
    }
};

struct Step {
    Field c, b;
    std::array<unsigned, 32> tag{};
};

Step advance(Kernel &kernel, Ledger &ledger, const Field &pre, unsigned bit) {
    Step next{pre, {}, {}};
    kernel.transport(next.c, bit);
    ledger.check(kernel, next.c);
    next.b = next.c;
    for (unsigned site = 0; site < next.b.size(); ++site)
        next.tag[site] = kernel.collide(next.b[site]);
    ledger.check(kernel, next.b);
    Field inverse = next.b;
    kernel.scatter(inverse);
    if (inverse != next.c)
        throw std::logic_error("inverse B mismatch");
    kernel.transport(inverse, bit, true);
    if (inverse != pre)
        throw std::logic_error("inverse C mismatch");
    return next;
}

struct State {
    Field field;
    unsigned bit;
};

void rewind(Kernel &kernel, Ledger &ledger, State &state, unsigned steps) {
    while (steps--) {
        state.bit ^= 1;
        kernel.scatter(state.field);
        ledger.check(kernel, state.field);
        kernel.transport(state.field, state.bit, true);
        ledger.check(kernel, state.field);
    }
}

bool radiation_equal(const Cell &a, const Cell &b) {
    return a[2] == b[2] && a[3] == b[3];
}

bool functional(Kernel &kernel, unsigned bit, const Field &pre, const Step &next,
                const Pair &t, const Pair &w) {
    if (bit != 1 || matter(pre[memory]) != w ||
        matter(next.c[memory]) == w || matter(next.b[memory]) == w ||
        next.tag[worker] != 2 || matter(next.c[worker]) == matter(pre[worker]) ||
        matter(next.b[worker]) == matter(next.c[worker]))
        return false;
    const Cell hybrid_c = hybrid_transport(kernel, pre, next.c[worker], worker, bit, t);
    if (matter(hybrid_c) != matter(pre[worker]) ||
        matter(next.b[worker]) == matter(hybrid_c))
        return false;
    Cell hybrid_b = hybrid_c;
    if (kernel.collide(hybrid_b) || hybrid_b != hybrid_c)
        return false;
    return check_escrow(kernel, pre, worker, bit, t, hybrid_c, hybrid_b);
}

constexpr std::array<const char *, 3> controls{"phase", "sign", "omit"};
constexpr std::array<const char *, 4> regions{"all", "site29", "site30", "outside"};
constexpr std::array<const char *, 6> events{
    "C_matter", "C_radiation", "B_branch", "B_live_vs_idle",
    "B_matched_matter", "B_matched_radiation"
};

struct Endpoint {
    unsigned tick{}, site{}, live_tag{}, alt_tag{}, count{};
    std::array<Cell, 10> cells{};
};
using Report = std::array<std::array<Endpoint, events.size()>, regions.size()>;

unsigned partner(unsigned coordinate, unsigned length, unsigned bit) {
    return (coordinate + (coordinate % 2 == bit ? 1 : length - 1)) % length;
}

void record(Endpoint &entry, unsigned tick, unsigned site, const Field &live,
            const Step &after, const Field &alt, const Step &other) {
    if (entry.count++ != 0) return;
    entry.tick = tick;
    entry.site = site;
    entry.live_tag = after.tag[site];
    entry.alt_tag = other.tag[site];
    const unsigned bit = tick % 2;
    const unsigned vertical = 4 * (site / 4) + partner(site % 4, 4, bit);
    const unsigned horizontal = 4 * partner(site / 4, 8, bit) + site % 4;
    entry.cells = {
        live[site], after.c[site], after.b[site], live[vertical], live[horizontal],
        alt[site], other.c[site], other.b[site], alt[vertical], alt[horizontal]
    };
}

void compare(Report &report, unsigned tick, const Field &live, const Step &after,
             const Field &alt, const Step &other) {
    for (unsigned site = 0; site < live.size(); ++site) {
        if (site == worker || site == memory) continue;
        const unsigned region = site == 29 ? 1 : site == 30 ? 2 : 3;
        const bool same_pre = live[site] == alt[site];
        const bool diff_matter = matter(after.c[site]) != matter(other.c[site]);
        const bool diff_radiation = !radiation_equal(after.c[site], other.c[site]);
        const bool worked = after.tag[site] && matter(after.c[site]) != matter(after.b[site]);
        const bool branches = worked && after.tag[site] != other.tag[site];
        const bool live_vs_idle = worked && other.tag[site] == 0;
        const std::array<bool, events.size()> hit{
            diff_matter, diff_radiation, branches, live_vs_idle,
            live_vs_idle && same_pre && diff_matter && !diff_radiation,
            live_vs_idle && same_pre && !diff_matter && diff_radiation
        };
        for (unsigned e = 0; e < events.size(); ++e) {
            if (!hit[e]) continue;
            record(report[0][e], tick, site, live, after, alt, other);
            record(report[region][e], tick, site, live, after, alt, other);
        }
    }
}

void emit_cell(const Kernel &kernel, const Cell &cell) {
    for (Id id : cell)
        for (I coefficient : kernel.value(id))
            std::cout << '\t' << coefficient;
}

void emit(const Kernel &kernel, unsigned rank, const std::array<Report, controls.size()> &reports) {
    for (unsigned a = 0; a < controls.size(); ++a) {
        for (unsigned r = 0; r < regions.size(); ++r) {
            for (unsigned e = 0; e < events.size(); ++e) {
                const Endpoint &v = reports[a][r][e];
                std::cout << "ROW\t" << rank << '\t' << controls[a] << '\t' << regions[r]
                          << '\t' << events[e] << '\t' << v.tick << '\t' << v.site
                          << '\t' << v.live_tag << '\t' << v.alt_tag << '\t' << v.count << '\n';
                if (!v.count) continue;
                std::cout << "LOCAL\t" << rank << '\t' << controls[a] << '\t' << regions[r]
                          << '\t' << events[e] << '\t' << v.tick << '\t' << v.site;
                for (const Cell &cell : v.cells)
                    emit_cell(kernel, cell);
                std::cout << '\n';
            }
        }
    }
}

void emit_direct(const Kernel &kernel, unsigned rank, unsigned arm, const Field &live,
                 const Step &after, const Field &alt, const Step &other) {
    constexpr unsigned receiver = 29;
    Endpoint local;
    record(local, fork_tick + 1, receiver, live, after, alt, other);
    std::cout << "DIRECT\t" << rank << '\t' << controls[arm]
              << '\t' << (matter(live[receiver]) != matter(after.c[receiver]))
              << '\t' << (matter(alt[receiver]) != matter(other.c[receiver]))
              << '\t' << !radiation_equal(live[receiver], after.c[receiver])
              << '\t' << !radiation_equal(alt[receiver], other.c[receiver])
              << '\t' << local.live_tag << '\t' << local.alt_tag;
    for (const Cell &cell : local.cells)
        emit_cell(kernel, cell);
    std::cout << '\n';
}

void phase_word(Kernel &kernel, Field &field, const Ring &factor) {
    for (unsigned lane = 0; lane < 2; ++lane)
        field[worker][lane] = kernel.intern(mul(kernel.value(field[worker][lane]), factor));
}

std::array<State, controls.size()> fork(Kernel &kernel, Ledger &ledger, State live,
                                       const Cell &worker_c, const Pair &w) {
    if (kernel.value(live.field[worker][0]) != output ||
        kernel.value(live.field[worker][1]) != scale(output, -1))
        throw std::logic_error("unexpected 181 B material word");
    std::array<State, controls.size()> alternatives{live, live, live};
    phase_word(kernel, alternatives[0].field, phase);
    if (matter(alternatives[0].field[worker]) != w)
        throw std::logic_error("phase arm does not install W");
    std::swap(alternatives[1].field[worker][0], alternatives[1].field[worker][1]);
    if (kernel.collide(alternatives[2].field[worker]) != 1 ||
        alternatives[2].field[worker] != worker_c)
        throw std::logic_error("omitted B2 does not restore 181 C");
    for (const State &arm : alternatives) {
        ledger.check(kernel, arm.field);
        for (unsigned site = 0; site < live.field.size(); ++site)
            if (site != worker && arm.field[site] != live.field[site])
                throw std::logic_error("intervention modifies a nonworker site");
    }
    for (unsigned a = 0; a < 2; ++a) {
        const Cell &changed = alternatives[a].field[worker];
        if (!radiation_equal(changed, live.field[worker]) ||
            changed[0] == live.field[worker][0] ||
            changed[1] == live.field[worker][1])
            throw std::logic_error("matter-only arm does not change exactly two rails");
    }
    return alternatives;
}

void invert_fork(Kernel &kernel, State &arm, unsigned a) {
    switch (a) {
    case 0:
        phase_word(kernel, arm.field, inverse_phase);
        break;
    case 1:
        std::swap(arm.field[worker][0], arm.field[worker][1]);
        break;
    case 2:
        if (kernel.collide(arm.field[worker]) != 2)
            throw std::logic_error("restore omitted B2 mismatch");
        break;
    default:
        throw std::logic_error("unknown intervention");
    }
}

void scan(Kernel &kernel, Ledger &ledger, const Key &key, const Query &query,
          const Pair &t, const Pair &w) {
    const auto [mode, rank] = key;
    if (mode != 2 || query.depth != 0)
        throw std::runtime_error("expected mode 2, depth 0 query");
    const unsigned limit = rank == 43 ? principal_limit : local_limit;
    const Relay predecessor = score_relay(kernel, query.cut, t, w);
    const bool eligible = predecessor.source125 && predecessor.restore157 &&
        predecessor.work_tick == 159 && predecessor.work_site == worker &&
        predecessor.work_tag == 2 && predecessor.work_offtag == 0 &&
        predecessor.paid_work_tick == 159;
    if (eligible != (rank == 0 || rank == 22 || rank == 43))
        throw std::logic_error("predecessor qualifying ranks changed");
    State live{query.cut, 1}, fork_state{};
    std::array<State, controls.size()> arms{}, starts{};
    std::array<Report, controls.size()> reports{};
    bool first_write = false;
    unsigned second_write = 0;
    for (unsigned tick = 1; tick <= limit; ++tick) {
        const Step next = advance(kernel, ledger, live.field, live.bit);
        if (tick == 159) {
            first_write = eligible && functional(kernel, live.bit, live.field, next, t, w);
            if (first_write != eligible)
                throw std::logic_error("first writer census no longer matches");
        }
        if (first_write && tick > 159 && !second_write &&
            functional(kernel, live.bit, live.field, next, t, w))
            second_write = tick;
        if (eligible && tick > fork_tick) {
            for (unsigned a = 0; a < controls.size(); ++a) {
                const Step other = advance(kernel, ledger, arms[a].field, arms[a].bit);
                compare(reports[a], tick, live.field, next, arms[a].field, other);
                if (tick == fork_tick + 1)
                    emit_direct(kernel, rank, a, live.field, next, arms[a].field, other);
                arms[a] = {other.b, arms[a].bit ^ 1};
            }
        }
        live = {next.b, live.bit ^ 1};
        if (eligible && tick == fork_tick) {
            if (second_write != fork_tick)
                throw std::logic_error("second qualifying write is not at 181 B");
            fork_state = live;
            arms = starts = fork(kernel, ledger, live, next.c[worker], w);
        }
    }
    rewind(kernel, ledger, live, limit);
    if (live.field != query.cut || live.bit != 1)
        throw std::logic_error("forward terminal inversion did not recover launch");
    if (eligible) {
        for (unsigned a = 0; a < controls.size(); ++a) {
            rewind(kernel, ledger, arms[a], limit - fork_tick);
            if (arms[a].field != starts[a].field || arms[a].bit != starts[a].bit)
                throw std::logic_error("counterfactual terminal inversion did not recover fork");
            invert_fork(kernel, arms[a], a);
            ledger.check(kernel, arms[a].field);
            if (arms[a].field != fork_state.field || arms[a].bit != fork_state.bit)
                throw std::logic_error("intervention inverse did not recover actual cut");
            rewind(kernel, ledger, arms[a], fork_tick);
            if (arms[a].field != query.cut || arms[a].bit != 1)
                throw std::logic_error("counterfactual terminal inversion did not recover launch");
        }
    }
    std::cout << "BASE\t" << rank << '\t' << limit << '\t' << first_write << '\t'
              << second_write << '\n';
    if (eligible) emit(kernel, rank, reports);
}
}

#ifndef CASCADE_LIBRARY
int main(int argc, char **argv) try {
    if (argc > 2) throw std::runtime_error("usage: cascade [query-file]");
    std::ifstream file;
    if (argc == 2) {
        file.open(argv[1]);
        if (!file) throw std::runtime_error("cannot open query file");
    }
    Kernel kernel;
    cascade::Ledger ledger;
    const Queries queries = read_queries(kernel, argc == 2 ? file : std::cin);
    if (queries.size() != rank_count)
        throw std::runtime_error("expected all 85 launches");
    const Pair t{kernel.intern(t_word), kernel.intern(scale(t_word, -1))};
    const Pair w{kernel.intern(w_word), kernel.intern(scale(w_word, -1))};
    for (const auto &[key, query] : queries)
        cascade::scan(kernel, ledger, key, query, t, w);
    if (!std::cout) throw std::runtime_error("failed writing cascade records");
    return 0;
} catch (const std::exception &error) {
    std::cerr << error.what() << '\n';
    return 2;
}

#endif
