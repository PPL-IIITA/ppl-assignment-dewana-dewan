class gift_essential :
	def __init__(self, valu, pric) :
		self.price = int(pric) # int
		self.value = int(valu)
		pass
	def name(self):
		return self.__class__.__name__
		

class gift_utility :
	def __init__(self, value, price, utility_value, utility_class) :
		self.utility_value = int(utility_value) # int
		self.utility_class = utility_class # string
		self.price = int(price) # int
		self.value = int(value) # int
	
	def name(self):
		return self.__class__.__name__
		

class gift_luxury :
	def __init__(self, value, price, luxury_rating, difficulty) :
		self.luxury_rating = int(luxury_rating) # int
		self.difficulty = int(difficulty) # int
		self.price = int(price) # int
		self.value = int(value) # int
	
	def name(self):
		return self.__class__.__name__	