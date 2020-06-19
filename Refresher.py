#Python Data types
import tkinter as tk
from tkinter import ttk as ttk

def setOutput(x):
	if len(intEnt.get()) > 0 :
		return ttk.Label(intEntry,text="Your entry x 2 =" + str(int(intEnt.get())*2),font=("Time Roman",12))
	else:
		return ttk.Label(intEntry,text="Your entry x 2 =0",font=("Time Roman",12))

#create a popup to input integers
x=0

intEntry = tk.Tk()
intEntry.geometry("400x400")
intLabel = ttk.Label(intEntry,text = "Enter an integer", font = ("Time Roman",12))
intLabel.pack(side = "left")
intEnt = ttk.Entry(intEntry, cursor = "dot", textvariable = "StringVar")
intEnt.pack(side = "right")
B1 = ttk.Button(intEntry,text="Quit",command=quit)
B1.pack(side="bottom")

outputLabel = ttk.Label()


B2 = ttk.Button(intEntry,text="Calculate",command=setOutput(outputLabel))
B2.pack()

outputLabel.pack()

intEntry.mainloop()

