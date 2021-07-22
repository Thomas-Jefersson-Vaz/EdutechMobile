while True:
  print("Calculadora simples")
  line = ("*"*44)
  print(line)
  print("Autor: TJVG4M34R13")
  print(line)
  a = input("primeiro número: ")         
  b = input("segundo número: ")
  print("Escolha o sinal:")
  c = input(" [+] \n [-] \n [×] \n [÷] \n")             
  print("\n") 
  if a.isnumeric() == True & b.isnumeric() == True:       
    if c == "+":
      d = a+b
      print("Resultado:",a,"+",b,"=",d,"\n","\n")       
    elif c == "-":
      d = a-b
      print("Resultado:",a,"-",b,"=",d,"\n","\n") 
    elif c == "×":
      d = a*b
      print("Resultado:",a,"×",b,"=",d,"\n","\n") 
    elif c == "÷":
      d = a/b
      print("Resultado:",a,"÷",b,"=",d,"\n","\n")
    else:
      print("Man tu é retardado ?\n")
    
  else:
     print("Tu é né?\n")    
  

   
  

  
  
  
  
  
  
  
  
  
   
  
  