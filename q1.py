import os
import sys
sys.path.append(os.path.abspath('./helper/'))
from reader import ReaderC
from couple import couple_maker
from weiter import write_couple

rdr = ReaderC()
arrB = rdr.readT('b')
arrG = rdr.readT('g')

cpm = couple_maker()
logger = write_couple()

arrCPL = []
for a_girl in arrG:
    newCPL, the_boy = cpm.jodi_bana(a_girl, arrB)
    if newCPL != None:
        arrCPL.append(newCPL)
        print(newCPL.boy_name,' ==> ', newCPL.girl_name)
        logger.log(newCPL.boy_name, newCPL.girl_name)

# Result of Q1 is in ./data/couples.csv