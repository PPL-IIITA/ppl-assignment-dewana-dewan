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

print('Please enter k:')
k = int(input())
l =len(arrCPL)
newCPL = None
print('The k least happiest couples (boy_name, girl_name, happiness, compatibility):\n')
for i in range(0, k):
    for j in range(0, l - 1 - i):
        if(arrCPL[j].happiness <= arrCPL[j + 1].happiness):
            temp = arrCPL[j]
            arrCPL[j] = arrCPL[j + 1]
            arrCPL[j + 1] = temp
    print(arrCPL[l - i - 1].boy_name, arrCPL[l - i - 1].girl_name, arrCPL[l - i - 1].happiness, arrCPL[l - i - 1].compatibility)
    # breaking up here
    the_girl, this_cant_boy = arrCPL[len(arrCPL) - 1].break_up(arrB, arrG)
    arrCPL.pop(l - i - 1)
    # trying to make a new couple here
    newCPL, the_boy = cpm.jodi_bana(the_girl, arrB, this_cant_boy)
    if newCPL == None:
        continue
    arrCPL.append(newCPL)