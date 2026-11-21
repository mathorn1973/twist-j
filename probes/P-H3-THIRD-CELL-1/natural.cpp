// SPDX-License-Identifier: Apache-2.0
// Native, held-writer word encounters on the original four-wire launches.
#define main second_write_main
#include "audit.cpp"
#undef main

namespace natural {

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
            throw std::logic_error("cut ledger mismatch");
    }
};

struct Steps {
    Field c, b;
    std::array<unsigned, 32> tags{};
};

Steps advance(Kernel &kernel, Ledger &ledger, const Field &pre, unsigned bit) {
    Steps next{pre, {}};
    kernel.transport(next.c, bit);
    ledger.check(kernel, next.c);
    next.b = next.c;
    for (unsigned site = 0; site < next.b.size(); ++site)
        next.tags[site] = kernel.collide(next.b[site]);
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


struct Edge {
    unsigned writer, reader, bit;
};
constexpr std::array<Edge, 3> edges{
    Edge{28, 29, 0}, Edge{28, 31, 1}, Edge{29, 30, 1}
};
constexpr std::array<unsigned, 3> writer_sites{28, 29, 30};
constexpr unsigned base_limit = 8192;
constexpr unsigned rank43_limit = 65536;

Pair matter(const Cell &cell) {
    return {cell[0], cell[1]};
}

Pair radiation(const Cell &cell) {
    return {cell[2], cell[3]};
}

enum class Carrier : unsigned { Matter, Clock };

Pair word(const Cell &cell, Carrier carrier) {
    return carrier == Carrier::Matter ? matter(cell) : Pair{cell[2], 0};
}

struct Write {
    unsigned tick{}, tag{};
    Cell incoming{}, outgoing{};
};

struct Encounter {
    unsigned rank{}, tick{}, bit{}, writer{}, reader{}, tag{};
    Carrier carrier{};
    Write write;
    Cell donor_pre{}, donor_c{}, donor_b{};
    Cell pre{}, c{}, b{};
};

struct Representative {
    std::uint64_t count{}, rank43_count{};
    Encounter sample, rank43_sample;

    void add(const Encounter &event) {
        if (count++ == 0) sample = event;
        if (event.rank == 43 && rank43_count++ == 0) rank43_sample = event;
    }

    const Encounter &preferred() const {
        return rank43_count > 0 ? rank43_sample : sample;
    }
};

using Readiness = std::array<Id, 7>;
using Output = std::array<Id, 7>;
using Groups = std::map<Readiness, std::map<Output, Representative>>;

Readiness readiness(const Encounter &event) {
    const auto &pre = event.pre;
    const auto &c = event.c;
    if (event.carrier == Carrier::Matter)
        return {pre[0], pre[1], pre[2], pre[3], c[2], c[3], 0};
    return {pre[0], pre[1], pre[2], pre[3], c[0], c[1], c[3]};
}

Output output(const Encounter &event) {
    const Pair input = word(event.donor_pre, event.carrier);
    const Pair arrival = word(event.c, event.carrier);
    return {input[0], input[1], arrival[0], arrival[1], event.tag, event.b[0], event.b[1]};
}

bool moved(const Encounter &event) {
    return word(event.pre, event.carrier) != word(event.c, event.carrier);
}

bool material_work(const Encounter &event) {
    return matter(event.c) != matter(event.b);
}

struct Counts {
    unsigned held{}, moved{}, active{};
};

struct Matched {
    std::uint64_t pairs{}, rank43_pairs{}, both_moved_pairs{};
    unsigned preference{};
    Encounter first, second;

    void add(const Representative &a, const Representative &b) {
        const auto &x = a.preferred();
        const auto &y = b.preferred();
        const bool both = moved(x) && moved(y);
        const unsigned priority = 2U * static_cast<unsigned>(both) +
            static_cast<unsigned>(x.rank == 43) + static_cast<unsigned>(y.rank == 43);
        if (pairs == 0 || priority > preference) {
            preference = priority;
            first = x;
            second = y;
        }
        pairs += a.count * b.count;
        rank43_pairs += a.rank43_count * b.rank43_count;
        if (both) both_moved_pairs += a.count * b.count;
    }
};

constexpr std::array<const char *, 5> contrasts{
    "distinct_input", "distinct_C", "active_idle", "same_tag_distinct_material",
    "two_active_tags"
};

const char *name(Carrier carrier) {
    return carrier == Carrier::Matter ? "matter" : "clk";
}

void print_cell(const Kernel &kernel, const Cell &cell) {
    for (Id id : cell)
        for (I value : kernel.value(id))
            std::cout << '\t' << value;
}

void print_encounter(const Kernel &kernel, const char *contrast,
                     unsigned arm, const Encounter &event) {
    std::cout << "ARM\t" << contrast << '\t' << arm << '\t' << name(event.carrier)
              << '\t' << event.writer << '\t' << event.reader << '\t' << event.rank
              << '\t' << event.write.tick << '\t' << event.write.tag
              << '\t' << event.tick << '\t' << event.bit << '\t' << moved(event)
              << '\t' << event.tag;
    for (const auto &cell : {event.write.incoming, event.write.outgoing,
                            event.donor_pre, event.donor_c, event.donor_b,
                            event.pre, event.c, event.b})
        print_cell(kernel, cell);
    std::cout << '\n';
}

void matched(const Kernel &kernel, const Edge &edge, Carrier carrier, const Groups &groups) {
    std::array<Matched, contrasts.size()> totals{};
    std::size_t outcomes = 0;
    for (const auto &[input, observations] : groups) {
        outcomes += observations.size();
        for (auto a = observations.begin(); a != observations.end(); ++a) {
            for (auto b = std::next(a); b != observations.end(); ++b) {
                const Encounter &x = a->second.sample;
                const Encounter &y = b->second.sample;
                if (word(x.donor_pre, carrier) == word(y.donor_pre, carrier)) continue;
                const std::array<bool, contrasts.size()> score{
                    true,
                    word(x.c, carrier) != word(y.c, carrier),
                    material_work(x) != material_work(y),
                    material_work(x) && material_work(y) && x.tag == y.tag &&
                        matter(x.b) != matter(y.b),
                    material_work(x) && material_work(y) && x.tag != y.tag
                };
                for (unsigned k = 0; k < score.size(); ++k)
                    if (score[k]) totals[k].add(a->second, b->second);
            }
        }
    }
    std::cout << "GROUPS\t" << edge.writer << '\t' << edge.reader << '\t' << name(carrier)
              << '\t' << groups.size() << '\t' << outcomes << '\n';
    for (unsigned k = 0; k < contrasts.size(); ++k) {
        const auto &total = totals[k];
        std::cout << "MATCH\t" << edge.writer << '\t' << edge.reader << '\t' << name(carrier)
                  << '\t' << contrasts[k] << '\t' << total.pairs << '\t'
                  << total.rank43_pairs << '\t' << total.both_moved_pairs << '\n';
        if (total.pairs) {
            print_encounter(kernel, contrasts[k], 1, total.first);
            print_encounter(kernel, contrasts[k], 2, total.second);
        }
    }
}

struct WriteCounts {
    Write first;
    std::array<unsigned, 3> tags{};
};

using EdgeGroups = std::array<std::array<Groups, 2>, edges.size()>;

void scan(Kernel &kernel, Ledger &ledger, const Key &key, const Query &query,
          EdgeGroups &groups) {
    if (key.first != 2 || query.depth != 0)
        throw std::runtime_error("expected mode 2, depth 0 four-wire launch");
    const unsigned rank = key.second;
    const unsigned limit = rank == 43 ? rank43_limit : base_limit;
    Field field = query.cut;
    std::array<std::array<Write, 2>, 32> held{};
    std::array<std::array<Counts, 2>, edges.size()> counts{};
    std::array<WriteCounts, 32> writes{};

    for (unsigned tick = 1; tick <= limit; ++tick) {
        const unsigned bit = tick % 2;
        const auto next = advance(kernel, ledger, field, bit);
        for (unsigned index = 0; index < edges.size(); ++index) {
            const auto [writer, reader, matching] = edges[index];
            if (matching != bit) continue;

            for (unsigned lane = 0; lane < held[writer].size(); ++lane) {
                const auto carrier = static_cast<Carrier>(lane);
                const Write &last = held[writer][lane];
                if (!last.tick) continue;
                if (word(last.outgoing, carrier) != word(field[writer], carrier))
                    throw std::logic_error("provenance does not match native pre-C carrier");
                const Encounter encounter{
                    rank, tick, bit, writer, reader, next.tags[reader], carrier, last,
                    field[writer], next.c[writer], next.b[writer],
                    field[reader], next.c[reader], next.b[reader]
                };
                auto &tally = counts[index][lane];
                ++tally.held;
                tally.moved += moved(encounter);
                tally.active += material_work(encounter);
                groups[index][lane][readiness(encounter)][output(encounter)].add(encounter);
            }
        }

        for (unsigned writer : writer_sites) {
            const bool material = matter(next.c[writer]) != matter(next.b[writer]);
            const unsigned tag = next.tags[writer];
            if (material) {
                if (!tag) throw std::logic_error("native material write without a tag");
                ++writes[writer].tags[tag];
                if (!writes[writer].first.tick)
                    writes[writer].first = {tick, tag, next.c[writer], next.b[writer]};
            }
            for (unsigned lane = 0; lane < held[writer].size(); ++lane) {
                const auto carrier = static_cast<Carrier>(lane);
                Write &last = held[writer][lane];
                const bool changed_c = word(next.c[writer], carrier) != word(field[writer], carrier);
                const bool changed_b = word(next.b[writer], carrier) != word(next.c[writer], carrier);
                if (changed_c || changed_b) last = {};
                if (material && changed_b)
                    last = {tick, tag, next.c[writer], next.b[writer]};
            }
        }
        field = next.b;
    }

    unsigned bit = (limit + 1) % 2;
    Field inverse = field;
    for (unsigned tick = limit; tick > 0; --tick) {
        bit ^= 1;
        kernel.scatter(inverse);
        kernel.transport(inverse, bit, true);
    }
    if (bit != 1 || inverse != query.cut)
        throw std::logic_error("final launch inverse mismatch");

    const auto &primary = writes[28].tags;
    std::cout << "RANK\t" << rank << '\t' << limit << '\t' << primary[1] + primary[2] << "\t1\n";
    for (unsigned writer : writer_sites) {
        const auto &writer_stats = writes[writer];
        std::cout << "WRITES\t" << rank << '\t' << writer
                  << '\t' << writer_stats.tags[1] << '\t' << writer_stats.tags[2]
                  << '\t' << writer_stats.first.tick << '\t' << writer_stats.first.tag;
        if (writer_stats.first.tick) {
            print_cell(kernel, writer_stats.first.incoming);
            print_cell(kernel, writer_stats.first.outgoing);
        }
        std::cout << '\n';
    }
    for (unsigned index = 0; index < edges.size(); ++index) {
        const auto &edge = edges[index];
        for (unsigned lane = 0; lane < counts[index].size(); ++lane) {
            const auto &tally = counts[index][lane];
            std::cout << "CONTACTS\t" << rank << '\t' << edge.writer << '\t' << edge.reader
                      << '\t' << name(static_cast<Carrier>(lane)) << '\t' << tally.held
                      << '\t' << tally.moved << '\t' << tally.active << '\n';
        }
    }
}

} // namespace natural

