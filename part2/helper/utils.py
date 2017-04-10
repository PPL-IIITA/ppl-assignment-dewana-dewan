from operator import attrgetter
import random

class allocator:
	"""
	Allocator class
	specifically for question 7,
	has implementations of array, sorted array(binary, search) and hash table
	"""
	def opt1(self, arrB, arrCPL):
		"""
		option 1:
		used for placing all the data in an array and do a linear search
		"""
		for boy in arrB:
			flag = 0
			for cpl in arrCPL:
				if(cpl.boy_name == boy):
					print(boy, ' found, is committed with ', cpl.girl_name)
					flag = 1
					break
			if(flag == 0):
				print(boy, ' is not commited')

	def opt2(self, arrB, arrCPL):
		"""
		option 2:
		used for sorting the array first, so that binary search can be applied
		"""
		# first sort
		arrCPL.sort(key=attrgetter('boy_name'))
		for boy in arrB:
			if(not self.binarySearch(arrCPL, boy)):
				print(boy, ' is not commited')

	def opt3(self, arrB, arrCPL):
		"""
		option 3:
		creates hash table with key boy name, for easy and fast access
		"""
		objCPL={}
		# create hash table
		for cpl in arrCPL:
			objCPL[cpl.boy_name] = cpl

		for boy in arrB:
			if(objCPL.get(boy, False)):
				print(boy, ' found, is committed with ', objCPL[boy].girl_name)
			else:
				print(boy, ' is not commited')


	def binarySearch(self, arrCPL, boy):
		'''
		Binary search funciton:

		Auxilary function for binary searching used along with option 2 described above
		'''
		'carries out binary search on the Couples list for searching girlfriend of a given boy'
		if (len(arrCPL) == 0):
			return False
		else:
			midpoint = len(arrCPL) // 2
			if (arrCPL[midpoint].boy_name == boy):
				print(boy, ' found, is committed with ', arrCPL[midpoint].girl_name)
				return True
			else:
				if (boy < arrCPL[midpoint].boy_name):
					return self.binarySearch(arrCPL[:midpoint], boy)
				else:
					return self.binarySearch(arrCPL[midpoint+1:], boy)

class randm:
	"""
	Random Class:

	specifically for question 10
	helps in selection of random elments
	"""
	def select(arr):
		"""
		funciton select

		takes in an array of suitable elemtns and randomly selects one of them
		used in gifting
		"""
		i = len(arr)
		if(i == 0):
			return None
		j = random.randint(0, i - 1)
		return arr[j]
