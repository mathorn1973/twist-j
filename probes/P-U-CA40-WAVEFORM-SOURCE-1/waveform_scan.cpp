// Copyright 2026 A. M. Thorn. SPDX-License-Identifier: Apache-2.0
// Conditional harmonic model scanner. No physical apparatus claim.
#include <algorithm>
#include <array>
#include <cmath>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>
#include <immintrin.h>
#include <omp.h>
#include <sched.h>

constexpr int N=78125, PAD=78128, BLOCK=1024, NB=(N+BLOCK-1)/BLOCK;
constexpr double PI=3.141592653589793238462643383279502884;
using Digits=std::array<int,7>;
struct alignas(64) Case {
    std::string name;
    double theta=0,phi0=0,weight[7]{},omega[7]{},unary[7][5]{},pair[21][25]{};
    double cr[7]{},ci[7]{},ar[7][7][5]{},ai[7][7][5]{};
    double anchor_phi[25]{},anchor_r[7][25]{},anchor_i[7][25]{};
};
struct Branch { double phase=0,r=0,source_phase=0,source_r=0,energy=0; };
struct Stats {
    double value[5]{},error=0,checksum=0;
    int witness[5]{};
};
static std::array<std::array<int,PAD>,7> labels;
static std::array<int,PAD> anchors;
Digits digits(int z) { Digits d{};for(int i=0;i<7;++i){d[i]=z%5;z/=5;}return d; }
void electronic(const Case&c,const Digits&d,double &p,double (&ar)[7],double (&ai)[7]) {
    p=c.phi0;
    for(int i=0;i<7;++i)p+=c.unary[i][d[i]];
    int k=0;for(int i=0;i<7;++i)for(int j=i+1;j<7;++j)p+=c.pair[k++][5*d[i]+d[j]];
    for(int m=0;m<7;++m){ar[m]=c.cr[m];ai[m]=c.ci[m];
        for(int i=0;i<7;++i){ar[m]+=c.ar[m][i][d[i]];ai[m]+=c.ai[m][i][d[i]];}}
}
Branch scalar(const Case&c,const Digits&d) {
    double p,ar[7],ai[7]; electronic(c,d,p,ar,ai);
    int anchor=5*d[3]+d[4];Branch b;double sp=p-c.anchor_phi[anchor];
    b.phase=std::remainder(p-c.theta*(d[3]!=d[4]),2*PI);
    for(int m=0;m<7;++m){
        double q=ar[m]*ar[m]+ai[m]*ai[m];b.r+=c.weight[m]*q;b.energy+=(c.omega[m]/c.omega[0])*q;
        double dr=ar[m]-c.anchor_r[m][anchor],di=ai[m]-c.anchor_i[m][anchor];
        b.source_r+=c.weight[m]*(dr*dr+di*di);
        sp+=c.anchor_r[m][anchor]*ai[m]-c.anchor_i[m][anchor]*ar[m];
    }
    b.source_phase=std::remainder(sp,2*PI);return b;
}
void update(Stats&s,const Branch&b,int z) {
    double values[]={std::abs(b.phase),b.r,std::abs(b.source_phase),b.source_r,b.energy};
    for(int k=0;k<5;++k){if(!std::isfinite(values[k])||values[k]<0)throw std::runtime_error("nonfinite branch");
        if(values[k]>s.value[k]){s.value[k]=values[k];s.witness[k]=z;}}
    s.checksum+=(b.phase+b.r+b.source_phase+b.source_r)*(1+z%31);
}
__attribute__((target("avx512f,avx512dq,avx512vl"),noinline))
Stats vector_block(const Case&c,int start,int stop,bool validate) {
    Stats s;
    #define SET(x) _mm512_set1_pd(x)
    #define ADD(a,b) _mm512_add_pd(a,b)
    #define SUB(a,b) _mm512_sub_pd(a,b)
    #define MUL(a,b) _mm512_mul_pd(a,b)
    #define GET(a,i) _mm512_i32gather_pd(i,a,8)
    for(int z=start;z<stop;z+=8){
        __m256i ix[7];for(int i=0;i<7;++i)ix[i]=_mm256_loadu_si256(reinterpret_cast<const __m256i*>(&labels[i][z]));
        auto ax=_mm256_loadu_si256(reinterpret_cast<const __m256i*>(&anchors[z]));
        __m512d p=SET(c.phi0),r=SET(0),sr=SET(0),en=SET(0);
        for(int i=0;i<7;++i)p=ADD(p,GET(c.unary[i],ix[i]));
        int k=0;for(int i=0;i<7;++i)for(int j=i+1;j<7;++j){
            auto ij=_mm256_add_epi32(_mm256_mullo_epi32(ix[i],_mm256_set1_epi32(5)),ix[j]);
            p=ADD(p,GET(c.pair[k++],ij));}
        auto sp=SUB(p,GET(c.anchor_phi,ax));
        for(int m=0;m<7;++m){
            auto ar=SET(c.cr[m]),ai=SET(c.ci[m]);
            for(int i=0;i<7;++i){ar=ADD(ar,GET(c.ar[m][i],ix[i]));ai=ADD(ai,GET(c.ai[m][i],ix[i]));}
            auto q=ADD(MUL(ar,ar),MUL(ai,ai));r=ADD(r,MUL(SET(c.weight[m]),q));
            en=ADD(en,MUL(SET(c.omega[m]/c.omega[0]),q));
            auto br=GET(c.anchor_r[m],ax),bi=GET(c.anchor_i[m],ax);
            auto dr=SUB(ar,br),di=SUB(ai,bi);
            sr=ADD(sr,MUL(SET(c.weight[m]),ADD(MUL(dr,dr),MUL(di,di))));
            sp=ADD(sp,SUB(MUL(br,ai),MUL(bi,ar)));
        }
        alignas(64) double pp[8],rr[8],ss[8],rp[8],ee[8];
        _mm512_store_pd(pp,p);_mm512_store_pd(rr,r);_mm512_store_pd(ss,sp);_mm512_store_pd(rp,sr);_mm512_store_pd(ee,en);
        for(int lane=0;lane<8 && z+lane<stop;++lane){int index=z+lane;
            Branch b{std::remainder(pp[lane]-c.theta*(labels[3][index]!=labels[4][index]),2*PI),rr[lane],std::remainder(ss[lane],2*PI),rp[lane],ee[lane]};
            if(validate){Branch ref=scalar(c,digits(index));
                double errors[]={std::abs(b.phase-ref.phase),std::abs(b.r-ref.r),std::abs(b.source_phase-ref.source_phase),std::abs(b.source_r-ref.source_r),std::abs(b.energy-ref.energy)};
                for(double e:errors){if(!std::isfinite(e))throw std::runtime_error("nonfinite validation");s.error=std::max(s.error,e);}}
            update(s,b,index);
        }
    }
    #undef SET
    #undef ADD
    #undef SUB
    #undef MUL
    #undef GET
    return s;
}
double bound(double r,double phase) {
    if(phase>PI/2)return 1;
    return std::min(1.0,std::sqrt(-2*std::expm1(-r)+4*std::exp(-r)*std::pow(std::sin(phase/2),2)));
}
std::vector<Case> read(const std::string&path) {
    std::ifstream in(path);int n=0;in>>n;if(n!=24)throw std::runtime_error("expected 24 contexts");
    std::vector<Case> out(n);
    auto number=[&](double&v){in>>v;if(!in||!std::isfinite(v))throw std::runtime_error("invalid input");};
    for(auto&c:out){in>>c.name;if(c.name.empty()||c.name.find_first_not_of("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-")!=std::string::npos)throw std::runtime_error("invalid case name");
        number(c.theta);number(c.phi0);
        for(auto&v:c.weight){number(v);if(v<0.5)throw std::runtime_error("invalid thermal weight");}
        for(auto&v:c.omega){number(v);if(v<=0)throw std::runtime_error("invalid mode frequency");}
        for(auto&row:c.unary)for(auto&v:row)number(v);
        for(auto&row:c.pair)for(auto&v:row)number(v);
        for(auto&v:c.cr)number(v);
        for(auto&v:c.ci)number(v);
        for(auto&mode:c.ar)for(auto&ion:mode)for(auto&v:ion)number(v);
        for(auto&mode:c.ai)for(auto&ion:mode)for(auto&v:ion)number(v);
        for(int a=0;a<5;++a)for(int b=0;b<5;++b){Digits d{};d[3]=a;d[4]=b;double p,re[7],im[7];electronic(c,d,p,re,im);int q=5*a+b;c.anchor_phi[q]=p;
            for(int m=0;m<7;++m){c.anchor_r[m][q]=re[m];c.anchor_i[m][q]=im[m];}}
    }
    std::string extra;if(in>>extra)throw std::runtime_error("trailing input");return out;
}
struct Scan { std::vector<Stats> stats;std::array<int,80> cpus{},places{};double seconds=0;int threads=0,migrated=0; };
Scan scan(const std::vector<Case>&cases,bool validate) {
    Scan out;out.stats.resize(cases.size()*NB);double t0=0,t1=0;
    // Each context is split into 77 blocks, so all 80 workers receive actual work.
    #pragma omp parallel shared(out,t0,t1)
    {
        int tid=omp_get_thread_num();out.cpus[tid]=sched_getcpu();out.places[tid]=omp_get_place_num();
        #pragma omp barrier
        #pragma omp single
        {out.threads=omp_get_num_threads();t0=omp_get_wtime();}
        #pragma omp for schedule(static)
        for(int task=0;task<static_cast<int>(out.stats.size());++task){int c=task/NB,start=(task%NB)*BLOCK;
            out.stats[task]=vector_block(cases[c],start,std::min(start+BLOCK,N),validate);}
        #pragma omp single
        {t1=omp_get_wtime();}
        if(out.cpus[tid]!=sched_getcpu()){
            #pragma omp atomic update
            out.migrated+=1;
        }
    }
    out.seconds=t1-t0;if(out.threads!=80||out.migrated)throw std::runtime_error("thread count or CPU migration");return out;
}
Stats reduce(const Scan&s,int c){Stats out;for(int k=0;k<NB;++k){const auto&v=s.stats[c*NB+k];out.error=std::max(out.error,v.error);out.checksum+=v.checksum;
    for(int j=0;j<5;++j)if(v.value[j]>out.value[j]||(v.value[j]==out.value[j]&&v.witness[j]<out.witness[j])){out.value[j]=v.value[j];out.witness[j]=v.witness[j];}}return out;}
