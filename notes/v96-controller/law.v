// NON-CANONICAL, SOFTWARE/SIMULATION only. Fixed #1316 arithmetic.
// N=3: 95 signed 16-bit registers; physical pointer is a separate input.
module twist_law #(parameter N=3)(
  input [(32*N-1)*16-1:0] state_in,
  input [2:0] physical_p,
  input [1:0] layer, // 0=G, 1=A, 2=B, 3=F
  input inverse,
  input [N-2:0] cuts,
  output reg [(32*N-1)*16-1:0] state_out,
  output reg [2:0] proposed_p,
  output reg valid
);
  localparam WORDS=32*N-1;
  reg signed [63:0] w [0:WORDS-1];
  reg signed [63:0] t [0:WORDS-1];
  reg signed [63:0] total, a,b,c,d,u,v,aa,bb,cc,dd,balance;
  reg signed [63:0] e0,e1,e2,e3,m0,m1;
  reg is_r,is_am,accept,box_ok;
  integer i,j,base,r,q,limit;
  function signed [63:0] qform;
    input signed [63:0] a,b,c,d;
    begin qform=6*(a*a+b*b+c*c+d*d)+4*(a*b+a*d+b*c+c*d)-2*(a*c+b*d); end
  endfunction
  function signed [63:0] hform;
    input signed [63:0] a,b,c,d;
    begin hform=2*a*a+3*b*b+c*c+d*d-2*a*b+2*a*c-a*d-b*c+3*b*d; end
  endfunction
  function signed [63:0] endpoint;
    input integer j;
    input am;
    begin
      endpoint=0;
      if(am) begin
        if(j==0 || j==10) endpoint=1;
        if(j==5 || j==9) endpoint=-1;
      end else begin
        if(j==0 || j==2) endpoint=1;
        if(j==1) endpoint=-2;
      end
    end
  endfunction
  always @* begin
    state_out=state_in; proposed_p=physical_p; valid=0;
    total=0; a=0;b=0;c=0;d=0;u=0;v=0;aa=0;bb=0;cc=0;dd=0;balance=0;
    e0=0;e1=0;e2=0;e3=0;m0=0;m1=0;
    is_r=0;is_am=0;accept=0;box_ok=(physical_p<5 && N>=2 && N<=16);
    base=0;r=0;q=0;limit=0;
    for(i=0;i<WORDS;i=i+1) begin
      w[i]=$signed(state_in[i*16+:16]); t[i]=w[i];
      if(i<31*N) begin
        case(i%31)
          24:limit=15;25:limit=9;26,27:limit=11;28:limit=12;29:limit=18;30:limit=41;
          default:limit=6;
        endcase
        if(w[i]>limit || w[i]<-limit) box_ok=0;
        if(i%31==30 && w[i]<0) box_ok=0;
      end else if(w[i]<0 || w[i]>41) box_ok=0;
    end
    // No multiplication of an unvalidated 16-bit input.
    if(box_ok) begin
      for(i=0;i<N;i=i+1) begin
        base=31*i;
        for(j=0;j<24;j=j+4) total=total+qform(w[base+j],w[base+j+1],w[base+j+2],w[base+j+3]);
        e0=w[base+24];e1=w[base+25];e2=w[base+26];e3=w[base+27];m0=w[base+28];m1=w[base+29];
        total=total+e0*e0+e1*e1+e2*e2+e3*e3+m0*m0+m1*m1+e0*(m0-m1)-e1*m0+(e2+e3)*m1+w[base+30];
      end
      for(i=31*N;i<WORDS;i=i+1) total=total+w[i];
      if(total==41) begin
        valid=1;
        if(layer==0) begin
          for(i=0;i<N;i=i+1) begin
            base=31*i;is_r=1;is_am=1;
            for(j=0;j<12;j=j+1) begin
              if(w[base+j]!=endpoint(j,0)) is_r=0;
              if(w[base+j]!=endpoint(j,1)) is_am=0;
            end
            e0=w[base+24];e1=w[base+25];e2=w[base+26];e3=w[base+27];
            a=2*e0-3*e1+e2+e3; b=-e0-e1+2*e2+2*e3;
            u=2*e0+2*e1+e2+e3; v=e0+e1+3*e2-2*e3;
            if((is_r||is_am) && a%5==0 && b%5==0 && u%5==0 && v%5==0) begin
              a=a/5;b=b/5;u=u/5;v=v/5;c=w[base+28];d=w[base+29];accept=1;
              if(is_r) begin
                aa=a+2*b+c+2*d;bb=2*a-b+2*c-d;cc=-5*b+c-3*d;dd=-5*a+5*b-3*c+4*d;
                if(aa%5 || bb%5 || cc%5 || dd%5) accept=0;
                aa=aa/5;bb=bb/5;cc=cc/5;dd=dd/5;
                balance=w[base+30]+4*hform(aa,bb,cc,dd)-2;
              end else begin
                aa=a-3*b-c-2*d;bb=-3*a+4*b-2*c+d;cc=5*b+c+2*d;dd=5*a-5*b+2*c-d;
                balance=w[base+30]+2-4*hform(a,b,c,d);
              end
              if(balance<0) accept=0;
              if(accept) begin
                for(j=0;j<12;j=j+1) t[base+j]=endpoint(j,is_r);
                t[base+24]=aa-bb+u;t[base+25]=-aa+u;t[base+26]=bb+v;t[base+27]=bb+u-v;
                t[base+28]=cc;t[base+29]=dd;t[base+30]=balance;
                if(i==N-1) begin
                  if(!inverse && is_r) proposed_p=(physical_p==4)?0:physical_p+1;
                  if(inverse && is_am) proposed_p=(physical_p==0)?4:physical_p-1;
                end
              end
            end
          end
        end else if(layer==1 || layer==2) begin
          for(i=0;i<N-1;i=i+1) if(!cuts[i]) begin
            r=31*(i+(layer==2))+30;q=31*N+i;t[r]=w[q];t[q]=w[r];
          end
        end else begin
          for(i=0;i<N;i=i+1) begin
            base=31*i;
            e0=w[base+24];e1=w[base+25];e2=w[base+26];e3=w[base+27];m0=w[base+28];m1=w[base+29];
            if(inverse) begin
              m0=m0+e0-e1;m1=m1-e0+e2+e3;
              e0=e0-m0+m1;e1=e1+m0;e2=e2-m1;e3=e3-m1;
            end else begin
              e0=e0+m0-m1;e1=e1-m0;e2=e2+m1;e3=e3+m1;
              m0=m0-e0+e1;m1=m1+e0-e2-e3;
            end
            t[base+24]=e0;t[base+25]=e1;t[base+26]=e2;t[base+27]=e3;t[base+28]=m0;t[base+29]=m1;
          end
        end
        for(i=0;i<WORDS;i=i+1) state_out[i*16+:16]=t[i][15:0];
      end
    end
  end
endmodule
