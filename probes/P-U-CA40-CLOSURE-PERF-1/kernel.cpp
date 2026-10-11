// Copyright 2026 A. M. Thorn. SPDX-License-Identifier: Apache-2.0
// Fixed-waveform computation with an a posteriori full-space defect enclosure.
// Candidate coefficients are exact dyadics. The hot certifier uses FP centers
// with rigorous normwise balls; cold restoration retains directed intervals.
// No numerical invocation is permitted before the public source pin.
#include "validated_model.hpp"
#include <algorithm>
#include <array>
#include <atomic>
#include <bit>
#include <cmath>
#include <complex>
#include <cstdint>
#include <filesystem>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <limits>
#include <mutex>
#include <stdexcept>
#include <string>
#include <unordered_map>
#include <vector>
#include <immintrin.h>
#include <omp.h>
#include <sched.h>
using C=std::complex<double>;
using V=std::vector<double>;
using I=vm::I;
using Z=vm::Z;
constexpr int M=7,B=8,CASES=6,THERMAL=120,BATCHES=15;
#define AVX __attribute__((target("avx512f,avx512dq,avx512vl")))
constexpr int RD=_MM_FROUND_TO_NEG_INF|_MM_FROUND_NO_EXC;
constexpr int RU=_MM_FROUND_TO_POS_INF|_MM_FROUND_NO_EXC;
AVX double ad(double a,double b){return _mm_cvtsd_f64(_mm_add_round_sd(_mm_set_sd(a),_mm_set_sd(b),RD));}
AVX double au(double a,double b){return _mm_cvtsd_f64(_mm_add_round_sd(_mm_set_sd(a),_mm_set_sd(b),RU));}
AVX double md(double a,double b){return _mm_cvtsd_f64(_mm_mul_round_sd(_mm_set_sd(a),_mm_set_sd(b),RD));}
AVX double mu(double a,double b){return _mm_cvtsd_f64(_mm_mul_round_sd(_mm_set_sd(a),_mm_set_sd(b),RU));}
AVX double dd(double a,double b){return _mm_cvtsd_f64(_mm_div_round_sd(_mm_set_sd(a),_mm_set_sd(b),RD));}
AVX double du(double a,double b){return _mm_cvtsd_f64(_mm_div_round_sd(_mm_set_sd(a),_mm_set_sd(b),RU));}
AVX double sd(double x){return _mm_cvtsd_f64(_mm_sqrt_round_sd(_mm_setzero_pd(),_mm_set_sd(x),RD));}
AVX double su(double x){return _mm_cvtsd_f64(_mm_sqrt_round_sd(_mm_setzero_pd(),_mm_set_sd(x),RU));}
I exact(double x){return {x,x};}
I neg(I a){return {-a.hi,-a.lo};}
AVX I add(I a,I b){return {ad(a.lo,b.lo),au(a.hi,b.hi)};}
AVX I sub(I a,I b){return add(a,neg(b));}
AVX I mul(I a,I b){return {std::min({md(a.lo,b.lo),md(a.lo,b.hi),md(a.hi,b.lo),md(a.hi,b.hi)}),std::max({mu(a.lo,b.lo),mu(a.lo,b.hi),mu(a.hi,b.lo),mu(a.hi,b.hi)})};}
AVX I divi(I a,I b){if(b.lo<=0&&b.hi>=0)throw std::runtime_error("interval division through zero");return mul(a,{dd(1,b.hi),du(1,b.lo)});}
AVX I sq(I a){if(a.lo<=0&&a.hi>=0)return {0,std::max(mu(a.lo,a.lo),mu(a.hi,a.hi))};return {std::min(md(a.lo,a.lo),md(a.hi,a.hi)),std::max(mu(a.lo,a.lo),mu(a.hi,a.hi))};}
AVX I root(I a){if(a.hi<0)throw std::runtime_error("negative square root interval");return {sd(std::max(0.0,a.lo)),su(std::max(0.0,a.hi))};}
double mag(I a){return std::max(std::abs(a.lo),std::abs(a.hi));}
double mid(I a){return a.lo/2+a.hi/2;}
C mid(Z a){return {mid(a.re),mid(a.im)};}
Z neg(Z a){return {neg(a.re),neg(a.im)};}
Z conjz(Z a){return {a.re,neg(a.im)};}
Z exact(C a){return {exact(a.real()),exact(a.imag())};}
AVX Z add(Z a,Z b){return {add(a.re,b.re),add(a.im,b.im)};}
AVX Z mul(Z a,Z b){return {sub(mul(a.re,b.re),mul(a.im,b.im)),add(mul(a.re,b.im),mul(a.im,b.re))};}
AVX Z scale(Z a,I b){return {mul(a.re,b),mul(a.im,b)};}
AVX I absz(Z a){return root(add(sq(a.re),sq(a.im)));}
void check(I a){if(!std::isfinite(a.lo)||!std::isfinite(a.hi)||a.lo>a.hi)throw std::runtime_error("nonfinite or inverted interval");}
void check(Z a){check(a.re);check(a.im);}

