// Copyright 2026 A. M. Thorn. SPDX-License-Identifier: Apache-2.0
// Fixed four-cell prefix performance experiment, never a full certificate.
// Compilation is permitted before pinning; execution is not.
#ifndef BENCHMARK_KERNEL
#error "BENCHMARK_KERNEL must name the selected immutable/optimized kernel.cpp"
#endif
#ifndef BENCHMARK_VARIANT
#error "BENCHMARK_VARIANT must be the string baseline or optimized"
#endif
#define main unused_full_campaign_main
#include BENCHMARK_KERNEL
#undef main
#include <memory>
#include <type_traits>

constexpr int PREFIX_L=8,PREFIX_G=10,PREFIX_N=512,PREFIX_CELLS=4;
constexpr int PREFIX_FIELDS=12;
const std::array<const char*,PREFIX_FIELDS> PREFIX_FIELD_NAMES={
 "guard","tail","continuum","jumps","total",
 "sampled_time_node_L2","sampled_projection_node_L2","sampled_arithmetic_node_L2",
 "maximum_node_bound","maximum_norm_error","endpoint_norm_squared_lo","endpoint_norm_squared_hi"
};

// This is a constructor compatibility adapter only. It does not select a
// numerical method at runtime or call the renamed long-campaign entry point.
template<class T> std::unique_ptr<T> prefix_ball_work(int guard_dimension,int candidate_dimension){
 if constexpr(std::is_constructible_v<T,int,int>)return std::make_unique<T>(guard_dimension,candidate_dimension);
 else return std::make_unique<T>(guard_dimension);
}

std::array<double,PREFIX_FIELDS> prefix_components(const Certificate&c,int lane,I norm){
 std::array<double,PREFIX_FIELDS> result={c.guard[lane],c.tail[lane],c.tube[lane],c.jumps[lane],c.total[lane],
  c.sampled_time_node_L2[lane],c.sampled_projection_node_L2[lane],c.sampled_arithmetic_node_L2[lane],
  c.max_node[lane],c.max_norm_error[lane],norm.lo,norm.hi};
 for(double value:result)if(!std::isfinite(value))throw std::runtime_error("nonfinite prefix component");
 return result;
}

void prefix_binary_write(std::ofstream&out,const double*values,size_t count){
 out.write(reinterpret_cast<const char*>(values),std::streamsize(count*sizeof(double)));
 if(!out)throw std::runtime_error("prefix binary write failed");
}

