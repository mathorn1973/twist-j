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

constexpr unsigned source = 7;
constexpr int width = 8;
constexpr unsigned height = 4, corr = 3;
constexpr unsigned window = 128, horizon = 64, follow = horizon + 1;
constexpr std::array<Ring, 3> published_ledger{{
    {-9, 2, -2, -3}, {19, 7, 5, 19}, {463, 0, 152, 152}
}};

unsigned site(int x, unsigned y) {
    return static_cast<unsigned>((x + width) % width) * height + y;
}

Pair matter(const Cell &a) {
    return {a[0], a[1]};
}

Pair radiation(const Cell &a) {
    return {a[2], a[3]};
}

Ring delta(const Kernel &k, const Cell &a, const Cell &b) {
    return add(k.value(a[corr]), k.value(b[corr]), -1);
}

const char *phase(const Kernel &k, const Field &pre, const Field &post,
                  unsigned donor, unsigned target) {
    const Ring gap = delta(k, pre[donor], pre[target]);
    const Ring after = delta(k, post[donor], post[target]);
    const bool admitted = integral_pair(k.value(pre[donor][corr]), k.value(pre[target][corr]));
    if (after != (admitted ? mul(gap, rho) : gap))
        throw std::logic_error("local gap phase mismatch");
    if (gap == zero) return "-";
    return admitted ? "2" : "0";
}

unsigned lane_mask(const Cell &real, const Cell &control) {
    unsigned mask = 0;
    for (unsigned lane = 0; lane < real.size(); ++lane)
        if (real[lane] != control[lane]) mask |= 1u << lane;
    return mask;
}

void print_persistence(const Kernel &k, const Cell &real_c, const Cell &control_c,
                       const Cell &real_b, const Cell &control_b, const Cell &real_next,
                       const Cell &control_next) {
    const bool matter_contrast = matter(real_b) != matter(control_b);
    const Ring next_delta = delta(k, real_next, control_next);
    std::cout << '\t' << (next_delta != zero)
              << '\t' << (matter_contrast && matter(real_next) != matter(control_next))
              << '\t' << (radiation(real_next) != radiation(control_next))
              << '\t' << (next_delta == delta(k, real_c, control_c))
              << '\t' << (radiation(real_next) == radiation(real_c) &&
                          radiation(control_next) == radiation(control_c))
              << '\t' << (matter_contrast && matter(real_next) == matter(real_b) &&
                          matter(control_next) == matter(control_b))
              << '\t' << (matter(real_c) != matter(real_b) && matter(real_next) == matter(real_b))
              << '\t' << (matter(control_c) != matter(control_b) && matter(control_next) == matter(control_b));
}

