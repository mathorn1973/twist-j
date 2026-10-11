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

constexpr int CMP_WINDOWS=4,CMP_DIMENSION=6435,CMP_FIELDS=12;
constexpr int CMP_ROWS=CMP_WINDOWS*CASES*THERMAL;
std::string comparison_layout(int steps){
 return "GRID_LOCAL_WINDOWS_V1\nsteps="+std::to_string(steps)+
  "\nwindows=4\ncases=6\ncolumns=120\ndimension=6435\ncomponents=12\n"
  "endpoints=window,case,column,basis,re_im\ncomponents=window,case,column,field\n"
  "encoding=little_endian_IEEE_binary64\n";
}
void comparison_validate_layout(const std::filesystem::path&dir,int steps){
 if(!std::filesystem::is_directory(dir))throw std::runtime_error("state directory missing");
 std::ifstream in(dir/"layout.txt",std::ios::binary);if(!in)throw std::runtime_error("layout missing");
 std::string text((std::istreambuf_iterator<char>(in)),std::istreambuf_iterator<char>());
 if(in.bad()||text!=comparison_layout(steps))throw std::runtime_error("wrong grid or binary layout");
 if(std::filesystem::file_size(dir/"endpoints.bin")!=uintmax_t(CMP_ROWS)*CMP_DIMENSION*2*sizeof(double)||
    std::filesystem::file_size(dir/"components.bin")!=uintmax_t(CMP_ROWS)*CMP_FIELDS*sizeof(double))throw std::runtime_error("wrong binary file size");
}
void comparison_read(std::ifstream&in,double*data,size_t count){
 in.read(reinterpret_cast<char*>(data),std::streamsize(count*sizeof(double)));
 if(!in)throw std::runtime_error("short binary read");
 for(size_t k=0;k<count;++k)if(!std::isfinite(data[k]))throw std::runtime_error("nonfinite saved value");
}
AVX I comparison_distance(const V&fine,const V&coarse){
 I norm2=exact(0);
 for(size_t k=0;k<fine.size();++k){I difference=sub(exact(fine[k]),exact(coarse[k]));norm2=add(norm2,sq(difference));}
 check(norm2);I distance=root(norm2);check(distance);return distance;
}

int main(int argc,char**argv){try{
 std::string fine,coarse,output;
 for(int i=1;i<argc;i+=2){if(i+1>=argc)throw std::runtime_error("missing CLI value");std::string key=argv[i];
  if(key=="--fine"&&fine.empty())fine=argv[i+1];else if(key=="--coarse"&&coarse.empty())coarse=argv[i+1];
  else if(key=="--output"&&output.empty())output=argv[i+1];else throw std::runtime_error("unknown or duplicate CLI argument");
 }
 if(fine.empty()||coarse.empty()||output.empty()||!std::filesystem::path(fine).is_absolute()||!std::filesystem::path(coarse).is_absolute()||!std::filesystem::path(output).is_absolute())throw std::runtime_error("absolute fine/coarse/output paths required");
 if(std::filesystem::exists(output))throw std::runtime_error("output JSON must be new");
 if constexpr(std::endian::native!=std::endian::little)throw std::runtime_error("little-endian required");
 if(sizeof(double)!=8||!std::numeric_limits<double>::is_iec559)throw std::runtime_error("IEEE binary64 required");
 __builtin_cpu_init();if(!__builtin_cpu_supports("avx512f")||!__builtin_cpu_supports("avx512dq")||!__builtin_cpu_supports("avx512vl"))throw std::runtime_error("AVX512 unavailable");
 floating_environment();comparison_validate_layout(fine,512);comparison_validate_layout(coarse,256);
 std::ifstream fe(std::filesystem::path(fine)/"endpoints.bin",std::ios::binary),ce(std::filesystem::path(coarse)/"endpoints.bin",std::ios::binary),fc(std::filesystem::path(fine)/"components.bin",std::ios::binary),cc(std::filesystem::path(coarse)/"components.bin",std::ios::binary);
 if(!fe||!ce||!fc||!cc)throw std::runtime_error("binary open failed");
 double started=omp_get_wtime();V fv(2*CMP_DIMENSION),cv(2*CMP_DIMENSION);std::array<double,CMP_FIELDS>fcomp{},ccomp{};
 int compatible=0,inconsistent=0,unresolved=0;double max_d_hi=0,max_R=0;
 std::ostringstream records;records<<std::setprecision(17);
 for(int row=0;row<CMP_ROWS;++row){
  comparison_read(fe,fv.data(),fv.size());comparison_read(ce,cv.data(),cv.size());comparison_read(fc,fcomp.data(),fcomp.size());comparison_read(cc,ccomp.data(),ccomp.size());
  for(double x:fcomp)if(x<0)throw std::runtime_error("negative fine component");
  for(double x:ccomp)if(x<0)throw std::runtime_error("negative coarse component");
  if(fcomp[10]>fcomp[11]||ccomp[10]>ccomp[11])throw std::runtime_error("inverted saved norm interval");
  I d=comparison_distance(fv,cv);double R=au(fcomp[4],ccomp[4]);if(!std::isfinite(R))throw std::runtime_error("nonfinite radius sum");
  const char*status;
  if(d.hi<=R){status="COMPATIBLE";++compatible;}else if(d.lo>R){status="INCONSISTENT";++inconsistent;}else{status="UNRESOLVED";++unresolved;}
  max_d_hi=std::max(max_d_hi,d.hi);max_R=std::max(max_R,R);
  if(row)records<<',';
  records<<"{\"window\":"<<row/(CASES*THERMAL)<<",\"case\":"<<(row/THERMAL)%CASES<<",\"column\":"<<row%THERMAL<<",\"d_lo\":"<<d.lo<<",\"d_hi\":"<<d.hi<<",\"eps_fine\":"<<fcomp[4]<<",\"eps_coarse\":"<<ccomp[4]<<",\"R\":"<<R<<",\"status\":\""<<status<<"\"}";
 }
 std::ostringstream summary;summary<<std::setprecision(17)<<"{\"status\":\"COMPLETED\",\"scope\":\"LOCAL_WINDOW_ENDPOINT_CONSISTENCY_ONLY\",\"full_trajectory_certificate\":false,\"propagation_executed\":false,\"normalization_applied\":false,\"phase_fit_applied\":false,\"fine_steps\":512,\"coarse_steps\":256,\"windows\":4,\"cases\":6,\"thermal_columns\":120,\"dimension\":6435,\"records\":2880,\"COMPATIBLE\":"<<compatible<<",\"INCONSISTENT\":"<<inconsistent<<",\"UNRESOLVED\":"<<unresolved<<",\"max_d_hi\":"<<max_d_hi<<",\"max_R\":"<<max_R<<",\"comparison_seconds\":"<<omp_get_wtime()-started<<",\"decisions\":["<<records.str()<<"]}\n";
 std::ofstream out(output);if(!out)throw std::runtime_error("output JSON open failed");out<<summary.str();out.close();if(!out)throw std::runtime_error("output JSON write failed");
 std::cout<<"{\"status\":\"COMPLETED\",\"records\":2880,\"COMPATIBLE\":"<<compatible<<",\"INCONSISTENT\":"<<inconsistent<<",\"UNRESOLVED\":"<<unresolved<<"}\n";
 return 0;
}catch(const std::exception&e){std::cerr<<e.what()<<'\n';return 2;}}
