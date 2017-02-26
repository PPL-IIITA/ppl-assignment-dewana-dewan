"""
Contains classes of all kinds of gifts
"""
class gift_essential :

	def __init__(self, valu, pric) :
		"""

		Initializes class of an essential gift
		
		attributes:
		price, value

		returns object of an essential gift

		"""
		self.price = int(pric) # int
		self.value = int(valu)
		pass
	def name(self):
		"""

		returns name of gift(useful in implementing gifting)

		"""
		return self.__class__.__name__
		

class gift_utility :
	def __init__(self, value, price, utility_value, utility_class) :
		"""
		Initializes class of an utility gift

		attributes:
		price, value, utility_value, utility_class

		returns object of an utility gift

		"""
		self.utility_value = int(utility_value) # int
		self.utility_class = utility_class # string
		self.price = int(price) # int
		self.value = int(value) # int
	
	def name(self):
		"""
		returns name of gift(useful in implementing gifting)
		"""
		return self.__class__.__name__
		

class gift_luxury :
	def __init__(self, value, price, luxury_rating, difficulty) :
		"""
		
		Initializes class of an luxury gift
		
		Attributes:
		value, price, luxury_rating, difficulty

		returns a luxury gift object
		"""
		self.luxury_rating = int(luxury_rating) # int
		self.difficulty = int(difficulty) # int
		self.price = int(price) # int
		self.value = int(value) # int
	
	def name(self):
		"""
		returns name of gift(useful in implementing gifting)
		"""
		return self.__class__.__name__	