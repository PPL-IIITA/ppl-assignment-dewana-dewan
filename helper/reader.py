import csv
from all_boys_girls import *
from all_gifts import *

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
    
    def readGFT(self):
        arrG_all = []
        arrG_ess = []
        arrG_lux = []
        the_file = csv.DictReader(open("./data/gifts.csv"))
        for tem in the_file:
            # print(tem)
            if(tem['type'] == 'essential'):
                new_gft = gift_essential(tem['value'], tem['price'])
                print(tem['value'], tem['price'])
                arrG_ess.append(new_gft)
            elif(tem['type'] == 'luxury'):
                new_gft = gift_luxury(tem['value'], tem['price'], tem['luxury_rating'], tem['difficulty'])
                arrG_lux.append(new_gft)
            elif(tem['type'] == 'utility'):
                new_gft = gift_utility(tem['value'], tem['price'], tem['utility_value'], tem['utility_class'])
            arrG_all.append(new_gft)
        
        return self.__sort(arrG_all), self.__sort(arrG_ess), self.__sort(arrG_lux)
    
    def __sort(self, arr):
        for i in range(len(arr) - 1):
            for j in range(len(arr) - 1 - i):
                if(arr[j].price >= arr[j + 1].price):
                    temp = arr[j]
                    arr[j] = arr[j + 1]
                    arr[j + 1] = temp
        return arr