import os
import sys
sys.path.append(os.path.abspath('./helper/'))
from reader import ReaderC
from couple import couple_maker
from weiter import write_couple

rdr = ReaderC()
arrB = rdr.readT('b')
arrG = rdr.readT('g')
arrG_all, arrG_ess, arrG_lux = rdr.readGFT()


cpm = couple_maker()
logger = write_couple()

arrCPL = []
for i in range(len(arrG) + len(arrB)):
    if(i % 2 == 0):
        newCPL, the_boy, the_girl = cpm.girl_choose(i, arrG, arrB)
    else:
        newCPL, the_boy, the_girl = cpm.boy_choose(i, arrG, arrB)
    if(newCPL == None):
        continue
    arrCPL.append(newCPL)
    the_boy.gifter(the_girl, arrG_all, arrG_lux)
    the_girl.calc_happiness()
    the_boy.calc_happiness(the_girl)
    newCPL.calc_all(the_boy, the_girl)
    logger.log(newCPL.boy_name, newCPL.girl_name, newCPL.happiness, newCPL.compatibility)