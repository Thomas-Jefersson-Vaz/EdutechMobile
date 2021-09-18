import datetime
print("Calculadora de idade")
line = ("*"*44)
print(line)
autor = ("autor: TJVG4M34R13")
print(autor)
w = 0
while (w == 0):
  line = ("*"*44)
  date = datetime.date.today()
  year = int(date.strftime("%Y"))
  ano = int(input("Em que ano você nasceu\n"))
  n = input("Você já fez aniversário este ano ?\nS\nN\n")
  if  n == "N" or n == "n" or n == "nao" or n == "não":
    ano +=1
   # if n == "S" or n == "s":
   #   ano +=0
  print("Você tem",year-ano,"anos de idade")
  print(line,"\n")
  p = input("Quer continuar? \n")
  if p == "s" or p == "S"or p == "sim":
    w == 0
    print("Obrigado por usar meu programa, volte sempre")
  else:
    w +=1
    print("Obrigado por usar meu programa")
