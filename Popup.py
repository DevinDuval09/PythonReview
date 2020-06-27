#generic dialogue box that will take input
import tkinter as tk
from tkinter import ttk as tkk

#make a popup box with an input button, output label, and quit button
#input: button function, instructions

class Popup():
	def __init__(self,instructions,press,datatype):
		x = 0
		self = tk.Tk()
		w = 400
		global h
		h = 200
		self.geometry("{}x{}".format(w,h))
		#label with instructions
		Instruct = tkk.Label(self,text=instructions,font=("Times Roman",12))
		Instruct.pack(side="top")
		#entry box
		Entry = tkk.Entry(self, cursor = "dot", textvariable = "StringVar")
		Entry.pack()
		#quite button
		Bquit=tkk.Button(self,text="Quit",command=quit)
		Bquit.pack(side="bottom")
		#output label
		lblOutput = tkk.Label(self,text="")

		#action button
		Baction=tkk.Button(self,text="Do instructions")
		Baction.pack()

		# id datatype
		def idDatatype():
			text = Entry.get()
			if text.isnumeric() or text.isdecimal():
				return "number"
			elif text.isprintable():
				return "word"
			else:
				return "mix"

		#function to write output label
		def writeout():
			#test datatype of input
			typ = ""
			if len(Entry.get()) > 0:
				typ = idDatatype()
			else:
				lblOutput.config(text="Enter a value")
			#if datatype is correct, do function
			if (datatype == "number"):
				try:
					x = press(float(Entry.get()))
					lblOutput.config(text=str(x))
				except:
					lblOutput.config(text="Please enter a number.")
			elif (typ == datatype) and (typ != "number"):
				x = press(Entry.get())
				lblOutput.config(text=x)
			else:
				lblOutput.config(text="Wrong datatype. Please enter a new value.")
			lblOutput.pack()
			lblOutput.update()
			self.update()
			self.resizable(height=True,width=False)
			global h
			
			if self.winfo_height() <= (lblOutput.winfo_height() + Baction.winfo_height() + Bquit.winfo_height()+Instruct.winfo_height()+Entry.winfo_height())+100:
				h = (lblOutput.winfo_height() + Baction.winfo_height() + Bquit.winfo_height()+Instruct.winfo_height()+Entry.winfo_height())+100
			elif self.winfo_height() > (lblOutput.winfo_height() + Baction.winfo_height() + Bquit.winfo_height()+Instruct.winfo_height()+Entry.winfo_height() + 100):
				h = (lblOutput.winfo_height() + Baction.winfo_height() + Bquit.winfo_height()+Instruct.winfo_height()+Entry.winfo_height())
			else:
				pass
			self.geometry("{}x{}".format(w,h))

		Baction.config(command=writeout)
		

		self.mainloop()