struct Basis {
 int L,d;std::vector<std::array<int,M>> n,up,down;
 std::vector<int> degree,start;std::vector<std::array<I,M>> raise,lower;
 std::array<I,vm::MAX_G+2> roots;
 std::array<std::array<I,vm::MAX_G+1>,vm::MAX_G+1> cr{},an{};
 explicit Basis(int cutoff,const vm::Prepared&p):L(cutoff){
  roots=p.sqrt_n;
  for(int n=0;n<=L;++n){cr[n][0]=an[n][0]=exact(1);for(int k=1;k<=n;++k)cr[n][k]=divi(mul(cr[n][k-1],roots[n-k+1]),exact(k));for(int k=1;k<=L-n;++k)an[n][k]=divi(mul(an[n][k-1],roots[n+k]),exact(k));}
  std::array<int,M> row{};
  auto visit=[&](auto&&self,int m,int left)->void{if(m==M-1){row[m]=left;n.push_back(row);return;}for(int k=0;k<=left;++k){row[m]=k;self(self,m+1,left-k);}};
  for(int total=0;total<=L;++total){start.push_back(int(n.size()));visit(visit,0,total);}start.push_back(int(n.size()));d=int(n.size());
  auto key=[](const std::array<int,M>&v){uint64_t out=0;for(int m=0;m<M;++m)out|=uint64_t(v[m])<<(5*m);return out;};
  std::unordered_map<uint64_t,int> index;for(int j=0;j<d;++j)if(!index.emplace(key(n[j]),j).second)throw std::runtime_error("basis index collision");
  up.resize(d);down.resize(d);raise.resize(d);lower.resize(d);degree.resize(d);
  for(int j=0;j<d;++j){int total=0;for(int v:n[j])total+=v;degree[j]=total;
   for(int m=0;m<M;++m){auto v=n[j];up[j][m]=down[j][m]=-1;lower[j][m]=p.sqrt_n[v[m]];raise[j][m]=p.sqrt_n[v[m]+1];
    if(v[m]){--v[m];down[j][m]=index.at(key(v));++v[m];}if(total<L){++v[m];up[j][m]=index.at(key(v));}
   }
  }
 }
};
C get(const V&v,int d,int row,int lane){return {v[row*B+lane],v[(d+row)*B+lane]};}
void put(V&v,int d,int row,int lane,C x){v[row*B+lane]=x.real();v[(d+row)*B+lane]=x.imag();}
AVX void axpy(V&y,const V&x,double a){auto z=_mm512_set1_pd(a);for(size_t k=0;k<y.size();k+=B)_mm512_storeu_pd(&y[k],_mm512_add_pd(_mm512_loadu_pd(&y[k]),_mm512_mul_pd(z,_mm512_loadu_pd(&x[k]))));}
AVX void ladder(const Basis&b,const V&x,V&out,const std::array<C,M>&coef,bool creation,int order){
 std::fill(out.begin(),out.end(),0.0);int begin=creation?b.start[order]:0,end=creation?b.d:b.start[b.L-order+1];
 for(int n=begin;n<end;++n){auto re=_mm512_setzero_pd(),im=re;
  for(int m=0;m<M;++m){int j=creation?b.down[n][m]:b.up[n][m];if(j<0)continue;double s=mid(creation?b.lower[n][m]:b.raise[n][m])/order;
   auto cr=_mm512_set1_pd(coef[m].real()*s),ci=_mm512_set1_pd(coef[m].imag()*s),xr=_mm512_loadu_pd(&x[j*B]),xi=_mm512_loadu_pd(&x[(b.d+j)*B]);
   re=_mm512_add_pd(re,_mm512_sub_pd(_mm512_mul_pd(cr,xr),_mm512_mul_pd(ci,xi)));im=_mm512_add_pd(im,_mm512_add_pd(_mm512_mul_pd(cr,xi),_mm512_mul_pd(ci,xr)));
  }_mm512_storeu_pd(&out[n*B],re);_mm512_storeu_pd(&out[(b.d+n)*B],im);
 }
}
struct Work {V term,temp,sum,half,dp,dm,lower,upper,k1,k2,k3,k4,stage,initial,f1,a0,a1,aux,trial;std::array<V,6> poly;
 explicit Work(int d):term(2*d*B),temp(term.size()),sum(term.size()),half(term.size()),dp(term.size()),dm(term.size()),lower(term.size()),upper(term.size()),k1(term.size()),k2(term.size()),k3(term.size()),k4(term.size()),stage(term.size()),initial(term.size()),f1(term.size()),a0(term.size()),a1(term.size()),aux(term.size()),trial(term.size()){for(auto&v:poly)v.resize(term.size());}
};
AVX void collective_displacement(const Basis&b,const V&x,V&out,const std::array<C,M>&beta,double gaussian,Work&w){
 std::array<C,M>ann;for(int m=0;m<M;++m)ann[m]=-std::conj(beta[m]);w.term=x;w.sum=x;
 for(int k=1;k<=b.L;++k){ladder(b,w.term,w.temp,ann,false,k);w.term.swap(w.temp);axpy(w.sum,w.term,1);}w.half=w.sum;w.term=w.half;out=w.half;
 for(int k=1;k<=b.L;++k){ladder(b,w.term,w.temp,beta,true,k);w.term.swap(w.temp);axpy(out,w.term,1);}
 auto a=_mm512_set1_pd(gaussian);for(size_t k=0;k<out.size();k+=B)_mm512_storeu_pd(&out[k],_mm512_mul_pd(a,_mm512_loadu_pd(&out[k])));
}
AVX void mode_exp(const Basis&b,const V&x,V&out,C beta,int mode,bool creation){
 std::array<C,vm::MAX_G+1>power;power[0]=1;for(int k=1;k<=b.L;++k)power[k]=power[k-1]*beta;
 std::array<std::array<C,vm::MAX_G+1>,vm::MAX_G+1>coef{};
 for(int n=0;n<=b.L;++n)for(int k=1;k<=(creation?n:b.L-n);++k)coef[n][k]=power[k]*mid(creation?b.cr[n][k]:b.an[n][k]);
 for(int n=0;n<b.d;++n){auto re=_mm512_loadu_pd(&x[n*B]),im=_mm512_loadu_pd(&x[(b.d+n)*B]);int row=n,count=creation?b.n[n][mode]:b.L-b.degree[n];
  for(int k=1;k<=count;++k){row=creation?b.down[row][mode]:b.up[row][mode];if(row<0)throw std::runtime_error("mode exponential index");C c=coef[b.n[n][mode]][k];auto cr=_mm512_set1_pd(c.real()),ci=_mm512_set1_pd(c.imag()),xr=_mm512_loadu_pd(&x[row*B]),xi=_mm512_loadu_pd(&x[(b.d+row)*B]);re=_mm512_add_pd(re,_mm512_sub_pd(_mm512_mul_pd(cr,xr),_mm512_mul_pd(ci,xi)));im=_mm512_add_pd(im,_mm512_add_pd(_mm512_mul_pd(cr,xi),_mm512_mul_pd(ci,xr)));}
  _mm512_storeu_pd(&out[n*B],re);_mm512_storeu_pd(&out[(b.d+n)*B],im);
 }
}
AVX void displacement(const Basis&b,const V&x,V&out,const std::array<C,M>&beta,double gaussian,Work&w){
 if(&x==&out||&x==&w.term||&x==&w.temp||&out==&w.term||&out==&w.temp)throw std::runtime_error("candidate displacement alias");
 mode_exp(b,x,w.term,-std::conj(beta[0]),0,false);
 for(int m=1;m<M;++m){mode_exp(b,w.term,w.temp,-std::conj(beta[m]),m,false);w.term.swap(w.temp);}
 for(int m=0;m<M;++m){mode_exp(b,w.term,w.temp,beta[m],m,true);w.term.swap(w.temp);}out.swap(w.term);auto a=_mm512_set1_pd(gaussian);for(size_t k=0;k<out.size();k+=B)_mm512_storeu_pd(&out[k],_mm512_mul_pd(a,_mm512_loadu_pd(&out[k])));
}
AVX void generator(const Basis&b,const V&y,V&out,const vm::Node&p,Work&w){
 std::fill(out.begin(),out.end(),0.0);
 for(int j=0;j<2;++j){if(!p.active[j])continue;std::array<C,M> beta,negative,ann,create;for(int m=0;m<M;++m){beta[m]=mid(p.beta[j][m]);negative[m]=-beta[m];create[m]=C(0,-1)*beta[m];ann[m]=std::conj(create[m]);}
  displacement(b,y,w.dp,beta,mid(p.gaussian[j]),w);displacement(b,y,w.dm,negative,mid(p.gaussian[j]),w);ladder(b,y,w.lower,ann,false,1);ladder(b,y,w.upper,create,true,1);
  C a=C(0,-0.5)*mid(p.phase[j]),bb=C(0,0.5)*std::conj(mid(p.phase[j]));double diagonal=mid(p.sn[j])+mid(p.cs[j])*mid(p.mean[j]),scale=2*mid(p.u),cs=mid(p.cs[j]);
  auto ar=_mm512_set1_pd(a.real()),ai=_mm512_set1_pd(a.imag()),br=_mm512_set1_pd(bb.real()),bi=_mm512_set1_pd(bb.imag()),di=_mm512_set1_pd(diagonal),co=_mm512_set1_pd(cs),sc=_mm512_set1_pd(scale);
  for(int n=0;n<b.d;++n){int r=n*B,i=(b.d+n)*B;auto pr=_mm512_loadu_pd(&w.dp[r]),pi=_mm512_loadu_pd(&w.dp[i]),mr=_mm512_loadu_pd(&w.dm[r]),mi=_mm512_loadu_pd(&w.dm[i]);
   auto re=_mm512_add_pd(_mm512_sub_pd(_mm512_mul_pd(ar,pr),_mm512_mul_pd(ai,pi)),_mm512_sub_pd(_mm512_mul_pd(br,mr),_mm512_mul_pd(bi,mi)));
   auto im=_mm512_add_pd(_mm512_add_pd(_mm512_mul_pd(ar,pi),_mm512_mul_pd(ai,pr)),_mm512_add_pd(_mm512_mul_pd(br,mi),_mm512_mul_pd(bi,mr)));
   re=_mm512_sub_pd(re,_mm512_add_pd(_mm512_mul_pd(di,_mm512_loadu_pd(&y[r])),_mm512_mul_pd(co,_mm512_add_pd(_mm512_loadu_pd(&w.lower[r]),_mm512_loadu_pd(&w.upper[r])))));
   im=_mm512_sub_pd(im,_mm512_add_pd(_mm512_mul_pd(di,_mm512_loadu_pd(&y[i])),_mm512_mul_pd(co,_mm512_add_pd(_mm512_loadu_pd(&w.lower[i]),_mm512_loadu_pd(&w.upper[i])))));
   _mm512_storeu_pd(&out[r],_mm512_add_pd(_mm512_loadu_pd(&out[r]),_mm512_mul_pd(sc,im)));_mm512_storeu_pd(&out[i],_mm512_sub_pd(_mm512_loadu_pd(&out[i]),_mm512_mul_pd(sc,re)));
  }
 }
}
// Componentwise enclosures. Explicit embedded AVX-512 rounding ignores the
// ambient rounding direction; gradual underflow is checked in every worker.
struct R {__m512d lo,hi;};
AVX R vr(I a){return {_mm512_set1_pd(a.lo),_mm512_set1_pd(a.hi)};}
AVX R vn(R a){auto z=_mm512_setzero_pd();return {_mm512_sub_round_pd(z,a.hi,RD),_mm512_sub_round_pd(z,a.lo,RU)};}
AVX R va(R a,R b){return {_mm512_add_round_pd(a.lo,b.lo,RD),_mm512_add_round_pd(a.hi,b.hi,RU)};}
AVX R vs(R a,R b){return va(a,vn(b));}
AVX R vmul(R a,R b){
 auto l0=_mm512_mul_round_pd(a.lo,b.lo,RD),l1=_mm512_mul_round_pd(a.lo,b.hi,RD),l2=_mm512_mul_round_pd(a.hi,b.lo,RD),l3=_mm512_mul_round_pd(a.hi,b.hi,RD);
 auto h0=_mm512_mul_round_pd(a.lo,b.lo,RU),h1=_mm512_mul_round_pd(a.lo,b.hi,RU),h2=_mm512_mul_round_pd(a.hi,b.lo,RU),h3=_mm512_mul_round_pd(a.hi,b.hi,RU);
 __mmask8 bad=_mm512_cmp_pd_mask(l0,l0,_CMP_UNORD_Q)|_mm512_cmp_pd_mask(l1,l1,_CMP_UNORD_Q)|_mm512_cmp_pd_mask(l2,l2,_CMP_UNORD_Q)|_mm512_cmp_pd_mask(l3,l3,_CMP_UNORD_Q)|_mm512_cmp_pd_mask(h0,h0,_CMP_UNORD_Q)|_mm512_cmp_pd_mask(h1,h1,_CMP_UNORD_Q)|_mm512_cmp_pd_mask(h2,h2,_CMP_UNORD_Q)|_mm512_cmp_pd_mask(h3,h3,_CMP_UNORD_Q);
 auto lo=_mm512_min_pd(_mm512_min_pd(l0,l1),_mm512_min_pd(l2,l3)),hi=_mm512_max_pd(_mm512_max_pd(h0,h1),_mm512_max_pd(h2,h3));
 return {_mm512_mask_mov_pd(lo,bad,_mm512_set1_pd(-std::numeric_limits<double>::infinity())),_mm512_mask_mov_pd(hi,bad,_mm512_set1_pd(std::numeric_limits<double>::infinity()))};
}
struct IV {V lo,hi;explicit IV(int d=0):lo(2*d*B),hi(lo.size()){};};
AVX R load(const IV&a,int k){return {_mm512_loadu_pd(&a.lo[k]),_mm512_loadu_pd(&a.hi[k])};}
AVX void save(IV&a,int k,R x){_mm512_storeu_pd(&a.lo[k],x.lo);_mm512_storeu_pd(&a.hi[k],x.hi);}
void zero(IV&a){std::fill(a.lo.begin(),a.lo.end(),0);std::fill(a.hi.begin(),a.hi.end(),0);}
void embed(IV&out,const V&x,int d,int g){zero(out);for(int n=0;n<d;++n)for(int lane=0;lane<B;++lane){int r=n*B+lane,i=(g+n)*B+lane;out.lo[r]=out.hi[r]=x[n*B+lane];out.lo[i]=out.hi[i]=x[(d+n)*B+lane];}}
AVX void iaxpy(IV&out,const IV&x,I a){auto q=vr(a);for(size_t k=0;k<out.lo.size();k+=B)save(out,k,va(load(out,k),vmul(q,load(x,k))));}
AVX void icaxpy(IV&out,const IV&x,Z a,int g){auto re=vr(a.re),im=vr(a.im);for(int n=0;n<g;++n){int r=n*B,i=(g+n)*B;auto xr=load(x,r),xi=load(x,i);save(out,r,va(load(out,r),vs(vmul(re,xr),vmul(im,xi))));save(out,i,va(load(out,i),va(vmul(re,xi),vmul(im,xr))));}}
AVX void iladder(const Basis&g,const IV&x,IV&out,const std::array<Z,M>&coef,bool creation,int order,int input_support){
 zero(out);int begin=creation?g.start[order]:0,end=creation?g.d:g.start[std::max(0,input_support-order+1)];
 std::array<std::array<Z,vm::MAX_G+2>,M> factors;
 // Roots depend only on the occupation, so scalar interval products are made
 // once per mode/occupation, never once per high-dimensional matrix row.
 for(int m=0;m<M;++m)for(int k=0;k<=g.L+1;++k)factors[m][k]=scale(coef[m],divi(g.roots[k],exact(order)));
 for(int n=begin;n<end;++n){auto re=vr(exact(0)),im=re;
  for(int m=0;m<M;++m){int j=creation?g.down[n][m]:g.up[n][m];if(j<0)continue;Z c=factors[m][g.n[n][m]+(creation?0:1)];auto cr=vr(c.re),ci=vr(c.im),xr=load(x,j*B),xi=load(x,(g.d+j)*B);
   re=va(re,vs(vmul(cr,xr),vmul(ci,xi)));im=va(im,va(vmul(cr,xi),vmul(ci,xr)));
  }save(out,n*B,re);save(out,(g.d+n)*B,im);
 }
}
AVX std::array<I,B> norm2(const IV&x,int d,int begin=0,int end=-1){
 if(end<0){end=d;}
 auto lower=_mm512_setzero_pd(),upper=lower,zero_v=lower;auto mask=_mm512_castsi512_pd(_mm512_set1_epi64(0x7fffffffffffffffLL));
 for(int n=begin;n<end;++n)for(int part=0;part<2;++part){auto a=load(x,(part*d+n)*B);auto al=_mm512_and_pd(a.lo,mask),ah=_mm512_and_pd(a.hi,mask),high=_mm512_max_pd(al,ah),low=_mm512_min_pd(al,ah);
  __mmask8 valid=_mm512_cmp_pd_mask(a.lo,a.hi,_CMP_LE_OQ)&_mm512_cmp_pd_mask(high,_mm512_set1_pd(std::numeric_limits<double>::infinity()),_CMP_LT_OQ);if(valid!=255)throw std::runtime_error("invalid vector interval");
  __mmask8 cross=_mm512_cmp_pd_mask(a.lo,zero_v,_CMP_LE_OQ)&_mm512_cmp_pd_mask(a.hi,zero_v,_CMP_GE_OQ);low=_mm512_mask_mov_pd(low,cross,zero_v);
  lower=_mm512_add_round_pd(lower,_mm512_mul_round_pd(low,low,RD),RD);upper=_mm512_add_round_pd(upper,_mm512_mul_round_pd(high,high,RU),RU);
 }double lo[B],hi[B];_mm512_storeu_pd(lo,lower);_mm512_storeu_pd(hi,upper);std::array<I,B>r{};for(int k=0;k<B;++k)r[k]={lo[k],hi[k]};return r;
}
struct IWork {IV term,temp,sum,half,dp,dm,lower,upper,value,derivative,residual,aux;explicit IWork(int d):term(d),temp(d),sum(d),half(d),dp(d),dm(d),lower(d),upper(d),value(d),derivative(d),residual(d),aux(d){};};
AVX void imode_exp(const Basis&b,const IV&x,IV&out,Z beta,int mode,bool creation,int support){
 std::array<Z,vm::MAX_G+1>power;power[0]=exact(C(1));for(int k=1;k<=b.L;++k)power[k]=mul(power[k-1],beta);
 std::array<std::array<Z,vm::MAX_G+1>,vm::MAX_G+1>coef{};
 for(int n=0;n<=b.L;++n)for(int k=1;k<=(creation?n:b.L-n);++k)coef[n][k]=scale(power[k],creation?b.cr[n][k]:b.an[n][k]);
 zero(out);int end=creation?b.d:b.start[support+1];
 for(int n=0;n<end;++n){auto re=load(x,n*B),im=load(x,(b.d+n)*B);int row=n,count=creation?b.n[n][mode]:support-b.degree[n];
  for(int k=1;k<=count;++k){row=creation?b.down[row][mode]:b.up[row][mode];if(row<0)throw std::runtime_error("interval mode index");Z c=coef[b.n[n][mode]][k];auto cr=vr(c.re),ci=vr(c.im),xr=load(x,row*B),xi=load(x,(b.d+row)*B);re=va(re,vs(vmul(cr,xr),vmul(ci,xi)));im=va(im,va(vmul(cr,xi),vmul(ci,xr)));}save(out,n*B,re);save(out,(b.d+n)*B,im);
 }
}
AVX std::array<double,B> idisplacement(const Basis&g,const IV&x,IV&out,const std::array<Z,M>&beta,I gaussian,int L,const std::array<I,vm::MAX_L+1>*tail,IWork&w){
 w.term=x;for(int m=0;m<M;++m){imode_exp(g,w.term,w.temp,neg(conjz(beta[m])),m,false,L);std::swap(w.term,w.temp);}w.half=w.term;
 std::array<double,B> outside{};
 if(tail)for(int l=0;l<=L;++l){auto n=norm2(w.half,g.d,g.start[l],g.start[l+1]);for(int lane=0;lane<B;++lane)outside[lane]=au(outside[lane],mu((*tail)[l].hi,su(n[lane].hi)));}
 for(int m=0;m<M;++m){imode_exp(g,w.term,w.temp,beta[m],m,true,g.L);std::swap(w.term,w.temp);}out=w.term;
 for(size_t k=0;k<out.lo.size();k+=B){save(out,k,vmul(vr(gaussian),load(out,k)));}
 return outside;
}
AVX void polynomial(const Work&w,int d,int g,I x,I h,IV&y,IV&derivative){
 zero(y);zero(derivative);for(int n=0;n<d;++n)for(int part=0;part<2;++part){int src=(part*d+n)*B,dst=(part*g+n)*B;auto p=vr(exact(0)),v=p;
  for(int q=5;q>=0;--q){v=va(vmul(v,vr(x)),p);R a{_mm512_loadu_pd(&w.poly[q][src]),_mm512_loadu_pd(&w.poly[q][src])};p=va(vmul(p,vr(x)),a);}save(y,dst,p);save(derivative,dst,vmul(v,vr(divi(exact(1),h))));
 }
}
struct Defect {std::array<double,B>guard{},tail{},time_node{},projection_node{};};
AVX Defect defect(const vm::Prepared&p,const Basis&g,const vm::Node&node,int L,IWork&w){
 zero(w.residual);icaxpy(w.residual,w.derivative,exact(C(0,1)),g.d);std::array<double,B>tail{};
 for(int j=0;j<2;++j){if(!node.active[j])continue;std::array<Z,M> beta,negative,ann,create;for(int m=0;m<M;++m){beta[m]=node.beta[j][m];negative[m]=neg(beta[m]);create[m]=mul(exact(C(0,-1)),beta[m]);ann[m]=conjz(create[m]);}
  auto tp=idisplacement(g,w.value,w.dp,beta,node.gaussian[j],L,&p.tail[j],w);auto tm=idisplacement(g,w.value,w.dm,negative,node.gaussian[j],L,&p.tail[j],w);
  iladder(g,w.value,w.lower,ann,false,1,L);iladder(g,w.value,w.upper,create,true,1,g.L);
  I twice=mul(exact(2),node.u);Z cp=scale(mul(exact(C(0,-0.5)),node.phase[j]),neg(twice)),cm=scale(mul(exact(C(0,0.5)),conjz(node.phase[j])),neg(twice));
  icaxpy(w.residual,w.dp,cp,g.d);icaxpy(w.residual,w.dm,cm,g.d);
  I diagonal=mul(twice,add(node.sn[j],mul(node.cs[j],node.mean[j]))),linear=mul(twice,node.cs[j]);iaxpy(w.residual,w.value,diagonal);iaxpy(w.residual,w.lower,linear);iaxpy(w.residual,w.upper,linear);
  for(int lane=0;lane<B;++lane)tail[lane]=au(tail[lane],mu(mag(node.u),au(tp[lane],tm[lane])));
 }
 auto inner_n=norm2(w.residual,g.d,0,g.start[L+1]);
 auto outer_n=norm2(w.residual,g.d,g.start[L+1]);
 Defect out;for(int lane=0;lane<B;++lane){out.time_node[lane]=su(inner_n[lane].hi);out.projection_node[lane]=su(outer_n[lane].hi);out.guard[lane]=su(au(inner_n[lane].hi,outer_n[lane].hi));out.tail[lane]=tail[lane];if(!std::isfinite(out.guard[lane])||!std::isfinite(tail[lane]))throw std::runtime_error("nonfinite full-space defect bound");}return out;
}

