// Copyright 2026 A. M. Thorn. SPDX-License-Identifier: Apache-2.0
// Floating estimates of analytic envelopes; not interval certificates.
#include <algorithm>
#include <array>
#include <cmath>
#include <complex>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <limits>
#include <memory>
#include <stdexcept>
#include <string>
#include <vector>
#include <immintrin.h>
#include <omp.h>
#include <sched.h>

using C=std::complex<double>;
constexpr int M=7, NS=80, Q=256, NC=50, NT=NC*NS, NM=12;
constexpr double PI=3.141592653589793238462643383279502884;
constexpr double ATOL=1e-9, PTOL=1e-8;
const char* metric_names[NM]={"alpha_rwa_sample","alpha_linear_sample","alpha_difference_sample",
 "alpha_rwa_envelope","alpha_linear_envelope","alpha_difference_envelope",
 "ld_rms_sample","ld_rms_envelope","adjacent_rms_sample","adjacent_rms_envelope",
 "adjacent_coherent_sample","adjacent_coherent_envelope"};
struct State { std::array<C,M> r{},l{};double pr=0,pl=0,unary=0; };
struct Input {
 double mu=0,k=0,tau=0,nbar=0,dt=0,cell=0;
 std::array<double,M> omega{},position{},variance{};
 double kappa[M][M]{},adjvar[6]{},theta[2]{},amp[2][16]{};
 C eta[M][M]{};
};
struct Fixture { int c=0,segment=0;double fraction=0;State expected; };
struct Prefix { std::array<State,NS+1> state; };
struct alignas(64) Table {
 double dr[M][Q]{},di[M][Q]{},er[M][Q]{},ei[M][Q]{};
 // cos/sin(omega_m absolute midpoint time), indexed [segment][mode][cell].
 std::vector<double> cosine,sine;
 Table():cosine(NS*M*Q),sine(NS*M*Q){}
};
struct Stats {
 std::array<double,NM> value{};
 std::array<int,NM> witness{};
 double duhamel=0,midpoint=0,quartic=0,lipschitz=0;
};
struct Scan {
 std::vector<Stats> tasks;
 std::array<int,80> cpus{},places{};
 int threads=0,migrations=0;
 double seconds=0;
};

