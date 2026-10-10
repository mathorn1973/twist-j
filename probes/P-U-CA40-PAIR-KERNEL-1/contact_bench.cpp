// Copyright 2026 A. M. Thorn. SPDX-License-Identifier: Apache-2.0
// Synthetic conditional-displacement/phase kernel; not a calibrated ion solver.
#include <algorithm>
#include <array>
#include <chrono>
#include <cmath>
#include <complex>
#include <cstdint>
#include <cstdlib>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <memory>
#include <stdexcept>
#include <string>
#include <vector>
#include <immintrin.h>
#include <mm_malloc.h>
#include <omp.h>
#ifdef __linux__
#include <sched.h>
#endif

constexpr int N = 78125, PAD = 78128, IONS = 7, MODES = 7;
constexpr double PI = 3.141592653589793238462643383279502884;
struct alignas(64) Coeff {
    double unary[7][5]{}, pair[21][25]{};
    double real[7][7][5]{}, imag[7][7][5]{};
    double common_real[7]{}, common_imag[7]{};
    int sign = 1;
};
struct Summary { double phase_max=0, r_max=0, checksum=0; };
struct Free { void operator()(double* p) const { _mm_free(p); } };
using Buffer = std::unique_ptr<double, Free>;
Buffer buffer() {
    auto p = static_cast<double*>(_mm_malloc(PAD*sizeof(double),64));
    if (!p) throw std::bad_alloc();
    return Buffer(p);
}
static std::array<std::array<int, PAD>, 7> labels;

// Integer generator and dyadic scales are frozen fixture data, not fitted data.
double value(unsigned c, unsigned k, int shift) {
    std::uint32_t h = (c+1u)*747796405u + (k+1u)*2891336453u;
    h ^= h >> 16; h *= 2246822519u; h ^= h >> 13;
    return std::ldexp(static_cast<double>(static_cast<int>(h % 17u)-8), shift);
}
Coeff coefficients(unsigned c) {
    Coeff t;
    t.sign = (c % 2 == 0) ? 1 : -1;
    unsigned k = 0;
    for (int i=0; i<7; ++i)
        for (int l=1; l<5; ++l) t.unary[i][l]=value(c,k++,-12);
    for (int p=0; p<21; ++p)
        for (int a=1; a<5; ++a)
            for (int b=1; b<5; ++b) t.pair[p][5*a+b]=value(c,k++,-14);
    for (int m=0; m<7; ++m) {
        t.common_real[m]=value(c,k++,-16);
        t.common_imag[m]=value(c,k++,-16);
        for (int i=0; i<7; ++i)
            for (int l=1; l<5; ++l) {
                t.real[m][i][l]=value(c,k++,-16);
                t.imag[m][i][l]=value(c,k++,-16);
            }
    }
    // Every 64th case is the ideal zero-error coefficient fixture.
    if (c % 64 == 0) { Coeff zero; zero.sign=t.sign; return zero; }
    return t;
}
void prepare_labels() {
    for (int z=0; z<PAD; ++z) {
        int q = z < N ? z : 0;
        for (int i=0; i<7; ++i) { labels[i][z]=q%5; q/=5; }
    }
}
double sample_checksum(const double* ph, const double* rr) {
    double s=0;
    for (int k=0; k<64; ++k) {
        int z=(k*1237)%N;
        s += (ph[z]+rr[z])*static_cast<double>(k+1);
    }
    return s;
}
__attribute__((noinline))
Summary scalar(const Coeff& t, double* ph, double* rr) {
    Summary s;
    for (int z=0; z<N; ++z) {
        double p=0, r=0;
        for (int i=0; i<7; ++i) p += t.unary[i][labels[i][z]];
        int pair=0;
        for (int i=0; i<7; ++i)
            for (int j=i+1; j<7; ++j)
                p += t.pair[pair++][5*labels[i][z]+labels[j][z]];
        for (int m=0; m<7; ++m) {
            double a=t.common_real[m], b=t.common_imag[m];
            for (int i=0; i<7; ++i) {
                a += t.real[m][i][labels[i][z]];
                b += t.imag[m][i][labels[i][z]];
            }
            r += (a*a+b*b)*((m+1)*0.5);
        }
        ph[z]=p; rr[z]=r;
        s.phase_max=std::max(s.phase_max,std::abs(p));
        s.r_max=std::max(s.r_max,r);
    }
    s.checksum=sample_checksum(ph,rr);
    return s;
}

