// Copyright 2026 A. M. Thorn. SPDX-License-Identifier: Apache-2.0
// Four adjacent checkpoints of one short prefix; no intermediate reset.
#ifndef BENCHMARK_KERNEL
#error "BENCHMARK_KERNEL must name the sealed optimized kernel.cpp"
#endif
#define main unused_full_campaign_main
#include BENCHMARK_KERNEL
#undef main
#include <memory>
#include <sstream>
#include <cstring>
#include "higher_order.hpp"

constexpr int GRID_L=8,GRID_G=10,GRID_WINDOWS=4,GRID_FIELDS=12;
constexpr int GRID_TASKS=CASES*BATCHES,GRID_SNAPSHOTS=GRID_WINDOWS*GRID_TASKS;
constexpr std::array<int,CASES> TASK_CASE_ORDER={1,2,4,5,0,3};
const std::array<const char*,GRID_FIELDS> GRID_FIELD_NAMES={
 "guard","tail","continuum","jumps","total",
 "sampled_time_node_L2","sampled_projection_node_L2","sampled_arithmetic_node_L2",
 "maximum_node_bound","maximum_norm_error","endpoint_norm_squared_lo","endpoint_norm_squared_hi"
};
struct PrefixCheckpoint {int absolute_segment,first_cell,block_cells,cumulative_cells;};

bool same_state(const V&a,const V&b){
 return a.size()==b.size()&&std::memcmp(a.data(),b.data(),a.size()*sizeof(double))==0;
}
std::array<const std::array<double,B>*,10> certificate_arrays(const Certificate&c){
 return {&c.guard,&c.tail,&c.tube,&c.jumps,&c.total,&c.max_node,&c.max_norm_error,
         &c.sampled_time_node_L2,&c.sampled_projection_node_L2,&c.sampled_arithmetic_node_L2};
}
bool same_certificate(const Certificate&a,const Certificate&b){
 auto aa=certificate_arrays(a),bb=certificate_arrays(b);
 for(size_t k=0;k<aa.size();++k)if(std::memcmp(aa[k]->data(),bb[k]->data(),B*sizeof(double)))return false;
 return true;
}
void check_monotone(const Certificate&before,const Certificate&after){
 auto aa=certificate_arrays(before),bb=certificate_arrays(after);
 for(size_t k=0;k<aa.size();++k)for(int lane=0;lane<B;++lane)
  if(!std::isfinite((*bb[k])[lane])||(*bb[k])[lane]<(*aa[k])[lane])throw std::runtime_error("cumulative certificate decreased or became nonfinite");
}

std::array<double,GRID_FIELDS> grid_components(const Certificate&c,int lane,I norm){
 std::array<double,GRID_FIELDS> values={c.guard[lane],c.tail[lane],c.tube[lane],c.jumps[lane],c.total[lane],
  c.sampled_time_node_L2[lane],c.sampled_projection_node_L2[lane],c.sampled_arithmetic_node_L2[lane],
  c.max_node[lane],c.max_norm_error[lane],norm.lo,norm.hi};
 for(double value:values)if(!std::isfinite(value)||value<0)throw std::runtime_error("invalid local component");
 if(norm.lo>norm.hi)throw std::runtime_error("inverted endpoint norm");
 return values;
}
void grid_write(std::ofstream&out,const double*values,size_t count){
 out.write(reinterpret_cast<const char*>(values),std::streamsize(count*sizeof(double)));
 if(!out)throw std::runtime_error("binary write failed");
}

