from tkinter import *

def calc():
  n = e1.get()
  if n.isnumeric():
    n = int(n)
    for i in range(0,11):
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
  else:
    txt.set("Por Favor coloque um número") 
    
       
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

l2 = Label(
  window,
  textvariable=txt
)
#grids
l1.grid(row=0, column=0)
e1.grid(row=0, column=1)
b1.grid(row=0, column=2)
l2.grid(row=1, column=1)


window.mainloop()