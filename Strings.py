#String manipulation
import tkinter
from tkinter import ttk
import Popup

def reverseString(text):
	return text[::-1]

p1 = Popup.Popup("Reverse the string",reverseString)