// A ball encloses one true complex vector per SIMD lane. N encloses the norm
// of the stored center, not the unknown true vector. All scalar bounds below
// use embedded directed arithmetic; ordinary center arithmetic is non-FMA RN.
struct Ball {V v;std::array<double,B> e{},N{};explicit Ball(int d=0):v(2*d*B){};};
struct BWork {Ball term,temp,dp,dm,lower,upper,value,derivative,residual,aux,coefficient,pvalue,pderivative;
 explicit BWork(int d,int polynomial_dimension):term(d),temp(d),dp(d),dm(d),lower(d),upper(d),value(d),derivative(d),residual(d),aux(d),coefficient(polynomial_dimension),pvalue(polynomial_dimension),pderivative(polynomial_dimension){};};
void bzero(Ball&a){std::fill(a.v.begin(),a.v.end(),0);a.e.fill(0);a.N.fill(0);}
AVX std::array<I,B> center_norm2(const V&x,int d,int begin=0,int end=-1){
 if(end<0)end=d;
 auto lo=_mm512_setzero_pd(),hi=lo;
 for(int n=begin;n<end;++n)for(int part=0;part<2;++part){auto a=_mm512_loadu_pd(&x[(part*d+n)*B]);
  if(_mm512_cmp_pd_mask(_mm512_abs_pd(a),_mm512_set1_pd(std::numeric_limits<double>::infinity()),_CMP_LT_OQ)!=255)throw std::runtime_error("nonfinite ball center");
  lo=_mm512_add_round_pd(lo,_mm512_mul_round_pd(a,a,RD),RD);hi=_mm512_add_round_pd(hi,_mm512_mul_round_pd(a,a,RU),RU);
 }
 double l[B],h[B];_mm512_storeu_pd(l,lo);_mm512_storeu_pd(h,hi);std::array<I,B>r{};for(int lane=0;lane<B;++lane)r[lane]={l[lane],h[lane]};return r;
}
AVX void btighten(Ball&a,int d){auto n=center_norm2(a.v,d);for(int lane=0;lane<B;++lane){a.N[lane]=su(n[lane].hi);if(!std::isfinite(a.e[lane])||a.e[lane]<0)throw std::runtime_error("invalid normwise ball");}}
AVX void bembed(Ball&out,const V&x,int d,int g){bzero(out);for(int n=0;n<d;++n)for(int lane=0;lane<B;++lane){out.v[n*B+lane]=x[n*B+lane];out.v[(g+n)*B+lane]=x[(d+n)*B+lane];}btighten(out,g);}
struct Round {double gamma,U;};
AVX Round rounding(int d,int operations){
 double ku=mu(double(operations),0x1p-53),den=ad(1,-ku);if(den<=0)throw std::runtime_error("roundoff operation domain");
 return {du(ku,den),du(mu(su(double(2*d)),mu(double(operations),std::numeric_limits<double>::denorm_min())),den)};
}
struct Coefficient {C center;double absolute,radius;};
AVX Coefficient coefficient(Z a){check(a);C c=mid(a);Z difference=add(a,neg(exact(c)));return {c,absz(exact(c)).hi,absz(difference).hi};}
AVX void bpropagate(Ball&out,const Ball&in,double S,double E,int q,int d){
 Round r=rounding(d,4*q+8);double rho=mu(su(2),mu(r.gamma,S));
 for(int lane=0;lane<B;++lane){out.e[lane]=au(au(mu(au(S,E),in.e[lane]),mu(au(E,rho),in.N[lane])),r.U);out.N[lane]=au(mu(au(S,rho),in.N[lane]),r.U);}
}
// Real scalar multiply/add, including uncertain operands. The input centers
// and radii are snapshotted before overwriting, so out may alias x or y.
AVX void bhorner(Ball&out,const Ball&x,I scalar,const Ball&y,int d){
 const auto xe=x.e,xn=x.N,ye=y.e,yn=y.N;double a=mid(scalar),aa=std::abs(a),rt=mag(sub(scalar,exact(a)));Round r=rounding(d,2);
 auto av=_mm512_set1_pd(a);for(size_t k=0;k<out.v.size();k+=B)_mm512_storeu_pd(&out.v[k],_mm512_add_pd(_mm512_mul_pd(av,_mm512_loadu_pd(&x.v[k])),_mm512_loadu_pd(&y.v[k])));
 for(int lane=0;lane<B;++lane){double base=au(mu(aa,xn[lane]),yn[lane]),local=au(mu(r.gamma,base),r.U);out.e[lane]=au(au(au(mu(au(aa,rt),xe[lane]),ye[lane]),mu(rt,xn[lane])),local);out.N[lane]=au(base,local);}
}
AVX void bscale(Ball&out,I scalar,int d){
 double a=mid(scalar),aa=std::abs(a),rt=mag(sub(scalar,exact(a)));Round r=rounding(d,1);
 auto av=_mm512_set1_pd(a);for(size_t k=0;k<out.v.size();k+=B)_mm512_storeu_pd(&out.v[k],_mm512_mul_pd(av,_mm512_loadu_pd(&out.v[k])));
 for(int lane=0;lane<B;++lane){double base=mu(aa,out.N[lane]),local=au(mu(r.gamma,base),r.U);out.e[lane]=au(au(mu(au(aa,rt),out.e[lane]),mu(rt,out.N[lane])),local);out.N[lane]=au(base,local);}
}
AVX void bcaxpy(Ball&out,const Ball&x,Z scalar,int d){
 const auto xe=x.e,xn=x.N,oe=out.e,on=out.N;auto c=coefficient(scalar);Round r=rounding(d,12);
 auto ar=_mm512_set1_pd(c.center.real()),ai=_mm512_set1_pd(c.center.imag());
 for(int n=0;n<d;++n){int a=n*B,b=(d+n)*B;auto xr=_mm512_loadu_pd(&x.v[a]),xi=_mm512_loadu_pd(&x.v[b]),yr=_mm512_loadu_pd(&out.v[a]),yi=_mm512_loadu_pd(&out.v[b]);
  _mm512_storeu_pd(&out.v[a],_mm512_add_pd(yr,_mm512_sub_pd(_mm512_mul_pd(ar,xr),_mm512_mul_pd(ai,xi))));_mm512_storeu_pd(&out.v[b],_mm512_add_pd(yi,_mm512_add_pd(_mm512_mul_pd(ar,xi),_mm512_mul_pd(ai,xr))));
 }
 for(int lane=0;lane<B;++lane){double product=mu(c.absolute,xn[lane]),local=au(mu(r.gamma,au(on[lane],mu(su(2),product))),r.U);out.e[lane]=au(au(au(oe[lane],mu(au(c.absolute,c.radius),xe[lane])),mu(c.radius,xn[lane])),local);out.N[lane]=au(au(on[lane],product),local);}
}
AVX void bmode_exp(const Basis&g,const Ball&x,Ball&out,Z beta,int mode,bool creation,int support){
 const int cutoff=creation?g.L:support;
 std::array<Z,vm::MAX_G+1>power{};power[0]=exact(C(1));for(int k=1;k<=cutoff;++k)power[k]=mul(power[k-1],beta);
 std::array<std::array<C,vm::MAX_G+1>,vm::MAX_G+1>table{};
 std::array<double,vm::MAX_G+1>rows{},cols{},erows{},ecols{};
 for(int n=0;n<=cutoff;++n){rows[n]=au(rows[n],1);cols[n]=au(cols[n],1);
  for(int k=1;k<=(creation?n:cutoff-n);++k){auto c=coefficient(scale(power[k],creation?g.cr[n][k]:g.an[n][k]));table[n][k]=c.center;int input=creation?n-k:n+k;
   rows[n]=au(rows[n],c.absolute);cols[input]=au(cols[input],c.absolute);erows[n]=au(erows[n],c.radius);ecols[input]=au(ecols[input],c.radius);
  }
 }
 double S=su(mu(*std::max_element(rows.begin(),rows.end()),*std::max_element(cols.begin(),cols.end()))),E=su(mu(*std::max_element(erows.begin(),erows.end()),*std::max_element(ecols.begin(),ecols.end())));
 int end=creation?g.d:g.start[support+1];
 // Creation overwrites every entry. Annihilation overwrites its full support;
 // only its untouched guard complement must be cleared after buffer reuse.
 if(!creation){std::fill(out.v.begin()+end*B,out.v.begin()+g.d*B,0);std::fill(out.v.begin()+(g.d+end)*B,out.v.end(),0);}
 for(int n=0;n<end;++n){auto re=_mm512_loadu_pd(&x.v[n*B]),im=_mm512_loadu_pd(&x.v[(g.d+n)*B]);int row=n,count=creation?g.n[n][mode]:support-g.degree[n];
  for(int k=1;k<=count;++k){row=creation?g.down[row][mode]:g.up[row][mode];if(row<0)throw std::runtime_error("ball mode index");C c=table[g.n[n][mode]][k];auto cr=_mm512_set1_pd(c.real()),ci=_mm512_set1_pd(c.imag()),xr=_mm512_loadu_pd(&x.v[row*B]),xi=_mm512_loadu_pd(&x.v[(g.d+row)*B]);
   re=_mm512_add_pd(re,_mm512_sub_pd(_mm512_mul_pd(cr,xr),_mm512_mul_pd(ci,xi)));im=_mm512_add_pd(im,_mm512_add_pd(_mm512_mul_pd(cr,xi),_mm512_mul_pd(ci,xr)));
  }_mm512_storeu_pd(&out.v[n*B],re);_mm512_storeu_pd(&out.v[(g.d+n)*B],im);
 }
 bpropagate(out,x,S,E,cutoff+1,g.d);
}
AVX std::array<double,B> bdisplacement(const Basis&g,const Ball&x,Ball&out,const std::array<Z,M>&beta,I gaussian,int L,const std::array<I,vm::MAX_L+1>*tail,BWork&w){
 if(&x==&out||&x==&w.term||&x==&w.temp||&out==&w.term||&out==&w.temp)throw std::runtime_error("ball displacement alias");
 bmode_exp(g,x,w.term,neg(conjz(beta[0])),0,false,L);
 for(int m=1;m<M;++m){bmode_exp(g,w.term,w.temp,neg(conjz(beta[m])),m,false,L);std::swap(w.term,w.temp);}
 std::array<double,B>outside{};double tailsq=0;
 if(tail){for(int l=0;l<=L;++l){auto n=center_norm2(w.term.v,g.d,g.start[l],g.start[l+1]);double t=(*tail)[l].hi;tailsq=au(tailsq,mu(t,t));for(int lane=0;lane<B;++lane)outside[lane]=au(outside[lane],mu(t,su(n[lane].hi)));}
  for(int lane=0;lane<B;++lane)outside[lane]=au(outside[lane],mu(su(tailsq),w.term.e[lane]));
 }
 for(int m=0;m<M;++m){bmode_exp(g,w.term,w.temp,beta[m],m,true,g.L);std::swap(w.term,w.temp);}std::swap(out,w.term);bscale(out,gaussian,g.d);return outside;
}
AVX void ball_ladder(const Basis&g,const Ball&x,Ball&out,const std::array<Z,M>&coef,bool creation,int L){
 std::array<std::array<C,vm::MAX_G+2>,M>table{};double S=0,E=0;
 for(int m=0;m<M;++m){double sm=0,em=0;for(int k=0;k<=L+1;++k){auto c=coefficient(scale(coef[m],g.roots[k]));table[m][k]=c.center;sm=std::max(sm,c.absolute);em=std::max(em,c.radius);}S=au(S,sm);E=au(E,em);}
 std::fill(out.v.begin(),out.v.end(),0);int end=g.start[creation?L+2:L];
 for(int n=0;n<end;++n){auto re=_mm512_setzero_pd(),im=re;
  for(int m=0;m<M;++m){int row=creation?g.down[n][m]:g.up[n][m];if(row<0||g.degree[row]>L)continue;C c=table[m][g.n[n][m]+(creation?0:1)];auto cr=_mm512_set1_pd(c.real()),ci=_mm512_set1_pd(c.imag()),xr=_mm512_loadu_pd(&x.v[row*B]),xi=_mm512_loadu_pd(&x.v[(g.d+row)*B]);re=_mm512_add_pd(re,_mm512_sub_pd(_mm512_mul_pd(cr,xr),_mm512_mul_pd(ci,xi)));im=_mm512_add_pd(im,_mm512_add_pd(_mm512_mul_pd(cr,xi),_mm512_mul_pd(ci,xr)));}
  _mm512_storeu_pd(&out.v[n*B],re);_mm512_storeu_pd(&out.v[(g.d+n)*B],im);
 }bpropagate(out,x,S,E,M,g.d);
}
using PolyNorms=std::array<std::array<double,B>,6>;
AVX PolyNorms polynomial_norms(const Work&w,int d){PolyNorms result{};for(int j=0;j<6;++j){auto n=center_norm2(w.poly[j],d);for(int lane=0;lane<B;++lane)result[j][lane]=su(n[lane].hi);}return result;}
void embed_coefficient(Ball&out,const V&x,int d,int g,const std::array<double,B>&N){
 if(d==g){out.v=x;out.e.fill(0);}else{bzero(out);for(int n=0;n<d;++n)for(int lane=0;lane<B;++lane){out.v[n*B+lane]=x[n*B+lane];out.v[(g+n)*B+lane]=x[(d+n)*B+lane];}}out.N=N;
}
void embed_ball(Ball&out,const Ball&x,int d,int g){
 if(&out==&x||int(x.v.size())!=2*d*B||int(out.v.size())!=2*g*B)throw std::runtime_error("polynomial ball embedding domain");
 for(int n=0;n<d;++n)for(int lane=0;lane<B;++lane){out.v[n*B+lane]=x.v[n*B+lane];out.v[(g+n)*B+lane]=x.v[(d+n)*B+lane];}
 std::fill(out.v.begin()+d*B,out.v.begin()+g*B,0);std::fill(out.v.begin()+(g+d)*B,out.v.end(),0);out.e=x.e;out.N=x.N;
}
AVX void bpolynomial(const Work&w,int d,int g,I x,I h,const PolyNorms&norms,BWork&bw){
 bzero(bw.pvalue);bzero(bw.pderivative);
 // All exact polynomial coefficients are in P_L. Center operations retain
 // the same order there; g deliberately retains the old conservative U_G.
 for(int q=5;q>=0;--q){bhorner(bw.pderivative,bw.pderivative,x,bw.pvalue,g);embed_coefficient(bw.coefficient,w.poly[q],d,d,norms[q]);bhorner(bw.pvalue,bw.pvalue,x,bw.coefficient,g);}
 bscale(bw.pderivative,divi(exact(1),h),g);btighten(bw.pvalue,d);btighten(bw.pderivative,d);embed_ball(bw.value,bw.pvalue,d,g);embed_ball(bw.derivative,bw.pderivative,d,g);
}
struct BallDefect {std::array<double,B>guard{},tail{},time_node{},projection_node{},arithmetic{};};
AVX BallDefect bdefect(const vm::Prepared&p,const Basis&g,const vm::Node&node,int L,BWork&w){
 bzero(w.residual);bcaxpy(w.residual,w.derivative,exact(C(0,1)),g.d);std::array<double,B>tail{};
 for(int j=0;j<2;++j){if(!node.active[j])continue;std::array<Z,M> beta,negative,ann,create;for(int m=0;m<M;++m){beta[m]=node.beta[j][m];negative[m]=neg(beta[m]);create[m]=mul(exact(C(0,-1)),beta[m]);ann[m]=conjz(create[m]);}
  auto tp=bdisplacement(g,w.value,w.dp,beta,node.gaussian[j],L,&p.tail[j],w);auto tm=bdisplacement(g,w.value,w.dm,negative,node.gaussian[j],L,&p.tail[j],w);
  ball_ladder(g,w.value,w.lower,ann,false,L);ball_ladder(g,w.value,w.upper,create,true,L);
  I twice=mul(exact(2),node.u);Z cp=scale(mul(exact(C(0,-0.5)),node.phase[j]),neg(twice)),cm=scale(mul(exact(C(0,0.5)),conjz(node.phase[j])),neg(twice));
  bcaxpy(w.residual,w.dp,cp,g.d);bcaxpy(w.residual,w.dm,cm,g.d);
  I diagonal=mul(twice,add(node.sn[j],mul(node.cs[j],node.mean[j]))),linear=mul(twice,node.cs[j]);bcaxpy(w.residual,w.value,{diagonal,exact(0)},g.d);bcaxpy(w.residual,w.lower,{linear,exact(0)},g.d);bcaxpy(w.residual,w.upper,{linear,exact(0)},g.d);
  for(int lane=0;lane<B;++lane)tail[lane]=au(tail[lane],mu(mag(node.u),au(tp[lane],tm[lane])));
 }
 auto inner_n=center_norm2(w.residual.v,g.d,0,g.start[L+1]),outer_n=center_norm2(w.residual.v,g.d,g.start[L+1]);BallDefect out;
 for(int lane=0;lane<B;++lane){double e=w.residual.e[lane];out.arithmetic[lane]=e;out.time_node[lane]=au(su(inner_n[lane].hi),e);out.projection_node[lane]=au(su(outer_n[lane].hi),e);out.guard[lane]=au(su(au(inner_n[lane].hi,outer_n[lane].hi)),e);out.tail[lane]=tail[lane];if(!std::isfinite(out.guard[lane])||!std::isfinite(tail[lane]))throw std::runtime_error("nonfinite ball defect bound");}return out;
}

