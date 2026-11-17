// SPDX-License-Identifier: Apache-2.0
// Four-coefficient native kernel and stock from the preceding head-pulse probe.
#include <array>
#include <algorithm>
#include <map>
#include <cstdint>
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
std::ostream &operator<<(std::ostream &o,const Ring &a) {
    return o<<'('<<a[0]<<','<<a[1]<<','<<a[2]<<','<<a[3]<<')';
}
Field bare_seed(Kernel &k) {
    Field f{};
    const Ring rho2=mul(rho,rho);
    const Ring d=add(add(Ring{2},rho),rho2);
    const Ring k0=add(J,rho2,-1);
    const Ring stash=add(k0,scale(mul(mul(rho,J),d),2),-1);
    for(unsigned y=0;y<4;++y) {
        f[y]={k.intern(scale(J,2)),k.intern(scale(J,-2)),k.intern(one),
              k.intern(y<2?Ring{-3}:stash)};
    }
    for(unsigned y=0;y<2;++y) {
        f[4+y][3]=k.intern(Ring{-3});
        f[8+y][3]=k.intern(Ring{5});
    }
    return f;
}

constexpr unsigned head = 4, receiver = 5, helper = 6, matter_helper = 7, bridge_site = 29;
constexpr Ring bridge_stock{3,4,4,8};
constexpr Ring head_clk{0,2,-1,1}, receiver_clk{-2,0,-1,0}, helper_clk{0,-1,-1,0};

Field reference(Kernel &k, Field f, bool bridge) {
    if (bridge) f[bridge_site][3] = k.intern(add(k.value(f[bridge_site][3]), bridge_stock));
    return f;
}

Field stock(Kernel &k, Field f, bool support, bool material_support) {
    const Ring D{1,-1,-1,1}, g=mul(J,D);
    f[head]={k.intern(D),k.intern(scale(D,-1)),k.intern(head_clk),f[head][3]};
    f[receiver]={k.intern(scale(g,-3)),k.intern(scale(g,-1)),
                 k.intern(receiver_clk),f[receiver][3]};
    if (support) f[helper][2]=k.intern(helper_clk);
    if (material_support) f[matter_helper][0]=k.intern({-1,0,-1,0});
    return f;
}

enum class Mode { Baseline, IngressActive, IngressSham, DelayedActive, DelayedSham };

const std::map<std::string, Mode> modes{
    {"baseline", Mode::Baseline},
    {"ingress_active", Mode::IngressActive}, {"ingress_sham", Mode::IngressSham},
    {"delayed_active", Mode::DelayedActive}, {"delayed_sham", Mode::DelayedSham}
};

Field prepared(Kernel &k, const Field &bare, Mode mode) {
    Field f = stock(k, reference(k, bare, true), true, true);
    if (mode == Mode::IngressActive || mode == Mode::IngressSham) {
        const I sign = mode == Mode::IngressActive ? 1 : -1;
        f[matter_helper][1] = k.intern(add(k.value(f[matter_helper][1]), scale(Ring{4,2,3,1}, sign)));
        constexpr Ring corr_stock{0,-2,-2,0};
        for (unsigned site : {matter_helper, matter_helper + 4}) {
            f[site][3] = k.intern(add(k.value(f[site][3]), corr_stock));
        }
    }
    if (mode == Mode::DelayedActive || mode == Mode::DelayedSham) {
        const I sign = mode == Mode::DelayedActive ? 1 : -1;
        f[helper][0] = k.intern(add(k.value(f[helper][0]), scale(Ring{3,-1,-1,1}, sign)));
    }
    return f;
}

std::array<Ring,3> account(Kernel &k,const Field &f) {
    std::array<Ring,3> out{};
    for(const auto &cell:f) for(unsigned lane=0;lane<4;++lane) {
        const Ring a=k.value(cell[lane]);
        out[lane/2]=add(out[lane/2],a);
        out[2]=add(out[2],norm(a));
    }
    return out;
}

using Tick=std::uint64_t;
constexpr Tick limit=1'000'000;
constexpr Tick audit_stride=4096;
constexpr std::array<unsigned,2> labels{44,4};
constexpr std::array<unsigned,2> predecessor_ticks{73,189};