// Both ISA paths have identical scalar operation order, including reductions
// over ion and mode. SIMD lanes cover consecutive basis branches.
#define DEFINE_SIMD(NAME,TARGET,V,IV,W,SET,SETI,ADD,MUL,GATHER,LOADI,IADD,IMUL,STORE,MAX,SUB) \
__attribute__((target(TARGET),noinline)) \
Summary NAME(const Coeff& t, double* ph, double* rr) { \
    V pm=SET(0.0), rm=SET(0.0); \
    for (int z=0; z<PAD; z+=W) { \
        IV ix[7]; \
        for (int i=0;i<7;++i) ix[i]=LOADI(reinterpret_cast<const IV*>(&labels[i][z])); \
        V p=SET(0.0), r=SET(0.0); \
        for (int i=0;i<7;++i) p=ADD(p,GATHER(t.unary[i],ix[i],8)); \
        int pair=0; \
        for (int i=0;i<7;++i) for (int j=i+1;j<7;++j) { \
            IV ij=IADD(IMUL(ix[i],SETI(5)),ix[j]); \
            p=ADD(p,GATHER(t.pair[pair++],ij,8)); \
        } \
        for (int m=0;m<7;++m) { \
            V a=SET(t.common_real[m]), b=SET(t.common_imag[m]); \
            for (int i=0;i<7;++i) { \
                a=ADD(a,GATHER(t.real[m][i],ix[i],8)); \
                b=ADD(b,GATHER(t.imag[m][i],ix[i],8)); \
            } \
            r=ADD(r,MUL(ADD(MUL(a,a),MUL(b,b)),SET((m+1)*0.5))); \
        } \
        STORE(ph+z,p); STORE(rr+z,r); \
        pm=MAX(pm,MAX(p,SUB(SET(0.0),p))); rm=MAX(rm,r); \
    } \
    alignas(64) double pp[W], rv[W]; STORE(pp,pm); STORE(rv,rm); \
    Summary s; for (int k=0;k<W;++k) {s.phase_max=std::max(s.phase_max,pp[k]);s.r_max=std::max(s.r_max,rv[k]);} \
    s.checksum=sample_checksum(ph,rr); return s; \
}
DEFINE_SIMD(avx2,"avx2",__m256d,__m128i,4,_mm256_set1_pd,_mm_set1_epi32,
    _mm256_add_pd,_mm256_mul_pd,_mm256_i32gather_pd,_mm_loadu_si128,
    _mm_add_epi32,_mm_mullo_epi32,_mm256_storeu_pd,_mm256_max_pd,_mm256_sub_pd)
#define GATHER512(P,I,S) _mm512_i32gather_pd(I,P,S)
DEFINE_SIMD(avx512,"avx512f,avx512dq,avx512vl",__m512d,__m256i,8,_mm512_set1_pd,_mm256_set1_epi32,
    _mm512_add_pd,_mm512_mul_pd,GATHER512,_mm256_loadu_si256,
    _mm256_add_epi32,_mm256_mullo_epi32,_mm512_storeu_pd,_mm512_max_pd,_mm512_sub_pd)
#undef DEFINE_SIMD
#undef GATHER512

using Kernel = Summary (*)(const Coeff&,double*,double*);
Kernel choose(const std::string& backend) {
    __builtin_cpu_init();
    if (backend=="scalar") return scalar;
    if (backend=="avx2" && __builtin_cpu_supports("avx2")) return avx2;
    if (backend=="avx512" && __builtin_cpu_supports("avx512f") &&
        __builtin_cpu_supports("avx512dq") && __builtin_cpu_supports("avx512vl")) return avx512;
    throw std::runtime_error("requested ISA unsupported or unknown");
}