AVX void hermite_step(const Basis&b,V&y,const vm::Cell&cell,Work&w){
 const double h=mid(cell.h),delta=h/128;w.initial=y;
 generator(b,y,w.k1,cell.stage[0],w);w.stage=y;axpy(w.stage,w.k1,h/2);
 generator(b,w.stage,w.k2,cell.stage[1],w);w.stage=y;axpy(w.stage,w.k2,h/2);
 generator(b,w.stage,w.k3,cell.stage[1],w);w.stage=y;axpy(w.stage,w.k3,h);
 generator(b,w.stage,w.k4,cell.stage[2],w);axpy(y,w.k1,h/6);axpy(y,w.k2,h/3);axpy(y,w.k3,h/3);axpy(y,w.k4,h/6);
 generator(b,y,w.f1,cell.stage[2],w);
 w.trial=w.initial;axpy(w.trial,w.k1,delta);generator(b,w.trial,w.a0,cell.stage[4],w);
 w.trial=w.initial;axpy(w.trial,w.k1,-delta);generator(b,w.trial,w.aux,cell.stage[3],w);axpy(w.a0,w.aux,-1);
 w.trial=y;axpy(w.trial,w.f1,delta);generator(b,w.trial,w.a1,cell.stage[6],w);
 w.trial=y;axpy(w.trial,w.f1,-delta);generator(b,w.trial,w.aux,cell.stage[5],w);axpy(w.a1,w.aux,-1);
 for(size_t k=0;k<y.size();++k){double c0=w.initial[k],c1=h*w.k1[k],c2=(h*h/(4*delta))*w.a0[k];
  double aa=y[k]-c0-c1-c2,bb=h*w.f1[k]-c1-2*c2,cc=(h*h/(2*delta))*w.a1[k]-2*c2;
  w.poly[0][k]=c0;w.poly[1][k]=c1;w.poly[2][k]=c2;w.poly[3][k]=10*aa-4*bb+cc/2;w.poly[4][k]=-15*aa+7*bb-cc;w.poly[5][k]=6*aa-3*bb+cc/2;
  if(!std::isfinite(y[k]))throw std::runtime_error("nonfinite candidate trajectory");
 }
}
struct Certificate {std::array<double,B> guard{},tail{},tube{},jumps{},total{},max_node{},max_norm_error{},sampled_time_node_L2{},sampled_projection_node_L2{},sampled_arithmetic_node_L2{};};
AVX void certify(const vm::Prepared&p,const Basis&b,const Basis&g,const vm::Cell&cell,const V&endpoint,const Work&w,BWork&bw,Certificate&c){
 std::array<double,B> qg{},qt{},qtime{},qprojection{},qarithmetic{};const auto norms=polynomial_norms(w,b.d);
 for(int j=0;j<16;++j){bpolynomial(w,b.d,g.d,cell.x[j],cell.h,norms,bw);auto bound=bdefect(p,g,cell.gauss[j],b.L,bw);
  for(int lane=0;lane<B;++lane){qg[lane]=au(qg[lane],mu(cell.w[j].hi,mu(bound.guard[lane],bound.guard[lane])));qt[lane]=au(qt[lane],mu(cell.w[j].hi,mu(bound.tail[lane],bound.tail[lane])));qtime[lane]=au(qtime[lane],mu(cell.w[j].hi,mu(bound.time_node[lane],bound.time_node[lane])));qprojection[lane]=au(qprojection[lane],mu(cell.w[j].hi,mu(bound.projection_node[lane],bound.projection_node[lane])));qarithmetic[lane]=au(qarithmetic[lane],mu(cell.w[j].hi,mu(bound.arithmetic[lane],bound.arithmetic[lane])));c.max_node[lane]=std::max(c.max_node[lane],au(bound.guard[lane],bound.tail[lane]));}
 }
 // On the Bernstein ellipse of [0,1], |x| <= 1/2+(rho+rho^-1)/4.
 I rho=exact(cell.rho);double radius=add(exact(0.5),divi(add(rho,divi(exact(1),rho)),exact(4))).hi;
 std::array<double,B> pn{},dn{};double power=1,previous=1;
 for(int j=0;j<6;++j){
  for(int lane=0;lane<B;++lane){double v=norms[j][lane];pn[lane]=au(pn[lane],mu(power,v));if(j)dn[lane]=au(dn[lane],mu(mu(double(j),previous),v));}
  previous=power;power=mu(power,radius);
 }
 double factor=4;for(int j=0;j<15;++j)factor=du(factor,cell.rho);factor=du(factor,ad(cell.rho,-1));
 for(int lane=0;lane<B;++lane){double Mbound=au(du(dn[lane],cell.h.lo),mu(cell.h_rho.hi,pn[lane]));
  c.guard[lane]=au(c.guard[lane],mu(cell.h.hi,su(qg[lane])));c.tail[lane]=au(c.tail[lane],mu(cell.h.hi,su(qt[lane])));c.tube[lane]=au(c.tube[lane],mu(cell.h.hi,mu(factor,Mbound)));
  // These two node-quadrature diagnostics do not separately enclose continuous
  // time integrals. The analytic continuum allowance belongs to the combined
  // defect above; only that combined defect enters the certificate total.
  c.sampled_time_node_L2[lane]=au(c.sampled_time_node_L2[lane],mu(cell.h.hi,su(qtime[lane])));
  c.sampled_projection_node_L2[lane]=au(c.sampled_projection_node_L2[lane],mu(cell.h.hi,su(qprojection[lane])));
  // Already included in guard; this is not an additional total or an
  // independent continuous-time certificate. Includes coefficient uncertainty.
  c.sampled_arithmetic_node_L2[lane]=au(c.sampled_arithmetic_node_L2[lane],mu(cell.h.hi,su(qarithmetic[lane])));
 }
 // Includes the final jump to the serialized endpoint, not only interior jumps.
 bpolynomial(w,b.d,g.d,exact(1),cell.h,norms,bw);bembed(bw.aux,endpoint,b.d,g.d);bcaxpy(bw.value,bw.aux,exact(C(-1)),g.d);auto jump=center_norm2(bw.value.v,g.d),en=center_norm2(endpoint,b.d);
 for(int lane=0;lane<B;++lane){c.jumps[lane]=au(c.jumps[lane],au(su(jump[lane].hi),bw.value.e[lane]));c.total[lane]=au(au(c.guard[lane],c.tail[lane]),au(c.tube[lane],c.jumps[lane]));check(exact(c.total[lane]));
  c.max_norm_error[lane]=std::max(c.max_norm_error[lane],std::max(std::abs(en[lane].lo-1),std::abs(en[lane].hi-1)));if(en[lane].hi>4)throw std::runtime_error("unstable candidate norm");
 }
}

