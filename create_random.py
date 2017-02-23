import csv
import random
import string

class randomWriter:
    """ Creates random boys and girls """

    def makeBoys():
        with open('boys.csv', 'w') as csvfile:
            fieldnames = ['name', 'attractiveness', 'intelligence', 'budget', 'is_committed', 'b_type']
            bwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
            bwriter.writeheader()
            b_type_choices = ['miser', 'generous', 'geeks']
            for i in range(10):
                temp_obj = {
                    'name': random.choice(string.ascii_uppercase) + ''.join(random.choice(string.ascii_lowercase) for _ in range(5)),
                    'attractiveness': random.randint(0,100),
                    'intelligence': random.randint(0,100),
                    'budget': random.randint(0,100),
                    'b_type': random.choice(b_type_choices),
                    'is_committed': False
                }
                print(temp_obj)
                bwriter.writerow(temp_obj)

    def makeGirls():
        with open('girls.csv', 'w') as csvfile:
            fieldnames = ['name', 'attractiveness', 'intelligence', 'maintainance', 'is_committed', 'g_type', 'choose_type']
            gwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
            gwriter.writeheader()
            choose_type_choices = ['m_attr', 'm_gen', 'm_rich']
            g_type_choices = ['miser', 'generous', 'geeks']
            for i in range(20):
                temp_obj = {
                    'name': random.choice(string.ascii_uppercase) + ''.join(random.choice(string.ascii_lowercase) for _ in range(5)),
                    'attractiveness': random.randint(0,100),
                    'intelligence': random.randint(0,100),
                    'maintainance': random.randint(0,100),
                    'g_type': random.choice(g_type_choices),
                    'choose_type':random.choice(choose_type_choices),
                    'is_committed': False
                }
                print(temp_obj)
                gwriter.writerow(temp_obj)