// Retain displacement memory and its Weyl cross phase in one common frame.
struct Gaussian { std::complex<double> alpha=0.0; double phase=0; };
Gaussian compose(Gaussian a, std::complex<double> beta, double phase=0) {
    a.phase += phase + std::imag(beta*std::conj(a.alpha));
    a.alpha += beta; return a;
}
std::complex<double> kernel(Gaussian a, Gaussian b, double nu) {
    return std::polar(std::exp(-nu*std::norm(a.alpha-b.alpha)),
        a.phase-b.phase+std::imag(std::conj(b.alpha)*a.alpha));
}
void gaussian_tests() {
    using C=std::complex<double>;
    Gaussian g;
    g=compose(g,C(1,0)); g=compose(g,C(0,1));
    g=compose(g,C(-1,0)); g=compose(g,C(0,-1));
    if (std::abs(g.alpha)>1e-14 || std::abs(g.phase-2)>1e-14)
        throw std::runtime_error("Gaussian loop phase failed");
    Gaussian a=compose({},C(0.25,0.5));
    Gaussian b=compose({},C(-0.5,0.25));
    if (std::abs(kernel(a,a,0.5)-C(1,0))>1e-14 ||
        std::abs(kernel(a,b,0.5)-std::conj(kernel(b,a,0.5)))>1e-14)
        throw std::runtime_error("Gaussian kernel failed");
    // Independent fixed value detects a missing/reversed Weyl phase.
    if (std::abs(kernel(a,b,0.5)-std::polar(std::exp(-5.0/16),-5.0/16))>1e-14)
        throw std::runtime_error("Gaussian Weyl phase sign failed");
    Gaussian hot_a=a, hot_b=b;
    hot_a.phase=1.0/8; hot_b.phase=-3.0/8;
    if (std::abs(kernel(hot_a,hot_b,1.5)-std::polar(std::exp(-15.0/16),3.0/16))>1e-14)
        throw std::runtime_error("Gaussian relative phase or thermal factor failed");
    auto undone=compose(a,-a.alpha);
    if (std::abs(undone.alpha)>1e-14 || std::abs(kernel(undone,{},0.5)-C(1,0))>1e-14)
        throw std::runtime_error("Gaussian memory inverse failed");
    // A common displacement is not zero motion, even when spin coherence is 1.
    if (std::norm(a.alpha)==0 || std::abs(kernel(a,a,0.5)-C(1,0))>1e-14)
        throw std::runtime_error("common displacement fixture failed");
}
double validate(Kernel run) {
    gaussian_tests();
    auto p=buffer(),r=buffer(),sp=buffer(),sr=buffer();
    double error=0;
    for (unsigned c : {0u,1u,510u,511u}) {
        Coeff t=coefficients(c);
        Summary a=scalar(t,sp.get(),sr.get()), b=run(t,p.get(),r.get());
        for (int z=0;z<N;++z) {
            if (!std::isfinite(p.get()[z]) || !std::isfinite(r.get()[z]))
                throw std::runtime_error("nonfinite validation output");
            error=std::max(error,std::abs(p.get()[z]-sp.get()[z]));
            error=std::max(error,std::abs(r.get()[z]-sr.get()[z]));
        }
        error=std::max({error,std::abs(a.phase_max-b.phase_max),std::abs(a.r_max-b.r_max)});
        // Independent long-double point checks decode digits directly, then
        // contract terms in a different (reverse) order without the SIMD labels.
        for (int z : {0,1,15624,39062,54321,78124}) {
            int digit[7],q=z; for(int i=0;i<7;++i){digit[i]=q%5;q/=5;}
            long double pp=0,rr=0;
            int pi=20;
            for(int i=5;i>=0;--i) for(int j=6;j>i;--j)
                pp += t.pair[pi--][5*digit[i]+digit[j]];
            for(int i=6;i>=0;--i) pp += t.unary[i][digit[i]];
            for(int m=6;m>=0;--m){
                long double ar=t.common_real[m],ai=t.common_imag[m];
                for(int i=6;i>=0;--i){ar+=t.real[m][i][digit[i]];ai+=t.imag[m][i][digit[i]];}
                rr += (ar*ar+ai*ai)*((m+1)*0.5L);
            }
            error=std::max(error,std::abs(p.get()[z]-static_cast<double>(pp)));
            error=std::max(error,std::abs(r.get()[z]-static_cast<double>(rr)));
            double target=t.sign*(4*PI/5)*(digit[3]!=digit[4]);
            if (std::abs((target+p.get()[z])-target-static_cast<double>(pp))>1e-12)
                throw std::runtime_error("target/residual reconstruction failed");
        }
    }
    if (error>1e-12) throw std::runtime_error("scalar/SIMD validation mismatch");
    return error;
}

