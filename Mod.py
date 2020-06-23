import Popup

#function to pass into popup
def func(x):
	return (x % 2)

p1 = Popup.Popup("Shows modulus of number divided by 2.",func,"number")