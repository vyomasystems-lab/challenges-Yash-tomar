# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
import random

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""
    cocotb.log.info('##### CTB: Inside test_mux testcase ########')

    ##assign input 
    dut.inp0 = random.randint(0, 3)
    dut.inp1 = random.randint(0, 3)
    dut.inp2 = random.randint(0, 3)
    dut.inp3 = random.randint(0, 3)
    dut.inp4.value = random.randint(0, 3)
    dut.inp5.value = random.randint(0, 3)
    dut.inp6.value = random.randint(0, 3)
    dut.inp7.value = random.randint(0, 3)
    dut.inp8.value = random.randint(0, 3)
    dut.inp9.value = random.randint(0, 3)
    dut.inp10.value = random.randint(0, 3)

    #dut.sel.value = $random%32
    dut.sel.value = 5

    yield Timer(1,'ns')

    assert dut.out.value ==dut.inp5.value "Randomize test failed"     