void score(Kernel &k, const Stages *real, const std::array<Stages, follow + 1> &control,
           unsigned rank, unsigned tick, unsigned distance) {
    const unsigned emission_bit = (1 + tick) % 2;
    constexpr int source_x = source / height;
    constexpr unsigned y = source % height;
    const int direction = static_cast<unsigned>(source_x % 2) == emission_bit ? 1 : -1;
    const unsigned target = site(source_x + direction * static_cast<int>(distance), y);
    unsigned first_age = 0, first_mask = 0, arrival = 0;
    char first_stage = '-';
    for (unsigned age = 1; age <= horizon; ++age) {
        const unsigned c_mask = lane_mask(real[age].contact[target], control[age].contact[target]);
        if (!first_age) {
            const unsigned b_mask = lane_mask(real[age].collision[target], control[age].collision[target]);
            if (c_mask || b_mask) {
                first_age = age;
                first_stage = c_mask ? 'C' : 'B';
                first_mask = c_mask ? c_mask : b_mask;
            }
        }
        if (c_mask & (1u << corr)) {
            arrival = age;
            break;
        }
    }
    if (first_age && first_age < distance)
        throw std::logic_error("local contrast before light cone");

    std::cout << rank << '\t' << tick << '\t' << distance << '\t' << target << '\t' << direction
              << '\t' << first_age << '\t' << first_stage << '\t' << first_mask << '\t' << arrival;
    if (!arrival) {
        for (unsigned i = 0; i < 34; ++i) std::cout << "\t-";
        std::cout << '\n';
        return;
    }

    const unsigned bit = (emission_bit + arrival - 1) % 2;
    const int x = target / height;
    const int incoming = static_cast<unsigned>(x % 2) == bit ? -1 : 1;
    const unsigned donor = site(x - incoming, y);
    const Field &pre_real = real[arrival - 1].collision;
    const Field &pre_control = control[arrival - 1].collision;
    const Cell &real_c = real[arrival].contact[target];
    const Cell &control_c = control[arrival].contact[target];
    const Cell &real_b = real[arrival].collision[target];
    const Cell &control_b = control[arrival].collision[target];

    const bool pre_equal = pre_real[target] == pre_control[target];
    const bool donor_differs = pre_real[donor][corr] != pre_control[donor][corr];
    const bool other_equal = lane_mask(real_c, control_c) == (1u << corr);
    const bool isolated = first_age == arrival && first_stage == 'C' &&
                          pre_equal && donor_differs && other_equal;
    const bool real_move = real_c[corr] != pre_real[target][corr];
    const bool control_move = control_c[corr] != pre_control[target][corr];
    const char *real_phase = isolated ? phase(k, pre_real, real[arrival].contact, donor, target) : "-";
    const char *control_phase = isolated ? phase(k, pre_control, control[arrival].contact, donor, target) : "-";
    Cell real_local = real_c, control_local = control_c;
    const unsigned real_tag = k.collide(real_local), control_tag = k.collide(control_local);
    if (real_local != real_b || control_local != control_b)
        throw std::logic_error("local B projection mismatch");
    std::cout << '\t' << bit << '\t' << donor << '\t' << incoming << '\t' << (incoming == direction)
              << '\t' << isolated << '\t' << pre_equal << '\t' << donor_differs << '\t' << other_equal
              << '\t' << real_move << '\t' << control_move << '\t' << (isolated && !real_move && control_move)
              << '\t' << (matter(real_c) != matter(real_b))
              << '\t' << (matter(control_c) != matter(control_b))
              << '\t' << (matter(real_b) != matter(control_b))
              << '\t' << real_tag << '\t' << control_tag << '\t' << real_phase << '\t' << control_phase;
    print_persistence(k, real_c, control_c, real_b, control_b, real[arrival + 1].contact[target],
                      control[arrival + 1].contact[target]);
    print_persistence(k, real_c, control_c, real_b, control_b, real[arrival + 1].collision[target],
                      control[arrival + 1].collision[target]);
    std::cout << '\n';
}

int main() try {
    Kernel k;
    const auto bare = bare_reference(k);
    std::cout << "rank\ttick\tlength\ttarget\tray\tfirst_age\tfirst_stage\tfirst_mask\tarrival"
                 "\tbit\tdonor\tincoming\toriginal\tisolated\tpre_equal\tdonor_differs\tother_equal"
                 "\tactual_move\tcontrol_move\tsuppression\tactual_write\tcontrol_write"
                 "\tmatter_contrast\tactual_tag\tcontrol_tag\tactual_phase\tcontrol_phase";
    for (const char stage : {'C', 'B'}) {
        for (const char *metric : {"corr_contrast", "matter_contrast", "field_contrast",
                                 "same_corr_contrast", "same_field_pair", "same_matter_pair",
                                 "retained_actual_write", "retained_control_write"})
            std::cout << '\t' << stage << '_' << metric;
    }
    std::cout << '\n';
    for (unsigned rank = 0; rank <= 84; ++rank) {
        const unsigned offset = raw_predecessor(k, bare, rank);
        if (offset % 2 != 1) throw std::logic_error("raw predecessor bit mismatch");
        std::array<Stages, window + follow + 1> live{};
        live[0].collision = prepared(k, bare[offset], Mode::IngressActive);
        if (account(k, live[0].collision) != published_ledger)
            throw std::logic_error("Q774 ledger mismatch");
        for (unsigned tick = 1; tick < live.size(); ++tick)
            live[tick] = audited_tick(k, live[tick - 1].collision, tick % 2, published_ledger);

        for (unsigned tick = 1; tick <= window; ++tick) {
            Cell restored = live[tick].contact[source];
            if (k.collide(restored) != 2) continue;
            if (restored != live[tick].collision[source] ||
                restored[corr] == live[tick].contact[source][corr])
                throw std::logic_error("source restoration mismatch");
            std::array<Stages, follow + 1> control{};
            control[0].collision = live[tick].collision;
            control[0].collision[source] = live[tick].contact[source];
            if (account(k, control[0].collision) != published_ledger)
                throw std::logic_error("local undo ledger mismatch");
            for (unsigned age = 1; age < control.size(); ++age)
                control[age] = audited_tick(k, control[age - 1].collision, (tick + age) % 2, published_ledger);
            for (unsigned distance = 1; distance <= 4; ++distance)
                score(k, live.data() + tick, control, rank, tick, distance);
        }
    }
} catch (const std::exception &error) {
    std::cerr << error.what() << '\n';
    return 2;
}
