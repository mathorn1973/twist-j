// SPDX-License-Identifier: Apache-2.0
// Search for two transported, recurrent native emissions on one original orbit.
#define main predecessor_main
#include "../P-H3-SECOND-WRITE-1/audit.cpp"
#undef main
#include "../P-H3-RENEWED-WORD-CHOICE-1/matches.hpp"

namespace double_renewal {

constexpr unsigned memory = receiver_site;
constexpr unsigned worker = 28;
constexpr unsigned first_tick = 159;

class Ledger {
    std::vector<Ring> norms;
public:
    void check(const Kernel &kernel, const Field &field) {
        std::array<Ring, 3> sum{};
        for (const Cell &cell : field) {
            for (unsigned rail = 0; rail < cell.size(); ++rail) {
                const Id id = cell[rail];
                while (norms.size() <= id)
                    norms.push_back(norm(kernel.value(static_cast<Id>(norms.size()))));
                const Ring &word = kernel.value(id);
                for (unsigned i = 0; i < word.size(); ++i) {
                    sum[rail / 2][i] += word[i];
                    sum[2][i] += norms[id][i];
                }
            }
        }
        if (sum != published_ledger)
            throw std::logic_error("stage ledger mismatch");
    }
};

struct Transition {
    Field c, b;
    std::array<unsigned, 32> tags{};
};

// The predecessor's exact compensated predicate, with no intervention in the live field.
bool functional_write(Kernel &kernel, unsigned bit, const Field &before,
                      const Transition &after, const Pair &t, const Pair &w) {
    if (bit != 1 || matter(before[memory]) != w ||
        matter(after.c[worker]) == matter(before[worker]) ||
        matter(after.b[worker]) == matter(after.c[worker]) ||
        project_collision(kernel, after.c[worker], after.b[worker]) != 2)
        return false;

    const Cell hybrid_c = hybrid_transport(kernel, before, after.c[worker], worker, bit, t);
    if (matter(hybrid_c) != matter(before[worker]) ||
        matter(after.b[worker]) == matter(hybrid_c))
        return false;

    Cell hybrid_b = hybrid_c;
    if (kernel.collide(hybrid_b) != 0 || hybrid_b != hybrid_c)
        return false;
    return check_escrow(kernel, before, worker, bit, t, hybrid_c, hybrid_b);
}

struct Held {
    unsigned tick{}, tag{}, prior{};
    bool anchor{};
    Cell c{}, b{};
};

// Site, bit, full pre-C writer, pre-C donor matter, incoming radiation, output matter.
using Episode = std::array<Id, 12>;

unsigned mate(unsigned site, unsigned bit) {
    const unsigned y = site % height;
    const unsigned dy = y % 2 == bit ? 1 : height - 1;
    return site - y + (y + dy) % height;
}

Episode episode(const Field &pre, const Transition &next, unsigned site, unsigned donor, unsigned bit) {
    const Cell &before = pre[site];
    const Cell &c = next.c[site];
    const Cell &b = next.b[site];
    return {site, bit, before[0], before[1], before[2], before[3],
            pre[donor][0], pre[donor][1], c[2], c[3], b[0], b[1]};
}

using Readiness = std::array<Id, 9>;

struct Outcome {
    Pair word, arrival, final;
    bool operator==(const Outcome &) const = default;
};

struct Representative {
    Outcome outcome;
    h3::Event event;
};

using Branches = std::array<std::vector<Representative>, 2>;
using Groups = std::unordered_map<Readiness, Branches, Hash>;
using Certificate = std::pair<h3::Event, h3::Event>;

std::optional<Certificate> observe(Groups &groups, const h3::Event &event, unsigned old_limit) {
    const Cell &pre = event.reader_pre;
    const Cell &c = event.reader_c;
    const Readiness key{event.writer, event.reader, event.bit,
                        pre[0], pre[1], pre[2], pre[3], c[2], c[3]};
    const Outcome outcome{matter(event.donor_pre), matter(c), matter(event.reader_b)};
    Branches &branches = groups[key];
    const unsigned tag = event.reader_tag;
    for (const Representative &other : branches[2 - tag]) {
        const Outcome &a = other.outcome;
        if (a.word == outcome.word || a.arrival == outcome.arrival || a.final == outcome.final)
            continue;
        if (event.read <= old_limit && other.event.read <= old_limit)
            throw std::logic_error("RR/BOTH_MOVED contradicts the frozen prefix zero");
        return Certificate{other.event, event};
    }
    auto &same = branches[tag - 1];
    if (std::none_of(same.begin(), same.end(),
                     [&](const Representative &other) { return other.outcome == outcome; }))
        same.push_back({outcome, event});
    return std::nullopt;
}

bool scan(Kernel &kernel, unsigned rank, const Field &launch, const Pair &t, const Pair &w) {
    const bool first_expected = rank == 43 || rank == 0 || rank == 22;
    const unsigned limit = rank == 43 ? 16'777'216 : first_expected ? 4'194'304 : 262'144;
    const unsigned old_limit = rank == 43 ? 1'048'576 : first_expected ? 65'536 : 8'192;
    Field field = launch;
    Ledger ledger;
    Groups groups;
    std::array<Held, 32> held{};
    std::unordered_map<Episode, unsigned, Hash> prior_writes;
    std::optional<Certificate> found;
    unsigned scanned = 0, recurrent_writes = 0, moved_active_reads = 0, bit = 1;
    bool source125 = false, restored157 = false, held158 = false, first_write = false;
    bool renewed_word = false;

    for (unsigned tick = 1; tick <= limit && !found; ++tick) {
        Transition next{field, {}};
        kernel.transport(next.c, bit);
        next.b = next.c;
        for (unsigned site = 0; site < next.b.size(); ++site)
            next.tags[site] = kernel.collide(next.b[site]);

        const Pair pre_word = matter(field[memory]);
        const Pair c_word = matter(next.c[memory]);
        const Pair b_word = matter(next.b[memory]);
        if (tick == 125) source125 = next.tags[source] == 2;
        if (tick == 157) restored157 = c_word == t && b_word == w && next.tags[memory] == 1;
        if (tick == 158) held158 = restored157 && pre_word == w && c_word == w && b_word == w;
        if (tick == first_tick) {
            first_write = source125 && held158 && c_word != w && b_word != w &&
                functional_write(kernel, bit, field, next, t, w);
            if (first_write != first_expected)
                throw std::logic_error("first writer census differs from the predecessor");
        }

        bool audited = false;
        const auto audit = [&] {
            if (audited) return;
            ledger.check(kernel, field);
            ledger.check(kernel, next.c);
            ledger.check(kernel, next.b);
            Field inverse = next.b;
            kernel.scatter(inverse);
            if (inverse != next.c) throw std::logic_error("selected inverse B mismatch");
            kernel.transport(inverse, bit, true);
            if (inverse != field) throw std::logic_error("selected inverse C mismatch");
            audited = true;
        };
        for (unsigned writer = 0; writer < held.size(); ++writer) {
            const Held &emission = held[writer];
            if (!emission.prior) continue;
            if (matter(field[writer]) != matter(emission.b))
                throw std::logic_error("held output differs from its pre-C carrier");
            const unsigned reader = mate(writer, bit);
            const unsigned tag = next.tags[reader];
            if (matter(field[reader]) == matter(next.c[reader]) ||
                matter(next.c[reader]) == matter(next.b[reader]))
                continue;
            if (tag != 1 && tag != 2)
                throw std::logic_error("material-changing reader has no active tag");
            audit();
            ++moved_active_reads;
            if (found) continue;
            const h3::Event event{
                rank, writer, reader, bit, emission.tick, tick, emission.tag, tag, emission.prior,
                emission.anchor, emission.c, emission.b, field[writer], field[reader],
                next.c[reader], next.b[reader]
            };
            found = observe(groups, event, old_limit);
        }

        for (unsigned writer = 0; writer < held.size(); ++writer) {
            const bool changed_c = matter(field[writer]) != matter(next.c[writer]);
            const bool changed_b = matter(next.c[writer]) != matter(next.b[writer]);
            if (changed_c || changed_b) held[writer] = {};
            const unsigned donor = mate(writer, bit);
            if (next.tags[writer] != 2 || !changed_b || !changed_c ||
                matter(field[donor]) == matter(next.c[donor]))
                continue;
            const auto [at, inserted] = prior_writes.try_emplace(
                episode(field, next, writer, donor, bit), tick);
            if (inserted) continue;
            audit();
            ++recurrent_writes;
            const bool anchor = writer == worker && tick > first_tick && first_write &&
                renewed_word && functional_write(kernel, bit, field, next, t, w);
            held[writer] = {tick, 2, at->second, anchor, next.c[writer], next.b[writer]};
        }
        if (tick > first_tick && first_write) {
            if (pre_word != w && c_word == w) renewed_word = true;
            if (c_word != w) renewed_word = false;
            if (c_word != w && b_word == w) renewed_word = true;
            if (b_word != w) renewed_word = false;
        }
        field = next.b;
        bit ^= 1;
        scanned = tick;
    }

    ledger.check(kernel, field);
    Field inverse = field;
    for (unsigned tick = scanned; tick > 0; --tick) {
        bit ^= 1;
        kernel.scatter(inverse);
        kernel.transport(inverse, bit, true);
    }
    if (bit != 1 || inverse != launch)
        throw std::logic_error("full inverse did not recover launch and bit");

    std::cout << "SCAN " << rank << ' ' << scanned << ' ' << limit << ' '
              << recurrent_writes << ' ' << moved_active_reads << '\n';
    if (found) {
        h3::match_detail::print_certificate(kernel, 2, 2, 1, found->first);
        h3::match_detail::print_certificate(kernel, 2, 2, 2, found->second);
    }
    return found.has_value();
}

}  // namespace double_renewal

int main() try {
    Kernel kernel;
    const Queries queries = read_queries(kernel, std::cin);
    if (queries.size() != rank_count)
        throw std::runtime_error("expected all 85 four-wire launches");
    for (unsigned rank = 0; rank < rank_count; ++rank) {
        const auto query = queries.find({2, rank});
        if (query == queries.end() || query->second.depth != 0)
            throw std::runtime_error("expected mode 2, depth 0 four-wire launch");
    }
    const Pair t{kernel.intern(t_word), kernel.intern(scale(t_word, -1))};
    const Pair w{kernel.intern(w_word), kernel.intern(scale(w_word, -1))};
    std::vector<unsigned> ranks{43, 0, 22};
    for (unsigned rank = 0; rank < rank_count; ++rank)
        if (rank != 43 && rank != 0 && rank != 22) ranks.push_back(rank);
    for (unsigned rank : ranks) {
        if (double_renewal::scan(kernel, rank, queries.at({2, rank}).cut, t, w)) break;
    }
    if (!std::cout) throw std::runtime_error("failed writing search records");
    return 0;
} catch (const std::exception &error) {
    std::cerr << error.what() << '\n';
    return 2;
}