int main(int argc,char**argv) {
    try {
        std::string backend="scalar";
        int threads=1,repeats=4,candidates=512;
        bool only_validate=false;
        for(int i=1;i<argc;++i){
            std::string a=argv[i];
            if(a=="--validate"){only_validate=true;continue;}
            if(i+1>=argc)throw std::runtime_error("missing CLI value");
            std::string v=argv[++i];
            if(a=="--backend")backend=v;
            else if(a=="--threads")threads=std::stoi(v);
            else if(a=="--repeats")repeats=std::stoi(v);
            else if(a=="--candidates")candidates=std::stoi(v);
            else throw std::runtime_error("unknown option");
        }
        if(threads<1||threads>80||repeats<1||repeats>64||candidates!=512)
            throw std::runtime_error("invalid bounded benchmark size");
        Kernel run=choose(backend);
        prepare_labels();
        double validation_error=validate(run);
        if(only_validate){
            std::cout<<std::setprecision(17)<<"{\"backend\":\""<<backend
                <<"\",\"validation_passed\":true,\"max_abs_error\":"<<validation_error<<"}\n";
            return 0;
        }
        std::vector<Coeff> cases;
        for(int c=0;c<candidates;++c)cases.push_back(coefficients(c));
        std::vector<Summary> results(static_cast<std::size_t>(candidates)*repeats);
        std::vector<int> cpus(threads,-1),places(threads,-1);
        int actual=0,migrated=0;
        double t0=0,t1=0;
        omp_set_dynamic(0); omp_set_num_threads(threads);
        // Buffers are allocated/first-touched by their owning worker.
        #pragma omp parallel shared(actual,t0,t1,migrated)
        {
            int tid=omp_get_thread_num();
            auto ph=buffer(),rr=buffer();
            std::fill_n(ph.get(),PAD,0.0); std::fill_n(rr.get(),PAD,0.0);
            #ifdef __linux__
            cpus[tid]=sched_getcpu();
            #else
            cpus[tid]=-1;
            #endif
            places[tid]=omp_get_place_num();
            #pragma omp single
            { actual=omp_get_num_threads(); }
            #pragma omp barrier
            #pragma omp single
            { t0=omp_get_wtime(); }
            for(int rep=0;rep<repeats;++rep){
                #pragma omp for schedule(static)
                for(int c=0;c<candidates;++c)
                    results[static_cast<std::size_t>(rep)*candidates+c]=run(cases[c],ph.get(),rr.get());
            }
            #pragma omp single
            { t1=omp_get_wtime(); }
            #ifdef __linux__
            if(cpus[tid]!=sched_getcpu()) {
                #pragma omp atomic update
                migrated += 1;
            }
            #endif
        }
        if(actual!=threads||migrated)throw std::runtime_error("worker count or affinity changed");
        double checksum=0,pm=0,rm=0;
        for(const auto&s:results){
            if(!std::isfinite(s.checksum)||!std::isfinite(s.phase_max)||!std::isfinite(s.r_max))
                throw std::runtime_error("nonfinite benchmark summary");
            checksum+=s.checksum; pm=std::max(pm,s.phase_max);rm=std::max(rm,s.r_max);
        }
        double bound=std::min(1.0,std::sqrt(-2*std::expm1(-rm)+4*std::exp(-rm)*std::pow(std::sin(pm/2),2)));
        std::cout<<std::setprecision(17)<<"{\"backend\":\""<<backend<<"\",\"threads\":"<<actual
            <<",\"candidates\":"<<candidates<<",\"repeats\":"<<repeats
            <<",\"branches_processed\":"<<static_cast<std::uint64_t>(N)*candidates*repeats
            <<",\"elapsed_seconds\":"<<t1-t0<<",\"checksum\":"<<checksum
            <<",\"phase_max\":"<<pm<<",\"r_max\":"<<rm
            <<",\"synthetic_bound\":"<<bound<<",\"validation_passed\":true,\"max_abs_error\":"<<validation_error
            <<",\"scope\":\"synthetic_coefficient_kernel_only\",\"thread_map\":[";
        for(int t=0;t<actual;++t){if(t)std::cout<<',';
            std::cout<<"{\"thread\":"<<t<<",\"cpu\":"<<cpus[t]<<",\"place\":"<<places[t]<<'}';}
        std::cout<<"]}\n";
        return 0;
    } catch(const std::exception&e){std::cerr<<e.what()<<'\n';return 2;}
}
