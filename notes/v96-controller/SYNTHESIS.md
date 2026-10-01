# Generic RTL synthesis receipt and board implementation boundary

NON-CANONICAL / SOFTWARE + STATIC SYNTHESIS, 2026-10-01. No bitstream,
placed timing, board resource fit, physical clock measurement or HIL result.

The coordinator actually ran Yosys 0.9, Ubuntu package 0.9-2, under Ubuntu
22.04 / WSL2 x86_64. Both commands below completed with exit 0 using the
default N=3 source. The first lowers and optimizes the full arithmetic core.
The second lowers the supervisor with its two arithmetic instances explicitly
treated as black boxes; it is not a flattened whole-device resource report.

```sh
yosys -Q -T -p 'read_verilog notes/v96-controller/law.v; hierarchy -top twist_law; proc; opt; stat'
yosys -Q -T -p 'read_verilog -lib notes/v96-controller/law.v; read_verilog notes/v96-controller/controller.v; hierarchy -top twist_controller; proc; opt; stat'
```

The tool and its Tcl runtime were unpacked from distribution packages into
an external development directory, without installing or changing repository
dependencies. Set `LD_LIBRARY_PATH` to that prefix's
`usr/lib/x86_64-linux-gnu` when using the unpacked binary. Package hashes:

| Downloaded package | SHA-256 |
| --- | --- |
| yosys 0.9-2 amd64 | b9f27c0a999753ecc12efa31ebdf97de5a0ca4f970780ddf580b8668a47e8a20 |
| libtcl8.6 8.6.12+dfsg-1build1 amd64 | 5232b051f9dcd567648ab3061848329ef15cc3a8cb1e66732be80f102dad293c |

Synthesized source hashes:

| File | SHA-256 |
| --- | --- |
| law.v | 6828a3990064ed5985b3f0cfaefe62c43e4b7d7c63d670afa881a7cc4e7b221c |
| controller.v | 2d5cbc360bed02e3b4e7ada9d61e13e984cc0cc13e63df7840097903be3fc538 |

## Actual generic statistics

| Quantity | Arithmetic core | Supervisor, law instances black-boxed |
| --- | ---: | ---: |
| Wires | 38,821 | 286 |
| Wire bits | 2,422,895 | 35,245 |
| Public wires | 105 | 45 |
| Public wire bits | 9,165 | 7,880 |
| Memories / memory bits | 0 / 0 | 0 / 0 |
| Remaining processes | 0 | 0 |
| Generic cells | 38,814 | 261 |

Core cell inventory: add 335; div 24; eq 193; gt 95; logic_and 14;
logic_not 17; logic_or 108; lt 102; mod 24; mul 314; mux 37,267;
ne 40; neg 6; pmux 140; reduce_bool 11; sub 124. No latch or flip-flop
cell remains in the optimized combinational core. The frontend initially
reported a latch for a procedural loop variable; it was removed by
optimization and is absent from these final statistics. Array lowering and
the large mux structure remain visible; this is not a compact mapped design.

Supervisor inventory: add 3; dff 15; eq 10; ge 2; gt 2; logic_and 4;
logic_not 16; logic_or 39; lt 1; mux 148; ne 7; pmux 7; reduce_or 2;
sub 3; twist_law 2. The 15 dff entries are **vector cells**, not 15
physical one-bit flip-flops. Likewise a generic multiplier or mux is not
one FPGA LUT or DSP. The two black boxes do not account for their logic here.

The optimizer reported a bounded mux-tree analysis stopping after too many
iterations; the command still completed and preserved the unoptimized
remaining logic. These counts establish neither minimality nor timing.

External transcript receipts (generated development output, not tracked
scientific evidence):

| Transcript | Bytes | SHA-256 |
| --- | ---: | --- |
| law-final-synthesis.txt | 932802 | 7fc978c2a50cab3f62d12a7a41a3f2711c368d25eda89c6a7a84235462db10f2 |
| controller-synthesis.txt | 12618 | bd7d05e1b31539e59a7a35e6e92448786be7ee7c91693034fcde0a17764884a3 |

A separate reviewer checked both stored transcript hashes and lengths, the
complete final cell inventories, current source hashes and the documented
black-box scope. No mismatch or resource/timing overclaim was found.

## Unfinished board gate

No Xilinx technology mapping, actual Arty resource utilization, placement,
routing, timing constraints, clock closure or pin assignment was performed.
In particular these large generic counts do not establish that the current
parallel arithmetic fits or runs at 100 MHz. A reviewed sequential or
otherwise optimized implementation may be required; any such change must
preserve the exact law and fixed external operation deadlines and receive
new equivalence tests and synthesis/timing receipts.

The next C03 gate is a concrete board implementation with reviewed clock/IO
constraints and mapped resource/timing reports, followed by independently
qualified ADC, contact, pointer and reserve feedback. The successful digital
simulations and this generic synthesis cannot authorize physical actuation.
