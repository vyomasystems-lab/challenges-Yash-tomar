# See LICENSE.vyoma for details

# SPDX-License-Identifier: CC0-1.0

import os


import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge
from cocotb.triggers import Timer

@cocotb.test()
async def test_seq_bug1(dut):
    """Test for seq detection """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    await FallingEdge(dut.clk)

    cocotb.log.info('#### CTB: Develop your test here! ######')
    await FallingEdge(dut.clk)
    dut.inp_bit.value = 1
    await RisingEdge(dut.clk)
    await Timer(10, units='ns')
    dut._log.info("Inp_bit : %s ,seq_seen : %s, current_state : %s , next_state : %s",str(dut.inp_bit.value),str(dut.seq_seen.value),str(dut.current_state.value),str(dut.next_state.value))

    await FallingEdge(dut.clk)
    dut.inp_bit.value = 1
    await RisingEdge(dut.clk)
    await Timer(10, units='ns')
    dut._log.info("Inp_bit : %s ,seq_seen : %s, current_state : %s , next_state : %s",str(dut.inp_bit.value),str(dut.seq_seen.value),str(dut.current_state.value),str(dut.next_state.value))
    
    await FallingEdge(dut.clk)  
    dut.inp_bit.value = 1
    await RisingEdge(dut.clk)
    await Timer(10, units='ns')
    dut._log.info("Inp_bit : %s ,seq_seen : %s, current_state : %s , next_state : %s",str(dut.inp_bit.value),str(dut.seq_seen.value),str(dut.current_state.value),str(dut.next_state.value))
    
    await FallingEdge(dut.clk)
    dut.inp_bit.value = 0
    await RisingEdge(dut.clk)
    await Timer(10, units='ns')
    dut._log.info("Inp_bit : %s ,seq_seen : %s, current_state : %s , next_state : %s",str(dut.inp_bit.value),str(dut.seq_seen.value),str(dut.current_state.value),str(dut.next_state.value))
    
    await FallingEdge(dut.clk)
    dut.inp_bit.value = 1
    await RisingEdge(dut.clk)
    await Timer(10, units='ns')
    dut._log.info("Inp_bit : %s ,seq_seen : %s, current_state : %s , next_state : %s",str(dut.inp_bit.value),str(dut.seq_seen.value),str(dut.current_state.value),str(dut.next_state.value))
    
    await FallingEdge(dut.clk)
    dut.inp_bit.value = 1
    await RisingEdge(dut.clk)
    await Timer(10, units='ns')
    dut._log.info("Inp_bit : %s ,seq_seen : %s, current_state : %s , next_state : %s",str(dut.inp_bit.value),str(dut.seq_seen.value),str(dut.current_state.value),str(dut.next_state.value))
    assert dut.seq_seen==1,"seq_det not achieve"

    await FallingEdge(dut.clk)
    dut.inp_bit.value = 0
    await RisingEdge(dut.clk)
    await Timer(10, units='ns')
    dut._log.info("Inp_bit : %s ,seq_seen : %s, current_state : %s , next_state : %s",str(dut.inp_bit.value),str(dut.seq_seen.value),str(dut.current_state.value),str(dut.next_state.value))
    
    await FallingEdge(dut.clk)
    dut.inp_bit.value = 1
    await RisingEdge(dut.clk)
    await Timer(10, units='ns')
    dut._log.info("Inp_bit : %s ,seq_seen : %s, current_state : %s , next_state : %s",str(dut.inp_bit.value),str(dut.seq_seen.value),str(dut.current_state.value),str(dut.next_state.value))
    
    await FallingEdge(dut.clk)
    dut.inp_bit.value = 0
    await RisingEdge(dut.clk)
    await Timer(10, units='ns')
    dut._log.info("Inp_bit : %s ,seq_seen : %s, current_state : %s , next_state : %s",str(dut.inp_bit.value),str(dut.seq_seen.value),str(dut.current_state.value),str(dut.next_state.value))
    
    await FallingEdge(dut.clk)
    dut.inp_bit.value = 1
    await RisingEdge(dut.clk)
    await Timer(10, units='ns')
    dut._log.info("Inp_bit : %s ,seq_seen : %s, current_state : %s , next_state : %s",str(dut.inp_bit.value),str(dut.seq_seen.value),str(dut.current_state.value),str(dut.next_state.value))
    
    await FallingEdge(dut.clk)
    dut.inp_bit.value = 1
    await RisingEdge(dut.clk)
    await Timer(10, units='ns')
    dut._log.info("Inp_bit : %s ,seq_seen : %s, current_state : %s , next_state : %s",str(dut.inp_bit.value),str(dut.seq_seen.value),str(dut.current_state.value),str(dut.next_state.value))
    
    
     15000.00ns INFO     #### CTB: Develop your test here! ######
 30010.00ns INFO     Inp_bit : 1 ,seq_seen : 0, current_state : 001 , next_state : 000
 40010.00ns INFO     Inp_bit : 1 ,seq_seen : 0, current_state : 000 , next_state : 001
 50010.00ns INFO     Inp_bit : 1 ,seq_seen : 0, current_state : 001 , next_state : 000
 60010.00ns INFO     Inp_bit : 0 ,seq_seen : 0, current_state : 010 , next_state : 000
 70010.00ns INFO     Inp_bit : 1 ,seq_seen : 0, current_state : 011 , next_state : 100
 80010.00ns INFO     Inp_bit : 1 ,seq_seen : 1, current_state : 100 , next_state : 000
 90010.00ns INFO     Inp_bit : 0 ,seq_seen : 0, current_state : 000 , next_state : 000
