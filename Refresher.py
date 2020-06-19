#Python Data types
import tkinter as tk
from tkinter import ttk as ttk

#create a popup to input integers
intEntry = tk.Tk()
intEntry.geometry("400x400")
intLabel = ttk.Label(intEntry,text = "Enter an integer", font = ("Time Roman",12))
intLabel.pack(side = "left")
intEnt = ttk.Entry(intEntry, cursor = "dot")
intEnt.pack(side = "right")
B1 = ttk.Button(intEntry,text="Quit",command=quit)
B1.pack(side="bottom")

outputLabel = ttk.Label(intEntry,text = "Your entry x 2 =" & domath(intEntry.get()))

intEntry.mainloop()

#do some INT math
def domath(x)
	return x * 2