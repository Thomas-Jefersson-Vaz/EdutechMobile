import datetime
date = datetime.date.today()
year = int(date.strftime("%Y"))
ano = int(input("Em que ano você nasceu\n"))
print("Você já fez aniversário este ano ?")
n = int(input("S = 1\n"
          "N = 2\n"))
if  n == 1:
  anoa =  ano+0
elif n == 2:
  anoa =  ano+1
print("Você tem",year-anoa,"anos de idade")

