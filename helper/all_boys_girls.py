class BMiser:
    def __init__(self, obja):
        self.name = obja['name']
        self.attractiveness = int(obja['attractiveness'])
        self.intelligence = int(obja['intelligence'])
        self.budget = int(obja['budget'])
        self.spent = 0
        self.min_attr = int(obja['min_attr'])
        self.is_committed = obja['is_committed']
        self.to_commited = None       
        self.happiness = None

class BGenerous:
    def __init__(self, obja):
        self.name = obja['name']
        self.attractiveness = int(obja['attractiveness'])
        self.intelligence = int(obja['intelligence'])
        self.budget = int(obja['budget'])
        self.spent = 0
        self.min_attr = int(obja['min_attr'])
        self.is_committed = obja['is_committed']
        self.to_commited = None       
        self.happiness = None
        

class BGeek:
    def __init__(self, obja):
        self.name = obja['name']
        self.attractiveness = int(obja['attractiveness'])
        self.intelligence = int(obja['intelligence'])
        self.budget = int(obja['budget'])
        self.spent = 0
        self.min_attr = int(obja['min_attr'])
        self.is_committed = obja['is_committed']
        self.to_commited = None       
        self.happiness = None
        
class GChoosy:
    def __init__(self, obja):
        self.name = obja['name']
        self.attractiveness = int(obja['attractiveness'])
        self.intelligence = int(obja['intelligence'])
        self.maintainance = int(obja['maintainance'])
        self.is_committed = obja['is_committed']
        self.choose_type = obja['choose_type']
        self.gift_received = None
        self.happiness = None
        self.to_commited = None       

class GNormal:
    def __init__(self, obja):
        self.name = obja['name']
        self.attractiveness = int(obja['attractiveness'])
        self.intelligence = int(obja['intelligence'])
        self.maintainance = int(obja['maintainance'])
        self.is_committed = obja['is_committed']
        self.choose_type = obja['choose_type']
        self.gift_received = None
        self.happiness = None
        self.to_commited = None       

class GDesperate:
    def __init__(self, obja):
        self.name = obja['name']
        self.attractiveness = int(obja['attractiveness'])
        self.intelligence = int(obja['intelligence'])
        self.maintainance = int(obja['maintainance'])
        self.is_committed = obja['is_committed']
        self.choose_type = obja['choose_type']
        self.gift_received = None 
        self.happiness = None
        self.to_commited = None       
        