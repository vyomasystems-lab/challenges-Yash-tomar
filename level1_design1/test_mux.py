# See LICENSE.vyoma for details

import cocotb
#import numpy as np
from cocotb.triggers import Timer
#from numpy 
import random


@cocotb.test()
async def basic_test_mux(dut):
    """Test for mux2"""
    cocotb.log.info('##### CTB: Inside test_mux testcase ########')

    i5 = 2;
    dut.inp5.value = i5;
    dut.sel.value = 5

    await Timer(1,'ns')
   
    assert dut.out.value == i5, "Randomize test failed {OUT} != {I5}, Expected value : {EXP}".format(OUT = int(dut.out.value),I5 = int(dut.inp5.value), EXP = i5)      


@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""
    cocotb.log.info('##### CTB: Inside test_mux testcase 2 ########')

    x=[]
    #x=np.random.randint(4, size=(32))
    for t in range(0,32):
        x.append( random.randint(0,3))

    print("X:",x)

    ##assign input 
    dut.inp0.value = x[0]
    dut.inp1.value = x[1]
    dut.inp2.value = x[2]
    dut.inp3.value = x[3]
    dut.inp4.value = x[4]
    dut.inp5.value = x[5]
    dut.inp6.value = x[6]
    dut.inp7.value = x[7]
    dut.inp8.value = x[8]
    dut.inp9.value = x[9]
    dut.inp10.value =x[10]
    dut.inp11.value =x[11]
    dut.inp12.value =x[12]
    dut.inp13.value =x[13]
    dut.inp14.value =x[14]
    dut.inp15.value =x[15]
    dut.inp16.value =x[16]
    dut.inp17.value =x[17]
    dut.inp18.value =x[18]
    dut.inp19.value =x[19]
    dut.inp20.value =x[20]
    dut.inp21.value =x[21]
    dut.inp22.value =x[22]
    dut.inp23.value =x[23]
    dut.inp24.value =x[24]
    dut.inp25.value =x[25]
    dut.inp26.value =x[26]
    dut.inp27.value =x[27]
    dut.inp28.value =x[28]
    dut.inp29.value =x[29]
    dut.inp30.value =x[30]
    
    for i in range(0,32):
            dut.sel.value = i
            await Timer(1,'ns')
            assert dut.out.value == (x[i]), "Randomize test failed {OUT}, sel:{SEL} , Expected value : {EXP}".format(OUT = int(dut.out.value), SEL=int(dut.sel.value),EXP = x[i])  
