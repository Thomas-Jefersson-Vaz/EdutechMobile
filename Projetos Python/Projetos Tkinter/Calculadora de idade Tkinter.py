from tkinter import *
import datetime

def calcular():
  r1 = e1.get()
  r2 = e2.get()
  date = datetime.date.today()
  year = int(date.strftime("%Y"))
  if r1.isnumeric():
    if  r2 == "N" or r2 == "n" or r2 == "nao" or r2 == "não":
      r1 = int(r1)
      r1 = year-r1
      r1 = r1 - 1
      txt.set(r1)
    if r2 == "":
      r1 = "Por Favor responda a pergunta"
      txt.set(r1)
    else:
      txt.set(r1)
  else:
    txt.set("Por favor use somente números\n no ano de nascimento")
def lim():
  e1.delete(0, END)
  e2.delete(0, END)
  txt.set("")
  

window = Tk()
window.title("Calculadora de idade")

#definir onde o app vai aparecer
# largura = window.winfo_screenwidth()
# altura = window.winfo_screenheight()
# posx = largura/2 - largura/2
# posy = altura/2 - altura/2
# window.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))





l1 = Label(
  window,
  text="Em que ano você faz aniversário")
l1.grid(row=0, column=0)

e1 = Entry(window)
e1.grid(row=0, column=1)

l2 = Label(
  window,
  text="Já fex aniversário esse ano?\n S = Sim \n N = Não"
)
l2.grid(row=1, column=0)

e2 = Entry(window)
e2.grid(row=1, column=1)

txt = StringVar()
txt.set("")

l3 = Label(
  window,
  textvariable=txt
)
l3.grid(row=3, column=0)

b1 = Button(
  window,
  text="Calcular idade",
  command=calcular
)
b1.grid(row=4, column=1)

b2 = Button(
  window,
  text="Limpar Tudo",
  command=lim
)
b2.grid(row=4, column=0)
window.mainloop