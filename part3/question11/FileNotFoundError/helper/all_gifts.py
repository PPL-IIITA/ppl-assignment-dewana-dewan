"""
Contains classes of all kinds of gifts
"""
class gift:
	"""

	base class for all gifts, contains only price and value

	"""
	def __init__(self, value, price):
		"""

		parent class(gift) constructor
		sets only price and value

		"""
		self.price = int(price) # int
		self.value = int(value) # int

	def name(self):
		"""

		returns name of gift(useful in implementing gifting)
		
		"""
		return self.__class__.__name__

class gift_essential(gift):
	"""

	class of a utility gift, derived from gift class
	
	"""
	pass		

class gift_utility(gift):
	"""

	class of a utility gift, derived from gift class
	
	"""
	def __init__(self, value, price, utility_value, utility_class) :
		"""
		Initializes class of an utility gift

		attributes:
		price, value, utility_value, utility_class

		returns object of an utility gift

		"""
		super().__init__(value, price)
		self.utility_value = int(utility_value) # int
		self.utility_class = utility_class # string		

class gift_luxury(gift):
	"""

	class of a luxury gift, derived from gift class
	
	"""
	def __init__(self, value, price, luxury_rating, difficulty) :
		"""
		
		Initializes class of an luxury gift
		
		Attributes:
		value, price, luxury_rating, difficulty

		returns a luxury gift object
		"""
		super().__init__(value, price)
		self.luxury_rating = int(luxury_rating) # int
		self.difficulty = int(difficulty) # int