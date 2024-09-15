print("\n")

print("\n")

import tkinter as tk

window = tk.Tk()
window.title("Calculator")
window.geometry("400x350")  # Set the window size

display = tk.Entry(window, width=35, borderwidth=5, justify="right")
display.grid(row=0, columnspan=4, padx=10, pady=10)

def button_click(char):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, str(current) + str(char))

def clear_all():
    display.delete(0, tk.END)

def calculate():
    expression = display.get()
    try:
        result = eval(expression)
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except ZeroDivisionError:
        display.delete(0, tk.END)
        display.insert(0, "Error: Division by zero")
    except Exception:
        display.delete(0, tk.END)
        display.insert(0, "Error: Invalid expression")

button_list = [
    "7", "8", "9", "/", "4", "5", "6", "*", "1", "2", "3", "-", "0", ".", "C", "="
]

row = 1
col = 0

for button_text in button_list:
    button = tk.Button(window, text=button_text, width=5, command=lambda char=button_text: button_click(char))
    button.grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

clear_button = tk.Button(window, text="Clear", width=11, command=clear_all)
clear_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

equals_button = tk.Button(window, text="=", width=11, command=calculate)
equals_button.grid(row=5, column=2, columnspan=2, padx=5, pady=5)

window.mainloop()