
import os
import sys
import csv

sys.path.append(os.path.abspath('./helper/'))

# print(sys.path)
from creater import randomWriter
from reader import ReaderC

rWriter = randomWriter(20, 10, 10)
rWriter.makeBoys()
rWriter.makeGirls()
rWriter.makeGifts()

####################
