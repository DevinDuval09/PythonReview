class clsPerson:

	def __init__(self,firstname,lastname,birthday,profession):
		self.person = (firstname,lastname,birthday,profession)

	def getFirstName(self):
		return self.person[0]

	def getLastName(self):
		return self.person[1]

	def getBirthday(self):
		return self.person[2]

	def getProfession(self):
		return self.person[3]

	def addInformation(tuple):
		self = self.person[0:len(person)] + tuple
