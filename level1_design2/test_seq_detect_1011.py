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
    #await Timer(2, units='ns')
    #yield RisingEdge(dut.inp_bit.value <= 1) 
    #await Timer(10, units='ns')
    #dut.inp_bit.value <= 0;
    #await Timer(10, units='ns')

    #dut.inp_bit.value <= 1;
    #await Timer(10, units='ns')
    #dut.inp_bit.value <= 1;
    #await Timer(10, units='ns')
    #assert dut.seq_seen == 1, "Seq_check test fails"

    await FallingEdge(dut.clk)
    dut.inp_bit.value <= 1
    await RisingEdge(dut.clk)
    print("Inp_bit : ",int(dut.inp_bit)," seq_seen : ",int(dut.seq_seen))
    await FallingEdge(dut.clk)
    dut.inp_bit.value <= 1
    await RisingEdge(dut.clk)
    #print("Inp_bit : ",int(dut.inp_bit)," seq_seen : ",int(dut.seq_seen))
    await FallingEdge(dut.clk)
    dut.inp_bit.value <= 0
    await RisingEdge(dut.clk)
    #print("Inp_bit : ",int(dut.inp_bit)," seq_seen : ",int(dut.seq_seen))
    await FallingEdge(dut.clk)
    dut.inp_bit.value <= 1
    await RisingEdge(dut.clk)
    #print("Inp_bit : ",int(dut.inp_bit)," seq_seen : ",int(dut.seq_seen))
    await FallingEdge(dut.clk)
    dut.inp_bit.value <= 1
    await RisingEdge(dut.clk)
    #print("Inp_bit : ",int(dut.inp_bit)," seq_seen : ",int(dut.seq_seen))
    await FallingEdge(dut.clk)
    dut.inp_bit.value <= 0
    await RisingEdge(dut.clk)
    #print("Inp_bit : ",int(dut.inp_bit)," seq_seen : ",int(dut.seq_seen))
    await FallingEdge(dut.clk)
    dut.inp_bit.value <= 1
    await RisingEdge(dut.clk)
    #print("Inp_bit : ",int(dut.inp_bit)," seq_seen : ",int(dut.seq_seen))
    await FallingEdge(dut.clk)
    dut.inp_bit.value <= 0
    await RisingEdge(dut.clk)
    #print("Inp_bit : ",int(dut.inp_bit)," seq_seen : ",int(dut.seq_seen))
    await FallingEdge(dut.clk)
    dut.inp_bit.value <= 1
    await RisingEdge(dut.clk)
    #print("Inp_bit : ",int(dut.inp_bit)," seq_seen : ",int(dut.seq_seen))
    await FallingEdge(dut.clk)
    dut.inp_bit.value <= 1
    await RisingEdge(dut.clk)
    #print("Inp_bit : ",int(dut.inp_bit)," seq_seen : ",int(dut.seq_seen))