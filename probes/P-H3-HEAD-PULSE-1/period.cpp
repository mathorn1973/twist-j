// SPDX-License-Identifier: Apache-2.0
// Non-canonical exact cycle audit of the H3 contact-phase fixtures.
// Build: g++ -std=c++20 -O3 period.cpp -o period
// Usage: ./period MODE {rawzero|rawN} [tick-bound]
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

bool projected_equal(const Field &actual,const Field &expected) {
    for(unsigned site=0;site<actual.size();++site) {
        for(unsigned lane=0;lane<actual[site].size();++lane) {
            if ((site==head || site==receiver) && lane!=3) continue;
            if (actual[site][lane]!=expected[site][lane]) return false;
        }
    }
    return true;
}

bool radiation_equal(const Field &actual,const Field &expected) {
    for (unsigned site=0; site<actual.size(); ++site)
        for (unsigned lane:{2u,3u})
            if (actual[site][lane]!=expected[site][lane]) return false;
    return true;
}

struct Class {
    Tick projected=0, reads=0, observations=0, writes=0, first_observation=0;
    Tick nominal_expected=0, nominal_missing=0, nominal_unqualified=0;
    Tick projected_work_clear=0, radiation_work_clear=0;
    std::map<Ring,Tick> words, written_words;
    // Encoded cut is 2 * tick for C and 2 * tick + 1 for B.
    std::map<Ring,Tick> held_cuts;
};
struct Violation {
    Tick count=0, first_tick=0;
    char first_stage='-';
    Ring first_before{}, first_after{};

    void note(Tick tick,char stage,Id before,Id after,const Kernel &k) {
        if(count++==0) {
            first_tick=tick;
            first_stage=stage;
            first_before=k.value(before);
            first_after=k.value(after);
        }
    }
    void print(const char *label) const {
        std::cout<<label<<" count="<<count;
        if(count) std::cout<<" first_tick="<<first_tick<<" first_stage="<<first_stage
                           <<" before="<<first_before<<" after="<<first_after;
        std::cout<<'\n';
    }
};
void print_class(const char *label,const std::map<Ring,Tick> &words) {
    std::cout<<label<<" distinct="<<words.size();
    for(const auto &[word,tick]:words) std::cout<<' '<<word<<'@'<<tick;
    std::cout<<'\n';
}
void print_intersection(const char *label,const std::map<Ring,Tick> &a,
                        const std::map<Ring,Tick> &b) {
    auto first=std::pair{UINT64_MAX,UINT64_MAX};
    Ring first_word{};
    std::size_t count=0;
    for(const auto &[word,tick]:a) {
        auto other=b.find(word);
        if(other==b.end()) continue;
        ++count;
        const auto pair=std::minmax(tick,other->second);
        const auto completion=std::pair{pair.second,pair.first};
        if(completion<first) {
            first=completion;
            first_word=word;
        }
    }
    std::cout<<label<<" distinct="<<count;
    if(count) std::cout<<" first_word="<<first_word<<" raw44_tick="<<a.at(first_word)
                       <<" raw4_tick="<<b.at(first_word);
    std::cout<<'\n';
}