double factorial(int n){double a=1;for(int k=2;k<=n;++k)a*=k;return a;}
C dense_element(const Basis&b,int n,int m,const std::array<C,M>&beta){C result=1;double norm=0;
 for(int i=0;i<M;++i){C sum=0;int a=b.n[n][i],bb=b.n[m][i];for(int j=0;j<=std::min(a,bb);++j)sum+=std::pow(beta[i],a-j)*std::pow(-std::conj(beta[i]),bb-j)/(factorial(j)*factorial(a-j)*factorial(bb-j));result*=std::sqrt(factorial(a)*factorial(bb))*sum;norm+=std::norm(beta[i]);}return std::exp(-norm/2)*result;
}
AVX std::array<Z,B> inner(const IV&left,const IV&right,int d){std::array<Z,B> z{};
 for(int n=0;n<d;++n)for(int lane=0;lane<B;++lane){int r=n*B+lane,i=(d+n)*B+lane;Z a{{left.lo[r],left.hi[r]},{left.lo[i],left.hi[i]}},bb{{right.lo[r],right.hi[r]},{right.lo[i],right.hi[i]}};z[lane]=add(z[lane],mul(conjz(a),bb));}
 return z;
}
AVX double ball_reference_enclosure(const Ball&ball,const IV&reference,int d){
 IV difference(d);for(int n=0;n<2*d;++n){auto c=_mm512_loadu_pd(&ball.v[n*B]);save(difference,n*B,vs(load(reference,n*B),R{c,c}));}auto norm=norm2(difference,d);double ratio=0;
 for(int lane=0;lane<B;++lane){double needed=su(norm[lane].hi);if(needed>ball.e[lane])throw std::runtime_error("ball does not contain independent interval fixture");if(ball.e[lane]>0)ratio=std::max(ratio,du(needed,ball.e[lane]));}return ratio;
}
AVX double ball_fixtures(const vm::Prepared&p){
 Basis b(2,p),g(4,p);Work w(b.d);BWork bw(g.d,b.d);IWork iw(g.d);V x(2*b.d*B);double ratio=0;
 for(int n=0;n<b.d;++n)for(int lane=0;lane<B;++lane)put(x,b.d,n,lane,C((n+lane)%7-3,(2*n+lane)%5-2)/32.);
 bembed(bw.value,x,b.d,g.d);embed(iw.value,x,b.d,g.d);std::array<Z,M>beta{};
 bdisplacement(g,bw.value,bw.dp,beta,exact(1),b.L,nullptr,bw);idisplacement(g,iw.value,iw.dp,beta,exact(1),b.L,nullptr,iw);ratio=std::max(ratio,ball_reference_enclosure(bw.dp,iw.dp,g.d));
 const vm::Node&node=p.cells[0].at(0).stage[0];for(int m=0;m<M;++m)beta[m]=node.beta[0][m];
 bdisplacement(g,bw.value,bw.dp,beta,node.gaussian[0],b.L,nullptr,bw);idisplacement(g,iw.value,iw.dp,beta,node.gaussian[0],b.L,nullptr,iw);ratio=std::max(ratio,ball_reference_enclosure(bw.dp,iw.dp,g.d));
 for(bool creation:{false,true}){ball_ladder(g,bw.value,bw.lower,beta,creation,b.L);iladder(g,iw.value,iw.lower,beta,creation,1,creation?g.L:b.L);ratio=std::max(ratio,ball_reference_enclosure(bw.lower,iw.lower,g.d));}
 for(int q=0;q<6;++q)for(size_t k=0;k<x.size();++k)w.poly[q][k]=x[k]/double(1<<(q+1));
 auto norms=polynomial_norms(w,b.d);I theta{0.125,0.125+0x1p-52},h{0.25,0.25+0x1p-52};bpolynomial(w,b.d,g.d,theta,h,norms,bw);polynomial(w,b.d,g.d,theta,h,iw.value,iw.derivative);
 ratio=std::max(ratio,ball_reference_enclosure(bw.value,iw.value,g.d));ratio=std::max(ratio,ball_reference_enclosure(bw.derivative,iw.derivative,g.d));
 // Guard-only comparison: prepared tail tables belong to the full campaign G,
 // so these small fixtures neither validate nor use their outside-tail values.
 bdefect(p,g,node,b.L,bw);defect(p,g,node,b.L,iw);ratio=std::max(ratio,ball_reference_enclosure(bw.residual,iw.residual,g.d));return ratio;
}
struct Fixtures {double dense_error=0,collective_error=0,ball_reference_ratio=0;bool directed=false,zero=false,adjoint=false;};
Fixtures fixtures(const vm::Prepared&p){
 Fixtures f;I a=add(exact(1),exact(0x1p-53));if(a.lo!=1||a.hi!=1+0x1p-52)throw std::runtime_error("directed add fixture");I z=mul(exact(1-0x1p-26),exact(1+0x1p-26));if(z.lo!=1-0x1p-52||z.hi!=z.lo)throw std::runtime_error("directed multiply fixture");f.directed=true;
 I tiny=mul(exact(std::numeric_limits<double>::denorm_min()),exact(0.5));if(tiny.lo!=0||tiny.hi!=std::numeric_limits<double>::denorm_min()||!(rounding(1,1).U>0))throw std::runtime_error("gradual underflow enclosure fixture");
 Basis b(2,p);Work w(b.d);IWork iw(b.d);V x(2*b.d*B),y(x.size()),dp(x.size());
 for(int n=0;n<b.d;++n)for(int lane=0;lane<B;++lane){put(x,b.d,n,lane,C((n+lane)%7-3,(2*n+lane)%5-2)/32.);put(y,b.d,n,lane,C((n+3*lane)%11-5,(n+lane)%3-1)/32.);}
 std::array<Z,M> ibeta{};embed(iw.value,x,b.d,b.d);idisplacement(b,iw.value,iw.dp,ibeta,exact(1),2,nullptr,iw);
 for(size_t k=0;k<x.size();++k){if(iw.dp.lo[k]>x[k]||iw.dp.hi[k]<x[k])throw std::runtime_error("zero displacement enclosure");}
 f.zero=true;
 const vm::Node&node=p.cells[0].at(0).stage[0];std::array<C,M>beta;for(int m=0;m<M;++m){ibeta[m]=node.beta[0][m];beta[m]=mid(ibeta[m]);}
 displacement(b,x,dp,beta,mid(node.gaussian[0]),w);
 collective_displacement(b,x,w.aux,beta,mid(node.gaussian[0]),w);for(size_t k=0;k<x.size();++k)f.collective_error=std::max(f.collective_error,std::abs(dp[k]-w.aux[k]));
 for(int n=0;n<b.d;++n)for(int lane=0;lane<B;++lane){C v=0;for(int m=0;m<b.d;++m)v+=dense_element(b,n,m,beta)*get(x,b.d,m,lane);f.dense_error=std::max(f.dense_error,std::abs(v-get(dp,b.d,n,lane)));}
 if(std::max(f.dense_error,f.collective_error)>1e-11)throw std::runtime_error("independent displacement fixture");
 idisplacement(b,iw.value,iw.dp,ibeta,node.gaussian[0],2,nullptr,iw);embed(iw.aux,y,b.d,b.d);auto left=inner(iw.aux,iw.dp,b.d);
 for(auto&v:ibeta){v=neg(v);}
 idisplacement(b,iw.aux,iw.dm,ibeta,node.gaussian[0],2,nullptr,iw);auto right=inner(iw.dm,iw.value,b.d);
 for(int lane=0;lane<B;++lane){I re=sub(left[lane].re,right[lane].re),im=sub(left[lane].im,right[lane].im);if(re.lo>0||re.hi<0||im.lo>0||im.hi<0)throw std::runtime_error("adjoint enclosure fixture");}f.adjoint=true;f.ball_reference_ratio=ball_fixtures(p);return f;
}
void json(I a){check(a);std::cout<<'['<<a.lo<<','<<a.hi<<']';}
void json(Z a){std::cout<<'[';json(a.re);std::cout<<',';json(a.im);std::cout<<']';}
void floating_environment(){unsigned x=_mm_getcsr();if(x&((1u<<15)|(1u<<6)|(3u<<13)))throw std::runtime_error("requires nearest rounding, gradual underflow, no DAZ/FTZ");}
const int LABELS[3][2]={{4,3},{4,4},{1,1}};

