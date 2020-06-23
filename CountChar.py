import Popup

def countchar(text):
	text = text.lower()
	dict = {}
	for l in text:
		if l in dict:
			dict[l]=dict[l]+1
		else:
			dict[l]=1

	cnt =""
	for l in dict:
		cnt =cnt + "\n" + l + " : " + str(dict[l])
		
	return cnt



p1 = Popup.Popup("Enter a word:",countchar,"word")
