// SPDX-License-Identifier: Apache-2.0
#define main predecessor_main
#include "audit.cpp"
#undef main

namespace renewal {

constexpr unsigned memory = receiver_site;
constexpr unsigned worker = 28;
constexpr unsigned first_tick = 159;

struct Occurrences {
    unsigned first{}, count{};
    bool record(unsigned tick) {
        ++count;
        if (first) return false;
        first = tick;
        return true;
    }
};

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
};

Transition advance(Kernel &kernel, Ledger &ledger, const Field &before, unsigned bit) {
    Transition next{before, {}};
    kernel.transport(next.c, bit);
    ledger.check(kernel, next.c);
    next.b = next.c;
    kernel.scatter(next.b);
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

void emit_field(const Kernel &kernel, const Field &field) {
    for (const Cell &cell : field)
        for (Id word : cell)
            for (I coefficient : kernel.value(word))
                std::cout << '\t' << coefficient;
    std::cout << '\n';
}

void witness(const Kernel &kernel, unsigned rank, unsigned tick, const char *label,
             const Field &before, const Transition &after) {
    if (rank != 43) return;
    const auto emit = [&](const char *stage, const Field &field) {
        std::cout << "WITNESS\t" << rank << '\t' << tick << '\t' << label << '\t' << stage;
        emit_field(kernel, field);
    };
    emit("pre", before);
    emit("c", after.c);
    emit("b", after.b);
}

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

bool same_radiation(const Cell &a, const Cell &b) {
    return a[2] == b[2] && a[3] == b[3];
}

void scan(Kernel &kernel, Ledger &ledger, const Key &key, const Query &query,
          const Pair &t, const Pair &w) {
    const auto [mode, rank] = key;
    if (mode != 2 || query.depth != 0)
        throw std::runtime_error("expected mode 2, depth 0 four-wire launch");

    const Field &launch = query.cut;
    const Relay predecessor = score_relay(kernel, launch, t, w);
    const bool first_expected = predecessor.source125 && predecessor.restore157 &&
        predecessor.work_tick == first_tick && predecessor.work_site == worker &&
        predecessor.work_tag == 2 && predecessor.work_offtag == 0 &&
        predecessor.paid_work_tick == first_tick;
    if (first_expected != (rank == 0 || rank == 22 || rank == 43))
        throw std::logic_error("first writer census differs from the predecessor");
    const unsigned limit = rank == 43 ? 1'048'576 : first_expected ? 65'536 : 8'192;
    Field field = launch;
    unsigned bit = 1, scanned = 0, period = 0, first_write = 0;
    unsigned source125 = 0, source_b2_after159 = 0;
    bool restored157 = false, held158 = false;
    Cell original_worker{}, original_c{};
    Occurrences renew_c, renew_b, strict_renew_b, pre_worker, radiation, ready, function;
    Occurrences word_ready, exact_work, ungated_b2;
    unsigned formation_tick = 0, formation_cut = 0;
    unsigned work_formation_tick = 0, work_formation_cut = 0;

    for (unsigned tick = 1; tick <= limit || (period && first_expected && tick <= first_tick + period); ++tick) {
        const Transition step = advance(kernel, ledger, field, bit);
        const Pair before_word = matter(field[memory]);
        const Pair c_word = matter(step.c[memory]);
        const Pair b_word = matter(step.b[memory]);
        if (tick == 125)
            source125 = project_collision(kernel, step.c[source], step.b[source]) == 2;
        if (tick == 157) {
            restored157 = c_word == t && b_word == w &&
                          project_collision(kernel, step.c[memory], step.b[memory]) == 1;
        }
        if (tick == 158) held158 = restored157 && before_word == w && c_word == w && b_word == w;
        if (tick == first_tick && first_expected && held158 && c_word != w && b_word != w &&
            functional_write(kernel, bit, field, step, t, w)) {
            first_write = tick;
            original_worker = field[worker];
            original_c = step.c[worker];
            witness(kernel, rank, tick, "first_write", field, step);
        }

        if (tick > first_tick) {
            if (step.c[source] != step.b[source] &&
                project_collision(kernel, step.c[source], step.b[source]) == 2)
                ++source_b2_after159;
            if (step.c[worker] != step.b[worker] &&
                project_collision(kernel, step.c[worker], step.b[worker]) == 2)
                ungated_b2.record(tick);
        }

        if (tick > first_tick && first_write) {
            const auto observe = [&](Occurrences &event, bool qualifies, const char *label) {
                if (qualifies && event.record(tick))
                    witness(kernel, rank, tick, label, field, step);
            };
            observe(renew_c, before_word != w && c_word == w, "renew_c");
            observe(renew_b, c_word != w && b_word == w, "renew_b");
            observe(strict_renew_b, c_word == t && b_word == w &&
                    project_collision(kernel, step.c[memory], step.b[memory]) == 1, "strict_renew_b");
            if (bit == 1) {
                const bool same_worker = field[worker] == original_worker;
                const bool same_corr = same_radiation(step.c[worker], original_c);
                observe(pre_worker, same_worker, "pre_worker");
                observe(radiation, same_corr, "radiation");
                observe(ready, same_worker && same_corr, "ready");
                const bool jointly_ready = same_worker && same_corr && before_word == w;
                observe(word_ready, jointly_ready, "word_ready");
                const bool paid_work = functional_write(kernel, bit, field, step, t, w);
                if (paid_work && !formation_tick)
                    throw std::logic_error("paid function lacks a renewed committed word");
                if (paid_work && !function.first) {
                    work_formation_tick = formation_tick;
                    work_formation_cut = formation_cut;
                }
                observe(function, paid_work, "function");
                observe(exact_work, jointly_ready && paid_work, "exact_work");
            }
        }

        if (tick > first_tick && first_write) {
            if (c_word == w && before_word != w) {
                formation_tick = tick;
                formation_cut = 1;
            } else if (c_word != w) {
                formation_tick = 0;
                formation_cut = 0;
            }
            if (b_word == w && c_word != w) {
                formation_tick = tick;
                formation_cut = 2;
            } else if (b_word != w) {
                formation_tick = 0;
                formation_cut = 0;
            }
        }

        field = step.b;
        bit ^= 1;
        scanned = tick;
        if (!period && bit == 1 && field == launch)
            period = tick;
        if (period && tick >= first_tick &&
            (!first_expected || tick >= first_tick + period))
            break;
    }
    if (bool(first_write) != first_expected)
        throw std::logic_error("first writer census differs from the predecessor");

    Field inverse = field;
    unsigned inverse_bit = bit;
    for (unsigned tick = scanned; tick != 0; --tick) {
        inverse_bit ^= 1;
        kernel.scatter(inverse);
        kernel.transport(inverse, inverse_bit, true);
    }
    if (inverse != launch || inverse_bit != 1)
        throw std::logic_error("full inverse mismatch");

    std::cout << mode << '\t' << rank << '\t' << limit << '\t' << scanned << '\t' << period
              << '\t' << first_write;
    for (const Occurrences &event : {renew_c, renew_b, strict_renew_b, pre_worker, radiation, ready, function})
        std::cout << '\t' << event.first << '\t' << event.count;
    std::cout << "\t1\t" << source125 << '\t' << source_b2_after159
              << '\t' << ungated_b2.count << '\t' << word_ready.first << '\t' << word_ready.count
              << '\t' << exact_work.first << '\t' << exact_work.count
              << '\t' << work_formation_tick << '\t' << work_formation_cut
              << '\t' << ungated_b2.first << '\n';
    std::cout << "END\t" << rank << '\t' << scanned << '\t' << bit;
    emit_field(kernel, field);
}

} // namespace renewal

