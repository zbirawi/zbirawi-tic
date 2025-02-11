import tkinter as tk
from tkinter import messagebox


root = tk.Tk()
root.title("TIC-ZBIRAWI")


digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
mark = ''  
count = 0  


panels = ['panel']  
for _ in range(9):
    panels.append('')  


root.resizable(False, False)  


mainframe = tk.Frame(
    root,
    bg='white',
    width=500,
    height=500
)
mainframe.pack()


root.mainloop()