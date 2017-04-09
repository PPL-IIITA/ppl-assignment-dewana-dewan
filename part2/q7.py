import os
import sys
from operator import attrgetter
sys.path.append(os.path.abspath('./helper/'))
from reader import ReaderC
from couple import couple_maker
from weiter import write_couple
from utils import allocator

rdr = ReaderC()
arrB = rdr.readT('b')
arrG = rdr.readT('g')
arrG_all, arrG_ess, arrG_lux = rdr.readGFT()


cpm = couple_maker()
logger = write_couple()

arrCPL = []
arrb = []
for a_girl in arrG:
    newCPL, the_boy = cpm.jodi_bana(a_girl, arrB)
    if newCPL == None:
        continue
    arrCPL.append(newCPL)
    the_boy.gifter(a_girl, arrG_all, arrG_lux)
    a_girl.calc_happiness()
    the_boy.calc_happiness(a_girl)
    newCPL.calc_all(the_boy, a_girl)
    logger.log(newCPL.boy_name, newCPL.girl_name, newCPL.happiness, newCPL.compatibility)

for boy in arrB:
	arrb.append(boy.name)

print('\nEnter desired choice:\n\t1. array(default)\n\t2. sorted array(binray search)\n\t3. hash table')
k=int(input())
alctr = allocator()
if (k == 2):
	alctr.opt2(arrb, arrCPL)
elif(k == 3):
	alctr.opt3(arrb, arrCPL)
else:
	alctr.opt1(arrb, arrCPL)