int main(int argc,char**argv){try{
 std::string input,output;char arm_id=0;
 for(int i=1;i<argc;i+=2){if(i+1>=argc)throw std::runtime_error("missing CLI value");std::string key=argv[i];
  if(key=="--input"&&input.empty())input=argv[i+1];
  else if(key=="--output"&&output.empty())output=argv[i+1];
  else if(key=="--arm"&&!arm_id){std::string value=argv[i+1];if(value.size()!=1)throw std::runtime_error("arm must be A or C");arm_id=value[0];}
  else throw std::runtime_error("unknown or duplicate CLI argument");
 }
 if(input.empty()||output.empty()||!arm_id||!std::filesystem::path(input).is_absolute()||!std::filesystem::path(output).is_absolute())throw std::runtime_error("absolute input/output and fixed arm required");
 const auto arm=integrator_panel::arm(arm_id);const int steps=arm.steps;
#if HIGHER_ORDER_CANDIDATE
 if(arm_id!='C')throw std::runtime_error("candidate binary accepts arm C only");
#else
 if(arm_id!='A')throw std::runtime_error("baseline binary accepts arm A only");
#endif
 if constexpr(std::endian::native!=std::endian::little)throw std::runtime_error("little-endian required");
 if(sizeof(double)!=8||!std::numeric_limits<double>::is_iec559)throw std::runtime_error("IEEE binary64 required");
 __builtin_cpu_init();if(!__builtin_cpu_supports("avx512f")||!__builtin_cpu_supports("avx512dq")||!__builtin_cpu_supports("avx512vl"))throw std::runtime_error("AVX512 unavailable");
 floating_environment();
 if(!std::filesystem::create_directory(output))throw std::runtime_error("output directory must be new");
 double begin=omp_get_wtime();std::ofstream lifecycle(std::filesystem::path(output)/"lifecycle.jsonl");
 if(!lifecycle)throw std::runtime_error("lifecycle open failed");
 lifecycle<<std::setprecision(17)<<"{\"phase\":\"model_preparation_started\",\"elapsed_seconds\":0}\n";lifecycle.flush();
 vm::Prepared prepared=vm::prepare(input,GRID_L,GRID_G,steps);
 lifecycle<<"{\"phase\":\"model_preparation_completed\",\"elapsed_seconds\":"<<omp_get_wtime()-begin<<"}\n";lifecycle.flush();
 Basis b(GRID_L,prepared),g(GRID_G,prepared);
 if(b.d!=6435||g.d!=19448||b.start[4]!=THERMAL)throw std::runtime_error("fixed basis mismatch");
 std::array<std::array<PrefixCheckpoint,CASES>,GRID_WINDOWS>checkpoints{};
 for(int c=0;c<CASES;++c){
  std::vector<int>occupied;
  for(int seg=0;seg<80;++seg){int cycle=seg/16;if((LABELS[c%3][0]+cycle)%5==0||(LABELS[c%3][1]+cycle)%5==0)occupied.push_back(seg);}
  int count=int(occupied.size());if(count!=(c%3==0?32:16)||prepared.cells[c].size()!=size_t(count*steps))throw std::runtime_error("occupied segment mismatch");
  int seg=occupied.front();if(seg!=(c%3==2?64:16))throw std::runtime_error("first occupied segment mismatch");
  for(int checkpoint=0;checkpoint<GRID_WINDOWS;++checkpoint){
   int cells=steps/128,q=checkpoint*cells,cumulative=(checkpoint+1)*cells;
   checkpoints[checkpoint][c]={seg,q,cells,cumulative};
   if(cumulative>steps)throw std::runtime_error("prefix crosses original segment");
   for(int local=0;local<cells;++local){const auto&cell=prepared.cells[c][q+local];
    for(int ion=0;ion<2;++ion)if(cell.stage[0].active[ion]!=int((LABELS[c%3][ion]+seg/16)%5==0))throw std::runtime_error("prefix active-ion mismatch");
   }
  }
 }
 Fixtures fixture=fixtures(prepared);
 lifecycle<<"{\"phase\":\"fixtures_completed\",\"elapsed_seconds\":"<<omp_get_wtime()-begin<<"}\n";lifecycle.flush();
 if(!lifecycle)throw std::runtime_error("lifecycle write failed");
 double preparation_seconds=omp_get_wtime()-begin;
 std::vector<V>states(GRID_SNAPSHOTS);std::vector<Certificate>certs(GRID_SNAPSHOTS);
 std::array<int,80>cpus{},places{};cpus.fill(-1);places.fill(-1);
 std::atomic<int>done{0},snapshots{0},initializations{0},transitions{0},polynomial_checks{0},monotonicity_checks{0},migrations{0};
 std::atomic<bool>failed{false};std::mutex lock;std::string failure;int workers=0;
 std::ofstream progress(std::filesystem::path(output)/"progress.jsonl");if(!progress)throw std::runtime_error("progress open failed");progress<<std::setprecision(17);
 omp_set_dynamic(0);omp_set_num_threads(80);
 if(omp_get_proc_bind()==omp_proc_bind_false)throw std::runtime_error("OpenMP binding required");
 double scan_begin=omp_get_wtime();
 #pragma omp parallel
 {
  int tid=omp_get_thread_num();std::unique_ptr<Work>w;std::unique_ptr<BWork>bw;
#if HIGHER_ORDER_CANDIDATE
  std::unique_ptr<HigherWork>high;
#endif
  #pragma omp single
  workers=omp_get_num_threads();
  try{
   if(tid<0||tid>=80)throw std::runtime_error("thread index outside fixed domain");
   cpus[tid]=sched_getcpu();places[tid]=omp_get_place_num();floating_environment();
   w=std::make_unique<Work>(b.d);bw=std::make_unique<BWork>(g.d,b.d);
#if HIGHER_ORDER_CANDIDATE
   high=std::make_unique<HigherWork>(b.d);
#endif
  }catch(const std::exception&e){std::lock_guard<std::mutex>guard(lock);failed=true;if(failure.empty())failure=e.what();}
  #pragma omp barrier
  #pragma omp for schedule(dynamic,1)
  for(int task=0;task<GRID_TASKS;++task){if(failed.load())continue;
   try{
    int c=TASK_CASE_ORDER[task/BATCHES],batch=task%BATCHES;V y(2*b.d*B);Certificate current{};
    // Exactly one thermal seed and zero certificate per complete short prefix.
    for(int lane=0;lane<B;++lane)put(y,b.d,batch*B+lane,lane,1);
    ++initializations;
    for(int checkpoint=0;checkpoint<GRID_WINDOWS;++checkpoint){
     const auto&selection=checkpoints[checkpoint][c];int snapshot=(checkpoint*CASES+c)*BATCHES+batch;
     if(checkpoint){int previous=snapshot-GRID_TASKS;
      if(!same_state(y,states[previous])||!same_certificate(current,certs[previous]))throw std::runtime_error("checkpoint carry changed");
      ++transitions;
     }
     for(int local=0;local<selection.block_cells;++local){const auto&cell=prepared.cells[c][selection.first_cell+local];
      V incoming=y;Certificate before=current;
#if HIGHER_ORDER_CANDIDATE
      higher_order_step(b,y,cell,*w,*high);
#else
      hermite_step(b,y,cell,*w);
#endif
      if(!same_state(incoming,w->poly[0]))throw std::runtime_error("polynomial start differs from incoming dyadic state");
      ++polynomial_checks;
      certify(prepared,b,g,cell,y,*w,*bw,current);check_monotone(before,current);++monotonicity_checks;
     }
     states[snapshot]=y;certs[snapshot]=current;int count=++snapshots;std::lock_guard<std::mutex>guard(lock);
     progress<<"{\"completed_snapshots\":"<<count<<",\"checkpoint\":"<<checkpoint<<",\"case\":"<<c<<",\"batch\":"<<batch<<",\"block_cells\":"<<selection.block_cells<<",\"cumulative_cells\":"<<selection.cumulative_cells<<",\"elapsed_seconds\":"<<omp_get_wtime()-scan_begin<<"}\n";progress.flush();
     if(!progress)throw std::runtime_error("progress write failed");
    }
    ++done;
   }catch(const std::exception&e){std::lock_guard<std::mutex>guard(lock);failed=true;if(failure.empty())failure=e.what();}
  }
  if(tid>=0&&tid<80&&cpus[tid]!=sched_getcpu())++migrations;
 }
 double kernel_seconds=omp_get_wtime()-scan_begin;progress.close();
 if(failed||done!=GRID_TASKS||snapshots!=GRID_SNAPSHOTS||initializations!=90||transitions!=270||polynomial_checks!=GRID_SNAPSHOTS*(steps/128)||monotonicity_checks!=polynomial_checks)throw std::runtime_error("partial continuous-prefix experiment: "+failure);
 if(workers!=80||migrations)throw std::runtime_error("worker count or migration");
 std::array<bool,80>seen{};
 for(int t=0;t<80;++t){if(cpus[t]<0||cpus[t]>=80||places[t]<0||places[t]>=80||seen[cpus[t]])throw std::runtime_error("invalid CPU placement");seen[cpus[t]]=true;}
 seen.fill(false);for(int t=0;t<80;++t){if(seen[places[t]])throw std::runtime_error("duplicate OpenMP place");seen[places[t]]=true;}
 lifecycle<<"{\"phase\":\"continuous_prefix_scan_completed\",\"elapsed_seconds\":"<<omp_get_wtime()-begin<<"}\n";lifecycle.flush();
 if(!lifecycle)throw std::runtime_error("lifecycle write failed");
 std::ofstream basisfile(std::filesystem::path(output)/"basis.json");
 basisfile<<"{\"scope\":\"SHORT_CONTINUOUS_PREFIX_ONLY\",\"cutoff\":8,\"guard\":10,\"thermal_cutoff\":3,\"occupations\":[";
 for(int row=0;row<b.d;++row){if(row)basisfile<<',';basisfile<<'[';for(int m=0;m<M;++m){if(m)basisfile<<',';basisfile<<b.n[row][m];}basisfile<<']';}basisfile<<"]}\n";basisfile.close();if(!basisfile)throw std::runtime_error("basis write failed");
 std::ofstream layout(std::filesystem::path(output)/"layout.txt",std::ios::binary);layout<<integrator_panel::layout(arm);layout.close();if(!layout)throw std::runtime_error("layout write failed");
 std::ofstream endpoints(std::filesystem::path(output)/"endpoints.bin",std::ios::binary),components(std::filesystem::path(output)/"components.bin",std::ios::binary);
 if(!endpoints||!components)throw std::runtime_error("binary output open failed");
 std::vector<std::array<I,B>>norms(GRID_SNAPSHOTS);
 for(int task=0;task<GRID_SNAPSHOTS;++task)norms[task]=center_norm2(states[task],b.d);
 for(int window=0;window<GRID_WINDOWS;++window)for(int c=0;c<CASES;++c)for(int column=0;column<THERMAL;++column){
  int task=(window*CASES+c)*BATCHES+column/B,lane=column%B;
  for(int row=0;row<b.d;++row){C value=get(states[task],b.d,row,lane);double pair[2]={value.real(),value.imag()};if(!std::isfinite(pair[0])||!std::isfinite(pair[1]))throw std::runtime_error("nonfinite local endpoint");grid_write(endpoints,pair,2);}
  auto values=grid_components(certs[task],lane,norms[task][lane]);grid_write(components,values.data(),values.size());
 }
 endpoints.close();components.close();if(!endpoints||!components)throw std::runtime_error("binary output close failed");
 auto endpoint_bytes=std::filesystem::file_size(std::filesystem::path(output)/"endpoints.bin"),component_bytes=std::filesystem::file_size(std::filesystem::path(output)/"components.bin");
 const uintmax_t expected_endpoint_bytes=uintmax_t(GRID_WINDOWS)*CASES*THERMAL*b.d*2*sizeof(double),expected_component_bytes=uintmax_t(GRID_WINDOWS)*CASES*THERMAL*GRID_FIELDS*sizeof(double);
 if(endpoint_bytes!=expected_endpoint_bytes||component_bytes!=expected_component_bytes)throw std::runtime_error("binary size mismatch");
 // One immutable contract body is shared by metadata and stdout.
 std::ostringstream immutable;immutable<<std::setprecision(17);
 immutable<<"{\"scope\":\"SHORT_CONTINUOUS_PREFIX_ONLY\",\"initial_state_in_moving_frame\":true,\"reset_between_checkpoints\":false,\"full_analytic_linear_history_retained\":true,\"full_trajectory_certificate\":false,\"final_coherences_computed\":false,\"cutoff\":8,\"guard\":10,\"steps_per_segment\":"<<steps
  <<",\"arm\":\""<<arm.id<<"\",\"integrator\":\""<<arm.integrator<<"\",\"dense_curve\":\""<<arm.dense<<"\",\"substeps_per_cell\":"<<arm.substeps<<",\"rhs_per_cell\":"<<arm.rhs
  <<",\"actual_substeps_per_checkpoint_block\":"<<(steps/128)*arm.substeps<<",\"actual_substeps_per_trajectory\":"<<4*(steps/128)*arm.substeps
  <<",\"checkpoints\":4,\"tasks\":90,\"snapshot_records\":360,\"trajectory_initializations\":"<<initializations<<",\"checkpoint_transitions\":"<<transitions<<",\"state_and_certificate_carry_checks\":"<<transitions
  <<",\"polynomial_start_checks\":"<<polynomial_checks<<",\"certificate_monotonicity_checks\":"<<monotonicity_checks<<",\"polynomial_start_matches_incoming\":true,\"cumulative_components_nondecreasing\":true"
  <<",\"cells_per_checkpoint_block\":"<<steps/128<<",\"cells_per_trajectory\":"<<4*(steps/128)<<",\"total_certified_cells\":"<<GRID_SNAPSHOTS*(steps/128)
  <<",\"cases\":6,\"thermal_columns\":120,\"thermal_cutoff\":3,\"dimension\":6435,\"guard_dimension\":19448,\"endpoint_bytes\":"<<endpoint_bytes<<",\"component_bytes\":"<<component_bytes
  <<",\"task_case_order\":[1,2,4,5,0,3],\"component_fields\":[";
 for(int k=0;k<GRID_FIELDS;++k){if(k)immutable<<',';immutable<<'"'<<GRID_FIELD_NAMES[k]<<'"';}
 immutable<<"],\"checkpoint_selection\":[";
 for(int checkpoint=0;checkpoint<GRID_WINDOWS;++checkpoint)for(int c=0;c<CASES;++c){
  if(checkpoint||c)immutable<<',';
  const auto&s=checkpoints[checkpoint][c];
  immutable<<"{\"checkpoint\":"<<checkpoint<<",\"case\":"<<c<<",\"labels\":["<<LABELS[c%3][0]<<','<<LABELS[c%3][1]
   <<"],\"first_occupied_absolute_segment\":"<<s.absolute_segment<<",\"first_occupied_cell\":0,\"block_first_occupied_cell\":"<<s.first_cell<<",\"block_cells\":"<<s.block_cells<<",\"cumulative_cells\":"<<s.cumulative_cells
   <<",\"start_original_segment_units\":["<<s.absolute_segment<<",1],\"endpoint_original_segment_units\":["<<s.absolute_segment*steps+s.cumulative_cells<<','<<steps
   <<"],\"elapsed_from_first_force_units\":["<<checkpoint+1<<",128],\"available_full_trajectory_cells\":"<<prepared.cells[c].size()<<'}';
 }
 immutable<<"],\"thermal_weights\":[";
 for(int col=0;col<THERMAL;++col){if(col)immutable<<',';immutable<<'['<<prepared.thermal[col].lo<<','<<prepared.thermal[col].hi<<']';}
 immutable<<']';
 const std::string contract=immutable.str();
 std::ofstream metadata(std::filesystem::path(output)/"metadata.json");metadata<<contract<<"}\n";metadata.close();if(!metadata)throw std::runtime_error("metadata write failed");
 std::ostringstream summary;summary<<std::setprecision(17)<<contract
  <<",\"status\":\"COMPLETED\",\"simd_lanes\":8,\"threads\":80,\"preparation_seconds\":"<<preparation_seconds<<",\"model_preparation_seconds\":"<<prepared.preparation_seconds<<",\"kernel_seconds\":"<<kernel_seconds
  <<",\"mpfr_version\":\""<<prepared.mpfr_version<<"\",\"migrations\":"<<migrations
  <<",\"binary_layout\":\"little-endian IEEE64; endpoints: checkpoint,case,column,basis,re/im; components: checkpoint,case,column,component_fields\""
  <<",\"fixtures\":{\"dense_displacement_error\":"<<fixture.dense_error<<",\"collective_displacement_error\":"<<fixture.collective_error
  <<",\"directed_arithmetic\":true,\"zero_displacement_enclosure\":true,\"adjoint_enclosure\":true,\"ball_interval_fixture_enclosure\":true,\"ball_reference_radius_ratio\":"<<fixture.ball_reference_ratio<<"},\"thread_map\":[";
 for(int t=0;t<80;++t){if(t)summary<<',';summary<<"{\"thread\":"<<t<<",\"cpu\":"<<cpus[t]<<",\"place\":"<<places[t]<<'}';}
 summary<<"],\"end_to_end_seconds\":"<<omp_get_wtime()-begin<<"}\n";
 std::cout<<summary.str();return 0;
}catch(const std::exception&e){std::cerr<<e.what()<<'\n';return 2;}}
