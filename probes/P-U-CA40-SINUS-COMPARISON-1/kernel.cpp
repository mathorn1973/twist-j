// Copyright 2026 A. M. Thorn. SPDX-License-Identifier: Apache-2.0
// Conditional seven-mode Galerkin calculation. FP diagnostics are not certificates.
#include <algorithm>
#include <array>
#include <atomic>
#include <bit>
#include <cmath>
#include <complex>
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
constexpr int M=7, B=8, CASES=6, THERMAL=120, BATCHES=15;
constexpr double PI=3.141592653589793238462643383279502884;
constexpr double NEG_TOL=1e-10, FIXTURE_TOL=1e-11;
#define AVX __attribute__((target("avx512f,avx512dq,avx512vl")))
struct Basis {
 int L,d;std::vector<std::array<int,M>> n;std::vector<int> degree,start;
 std::vector<std::array<int,M>> up,down;std::vector<std::array<double,M>> raise,lower;
 explicit Basis(int cutoff):L(cutoff){
  std::array<int,M> row{};
  auto visit=[&](auto&&self,int mode,int left)->void{
   if(mode==M-1){row[mode]=left;n.push_back(row);return;}
   for(int k=0;k<=left;++k){row[mode]=k;self(self,mode+1,left-k);}
  };
  for(int total=0;total<=L;++total){start.push_back(int(n.size()));visit(visit,0,total);}
  start.push_back(int(n.size()));d=int(n.size());
  auto code=[](const std::array<int,M>&v){int out=0;for(int m=0;m<M;++m)out|=v[m]<<(3*m);return out;};
  std::unordered_map<int,int>index;for(int i=0;i<d;++i)index.emplace(code(n[i]),i);
  up.resize(d);down.resize(d);raise.resize(d);lower.resize(d);degree.resize(d);
  for(int i=0;i<d;++i){int total=0;for(int x:n[i])total+=x;degree[i]=total;
   for(int m=0;m<M;++m){auto v=n[i];up[i][m]=-1;down[i][m]=-1;
    lower[i][m]=std::sqrt(double(v[m]));raise[i][m]=std::sqrt(double(v[m]+1));
    if(v[m]){--v[m];down[i][m]=index.at(code(v));++v[m];}
    if(total<L){++v[m];up[i][m]=index.at(code(v));}
   }
  }
 }
};
C get(const V&v,int d,int row,int lane){return {v[row*B+lane],v[(d+row)*B+lane]};}
void put(V&v,int d,int row,int lane,C x){v[row*B+lane]=x.real();v[(d+row)*B+lane]=x.imag();}
AVX void axpy(V&out,const V&x,double a){auto c=_mm512_set1_pd(a);for(size_t i=0;i<out.size();i+=B)_mm512_storeu_pd(&out[i],_mm512_add_pd(_mm512_loadu_pd(&out[i]),_mm512_mul_pd(c,_mm512_loadu_pd(&x[i]))));}
AVX void ladder(const Basis&b,const V&x,V&out,const std::array<C,M>&coef,bool creation,int order){
 std::fill(out.begin(),out.end(),0.0);
 int begin=creation?b.start[order]:0,end=creation?b.d:b.start[b.L-order+1];
 for(int n=begin;n<end;++n){auto re=_mm512_setzero_pd(),im=re;
  for(int m=0;m<M;++m){int j=creation?b.down[n][m]:b.up[n][m];if(j<0)continue;
   double s=(creation?b.lower[n][m]:b.raise[n][m])/order;
   auto cr=_mm512_set1_pd(coef[m].real()*s),ci=_mm512_set1_pd(coef[m].imag()*s);
   auto xr=_mm512_loadu_pd(&x[j*B]),xi=_mm512_loadu_pd(&x[(b.d+j)*B]);
   re=_mm512_add_pd(re,_mm512_sub_pd(_mm512_mul_pd(cr,xr),_mm512_mul_pd(ci,xi)));
   im=_mm512_add_pd(im,_mm512_add_pd(_mm512_mul_pd(cr,xi),_mm512_mul_pd(ci,xr)));
  }
  _mm512_storeu_pd(&out[n*B],re);_mm512_storeu_pd(&out[(b.d+n)*B],im);
 }
}
struct Workspace {
 V term,temp,sum,half,dp,dm,x,lower,upper,k1,k2,k3,k4,stage;
 explicit Workspace(int d):term(2*d*B),temp(term.size()),sum(term.size()),half(term.size()),dp(term.size()),dm(term.size()),x(term.size()),lower(term.size()),upper(term.size()),k1(term.size()),k2(term.size()),k3(term.size()),k4(term.size()),stage(term.size()){}
};
AVX void displacement(const Basis&b,const V&x,V&out,const std::array<C,M>&beta,Workspace&w){
 std::array<C,M>ann;double norm=0;for(int m=0;m<M;++m){ann[m]=-std::conj(beta[m]);norm+=std::norm(beta[m]);}
 w.term=x;w.sum=x;
 for(int k=1;k<=b.L;++k){ladder(b,w.term,w.temp,ann,false,k);w.term.swap(w.temp);axpy(w.sum,w.term,1);}
 w.half=w.sum;w.term=w.half;out=w.half;
 for(int k=1;k<=b.L;++k){ladder(b,w.term,w.temp,beta,true,k);w.term.swap(w.temp);axpy(out,w.term,1);}
 auto scale=_mm512_set1_pd(std::exp(-norm/2));for(size_t i=0;i<out.size();i+=B)_mm512_storeu_pd(&out[i],_mm512_mul_pd(scale,_mm512_loadu_pd(&out[i])));
}
std::array<double,B> norms(const Basis&b,const V&x,int first=0){std::array<double,B>out{};for(int n=first;n<b.d;++n)for(int lane=0;lane<B;++lane)out[lane]+=std::norm(get(x,b.d,n,lane));return out;}
struct Input {double mu,k,tau,nbar,dt,omega[M],pos[M],kap[M][M],theta[2],amp[2][16];C eta[M][M];};
Input read(const std::string&path){std::ifstream f(path);Input in{};auto num=[&](double&x){f>>x;if(!f||!std::isfinite(x))throw std::runtime_error("invalid input");};
 num(in.mu);num(in.k);num(in.tau);num(in.nbar);in.dt=in.tau/16;
 if(in.tau!=1e-4||in.nbar!=0.05||in.mu<=0||in.k<=0)throw std::runtime_error("frozen constants mismatch");
 for(double&v:in.omega){num(v);}
 for(double&v:in.pos){num(v);}
 for(auto&row:in.kap)for(double&v:row)num(v);
 double re[M][M],im[M][M];for(auto&row:re)for(double&v:row)num(v);for(auto&row:im)for(double&v:row)num(v);
 for(int m=0;m<M;++m)for(int i=0;i<M;++i){in.eta[m][i]={re[m][i],im[m][i]};if(std::abs(in.eta[m][i]-in.kap[m][i]*std::polar(1.0,in.k*in.pos[i]))>1e-12)throw std::runtime_error("eta consistency");}
 for(int s=0;s<2;++s){num(in.theta[s]);for(double&v:in.amp[s])num(v);}
 std::string extra;if(f>>extra)throw std::runtime_error("trailing input");return in;
}
double sinc(double x){if(std::abs(x)<1e-4){double y=x*x;return 1+y*(-1.0/6+y*(1.0/120-y/5040));}return std::sin(x)/x;}
C J(double a,double h){return h*sinc(a*h/2)*std::polar(1.0,a*h/2);}
double qdiag(double a,double h){double x=a*h;if(std::abs(x)<1e-3)return h*h*x*(1.0/6+x*x*(-1.0/120+x*x*(1.0/5040-x*x/362880)));return h*h*(x-std::sin(x))/(x*x);}
C K(double a,double b,double h){if(a==b)return {std::norm(J(a,h))/2,qdiag(a,h)};if(b==0)throw std::runtime_error("unexpected zero frequency");return (J(a,h)-J(a-b,h))/C(0,b);}
struct Linear {std::array<C,M>alpha{};double phase=0;};
const int LABELS[3][2]={{4,3},{4,4},{1,1}};
std::array<int,2> response(int c,int seg){int cycle=seg/16;return {int((LABELS[c%3][0]+cycle)%5==0),int((LABELS[c%3][1]+cycle)%5==0)};}
Linear advance(const Input&in,const Linear&old,int c,int seg,double h){Linear out=old;auto s=response(c,seg);double u=in.amp[c/3][seg%16],t=seg*in.dt;
 for(int m=0;m<M;++m){C g=in.eta[m][3]*double(s[0])+in.eta[m][4]*double(s[1]);double a=in.omega[m]-in.mu,b=in.omega[m]+in.mu;
  C bm=u*g*std::polar(1.0,a*t),bp=u*std::conj(g)*std::polar(1.0,b*t),da=C(0,-1)*(bm*J(a,h)+bp*J(b,h));
  out.phase+=std::norm(bm)*qdiag(a,h)+std::norm(bp)*qdiag(b,h)+std::imag(bm*std::conj(bp)*K(a,b,h)+bp*std::conj(bm)*K(b,a,h)+da*std::conj(old.alpha[m]));out.alpha[m]+=da;
 }return out;
}
struct Node {double u=0,cs[2]{},sn[2]{},mean[2]{},k2[2]{};int active[2]{};std::array<C,M> beta[2];};
struct Step {Node point[3];};
Node node(const Input&in,const Linear&state,int c,int seg,double offset){Node out;double t=seg*in.dt+offset;auto s=response(c,seg);out.u=in.amp[c/3][seg%16];
 for(int j=0;j<2;++j){int i=j+3;out.active[j]=s[j];double chi=in.k*in.pos[i]-in.mu*t;out.cs[j]=std::cos(chi);out.sn[j]=std::sin(chi);
  for(int m=0;m<M;++m){C phase=std::polar(1.0,in.omega[m]*t);out.beta[j][m]=C(0,in.kap[m][i])*phase;out.mean[j]+=2*in.kap[m][i]*std::real(state.alpha[m]*std::conj(phase));out.k2[j]+=in.kap[m][i]*in.kap[m][i];}
 }return out;
}
struct Prepared {std::array<std::vector<Step>,CASES> steps;std::array<Linear,CASES> final;};
Prepared prepare(const Input&in,int sub){Prepared out;
 for(int c=0;c<CASES;++c){Linear state;for(int seg=0;seg<80;++seg){auto s=response(c,seg);
   if(s[0]||s[1])for(int q=0;q<sub;++q){Step step;for(int j=0;j<3;++j){double h=(q+j*0.5)*in.dt/sub;step.point[j]=node(in,advance(in,state,c,seg,h),c,seg,h);}out.steps[c].push_back(step);}
   state=advance(in,state,c,seg,in.dt);
  }out.final[c]=state;
 }return out;
}
struct Diagnostics {std::array<double,B> integral{},norm_error{},boundary{};double min_deficit=0;};
// Triangle projection residual sampled at RK nodes, not a continuous certificate.
AVX std::array<double,B> hamiltonian(const Basis&b,const V&y,V&out,const Node&p,Workspace&w,Diagnostics&diag){
 std::fill(out.begin(),out.end(),0.0);std::array<double,B>residual{};auto norm=norms(b,y),top=norms(b,y,b.start[b.L]);
 for(int lane=0;lane<B;++lane)diag.boundary[lane]=std::max(diag.boundary[lane],top[lane]);
 for(int j=0;j<2;++j){if(!p.active[j])continue;std::array<C,M>negative,ann,create;
  for(int m=0;m<M;++m){negative[m]=-p.beta[j][m];create[m]=C(0,-1)*p.beta[j][m];ann[m]=std::conj(create[m]);}
  displacement(b,y,w.dp,p.beta[j],w);displacement(b,y,w.dm,negative,w);
  ladder(b,y,w.lower,ann,false,1);ladder(b,y,w.upper,create,true,1);w.x=w.lower;axpy(w.x,w.upper,1);
  auto np=norms(b,w.dp),nm=norms(b,w.dm);std::array<double,B>bt{};
  for(int n=b.start[b.L-1];n<b.start[b.L];++n)for(int lane=0;lane<B;++lane){C value=0;for(int m=0;m<M;++m){int src=b.up[n][m];if(src>=0)value+=ann[m]*b.raise[n][m]*get(y,b.d,src,lane);}bt[lane]+=std::norm(value);}
  for(int lane=0;lane<B;++lane){double dp=norm[lane]-np[lane],dm=norm[lane]-nm[lane];diag.min_deficit=std::min({diag.min_deficit,dp,dm});
   if(dp<-NEG_TOL*(1+norm[lane])||dm<-NEG_TOL*(1+norm[lane]))throw std::runtime_error("negative displacement norm deficit beyond tolerance");
   residual[lane]+=2*std::abs(p.u)*((std::sqrt(std::max(0.0,dp))+std::sqrt(std::max(0.0,dm)))/2+std::abs(p.cs[j])*std::sqrt(p.k2[j]*top[lane]+bt[lane]));
  }
  // exp(i(chi+m)) without reconstructing chi from an inverse trig function.
  C phase=C(p.cs[j],p.sn[j])*std::polar(1.0,p.mean[j]);C a=C(0,-0.5)*phase,bb=C(0,0.5)*std::conj(phase);
  double diagonal=p.sn[j]+p.cs[j]*p.mean[j],scale=2*p.u;
  auto ar=_mm512_set1_pd(a.real()),ai=_mm512_set1_pd(a.imag()),br=_mm512_set1_pd(bb.real()),bi=_mm512_set1_pd(bb.imag());
  for(int n=0;n<b.d;++n){int ir=n*B,ii=(b.d+n)*B;auto pr=_mm512_loadu_pd(&w.dp[ir]),pi=_mm512_loadu_pd(&w.dp[ii]),mr=_mm512_loadu_pd(&w.dm[ir]),mi=_mm512_loadu_pd(&w.dm[ii]);
   auto re=_mm512_add_pd(_mm512_sub_pd(_mm512_mul_pd(ar,pr),_mm512_mul_pd(ai,pi)),_mm512_sub_pd(_mm512_mul_pd(br,mr),_mm512_mul_pd(bi,mi)));
   auto im=_mm512_add_pd(_mm512_add_pd(_mm512_mul_pd(ar,pi),_mm512_mul_pd(ai,pr)),_mm512_add_pd(_mm512_mul_pd(br,mi),_mm512_mul_pd(bi,mr)));
   re=_mm512_sub_pd(re,_mm512_add_pd(_mm512_mul_pd(_mm512_set1_pd(diagonal),_mm512_loadu_pd(&y[ir])),_mm512_mul_pd(_mm512_set1_pd(p.cs[j]),_mm512_loadu_pd(&w.x[ir]))));
   im=_mm512_sub_pd(im,_mm512_add_pd(_mm512_mul_pd(_mm512_set1_pd(diagonal),_mm512_loadu_pd(&y[ii])),_mm512_mul_pd(_mm512_set1_pd(p.cs[j]),_mm512_loadu_pd(&w.x[ii]))));
   // Return -i H y for RK4.
   _mm512_storeu_pd(&out[ir],_mm512_add_pd(_mm512_loadu_pd(&out[ir]),_mm512_mul_pd(_mm512_set1_pd(scale),im)));
   _mm512_storeu_pd(&out[ii],_mm512_sub_pd(_mm512_loadu_pd(&out[ii]),_mm512_mul_pd(_mm512_set1_pd(scale),re)));
  }
 }
 return residual;
}
void evolve(const Basis&b,V&y,const std::vector<Step>&steps,double h,Workspace&w,Diagnostics&d){
 for(const Step&s:steps){auto a=hamiltonian(b,y,w.k1,s.point[0],w,d);w.stage=y;axpy(w.stage,w.k1,h/2);
  auto bb=hamiltonian(b,w.stage,w.k2,s.point[1],w,d);w.stage=y;axpy(w.stage,w.k2,h/2);
  auto c=hamiltonian(b,w.stage,w.k3,s.point[1],w,d);w.stage=y;axpy(w.stage,w.k3,h);
  auto dd=hamiltonian(b,w.stage,w.k4,s.point[2],w,d);axpy(y,w.k1,h/6);axpy(y,w.k2,h/3);axpy(y,w.k3,h/3);axpy(y,w.k4,h/6);
  auto n=norms(b,y);for(int lane=0;lane<B;++lane){if(!std::isfinite(n[lane])||n[lane]>4)throw std::runtime_error("nonfinite or unstable RK state");d.norm_error[lane]=std::max(d.norm_error[lane],std::abs(n[lane]-1));d.integral[lane]+=h*(a[lane]+2*bb[lane]+2*c[lane]+dd[lane])/6;}
 }
}
double factorial(int n){double v=1;for(int k=2;k<=n;++k)v*=k;return v;}
C dense_element(const Basis&b,int n,int m,const std::array<C,M>&beta){C result=1;double norm=0;
 for(int i=0;i<M;++i){C sum=0;int a=b.n[n][i],bb=b.n[m][i];for(int j=0;j<=std::min(a,bb);++j)sum+=std::pow(beta[i],a-j)*std::pow(-std::conj(beta[i]),bb-j)/(factorial(j)*factorial(a-j)*factorial(bb-j));result*=std::sqrt(factorial(a)*factorial(bb))*sum;norm+=std::norm(beta[i]);}
 return std::exp(-norm/2)*result;
}
struct FixtureReport {double dense_error=0,adjoint_error=0,zero_error=0,hermiticity_error=0,single_mode_error=0;};
FixtureReport fixtures(){Basis b(2);Workspace w(b.d);V x(2*b.d*B),y(x.size()),dp(x.size()),dm(x.size());FixtureReport out;
 for(int n=0;n<b.d;++n)for(int lane=0;lane<B;++lane){put(x,b.d,n,lane,C((n+lane)%7-3,(2*n+lane)%5-2)/32.0);put(y,b.d,n,lane,C((n+3*lane)%11-5,(n+lane)%3-1)/48.0);}
 std::array<C,M>beta;for(int m=0;m<M;++m)beta[m]=C(m+1,7-m)/100.;
 for(int kind=0;kind<3;++kind){auto z=beta;if(kind==1)z.fill(0);if(kind==2){z.fill(0);z[3]=C(0.07,-0.03);}displacement(b,x,dp,z,w);
  for(int n=0;n<b.d;++n)for(int lane=0;lane<B;++lane){C value=0;for(int m=0;m<b.d;++m)value+=dense_element(b,n,m,z)*get(x,b.d,m,lane);double error=std::abs(value-get(dp,b.d,n,lane));out.dense_error=std::max(out.dense_error,error);if(kind==1)out.zero_error=std::max(out.zero_error,std::abs(get(dp,b.d,n,lane)-get(x,b.d,n,lane)));if(kind==2)out.single_mode_error=std::max(out.single_mode_error,error);}
 }
 displacement(b,x,dp,beta,w);for(C&v:beta)v=-v;displacement(b,y,dm,beta,w);
 for(int lane=0;lane<B;++lane){C a=0,bb=0;for(int n=0;n<b.d;++n){a+=std::conj(get(y,b.d,n,lane))*get(dp,b.d,n,lane);bb+=std::conj(get(dm,b.d,n,lane))*get(x,b.d,n,lane);}out.adjoint_error=std::max(out.adjoint_error,std::abs(a-bb));}
 Node p;p.u=0.7;p.active[0]=1;p.cs[0]=std::cos(0.4);p.sn[0]=std::sin(0.4);p.mean[0]=0.2;p.beta[0]=beta;for(C v:beta)p.k2[0]+=std::norm(v);Diagnostics diag;
 hamiltonian(b,x,dp,p,w,diag);hamiltonian(b,y,dm,p,w,diag);
 for(int lane=0;lane<B;++lane){C a=0,bb=0;for(int n=0;n<b.d;++n){a+=std::conj(get(y,b.d,n,lane))*C(0,1)*get(dp,b.d,n,lane);bb+=std::conj(C(0,1)*get(dm,b.d,n,lane))*get(x,b.d,n,lane);}out.hermiticity_error=std::max(out.hermiticity_error,std::abs(a-bb));}
 p.active[0]=0;hamiltonian(b,x,dp,p,w,diag);for(double v:dp)out.zero_error=std::max(out.zero_error,std::abs(v));
 if(std::max({out.dense_error,out.adjoint_error,out.zero_error,out.hermiticity_error,out.single_mode_error})>FIXTURE_TOL){throw std::runtime_error("independent small operator fixtures failed");}
 return out;
}
void complex_json(C z){std::cout<<'['<<z.real()<<','<<z.imag()<<']';}
int main(int argc,char**argv){try{
 std::string input,output;int cutoff=0,sub=0;for(int i=1;i<argc;i+=2){if(i+1>=argc)throw std::runtime_error("missing CLI value");std::string key=argv[i];if(key=="--input")input=argv[i+1];else if(key=="--output")output=argv[i+1];else if(key=="--cutoff")cutoff=std::stoi(argv[i+1]);else if(key=="--steps")sub=std::stoi(argv[i+1]);else throw std::runtime_error("unknown option");}
 if(input.empty()||output.empty()||(cutoff!=4&&cutoff!=6)||(sub!=128&&sub!=256&&sub!=512)||(cutoff==4&&sub!=128))throw std::runtime_error("frozen CLI panel required");
 if constexpr(std::endian::native!=std::endian::little)throw std::runtime_error("little-endian endpoint format required");
 __builtin_cpu_init();if(!__builtin_cpu_supports("avx512f")||!__builtin_cpu_supports("avx512dq")||!__builtin_cpu_supports("avx512vl"))throw std::runtime_error("AVX512 unavailable");
 if(!std::filesystem::create_directory(output))throw std::runtime_error("output directory must be new");
 double t0=omp_get_wtime();Input in=read(input);Basis b(cutoff);if(b.start[4]!=THERMAL)throw std::runtime_error("thermal basis size");FixtureReport fixture=fixtures();Prepared prepared=prepare(in,sub);
 std::ofstream basis_file(std::filesystem::path(output)/"basis.json");basis_file<<"{\"cutoff\":"<<cutoff<<",\"thermal_cutoff\":3,\"occupations\":[";for(int n=0;n<b.d;++n){if(n)basis_file<<',';basis_file<<'[';for(int m=0;m<M;++m){if(m)basis_file<<',';basis_file<<b.n[n][m];}basis_file<<']';}basis_file<<"]}\n";basis_file.close();if(!basis_file)throw std::runtime_error("basis write failed");
 std::vector<V>states(CASES*BATCHES);std::vector<Diagnostics>diagnostics(CASES*BATCHES);std::mutex lock;std::ofstream progress(std::filesystem::path(output)/"progress.jsonl");if(!progress)throw std::runtime_error("progress file open failed");progress<<std::setprecision(17);std::atomic<int>completed{0};std::atomic<bool>failed{false};std::string failure;
 std::array<int,80>cpus{},places{};std::atomic<int>migrations{0};int workers=0;omp_set_dynamic(0);omp_set_num_threads(80);double prep_seconds=omp_get_wtime()-t0,scan0=omp_get_wtime();
 #pragma omp parallel
 {
  int tid=omp_get_thread_num();if(tid>=80)std::terminate();cpus[tid]=sched_getcpu();places[tid]=omp_get_place_num();
  #pragma omp single
  workers=omp_get_num_threads();
  Workspace w(b.d);
  #pragma omp for schedule(dynamic,1)
  for(int task=0;task<CASES*BATCHES;++task){if(failed.load())continue;try{
    int c=task/BATCHES,batch=task%BATCHES;V y(2*b.d*B);for(int lane=0;lane<B;++lane)put(y,b.d,batch*B+lane,lane,1);
    evolve(b,y,prepared.steps[c],in.dt/sub,w,diagnostics[task]);states[task]=std::move(y);int done=++completed;
    std::lock_guard<std::mutex>guard(lock);double drift=*std::max_element(diagnostics[task].norm_error.begin(),diagnostics[task].norm_error.end());progress<<"{\"completed\":"<<done<<",\"case\":"<<c<<",\"batch\":"<<batch<<",\"max_norm_error\":"<<drift<<",\"elapsed_seconds\":"<<omp_get_wtime()-scan0<<"}\n";progress.flush();if(!progress)throw std::runtime_error("progress write failed");
   }catch(const std::exception&e){std::lock_guard<std::mutex>guard(lock);failed=true;if(failure.empty())failure=e.what();}}
  if(cpus[tid]!=sched_getcpu())++migrations;
 }
 double kernel_seconds=omp_get_wtime()-scan0;progress.close();if(failed||completed!=90)throw std::runtime_error("partial campaign: "+failure);if(workers!=80||migrations)throw std::runtime_error("worker count or migration");
 std::ofstream binary(std::filesystem::path(output)/"endpoints.bin",std::ios::binary);for(int c=0;c<CASES;++c)for(int n=0;n<THERMAL;++n)for(int row=0;row<b.d;++row){C value=get(states[c*BATCHES+n/B],b.d,row,n%B);double pair[2]={value.real(),value.imag()};binary.write(reinterpret_cast<char*>(pair),sizeof(pair));}binary.close();if(!binary)throw std::runtime_error("endpoint write failed");
 double q=in.nbar/(1+in.nbar),base=std::pow(1-q,7),retained=0;std::array<double,THERMAL>weight;for(int n=0;n<THERMAL;++n){weight[n]=base*std::pow(q,b.degree[n]);retained+=weight[n];}
 std::cout<<std::setprecision(17)<<"{\"status\":\"COMPLETED\",\"scope\":\"finite_Galerkin_RK4_FP_estimate_not_certificate\",\"cutoff\":"<<cutoff<<",\"thermal_cutoff\":3,\"thermal_columns\":120,\"dimension\":"<<b.d<<",\"steps_per_segment\":"<<sub<<",\"cases\":6,\"tasks\":90,\"threads\":80,\"retained_thermal_weight\":"<<retained<<",\"omitted_thermal_weight\":"<<1-retained<<",\"preparation_seconds\":"<<prep_seconds<<",\"kernel_seconds\":"<<kernel_seconds<<",\"fixtures\":{\"dense_displacement_error\":"<<fixture.dense_error<<",\"adjoint_error\":"<<fixture.adjoint_error<<",\"zero_error\":"<<fixture.zero_error<<",\"hermiticity_error\":"<<fixture.hermiticity_error<<",\"single_mode_error\":"<<fixture.single_mode_error<<"},\"branches\":[";
 for(int c=0;c<CASES;++c){if(c)std::cout<<',';C overlap=0;double normerror=0,boundary=0,residual=0,deficit=0;
  for(int n=0;n<THERMAL;++n){auto&d=diagnostics[c*BATCHES+n/B];int lane=n%B;overlap+=weight[n]*get(states[c*BATCHES+n/B],b.d,n,lane);normerror=std::max(normerror,d.norm_error[lane]);boundary=std::max(boundary,d.boundary[lane]);residual+=weight[n]*d.integral[lane]*d.integral[lane];deficit=std::min(deficit,d.min_deficit);}
  std::cout<<"{\"case\":"<<c<<",\"sign\":"<<(c<3?1:-1)<<",\"labels\":["<<LABELS[c%3][0]<<','<<LABELS[c%3][1]<<"],\"active_steps\":"<<prepared.steps[c].size()<<",\"retained_same_branch_overlap\":";complex_json(overlap);std::cout<<",\"max_norm_error\":"<<normerror<<",\"max_boundary_weight\":"<<boundary<<",\"sampled_projection_residual_integral\":"<<std::sqrt(residual)<<",\"minimum_displacement_norm_deficit\":"<<deficit<<",\"linear_phase\":"<<prepared.final[c].phase<<",\"linear_alpha\":[";for(int m=0;m<M;++m){if(m)std::cout<<',';complex_json(prepared.final[c].alpha[m]);}std::cout<<"]}";
 }
 std::cout<<"],\"pair_coherences\":[";Workspace w(b.d);V displaced(2*b.d*B);bool first=true;
 for(int sign=0;sign<2;++sign)for(int a=0;a<3;++a)for(int bb=a+1;bb<3;++bb){int c=3*sign+a,d=3*sign+bb;C overlap=0;std::array<C,M>delta;double phase=prepared.final[c].phase-prepared.final[d].phase,r=0;
  for(int m=0;m<M;++m){delta[m]=prepared.final[c].alpha[m]-prepared.final[d].alpha[m];phase+=std::imag(std::conj(prepared.final[d].alpha[m])*prepared.final[c].alpha[m]);r+=(in.nbar+0.5)*std::norm(delta[m]);}
  for(int batch=0;batch<BATCHES;++batch){displacement(b,states[c*BATCHES+batch],displaced,delta,w);for(int lane=0;lane<B;++lane){C inner=0;for(int n=0;n<b.d;++n)inner+=std::conj(get(states[d*BATCHES+batch],b.d,n,lane))*get(displaced,b.d,n,lane);overlap+=weight[batch*B+lane]*inner;}}
  C sine=std::polar(1.0,phase)*overlap,linear=std::exp(C(-r,phase));if(!first)std::cout<<',';first=false;std::cout<<"{\"cases\":["<<c<<','<<d<<"],\"sine_retained\":";complex_json(sine);std::cout<<",\"linear_full\":";complex_json(linear);std::cout<<",\"witness_center\":"<<std::abs(sine-linear)/2<<",\"thermal_radius\":"<<(1-retained)/2<<'}';
 }
 std::cout<<"],\"thread_map\":[";for(int t=0;t<80;++t){if(t)std::cout<<',';std::cout<<"{\"thread\":"<<t<<",\"cpu\":"<<cpus[t]<<",\"place\":"<<places[t]<<'}';}std::cout<<"],\"end_to_end_seconds\":"<<omp_get_wtime()-t0<<"}\n";
 return 0;
}catch(const std::exception&e){std::cerr<<e.what()<<'\n';return 2;}}
