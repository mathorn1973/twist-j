// SPDX-License-Identifier: Apache-2.0
// Exact continuation of the original rank-43 H3 relay experiment.
#include "dynamics.hpp"

#include <array>
#include <cstddef>
#include <cstdint>
#include <iostream>
#include <optional>
#include <stdexcept>
#include <string>
#include <unordered_map>
#include <vector>

namespace {

constexpr unsigned writer = 1, reader = 2, target = 3;
constexpr unsigned prefix = 1u << 26, ceiling = 1u << 30;
constexpr unsigned fixed_read = 36'442'233;
using Pair = std::array<Id, 2>;
using Ready = std::array<Id, 6>;
using Episode = std::array<Id, 12>;

struct EpisodeHash {
    std::size_t operator()(const Episode &key) const noexcept {
        std::uint64_t hash = 0;
        for (Id id : key)
            hash = (hash ^ id) * 0x9e3779b185ebca87ULL + 0x846ca68bULL;
        return static_cast<std::size_t>(hash ^ (hash >> 32));
    }
};

Pair matter(const Cell &cell) {
    return {cell[0], cell[1]};
}

Ready ready(const Cell &pre, const Cell &contact) {
    return {pre[0], pre[1], pre[2], pre[3], contact[2], contact[3]};
}

unsigned moved_rails(const Cell &pre, const Cell &contact) {
    return static_cast<unsigned>(pre[0] != contact[0]) +
           static_cast<unsigned>(pre[1] != contact[1]);
}

struct Counts {
    unsigned recurrences{};
    std::array<unsigned, 2> reads{}, relay{}, returned{}, overwrite{};
};

struct Emission {
    unsigned prior, tick;
    Cell contact, output;
};

struct Hit {
    unsigned tick;
    Ready input;
    Pair source, arrival, output;
};

struct Pending {
    Hit event;
    unsigned branch;
};

struct Fixed {
    Emission emission;
    Cell donor_pre, pre, contact, output;
    Pair target_pre{}, target_contact{};
    unsigned stop{}, moved{};
};

void check(bool condition, const char *message) {
    if (!condition) throw std::logic_error(message);
}

bool compatible(const Hit &a, const Hit &b) {
    return a.input == b.input && a.source != b.source &&
           a.arrival != b.arrival && a.output != b.output;
}

std::array<std::uint64_t, 3> pairs(const Hit &reference,
                                  const std::vector<Hit> &novel_B1,
                                  const std::vector<Hit> &all_B2) {
    std::array<std::uint64_t, 3> counts{};
    for (const Hit &a : novel_B1) {
        counts[0] += compatible(a, reference);
        for (const Hit &b : all_B2) {
            if (!compatible(a, b)) continue;
            counts[1] += b.tick <= prefix;
            ++counts[2];
        }
    }
    return counts;
}

void print_counts(const char *label, unsigned ticks, const Counts &count,
                  const std::optional<Pending> &current) {
    std::cout << label << ' ' << ticks << ' ' << count.recurrences;
    for (const auto &arms : {count.reads, count.relay, count.returned, count.overwrite})
        std::cout << ' ' << arms[0] << ' ' << arms[1];
    std::cout << ' ' << (current && current->branch == 1)
              << ' ' << (current && current->branch == 2) << '\n';
}

template <std::size_t N>
void print_words(const Dynamics &dynamics, const std::array<Id, N> &ids) {
    for (Id id : ids)
        for (auto value : dynamics.value(id)) std::cout << ' ' << value;
}

template <std::size_t N>
bool exact(const Dynamics &dynamics, const std::array<Id, N> &actual,
           const std::array<Word, N> &expected) {
    for (std::size_t i = 0; i < N; ++i)
        if (dynamics.value(actual[i]) != expected[i]) return false;
    return true;
}

void verify_fixed(const Dynamics &d, const Fixed &f) {
    check(f.emission.prior == 8'176'761 && f.emission.tick == 36'442'231 &&
          f.stop == 36'442'234 && f.moved == 2, "fixed event times differ from #2053");
    check(exact(d, f.emission.contact, std::array{
              Word{-2,-2,0,-4}, Word{2,2,0,4}, Word{2,0,1,0}, Word{-2,0,-3,0}}) &&
          exact(d, f.emission.output, std::array{
              Word{0,-2,0,-2}, Word{0,2,0,2}, Word{0,-2,1,-2}, Word{0,2,-3,2}}) &&
          exact(d, f.donor_pre, std::array{
              Word{0,-2,0,-2}, Word{0,2,0,2}, Word{-2,-3,0,-3}, Word{0,2,-3,2}}) &&
          exact(d, f.pre, std::array{
              Word{2,2,2,2}, Word{-2,-2,-2,-2}, Word{4,2,4,2}, Word{3,2,0,4}}) &&
          exact(d, f.contact, std::array{
              Word{2,-1,1,1}, Word{-2,1,-1,-1}, Word{4,2,4,2}, Word{6,2,2,4}}) &&
          exact(d, f.output, std::array{
              Word{1,0,1,2}, Word{-1,0,-1,-2}, Word{2,1,2,1}, Word{8,3,4,5}}) &&
          exact(d, f.target_pre, std::array{Word{-1,0,-1,0},Word{1,0,1,0}}) &&
          exact(d, f.target_contact, std::array{Word{0,1,0,2},Word{0,-1,0,-2}}),
          "fixed local fields differ from #2053");
}

void audit_target(const Dynamics &d, const Cell &a, const Cell &b,
                  const Cell &a_after, const Cell &b_after) {
    for (unsigned i = 0; i < 2; ++i) {
        const Id a0 = a[i], b0 = b[i], a1 = a_after[i], b1 = b_after[i];
        check((a0 != a1) == (b0 != b1), "target C endpoint movement differs");
        for (unsigned j = 0; j < 4; ++j) {
            const auto x = d.value(a0)[j], y = d.value(b0)[j];
            check(x + y == d.value(a1)[j] + d.value(b1)[j], "target C ledger mismatch");
            if ((x - y) % 2 != 0)
                check(a0 == a1 && b0 == b1, "refused target rail moved");
        }
    }
}

void scan(Dynamics &dynamics, Field &field) {
    Counts before, after;
    std::unordered_map<Episode, unsigned, EpisodeHash> original;
    std::optional<Emission> held;
    std::optional<Pending> current;
    std::optional<Fixed> fixed;
    std::optional<Hit> reference;
    std::vector<Hit> novel_B1, all_B2;
    unsigned bit = 1;
    unsigned odd_contacts = 0, four_ready = 0, six_ready = 0;

    for (unsigned tick = 1; tick <= ceiling; ++tick) {
        const Cell writer_pre = field[writer], reader_pre = field[reader];
        const Cell donor_pre = bit ? reader_pre : field[0];
        const Cell target_pre = field[target];
        Cell writer_c{}, reader_c{};
        unsigned writer_tag{}, reader_tag{};
        dynamics.advance(field, bit, writer_c, reader_c, writer_tag, reader_tag);

        if (tick > prefix && bit) {
            ++odd_contacts;
            if (reader_pre == fixed->pre) {
                ++four_ready;
                if (reader_c[2] == fixed->contact[2] && reader_c[3] == fixed->contact[3])
                    ++six_ready;
            }
        }

        if (current) {
            const Pending &record = *current;
            check(matter(reader_pre) == record.event.output, "held reader word interrupted");
            const unsigned moved = moved_rails(reader_pre, reader_c);
            const bool overwritten = matter(reader_c) != matter(field[reader]);
            if (moved || overwritten) {
                Counts &counts = record.event.tick <= prefix ? before : after;
                const unsigned branch = record.branch - 1;
                if (moved && bit == 0) {
                    const Cell &target_c = dynamics.third_c();
                    audit_target(dynamics, reader_pre, target_pre, reader_c, target_c);
                    ++counts.relay[branch];
                    if (record.branch == 2) all_B2.push_back(record.event);
                    else if (record.event.tick > prefix) novel_B1.push_back(record.event);
                    if (record.event.tick == fixed_read) {
                        check(dynamics.third_btag() == 0, "fixed target must take B0");
                        fixed->target_pre = matter(target_pre);
                        fixed->target_contact = matter(target_c);
                        fixed->stop = tick;
                        fixed->moved = moved;
                        verify_fixed(dynamics, *fixed);
                        reference = record.event;
                    }
                } else if (moved) {
                    ++counts.returned[branch];
                } else {
                    ++counts.overwrite[branch];
                }
                current.reset();
            }
        }

        const unsigned receiver_moved = moved_rails(reader_pre, reader_c);
        if (held && bit && receiver_moved == 2 && reader_tag &&
            matter(reader_c) != matter(field[reader])) {
            check(reader_tag <= 2 && !current && matter(writer_pre) == matter(held->output),
                  "first hop source provenance mismatch");
            check(matter(writer_pre) != matter(writer_c), "only one first-hop endpoint moved");
            const Hit item{tick, ready(reader_pre, reader_c), matter(writer_pre),
                           matter(reader_c), matter(field[reader])};
            current = Pending{item, reader_tag};
            ++(tick <= prefix ? before : after).reads[reader_tag - 1];
            if (tick == fixed_read) {
                check(reader_tag == 2, "fixed read must be B2");
                fixed = Fixed{*held, writer_pre, reader_pre, reader_c, field[reader]};
            }
        }

        const bool writer_moved = matter(writer_pre) != matter(writer_c);
        const bool writer_changed_b = matter(writer_c) != matter(field[writer]);
        if (writer_moved || writer_changed_b) held.reset();
        if (writer_tag == 2 && writer_moved && writer_changed_b) {
            // Every C rail conserves the sum of its two endpoints. A change
            // on the writer rail therefore changes the donor on that rail.
            const auto &output = field[writer];
            const Episode key{writer, bit, writer_pre[0], writer_pre[1], writer_pre[2],
                writer_pre[3], donor_pre[0], donor_pre[1], writer_c[2], writer_c[3],
                output[0], output[1]};
            const auto [it, inserted] = original.try_emplace(key, tick);
            if (!inserted) {
                held = Emission{it->second, tick, writer_c, output};
                ++(tick <= prefix ? before : after).recurrences;
            }
        }
        bit ^= 1;
        if (tick == prefix) {
            check(reference && fixed && !current && before.recurrences == 153'059 &&
                  before.reads == std::array{554u, 159u} &&
                  before.relay == std::array{102u, 13u} &&
                  before.returned == std::array{144u, 2u} &&
                  before.overwrite == std::array{308u, 144u},
                  "the original #2053 prefix disagrees");
            print_counts("PREFIX", prefix, before, current);
        }
    }

    print_counts("POST", ceiling, after, current);
    std::cout << "READINESS " << odd_contacts << ' ' << four_ready << ' ' << six_ready << '\n';
    const auto matched = pairs(*reference, novel_B1, all_B2);
    std::cout << "PAIRS " << matched[0] << ' ' << matched[1] << ' ' << matched[2] << '\n';
    std::cout << "FIXED " << fixed->emission.prior << ' ' << fixed->emission.tick << ' '
              << fixed_read << ' ' << fixed->stop << ' ' << fixed->moved << '\n';
    std::cout << "FIXED_WORDS";
    for (const Cell &cell : {fixed->emission.contact, fixed->emission.output, fixed->donor_pre,
                             fixed->pre, fixed->contact, fixed->output})
        print_words(dynamics, cell);
    print_words(dynamics, fixed->target_pre);
    print_words(dynamics, fixed->target_contact);
    std::cout << "\nFINAL " << ceiling << ' ' << bit;
    for (const Cell &cell : field) print_words(dynamics, cell);
    std::cout << '\n';
}

} // namespace

int main() try {
    int mode{}, rank{}, depth{};
    check(static_cast<bool>(std::cin >> mode >> rank >> depth) &&
          mode == 2 && rank == 43 && depth == 0, "expected mode 2, depth 0, rank 43");
    Dynamics dynamics;
    Field field{};
    for (Cell &cell : field) {
        for (Id &id : cell) {
            Word word{};
            for (auto &coefficient : word)
                check(static_cast<bool>(std::cin >> coefficient), "truncated launch");
            id = dynamics.intern(word);
        }
    }
    std::string extra;
    check(!(std::cin >> extra), "trailing launch data");
    scan(dynamics, field);
    check(static_cast<bool>(std::cout), "failed writing continuation records");
    return 0;
} catch (const std::exception &error) {
    std::cerr << error.what() << '\n';
    return 2;
}