double sinc(double x){if(std::abs(x)<1e-4){double y=x*x;return 1+y*(-1.0/6+y*(1.0/120-y/5040));}return std::sin(x)/x;}
C J(double a,double h){return h*sinc(a*h/2)*std::polar(1.0,a*h/2);}
double diagonal_phase(double a,double h){
 double x=a*h;if(std::abs(x)<1e-3)return h*h*x*(1.0/6+x*x*(-1.0/120+x*x*(1.0/5040-x*x/362880)));
 return h*h*(x-std::sin(x))/(x*x);
}
C K(double a,double b,double h){
 if(a==b)return C(std::norm(J(a,h))/2,diagonal_phase(a,h));
 if(b==0){
  if(a==0)return C(h*h/2,0);
  // Entire series of integral s exp(i a s) ds, stable at small argument.
  if(std::abs(a*h)<0.1){C sum=0,term=1;for(int n=0;n<20;++n){sum+=term*(h*h/(n+2));term*=C(0,a*h)/(n+1.0);}return sum;}
  return h*std::polar(1.0,a*h)/C(0,a)+(std::polar(1.0,a*h)-C(1,0))/(a*a);
 }
 return (J(a,h)-J(a-b,h))/C(0,b);
}
std::array<int,2> labels(int c){int b=c%25;return {b/5,b%5};}
std::array<double,2> active(int c,int seg){auto z=labels(c);int cycle=seg/16;return {double((z[0]+cycle)%5==0),double((z[1]+cycle)%5==0)};}
C force(const Input&in,int c,int seg,int m){auto s=active(c,seg);return in.eta[m][3]*s[0]+in.eta[m][4]*s[1];}
State advance(const Input&in,const State&old,int c,int seg,double h){
 State out=old;double t0=seg*in.dt,u=in.amp[c/25][seg%16];auto s=active(c,seg);
 for(int m=0;m<M;++m){
  double a=in.omega[m]-in.mu,b=in.omega[m]+in.mu;C g=force(in,c,seg,m);
  C bm=u*g*std::polar(1.0,a*t0),bp=u*std::conj(g)*std::polar(1.0,b*t0);
  C dr=C(0,-1)*bm*J(a,h),dl=dr+C(0,-1)*bp*J(b,h);
  double qr=std::norm(bm)*diagonal_phase(a,h);
  double ql=qr+std::norm(bp)*diagonal_phase(b,h)+
   std::imag(bm*std::conj(bp)*K(a,b,h)+bp*std::conj(bm)*K(b,a,h));
  out.pr+=qr+std::imag(dr*std::conj(old.r[m]));
  out.pl+=ql+std::imag(dl*std::conj(old.l[m]));
  out.r[m]+=dr;out.l[m]+=dl;
 }
 for(int j=0;j<2;++j){int i=j+3;double x0=in.k*in.position[i]-in.mu*t0,x1=x0-in.mu*h;
  out.unary-=2*u*s[j]*(std::cos(x1)-std::cos(x0))/in.mu;}
 return out;
}
Input read(const std::string&path,std::vector<Fixture>&fixtures){
 std::ifstream f(path);Input in;int q=0;f>>q;if(q!=Q)throw std::runtime_error("grid must be 256");
 auto num=[&](double&x){f>>x;if(!f||!std::isfinite(x))throw std::runtime_error("invalid numeric input");};
 num(in.mu);num(in.k);num(in.tau);num(in.nbar);
 if(in.mu<=0||in.k<=0||in.tau!=1e-4||in.nbar!=0.05)throw std::runtime_error("input constants mismatch");
 in.dt=in.tau/16;in.cell=in.dt/Q;
 for(double&x:in.omega){num(x);if(x<=0)throw std::runtime_error("mode frequency");}
 for(double&x:in.position)num(x);
 for(auto&row:in.kappa)for(double&x:row)num(x);
 double re[M][M]{},im[M][M]{};
 for(auto&row:re){for(double&x:row)num(x);}
 for(auto&row:im){for(double&x:row)num(x);}
 for(int m=0;m<M;++m)for(int i=0;i<M;++i){in.eta[m][i]=C(re[m][i],im[m][i]);
  if(std::abs(in.eta[m][i]-in.kappa[m][i]*std::polar(1.0,in.k*in.position[i]))>1e-12)
   throw std::runtime_error("eta/kappa spatial-phase mismatch");}
 for(int sign=0;sign<2;++sign){num(in.theta[sign]);for(double&u:in.amp[sign])num(u);}
 for(int i=0;i<M;++i)for(int m=0;m<M;++m)in.variance[i]+=in.kappa[m][i]*in.kappa[m][i]*(2*in.nbar+1);
 for(int i=0;i<6;++i){if(in.position[i+1]<=in.position[i])throw std::runtime_error("ion order");
  for(int m=0;m<M;++m){double d=in.kappa[m][i+1]-in.kappa[m][i];in.adjvar[i]+=d*d*(2*in.nbar+1);}}
 int n=0;f>>n;if(n!=4450)throw std::runtime_error("expected 4450 independent fixtures");fixtures.resize(n);
 for(auto&x:fixtures){f>>x.c>>x.segment;num(x.fraction);
  if(x.c<0||x.c>=NC||x.segment<0||x.segment>NS||x.fraction<0||x.fraction>1||(x.segment==NS&&x.fraction!=0))throw std::runtime_error("fixture index");
  num(x.expected.pr);num(x.expected.pl);num(x.expected.unary);
  for(auto*arr:{&x.expected.r,&x.expected.l})for(C&z:*arr){double r,i;num(r);num(i);z=C(r,i);}}
 std::string extra;if(f>>extra)throw std::runtime_error("trailing input");return in;
}
Table prepare(const Input&in){
 Table t;for(int m=0;m<M;++m)for(int q=0;q<Q;++q){double h=(q+0.5)*in.cell;
  C d=C(0,-1)*J(in.omega[m]-in.mu,h),e=C(0,-1)*J(in.omega[m]+in.mu,h);
  t.dr[m][q]=d.real();t.di[m][q]=d.imag();t.er[m][q]=e.real();t.ei[m][q]=e.imag();
  for(int s=0;s<NS;++s){int ix=(s*M+m)*Q+q;double a=in.omega[m]*(s*in.dt+h);t.cosine[ix]=std::cos(a);t.sine[ix]=std::sin(a);}}
 return t;
}
void update(Stats&s,const std::array<double,NM>&v,int witness){
 for(int k=0;k<NM;++k){if(!std::isfinite(v[k])||v[k]<0)throw std::runtime_error("nonfinite trajectory metric");
  if(v[k]>s.value[k]){s.value[k]=v[k];s.witness[k]=witness;}}
}
// Nonnegative Gaussian decomposition of E[R_chi(X)^2]; no cancellation clamp.
double remainder_rms(double chi,double mean,double variance){
 double e=std::exp(-variance/2),sn=std::sin(chi+mean),cs=std::cos(chi+mean);
 double a=e*sn-std::sin(chi)-std::cos(chi)*mean;
 double b=-std::expm1(-variance),v2=variance*variance;
 double tail=variance<0.1?variance*v2*(1.0/6+v2*(1.0/120+v2*(1.0/5040+v2/362880))):std::sinh(variance)-variance;
 double d=std::cos(chi)-e*cs;
 double rho2=a*a+0.5*sn*sn*b*b+cs*cs*std::exp(-variance)*tail+variance*d*d;
 if(!std::isfinite(rho2)||rho2<0)throw std::runtime_error("invalid Gaussian remainder");
 return std::sqrt(rho2);
}
void ld_cell(Stats&out,const Input&in,int c,int seg,int q,const double*mean,const double*limit,const double*deriv){
 double u=std::abs(in.amp[c/25][seg%16]),t=seg*in.dt+(q+0.5)*in.cell;auto s=active(c,seg);
 for(int j=0;j<2;++j){int i=j+3;double v=in.variance[i],l2=limit[i]*limit[i];
  double fourth=std::sqrt(l2*l2+6*l2*v+3*v*v),rho=remainder_rms(in.k*in.position[i]-in.mu*t,mean[i],v);
  double lip=std::abs(in.mu)*fourth/2+deriv[i]*std::sqrt(l2+v),factor=2*in.cell*u*s[j];
  out.midpoint+=factor*rho;out.quartic+=factor*fourth/2;
  out.lipschitz+=factor*in.cell*lip/2;out.duhamel+=factor*std::min(fourth/2,rho+in.cell*lip/2);
 }
}
Stats scalar_task(const Input&in,const Table&t,const Prefix&prefix,int c,int seg){
 Stats out;double u=in.amp[c/25][seg%16],half=in.cell/2;
 C bm[M],bp[M];double F[M];
 for(int m=0;m<M;++m){C g=force(in,c,seg,m);bm[m]=u*g*std::polar(1.0,(in.omega[m]-in.mu)*seg*in.dt);
  bp[m]=u*std::conj(g)*std::polar(1.0,(in.omega[m]+in.mu)*seg*in.dt);F[m]=2*std::abs(u)*std::abs(g);}
 for(int q=0;q<Q;++q){C ar[M],al[M];double ae[M],mean[M]{},limit[M]{},derivative[M]{};std::array<double,NM>v{};
  for(int m=0;m<M;++m){ar[m]=prefix.state[seg].r[m]+bm[m]*C(t.dr[m][q],t.di[m][q]);
   al[m]=prefix.state[seg].l[m]+bm[m]*C(t.dr[m][q],t.di[m][q])+bp[m]*C(t.er[m][q],t.ei[m][q]);
   double r=std::abs(ar[m]),l=std::abs(al[m]),d=std::abs(al[m]-ar[m]);ae[m]=l+half*F[m];
   v[0]=std::max(v[0],r);v[1]=std::max(v[1],l);v[2]=std::max(v[2],d);
   v[3]=std::max(v[3],r+half*F[m]/2);v[4]=std::max(v[4],ae[m]);v[5]=std::max(v[5],d+half*F[m]/2);}
  for(int i=0;i<M;++i){double deriv=0;for(int m=0;m<M;++m){int ix=(seg*M+m)*Q+q;
    mean[i]+=2*in.kappa[m][i]*(al[m].real()*t.cosine[ix]+al[m].imag()*t.sine[ix]);
    deriv+=2*std::abs(in.kappa[m][i])*(F[m]+in.omega[m]*ae[m]);}
   derivative[i]=deriv;limit[i]=std::abs(mean[i])+half*deriv;
   v[6]=std::max(v[6],std::sqrt(mean[i]*mean[i]+in.variance[i]));v[7]=std::max(v[7],std::sqrt(limit[i]*limit[i]+in.variance[i]));}
  for(int i=0;i<6;++i){double deriv=0;for(int m=0;m<M;++m)deriv+=2*std::abs(in.kappa[m][i+1]-in.kappa[m][i])*(F[m]+in.omega[m]*ae[m]);
   double d=std::abs(mean[i+1]-mean[i]),a=d+half*deriv,den=in.k*(in.position[i+1]-in.position[i]);
   v[8]=std::max(v[8],std::sqrt(d*d+in.adjvar[i])/den);v[9]=std::max(v[9],std::sqrt(a*a+in.adjvar[i])/den);
   v[10]=std::max(v[10],d/den);v[11]=std::max(v[11],a/den);}
  ld_cell(out,in,c,seg,q,mean,limit,derivative);update(out,v,seg*Q+q);
 }
 return out;
}

