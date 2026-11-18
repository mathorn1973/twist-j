// SPDX-License-Identifier: Apache-2.0
// Independent four-coefficient replay of the fixed two-tick binary construction.
#define main predecessor_main
#include "audit.cpp"
#undef main

namespace binary {

constexpr RingCell bank{{{-5,1,-1,-3},{-4,1,-1,0},{-1,0,-2,5},{-1,0,-3,5}}};
constexpr RingCell writer_stock{{{-1,0,0,0},{1,0,0,0},{2,1,2,0},{0,1,0,0}}};
constexpr RingCell reader_stock{{{-1,-1,0,1},{1,1,0,-1},{1,0,0,-1},{0,-1,0,0}}};
constexpr RingCell input_stock{{{3,0,2,2},{-3,0,-2,-2},{},{}}};
constexpr std::array<Ring, 2> writer_word{{{0,1,0,1},{-1,-1,0,-1}}};
constexpr std::array<Ring, 2> reader_word{{{0,-1,-1,0},{0,0,1,1}}};
constexpr std::array<unsigned, 6> clocks{0, 1, 4, 5, 8, 9};
constexpr std::array<Ring, 3> bare_ledger{{{}, {18,6,8,10}, {270,0,94,94}}};

void require(bool ok, const char *name) {
    if (!ok) throw std::runtime_error(name);
}

Pair matter(const Cell &c) { return {c[0], c[1]}; }
Pair radiation(const Cell &c) { return {c[2], c[3]}; }

Pair antipodal(Kernel &kernel, const Ring &word) {
    return {kernel.intern(word), kernel.intern(scale(word, -1))};
}

Cell cell(Kernel &kernel, const RingCell &value) {
    Cell out{};
    for (unsigned lane = 0; lane < out.size(); ++lane) out[lane] = kernel.intern(value[lane]);
    return out;
}

Field previous(Kernel &kernel, Field end, unsigned bit) {
    kernel.scatter(end);
    kernel.transport(end, bit, true);
    return end;
}

unsigned collision_tag(Kernel &kernel, const Stages &step, unsigned site) {
    Cell c = step.contact[site];
    const unsigned tag = kernel.collide(c);
    require(c == step.collision[site], "collision tag agrees with complete replay");
    return tag;
}

void install(Field &field, unsigned site, const Pair &word) {
    field[site][0] = word[0];
    field[site][1] = word[1];
}

struct Arm {
    Field initial;
    Stages first;
    Stages second;
    unsigned writer_tag, reader_tag, predecessor_tag;
};

Arm prepare(Kernel &kernel, const Field &bare, unsigned x, unsigned sign) {
    const unsigned writer = 4 * x, reader = writer + 1, input = writer + 3;
    Field start = bare;
    start[6] = cell(kernel, bank);
    start[writer] = cell(kernel, writer_stock);
    start[reader] = cell(kernel, reader_stock);
    start[input] = cell(kernel, input_stock);
    if (sign) std::swap(start[input][0], start[input][1]);
    for (unsigned site : clocks) require(start[site][3] == bare[site][3], "clock CORR untouched");
    require(account(kernel, start) == published_ledger, "Q774 funded launch");
    const Stages first = audited_tick(kernel, start, 1, published_ledger);
    const Stages second = audited_tick(kernel, first.collision, 0, published_ledger);
    require(previous(kernel, previous(kernel, second.collision, 0), 1) == start,
            "two-tick native reverse");
    const Field preceding = previous(kernel, start, 0);
    require(account(kernel, preceding) == published_ledger, "inverse launch account");
    const auto precedent = audited_tick(kernel, preceding, 0, published_ledger);
    require(precedent.collision == start, "native launch predecessor");
    return {start, first, second, collision_tag(kernel, first, writer),
            collision_tag(kernel, second, reader), collision_tag(kernel, precedent, input)};
}

struct Summary {
    unsigned ready{}, words{}, both_work{}, expected{}, causal{}, nonempty_predecessor{};
    std::map<std::pair<unsigned, unsigned>, unsigned> tags;
    std::vector<unsigned> passed;
};

void check(Kernel &kernel, Summary &summary, const Field &bare, unsigned x, unsigned rank) {
    const unsigned writer = 4 * x, reader = writer + 1;
    const std::array<Arm, 2> arms{prepare(kernel, bare, x, 0), prepare(kernel, bare, x, 1)};
    const auto &a = arms[0];
    const auto &b = arms[1];
    const bool ready = a.first.collision[reader] == b.first.collision[reader]
        && radiation(a.second.contact[reader]) == radiation(b.second.contact[reader]);
    const bool both_work = std::all_of(arms.begin(), arms.end(), [reader](const Arm &arm) {
        return matter(arm.second.contact[reader]) != matter(arm.second.collision[reader]);
    });
    bool words = true;
    bool expected = a.reader_tag == 1 && b.reader_tag == 2;
    bool causal = ready && a.reader_tag != b.reader_tag && both_work;
    for (unsigned sign = 0; sign < arms.size(); ++sign) {
        const Arm &live = arms[sign];
        const Arm &other = arms[1 - sign];
        const Pair own = matter(live.first.collision[writer]);
        const Pair alternative = matter(other.first.collision[writer]);
        words &= live.writer_tag == 2 && matter(live.first.contact[writer]) != own
            && own == antipodal(kernel, writer_word[sign]);
        expected &= matter(live.second.collision[reader]) == antipodal(kernel, reader_word[sign]);
        summary.nonempty_predecessor += live.predecessor_tag != 0;
        if (own == alternative) {
            causal = false;
            continue;
        }
        Field changed = live.first.collision;
        install(changed, writer, alternative);
        if (account(kernel, changed) != published_ledger) {
            causal = false;
            continue;
        }
        const auto swapped = audited_tick(kernel, changed, 0, published_ledger);
        Field reverse = previous(kernel, swapped.collision, 0);
        require(reverse == changed, "swap reverse reaches exchanged cut");
        install(reverse, writer, own);
        require(reverse == live.first.collision && previous(kernel, reverse, 1) == live.initial,
                "swap reversal reaches original launch");
        causal &= swapped.contact[reader] == other.second.contact[reader]
            && swapped.collision[reader] == other.second.collision[reader]
            && collision_tag(kernel, swapped, reader) == other.reader_tag;
    }
    summary.ready += ready;
    summary.words += words;
    summary.both_work += both_work;
    summary.expected += expected;
    summary.causal += causal;
    ++summary.tags[{a.reader_tag, b.reader_tag}];
    if (ready && words && both_work && expected && causal) summary.passed.push_back(rank);
    if (rank == 43)
        std::cout << "raw43 x=" << x << " writer=" << a.writer_tag << '/' << b.writer_tag
                  << " reader=" << a.reader_tag << '/' << b.reader_tag
                  << " readiness=" << ready << " swap=" << causal << '\n';
}

} // namespace binary