std::array<Field,622> bare_reference(Kernel &k) {
    Field bare=bare_seed(k);
    const Field initial=bare;
    const auto ledger=account(k,bare);
    std::array<Field,622> cuts{};
    for(unsigned n=0;n<cuts.size();++n) {
        cuts[n]=bare;
        k.transport(bare,n%2);
        if(account(k,bare)!=ledger) throw std::logic_error("bare transport ledger");
        k.scatter(bare);
        if(account(k,bare)!=ledger) throw std::logic_error("bare collision ledger");
        if(n%2 && bare==initial && n!=621) throw std::logic_error("early bare return");
    }
    if(bare!=initial) throw std::logic_error("missing bare return");
    return cuts;
}

unsigned raw_predecessor(Kernel &k,const std::array<Field,622> &bare,unsigned rank) {
    Field ready=bare_seed(k);
    Id left=ready[0][3], middle=ready[4][3], right=ready[8][3];
    for(unsigned r=0; r<rank; ++r) {
        k.contact(left,middle,false);
        k.contact(middle,right,false);
    }
    for(unsigned y=0; y<2; ++y) {
        ready[y][3]=left;
        ready[4+y][3]=middle;
        ready[8+y][3]=right;
    }
    unsigned offset=0;
    bool found=false;
    for(unsigned tick=2; tick<=bare.size(); tick+=2) {
        if(bare[tick%bare.size()]!=ready) continue;
        if(found) throw std::logic_error("duplicate raw ready cut");
        found=true;
        offset=tick-1;
    }
    if(!found) throw std::logic_error("missing raw ready cut");
    return offset;
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

struct Contrast {
    unsigned tick = 0;
    bool isolated = false;
    bool hit = false;
    bool survives = false;
    bool retains = false;
    int donor = -1;
    bool local_equal = false;
    bool donor_differs = false;
    bool matter_equal = false;
    bool first_three_equal = false;
    bool radiation_echo = false;
    unsigned conversion_tick = 0;
    unsigned conversion_left_tag = 0;
    unsigned conversion_right_tag = 0;
    bool conversion_left_moves = false;
    bool conversion_right_moves = false;
    bool conversion_survives = false;
    bool conversion_retains = false;
    Pair conversion_words{};
};

constexpr unsigned target = 7;
constexpr unsigned row_width = 4;
constexpr unsigned horizon = 64;
constexpr unsigned conversion_window = 4;
constexpr unsigned full_horizon = horizon + conversion_window + 1;
constexpr Ring launch_vector{0, -1, 1, 0};
constexpr std::array<std::array<unsigned, 2>, 3> comparisons{{{0, 2}, {1, 2}, {0, 1}}};
constexpr std::array<const char *, 3> comparison_names{"plus_zero", "minus_zero", "plus_minus"};

void audit_launch(Kernel &kernel, const Field &base, unsigned rank,
                  unsigned distance) {
    const unsigned site = row_width * ((1 + distance) % 8) + 3;
    std::array<Field, 3> states{base, base, base};
    std::array<std::array<Ring, 3>, 3> ledgers{};
    constexpr std::array<int, 3> signs{1, -1, 0};
    const auto base_ledger = account(kernel, base);
    for (unsigned arm = 0; arm < states.size(); ++arm) {
        states[arm][site][3] = kernel.intern(
            add(kernel.value(base[site][3]), scale(launch_vector, 16 * signs[arm])));
        ledgers[arm] = account(kernel, states[arm]);
        const Ring stock = scale(launch_vector, 16 * signs[arm]);
        const std::array<Ring, 3> expected{
            base_ledger[0], add(base_ledger[1], stock), add(base_ledger[2], norm(stock))};
        if (ledgers[arm] != expected)
            throw std::logic_error("launch ledger mismatch");
    }
    if (ledgers[0][2] != ledgers[1][2])
        throw std::logic_error("opposed launch energies differ");

    std::array<Contrast, 3> results{};
    std::array<Pair, 3> words{};
    for (unsigned tick = 1; tick <= full_horizon; ++tick) {
        const unsigned bit = tick % 2;
        const unsigned donor_x = bit ? 2 : 0;
        const unsigned donor_site = row_width * donor_x + 3;
        std::array<Stages, 3> cuts{};
        for (unsigned arm = 0; arm < states.size(); ++arm)
            cuts[arm] = audited_tick(kernel, states[arm], bit, ledgers[arm]);

        for (unsigned index = 0; index < comparisons.size(); ++index) {
            const auto [left, right] = comparisons[index];
            auto &result = results[index];
            const Cell &before_l = states[left][target];
            const Cell &before_r = states[right][target];
            const Cell &c_l = cuts[left].contact[target];
            const Cell &c_r = cuts[right].contact[target];
            const Cell &b_l = cuts[left].collision[target];
            const Cell &b_r = cuts[right].collision[target];

            if (result.hit && tick == result.tick + 1) {
                result.survives = c_l[0] != c_r[0] && b_l[0] != b_r[0];
                result.retains = Pair{c_l[0], c_r[0]} == words[index] &&
                                 Pair{b_l[0], b_r[0]} == words[index];
            }
            const bool radiation_differs = c_l[3] != c_r[3];
            const bool matter_equal = c_l[0] == c_r[0] && c_l[1] == c_r[1];
            const bool first_three_equal = matter_equal && c_l[2] == c_r[2];
            if (result.tick && tick == result.tick + 1)
                result.radiation_echo = radiation_differs && b_l[3] != b_r[3];

            if (!result.tick && tick <= horizon && radiation_differs) {
                result.tick = tick;
                result.donor = donor_x;
                result.local_equal = before_l == before_r;
                result.donor_differs = states[left][donor_site][3] != states[right][donor_site][3];
                result.matter_equal = matter_equal;
                result.first_three_equal = first_three_equal;
                result.isolated = result.local_equal && result.donor_differs && first_three_equal;
                result.hit = result.isolated && b_l[0] != b_r[0];
                if (result.hit) words[index] = {b_l[0], b_r[0]};
            }

            if (result.conversion_tick && tick == result.conversion_tick + 1) {
                result.conversion_survives = c_l[0] != c_r[0] && b_l[0] != b_r[0];
                result.conversion_retains = Pair{c_l[0], c_r[0]} == result.conversion_words &&
                                            Pair{b_l[0], b_r[0]} == result.conversion_words;
            }
            if (!result.conversion_tick && result.tick && tick <= result.tick + conversion_window &&
                first_three_equal && radiation_differs && b_l[0] != b_r[0]) {
                result.conversion_tick = tick;
                Cell local_l = c_l;
                Cell local_r = c_r;
                result.conversion_left_tag = kernel.collide(local_l);
                result.conversion_right_tag = kernel.collide(local_r);
                if (local_l != b_l || local_r != b_r)
                    throw std::logic_error("local conversion disagrees with full B");
                result.conversion_left_moves = b_l[0] != c_l[0];
                result.conversion_right_moves = b_r[0] != c_r[0];
                result.conversion_words = {b_l[0], b_r[0]};
            }
        }
        for (unsigned arm = 0; arm < states.size(); ++arm)
            states[arm] = cuts[arm].collision;
    }

    for (unsigned index = 0; index < comparisons.size(); ++index) {
        const auto &r = results[index];
        std::cout << rank << '\t' << distance << '\t' << comparison_names[index] << '\t'
                  << r.tick << '\t' << r.donor << '\t' << r.local_equal << '\t'
                  << r.donor_differs << '\t' << r.matter_equal << '\t' << r.first_three_equal << '\t'
                  << r.isolated << '\t' << r.hit << '\t' << r.survives << '\t' << r.retains << '\t'
                  << r.radiation_echo << '\t' << r.conversion_tick << '\t'
                  << r.conversion_left_tag << '\t' << r.conversion_right_tag << '\t'
                  << r.conversion_left_moves << '\t' << r.conversion_right_moves << '\t'
                  << r.conversion_survives << '\t' << r.conversion_retains << '\n';
    }
}

int main() try {
    Kernel kernel;
    const auto bare = bare_reference(kernel);
    std::cout << "rank\tdistance\tcomparison\tfirst_tick\tdonor_x\tlocal_equal\t"
                 "donor_differs\tmatter_equal\tfirst_three_equal\tisolated\thit\tsurvives\tretains\t"
                 "radiation_echo\tconversion_tick\tconversion_left_tag\tconversion_right_tag\t"
                 "conversion_left_moves\tconversion_right_moves\tconversion_survives\tconversion_retains\n";
    for (unsigned rank = 0; rank <= 84; ++rank) {
        const unsigned offset = raw_predecessor(kernel, bare, rank);
        if (offset % 2 != 1) throw std::logic_error("raw predecessor bit mismatch");
        const Field base = prepared(kernel, bare[offset], Mode::IngressActive);
        for (unsigned distance = 1; distance <= 4; ++distance)
            audit_launch(kernel, base, rank, distance);
    }
} catch (const std::exception &error) {
    std::cerr << error.what() << '\n';
    return 2;
}
