// Copyright 2026 A. M. Thorn. SPDX-License-Identifier: Apache-2.0
// Four independent local reset windows. Never a full-trajectory campaign.
#ifndef BENCHMARK_KERNEL
#error "BENCHMARK_KERNEL must name the sealed optimized kernel.cpp"
#endif
#define main unused_full_campaign_main
#include BENCHMARK_KERNEL
#undef main
#include <memory>
#include <sstream>
#include "higher_order.hpp"

constexpr int GRID_L=8,GRID_G=10,GRID_WINDOWS=4,GRID_FIELDS=12;
constexpr int GRID_TASKS=GRID_WINDOWS*CASES*BATCHES;
const std::array<const char*,GRID_FIELDS> GRID_FIELD_NAMES={
 "guard","tail","continuum","jumps","total",
 "sampled_time_node_L2","sampled_projection_node_L2","sampled_arithmetic_node_L2",
 "maximum_node_bound","maximum_norm_error","endpoint_norm_squared_lo","endpoint_norm_squared_hi"
};
struct GridWindow {int occupied_segment,absolute_segment,q,first_cell,cells;};

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
  else if(key=="--arm"&&!arm_id){std::string value=argv[i+1];if(value.size()!=1)throw std::runtime_error("arm must be A, B or C");arm_id=value[0];}
  else throw std::runtime_error("unknown or duplicate CLI argument");
 }
 if(input.empty()||output.empty()||!arm_id||!std::filesystem::path(input).is_absolute()||!std::filesystem::path(output).is_absolute())throw std::runtime_error("absolute input/output and fixed arm required");
 const auto arm=integrator_panel::arm(arm_id);const int steps=arm.steps;
#if HIGHER_ORDER_CANDIDATE
 if(arm_id!='C')throw std::runtime_error("candidate binary accepts arm C only");
