import tkinter as tk
from math import *

mainScreen = tk.Tk()
mainScreen.title("Calculator")

canvas = tk.Canvas(mainScreen, width = 390, height = 520,bg="RoyalBlue4")
canvas.pack()

result = tk.StringVar()
global num
num = ""

def calc(n):
  global num
  num += str(n)
  result.set(num)

def evaluate():
  global num
  try:
    total = str(eval(num))
    num += "= " +total
    result.set(num)
    num=""
  except:
    result.set("Error!")
    num=""

def allClear():
  global num
  numberEntry.delete(0, tk.END)
  num = ""

def delete():
  global num
  numberEntry.delete(len(num)-1,tk.END)
  num = num[0:len(num)-1]

def fact():
  global num
  try:
    num = int(num)
    fact = 1
    while num>0:
      fact *= num
      num = num-1
    result.set(fact)
    num=""
  except:
    result.set("Error!")
    num=""


numberEntry = tk.Entry (mainScreen,fg="black", bg="#e6fff9",font=("Helvetica",15),textvariable = result)
numberEntry.place(x = 1, y = 10, width=388, height=120)

num1button = tk.Button(text='1', fg="black", bg="lightBlue",font=("Helvetica",15),width=3,command= lambda:calc(1))
num2button = tk.Button(text='2', fg="black", bg="lightBlue",font=("Helvetica",15),width=3,command= lambda:calc(2))
num3button = tk.Button(text='3', fg="black", bg="lightBlue",font=("Helvetica",15),width=3,command= lambda:calc(3))
num4button = tk.Button(text='4', fg="black", bg="lightBlue",font=("Helvetica",15),width=3,command= lambda:calc(4))
num5button = tk.Button(text='5', fg="black", bg="lightBlue",font=("Helvetica",15),width=3,command= lambda:calc(5))
num6button = tk.Button(text='6', fg="black", bg="lightBlue",font=("Helvetica",15),width=3,command= lambda:calc(6))
num7button = tk.Button(text='7', fg="black", bg="lightBlue",font=("Helvetica",15),width=3,command= lambda:calc(7))
num8button = tk.Button(text='8', fg="black", bg="lightBlue",font=("Helvetica",15),width=3,command= lambda:calc(8))
num9button = tk.Button(text='9', fg="black", bg="lightBlue",font=("Helvetica",15),width=3,command= lambda:calc(9))
num0button = tk.Button(text='0', fg="black", bg="lightBlue",font=("Helvetica",15),width=3,command= lambda:calc(0))
clearbutton = tk.Button(text='AC', fg="black", bg="lightBlue",font=("Helvetica",15),width=3,command=allClear)
delbutton = tk.Button(text='⌫', fg="black", bg="lightBlue",font=("Helvetica",15),width=3,command=delete)
ebutton = tk.Button(text='e', fg="darkBlue", bg="White",font=("Helvetica",15),width=3,command= lambda:calc("e"))
dotbutton = tk.Button(text='.', fg="darkBlue", bg="White",font=("Helvetica",15),width=3,command= lambda:calc("."))
addbutton = tk.Button(text='+',fg="darkBlue", bg="White",font=("Helvetica",15),width=3,command= lambda:calc("+"))
subbutton = tk.Button(text='-',fg="darkBlue", bg="White",font=("Helvetica",15),width=3,command= lambda:calc("-"))
mulbutton = tk.Button(text='X',fg="darkBlue", bg="White",font=("Helvetica",15),width=3,command= lambda:calc("*"))
divbutton = tk.Button(text='÷',fg="darkBlue", bg="White",font=("Helvetica",15),width=3,command= lambda:calc("/"))
rootbutton = tk.Button(text='√x',fg="darkBlue", bg="White",font=("Helvetica",15),width=3,command= lambda:calc("**0.5"))
modbutton = tk.Button(text='%',fg="darkBlue", bg="White",font=("Helvetica",15),width=3,command= lambda:calc("/100"))
squarebutton = tk.Button(text='x^2',fg="darkBlue", bg="White",font=("Helvetica",15),width=3,command= lambda:calc("**2"))
equalbutton = tk.Button(text='=',fg="darkBlue", bg="White",font=("Helvetica",15),width=3,command= evaluate)

powerbutton = tk.Button(text='x^y',fg="darkBlue", bg="White",font=("Helvetica",15),width=3,command= lambda:calc("**"))
logbutton = tk.Button(text='lg',fg="darkBlue", bg="White",font=("Helvetica",15),width=3,command= lambda:calc("log10"))
nlogbutton = tk.Button(text='ln',fg="darkBlue", bg="White",font=("Helvetica",15),width=3,command= lambda:calc("log"))
b1button = tk.Button(text='(',fg="darkBlue", bg="White",font=("Helvetica",15),width=3,command= lambda:calc("("))
b2button = tk.Button(text=')',fg="darkBlue", bg="White",font=("Helvetica",15),width=3,command= lambda:calc(")"))
factbutton = tk.Button(text='x!',fg="darkBlue", bg="White",font=("Helvetica",15),width=3,command=fact)
invbutton = tk.Button(text='1/x',fg="darkBlue", bg="White",font=("Helvetica",15),width=3,command = lambda:calc("1/"))
pibutton = tk.Button(text='π',fg="darkBlue", bg="White",font=("Helvetica",15),width=3,command= lambda:calc("pi"))

canvas.create_window(45, 200, window=powerbutton)
canvas.create_window(120, 200, window=logbutton)
canvas.create_window(195, 200, window=nlogbutton)
canvas.create_window(270, 200, window=b1button)
canvas.create_window(345, 200, window=b2button)

canvas.create_window(45, 250, window=squarebutton)
canvas.create_window(120, 250, window=clearbutton)
canvas.create_window(195, 250, window=delbutton)
canvas.create_window(270, 250, window=modbutton)
canvas.create_window(345, 250, window=divbutton)

canvas.create_window(45, 300, window=rootbutton)
canvas.create_window(120, 300, window=num7button)
canvas.create_window(195, 300, window=num8button)
canvas.create_window(270, 300, window=num9button)
canvas.create_window(345, 300, window=mulbutton)

canvas.create_window(45, 350, window=factbutton)
canvas.create_window(120, 350, window=num4button)
canvas.create_window(195, 350, window=num5button)
canvas.create_window(270, 350, window=num6button)
canvas.create_window(345, 350, window=subbutton)

canvas.create_window(45, 400, window=invbutton)
canvas.create_window(120, 400, window=num1button)
canvas.create_window(195, 400, window=num2button)
canvas.create_window(270, 400, window=num3button)
canvas.create_window(345, 400, window=addbutton)

canvas.create_window(45, 450, window=pibutton)
canvas.create_window(120, 450, window=ebutton)
canvas.create_window(195, 450, window=num0button)
canvas.create_window(270, 450, window=dotbutton)
canvas.create_window(345, 450, window=equalbutton)

mainScreen.mainloop()