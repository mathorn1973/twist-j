// SPDX-License-Identifier: Apache-2.0
// Four-coefficient native kernel from P-H3-FUNDED-RECEIVER-1 (0b69d975fe1386b1a5f457997ebd620187574206).
#include <array>
#include <algorithm>
#include <map>
#include <limits>
#include <cstdint>
#include <fstream>
#include <sstream>
#include <iostream>
#include <stdexcept>
#include <string>
#include <unordered_map>
#include <vector>

using I = std::int64_t;
using W = __int128_t;
using Id = std::uint32_t;
using Ring = std::array<I, 4>;
using Cell = std::array<Id, 4>;
using Field = std::array<Cell, 32>;
using Pair = std::array<Id, 2>;
constexpr Ring zero{}, one{1}, rho{0,0,1}, J{1,0,1}, invJ{0,-1,-1};
constexpr I coefficient_bound = I{1} << 29;

I checked(W x) {
    if (x < -coefficient_bound || x > coefficient_bound)
        throw std::overflow_error("checked ring-coefficient bound exceeded");
    return static_cast<I>(x);
}
Ring add(Ring a, Ring b, I sign=1) {
    for (size_t i=0; i<4; ++i) a[i]=checked(W(a[i])+W(sign)*b[i]);
    return a;
}
Ring scale(Ring a, I m) {
    for (auto &x:a) x=checked(W(x)*m);
    return a;
}
Ring mul(const Ring &a, const Ring &b) {
    std::array<W,5> c{};
    for(size_t i=0; i<4; ++i)
        for(size_t q=0; q<4; ++q) c[(i+q)%5]+=W(a[i])*b[q];
    return {checked(c[0]-c[4]),checked(c[1]-c[4]),
            checked(c[2]-c[4]),checked(c[3]-c[4])};
}
Ring norm(const Ring &a) {
    return mul(a, {checked(W(a[0])-a[1]), -a[1], checked(W(a[3])-a[1]), checked(W(a[2])-a[1])});
}
Ring half(Ring a) {
    for(auto &x:a) {
        if(x%2) throw std::logic_error("nonintegral half-gap");
        x/=2;
    }
    return a;
}

using RingPair = std::array<Ring, 2>;
using RingCell = std::array<Ring, 4>;

RingPair native_contact(const RingPair &in, bool inverse) {
    const Ring gap = half(add(in[0], in[1], -1));
    const Ring midpoint = half(add(in[0], in[1]));
    const Ring rotated = mul(gap, inverse ? Ring{0, 0, 0, 1} : rho);
    return {add(midpoint, rotated), add(midpoint, rotated, -1)};
}

bool integral_pair(const Ring &a, const Ring &b) {
    for (unsigned i = 0; i < a.size(); ++i) {
        if ((a[i] - b[i]) % 2) return false;
    }
    return true;
}

std::pair<RingCell, unsigned> native_collision(const RingCell &in) {
    if (in[0] == in[1] || in[2] == in[3] ||
        !integral_pair(in[0], in[1]) || !integral_pair(in[2], in[3])) return {in, 0};

    Ring d = half(add(in[0], in[1], -1));
    Ring f = half(add(in[2], in[3], -1));
    const Ring hd = norm(d), hf = norm(f);
    static const Ring theta = norm(J);
    const unsigned tag = hf == mul(theta, hd) ? 1 : hd == mul(theta, hf) ? 2 : 0;
    if (!tag) return {in, 0};

    const Ring m = half(add(in[0], in[1]));
    const Ring n = half(add(in[2], in[3]));
    d = mul(d, tag == 1 ? J : invJ);
    f = mul(f, tag == 1 ? invJ : J);
    return {{add(m, d), add(m, d, -1), add(n, f), add(n, f, -1)}, tag};
}

template<std::size_t size>
Ring hermitian_account(const std::array<Ring, size> &a) {
    Ring sum{};
    for (const Ring &v : a) sum = add(sum, norm(v));
    return sum;
}

