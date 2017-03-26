
import os
import sys
import csv

sys.path.append(os.path.abspath('./helper/'))

from creater import randomWriter
from reader import ReaderC

print("Enter number of boys:")
b = input()
print("Enter number of girls:")
g = input()
print("Enter number of gifts:")
gft = input()

rWriter = randomWriter(int(b), int(g), int(gft))

rWriter.makeBoys()
rWriter.makeGirls()
rWriter.makeGifts()
