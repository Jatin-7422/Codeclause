# All Rights are Reserved by Jatin Kumar

import tkinter as tk

calculator = ""


# function to add symbols and numbers into the text area
def add(symbol):
    global calculator
    calculator += str(symbol)
    t_result.delete(1.0, "end")
    t_result.insert(1.0, calculator)

# function to perform calculation
def evaluate():
    global calculator
    try:
        calculation = str(eval(calculator))
        calculator = calculation + ""
        t_result.delete(1.0, "end")
        t_result.insert(1.0, calculation)
    except:
        clear()
        t_result.insert(1.0, "Error")
        pass

# function to clear the text area
def clear():
    global calculator
    calculator = ""
    t_result.delete(1.0, "end")


# Make Background of our Calculator
root = tk.Tk()
root.title("Calculator by Jatin")
root.geometry("300x300")
t_result = tk.Text(root, height=2, width=15, font=("lucida", 25))
t_result.grid(columnspan=5)


# Making Buttons
btn1 = tk.Button(root, text="1", command=lambda: add(1), width=5, font=("Arial", 14))
btn1.grid(row=2, column=1)

btn2 = tk.Button(root, text="2", command=lambda: add(2), width=5, font=("Arial", 14))
btn2.grid(row=2, column=2)

btn3 = tk.Button(root, text="3", command=lambda: add(3), width=5, font=("Arial", 14))
btn3.grid(row=2, column=3)

btn4 = tk.Button(root, text="4", command=lambda: add(4), width=5, font=("Arial", 14))
btn4.grid(row=3, column=1)

btn5 = tk.Button(root, text="5", command=lambda: add(5), width=5, font=("Arial", 14))
btn5.grid(row=3, column=2)

btn6 = tk.Button(root, text="6", command=lambda: add(6), width=5, font=("Arial", 14))
btn6.grid(row=3, column=3)

btn7 = tk.Button(root, text="7", command=lambda: add(7), width=5, font=("Arial", 14))
btn7.grid(row=4, column=1)

btn8 = tk.Button(root, text="8", command=lambda: add(8), width=5, font=("Arial", 14))
btn8.grid(row=4, column=2)

btn9 = tk.Button(root, text="9", command=lambda: add(9), width=5, font=("Arial", 14))
btn9.grid(row=4, column=3)

btn0 = tk.Button(root, text="0", command=lambda: add(0), width=5, font=("Arial", 14))
btn0.grid(row=5, column=2)

plus = tk.Button(root, text="+", command=lambda: add("+"), width=5, font=("Arial", 14))
plus.grid(row=2, column=4)

minus = tk.Button(root, text="-", command=lambda: add("-"), width=5, font=("Arial", 14))
minus.grid(row=3, column=4)

multiply = tk.Button(root, text="*", command=lambda: add("*"), width=5, font=("Arial", 14))
multiply.grid(row=4, column=4)

divide = tk.Button(root, text="/", command=lambda: add("/"), width=5, font=("Arial", 14))
divide.grid(row=5, column=4)

open_paranthesis = tk.Button(root, text="(", command=lambda: add("("), width=5, font=("Arial", 14))
open_paranthesis.grid(row=5, column=1)

close_paranthesis = tk.Button(root, text=")", command=lambda: add(")"), width=5, font=("Arial", 14))
close_paranthesis.grid(row=5, column=3)

Clear = tk.Button(root, text="AC", command=clear, width=11, font=("Arial", 14))
Clear.grid(row=6, column=1, columnspan=2)

Equal = tk.Button(root, text="=", command=evaluate, width=11, font=("Arial", 14))
Equal.grid(row=6, column=3, columnspan=2)

root.mainloop()