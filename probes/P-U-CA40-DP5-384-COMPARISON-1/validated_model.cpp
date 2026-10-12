// Copyright 2026 A. M. Thorn. SPDX-License-Identifier: Apache-2.0
// MPFR coefficient enclosures; this file never propagates a state vector.
#include "validated_model.hpp"
#include <mpfr.h>
#undef mpfr_version
#include <algorithm>
#include <cmath>
#include <fstream>
#include <mutex>
#include <stdexcept>
#include <utility>
#include <omp.h>
namespace vm { namespace {
constexpr mpfr_prec_t PREC=192;
struct R {
 mpfr_t l,u;
 R(){mpfr_init2(l,PREC);mpfr_init2(u,PREC);mpfr_set_zero(l,0);mpfr_set_zero(u,0);}
 R(long n):R(){mpfr_set_si(l,n,MPFR_RNDD);mpfr_set_si(u,n,MPFR_RNDU);}
 explicit R(const std::string&s):R(){if(mpfr_set_str(l,s.c_str(),10,MPFR_RNDD)||mpfr_set_str(u,s.c_str(),10,MPFR_RNDU))throw std::runtime_error("invalid decimal token");}
 R(const R&a):R(){mpfr_set(l,a.l,MPFR_RNDD);mpfr_set(u,a.u,MPFR_RNDU);}
 R(R&&a) noexcept:R(){mpfr_swap(l,a.l);mpfr_swap(u,a.u);}
 R&operator=(const R&a){if(this!=&a){mpfr_set(l,a.l,MPFR_RNDD);mpfr_set(u,a.u,MPFR_RNDU);}return *this;}
 R&operator=(R&&a) noexcept {mpfr_swap(l,a.l);mpfr_swap(u,a.u);return *this;}
 ~R(){mpfr_clear(l);mpfr_clear(u);}
};
R operator+(const R&a,const R&b){R o;mpfr_add(o.l,a.l,b.l,MPFR_RNDD);mpfr_add(o.u,a.u,b.u,MPFR_RNDU);return o;}
R operator-(const R&a,const R&b){R o;mpfr_sub(o.l,a.l,b.u,MPFR_RNDD);mpfr_sub(o.u,a.u,b.l,MPFR_RNDU);return o;}
R operator-(const R&a){R o;mpfr_neg(o.l,a.u,MPFR_RNDD);mpfr_neg(o.u,a.l,MPFR_RNDU);return o;}
R operator*(const R&a,const R&b){R o,t;mpfr_set_inf(o.l,1);mpfr_set_inf(o.u,-1);for(int i=0;i<2;++i)for(int j=0;j<2;++j){auto x=i?a.u:a.l;auto y=j?b.u:b.l;mpfr_mul(t.l,x,y,MPFR_RNDD);mpfr_mul(t.u,x,y,MPFR_RNDU);if(mpfr_less_p(t.l,o.l))mpfr_set(o.l,t.l,MPFR_RNDD);if(mpfr_greater_p(t.u,o.u))mpfr_set(o.u,t.u,MPFR_RNDU);}return o;}
R operator/(const R&a,const R&b){if(mpfr_sgn(b.l)<=0&&mpfr_sgn(b.u)>=0)throw std::runtime_error("interval denominator contains zero");R inv;mpfr_ui_div(inv.l,1,b.u,MPFR_RNDD);mpfr_ui_div(inv.u,1,b.l,MPFR_RNDU);return a*inv;}
R sqr(const R&a){R o;if(mpfr_sgn(a.l)>=0){mpfr_sqr(o.l,a.l,MPFR_RNDD);mpfr_sqr(o.u,a.u,MPFR_RNDU);}else if(mpfr_sgn(a.u)<=0){mpfr_sqr(o.l,a.u,MPFR_RNDD);mpfr_sqr(o.u,a.l,MPFR_RNDU);}else{R x;mpfr_sqr(x.l,a.l,MPFR_RNDU);mpfr_sqr(x.u,a.u,MPFR_RNDU);mpfr_set_zero(o.l,0);mpfr_max(o.u,x.l,x.u,MPFR_RNDU);}return o;}
R absr(const R&a){if(mpfr_sgn(a.l)>=0)return a;if(mpfr_sgn(a.u)<=0)return -a;R o;mpfr_set_zero(o.l,0);mpfr_neg(o.u,a.l,MPFR_RNDU);mpfr_max(o.u,o.u,a.u,MPFR_RNDU);return o;}
R root(const R&a){if(mpfr_sgn(a.l)<0)throw std::runtime_error("negative interval sqrt");R o;mpfr_sqrt(o.l,a.l,MPFR_RNDD);mpfr_sqrt(o.u,a.u,MPFR_RNDU);return o;}
R expr(const R&a){R o;mpfr_exp(o.l,a.l,MPFR_RNDD);mpfr_exp(o.u,a.u,MPFR_RNDU);return o;}
R trig(const R&a,bool cosine){R o,width;mpfr_sub(width.u,a.u,a.l,MPFR_RNDU);if(cosine){mpfr_cos(o.l,a.l,MPFR_RNDD);mpfr_cos(o.u,a.l,MPFR_RNDU);}else{mpfr_sin(o.l,a.l,MPFR_RNDD);mpfr_sin(o.u,a.l,MPFR_RNDU);}mpfr_sub(o.l,o.l,width.u,MPFR_RNDD);mpfr_add(o.u,o.u,width.u,MPFR_RNDU);if(mpfr_cmp_si(o.l,-1)<0)mpfr_set_si(o.l,-1,MPFR_RNDD);if(mpfr_cmp_si(o.u,1)>0)mpfr_set_si(o.u,1,MPFR_RNDU);return o;}
R sinr(const R&a){return trig(a,false);}R cosr(const R&a){return trig(a,true);}
R pi(){R o;mpfr_const_pi(o.l,MPFR_RNDD);mpfr_const_pi(o.u,MPFR_RNDU);return o;}
I small(const R&a){I o{mpfr_get_d(a.l,MPFR_RNDD),mpfr_get_d(a.u,MPFR_RNDU)};if(!std::isfinite(o.lo)||!std::isfinite(o.hi)||o.lo>o.hi)throw std::runtime_error("invalid binary64 interval");return o;}
struct C {R re,im;C()=default;C(R r,R i=R(0)):re(std::move(r)),im(std::move(i)){};};
C operator+(const C&a,const C&b){return {a.re+b.re,a.im+b.im};}
C operator-(const C&a,const C&b){return {a.re-b.re,a.im-b.im};}
C operator*(const C&a,const C&b){return {a.re*b.re-a.im*b.im,a.re*b.im+a.im*b.re};}
C operator*(const C&a,const R&b){return {a.re*b,a.im*b};}
C operator/(const C&a,const R&b){return {a.re/b,a.im/b};}
C conj(const C&a){return {a.re,-a.im};}
C minus_i(const C&a){return {a.im,-a.re};}
C cis(const R&a){return {cosr(a),sinr(a)};}
R norm(const C&a){return sqr(a.re)+sqr(a.im);}R mag(const C&a){return root(norm(a));}
Z small(const C&a){return {small(a.re),small(a.im)};}
bool iszero(const R&a){return mpfr_zero_p(a.l)&&mpfr_zero_p(a.u);}
C J(const R&a,const R&h){if(iszero(a))return {h,R(0)};return minus_i(cis(a*h)-C(R(1)))/a;}
C K(const R&a,const R&b,const R&h,bool same){if(same){if(iszero(a))return {sqr(h)/R(2),R(0)};return {norm(J(a,h))/R(2),h/a-sinr(a*h)/sqr(a)};}return minus_i(J(a,h)-J(a-b,h))/b;}
struct BigLinear {std::array<C,7>alpha;R phase;};
struct Input {
 R axial,offset,wavelength,hbar,mass,tau,nbar,k,mu,dt;
 std::array<R,7>omega,pos;
 std::array<std::array<R,7>,7>vectors,kap;
 std::array<std::array<C,7>,7>eta,legacy_eta;
 std::array<std::array<R,16>,2>amp;
 std::array<R,2>k2,b,gaussian;
};
Input read(const std::string&path){std::ifstream f(path);std::string version;f>>version;if(version!="EXACT-CA40-1")throw std::runtime_error("input format");auto get=[&](){std::string s;if(!(f>>s))throw std::runtime_error("short exact input");return R(s);};Input in;
 in.axial=get();in.offset=get();in.wavelength=get();in.hbar=get();in.mass=get();in.tau=get();in.nbar=get();
 if(mpfr_cmp(in.tau.l,R("0.0001").l)||mpfr_cmp(in.nbar.l,R("0.05").l))throw std::runtime_error("frozen timing/thermal value");
 for(auto&v:in.omega)v=get();
 for(auto&v:in.pos)v=get();
 for(auto&row:in.vectors)for(auto&v:row)v=get();
 for(auto&row:in.legacy_eta)for(auto&v:row){v.re=get();v.im=get();}
 for(auto&row:in.amp)for(auto&v:row)v=get();
 std::string extra;if(f>>extra)throw std::runtime_error("trailing exact input");
 in.k=R(2)*pi()/in.wavelength;in.mu=R(2)*pi()*(in.axial+in.offset);in.dt=in.tau/R(16);
 for(int m=0;m<7;++m)for(int i=0;i<7;++i){in.kap[m][i]=in.k*in.vectors[m][i]*root(in.hbar/(R(2)*in.mass*in.omega[m]));in.eta[m][i]=cis(in.k*in.pos[i])*in.kap[m][i];}
 for(int j=0;j<2;++j){for(int m=0;m<7;++m)in.k2[j]=in.k2[j]+sqr(in.kap[m][j+3]);in.b[j]=root(in.k2[j]);in.gaussian[j]=expr(-in.k2[j]/R(2));}return in;
}
constexpr int labels[3][2]={{4,3},{4,4},{1,1}};
struct Segment {int c,seg;int active[2];R u,t0;BigLinear initial;std::array<C,7>g,cm,cp;};
Segment segment(const Input&in,int c,int seg,const BigLinear&prefix){Segment s;s.c=c;s.seg=seg;s.u=in.amp[c/3][seg%16];s.t0=in.dt*R(seg);s.initial=prefix;for(int i=0;i<2;++i)s.active[i]=int((labels[c%3][i]+seg/16)%5==0);
 for(int m=0;m<7;++m){for(int j=0;j<2;++j)if(s.active[j])s.g[m]=s.g[m]+in.eta[m][j+3];s.cm[m]=s.g[m]*s.u*cis((in.omega[m]-in.mu)*s.t0);s.cp[m]=conj(s.g[m])*s.u*cis((in.omega[m]+in.mu)*s.t0);}return s;}
std::array<C,7> alpha_at(const Input&in,const Segment&s,const R&offset){auto a=s.initial.alpha;for(int m=0;m<7;++m)a[m]=a[m]+minus_i(s.cm[m]*J(in.omega[m]-in.mu,offset)+s.cp[m]*J(in.omega[m]+in.mu,offset));return a;}
BigLinear advance(const Input&in,const Segment&s,const R&h){BigLinear out=s.initial;if(!(s.active[0]||s.active[1]))return out;for(int m=0;m<7;++m){R a=in.omega[m]-in.mu,b=in.omega[m]+in.mu;C da=minus_i(s.cm[m]*J(a,h)+s.cp[m]*J(b,h));
 C area=s.cm[m]*conj(s.cm[m])*K(a,a,h,true)+s.cp[m]*conj(s.cp[m])*K(b,b,h,true)+s.cm[m]*conj(s.cp[m])*K(a,b,h,false)+s.cp[m]*conj(s.cm[m])*K(b,a,h,false);
 out.phase=out.phase+area.im+(da*conj(s.initial.alpha[m])).im;out.alpha[m]=out.alpha[m]+da;}return out;}
std::array<R,2> means(const Input&in,const std::array<C,7>&alpha,const R&t){std::array<R,2>out;for(int j=0;j<2;++j)for(int m=0;m<7;++m)out[j]=out[j]+R(2)*in.kap[m][j+3]*(alpha[m]*cis(-in.omega[m]*t)).re;return out;}
Node node(const Input&in,const Segment&s,const R&offset){Node out;R t=s.t0+offset;auto alpha=alpha_at(in,s,offset);auto mean=means(in,alpha,t);out.u=small(s.u);
 for(int j=0;j<2;++j){int i=j+3;R chi=in.k*in.pos[i]-in.mu*t;out.active[j]=s.active[j];out.cs[j]=small(cosr(chi));out.sn[j]=small(sinr(chi));out.mean[j]=small(mean[j]);out.phase[j]=small(cis(chi+mean[j]));out.k2[j]=small(in.k2[j]);out.gaussian[j]=small(in.gaussian[j]);out.beta_norm[j]=small(in.b[j]);for(int m=0;m<7;++m)out.beta[j][m]=small(C(R(0),in.kap[m][i])*cis(in.omega[m]*t));}return out;}
R tube(const Input&in,const Segment&s,const R&center,const R&h,int L){R rho(6),half=h/R(2),rad=half*(rho+R(1)/rho)/R(2),Y=half*(rho-R(1)/rho)/R(2);auto alpha=alpha_at(in,s,center);auto mean=means(in,alpha,s.t0+center);std::array<R,7>F,A;
 for(int m=0;m<7;++m){F[m]=mag(s.g[m]*s.u)*(expr(absr(in.omega[m]-in.mu)*Y)+expr((in.omega[m]+in.mu)*Y));A[m]=mag(alpha[m])+rad*F[m];}
 R out;for(int j=0;j<2;++j){if(!s.active[j])continue;R B2,Mprime;for(int m=0;m<7;++m){R e=expr(in.omega[m]*Y);B2=B2+sqr(in.kap[m][j+3])*sqr(e);Mprime=Mprime+R(2)*absr(in.kap[m][j+3])*e*(F[m]+in.omega[m]*A[m]);}
 R B=root(B2),D=expr(-in.k2[j]/R(2)+B2/R(2)+R(2)*B*root(R(L))),X=B*(root(R(L))+root(R(L+1)));
 out=out+R(2)*absr(s.u)*(D*expr(Y*(in.mu+Mprime))+expr(in.mu*Y)*(R(1)+absr(mean[j])+rad*Mprime+X));}return out;}
std::pair<R,R> legendre(const R&x){R a(1),b=x;for(int n=2;n<=16;++n){R c=(R(2*n-1)*x*b-R(n-1)*a)/R(n);a=std::move(b);b=std::move(c);}return {b,a};}
int sign(const R&a){return mpfr_sgn(a.l)>0?1:mpfr_sgn(a.u)<0?-1:0;}
std::array<std::pair<R,R>,16> gauss(){const char*seeds[]={"0.095012509837637440","0.281603550779258913","0.458016777657227386","0.617876244402643748","0.755404408355003034","0.865631202387831744","0.944575023073232576","0.989400934991649933"};std::array<std::pair<R,R>,16>out;
 for(int j=0;j<8;++j){R a=R(seeds[j])-R("0.00000000000001"),b=R(seeds[j])+R("0.00000000000001");R lo,hi;mpfr_set(lo.l,a.l,MPFR_RNDD);mpfr_set(lo.u,a.l,MPFR_RNDD);mpfr_set(hi.l,b.u,MPFR_RNDU);mpfr_set(hi.u,b.u,MPFR_RNDU);int sl=sign(legendre(lo).first),sh=sign(legendre(hi).first);if(!sl||!sh||sl==sh)throw std::runtime_error("Gauss root bracket");
  for(int k=0;k<100;++k){R mid;mpfr_add(mid.l,lo.l,hi.u,MPFR_RNDN);mpfr_div_2ui(mid.l,mid.l,1,MPFR_RNDN);mpfr_set(mid.u,mid.l,MPFR_RNDN);int sm=sign(legendre(mid).first);if(!sm)throw std::runtime_error("Gauss root sign indeterminate");if(sm==sl)lo=mid;else hi=mid;}
  R z;mpfr_set(z.l,lo.l,MPFR_RNDD);mpfr_set(z.u,hi.u,MPFR_RNDU);auto pp=legendre(z);R derivative=R(16)*(z*pp.first-pp.second)/(sqr(z)-R(1));R w=R(1)/((R(1)-sqr(z))*sqr(derivative));out[8+j]={(z+R(1))/R(2),w};out[7-j]={(R(1)-z)/R(2),w};
 }
 R sum;for(int j=0;j<16;++j){auto&v=out[j];if(mpfr_sgn(v.second.l)<=0)throw std::runtime_error("nonpositive Gauss weight");if(mpfr_sgn(v.first.l)<=0||mpfr_cmp_si(v.first.u,1)>=0)throw std::runtime_error("Gauss node outside open unit interval");if(j&&mpfr_cmp(out[j-1].first.u,v.first.l)>=0)throw std::runtime_error("Gauss roots not disjoint");sum=sum+v.second;}if(mpfr_cmp_si(sum.l,1)>0||mpfr_cmp_si(sum.u,1)<0)throw std::runtime_error("Gauss weights miss unity");return out;
}
R tail(const Input&in,int ion,int j,int G){int K0=G-j+1;R term(1);for(int k=1;k<=K0;++k)term=term*in.b[ion]*root(R(j+k))/R(k);R ratio=in.b[ion]*root(R(j+K0+1))/R(K0+1);if(mpfr_cmp_si(ratio.u,1)>=0)throw std::runtime_error("creation-tail ratio not below one");R upper=in.gaussian[ion]*term/(R(1)-ratio);R out;mpfr_set_zero(out.l,0);mpfr_set(out.u,upper.u,MPFR_RNDU);return out;}
long choose(int n,int k){long r=1;for(int i=1;i<=k;++i)r=r*(n+1-i)/i;return r;}
} // internal interval implementation
Prepared prepare(const std::string&path,int cutoff,int guard,int steps){
 if(cutoff<3||cutoff>MAX_L||guard<cutoff+1||guard>MAX_G||steps<=0)throw std::runtime_error("validated model configuration");
 if(!mpfr_buildopt_tls_p())throw std::runtime_error("MPFR thread-local support required");
 for(const char* text:{"0","0.1","-3.7","1000000"}){R z(text);R identity=sqr(sinr(z))+sqr(cosr(z));if(mpfr_cmp_si(identity.l,1)>0||mpfr_cmp_si(identity.u,1)<0)throw std::runtime_error("trigonometric interval identity fixture");}
 double started=omp_get_wtime();Input in=read(path);Prepared out;out.mpfr_version=mpfr_get_version();auto g=gauss();R h=in.dt/R(steps);std::array<BigLinear,6>final;std::vector<Segment>segments;
 for(int c=0;c<6;++c){BigLinear prefix;for(int seg=0;seg<80;++seg){Segment s=segment(in,c,seg,prefix);if(s.active[0]||s.active[1])segments.push_back(s);prefix=advance(in,s,in.dt);}final[c]=prefix;out.final[c].phase=small(prefix.phase);for(int m=0;m<7;++m)out.final[c].alpha[m]=small(prefix.alpha[m]);}
 for(int j=0;j<2;++j)for(int degree=0;degree<=cutoff;++degree)out.tail[j][degree]=small(tail(in,j,degree,guard));
 for(int n=0;n<MAX_G+2;++n)out.sqrt_n[n]=small(root(R(n)));
 R r=R(1)/R(21),base(1);for(int m=0;m<7;++m)base=base*R(20)/R(21);R retained;int idx=0;for(int degree=0;degree<=3;++degree){R weight=base;for(int k=0;k<degree;++k)weight=weight*r;for(long n=0;n<choose(degree+6,6);++n)out.thermal[idx++]=small(weight);retained=retained+weight*R(choose(degree+6,6));}if(idx!=120)throw std::runtime_error("thermal inventory");out.thermal_tail=small(R(1)-retained);
 R mismatch;for(int m=0;m<7;++m)for(int i=0;i<7;++i){R d=mag(in.eta[m][i]-in.legacy_eta[m][i]);if(mpfr_greater_p(d.u,mismatch.u))mpfr_set(mismatch.u,d.u,MPFR_RNDU);}out.legacy_eta_mismatch=small(mismatch);
 int pair=0;for(int sg=0;sg<2;++sg)for(int a=0;a<3;++a)for(int b=a+1;b<3;++b){int ca=3*sg+a,cb=3*sg+b;R theta=final[ca].phase-final[cb].phase,normdelta;for(int m=0;m<7;++m){C d=final[ca].alpha[m]-final[cb].alpha[m];out.delta[pair][m]=small(d);normdelta=normdelta+norm(d);theta=theta+(conj(final[cb].alpha[m])*final[ca].alpha[m]).im;}C rotation=cis(theta);out.rotation[pair]=small(rotation);out.linear_pair[pair]=small(rotation*expr(-(in.nbar+R(1)/R(2))*normdelta));out.delta_gaussian[pair]=small(expr(-normdelta/R(2)));out.delta_norm[pair]=small(root(normdelta));++pair;}
 std::array<int,6>counts{};struct Task{int segment,q,index;};std::vector<Task>tasks;for(int s=0;s<int(segments.size());++s){int c=segments[s].c;for(int q=0;q<steps;++q)tasks.push_back({s,q,counts[c]++});}for(int c=0;c<6;++c)out.cells[c].resize(counts[c]);
 std::mutex lock;std::string failure;bool failed=false;omp_set_dynamic(0);
 #pragma omp parallel for schedule(dynamic,16) num_threads(80)
 for(int task=0;task<int(tasks.size());++task){try{auto work=tasks[task];const auto&s=segments[work.segment];Cell cell;cell.h=small(h);
#if HIGHER_ORDER_CANDIDATE
  std::array<R,11>x={R(0),R(1)/R(10),R(3)/R(20),R(2)/R(5),R(4)/R(9),R(1)/R(2),R(3)/R(5),R(13)/R(20),R(9)/R(10),R(17)/R(18),R(1)};
  for(int k=0;k<11;++k)cell.stage[k]=node(in,s,(R(work.q)+x[k])*h);
#else
  std::array<R,7>x={R(0),R(1)/R(2),R(1),-R(1)/R(128),R(1)/R(128),R(1)-R(1)/R(128),R(1)+R(1)/R(128)};
  for(int k=0;k<7;++k)cell.stage[k]=node(in,s,(R(work.q)+x[k])*h);
#endif
  for(int k=0;k<16;++k){cell.x[k]=small(g[k].first);cell.w[k]=small(g[k].second);cell.gauss[k]=node(in,s,(R(work.q)+g[k].first)*h);}
  cell.h_rho=small(tube(in,s,(R(work.q)+R(1)/R(2))*h,h,cutoff));out.cells[s.c][work.index]=std::move(cell);
 }catch(const std::exception&e){std::lock_guard<std::mutex>guard_lock(lock);failed=true;if(failure.empty())failure=e.what();}}
 if(failed)throw std::runtime_error("coefficient enclosure failed: "+failure);
 out.preparation_seconds=omp_get_wtime()-started;return out;
}
} // namespace vm
