from tkinter import *
from tkinter.ttk import *

def cc():
  add.grid(row=1, column=0)
def add():
  print("a")


def imc():
  l1.grid(row=1, column=0)
  altura.grid(row=2, column=1)
  peso.grid(row=3, column=1)
  l2.grid(row=2, column=0)
  l3.grid(row=3, column=0)



window = Tk()

reset = Button(window, text="reset", command=lambda: window.add)


      #Calculadora Simples
cc = Button(window, text="calc comum", command=cc)
cc.grid(row=0, column=0)

add = Button(window, text="somar", command=add)

#Calculadora Imc
imc = Button(window, text="imc", command=imc)
imc.grid(row=0, column=1)

l1 = Label(window, text="Coloque seus dados para calcular seu imc")
l2 = Label(window, text="altura")
l3 = Label(window, text="Peso")
altura = Entry(window)
peso = Entry(window)




window.mainloop