int main() try {
    Kernel kernel;
    std::array<binary::Summary, 2> result{};
    constexpr std::array<unsigned, 2> columns{5, 7};
    for (unsigned rank = 0; rank < 85; ++rank) {
        unsigned id;
        binary::require(bool(std::cin >> id) && id == rank, "exactly 85 ordered input ranks");
        Field bare{};
        for (Cell &site : bare) {
            for (Id &lane : site) {
                Ring value{};
                for (I &coefficient : value)
                    binary::require(bool(std::cin >> coefficient), "complete bare coefficient row");
                lane = kernel.intern(value);
            }
        }
        binary::require(account(kernel, bare) == binary::bare_ledger, "initial bare Q446 account");
        for (unsigned index = 0; index < columns.size(); ++index)
            binary::check(kernel, result[index], bare, columns[index], rank);
    }
    unsigned tail;
    binary::require(!(std::cin >> tail) && std::cin.eof(), "no extra input rows");
    binary::require(result[0].passed.size() == 85, "column 5 theorem on all 85 starts");
    for (unsigned index = 0; index < result.size(); ++index) {
        const auto &s = result[index];
        std::cout << "x=" << columns[index] << " inputs=85 both_authentic=" << s.words
                  << " ready=" << s.ready << " both_material=" << s.both_work
                  << " expected_exact=" << s.expected << " causal_swap=" << s.causal
                  << " predecessor_source_active_arms=" << s.nonempty_predecessor << '\n';
        for (const auto &[tags, count] : s.tags)
            std::cout << "tags " << tags.first << '/' << tags.second << ' ' << count << '\n';
        std::cout << "passing ranks";
        for (unsigned rank : s.passed) std::cout << ' ' << rank;
        std::cout << '\n';
    }
    return 0;
} catch (const std::exception &e) {
    std::cerr << e.what() << '\n';
    return 1;
}
