// Copyright 2026 A. M. Thorn. SPDX-License-Identifier: Apache-2.0
// One fixed full-word campaign. No resume, retry, grid or cutoff selection.
#if !defined(HIGHER_ORDER_CANDIDATE) || HIGHER_ORDER_CANDIDATE != 1
#error "This harness requires HIGHER_ORDER_CANDIDATE=1"
#endif
#define main unused_inherited_campaign_main
#include "kernel.cpp"
#undef main
#include <memory>
#include <sstream>
#include <cstring>
#include "higher_order.hpp"

constexpr int FULL_L=8,FULL_G=10,FULL_STEPS=384,FULL_SEGMENTS=80,FULL_FIELDS=12;
constexpr int FULL_TASKS=CASES*BATCHES,FULL_SNAPSHOTS=FULL_TASKS*(FULL_SEGMENTS+1);
constexpr long FULL_CELLS=737280;
constexpr std::array<int,CASES> TASK_CASE_ORDER={1,2,4,5,0,3};
constexpr const char* FULL_SCOPE="FULL_WORD_SIX_CASES_K3_CONDITIONAL";
const std::array<const char*,FULL_FIELDS> FIELD_NAMES={
 "guard","tail","continuum","jumps","total",
 "sampled_time_node_L2","sampled_projection_node_L2","sampled_arithmetic_node_L2",
 "maximum_node_bound","maximum_norm_error","endpoint_norm_squared_lo","endpoint_norm_squared_hi"
};
bool same_state(const V&a,const V&b){return a.size()==b.size()&&std::memcmp(a.data(),b.data(),a.size()*sizeof(double))==0;}
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
std::array<double,FULL_FIELDS> components(const Certificate&c,int lane,I norm){
 std::array<double,FULL_FIELDS> values={c.guard[lane],c.tail[lane],c.tube[lane],c.jumps[lane],c.total[lane],
  c.sampled_time_node_L2[lane],c.sampled_projection_node_L2[lane],c.sampled_arithmetic_node_L2[lane],
  c.max_node[lane],c.max_norm_error[lane],norm.lo,norm.hi};
 for(double value:values)if(!std::isfinite(value)||value<0)throw std::runtime_error("invalid saved component");
 if(norm.lo>norm.hi)throw std::runtime_error("inverted endpoint norm");
 return values;
}
void write_doubles(std::ofstream&out,const double*values,size_t count){
 out.write(reinterpret_cast<const char*>(values),std::streamsize(count*sizeof(double)));
 if(!out)throw std::runtime_error("binary write failed");
}
void fields_json(std::ostream&out){
 out<<'[';for(int k=0;k<FULL_FIELDS;++k){if(k)out<<',';out<<'"'<<FIELD_NAMES[k]<<'"';}out<<']';
}
void emit(std::ostream&out,I a){check(a);out<<'['<<a.lo<<','<<a.hi<<']';}
void emit(std::ostream&out,Z a){out<<'[';emit(out,a.re);out<<',';emit(out,a.im);out<<']';}
void atomic_text(const std::filesystem::path&path,const std::string&text){
 auto temporary=path;temporary+=".tmp";
 if(std::filesystem::exists(path)||std::filesystem::exists(temporary))throw std::runtime_error("immutable record already exists");
 std::ofstream out(temporary,std::ios::binary);out<<text;out.close();
 if(!out)throw std::runtime_error("record write failed");
 std::filesystem::rename(temporary,path);
}
std::string full_layout(){
 return "FULL_WORD_SEGMENT_CHECKPOINTS_V1\nsteps=384\nintegrator=DP5_TWO_HALF_STEPS\n"
  "dense_curve=QUINTIC_THREE_POINT_HERMITE\nsubsteps_per_cell=2\nrhs_per_cell=13\n"
  "segment_boundaries=81\ncases=6\ncolumns=120\nbatch_columns=8\ndimension=6435\ncomponents=12\n"
  "checkpoint_payload=lane,basis,re_im;then_lane,field\ncheckpoint_endpoint_bytes=823680\n"
  "checkpoint_component_bytes=768\ncheckpoint_bytes=824448\n"
  "final_endpoints=case,column,basis,re_im\nfinal_components=case,column,field\n"
  "encoding=little_endian_IEEE_binary64\ncommit=checkpoint-N.json_after_payload_rename\n";
}
std::filesystem::path task_directory(const std::filesystem::path&output,int c,int batch){
 return output/"checkpoints"/("case-"+std::to_string(c))/("batch-"+std::to_string(batch));
}
// The marker is committed only after the complete binary payload is closed and
// renamed. A .tmp or markerless .bin is preserved but is not a checkpoint.
void save_checkpoint(const std::filesystem::path&output,const Basis&b,const V&y,const Certificate&cert,
                     int c,int batch,int boundary,int cells,int active_segments,int cpu,int place){
 auto directory=task_directory(output,c,batch);auto stem="checkpoint-"+std::to_string(boundary);
 auto payload=directory/(stem+".bin"),temporary=directory/(stem+".bin.tmp"),marker=directory/(stem+".json");
 if(std::filesystem::exists(payload)||std::filesystem::exists(temporary)||std::filesystem::exists(marker))throw std::runtime_error("checkpoint already exists");
 std::ofstream out(temporary,std::ios::binary);if(!out)throw std::runtime_error("checkpoint open failed");
 for(int lane=0;lane<B;++lane)for(int row=0;row<b.d;++row){C value=get(y,b.d,row,lane);double z[2]={value.real(),value.imag()};
  if(!std::isfinite(z[0])||!std::isfinite(z[1]))throw std::runtime_error("nonfinite checkpoint endpoint");
  write_doubles(out,z,2);
 }
 auto norms=center_norm2(y,b.d);
 for(int lane=0;lane<B;++lane){auto values=components(cert,lane,norms[lane]);write_doubles(out,values.data(),values.size());}
 out.close();if(!out)throw std::runtime_error("checkpoint close failed");
 if(std::filesystem::file_size(temporary)!=824448)throw std::runtime_error("checkpoint size mismatch");
 std::filesystem::rename(temporary,payload);
 std::ostringstream record;record<<std::setprecision(17)
  <<"{\"schema\":\"FULL_SEGMENT_CHECKPOINT_V1\",\"scope\":\""<<FULL_SCOPE<<"\",\"case\":"<<c<<",\"batch\":"<<batch
  <<",\"segment_boundary\":"<<boundary<<",\"physical_time_seconds_rational\":["<<boundary<<",160000],\"thermal_column_start\":"<<batch*B
  <<",\"thermal_columns\":8,\"dimension\":6435,\"cumulative_cells\":"<<cells<<",\"active_segments_completed\":"<<active_segments
  <<",\"payload\":\""<<stem<<".bin\",\"payload_bytes\":824448,\"endpoint_bytes\":823680,\"component_bytes\":768,\"component_offset\":823680"
  <<",\"cpu\":"<<cpu<<",\"place\":"<<place<<",\"component_fields\":";fields_json(record);record<<"}\n";
 atomic_text(marker,record.str());
}
AVX void worker_arithmetic_fixture(){
 alignas(64) double lo[8],hi[8];
 _mm512_store_pd(lo,_mm512_add_round_pd(_mm512_set1_pd(1),_mm512_set1_pd(0x1p-53),RD));
 _mm512_store_pd(hi,_mm512_add_round_pd(_mm512_set1_pd(1),_mm512_set1_pd(0x1p-53),RU));
 for(int lane=0;lane<B;++lane)if(lo[lane]!=1||hi[lane]!=0x1.0000000000001p0)throw std::runtime_error("worker directed SIMD fixture");
 const double tiny=std::numeric_limits<double>::denorm_min();
 if(md(tiny,0.5)!=0||mu(tiny,0.5)!=tiny)throw std::runtime_error("worker subnormal fixture");
}
void bound_worker(int cpu,int place){
 cpu_set_t allowed;CPU_ZERO(&allowed);
 if(cpu<0||cpu>=80||place<0||place>=80||sched_getaffinity(0,sizeof(allowed),&allowed)!=0||CPU_COUNT(&allowed)!=1||!CPU_ISSET(cpu,&allowed))throw std::runtime_error("worker must have singleton CPU affinity");
 if(omp_get_place_num_procs(place)!=1)throw std::runtime_error("OpenMP place is not a singleton");
 int place_cpu=-1;omp_get_place_proc_ids(place,&place_cpu);if(place_cpu!=cpu)throw std::runtime_error("OpenMP place/CPU mismatch");
}
void check_coverage(int workers,const std::array<int,80>&cpus,const std::array<int,80>&places){
 if(workers!=80)throw std::runtime_error("exactly 80 workers required");
 std::array<bool,80>seen_cpu{},seen_place{};
 for(int t=0;t<80;++t){if(cpus[t]<0||cpus[t]>=80||places[t]<0||places[t]>=80||seen_cpu[cpus[t]]||seen_place[places[t]])throw std::runtime_error("worker coverage is not a bijection");seen_cpu[cpus[t]]=true;seen_place[places[t]]=true;}
}

