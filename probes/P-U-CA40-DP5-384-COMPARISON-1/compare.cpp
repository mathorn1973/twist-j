// Copyright 2026 A. M. Thorn. SPDX-License-Identifier: Apache-2.0
// Read-only directed-arithmetic comparison of already saved local endpoints.
#ifndef BENCHMARK_KERNEL
#error "BENCHMARK_KERNEL must name the sealed optimized kernel.cpp"
#endif
#define main unused_full_campaign_main
#include BENCHMARK_KERNEL
#undef main
#include <iterator>
#include <sstream>
#include "higher_order.hpp"

constexpr int CMP_WINDOWS=4,CMP_DIMENSION=6435,CMP_FIELDS=12;
constexpr int CMP_ROWS=CMP_WINDOWS*CASES*THERMAL;
integrator_panel::Arm comparison_validate_layout(const std::filesystem::path&dir){
 if(!std::filesystem::is_directory(dir))throw std::runtime_error("state directory missing");
 std::ifstream in(dir/"layout.txt",std::ios::binary);if(!in)throw std::runtime_error("layout missing");
 std::string text((std::istreambuf_iterator<char>(in)),std::istreambuf_iterator<char>());
 if(in.bad())throw std::runtime_error("layout read failed");
 if(std::filesystem::file_size(dir/"endpoints.bin")!=uintmax_t(CMP_ROWS)*CMP_DIMENSION*2*sizeof(double)||
    std::filesystem::file_size(dir/"components.bin")!=uintmax_t(CMP_ROWS)*CMP_FIELDS*sizeof(double))throw std::runtime_error("wrong binary file size");
 for(char id:{'A','C'}){const auto arm=integrator_panel::arm(id);if(text==integrator_panel::layout(arm))return arm;}
 throw std::runtime_error("wrong integrator or binary layout");
}
void comparison_read(std::ifstream&in,double*data,size_t count){
 in.read(reinterpret_cast<char*>(data),std::streamsize(count*sizeof(double)));
 if(!in)throw std::runtime_error("short binary read");
 for(size_t k=0;k<count;++k)if(!std::isfinite(data[k]))throw std::runtime_error("nonfinite saved value");
}
AVX I comparison_distance(const V&left,const V&right){
 I norm2=exact(0);
 for(size_t k=0;k<left.size();++k){I difference=sub(exact(left[k]),exact(right[k]));norm2=add(norm2,sq(difference));}
 check(norm2);I distance=root(norm2);check(distance);return distance;
}

