"""
This file contains classes of all types of boys and girls
"""
from math import log, exp
from weiter import write_gift

class BMiser:
    """
    Class of a Miser boy
    
    attributes:
    name, attractiveness, intelligence, budget, spent, min_attr, is_commited, to_commited, happiness

    """
    def __init__(self, obja):
        """

        Initializes a boy of type Miser

        and sets attributes appopriately

        """
        self.name = obja['name']
        self.attractiveness = int(obja['attractiveness'])
        self.intelligence = int(obja['intelligence'])
        self.budget = int(obja['budget'])
        self.spent = 0
        self.min_attr = int(obja['min_attr'])
        self.is_committed = obja['is_committed']
        self.to_commited = None       
        self.happiness = None

    def gifter(self, girl, arrGFT, arrL):
        """
        
        Contains logic for all gifting from the Miser boy to his girlfriend
        
        """
        i = 0
        lgr = write_gift()
        while (self.spent <= self.budget and self.spent <= girl.maintainance and i < len(arrGFT)):
            if(self.spent + arrGFT[i].price <= self.budget):
                self.spent += arrGFT[i].price
                girl.gift_received[arrGFT[i].name()].append(arrGFT[i])                
                lgr.log(self.name, girl.name, arrGFT[i].name(), arrGFT[i].price)
            i += 1
        lgr.log_end()
    
    def calc_happiness(self, g):
        """

        Calculates and sets happiness of boy
        
        """
        self.happiness = self.budget - self.spent


class BGenerous:
    """
    
    class of generous boy

    attributes:
    name, attractiveness, intelligence, budget, spent, min_attr, is_commited, to_commited, happiness

    """
    def __init__(self, obja):
        """

        Initializes a boy of type Generous

        and sets attributes appopriately
        
        """
        self.name = obja['name']
        self.attractiveness = int(obja['attractiveness'])
        self.intelligence = int(obja['intelligence'])
        self.budget = int(obja['budget'])
        self.spent = 0
        self.min_attr = int(obja['min_attr'])
        self.is_committed = obja['is_committed']
        self.to_commited = None       
        self.happiness = None
        
    def gifter(self, girl, arrGFT, arrL):
        """

        Contains logic for all gifting from Generous boy to his girlfriend

        """
        i = len(arrGFT) - 1
        lgr = write_gift()
        while (self.spent <= self.budget and i >=0):
            if(self.spent + arrGFT[i].price <= self.budget):
                self.spent += arrGFT[i].price
                girl.gift_received[arrGFT[i].name()].append(arrGFT[i])                
                lgr.log(self.name, girl.name, arrGFT[i].name(), arrGFT[i].price)
            i -= 1
        lgr.log_end()

    def calc_happiness(self, g):
        """
        
        Calculates and sets happiness of boy

        """
        self.happiness = g.happiness

class BGeek:
    """

    class of geek boy
    
    attributes:
    name, attractiveness, intelligence, budget, spent, min_attr, is_commited, to_commited, happiness

    """
    def __init__(self, obja):
        """

        Initializes a boy of type Geek

        and sets attributes appopriately

        """
        self.name = obja['name']
        self.attractiveness = int(obja['attractiveness'])
        self.intelligence = int(obja['intelligence'])
        self.budget = int(obja['budget'])
        self.spent = 0
        self.min_attr = int(obja['min_attr'])
        self.is_committed = obja['is_committed']
        self.to_commited = None       
        self.happiness = None

    def gifter(self, girl, arrGFT, arrL):
        """

        Contains logic for all gifting from Geek boy to his girlfriend
        
        """
        i = 0
        flg = 0
        lgr = write_gift()
        while (self.spent <= self.budget and i < len(arrGFT)):
            if(self.spent + arrGFT[i].price <= self.budget):
                self.spent += arrGFT[i].price
                girl.gift_received[arrGFT[i].name()].append(arrGFT[i])                
                if(arrGFT[i].name() == 'gift_luxury'):
                    flg += 1
                lgr.log(self.name, girl.name,arrGFT[i].name(), arrGFT[i].price)
            i += 1
        
        if(len(arrL) != 0):
            if(self.spent + arrL[0].price <= self.budget and flg == 0):
                self.spent += arrL[0].price
                girl.gift_received[arrL[0].name()].append(arrL[0])                

        lgr.log_end()
        
    def calc_happiness(self, g):
        """

        Calculates and sets happiness of boy
        
        """
        self.happiness = g.intelligence

