from operator import attrgetter

class allocator:
	def opt1(self, arrB, arrCPL):
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
		# first sort
		arrCPL.sort(key=attrgetter('boy_name'))
		for boy in arrB:
			if(not self.binarySearch(arrCPL, boy)):
				print(boy, ' is not commited')

	def opt3(self, arrB, arrCPL):
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