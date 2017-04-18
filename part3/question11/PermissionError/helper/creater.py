import csv
import sys
import random
import string
"""
Contains class randomWriter
Creates random gifts, boys and girls

"""

class randomWriter:
    """ Creates random boys and girls """

    def __init__(self, no_boys, no_girls, no_gifts):
        """
        initializes a randomwriter
        sets number of boys, girls and gifts
        """
        self.boys_no = no_boys
        self.girls_no = no_girls
        self.gift_no = no_gifts

    def makeBoys(self):
        """

        this function creates random boys and places them in boys.csv
        
        """
        try:
            with open('./data/boys.csv', 'w') as csvfile:
                fieldnames = ['name', 'attractiveness', 'min_attr', 'intelligence', 'budget', 'is_committed', 'b_type']
                bwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
                bwriter.writeheader()
                b_type_choices = ['miser', 'generous', 'geeks']
                for i in range(self.boys_no):
                    temp_obj = {
                        'name': random.choice(string.ascii_uppercase) + ''.join(random.choice(string.ascii_lowercase) for _ in range(5)),
                        'attractiveness': random.randint(0,100),
                        'min_attr': random.randint(0,50),
                        'intelligence': random.randint(0,100),
                        'budget': random.randint(0,100),
                        'b_type': random.choice(b_type_choices),
                        'is_committed': False
                    }
                    print(temp_obj)
                    bwriter.writerow(temp_obj)
        except PermissionError:
            print("Exiting -- You don't have apt. permissions")
            sys.exit()

    def makeGirls(self):
        """
        
        this function creates random girls and places them in girls.csv
        
        """
        try:
            with open('./data/girls.csv', 'w') as csvfile:
                fieldnames = ['name', 'attractiveness', 'intelligence', 'maintainance', 'is_committed', 'g_type', 'choose_type']
                gwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
                gwriter.writeheader()
                choose_type_choices = ['m_attr', 'm_gen', 'm_rich']
                g_type_choices = ['choosy', 'normal', 'desperate']
                for i in range(self.girls_no):
                    temp_obj = {
                        'name': random.choice(string.ascii_uppercase) + ''.join(random.choice(string.ascii_lowercase) for _ in range(5)),
                        'attractiveness': random.randint(0,100),
                        'intelligence': random.randint(0,100),
                        'maintainance': random.randint(0,50),
                        'g_type': random.choice(g_type_choices),
                        'choose_type':random.choice(choose_type_choices),
                        'is_committed': False
                    }
                    print(temp_obj)
                    gwriter.writerow(temp_obj)
        except PermissionError:
            print("Exiting -- You don't have apt. permissions")
            sys.exit()

    def makeGifts(self):
        """
        
        this function creates random gifts and places them in gifts.csv
        
        """
        try:
            with open('./data/gifts.csv', 'w') as csvfile:
                fieldnames = ['type', 'value', 'price', 'utility_value', 'utility_class', 'luxury_rating', 'difficulty']
                gftwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
                gftwriter.writeheader()
                for i in range(0, self.gift_no):
                    decd = random.randint(0, 10)
                    if(decd <= 4):
                        # make essential gift
                        temp_obj = {
                            'type': 'essential', 
                            'value': random.randint(0,20), 
                            'price': random.randint(5,20), 
                            'utility_value': None, 
                            'utility_class': None, 
                            'luxury_rating': None, 
                            'difficulty': None
                        }
                    elif(decd > 4 and decd <=8 ):
                        temp_obj = {
                            'type': 'utility', 
                            'value': random.randint(0,20), 
                            'price': random.randint(5,20), 
                            'utility_value': random.randint(0,10), 
                            'utility_class': random.randint(0,10), 
                            'luxury_rating': None, 
                            'difficulty': None
                        }
                    else:
                        temp_obj = {
                            'type': 'luxury', 
                            'value': random.randint(10,40), 
                            'price': random.randint(10,40), 
                            'utility_value': None, 
                            'utility_class': None, 
                            'luxury_rating':random.randint(0,10), 
                            'difficulty':random.randint(0,10)
                        }
                    print(temp_obj)
                    gftwriter.writerow(temp_obj)
        except PermissionError:
            print("Exiting -- You don't have apt. permissions")
            sys.exit()