__attribute__((target("avx512f,avx512dq,avx512vl"),noinline))
Stats vector_task(const Input&in,const Table&t,const Prefix&prefix,int c,int seg){
 #define S(x) _mm512_set1_pd(x)
 #define A(x,y) _mm512_add_pd(x,y)
 #define B(x,y) _mm512_sub_pd(x,y)
 #define P(x,y) _mm512_mul_pd(x,y)
 #define SQ(x) _mm512_sqrt_pd(x)
 #define ABS(x) _mm512_abs_pd(x)
 #define LD(x) _mm512_loadu_pd(x)
 #define MAX(x,y) _mm512_max_pd(x,y)
 Stats out;double u=in.amp[c/25][seg%16],half=in.cell/2;
 C bm[M],bp[M];double F[M];
 for(int m=0;m<M;++m){C g=force(in,c,seg,m);bm[m]=u*g*std::polar(1.0,(in.omega[m]-in.mu)*seg*in.dt);
  bp[m]=u*std::conj(g)*std::polar(1.0,(in.omega[m]+in.mu)*seg*in.dt);F[m]=2*std::abs(u)*std::abs(g);}
 for(int q=0;q<Q;q+=8){__m512d lr[M],li[M],ae[M],mean[M],limit[M],derivative[M],v[NM];for(auto&x:v)x=S(0);
  for(int m=0;m<M;++m){auto dr=LD(&t.dr[m][q]),di=LD(&t.di[m][q]),er=LD(&t.er[m][q]),ei=LD(&t.ei[m][q]);
   auto xr=B(P(S(bm[m].real()),dr),P(S(bm[m].imag()),di));auto xi=A(P(S(bm[m].real()),di),P(S(bm[m].imag()),dr));
   auto rr=A(S(prefix.state[seg].r[m].real()),xr),ri=A(S(prefix.state[seg].r[m].imag()),xi);
   lr[m]=A(A(S(prefix.state[seg].l[m].real()),xr),B(P(S(bp[m].real()),er),P(S(bp[m].imag()),ei)));
   li[m]=A(A(S(prefix.state[seg].l[m].imag()),xi),A(P(S(bp[m].real()),ei),P(S(bp[m].imag()),er)));
   auto r=SQ(A(P(rr,rr),P(ri,ri))),l=SQ(A(P(lr[m],lr[m]),P(li[m],li[m])));
   auto drr=B(lr[m],rr),dri=B(li[m],ri),d=SQ(A(P(drr,drr),P(dri,dri)));ae[m]=A(l,S(half*F[m]));
   v[0]=MAX(v[0],r);v[1]=MAX(v[1],l);v[2]=MAX(v[2],d);v[3]=MAX(v[3],A(r,S(half*F[m]/2)));
   v[4]=MAX(v[4],ae[m]);v[5]=MAX(v[5],A(d,S(half*F[m]/2)));}
  for(int i=0;i<M;++i){mean[i]=S(0);auto deriv=S(0);for(int m=0;m<M;++m){int ix=(seg*M+m)*Q+q;
    mean[i]=A(mean[i],P(S(2*in.kappa[m][i]),A(P(lr[m],LD(&t.cosine[ix])),P(li[m],LD(&t.sine[ix])))));
    deriv=A(deriv,P(S(2*std::abs(in.kappa[m][i])),A(S(F[m]),P(S(in.omega[m]),ae[m]))));}
   derivative[i]=deriv;limit[i]=A(ABS(mean[i]),P(S(half),deriv));
   v[6]=MAX(v[6],SQ(A(P(mean[i],mean[i]),S(in.variance[i]))));v[7]=MAX(v[7],SQ(A(P(limit[i],limit[i]),S(in.variance[i]))));}
  for(int i=0;i<6;++i){auto deriv=S(0);for(int m=0;m<M;++m)deriv=A(deriv,P(S(2*std::abs(in.kappa[m][i+1]-in.kappa[m][i])),A(S(F[m]),P(S(in.omega[m]),ae[m]))));
   auto d=ABS(B(mean[i+1],mean[i])),a=A(d,P(S(half),deriv));double inv=1/(in.k*(in.position[i+1]-in.position[i]));
   v[8]=MAX(v[8],P(S(inv),SQ(A(P(d,d),S(in.adjvar[i])))));v[9]=MAX(v[9],P(S(inv),SQ(A(P(a,a),S(in.adjvar[i])))));
   v[10]=MAX(v[10],P(S(inv),d));v[11]=MAX(v[11],P(S(inv),a));}
  alignas(64) double values[NM][8],means[M][8],limits[M][8],derivs[M][8];
  for(int k=0;k<NM;++k)_mm512_store_pd(values[k],v[k]);
  for(int i=0;i<M;++i){_mm512_store_pd(means[i],mean[i]);_mm512_store_pd(limits[i],limit[i]);_mm512_store_pd(derivs[i],derivative[i]);}
  for(int lane=0;lane<8;++lane){std::array<double,NM>node{};for(int k=0;k<NM;++k)node[k]=values[k][lane];
   double m[M],l[M],d[M];for(int i=0;i<M;++i){m[i]=means[i][lane];l[i]=limits[i][lane];d[i]=derivs[i][lane];}
   update(out,node,seg*Q+q+lane);ld_cell(out,in,c,seg,q+lane,m,l,d);}
 }
 #undef S
 #undef A
 #undef B
 #undef P
 #undef SQ
 #undef ABS
 #undef LD
 #undef MAX
 return out;
}
Scan scan(const Input&in,const Table&t,const std::array<Prefix,NC>&prefix,bool simd){
 Scan out;out.tasks.resize(NT);double t0=0,t1=0;
 #pragma omp parallel shared(out,t0,t1)
 {
  int tid=omp_get_thread_num();out.cpus[tid]=sched_getcpu();out.places[tid]=omp_get_place_num();
  #pragma omp barrier
  #pragma omp single
  {out.threads=omp_get_num_threads();t0=omp_get_wtime();}
  #pragma omp for schedule(static)
  for(int task=0;task<NT;++task){int c=task/NS,s=task%NS;out.tasks[task]=simd?vector_task(in,t,prefix[c],c,s):scalar_task(in,t,prefix[c],c,s);}
  #pragma omp single
  {t1=omp_get_wtime();}
  if(out.cpus[tid]!=sched_getcpu()){
   #pragma omp atomic update
   out.migrations+=1;
  }
 }
 out.seconds=t1-t0;if(out.threads!=80||out.migrations)throw std::runtime_error("thread count/migration");return out;
}
Stats reduce(const Scan&scan,int c){Stats out;for(int s=0;s<NS;++s){const Stats&v=scan.tasks[c*NS+s];out.duhamel+=v.duhamel;out.midpoint+=v.midpoint;out.quartic+=v.quartic;out.lipschitz+=v.lipschitz;
 for(int k=0;k<NM;++k)if(v.value[k]>out.value[k]||(v.value[k]==out.value[k]&&v.witness[k]<out.witness[k])){out.value[k]=v.value[k];out.witness[k]=v.witness[k];}}
 return out;
}
C coherence(const State&a,const State&b,double weight,bool linear){
 double r=0,p=(linear?a.pl:a.pr)-(linear?b.pl:b.pr);for(int m=0;m<M;++m){C x=linear?a.l[m]:a.r[m],y=linear?b.l[m]:b.r[m];r+=weight*std::norm(x-y);p+=std::imag(std::conj(y)*x);}return std::exp(C(-r,p));
}
struct Comparison {
 double raw=0,optimized=0,gamma=0,bell=0,rwa_ideal=0,rwa_alpha=0,linear_alpha=0,unary=0,unary_spread=0;
 double continuous=0,continuous_phase=0,continuous_r=0;
 int za=0,zb=1,continuous_case=0,continuous_segment=0;
 std::array<double,25>phase{},exponent{};
};
double relative_phase(const State&s){double phase=s.pl-s.pr;for(int m=0;m<M;++m)phase+=std::imag(std::conj(s.r[m])*s.l[m]);return phase;}
std::array<double,2> continuous_limits(const Input&in,const State&mid,int c,int seg){
 double deriv=0,r=0,half=in.dt/2,u=std::abs(in.amp[c/25][seg%16]);
 for(int m=0;m<M;++m){double F=u*std::abs(force(in,c,seg,m));
  double AL=std::abs(mid.l[m])+in.dt*F,AR=std::abs(mid.r[m])+half*F;
  deriv+=F*(AL+AR);double da=std::abs(mid.l[m]-mid.r[m])+half*F;r+=(in.nbar+0.5)*da*da;}
 return {deriv,r};
}
Comparison compare(const Input&in,const std::array<Prefix,NC>&p,int sign){
 Comparison out;std::array<C,25>points;std::vector<double>candidates{0};double umin=std::numeric_limits<double>::infinity(),umax=-umin;
 double base=p[sign*25].state[NS].pr;
 for(int z=0;z<25;++z){const State&s=p[sign*25+z].state[NS];double r=0,phase=s.pl-s.pr;
  for(int m=0;m<M;++m){r+=(in.nbar+0.5)*std::norm(s.l[m]-s.r[m]);phase+=std::imag(std::conj(s.r[m])*s.l[m]);out.rwa_alpha=std::max(out.rwa_alpha,std::abs(s.r[m]));out.linear_alpha=std::max(out.linear_alpha,std::abs(s.l[m]));}
  out.phase[z]=phase;out.exponent[z]=r;points[z]=std::exp(C(-r,phase));
  candidates.push_back(std::arg(points[z]));candidates.push_back(std::arg(points[z])+PI);
  out.rwa_ideal=std::max(out.rwa_ideal,std::abs(std::remainder(s.pr-base-in.theta[sign]*(z/5!=z%5),2*PI)));
  umin=std::min(umin,s.unary);umax=std::max(umax,s.unary);
 }
 for(int z=0;z<25;++z)for(int w=z+1;w<25;++w){C d=points[z]-points[w];if(std::abs(d)>0){candidates.push_back(std::arg(d)+PI/2);candidates.push_back(std::arg(d)-PI/2);}
  const State&a=p[sign*25+z].state[NS];const State&b=p[sign*25+w].state[NS];double D=std::abs(coherence(a,b,in.nbar+0.5,true)-coherence(a,b,in.nbar+0.5,false))/2;
  if(D>out.bell){out.bell=D;out.za=z;out.zb=w;}}
 auto squared=[&](double gamma){double worst=0;for(int z=0;z<25;++z){double sine=std::sin((out.phase[z]-gamma)/2);worst=std::max(worst,-2*std::expm1(-out.exponent[z])+4*std::exp(-out.exponent[z])*sine*sine);}return worst;};
 double best=std::numeric_limits<double>::infinity();for(double gamma:candidates){double score=squared(gamma);if(score<best){best=score;out.gamma=gamma;}}
 out.raw=std::min(1.0,std::sqrt(squared(0)));out.optimized=std::min(1.0,std::sqrt(best));out.unary=p[sign*25].state[NS].unary;out.unary_spread=umax-umin;
 if(out.rwa_ideal>1e-8||out.rwa_alpha>1e-9||out.unary_spread>1e-8)throw std::runtime_error("prior RWA gate/unary sanity failed");
 if(out.bell>out.optimized+1e-7)throw std::runtime_error("Bell witness exceeds RWA comparison upper estimate");
 for(int seg=0;seg<NS;++seg){int anchor=sign*25;State anchor_mid=advance(in,p[anchor].state[seg],anchor,seg,in.dt/2);
  double anchor_phase=relative_phase(anchor_mid),anchor_deriv=continuous_limits(in,anchor_mid,anchor,seg)[0];
  for(int z=0;z<25;++z){int c=sign*25+z;State mid=advance(in,p[c].state[seg],c,seg,in.dt/2);auto lim=continuous_limits(in,mid,c,seg);
   double phase=std::min(PI,std::abs(std::remainder(relative_phase(mid)-anchor_phase,2*PI))+in.dt/2*(lim[0]+anchor_deriv));
   double sine=std::sin(phase/2),bound=phase>PI/2?1:std::min(1.0,std::sqrt(-2*std::expm1(-lim[1])+4*std::exp(-lim[1])*sine*sine));
   out.continuous_phase=std::max(out.continuous_phase,phase);out.continuous_r=std::max(out.continuous_r,lim[1]);
   if(bound>out.continuous){out.continuous=bound;out.continuous_case=c;out.continuous_segment=seg;}
  }
 }
 return out;
}
void print_array(const std::array<double,25>&a){std::cout<<'[';for(int i=0;i<25;++i){if(i)std::cout<<',';std::cout<<a[i];}std::cout<<']';}
int main(int argc,char**argv){try{
 if(argc!=3||std::string(argv[1])!="--input")throw std::runtime_error("usage: trajectory --input input.txt");
 __builtin_cpu_init();if(!__builtin_cpu_supports("avx512f")||!__builtin_cpu_supports("avx512dq")||!__builtin_cpu_supports("avx512vl"))throw std::runtime_error("AVX512 unavailable");
 omp_set_dynamic(0);omp_set_num_threads(80);double prep0=omp_get_wtime();std::vector<Fixture>fixtures;Input in=read(argv[2],fixtures);
 auto prefix=std::make_unique<std::array<Prefix,NC>>();
 for(int c=0;c<NC;++c)for(int s=0;s<NS;++s)(*prefix)[c].state[s+1]=advance(in,(*prefix)[c].state[s],c,s,in.dt);
 double oracle_a=0,oracle_p=0;for(const auto&f:fixtures){State actual=(*prefix)[f.c].state[f.segment];if(f.fraction>0)actual=advance(in,actual,f.c,f.segment,in.dt*f.fraction);
  oracle_p=std::max({oracle_p,std::abs(actual.pr-f.expected.pr),std::abs(actual.pl-f.expected.pl),std::abs(actual.unary-f.expected.unary)});
  for(int m=0;m<M;++m)oracle_a=std::max({oracle_a,std::abs(actual.r[m]-f.expected.r[m]),std::abs(actual.l[m]-f.expected.l[m])});}
 if(!std::isfinite(oracle_a)||!std::isfinite(oracle_p)||oracle_a>ATOL||oracle_p>PTOL)throw std::runtime_error("independent scalar oracle discrepancy");
 Table table=prepare(in);double prep_seconds=omp_get_wtime()-prep0;
 Scan scalar_scan=scan(in,table,*prefix,false),vector_scan=scan(in,table,*prefix,true);
 double diff=0;for(int task=0;task<NT;++task){const Stats&a=scalar_scan.tasks[task];const Stats&b=vector_scan.tasks[task];
  for(int k=0;k<NM;++k){double d=std::abs(a.value[k]-b.value[k]);diff=std::max(diff,d);if(!std::isfinite(d)||d>1e-9+1e-12*std::abs(a.value[k]))throw std::runtime_error("scalar/SIMD trajectory discrepancy");}
  for(auto member:{&Stats::duhamel,&Stats::midpoint,&Stats::quartic,&Stats::lipschitz}){double d=std::abs(a.*member-b.*member);diff=std::max(diff,d);if(!std::isfinite(d)||d>1e-9+1e-12*std::abs(a.*member))throw std::runtime_error("scalar/SIMD integral discrepancy");}}
 std::array<Comparison,2>comparison{compare(in,*prefix,0),compare(in,*prefix,1)};
 std::cout<<std::setprecision(17)<<"{\"status\":\"PASS\",\"scope\":\"FP_estimates_of_analytic_envelopes\",\"backend\":\"avx512\",\"threads\":80,\"nsub\":256,\"cases\":50,\"tasks\":4000,\"midpoints_per_model\":1024000,\"oracle_fixtures\":4450,\"oracle_alpha_error\":"<<oracle_a<<",\"oracle_phase_error\":"<<oracle_p<<",\"scalar_simd_error\":"<<diff<<",\"preparation_seconds\":"<<prep_seconds<<",\"scalar_seconds\":"<<scalar_scan.seconds<<",\"kernel_seconds\":"<<vector_scan.seconds<<",\"branches\":[";
 for(int c=0;c<NC;++c){if(c)std::cout<<',';Stats s=reduce(vector_scan,c);std::cout<<"{\"case\":"<<c<<",\"sign\":"<<(c/25==0?1:-1)<<",\"active_labels\":["<<(c%25)/5<<','<<c%5<<"],\"ld_duhamel_uncapped\":"<<s.duhamel<<",\"ld_midpoint_integral\":"<<s.midpoint<<",\"ld_quartic_envelope\":"<<s.quartic<<",\"ld_lipschitz_allowance\":"<<s.lipschitz<<",\"ld_envelope_gap\":"<<s.duhamel-s.midpoint;
  for(int k=0;k<NM;++k){std::cout<<",\""<<metric_names[k]<<"\":"<<s.value[k];}
  std::cout<<",\"witness_cells\":[";
  for(int k=0;k<NM;++k){if(k)std::cout<<',';std::cout<<s.witness[k];}std::cout<<"]}";}
 std::cout<<"],\"comparisons\":[";for(int sign=0;sign<2;++sign){if(sign)std::cout<<',';const auto&x=comparison[sign];
  std::cout<<"{\"sign\":"<<(sign==0?1:-1)<<",\"rwa_linear_raw_bound\":"<<x.raw<<",\"rwa_linear_optimized_bound\":"<<x.optimized<<",\"common_phase_gamma\":"<<x.gamma<<",\"bell_trace_distance_max\":"<<x.bell<<",\"bell_pair\":["<<x.za<<','<<x.zb<<"],\"rwa_ideal_phase_error\":"<<x.rwa_ideal<<",\"rwa_endpoint_alpha_max\":"<<x.rwa_alpha<<",\"linear_endpoint_alpha_max\":"<<x.linear_alpha<<",\"uncompensated_unary_phase\":"<<x.unary<<",\"unary_branch_spread\":"<<x.unary_spread<<",\"rwa_linear_continuous_anchor_bound\":"<<x.continuous<<",\"rwa_continuous_phase_envelope\":"<<x.continuous_phase<<",\"rwa_continuous_r_envelope\":"<<x.continuous_r<<",\"rwa_continuous_witness\":["<<x.continuous_case<<','<<x.continuous_segment<<"],\"raw_phase_differences\":";print_array(x.phase);std::cout<<",\"displacement_exponents\":";print_array(x.exponent);std::cout<<'}';}
 std::cout<<"],\"initial_thermal_rms_by_ion\":[";for(int i=0;i<M;++i){if(i)std::cout<<',';std::cout<<std::sqrt(in.variance[i]);}
 std::cout<<"],\"thread_map\":[";for(int t=0;t<80;++t){if(t)std::cout<<',';std::cout<<"{\"thread\":"<<t<<",\"cpu\":"<<vector_scan.cpus[t]<<",\"place\":"<<vector_scan.places[t]<<'}';}
 std::cout<<"],\"scalar_thread_map\":[";for(int t=0;t<80;++t){if(t)std::cout<<',';std::cout<<"{\"thread\":"<<t<<",\"cpu\":"<<scalar_scan.cpus[t]<<",\"place\":"<<scalar_scan.places[t]<<'}';}std::cout<<"]}\n";
 return 0;
}catch(const std::exception&e){std::cerr<<e.what()<<'\n';return 2;}}
