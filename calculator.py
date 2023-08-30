from tkinter import *

exp = ''

def press(number):
    global exp
    exp += str(number)
    equation.set(exp)

def equalpress():
    try:
        global exp
        total = str(eval(exp))
        equation.set(total)
        exp = ""
    except:
        equation.set("Syntax error")
        exp = ""

def calculate_square():
    global exp
    try:
        num = eval(exp)
        square = num ** 2
        equation.set(square)
        exp = ""
    except:
        equation.set("Error")
        exp = ""

def decimal_to_binary():
    global exp
    try:
        num = eval(exp)
        binary = bin(num)[2:]
        equation.set(binary)
        exp = ""
    except:
        equation.set("Error")
        exp = ""

def binary_to_hex():
    global exp
    try:
        num = int(exp, 2)
        hexadecimal = hex(num)[2:].upper()
        equation.set(hexadecimal)
        exp = ""
    except:
        equation.set("Error")
        exp = ""

def clear():
    global exp
    exp = ''
    equation.set('')

tk = Tk()
tk.configure(background="grey")
tk.title('Calculator by codewithcurious.com')
tk.geometry('280x340')

equation = StringVar()
Text_Entry_Box = Entry(tk, textvariable=equation, width=20)
Text_Entry_Box.grid(columnspan=8, ipadx=100)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '=', '+', 'Clear',
    'Square', 'Binary', 'Hex'
]

row_val = 2
col_val = 0

for button_label in buttons:
    if button_label == '=':
        button = Button(tk, text=button_label, fg='black', bg='#ADFF2F', command=equalpress, height=2, width=7)
    elif button_label == 'Clear':
        button = Button(tk, text=button_label, fg='black', bg='#ADFF2F', command=clear, height=2, width=7)
    elif button_label == 'Square':
        button = Button(tk, text=button_label, fg='black', bg='#ADFF2F', command=calculate_square, height=2, width=7)
    elif button_label == 'Binary':
        button = Button(tk, text=button_label, fg='black', bg='#ADFF2F', command=decimal_to_binary, height=2, width=7)
    elif button_label == 'Hex':
        button = Button(tk, text=button_label, fg='black', bg='#ADFF2F', command=binary_to_hex, height=2, width=7)
    else:
        button = Button(tk, text=button_label, fg='black', bg='#ADFF2F', command=lambda num=button_label: press(num), height=2, width=7)

    button.grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

tk.mainloop()
