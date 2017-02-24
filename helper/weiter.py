import datetime
import csv

class write_couple:
    def __init__(self):
        pass
    
    def log(self, gname, bname):
        with open('./data/couples.csv', 'a') as csvfile:
            logger = csv.writer(csvfile)
            logger.writerow([datetime.datetime.now().isoformat(), gname, bname])