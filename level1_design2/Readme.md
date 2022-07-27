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
                     
