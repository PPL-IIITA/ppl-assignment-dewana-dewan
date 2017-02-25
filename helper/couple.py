from math import fabs

class couple :
	def __init__(self, bname, gname) :
		self.boy_name = bname # string
		self.girl_name = gname # string
		self.happiness = None # int
		self.compatibility = None # int
		pass
	def happiness_calculator (self, boy, girl) :
		# returns 
		pass
	def compatibility_calculator (self, boy) :
		# returns 
		pass

	def calc_all(self, b, g):
		# print(b.happiness, g.happiness)
		self.happiness = b.happiness + g.happiness
		self.compatibility = fabs(b.budget - g.maintainance) + fabs(g.attractiveness - b.attractiveness) + fabs(g.intelligence - b.intelligence)


class couple_maker :
	def __init__(self) :
		pass

	# 3 cases
	# most attr, most rich, most intelligent
	# maybe a function for each will do
	def jodi_bana (self, girl, single_boy_collection):
		# print(girl.name, girl.choose_type)
		if(girl.choose_type == 'm_attr'):
			temp_boy = self.__find_apt(girl, self.__sortby('attractiveness', single_boy_collection))
		elif(girl.choose_type == 'm_gen'):
			temp_boy = self.__find_apt(girl, self.__sortby('intelligence', single_boy_collection))
		elif(girl.choose_type == 'm_rich'):
			temp_boy = self.__find_apt(girl, self.__sortby('budget', single_boy_collection)) 
		# print(temp_boy)
		if(temp_boy == None):
			print('No match found for ', girl.name)
			return None, None
		
		new_couple = couple(temp_boy.name, girl.name)
		# print(temp_boy.name, girl.name)
		girl.is_committed = 'True'
		temp_boy.is_committed = 'True'
		return new_couple, temp_boy

	
	def __find_apt(self, girl, single_boy_collection):
		# for i in range(0, len(single_boy_collection)):
			# print(single_boy_collection[i].name, single_boy_collection[i].attractiveness)
		for a_boy in single_boy_collection:
			# print(a_boy.name, a_boy.budget,' => ', girl.maintainance, girl.attractiveness, ' >= ', a_boy.min_attr)
			# print(bool(a_boy.is_committed) == False, a_boy.budget >= girl.maintainance, girl.attractiveness >= a_boy.min_attr)
			# print(type(a_boy.is_committed), type(a_boy.budget), type(girl.maintainance), girl.attractiveness >= a_boy.min_attr)
			if(a_boy.is_committed == 'False' and (a_boy.budget >= girl.maintainance) and (girl.attractiveness >= a_boy.min_attr)):
				return a_boy

	
	def __sortby(self, parm, coll):
		maxx = len(coll)
		t_coll = coll
		for i in range(0, maxx ):
			for j in range(0, maxx - 1):
				if(getattr(t_coll[j], parm) >= getattr(t_coll[j + 1], parm) ):
					temp = t_coll[j]
					t_coll[j] = t_coll[j + 1]
					t_coll[j + 1] = temp
		return t_coll
	

