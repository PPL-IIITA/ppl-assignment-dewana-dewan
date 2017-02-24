import csv
from all_boys_girls import *

class ReaderC:

    def __init__(self):
        pass

    def readT(self, char_desc):
        arrT = []
        if char_desc == 'b':
            the_file = csv.DictReader(open("./data/boys.csv"))            
            for tem in the_file:
                # print(tem['b_type'])
                if(tem['b_type'] == 'miser'):
                    temp_boy = BMiser(tem)
                if(tem['b_type'] == 'generous'):
                    temp_boy = BGenerous(tem)
                if(tem['b_type'] == 'geeks'):
                    temp_boy = BGeek(tem)
                arrT.append(temp_boy)
        
        elif char_desc == 'g':
            the_file = csv.DictReader(open("./data/girls.csv"))
            for tem in the_file:
                # print(tem['b_type'])
                if(tem['g_type'] == 'choosy'):
                    temp_girl = GChoosy(tem)
                if(tem['g_type'] == 'normal'):
                    temp_girl = GNormal(tem)
                if(tem['g_type'] == 'desperate'):
                    temp_girl = GDesperate(tem)
                arrT.append(temp_girl)
        return arrT