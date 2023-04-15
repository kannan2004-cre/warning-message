import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.withdraw()  # hide the root window

# show the warning dialog box with the warning symbol
messagebox.showwarning("Warning", "This is a warning message!")

# exit the program
root.destroy()
