import Popup
import clsPerson
global per1
per1 = clsPerson


def createWorkHist(commaList):
	global per1
	data = commaList.split(",")
	per1.addWorkExp(data[0],data[1],data[2],data[3])
	return per1.createResume()

def initPerson(commaList):
	global per1
	data = commaList.split(",")
	per1 = clsPerson.clsPerson(data[0],data[1],data[2],data[3])
	p2 = Popup.Popup("Enter Job Title,company,start date,end date:",createWorkHist,"word")



p1 = Popup.Popup("Enter firstname,lastname,phone number,email",initPerson,"word")