int main(int argc, char **argv) try {
    if (argc > 2) throw std::runtime_error("usage: natural [query-text-file]");
    std::ifstream file;
    if (argc == 2) {
        file.open(argv[1]);
        if (!file) throw std::runtime_error("cannot open query file");
    }
    Kernel kernel;
    natural::Ledger ledger;
    const Queries queries = read_queries(kernel, argc == 2 ? file : std::cin);
    if (queries.size() != rank_count)
        throw std::runtime_error("expected all 85 four-wire launches");
    natural::EdgeGroups groups{};
    std::cout << "# RANK rank horizon writer_writes full_inverse\n"
                 "# WRITES rank site count_B1 count_B2 first_tick first_tag [first_C first_B]\n"
                 "# CONTACTS rank writer reader carrier held moved material_work\n"
                 "# GROUPS writer reader carrier readiness_keys distinct_outcomes\n"
                 "# MATCH writer reader carrier contrast encounter_pairs both_rank43 both_moved\n"
                 "# ARM contrast arm carrier writer reader rank write_tick write_tag read_tick"
                 " bit moved reader_tag writer_C writer_B donor_pre donor_C donor_B"
                 " receiver_pre receiver_C receiver_B (cells each 16 j-basis coefficients)\n";
    for (const auto &[key, query] : queries)
        natural::scan(kernel, ledger, key, query, groups);
    for (unsigned side = 0; side < natural::edges.size(); ++side)
        for (unsigned lane = 0; lane < groups[side].size(); ++lane)
            natural::matched(kernel, natural::edges[side],
                             static_cast<natural::Carrier>(lane), groups[side][lane]);
    if (!std::cout) throw std::runtime_error("failed to write natural records");
    return 0;
} catch (const std::exception &error) {
    std::cerr << error.what() << '\n';
    return 2;
}