class GChoosy:
    """
    
    Class of a Choosy girl

    attributes:
    name, attractiveness, intelligence, maintainance, is_commited, to_commited, happiness, choose_type, gifts_recieved 
    
    """
    def __init__(self, obja):
        """
    
        Initializes a Girl of type Choosy
    
        """
        self.name = obja['name']
        self.attractiveness = int(obja['attractiveness'])
        self.intelligence = int(obja['intelligence'])
        self.maintainance = int(obja['maintainance'])
        self.is_committed = obja['is_committed']
        self.choose_type = obja['choose_type']
        self.gift_received = {
            'gift_luxury':[],
            'gift_essential':[],
            'gift_utility':[]
        }
        self.happiness = None
        self.to_commited = None
    
    def calc_happiness(self):
        """
        
        Calculates and sets happiness of girl using appropriate logic
        
        """
        mapp = ['gift_essential', 'gift_luxury', 'gift_utility']
        self.happiness = 0
        for i in range(3):
            if(i == 1):
                fct = 2
            else:
                fct = 1
            for gft in self.gift_received[mapp[i]]:
                # print(self.happiness)
                self.happiness += (gft.price * fct)
                # print(gft.price, self.happiness)
        if(self.happiness > 0):
            self.happiness = log(self.happiness)
        else:
            self.happiness = 0

class GNormal:
    """
    
    Class of a normal girl
    
    attributes:
    name, attractiveness, intelligence, maintainance, is_commited, to_commited, happiness, choose_type, gifts_recieved 
    
    """
    def __init__(self, obja):
        """
        Initializes a Girl of type Normal
        """
        self.name = obja['name']
        self.attractiveness = int(obja['attractiveness'])
        self.intelligence = int(obja['intelligence'])
        self.maintainance = int(obja['maintainance'])
        self.is_committed = obja['is_committed']
        self.choose_type = obja['choose_type']
        self.gift_received = {
            'gift_luxury':[],
            'gift_essential':[],
            'gift_utility':[]
        }        
        self.happiness = None
        self.to_commited = None       

    def calc_happiness(self):
        """

        Calculates and sets happiness of girl using appropriate logic

        """
        mapp = ['gift_essential', 'gift_luxury', 'gift_utility']
        self.happiness = 0
        for i in range(3):
            for gft in self.gift_received[mapp[i]]:
                self.happiness += gft.price
                self.happiness += gft.value


class GDesperate:
    """

    Class of a desperate girl

    attributes:
    name, attractiveness, intelligence, maintainance, is_commited, to_commited, happiness, choose_type, gifts_recieved 
    
    """
    def __init__(self, obja):
        """
    
        Initializes a Girl of type Desperate
    
        """
        self.name = obja['name']
        self.attractiveness = int(obja['attractiveness'])
        self.intelligence = int(obja['intelligence'])
        self.maintainance = int(obja['maintainance'])
        self.is_committed = obja['is_committed']
        self.choose_type = obja['choose_type']
        self.gift_received = {
            'gift_luxury':[],
            'gift_essential':[],
            'gift_utility':[]
        }        
        self.happiness = None
        self.to_commited = None       
        
    def calc_happiness(self):
        """
    
        Calculates and sets happiness of girl using appropriate logic
    
        """
        mapp = ['gift_essential', 'gift_luxury', 'gift_utility']
        self.happiness = 0
        for i in range(3):
            for gft in self.gift_received[mapp[i]]:
                self.happiness += gft.price
        self.happiness = exp(self.happiness)