`timescale 1ns/1ps
module controller_tb;
  reg clk=0; always #5 clk=~clk;
  reg reset,prepare,start,inv,p_valid,disconnected,done,confirmed,adc,samples,dock,reserve,energy,voltage;
  reg [1519:0] preparation;
  reg [2:0] p;
  reg [1:0] cuts,cut_a,cut_b;
  wire [1519:0] registers;
  wire valid,error,busy,enable;
  wire [1:0] layer;
  wire [2:0] desired;
  integer scenario,cycles,pulses,enabled_ticks;
  twist_controller #(.TICKS_PER_SECOND(1000),.MACROSTEPS(20),.TURNAROUND_AT(10)) dut(
    clk,reset,prepare,preparation,start,inv,cuts,p,p_valid,cut_a,cut_b,
    disconnected,done,confirmed,adc,samples,dock,reserve,energy,voltage,
    registers,valid,error,busy,enable,layer,desired);
  task tick; begin @(posedge clk); #1; end endtask
  task initialize;
    begin
      reset=1;prepare=0;start=0;inv=(scenario==13);p_valid=1;disconnected=1;done=0;confirmed=1;
      adc=1;samples=1;dock=1;reserve=1;energy=1;voltage=1;p=0;cuts=0;cut_a=0;cut_b=0;
      preparation=0;
      preparation[0*16+:16]=1;preparation[1*16+:16]=-2;preparation[2*16+:16]=1;
      preparation[24*16+:16]=1;preparation[25*16+:16]=1;
      preparation[26*16+:16]=-2;preparation[27*16+:16]=-2;
      preparation[28*16+:16]=1;preparation[29*16+:16]=2;
      preparation[62*16+:16]=1;preparation[63*16+:16]=-2;preparation[64*16+:16]=1;
      tick;reset=0;prepare=1;tick;prepare=0;
      if(!valid || error) $fatal(1,"preparation rejected");
      start=1;tick;start=0;
      if(!busy || error) $fatal(1,"start rejected");
      cycles=0;pulses=0;enabled_ticks=0;
    end
  endtask
  initial begin
    for(scenario=0;scenario<14;scenario=scenario+1) begin
      initialize;
      while(busy && cycles<200005) begin
        @(negedge clk);
        done=0;disconnected=!enable;
        if(enable) begin
          enabled_ticks=enabled_ticks+1;
          if(enabled_ticks==3 && scenario!=7) begin done=1;p=desired;pulses=pulses+1;end
        end else enabled_ticks=0;
        if(cycles>=5) begin
          case(scenario)
            1:adc=0;
            2:samples=0;
            3:dock=0;
            4:reserve=0;
            5:cut_a=1;
            6:cut_b=1;
            8:begin p=5;p_valid=0;end
            9:confirmed=0;
            10:voltage=0;
            11:energy=0;
          endcase
        end
        if(scenario==12 && dut.phase==1) done=1; // stale completion during BREAK
        tick;cycles=cycles+1;
      end
      if(scenario==0 || scenario==13) begin
        if(error || !valid || registers!==preparation || p!=0 || cycles!=200000 || pulses!=80)
          $fatal(1,"roundtrip/calendar failed cycles=%0d pulses=%0d p=%0d error=%0d",cycles,pulses,p,error);
      end else begin
        if(!error || valid || enable) $fatal(1,"fault scenario %0d did not fail closed",scenario);
        start=1;tick;start=0;
        if(!error || valid || busy) $fatal(1,"ERROR not absorbing");
      end
    end
    $display("SIMULATION controller both 200s roundtrips +12 fault cases PASS; no HIL");
    $finish;
  end
endmodule