int main(int argc,char**argv){try{
 std::string left,right,output;
 for(int i=1;i<argc;i+=2){if(i+1>=argc)throw std::runtime_error("missing CLI value");std::string key=argv[i];
  if(key=="--left"&&left.empty())left=argv[i+1];else if(key=="--right"&&right.empty())right=argv[i+1];
  else if(key=="--output"&&output.empty())output=argv[i+1];else throw std::runtime_error("unknown or duplicate CLI argument");
 }
 if(left.empty()||right.empty()||output.empty()||!std::filesystem::path(left).is_absolute()||!std::filesystem::path(right).is_absolute()||!std::filesystem::path(output).is_absolute())throw std::runtime_error("absolute left/right/output paths required");
 if(std::filesystem::exists(output))throw std::runtime_error("output JSON must be new");
 if constexpr(std::endian::native!=std::endian::little)throw std::runtime_error("little-endian required");
 if(sizeof(double)!=8||!std::numeric_limits<double>::is_iec559)throw std::runtime_error("IEEE binary64 required");
 __builtin_cpu_init();if(!__builtin_cpu_supports("avx512f")||!__builtin_cpu_supports("avx512dq")||!__builtin_cpu_supports("avx512vl"))throw std::runtime_error("AVX512 unavailable");
 floating_environment();const auto left_arm=comparison_validate_layout(left),right_arm=comparison_validate_layout(right);
 if(left_arm.id==right_arm.id)throw std::runtime_error("comparison requires different arms");
 std::ifstream fe(std::filesystem::path(left)/"endpoints.bin",std::ios::binary),ce(std::filesystem::path(right)/"endpoints.bin",std::ios::binary),fc(std::filesystem::path(left)/"components.bin",std::ios::binary),cc(std::filesystem::path(right)/"components.bin",std::ios::binary);
 if(!fe||!ce||!fc||!cc)throw std::runtime_error("binary open failed");
 double started=omp_get_wtime();V fv(2*CMP_DIMENSION),cv(2*CMP_DIMENSION);std::array<double,CMP_FIELDS>fcomp{},ccomp{};
 int compatible=0,inconsistent=0,unresolved=0;double max_d_hi=0,max_R=0;
 std::ostringstream records;records<<std::setprecision(17);
 for(int row=0;row<CMP_ROWS;++row){
  comparison_read(fe,fv.data(),fv.size());comparison_read(ce,cv.data(),cv.size());comparison_read(fc,fcomp.data(),fcomp.size());comparison_read(cc,ccomp.data(),ccomp.size());
  for(double x:fcomp)if(x<0)throw std::runtime_error("negative left component");
  for(double x:ccomp)if(x<0)throw std::runtime_error("negative right component");
  if(fcomp[10]>fcomp[11]||ccomp[10]>ccomp[11])throw std::runtime_error("inverted saved norm interval");
  I d=comparison_distance(fv,cv);double R=au(fcomp[4],ccomp[4]);if(!std::isfinite(R))throw std::runtime_error("nonfinite radius sum");
  const char*status;
  if(d.hi<=R){status="COMPATIBLE";++compatible;}else if(d.lo>R){status="INCONSISTENT";++inconsistent;}else{status="UNRESOLVED";++unresolved;}
  max_d_hi=std::max(max_d_hi,d.hi);max_R=std::max(max_R,R);
  if(row)records<<',';
  records<<"{\"window\":"<<row/(CASES*THERMAL)<<",\"case\":"<<(row/THERMAL)%CASES<<",\"column\":"<<row%THERMAL<<",\"d_lo\":"<<d.lo<<",\"d_hi\":"<<d.hi<<",\"eps_left\":"<<fcomp[4]<<",\"eps_right\":"<<ccomp[4]<<",\"R\":"<<R<<",\"status\":\""<<status<<"\"}";
 }
 std::ostringstream summary;summary<<std::setprecision(17)<<"{\"status\":\"COMPLETED\",\"scope\":\"LOCAL_WINDOW_ENDPOINT_CONSISTENCY_ONLY\",\"full_trajectory_certificate\":false,\"propagation_executed\":false,\"normalization_applied\":false,\"phase_fit_applied\":false,\"left_arm\":\""<<left_arm.id<<"\",\"right_arm\":\""<<right_arm.id<<"\",\"left_steps\":"<<left_arm.steps<<",\"right_steps\":"<<right_arm.steps<<",\"windows\":4,\"cases\":6,\"thermal_columns\":120,\"dimension\":6435,\"records\":2880,\"COMPATIBLE\":"<<compatible<<",\"INCONSISTENT\":"<<inconsistent<<",\"UNRESOLVED\":"<<unresolved<<",\"max_d_hi\":"<<max_d_hi<<",\"max_R\":"<<max_R<<",\"comparison_seconds\":"<<omp_get_wtime()-started<<",\"decisions\":["<<records.str()<<"]}\n";
 std::ofstream out(output);if(!out)throw std::runtime_error("output JSON open failed");out<<summary.str();out.close();if(!out)throw std::runtime_error("output JSON write failed");
 std::cout<<"{\"status\":\"COMPLETED\",\"records\":2880,\"COMPATIBLE\":"<<compatible<<",\"INCONSISTENT\":"<<inconsistent<<",\"UNRESOLVED\":"<<unresolved<<"}\n";
 return 0;
}catch(const std::exception&e){std::cerr<<e.what()<<'\n';return 2;}}
