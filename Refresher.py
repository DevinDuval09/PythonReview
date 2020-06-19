#Python Data types
import tkinter as tk
from tkinter import ttk as ttk

#create a popup to input integers
intEntry = tk.tk()
intLabel = ttk.Label(intEntry,text = "Enter an integer", font = ("Time Roman",12))
intLabel.pack(side = left)
intEnt = entry(intEntry, cursor = "dot")
intEnt.pack(side = "right")
