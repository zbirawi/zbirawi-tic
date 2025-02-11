import tkinter as tk
from tkinter import messagebox


root = tk.Tk()
root.title("TIC-ZBIRZWI")
root.configure(bg="#2c3e50")  


digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]  
mark = ''  
count = 0  
panels = ['panel', '', '', '', '', '', '', '', '', ''] 


font_style = ("Helvetica", 14, "bold")
button_style = {"width": 10, "height": 3, "font": ("Helvetica", 20, "bold"), "bg": "#ecf0f1", "fg": "#34495e", "activebackground": "#3498db", "activeforeground": "#ecf0f1"}


player1_label = tk.Label(root, text="Player 1 (X)", font=("Helvetica", 18), fg="#1abc9c", bg="#2c3e50")
player1_label.grid(row=0, column=0, columnspan=3, pady=20)

player2_label = tk.Label(root, text="Player 2 (O)", font=("Helvetica", 18), fg="#e74c3c", bg="#2c3e50")
player2_label.grid(row=1, column=0, columnspan=3, pady=10)


buttons = [tk.Button(root, text=str(i), **button_style, command=lambda i=i: checker(i)) for i in range(1, 10)]


row, col = 2, 0
for i, button in enumerate(buttons):
    button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    col += 1
    if col == 3:
        col = 0
        row += 1


root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)


def checker(digit):
    global count, mark, digits, panels
    
    if digit in digits:
        digits.remove(digit)
        
        
        if count % 2 == 0:
            mark = 'X'
        else:
            mark = 'O'
        
        
        panels[digit] = mark
        
        
        buttons[digit - 1].config(text=mark, state="disabled", fg="#ecf0f1")
        
        
        count += 1
        
        
        if win(mark):
            messagebox.showinfo("Tic-Tac-Toe", f"Player {mark} wins!", icon="info")
            root.destroy()   
            return
        
        
        if count > 8:
            messagebox.showinfo("Tic-Tac-Toe", "Match Tied", icon="info")
            root.destroy() 


def win(mark):
    
    win_combinations = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],  
        [1, 4, 7], [2, 5, 8], [3, 6, 9],  
        [1, 5, 9], [3, 5, 7]  
    ]
    for combination in win_combinations:
        if all(panels[pos] == mark for pos in combination):
            return True
    return False


root.mainloop()