int main(int argc,char**argv){try{
 std::string input,output;
 for(int i=1;i<argc;i+=2){if(i+1>=argc)throw std::runtime_error("missing CLI value");std::string key=argv[i];
  if(key=="--input"&&input.empty())input=argv[i+1];else if(key=="--output"&&output.empty())output=argv[i+1];else throw std::runtime_error("unknown or duplicate CLI argument");
 }
 if(input.empty()||output.empty()||!std::filesystem::path(input).is_absolute()||!std::filesystem::path(output).is_absolute())throw std::runtime_error("absolute input/output required");
 if constexpr(std::endian::native!=std::endian::little)throw std::runtime_error("little-endian required");
 if(sizeof(double)!=8||!std::numeric_limits<double>::is_iec559)throw std::runtime_error("IEEE binary64 required");
 __builtin_cpu_init();if(!__builtin_cpu_supports("avx512f")||!__builtin_cpu_supports("avx512dq")||!__builtin_cpu_supports("avx512vl"))throw std::runtime_error("AVX512 unavailable");
 floating_environment();if(omp_get_proc_bind()==omp_proc_bind_false)throw std::runtime_error("OpenMP binding required");
 if(!std::filesystem::create_directory(output))throw std::runtime_error("output directory must be new");
 const auto output_path=std::filesystem::path(output);double begin=omp_get_wtime();
 std::ofstream lifecycle(output_path/"lifecycle.jsonl");if(!lifecycle)throw std::runtime_error("lifecycle open failed");lifecycle<<std::setprecision(17);
 auto phase=[&](const char*name){lifecycle<<"{\"phase\":\""<<name<<"\",\"elapsed_seconds\":"<<omp_get_wtime()-begin<<"}\n";lifecycle.flush();if(!lifecycle)throw std::runtime_error("lifecycle write failed");};
 phase("model_preparation_started");vm::Prepared prepared=vm::prepare(input,FULL_L,FULL_G,FULL_STEPS);phase("model_preparation_completed");
 Basis b(FULL_L,prepared),g(FULL_G,prepared);if(b.d!=6435||g.d!=19448||b.start[4]!=THERMAL)throw std::runtime_error("fixed basis mismatch");
 std::array<std::array<int,FULL_SEGMENTS>,CASES>segment_offset{};
 for(int c=0;c<CASES;++c){int occupied=0;segment_offset[c].fill(-1);
  for(int seg=0;seg<FULL_SEGMENTS;++seg){int active[2]={int((LABELS[c%3][0]+seg/16)%5==0),int((LABELS[c%3][1]+seg/16)%5==0)};
   if(!(active[0]||active[1]))continue;
   segment_offset[c][seg]=occupied*FULL_STEPS;++occupied;
   for(int q=0;q<FULL_STEPS;++q){const auto&cell=prepared.cells[c].at(segment_offset[c][seg]+q);
    for(const auto&node:cell.stage)for(int ion=0;ion<2;++ion)if(node.active[ion]!=active[ion])throw std::runtime_error("stage segment profile mismatch");
    for(const auto&node:cell.gauss)for(int ion=0;ion<2;++ion)if(node.active[ion]!=active[ion])throw std::runtime_error("Gauss segment profile mismatch");
   }
  }
  if(occupied!=(c%3==0?32:16)||prepared.cells[c].size()!=size_t(occupied*FULL_STEPS))throw std::runtime_error("occupied segment inventory");
 }
 Fixtures fixture=fixtures(prepared);phase("fixtures_completed");
 std::ostringstream basis_record;basis_record<<"{\"scope\":\""<<FULL_SCOPE<<"\",\"cutoff\":8,\"guard\":10,\"thermal_cutoff\":3,\"occupations\":[";
 for(int row=0;row<b.d;++row){if(row)basis_record<<',';basis_record<<'[';for(int m=0;m<M;++m){if(m)basis_record<<',';basis_record<<b.n[row][m];}basis_record<<']';}basis_record<<"]}\n";
 atomic_text(output_path/"basis.json",basis_record.str());atomic_text(output_path/"layout.txt",full_layout());
 for(int c=0;c<CASES;++c)for(int batch=0;batch<BATCHES;++batch)if(!std::filesystem::create_directories(task_directory(output_path,c,batch)))throw std::runtime_error("checkpoint task directory exists");
 std::ostringstream metadata;metadata<<std::setprecision(17)<<"{\"scope\":\""<<FULL_SCOPE<<"\",\"cutoff\":8,\"guard\":10,\"steps_per_segment\":384,\"integrator\":\"DP5_TWO_HALF_STEPS\",\"dense_curve\":\"QUINTIC_THREE_POINT_HERMITE\",\"substeps_per_cell\":2,\"rhs_per_cell\":13,\"original_segments\":80,\"segment_seconds_rational\":[1,160000],\"final_time_seconds_rational\":[1,2000],\"cases\":6,\"thermal_columns\":120,\"thermal_cutoff\":3,\"dimension\":6435,\"guard_dimension\":19448,\"tasks\":90,\"required_snapshots\":7290,\"required_cells\":737280,\"required_active_task_segments\":1920,\"required_inactive_task_segments\":5280,\"initial_state_in_moving_frame\":true,\"reset_between_checkpoints\":false,\"fsal_between_cells\":false,\"normalization_applied\":false,\"phase_fit_applied\":false,\"task_case_order\":[1,2,4,5,0,3],\"component_fields\":";fields_json(metadata);
 metadata<<",\"case_active_cells\":[12288,6144,6144,12288,6144,6144],\"thermal_weights\":[";
 for(int n=0;n<THERMAL;++n){if(n)metadata<<',';emit(metadata,prepared.thermal[n]);}metadata<<"],\"thermal_tail\":";emit(metadata,prepared.thermal_tail);metadata<<"}\n";
 atomic_text(output_path/"metadata.json",metadata.str());
 double preparation_seconds=omp_get_wtime()-begin;
 std::vector<V>states(FULL_TASKS);std::vector<Certificate>certs(FULL_TASKS);
 std::array<int,80>cpus{},places{},worker_tasks{};cpus.fill(-1);places.fill(-1);
 std::atomic<long>done{0},snapshots{0},initializations{0},carry_checks{0},poly_checks{0},monotone_checks{0},inactive_checks{0},active_segments{0},migrations{0},worker_fixtures{0};
 std::atomic<bool>failed{false};std::mutex lock;std::string failure;int workers=0;
 std::ofstream progress(output_path/"progress.jsonl");if(!progress)throw std::runtime_error("progress open failed");progress<<std::setprecision(17);
 omp_set_dynamic(0);omp_set_num_threads(80);double scan_begin=omp_get_wtime();
 #pragma omp parallel
 {
  int tid=omp_get_thread_num();std::unique_ptr<Work>w;std::unique_ptr<BWork>bw;std::unique_ptr<HigherWork>high;
  #pragma omp single
  workers=omp_get_num_threads();
  try{
   if(tid<0||tid>=80)throw std::runtime_error("thread index outside fixed domain");
   cpus[tid]=sched_getcpu();places[tid]=omp_get_place_num();floating_environment();bound_worker(cpus[tid],places[tid]);worker_arithmetic_fixture();++worker_fixtures;
   w=std::make_unique<Work>(b.d);bw=std::make_unique<BWork>(g.d,b.d);high=std::make_unique<HigherWork>(b.d);
  }catch(const std::exception&e){std::lock_guard<std::mutex>guard(lock);failed=true;if(failure.empty())failure=e.what();}
  #pragma omp barrier
  #pragma omp single
  {
   try{check_coverage(workers,cpus,places);if(worker_fixtures!=80)throw std::runtime_error("worker fixture inventory");phase("worker_coverage_validated");}
   catch(const std::exception&e){std::lock_guard<std::mutex>guard(lock);failed=true;if(failure.empty())failure=e.what();}
  }
  #pragma omp for schedule(dynamic,1)
  for(int task=0;task<FULL_TASKS;++task){if(failed.load())continue;
   try{
    int c=TASK_CASE_ORDER[task/BATCHES],batch=task%BATCHES;V y(2*b.d*B);Certificate current{};
    for(int lane=0;lane<B;++lane)put(y,b.d,batch*B+lane,lane,1);
    ++initializations;++worker_tasks[tid];int cells=0,occupied=0;
    save_checkpoint(output_path,b,y,current,c,batch,0,0,0,cpus[tid],places[tid]);++snapshots;
    V saved=y;Certificate saved_certificate=current;
    for(int seg=0;seg<FULL_SEGMENTS&&!failed.load();++seg){
     if(!same_state(y,saved)||!same_certificate(current,saved_certificate))throw std::runtime_error("state/certificate segment carry mismatch");
     ++carry_checks;int offset=segment_offset[c][seg];
     if(offset>=0){
      for(int q=0;q<FULL_STEPS&&!failed.load();++q){const auto&cell=prepared.cells[c][offset+q];V incoming=y;Certificate before=current;
       higher_order_step(b,y,cell,*w,*high);
       if(!same_state(incoming,w->poly[0]))throw std::runtime_error("polynomial start differs from incoming dyadic state");
       ++poly_checks;certify(prepared,b,g,cell,y,*w,*bw,current);check_monotone(before,current);++monotone_checks;++cells;
       if(cells%32==0){
        if(sched_getcpu()!=cpus[tid]||omp_get_place_num()!=places[tid]){++migrations;throw std::runtime_error("worker migration");}
        std::lock_guard<std::mutex>guard(lock);progress<<"{\"kind\":\"cells\",\"case\":"<<c<<",\"batch\":"<<batch<<",\"original_segment\":"<<seg<<",\"cell_in_segment\":"<<q+1<<",\"cells\":"<<cells<<",\"total_cells\":"<<prepared.cells[c].size()<<",\"error_bound_max\":"<<*std::max_element(current.total.begin(),current.total.end())<<",\"elapsed_seconds\":"<<omp_get_wtime()-scan_begin<<"}\n";progress.flush();if(!progress)throw std::runtime_error("progress write failed");
       }
      }
      if(failed.load())break;
      ++occupied;++active_segments;
     }else{
      if(!same_state(y,saved)||!same_certificate(current,saved_certificate))throw std::runtime_error("inactive segment changed state or certificate");
      ++inactive_checks;
     }
     check_monotone(saved_certificate,current);
     if(sched_getcpu()!=cpus[tid]||omp_get_place_num()!=places[tid]){++migrations;throw std::runtime_error("worker migration");}
     save_checkpoint(output_path,b,y,current,c,batch,seg+1,cells,occupied,cpus[tid],places[tid]);long count=++snapshots;saved=y;saved_certificate=current;
     std::lock_guard<std::mutex>guard(lock);progress<<"{\"kind\":\"checkpoint\",\"committed_snapshots\":"<<count<<",\"case\":"<<c<<",\"batch\":"<<batch<<",\"segment_boundary\":"<<seg+1<<",\"cells\":"<<cells<<",\"error_bound_max\":"<<*std::max_element(current.total.begin(),current.total.end())<<",\"elapsed_seconds\":"<<omp_get_wtime()-scan_begin<<"}\n";progress.flush();if(!progress)throw std::runtime_error("progress write failed");
    }
    if(failed.load())continue;
    if(cells!=int(prepared.cells[c].size())||occupied!=(c%3==0?32:16))throw std::runtime_error("completed task inventory mismatch");
    states[c*BATCHES+batch]=std::move(y);certs[c*BATCHES+batch]=current;long count=++done;
    std::lock_guard<std::mutex>guard(lock);progress<<"{\"kind\":\"task_completed\",\"completed_tasks\":"<<count<<",\"case\":"<<c<<",\"batch\":"<<batch<<",\"cells\":"<<cells<<",\"elapsed_seconds\":"<<omp_get_wtime()-scan_begin<<"}\n";progress.flush();if(!progress)throw std::runtime_error("progress write failed");
   }catch(const std::exception&e){std::lock_guard<std::mutex>guard(lock);failed=true;if(failure.empty())failure=e.what();}
  }
  if(tid>=0&&tid<80&&cpus[tid]!=sched_getcpu())++migrations;
 }
 double kernel_seconds=omp_get_wtime()-scan_begin;progress.close();
 if(failed||done!=90||snapshots!=7290||initializations!=90||carry_checks!=7200||poly_checks!=FULL_CELLS||monotone_checks!=FULL_CELLS||inactive_checks!=5280||active_segments!=1920)throw std::runtime_error("partial full-word campaign: "+failure);
 check_coverage(workers,cpus,places);if(migrations||worker_fixtures!=80)throw std::runtime_error("worker validation failed");
 for(int count:worker_tasks)if(count==0)throw std::runtime_error("worker did not propagate a task");
 phase("full_word_scan_completed");
 std::ofstream endpoint(output_path/"endpoints.bin",std::ios::binary),component_file(output_path/"components.bin",std::ios::binary);
 if(!endpoint||!component_file)throw std::runtime_error("final artifact open failed");
 std::vector<std::array<I,B>>saved_norms(FULL_TASKS);for(int task=0;task<FULL_TASKS;++task)saved_norms[task]=center_norm2(states[task],b.d);
 for(int c=0;c<CASES;++c)for(int n=0;n<THERMAL;++n){int task=c*BATCHES+n/B,lane=n%B;
  for(int row=0;row<b.d;++row){C v=get(states[task],b.d,row,lane);double z[2]={v.real(),v.imag()};write_doubles(endpoint,z,2);}
  auto z=components(certs[task],lane,saved_norms[task][lane]);write_doubles(component_file,z.data(),z.size());
 }
 endpoint.close();component_file.close();if(!endpoint||!component_file)throw std::runtime_error("final artifact close failed");
 if(std::filesystem::file_size(output_path/"endpoints.bin")!=74131200||std::filesystem::file_size(output_path/"components.bin")!=69120)throw std::runtime_error("final artifact size mismatch");
 // Inherited full-time restoration and unnormalized thermal error accounting.
 std::array<double,6>errors{},norms{};std::array<std::array<double,7>,6>branch_components{};I retained{};for(I weight:prepared.thermal)retained=add(retained,weight);IWork iw(b.d);
 for(int c=0;c<6;++c){double e2=0,n2=0;std::array<double,7>r{};
  for(int batch=0;batch<15;++batch){embed(iw.value,states[c*15+batch],b.d,b.d);auto nn=norm2(iw.value,b.d);auto&cert=certs[c*15+batch];
   for(int lane=0;lane<8;++lane){double weight=prepared.thermal[batch*8+lane].hi;e2=au(e2,mu(weight,mu(cert.total[lane],cert.total[lane])));n2=au(n2,mu(weight,nn[lane].hi));double z[7]={cert.guard[lane],cert.tail[lane],cert.tube[lane],cert.jumps[lane],cert.sampled_time_node_L2[lane],cert.sampled_projection_node_L2[lane],cert.sampled_arithmetic_node_L2[lane]};for(int k=0;k<7;++k)r[k]=au(r[k],mu(weight,mu(z[k],z[k])));}}
  errors[c]=su(e2);norms[c]=su(n2);for(int k=0;k<7;++k)branch_components[c][k]=su(r[k]);
  if(!std::isfinite(errors[c])||!std::isfinite(norms[c]))throw std::runtime_error("nonfinite final branch enclosure");
 }
 struct Pair {Z sine,linear;I center,interval;double numerical,thermal,arithmetic,total;};std::array<Pair,6>pairs;int index=0;
 for(int sign=0;sign<2;++sign)for(int a=0;a<3;++a)for(int bb=a+1;bb<3;++bb){int c=3*sign+a,d=3*sign+bb;Z overlap{};
  for(int batch=0;batch<15;++batch){embed(iw.value,states[c*15+batch],b.d,b.d);embed(iw.aux,states[d*15+batch],b.d,b.d);idisplacement(b,iw.value,iw.dp,prepared.delta[index],prepared.delta_gaussian[index],FULL_L,nullptr,iw);auto z=inner(iw.aux,iw.dp,b.d);for(int lane=0;lane<8;++lane)overlap=add(overlap,scale(z[lane],prepared.thermal[batch*8+lane]));}
  Pair&v=pairs[index];v.sine=mul(prepared.rotation[index],overlap);v.linear=prepared.linear_pair[index];v.center=divi(absz(add(v.sine,neg(v.linear))),exact(2));
  double retained_root=su(retained.hi);v.numerical=du(std::min(au(mu(errors[c],retained_root),mu(errors[d],norms[c])),au(mu(errors[d],retained_root),mu(errors[c],norms[d]))),2);v.thermal=du(prepared.thermal_tail.hi,2);v.arithmetic=du(au(v.center.hi,-v.center.lo),2);double radius=au(v.numerical,v.thermal);v.total=au(radius,v.arithmetic);
  v.interval={std::max(0.0,ad(v.center.lo,-radius)),std::min(1.0,au(v.center.hi,radius))};check(v.interval);if(!std::isfinite(v.total))throw std::runtime_error("nonfinite final pair radius");++index;
 }
 phase("full_time_restoration_completed");
 std::ostringstream result;result<<std::setprecision(17)<<"{\"status\":\"COMPLETED\",\"scope\":\""<<FULL_SCOPE<<"\",\"error_account_scope\":\"normwise_ball_full_space_defect\",\"full_trajectory_certificate\":true,\"final_coherences_computed\":true,\"cutoff\":8,\"guard\":10,\"dimension\":6435,\"guard_dimension\":19448,\"steps_per_segment\":384,\"integrator\":\"DP5_TWO_HALF_STEPS\",\"dense_curve\":\"QUINTIC_THREE_POINT_HERMITE\",\"thermal_columns\":120,\"thermal_cutoff\":3,\"cases\":6,\"threads\":80,\"simd_lanes\":8,\"final_time_seconds_rational\":[1,2000],\"preparation_seconds\":"<<preparation_seconds<<",\"model_preparation_seconds\":"<<prepared.preparation_seconds<<",\"kernel_seconds\":"<<kernel_seconds<<",\"mpfr_version\":\""<<prepared.mpfr_version<<"\",\"completed_tasks\":"<<done<<",\"committed_snapshots\":"<<snapshots<<",\"trajectory_initializations\":"<<initializations<<",\"state_and_certificate_carry_checks\":"<<carry_checks<<",\"polynomial_start_checks\":"<<poly_checks<<",\"certificate_monotonicity_checks\":"<<monotone_checks<<",\"inactive_identity_checks\":"<<inactive_checks<<",\"active_task_segments\":"<<active_segments<<",\"worker_arithmetic_fixtures\":"<<worker_fixtures<<",\"migrations\":"<<migrations<<",\"reset_between_checkpoints\":false,\"normalization_applied\":false,\"phase_fit_applied\":false,\"legacy_eta_mismatch\":";emit(result,prepared.legacy_eta_mismatch);result<<",\"retained_thermal_weight\":";emit(result,retained);result<<",\"thermal_tail\":";emit(result,prepared.thermal_tail);
 result<<",\"fixtures\":{\"dense_displacement_error\":"<<fixture.dense_error<<",\"collective_displacement_error\":"<<fixture.collective_error<<",\"directed_arithmetic\":true,\"zero_displacement_enclosure\":true,\"adjoint_enclosure\":true,\"ball_interval_fixture_enclosure\":true,\"ball_reference_radius_ratio\":"<<fixture.ball_reference_ratio<<"},\"branches\":[";
 for(int c=0;c<6;++c){if(c)result<<',';result<<"{\"case\":"<<c<<",\"labels\":["<<LABELS[c%3][0]<<','<<LABELS[c%3][1]<<"],\"error_bound\":"<<errors[c]<<",\"weighted_endpoint_norm\":"<<norms[c]<<",\"guard_component\":"<<branch_components[c][0]<<",\"tail_component\":"<<branch_components[c][1]<<",\"continuum_component\":"<<branch_components[c][2]<<",\"jump_component\":"<<branch_components[c][3]<<",\"sampled_time_node_L2\":"<<branch_components[c][4]<<",\"sampled_projection_node_L2\":"<<branch_components[c][5]<<",\"sampled_arithmetic_node_L2\":"<<branch_components[c][6]<<",\"node_split_scope\":\"diagnostic_quadrature_only_continuum_allowance_is_combined\",\"linear_phase\":";emit(result,prepared.final[c].phase);result<<",\"linear_alpha\":[";for(int m=0;m<7;++m){if(m)result<<',';emit(result,prepared.final[c].alpha[m]);}result<<"],\"columns\":[";
  for(int n=0;n<120;++n){if(n)result<<',';auto&v=certs[c*15+n/8];int lane=n%8;result<<"{\"thermal_index\":"<<n<<",\"guard\":"<<v.guard[lane]<<",\"tail\":"<<v.tail[lane]<<",\"continuum\":"<<v.tube[lane]<<",\"jumps\":"<<v.jumps[lane]<<",\"total\":"<<v.total[lane]<<",\"sampled_time_node_L2\":"<<v.sampled_time_node_L2[lane]<<",\"sampled_projection_node_L2\":"<<v.sampled_projection_node_L2[lane]<<",\"sampled_arithmetic_node_L2\":"<<v.sampled_arithmetic_node_L2[lane]<<",\"maximum_node_bound\":"<<v.max_node[lane]<<",\"maximum_norm_error\":"<<v.max_norm_error[lane]<<'}';}result<<"]}";
 }
 result<<"],\"pair_coherences\":[";index=0;
 for(int sign=0;sign<2;++sign)for(int a=0;a<3;++a)for(int bb=a+1;bb<3;++bb){auto&v=pairs[index];if(index)result<<',';result<<"{\"cases\":["<<3*sign+a<<','<<3*sign+bb<<"],\"sine_retained_interval\":";emit(result,v.sine);result<<",\"linear_full_interval\":";emit(result,v.linear);result<<",\"witness_center_interval\":";emit(result,v.center);result<<",\"numerical_radius\":"<<v.numerical<<",\"thermal_radius\":"<<v.thermal<<",\"arithmetic_radius\":"<<v.arithmetic<<",\"total_radius\":"<<v.total<<",\"certified_trace_distance_interval\":";emit(result,v.interval);result<<'}';++index;}
 result<<"],\"thread_map\":[";for(int t=0;t<80;++t){if(t)result<<',';result<<"{\"thread\":"<<t<<",\"cpu\":"<<cpus[t]<<",\"place\":"<<places[t]<<",\"completed_tasks\":"<<worker_tasks[t]<<'}';}result<<"],\"end_to_end_seconds\":"<<omp_get_wtime()-begin<<"}\n";
 atomic_text(output_path/"result.json",result.str());std::cout<<result.str();return 0;
}catch(const std::exception&e){std::cerr<<e.what()<<'\n';return 2;}}