100010.00ns INFO     Inp_bit : 1 ,seq_seen : 0, current_state : 001 , next_state : 000
110010.00ns INFO     Inp_bit : 0 ,seq_seen : 0, current_state : 010 , next_state : 000
120010.00ns INFO     Inp_bit : 1 ,seq_seen : 0, current_state : 011 , next_state : 100
130010.00ns INFO     Inp_bit : 1 ,seq_seen : 1, current_state : 100 , next_state : 000
130010.00ns INFO     test_seq_bug1 passed
130010.00ns INFO     ********************************************************************************************
                     ** TEST                                STATUS  SIM TIME (ns)  REAL TIME (s)  RATIO (ns/s) **
                     ********************************************************************************************
                     ** test_seq_detect_1011.test_seq_bug1   PASS      130010.00           0.01   25690260.40  **
                     ********************************************************************************************
                     ** TESTS=1 PASS=1 FAIL=0 SKIP=0                   130010.00           0.02    6537681.39  **
                     ********************************************************************************************
                     
                     ERROR:inserted in code
                     // See LICENSE.vyoma for more details
// Verilog module for Sequence detection: 1011
module seq_detect_1011(seq_seen, inp_bit, reset, clk);

  output seq_seen;
  input inp_bit;
  input reset;
  input clk;

  parameter IDLE = 0,
            SEQ_1 = 1, 
            SEQ_10 = 2,
            SEQ_101 = 3,
            SEQ_1011 = 4;

  reg [2:0] current_state, next_state;

  // if the current state of the FSM has the sequence 1011, then the output is
  // high
  assign seq_seen = current_state == SEQ_1011 ? 1 : 0;

  // state transition
  always @(posedge clk)
  begin
    if(reset)
    begin
      current_state <= IDLE;
    end
    else
    begin
      current_state <= next_state;
    end
  end

  // state transition based on the input and current state
  always @(inp_bit or current_state)
  begin
    case(current_state)
      IDLE:
      begin
        if(inp_bit == 1)
          next_state = SEQ_1;
        else
          next_state = IDLE;
      end
      SEQ_1:
      begin
        if(inp_bit == 1)
          next_state = IDLE;
        else
          next_state = SEQ_10;
      end
      SEQ_10:
      begin
        if(inp_bit == 1)
          next_state = SEQ_10;
        else
          next_state = IDLE;
      end
      SEQ_101:
      begin
        if(inp_bit == 1)
          next_state = SEQ_1011;
        else
          next_state = IDLE;
      end
      SEQ_1011:
      begin
        next_state = IDLE;
      end
    endcase
  end

  `ifdef COCOTB_SIM
initial begin
  $dumpfile ("seq_detect_1011.vcd");
  $dumpvars (0, seq_detect_1011);
  #1;
end
endmodule

Result log:-
                    
                     
                      15000.00ns INFO     #### CTB: Develop your test here! ######
 30010.00ns INFO     Inp_bit : 1 ,seq_seen : 0, current_state : 001 , next_state : 000
 40010.00ns INFO     Inp_bit : 1 ,seq_seen : 0, current_state : 000 , next_state : 001
 50010.00ns INFO     Inp_bit : 1 ,seq_seen : 0, current_state : 001 , next_state : 000
 60010.00ns INFO     Inp_bit : 0 ,seq_seen : 0, current_state : 010 , next_state : 000
 70010.00ns INFO     Inp_bit : 1 ,seq_seen : 0, current_state : 010 , next_state : 010
 80010.00ns INFO     Inp_bit : 1 ,seq_seen : 0, current_state : 010 , next_state : 010
 80010.00ns INFO     test_seq_bug1 failed
                     Traceback (most recent call last):
                       File "/workspace/challenges-Yash-tomar/level1_design2/test_seq_detect_1011.py", line 65, in test_seq_bug1
                         assert dut.seq_seen==1,"seq_seen not achieve"
                     AssertionError: seq_seen not achieve
 80010.00ns INFO     ********************************************************************************************
                     ** TEST                                STATUS  SIM TIME (ns)  REAL TIME (s)  RATIO (ns/s) **
                     ********************************************************************************************
                     ** test_seq_detect_1011.test_seq_bug1   FAIL       80010.00           0.00   23421710.44  **
                     ********************************************************************************************
                     ** TESTS=1 PASS=0 FAIL=1 SKIP=0                    80010.00           0.02    4573016.83  **
                     ********************************************************************************************
                     
                     
Error Fix:-
Next state will be s101 when there is high input_bit in s10 state
