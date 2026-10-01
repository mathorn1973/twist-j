// NON-CANONICAL timed physical-commit supervisor. No instrument driver.
// Default 100 MHz; ticks/second must be divisible by 10 and independently
// calibrated. No direct pin/IO/analog safety qualification is claimed.
module twist_controller #(parameter N=3, parameter [63:0] TICKS_PER_SECOND=100000000,
  parameter MACROSTEPS=10, parameter TURNAROUND_AT=0)(
  input clk, reset,
  input prepare, input [(32*N-1)*16-1:0] preparation,
  input start, inverse_mode, input [N-2:0] cut_request,
  input [2:0] physical_p, input p_valid,
  input [N-2:0] physical_cut_a,physical_cut_b,
  input disconnected,operation_done,measurement_confirmed,
  input adc_ok,samples_complete,dock_identity_ok,reserve_ok,energy_bounds_ok,voltage_ok,
  output reg [(32*N-1)*16-1:0] registers,
  output reg state_valid,error,busy,
  output reg actuation_enable,
  output [1:0] active_layer,
  output [2:0] desired_p
);
  localparam WORDS=32*N-1;
  reg prepared,reverse;
  reg [N-2:0] cuts;
  reg [1:0] stage;
  reg [2:0] phase; // 0=start,1=break,2=execute,3=settle,4=read until commit
  reg [63:0] ticks,slot_ticks,deadline_ticks;
  reg [WORDS*16-1:0] pending;
  reg [2:0] pending_p;
  reg [2:0] input_p;
  integer macrostep;
  wire [WORDS*16-1:0] proposal,load_proposal;
  wire [2:0] proposal_p,load_p;
  wire law_valid,load_valid;
  assign active_layer=reverse ? 3-stage : stage;
  assign desired_p=pending_p;
  twist_law #(N) law(registers,physical_p,active_layer,reverse,cuts,proposal,proposal_p,law_valid);
  twist_law #(N) load_check(preparation,physical_p,2'd3,1'b0,cut_request,load_proposal,load_p,load_valid);
  always @* begin
    case(active_layer)
      0:begin slot_ticks=2*TICKS_PER_SECOND;deadline_ticks=17*TICKS_PER_SECOND/10;end
      1,2:begin slot_ticks=5*TICKS_PER_SECOND/2;deadline_ticks=22*TICKS_PER_SECOND/10;end
      3:begin slot_ticks=3*TICKS_PER_SECOND;deadline_ticks=TICKS_PER_SECOND/10;end
    endcase
  end
  always @(posedge clk) begin
    if(reset) begin
      registers<=0;state_valid<=0;error<=0;busy<=0;prepared<=0;
      actuation_enable<=0;reverse<=0;cuts<=0;stage<=0;phase<=0;ticks<=0;pending<=0;pending_p<=0;input_p<=0;macrostep<=0;
    end else if(!error) begin
      if(prepare) begin
        if(busy || !load_valid || !p_valid || !disconnected || !measurement_confirmed ||
           !adc_ok || !samples_complete || !dock_identity_ok || !reserve_ok || !energy_bounds_ok || !voltage_ok ||
           physical_cut_a!=cut_request || physical_cut_b!=cut_request) begin
          error<=1;state_valid<=0;busy<=0;actuation_enable<=0;
        end else begin registers<=preparation;prepared<=1;state_valid<=1; end
      end else if(start && !busy) begin
        if(!prepared || !p_valid || physical_p>4 || !disconnected ||
           physical_cut_a!=cut_request || physical_cut_b!=cut_request ||
           TICKS_PER_SECOND<100 || TICKS_PER_SECOND>1000000000 || TICKS_PER_SECOND%10!=0 ||
           MACROSTEPS<1 || MACROSTEPS>20 || TURNAROUND_AT<0 || TURNAROUND_AT>=MACROSTEPS) begin
          error<=1;state_valid<=0;
        end else begin
          busy<=1;reverse<=inverse_mode;cuts<=cut_request;stage<=0;phase<=0;ticks<=0;macrostep<=0;
        end
      end else if(busy) begin
        if(!adc_ok || !samples_complete || !dock_identity_ok || !reserve_ok || !voltage_ok ||
           physical_cut_a!=cuts || physical_cut_b!=cuts ||
           start || (phase<3 && (ticks>deadline_ticks ||
                (ticks==deadline_ticks && !(phase==2 && operation_done))))) begin
          error<=1;busy<=0;state_valid<=0;actuation_enable<=0;
        end else begin
          ticks<=ticks+1;
          case(phase)
            0:begin
              if(!law_valid || !p_valid || physical_p>4) begin error<=1;busy<=0;state_valid<=0;end
              else begin pending<=proposal;pending_p<=proposal_p;input_p<=physical_p;phase<=1;state_valid<=0; end
            end
            1:begin
              if(!p_valid || physical_p!=input_p || operation_done) begin error<=1;busy<=0;state_valid<=0;end
              else if(disconnected) begin actuation_enable<=1;phase<=2;end
            end
            2:begin
              if(operation_done) begin actuation_enable<=0;phase<=3;end
            end
            3:begin
              if(ticks>=slot_ticks-TICKS_PER_SECOND/10) begin
                if(!p_valid || physical_p!=pending_p || !energy_bounds_ok || !disconnected || !measurement_confirmed) begin
                  error<=1;busy<=0;state_valid<=0;
                end else begin phase<=4;end
              end
            end
            4:begin
              // Keep validating the entire settled window, not one good sample.
              if(!p_valid || physical_p!=pending_p || !energy_bounds_ok || !disconnected || !measurement_confirmed) begin
                error<=1;busy<=0;state_valid<=0;
              end
            end
            default:begin error<=1;busy<=0;state_valid<=0;actuation_enable<=0;end
          endcase
          if(ticks>=slot_ticks-1) begin
            if(phase!=4 || !p_valid || physical_p!=pending_p || !energy_bounds_ok ||
               !disconnected || !measurement_confirmed) begin
              error<=1;busy<=0;state_valid<=0;actuation_enable<=0;
            end else begin
              registers<=pending;state_valid<=1;phase<=0;ticks<=0;
              if(stage==3) begin
                stage<=0;
                if(macrostep==MACROSTEPS-1) busy<=0;
                else begin
                  macrostep<=macrostep+1;
                  if(TURNAROUND_AT!=0 && macrostep+1==TURNAROUND_AT) reverse<=!reverse;
                end
              end else stage<=stage+1;
            end
          end
        end
      end
    end
  end
endmodule