int main(int argc,char**argv){try{
 std::string input,output,variant=BENCHMARK_VARIANT;
 if(variant!="baseline"&&variant!="optimized")throw std::runtime_error("invalid compile-time variant");
 for(int i=1;i<argc;i+=2){if(i+1>=argc)throw std::runtime_error("missing CLI value");std::string key=argv[i];
  if(key=="--input")input=argv[i+1];else if(key=="--output")output=argv[i+1];else throw std::runtime_error("prefix accepts only --input and --output");
 }
 if(input.empty()||output.empty()||!std::filesystem::path(input).is_absolute()||!std::filesystem::path(output).is_absolute())throw std::runtime_error("absolute input/output paths required");
 if constexpr(std::endian::native!=std::endian::little)throw std::runtime_error("little-endian binary format required");
 if(sizeof(double)!=8||!std::numeric_limits<double>::is_iec559)throw std::runtime_error("IEEE binary64 required");
 __builtin_cpu_init();if(!__builtin_cpu_supports("avx512f")||!__builtin_cpu_supports("avx512dq")||!__builtin_cpu_supports("avx512vl"))throw std::runtime_error("AVX512 unavailable");
 floating_environment();
 if(!std::filesystem::create_directory(output))throw std::runtime_error("output directory must be new");
 double begin=omp_get_wtime();std::ofstream lifecycle(std::filesystem::path(output)/"lifecycle.jsonl");
 if(!lifecycle)throw std::runtime_error("lifecycle open failed");
 lifecycle<<std::setprecision(17)<<"{\"phase\":\"model_preparation_started\",\"elapsed_seconds\":0}\n";lifecycle.flush();
 vm::Prepared prepared=vm::prepare(input,PREFIX_L,PREFIX_G,PREFIX_N);
 lifecycle<<"{\"phase\":\"model_preparation_completed\",\"elapsed_seconds\":"<<omp_get_wtime()-begin<<"}\n";lifecycle.flush();
 Basis b(PREFIX_L,prepared),g(PREFIX_G,prepared);if(b.start[4]!=THERMAL)throw std::runtime_error("thermal basis mismatch");
 for(int c=0;c<CASES;++c)if(prepared.cells[c].size()<PREFIX_CELLS)throw std::runtime_error("insufficient prepared prefix cells");
 Fixtures fixture=fixtures(prepared);
 lifecycle<<"{\"phase\":\"fixtures_completed\",\"elapsed_seconds\":"<<omp_get_wtime()-begin<<"}\n";lifecycle.flush();
 if(!lifecycle)throw std::runtime_error("lifecycle write failed");
 double preparation_seconds=omp_get_wtime()-begin;
 std::vector<V>states(CASES*BATCHES);std::vector<Certificate>certs(CASES*BATCHES);
 std::array<int,80>cpus{},places{};cpus.fill(-1);places.fill(-1);
 std::atomic<int>done{0},migrations{0};std::atomic<bool>failed{false};std::mutex lock;std::string failure;int workers=0;
 std::ofstream progress(std::filesystem::path(output)/"progress.jsonl");if(!progress)throw std::runtime_error("progress open failed");progress<<std::setprecision(17);
 omp_set_dynamic(0);omp_set_num_threads(80);
 if(omp_get_proc_bind()==omp_proc_bind_false)throw std::runtime_error("OpenMP binding required");
 double scan_begin=omp_get_wtime();
 #pragma omp parallel
 {
  int tid=omp_get_thread_num();std::unique_ptr<Work>w;std::unique_ptr<BWork>bw;
  #pragma omp single
  workers=omp_get_num_threads();
  try{
   if(tid<0||tid>=80)throw std::runtime_error("thread index outside fixed domain");
   cpus[tid]=sched_getcpu();places[tid]=omp_get_place_num();floating_environment();
   w=std::make_unique<Work>(b.d);bw=prefix_ball_work<BWork>(g.d,b.d);
  }catch(const std::exception&e){std::lock_guard<std::mutex>guard(lock);failed=true;if(failure.empty())failure=e.what();}
  #pragma omp barrier
  #pragma omp for schedule(dynamic,1)
  for(int task=0;task<CASES*BATCHES;++task){if(failed.load())continue;
   try{
    int c=task/BATCHES,batch=task%BATCHES;V y(2*b.d*B);
    for(int lane=0;lane<B;++lane)put(y,b.d,batch*B+lane,lane,1);
    // The only dynamics loop reachable from this benchmark entry point.
    // Four occupied cells are fixed; CLI arguments cannot enlarge it.
    for(int cell=0;cell<PREFIX_CELLS;++cell){hermite_step(b,y,prepared.cells[c][cell],*w);certify(prepared,b,g,prepared.cells[c][cell],y,*w,*bw,certs[task]);}
    states[task]=std::move(y);int count=++done;std::lock_guard<std::mutex>guard(lock);
    progress<<"{\"completed\":"<<count<<",\"case\":"<<c<<",\"batch\":"<<batch<<",\"cells\":4,\"elapsed_seconds\":"<<omp_get_wtime()-scan_begin<<"}\n";progress.flush();
    if(!progress)throw std::runtime_error("progress write failed");
   }catch(const std::exception&e){std::lock_guard<std::mutex>guard(lock);failed=true;if(failure.empty())failure=e.what();}
  }
  if(tid>=0&&tid<80&&cpus[tid]!=sched_getcpu())++migrations;
 }
 double kernel_seconds=omp_get_wtime()-scan_begin;progress.close();
 if(failed||done!=CASES*BATCHES)throw std::runtime_error("partial prefix experiment: "+failure);
 if(workers!=80||migrations)throw std::runtime_error("worker count or migration");
 std::array<bool,80>seen{};
 for(int t=0;t<80;++t){if(cpus[t]<0||cpus[t]>=80||places[t]<0||places[t]>=80||seen[cpus[t]])throw std::runtime_error("invalid CPU placement");seen[cpus[t]]=true;}
 seen.fill(false);for(int t=0;t<80;++t){if(seen[places[t]])throw std::runtime_error("duplicate OpenMP place");seen[places[t]]=true;}
 lifecycle<<"{\"phase\":\"prefix_scan_completed\",\"elapsed_seconds\":"<<omp_get_wtime()-begin<<"}\n";lifecycle.flush();
 if(!lifecycle)throw std::runtime_error("lifecycle write failed");

 std::ofstream basisfile(std::filesystem::path(output)/"basis.json");
 basisfile<<"{\"scope\":\"PREFIX_PERFORMANCE_ONLY\",\"cutoff\":8,\"guard\":10,\"thermal_cutoff\":3,\"occupations\":[";
 for(int row=0;row<b.d;++row){if(row)basisfile<<',';basisfile<<'[';for(int m=0;m<M;++m){if(m)basisfile<<',';basisfile<<b.n[row][m];}basisfile<<']';}basisfile<<"]}\n";basisfile.close();if(!basisfile)throw std::runtime_error("basis write failed");
 std::ofstream endpoints(std::filesystem::path(output)/"endpoints.bin",std::ios::binary),components(std::filesystem::path(output)/"components.bin",std::ios::binary);
 if(!endpoints||!components)throw std::runtime_error("binary output open failed");
 std::array<std::array<I,THERMAL>,CASES>norms{};
 for(int c=0;c<CASES;++c)for(int batch=0;batch<BATCHES;++batch){auto values=center_norm2(states[c*BATCHES+batch],b.d);for(int lane=0;lane<B;++lane)norms[c][batch*B+lane]=values[lane];}
 for(int c=0;c<CASES;++c)for(int column=0;column<THERMAL;++column){
  for(int row=0;row<b.d;++row){C value=get(states[c*BATCHES+column/B],b.d,row,column%B);double pair[2]={value.real(),value.imag()};if(!std::isfinite(pair[0])||!std::isfinite(pair[1]))throw std::runtime_error("nonfinite prefix endpoint");prefix_binary_write(endpoints,pair,2);}
  auto values=prefix_components(certs[c*BATCHES+column/B],column%B,norms[c][column]);prefix_binary_write(components,values.data(),values.size());
 }
 endpoints.close();components.close();if(!endpoints||!components)throw std::runtime_error("binary output close failed");
 auto endpoint_bytes=std::filesystem::file_size(std::filesystem::path(output)/"endpoints.bin"),component_bytes=std::filesystem::file_size(std::filesystem::path(output)/"components.bin");
 const uintmax_t expected_endpoint_bytes=uintmax_t(CASES)*THERMAL*b.d*2*sizeof(double),expected_component_bytes=uintmax_t(CASES)*THERMAL*PREFIX_FIELDS*sizeof(double);
 if(endpoint_bytes!=expected_endpoint_bytes||component_bytes!=expected_component_bytes)throw std::runtime_error("binary output size mismatch");
 std::cout<<std::setprecision(17)<<"{\"status\":\"COMPLETED\",\"scope\":\"PREFIX_PERFORMANCE_ONLY\",\"variant\":\""<<variant<<"\",\"full_trajectory_certificate\":false,\"final_coherences_computed\":false,\"cutoff\":8,\"guard\":10,\"steps_per_segment\":512,\"prefix_occupied_cells_per_task\":4,\"tasks\":90,\"cases\":6,\"thermal_columns\":120,\"thermal_cutoff\":3,\"simd_lanes\":8,\"threads\":80,\"dimension\":"<<b.d<<",\"guard_dimension\":"<<g.d<<",\"preparation_seconds\":"<<preparation_seconds<<",\"model_preparation_seconds\":"<<prepared.preparation_seconds<<",\"kernel_seconds\":"<<kernel_seconds<<",\"mpfr_version\":\""<<prepared.mpfr_version<<"\",\"migrations\":"<<migrations<<",\"endpoint_bytes\":"<<endpoint_bytes<<",\"component_bytes\":"<<component_bytes<<",\"binary_layout\":\"little-endian IEEE64; endpoints: case,column,basis,re/im; components: case,column,component_fields\",\"fixtures\":{\"dense_displacement_error\":"<<fixture.dense_error<<",\"collective_displacement_error\":"<<fixture.collective_error<<",\"directed_arithmetic\":true,\"zero_displacement_enclosure\":true,\"adjoint_enclosure\":true,\"ball_interval_fixture_enclosure\":true,\"ball_reference_radius_ratio\":"<<fixture.ball_reference_ratio<<"},\"component_fields\":[";
 for(int k=0;k<PREFIX_FIELDS;++k){if(k)std::cout<<',';std::cout<<'"'<<PREFIX_FIELD_NAMES[k]<<'"';}
 std::cout<<"],\"branches\":[";
 for(int c=0;c<CASES;++c){if(c)std::cout<<',';std::cout<<"{\"case\":"<<c<<",\"labels\":["<<LABELS[c%3][0]<<','<<LABELS[c%3][1]<<"],\"available_full_trajectory_cells\":"<<prepared.cells[c].size()<<",\"columns\":[";
  for(int column=0;column<THERMAL;++column){if(column)std::cout<<',';auto values=prefix_components(certs[c*BATCHES+column/B],column%B,norms[c][column]);std::cout<<"{\"thermal_index\":"<<column;for(int k=0;k<PREFIX_FIELDS;++k)std::cout<<",\""<<PREFIX_FIELD_NAMES[k]<<"\":"<<values[k];std::cout<<'}';}std::cout<<"]}";
 }
 std::cout<<"],\"thread_map\":[";for(int t=0;t<80;++t){if(t)std::cout<<',';std::cout<<"{\"thread\":"<<t<<",\"cpu\":"<<cpus[t]<<",\"place\":"<<places[t]<<'}';}
 std::cout<<"],\"end_to_end_seconds\":"<<omp_get_wtime()-begin<<"}\n";return 0;
}catch(const std::exception&e){std::cerr<<e.what()<<'\n';return 2;}}
