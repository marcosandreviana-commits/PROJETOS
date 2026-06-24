rota = int(input("1 p/ ponte, 2 p/ tunel, escolha:"))
                         
if rota == 1:
    carro = input("tem carro blindado?")
    ponte = input("a ponte está ok?")
    if carro =="sim" and ponte =="sim":
        print("vá pela ponte")
    else:
        print("você continua encurralado")
elif rota == 2:
    mascara = input("tem máscara?")
    cartao = input("tem cartão?")
    if mascara =="sim" and cartao == "sim": 
        print("vá pelo túnel")
    else:
       print("você continua encurralado")    
else:
    print("opção invalida")       
