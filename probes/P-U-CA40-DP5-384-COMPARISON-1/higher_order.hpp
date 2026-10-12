// Copyright 2026 A. M. Thorn. SPDX-License-Identifier: Apache-2.0
// Include only after the unchanged sealed kernel.cpp definitions.
#pragma once
#include "dp5_tableau.hpp"
namespace integrator_panel {
struct Arm {char id;int steps;const char*integrator;const char*dense;int substeps,rhs;};
inline Arm arm(char id){
 if(id=='A')return {'A',512,"RK4","QUINTIC_ENDPOINT_DIRECTIONAL_FD",1,9};
 if(id=='C')return {'C',384,"DP5_TWO_HALF_STEPS","QUINTIC_THREE_POINT_HERMITE",2,13};
 throw std::runtime_error("arm must be A or C");
}
inline std::string layout(const Arm&a){
 return "INTEGRATOR_LOCAL_WINDOWS_V1\narm="+std::string(1,a.id)+"\nsteps="+std::to_string(a.steps)+
  "\nintegrator="+a.integrator+"\ndense_curve="+a.dense+
  "\nsubsteps_per_cell="+std::to_string(a.substeps)+"\nrhs_per_cell="+std::to_string(a.rhs)+
  "\nactual_substeps_per_window="+std::to_string(a.substeps*(a.steps/128))+
  "\nwindows=4\ncases=6\ncolumns=120\ndimension=6435\ncomponents=12\n"
  "endpoints=window,case,column,basis,re_im\ncomponents=window,case,column,field\n"
  "encoding=little_endian_IEEE_binary64\n";
}
} // namespace integrator_panel

#if HIGHER_ORDER_CANDIDATE
struct HigherWork {
 std::array<V,5> k;V stage,midpoint,f0,fmid;
 explicit HigherWork(int d):stage(2*d*B),midpoint(stage.size()),f0(stage.size()),fmid(stage.size()){
  for(auto&v:k)v.resize(stage.size());
 }
};

// Five new internal stages plus the derivative at the actually stored output.
// The incoming derivative is reused, never confused with the c=1 stage k6.
AVX int dp5_half_step(const Basis&b,const V&input,V&output,const V&finput,V&foutput,
                     const vm::Cell&cell,int offset,double step,Work&w,HigherWork&high){
 if(&input==&output||&finput==&foutput||&output==&foutput)throw std::runtime_error("DP5 half-step alias");
 std::array<const V*,6>derivatives{};derivatives[0]=&finput;
 for(int stage=1;stage<6;++stage){
  high.stage=input;
  for(int previous=0;previous<stage;++previous){const auto q=dp5::A[stage][previous];if(q.n)axpy(high.stage,*derivatives[previous],step*dp5::value(q));}
  generator(b,high.stage,high.k[stage-1],cell.stage[offset+stage],w);derivatives[stage]=&high.k[stage-1];
 }
 output=input;
 for(int stage=0;stage<6;++stage){const auto q=dp5::B[stage];if(q.n)axpy(output,*derivatives[stage],step*dp5::value(q));}
 generator(b,output,foutput,cell.stage[offset+5],w);
 return 6;
}

AVX void higher_order_step(const Basis&b,V&y,const vm::Cell&cell,Work&w,HigherWork&high){
 const double h=mid(cell.h);w.initial=y;
 generator(b,w.initial,high.f0,cell.stage[0],w);int rhs=1;
 rhs+=dp5_half_step(b,w.initial,high.midpoint,high.f0,high.fmid,cell,0,h/2,w,high);
 rhs+=dp5_half_step(b,high.midpoint,y,high.fmid,w.f1,cell,5,h/2,w,high);
 if(rhs!=13)throw std::runtime_error("DP5 fixed RHS inventory");
 for(size_t k=0;k<y.size();++k){
  const double c0=w.initial[k],c1=h*high.f0[k];
  const double aa=high.midpoint[k]-c0-c1/2,bb=h*high.fmid[k]-c1;
  const double cc=y[k]-c0-c1,dd=h*w.f1[k]-c1;
  // c0 is an exact copy of the incoming dyadic state. The existing certifier
  // accounts for the final polynomial/output jump; no initial jump is hidden.
  w.poly[0][k]=c0;w.poly[1][k]=c1;
  w.poly[2][k]=16*aa-8*bb+7*cc-dd;
  w.poly[3][k]=-32*aa+32*bb-34*cc+5*dd;
  w.poly[4][k]=16*aa-40*bb+52*cc-8*dd;
  w.poly[5][k]=16*bb-24*cc+4*dd;
  if(!std::isfinite(y[k]))throw std::runtime_error("nonfinite DP5 endpoint");
  for(int j=0;j<6;++j)if(!std::isfinite(w.poly[j][k]))throw std::runtime_error("nonfinite Hermite coefficient");
 }
}
#endif
