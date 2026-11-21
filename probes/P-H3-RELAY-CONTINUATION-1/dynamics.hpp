// SPDX-License-Identifier: Apache-2.0
#pragma once

#include <algorithm>
#include <array>
#include <bit>
#include <cstdint>
#include <cstring>
#include <fstream>
#include <iostream>
#include <limits>
#include <map>
#include <sstream>
#include <stdexcept>
#include <string>
#include <unordered_map>
#include <vector>

// Use the frozen exact contacts, collisions and local inverse/account checks
// on cache misses. Isolate the predecessor's standalone program and names.
namespace h3_tile_kernel {
#define main predecessor_program
#include "../P-H3-SECOND-WRITE-1/audit.cpp"
#undef main
}  // namespace h3_tile_kernel

using Word = std::array<std::int64_t, 4>;
using Id = std::uint32_t;
using Cell = std::array<Id, 4>;
using Field = std::array<Cell, 32>;

class Dynamics {
    using Tile = std::array<Cell, 4>;

    struct Entry {
        Tile before{}, contact{}, after{};
        std::array<unsigned char, 4> tags{};
        bool valid{}, unchanged{};
    };

    static constexpr std::size_t cache_size = std::size_t{1} << 16;
    static_assert(sizeof(Tile) == sizeof(std::array<std::uint64_t, 8>));
    h3_tile_kernel::Kernel kernel;
    std::vector<Entry> shared{cache_size};
    std::array<std::array<std::array<Entry, 2>, 8>, 2> recent{};
    Cell third_contact{};
    unsigned third_tag{};

    static bool equals(const Tile &a, const Tile &b) {
        return std::memcmp(a.data(), b.data(), sizeof(Tile)) == 0;
    }

    static std::size_t bucket(const Tile &tile) {
        const auto groups = std::bit_cast<std::array<std::uint64_t, 8>>(tile);
        constexpr std::array<std::uint64_t, 8> weights{
            0x9e3779b185ebca87ULL, 0xc2b2ae3d27d4eb4fULL, 0x165667b19e3779f9ULL,
            0x85ebca77c2b2ae63ULL, 0x27d4eb2f165667c5ULL, 0x94d049bb133111ebULL,
            0xbf58476d1ce4e5b9ULL, 0xd6e8feb86659fd93ULL
        };
        std::uint64_t hash = 0;
        for (std::size_t i = 0; i < groups.size(); ++i) hash += groups[i] * weights[i];
        hash ^= hash >> 31;
        hash *= 0x9e3779b185ebca87ULL;
        return hash >> 48;
    }

    void fill(Entry &entry, const Tile &before) {
        entry.before = before;
        entry.contact = before;
        Tile &contact = entry.contact;
        // Each matching partitions the lattice into disjoint 2 by 2 tiles.
        // Lanes 0..2 follow the oriented y bonds, lane 3 the oriented x bonds.
        for (unsigned rail = 0; rail < 3; ++rail) {
            kernel.contact(contact[0][rail], contact[1][rail], false);
            kernel.contact(contact[2][rail], contact[3][rail], false);
        }
        kernel.contact(contact[0][3], contact[2][3], false);
        kernel.contact(contact[1][3], contact[3][3], false);
        entry.after = contact;
        for (unsigned i = 0; i < entry.after.size(); ++i)
            entry.tags[i] = static_cast<unsigned char>(kernel.collide(entry.after[i]));
        entry.unchanged = equals(entry.before, entry.after);
        entry.valid = true;
    }

    const Entry &transition(const Tile &before, std::array<Entry, 2> &local) {
        if (local[0].valid && equals(before, local[0].before)) return local[0];
        if (local[1].valid && equals(before, local[1].before)) return local[1];
        Entry &entry = shared[bucket(before)];
        if (!entry.valid || !equals(before, entry.before)) fill(entry, before);
        local[1] = local[0];
        local[0] = entry;
        return local[0];
    }

    template<unsigned First, unsigned Second, unsigned Third, unsigned Fourth>
    void update(Field &field, std::array<Entry, 2> &memo, Cell &writer_c,
                Cell &reader_c, unsigned &writer_btag, unsigned &reader_btag) {
        constexpr std::array<unsigned, 4> sites{First, Second, Third, Fourth};
        const Tile before{field[First], field[Second], field[Third], field[Fourth]};
        const Entry &entry = transition(before, memo);
        for (unsigned i = 0; i < sites.size(); ++i) {
            if (sites[i] == 1) {
                writer_c = entry.contact[i];
                writer_btag = entry.tags[i];
            } else if (sites[i] == 2) {
                reader_c = entry.contact[i];
                reader_btag = entry.tags[i];
            } else if (sites[i] == 3) {
                third_contact = entry.contact[i];
                third_tag = entry.tags[i];
            }
        }
        if (!entry.unchanged) {
            field[First] = entry.after[0];
            field[Second] = entry.after[1];
            field[Third] = entry.after[2];
            field[Fourth] = entry.after[3];
        }
    }

    template<unsigned Bit, std::size_t Index>
    void tile(Field &field, Cell &writer_c, Cell &reader_c,
              unsigned &writer_btag, unsigned &reader_btag) {
        constexpr unsigned x = Bit + 2 * (Index / 2);
        constexpr unsigned y = Bit + 2 * (Index % 2);
        constexpr unsigned next_x = (x + 1) % 8;
        constexpr unsigned next_y = (y + 1) % 4;
        update<4 * x + y, 4 * x + next_y, 4 * next_x + y, 4 * next_x + next_y>(
            field, recent[Bit][Index], writer_c, reader_c, writer_btag, reader_btag);
    }

    template<unsigned Bit, std::size_t... Index>
    void advance_tiles(Field &field, Cell &writer_c, Cell &reader_c,
                       unsigned &writer_btag, unsigned &reader_btag,
                       std::index_sequence<Index...>) {
        (tile<Bit, Index>(field, writer_c, reader_c, writer_btag, reader_btag), ...);
    }

public:
    Id intern(const Word &word) { return kernel.intern(word); }
    const Word &value(Id id) const { return kernel.value(id); }
    const Cell &third_c() const { return third_contact; }
    unsigned third_btag() const { return third_tag; }

    void advance(Field &field, unsigned bit, Cell &writer_c, Cell &reader_c,
                 unsigned &writer_btag, unsigned &reader_btag) {
        if (bit == 0)
            advance_tiles<0>(field, writer_c, reader_c, writer_btag, reader_btag,
                             std::make_index_sequence<8>{});
        else if (bit == 1)
            advance_tiles<1>(field, writer_c, reader_c, writer_btag, reader_btag,
                             std::make_index_sequence<8>{});
        else
            throw std::invalid_argument("invalid H3 matching bit");
    }
};
