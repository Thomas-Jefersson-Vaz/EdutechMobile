from tkinter import * 

def add():
  r1=int(n1.get())
  r2=int(n2.get())
  r=r1, "+", r2, "=", r1+r2
  txtb.delete(1.0, END)
  txtb.insert(END, r)
def sub():
  r1=int(n1.get())
  r2=int(n2.get())
  r=r1, "-", r2, "=", r1-r2
  txtb.delete(1.0, END)
  txtb.insert(END, r)
def mul():
  r1=int(n1.get())
  r2=int(n2.get())
  r=r1, "x", r2, "=", r1*r2
  txtb.delete(1.0, END)
  txtb.insert(END, r)
def div():
  r1=int(n1.get())
  r2=int(n2.get())
  r=r1, "÷", r2, "=", r1/r2
  txtb.delete(1.0, END)
  txtb.insert(END, r)
def lim():
  n1.delete(0, END)
  n2.delete(0, END)
  txtb.delete(1.0, END)

window = Tk()
window.title("Calculadora Simples")
window.geometry("280x180")

Label1 = Label(
  window,
  text="Primeiro Número")
Label1.grid(row=0, column=0)

n1 = Entry(window)
n1.grid(row=0, column=1)

Label2 = Label(
  window,
  text="Segundo Número")
Label2.grid(row=1, column=0)

n2 = Entry(window)
n2.grid(row=1, column=1)

Label3 = Label(window, text="Resultado:")
Label3.grid(row=2, column=0)

txtb = Text(window, width=15, height=1)
txtb.grid(row=2, column=1)

b1 = Button(window, text="adição", width=18, command=add)
b1.grid(row=3, column=0)

b2 = Button(window, text="Subtração", width=18, command=sub)
b2.grid(row=3, column=1)

b3 = Button(window, text="Multiplicação", width=18, command=mul)
b3.grid(row=4, column=0)

b4 = Button(window, text="Divisão", width=18, command=div)
b4.grid(row=4, column=1)

b5 = Button(window, text="limpar", width=18, command=lim)
b5.grid(row=5, column=0)

window.mainloop()