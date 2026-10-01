`timescale 1ns/1ps
module law_tb;
  reg [1519:0] input_state,expected_state;
  reg [2:0] p,expected_p;
  reg [1:0] layer,cuts;
  reg inverse,expected_valid;
  wire [1519:0] actual_state;
  wire [2:0] actual_p;
  wire valid;
  integer fd,rc,count;
  reg [4095:0] filename;
  twist_law dut(input_state,p,layer,inverse,cuts,actual_state,actual_p,valid);
  initial begin
    if(!$value$plusargs("vectors=%s",filename)) $fatal(1,"missing vectors");
    fd=$fopen(filename,"r"); if(fd==0) $fatal(1,"cannot open vectors");
    count=0;
    while(!$feof(fd)) begin
      rc=$fscanf(fd,"%h %h %h %h %h %h %h %h\n",input_state,p,layer,inverse,cuts,expected_valid,expected_state,expected_p);
      if(rc!=8) $fatal(1,"bad vector row");
      #1;
      if(valid!==expected_valid || actual_state!==expected_state || actual_p!==expected_p)
        $fatal(1,"RTL mismatch row %0d layer=%0d inverse=%0d p=%0d",count,layer,inverse,p);
      count=count+1;
    end
    $display("SIMULATION law vectors=%0d PASS; no physical qualification",count);
    $finish;
  end
endmodule