int main(int argc, char **argv) try {
    if (argc > 2) throw std::runtime_error("usage: renew [query-text-file]");
    std::ifstream file;
    if (argc == 2) {
        file.open(argv[1]);
        if (!file) throw std::runtime_error("cannot open query file");
    }
    Kernel kernel;
    renewal::Ledger ledger;
    const Queries queries = read_queries(kernel, argc == 2 ? file : std::cin);
    if (queries.size() != rank_count)
        throw std::runtime_error("expected all 85 four-wire launches");
    const Pair t{kernel.intern(t_word), kernel.intern(scale(t_word, -1))};
    const Pair w{kernel.intern(w_word), kernel.intern(scale(w_word, -1))};
    std::cout << "mode\trank\tlimit\tscanned\tperiod\tfirst_write"
                 "\trenew_c\trenew_c_count\trenew_b\trenew_b_count"
                 "\tstrict_renew_b\tstrict_renew_b_count\tpre_worker\tpre_worker_count"
                 "\tradiation\tradiation_count\tready\tready_count\tfunction\tfunction_count\tinverse"
                 "\tsource125\tsource_b2_after159\tworker_b2_after159"
                 "\tword_ready\tword_ready_count\texact_work\texact_work_count"
                 "\twork_formation_tick\twork_formation_cut\tfirst_ungated_b2_after159\n";
    for (const auto &[key, query] : queries)
        renewal::scan(kernel, ledger, key, query, t, w);
    if (!std::cout) throw std::runtime_error("failed writing renewal records");
    return 0;
} catch (const std::exception &error) {
    std::cerr << error.what() << '\n';
    return 2;
}
