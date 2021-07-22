while True:
  print("Calculadora simples")
  line = ("*"*44)
  print(line)
  print("Autor: TJVG4M34R13")
  print(line)
  a = int(input("primeiro número: "))            
  b = int(input("segundo número: ")) 
  print("Escolha o sinal:")
  c = int(input("[1] + \n"
                "[2] - \n"
                "[3] × \n"
                "[4] ÷ \n\n"))
  print("\n")              
  if c == 1:
    d = a+b
    print("Resultado:",a,"+",b,"=",d,"\n","\n")       
  elif c == 2:
    d = a-b
    print("Resultado:",a,"-",b,"=",d,"\n","\n") 
  elif c == 3:
    d = a*b
    print("Resultado:",a,"×",b,"=",d,"\n","\n") 
  elif c == 4:
    d = a/b
    print("Resultado:",a,"÷",b,"=",d,"\n","\n")
  elif c != 1:
    print("escolha um sinal válido\n")
  elif c != 2:
    print("")
  elif c != 3:
    print("")
  elif c != 1:
    print("")
    
  

  
  
  
  
  
  
  
  
  
   
  
  
