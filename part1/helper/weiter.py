import datetime
import csv
"""
contains all logger classes
"""

class write_couple:
    """
    initializes class that logs couple formation
    """
    def __init__(self):
        """
        initializes class that logs couples
        """
        pass
    
    def log(self, gname, bname, h=None, c=None):
        """
        
        log funciton 
        opens couples.csv and logs boy name, girlfriend name, couple's happiness and their compatibility
        along with a time stamp

        """
        with open('./data/couples.csv', 'a') as csvfile:
            logger = csv.writer(csvfile)
            logger.writerow([datetime.datetime.now().isoformat(), gname, bname, h, c])

class write_gift:
    """
    initializes class that logs gifting transactions
    """
    def __init__(self):
        """
        initializes class that logs all gifting transactions
        """
        pass
    
    def log(self, bname, gname, typ, price):
        """

        log function
        opens gifts_log.csv and logs a gift transactioin between a couple
        along with a time stamp
        
        """
        with open('./data/gifts_log.csv', 'a') as csvfile:
            logger = csv.writer(csvfile)
            strr = (bname + ' gifted ' + gname + ' a gift of type ' + typ + ' worth '  + str(price))
            logger.writerow([datetime.datetime.now().isoformat(), strr])
    
    def log_end(self):
        """
        
        extra function that puts and end string after change of couple
        along with time stamp
        
        """
        with open('./data/gifts_log.csv', 'a') as csvfile:
            logger = csv.writer(csvfile)
            strr= '*****************'
            logger.writerow([datetime.datetime.now().isoformat(), strr])