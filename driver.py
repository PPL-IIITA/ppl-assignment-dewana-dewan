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
print('The k happiest couples:')
for i in range(0, k):
    for j in range(0, len(arrCPL) - 1):
        if(arrCPL[j].happiness >= arrCPL[j + 1].happiness):
            temp = arrCPL[j]
            arrCPL[j] = arrCPL[j + 1]
            arrCPL[j + 1] = temp
    print(arrCPL[l - i - 1].boy_name, arrCPL[l - i - 1].girl_name, arrCPL[l - i - 1].happiness, arrCPL[l - i - 1].compatibility)

print('The k compatible couples:')
for i in range(0, k):
    for j in range(0, len(arrCPL) - 1):
        if(arrCPL[j].compatibility >= arrCPL[j + 1].compatibility):
            temp = arrCPL[j]
            arrCPL[j] = arrCPL[j + 1]
            arrCPL[j + 1] = temp
    print(arrCPL[l - i - 1].boy_name, arrCPL[l - i - 1].girl_name, arrCPL[l - i - 1].happiness, arrCPL[l - i - 1].compatibility)
