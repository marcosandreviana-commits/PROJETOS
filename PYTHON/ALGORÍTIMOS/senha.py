cont = 0
senha = input("digite sua senha:")

while True:
    if senha == "1234":
       print("seja bem vindo")
       break
    else:
       cont = cont + 1
       if cont < 3:
          print("acesso negado")
          print(f"voce tem mais {3 -cont} tentativas")
          senha = input("tente novamente:")
       else:
          print("bloqueado")
          break
