import csv

class Reader:

    def __init__(self):
        pass

    def readT(self, char_desc):
        if char_desc == 'b':
            the_file = csv.DictReader(open("./data/boys.csv"))
        elif char_desc == 'g':
            the_file = csv.DictReader(open("./data/girls.csv"))
        else:
            print('Invalid Character')
            return
            
        arrT = []
        for tem in the_file:
            arrT.append(tem)
        # self.boys_no = len(arrT)
        return arrT