int main(int argc,char**argv){try{
    if(argc!=3||std::string(argv[1])!="--input")throw std::runtime_error("usage: waveform_scan --input coefficients.txt");
    __builtin_cpu_init();if(!__builtin_cpu_supports("avx512f")||!__builtin_cpu_supports("avx512dq")||!__builtin_cpu_supports("avx512vl"))throw std::runtime_error("AVX512 unavailable");
    omp_set_dynamic(0);omp_set_num_threads(80);
    for(int z=0;z<PAD;++z){auto d=digits(z<N?z:0);for(int i=0;i<7;++i)labels[i][z]=d[i];anchors[z]=5*d[3]+d[4];}
    auto cases=read(argv[2]);auto checked=scan(cases,true);double error=0;
    for(int c=0;c<24;++c)error=std::max(error,reduce(checked,c).error);
    if(error>1e-9)throw std::runtime_error("scalar/SIMD discrepancy exceeds 1e-9");
    auto timed=scan(cases,false);
    std::cout<<std::setprecision(17)<<"{\"status\":\"PASS\",\"backend\":\"avx512\",\"threads\":80,\"branches\":"<<24LL*N
       <<",\"kernel_seconds\":"<<timed.seconds<<",\"validation_seconds\":"<<checked.seconds<<",\"max_abs_error\":"<<error<<",\"cases\":[";
    for(int c=0;c<24;++c){if(c)std::cout<<',';auto s=reduce(timed,c);auto v=reduce(checked,c);
        if(s.checksum!=v.checksum)throw std::runtime_error("validation/timed diagnostic mismatch");
        std::cout<<"{\"name\":\""<<cases[c].name<<"\",\"gate_phase_max\":"<<s.value[0]<<",\"gate_r_max\":"<<s.value[1]
         <<",\"source_phase_max\":"<<s.value[2]<<",\"source_r_max\":"<<s.value[3]<<",\"motion_energy_quanta_max\":"<<s.value[4]
         <<",\"gate_bound\":"<<bound(s.value[1],s.value[0])<<",\"source_bound\":"<<bound(s.value[3],s.value[2])<<",\"checksum\":"<<s.checksum<<",\"witness_indices\":[";
        for(int k=0;k<5;++k){if(k)std::cout<<',';std::cout<<s.witness[k];}std::cout<<"]}";
    }
    std::cout<<"],\"thread_map\":[";
    for(int t=0;t<80;++t){if(t)std::cout<<',';std::cout<<"{\"thread\":"<<t<<",\"cpu\":"<<timed.cpus[t]<<",\"place\":"<<timed.places[t]<<"}";}
    std::cout<<"]}\n";return 0;
}catch(const std::exception&e){std::cerr<<e.what()<<'\n';return 2;}}