#else
 if(arm_id=='C')throw std::runtime_error("baseline binary accepts arms A/B only");
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
 std::array<std::array<GridWindow,CASES>,GRID_WINDOWS>windows{};
 const int q256[GRID_WINDOWS]={0,128,128,254};
 for(int c=0;c<CASES;++c){
  std::vector<int>occupied;
  for(int seg=0;seg<80;++seg){int cycle=seg/16;if((LABELS[c%3][0]+cycle)%5==0||(LABELS[c%3][1]+cycle)%5==0)occupied.push_back(seg);}
  int count=int(occupied.size());if(count!=(c%3==0?32:16)||prepared.cells[c].size()!=size_t(count*steps))throw std::runtime_error("occupied segment mismatch");
  int ordinal[GRID_WINDOWS]={0,(count-1)/3,2*(count-1)/3,count-1};
  for(int window=0;window<GRID_WINDOWS;++window){
   int q=q256[window]*(steps/256),cells=steps/128,seg=occupied[ordinal[window]];
   windows[window][c]={ordinal[window],seg,q,ordinal[window]*steps+q,cells};
   if(q+cells>steps)throw std::runtime_error("window crosses original segment");
   for(int local=0;local<cells;++local){const auto&cell=prepared.cells[c][windows[window][c].first_cell+local];
    for(int ion=0;ion<2;++ion)if(cell.stage[0].active[ion]!=int((LABELS[c%3][ion]+seg/16)%5==0))throw std::runtime_error("window active-ion mismatch");
   }
  }
 }
 Fixtures fixture=fixtures(prepared);
 lifecycle<<"{\"phase\":\"fixtures_completed\",\"elapsed_seconds\":"<<omp_get_wtime()-begin<<"}\n";lifecycle.flush();
 if(!lifecycle)throw std::runtime_error("lifecycle write failed");
 double preparation_seconds=omp_get_wtime()-begin;
 std::vector<V>states(GRID_TASKS);std::vector<Certificate>certs(GRID_TASKS);
 std::array<int,80>cpus{},places{};cpus.fill(-1);places.fill(-1);
 std::atomic<int>done{0},migrations{0};std::atomic<bool>failed{false};std::mutex lock;std::string failure;int workers=0;
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
    int window=task/(CASES*BATCHES),c=(task/BATCHES)%CASES,batch=task%BATCHES;
    const GridWindow&selection=windows[window][c];V y(2*b.d*B);
    // A fresh unit vector in the moving frame, not the actual nonlinear
    // mid-trajectory state. Every local certificate starts from zero.
    for(int lane=0;lane<B;++lane)put(y,b.d,batch*B+lane,lane,1);
    // This is the only reachable dynamics loop: exactly 2 or 4 local cells.
    for(int local=0;local<selection.cells;++local){const auto&cell=prepared.cells[c][selection.first_cell+local];
#if HIGHER_ORDER_CANDIDATE
     higher_order_step(b,y,cell,*w,*high);
#else
     hermite_step(b,y,cell,*w);
#endif
     certify(prepared,b,g,cell,y,*w,*bw,certs[task]);
    }
    states[task]=std::move(y);int count=++done;std::lock_guard<std::mutex>guard(lock);
    progress<<"{\"completed\":"<<count<<",\"window\":"<<window<<",\"case\":"<<c<<",\"batch\":"<<batch<<",\"cells\":"<<selection.cells<<",\"elapsed_seconds\":"<<omp_get_wtime()-scan_begin<<"}\n";progress.flush();
    if(!progress)throw std::runtime_error("progress write failed");
   }catch(const std::exception&e){std::lock_guard<std::mutex>guard(lock);failed=true;if(failure.empty())failure=e.what();}
  }
  if(tid>=0&&tid<80&&cpus[tid]!=sched_getcpu())++migrations;
 }
 double kernel_seconds=omp_get_wtime()-scan_begin;progress.close();
 if(failed||done!=GRID_TASKS)throw std::runtime_error("partial local-window experiment: "+failure);
 if(workers!=80||migrations)throw std::runtime_error("worker count or migration");
 std::array<bool,80>seen{};
 for(int t=0;t<80;++t){if(cpus[t]<0||cpus[t]>=80||places[t]<0||places[t]>=80||seen[cpus[t]])throw std::runtime_error("invalid CPU placement");seen[cpus[t]]=true;}
 seen.fill(false);for(int t=0;t<80;++t){if(seen[places[t]])throw std::runtime_error("duplicate OpenMP place");seen[places[t]]=true;}
 lifecycle<<"{\"phase\":\"local_window_scan_completed\",\"elapsed_seconds\":"<<omp_get_wtime()-begin<<"}\n";lifecycle.flush();
 if(!lifecycle)throw std::runtime_error("lifecycle write failed");
 std::ofstream basisfile(std::filesystem::path(output)/"basis.json");
 basisfile<<"{\"scope\":\"LOCAL_WINDOW_INTEGRATOR_COMPARISON_ONLY\",\"cutoff\":8,\"guard\":10,\"thermal_cutoff\":3,\"occupations\":[";
 for(int row=0;row<b.d;++row){if(row)basisfile<<',';basisfile<<'[';for(int m=0;m<M;++m){if(m)basisfile<<',';basisfile<<b.n[row][m];}basisfile<<']';}basisfile<<"]}\n";basisfile.close();if(!basisfile)throw std::runtime_error("basis write failed");
 std::ofstream layout(std::filesystem::path(output)/"layout.txt",std::ios::binary);layout<<integrator_panel::layout(arm);layout.close();if(!layout)throw std::runtime_error("layout write failed");
 std::ofstream endpoints(std::filesystem::path(output)/"endpoints.bin",std::ios::binary),components(std::filesystem::path(output)/"components.bin",std::ios::binary);
 if(!endpoints||!components)throw std::runtime_error("binary output open failed");
 std::vector<std::array<I,B>>norms(GRID_TASKS);
 for(int task=0;task<GRID_TASKS;++task)norms[task]=center_norm2(states[task],b.d);
 for(int window=0;window<GRID_WINDOWS;++window)for(int c=0;c<CASES;++c)for(int column=0;column<THERMAL;++column){
  int task=(window*CASES+c)*BATCHES+column/B,lane=column%B;
  for(int row=0;row<b.d;++row){C value=get(states[task],b.d,row,lane);double pair[2]={value.real(),value.imag()};if(!std::isfinite(pair[0])||!std::isfinite(pair[1]))throw std::runtime_error("nonfinite local endpoint");grid_write(endpoints,pair,2);}
  auto values=grid_components(certs[task],lane,norms[task][lane]);grid_write(components,values.data(),values.size());
 }
 endpoints.close();components.close();if(!endpoints||!components)throw std::runtime_error("binary output close failed");
 auto endpoint_bytes=std::filesystem::file_size(std::filesystem::path(output)/"endpoints.bin"),component_bytes=std::filesystem::file_size(std::filesystem::path(output)/"components.bin");
 const uintmax_t expected_endpoint_bytes=uintmax_t(GRID_WINDOWS)*CASES*THERMAL*b.d*2*sizeof(double),expected_component_bytes=uintmax_t(GRID_WINDOWS)*CASES*THERMAL*GRID_FIELDS*sizeof(double);
 if(endpoint_bytes!=expected_endpoint_bytes||component_bytes!=expected_component_bytes)throw std::runtime_error("binary size mismatch");
 std::ostringstream summary;summary<<std::setprecision(17);
 summary<<"{\"status\":\"COMPLETED\",\"scope\":\"LOCAL_WINDOW_INTEGRATOR_COMPARISON_ONLY\",\"reset_state_in_moving_frame\":true,\"full_analytic_linear_history_retained\":true,\"full_trajectory_certificate\":false,\"final_coherences_computed\":false,\"cutoff\":8,\"guard\":10,\"steps_per_segment\":"<<steps<<",\"arm\":\""<<arm.id<<"\",\"integrator\":\""<<arm.integrator<<"\",\"dense_curve\":\""<<arm.dense<<"\",\"substeps_per_cell\":"<<arm.substeps<<",\"rhs_per_cell\":"<<arm.rhs<<",\"actual_substeps_per_window\":"<<(steps/128)*arm.substeps<<",\"windows\":4,\"local_cells_per_task\":"<<steps/128<<",\"tasks\":360,\"total_certified_cells\":"<<GRID_TASKS*(steps/128)<<",\"cases\":6,\"thermal_columns\":120,\"thermal_cutoff\":3,\"simd_lanes\":8,\"threads\":80,\"dimension\":"<<b.d<<",\"guard_dimension\":"<<g.d<<",\"preparation_seconds\":"<<preparation_seconds<<",\"model_preparation_seconds\":"<<prepared.preparation_seconds<<",\"kernel_seconds\":"<<kernel_seconds<<",\"mpfr_version\":\""<<prepared.mpfr_version<<"\",\"migrations\":"<<migrations<<",\"endpoint_bytes\":"<<endpoint_bytes<<",\"component_bytes\":"<<component_bytes<<",\"binary_layout\":\"little-endian IEEE64; endpoints: window,case,column,basis,re/im; components: window,case,column,component_fields\",\"fixtures\":{\"dense_displacement_error\":"<<fixture.dense_error<<",\"collective_displacement_error\":"<<fixture.collective_error<<",\"directed_arithmetic\":true,\"zero_displacement_enclosure\":true,\"adjoint_enclosure\":true,\"ball_interval_fixture_enclosure\":true,\"ball_reference_radius_ratio\":"<<fixture.ball_reference_ratio<<"},\"component_fields\":[";
 for(int k=0;k<GRID_FIELDS;++k){if(k)summary<<',';summary<<'"'<<GRID_FIELD_NAMES[k]<<'"';}
 summary<<"],\"window_selection\":[";
 for(int window=0;window<GRID_WINDOWS;++window)for(int c=0;c<CASES;++c){if(window||c)summary<<',';const auto&s=windows[window][c];
  summary<<"{\"window\":"<<window<<",\"case\":"<<c<<",\"labels\":["<<LABELS[c%3][0]<<','<<LABELS[c%3][1]<<"],\"occupied_segment_ordinal\":"<<s.occupied_segment<<",\"absolute_segment\":"<<s.absolute_segment<<",\"start_subcell\":"<<s.q<<",\"first_occupied_cell\":"<<s.first_cell<<",\"cells\":"<<s.cells<<",\"start_original_segment_units\":["<<s.absolute_segment*steps+s.q<<','<<steps<<"],\"duration_original_segment_units\":[1,128],\"available_full_trajectory_cells\":"<<prepared.cells[c].size()<<'}';
 }
 summary<<"],\"thermal_weights\":[";for(int col=0;col<THERMAL;++col){if(col)summary<<',';summary<<'['<<prepared.thermal[col].lo<<','<<prepared.thermal[col].hi<<']';}
 summary<<"],\"thread_map\":[";for(int t=0;t<80;++t){if(t)summary<<',';summary<<"{\"thread\":"<<t<<",\"cpu\":"<<cpus[t]<<",\"place\":"<<places[t]<<'}';}
 summary<<']';
 // This file contains only immutable fields, so same-arm repeats can be
 // compared byte for byte. Timings, fixtures and worker maps stay on stdout.
 std::ostringstream immutable;immutable<<std::setprecision(17);
 immutable<<"{\"scope\":\"LOCAL_WINDOW_INTEGRATOR_COMPARISON_ONLY\",\"reset_state_in_moving_frame\":true,\"full_analytic_linear_history_retained\":true,\"full_trajectory_certificate\":false,\"final_coherences_computed\":false,\"cutoff\":8,\"guard\":10,\"steps_per_segment\":"<<steps<<",\"arm\":\""<<arm.id<<"\",\"integrator\":\""<<arm.integrator<<"\",\"dense_curve\":\""<<arm.dense<<"\",\"substeps_per_cell\":"<<arm.substeps<<",\"rhs_per_cell\":"<<arm.rhs<<",\"actual_substeps_per_window\":"<<(steps/128)*arm.substeps<<",\"windows\":4,\"cases\":6,\"thermal_columns\":120,\"thermal_cutoff\":3,\"dimension\":6435,\"guard_dimension\":19448,\"local_cells_per_task\":"<<steps/128<<",\"endpoint_bytes\":"<<endpoint_bytes<<",\"component_bytes\":"<<component_bytes<<",\"component_fields\":[";
 for(int k=0;k<GRID_FIELDS;++k){if(k)immutable<<',';immutable<<'"'<<GRID_FIELD_NAMES[k]<<'"';}
 immutable<<"],\"window_selection\":[";
 for(int window=0;window<GRID_WINDOWS;++window)for(int c=0;c<CASES;++c){if(window||c)immutable<<',';const auto&s=windows[window][c];
  immutable<<"{\"window\":"<<window<<",\"case\":"<<c<<",\"labels\":["<<LABELS[c%3][0]<<','<<LABELS[c%3][1]<<"],\"occupied_segment_ordinal\":"<<s.occupied_segment<<",\"absolute_segment\":"<<s.absolute_segment<<",\"start_subcell\":"<<s.q<<",\"first_occupied_cell\":"<<s.first_cell<<",\"cells\":"<<s.cells<<",\"start_original_segment_units\":["<<s.absolute_segment*steps+s.q<<','<<steps<<"],\"duration_original_segment_units\":[1,128],\"available_full_trajectory_cells\":"<<prepared.cells[c].size()<<'}';
 }
 immutable<<"],\"thermal_weights\":[";for(int col=0;col<THERMAL;++col){if(col)immutable<<',';immutable<<'['<<prepared.thermal[col].lo<<','<<prepared.thermal[col].hi<<']';}immutable<<"]}\n";
 std::ofstream metadata(std::filesystem::path(output)/"metadata.json");metadata<<immutable.str();metadata.close();if(!metadata)throw std::runtime_error("metadata write failed");
 summary<<",\"end_to_end_seconds\":"<<omp_get_wtime()-begin<<"}\n";
 std::cout<<summary.str();return 0;
}catch(const std::exception&e){std::cerr<<e.what()<<'\n';return 2;}}
