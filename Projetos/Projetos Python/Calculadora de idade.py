import datetime
print("Calculadora de idade")
line = ("*"*44)
print(line)
autor = ("autor: TJVG4M34R13")
print(autor)
while True:
  line = ("*"*44)
  date = datetime.date.today()
  year = int(date.strftime("%Y"))
  while True:
    ano = int(input("Em que ano você nasceu\n"))
    n = input("Você já fez aniversário este ano ?\nS\nN\n")
    if  n == "N" or n == "n":
      ano +=1
   # if n == "S" or n == "s":
   #   ano +=0
    print("Você tem",year-ano,"anos de idade")
    print(line,"\n")