struct Hash {
    template<class T,size_t n> size_t operator()(const std::array<T,n>& a) const noexcept {
        std::uint64_t h=0x9e3779b97f4a7c15ULL;
        for(auto x:a) {
            h^=static_cast<std::uint64_t>(x)+0x9e3779b97f4a7c15ULL+(h<<6)+(h>>2);
        }
        return h;
    }
};
struct Entry {
    Ring value;
    unsigned parity;
};
class Kernel {
    std::vector<Entry> values;
    std::unordered_map<Ring,Id,Hash> ids;
    std::array<std::unordered_map<Pair,Pair,Hash>,2> contact_cache;
    std::unordered_map<Cell,std::pair<Cell,unsigned>,Hash> collision_cache;
    std::array<std::array<std::array<unsigned,2>,16>,2> rows{}, columns{};
public:
    explicit Kernel() {
        intern(zero);
        for(unsigned b=0; b<2; ++b) {
            unsigned ix=0;
            for(unsigned x=0; x<8; ++x)
                for(unsigned y=b; y<4; y+=2) rows[b][ix++]={4*x+y,4*x+(y+1)%4};
            ix=0;
            for(unsigned x=b; x<8; x+=2)
                for(unsigned y=0; y<4; ++y) columns[b][ix++]={4*x+y,4*((x+1)%8)+y};
        }
    }
    Id intern(const Ring &a) {
        auto it=ids.find(a);
        if(it!=ids.end()) return it->second;
        if(values.size()>=2'000'000) throw std::overflow_error("exact ring capacity limit reached");
        unsigned parity=0;
        for(size_t x=0; x<4; ++x) parity|=(static_cast<unsigned>(a[x])&1u)<<x;
        Id id=static_cast<Id>(values.size());
        values.push_back({a,parity});
        ids.emplace(a,id);
        return id;
    }
    const Ring &value(Id id) const {return values[id].value;}
    void contact(Id &a, Id &b, bool inverse) {
        if(a==b || values[a].parity!=values[b].parity) return;
        const bool reversed=a>b;
        Pair key=reversed?Pair{b,a}:Pair{a,b};
        auto &cache=contact_cache[inverse];
        auto it=cache.find(key);
        if(it==cache.end()) {
            const RingPair in{value(key[0]), value(key[1])};
            const RingPair mapped = native_contact(in, inverse);
            if (add(in[0], in[1]) != add(mapped[0], mapped[1]) ||
                hermitian_account(in) != hermitian_account(mapped)) {
                throw std::logic_error("contact conservation mismatch");
            }
            if (!integral_pair(mapped[0], mapped[1]) ||
                native_contact(mapped, !inverse) != in) {
                throw std::logic_error("contact inverse mismatch");
            }
            const Pair out{intern(mapped[0]), intern(mapped[1])};
            if(cache.size()>=500'000) cache.clear();
            it=cache.emplace(key,out).first;
        }
        a=it->second[reversed]; b=it->second[!reversed];
    }
    unsigned collide(Cell &a) {
        if(a[0]==a[1] || a[2]==a[3] || values[a[0]].parity!=values[a[1]].parity ||
            values[a[2]].parity!=values[a[3]].parity) return 0;
        if(collision_cache.size()>=500'000) collision_cache.clear();
        auto it=collision_cache.find(a);
        if(it!=collision_cache.end()) {
            a=it->second.first;
            return it->second.second;
        }
        const RingCell in{value(a[0]), value(a[1]), value(a[2]), value(a[3])};
        const auto [mapped, tag] = native_collision(in);
        Cell out = a;
        if (tag) {
            if (add(in[0], in[1]) != add(mapped[0], mapped[1]) ||
                add(in[2], in[3]) != add(mapped[2], mapped[3]) ||
                hermitian_account(in) != hermitian_account(mapped)) {
                throw std::logic_error("collision conservation mismatch");
            }
            const auto [recovered, inverse_tag] = native_collision(mapped);
            if (recovered != in || inverse_tag != 3 - tag) {
                throw std::logic_error("collision inverse mismatch");
            }
            for (unsigned lane = 0; lane < out.size(); ++lane) out[lane] = intern(mapped[lane]);
        }
        collision_cache.emplace(a,std::pair{out,tag});
        a=out;
        return tag;
    }
    void transport(Field &f,unsigned b,bool inverse=false) {
        for(auto [i,j]:rows[b]) for(unsigned lane=0;lane<3;++lane)
            contact(f[i][lane],f[j][lane],inverse);
        for(auto [i,j]:columns[b]) contact(f[i][3],f[j][3],inverse);
    }
    unsigned scatter(Field &f) {
        unsigned head_tag=0;
        for(unsigned site=0;site<f.size();++site) {
            const auto tag=collide(f[site]);
            if(site==4) head_tag=tag;
        }
        return head_tag;
    }

};
std::array<Ring,3> account(Kernel &k,const Field &f) {
    std::array<Ring,3> out{};
    for(const auto &cell:f) for(unsigned lane=0;lane<4;++lane) {
        const Ring a=k.value(cell[lane]);
        out[lane/2]=add(out[lane/2],a);
        out[2]=add(out[2],norm(a));
    }
    return out;
}

struct Stages {
    Field contact;
    Field collision;
    unsigned head_tag;
};

Stages audited_tick(Kernel &kernel, const Field &before, unsigned bit,
                    const std::array<Ring, 3> &ledger) {
    Field contact = before;
    kernel.transport(contact, bit);
    if (account(kernel, contact) != ledger)
        throw std::logic_error("forward C ledger mismatch");

    Field collision = contact;
    unsigned head_tag = kernel.scatter(collision);
    if (account(kernel, collision) != ledger)
        throw std::logic_error("forward B ledger mismatch");

    Field inverse = collision;
    kernel.scatter(inverse);
    if (inverse != contact)
        throw std::logic_error("full inverse B mismatch");
    kernel.transport(inverse, bit, true);
    if (inverse != before)
        throw std::logic_error("full inverse C mismatch");
    return {contact, collision, head_tag};
}


constexpr unsigned source = 7;
constexpr unsigned receiver_site = 31;
constexpr unsigned rank_count = 85;
constexpr unsigned height = 4, width = 8, corr = 3;

constexpr std::array<Ring, 3> published_ledger{{
    {-9, 2, -2, -3}, {19, 7, 5, 19}, {463, 0, 152, 152}
}};

Pair matter(const Cell &cell) {
    return {cell[0], cell[1]};
}

bool first_three_equal(const Cell &a, const Cell &b) {
    return a[0] == b[0] && a[1] == b[1] && a[2] == b[2];
}


constexpr unsigned emission_tick = 125, restoration_tick = 157, last_tick = 164;
constexpr Ring t_word{1, 1, 1, 1}, w_word{1, 0, 1, 1};
using Timeline = std::array<Stages, last_tick + 1>;

struct Relay {
    unsigned source125{}, restore157{}, first_local{}, read_tick{}, inhibit_tick{};
    unsigned work_tick{}, work_site{}, work_tag{}, work_offtag{}, escrow_tick{};
    unsigned retained_read_tick{}, retained_work_tick{};
    unsigned paid_effect_tick{}, paid_work_tick{};
};

unsigned project_collision(Kernel &kernel, const Cell &pre, const Cell &post) {
    Cell projection = pre;
    const unsigned tag = kernel.collide(projection);
    if (projection != post) throw std::logic_error("local B projection mismatch");
    return tag;
}

Cell hybrid_transport(Kernel &kernel, const Field &before, const Cell &after,
                      unsigned worker, unsigned bit, const Pair &replacement) {
    Cell result = after;
    Pair producer = replacement;
    for (unsigned rail = 0; rail < replacement.size(); ++rail) {
        result[rail] = before[worker][rail];
        if (worker % height % 2 == bit)
            kernel.contact(result[rail], producer[rail], false);
        else
            kernel.contact(producer[rail], result[rail], false);
    }
    return result;
}

bool check_escrow(Kernel &kernel, const Field &before, unsigned worker, unsigned bit,
                  const Pair &replacement, const Cell &hybrid_c, const Cell &hybrid_b) {
    for (unsigned site = 0; site < before.size(); ++site) {
        if (site / height == receiver_site / height || matter(before[site]) != replacement)
            continue;

        Field swapped = before;
        for (unsigned rail = 0; rail < replacement.size(); ++rail)
            std::swap(swapped[site][rail], swapped[receiver_site][rail]);
        if (account(kernel, swapped) != published_ledger)
            throw std::logic_error("escrow swap ledger mismatch");

        const Stages restored = audited_tick(kernel, swapped, bit, published_ledger);
        if (restored.contact[worker] != hybrid_c || restored.collision[worker] != hybrid_b)
            throw std::logic_error("escrow worker projection mismatch");

        Field inverse = restored.collision;
        kernel.scatter(inverse);
        kernel.transport(inverse, bit, true);
        for (unsigned rail = 0; rail < replacement.size(); ++rail)
            std::swap(inverse[site][rail], inverse[receiver_site][rail]);
        if (inverse != before)
            throw std::logic_error("escrow inverse swap mismatch");
        return true;
    }
    return false;
}

Relay score_relay(Kernel &kernel, const Field &launch, const Pair &unrestored,
                  const Pair &restored) {
    Relay result;
    Timeline live{};
    live[0].collision = launch;
    for (unsigned tick = 1; tick <= last_tick; ++tick)
        live[tick] = audited_tick(kernel, live[tick - 1].collision, tick % 2, published_ledger);

    const Stages &emission = live[emission_tick];
    if (project_collision(kernel, emission.contact[source], emission.collision[source]) != 2)
        return result;
    result.source125 = 1;
    Cell undone = emission.collision[source];
    if (kernel.collide(undone) != 1 || undone != emission.contact[source] ||
        undone[corr] == emission.collision[source][corr])
        throw std::logic_error("source B2 undo mismatch");

    Timeline off{};
    off[emission_tick].collision = emission.collision;
    off[emission_tick].collision[source] = undone;
    if (account(kernel, off[emission_tick].collision) != published_ledger)
        throw std::logic_error("source undo ledger mismatch");
    for (unsigned tick = emission_tick + 1; tick <= last_tick; ++tick)
        off[tick] = audited_tick(kernel, off[tick - 1].collision, tick % 2, published_ledger);

    const Cell &live_memory_c = live[restoration_tick].contact[receiver_site];
    const Cell &live_memory_b = live[restoration_tick].collision[receiver_site];
    const Cell &off_memory_c = off[restoration_tick].contact[receiver_site];
    const Cell &off_memory_b = off[restoration_tick].collision[receiver_site];
    if (matter(live_memory_c) != unrestored || matter(live_memory_b) != restored ||
        !first_three_equal(live_memory_c, off_memory_c) ||
        live_memory_c[corr] == off_memory_c[corr] || off_memory_c != off_memory_b ||
        project_collision(kernel, live_memory_c, live_memory_b) != 1 ||
        project_collision(kernel, off_memory_c, off_memory_b) != 0)
        return result;
    result.restore157 = 1;

    result.first_local = 1;
    for (unsigned tick = emission_tick + 1; tick < restoration_tick; ++tick) {
        if (live[tick].contact[receiver_site] != off[tick].contact[receiver_site] ||
            live[tick].collision[receiver_site] != off[tick].collision[receiver_site]) {
            result.first_local = 0;
            break;
        }
    }

    for (unsigned tick = restoration_tick + 1; tick <= last_tick; ++tick) {
        const unsigned worker = tick % 2 ? 28 : 30;
        const Field &live_pre = live[tick - 1].collision;
        const Field &off_pre = off[tick - 1].collision;
        const Cell &live_c = live[tick].contact[worker];
        const Cell &off_c = off[tick].contact[worker];
        const Cell &live_b = live[tick].collision[worker];
        const Cell &off_b = off[tick].collision[worker];
        const Cell hybrid_c = hybrid_transport(kernel, live_pre, live_c, worker, tick % 2, unrestored);
        Cell hybrid_b = hybrid_c;
        const unsigned hybrid_tag = kernel.collide(hybrid_b);
        const Pair before = matter(live_pre[worker]);
        const bool read = matter(live_c) != before;
        const bool differs = matter(live_c) != matter(hybrid_c);
        const bool escrow = differs && (read || matter(hybrid_c) != before) &&
                            check_escrow(kernel, live_pre, worker, tick % 2,
                                         unrestored, hybrid_c, hybrid_b);
        if (escrow) {
            if (!result.paid_effect_tick) result.paid_effect_tick = tick;
            const unsigned live_tag = project_collision(kernel, live_c, live_b);
            if (!result.paid_work_tick && matter(live_b) != matter(live_c) &&
                matter(live_b) != matter(hybrid_b) && live_tag && live_tag != hybrid_tag)
                result.paid_work_tick = tick;
        }

        if (differs && matter(off_pre[receiver_site]) == unrestored &&
            live_pre[worker] == off_pre[worker] && live_c[2] == off_c[2] &&
            live_c[3] == off_c[3]) {
            if (matter(hybrid_c) == matter(off_c) && matter(hybrid_b) == matter(off_b)) {
                const bool inhibit = !read && matter(off_c) != before;
                if (!read && !inhibit) throw std::logic_error("unclassified C contrast");
                if (read && !result.read_tick) result.read_tick = tick;
                if (inhibit && !result.inhibit_tick) result.inhibit_tick = tick;
                if (tick >= restoration_tick + 2 && !result.retained_read_tick)
                    result.retained_read_tick = tick;

                const unsigned live_tag = project_collision(kernel, live_c, live_b);
                const unsigned off_tag = project_collision(kernel, off_c, off_b);
                if (matter(live_c) != matter(live_b) && matter(live_b) != matter(off_b) &&
                    live_tag != off_tag && off_tag == hybrid_tag) {
                    if (!result.work_tick) {
                        result.work_tick = tick;
                        result.work_site = worker;
                        result.work_tag = live_tag;
                        result.work_offtag = off_tag;
                    }
                    if (tick >= restoration_tick + 2 && !result.retained_work_tick)
                        result.retained_work_tick = tick;
                }

                if (!result.escrow_tick && escrow) result.escrow_tick = tick;
            }
        }
        if (matter(live[tick].contact[receiver_site]) != restored ||
            matter(live[tick].collision[receiver_site]) != restored)
            break;
    }
    return result;
}

struct Query {
    unsigned depth;
    Field cut;
};

using Key = std::pair<int, unsigned>;
using Queries = std::map<Key, Query>;

Queries read_queries(Kernel &kernel, std::istream &in) {
    Queries queries;
    std::string line;
    while (std::getline(in, line)) {
        std::istringstream record(line);
        int mode;
        unsigned rank;
        I depth;
        if (!(record >> mode >> rank >> depth) || mode < 0 || rank >= rank_count ||
            depth < 0 || depth > std::numeric_limits<unsigned>::max())
            throw std::runtime_error("invalid mode, rank, or depth in query record");
        const auto [entry, fresh] =
            queries.emplace(Key{mode, rank}, Query{static_cast<unsigned>(depth), {}});
        if (!fresh) throw std::runtime_error("duplicate query record");

        Field &field = entry->second.cut;
        for (auto &cell : field) {
            for (auto &lane : cell) {
                Ring value{};
                for (I &component : value) {
                    if (!(record >> component))
                        throw std::runtime_error("truncated or invalid query coefficients");
                    component = checked(component);
                }
                lane = kernel.intern(value);
            }
        }
        std::string extra;
        if (record >> extra) throw std::runtime_error("trailing data in query record");
        if (account(kernel, field) != published_ledger)
            throw std::logic_error("Q774 ledger mismatch in query record");
    }
    if (!in.eof()) throw std::runtime_error("failed reading query file");
    if (queries.empty()) throw std::runtime_error("no query records");
    return queries;
}

Field reconstruct_launch(Kernel &kernel, const Query &query) {
    Field launch = query.cut;
    for (unsigned tick = query.depth; tick != 0; --tick) {
        Field restored_c = launch;
        kernel.scatter(restored_c);
        if (account(kernel, restored_c) != published_ledger)
            throw std::logic_error("query inverse B ledger mismatch");
        Field restored_pre = restored_c;
        kernel.transport(restored_pre, tick % 2, true);
        if (account(kernel, restored_pre) != published_ledger)
            throw std::logic_error("query inverse C ledger mismatch");
        const Stages checked = audited_tick(kernel, restored_pre, tick % 2, published_ledger);
        if (checked.contact != restored_c || checked.collision != launch)
            throw std::logic_error("query inverse step round-trip mismatch");
        launch = restored_pre;
    }

    Field replay = launch;
    for (unsigned age = 0; age < query.depth; ++age)
        replay = audited_tick(kernel, replay, (age + 1) % 2, published_ledger).collision;
    if (replay != query.cut)
        throw std::logic_error("query depth readback mismatch");
    return launch;
}

void emit_launch(const Kernel &kernel, const Key &key, const Field &launch) {
    std::cout << key.first << '\t' << key.second;
    for (const auto &cell : launch) {
        for (const auto lane : cell) {
            for (const I component : kernel.value(lane))
                std::cout << '\t' << component;
        }
    }
    std::cout << '\n';
}

int main(int argc, char **argv) try {
    const bool launch_only = argc > 1 && std::string(argv[1]) == "--launch";
    const int file_arg = launch_only ? 2 : 1;
    if (argc > file_arg + 1)
        throw std::runtime_error("usage: relay_audit [--launch] [query-text-file]");
    std::ifstream file;
    if (argc > file_arg) {
        file.open(argv[file_arg]);
        if (!file) throw std::runtime_error("cannot open query file");
    }
    Kernel kernel;
    const auto queries = read_queries(kernel, argc > file_arg ? file : std::cin);
    const Pair unrestored{kernel.intern(t_word), kernel.intern(scale(t_word, -1))};
    const Pair restored{kernel.intern(w_word), kernel.intern(scale(w_word, -1))};

    if (!launch_only) {
        std::cout << "mode\trank\tsource125\trestore157\tfirst_local\tread_tick\tinhibit_tick"
                     "\twork_tick\twork_site\twork_tag\twork_offtag\tescrow_tick"
                     "\tretained_read_tick\tretained_work_tick\tpaid_effect_tick\tpaid_work_tick\n";
    }
    // Both formats emit exactly one data row per query, in ascending (mode, rank) order.
    for (const auto &[key, query] : queries) {
        const Field launch = reconstruct_launch(kernel, query);
        if (launch_only) {
            emit_launch(kernel, key, launch);
            continue;
        }
        const Relay r = score_relay(kernel, launch, unrestored, restored);
        std::cout << key.first << '\t' << key.second << '\t' << r.source125 << '\t' << r.restore157
                  << '\t' << r.first_local << '\t' << r.read_tick << '\t' << r.inhibit_tick
                  << '\t' << r.work_tick << '\t' << r.work_site << '\t' << r.work_tag
                  << '\t' << r.work_offtag << '\t' << r.escrow_tick
                  << '\t' << r.retained_read_tick << '\t' << r.retained_work_tick
                  << '\t' << r.paid_effect_tick << '\t' << r.paid_work_tick << '\n';
    }
    if (!std::cout) throw std::runtime_error("failed writing relay records");
    return 0;
} catch (const std::exception &error) {
    std::cerr << error.what() << '\n';
    return 2;
}