int main(int argc,char **argv) try {
    if(argc<3 || argc>4)
        throw std::runtime_error("usage: period MODE {rawzero|rawN} [tick-bound]");
    const std::string mode=argv[1], start=argv[2];
    const auto preparation = modes.find(mode);
    if (preparation == modes.end()) throw std::runtime_error("unknown preparation");
    unsigned rank=0;
    if(start!="rawzero") {
        if(start.size()<4 || start.size()>5 || start.substr(0,3)!="raw" ||
           start.find_first_not_of("0123456789",3)!=std::string::npos)
            throw std::runtime_error("starting cut must be rawzero or rawN with N in 0..84");
        rank=std::stoul(start.substr(3));
        if(rank>84) throw std::runtime_error("raw rank must be in 0..84");
    }
    Tick horizon=argc==4?std::stoull(argv[3]):limit;
    if(!horizon || horizon>limit) throw std::runtime_error("tick-bound must be in 1..1,000,000");
    Kernel k;
    const auto bare=bare_reference(k);
    if(raw_predecessor(k,bare,44)!=predecessor_ticks[0] ||
       raw_predecessor(k,bare,4)!=predecessor_ticks[1])
        throw std::logic_error("raw 44 or raw 4 predecessor disagrees with the pinned cut");
    const unsigned offset=start=="rawzero" ? 0 : raw_predecessor(k,bare,rank);
    std::array<Field,2> cuts{}, work_reference{};
    for (unsigned i=0; i<cuts.size(); ++i) {
        cuts[i] = prepared(k, bare[predecessor_ticks[i]], preparation->second);
        work_reference[i] = prepared(k, bare[predecessor_ticks[i]+2], preparation->second);
    }
    Field f = prepared(k, bare[offset], preparation->second);
    const Field initial=f;
    const unsigned initial_bit=offset%2;
    const auto expected=account(k,f);
    const auto &h=expected[2];
    const auto trace=5*h[0]-(h[0]+h[1]+h[2]+h[3]);
    std::cout<<"preparation="<<mode<<" starting_cut="<<start<<" next_bit="<<initial_bit<<" horizon="<<horizon<<" Q="<<trace/2
             <<" matter="<<expected[0]<<" radiation="<<expected[1]
             <<" hermitian="<<h<<'\n';
    // A forward tick is C then B, so undo B before undoing C.
    // Capture the unique complete predecessor to audit a return on any tick.
    Field return_predecessor=initial;
    k.scatter(return_predecessor);
    k.transport(return_predecessor,1-initial_bit,true);
    f=initial;

    Tick transport_writes=0,scatter_writes=0,audits=0,visited=0,first_return=0;
    std::array<Class,2> classes{};
    Violation unscheduled,hold,missing_write,post_write_loss;
    Id held=f[receiver][0];
    Id last_written=held;
    int pending=-1, last_write_phase=-1;
    for(Tick n=0;n<horizon;++n) {
        const Tick tick=n+1;
        const unsigned bit=(offset+n)%2;
        const auto nominal_cut=(offset+n)%bare.size();
        const bool audited=(tick%audit_stride==0) || tick==horizon ||
                           (bit!=initial_bit && f==return_predecessor);
        Field prior{},work{};
        if(audited) prior=f;

        int projected=-1;
        if(bit) for(unsigned label=0;label<cuts.size();++label) {
            if(projected_equal(f,cuts[label])) {
                projected=static_cast<int>(label);
                ++classes[label].projected;
                break;
            }
        }

        const Id before=f[receiver][0];
        k.transport(f,bit);
        const Id after_c=f[receiver][0];
        if(after_c!=before) ++transport_writes;
        if(audited) {
            work=f;
            if(account(k,f)!=expected) throw std::logic_error("transport ledger mismatch");
        }
        const unsigned head_tag=k.scatter(f);
        const Id after_b=f[receiver][0];
        if(after_b!=after_c) ++scatter_writes;
        if(audited) {
            if(account(k,f)!=expected) throw std::logic_error("collision ledger mismatch");
            Field inverse=f;
            k.scatter(inverse);
            if(inverse!=work) throw std::logic_error("inverse B mismatch");
            k.transport(inverse,bit,true);
            if(inverse!=prior) throw std::logic_error("inverse tick mismatch");
            ++audits;
        }
        for (unsigned phase=0; phase<predecessor_ticks.size(); ++phase) {
            if(nominal_cut!=predecessor_ticks[phase]) continue;
            auto &record=classes[phase];
            ++record.nominal_expected;
            if(projected!=static_cast<int>(phase)) ++record.nominal_missing;
            else if(head_tag!=1) ++record.nominal_unqualified;
        }
        if(pending>=0) {
            Class &record=classes[pending];
            if(projected_equal(f,work_reference[pending])) ++record.projected_work_clear;
            if(radiation_equal(f,work_reference[pending])) ++record.radiation_work_clear;
            if(record.observations++==0) record.first_observation=tick;
            const Ring word=k.value(after_b);
            record.words.try_emplace(word,tick);
            if(after_b!=before) {
                ++record.writes;
                record.written_words.try_emplace(word,tick);
                last_write_phase = pending;
                last_written = after_b;
            } else missing_write.note(tick,'B',before,after_b,k);
            held=after_b;
        } else {
            if(after_c!=before) unscheduled.note(tick,'C',before,after_c,k);
            if(after_b!=after_c) unscheduled.note(tick,'B',after_c,after_b,k);
            if(after_c!=held) hold.note(tick,'C',held,after_c,k);
            if(after_b!=held) hold.note(tick,'B',held,after_b,k);
            if (last_write_phase >= 0) {
                auto &held_cuts = classes[last_write_phase].held_cuts;
                held_cuts.try_emplace(k.value(after_c), 2 * tick);
                held_cuts.try_emplace(k.value(after_b), 2 * tick + 1);
                if (after_c != last_written) post_write_loss.note(tick,'C',last_written,after_c,k);
                if (after_b != last_written) post_write_loss.note(tick,'B',last_written,after_b,k);
            }
        }
        pending=projected>=0 && head_tag==1?projected:-1;
        if(pending>=0) ++classes[pending].reads;

        visited=tick;
        if(bit!=initial_bit && f==initial) {
            first_return=tick;
            break;
        }
    }

    // The native tick with matching bit is bijective. Exact return to the
    // initial state is necessarily the orbit's first repeat.
    std::cout<<"ticks="<<visited<<" first_full_return=";
    if(first_return) std::cout<<first_return;
    else std::cout<<"none_within_bound";
    std::cout<<" audit_count="<<audits<<" transport_writes="<<transport_writes
             <<" collision_writes="<<scatter_writes<<'\n';
    for(unsigned i=0;i<classes.size();++i) {
        const auto &c=classes[i];
        std::cout<<"raw="<<labels[i]<<" projected_predecessors="<<c.projected
                 <<" B1_reads="<<c.reads<<" following_observations="<<c.observations
                 <<" changed_words="<<c.writes<<" first_observation="<<c.first_observation
                 <<" nominal_expected_reads="<<c.nominal_expected
                 <<" nominal_mismatched_predecessors="<<c.nominal_missing
                 <<" nominal_predecessors_without_B1="<<c.nominal_unqualified
                 <<" work_carrier_clears="<<c.projected_work_clear
                 <<" work_radiation_clears="<<c.radiation_work_clear
                 <<'\n';
        print_class("observed_class",c.words);
        print_class("written_class",c.written_words);
        print_class("post_write_cuts",c.held_cuts);
    }
    if (pending >= 0) std::cout << "read_pending_beyond_bound=" << labels[pending] << '\n';
    print_intersection("observed_class_intersection",classes[0].words,classes[1].words);
    print_intersection("written_class_intersection",classes[0].written_words,classes[1].written_words);
    print_intersection("post_write_cut_intersection",classes[0].held_cuts,classes[1].held_cuts);
    unscheduled.print("unscheduled_substep_changes");
    hold.print("hold_mismatches");
    post_write_loss.print("post_write_loss");
    missing_write.print("qualifying_contacts_without_final_change");
} catch(const std::exception &e) {
    std::cerr<<e.what()<<'\n';
    return 2;
}
