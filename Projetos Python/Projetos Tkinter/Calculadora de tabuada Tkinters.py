from tkinter import *

def calc():
  n = e1.get()
  if n.isnumeric():
    n = int(n)
    t1.delete(1.0, END)
    if txta == 11:
      for i in range(0,txta):
        t = int(txta)
        a = f"{i} x {n} = {i*n} \n"
        t1.insert(END, a)
    if txta == 101:
      for i in range(0,txta):
        t = int(txta)
        a = f"{i} x {n} = {i*n} \n"
        t1.insert(END, a)
    if txta == 1001:
      for i in range(0,txta):
        t = int(txta)
        a = f"{i} x {n} = {i*n} \n"
        t1.insert(END, a)
  else:
    t1.delete(1.0, END)
    a = "Por Favor coloque um número"
    t1.insert(END, a) 

def n2():
  global txta
  txta = 11
def n3():
  global txta
  txta = 101
def n4():
  global txta
  txta = 1001
def lim():
  t1.delete(1.0, END)
  e1.delete(0, END)




window = Tk()
window.title("Calculadora de tabuada")

l1 = Label(
  window,
  text="Coloque seu número"
)

e1 = Entry(window)

b1 = Button(
  window,
  text="calcular",
  command=calc
)

t1 = Text(window, width=15)

txta = IntVar()
txta.set("")

b5 = Button(
  window,
  text="Limpar tudo",
  command=lim
)

l3 = Label(
  window,
  text="Escolha até onde vai sua tabuada"
)

b2 = Button(
  window,
  text="1-10",
  command=n2
)

b3 = Button(
  window,
  text="1-100",
  command=n3
)
b4 = Button(
  window,
  text="1-1000",
  command=n4
)
#grids
l1.grid(row=0, column=0)
e1.grid(row=0, column=1)
b1.grid(row=0, column=2)
t1.grid(row=3, column=1)
l3.grid(row=1, column=0)
b2.grid(row=2, column=0)
b3.grid(row=2, column=1)
b4.grid(row=2, column=2)
b5.grid(row=3, column=0)


window.mainloop()