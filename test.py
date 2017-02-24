
import os
import sys
import csv

sys.path.append(os.path.abspath('./helper/'))

# print(sys.path)
from creater import randomWriter
from reader import ReaderC

rWriter = randomWriter(10, 20)
rWriter.makeBoys()
rWriter.makeGirls()

####################


r1 = ReaderC()
arr = r1.readT('b')
print(arr)