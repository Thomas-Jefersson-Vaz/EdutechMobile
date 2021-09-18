from tkinter import *

def calc():
  n = e1.get()
  if n.isnumeric():
    n = int(n)
    if txta == 11:
      txt.set(
      f"{1} x {n} = {1*n} \n"
      f"{2} x {n} = {2*n} \n"
      f"{3} x {n} = {3*n} \n"
      f"{4} x {n} = {4*n} \n"
      f"{5} x {n} = {5*n} \n"
      f"{6} x {n} = {6*n} \n"
      f"{7} x {n} = {7*n} \n" 
      f"{8} x {n} = {8*n} \n" 
      f"{9} x {n} = {9*n} \n" 
      f"{10} x {n} = {10*n}")
    if txta == 101:
      f"{1} x {n} = {1*n} \n"
      f"{2} x {n} = {2*n} \n"
      f"{3} x {n} = {3*n} \n"
      f"{4} x {n} = {4*n} \n"
      f"{5} x {n} = {5*n} \n"
      f"{6} x {n} = {6*n} \n"
      f"{7} x {n} = {7*n} \n" 
      f"{8} x {n} = {8*n} \n" 
      f"{9} x {n} = {9*n} \n" 
      f"{10} x {n} = {10*n} \n "
  else:
    txt.set("Por Favor coloque um número") 


def n2():
  txta.set(11)
def n3():
  txta.set(101)
def n4():
  txta.set(1001)

       




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

txt = StringVar()
txt.set("")

txta = IntVar()
txta.set()



l2 = Label(
  window,
  textvariable=txt
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
l2.grid(row=3, column=1)
l3.grid(row=1, column=0)
b2.grid(row=2, column=0)
b3.grid(row=2, column=1)
b4.grid(row=2, column=2)

window.mainloop()