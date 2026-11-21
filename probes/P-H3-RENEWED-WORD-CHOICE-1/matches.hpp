// SPDX-License-Identifier: Apache-2.0
#pragma once

#include <algorithm>
#include <array>
#include <compare>
#include <cstdint>
#include <iostream>
#include <map>
#include <optional>
#include <stdexcept>
#include <tuple>
#include <utility>

namespace h3 {

struct Event {
    unsigned rank, writer, reader, bit, write, read, writer_tag, reader_tag, prior;
    bool anchor;
    Cell writer_c, writer_b, donor_pre, reader_pre, reader_c, reader_b;
};

namespace match_detail {

constexpr std::array categories{"A", "R", "RR", "AA", "A181"};
constexpr std::array modes{"ANY", "MARKED_MOVED", "BOTH_MOVED"};

inline Pair matter(const Cell &cell) {
    return {cell[0], cell[1]};
}

inline Pair radiation(const Cell &cell) {
    return {cell[2], cell[3]};
}

using Readiness = std::tuple<unsigned, unsigned, unsigned, Cell, Pair>;

struct Mark {
    bool anchor, recurrent, anchor181, moved;

    auto operator<=>(const Mark &) const = default;
};

struct Outcome {
    Pair word, arrival, final;
    Mark mark;

    auto operator<=>(const Outcome &) const = default;
};

// Exact grouping keys use interned words. Representative order uses only
// provenance coordinates, and therefore does not depend on intern IDs.
inline auto order(const Event &event) {
    return std::tuple{event.read, event.read - event.write, event.write, event.rank,
                      event.writer, event.reader, event.bit,
                      event.writer_tag, event.reader_tag, event.prior, event.anchor};
}

struct Bucket {
    std::uint64_t count{};
    Event exemplar{};

    void add(const Event &event) {
        if (count++ == 0 || order(event) < order(exemplar)) exemplar = event;
    }
};

struct Certificate {
    Event first, second;
    bool first_marked_moved, second_marked_moved;

    auto key() const {
        return std::tuple{!(first_marked_moved || second_marked_moved),
                          std::max(first.read, second.read), std::min(first.read, second.read),
                          first.rank, first.read - first.write, second.read - second.write,
                          order(first), order(second)};
    }
};

using Census = std::array<std::array<std::uint64_t, modes.size()>, categories.size()>;
using Certificates =
    std::array<std::array<std::optional<Certificate>, modes.size()>, categories.size()>;

inline Certificates certificates;

inline void record(Census &counts, unsigned category, unsigned mode,
                   const Bucket &a, const Bucket &b, bool moved_a, bool moved_b) {
    counts[category][mode] += a.count * b.count;
    Certificate candidate{a.exemplar, b.exemplar, moved_a, moved_b};
    if (std::tuple{!moved_b, order(b.exemplar)} < std::tuple{!moved_a, order(a.exemplar)}) {
        std::swap(candidate.first, candidate.second);
        std::swap(candidate.first_marked_moved, candidate.second_marked_moved);
    }
    auto &best = certificates[category][mode];
    if (!best || candidate.key() < best->key()) best = candidate;
}

inline void compare(Census &counts, const Outcome &a, const Bucket &bucket_a,
                    const Outcome &b, const Bucket &bucket_b) {
    if (a.word == b.word || a.arrival == b.arrival || a.final == b.final) return;

    const std::array marks_a{a.mark.anchor, a.mark.recurrent, a.mark.recurrent,
                             a.mark.anchor, a.mark.anchor181};
    const std::array marks_b{b.mark.anchor, b.mark.recurrent, b.mark.recurrent,
                             b.mark.anchor, b.mark.anchor181};
    const std::array eligible{marks_a[0] || marks_b[0], marks_a[1] || marks_b[1],
                              marks_a[2] && marks_b[2], marks_a[3] && marks_b[3],
                              marks_a[4] || marks_b[4]};
    for (unsigned category = 0; category < categories.size(); ++category) {
        if (!eligible[category]) continue;
        const bool moved_a = marks_a[category] && a.mark.moved;
        const bool moved_b = marks_b[category] && b.mark.moved;
        record(counts, category, 0, bucket_a, bucket_b, moved_a, moved_b);
        if (moved_a || moved_b) record(counts, category, 1, bucket_a, bucket_b, moved_a, moved_b);
        if (a.mark.moved && b.mark.moved)
            record(counts, category, 2, bucket_a, bucket_b, moved_a, moved_b);
    }
}

inline void print_certificate(const Kernel &kernel, unsigned category, unsigned mode,
                              unsigned arm, const Event &event) {
    std::cout << "CERT\t" << categories[category] << '\t' << modes[mode] << '\t' << arm
              << '\t' << event.rank << '\t' << event.writer << '\t' << event.reader
              << '\t' << event.bit << '\t' << event.write << '\t' << event.read
              << '\t' << event.writer_tag << '\t' << event.reader_tag << '\t' << event.prior
              << '\t' << static_cast<unsigned>(event.anchor);
    for (const Cell &cell : {event.writer_c, event.writer_b, event.donor_pre,
                             event.reader_pre, event.reader_c, event.reader_b}) {
        for (auto id : cell)
            for (auto coefficient : kernel.value(id)) std::cout << '\t' << coefficient;
    }
    std::cout << '\n';
}

}  // namespace match_detail

class Matches {
    using Branches = std::array<std::map<match_detail::Outcome, match_detail::Bucket>, 2>;
    std::map<match_detail::Readiness, Branches> groups;
    std::optional<unsigned> active_rank;

public:
    explicit Matches(Kernel &) {}

