#Python Data types
import tkinter as tk
from tkinter import ttk as ttk




#create a popup to input integers

intEntry = tk.Tk()
intEntry.geometry("400x400")
intLabel = ttk.Label(intEntry,text = "Enter an integer", font = ("Time Roman",12))
intLabel.pack(side = "left")
intEnt = ttk.Entry(intEntry, cursor = "dot", textvariable = "StringVar")
intEnt.pack(side = "right")
B1 = ttk.Button(intEntry,text="Quit",command=quit)
B1.pack(side="bottom")

def press():
	if len(intEnt.get())>0:
		x = int(intEnt.get())
	else:
		x=0

	y = x*2
	print(x)
	print(y)
	outputLabel = ttk.Label(intEntry,text=str(y))
	outputLabel.pack()
	intEntry.update()
	outputLabel.update()

B2 = ttk.Button(intEntry,text="Calculate",command=press)
B2.pack()



intEntry.mainloop()

