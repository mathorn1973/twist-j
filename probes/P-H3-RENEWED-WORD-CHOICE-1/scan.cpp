// SPDX-License-Identifier: Apache-2.0
// Native held-word encounters on the original four-wire launches.
#define main predecessor_main
#include "../P-H3-SECOND-WRITE-1/audit.cpp"
#undef main
#include "matches.hpp"

namespace renewed {

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

Transition advance(Kernel &kernel, Ledger &ledger, const Field &before, unsigned bit) {
    Transition next{before, {}};
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
    if (inverse != before)
        throw std::logic_error("inverse C mismatch");
    return next;
}

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

unsigned admitted_rails(Kernel &kernel, const Cell &a, const Cell &b) {
    unsigned count = 0;
    for (unsigned lane = 0; lane < 2; ++lane)
        count += integral_pair(kernel.value(a[lane]), kernel.value(b[lane]));
    return count;
}

Episode episode(const Field &pre, const Transition &next, unsigned site, unsigned donor, unsigned bit) {
    const Cell &before = pre[site];
    const Cell &c = next.c[site];
    const Cell &b = next.b[site];
    return {site, bit, before[0], before[1], before[2], before[3],
            pre[donor][0], pre[donor][1], c[2], c[3], b[0], b[1]};
}

void scan(Kernel &kernel, Ledger &ledger, unsigned rank, const Field &launch,
          const Pair &t, const Pair &w) {
    const bool first_expected = rank == 0 || rank == 22 || rank == 43;
    const unsigned limit = rank == 43 ? 1'048'576 : first_expected ? 65'536 : 8'192;
    Field field = launch;
    h3::Matches matches(kernel);
    std::array<Held, 32> held{};
    std::unordered_map<Episode, unsigned, Hash> prior_writes;
    bool source125 = false, restored157 = false, held158 = false, first_write = false;
    unsigned formation_tick = 0, first_anchor = 0;
    unsigned count_anchor = 0, count_repeat = 0, anchor_contacts = 0;
    unsigned anchor_moved = 0, anchor_active = 0;
    unsigned moved_b1 = 0, moved_b2 = 0;
    unsigned bit = 1;

    for (unsigned tick = 1; tick <= limit; ++tick) {
        const Transition next = advance(kernel, ledger, field, bit);
        const Pair pre_word = matter(field[memory]);
        const Pair c_word = matter(next.c[memory]);
        const Pair b_word = matter(next.b[memory]);
        if (tick == 125)
            source125 = next.tags[source] == 2;
        if (tick == 157)
            restored157 = c_word == t && b_word == w && next.tags[memory] == 1;
        if (tick == 158)
            held158 = restored157 && pre_word == w && c_word == w && b_word == w;
        if (tick == first_tick) {
            first_write = source125 && held158 && c_word != w && b_word != w &&
                functional_write(kernel, bit, field, next, t, w);
            if (first_write != first_expected)
                throw std::logic_error("first writer census differs from the predecessor");
        }

        const bool anchor = tick > first_tick && first_write &&
            functional_write(kernel, bit, field, next, t, w);
        if (anchor) {
            if (!formation_tick)
                throw std::logic_error("anchor lacks a continuously renewed stored word");
            ++count_anchor;
            if (!first_anchor) first_anchor = tick;
        }
        if (tick > first_tick && first_write) {
            if (pre_word != w && c_word == w) formation_tick = tick;
            if (c_word != w) formation_tick = 0;
            if (c_word != w && b_word == w) formation_tick = tick;
            if (b_word != w) formation_tick = 0;
        }

        if (tick == 182 && first_expected) {
            const unsigned reader = mate(worker, bit);
            const Held &outgoing = held[worker];
            if (!outgoing.anchor || outgoing.tick != 181 || reader != 29)
                throw std::logic_error("missing anchor at the 181 B to 182 C cut");
            const bool changed = matter(field[reader]) != matter(next.c[reader]);
            const unsigned admitted = admitted_rails(kernel, field[worker], field[reader]);
            if (rank == 43 && (admitted != 0 || changed || next.tags[reader] != 0))
                throw std::logic_error("rank-43 immediate encounter differs from the predecessor");
            std::cout << "CUT181 " << rank << ' '
                      << admitted << ' '
                      << changed << ' ' << next.tags[reader] << '\n';
        }

        // Observe the pre-C carrier before invalidating or replacing its provenance.
        for (unsigned writer = 0; writer < held.size(); ++writer) {
            const Held &emission = held[writer];
            if (!emission.tick) continue;
            if (matter(field[writer]) != matter(emission.b))
                throw std::logic_error("held output differs from its native pre-C carrier");
            const unsigned reader = mate(writer, bit);
            const bool moved = matter(field[reader]) != matter(next.c[reader]);
            const unsigned reader_tag = next.tags[reader];
            const bool active = matter(next.c[reader]) != matter(next.b[reader]);
            if (emission.anchor) {
                ++anchor_contacts;
                anchor_moved += moved;
                anchor_active += active;
                moved_b1 += moved && active && reader_tag == 1;
                moved_b2 += moved && active && reader_tag == 2;
            }
            if (!active) continue;
            if (reader_tag != 1 && reader_tag != 2)
                throw std::logic_error("material-changing reader has no active tag");
            h3::Event event{};
            event.rank = rank;
            event.writer = writer;
            event.reader = reader;
            event.bit = bit;
            event.write = emission.tick;
            event.read = tick;
            event.writer_tag = emission.tag;
            event.reader_tag = reader_tag;
            event.prior = emission.prior;
            event.anchor = emission.anchor;
            event.writer_c = emission.c;
            event.writer_b = emission.b;
            event.donor_pre = field[writer];
            event.reader_pre = field[reader];
            event.reader_c = next.c[reader];
            event.reader_b = next.b[reader];
            matches.observe(event);
        }

        for (unsigned writer = 0; writer < held.size(); ++writer) {
            const bool changed_c = matter(field[writer]) != matter(next.c[writer]);
            const bool changed_b = matter(next.c[writer]) != matter(next.b[writer]);
            if (changed_c || changed_b) held[writer] = {};
            if (!changed_b) continue;
            const unsigned tag = next.tags[writer], donor = mate(writer, bit);
            if (tag != 1 && tag != 2)
                throw std::logic_error("material-changing writer has no active tag");
            unsigned prior = 0;
            if (tag == 2 && changed_c && matter(field[donor]) != matter(next.c[donor])) {
                const auto [at, inserted] = prior_writes.try_emplace(
                    episode(field, next, writer, donor, bit), tick);
                if (!inserted) {
                    prior = at->second;
                    ++count_repeat;
                }
            }
            held[writer] = {tick, tag, prior, anchor && writer == worker,
                            next.c[writer], next.b[writer]};
        }
        field = next.b;
        bit ^= 1;
    }

    Field inverse = field;
    for (unsigned tick = limit; tick > 0; --tick) {
        bit ^= 1;
        kernel.scatter(inverse);
        kernel.transport(inverse, bit, true);
    }
    if (bit != 1 || inverse != launch)
        throw std::logic_error("full inverse did not recover launch and matching bit");
    if (first_anchor != (first_expected ? 181u : 0u) ||
        (rank == 43 && count_anchor != 12'938))
        throw std::logic_error("anchor census differs from the predecessor");
    std::cout << "RANK " << rank << ' ' << limit << ' ' << count_anchor << ' '
              << count_repeat << ' ' << anchor_contacts << ' ' << anchor_moved << ' '
              << anchor_active << ' ' << first_anchor << ' ' << moved_b1 << ' ' << moved_b2 << '\n';
    matches.finish(rank);
}

} // namespace renewed

int main() try {
    Kernel kernel;
    renewed::Ledger ledger;
    const Queries queries = read_queries(kernel, std::cin);
    if (queries.size() != rank_count)
        throw std::runtime_error("expected all 85 four-wire launches");
    const Pair t{kernel.intern(t_word), kernel.intern(scale(t_word, -1))};
    const Pair w{kernel.intern(w_word), kernel.intern(scale(w_word, -1))};
    for (unsigned rank = 0; rank < rank_count; ++rank) {
        const auto query = queries.find({2, rank});
        if (query == queries.end() || query->second.depth != 0)
            throw std::runtime_error("expected mode 2, depth 0 four-wire launch");
        renewed::scan(kernel, ledger, rank, query->second.cut, t, w);
    }
    h3::report(kernel);
    if (!std::cout) throw std::runtime_error("failed writing encounter records");
    return 0;
} catch (const std::exception &error) {
    std::cerr << error.what() << '\n';
    return 2;
}
