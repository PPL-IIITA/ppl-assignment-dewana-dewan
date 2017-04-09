# This question hasn't been properly implementsed yet, kindly don't consder this

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
print('Please enter k:')
k = int(input())
for a_girl in arrG:
    newCPL, the_boy = cpm.jodi_bana(a_girl, arrB)
    if newCPL == None:
        continue
    arrCPL.append(newCPL)
    # function overloaded, passing 1 as a parameter here lets teh selection be random
    the_boy.gifter(a_girl, arrG_all, arrG_lux, 1, 1, k)
    a_girl.calc_happiness()
    the_boy.calc_happiness(a_girl)
    newCPL.calc_all(the_boy, a_girl)
    logger.log(newCPL.boy_name, newCPL.girl_name, newCPL.happiness, newCPL.compatibility)
