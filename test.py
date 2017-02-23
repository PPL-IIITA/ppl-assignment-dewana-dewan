# from create_random import randomWriter
import os
import sys

sys.path.append(os.path.abspath('./helper/'))

# print(sys.path)


# rWriter = randomWriter(10, 20)
# rWriter.makeBoys()
# rWriter.makeGirls()

####################

from reader import Reader

r1 = Reader()
arr = Reader().readT('b')
print(arr)