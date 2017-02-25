import datetime
import csv

class write_couple:
    def __init__(self):
        pass
    
    def log(self, gname, bname):
        with open('./data/couples.csv', 'a') as csvfile:
            logger = csv.writer(csvfile)
            logger.writerow([datetime.datetime.now().isoformat(), gname, bname])

class write_gift:
    def __init__(self):
        pass
    
    def log(self, bname, gname, typ, price):
        with open('./data/gifts_log.csv', 'a') as csvfile:
            logger = csv.writer(csvfile)
            strr = (bname + ' gifted ' + gname + ' a gift of type ' + typ + ' worth '  + str(price))
            logger.writerow([datetime.datetime.now().isoformat(), strr])
    
    def log_end(self):
        with open('./data/gifts_log.csv', 'a') as csvfile:
            logger = csv.writer(csvfile)
            strr= '*****************'
            logger.writerow([datetime.datetime.now().isoformat(), strr])