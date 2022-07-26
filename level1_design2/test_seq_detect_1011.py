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
    assert dut.seq_seen==1,"seq_seen not achieve"

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
    assert dut.seq_seen==1,"seq_det not achieve"