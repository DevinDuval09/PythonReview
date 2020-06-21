#generic dialogue box that will take input
import tkinter as tk
from tkinter import ttk as tkk

#make a popup box with an input button, output label, and quit button
#input: button function, instructions

class Popup():
	def __init__(self,instructions,press):
		x = 0
		self = tk.Tk()
		self.geometry("200x200")
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
		lblOutput = tkk.Button(self,text="")
		lblOutput.pack()
		#function to write output label
		def writeout():
			if len(Entry.get()) > 0:
				x = press(Entry.get())
				lblOutput.config(text=str(x))
			else:
				lblOutput.config(text="")

		#action button
		Baction=tkk.Button(self,text="Do instructions",command=writeout)
		Baction.pack()

		self.mainloop()

