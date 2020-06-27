import Popup
import clsPerson

def initPerson(commaList):
	data = commaList.split(",")
	per1 = clsPerson.clsPerson(data[0],data[1],data[2],data[3])

	return "Name: {} \n Birthday: {} \n Profession: {}".format(per1.getFirstName() + " " + per1.getLastName(),per1.getBirthday(),per1.getProfession())

p1 = Popup.Popup("Enter firstname,lastname,birthday,profession",initPerson,"word")