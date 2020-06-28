class clsPerson:

	def __init__(self,firstname,lastname,phoneNumber,email):
		self.person = (firstname,lastname,phoneNumber,email)
		self.workExp= ()

	def getFirstName(self):
		return self.person[0]

	def getLastName(self):
		return self.person[1]

	def getPhoneNumber(self):
		return self.person[2]

	def getEmail(self):
		return self.person[3]

	def addWorkExp(self,jobtitle,company,sDate,eDate):
		self.workExp = self.workExp + (jobtitle,company,sDate,eDate)

	def createResume(self):
		resume = "{}\n Phone: {}\n Email: {}\n".format(self.person[0] + self.person[1],self.person[2],self.person[3])
		for x in range(0,len(self.workExp),4):
			resume = resume + "\nTitle: {}\nCompany: {}\nFrom: {} to {}\n".format(self.workExp[x],self.workExp[x+1],self.workExp[x+2],self.workExp[x+3])
		return resume

