// SPDX-License-Identifier: Apache-2.0
// Follow held receiver output on the unchanged rank-43 H3 trajectory.
#define main predecessor_main
#include "../P-H3-SECOND-WRITE-1/audit.cpp"
#undef main
#include "../P-H3-RENEWED-WORD-CHOICE-1/matches.hpp"

namespace output_relay {

constexpr unsigned writer = 1, carrier = 2, third = 3, match_bit = 1, rank = 43;
constexpr unsigned limit = 67'108'864;
constexpr std::array fixed_ticks{7'390'475u, 9'915'383u};

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

struct Source {
    unsigned tick, prior;
    Cell c, b;
};

using Cut = std::array<Cell, 4>;

struct Relay {
    h3::Event event;
    unsigned tick{}, site{}, attempts{}, refused{}, moved{};
    unsigned first_tick{}, first_admitted{}, first_moved{}, third_tag{};
    const char *stage{};
    Cut first{}, stop{};
};

unsigned changed_rails(const Cell &a, const Cell &b) {
    return static_cast<unsigned>(a[0] != b[0]) + static_cast<unsigned>(a[1] != b[1]);
}

unsigned admitted_rails(Kernel &kernel, const Cell &a, const Cell &b) {
    return static_cast<unsigned>(integral_pair(kernel.value(a[0]), kernel.value(b[0]))) +
           static_cast<unsigned>(integral_pair(kernel.value(a[1]), kernel.value(b[1])));
}

Cut cut(const Field &pre, const Field &post, unsigned mate_site) {
    return {pre[carrier], post[carrier], pre[mate_site], post[mate_site]};
}

bool follow(Kernel &kernel, Relay &relay, const Field &pre, const Transition &next,
            unsigned tick, unsigned bit) {
    if (matter(pre[carrier]) != matter(relay.event.reader_b))
        throw std::logic_error("receiver output provenance differs from its native carrier");
    const unsigned mate_site = mate(carrier, bit);
    const unsigned moved = changed_rails(pre[mate_site], next.c[mate_site]);
    for (unsigned rail = 0; rail < 2; ++rail) {
        if ((pre[carrier][rail] != next.c[carrier][rail]) !=
            (pre[mate_site][rail] != next.c[mate_site][rail]))
            throw std::logic_error("C changes material at just one contact endpoint");
    }
    if (mate_site == third) {
        const unsigned admitted = admitted_rails(kernel, pre[carrier], pre[third]);
        if (moved > admitted) throw std::logic_error("refused material rail moved");
        ++relay.attempts;
        relay.refused += 2 - admitted;
        if (!relay.first_tick) {
            relay.first_tick = tick;
            relay.first_admitted = admitted;
            relay.first_moved = moved;
            relay.first = cut(pre, next.c, third);
        }
    }
    if (moved) {
        relay.stage = "C";
        relay.site = mate_site;
        relay.stop = cut(pre, next.c, mate_site);
        if (mate_site == third) {
            relay.moved = moved;
            relay.third_tag = next.tags[third];
        }
    } else if (matter(next.c[carrier]) != matter(next.b[carrier])) {
        relay.stage = "B";
        relay.site = carrier;
        relay.stop = cut(next.c, next.b, mate_site);
    } else {
        return false;
    }
    relay.tick = tick;
    return true;
}

using Readiness = std::array<Id, 6>;

struct Outcome {
    Pair word, arrival, output;
    bool operator==(const Outcome &) const = default;
};
struct Representative {
    Outcome outcome;
    Relay relay;
};

using Branches = std::array<std::vector<Representative>, 2>;
using Groups = std::unordered_map<Readiness, Branches, Hash>;
using Witness = std::pair<Relay, Relay>;

std::optional<Witness> observe(Groups &groups, const Relay &relay) {
    const h3::Event &event = relay.event;
    const Cell &pre = event.reader_pre;
    const Cell &c = event.reader_c;
    const Readiness key{pre[0], pre[1], pre[2], pre[3], c[2], c[3]};
    const Outcome outcome{matter(event.donor_pre), matter(c), matter(event.reader_b)};
    const unsigned tag = event.reader_tag;
    Branches &branches = groups[key];
    for (const Representative &other : branches[2 - tag]) {
        const Outcome &a = other.outcome;
        if (a.word != outcome.word && a.arrival != outcome.arrival && a.output != outcome.output)
            return Witness{other.relay, relay};
    }
    auto &same = branches[tag - 1];
    if (std::none_of(same.begin(), same.end(),
                     [&](const Representative &other) { return other.outcome == outcome; }))
        same.push_back({outcome, relay});
    return std::nullopt;
}

unsigned fixed_arm(unsigned read) {
    if (read == fixed_ticks[0]) return 1;
    if (read == fixed_ticks[1]) return 2;
    return 0;
}

void print_cut(const Kernel &kernel, unsigned arm, const char *label, const Cut &state) {
    std::cout << "TRACE " << arm << ' ' << label;
    for (const Cell &cell : state)
        for (Id id : cell)
            for (auto coefficient : kernel.value(id)) std::cout << ' ' << coefficient;
    std::cout << '\n';
}

void emit(const Kernel &kernel, unsigned arm, const Relay &relay) {
    h3::match_detail::print_certificate(kernel, 2, 2, arm, relay.event);
    std::cout << "RELAY " << arm << ' ' << relay.event.read << ' ' << relay.tick << ' '
              << relay.stage << ' ' << relay.site << ' ' << relay.attempts << ' '
              << relay.refused << ' ' << relay.moved << ' ' << relay.first_tick << ' '
              << relay.first_admitted << ' ' << relay.first_moved << ' ' << relay.third_tag << '\n';
    if (relay.first_tick) print_cut(kernel, arm, "FIRST3", relay.first);
    print_cut(kernel, arm, "STOP", relay.stop);
}

void scan(Kernel &kernel, const Field &launch) {
    Field field = launch;
    Ledger ledger;
    std::unordered_map<Episode, unsigned, Hash> earlier;
    std::optional<Source> held;
    std::optional<Relay> pending;
    std::array<std::optional<Relay>, 2> fixed;
    std::optional<Witness> alternative;
    Groups groups;
    std::array<unsigned, 2> reads{}, hits{};
    unsigned repeat_count = 0, bit = 1, scanned = 0;

    for (unsigned tick = 1; tick <= limit; ++tick) {
        Transition next{field, {}};
        kernel.transport(next.c, bit);
        next.b = next.c;
        for (unsigned site = 0; site < next.b.size(); ++site)
            next.tags[site] = kernel.collide(next.b[site]);

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

        if (pending) {
            const unsigned mate_site = mate(carrier, bit);
            // Audit the first attempt at site 3, including refusal with an unchanged pair.
            const bool first_attempt = mate_site == third && !pending->first_tick;
            const bool stopped = follow(kernel, *pending, field, next, tick, bit);
            if (first_attempt || stopped) audit();
            if (stopped) {
                if (pending->moved) {
                    ++hits[pending->event.reader_tag - 1];
                    if (!alternative) alternative = observe(groups, *pending);
                }
                if (unsigned arm = fixed_arm(pending->event.read)) fixed[arm - 1] = *pending;
                pending.reset();
            }
        }

        bool recorded = false;
        const unsigned tag = next.tags[carrier];
        if (held && bit == match_bit && changed_rails(field[carrier], next.c[carrier]) == 2 &&
            (tag == 1 || tag == 2) && matter(next.c[carrier]) != matter(next.b[carrier])) {
            if (pending || mate(writer, bit) != carrier || matter(field[writer]) != matter(held->b))
                throw std::logic_error("pre-C source word is not continuously held");
            audit();
            pending = Relay{h3::Event{rank, writer, carrier, bit, held->tick, tick, 2, tag, held->prior,
                                       false, held->c, held->b, field[writer], field[carrier],
                                       next.c[carrier], next.b[carrier]}};
            ++reads[tag - 1];
            recorded = true;
        }
        if (fixed_arm(tick) && !recorded)
            throw std::logic_error("missing a fixed #2049 recurrent read");

        const bool changed_c = matter(field[writer]) != matter(next.c[writer]);
        const bool changed_b = matter(next.c[writer]) != matter(next.b[writer]);
        if (changed_c || changed_b) held.reset();
        if (next.tags[writer] == 2 && changed_c && changed_b) {
            const unsigned donor = mate(writer, bit);
            if (matter(field[donor]) != matter(next.c[donor])) {
                const auto [at, fresh] = earlier.try_emplace(episode(field, next, writer, donor, bit), tick);
                if (!fresh) {
                    audit();
                    held = Source{tick, at->second, next.c[writer], next.b[writer]};
                    ++repeat_count;
                }
            }
        }

        field = next.b;
        bit ^= 1;
        scanned = tick;
        if (fixed[0] && fixed[1] && ((fixed[0]->moved && fixed[1]->moved) || alternative))
            break;
    }

    std::array<unsigned, 2> still_held{};
    if (pending) {
        ++still_held[pending->event.reader_tag - 1];
        if (unsigned arm = fixed_arm(pending->event.read)) {
            pending->tick = scanned;
            pending->stage = "END";
            pending->site = 32;
            pending->stop = cut(field, field, third);
            fixed[arm - 1] = *pending;
        }
    }
    if (!fixed[0] || !fixed[1]) throw std::logic_error("fixed relay records are missing");

    ledger.check(kernel, field);
    Field inverse = field;
    for (unsigned tick = scanned; tick > 0; --tick) {
        bit ^= 1;
        kernel.scatter(inverse);
        kernel.transport(inverse, bit, true);
    }
    if (bit != 1 || inverse != launch)
        throw std::logic_error("full inverse did not recover launch and bit");

    std::cout << "SCAN " << scanned << ' ' << limit << ' ' << repeat_count << ' '
              << reads[0] << ' ' << reads[1] << ' ' << hits[0] << ' ' << hits[1] << ' '
              << still_held[0] << ' ' << still_held[1] << '\n';
    emit(kernel, 1, *fixed[0]);
    emit(kernel, 2, *fixed[1]);
    if ((!fixed[0]->moved || !fixed[1]->moved) && alternative) {
        emit(kernel, 3, alternative->first);
        emit(kernel, 4, alternative->second);
    }
}

}  // namespace output_relay

int main() try {
    Kernel kernel;
    const Queries queries = read_queries(kernel, std::cin);
    const auto entry = queries.find({2, output_relay::rank});
    if ((queries.size() != 1 && queries.size() != rank_count) ||
        entry == queries.end() || entry->second.depth != 0)
        throw std::runtime_error("expected mode 2, depth 0 rank-43 four-wire launch");
    output_relay::scan(kernel, entry->second.cut);
    if (!std::cout) throw std::runtime_error("failed writing relay records");
    return 0;
} catch (const std::exception &error) {
    std::cerr << error.what() << '\n';
    return 2;
}
