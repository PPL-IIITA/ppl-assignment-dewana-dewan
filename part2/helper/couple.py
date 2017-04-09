from math import fabs
"""
has class "couple" and "couple_maker"
"""

class couple :
	"""
	
	Class couple

	attributes:
	boy name, girl name, happiness and compatibily
	
	methods:
	__init__
	calc_all

	"""
	def __init__(self, bname, gname) :
		"""
		
		initializes couple class, sets boy name and girl name and returns the object
		
		"""
		self.boy_name = bname # string
		self.girl_name = gname # string
		self.happiness = None # int
		self.compatibility = None # int
		pass

	def calc_all(self, b, g):
		"""
		
		calculates the happiness and compatibilty of a couple
		
		"""
		# print(b.happiness, g.happiness)
		self.happiness = b.happiness + g.happiness
		self.compatibility = fabs(b.budget - g.maintainance) + fabs(g.attractiveness - b.attractiveness) + fabs(g.intelligence - b.intelligence)

	def break_up(self, b_all, g_all):
		for a_boy in b_all:
			if a_boy.name == self.boy_name:
				the_boy = a_boy
				break
		for a_girl in g_all:
			if a_girl.name == self.girl_name:
				the_girl = a_girl
				break
		the_girl.is_committed = False
		the_girl.gifts_recieved = {
            'gift_luxury':[],
            'gift_essential':[],
            'gift_utility':[]
        }
		the_girl.happiness = None
		the_girl.to_commited = None
		the_boy.is_committed = False
		the_boy.to_commited = None
		the_boy.happiness = None
		the_boy.spent = 0
		return the_girl, the_boy


class couple_maker :
	"""

	Couple_maker class, this class makes couples
	
	"""
	def __init__(self) :
		"""
	
		initializes couple_maker class
	
		"""
		pass
	
	def girl_choose(self, i, arrG, arrB):
		i = int(i / 2)
		print(i, len(arrG), arrG[i].is_committed)
		if(i < len(arrG) and (arrG[i].is_committed == False)):
			pass
		else:
			return None, None, None
		newcpl = None
		newcpl, boy = self.jodi_bana(arrG[i], arrB)
		print('asdasda')
		return newcpl, boy, arrG[i]

	def boy_choose(self, i, arrG, arrB):
		i = int(i / 2)
		if(i < len(arrG) and (arrG[i].is_committed == False)):
			pass
		else:
			return None, None, None
		boy = arrB[i]
		newcpl = None
		for j in range(len(arrG)):
			if(arrG[j].is_committed == False and (boy.budget >= arrG[j].maintainance) and (arrG[j].attractiveness >= boy.min_attr)):
				newcpl = couple(boy.name, arrG[j].name)
				print('yeess')
		return newcpl, boy, arrG[j]


	def jodi_bana (self, girl, single_boy_collection, no_boy = None):
		"""	
		Containes logic to form couples

		-- >  3 cases(kind of girls)
		most attr, most rich, most intelligent
		
		sorts array of boys accordingly and selects a suitable boy(using find_apt function)

		retuns so formed couple and the chosen boy

		"""
		# print(girl.name, girl.choose_type)
		if(girl.choose_type == 'm_attr'):
			temp_boy = self.__find_apt(girl, self.__sortby('attractiveness', single_boy_collection), no_boy)
		elif(girl.choose_type == 'm_gen'):
			temp_boy = self.__find_apt(girl, self.__sortby('intelligence', single_boy_collection), no_boy)
		elif(girl.choose_type == 'm_rich'):
			temp_boy = self.__find_apt(girl, self.__sortby('budget', single_boy_collection), no_boy) 
		# print(temp_boy)
		if(temp_boy == None):
			print('No match found for ', girl.name)
			return None, None
		
		new_couple = couple(temp_boy.name, girl.name)
		# print(temp_boy.name, girl.name)
		girl.is_committed = 'True'
		temp_boy.is_committed = 'True'
		return new_couple, temp_boy

	
	def __find_apt(self, girl, single_boy_collection, no_boy = None):
		"""

		This function finds an appropriate boy for a girl 
		and returns the boy object
		
		"""
		# for i in range(0, len(single_boy_collection)):
			# print(single_boy_collection[i].name, single_boy_collection[i].attractiveness)
		for a_boy in single_boy_collection:
			# print(a_boy.name, a_boy.budget,' => ', girl.maintainance, girl.attractiveness, ' >= ', a_boy.min_attr)
			# print(bool(a_boy.is_committed) == False, a_boy.budget >= girl.maintainance, girl.attractiveness >= a_boy.min_attr)
			# print(type(a_boy.is_committed), type(a_boy.budget), type(girl.maintainance), girl.attractiveness >= a_boy.min_attr)
			if(no_boy != None):
				if(a_boy.is_committed == 'False' and (a_boy.budget >= girl.maintainance) and (girl.attractiveness >= a_boy.min_attr) and (a_boy.name != no_boy.name)):
					return a_boy
			else:
				if(a_boy.is_committed == 'False' and (a_boy.budget >= girl.maintainance) and (girl.attractiveness >= a_boy.min_attr)):
					return a_boy
	

	def __sortby(self, parm, coll):
		"""
		
		private
		helper function

		used in selecting an apropriate boy

		sorts the list of boys as per passed key
		
		"""
		maxx = len(coll)
		t_coll = coll
		for i in range(0, maxx ):
			for j in range(0, maxx - 1):
				if(getattr(t_coll[j], parm) >= getattr(t_coll[j + 1], parm) ):
					temp = t_coll[j]
					t_coll[j] = t_coll[j + 1]
					t_coll[j + 1] = temp
		return t_coll
	

