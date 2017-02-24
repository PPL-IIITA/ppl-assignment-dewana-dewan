import os
import sys

sys.path.append(os.path.abspath('./helper/'))

from reader import ReaderC
from couple import couple_maker
from weiter import write_couple

rdr = ReaderC()
arrB = rdr.readT('b')
# print(arrB)
arrG = rdr.readT('g')
# print(arrG)
arrG_all, arrG_ess, arrG_lux = rdr.readGFT()
print(arrG_all)


cpm = couple_maker()
logger = write_couple()

arrCPL = []
for a_girl in arrG:
    newCPL = cpm.jodi_bana(a_girl, arrB)
    if newCPL == None:
        continue
    arrCPL.append(newCPL)
    logger.log(newCPL.boy_name, newCPL.girl_name)
    print(newCPL.boy_name, newCPL.girl_name)