    void observe(const Event &event) {
        using namespace match_detail;
        if ((active_rank && *active_rank != event.rank) || event.read <= event.write
            || event.reader_tag < 1 || event.reader_tag > 2) {
            throw std::logic_error("invalid H3 matched encounter");
        }
        active_rank = event.rank;
        const Readiness readiness{event.writer, event.reader, event.bit,
                                  event.reader_pre, radiation(event.reader_c)};
        const Pair arrival = matter(event.reader_c);
        const Mark mark{event.anchor, event.prior > 0, event.anchor && event.write == 181,
                        matter(event.reader_pre) != arrival};
        const Outcome outcome{matter(event.donor_pre), arrival, matter(event.reader_b), mark};
        groups[readiness][event.reader_tag - 1][outcome].add(event);
    }

    void finish(unsigned rank) {
        using namespace match_detail;
        if (active_rank && *active_rank != rank) throw std::logic_error("H3 census rank mismatch");
        Census counts{};
        // Cross the two branch buckets once. Identical observations retain
        // their multiplicities, so each unordered pair contributes exactly once.
        for (const auto &[readiness, branches] : groups) {
            for (const auto &[a, bucket_a] : branches[0]) {
                for (const auto &[b, bucket_b] : branches[1]) {
                    compare(counts, a, bucket_a, b, bucket_b);
                }
            }
        }
        for (unsigned category = 0; category < categories.size(); ++category)
            for (unsigned mode = 0; mode < modes.size(); ++mode)
                std::cout << "MATCH\t" << rank << '\t' << categories[category] << '\t'
                          << modes[mode] << '\t' << counts[category][mode] << '\n';
        groups.clear();
        active_rank.reset();
    }
};

inline void report(const Kernel &kernel) {
    using namespace match_detail;
    for (unsigned category = 0; category < categories.size(); ++category) {
        for (unsigned mode = 0; mode < modes.size(); ++mode) {
            if (const auto &pair = certificates[category][mode]) {
                print_certificate(kernel, category, mode, 1, pair->first);
                print_certificate(kernel, category, mode, 2, pair->second);
            }
        }
    }
}

}  // namespace h3
