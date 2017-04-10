"""
This file contains classes of all types of boys and girls
"""
from math import log, exp
from weiter import write_gift
from utils import randm

class boy:
    """

    Parent class of all boys
    
    """
    def __init__(self, obja):
        """

        initializes a boy
        
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

class BMiser(boy):
    """
    Class of a Miser boy
    
    attributes:
    name, attractiveness, intelligence, budget, spent, min_attr, is_commited, to_commited, happiness

    """
    def gifter(self, girl, arrGFT, arrL, choice = 1, randomk = 0, k = 0):
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

        arrgft = []
        if(choice == 2):
            if(len(girl.gift_received['gift_luxury']) == 0 and len(arrL) != 0):
                self.spent += arrL[0].price
                girl.gift_received[arrL[0].name()].append(arrL[0])
            if(len(girl.gift_received['gift_essential']) == 0):
                for gft in arrGFT:
                    if gft.name() == 'gift_essential':
                        arrgft.append(gft)
                    gft = randm.select(arrgft)    
                    if(gft != None):
                        girl.gift_received[gft.name()].append(gft)
            if(len(girl.gift_received['gift_utility']) == 0):
                for gft in arrGFT:
                    if gft.name() == 'gift_utility':
                        arrgft.append(gft)
                    gft = randm.select(arrgft) 
                    if(gft != None):
                        girl.gift_received[gft.name()].append(gft)

        lgr.log_end()
    
    def calc_happiness(self, g):
        """

        Calculates and sets happiness of boy
        
        """
        self.happiness = self.budget - self.spent


class BGenerous(boy):
    """
    
    class of generous boy

    attributes:
    name, attractiveness, intelligence, budget, spent, min_attr, is_commited, to_commited, happiness

    """    
    def gifter(self, girl, arrGFT, arrL, choice = 1, randomk = 0, k = 0):
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

        arrgft = []
        if(choice == 2):
            if(len(girl.gift_received['gift_luxury']) == 0 and len(arrL) != 0):
                self.spent += arrL[0].price
                girl.gift_received[arrL[0].name()].append(arrL[0])
            if(len(girl.gift_received['gift_essential']) == 0):
                for gft in arrGFT:
                    if gft.name() == 'gift_essential':
                        arrgft.append(gft)
                    gft = randm.select(arrgft)    
                    if(gft != None):
                        girl.gift_received[gft.name()].append(gft)
            if(len(girl.gift_received['gift_utility']) == 0):
                for gft in arrGFT:
                    if gft.name() == 'gift_utility':
                        arrgft.append(gft)
                    gft = randm.select(arrgft)    
                    if(gft != None):
                        girl.gift_received[gft.name()].append(gft)

        lgr.log_end()

    def calc_happiness(self, g):
        """
        
        Calculates and sets happiness of boy

        """
        self.happiness = g.happiness

class BGeek(boy):
    """

    class of geek boy
    
    attributes:
    name, attractiveness, intelligence, budget, spent, min_attr, is_commited, to_commited, happiness

    """
    def gifter(self, girl, arrGFT, arrL, choice = 1, randomk = 0, k = 0):
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

        arrgft = []
        if(len(arrL) != 0):
            if(self.spent + arrL[0].price <= self.budget and flg == 0):
                self.spent += arrL[0].price
                girl.gift_received[arrL[0].name()].append(arrL[0])                

        if(choice == 2):
            if(len(girl.gift_received['gift_luxury']) == 0 and len(arrL) != 0):
                self.spent += arrL[0].price
                girl.gift_received[arrL[0].name()].append(arrL[0])
            if(len(girl.gift_received['gift_essential']) == 0):
                for gft in arrGFT:
                    if gft.name() == 'gift_essential':
                        arrgft.append(gft)
                    gft = randm.select(arrgft)    
                    if(gft != None):
                        girl.gift_received[gft.name()].append(gft)
            if(len(girl.gift_received['gift_utility']) == 0):
                for gft in arrGFT:
                    if gft.name() == 'gift_utility':
                        arrgft.append(gft)
                    gft = randm.select(arrgft)    
                    if(gft != None):
                        girl.gift_received[gft.name()].append(gft)

        lgr.log_end()
        
    def calc_happiness(self, g):
        """

        Calculates and sets happiness of boy
        
        """
        self.happiness = g.intelligence

class girl:
    """

    parent class of all girls

    """
    def __init__(self, obja):
        """
    
        Initializes a Girl
    
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

class GChoosy(girl):
    """
    
    Class of a Choosy girl

    attributes:
    name, attractiveness, intelligence, maintainance, is_commited, to_commited, happiness, choose_type, gifts_recieved 
    
    """    
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

class GNormal(girl):
    """
    
    Class of a normal girl
    
    attributes:
    name, attractiveness, intelligence, maintainance, is_commited, to_commited, happiness, choose_type, gifts_recieved 
    
    """
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


class GDesperate(girl):
    """

    Class of a desperate girl

    attributes:
    name, attractiveness, intelligence, maintainance, is_commited, to_commited, happiness, choose_type, gifts_recieved 
    
    """
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