int main(int argc,char**argv){try{
 std::string input,output;int L=0,G=0,sub=0;
 for(int i=1;i<argc;i+=2){if(i+1>=argc)throw std::runtime_error("missing CLI value");std::string key=argv[i];if(key=="--input")input=argv[i+1];else if(key=="--output")output=argv[i+1];else if(key=="--cutoff")L=std::stoi(argv[i+1]);else if(key=="--guard")G=std::stoi(argv[i+1]);else if(key=="--steps")sub=std::stoi(argv[i+1]);else throw std::runtime_error("unknown CLI option");}
 bool allowed=(L==8&&G==10&&sub==512)||(L==10&&G==12&&sub==512)||(L==10&&G==12&&sub==1024)||(L==12&&G==14&&sub==1024);
 if(input.empty()||output.empty()||!allowed)throw std::runtime_error("outside frozen configuration domain");
 if constexpr(std::endian::native!=std::endian::little)throw std::runtime_error("little-endian endpoint format required");
 __builtin_cpu_init();if(!__builtin_cpu_supports("avx512f")||!__builtin_cpu_supports("avx512dq")||!__builtin_cpu_supports("avx512vl"))throw std::runtime_error("AVX512 unavailable");floating_environment();
 if(!std::filesystem::create_directory(output)){throw std::runtime_error("output directory must be new");}
 double start=omp_get_wtime();std::ofstream lifecycle(std::filesystem::path(output)/"lifecycle.jsonl");if(!lifecycle)throw std::runtime_error("lifecycle open failed");lifecycle<<std::setprecision(17)<<"{\"phase\":\"model_preparation_started\",\"elapsed_seconds\":0}\n";lifecycle.flush();
 vm::Prepared prepared=vm::prepare(input,L,G,sub);lifecycle<<"{\"phase\":\"model_preparation_completed\",\"elapsed_seconds\":"<<omp_get_wtime()-start<<"}\n";lifecycle.flush();
 Basis b(L,prepared),g(G,prepared);if(b.start[4]!=THERMAL)throw std::runtime_error("thermal basis mismatch");Fixtures fixture=fixtures(prepared);lifecycle<<"{\"phase\":\"fixtures_completed\",\"elapsed_seconds\":"<<omp_get_wtime()-start<<"}\n";lifecycle.flush();if(!lifecycle)throw std::runtime_error("lifecycle write failed");
 std::ofstream basisfile(std::filesystem::path(output)/"basis.json");basisfile<<"{\"cutoff\":"<<L<<",\"guard\":"<<G<<",\"thermal_cutoff\":3,\"occupations\":[";
 for(int n=0;n<b.d;++n){if(n)basisfile<<',';basisfile<<'[';for(int m=0;m<M;++m){if(m)basisfile<<',';basisfile<<b.n[n][m];}basisfile<<']';}basisfile<<"]}\n";basisfile.close();if(!basisfile)throw std::runtime_error("basis write failed");
 std::vector<V>states(CASES*BATCHES);std::vector<Certificate>certs(CASES*BATCHES);std::array<int,80>cpus{},places{};std::atomic<int>done{0},migrations{0};std::atomic<bool>failed{false};std::string failure;std::mutex lock;int workers=0;
 std::ofstream progress(std::filesystem::path(output)/"progress.jsonl");if(!progress)throw std::runtime_error("progress open failed");progress<<std::setprecision(17);double prep_seconds=omp_get_wtime()-start,scan0=omp_get_wtime();omp_set_dynamic(0);omp_set_num_threads(80);
 #pragma omp parallel
 {
  int tid=omp_get_thread_num();if(tid>=80)std::terminate();cpus[tid]=sched_getcpu();places[tid]=omp_get_place_num();
  #pragma omp single
  workers=omp_get_num_threads();
  Work w(b.d);BWork iw(g.d,b.d);
  #pragma omp for schedule(dynamic,1)
  for(int task=0;task<CASES*BATCHES;++task){if(failed.load())continue;try{floating_environment();int c=task/BATCHES,batch=task%BATCHES;V y(2*b.d*B);for(int lane=0;lane<B;++lane)put(y,b.d,batch*B+lane,lane,1);
    size_t completed_cells=0;for(const auto&cell:prepared.cells[c]){if(failed.load())break;hermite_step(b,y,cell,w);certify(prepared,b,g,cell,y,w,iw,certs[task]);++completed_cells;
     if(completed_cells%32==0){std::lock_guard<std::mutex>guard(lock);progress<<"{\"case\":"<<c<<",\"batch\":"<<batch<<",\"cells\":"<<completed_cells<<",\"total_cells\":"<<prepared.cells[c].size()<<",\"error_bound_max\":"<<*std::max_element(certs[task].total.begin(),certs[task].total.end())<<",\"elapsed_seconds\":"<<omp_get_wtime()-scan0<<"}\n";progress.flush();}
    }
    if(failed.load()){continue;}
    states[task]=std::move(y);int count=++done;std::lock_guard<std::mutex>guard(lock);progress<<"{\"completed\":"<<count<<",\"case\":"<<c<<",\"batch\":"<<batch<<",\"cells\":"<<completed_cells<<",\"error_bound_max\":"<<*std::max_element(certs[task].total.begin(),certs[task].total.end())<<",\"elapsed_seconds\":"<<omp_get_wtime()-scan0<<"}\n";progress.flush();if(!progress)throw std::runtime_error("progress write failed");
   }catch(const std::exception&e){std::lock_guard<std::mutex>guard(lock);failed=true;if(failure.empty())failure=e.what();}}
  if(cpus[tid]!=sched_getcpu())++migrations;
 }
 double kernel_seconds=omp_get_wtime()-scan0;progress.close();if(failed||done!=90)throw std::runtime_error("partial campaign: "+failure);if(workers!=80||migrations)throw std::runtime_error("worker count or migration");
 std::array<bool,80>seen{};for(int t=0;t<80;++t){if(cpus[t]<0||cpus[t]>=80||places[t]<0||places[t]>=80||seen[cpus[t]])throw std::runtime_error("invalid CPU placement");seen[cpus[t]]=true;}seen.fill(false);for(int t=0;t<80;++t){if(seen[places[t]])throw std::runtime_error("duplicate OpenMP place");seen[places[t]]=true;}
 std::ofstream endpoint(std::filesystem::path(output)/"endpoints.bin",std::ios::binary);for(int c=0;c<6;++c)for(int n=0;n<120;++n)for(int row=0;row<b.d;++row){C v=get(states[c*15+n/8],b.d,row,n%8);double pair[2]={v.real(),v.imag()};endpoint.write(reinterpret_cast<char*>(pair),sizeof(pair));}endpoint.close();if(!endpoint)throw std::runtime_error("endpoint write failed");
 std::array<double,6>errors{},norms{};std::array<std::array<double,7>,6>components{};I retained{};for(I weight:prepared.thermal)retained=add(retained,weight);IWork iw(b.d);
 for(int c=0;c<6;++c){double e2=0,n2=0;std::array<double,7>r{};
  for(int batch=0;batch<15;++batch){embed(iw.value,states[c*15+batch],b.d,b.d);auto nn=norm2(iw.value,b.d);auto&cert=certs[c*15+batch];
   for(int lane=0;lane<8;++lane){double w=prepared.thermal[batch*8+lane].hi;e2=au(e2,mu(w,mu(cert.total[lane],cert.total[lane])));n2=au(n2,mu(w,nn[lane].hi));double z[7]={cert.guard[lane],cert.tail[lane],cert.tube[lane],cert.jumps[lane],cert.sampled_time_node_L2[lane],cert.sampled_projection_node_L2[lane],cert.sampled_arithmetic_node_L2[lane]};for(int k=0;k<7;++k)r[k]=au(r[k],mu(w,mu(z[k],z[k])));}}
  errors[c]=su(e2);norms[c]=su(n2);for(int k=0;k<7;++k)components[c][k]=su(r[k]);
 }
 struct Pair {Z sine,linear;I center,interval;double numerical,thermal,arithmetic,total;};std::array<Pair,6> pairs;int index=0;
 for(int sign=0;sign<2;++sign)for(int a=0;a<3;++a)for(int bb=a+1;bb<3;++bb){int c=3*sign+a,d=3*sign+bb;Z overlap{};
  for(int batch=0;batch<15;++batch){embed(iw.value,states[c*15+batch],b.d,b.d);embed(iw.aux,states[d*15+batch],b.d,b.d);idisplacement(b,iw.value,iw.dp,prepared.delta[index],prepared.delta_gaussian[index],L,nullptr,iw);auto z=inner(iw.aux,iw.dp,b.d);for(int lane=0;lane<8;++lane)overlap=add(overlap,scale(z[lane],prepared.thermal[batch*8+lane]));}
  Pair&v=pairs[index];v.sine=mul(prepared.rotation[index],overlap);v.linear=prepared.linear_pair[index];v.center=divi(absz(add(v.sine,neg(v.linear))),exact(2));
  double retained_root=su(retained.hi);v.numerical=du(std::min(au(mu(errors[c],retained_root),mu(errors[d],norms[c])),au(mu(errors[d],retained_root),mu(errors[c],norms[d]))),2);v.thermal=du(prepared.thermal_tail.hi,2);v.arithmetic=du(au(v.center.hi,-v.center.lo),2);double radius=au(v.numerical,v.thermal);v.total=au(radius,v.arithmetic);
  v.interval={std::max(0.0,ad(v.center.lo,-radius)),std::min(1.0,au(v.center.hi,radius))};++index;
 }
 std::cout<<std::setprecision(17)<<"{\"status\":\"COMPLETED\",\"scope\":\"normwise_ball_full_space_defect\",\"cutoff\":"<<L<<",\"guard\":"<<G<<",\"dimension\":"<<b.d<<",\"guard_dimension\":"<<g.d<<",\"steps_per_segment\":"<<sub<<",\"thermal_columns\":120,\"thermal_cutoff\":3,\"cases\":6,\"threads\":80,\"preparation_seconds\":"<<prep_seconds<<",\"model_preparation_seconds\":"<<prepared.preparation_seconds<<",\"kernel_seconds\":"<<kernel_seconds<<",\"mpfr_version\":\""<<prepared.mpfr_version<<"\",\"legacy_eta_mismatch\":";json(prepared.legacy_eta_mismatch);std::cout<<",\"retained_thermal_weight\":";json(retained);std::cout<<",\"thermal_tail\":";json(prepared.thermal_tail);
 std::cout<<",\"fixtures\":{\"dense_displacement_error\":"<<fixture.dense_error<<",\"collective_displacement_error\":"<<fixture.collective_error<<",\"directed_arithmetic\":true,\"zero_displacement_enclosure\":true,\"adjoint_enclosure\":true,\"ball_interval_fixture_enclosure\":true,\"ball_reference_radius_ratio\":"<<fixture.ball_reference_ratio<<"},\"branches\":[";
 for(int c=0;c<6;++c){if(c)std::cout<<',';std::cout<<"{\"case\":"<<c<<",\"labels\":["<<LABELS[c%3][0]<<','<<LABELS[c%3][1]<<"],\"error_bound\":"<<errors[c]<<",\"weighted_endpoint_norm\":"<<norms[c]<<",\"guard_component\":"<<components[c][0]<<",\"tail_component\":"<<components[c][1]<<",\"continuum_component\":"<<components[c][2]<<",\"jump_component\":"<<components[c][3]<<",\"sampled_time_node_L2\":"<<components[c][4]<<",\"sampled_projection_node_L2\":"<<components[c][5]<<",\"sampled_arithmetic_node_L2\":"<<components[c][6]<<",\"node_split_scope\":\"diagnostic_quadrature_only_continuum_allowance_is_combined\",\"linear_phase\":";json(prepared.final[c].phase);std::cout<<",\"linear_alpha\":[";for(int m=0;m<7;++m){if(m)std::cout<<',';json(prepared.final[c].alpha[m]);}std::cout<<"],\"columns\":[";
  for(int n=0;n<120;++n){if(n)std::cout<<',';auto&v=certs[c*15+n/8];int lane=n%8;std::cout<<"{\"thermal_index\":"<<n<<",\"guard\":"<<v.guard[lane]<<",\"tail\":"<<v.tail[lane]<<",\"continuum\":"<<v.tube[lane]<<",\"jumps\":"<<v.jumps[lane]<<",\"total\":"<<v.total[lane]<<",\"sampled_time_node_L2\":"<<v.sampled_time_node_L2[lane]<<",\"sampled_projection_node_L2\":"<<v.sampled_projection_node_L2[lane]<<",\"sampled_arithmetic_node_L2\":"<<v.sampled_arithmetic_node_L2[lane]<<",\"maximum_node_bound\":"<<v.max_node[lane]<<",\"maximum_norm_error\":"<<v.max_norm_error[lane]<<'}';}std::cout<<"]}";
 }
 std::cout<<"],\"pair_coherences\":[";index=0;
 for(int sign=0;sign<2;++sign)for(int a=0;a<3;++a)for(int bb=a+1;bb<3;++bb){auto&v=pairs[index];if(index)std::cout<<',';std::cout<<"{\"cases\":["<<3*sign+a<<','<<3*sign+bb<<"],\"sine_retained_interval\":";json(v.sine);std::cout<<",\"linear_full_interval\":";json(v.linear);std::cout<<",\"witness_center_interval\":";json(v.center);std::cout<<",\"numerical_radius\":"<<v.numerical<<",\"thermal_radius\":"<<v.thermal<<",\"arithmetic_radius\":"<<v.arithmetic<<",\"total_radius\":"<<v.total<<",\"certified_trace_distance_interval\":";json(v.interval);std::cout<<'}';++index;}
 std::cout<<"],\"thread_map\":[";for(int t=0;t<80;++t){if(t)std::cout<<',';std::cout<<"{\"thread\":"<<t<<",\"cpu\":"<<cpus[t]<<",\"place\":"<<places[t]<<'}';}std::cout<<"],\"end_to_end_seconds\":"<<omp_get_wtime()-start<<"}\n";return 0;
}catch(const std::exception&e){std::cerr<<e.what()<<'\n';return 2;}}
